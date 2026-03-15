from pathlib import Path

from webhook_replay_cli.services.replayer import WebhookReplayer


def test_replayer_loads_and_replays_events(tmp_path: Path) -> None:
    input_file = tmp_path / "events.json"
    input_file.write_text(
        '[{"event_id":"evt-1","target_url":"https://example.test/hook","payload":{"ok":true}}]',
        encoding="utf-8",
    )

    results = WebhookReplayer().replay_with_retries(str(input_file), dry_run=True, max_retries=1)

    assert len(results) == 1
    assert results[0].status == "skipped"


def test_replayer_retries_failed_events(tmp_path: Path) -> None:
    input_file = tmp_path / "events.json"
    input_file.write_text(
        '[{"event_id":"evt-2","target_url":"https://example.test/hook","payload":{"simulate":"fail"}}]',
        encoding="utf-8",
    )

    results = WebhookReplayer().replay_with_retries(str(input_file), dry_run=False, max_retries=3)

    assert len(results) == 1
    assert results[0].status == "failed"
    assert results[0].attempts == 3
