---
title: https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-traversal-order
url: https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-traversal-order
source: md.txt
---

The [Default focus traversal order](https://developer.android.com/develop/ui/compose/touch-input/focus) section described how Compose
automatically adds focus traversal behavior to your elements, for both
one-dimensional (`tab` key) and two-dimensional (arrow keys) navigation. In some
cases, you might need to override this default behavior and be more explicit
about the required traversal order.

## Override one-dimensional traversal order

To change the default focus traversal order for one-dimensional navigation, you
create a set of references, one for each focusable composable:


```kotlin
val (first, second, third, fourth) = remember { FocusRequester.createRefs() }
```

<br />

Then, use the [`focusRequester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)) modifier to associate each of them with a
composable:


```kotlin
Column {
    Row {
        TextButton({}, Modifier.focusRequester(first)) { Text("First field") }
        TextButton({}, Modifier.focusRequester(third)) { Text("Third field") }
    }

    Row {
        TextButton({}, Modifier.focusRequester(second)) { Text("Second field") }
        TextButton({}, Modifier.focusRequester(fourth)) { Text("Fourth field") }
    }
}
```

<br />

You can now use the [`focusProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier to specify a custom traversal order:


```kotlin
Column {
    Row {
        TextButton(
            {},
            Modifier
                .focusRequester(first)
                .focusProperties { next = second }
        ) {
            Text("First field")
        }
        TextButton(
            {},
            Modifier
                .focusRequester(third)
                .focusProperties { next = fourth }
        ) {
            Text("Third field")
        }
    }

    Row {
        TextButton(
            {},
            Modifier
                .focusRequester(second)
                .focusProperties { next = third }
        ) {
            Text("Second field")
        }
        TextButton(
            {},
            Modifier
                .focusRequester(fourth)
                .focusProperties { next = first }
        ) {
            Text("Fourth field")
        }
    }
}
```

<br />

## Override two-dimensional traversal order

It is also possible to add fine-grained control over the focus traversal order
for two-dimensional navigation with the arrow keys. For each element, you can
override the default navigation destination for each of the directions by adding
the [`focusProperties`](https://developer.android.com/reference/kotlin/androidx/compose/ui/focus/package-summary#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier and specifying the item that would come up,
down, or any other direction:


```kotlin
TextButton(
    onClick = {},
    modifier = Modifier
        .focusRequester(fourth)
        .focusProperties {
            down = third
            right = second
        }
) {}
```

<br />

This technique not only effectively uses keyboard arrows, but would work with
D-Pads and sticks on wired and wireless controllers.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Change focus behavior](https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-behavior)
- [Focus in Compose](https://developer.android.com/develop/ui/compose/touch-input/focus)