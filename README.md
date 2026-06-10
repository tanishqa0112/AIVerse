# AIVerse 🤖

> Your intelligent, self-updating guide to the AI ecosystem.

AIVerse is an open-source project that helps developers, researchers, and enthusiasts:

- Discover and compare AI tools, LLMs, and agents
- Understand strengths, weaknesses, and ideal use cases for each
- Stay updated with curated market signals and community contributions

## Features

- 🔍 Search AI tools by use case, category, or capability (app layer, in progress)
- ⚖️ Side-by-side comparison of any two AI tools
- 🧠 AI-powered explanations (via LLM integration)
- 📰 Market pulse feed of notable AI releases and trends
- 🏷️ Categorized: LLMs, agents, dev tools, platforms, and more
- ✅ Open-source and community-driven

## Repository layout

| Path | Purpose |
|------|---------|
| `schema/` | JSON Schema for validated catalog entries |
| `data/tools/` | Products and platforms (IDEs, APIs, orchestration, eval, etc.) |
| `data/llms/` | Model families and hosting options |
| `data/agents/` | Agent runtimes, frameworks, and patterns |
| `data/market-pulse/` | Short dated notes on notable releases and trends (YAML) |
| `scripts/` | Validation and checks |

## Quick start

```bash
pip install -r requirements.txt
python scripts/validate.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Add or update entries with sources where possible; prefer neutral, specific language over superlatives.

## Publish on GitHub

```bash
git remote add origin https://github.com/tanishqa0112/AIVerse.git
git branch -M main
git push -u origin main
```

CI runs `scripts/validate.py` on every push and pull request.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Tanishqa Rawlani.
