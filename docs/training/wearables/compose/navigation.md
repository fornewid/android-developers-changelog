---
title: https://developer.android.com/training/wearables/compose/navigation
url: https://developer.android.com/training/wearables/compose/navigation
source: md.txt
---

> Documentation index: https://developer.android.com/training/wearables/compose/llms.txt

Compose for Wear OS Material version <button value="2.5">2.5</button> <button value="3" default="">3</button>

*** ** * ** ***

<br />

The [Navigation component](https://developer.android.com/guide/navigation.md.txt) in Android Jetpack provides
support for Jetpack Compose applications. You can navigate between composables
while taking advantage of the Navigation component's infrastructure and
features.

This page describes the differences with Jetpack Navigation on Compose for Wear
OS.

> [!NOTE]
> **Note:** If you are not familiar with the Navigation component, review the [Navigating with Compose](https://developer.android.com/jetpack/compose/navigation) resources before continuing.

## Setup

Use the following dependency in your app module's build.gradle file:

### Kotlin

```kotlin
dependencies {
    def wear_compose_version = "1.7.2"
    implementation "androidx.wear.compose:compose-navigation:$wear_compose_version"
}
```

This is used **instead** of the `androidx.navigation:navigation-compose`
artifact because it provides alternative implementations specific to Wear OS.

## Create a navigation controller, host and graph

Navigating with Compose for Wear OS requires the same three components needed on
non-Wear OS apps: the navigation controller, host and graph.

Use
[`rememberSwipeDismissableNavController()`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary.md.txt#rememberSwipeDismissableNavController())
to create an instance of `WearNavigator`, an implementation of `NavController`
suitable for Wear OS applications:


```kotlin
val navController = rememberSwipeDismissableNavController()
```

<br />

The [`NavController`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController.md.txt) is
the primary API used to navigate in Compose applications. It controls navigating
between composables in the navigation host which, on Wear OS, is
[`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/package-summary.md.txt#SwipeDismissableNavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,androidx.wear.compose.navigation.SwipeDismissableNavHostState,kotlin.String,kotlin.Function1)).


```kotlin
val navController = rememberSwipeDismissableNavController()
SwipeDismissableNavHost(
    navController = navController,
    startDestination = "message_list"
) {
    // TODO: build navigation graph
}
```

<br />

Like the
[`NavHost` composable](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary.md.txt#NavHost(androidx.navigation.NavHostController,kotlin.String,androidx.compose.ui.Modifier,kotlin.String,kotlin.Function1)),
it takes a reference to the navigation controller, the route for the start
destination, and the builder for the navigation graph which is shown here as a
trailing lambda.

The start destination must be provided in the navigation graph builder, along
with all other destinations that should be navigable with the navigation
controller.
In your Wear OS app, declare [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable.md.txt#SwipeDismissableNavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState)) as a content of the [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary.md.txt#AppScaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1)) to support top-level components like time, scroll or position indicator, and page indicator. Use a [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary.md.txt#AppScaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1)) object above the [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable.md.txt#SwipeDismissableNavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState)) and the [`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary.md.txt#ScreenScaffold(androidx.wear.compose.foundation.lazy.ScalingLazyListState,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,kotlin.Function0,kotlin.Function1,androidx.compose.ui.unit.Dp,kotlin.Function2)) at the screen level to add a `TimeText` object to the screen by default and to make sure it animates correctly when navigating between screens. Additionally, `ScreenScaffold` adds a `PositionIndicator` for scrollable content.

```kotlin
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
    val transformationSpec = rememberTransformationSpec()

    ScreenScaffold(
        scrollState = scrollState,
    ) { contentPadding ->
        // Screen content goes here
        // ...
```

## Display dialogs

To display a dialog using Material 3 for Compose on Wear OS---such as
[`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/AlertDialog.composable.md.txt), [`ConfirmationDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ConfirmationDialog.composable.md.txt), [`OpenOnPhoneDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/OpenOnPhoneDialog.composable.md.txt),
or [`Dialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/Dialog.composable.md.txt)---declare the dialog composable directly inside the screen
composable destination that opens it. To do so, complete these steps:

1. Control the dialog's visibility using a boolean state variable, and pass that state to the dialog's `visible` parameter. Use either `rememberSaveable` or a state that's hoisted to a `ViewModel`.
2. In the `onDismissRequest` callback, and in any other confirmation or dismissal action callbacks, set the state variable to `false`. That way, the dialog animates out and returns to the underlying screen when the user swipes to dismiss or chooses an action.

For more information, see the [`AlertDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/AlertDialog.composable.md.txt), [`ConfirmationDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ConfirmationDialog.composable.md.txt),
and [`OpenOnPhoneDialog`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/OpenOnPhoneDialog.composable.md.txt) API reference documentation.

> [!NOTE]
> **Note:** To show a smooth animation in your app, don't add dialogs as separate `composable` destinations in [`SwipeDismissableNavHost`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation/SwipeDismissableNavHost.composable.md.txt#SwipeDismissableNavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.wear.compose.navigation.SwipeDismissableNavHostState)).  
>
> When using Material 3 for Compose on Wear OS, dialog components are full-screen overlays that provide their own entry and exit animations. The system also scales the parent window when launched inside an [`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/package-summary.md.txt#AppScaffold(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function1)), and the system handles the swipe-to-dismiss gesture.

To learn more about Jetpack Navigation, see
[Navigating with Compose](https://developer.android.com/jetpack/compose/navigation) or take the
[Jetpack Compose Navigation code lab](https://developer.android.com/codelabs/jetpack-compose-navigation).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate Jetpack Navigation to Navigation Compose](https://developer.android.com/develop/ui/compose/migrate/migration-scenarios/navigation.md.txt)
- [Navigation with Compose](https://developer.android.com/guide/navigation.md.txt#framework-options)
- [Navigate between screens with Compose](https://developer.android.com/codelabs/basic-android-kotlin-compose-navigation)