# webhook-replay-cli

Python CLI for replaying failed webhook events with dry-run support, retry policies, structured output, and operational safety.

## Overview

`webhook-replay-cli` is a Python command-line tool for replaying previously failed webhook events to downstream systems in a controlled way.

It is aimed at operational workflows where teams need to:

- retry failed deliveries
- inspect payloads before replaying them
- avoid unsafe bulk reprocessing
- keep replay behavior visible and deterministic

## Why This Repo Exists

This project is meant to show practical Python work in the same engineering space as backend systems and integrations:

- HTTP clients
- CLI ergonomics
- retry behavior
- structured logs
- safe operational tooling

It is not a random Python exercise. It is aligned with real integration support work.

## Features

- replay events from JSON input
- dry-run mode
- configurable retry count
- deterministic retry loop with per-event attempt tracking
- batch summary output
- structured terminal output
- designed for extension with CSV, queues, or persistence later

## Example Usage

```bash
python -m webhook_replay_cli replay --input examples/events.json --dry-run
python -m webhook_replay_cli replay --input examples/events.json --max-retries 3
```

## Architecture

- `cli.py` handles argument parsing
- `services/replayer.py` owns replay orchestration and summaries
- `clients/http_client.py` wraps outbound HTTP behavior
- `models.py` defines event data structures
- `formatters.py` keeps terminal output separate from replay logic

## Tradeoffs

- simple standard-library implementation over extra dependencies
- local file input for v1 instead of database-backed replay
- sync HTTP flow for clarity in the first version

## Future Improvements

- async replay mode
- CSV input support
- persistent replay history
- exponential backoff strategies
- richer exit codes and CI
