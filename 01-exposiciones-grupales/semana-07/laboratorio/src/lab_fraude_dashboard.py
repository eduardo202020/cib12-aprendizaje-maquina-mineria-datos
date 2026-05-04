from __future__ import annotations

import argparse
import json
import queue
import threading
import time
from collections import deque
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from streaming_core import DEFAULT_CHECKPOINT_DIR, DEFAULT_DATASET, FraudStreamingEngine, load_events


WEB_ROOT = Path(__file__).resolve().parents[1] / "web"


class SimulationController:
    def __init__(self, dataset: Path, speed: float, port: int) -> None:
        self.dataset = dataset
        self.speed = speed
        self.port = port
        self.events = sorted(load_events(dataset), key=lambda item: item.arrival_time)
        self.engine = FraudStreamingEngine(
            window_seconds=120,
            allowed_lateness=45,
            checkpoint_every=4,
            checkpoint_dir=DEFAULT_CHECKPOINT_DIR,
        )
        self.lock = threading.Lock()
        self.queue: queue.Queue[Any] = queue.Queue()
        self.recent_decisions: deque[dict[str, Any]] = deque(maxlen=12)
        self.recent_broker: deque[dict[str, Any]] = deque(maxlen=12)
        self.running = False
        self.status = "listo"
        self.produced_count = 0
        self.processed_count = 0
        self.current_event: dict[str, Any] | None = None

    def snapshot(self) -> dict[str, Any]:
        with self.lock:
            return {
                "running": self.running,
                "status": self.status,
                "port": self.port,
                "dataset": str(self.dataset),
                "produced_count": self.produced_count,
                "processed_count": self.processed_count,
                "queue_depth": self.queue.qsize(),
                "summary": {
                    "aprobadas": self.engine.summary["aprobadas"],
                    "revisadas": self.engine.summary["revisadas"],
                    "bloqueadas": self.engine.summary["bloqueadas"],
                    "tardios": self.engine.summary["tardios"],
                    "duplicados": self.engine.summary["duplicados"],
                },
                "watermark": self.engine.current_watermark.isoformat() if self.engine.current_watermark else None,
                "current_event": self.current_event,
                "recent_decisions": list(self.recent_decisions),
                "recent_broker": list(self.recent_broker),
            }

    def start(self) -> bool:
        with self.lock:
            if self.running:
                return False
            self.running = True
            self.status = "iniciando"
            self.produced_count = 0
            self.processed_count = 0
            self.current_event = None
            self.recent_decisions.clear()
            self.recent_broker.clear()
            self.engine.reset()
            self.queue = queue.Queue()

        producer = threading.Thread(target=self._run_producer, daemon=True)
        processor = threading.Thread(target=self._run_processor, daemon=True)
        producer.start()
        processor.start()
        return True

    def _run_producer(self) -> None:
        previous_arrival = None
        with self.lock:
            self.status = "produciendo eventos"

        for event in self.events:
            if previous_arrival is not None:
                delta = (event.arrival_time - previous_arrival).total_seconds()
                time.sleep(max(0.1, delta / self.speed))
            previous_arrival = event.arrival_time

            self.queue.put(event)
            with self.lock:
                self.produced_count += 1
                self.current_event = event.to_json_ready()
                self.recent_broker.appendleft(
                    {
                        "event_id": event.event_id,
                        "card_id": event.card_id,
                        "amount": event.amount,
                        "country": event.country,
                        "arrival_time": event.arrival_time.strftime("%H:%M:%S"),
                        "event_time": event.event_time.strftime("%H:%M:%S"),
                    }
                )

        self.queue.put(None)

    def _run_processor(self) -> None:
        while True:
            item = self.queue.get()
            if item is None:
                break

            decision = self.engine.process_event(item)
            if self.engine.processed_count % self.engine.checkpoint_every == 0:
                self.engine.write_checkpoint(final=False)

            with self.lock:
                self.processed_count = self.engine.processed_count
                self.status = "procesando flujo"
                self.recent_decisions.appendleft(
                    {
                        "event_id": decision.event_id,
                        "card_id": decision.card_id,
                        "amount": decision.amount,
                        "country": decision.country,
                        "decision": decision.decision,
                        "reasons": decision.reasons,
                        "watermark": decision.watermark.strftime("%H:%M:%S") if decision.watermark else None,
                        "event_time": decision.event_time.strftime("%H:%M:%S"),
                        "arrival_time": decision.arrival_time.strftime("%H:%M:%S"),
                    }
                )

            time.sleep(0.35)

        self.engine.write_checkpoint(final=True)
        with self.lock:
            self.running = False
            self.status = "flujo finalizado"
            self.processed_count = self.engine.processed_count


def build_handler(controller: SimulationController) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path == "/api/state":
                self._send_json(controller.snapshot())
                return
            if parsed.path == "/" or parsed.path == "/index.html":
                self._send_file(WEB_ROOT / "index.html", "text/html; charset=utf-8")
                return
            if parsed.path == "/app.js":
                self._send_file(WEB_ROOT / "app.js", "application/javascript; charset=utf-8")
                return
            if parsed.path == "/styles.css":
                self._send_file(WEB_ROOT / "styles.css", "text/css; charset=utf-8")
                return
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")

        def do_POST(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path == "/api/start":
                started = controller.start()
                self._send_json({"started": started, "state": controller.snapshot()})
                return
            self.send_error(HTTPStatus.NOT_FOUND, "Not Found")

        def log_message(self, format: str, *args: Any) -> None:
            return

        def _send_json(self, payload: dict[str, Any]) -> None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _send_file(self, path: Path, content_type: str) -> None:
            data = path.read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    return Handler


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dashboard visual del laboratorio de fraude en streaming.")
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--speed", type=float, default=6.0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    controller = SimulationController(dataset=args.dataset, speed=args.speed, port=args.port)
    server = ThreadingHTTPServer(("127.0.0.1", args.port), build_handler(controller))
    print(f"Dashboard disponible en http://127.0.0.1:{args.port}")
    print("Abre esa URL en el navegador y pulsa 'Iniciar simulacion'.")
    server.serve_forever()


if __name__ == "__main__":
    main()
