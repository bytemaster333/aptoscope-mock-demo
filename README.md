# Aptoscope — Mock Grafana Demo (Aptos CLI Telemetry)

**Status:** 🧪 **Mock Demo (no real Aptos required)**  
**What it is:** A zero-dependency showcase of how Aptos CLI telemetry **would look** in Grafana using a **seeded SQLite** database. Ideal for grant reviewers: quick to run, clear visuals, and no chain/tooling setup.

---

## Why this demo?
- ⚡ **Fast to evaluate:** `make seed && make up` brings up Grafana with preloaded data.
- 🔍 **What you’ll see:** CLI activity, duration trends, subcommand breakdown, and success vs failure — exactly the kind of reliability/observability signals we’ll ship for real Aptos workflows.
- 🔒 **Local-first:** No cloud, no external APIs. Everything runs in Docker on your machine.

> **Note:** This is a **mock** dataset: numbers and errors are synthetic. It demonstrates UI/queries only — not live metrics.

---

## Quickstart

```bash
cp .env.example .env
make seed
make up
# Open http://localhost:3000  (user: admin, pass: admin)
