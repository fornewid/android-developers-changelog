---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus
url: https://developer.android.com/develop/ui/compose/touch-input/focus/react-to-focus
source: md.txt
---

Every time focus changes across the composition tree, Compose fires a focus
event that parent and child modifiers can observe. You can use the
[`onFocusChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).onFocusChanged(kotlin.Function1)) modifier to listen for focus state transitions, query current
focus properties, and trigger state-driven UI updates.

## Observe focus state with onFocusChanged

The [`onFocusChanged`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).onFocusChanged(kotlin.Function1)) modifier provides a [`FocusState`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusState) object whenever an
element gains or loses focus.

For example, you can observe focus changes to update custom component state
(such as changing an element's border color or triggering an animation):


```kotlin
var color by remember { mutableStateOf(Color.White) }
Card(
    modifier = Modifier
        .onFocusChanged {
            color = if (it.isFocused) Red else White
        }
        .border(5.dp, color)
) {}
```

<br />

In this example, `remember` stores the border color across recompositions, and
the border color updates whenever the element's focus state transitions.

> [!NOTE]
> **Note:** For standard Material 3 focus indications (such as ripples or focus rings), see [Indicate focus state](https://developer.android.com/develop/ui/compose/touch-input/focus/focused-state).

## FocusState properties

The [`FocusState`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusState) object passed to `onFocusChanged` provides three key
properties:

- **[`isFocused`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusState#isFocused())** : Returns `true` if the specific composable to which this modifier is attached currently holds active input focus.
- **[`hasFocus`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusState#hasFocus())** : Returns `true` if this composable or any of its child composables currently has focus. This is useful for parent containers (like cards or toolbars) that need to know when any child within them is active.
- **[`isCaptured`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusState#isCaptured())** : Returns `true` if focus is currently locked to the element (for example, during modal sub-interactions using `captureFocus()`). While captured, attempting to move focus to other elements don't clear focus.

    Modifier.onFocusChanged { focusState ->
        val isFocused = focusState.isFocused
        val hasFocus = focusState.hasFocus
        val isCaptured = focusState.isCaptured
    }

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Indicate focus state](https://developer.android.com/develop/ui/compose/touch-input/focus/focused-state)
- [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)
- [Capture and release focus](https://developer.android.com/develop/ui/compose/touch-input/focus/capture-and-release-focus)