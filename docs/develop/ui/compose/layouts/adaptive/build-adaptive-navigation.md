---
title: Build adaptive navigation  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/build-adaptive-navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Build adaptive navigation Stay organized with collections Save and categorize content based on your preferences.




Most apps have a few top-level destinations that are accessible through the
app's primary navigation UI. In compact windows, such as a standard phone
display, the destinations are typically displayed in a navigation bar at the
bottom of the window. In an expanded window, such as a full screen app on a
tablet, a navigation rail alongside the app is usually a better choice since the
navigation controls are easier to reach while holding the left and right sides
of the device.

[`NavigationSuiteScaffold`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteScaffold.composable) simplifies switching
between navigation UIs by displaying the appropriate navigation UI composable
based on [`WindowSizeClass`](/reference/kotlin/androidx/window/core/layout/WindowSizeClass). This includes dynamically
changing the UI during runtime window size changes. The default behavior is to
show either of the following UI components:

* **Navigation bar** if the width or height is compact or if the device is in
  tabletop posture
* **Navigation rail** for everything else

![](/static/develop/ui/compose/images/layouts/adaptive/navigationsuitescaffold_with_nav_bar.png)


**Figure 1.** `NavigationSuiteScaffold` displays a navigation bar in compact windows.


![](/static/develop/ui/compose/images/layouts/adaptive/navigationsuitescaffold_with_nav_rail.png)


**Figure 2.** `NavigationSuiteScaffold` displays a navigation rail in expanded windows.

## Add dependencies

`NavigationSuiteScaffold` is part of the
[Material3 adaptive navigation suite](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/package-summary)
library. Add a dependency for the library in the `build.gradle` file of your app
or module:

### Kotlin

```
implementation("androidx.compose.material3:material3-adaptive-navigation-suite")
```

### Groovy

```
implementation 'androidx.compose.material3:material3-adaptive-navigation-suite'
```

## Create a scaffold

The two main parts of `NavigationSuiteScaffold` are the navigation suite items
and the content for the selected destination. You can directly define the
navigation suite items in a composable, but it's common to have these defined
elsewhere, for example, in an enum:

```
enum class AppDestinations(
    @StringRes val label: Int,
    val icon: ImageVector,
    @StringRes val contentDescription: Int
) {
    HOME(R.string.home, Icons.Default.Home, R.string.home),
    FAVORITES(R.string.favorites, Icons.Default.Favorite, R.string.favorites),
    SHOPPING(R.string.shopping, Icons.Default.ShoppingCart, R.string.shopping),
    PROFILE(R.string.profile, Icons.Default.AccountBox, R.string.profile),
}

SampleNavigationSuiteScaffold.kt
```

To use `NavigationSuiteScaffold`, you must track the current destination, which
you can do by using `rememberSaveable`:

```
var currentDestination by rememberSaveable { mutableStateOf(AppDestinations.HOME) }

SampleNavigationSuiteScaffold.kt
```

