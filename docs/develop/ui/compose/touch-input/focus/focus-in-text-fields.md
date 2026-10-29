---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields
source: md.txt
---

When users navigate a Compose UI with a hardware keyboard, D-pad, or rotary
controller, text fields participate in focus navigation alongside other focus
targets.

By default, focus isn't trapped in text fields. You don't need to add custom
key event handlers (`onKeyEvent` or `onPreviewKeyEvent`) to allow users to leave
a text field. Users can always escape using <kbd>Shift+Tab</kbd> or by navigating past
the text boundaries with directional keys.

[`KeyboardOptions`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/KeyboardOptions) can be used to provide an intuitive software keyboard
action that coordinates with hardware keyboard navigation.
[`ImeAction.Next`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/input/ImeAction#Next()) moves focus to the next focus target, for example.

## One-dimensional focus traversal

In one-dimensional focus traversal,
the behavior of the <kbd>Tab</kbd> key depends on the
`lineLimits` configured on the text field:

- **Single-line text fields ([`TextFieldLineLimits.SingleLine`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldLineLimits.SingleLine))** Pressing the <kbd>Tab</kbd> key moves focus to the next focus target in the UI.
- **Multi-line text fields ([`TextFieldLineLimits.MultiLine`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldLineLimits.MultiLine)`()` or
  default)** : Pressing the <kbd>Tab</kbd> key inserts a tab character (`\t`) into the text buffer instead of moving focus.
- **Reverse navigation (<kbd>Shift+Tab</kbd>)** : Pressing <kbd>Shift+Tab</kbd> unconditionally moves focus backward to the previous focus target in both single-line and multi-line text fields.


```kotlin
// Single-line text field: Tab advances focus to the next focus target
BasicTextField(
    state = singleLineState,
    lineLimits = TextFieldLineLimits.SingleLine,
    modifier = Modifier.fillMaxWidth()
)

// Multi-line text field: Tab inserts '\t'; Shift + Tab moves to previous target
BasicTextField(
    state = multiLineState,
    lineLimits = TextFieldLineLimits.MultiLine(),
    modifier = Modifier.fillMaxWidth()
)
```

<br />

## Two-dimensional focus traversal

When using arrow keys (or a D-pad),
directional keys first move the text cursor (caret)
within the text field:

- **Vertical navigation (up / down)** : Pressing the `Down` key moves the caret downward line by line. When the caret reaches the last line, pressing the <kbd>Down</kbd> key again transfers focus to the adjacent focus target below the text field. Pressing the <kbd>Up</kbd> key on the first line moves focus to the preceding focus target.
- **Horizontal navigation (left / right / start / end)**: Pressing horizontal arrow keys moves the caret through the characters. When the caret reaches the start or end of the text buffer, pressing the directional key again transfers focus to the adjacent focus target in that direction.

## Text fields on Android TV

On Android TV, using D-pad controllers without a physical keyboard:

1. Moving focus to a text field automatically displays the on-screen software keyboard.
2. The user navigates the keys of the software keyboard using the D-pad.
3. Pressing the **Back** button dismisses the software keyboard while preserving focus on the text field.
4. Once the software keyboard is dismissed, pressing D-pad directional keys moves focus to neighboring focus targets on the screen.
5. Pressing the **Back** button a second time triggers standard system back navigation.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)
- [Test focus navigation](https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus)