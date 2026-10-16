---
title: https://developer.android.com/tools/agents/android-cli/commands/input_scroll
url: https://developer.android.com/tools/agents/android-cli/commands/input_scroll
source: md.txt
---

Scroll a container element, optionally until a target element appears.

## Usage

    android input scroll [-h] [--amount=PARAM] [--dir=PARAM] [--match=PARAM] [--speed=PARAM] [--until=PARAM] [--wait=PARAM] <target>

## Options

- `--amount=PARAM` - Scroll distance as fraction of container size (0.0 to 1.0).
- `--dir=PARAM` - Direction to scroll (up, down, left, right).
- `-h,--help` - Shows the help message for the specified command.
- `--match=PARAM` - Behavior when multiple elements match: 'single' (error on multiple matches) or 'first'.
- `--speed=PARAM` - Speed of each scroll gesture in pixels per second.
- `--until=PARAM` - Selector of target element to scroll until visible. Same syntax as .
- `--wait=PARAM` - Maximum duration to wait for the scroll target to appear in layout (ms).

`input` options:

- `--device=PARAM` - Device serial number or emulator ID (as reported by 'adb devices').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<target>` - Target container element selector to scroll

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