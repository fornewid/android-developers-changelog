---
title: https://developer.android.com/tools/agents/android-cli/commands/input_text
url: https://developer.android.com/tools/agents/android-cli/commands/input_text
source: md.txt
---

Type text into a UI element matching a selector.

## Usage

    android input text [-h] [--match=PARAM] [--submit] [--wait=PARAM] <string> <selector>

## Options

- `-h,--help` - Shows the help message for the specified command.
- `--match=PARAM` - Behavior when multiple elements match: 'single' (error on multiple matches) or 'first'.
- `--submit` - Press Enter/OK key after entering text.
- `--wait=PARAM` - Maximum duration to wait for the target element to appear in layout (ms).

`input` options:

- `--device=PARAM` - Device serial number or emulator ID (as reported by 'adb devices').

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Positional arguments

- `<string>` - Text string to type into the target element (replaces existing text).
- `<selector>` - Target input element selector of comma-separated key=value pairs

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