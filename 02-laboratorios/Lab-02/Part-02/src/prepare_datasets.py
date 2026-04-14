from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, Iterator, List

from common import (
    FINGERPRINT_DIR,
    ONLINE_DIR,
    RAW_DATASET_DIR,
    ensure_runtime_dirs,
    load_sensors_config,
    parse_hst_filename,
    write_csv,
)


INVALID_SENSOR_VALUE = 100
MIN_ENTRIES_PER_SENSOR = 2
MIN_WINDOW_SIZE = 0.5
MAX_WINDOW_SIZE = 2.5
FILTER_METHOD = "max"


class FingerprintWindow:
    def __init__(
        self,
        sensor_aliases: List[str],
        min_window_size: float,
        max_window_size: float,
        min_entries_per_sensor: int,
        min_valid_sensors: int,
        invalid_sensor_value: int = INVALID_SENSOR_VALUE,
    ) -> None:
        self.sensor_aliases = sensor_aliases
        self.min_window_size = min_window_size
        self.max_window_size = max_window_size
        self.min_entries_per_sensor = min_entries_per_sensor
        self.min_valid_sensors = min_valid_sensors
        self.invalid_sensor_value = invalid_sensor_value
        self.stack: List[dict] = []

    def clear(self) -> None:
        self.stack = []

    def _trim(self, timestamp: float) -> None:
        while self.stack and timestamp - self.stack[0]["timestamp"] > self.max_window_size:
            self.stack.pop(0)

    def _valid_sensor_count(self) -> int:
        counts = defaultdict(int)
        for item in self.stack:
            counts[item["sensor_alias"]] += 1
        return sum(1 for alias in self.sensor_aliases if counts.get(alias, 0) >= self.min_entries_per_sensor)

    def _compose_fingerprint(self) -> Dict[str, int]:
        by_sensor = defaultdict(list)
        for item in self.stack:
            by_sensor[item["sensor_alias"]].append(item["rssi"])

        fingerprint = {}
        for alias in self.sensor_aliases:
            values = by_sensor.get(alias, [])
            if len(values) >= self.min_entries_per_sensor:
                if FILTER_METHOD != "max":
                    raise ValueError("Only max filtering is implemented in this pipeline.")
                fingerprint[alias] = max(values)
            else:
                fingerprint[alias] = self.invalid_sensor_value
        return fingerprint

    def process(self, reading: dict) -> dict | None:
        timestamp = float(reading["timestamp"])
        self.stack.append(reading)
        self._trim(timestamp)

        if not self.stack:
            return None
        if timestamp - self.stack[0]["timestamp"] < self.min_window_size:
            return None
        if self._valid_sensor_count() < self.min_valid_sensors:
            return None

        fingerprint = self._compose_fingerprint()
        self.stack = []
        result = {
            "sample_id": reading["sample_id"],
            "pos_x": reading["pos_x"],
            "pos_y": reading["pos_y"],
            "pos_z": reading["pos_z"],
            **fingerprint,
        }
        return result


