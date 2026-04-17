# PostPilot Project Documentation

## 1) Project Overview

`PostPilot` is a Python CLI automation tool that discovers trending tech stories and turns them into LinkedIn-ready draft posts using OpenAI.

The current product is **human-in-the-loop**:
- it generates content automatically,
- then asks the user to approve, skip, or rewrite each draft,
- and saves approved drafts to local storage.

---

## 2) Project Goals

- Reduce time spent writing social content.
- Keep posts relevant by sourcing trending tech topics.
- Preserve quality through manual approval before saving.

---

## 3) Repository Structure

```text
postpilot/
├─ main.py
├─ generator/
│  └─ post_generator.py
├─ scrapers/
│  └─ reddit_scraper.py
├─ storage/
│  └─ posts.json
├─ README.md
├─ .gitignore
└─ .env  (not documented here by design)
```

### File Roles

- `main.py`
  - Main orchestrator.
  - Runs scraping, generation, decision loop, and saving.

- `generator/post_generator.py`
  - Builds prompt and calls OpenAI (`gpt-4o-mini`) to generate LinkedIn text.

- `scrapers/reddit_scraper.py`
  - Fetches top stories from **Hacker News API** (despite filename).

- `storage/posts.json`
  - Local persistent store of approved generated posts.

- `README.md`
  - Project intro, setup notes, and high-level stack.

---

## 4) Runtime Workflow

1. **Agent starts** from `main.py`.
2. **Scraper fetches trending stories** (default limit: 5) from Hacker News.
3. **Generator creates LinkedIn draft** for each story with style constraints.
4. **User makes decision**:
   - `y` = approve and save
   - `n` = skip
   - `r` = rewrite once, then optional save
5. **Approved drafts are appended** to `storage/posts.json` with metadata.
6. **Session ends** after processing all fetched stories.

---

## 5) Data Model (Current)

Each saved post in `storage/posts.json` includes:

- `source_title` (string)
- `source_url` (string)
- `content` (string)
- `approved_at` (datetime string)
- `status` (currently `"approved"`)

---

## 6) Prompting & Content Rules

The generator enforces these output guidelines:

- Start with a strong hook.
- Do not start with `"I"`.
- Keep length around 150-200 words.
- End with a question to encourage comments.
- Add 3 relevant hashtags.
- Tone should sound human.

---

## 7) Scope Definition

### In Scope (Now)

- CLI-based content generation.
- Hacker News as source feed.
- Manual review/approval loop.
- Local JSON persistence.

### Out of Scope (Now)

- Direct auto-posting to LinkedIn.
- Scheduling/calendar workflows.
- UI/web dashboard.
- Database storage.
- Multi-source aggregation (Reddit/X/RSS/etc.).
- Automated quality scoring or moderation pipeline.

---

## 8) Current Limitations / Risks

- **Module naming mismatch**: `reddit_scraper.py` actually handles Hacker News.
- **README dependency mismatch**: mentions `praw`, but current scraper uses `requests` + Hacker News endpoints.
- **No robust error handling** for:
  - network failures,
  - API timeouts,
  - malformed responses,
  - missing API key.
- **Execution guard missing**: `run_agent()` executes on import; safer pattern is `if __name__ == "__main__":`.
- **No tests** to validate scraper behavior, generation flow, or persistence logic.

---

## 9) Recommended Next Steps

1. Add `if __name__ == "__main__":` guard in `main.py`.
2. Rename `scrapers/reddit_scraper.py` to `hackernews_scraper.py`.
3. Align `README.md` with actual implementation and dependencies.
4. Add basic error handling + request timeouts.
5. Add `requirements.txt` (or `pyproject.toml`) for reproducible setup.
6. Add minimal tests for:
   - scraper output shape,
   - save logic,
   - decision-loop paths.

---

## 10) Quick Operational Summary

`PostPilot` is a good MVP for AI-assisted social content creation:
- simple architecture,
- practical human approval step,
- working local persistence.

The next maturity step is reliability (error handling/testing) and naming/docs consistency.
