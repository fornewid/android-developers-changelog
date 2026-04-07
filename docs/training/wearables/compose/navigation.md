---
title: Navigation with Compose for Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/compose/navigation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Navigation with Compose for Wear OS Stay organized with collections Save and categorize content based on your preferences.



Compose for Wear OS Material version

2.5
3


---

The [Navigation component](/guide/navigation) in Android Jetpack provides
support for Jetpack Compose applications. You can navigate between composables
while taking advantage of the Navigation component’s infrastructure and
features.

This page describes the differences with Jetpack Navigation on Compose for Wear
OS.

**Note:** If you are not familiar with the Navigation component, review the
[Navigating with Compose](/jetpack/compose/navigation) resources before
continuing.

## Setup

Use the following dependency in your app module’s build.gradle file:

### Kotlin

```
dependencies {
    def wear_compose_version = "1.6.0"
    implementation "androidx.wear.compose:compose-navigation:$wear_compose_version"
}
```

This is used **instead** of the `androidx.navigation:navigation-compose`
artifact because it provides alternative implementations specific to Wear OS.

## Create a navigation controller, host and graph

Navigating with Compose for Wear OS requires the same three components needed on
non-Wear OS apps: the navigation controller, host and graph.

Use
[`rememberSwipeDismissableNavController()`](/reference/kotlin/androidx/wear/compose/navigation/package-summary#rememberSwipeDismissableNavController())
to create an instance of `WearNavigator`, an implementation of `NavController`
suitable for Wear OS applications:

```
val navController = rememberSwipeDismissableNavController()

Navigation.kt
```

The [`NavController`](/reference/kotlin/androidx/navigation/NavController) is
the primary API used to navigate in Compose applications. It controls navigating
between composables in the navigation host which, on Wear OS, is
[`SwipeDismissableNavHost`](/reference/kotlin/androidx/wear/compose/navigation/package-summary#SwipeDismissableNavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,androidx.wear.compose.navigation.SwipeDismissableNavHostState,kotlin.String,kotlin.Function1)).

```
val navController = rememberSwipeDismissableNavController()
SwipeDismissableNavHost(
    navController = navController,
    startDestination = "message_list"
) {
    // TODO: build navigation graph
}

Navigation.kt
```

Like the
[`NavHost` composable](/reference/kotlin/androidx/navigation/compose/package-summary#NavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,kotlin.String,kotlin.Function1)),
it takes a reference to the navigation controller, the route for the start
destination, and the builder for the navigation graph which is shown here as a
trailing lambda.

The start destination must be provided in the navigation graph builder, along
with all other destinations that should be navigable with the navigation
controller.

In your Wear OS app, declare [`SwipeDismissableNavHost`](/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable#SwipeDismissableNavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState)) as a content of the
[`AppScaffold`](/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1)) to support top-level components like time, scroll or
position indicator, and page indicator.
Use a [`AppScaffold`](/reference/kotlin/androidx/wear/compose/material3/package-summary#AppScaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1)) object above the [`SwipeDismissableNavHost`](/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable#SwipeDismissableNavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState))
and the [`ScreenScaffold`](/reference/kotlin/androidx/wear/compose/material3/package-summary#ScreenScaffold(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2)) at the screen level to add a `TimeText` object
to the screen by default and to make sure it animates correctly when navigating
between screens.
Additionally, `ScreenScaffold` adds a `PositionIndicator` for scrollable content.

```
    AppScaffold {
        val navController = rememberSwipeDismissableNavController()
        SwipeDismissableNavHost(
            navController = navController,
            startDestination = "message_list"
        ) {
            composable("message_list") {
                MessageList(onMessageClick = { id ->
                    navController.navigate("message_detail/$id")
                })
            }
            composable("message_detail/{id}") {
                MessageDetail(id = it.arguments?.getString("id")!!)
            }
        }
    }
}

// Implementation of one of the screens in the navigation
@Composable
fun MessageDetail(id: String) {
    // .. Screen level content goes here
    val scrollState = rememberTransformingLazyColumnState()

    val padding = rememberResponsiveColumnPadding(
        first = ColumnItemType.BodyText
    )

    ScreenScaffold(
        scrollState = scrollState,
        contentPadding = padding
    ) { scaffoldPaddingValues ->
        // Screen content goes here
        // ...

Navigation.kt
```

To learn more about Jetpack Navigation, see
[Navigating with Compose](/jetpack/compose/navigation) or take the
[Jetpack Compose Navigation code lab](/codelabs/jetpack-compose-navigation).

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Migrate Jetpack Navigation to Navigation Compose](/develop/ui/compose/migrate/migration-scenarios/navigation)
* [Navigation with Compose](/develop/ui/compose/navigation)
* [Navigate between screens with Compose](/codelabs/basic-android-kotlin-compose-navigation/index.lab)