---
title: https://developer.android.com/tools/agents/android-cli/commands/input
url: https://developer.android.com/tools/agents/android-cli/commands/input
source: md.txt
---

Interact with Android apps by performing gestures and key events on UI elements.

## Usage

    android input [-h] [--device=PARAM]

## Options

- `--device=PARAM` - Device serial number or emulator ID (as reported by 'adb devices').
- `-h,--help` - Shows the help message for the specified command.

`android` options:

- `--sdk=PARAM` - Path to the Android SDK.
- `-v,--verbose` - Enable verbose output for troubleshooting.
- `-V,--version` - Print version information and exit.

## Subcommands

- **[`key`](https://developer.android.com/tools/agents/android-cli/commands/input_key)** - Press a hardware button, navigation key, or Android keycode.
- **[`scroll`](https://developer.android.com/tools/agents/android-cli/commands/input_scroll)** - Scroll a container element, optionally until a target element appears.
- **[`swipe`](https://developer.android.com/tools/agents/android-cli/commands/input_swipe)** - Swipe from a UI element matching a selector in a given direction.
- **[`tap`](https://developer.android.com/tools/agents/android-cli/commands/input_tap)** - Tap on a UI element matching a selector.
- **[`text`](https://developer.android.com/tools/agents/android-cli/commands/input_text)** - Type text into a UI element matching a selector.

## Description

`android input` performs user interactions and hardware inputs on a connected
Android device or emulator.

AI agents and test scripts can use `android input` in combination with
\[`android layout`\]\[layout\] or \[`android screen`\]\[screen\] to discover UI elements
and interact with them via gestures or keystrokes.

### UI element selectors

Most `input` subcommands target UI elements using a selector expression. A
selector is a comma-separated list of `key=value` or `key:value` pairs
specifying properties that a target element must satisfy. Enclose selectors in
single quotes to prevent shell interpretation of spaces, commas, or special
characters.

Selectors match against the app's live accessibility node hierarchy:

- **String properties** : Matched as case-insensitive substrings by default. Pass `*` to match any element with a non-empty value for that property.
  - `text` (synonym: `txt`): The visible text displayed on the element.
  - `id` (synonym: `res`): The view resource ID name (for example, `id=submit_button` or the full resource name `com.example.app:id/submit_button`).
  - `class` (synonyms: `clazz`, `cls`, `clz`): The element class name or simple class name (such as `class=Button` or `android.widget.Button`).
  - `desc` (synonym: `content`): The accessibility content description.
- **Interaction properties** : Matched as boolean values (`true` or `false`).
  - `clickable` (synonym: `click`): Whether the element can be clicked.
  - `checkable`: Whether the element can be checked or toggled.
  - `scrollable` (synonym: `scroll`): Whether the element is a scrollable container.
  - `focusable`: Whether the element can receive focus.
  - `longclickable` (synonym: `longclick`): Whether the element supports long clicks.
- **State properties** : Matched as boolean values (`true` or `false`).
  - `checked`: Whether the element is currently checked.
  - `focused`: Whether the element currently has focus.
  - `selected`: Whether the element is currently selected.

### Match behavior (`--match`)

When a selector matches more than one element on the screen:

- `--match=single` (default): Fails with an error and lists all matching elements, ensuring interactions do not trigger the wrong UI component.
- `--match=first`: Interacts with the first matching element encountered in the UI hierarchy.

### Available gestures and commands

- **`tap <target>`**: Clicks the center of the targeted element.
- **`text <string> <target>`** : Clears existing text and types `<string>` into the targeted element. Pass `--submit` to send an Enter/OK key event after typing.
- **`scroll <target>`** : Scrolls a container element in a specified direction (`--dir=up|down|left|right`). Use `--until=<selector>` to keep scrolling until a matching element appears.
- **`swipe <target>`** : Performs a swipe gesture starting from `<target>` in a direction (`--dir=up|down|left|right`), with optional `--distance` (fraction of screen) and `--speed` (pixels per second).
- **`key <key>`** : Sends a hardware button or key event (such as `back`, `home`, `recents`, `power`, `volume-up`, `volume-down`, `enter`, `tab`, `esc`, or an integer Android keycode). Supports modifier flags `--shift`, `--alt`, and `--ctrl`.

### Specify a target device (`--device`)

If multiple devices or emulators are connected, pass `--device=<serial-number>`
(as reported by `adb devices`) to direct input events to a specific device.

### Examples

Tap a button by its visible text:

    android input tap 'text=Submit'

Tap an element matching multiple properties:

    android input tap 'id=submit_btn,class=Button,clickable=true'

Tap the first matching element when multiple matches exist:

    android input tap --match=first 'class=android.widget.TextView'

Type text into an input field and submit:

    android input text 'user@example.com' 'id=email_input' --submit

Scroll a container down until an item appears:

    android input scroll 'id=recycler_view' --dir=down --until='text=Settings'

Swipe left on a card element:

    android input swipe 'id=card_view' --dir=left

Press the device Back button:

    android input key back