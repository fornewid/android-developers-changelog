---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-follow-target
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-follow-target
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

While a standard [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/Subspace.composable) stays at a fixed position that's determined by
the system, sometimes you might want your app's spatial UI to move dynamically
with the user or stay attached to a specific location in its environment or in
the real world. You can pass a [`FollowTarget`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowTarget) to the `follow` parameter of
[`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/Subspace.composable#Subspace(androidx.xr.compose.subspace.animation.follow.FollowTarget,androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.Function1)) to build experiences like head-locked HUDs or information panels
attached to real-world objects.

> [!NOTE]
> **Note:** The `Subspace` API with the `follow` parameter is experimental and requires opting in with `@OptIn(ExperimentalFollowingSubspaceApi::class)`.

## Add a subspace that follows the user's view

To add a subspace that's positioned relative to the user's field of view, use
[`FollowTarget.view`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowTarget#view(androidx.xr.compose.subspace.animation.follow.FollowMode)). [Depending on the follow mode you specify](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspace-follow-target#follow-modes), this
lets you continuously track the user's head movements or place content
statically based on where they are looking. You could use this for things like
HUDs, persistent notifications, or quick-action controls.

### Declare and request permissions

Before requesting permissions, you must [declare them in your app's manifest](https://developer.android.com/training/permissions/declaring)
file using the [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element) element.

    <manifest ...>
        <!-- Only declare permissions that your app actually needs. In this example,
        we declare permissions for head tracking. -->
        <uses-permission android:name="android.permission.HEAD_TRACKING"/>
        <application ...>
            ...
        </application>
    </manifest>

Now request the permissions. For more information, review the [permission
principles and workflows](https://developer.android.com/training/permissions/requesting#principles) to make sure you provide the best experience for
your users, like [checking whether the user has already granted the runtime
permissions](https://developer.android.com/training/permissions/requesting#already-granted) your app requires and [whether your app should show a
rationale](https://developer.android.com/training/permissions/requesting#explain) to the user before requesting this permission.

### Configure your session

Next, you'll configure your app's [session that is created for you when using
Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#localsession) by setting [`DeviceTrackingMode.SPATIAL`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DeviceTrackingMode#SPATIAL()):

    val session = checkNotNull(LocalSession.current)
    session.configure(
        config = Config.Builder(session.config).setDeviceTracking(DeviceTrackingMode.SPATIAL)
            .build()
    )

### Create the subspace

Finally, you'll create a subspace that targets the user's view, together with a
follow mode:

    // Example: A subspace that softly follows the user's view (like a HUD)
    Subspace(
        follow = FollowTarget.view(
            // Customizing the soft follow to move slightly faster and tracking all dimensions
            mode = FollowMode.soft(
            )
        ),
        modifier = modifier,
    ) {
        SpatialPanel {
          // SpatialPanel Content
        }
    }

#### Follow modes for subspaces that target a user's view

When you use [`FollowTarget.view`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowTarget#view(androidx.xr.compose.subspace.animation.follow.FollowMode)) as your target, you can customize how the
content behaves by specifying a [`FollowMode`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowMode):

- [`FollowMode.soft`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowMode#soft(androidx.xr.compose.subspace.animation.follow.TrackedDimensions,kotlin.Long,kotlin.Long,androidx.xr.compose.subspace.animation.follow.FollowThresholds)): The content gradually catches up to the target's movements, creating a smooth floating effect.
- [`FollowMode.snap`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowMode#snap(androidx.xr.compose.subspace.animation.follow.TrackedDimensions)): The content is placed in front of the user once based on their initial view pose and stays stationary afterward.
- [`FollowMode.tight`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowMode#tight(androidx.xr.compose.subspace.animation.follow.TrackedDimensions)): The content tracks the user's view immediately with minimal delay, keeping content closely tethered to their movement.

All follow modes let you choose which dimensions of movement are tracked from
the following options:

- X axis
- Y axis
- Pitch
- Roll
- Yaw
- [`RotationOnly`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/TrackedDimensions#RotationOnly()): Lets you specify a single value to track the dimensions that are related to rotation (pitch, yaw, and roll).

You can choose any combination of these dimensions, or use the default value of
[`TrackedDimensions.All`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/TrackedDimensions#All()) that tracks them all.

## Add a subspace that follows an environmental feature

To add a subspace that locks the spatial content strictly to a physical feature
in the user's environment, use [`FollowTarget.anchor()`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/follow/FollowTarget#anchor(androidx.xr.arcore.Anchor,androidx.xr.compose.subspace.animation.follow.FollowMode)). Use this type of
target to follow a detected plane, an anchor, or a geospatial location.

Tracking real-world features requires additional permissions and session
configurations depending on the feature you're following.

For detailed instructions on working with [perception capabilities for ARCore
features](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore), as well as setting up the necessary permissions and configuring
your session to use `FollowTarget.anchor()`, see the Jetpack XR SDK
documentation for [Planes](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/planes), [Anchors](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/anchors), and [Geospatial poses](https://developer.android.com/partners/xr/geospatial-poses).

The following example creates a subspace that follows a real-world anchor:

    // A subspace locked to a real-world anchor
    Subspace(
        follow = FollowTarget.anchor(anchor = myAnchor)
    ) {
        // Rotate the panel to ensure it faces the user while remaining anchored
        SpatialPanel(SubspaceModifier.rotateToLookAtUser()) {
          // SpatialPanel Content
        }
    }

## Avoid spatial overlap

Each `Subspace` you create manages its own independent 3D scene and has no
awareness of other subspaces that exist, so it doesn't automatically avoid
collisions.

To prevent your head-locked HUD from clipping through your anchored POI panels
(Z-fighting), explicitly manage your layout volumes using these methods:

1. **Use offsets** : Use [`SubspaceModifier.offset`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).offset(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) to push peripheral UI (like your HUD) closer or further away on the Z-axis, or shift it to the edges of the user's vision.
2. **Restrict sizes** : Apply modifiers like [`requiredSizeIn`](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/layout/SubspaceModifier#(androidx.xr.compose.subspace.layout.SubspaceModifier).requiredSizeIn(androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp)) to constrain the bounding boxes of your spaces.

For more information about coordinate spaces, layout constraints, and all of the
available tracking configurations, see the [`Subspace`](https://developer.android.com/reference/kotlin/androidx/xr/compose/spatial/Subspace.composable#Subspace(androidx.xr.compose.subspace.layout.SubspaceModifier,kotlin.Function1)) reference
documentation.