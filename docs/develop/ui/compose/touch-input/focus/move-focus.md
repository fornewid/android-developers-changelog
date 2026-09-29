---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus
url: https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus
source: md.txt
---

[`FocusManager`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusManager) lets you move focus directionally or clear it entirely.
Use [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester) for direct component targeting (see [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)).

## Directional focus movement with FocusManager

To move focus programmatically in a relative direction:

1. Obtain the `FocusManager` instance using [`LocalFocusManager.current`](https://developer.android.com/reference/kotlin/androidx/compose/ui/platform/package-summary#LocalFocusManager()).
2. Call [`moveFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusManager#moveFocus(androidx.compose.ui.focus.FocusDirection)) with a [`FocusDirection`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusDirection) value (`Next`, `Previous`, `Up`, `Down`, `Left`, `Right`, `Enter`, or `Exit`).


```kotlin
val focusManager = LocalFocusManager.current

Button(
    onClick = {
        focusManager.moveFocus(FocusDirection.Next)
    }
) {
    Text("Next Field")
}
```

<br />

## Clear focus

To remove focus from whichever element currently holds it
(for example, when the user presses the <kbd>Esc</kbd> key),
call [`clearFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusManager#clearFocus(kotlin.Boolean)):


```kotlin
val focusManager = LocalFocusManager.current

Box(
    modifier = Modifier.onPreviewKeyEvent { keyEvent ->
        if (keyEvent.key == Key.Escape && keyEvent.type == KeyEventType.KeyUp) {
            focusManager.clearFocus()
            true
        } else {
            false
        }
    }
)
```

<br />

The `clearFocus()` function accepts an optional `force: Boolean = false`
parameter:

- **`force = false` (default)** : Respects focus locks and will not clear focus if the active component has [captured focus](https://developer.android.com/develop/ui/compose/touch-input/focus/capture-and-release-focus).
- **`force = true`**: Unconditionally clears focus even if a component has captured focus.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)