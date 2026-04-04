---
title: Access a session for creating spatialized UI and entities  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Access a session for creating spatialized UI and entities Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

The [`Session`](/reference/kotlin/androidx/xr/runtime/Session) provides the primary interface to spatialized functionality
for your app. Each spatialized `Activity` must create and hold an instance of
`Session`. After your app creates a session, it can use the `Session` interfaces
to create spatialized content entities such as panels or 3d models, as well as
[set a spatial environment](/develop/xr/jetpack-xr-sdk/add-environments), [identify user position](/reference/kotlin/androidx/xr/scenecore/SpatialUser), and [anchor
content](/develop/xr/jetpack-xr-sdk/work-with-entities) to the real world.

**Caution:** Due to a [known issue](/jetpack/androidx/releases/xr-scenecore#1.0.0-alpha04) that ties the session to the Activity
lifecycle, the session can become invalid in various situations that
automatically recreate the activity. These include, but are not limited to
resizing a main panel, connecting peripherals, and changing between light and
dark theme. If you run into session invalidation issues, you may need to make
your main panel non-resizable, use a dynamic panel entity, disable activity
recreation for [specific config changes](/guide/topics/resources/runtime-changes#restrict-activity), or disable light or dark theme
changes.

## Access a session from Jetpack Compose for XR

When using Jetpack Compose for XR, the session is created for you and can be
accessed using [`LocalSession.current`](/reference/kotlin/androidx/xr/compose/platform/package-summary#LocalSession()). See the following example:

```
@Composable
fun ComposableUsingSession() {
    val session = LocalSession.current
}

Session.kt
```

## Access a session from Jetpack XR Runtime

If you're creating spatialized entities from the Jetpack SceneCore library,
you'll need to create a session.

To create a session, pass an activity to the [`create()`](/reference/kotlin/androidx/xr/runtime/Session#create(android.app.Activity,kotlin.coroutines.CoroutineContext))
method, as shown in the following example:

```
when (val result = Session.create(this)) {
    is SessionCreateSuccess -> {
        val xrSession = result.session
        // ...
    }
    else ->
        TODO(/* A different unhandled exception was thrown. */)
}

Session.kt
```

**Note:** You can only create a session on either an Android XR device, or on a
[supported ARCore device](https://developers.google.com/ar/devices).**Note:** Some features, such as [hand tracking](/develop/xr/jetpack-xr-sdk/arcore/hands) and [plane tracking](/develop/xr/jetpack-xr-sdk/arcore/planes),
require additional runtime permissions in order for session configuration to
succeed.

When a session's activity is destroyed, all spatial UI and 3D content associated
with that session is destroyed and the session is no longer valid.

## See also

* [Check for spatial capabilities](/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
* [Transition between HSM and FSM](/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
* [Add spatial environments to your app](/develop/xr/jetpack-xr-sdk/add-environments)
* [Add 3D models to your app](/develop/xr/jetpack-xr-sdk/add-3d-models)