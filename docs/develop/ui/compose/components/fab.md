---
title: https://developer.android.com/develop/ui/compose/components/fab
url: https://developer.android.com/develop/ui/compose/components/fab
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/components/llms.txt

A [Floating Action Button (FAB)](https://m3.material.io/components/floating-action-button/guidelines#9a56f806-8840-4910-8f53-3cb2a6c81c86) is a high-emphasis button that lets the user
perform a primary action in an application. It promotes a single, focused action
that is the most common pathway a user might take and is typically found
anchored to the bottom right of the screen.

Consider these three use cases where you might use a FAB:

- **Create new item**: In a note-taking app, a FAB might be used to quickly create a new note.
- **Add new contact**: In a chat app, a FAB could open an interface that lets the user add someone to a conversation.
- **Center location**: In a map interface, a FAB could center the map on the user's current location.

In Material Design, there are four types of FAB:

- **FAB**: A floating action button of ordinary size.
- **Small FAB**: A smaller floating action button.
- **Large FAB**: A larger floating action button.
- **Extended FAB**: A floating action button that contains more than just an icon.

![An example of each of the four floating action button components.](https://developer.android.com/static/develop/ui/compose/images/components/fabs.svg) **Figure 1.** The four floating action button types.

## API surface

Although there are several composables you can use to create floating action
buttons consistent with Material Design, their parameters don't differ greatly.
Among the key parameters you should keep in mind are the following:

- `onClick`: The function called when the user presses the button.
- `containerColor`: The color of the button.
- `contentColor`: The color of the icon.

## Floating action button

To create a general floating action button, use the basic
[`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButton.composable.md.txt#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. The following example demonstrates a
basic implementation of a FAB:


```kotlin
@Composable
fun Example(onClick: () -> Unit) {
    FloatingActionButton(
        onClick = { onClick() },
    ) {
        Icon(painter = rememberVectorPainter(AppIcons.Add), "Floating action button.")
    }
}
```

<br />

This implementation appears as follows:
![A floating action button with an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_fab.png) **Figure 2.** A floating action button.

## Small button

To create a small floating action button, use the
[`SmallFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SmallFloatingActionButton.composable.md.txt#SmallFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. The following example demonstrates
how to do so, with the addition of custom colors.


```kotlin
@Composable
fun SmallExample(onClick: () -> Unit) {
    SmallFloatingActionButton(
        onClick = { onClick() },
        containerColor = MaterialTheme.colorScheme.secondaryContainer,
        contentColor = MaterialTheme.colorScheme.secondary
    ) {
        Icon(painter = rememberVectorPainter(AppIcons.Add), "Small floating action button.")
    }
}
```

<br />

> [!NOTE]
> **Note:** Because the various FAB composables share many parameters, you can use the approach in this example to customize colors with other composables.

This implementation appears as follows:
![A small floating action button with an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_smallfab.png) **Figure 3.** A small floating action button.

## Large button

To create a large floating action button, use the
[`LargeFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LargeFloatingActionButton.composable.md.txt#LargeFloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) composable. This composable is not
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
        Icon(painter = rememberVectorPainter(AppIcons.Add), "Large floating action button")
    }
}
```

<br />

This implementation appears as follows:
![A large floating action button with an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_largefab.png) **Figure 4.** A large floating action button.

## Extended button

You can create more complex floating action buttons with the
[`ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ExtendedFloatingActionButton.composable.md.txt#ExtendedFloatingActionButton(kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource)) composable. The key difference between it
and [`FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButton.composable.md.txt#FloatingActionButton(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.material3.FloatingActionButtonElevation,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)) is that it has dedicated `icon` and `text`
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
        icon = { Icon(painter = rememberVectorPainter(AppIcons.Edit), "Extended floating action button.") },
        text = { Text(text = "Extended FAB") },
    )
}
```

<br />

This implementation appears as follows:
![An extended floating action button with an edit icon and the text 'Extended FAB'.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_components_extendedfab.png) **Figure 5.** A floating action button with both text and an icon.

## M3 Expressive update

The FAB offers additional sizes to match the extended FAB and expanded color
options, including [`MediumFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/MediumFloatingActionButton.composable.md.txt), which is recommended for
most situations alongside existing FAB sizes.
![Floating action buttons with expressive color and size variants.](https://developer.android.com/static/develop/ui/compose/images/components/fab_expressive_update.png) **Figure 6.** Material 3 Expressive floating action button color and size variations.

For more information about the M3 Expressive updates for floating action
buttons, see the [Material Design 3 Floating action button guidelines](https://m3.material.io/components/floating-action-button/guidelines#9a56f806-8840-4910-8f53-3cb2a6c81c86).

### Medium floating action button

The medium FAB is recommended for most situations, and works best in compact and
medium windows. Use it for important actions without taking up too much space.

The following snippet demonstrates how to implement a medium floating action
button using [`MediumFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/MediumFloatingActionButton.composable.md.txt):


```kotlin
@Composable
fun MediumFloatingActionButtonSample() {
    MediumFloatingActionButton(onClick = {}) {
        Icon(
            painter = rememberVectorPainter(AppIcons.Add),
            contentDescription = "Add",
            modifier = Modifier.size(FloatingActionButtonDefaults.MediumIconSize),
        )
    }
}
```
![A medium floating action button with rounded square corners and an 'add' icon.](https://developer.android.com/static/develop/ui/compose/images/components/previews/android_compose_expressive_components_mediumfab.png) A medium floating action button.

<br />

## Additional resources

- [Common buttons](https://developer.android.com/develop/ui/compose/components/button.md.txt)
- [Material UI docs](https://m3.material.io/components/floating-action-button/overview)