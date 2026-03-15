import json
from pathlib import Path

from webhook_replay_cli.clients.http_client import HttpReplayClient, ReplayResult
from webhook_replay_cli.models import ReplaySummary, WebhookEvent


class WebhookReplayer:
    def __init__(self, client: HttpReplayClient | None = None) -> None:
        self.client = client or HttpReplayClient()

    def load_events(self, input_path: str) -> list[WebhookEvent]:
        raw_events = json.loads(Path(input_path).read_text(encoding="utf-8"))

        return [
            WebhookEvent(
                event_id=item["event_id"],
                target_url=item["target_url"],
                payload=item["payload"],
            )
            for item in raw_events
        ]

    def replay(self, input_path: str, dry_run: bool) -> list[ReplayResult]:
        events = self.load_events(input_path)

        return [
            self.client.send(
                event_id=event.event_id,
                target_url=event.target_url,
                payload=event.payload,
                dry_run=dry_run,
            )
            for event in events
        ]

    def replay_with_retries(
        self,
        input_path: str,
        dry_run: bool,
        max_retries: int,
    ) -> list[ReplayResult]:
        results: list[ReplayResult] = []

        for event in self.load_events(input_path):
            attempt = 1
            result = self.client.send(
                event_id=event.event_id,
                target_url=event.target_url,
                payload=event.payload,
                dry_run=dry_run,
                attempt=attempt,
            )

            while result.status == "failed" and attempt < max_retries:
                attempt += 1
                result = self.client.send(
                    event_id=event.event_id,
                    target_url=event.target_url,
                    payload=event.payload,
                    dry_run=dry_run,
                    attempt=attempt,
                )

            results.append(result)

        return results

    def summarize(self, results: list[ReplayResult]) -> ReplaySummary:
        return ReplaySummary(
            total=len(results),
            sent=sum(1 for result in results if result.status == "sent"),
            skipped=sum(1 for result in results if result.status == "skipped"),
            failed=sum(1 for result in results if result.status == "failed"),
        )
