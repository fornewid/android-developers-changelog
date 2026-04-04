---
title: Create anchors with ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Create anchors with ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

An Anchor describes a fixed location and orientation in the real world.
Attaching an object to an anchor helps objects appear realistically placed in
the real world.

## Access a session

Create anchors through an ARCore for Jetpack XR [`Session`](/reference/kotlin/androidx/xr/runtime/Session). If you're
enhancing [spatial UI](/develop/xr/jetpack-xr-sdk/ui-compose) using Jetpack Compose for XR, [access a session from
Jetpack Compose for XR](/develop/xr/jetpack-xr-sdk/add-session#localsession). If you're working with [spatialized entities](/develop/xr/jetpack-xr-sdk/work-with-entities)
from the Jetpack SceneCore library, [access a session from Jetpack XR
Runtime](/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Creating and loading anchors does not require the session to be configured.
However, anchor persistence is not enabled by default on XR sessions. To persist
and load anchors from local storage, configure the session and set the
[`AnchorPersistenceMode.LOCAL`](/reference/kotlin/androidx/xr/runtime/AnchorPersistenceMode#LOCAL()) mode:

```
val newConfig = session.config.copy(
    anchorPersistence = AnchorPersistenceMode.LOCAL,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}

Anchors.kt
```

**Note:** Creating, loading, and persisting anchors requires the
`android.permission.SCENE_UNDERSTANDING_COARSE` [runtime permission](/training/permissions/requesting) to be
granted to your app.

## Anchor content to a fixed location in space

An anchor is created using a [`Pose`](/reference/kotlin/androidx/xr/runtime/math/Pose), which can be interpreted relative to
an existing [`Anchorable`](/reference/kotlin/androidx/xr/arcore/Anchorable) or not. An `Anchorable` is a [`Trackable`](/reference/kotlin/androidx/xr/arcore/Trackable)
that can have anchors attached to it.

### Create an anchor relative to an Anchorable

When an anchor is created relative to an `Anchorable`, such as a `Plane`, which
makes the anchor follow the attached `Anchorable` when it moves through space.

```
when (val result = anchorable.createAnchor(pose)) {
    is AnchorCreateSuccess -> { /* anchor stored in `result.anchor`. */ }
    else -> { /* handle failure */ }
}

Anchors.kt
```

### Create an anchor without an Anchorable

To create an anchor that isn't attached to an `Anchorable`:

```
when (val result = Anchor.create(session, pose)) {
    is AnchorCreateSuccess -> { /* anchor stored in `result.anchor`. */ }
    else -> { /* handle failure */ }
}

Anchors.kt
```

### Attach an entity to an anchor

To render a model at this location, [create a `GltfModel`](/develop/xr/jetpack-xr-sdk/add-3d-models#place-3d) and set its
parent to an `AnchorEntity`.

```
AnchorEntity.create(session, anchor).apply {
    parent = session.scene.activitySpace
    addChild(entity)
}

Anchors.kt
```

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

To persist an anchor, use [`Anchor.persist()`](/reference/kotlin/androidx/xr/arcore/Anchor#persist) as shown here:

```
val uuid = anchor.persist()

AnchorPersistence.kt
```

Your app can retrieve the anchor by using the [`UUID`](/reference/java/util/UUID) in a future session:

```
when (val result = Anchor.load(session, uuid)) {
    is AnchorCreateSuccess -> {
        // Loading was successful. The anchor is stored in result.anchor.
    }
    else -> {
        // handle failure
    }
}

AnchorPersistence.kt
```

When you don't need an anchor anymore, call [`unpersist()`](/reference/kotlin/androidx/xr/arcore/Anchor#unpersist(androidx.xr.runtime.Session,java.util.UUID)). This removes
the anchor from your app's storage and makes the given UUID unretrievable for
calls to [`Anchor.load()`](/reference/kotlin/androidx/xr/arcore/Anchor#load).

```
Anchor.unpersist(session, uuid)

AnchorPersistence.kt
```

Your app can also request a list of all anchors that have been persisted that
are still present in your app's storage:

```
val uuids = Anchor.getPersistedAnchorUuids(session)

AnchorPersistence.kt
```