#!/usr/bin/env python3
"""
Bleeding Retro Wiki - Content Pipeline
---------------------------------------
Reads recent Discord messages from #modding-news, extracts GitHub repo links,
fetches repo content, generates a structured mod entry via AI, appends it to
the appropriate console page, opens a PR, and pings #chip-wiki-drafts.

Run as a one-shot script (cron/heartbeat triggered).
"""

import json
import logging
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

MONITOR_CHANNEL_ID = "804527195737161728"   # #modding-news
REVIEW_CHANNEL_ID  = "1477426307649241199"  # #chip-wiki-drafts
CHRIS_USER_ID      = "269900067249455104"
WIKI_REPO          = "dubesinhower/dmc-wiki"
WIKI_REPO_URL      = f"https://github.com/{WIKI_REPO}"
WIKI_LOCAL_PATH    = Path(__file__).parent.parent  # workspace/dmc-wiki/
PIPELINE_DIR       = Path(__file__).parent
STATE_FILE         = PIPELINE_DIR / "state.json"
DISCORD_API        = "https://discord.com/api/v10"

CONSOLES_DIR       = WIKI_LOCAL_PATH / "src" / "content" / "docs" / "consoles"

VALID_CONSOLE_SLUGS = [
    "nes", "snes", "n64", "gamecube", "gameboy", "gba",
    "genesis", "saturn", "dreamcast", "game-gear",
    "ps1", "ps2", "neo-geo", "xbox", "tg16-pce", "laser-active",
    "atari", "obscure",
]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("pipeline")

# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"processed_message_ids": [], "processed_repos": []}


def save_state(state: dict):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
    log.info("State saved.")


# ---------------------------------------------------------------------------
# Discord helpers
# ---------------------------------------------------------------------------

def get_discord_token() -> str:
    """Resolve Discord bot token from env or OpenClaw config."""
    token = os.environ.get("DISCORD_BOT_TOKEN")
    if token:
        return token

    # Fall back to OpenClaw config
    config_path = Path.home() / ".openclaw" / "openclaw.json"
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)
        token = config.get("channels", {}).get("discord", {}).get("token")
        if token:
            return token

    raise RuntimeError(
        "Discord bot token not found. Set DISCORD_BOT_TOKEN env var or ensure "
        "OpenClaw discord channel is configured."
    )


def discord_headers(token: str) -> dict:
    return {"Authorization": f"Bot {token}", "Content-Type": "application/json"}


def fetch_recent_messages(token: str, channel_id: str, limit: int = 50) -> list[dict]:
    """Fetch recent messages from a Discord channel."""
    url = f"{DISCORD_API}/channels/{channel_id}/messages"
    resp = requests.get(url, headers=discord_headers(token), params={"limit": limit})
    resp.raise_for_status()
    messages = resp.json()
    log.info(f"Fetched {len(messages)} messages from channel {channel_id}.")
    return messages


def post_discord_message(token: str, channel_id: str, content: str):
    """Post a message to a Discord channel."""
    url = f"{DISCORD_API}/channels/{channel_id}/messages"
    resp = requests.post(
        url,
        headers=discord_headers(token),
        json={"content": content},
    )
    resp.raise_for_status()
    log.info(f"Posted message to channel {channel_id}.")
    return resp.json()


# ---------------------------------------------------------------------------
# Generation scope filter (6th gen and older only)
# ---------------------------------------------------------------------------

_OUT_OF_SCOPE_PATTERNS = re.compile(
    r"\b("
    r"ps3|ps4|ps5|playstation\s*3|playstation\s*4|playstation\s*5"
    r"|xbox[\s\-]?360|xbox[\s\-]?one|xbox[\s\-]?series|xbone"
    r"|wii[\s\-]?u|wiiu"
    r"|nintendo[\s\-]?switch|nsw|nswitch"
    r"|nintendo[\s\-]?ds|nds|dsi"
    r"|3ds|new[\s\-]?3ds|2ds"
    r"|psp|ps[\s\-]?vita|psvita"
    r")\b",
    re.IGNORECASE,
)


def is_in_scope(repo: str, message_text: str) -> bool:
    """Return False if repo or message clearly references 7th-gen-or-newer hardware."""
    combined = f"{repo} {message_text}"
    if _OUT_OF_SCOPE_PATTERNS.search(combined):
        return False
    return True


# ---------------------------------------------------------------------------
# GitHub repo extraction
# ---------------------------------------------------------------------------

