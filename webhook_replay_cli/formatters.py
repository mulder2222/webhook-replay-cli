from webhook_replay_cli.clients.http_client import ReplayResult


def render_result(result: ReplayResult) -> str:
    return f"[{result.status.upper()}] {result.event_id} - {result.detail}"
