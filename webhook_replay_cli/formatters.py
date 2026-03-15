from webhook_replay_cli.clients.http_client import ReplayResult
from webhook_replay_cli.models import ReplaySummary


def render_result(result: ReplayResult) -> str:
    return f"[{result.status.upper()}] {result.event_id} (attempt {result.attempts}) - {result.detail}"


def render_summary(summary: ReplaySummary) -> str:
    return (
        f"Summary: total={summary.total}, sent={summary.sent}, "
        f"skipped={summary.skipped}, failed={summary.failed}"
    )
