from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def run(command: list[str]) -> int:
    print("Running:", " ".join(command))
    completed = subprocess.run(command, cwd=SCRIPT_DIR.parent)
    return completed.returncode


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Lab-02 Part-02 pipeline.")
    parser.add_argument("--fingerprint-name", default="lab02_ble_ferrero")
    parser.add_argument("--skip-train", action="store_true")
    parser.add_argument("--skip-eval", action="store_true")
    args = parser.parse_args()

    python = sys.executable

    prepare_cmd = [python, str(SCRIPT_DIR / "prepare_datasets.py"), "--fingerprint-name", args.fingerprint_name]
    if run(prepare_cmd) != 0:
        raise SystemExit(1)

    if not args.skip_train:
        for variant in ("with_empty_values", "without_empty_values"):
            train_cmd = [
                python,
                str(SCRIPT_DIR / "train_m2.py"),
                "--fingerprint-name",
                args.fingerprint_name,
                "--variant",
                variant,
            ]
            if run(train_cmd) != 0:
                raise SystemExit(1)

    if not args.skip_eval:
        for variant in ("with_empty_values", "without_empty_values"):
            eval_cmd = [
                python,
                str(SCRIPT_DIR / "evaluate_m2.py"),
                "--fingerprint-name",
                args.fingerprint_name,
                "--variant",
                variant,
            ]
            if run(eval_cmd) != 0:
                raise SystemExit(1)


if __name__ == "__main__":
    main()
