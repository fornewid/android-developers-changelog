---
title: https://developer.android.com/tools/agents/android-cli/commands/preview_list
url: https://developer.android.com/tools/agents/android-cli/commands/preview_list
source: md.txt
---

Lists available Jetpack Compose @Preview functions in a target.

## Usage

    android preview list [-h] [--all] [--format=PARAM] [<reference>] [-- <build_args>]

## Options

- `--all` - Include previews from dependent modules in the workspace (excludes .gradle, third_party, and external directories).
- `-f,--format=PARAM` - Output format ('text' or 'json'; default: 'text').
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<reference>` - Build reference (\[system://\]\[path\]?\[target\]).
- `-- <build_args>` - Arguments passed verbatim to the build system. Use -- to separate from other arguments.

## Description

`android preview list` compiles the target and scans its classpath for Jetpack
Compose `@Preview` functions (including custom MultiPreview annotations),
printing their fully qualified names to standard output.

Pass a build reference (`[system://][path]?[target]`) to select the workspace
and target to inspect, or omit `<reference>` to use the default target in the
current workspace.

### Filter and format preview list output

- `--all`: Includes `@Preview` functions from dependent targets in the workspace (excluding `.gradle`, `third_party`, and `external` directories).
- `-f, --format`: Selects `text` (default, one fully qualified method name per line) or structured `json` output.

### Examples

List `@Preview` functions in `:app` in the current Gradle workspace:

    android preview list :app

List `@Preview` functions across `:app` and its workspace dependencies in JSON
format:

    android preview list :app --all --format=json