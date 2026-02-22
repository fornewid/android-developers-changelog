---
title: https://developer.android.com/develop/ui/compose/system/predictive-back-setup
url: https://developer.android.com/develop/ui/compose/system/predictive-back-setup
source: md.txt
---

Predictive back and system animations are enabled by default. If your app
intercepts the back event and you haven't migrated to predictive back,
[update your app to use supported back navigation APIs](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#update-custom)
The predictive back-to-home animation. The predictive cross-activity animation. The predictive cross-task animation.

## Enable default system animations

The back-to-home, cross-activity, and cross-task system animations are available
on Android 15 and later devices for apps that have migrated to the supported
back handling APIs.

- **Back-to-home**: Returns the user to the home screen.
- **Cross-activity**: Transitions between activities within the app.
- **Cross-task** : Transitions between [tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack).

These animations are enabled by default on Android 15 and higher. On devices
running Android 13 or 14, users can enable them through the
[Developer options](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture#dev-option).

> [!NOTE]
> **Note:** Intercepting back at the root activity (e.g. `MainActivity.kt`) disables the back-to-home animation, and intercepting back at an Activity disables the cross-activity animation.

To get the system animations, update your AndroidX `Activity` dependency
to [1.6.0](https://developer.android.com/jetpack/androidx/releases/activity#version_160_3) or higher.

## Enable predictive back with Navigation Compose

To use predictive back in Navigation Compose, ensure you're using the
`navigation-compose` [2.8.0](https://developer.android.com/jetpack/androidx/releases/navigation#2.8.0)
library or higher.

Navigation Compose automatically cross-fades between screens when the user
swipes back:
**Figure 2.** The default crossfade in-app animation in SociaLite.

When navigating, you can create custom transitions with
[`popEnterTransition`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#NavHost(androidx.navigation.NavHostController,kotlin.Any,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.reflect.KClass,kotlin.collections.Map,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1)) and [`popExitTransition`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#NavHost(androidx.navigation.NavHostController,kotlin.Any,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.reflect.KClass,kotlin.collections.Map,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1)). When applied to your
`NavHost`, these modifiers let you define how the enter and exit screens
animate. You can use them to create a variety of effects, such as scaling,
fading, or sliding.

In this example, `scaleOut` is used within `popExitTransition` to scale down
the exiting screen as the user navigates back. Additionally, the
`transformOrigin` parameter determines the point around which the scaling
animation occurs. By default, it's the center of the screen (`0.5f, 0.5f`).
You can adjust this value to make the scaling originate from a different point.


```kotlin
NavHost(
    navController = navController,
    startDestination = Home,
    popExitTransition = {
        scaleOut(
            targetScale = 0.9f,
            transformOrigin = TransformOrigin(pivotFractionX = 0.5f, pivotFractionY = 0.5f)
        )
    },
    popEnterTransition = {
        EnterTransition.None
    },
    modifier = modifier,
)
```

<br />

This code produces the following result:
**Figure 3.** A custom in-app animation in SociaLite.

`popEnterTransition` and `popExitTransition` specifically control animations
when popping the back stack, with a back gesture, for example. You can also use `enterTransition` and `exitTransition` to define animations for entering and
exiting composables in general, not only for predictive back. If you only set `enterTransition` and `exitTransition`, they are used for both regular
navigation and popping the back stack. However, using `popEnterTransition` and `popExitTransition` lets you create distinct animations for back navigation.

## Integrate with shared element transitions

Shared element transitions provide a smooth visual connection between
composables with shared content, often used for navigation.
**Figure 4.** Shared element transition with predictive back in Navigation Compose.

To use shared elements with Navigation Compose, see
[Predictive back with shared elements](https://developer.android.com/develop/ui/compose/animation/shared-elements/navigation#predictive-back).

## Support predictive back with Material Compose components

Many components in the Material Compose library are designed to work seamlessly
with predictive back gestures. To enable predictive back animations in these
components, include the latest [Material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) dependency (`androidx.compose.material3:material3-*:1.3.0` or higher) in your project.

The Material components that support predictive back animations include:

- [`SearchBar`](https://m3.material.io/components/search/guidelines#3f2d4e47-2cf5-4c33-b6e1-5368ceaade55)
- [`ModalBottomSheet`](https://m3.material.io/components/bottom-sheets/guidelines#c72ba2b1-906d-4cfa-9a6a-91e79555bad0)
- [`ModalDrawerSheet/DismissibleDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.material3.DrawerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1))
- [`ModalNavigationDrawer/DismissibleNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.material3.DrawerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1))

[`SearchBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#SearchBar(kotlin.Function0,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.material3.SearchBarColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)) and [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalBottomSheet(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.SheetState,androidx.compose.ui.unit.Dp,kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ModalBottomSheetProperties,kotlin.Function1)) automatically animate with
predictive back gestures. [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,androidx.compose.ui.graphics.Color,kotlin.Function0)),
[`ModalDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ModalDrawerSheet(androidx.compose.material3.DrawerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)), [`DismissibleDrawerSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DismissibleDrawerSheet(androidx.compose.material3.DrawerState,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.foundation.layout.WindowInsets,kotlin.Function1)), and
[`DismissibleNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#DismissibleNavigationDrawer(kotlin.Function0,androidx.compose.ui.Modifier,androidx.compose.material3.DrawerState,kotlin.Boolean,kotlin.Function0)) require you to pass the `drawerState` to
their respective sheet content composables.

## Test the predictive back gesture animation

If you still use Android 13 or Android 14, you can test the back-to-home
animation.

To test this animation, follow these steps:

1. On your device, go to **Settings \> System \> Developer options**.
2. Select **Predictive back animations**.
3. Launch your updated app, and use the back gesture to see it in action.

On Android 15 and later, this feature is enabled by default.

## Additional resources

- [Add predictive back animations codelab](https://developer.android.com/codelabs/predictive-back#0)
- [Advanced layout animations in Compose video](https://www.youtube.com/watch?v=PR6rz1QUkAM&t=1195s&ab_channel=AndroidDevelopers)