In the following example, the `navigationSuiteItems` parameter (type
[`NavigationSuiteScope`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteScope)) uses its [`item`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteScope#item(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,kotlin.Function0,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) function
to define the navigation UI for an individual destination. The destination UI is
used across navigation bars, rails, and drawers. To create navigation items, you
loop over your `AppDestinations` (defined in the preceding snippet):

```
NavigationSuiteScaffold(
    navigationSuiteItems = {
        AppDestinations.entries.forEach {
            item(
                icon = {
                    Icon(
                        it.icon,
                        contentDescription = stringResource(it.contentDescription)
                    )
                },
                label = { Text(stringResource(it.label)) },
                selected = it == currentDestination,
                onClick = { currentDestination = it }
            )
        }
    }
) {
    // TODO: Destination content.
}

SampleNavigationSuiteScaffold.kt
```

Within the destination content lambda, use the `currentDestination` value to
decide what UI to display. If you use a navigation library in your app, use it
here to display the appropriate destination. A when statement can suffice:

```
NavigationSuiteScaffold(
    navigationSuiteItems = { /*...*/ }
) {
    // Destination content.
    when (currentDestination) {
        AppDestinations.HOME -> HomeDestination()
        AppDestinations.FAVORITES -> FavoritesDestination()
        AppDestinations.SHOPPING -> ShoppingDestination()
        AppDestinations.PROFILE -> ProfileDestination()
    }
}

SampleNavigationSuiteScaffold.kt
```

## Change colors

`NavigationSuiteScaffold` creates a [`Surface`](/reference/kotlin/androidx/compose/material3/Surface.composable#Surface(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.BorderStroke,kotlin.Function0)) over the entire area
the scaffold occupies, typically the full window. On top of that, the scaffold
draws the particular navigation UI, such as a [`NavigationBar`](/reference/kotlin/androidx/compose/material3/NavigationBar.composable#NavigationBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)).
Both the surface and the navigation UI use the values specified in your app's
theme, but you can override the theme values.

The `containerColor` parameter specifies the color of the surface. The default
is the background color of your color scheme. The `contentColor` parameter
specifies the color of content *on* that surface. The default is the "on" color
of whatever is specified for `containerColor`. For example, if `containerColor`
uses the `background` color, then `contentColor` uses the `onBackground` color.
See [Material Design 3 theming in Compose](/develop/ui/compose/designsystems/material3)
for more details about how the color system works. When overriding these values,
use values defined in your theme so your app supports dark and light display
modes:

```
NavigationSuiteScaffold(
    navigationSuiteItems = { /* ... */ },
    containerColor = MaterialTheme.colorScheme.primary,
    contentColor = MaterialTheme.colorScheme.onPrimary,
) {
    // Content...
}

SampleNavigationSuiteScaffold.kt
```

The navigation UI is drawn in front of the `NavigationSuiteScaffold` surface.
The default values for the UI colors are provided by
[`NavigationSuiteDefaults.colors()`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteDefaults#colors(androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color)), but you
can override these values as well. For example, if you want the background of
the navigation bar to be transparent but the other values to be the defaults,
override `navigationBarContainerColor`:

```
NavigationSuiteScaffold(
    navigationSuiteItems = { /* ... */ },
    navigationSuiteColors = NavigationSuiteDefaults.colors(
        navigationBarContainerColor = Color.Transparent,
    )
) {
    // Content...
}

SampleNavigationSuiteScaffold.kt
```

Ultimately, you can customize each item in the navigation UI. When calling the
[`item`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteScope#item(kotlin.Boolean,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function0,kotlin.Boolean,kotlin.Function0,androidx.compose.material3.adaptive.navigationsuite.NavigationSuiteItemColors,androidx.compose.foundation.interaction.MutableInteractionSource)) function, you can pass in an instance of
[`NavigationSuiteItemColors`](/reference/kotlin/androidx/compose/material3/adaptive/navigationsuite/NavigationSuiteItemColors). The class specifies
the colors for items in a navigation bar, navigation rail, and navigation
drawer. That means you can have identical colors across each navigation UI type,
or you can vary the colors based on your needs. Define the colors at the
`NavigationSuiteScaffold` level to use the same object instance for all items
and call the `NavigationSuiteDefaults.itemColors()` function to override only
the ones you want to change:

```
val myNavigationSuiteItemColors = NavigationSuiteDefaults.itemColors(
    navigationBarItemColors = NavigationBarItemDefaults.colors(
        indicatorColor = MaterialTheme.colorScheme.primaryContainer,
        selectedIconColor = MaterialTheme.colorScheme.onPrimaryContainer
    ),
)

NavigationSuiteScaffold(
    navigationSuiteItems = {
        AppDestinations.entries.forEach {
            item(
                icon = {
                    Icon(
                        it.icon,
                        contentDescription = stringResource(it.contentDescription)
                    )
                },
                label = { Text(stringResource(it.label)) },
                selected = it == currentDestination,
                onClick = { currentDestination = it },
                colors = myNavigationSuiteItemColors,
            )
        }
    },
) {
    // Content...
}

SampleNavigationSuiteScaffold.kt
```

## Customize navigation types

The default behavior of `NavigationSuiteScaffold` changes the navigation UI
based on [window size
classes](/develop/ui/compose/layouts/adaptive/window-size-classes). However, you
may want to override this behavior. For example, if your app shows a single
large pane of content for a feed, the app could use a permanent navigation
drawer for expanded windows but still fall back to the default behavior for
compact and medium window size classes:

```
val adaptiveInfo = currentWindowAdaptiveInfo()
val customNavSuiteType = with(adaptiveInfo) {
    if (windowSizeClass.isWidthAtLeastBreakpoint(WIDTH_DP_EXPANDED_LOWER_BOUND)) {
        NavigationSuiteType.NavigationDrawer
    } else {
        NavigationSuiteScaffoldDefaults.calculateFromAdaptiveInfo(adaptiveInfo)
    }
}

NavigationSuiteScaffold(
    navigationSuiteItems = { /* ... */ },
    layoutType = customNavSuiteType,
) {
    // Content...
}

SampleNavigationSuiteScaffold.kt
```

## Additional resources

* [Principles of navigation](/guide/navigation/navigation-principles)
* Material Design guidance:

  + [Navigation bar](https://m3.material.io/components/navigation-bar/overview)
  + [Navigation rail](https://m3.material.io/components/navigation-rail/overview)
  + [Navigation drawer](https://m3.material.io/components/navigation-drawer/overview)
* `androidx.compose.material3` library components:

  + [`NavigationBar`](/reference/kotlin/androidx/compose/material3/NavigationBar.composable#NavigationBar(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1))
  + [`NavigationRail`](/reference/kotlin/androidx/compose/material3/NavigationRail.composable#NavigationRail(androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1))
  + [`ModalNavigationDrawer`](/reference/kotlin/androidx/compose/material3/ModalNavigationDrawer.composable#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0))
  + [`PermanentNavigationDrawer`](/reference/kotlin/androidx/compose/material3/PermanentNavigationDrawer.composable#PermanentNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0))

[Previous

arrow\_back

Support camera on multiple form factors](/develop/ui/compose/layouts/adaptive/camera-form-factors-support)

[Next

Build a list-detail layout

arrow\_forward](/develop/ui/compose/layouts/adaptive/list-detail)