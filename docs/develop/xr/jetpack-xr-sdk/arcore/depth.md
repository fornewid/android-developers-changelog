---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Your app can retrieve depth information through ARCore for Jetpack XR to
determine how close physical objects are to the device.


Your browser doesn't support HTML video. Here is a
[link to the video](https://developer.android.com/static/develop/xr/develop/videos/arcore_raw_depth.mp4) instead.

## Create an ARCore for Jetpack XR session

Obtain depth information through an ARCore for Jetpack XR
[`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session). If you're enhancing [spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose) using Jetpack Compose
for XR, [access a session from Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#localsession). If you're working
with [spatialized entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities) from the Jetpack SceneCore library, [access a
session from Jetpack XR Runtime](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Depth map retrieval is not enabled by default on XR sessions. To enable depth
map retrieval, configure the session and set a
[`DepthEstimationMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.DepthEstimationMode):


```kotlin
val newConfig = session.config.copy(
    depthEstimation = Config.DepthEstimationMode.SMOOTH_ONLY,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}
```

<br />

The following values of `DepthEstimationMode` are available:

- `DISABLED`: No information about scene depth is provided.
- `RAW_ONLY`: Depth estimation is enabled with raw depth and confidence values.
- `SMOOTH_ONLY`: Depth estimation is enabled with smooth depth and confidence values.
- `SMOOTH_AND_RAW`: Depth estimation is enabled with both raw and smooth depth and confidence values.

Raw depth maps provide depth estimates with higher accuracy, but raw depth
images might not include depth estimates for all pixels in the camera image. In
contrast, the smooth depth maps provide estimated depth for every pixel, but
per-pixel depth data might be less accurate due to smoothing and interpolation
of depth estimates.

> [!NOTE]
> **Note:** Enabling any depth estimation mode requires the `android.permission.SCENE_UNDERSTANDING_FINE` [runtime permission](https://developer.android.com/training/permissions/requesting) to be granted to your app.

## Retrieve depth data

To obtain depth data for a given camera, use [`DepthMap`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/DepthMap):


```kotlin
val depthMap = DepthMap.left(session) ?: returnhttps://github.com/android/snippets/blob/ed5bd1be020d430170fb3f14a1636696195f5733/xr/src/main/java/com/example/xr/arcore/DepthMaps.kt#L40-L40
```

<br />

Different devices have different capabilities. Devices with a stereo camera
configuration return non-null depth maps for the `left` and `right` cameras.
Likewise, devices with a singular camera return a non-null depth map using
`mono`.

## Calculate depth values

You can obtain depth and confidence values from the resulting depth map:


```kotlin
val depthMap = DepthMap.left(session) ?: returnhttps://github.com/android/snippets/blob/ed5bd1be020d430170fb3f14a1636696195f5733/xr/src/main/java/com/example/xr/arcore/DepthMaps.kt#L40-L40
```

<br />

Depending on the configuration setting used, access the corresponding depth map
using `smoothDepthMap` or `rawDepthMap`. Measurements contained in these maps
are expressed in meters. You can also access the confidence values using
`smoothConfidenceMap` and `rawConfidenceMap`. These values range from 0 to 255,
where 255 represents the highest confidence.

To render a depth map for debug or visualization purposes, see the [Depth part
of the ARCore test app](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:xr/arcore/integration-tests/testapp/src/main/kotlin/androidx/xr/arcore/testapp/depthmaps/).