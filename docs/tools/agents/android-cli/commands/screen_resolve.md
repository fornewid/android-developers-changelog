---
title: https://developer.android.com/tools/agents/android-cli/commands/screen_resolve
url: https://developer.android.com/tools/agents/android-cli/commands/screen_resolve
source: md.txt
---

Targets UI elements visually. Substitutes bounding box coordinates from an annotated screenshot into a string, replacing all instances of `#N` with the center coordinates of the bounding box labeled `N`.

## Usage

    android screen resolve [-h] [--screenshot=PARAM] [--string=PARAM]

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--screenshot=PARAM` - A screenshot captured with `android screen capture --annotate`.
- `--string=PARAM` - The string to substitute coordinates into.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Description

`android screen resolve` translates visual label placeholders (`#N`) from an annotated screenshot (captured with [`android screen capture --annotate`](https://developer.android.com/tools/agents/android-cli/commands/screen_capture)) into their corresponding screen center coordinates (`x y`).

This enables AI agents and automation scripts to generate `adb shell input` commands (such as taps and swipes) by referencing numbered labels from the annotated image instead of manually calculating pixel coordinates.

### Examples

If label `5` in `ui.png` is centered at coordinates `(500, 1000)`, running:

    android screen resolve --screenshot=ui.png --string="input tap #5"

outputs `input tap 500 1000`.