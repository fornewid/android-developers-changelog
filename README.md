# Android Developers Changelog

This project tracks changes to the Android Developers documentation sitemap and generates a changelog using Gemini.

## Setup

1.  Install dependencies:
    ```bash
    pip install -r scripts/requirements.txt
    ```

2.  Set up environment variables:
    - Copy `.env.example` to `.env` (if needed, but mainly for `GEMINI_API_KEY` in local dev).
    - `GEMINI_API_KEY` is required for summarization.

3.  Run the fetcher:
    ```bash
    python scripts/fetch_android_docs.py
    ```

4.  Summarize changes (usually run by CI, but can be run locally):
    ```bash
    python scripts/summarize_android_changes.py --files M:docs/some_file.md
    ```

## Structure
- `scripts/`: Python scripts for fetching and summarizing.
- `docs/`: Fetched documentation (Markdown converted from HTML).
- `pages/`: Generated changelog JSON and diffs.
- `.github/workflows/`: Automation.
