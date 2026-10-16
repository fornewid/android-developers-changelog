---
title: https://developer.android.com/tools/agents/android-cli/commands/input_swipe
url: https://developer.android.com/tools/agents/android-cli/commands/input_swipe
source: md.txt
---

Swipe from a UI element matching a selector in a given direction.

## Usage

    android input swipe [-h] [--dir=PARAM] [--distance=PARAM] [--match=PARAM] [--speed=PARAM] [--wait=PARAM] <target>

## Options

- `--dir=PARAM` - Direction to swipe: up, down, left, right.
- `--distance=PARAM` - Swipe distance as fraction of screen size (0.0 to 1.0).
- `-h,--help` - Shows the help message for the specified command.
- `--match=PARAM` - Behavior when multiple elements match: 'single' (error on multiple matches) or 'first'.
- `--speed=PARAM` - Speed of swipe in pixels per second.
- `--wait=PARAM` - Maximum duration to wait for the target element to appear in layout (ms).

`input` options:

- `--device=PARAM` - Device serial number or emulator ID (as reported by 'adb devices').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<target>` - Target UI element selector to swipe from

Target UI elements using selectors composed of comma-separated key=value pairs
matching accessibility node properties.
For example, text=search,clz=EditText,clickable=true targets clickable EditText
elements containing the text 'search'

Supported string fields:
- text (or txt) for visible text
- id (or res) for view resource ID
- class (or clz) for element class name
- desc (or content) for accessibility content description

Supported boolean fields (true or false):
- clickable
- scrollable
- checkable
- focusable
- longclickable
- checked
- focused
- selected

Note that string selectors match as case-insensitive substrings. The selector
txt=var would match "var", "Variable", and "There was significant variance"