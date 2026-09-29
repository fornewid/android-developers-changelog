---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/capture-and-release-focus
url: https://developer.android.com/develop/ui/compose/touch-input/focus/capture-and-release-focus
source: md.txt
---

In specialized interaction modes (such as an embedded drawing canvas, game
controller surface, or modal input dialog), your app might need to temporarily
lock focus to a single component and prevent <kbd>Tab</kbd>
or directional keys from navigating away.

> [!WARNING]
> **Warning:** Capturing focus can cause accessibility issues. Users might not be able to navigate to other focusable components.

## Capture focus

To capture focus, invoke [`captureFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.focus.FocusRequesterModifierNode).captureFocus()) on a [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester):


```kotlin
val focusRequester = remember { FocusRequester() }

Box(
    modifier = Modifier
        .focusRequester(focusRequester)
        .focusable()
        .onFocusChanged { focusState ->
            if (focusState.isFocused) {
                focusRequester.captureFocus()
            }
        }
)
```

<br />

> [!IMPORTANT]
> **Key Point:** The target component must already hold active focus (`isFocused == true`) when calling `captureFocus()`. Invoking `captureFocus()` on an unfocused element returns `false` and fails to capture focus.

While focus is captured, standard focus navigation keys (such as <kbd>Tab</kbd>)
don't move focus to neighboring components.

## Release focus

To exit the captured state and restore normal focus navigation across the UI,
call [`freeFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.focus.FocusRequesterModifierNode).freeFocus()):


```kotlin
IconButton(
    onClick = {
        focusRequester.freeFocus()
    }
) {
    Icon(Icons.Default.Close, contentDescription = "Exit focus lock")
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)
- [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)