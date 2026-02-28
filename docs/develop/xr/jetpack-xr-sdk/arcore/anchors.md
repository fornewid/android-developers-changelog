---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

An Anchor describes a fixed location and orientation in the real world.
Attaching an object to an anchor helps objects appear realistically placed in
the real world.

## Access a session

Create anchors through an ARCore for Jetpack XR [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session). If you're
enhancing [spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose) using Jetpack Compose for XR, [access a session from
Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#localsession). If you're working with [spatialized entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities)
from the Jetpack SceneCore library, [access a session from Jetpack XR
Runtime](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Creating and loading anchors does not require the session to be configured.
However, anchor persistence is not enabled by default on XR sessions. To persist
and load anchors from local storage, configure the session and set the
[`AnchorPersistenceMode.LOCAL`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/AnchorPersistenceMode#LOCAL()) mode:


```kotlin
val newConfig = session.config.copy(
    anchorPersistence = AnchorPersistenceMode.LOCAL,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}
```

<br />

> [!NOTE]
> **Note:** Creating, loading, and persisting anchors requires the `android.permission.SCENE_UNDERSTANDING_COARSE` [runtime permission](https://developer.android.com/training/permissions/requesting) to be granted to your app.

## Anchor content to a fixed location in space

An anchor is created using a [`Pose`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/Pose), which can be interpreted relative to
an existing [`Trackable`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Trackable) or not.

### Create an anchor relative to a Trackable

When an anchor is created relative to a `Trackable`, such as a `Plane`, which
makes the anchor follow the attached `Trackable` when it moves through space.


```kotlin
when (val result = trackable.createAnchor(pose)) {
    is AnchorCreateSuccess -> { /* anchor stored in `result.anchor`. */ }
    else -> { /* handle failure */ }
}
```

<br />

### Create an anchor without a Trackable

To create an anchor that isn't attached to a `Trackable`:


```kotlin
when (val result = Anchor.create(session, pose)) {
    is AnchorCreateSuccess -> { /* anchor stored in `result.anchor`. */ }
    else -> { /* handle failure */ }
}
```

<br />

### Attach an entity to an anchor

To render a model at this location, [create a `GltfModel`](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-3d-models#place-3d) and set its
parent to an `AnchorEntity`.


```kotlin
AnchorEntity.create(session, anchor).apply {
    parent = session.scene.activitySpace
    addChild(entity)
}
```

<br />

## Understand TrackingState

Each `Trackable` has a `TrackingState` that should be checked before being used.
A `Trackable` that has a `TrackableState` of `Tracking` has its `Pose` actively
updated by the system. A `Trackable` that is `Paused` may become `Tracking` in
the future, whereas one that is `Stopped` will never become `Tracking`.

## Persist an Anchor throughout sessions

An anchor that is not persisted disappears after a session is destroyed. By
persisting an anchor, your app remembers that anchor's position in its private
app data. This anchor can be retrieved in a subsequent session and is anchored
in the same location in the world.

To persist an anchor, use [`Anchor.persist()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#persist) as shown here:


```kotlin
val uuid = anchor.persist()
```

<br />

Your app can retrieve the anchor by using the [`UUID`](https://developer.android.com/reference/java/util/UUID) in a future session:


```kotlin
when (val result = Anchor.load(session, uuid)) {
    is AnchorCreateSuccess -> {
        // Loading was successful. The anchor is stored in result.anchor.
    }
    else -> {
        // handle failure
    }
}
```

<br />

When you don't need an anchor anymore, call [`unpersist()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#unpersist(androidx.xr.runtime.Session,java.util.UUID)). This removes
the anchor from your app's storage and makes the given UUID unretrievable for
calls to [`Anchor.load()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Anchor#load).


```kotlin
Anchor.unpersist(session, uuid)
```

<br />

Your app can also request a list of all anchors that have been persisted that
are still present in your app's storage:


```kotlin
val uuids = Anchor.getPersistedAnchorUuids(session)
```

<br />