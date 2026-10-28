---
title: Focus in text fields  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Focus in text fields Stay organized with collections Save and categorize content based on your preferences.





When users navigate a Compose UI with a hardware keyboard, D-pad, or rotary
controller, text fields participate in focus navigation alongside other focus
targets.

By default, focus isn't trapped in text fields. You don't need to add custom
key event handlers (`onKeyEvent` or `onPreviewKeyEvent`) to allow users to leave
a text field. Users can always escape using `Shift+Tab` or by navigating past
the text boundaries with directional keys.

[`KeyboardOptions`](/reference/kotlin/androidx/compose/foundation/text/KeyboardOptions) can be used to provide an intuitive software keyboard
action that coordinates with hardware keyboard navigation.
[`ImeAction.Next`](/reference/kotlin/androidx/compose/ui/text/input/ImeAction#Next()) moves focus to the next focus target, for example.

## One-dimensional focus traversal

In one-dimensional focus traversal,
the behavior of the `Tab` key depends on the
`lineLimits` configured on the text field:

* **Single-line text fields ([`TextFieldLineLimits.SingleLine`](/reference/kotlin/androidx/compose/foundation/text/input/TextFieldLineLimits.SingleLine))**
  Pressing the `Tab` key moves focus to
  the next focus target in the UI.
* **Multi-line text fields ([`TextFieldLineLimits.MultiLine`](/reference/kotlin/androidx/compose/foundation/text/input/TextFieldLineLimits.MultiLine)`()` or
  default)**:
  Pressing the `Tab` key inserts a tab character (`\t`) into
  the text buffer instead of moving focus.
* **Reverse navigation (`Shift+Tab`)**:
  Pressing `Shift+Tab` unconditionally moves focus backward
  to the previous focus target
  in both single-line and multi-line text fields.

```
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

FocusInTextFields.kt
```

## Two-dimensional focus traversal

When using arrow keys (or a D-pad),
directional keys first move the text cursor (caret)
within the text field:

* **Vertical navigation (up / down)**:
  Pressing the `Down` key moves the caret downward line by line.
  When the caret reaches the last line,
  pressing the `Down` key again transfers focus
  to the adjacent focus target below the text field.
  Pressing the `Up` key on the first line moves focus
  to the preceding focus target.
* **Horizontal navigation (left / right / start / end)**:
  Pressing horizontal arrow keys moves the caret
  through the characters.
  When the caret reaches the start or end of the text buffer,
  pressing the directional key again transfers
  focus to the adjacent focus target in that direction.

## Text fields on Android TV

On Android TV, using D-pad controllers without a physical keyboard:

1. Moving focus to a text field automatically displays
   the on-screen software keyboard.
2. The user navigates the keys of the software keyboard
   using the D-pad.
3. Pressing the **Back** button dismisses the software keyboard
   while preserving focus on the text field.
4. Once the software keyboard is dismissed,
   pressing D-pad directional keys moves focus to
   neighboring focus targets on the screen.
5. Pressing the **Back** button a second time triggers
   standard system back navigation.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Focus targets](/develop/ui/compose/touch-input/focus/focus-target)
* [Focus traversal order](/develop/ui/compose/touch-input/focus/focus-traversal)
* [Group focus targets](/develop/ui/compose/touch-input/focus/focus-group)
* [Test focus navigation](/develop/ui/compose/touch-input/focus/testing-focus)

[Previous

arrow\_back

Focus traversal order](/develop/ui/compose/touch-input/focus/focus-traversal)

[Next

Group focus targets

arrow\_forward](/develop/ui/compose/touch-input/focus/focus-group)