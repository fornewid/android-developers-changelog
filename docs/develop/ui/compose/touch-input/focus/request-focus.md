---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus
url: https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus
source: md.txt
---

In some user flows, your application needs to explicitly move focus
to a specific component. For example, when a user clicks a "Search" button,
you might want to automatically place focus into the search input field.

## Use FocusRequester

To explicitly request focus:

1. Create and remember a [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester) instance: `val focusRequester = remember { FocusRequester() }`.
2. Attach the `FocusRequester` to the target composable using the [`focusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)) modifier.
3. Call [`requestFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester#requestFocus()) inside an event callback (such as `onClick`) or a coroutine scope.


```kotlin
val focusRequester = remember { FocusRequester() }
var text by remember { mutableStateOf("") }

TextField(
    value = text,
    onValueChange = { text = it },
    modifier = Modifier.focusRequester(focusRequester)
)
```

<br />


```kotlin
val focusRequester = remember { FocusRequester() }
var text by remember { mutableStateOf("") }

TextField(
    value = text,
    onValueChange = { text = it },
    modifier = Modifier.focusRequester(focusRequester)
)

Button(onClick = { focusRequester.requestFocus() }) {
    Text("Request focus on TextField")
}
```

<br />

> [!NOTE]
> **Note:** Always invoke `focusRequester.requestFocus()` inside event callbacks, side-effects (`LaunchedEffect`), or coroutines---never directly within the body of a composable function, which causes repeated execution on every recomposition.

## Set initial screen focus

To place initial focus on a specific component when a screen first appears,
trigger `requestFocus()` inside a `LaunchedEffect(Unit)`:

    LaunchedEffect(Unit) {
        focusRequester.requestFocus()
    }

When navigating between containers or returning from another screen,
you can also attach `focusRestorer()` to parent containers
to automatically return focus to the last focused child.
For more information, see the [Restore focus](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-restoration) guide.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)
- [Restore focus](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-restoration)
- [Move and clear focus](https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus)