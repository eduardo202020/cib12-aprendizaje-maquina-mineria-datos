from __future__ import annotations

import argparse
from pathlib import Path

from streaming_core import DEFAULT_CHECKPOINT_DIR, DEFAULT_DATASET, FraudStreamingEngine, load_events


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Laboratorio local de stream processing para fraude con tarjetas."
    )
    parser.add_argument("--dataset", type=Path, default=DEFAULT_DATASET)
    parser.add_argument("--window-seconds", type=int, default=120)
    parser.add_argument("--allowed-lateness", type=int, default=45)
    parser.add_argument("--checkpoint-every", type=int, default=4)
    parser.add_argument("--checkpoint-dir", type=Path, default=DEFAULT_CHECKPOINT_DIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    events = load_events(args.dataset)
    lab = FraudStreamingEngine(
        window_seconds=args.window_seconds,
        allowed_lateness=args.allowed_lateness,
        checkpoint_every=args.checkpoint_every,
        checkpoint_dir=args.checkpoint_dir,
    )

    print("\nLABORATORIO: FRAUDE CON TARJETAS EN STREAMING\n")
    print("Se procesa por arrival_time, pero las reglas usan event_time y watermark.\n")
    print(f"{'ARRIVAL':19} {'EVENT':19} {'CARD':10} {'MONTO':>8} {'DECISION':18} DETALLE")
    print("-" * 110)

    for event in sorted(events, key=lambda item: item.arrival_time):
        decision = lab.process_event(event)
        extras = []
        if decision.watermark:
            extras.append("watermark=" + decision.watermark.strftime("%H:%M:%S"))
        if decision.transaction_count is not None:
            extras.append(f"tx_ventana={decision.transaction_count}")
        if decision.amount_sum is not None:
            extras.append(f"monto_ventana={decision.amount_sum:.2f}")

        detail = "; ".join(decision.reasons + extras)
        print(
            f"{event.arrival_time.strftime('%H:%M:%S'):19} "
            f"{event.event_time.strftime('%H:%M:%S'):19} "
            f"{event.card_id:10} "
            f"{event.amount:8.2f} "
            f"{decision.decision:18} "
            f"{detail}"
        )

        if lab.processed_count % lab.checkpoint_every == 0:
            lab.write_checkpoint(final=False)

    lab.write_checkpoint(final=True)
    print("\nRESUMEN DEL LABORATORIO\n")
    print(f"Eventos procesados: {lab.processed_count}")
    print(f"Aprobadas:          {lab.summary['aprobadas']}")
    print(f"Revisadas:          {lab.summary['revisadas']}")
    print(f"Bloqueadas:         {lab.summary['bloqueadas']}")
    print(f"Tardias auditadas:  {lab.summary['tardios']}")
    print(f"Duplicados:         {lab.summary['duplicados']}")
    print(f"Checkpoints:        {len(list(args.checkpoint_dir.glob('checkpoint-*.json')))}")


if __name__ == "__main__":
    main()
