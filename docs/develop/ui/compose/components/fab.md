---
title: Floating action button  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/components/fab
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Floating action button Stay organized with collections Save and categorize content based on your preferences.



A Floating Action Button (FAB) is a high-emphasis button that lets the user
perform a primary action in an application. It promotes a single, focused action
that is the most common pathway a user might take and is typically found
anchored to the bottom right of the screen.

Consider these three use cases where you might use a FAB:

* **Create new item**: In a note-taking app, a FAB might be used to quickly
  create a new note.
* **Add new contact**: In a chat app, a FAB could open an interface that lets
  the user add someone to a conversation.
* **Center location**: In a map interface, a FAB could center the map on the
  user's current location.

In Material Design, there are four types of FAB:

* **FAB**: A floating action button of ordinary size.
* **Small FAB**: A smaller floating action button.
* **Large FAB**: A larger floating action button.
* **Extended FAB**: A floating action button that contains more than just an
  icon.

![An example of each of the four floating action button components.](/static/develop/ui/compose/images/components/fabs.svg)


**Figure 1.** The four floating action button types.

## API surface

Although there are several composables you can use to create floating action
buttons consistent with Material Design, their parameters don't differ greatly.
Among the key parameters you should keep in mind are the following:

* `onClick`: The function called when the user presses the button.
* `containerColor`: The color of the button.
* `contentColor`: The color of the icon.

## Floating action button

To create a general floating action button, use the basic
[`FloatingActionButton`](/reference/kotlin/androidx/compose/material3/FloatingActionButton.composable#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. The following example demonstrates a
basic implementation of a FAB:

```
@Composable
fun Example(onClick: () -> Unit) {
    FloatingActionButton(
        onClick = { onClick() },
    ) {
        Icon(Icons.Filled.Add, "Floating action button.")
    }
}

FloatingActionButton.kt
```

This implementation appears as follows:

![A standard floating action button with rounded corner, a shadow, and an 'add' icon.](/static/develop/ui/compose/images/components/fab.png)


**Figure 2.** A floating action button.

## Small button

To create a small floating action button, use the
[`SmallFloatingActionButton`](/reference/kotlin/androidx/compose/material3/SmallFloatingActionButton.composable#SmallFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. The following example demonstrates
how to do so, with the addition of custom colors.

```
@Composable
fun SmallExample(onClick: () -> Unit) {
    SmallFloatingActionButton(
        onClick = { onClick() },
        containerColor = MaterialTheme.colorScheme.secondaryContainer,
        contentColor = MaterialTheme.colorScheme.secondary
    ) {
        Icon(Icons.Filled.Add, "Small floating action button.")
    }
}

FloatingActionButton.kt
```

**Note:** Because the various FAB composables share many parameters, you can use the
approach in this example to customize colors with other composables.

This implementation appears as follows:

![An implementation of SmallFloatingActionButton that contains an 'add' icon.](/static/develop/ui/compose/images/components/fab-small.png)


**Figure 3.** A small floating action button.

## Large button

To create a large floating action button, use the
[`LargeFloatingActionButton`](/reference/kotlin/androidx/compose/material3/LargeFloatingActionButton.composable#LargeFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. This composable is not
significantly different from the other examples aside from the fact that it
results in a bigger button.

The following is a straightforward implementation of a large FAB.

**Note:** This example passes `CircleShape` as the value for the `shape` parameter,
resulting in a round button, rather than a square with rounded borders. You can
pass any instance of `Shape`, or set the value of `MaterialTheme.shape.large` to
adjust it across your app.

```
@Composable
fun LargeExample(onClick: () -> Unit) {
    LargeFloatingActionButton(
        onClick = { onClick() },
        shape = CircleShape,
    ) {
        Icon(Icons.Filled.Add, "Large floating action button")
    }
}

FloatingActionButton.kt
```

This implementation appears as follows:

![An implementation of LargeFloatingActionButton that contains an 'add' icon.](/static/develop/ui/compose/images/components/fab-large.png)


**Figure 4.** A large floating action button.

## Extended button

You can create more complex floating action buttons with the
[`ExtendedFloatingActionButton`](/reference/kotlin/androidx/compose/material3/ExtendedFloatingActionButton.composable#ExtendedFloatingActionButton(kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource)) composable. The key difference between it
and [`FloatingActionButton`](/reference/kotlin/androidx/compose/material3/FloatingActionButton.composable#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) is that it has dedicated `icon` and `text`
parameters. They let you create a button with more complex content that scales
to fit its content appropriately.

The following snippet demonstrates how to implement
`ExtendedFloatingActionButton`, with example values passed for `icon` and
`text`.

```
@Composable
fun ExtendedExample(onClick: () -> Unit) {
    ExtendedFloatingActionButton(
        onClick = { onClick() },
        icon = { Icon(Icons.Filled.Edit, "Extended floating action button.") },
        text = { Text(text = "Extended FAB") },
    )
}

FloatingActionButton.kt
```

This implementation appears as follows:

![An implementation of ExtendedFloatingActionButton that displays text that says 'extended button' and an edit icon.](/static/develop/ui/compose/images/components/fab-extended.png)


**Figure 5.** A floating action button with both text and an icon.

## Additional resources

* [Common buttons](/develop/ui/compose/components/button)
* [Material UI docs](https://m3.material.io/components/floating-action-button/overview)