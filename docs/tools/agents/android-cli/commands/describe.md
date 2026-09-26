---
title: https://developer.android.com/tools/agents/android-cli/commands/describe
url: https://developer.android.com/tools/agents/android-cli/commands/describe
source: md.txt
---

Analyzes an Android project to generate descriptive metadata. This command identifies and outputs the paths to JSON files that detail the project's structure, including build targets and their corresponding output artifact locations (such as APKs). This information enables other tools and commands to locate build artifacts efficiently.

## Usage

    android describe [-h] [--project_dir=PARAM]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--project_dir=PARAM` - The project directory to describe.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android describe` inspects an Android project and outputs the project's modules, variants, build targets, and output artifact paths (such as compiled APK files or redirect files).

AI agents and automation scripts can use `android describe` to discover where build outputs are located before deploying them with [`android install`](https://developer.android.com/tools/agents/android-cli/commands/install) or [`android run`](https://developer.android.com/tools/agents/android-cli/commands/run).

### Specify a project directory (`--project_dir`)

If `--project_dir` is omitted, `android describe` analyzes the project in the current working directory.

### Examples

Describe the Android project in the current working directory:

    android describe

Describe an Android project in a specific directory:

    android describe --project_dir=/path/to/your/project