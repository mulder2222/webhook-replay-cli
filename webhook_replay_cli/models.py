from dataclasses import dataclass


@dataclass(slots=True)
class WebhookEvent:
    event_id: str
    target_url: str
    payload: dict


@dataclass(slots=True)
class ReplaySummary:
    total: int
    sent: int
    skipped: int
    failed: int
