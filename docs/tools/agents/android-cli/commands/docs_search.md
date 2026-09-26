---
title: https://developer.android.com/tools/agents/android-cli/commands/docs_search
url: https://developer.android.com/tools/agents/android-cli/commands/docs_search
source: md.txt
---

Searches Android documentation. Enclose keywords in quotes.

## Usage

    android docs search [-h] <query>

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<query>` - The query to search the documentation for. Enclose keywords in quotes.

## Description

`android docs search` queries the official [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) and returns a ranked list of matching documentation articles along with their `kb://` URLs.

Pass any `kb://` URL from the search results to [`android docs fetch`](https://developer.android.com/tools/agents/android-cli/commands/docs_fetch) to read the full article in your terminal.

### Examples

Search for documentation on Jetpack Compose navigation:

    android docs search "Jetpack Compose navigation"

Search for guidance on improving app startup performance:

    android docs search "How do I improve my app performance?"