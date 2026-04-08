---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

The [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session) provides the primary interface to spatialized functionality
for your app. Each spatialized `Activity` must create and hold an instance of
`Session`. After your app creates a session, it can use the `Session` interfaces
to create spatialized content entities such as panels or 3d models, as well as
[set a spatial environment](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments), [identify user position](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialUser), and [anchor
content](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities) to the real world.

> [!CAUTION]
> **Caution:** Due to a [known issue](https://developer.android.com/jetpack/androidx/releases/xr-scenecore#1.0.0-alpha04) that ties the session to the Activity lifecycle, the session can become invalid in various situations that automatically recreate the activity. These include, but are not limited to resizing a main panel, connecting peripherals, and changing between light and dark theme. If you run into session invalidation issues, you may need to make your main panel non-resizable, use a dynamic panel entity, disable activity recreation for [specific config changes](https://developer.android.com/guide/topics/resources/runtime-changes#restrict-activity), or disable light or dark theme changes.

## Access a session from Jetpack Compose for XR

When using Jetpack Compose for XR, the session is created for you and can be
accessed using [`LocalSession.current`](https://developer.android.com/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSession()). See the following example:


```kotlin
@Composable
fun ComposableUsingSession() {
    val session = LocalSession.current
}
```

<br />

## Access a session from Jetpack XR Runtime

If you're creating spatialized entities from the Jetpack SceneCore library,
you'll need to create a session.

To create a session, pass an activity to the [`create()`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#create(android.app.Activity,kotlin.coroutines.CoroutineContext))
method, as shown in the following example:


```kotlin
when (val result = Session.create(this)) {
    is SessionCreateSuccess -> {
        val xrSession = result.session
        // ...
    }
    else ->
        TODO(/* A different unhandled exception was thrown. */)
}
```

<br />

> [!NOTE]
> **Note:** You can only create a session on either an Android XR device, or on a [supported ARCore device](https://developers.google.com/ar/devices).

> [!NOTE]
> **Note:** Some features, such as [hand tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/hands) and [plane tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes), require additional runtime permissions in order for session configuration to succeed.

When a session's activity is destroyed, all spatial UI and 3D content associated
with that session is destroyed and the session is no longer valid.

## See also

- [Check for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
- [Transition between HSM and FSM](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
- [Add spatial environments to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments)
- [Add 3D models to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models)