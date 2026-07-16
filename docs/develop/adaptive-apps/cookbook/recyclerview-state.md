---
title: https://developer.android.com/develop/adaptive-apps/cookbook/recyclerview-state
url: https://developer.android.com/develop/adaptive-apps/cookbook/recyclerview-state
source: md.txt
---

![Three star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/three-star-rating.png)

Scrollable lists in Jetpack Compose, such as [`LazyColumn`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)) and [`LazyRow`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#LazyRow(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.LazyListState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,kotlin.Function1)),
can display large amounts of data efficiently. However, configuration changes,
such as device rotation or folding/unfolding a foldable device, can reset the
state of a list, forcing users to again scroll to their previous position.

## Best practices

Scrollable lists should maintain their state---in particular, scroll
position---and the state of their individual list elements (like text inputs) during all configuration changes to provide a seamless user experience.

## Ingredients

- [`rememberLazyListState()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/package-summary#rememberLazyListState(kotlin.Int,kotlin.Int)): Creates and remembers a [`LazyListState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState) that is used to control and observe the scroll position of the list. It automatically persists across configuration changes.
- [`rememberSaveable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary#rememberSaveable(kotlin.Array,androidx.compose.runtime.saveable.Saver,kotlin.String,kotlin.Function0)): Remembers the state value across configuration changes, useful for preserving individual list element states (like text field inputs).

## Steps

In Jetpack Compose, preserving the scroll position of a list is handled
automatically when you use a scroll state. To preserve the state of individual,
complex list elements (such as `TextField` inputs), use `rememberSaveable`.

### 1. Preserve list scroll state

To save and restore the scroll position of your list across configuration
changes, create a [`LazyListState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/lazy/LazyListState) using `rememberLazyListState()` and pass
it as the `state` parameter of your scrollable list, such as a `LazyColumn`.

Compose automatically persists the scroll position for you.

### 2. Preserve individual list element state

If your list contains stateful elements (for example, items with text fields),
the state of those individual elements can be lost when they are scrolled
off-screen and recycled, or during configuration changes.

To preserve individual element state, use `rememberSaveable` inside the list
item scope. This ensures that when the item is recomposed or scrolled back into
view, its state is restored.

Here is a complete, compilable implementation demonstrating both scroll state
and item state restoration:


```kotlin
// Scroll state is automatically saved and restored by rememberLazyListState
val listState = rememberLazyListState()

LazyColumn(state = listState) {
    items(100) { index ->
        // Use rememberSaveable to preserve individual item state (e.g., text input)
        var text by rememberSaveable { mutableStateOf("") }
        TextField(
            value = text,
            onValueChange = { text = it },
            label = { Text("Item $index") }
        )
    }
}
```

<br />

## Results

Your scrollable list is now able to restore its scroll position and the state of
every element in the list.

## Additional resources

- [Lists and grids in Compose](https://developer.android.com/develop/ui/compose/lists)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state#save-ui-state)