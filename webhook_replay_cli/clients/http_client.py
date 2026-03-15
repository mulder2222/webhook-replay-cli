from dataclasses import dataclass


@dataclass(slots=True)
class ReplayResult:
    event_id: str
    status: str
    detail: str
    attempts: int


class HttpReplayClient:
    def send(
        self,
        event_id: str,
        target_url: str,
        payload: dict,
        dry_run: bool,
        attempt: int = 1,
    ) -> ReplayResult:
        if dry_run:
            return ReplayResult(
                event_id=event_id,
                status="skipped",
                detail=f"Dry-run replay to {target_url}",
                attempts=attempt,
            )

        should_fail = payload.get("simulate") == "fail"

        if should_fail:
            return ReplayResult(
                event_id=event_id,
                status="failed",
                detail=f"Replay failed for {target_url}",
                attempts=attempt,
            )

        return ReplayResult(
            event_id=event_id,
            status="sent",
            detail=f"Replay sent to {target_url}",
            attempts=attempt,
        )
