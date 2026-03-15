import argparse

from webhook_replay_cli.formatters import render_result, render_summary
from webhook_replay_cli.services.replayer import WebhookReplayer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="webhook-replay")
    subparsers = parser.add_subparsers(dest="command", required=True)

    replay_parser = subparsers.add_parser("replay", help="Replay webhook events from a JSON file.")
    replay_parser.add_argument("--input", required=True, help="Path to a JSON file containing events.")
    replay_parser.add_argument("--dry-run", action="store_true", help="Validate and print actions without sending.")
    replay_parser.add_argument(
        "--max-retries",
        type=int,
        default=1,
        help="Maximum replay attempts per event.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "replay":
        replayer = WebhookReplayer()
        results = replayer.replay_with_retries(
            input_path=args.input,
            dry_run=args.dry_run,
            max_retries=args.max_retries,
        )
        for result in results:
            print(render_result(result))
        print(render_summary(replayer.summarize(results)))


if __name__ == "__main__":
    main()
