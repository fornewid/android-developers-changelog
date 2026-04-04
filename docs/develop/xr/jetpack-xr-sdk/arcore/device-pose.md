---
title: Track a device's pose using ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Track a device's pose using ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

With ARCore for Jetpack XR, your app can retrieve a device's *pose*: the
orientation (pitch, yaw, roll) and a position (X, Y, Z) of the device relative
to the world origin.

**Note:** The accuracy of the positional data varies depending on the sensors and
capabilities of the user's device.

Use this information to render digital content in the real world, or convert the
device pose to a geospatial pose to generate location-aware data.

## Access a session

Access device pose information through a Jetpack XR Runtime [`Session`](/reference/kotlin/androidx/xr/runtime/Session),
which your [app must create](/develop/xr/jetpack-xr-sdk/arcore#access-session-runtime).

## Configure the session

Device pose information is not enabled by default on XR sessions. To enable your
app to retrieve device pose information, configure the session and set the
[`DeviceTrackingMode.LAST_KNOWN`](/reference/kotlin/androidx/xr/runtime/DeviceTrackingMode#LAST_KNOWN()) mode:

```
// Define the configuration object to enable tracking device pose.
val newConfig = session.config.copy(
    deviceTracking = DeviceTrackingMode.LAST_KNOWN
)
// Apply the configuration to the session.
try {
    when (val configResult = session.configure(newConfig)) {
        is SessionConfigureSuccess -> {
            // The session is now configured to track the device's pose.
        }
        else -> {
            // Catch-all for other configuration errors returned using the result class.
        }
    }
} catch (e: UnsupportedOperationException) {
    // Handle configuration failure. For example, if the specific mode is not supported on the current device or API version.
}

DevicePose.kt
```

Not all XR devices support the `DeviceTrackingMode.LAST_KNOWN` mode. If
[`Session.configure()`](/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)) succeeds, the device supports this mode.

**Note:** Enabling this mode on immersive devices requires the
`android.permission.HEAD_TRACKING` [runtime permission](/guide/topics/permissions/overview#runtime) to be granted to your
app.

## Obtain the device pose

After you've configured the session, you can obtain the device's pose within the
AR coordinate system using the [`ArDevice`](/reference/kotlin/androidx/xr/arcore/ArDevice) object:

```
// Get the ArDevice instance
val arDevice = ArDevice.getInstance(session)
// There are two ways to get the device pose.

// 1. Get the current device pose once.
// This is the device's position and orientation relative to the tracking origin.
val devicePose = arDevice.state.value.devicePose
processDevicePose(devicePose)

// 2. Continuously receive updates for the device pose.
// `collect` is a suspending function that will run indefinitely and process new poses.
arDevice.state.collect { state ->
    processDevicePose(state.devicePose)
}

DevicePose.kt
```

## Get the device pose's translation and rotation

The device `Pose` represents the device's position (translation) and orientation
(rotation) relative to the tracking origin. Use this information in your app to
enhance your app's experience:

1. **Provide positionally accurate navigation instructions**: Positional data
   can be used to help a user orient themselves and navigate their surroundings
   with help from overlaid digital content.
2. **Calculate intermediate world alignment**: This pose is consumed by the
   [Geospatial API](/develop/xr/jetpack-xr-sdk/arcore/geospatial) to calculate the real-world location.

```
fun processDevicePose(pose: Pose) {
    // Extract Translation and Rotation
    val translation = pose.translation // Vector3(x, y, z)
    val rotation = pose.rotation // Quaternion (x, y, z, w)
    TODO(/* Use the translation and rotation in your app. */)
}

DevicePose.kt
```

## Convert the device pose to a geospatial pose

Once you have the device pose, you can obtain a geospatial pose from it.
Converting to a geospatial pose takes your AR content from a temporary, isolated
experience to a permanent, universally shared, and context-aware feature in the
real world.

Learn how to [convert a device pose to a geospatial pose](/develop/xr/jetpack-xr-sdk/arcore/geospatial#convert-device-pose) in the Geospatial
API documentation.