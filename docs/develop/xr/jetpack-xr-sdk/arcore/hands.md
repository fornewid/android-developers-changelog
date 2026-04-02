---
title: Work with hands using ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/hands
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Work with hands using ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

ARCore for Jetpack XR can provide information about the user's detected hands,
and gives pose information for hands and their associated joints. This hand data
can be used to attach entities and models to a user's hands, for example, a tool
menu:

[


Your browser doesn't support HTML video. Here is a
[link to the video](/static/develop/xr/jetpack-xr-sdk/videos/watch.mp4) instead.

](/static/develop/xr/jetpack-xr-sdk/videos/watch.mp4)

## Access a session

Access hand information through a Jetpack XR Runtime [`Session`](/reference/kotlin/androidx/xr/runtime/Session),
which your [app can create](/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Hand tracking is not enabled by default on XR sessions. To receive hand data,
configure the session and set the [`HandTrackingMode.BOTH`](/reference/kotlin/androidx/xr/runtime/HandTrackingMode#BOTH()) mode:

```
val newConfig = session.config.copy(
    handTracking = HandTrackingMode.BOTH
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}

Hands.kt
```

**Note:** Tracking the user's hands requires the `android.permission.HAND_TRACKING`
[runtime permission](/training/permissions/requesting) to be granted to your app.

## Retrieve hand data

Hand data is available for left and right hands separately. Use each hand's
`state` to access pose positions for each joint:

```
Hand.left(session)?.state?.collect { handState -> // or Hand.right(session)
    // Hand state has been updated.
    // Use the state of hand joints to update an entity's position.
    renderPlanetAtHandPalm(handState)
}

Hands.kt
```

Hands have the following properties:

* `trackingState`: whether or not the hand is being tracked.
* `handJoints`: a map of hand joints to poses. Hand joint poses are specified
  by the [OpenXR standards](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#convention-of-hand-joints).

  [


  Your browser doesn't support HTML video. Here is a
  [link to the video](/static/develop/xr/develop/videos/hand-debug.mp4) instead.

  ](/static/develop/xr/jetpack-xr-sdk/videos/hand-debug.mp4)

## Use hand data in your app

The positions of a user's hand joints can be used to [anchor 3D objects](/develop/xr/jetpack-xr-sdk/arcore/anchors#anchor-content) to a
user's hands, for example, to attach a model to the left palm:

```
val palmPose = leftHandState.handJoints[HandJointType.HAND_JOINT_TYPE_PALM] ?: return

// the down direction points in the same direction as the palm
val angle = Vector3.angleBetween(palmPose.rotation * Vector3.Down, Vector3.Up)
palmEntity.setEnabled(angle > Math.toRadians(40.0))

val transformedPose =
    session.scene.perceptionSpace.transformPoseTo(
        palmPose,
        session.scene.activitySpace,
    )
val newPosition = transformedPose.translation + transformedPose.down * 0.05f
palmEntity.setPose(Pose(newPosition, transformedPose.rotation))

Hands.kt
```

[


Your browser doesn't support HTML video. Here is a
[link to the video](/static/develop/xr/jetpack-xr-sdk/videos/left.mp4) instead.

](/static/develop/xr/jetpack-xr-sdk/videos/left.mp4)

Or to attach a model to your right hand's index finger tip:

```
val tipPose = rightHandState.handJoints[HandJointType.HAND_JOINT_TYPE_INDEX_TIP] ?: return

// the forward direction points towards the finger tip.
val angle = Vector3.angleBetween(tipPose.rotation * Vector3.Forward, Vector3.Up)
indexFingerEntity.setEnabled(angle > Math.toRadians(40.0))

val transformedPose =
    session.scene.perceptionSpace.transformPoseTo(
        tipPose,
        session.scene.activitySpace,
    )
val position = transformedPose.translation + transformedPose.forward * 0.03f
val rotation = Quaternion.fromLookTowards(transformedPose.up, Vector3.Up)
indexFingerEntity.setPose(Pose(position, rotation))

Hands.kt
```

[


Your browser doesn't support HTML video. Here is a
[link to the video](/static/develop/xr/jetpack-xr-sdk/videos/right.mp4) instead.

](/static/develop/xr/jetpack-xr-sdk/videos/right.mp4)

## Detect basic hand gestures

Use the poses of joints in the hand to detect basic hand gestures. Consult the
[Conventions of hand joints](https://registry.khronos.org/OpenXR/specs/1.0/html/xrspec.html#convention-of-hand-joints) to determine which range of poses
the joints should be in to register as a given pose.

For example, to detect a pinch with the thumb and the index finger, use the
distance between the two tip joints:

```
val thumbTip = handState.handJoints[HandJointType.HAND_JOINT_TYPE_THUMB_TIP] ?: return false
val thumbTipPose = session.scene.perceptionSpace.transformPoseTo(thumbTip, session.scene.activitySpace)
val indexTip = handState.handJoints[HandJointType.HAND_JOINT_TYPE_INDEX_TIP] ?: return false
val indexTipPose = session.scene.perceptionSpace.transformPoseTo(indexTip, session.scene.activitySpace)
return Vector3.distance(thumbTipPose.translation, indexTipPose.translation) < 0.05

Hands.kt
```

An example of a more complicated gesture is the "stop" gesture. In this gesture,
each finger should be outstretched, that is, each joint in each finger should
roughly be pointing in the same direction:

```
val threshold = toRadians(angleInDegrees = 30f)
fun pointingInSameDirection(joint1: HandJointType, joint2: HandJointType): Boolean {
    val forward1 = handState.handJoints[joint1]?.forward ?: return false
    val forward2 = handState.handJoints[joint2]?.forward ?: return false
    return Vector3.angleBetween(forward1, forward2) < threshold
}
return pointingInSameDirection(HandJointType.HAND_JOINT_TYPE_INDEX_PROXIMAL, HandJointType.HAND_JOINT_TYPE_INDEX_TIP) &&
    pointingInSameDirection(HandJointType.HAND_JOINT_TYPE_MIDDLE_PROXIMAL, HandJointType.HAND_JOINT_TYPE_MIDDLE_TIP) &&
    pointingInSameDirection(HandJointType.HAND_JOINT_TYPE_RING_PROXIMAL, HandJointType.HAND_JOINT_TYPE_RING_TIP)

Hands.kt
```

Keep the following points in mind when developing custom detection for hand
gestures:

* Users may have a different interpretation of any given gesture. For example,
  some may consider a "stop" gesture to have the fingers splayed out, while
  others may find it more intuitive to have the fingers close together.
* Some gestures may be uncomfortable to maintain. Use intuitive gestures that
  don't strain a user's hands.

## Determine the user's secondary hand

The Android system places system navigation on the user's primary hand, as
specified by the user in system preferences. Use the secondary hand for your
custom gestures to avoid conflicts with system navigation gestures:

```
val handedness = Hand.getPrimaryHandSide(activity.contentResolver)
val secondaryHand = if (handedness == Hand.HandSide.LEFT) Hand.right(session) else Hand.left(session)
val handState = secondaryHand?.state ?: return
detectGesture(handState)

Hands.kt
```

---

OpenXR™ and the OpenXR logo are trademarks owned
by The Khronos Group Inc. and are registered as a trademark in China,
the European Union, Japan and the United Kingdom.