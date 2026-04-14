from __future__ import annotations

import argparse
import json
import pickle
import sys
from pathlib import Path

from common import FINGERPRINT_DIR, POS_LIMITS, ensure_runtime_dirs, model_output_dir


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def ensure_supported_python() -> None:
    major, minor = sys.version_info[:2]
    if not ((major, minor) in {(3, 10), (3, 11)}):
        fail(
            "M2 training requires Python 3.10 or 3.11 for TensorFlow compatibility. "
            f"Current interpreter: {major}.{minor}"
        )


def load_training_rows(csv_path: Path):
    import csv

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        fail(f"Training CSV is empty: {csv_path}")
    sensor_columns = sorted(
        col for col in rows[0].keys() if col not in {"sample_id", "pos_x", "pos_y", "pos_z", "trajectory"}
    )
    x_values = [[float(row[col]) for col in sensor_columns] for row in rows]
    y_values = [[float(row["pos_x"]), float(row["pos_y"])] for row in rows]
    return sensor_columns, x_values, y_values


def standard_scale_fit_transform(matrix):
    import numpy as np

    x = np.asarray(matrix, dtype="float32")
    mean = x.mean(axis=0)
    std = x.std(axis=0)
    std[std == 0] = 1.0
    return (x - mean) / std, {"mean": mean.tolist(), "std": std.tolist()}


def minmax_scale_targets(targets):
    import numpy as np

    y = np.asarray(targets, dtype="float32")
    scale_x = POS_LIMITS["max_x"] - POS_LIMITS["min_x"]
    scale_y = POS_LIMITS["max_y"] - POS_LIMITS["min_y"]
    y_scaled = y.copy()
    y_scaled[:, 0] = (y[:, 0] - POS_LIMITS["min_x"]) / scale_x
    y_scaled[:, 1] = (y[:, 1] - POS_LIMITS["min_y"]) / scale_y
    return y_scaled


def build_m2_model(input_dim: int, empty_values: bool):
    import tensorflow as tf

    inputs = tf.keras.layers.Input(shape=(input_dim,), name="input_1")
    layer = tf.keras.layers.Dense(1024, activation="linear", name="dense")(inputs)
    layer = tf.keras.layers.ReLU(name="re_lu")(layer)
    layer = tf.keras.layers.Dropout(0.5 if empty_values else 0.25, name="dropout")(layer)
    layer = tf.keras.layers.Dense(128, activation="linear", name="dense_1")(layer)
    layer = tf.keras.layers.ReLU(name="re_lu_1")(layer)
    layer = tf.keras.layers.Dense(16, activation="linear", name="dense_2")(layer)
    layer = tf.keras.layers.ReLU(name="re_lu_2")(layer)
    if empty_values:
        layer = tf.keras.layers.Dropout(0.25, name="dropout_1")(layer)
    outputs = tf.keras.layers.Dense(2, activation="linear", name="regression_head_1")(layer)
    model = tf.keras.Model(inputs=inputs, outputs=outputs, name="M2")
    learning_rate = 0.0001 if empty_values else 0.001
    model.compile(
        loss="mse",
        optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate, jit_compile=False),
        metrics=["mse", "accuracy"],
    )
    return model


def main() -> None:
    parser = argparse.ArgumentParser(description="Train M2 using processed fingerprint CSV files.")
    parser.add_argument("--fingerprint-name", default="lab02_ble_ferrero")
    parser.add_argument("--variant", choices=["with_empty_values", "without_empty_values"], default="with_empty_values")
    parser.add_argument("--epochs", type=int, default=1000)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--tag", default="", help="Optional suffix for output folder name.")
    args = parser.parse_args()

    ensure_supported_python()
    try:
        import numpy as np
        import tensorflow as tf
    except Exception as exc:
        fail(
            "Training dependencies are missing. Create a Python 3.10/3.11 environment and install "
            f"numpy plus tensorflow. Import error: {exc}"
        )

    tf.random.set_seed(args.seed)
    np.random.seed(args.seed)

    ensure_runtime_dirs()
    csv_path = FINGERPRINT_DIR / args.fingerprint_name / f"{args.variant}.csv"
    model_variant_dir = args.variant if not args.tag else f"{args.variant}_{args.tag}"
    model_dir = model_output_dir("M2", args.variant, args.tag)
    model_dir.mkdir(parents=True, exist_ok=True)

    sensor_columns, x_values, y_values = load_training_rows(csv_path)
    x_scaled, scaler_params = standard_scale_fit_transform(x_values)
    y_scaled = minmax_scale_targets(y_values)

    empty_values = args.variant == "with_empty_values"
    model = build_m2_model(input_dim=len(sensor_columns), empty_values=empty_values)
    callback = tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        min_delta=0.0001,
        patience=10,
        restore_best_weights=True,
    )
    history = model.fit(
        x_scaled,
        y_scaled,
        validation_split=0.2,
        epochs=args.epochs,
        batch_size=args.batch_size,
        verbose=2,
        callbacks=[callback],
    )

    model_path = model_dir / "model.keras"
    scaler_path = model_dir / "scaler.pkl"
    metrics_path = model_dir / "training_summary.json"

    model.save(model_path)
    with scaler_path.open("wb") as handle:
        pickle.dump({"sensor_columns": sensor_columns, **scaler_params}, handle)
    metrics_path.write_text(
        json.dumps(
            {
                "fingerprint_name": args.fingerprint_name,
                "variant": args.variant,
                "output_variant": model_variant_dir,
                "seed": args.seed,
                "epochs_ran": len(history.history.get("loss", [])),
                "final_loss": history.history.get("loss", [None])[-1],
                "final_val_loss": history.history.get("val_loss", [None])[-1],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Saved model to {model_path}")


if __name__ == "__main__":
    main()
