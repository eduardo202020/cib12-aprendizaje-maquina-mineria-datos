from __future__ import annotations

import argparse
import csv
import json
import math
import pickle
import sys
from pathlib import Path

from common import ONLINE_DIR, POS_LIMITS, ensure_runtime_dirs, metrics_output_path, model_output_dir


def fail(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(1)


def descale_targets(values):
    import numpy as np

    array = np.asarray(values, dtype="float32").copy()
    array[:, 0] = array[:, 0] * (POS_LIMITS["max_x"] - POS_LIMITS["min_x"]) + POS_LIMITS["min_x"]
    array[:, 1] = array[:, 1] * (POS_LIMITS["max_y"] - POS_LIMITS["min_y"]) + POS_LIMITS["min_y"]
    return array


def scale_inputs(rows, sensor_columns, scaler_params):
    import numpy as np

    matrix = np.asarray([[float(row[col]) for col in sensor_columns] for row in rows], dtype="float32")
    mean = np.asarray(scaler_params["mean"], dtype="float32")
    std = np.asarray(scaler_params["std"], dtype="float32")
    std[std == 0] = 1.0
    return (matrix - mean) / std


def scale_targets(rows):
    import numpy as np

    targets = np.asarray([[float(row["pos_x"]), float(row["pos_y"])] for row in rows], dtype="float32")
    targets[:, 0] = (targets[:, 0] - POS_LIMITS["min_x"]) / (POS_LIMITS["max_x"] - POS_LIMITS["min_x"])
    targets[:, 1] = (targets[:, 1] - POS_LIMITS["min_y"]) / (POS_LIMITS["max_y"] - POS_LIMITS["min_y"])
    return targets


def compute_distance_stats(distances):
    ordered = sorted(distances)
    if not ordered:
        return {}
    def percentile(p):
        if len(ordered) == 1:
            return ordered[0]
        index = (len(ordered) - 1) * p
        lower = math.floor(index)
        upper = math.ceil(index)
        if lower == upper:
            return ordered[lower]
        weight = index - lower
        return ordered[lower] * (1 - weight) + ordered[upper] * weight

    return {
        "count": len(ordered),
        "min": min(ordered),
        "q1": percentile(0.25),
        "median": percentile(0.5),
        "mean": sum(ordered) / len(ordered),
        "q3": percentile(0.75),
        "max": max(ordered),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate M2 on online processed fingerprints.")
    parser.add_argument("--fingerprint-name", default="lab02_ble_ferrero")
    parser.add_argument("--variant", choices=["with_empty_values", "without_empty_values"], default="with_empty_values")
    parser.add_argument("--tag", default="", help="Optional suffix for output folder name.")
    args = parser.parse_args()

    if sys.version_info[:2] not in {(3, 10), (3, 11)}:
        fail("Evaluation requires Python 3.10 or 3.11 for TensorFlow compatibility.")

    try:
        import numpy as np
        import tensorflow as tf
    except Exception as exc:
        fail(f"Evaluation dependencies are missing: {exc}")

    ensure_runtime_dirs()
    dataset_path = ONLINE_DIR / args.fingerprint_name / f"{args.variant}.csv"
    model_variant_dir = args.variant if not args.tag else f"{args.variant}_{args.tag}"
    model_dir = model_output_dir("M2", args.variant, args.tag)
    model_path = model_dir / "model.keras"
    scaler_path = model_dir / "scaler.pkl"
    output_path = metrics_output_path("M2", args.variant, args.tag)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not dataset_path.exists():
        fail(f"Online dataset not found: {dataset_path}")
    if not model_path.exists():
        fail(f"Model not found: {model_path}")
    if not scaler_path.exists():
        fail(f"Scaler not found: {scaler_path}")

    with dataset_path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    with scaler_path.open("rb") as handle:
        scaler_params = pickle.load(handle)

    sensor_columns = scaler_params["sensor_columns"]
    x_scaled = scale_inputs(rows, sensor_columns, scaler_params)
    y_scaled = scale_targets(rows)
    y_true = descale_targets(y_scaled)

    model = tf.keras.models.load_model(model_path)
    predictions_scaled = model.predict(x_scaled, verbose=0)
    predictions = descale_targets(predictions_scaled)

    distances = [
        math.sqrt((float(pred[0]) - float(real[0])) ** 2 + (float(pred[1]) - float(real[1])) ** 2)
        for pred, real in zip(predictions, y_true)
    ]
    stats = compute_distance_stats(distances)
    output_path.write_text(
        json.dumps(
            {
                "fingerprint_name": args.fingerprint_name,
                "variant": args.variant,
                "output_variant": model_variant_dir,
                "distance_stats": stats,
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
