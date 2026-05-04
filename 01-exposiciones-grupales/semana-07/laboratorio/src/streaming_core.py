from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATASET = ROOT / "data" / "transacciones.jsonl"
DEFAULT_CHECKPOINT_DIR = ROOT / "checkpoints"


@dataclass
class TransactionEvent:
    event_id: str
    card_id: str
    merchant: str
    amount: float
    country: str
    event_time: datetime
    arrival_time: datetime

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "TransactionEvent":
        return cls(
            event_id=payload["event_id"],
            card_id=payload["card_id"],
            merchant=payload["merchant"],
            amount=float(payload["amount"]),
            country=payload["country"],
            event_time=datetime.fromisoformat(payload["event_time"]),
            arrival_time=datetime.fromisoformat(payload["arrival_time"]),
        )

    def to_json_ready(self) -> dict[str, Any]:
        return {
            "event_id": self.event_id,
            "card_id": self.card_id,
            "merchant": self.merchant,
            "amount": self.amount,
            "country": self.country,
            "event_time": self.event_time.isoformat(),
            "arrival_time": self.arrival_time.isoformat(),
        }


@dataclass
class FraudDecision:
    event_id: str
    card_id: str
    amount: float
    country: str
    merchant: str
    event_time: datetime
    arrival_time: datetime
    decision: str
    reasons: list[str]
    watermark: datetime | None
    transaction_count: int | None
    amount_sum: float | None

    def to_json_ready(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["event_time"] = self.event_time.isoformat()
        payload["arrival_time"] = self.arrival_time.isoformat()
        payload["watermark"] = self.watermark.isoformat() if self.watermark else None
        return payload


class FraudStreamingEngine:
    def __init__(
        self,
        window_seconds: int,
        allowed_lateness: int,
        checkpoint_every: int,
        checkpoint_dir: Path,
    ) -> None:
        self.window = timedelta(seconds=window_seconds)
        self.allowed_lateness = timedelta(seconds=allowed_lateness)
        self.checkpoint_every = checkpoint_every
        self.checkpoint_dir = checkpoint_dir
        self.reset()

    def reset(self) -> None:
        self.state: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.seen_event_ids: set[str] = set()
        self.max_event_time: datetime | None = None
        self.processed_count = 0
        self.summary = defaultdict(int)

    @property
    def current_watermark(self) -> datetime | None:
        if self.max_event_time is None:
            return None
        return self.max_event_time - self.allowed_lateness

    def process_event(self, event: TransactionEvent) -> FraudDecision:
        self.processed_count += 1

        if event.event_id in self.seen_event_ids:
            self.summary["duplicados"] += 1
            return FraudDecision(
                event_id=event.event_id,
                card_id=event.card_id,
                amount=event.amount,
                country=event.country,
                merchant=event.merchant,
                event_time=event.event_time,
                arrival_time=event.arrival_time,
                decision="IGNORAR_DUPLICADO",
                reasons=["event_id repetido"],
                watermark=self.current_watermark,
                transaction_count=None,
                amount_sum=None,
            )

        self.seen_event_ids.add(event.event_id)

        if self.max_event_time is None or event.event_time > self.max_event_time:
            self.max_event_time = event.event_time

        watermark = self.current_watermark
        if watermark and event.event_time < watermark:
            self.summary["tardios"] += 1
            lateness = int((watermark - event.event_time).total_seconds())
            return FraudDecision(
                event_id=event.event_id,
                card_id=event.card_id,
                amount=event.amount,
                country=event.country,
                merchant=event.merchant,
                event_time=event.event_time,
                arrival_time=event.arrival_time,
                decision="AUDITAR_TARDE",
                reasons=[f"evento tardio por {lateness} s respecto al watermark"],
                watermark=watermark,
                transaction_count=None,
                amount_sum=None,
            )

        current_state = self.state[event.card_id]
        cutoff = event.event_time - self.window
        current_state[:] = [item for item in current_state if item["event_time"] >= cutoff]

        reasons: list[str] = []
        if event.amount >= 900:
            reasons.append("monto individual alto")

        if current_state:
            last_country = current_state[-1]["country"]
            last_event_time = current_state[-1]["event_time"]
            if last_country != event.country and (event.event_time - last_event_time) <= timedelta(minutes=2):
                reasons.append("cambio de pais en menos de 2 minutos")

        amount_sum = sum(item["amount"] for item in current_state) + event.amount
        transaction_count = len(current_state) + 1
        if transaction_count >= 3 and amount_sum >= 1200:
            reasons.append("alta frecuencia y monto acumulado en ventana")

        current_state.append(
            {
                "event_id": event.event_id,
                "event_time": event.event_time,
                "amount": event.amount,
                "country": event.country,
            }
        )

        if "alta frecuencia y monto acumulado en ventana" in reasons:
            decision = "BLOQUEAR"
            self.summary["bloqueadas"] += 1
        elif reasons:
            decision = "REVISAR"
            self.summary["revisadas"] += 1
        else:
            decision = "APROBAR"
            self.summary["aprobadas"] += 1

        return FraudDecision(
            event_id=event.event_id,
            card_id=event.card_id,
            amount=event.amount,
            country=event.country,
            merchant=event.merchant,
            event_time=event.event_time,
            arrival_time=event.arrival_time,
            decision=decision,
            reasons=reasons or ["sin patron sospechoso"],
            watermark=watermark,
            transaction_count=transaction_count,
            amount_sum=amount_sum,
        )

    def write_checkpoint(self, final: bool) -> Path:
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        suffix = "final" if final else f"{self.processed_count:03d}"
        path = self.checkpoint_dir / f"checkpoint-{suffix}.json"
        payload = {
            "processed_count": self.processed_count,
            "max_event_time": self.max_event_time.isoformat() if self.max_event_time else None,
            "seen_event_ids": sorted(self.seen_event_ids),
            "summary": dict(self.summary),
            "state": {
                card_id: [
                    {
                        "event_id": item["event_id"],
                        "event_time": item["event_time"].isoformat(),
                        "amount": item["amount"],
                        "country": item["country"],
                    }
                    for item in values
                ]
                for card_id, values in self.state.items()
            },
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return path


def load_events(dataset: Path = DEFAULT_DATASET) -> list[TransactionEvent]:
    events = []
    for line in dataset.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        events.append(TransactionEvent.from_dict(json.loads(line)))
    return events
