---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group
url: https://developer.android.com/develop/ui/compose/touch-input/focus/focus-group
source: md.txt
---

You can group multiple focus targets together using the [`focusGroup`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusGroup()) modifier.
Grouping lets you manage focus hierarchies, isolate logical UI regions (such as
toolbars, dialog actions, or card lists), and intercept when focus enters or
exits a region.

## Focus group concepts: enter, exit, and default traversal

A focus group establishes a cohesive navigation boundary around its child focus
targets. Understanding how focus moves across this boundary relies on two key
concepts:

- **Enter**: The event that occurs when focus transitions from any element outside the focus group to an element inside the group.
- **Exit**: The event that occurs when focus leaves the last internal element of the group and transitions to an external focus target.

![Diagram showing Enter and Exit transitions across a focus group boundary.](https://developer.android.com/static/develop/ui/compose/images/touchinput/focus-group-concepts.svg) **Figure 1.** Focus group with enter and exit events.

## Default focus traversal behavior

By default, when a focus group receives focus from the outside:

1. **Entering the group** : Compose automatically selects an internal child focus target. For one-dimensional (<kbd>Tab</kbd>) navigation, it selects the first child in visual appearance order. For two-dimensional (arrow key or D-pad) navigation, it selects the child that is geometrically closest to the incoming direction.
2. **Navigating within the group**: Repeated navigation key presses move focus among the sibling focus targets enclosed by the group.
3. **Exiting the group**: Once the user navigates past the last focus target inside the group, the next key press exits the group and moves focus to the neighboring focus target outside the group.

## Customize focus entry redirection

In many UI designs, the default entry target (such as the first child in
appearance order) is not the most logical or convenient choice for the user.

### Intention and use cases

Consider a confirmation dialog with a "Cancel" button on the left and a
primary "Confirm" button on the right. When the user navigates down into the
button bar from a form field:

- **Default behavior**: Focus would land on "Cancel" because it is the first button in visual appearance order.
- **Intended behavior** : Because "Confirm" is the primary recommended action, you may want focus to land directly on "Confirm" when entering the button group from earlier in the focus order, while still allowing the user to press <kbd>Left</kbd> to select "Cancel" if needed.

![Default focus entry into a button group.](https://developer.android.com/static/develop/ui/compose/images/touchinput/focus-group-default-target.png) **Figure 2.** **Cancel** and **Confirm** buttons with default focus entry target.

Other common use cases include:

- Moving focus directly to the currently selected tab when entering a `TabRow`.
- Moving focus directly to the "Play / Pause" control when entering a media playback bar.

### Implementation with onEnter and FocusRequester

To redirect focus upon entering a focus group:

1. Apply the `focusGroup` modifier to the parent container enclosing the related focus targets.
2. Apply the [`focusProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusProperties)modifier to the container, and configure the [`onEnter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusProperties#onEnter()) callback.
3. In the `onEnter` callback (scoped to [`FocusEnterExitScope`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusEnterExitScope)), call [`requestFocus()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester#requestFocus()) on a [`FocusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusRequester) associated with the preferred default child using [`focusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/Modifier#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)).


```kotlin
val defaultChildRequester = remember { FocusRequester() }

Row(
    modifier = Modifier
        .focusGroup()
        .focusProperties {
            // Intercept entry into this group and redirect focus to the primary action
            onEnter = {
                defaultChildRequester.requestFocus()
            }
        }
) {
    Button(onClick = { /* Cancel action */ }) {
        Text("Cancel")
    }
    Button(
        onClick = { /* Confirm action */ },
        modifier = Modifier.focusRequester(defaultChildRequester)
    ) {
        Text("Confirm (Default)")
    }
}
```

<br />

Inside `onEnter` and [`onExit`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusProperties#onExit()), you can also call [`cancelFocusChange()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/FocusEnterExitScope#cancelFocusChange()) to
completely block focus transitions across the boundary, or inspect
`requestedFocusDirection` to customize routing based on whether the user
navigated using <kbd>Tab</kbd>, <kbd>Down</kbd>, or <kbd>Left</kbd>.

## Scrollable containers are focus groups by default

In Jetpack Compose, scrollable containers such as [`LazyRow`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyRow(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)), [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)),
and [`LazyVerticalGrid`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/grid/package-summary#LazyVerticalGrid(androidx.compose.foundation.lazy.grid.GridCells,androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.grid.LazyGridState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.compose.foundation.OverscrollEffect,kotlin.Function1)) automatically act as focus groups.
You don't need to explicitly apply the `focusGroup` modifier
to them to set `onEnter` or `onExit` callbacks.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Focus targets](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-target)
- [Focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-traversal)
- [Focus in text fields](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-in-text-fields)
- [Restore focus](https://developer.android.com/develop/ui/compose/touch-input/focus/focus-restoration)
- [Programmatically request focus](https://developer.android.com/develop/ui/compose/touch-input/focus/request-focus)
- [Test focus navigation](https://developer.android.com/develop/ui/compose/touch-input/focus/testing-focus)