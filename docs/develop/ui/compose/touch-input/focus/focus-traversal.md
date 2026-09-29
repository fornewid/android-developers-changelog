---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal
source: md.txt
---

Users can move keyboard focus across UI elements
using the <kbd>Tab</kbd> key or directional (arrow / D-pad) keys:

- <kbd>Tab</kbd> / <kbd>Shift+Tab</kbd>: Move focus forward or backward in one-dimensional appearance order.
- Directional keys: Move focus two-dimensionally (<kbd>Up</kbd>, <kbd>Down</kbd>, <kbd>Left</kbd>, and <kbd>Right</kbd>).

## One-dimensional focus traversal

In one-dimensional focus traversal,
the <kbd>Tab</kbd> key advances focus through the UI based on
the visual **appearance order** on the screen.

For example, when four buttons are arranged in rows:


```kotlin
Column {
    Row {
        Button(onClick = { /* ... */ }) { Text("1st") }
        Button(onClick = { /* ... */ }) { Text("2nd") }
    }
    Row {
        Button(onClick = { /* ... */ }) { Text("3rd") }
        Button(onClick = { /* ... */ }) { Text("4th") }
    }
}
```

<br />

Pressing the <kbd>Tab</kbd> key moves focus sequentially across
the buttons in the following order:

1. **1st button** (top-start)
2. **2nd button** (top-end)
3. **3rd button** (bottom-start)
4. **4th button** (bottom-end)

Pressing <kbd>Tab</kbd> on the final element wraps back
to the first focus target.
Pressing <kbd>Shift+Tab</kbd> moves focus in reverse order.

## Two-dimensional focus traversal

Pressing keyboard arrow keys or
using a [D-pad](https://developer.android.com/training/tv/get-started/navigation#controllers) triggers two-dimensional focus traversal.

In two-dimensional traversal,
the system inspects the geometric coordinates and
spatial boundaries of UI elements
to determine the closest target in the requested direction.

Two-dimensional focus traversal **does not wrap around** .
If the user presses the <kbd>Down</kbd> key
while focused on the bottom-most element,
focus remains on that element
rather than jumping to the top of the screen.

## Reset focus traversal with pointer clicks

When switching between a physical keyboard and a mouse or touchpad on desktop
or large-screen devices:

- **Clear focus on tap or click**: Clicking or tapping on non-interactive space with a mouse or touchpad releases focus from the active element.
- **Restart traversal** : After focus is cleared, the next <kbd>Tab</kbd> key press restarts one-dimensional traversal at the **first focus target** in visual appearance order, rather than resuming from the previously active element. It is same to the two-dimensional focus traversal. The directional keys moves keyboard focus to the closest focus target in the requested direction.

For details on programmatically clearing focus, see [Move and clear focus](https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus).

## Customize focus traversal order

You can customize traversal behavior
with the [`focusProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier.

### Customize one-dimensional traversal order

To override one-dimensional traversal,
specify the [`next`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusProperties#next()) or [`previous`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusProperties#previous()) property
with a [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester):

1. Create a `FocusRequester` object with `remember { FocusRequester() }`.
2. Attach the `FocusRequester` to the target composable using the [`focusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)) modifier.
3. Apply the `focusProperties` modifier to the source composable and assign the `FocusRequester` to `next` (for <kbd>Tab</kbd>) or `previous` (for <kbd>Shift+Tab</kbd>).


```kotlin
val (first, second, third) = remember { FocusRequester.createRefs() }

Column {
    Button(
        onClick = { /* ... */ },
        modifier = Modifier
            .focusRequester(first)
            .focusProperties { next = third }
    ) {
        Text("First (Tab jumps to Third)")
    }
    Button(
        onClick = { /* ... */ },
        modifier = Modifier.focusRequester(second)
    ) {
        Text("Second")
    }
    Button(
        onClick = { /* ... */ },
        modifier = Modifier.focusRequester(third)
    ) {
        Text("Third")
    }
}
```

<br />

### Customize two-dimensional traversal order

Similarly, you can override two-dimensional focus traversal
by assigning `FocusRequester` instances
to `up`, `down`, `start`, `end`, `left`, or `right`
within `focusProperties`:


```kotlin
val (topButton, bottomButton) = remember { FocusRequester.createRefs() }

Button(
    onClick = { /* ... */ },
    modifier = Modifier
        .focusRequester(topButton)
        .focusProperties {
            down = bottomButton
            right = bottomButton
        }
) {
    Text("Top button")
}
Button(
    onClick = { /* ... */ },
    modifier = Modifier.focusRequester(bottomButton)
) {
    Text("Bottom button")
}
```

<br />

To block focus navigation in a specific direction
(for example, at layout boundaries),
assign [`FocusRequester.Cancel`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester#Cancel()) to that property
(for example, `down = FocusRequester.Cancel`).
To explicitly retain the system's default traversal algorithm for
a given direction, assign [`FocusRequester.Default`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester#Default()).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus in text fields](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields)
- [Group focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group)
- [Move and clear focus](https://developer.android.com/develop/ui/compose/touch-input/focus/move-focus)
- [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)
- [Test focus navigation](https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus)