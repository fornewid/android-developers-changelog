---
title: https://developer.android.com/tools/agents/android-cli/commands/docs_fetch
url: https://developer.android.com/tools/agents/android-cli/commands/docs_fetch
source: md.txt
---

Fetches an Android documentation article from a URL starting with `kb://`.

## Usage

    android docs fetch [-h] <url>

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<url>` - The specific URL of the documentation article to fetch. You can find available URLs by running [`android docs search <query>`](https://developer.android.com/tools/agents/android-cli/commands/docs_search) first.

## Description

`android docs fetch` downloads and prints the full content of an article from the [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources) using its `kb://` URL.

To discover valid `kb://` URLs, run [`android docs search <query>`](https://developer.android.com/tools/agents/android-cli/commands/docs_search) first.

### Examples

Fetch the performance overview article from the Android Knowledge Base:

    android docs fetch kb://android/topic/performance/overview