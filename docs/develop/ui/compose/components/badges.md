---
title: https://developer.android.com/develop/ui/compose/components/badges
url: https://developer.android.com/develop/ui/compose/components/badges
source: md.txt
---

Use a [badge](https://m3.material.io/components/badges/overview) to display a small visual element to denote status
or a numeric value on another composable. Here are a few common scenarios where
you might use a badge:

- **Notifications**: Display the number of unread notifications on an app icon or notification bell.
- **Messages**: Indicate new or unread messages within a chat application.
- **Status updates**: Show the status of a task, such as "complete," "in progress," or "failed."
- **Cart quantity**: Display the number of items in a user's shopping cart.
- **New content**: Highlight new content or features available to the user.

![Different example of the badge component.](https://developer.android.com/static/develop/ui/compose/images/components/badges.svg) **Figure 1.** Badge examples

## API surface

Use the [`BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BadgedBox(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) composable to implement badges in your application. It
is ultimately a container. You control its appearance with these two main
parameters:

- `content`: The composable content that the `BadgedBox` contains. Typically `Icon`.
- `badge`: The composable that appears as the badge over the content. Typically the dedicated [`Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Badge(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) composable.

## Basic example

This code snippet shows a basic implementation of `BadgedBox`:


```kotlin
@Composable
fun BadgeExample() {
    BadgedBox(
        badge = {
            Badge()
        }
    ) {
        Icon(
            imageVector = Icons.Filled.Mail,
            contentDescription = "Email"
        )
    }
}
```

<br />

This example displays a badge that overlaps the provided `Icon` composable. Note
the following in the code:

- [`BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BadgedBox(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) serves as the overall container.
- The argument for the `badge` parameter of `BadgedBox` is [`Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Badge(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)). Because `Badge` has no arguments of its own, the app displays the default badge, which is a small red circle.
- `Icon` serves as the argument for the `content` parameter of `BadgedBox`. It is the icon over which the badge appears. In this case, it is a mail icon.

This is how it appears:
![A simple badge that contains no content.](https://developer.android.com/static/develop/ui/compose/images/components/badge-simple.png) **Figure 2.** A minimal badge implementation.

> [!IMPORTANT]
> **Important:** You can pass any composable to the `BadgedBox` composable's content slot. You could therefore create a badge that displays on a `Button`, an `Image`, or any other composable.

## Detailed example

The following snippet demonstrates how you can display values in the badge that
respond to user actions.


```kotlin
@Composable
fun BadgeInteractiveExample() {
    var itemCount by remember { mutableIntStateOf(0) }

    Column(
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        BadgedBox(
            badge = {
                if (itemCount > 0) {
                    Badge(
                        containerColor = Color.Red,
                        contentColor = Color.White
                    ) {
                        Text("$itemCount")
                    }
                }
            }
        ) {
            Icon(
                imageVector = Icons.Filled.ShoppingCart,
                contentDescription = "Shopping cart",
            )
        }
        Button(onClick = { itemCount++ }) {
            Text("Add item")
        }
    }
}
```

<br />

This example implements a shopping cart icon with a badge that displays the
number of items in the user's cart.

- The [`BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BadgedBox(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) displays only when the item count is over 0.
- The arguments for `containerColor` and `contentColor` control the appearance of the badge.
- The `Text` composable for the content slot of [`Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Badge(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) appears within the badge. In this case, it displays the number of items in the cart.

This implementation appears as follows:
![A badge implementation that contains the number of items in a shopping cart.](https://developer.android.com/static/develop/ui/compose/images/components/badge-advanced.png) **Figure 3.** A badge that displays the number of items in a shopping cart.

## Additional resources

- [Material 3 - Badges](https://m3.material.io/components/badges/overview)
- [`BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BadgedBox(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1))
- [`Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Badge(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1))