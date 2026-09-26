---
title: https://developer.android.com/tools/agents/android-cli/commands/skills
url: https://developer.android.com/tools/agents/android-cli/commands/skills
source: md.txt
---

Manages Android CLI skills. Includes commands to install, remove, list, and search for skills by keyword.

## Usage

    android skills [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`add`](https://developer.android.com/tools/agents/android-cli/commands/skills_add)** - Installs a specific skill by its ID to your environment.
- **[`find`](https://developer.android.com/tools/agents/android-cli/commands/skills_find)** - Searches for available skills in the repository matching a keyword.
- **[`list`](https://developer.android.com/tools/agents/android-cli/commands/skills_list)** - Lists installed and available skills.
- **[`remove`](https://developer.android.com/tools/agents/android-cli/commands/skills_remove)** - Removes an installed skill by its ID.
- **[`update`](https://developer.android.com/tools/agents/android-cli/commands/skills_update)** - Updates installed skills.

## Description

The `android skills` command set manages [Android skills](https://developer.android.com/tools/agents/android-skills)---curated instruction packages that teach AI coding agents how to follow official Android architecture, UI, and tooling best practices.

### Scope skills by agent or project

- `--agent`: Targets a comma-separated list of specific AI agents (for example, `gemini`, `claude`, or `codex`). When omitted, commands apply to all detected agent configurations on your machine.
- `--project`: Installs, updates, lists, or removes skills in a specific project root directory instead of your global user profile.