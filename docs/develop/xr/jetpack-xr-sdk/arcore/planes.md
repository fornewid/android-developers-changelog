---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

ARCore for Jetpack XR can detect flat surfaces in the user's environment and
provide information on them such as their pose, size, and orientation. This can
help your app find surfaces like tables to place objects on.

## Access a session

Access plane information through an ARCore for Jetpack XR [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session). If
you're enhancing [spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose) using Jetpack Compose for XR, [access a session
from Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#localsession). If you're working with
[spatialized entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities) from the Jetpack SceneCore library, [access a session
from Jetpack XR Runtime](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Plane detection is not enabled by default on XR sessions. To enable plane
tracking, configure the session and set the
[`PlaneTrackingMode.HORIZONTAL_AND_VERTICAL`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.PlaneTrackingMode#HORIZONTAL_AND_VERTICAL()) mode:


```kotlin
val newConfig = session.config.copy(
    planeTracking = Config.PlaneTrackingMode.HORIZONTAL_AND_VERTICAL,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}
```

<br />

> [!NOTE]
> **Note:** Plane tracking requires the `android.permission.SCENE_UNDERSTANDING_COARSE` [runtime permission](https://developer.android.com/training/permissions/requesting) to be granted to your app.

## Retrieve the state of perceived planes

ARCore for Jetpack XR provides the state of planes through a
[`StateFlow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/) that emits the state of planes. Subscribing to
planes in a session notifies your app when planes are added, updated, or
removed.


```kotlin
Plane.subscribe(session).collect { planes ->
    // Planes have changed; update plane rendering
}
```

<br />

A plane has the following properties:

- [`label`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.State#label()): a semantic description of a given [`Plane`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane). Could be a [`WALL`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.Label#WALL()), [`FLOOR`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.Label#FLOOR()), [`CEILING`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.Label#CEILING()), or [`TABLE`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.Label#TABLE()).
- [`centerPose`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.State#centerPose()): The pose of the center of the detected plane.
- [`extents`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.State#extents()): The dimensions of the detected plane, in meters.
- [`vertices`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Plane.State#vertices()): A list of vertices of a convex polygon that approximates the plane.

### Perform a hit-test against planes

A hit-test is a method of calculating the intersection of a ray with objects
tracked by the session. A common application of a hit-test is to point at a
table and place an object at that location. Conducting a hit-test results in a
list of hit objects. In other words, a hit-test doesn't stop at the first object
hit. However, often you may only be interested in the first object hit of a
given type.

To perform a hit-test, use [`Interaction.hitTest()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/package-summary#hittest) with a [`Ray`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Ray):


```kotlin
val results = androidx.xr.arcore.hitTest(session, ray)
// When interested in the first Table hit:
val tableHit = results.firstOrNull {
    val trackable = it.trackable
    trackable is Plane && trackable.state.value.label == Plane.Label.TABLE
}
```

<br />