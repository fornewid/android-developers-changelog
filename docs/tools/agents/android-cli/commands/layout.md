---
title: https://developer.android.com/tools/agents/android-cli/commands/layout
url: https://developer.android.com/tools/agents/android-cli/commands/layout
source: md.txt
---

Returns the layout tree of an app.

## Usage

    android layout [-dhp] [--device=PARAM] [--flat] [--full] [--no-idle] [--output=PARAM]

## Options

- `--device=PARAM` - The device serial number.
- `-d,--diff` - Deprecated; no-op flag. Will be removed in a future release.
- `--flat` - Returns a flat list instead of a tree.
- `--full` - Returns the full tree, including non-interactive and hidden elements.
- `-h,--help` - Shows the help message for the specified command.
- `--no-idle` - Don't wait for layout idle state when fetching layout.
- `-o,--output=PARAM` - Writes the layout to the specified file or directory. If omitted, prints to standard output.
- `-p,--pretty` - Pretty-prints the returned JSON.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android layout` captures the live UI hierarchy of the active screen on a connected Android device or emulator and outputs it in JSON format.

AI agents and test scripts can use `android layout` to inspect visible text, resource IDs, accessibility descriptions, interaction states, and element bounds without relying solely on visual screenshots.

### Format and filter layout output

- `-p, --pretty`: Formats the JSON output with indentation and line breaks for human readability.
- `-o, --output`: Writes the layout JSON to the specified file path instead of standard output.
- `--flat`: Outputs a flat JSON list of UI nodes instead of a nested hierarchy tree.
- `--full`: Includes non-interactive and hidden UI elements that are filtered out by default.
- `--no-idle`: Captures the layout immediately without waiting for the app UI thread to reach an idle state.

### Examples

Print the pretty-formatted UI layout tree of the active screen:

    android layout --pretty

Save the full UI hierarchy (including non-interactive elements) to a file:

    android layout --pretty --full --output=./hierarchy.json