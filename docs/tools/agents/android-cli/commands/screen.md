---
title: https://developer.android.com/tools/agents/android-cli/commands/screen
url: https://developer.android.com/tools/agents/android-cli/commands/screen
source: md.txt
---

Captures and inspects the screen of a connected Android device or emulator.

## Usage

    android screen [-h]

## Options

- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`capture`](https://developer.android.com/tools/agents/android-cli/commands/screen_capture)** - Outputs the device screen to a PNG.
- **[`resolve`](https://developer.android.com/tools/agents/android-cli/commands/screen_resolve)** - Targets UI elements visually. Substitutes bounding box coordinates from an annotated screenshot into a string, replacing all instances of `#N` with the center coordinates of the bounding box labeled `N`.

## Description

The `android screen` command set captures screenshots from a connected Android device or emulator and provides computer-vision annotations so AI agents and scripts can visually target UI elements.

### Target UI elements visually

Here is the sequence of commands for visually targeting UI elements:

1. Run [`android screen capture --annotate --output=ui.png`](https://developer.android.com/tools/agents/android-cli/commands/screen_capture) to capture the active device screen with numbered bounding boxes drawn around detected UI elements.
2. Inspect `ui.png` to identify the label number (`#N`) of the UI element you want to interact with.
3. Run [`android screen resolve --screenshot=ui.png --string="input tap #N"`](https://developer.android.com/tools/agents/android-cli/commands/screen_resolve) to substitute `#N` with the exact `(x, y)` center coordinates of that bounding box.