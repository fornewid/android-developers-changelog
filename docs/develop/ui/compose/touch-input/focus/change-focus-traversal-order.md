---
title: Change focus traversal order  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/touch-input/focus/change-focus-traversal-order
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Change focus traversal order Stay organized with collections Save and categorize content based on your preferences.



The [Default focus traversal order](/develop/ui/compose/touch-input/focus) section described how Compose
automatically adds focus traversal behavior to your elements, for both
one-dimensional (`tab` key) and two-dimensional (arrow keys) navigation. In some
cases, you might need to override this default behavior and be more explicit
about the required traversal order.

## Override one-dimensional traversal order

To change the default focus traversal order for one-dimensional navigation, you
create a set of references, one for each focusable composable:

```
val (first, second, third, fourth) = remember { FocusRequester.createRefs() }

FocusSnippets.kt
```

Then, use the [`focusRequester`](/reference/kotlin/androidx/compose/ui/focus/focusRequester.modifier#(androidx.compose.ui.Modifier).focusRequester(androidx.compose.ui.focus.FocusRequester)) modifier to associate each of them with a
composable:

```
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

FocusSnippets.kt
```

You can now use the [`focusProperties`](/reference/kotlin/androidx/compose/ui/focus/focusProperties.modifier#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier to specify a custom traversal order:

```
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

FocusSnippets.kt
```

## Override two-dimensional traversal order

It is also possible to add fine-grained control over the focus traversal order
for two-dimensional navigation with the arrow keys. For each element, you can
override the default navigation destination for each of the directions by adding
the [`focusProperties`](/reference/kotlin/androidx/compose/ui/focus/focusProperties.modifier#(androidx.compose.ui.Modifier).focusProperties(kotlin.Function1)) modifier and specifying the item that would come up,
down, or any other direction:

```
TextButton(
    onClick = {},
    modifier = Modifier
        .focusRequester(fourth)
        .focusProperties {
            down = third
            right = second
        }
) {}

FocusSnippets.kt
```

This technique not only effectively uses keyboard arrows, but would work with
D-Pads and sticks on wired and wireless controllers.

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Change focus behavior](/develop/ui/compose/touch-input/focus/change-focus-behavior)
* [Focus in Compose](/develop/ui/compose/touch-input/focus)

[Previous

arrow\_back

Overview](/develop/ui/compose/touch-input/focus)

[Next

Change focus behavior

arrow\_forward](/develop/ui/compose/touch-input/focus/change-focus-behavior)