---
title: https://developer.android.com/develop/ui/compose/system/material-insets
url: https://developer.android.com/develop/ui/compose/system/material-insets
source: md.txt
---

For ease of use, many of the built-in Material 3 composables
([`androidx.compose.material3`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary))
handle insets themselves, based on how the composables are placed in your app
according to the Material specifications.

> [!NOTE]
> **Note:** Material 2 Components ([`androidx.compose.material`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary)) don't automatically handle insets themselves. However, you can get access to the insets and apply them manually. In [`androidx.compose.material 1.6.0`](https://developer.android.com/jetpack/androidx/releases/compose-material#1.6.0-alpha03) and later use the `windowInsets` parameter to apply the insets manually for [`BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomAppBar(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)), [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TopAppBar(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,kotlin.Function1)), [`BottomNavigation`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#BottomNavigation(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1)), and [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#NavigationRail(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1,kotlin.Function1)). Likewise, use the `contentWindowInsets` parameter for [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Scaffold(androidx.compose.foundation.layout.WindowInsets,androidx.compose.ui.Modifier,androidx.compose.material.ScaffoldState,kotlin.Function0,kotlin.Function0,kotlin.Function1,kotlin.Function0,androidx.compose.material.FabPosition,kotlin.Boolean,kotlin.Function1,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)). Otherwise, apply the insets manually as padding.

## Inset handling composables

The following is a list of the [Material
Components](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary) that
automatically handle insets.

## App bars

- [`TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#TopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) / [`SmallTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SmallTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) / [`CenterAlignedTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#CenterAlignedTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) / [`MediumTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#MediumTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)) / [`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)): Applies the *top* and *horizontal* sides of the system bars as padding since it is used at the top of the window.
- [`BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#BottomAppBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)): Applies the *bottom* and *horizontal* sides of the system bars as padding.

### Content containers

- [`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) / [`DismissibleDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DismissibleDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) / [`PermanentDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#PermanentDrawerSheet(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) (content inside a modal navigation drawer): Applies *vertical* and *start* insets to content.
- [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function1)): Applies the *bottom* insets.
- [`NavigationBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) : Applies the *bottom* and *horizontal* insets.
- [`NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)): Applies the *vertical* and *start* insets.

### Scaffold

By default,
[`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#Scaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.FabPosition,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1))
provides insets as parameter `PaddingValues` for you to consume and use.
`Scaffold` does not apply the insets to content; this responsibility is yours.
For example, to consume these insets with a `LazyColumn` inside a `Scaffold`:


```kotlin
Scaffold { innerPadding ->
    // innerPadding contains inset information for you to use and apply
    LazyColumn(
        // consume insets as scaffold doesn't do it by default
        modifier = Modifier.consumeWindowInsets(innerPadding),
        contentPadding = innerPadding
    ) {
        // ..
    }
}
```

<br />

The following video shows a `LazyColumn` within a `Scaffold` with edge-to-edge
display disabled and enabled:
Alas, your browser doesn't support HTML5 video. That's OK! You can still [download the video](https://developer.android.com/static/develop/ui/compose/images/layouts/insets/LazyColumn_E2E.mp4) and watch it with a video player.

Using the `PaddingValues` parameter in `Scaffold` is generally enough to inset
your UI away from the system UI and display cutouts. Avoid using additional
inset handling approaches like rulers, padding modifiers, or inset size
modifiers if using `Scaffold` to avoid applying too much padding to your UI.

## Override default insets

You can change the `windowInsets` parameter passed to the composable to
configure the composable's behavior. This parameter can be a different type of
window inset to apply instead, or disabled by passing an empty instance:
`WindowInsets(0, 0, 0, 0)`.

For example, to disable the inset handling on
[`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#LargeTopAppBar(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,androidx.compose.material3.TopAppBarColors,androidx.compose.material3.TopAppBarScrollBehavior)),
set the `windowInsets` parameter to an empty instance:


```kotlin
LargeTopAppBar(
    windowInsets = WindowInsets(0, 0, 0, 0),
    title = {
        Text("Hi")
    }
)
```

<br />