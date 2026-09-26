---
title: https://developer.android.com/tools/agents/android-cli/commands/skills_list
url: https://developer.android.com/tools/agents/android-cli/commands/skills_list
source: md.txt
---

Lists installed and available skills.

## Usage

    android skills list [-h] [--agent=PARAM] [--long] [--project=PARAM]

## Options

- `--agent=PARAM` - Comma-separated list of agents to list the installed skills for. If not specified, skills available for installation are listed.
- `-h,--help` - Shows the help message for the specified command.
- `--long` - Use long output format.
- `--project=PARAM` - Path to a project root.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android skills list` displays the available official Android skills and indicates which agents each skill is currently installed for.

Pass `--agent` to list all skills currently installed for the specified agents.

### Examples

List all available skills and their descriptions:

    android skills list --long

List only the skills installed for Gemini:

    android skills list --agent=gemini