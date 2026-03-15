import argparse

from webhook_replay_cli.formatters import render_result
from webhook_replay_cli.services.replayer import WebhookReplayer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="webhook-replay")
    subparsers = parser.add_subparsers(dest="command", required=True)

    replay_parser = subparsers.add_parser("replay", help="Replay webhook events from a JSON file.")
    replay_parser.add_argument("--input", required=True, help="Path to a JSON file containing events.")
    replay_parser.add_argument("--dry-run", action="store_true", help="Validate and print actions without sending.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "replay":
        replayer = WebhookReplayer()
        for result in replayer.replay(input_path=args.input, dry_run=args.dry_run):
            print(render_result(result))


if __name__ == "__main__":
    main()
