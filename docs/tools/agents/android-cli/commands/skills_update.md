---
title: https://developer.android.com/tools/agents/android-cli/commands/skills_update
url: https://developer.android.com/tools/agents/android-cli/commands/skills_update
source: md.txt
---

Updates installed skills.

## Usage

    android skills update [-h] [--agent=PARAM] [--all] [--project=PARAM] [<skill>]

## Options

- `--agent=PARAM` - Comma-separated list of agents to update the skill for. If not specified, skills are updated for all detected agents.
- `--all` - Update all installed skills.
- `-h,--help` - Shows the help message for the specified command.
- `--project=PARAM` - Path to a project root.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<skill>` - The name of the skill to update.

## Description

`android skills update` updates installed Android skills to their latest published versions.

Specify one or more `<skill>` names to update specific skills, or pass `--all` to update all installed skills across your configured agents.

### Examples

Update all installed skills for all detected agents:

    android skills update --all

Update only the `edge-to-edge` skill for Gemini:

    android skills update --agent=gemini edge-to-edge