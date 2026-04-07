from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATASET_DIR = ROOT_DIR / "datos" / "raw" / "Position-Annotated-BLE-RSSI-Dataset"
PROCESSED_DIR = ROOT_DIR / "datos" / "processed"
FINGERPRINT_DIR = PROCESSED_DIR / "fingerprints"
ONLINE_DIR = PROCESSED_DIR / "online"
RESULTS_DIR = ROOT_DIR / "resultados"
MODELS_DIR = RESULTS_DIR / "models"
METRICS_DIR = RESULTS_DIR / "metrics"
LOGS_DIR = RESULTS_DIR / "logs"

POS_LIMITS = {
    "min_x": 0.0,
    "max_x": 20.66,
    "min_y": 0.0,
    "max_y": 17.64,
}


@dataclass(frozen=True)
class SensorInfo:
    mac: str
    alias: str


def ensure_runtime_dirs() -> None:
    for path in (
        FINGERPRINT_DIR,
        ONLINE_DIR,
        MODELS_DIR,
        METRICS_DIR,
        LOGS_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)


def load_sensors_config(config_path: Path | None = None) -> List[SensorInfo]:
    config_path = config_path or RAW_DATASET_DIR / "cnf" / "tetam.dev"
    lines = config_path.read_text(encoding="utf-8").splitlines()
    dongles_line = next(line for line in lines if line.startswith("Dongles:"))
    dongles = json.loads(dongles_line.split("Dongles:", 1)[1])
    sensors = [SensorInfo(mac=mac, alias=payload[2]) for mac, payload in dongles.items()]
    sensors.sort(key=lambda sensor: sensor.alias)
    return sensors


def parse_float_token(token: str) -> float:
    return float(token)


def parse_hst_filename(file_path: Path) -> Dict[str, float | str]:
    stem_parts = file_path.stem.split("_")
    if len(stem_parts) < 4:
        raise ValueError(f"Unexpected offline filename format: {file_path.name}")
    alias = stem_parts[0]
    x, y, z = map(parse_float_token, stem_parts[1:4])
    return {"alias": alias, "pos_x": x, "pos_y": y, "pos_z": z}


def euclidean_distance(point_a: Sequence[float], point_b: Sequence[float]) -> float:
    return math.sqrt(sum((float(a) - float(b)) ** 2 for a, b in zip(point_a, point_b)))


def write_csv(rows: Iterable[dict], output_path: Path, fieldnames: Sequence[str]) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
            count += 1
    return count


def load_csv_rows(csv_path: Path) -> List[dict]:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

