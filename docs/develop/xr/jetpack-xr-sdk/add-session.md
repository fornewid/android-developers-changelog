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
to create spatialized content entities such as panels or 3D models, as well as
[set a spatial environment](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments), [identify user position](https://developer.android.com/reference/kotlin/androidx/xr/scenecore/SpatialUser), and [anchor
content](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities) to the real world.

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

To create a session, pass a [`Context`](https://developer.android.com/reference/kotlin/android/content/Context) to the
[`create()`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#create(android.content.Context,kotlin.coroutines.CoroutineContext,androidx.lifecycle.LifecycleOwner)) method. This `Context` can be an `Activity` on
immersive XR devices or mobile devices, or a
[projected context](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware-projected-context) on Intelligent Eyewear.

Creating an ARCore session can be an expensive task, and should be
[processed in the background](https://developer.android.com/develop/background-work/background-tasks/asynchronous), as shown in
the following example:


```kotlin
lifecycleScope.launch {
    when (val result = Session.create(context)) {
        is SessionCreateSuccess -> {
            val xrSession = result.session
            // ...
        }
        else ->
            TODO(/* A different unhandled exception was thrown. */)
    }
}
```

<br />

> [!NOTE]
> **Note:** You can only create a session on either an Android XR device, or on a [supported ARCore device](https://developers.google.com/ar/devices). See [`SessionCreateResult`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/SessionCreateResult) to see reasons why a session may not be able to be created.

The `create()` function can use an optional
[`LifecycleOwner`](https://developer.android.com/reference/kotlin/androidx/lifecycle/LifecycleOwner) parameter, which allows the
session's lifecycle to be managed by a different `LifecycleOwner`. The
`LifecycleOwner` must begin and end its lifecycle within the scope of the
provided context, otherwise the `Session` may be prone to leaks.

> [!NOTE]
> **Note:** Some features, such as [hand tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/hands) and [plane tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes), require additional runtime permissions in order for session configuration to succeed.

## See also

- [Check for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities)
- [Transition between HSM and FSM](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)
- [Add spatial environments to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments)
- [Add 3D models to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models)