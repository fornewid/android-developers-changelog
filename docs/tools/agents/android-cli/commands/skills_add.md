---
title: https://developer.android.com/tools/agents/android-cli/commands/skills_add
url: https://developer.android.com/tools/agents/android-cli/commands/skills_add
source: md.txt
---

Installs a specific skill by its ID to your environment.

## Usage

    android skills add [-h] [--agent=PARAM] [--all] [--project=PARAM] [<skill>]

## Options

- `--agent=PARAM` - Comma-separated list of agents to install the skill for. If not specified, skills are installed for all detected agents.
- `--all` - Install all skills.
- `-h,--help` - Shows the help message for the specified command.
- `--project=PARAM` - Path to a project root.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<skill>` - The name of the skill to install.

## Description

`android skills add` downloads and installs one or more [Android skills](https://developer.android.com/tools/agents/android-skills) into the skill directories of your AI coding agents.

If no existing agent directories are detected and `--agent` is omitted, skills are installed by default for Gemini and Antigravity at `~/.gemini/antigravity/skills`. If a skill is already installed, `android skills add` updates it to the latest version.

> [!NOTE]
> **Note:** If you customize an installed skill, rename its directory so that future runs of `android skills add` or `android skills update` do not overwrite your changes.

### Configure installation options

- `--all`: Installs or updates all available official Android skills at once.
- `--agent`: Comma-separated list of agents to install the skill for (for example, `gemini`, `claude`, or `codex`).
- `--project`: Installs the skill into the specified project directory rather than globally.

### Examples

Install the `edge-to-edge` skill for Gemini:

    android skills add --agent=gemini edge-to-edge

Install all official Android skills for all detected agents:

    android skills add --all