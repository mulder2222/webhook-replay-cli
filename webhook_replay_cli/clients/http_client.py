from dataclasses import dataclass


@dataclass(slots=True)
class ReplayResult:
    event_id: str
    status: str
    detail: str


class HttpReplayClient:
    def send(self, event_id: str, target_url: str, payload: dict, dry_run: bool) -> ReplayResult:
        if dry_run:
            return ReplayResult(event_id=event_id, status="skipped", detail=f"Dry-run replay to {target_url}")

        return ReplayResult(event_id=event_id, status="sent", detail=f"Replay sent to {target_url}")
