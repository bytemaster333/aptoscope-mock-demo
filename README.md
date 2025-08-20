# Aptoscope — Mock Grafana Demo (Aptos-style CLI Telemetry)

> **Status:** **Mock demo** (seeded SQLite data) · **Local-first** · **Dockerized**  
> **One-liner:** Turn Aptos CLI activity into clear, actionable operational insight—before wiring any real collectors.

![Aptoscope Demo](./screenshot.png)

## What it is
Aptoscope is a **Grafana dashboard** powered by a **seeded SQLite** dataset that mimics Aptos CLI telemetry. It lets reviewers experience the **final UX**—charts, tables, and KPIs—without installing Aptos or running collectors.

## Why it matters (benefits)
- **Faster diagnosis:** Visualize command failures, spikes, and slowdowns (e.g., `move publish`).
- **Reliability metrics that stick:** Success rate, latency trends, and subcommand usage become standard team KPIs.
- **Zero friction:** Works fully offline with mock data; real collectors can be plugged in later with the same schema.
- **Privacy by design:** Local database & Docker; no external services required by default.

## What you’ll see
- **Full CLI Command Log:** recent commands with arguments, profiles, and exit codes.
- **Command Duration Over Time:** trend of execution latencies (ms).
- **Subcommand Usage Breakdown:** which Move/CLI operations run most.
- **Success vs Failure:** quick health snapshot for the current window.

## Quickstart
```bash
cp .env.example .env
make seed
make up
# Open: http://localhost:3000  (user: admin, pass: admin)
```

---

## How it works
- **Data:** scripts/generate_mock_db.py seeds mock/aptos_logs.db with realistic Aptos-style events.
- **Provisioning:** Grafana auto-loads the SQLite datasource and the Aptoscope dashboard.
- **Schema:** logs(timestamp_ms, grp, subcommand, duration_ms, exit_code, network, profile, args, stdout, stderr).

---

## Screenshots
