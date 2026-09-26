---
title: https://developer.android.com/tools/agents/android-cli/commands/docs
url: https://developer.android.com/tools/agents/android-cli/commands/docs
source: md.txt
---

Searches and fetches developer documentation from the official Android Knowledge Base.

## Usage

    android docs [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`fetch`](https://developer.android.com/tools/agents/android-cli/commands/docs_fetch)** - Fetches an Android documentation article from a URL starting with `kb://`.
- **[`search`](https://developer.android.com/tools/agents/android-cli/commands/docs_search)** - Searches Android documentation. Enclose keywords in quotes.

## Description

The `android docs` command set provides two-step access to the official [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) directly from your terminal:

1. Run [`android docs search`](https://developer.android.com/tools/agents/android-cli/commands/docs_search) with a natural-language query or keywords to find matching documentation articles and their `kb://` URLs.
2. Run [`android docs fetch`](https://developer.android.com/tools/agents/android-cli/commands/docs_fetch) with a `kb://` URL returned by `search` to output the full Markdown content of the article to standard output.

### Examples

Search for articles about app performance and fetch a matching result:

    android docs search "How do I improve my app performance?"
    android docs fetch kb://android/topic/performance/overview