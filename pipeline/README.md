# Bleeding Retro Wiki — Content Pipeline

Automated pipeline that monitors Discord for retro console mod announcements, fetches GitHub repo content, and generates structured wiki draft pages via AI — then opens a PR and pings the review channel.

## How It Works

1. **Reads** recent messages from `#modding-news` (Discord)
2. **Extracts** GitHub repo links from those messages
3. **Fetches** repo content: README, wiki pages, release notes, BOM files
4. **Generates** a structured Astro Starlight MDX draft via AI (Anthropic → Ollama → placeholder)
5. **Commits** the draft to a new branch (`draft/<mod-name>-YYYYMMDD`)
6. **Opens** a GitHub PR to `main` via `gh` CLI
7. **Pings** `#chip-wiki-drafts` with a summary and PR link

## Quick Start

```bash
cd workspace/dmc-wiki/pipeline
pip install -r requirements.txt
python run_pipeline.py
```

## Environment Variables

| Variable | Required | Description |
|---|---|---|
| `DISCORD_BOT_TOKEN` | Optional | Discord bot token. Falls back to OpenClaw config automatically. |
| `ANTHROPIC_API_KEY` | Optional | Enables AI-powered draft generation (recommended). Without it, drafts are placeholder-only. |
| `GITHUB_TOKEN` | Optional | GitHub PAT for higher API rate limits (unauthenticated = 60 req/hr). |

> **Note:** The Discord token is automatically sourced from `~/.openclaw/openclaw.json` if `DISCORD_BOT_TOKEN` is not set.

## GitHub Auth

The `gh` CLI must be authenticated. It's already configured as `dubesinhower`. Verify with:

```bash
gh auth status
```

## State Tracking

`pipeline/state.json` tracks processed Discord message IDs and GitHub repos to avoid duplicates across runs. It's safe to edit manually if you want to reprocess something.

Example:
```json
{
  "processed_message_ids": ["804527195737161728"],
  "processed_repos": ["someuser/some-mod-repo"]
}
```

To reprocess a repo, remove it from `processed_repos`.

## Draft Output

Drafts are written to:
- `src/content/docs/consoles/` — for console-specific mods (GameCube, Wii, PS2, etc.)
- `src/content/docs/topics/` — for general topics, tools, or cross-platform content

The script auto-detects based on keywords in the generated content.

All drafts have `draft: true` in frontmatter. Remove it when the page is ready to publish.

## Cron / Heartbeat

To run every hour via cron:

```cron
0 * * * * cd /home/openclawadmin/.openclaw/workspace/dmc-wiki && python3 pipeline/run_pipeline.py >> pipeline/pipeline.log 2>&1
```

Or use OpenClaw's heartbeat by adding to `HEARTBEAT.md`:
```
- [ ] Run wiki pipeline: `python3 /home/openclawadmin/.openclaw/workspace/dmc-wiki/pipeline/run_pipeline.py`
```

## Discord Channels

| Channel | ID | Purpose |
|---|---|---|
| `#modding-news` | `804527195737161728` | Monitored for mod announcements |
| `#chip-wiki-drafts` | `1477426307649241199` | Receives draft notifications |

## Troubleshooting

- **"Discord bot token not found"** — Set `DISCORD_BOT_TOKEN` env var or check OpenClaw config
- **"gh pr create failed"** — Run `gh auth status` to verify authentication
- **Drafts are placeholder-only** — Set `ANTHROPIC_API_KEY` for AI-powered generation
- **Rate limit errors from GitHub API** — Set `GITHUB_TOKEN` for higher limits
