from dataclasses import dataclass


@dataclass(slots=True)
class WebhookEvent:
    event_id: str
    target_url: str
    payload: dict
