---
title: Retrieve depth information in your app with ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Retrieve depth information in your app with ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

Your app can retrieve depth information through ARCore for Jetpack XR to
determine how close physical objects are to the device.

[


Your browser doesn't support HTML video. Here is a
[link to the video](/static/develop/xr/develop/videos/arcore_raw_depth.mp4) instead.

](/static/develop/xr/jetpack-xr-sdk/videos/arcore_raw_depth.mp4)

## Create an ARCore for Jetpack XR session

Obtain depth information through an ARCore for Jetpack XR
[`Session`](/reference/kotlin/androidx/xr/runtime/Session). If you're enhancing [spatial UI](/develop/xr/jetpack-xr-sdk/ui-compose) using Jetpack Compose
for XR, [access a session from Jetpack Compose for XR](/develop/xr/jetpack-xr-sdk/add-session#localsession). If you're working
with [spatialized entities](/develop/xr/jetpack-xr-sdk/work-with-entities) from the Jetpack SceneCore library, [access a
session from Jetpack XR Runtime](/develop/xr/jetpack-xr-sdk/add-session#access-session).

## Configure the session

Depth map retrieval is not enabled by default on XR sessions. To enable depth
map retrieval, configure the session and set a
[`DepthEstimationMode`](/reference/kotlin/androidx/xr/runtime/DepthEstimationMode):

```
val newConfig = session.config.copy(
    depthEstimation = DepthEstimationMode.SMOOTH_ONLY,
)
when (val result = session.configure(newConfig)) {
    is SessionConfigureSuccess -> TODO(/* Success! */)
    else ->
        TODO(/* The session could not be configured. See SessionConfigureResult for possible causes. */)
}

DepthMaps.kt
```

The following values of `DepthEstimationMode` are available:

* `DISABLED`: No information about scene depth is provided.
* `RAW_ONLY`: Depth estimation is enabled with raw depth and confidence
  values.
* `SMOOTH_ONLY`: Depth estimation is enabled with smooth depth and confidence
  values.
* `SMOOTH_AND_RAW`: Depth estimation is enabled with both raw and smooth depth
  and confidence values.

Raw depth maps provide depth estimates with higher accuracy, but raw depth
images might not include depth estimates for all pixels in the camera image. In
contrast, the smooth depth maps provide estimated depth for every pixel, but
per-pixel depth data might be less accurate due to smoothing and interpolation
of depth estimates.

**Note:** Enabling any depth estimation mode requires the
`android.permission.SCENE_UNDERSTANDING_FINE`
[runtime permission](/training/permissions/requesting) to be granted to your app.

## Retrieve depth data

To obtain depth data for a given camera, use [`DepthMap`](/reference/kotlin/androidx/xr/arcore/DepthMap):

```
val depthMap = DepthMap.left(session) ?: return

DepthMaps

.kt
```

Different devices have different capabilities. Devices with a stereo camera
configuration return non-null depth maps for the `left` and `right` cameras.
Likewise, devices with a singular camera return a non-null depth map using
`mono`.

## Calculate depth values

You can obtain depth and confidence values from the resulting depth map:

```
val depthMap = DepthMap.left(session) ?: return

DepthMaps

.kt
```

Depending on the configuration setting used, access the corresponding depth map
using `smoothDepthMap` or `rawDepthMap`. Measurements contained in these maps
are expressed in meters. You can also access the confidence values using
`smoothConfidenceMap` and `rawConfidenceMap`. These values range from 0 to 255,
where 255 represents the highest confidence.

To render a depth map for debug or visualization purposes, see the [Depth part
of the ARCore test app](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:xr/arcore/integration-tests/testapp/src/main/kotlin/androidx/xr/arcore/testapp/depthmaps/).