GITHUB_REPO_RE = re.compile(
    r"https?://github\.com/([A-Za-z0-9_.\-]+/[A-Za-z0-9_.\-]+)"
)


def extract_github_repos(messages: list[dict]) -> list[tuple[str, str]]:
    """Return list of (message_id, repo_full_name) tuples from messages."""
    found = []
    for msg in messages:
        text = msg.get("content", "")
        for embed in msg.get("embeds", []):
            text += " " + (embed.get("url") or "") + " " + (embed.get("description") or "")
        for match in GITHUB_REPO_RE.finditer(text):
            repo = match.group(1).rstrip("/")
            repo = re.sub(r"\.git$", "", repo)
            found.append((msg["id"], repo))
    return found


# ---------------------------------------------------------------------------
# GitHub repo content fetching
# ---------------------------------------------------------------------------

GITHUB_API = "https://api.github.com"


def github_headers() -> dict:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if result.returncode == 0:
            token = result.stdout.strip()
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def fetch_file_content(repo: str, path: str) -> Optional[str]:
    """Fetch decoded text content of a file in a GitHub repo."""
    url = f"{GITHUB_API}/repos/{repo}/contents/{path}"
    resp = requests.get(url, headers=github_headers())
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    data = resp.json()
    if isinstance(data, list):
        return None
    import base64
    try:
        return base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    except Exception:
        return None


def fetch_repo_wiki_pages(repo: str) -> list[str]:
    """Try to fetch GitHub wiki content (clone the wiki repo)."""
    wiki_url = f"https://github.com/{repo}.wiki.git"
    pages = []
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            ["git", "clone", "--depth=1", wiki_url, tmpdir],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            return []
        for md_file in Path(tmpdir).glob("*.md"):
            pages.append(md_file.read_text(errors="replace"))
    return pages


def fetch_releases(repo: str) -> str:
    """Fetch latest release notes from GitHub API."""
    url = f"{GITHUB_API}/repos/{repo}/releases/latest"
    resp = requests.get(url, headers=github_headers())
    if resp.status_code == 404:
        return ""
    resp.raise_for_status()
    data = resp.json()
    return data.get("body", "")


def fetch_repo_content(repo: str) -> dict:
    """Aggregate all useful content from a GitHub repo."""
    log.info(f"Fetching content for repo: {repo}")
    content = {"repo": repo, "readme": None, "wiki": [], "releases": "", "bom": None}

    for readme_name in ["README.md", "readme.md", "README", "ReadMe", "Readme.md", "README.txt", "readme.txt", "readme", "README.rst"]:
        text = fetch_file_content(repo, readme_name)
        if text:
            content["readme"] = text
            log.info(f"  Found README as '{readme_name}' ({len(text)} chars)")
            break

    for bom_name in ["BOM.md", "bom.md", "BOM.csv", "bom.csv", "parts.md", "PARTS.md"]:
        text = fetch_file_content(repo, bom_name)
        if text:
            content["bom"] = text
            log.info(f"  Found BOM: {bom_name}")
            break

    content["releases"] = fetch_releases(repo)
    if content["releases"]:
        log.info(f"  Found release notes ({len(content['releases'])} chars)")

    wiki_pages = fetch_repo_wiki_pages(repo)
    content["wiki"] = wiki_pages
    if wiki_pages:
        log.info(f"  Found {len(wiki_pages)} wiki page(s)")

    return content


# ---------------------------------------------------------------------------
# Console identification
# ---------------------------------------------------------------------------