def iter_offline_groups(hst_dir: Path) -> Iterator[tuple[str, List[dict]]]:
    groups: Dict[str, List[dict]] = defaultdict(list)
    for file_path in sorted(hst_dir.rglob("*.mbd")):
        file_meta = parse_hst_filename(file_path)
        group_id = f"{file_path.parent.name}:{file_meta['pos_x']:.2f}:{file_meta['pos_y']:.2f}:{file_meta['pos_z']:.2f}"
        with file_path.open("r", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            for row in reader:
                if len(row) < 4:
                    continue
                groups[group_id].append(
                    {
                        "timestamp": float(row[0]),
                        "sensor_alias": file_meta["alias"],
                        "rssi": int(float(row[3])),
                        "pos_x": float(file_meta["pos_x"]),
                        "pos_y": float(file_meta["pos_y"]),
                        "pos_z": float(file_meta["pos_z"]),
                        "sample_id": group_id,
                    }
                )
    for group_id in sorted(groups):
        rows = sorted(groups[group_id], key=lambda item: item["timestamp"])
        yield group_id, rows


def build_offline_rows(min_valid_sensors: int, sensor_aliases: List[str]) -> List[dict]:
    rows: List[dict] = []
    hst_dir = RAW_DATASET_DIR / "hst"
    for group_id, group_rows in iter_offline_groups(hst_dir):
        window = FingerprintWindow(
            sensor_aliases=sensor_aliases,
            min_window_size=MIN_WINDOW_SIZE,
            max_window_size=MAX_WINDOW_SIZE,
            min_entries_per_sensor=MIN_ENTRIES_PER_SENSOR,
            min_valid_sensors=min_valid_sensors,
        )
        emitted = 0
        for reading in group_rows:
            reading["sample_id"] = f"{group_id}:{emitted}"
            fingerprint = window.process(reading)
            if fingerprint is not None:
                fingerprint["sample_id"] = f"{group_id}:{emitted}"
                rows.append(fingerprint)
                emitted += 1
    return rows


def iter_online_readings(trajectory_dir: Path) -> Iterator[dict]:
    merged: List[dict] = []
    for file_path in sorted(trajectory_dir.rglob("*.mbd")):
        alias = file_path.stem.split("_")[0]
        with file_path.open("r", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            for index, row in enumerate(reader):
                if len(row) < 7:
                    continue
                merged.append(
                    {
                        "timestamp": float(row[0]),
                        "sensor_alias": alias,
                        "rssi": int(float(row[3])),
                        "pos_x": float(row[4]),
                        "pos_y": float(row[5]),
                        "pos_z": float(row[6]),
                        "sample_id": f"{trajectory_dir.name}:{index}",
                    }
                )
    merged.sort(key=lambda item: item["timestamp"])
    for item in merged:
        yield item


def build_online_rows(min_valid_sensors: int, sensor_aliases: List[str]) -> List[dict]:
    rows: List[dict] = []
    trk_dir = RAW_DATASET_DIR / "trk"
    for trajectory_dir in sorted(path for path in trk_dir.iterdir() if path.is_dir()):
        window = FingerprintWindow(
            sensor_aliases=sensor_aliases,
            min_window_size=MIN_WINDOW_SIZE,
            max_window_size=MAX_WINDOW_SIZE,
            min_entries_per_sensor=MIN_ENTRIES_PER_SENSOR,
            min_valid_sensors=min_valid_sensors,
        )
        emitted = 0
        for reading in iter_online_readings(trajectory_dir):
            reading["sample_id"] = f"{trajectory_dir.name}:{emitted}"
            fingerprint = window.process(reading)
            if fingerprint is not None:
                fingerprint["sample_id"] = f"{trajectory_dir.name}:{emitted}"
                fingerprint["trajectory"] = trajectory_dir.name
                rows.append(fingerprint)
                emitted += 1
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Build offline and online fingerprint CSV files for Lab-02 Part-02.")
    parser.add_argument("--fingerprint-name", default="lab02_ble_ferrero", help="Output dataset folder name.")
    args = parser.parse_args()

    ensure_runtime_dirs()
    sensors = load_sensors_config()
    sensor_aliases = [sensor.alias for sensor in sensors]
    fieldnames = ["sample_id", "pos_x", "pos_y", "pos_z", *sensor_aliases]
    online_fieldnames = ["sample_id", "trajectory", "pos_x", "pos_y", "pos_z", *sensor_aliases]

    fingerprint_output_dir = FINGERPRINT_DIR / args.fingerprint_name
    online_output_dir = ONLINE_DIR / args.fingerprint_name
    fingerprint_output_dir.mkdir(parents=True, exist_ok=True)
    online_output_dir.mkdir(parents=True, exist_ok=True)

    summary: Dict[str, int | str | dict] = {
        "fingerprint_name": args.fingerprint_name,
        "sensor_count": len(sensor_aliases),
        "sensors": sensor_aliases,
        "variants": {},
    }

    for variant_name, min_valid_sensors in (
        ("with_empty_values", 10),
        ("without_empty_values", 12),
    ):
        offline_rows = build_offline_rows(min_valid_sensors=min_valid_sensors, sensor_aliases=sensor_aliases)
        online_rows = build_online_rows(min_valid_sensors=min_valid_sensors, sensor_aliases=sensor_aliases)

        offline_path = fingerprint_output_dir / f"{variant_name}.csv"
        online_path = online_output_dir / f"{variant_name}.csv"

        offline_count = write_csv(offline_rows, offline_path, fieldnames)
        online_count = write_csv(online_rows, online_path, online_fieldnames)

        summary["variants"][variant_name] = {
            "min_valid_sensors": min_valid_sensors,
            "offline_rows": offline_count,
            "online_rows": online_count,
            "offline_path": str(offline_path.relative_to(RAW_DATASET_DIR.parents[2])),
            "online_path": str(online_path.relative_to(RAW_DATASET_DIR.parents[2])),
        }

    summary_path = online_output_dir / "preparation_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
