---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button
url: https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button
source: md.txt
---

<br />

A floating action button (FAB) is a high-emphasis button that lets the user
perform a primary action in an application. It promotes a single, focused action
that is the most common pathway a user might take and is typically found
anchored to the bottom right of the screen.

Consider these three use cases where you might use a FAB:

- **Create new item**: In a note-taking app, a FAB might be used to quickly create a new note.
- **Add new contact**: In a chat app, a FAB could open an interface that lets the user add someone to a conversation.
- **Center location**: In a map interface, a FAB could center the map on the user's current location.

In Material Design, there are four types of FAB:

- [FAB](https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button#basic): A floating action button of ordinary size.
- [Small FAB](https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button#small): A smaller floating action button.
- [Large FAB](https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button#large): A larger floating action button.
- [Extended FAB](https://developer.android.com/develop/ui/compose/quick-guides/content/create-floating-action-button#extended): A floating action button that contains more than just an icon.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

### Kotlin


```kotlin
  implementation(platform("androidx.compose:compose-bom:2026.02.01"))
```

<br />

### Groovy


```groovy
  implementation platform('androidx.compose:compose-bom:2026.02.01')
```

<br />

## Create a basic floating action button

To create a general floating action button, use the basic
[`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable:


```kotlin
@Composable
fun Example(onClick: () -> Unit) {
    FloatingActionButton(
        onClick = { onClick() },
    ) {
        Icon(Icons.Filled.Add, "Floating action button.")
    }
}
```

<br />

### Result

![A standard floating action button with rounded corner, a shadow, and an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/fab.png) **Figure 1.** A floating action button.

## Create a small floating action button

To create a small floating action button, use the
[`SmallFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SmallFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. The following example demonstrates
how to do so, with the addition of custom colors.


```kotlin
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
```

<br />

> [!NOTE]
> **Note:** Because the various FAB composables share many parameters, you can use the approach in this example to customize colors with other composables.

### Result

![An implementation of SmallFloatingActionButton that contains an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/fab-small.png) **Figure 2.** A small floating action button.

## Create a large floating action button

To create a large floating action button, use the
[`LargeFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. This composable is not
significantly different from the other examples aside from the fact that it
results in a bigger button.

The following is a straightforward implementation of a large FAB.

> [!NOTE]
> **Note:** This example passes `CircleShape` as the value for the `shape` parameter, resulting in a round button, rather than a square with rounded borders. You can pass any instance of `Shape`, or set the value of `MaterialTheme.shape.large` to adjust it across your app.


```kotlin
@Composable
fun LargeExample(onClick: () -> Unit) {
    LargeFloatingActionButton(
        onClick = { onClick() },
        shape = CircleShape,
    ) {
        Icon(Icons.Filled.Add, "Large floating action button")
    }
}
```

<br />

### Result

![An implementation of LargeFloatingActionButton that contains an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/fab-large.png) **Figure 3.** A large floating action button.

## Create an extended floating action button

You can create more complex floating action buttons with the
[`ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ExtendedFloatingActionButton(kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource)) composable. The key difference between it
and [`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) is that it has dedicated `icon` and `text`
parameters. They let you create a button with more complex content that scales
to fit its content appropriately.

The following snippet demonstrates how to implement
`ExtendedFloatingActionButton`, with example values passed for `icon` and
`text`.


```kotlin
@Composable
fun ExtendedExample(onClick: () -> Unit) {
    ExtendedFloatingActionButton(
        onClick = { onClick() },
        icon = { Icon(Icons.Filled.Edit, "Extended floating action button.") },
        text = { Text(text = "Extended FAB") },
    )
}
```

<br />

### Result

![An implementation of ExtendedFloatingActionButton that displays text that says 'extended button' and an edit icon.](https://developer.android.com/static/develop/ui/compose/images/components/fab-extended.png) **Figure 4.** A floating action button with both text and an icon.

## Key points

Although there are several composables you can use to create floating action
buttons consistent with Material Design, their parameters don't differ greatly.
Among the key parameters you should keep in mind are the following:

- `onClick`: The function called when the user presses the button.
- `containerColor`: The color of the button.
- `contentColor`: The color of the icon.

z## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)