def _call_openclaw_agent(prompt: str, timeout: int = 60) -> Optional[str]:
    """Call openclaw agent and return the text reply, or None on failure."""
    try:
        result = subprocess.run(
            ["openclaw", "agent", "--agent", "main", "--message", prompt, "--json"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except FileNotFoundError:
        log.warning("openclaw CLI not found in PATH.")
        return None
    except subprocess.TimeoutExpired:
        log.warning("openclaw agent timed out.")
        return None

    if result.returncode != 0:
        log.warning(f"openclaw agent exited {result.returncode}: {result.stderr[:200]}")
        return None

    raw = result.stdout.strip()
    if not raw:
        return None

    try:
        data = json.loads(raw)
        text = (
            data.get("reply")
            or data.get("text")
            or data.get("content")
            or data.get("message")
        )
        if not text:
            result_field = data.get("result")
            if isinstance(result_field, dict):
                payloads = result_field.get("payloads", [])
                if payloads and isinstance(payloads[0], dict):
                    text = payloads[0].get("text")
            if not text and isinstance(result_field, str):
                text = result_field
            elif not text and isinstance(data.get("output"), str):
                text = data["output"]
        return text.strip() if text else None
    except json.JSONDecodeError:
        return raw.strip()


def identify_console(content: dict) -> str:
    """Ask the AI which console slug this mod targets. Returns a valid slug."""
    repo_name = content["repo"]
    readme_excerpt = (content["readme"] or "")[:300]

    slug_list = ", ".join(VALID_CONSOLE_SLUGS)
    prompt = (
        f"Given this GitHub repo name and README excerpt, which console does this mod target?\n"
        f"Repo: {repo_name}\n"
        f"README: {readme_excerpt}\n\n"
        f"Reply with ONLY the console slug from this list:\n"
        f"{slug_list}\n\n"
        f"If unsure, reply: obscure"
    )

    log.info("Identifying target console via openclaw agent...")
    reply = _call_openclaw_agent(prompt, timeout=60)

    if reply:
        # Extract just the slug (first word, stripped)
        candidate = reply.strip().lower().split()[0].rstrip(".,;:")
        if candidate in VALID_CONSOLE_SLUGS:
            log.info(f"Console identified: {candidate}")
            return candidate
        # Try finding any valid slug in the reply
        for slug in VALID_CONSOLE_SLUGS:
            if slug in reply.lower():
                log.info(f"Console identified (from reply): {slug}")
                return slug

    log.warning("Could not identify console, defaulting to 'obscure'.")
    return "obscure"


# ---------------------------------------------------------------------------
# AI mod entry generation
# ---------------------------------------------------------------------------

MOD_ENTRY_PROMPT_TEMPLATE = """You are writing a mod entry for the Bleeding Retro Wiki — a retro console modding reference site.

Generate a mod entry section based on the following GitHub repository content.

Repo: {repo_name}
URL: {repo_url}

Content:
{content}

Generate ONLY a mod entry in this exact format (no extra explanation, no code fences):

### [Mod Name]

[Brief description of what the mod does.]

- **Compatible hardware:** [list board revisions/variants]
- **Required parts:** [parts list or "See source for full BOM"]
- **Difficulty:** [Beginner / Intermediate / Advanced]
- **Source:** [{repo_url}]({repo_url})"""


def generate_mod_entry(content: dict) -> Optional[str]:
    """Generate a mod entry section via openclaw agent."""
    repo = content["repo"]
    repo_url = f"https://github.com/{repo}"

    parts = []
    if content["readme"]:
        parts.append(f"### README\n\n{content['readme']}")
    if content["bom"]:
        parts.append(f"### BOM / Parts List\n\n{content['bom']}")
    if content["releases"]:
        parts.append(f"### Release Notes\n\n{content['releases']}")
    if content["wiki"]:
        wiki_text = "\n\n---\n\n".join(content["wiki"])
        parts.append(f"### Wiki Pages\n\n{wiki_text}")

    combined_content = "\n\n".join(parts) if parts else "(no content found)"

    prompt = MOD_ENTRY_PROMPT_TEMPLATE.format(
        repo_name=repo,
        repo_url=repo_url,
        content=combined_content,
    )

    log.info("Generating mod entry via openclaw agent...")
    reply = _call_openclaw_agent(prompt, timeout=120)

    if reply:
        # Strip any accidental code fences
        reply = re.sub(r"^```(?:mdx?)?\s*\n?", "", reply.strip())
        reply = re.sub(r"\n?```\s*$", "", reply.strip())
        return reply.strip()

    log.warning("openclaw agent unavailable — using placeholder mod entry.")
    return generate_mod_entry_fallback(content)


def generate_mod_entry_fallback(content: dict) -> str:
    """Generate a placeholder mod entry when no AI is available."""
    repo = content["repo"]
    repo_url = f"https://github.com/{repo}"
    mod_name = repo.split("/")[-1].replace("-", " ").replace("_", " ").title()

    return (
        f"### {mod_name}\n\n"
        f"TODO: Add description.\n\n"
        f"- **Compatible hardware:** TODO\n"
        f"- **Required parts:** See source for full BOM\n"
        f"- **Difficulty:** TODO\n"
        f"- **Source:** [{repo_url}]({repo_url})\n"
    )


# ---------------------------------------------------------------------------
# Console page manipulation
# ---------------------------------------------------------------------------

MODS_PLACEHOLDER = "_No mods documented yet. Check back soon._"


def append_mod_to_console_page(console_slug: str, mod_entry: str) -> Path:
    """
    Insert mod_entry into the ## Mods section of the console page.
    Replaces placeholder text if present, otherwise appends after existing mods.
    Returns the path of the modified file.
    """
    page_path = CONSOLES_DIR / f"{console_slug}.mdx"
    if not page_path.exists():
        log.warning(f"Console page not found: {page_path}. Falling back to obscure.")
        page_path = CONSOLES_DIR / "obscure.mdx"

    current = page_path.read_text(encoding="utf-8")

    # If placeholder exists, replace it
    if MODS_PLACEHOLDER in current:
        updated = current.replace(MODS_PLACEHOLDER, mod_entry, 1)
    else:
        # Find ## Resources (or end of file) and insert before it
        resources_match = re.search(r"^## Resources", current, re.MULTILINE)
        if resources_match:
            insert_pos = resources_match.start()
            updated = current[:insert_pos] + mod_entry + "\n\n" + current[insert_pos:]
        else:
            # Append at end
            updated = current.rstrip() + "\n\n" + mod_entry + "\n"

    page_path.write_text(updated, encoding="utf-8")
    log.info(f"Updated console page: {page_path}")
    return page_path


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    """Convert text to URL-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Git / PR operations
# ---------------------------------------------------------------------------

def run_git(args: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git"] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=check,
    )


def create_pr(console_slug: str, mod_slug: str, page_path: Path, repo: str) -> Optional[str]:
    """
    Commit the updated console page to a new branch and open a PR.
    Returns the PR URL or None on failure.
    """
    date_str = datetime.now().strftime("%Y%m%d")
    branch_name = f"draft/{console_slug}-{mod_slug}-{date_str}"

    log.info(f"Creating branch: {branch_name}")

    run_git(["fetch", "origin"], cwd=WIKI_LOCAL_PATH)
    run_git(["checkout", "main"], cwd=WIKI_LOCAL_PATH)
    run_git(["pull", "origin", "main"], cwd=WIKI_LOCAL_PATH)
    run_git(["checkout", "-b", branch_name], cwd=WIKI_LOCAL_PATH)

    run_git(["add", str(page_path)], cwd=WIKI_LOCAL_PATH)
    commit_msg = (
        f"feat(wiki): add {mod_slug} mod to {console_slug} page\n\n"
        f"Auto-generated from {repo}"
    )
    run_git(["commit", "-m", commit_msg], cwd=WIKI_LOCAL_PATH)

    result = run_git(["push", "-u", "origin", branch_name], cwd=WIKI_LOCAL_PATH, check=False)
    if result.returncode != 0:
        log.error(f"Push failed: {result.stderr}")
        run_git(["checkout", "main"], cwd=WIKI_LOCAL_PATH)
        return None

    repo_url = f"https://github.com/{repo}"
    pr_title = f"[Draft] Add {mod_slug} to {console_slug} page"
    pr_body = (
        f"Auto-generated mod entry appended to `consoles/{console_slug}.mdx`.\n\n"
        f"**Source repo:** [{repo}]({repo_url})\n\n"
        f"**Review checklist:**\n"
        f"- [ ] Verify mod name and description\n"
        f"- [ ] Check compatible hardware list\n"
        f"- [ ] Validate parts list / BOM\n"
        f"- [ ] Set correct installation difficulty\n"
        f"- [ ] Remove draft status when ready to publish\n"
    )
    result = subprocess.run(
        ["gh", "pr", "create",
         "--repo", WIKI_REPO,
         "--title", pr_title,
         "--body", pr_body,
         "--head", branch_name,
         "--base", "main"],
        cwd=WIKI_LOCAL_PATH,
        capture_output=True,
        text=True,
    )

    run_git(["checkout", "main"], cwd=WIKI_LOCAL_PATH)

    if result.returncode != 0:
        log.error(f"gh pr create failed: {result.stderr}")
        return None

    pr_url = result.stdout.strip()
    log.info(f"PR created: {pr_url}")
    return pr_url


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline():
    log.info("=== Bleeding Retro Wiki Pipeline — Starting ===")

    state = load_state()
    processed_msgs = set(state.get("processed_message_ids", []))
    processed_repos = set(state.get("processed_repos", []))

    try:
        token = get_discord_token()
    except RuntimeError as e:
        log.error(str(e))
        sys.exit(1)

    try:
        messages = fetch_recent_messages(token, MONITOR_CHANNEL_ID, limit=50)
    except requests.HTTPError as e:
        log.error(f"Failed to fetch Discord messages: {e}")
        sys.exit(1)

    repo_candidates = extract_github_repos(messages)
    log.info(f"Found {len(repo_candidates)} GitHub repo reference(s) in messages.")

    message_text_by_id = {m["id"]: m.get("content", "") for m in messages}

    new_work = []
    seen_repos_this_run = set()
    for msg_id, repo in repo_candidates:
        if msg_id in processed_msgs:
            log.debug(f"Skipping already-processed message {msg_id}")
            continue
        if repo in processed_repos:
            log.debug(f"Skipping already-processed repo {repo}")
            processed_msgs.add(msg_id)
            continue
        repo_key = repo.lower()
        if repo_key in seen_repos_this_run:
            log.debug(f"Skipping duplicate repo: {repo}")
            processed_msgs.add(msg_id)
            continue
        msg_text = message_text_by_id.get(msg_id, "")
        if not is_in_scope(repo, msg_text):
            log.warning(f"Skipping out-of-scope repo (7th gen+): {repo} (message {msg_id})")
            processed_msgs.add(msg_id)
            continue
        seen_repos_this_run.add(repo_key)
        new_work.append((msg_id, repo))

    if not new_work:
        log.info("No new repos to process. All caught up!")
        save_state(state)
        return

    log.info(f"Processing {len(new_work)} new repo(s)...")

    for msg_id, repo in new_work:
        log.info(f"--- Processing: {repo} (from message {msg_id}) ---")

        try:
            content = fetch_repo_content(repo)

            if not content["readme"] and not content["bom"]:
                log.warning(f"No useful content found for {repo}, skipping.")
                processed_msgs.add(msg_id)
                processed_repos.add(repo)
                continue

            # AI pre-check: confirm this targets 6th-gen or older hardware
            readme_preview = (content["readme"] or "")[:500]
            precheck_prompt = (
                f"Repo: {repo}\n\n"
                f"README (first 500 chars):\n{readme_preview}\n\n"
                "Is this mod/project targeting a 6th generation or older gaming console "
                "(PS2, GameCube, GBA, Dreamcast, N64, SNES, Genesis, etc. and older)? "
                "Reply with only YES or NO."
            )
            in_scope_ai = True
            reply = _call_openclaw_agent(precheck_prompt, timeout=60)
            if reply and reply.strip().upper().startswith("NO"):
                in_scope_ai = False

            if not in_scope_ai:
                log.warning(f"AI pre-check: {repo} is out of scope. Skipping.")
                processed_msgs.add(msg_id)
                processed_repos.add(repo)
                continue

            # Identify target console
            console_slug = identify_console(content)

            # Generate mod entry
            mod_entry = generate_mod_entry(content)
            if not mod_entry:
                log.warning(f"Could not generate mod entry for {repo}, skipping.")
                processed_msgs.add(msg_id)
                processed_repos.add(repo)
                continue

            # Append to console page
            page_path = append_mod_to_console_page(console_slug, mod_entry)

            # Derive mod slug from repo name
            mod_slug = slugify(repo.split("/")[-1])

            # Create PR
            pr_url = create_pr(console_slug, mod_slug, page_path, repo)

            # Notify Discord
            repo_url = f"https://github.com/{repo}"
            console_page = f"consoles/{console_slug}.mdx"

            if pr_url:
                notify_msg = (
                    f"🎮 **New mod entry added to wiki!**\n\n"
                    f"**Console page updated:** `{console_page}`\n"
                    f"**Mod source:** <{repo_url}>\n"
                    f"**PR:** {pr_url}\n\n"
                    f"<@{CHRIS_USER_ID}> — ready for your review! 👀"
                )
            else:
                notify_msg = (
                    f"⚠️ **Wiki mod entry generated but PR creation failed**\n\n"
                    f"**Console page:** `{console_page}`\n"
                    f"**Mod source:** <{repo_url}>\n"
                    f"Check the pipeline logs for details.\n\n"
                    f"<@{CHRIS_USER_ID}>"
                )

            try:
                post_discord_message(token, REVIEW_CHANNEL_ID, notify_msg)
            except requests.HTTPError as e:
                log.error(f"Failed to post Discord notification: {e}")

            processed_msgs.add(msg_id)
            processed_repos.add(repo)

        except Exception as e:
            log.error(f"Error processing {repo}: {e}", exc_info=True)

    state["processed_message_ids"] = list(processed_msgs)
    state["processed_repos"] = list(processed_repos)
    save_state(state)

    log.info("=== Pipeline complete ===")


if __name__ == "__main__":
    run_pipeline()
