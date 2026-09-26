---
title: https://developer.android.com/tools/agents/android-cli/commands/skills_remove
url: https://developer.android.com/tools/agents/android-cli/commands/skills_remove
source: md.txt
---

Removes an installed skill by its ID.

## Usage

    android skills remove [-h] [--agent=PARAM] [--project=PARAM] [<skill>]

## Options

- `--agent=PARAM` - Comma-separated list of agents to remove the skill for. If not specified, skills are removed for all detected agents.
- `-h,--help` - Shows the help message for the specified command.
- `--project=PARAM` - Path to a project root.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<skill>` - The name of the skill to remove.

## Description

`android skills remove` uninstalls one or more skills from your AI agent skill directories.

If `--agent` is omitted, the specified skill is removed from all detected agents.

### Examples

Remove the `edge-to-edge` skill from all detected agents:

    android skills remove edge-to-edge

Remove the `edge-to-edge` skill only from Gemini:

    android skills remove --agent=gemini edge-to-edge