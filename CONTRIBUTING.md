# Contributing to AIVerse

Thank you for helping keep this resource accurate and useful.

## Principles

1. **Verifiable**: Link to docs, papers, or official announcements when stating capabilities or pricing.
2. **Specific**: Say what a tool does in context (e.g. “strong for RAG-heavy workflows”) rather than “best in class.”
3. **Balanced**: Every substantive entry should list both strengths and weaknesses (or “limitations”) where applicable.
4. **Neutral tone**: Describe trade-offs; avoid marketing language.

## What to add

- **New entries** under `data/tools/`, `data/llms/`, or `data/agents/` as JSON files, one file per `id`.
- **Market pulse** items in `data/market-pulse/` as YAML snippets (see existing examples).
- **Schema changes** only when we need new fields; discuss in an issue first for large shifts.

## File naming

- Use the entry `id` as the filename: `my-tool-id.json`.
- IDs: lowercase, hyphen-separated ASCII (e.g. `example-copilot-api`).

## Validate before you PR

From the repo root:

```bash
pip install -r requirements.txt
python scripts/validate.py
```

## Pull request checklist

- `python scripts/validate.py` passes
- Entry includes `last_updated` (ISO date)
- Strengths and weaknesses (or clear “unknown / TBD” with a note) where relevant
- Links point to stable URLs where possible
