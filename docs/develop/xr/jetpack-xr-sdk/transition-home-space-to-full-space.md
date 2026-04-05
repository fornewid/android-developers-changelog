---
title: Transition from Home Space to Full Space  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Transition from Home Space to Full Space Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

A user can experience your app in two modes, Home Space or Full Space. In Home
Space, a user is able to multitask with your app running side by side with other
apps. In Full Space, your app takes center stage as the focus of the user's
experience with full access to the immersive capabilities of Android XR.

Your app opens in Home Space by default unless you specify otherwise as
described in the [Declare the default mode for launch](#declare-default-mode) section.

[Spatialization](/design/ui/xr/guides/foundations) is only supported in Full Space. Your app can transition to
Full Space to take advantage of spatial and 3D capabilities. When your app has
focus, you can transition between these modes by requesting the corresponding
space.

## Use `SpaceToggleButton` to switch between Home Space and Full Space

To transition between Home Space and Full Space use the
[`SpaceToggleButton`](/reference/kotlin/androidx/xr/compose/material3/SpaceToggleButton.composable#SpaceToggleButton(androidx.compose.ui.Modifier,androidx.compose.material3.IconToggleButtonColors,kotlin.Function1)) composable from the [Material Design for XR](/jetpack/androidx/releases/xr-compose-material3) library.

This is a composable button that adapts to the current spatial mode and toggles
between Full Space and Home Space.

## Build a custom transition between Home Space and Full Space

If you are using the Jetpack Compose for XR library, request home space or full
space using the [`LocalSession`](/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSession()) composition local.

```
val session = LocalSession.current ?: return
session.scene.requestHomeSpaceMode()
// or
session.scene.requestFullSpaceMode()

ModeTransition.kt
```

If you are using the Jetpack SceneCore library, you can request the
corresponding space from the [`Session`](/reference/kotlin/androidx/xr/runtime/Session); see [Access Session from Jetpack
SceneCore](/develop/xr/jetpack-xr-sdk/add-session#access-session).

```
xrSession.scene.requestHomeSpaceMode()

ModeTransition.kt
```

See the [Learn Android XR Fundamentals: Part 1 - Modes and Spatial Panels](/codelabs/xr-fundamentals-part-1#5)
codelab for examples of how to use these requests to transition between modes by
clicking a button. We also recommend reviewing our [design guidance](/design/ui/xr/guides/foundations) to learn
more about Home Space to Full Space and how to best transition between the two.

## Declare the default mode for launch

Alternatively, you can add the following lines to your Android Manifest file to
choose which space your app should open in:

```
<!-- Launch in Full Space. -->
<property
   android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
   android:value="XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED" />

<!-- Or, launch in Home Space. -->
<property
   android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
   android:value="XR_ACTIVITY_START_MODE_HOME_SPACE" />
```

**Note:** These manifest attributes can be declared at either the `<activity>` or
the `<application>` level in your app's manifest. Declaring at the activity
level will impact the launch preference for the activity element you apply it
to.

## See also

* [Check for spatial capabilities](/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
* [Create a session](/develop/xr/jetpack-xr-sdk/add-session)
* [Add environments to your app](/develop/xr/jetpack-xr-sdk/add-environments)
* [Add 3D models to your app](/develop/xr/jetpack-xr-sdk/add-3d-models)