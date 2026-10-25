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
matching accessibility node properties. You can also write key:value.
For example, text=search,clz=EditText,clickable=true targets clickable EditText
elements containing the text 'search'

Supported string fields:
- text (or txt) for visible text
- id (or res) for view resource ID
- class (or clazz, cls, clz) for element class name
- desc (or content) for accessibility content description

Supported boolean fields (true or false):
- clickable (or click)
- scrollable (or scroll)
- checkable
- focusable
- longclickable (or longclick)
- checked
- focused
- selected

Note that string selectors match as case-insensitive substrings by default. The
selector txt=var would match "var", "Variable", and "There was significant
variance". The selector txt=\* matches any non-empty value. Spaces around a value
are ignored, except inside a regular expression.
Wrap a value in slashes to use a regular expression instead. Regular expressions
are case-sensitive and can match any part of the value. For example, txt=/\^Var$/
matches only "Var". Add the i flag for a case-insensitive match, for example
txt=/\^var$/i. Escape a "/" inside a regular expression as "\\/", for example
id=/:id\\/submit$/. Commas and spaces inside a regular expression are part of it,
for example txt=/\^Item \[0-9\]{1,2}$/. A value that starts with "/" is always a
regular expression, so use txt=/\^\\/help/ to match text that starts with "/help"