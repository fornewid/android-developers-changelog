---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

With ARCore for Jetpack XR, your app can retrieve a device's *pose*: the
orientation (pitch, yaw, roll) and a position (X, Y, Z) of the device relative
to the world origin.

> [!NOTE]
> **Note:** The accuracy of the positional data varies depending on the sensors and capabilities of the user's device.

Use this information to render digital content in the real world, or convert the
device pose to a geospatial pose to generate location-aware data.

## Access a session

Access device pose information through a Jetpack XR Runtime [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session),
which your [app must create](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore#access-session-runtime).

## Configure the session

Device pose information is not enabled by default on XR sessions. To enable your
app to retrieve device pose information, configure the session and set the
[`DeviceTrackingMode.LAST_KNOWN`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/DeviceTrackingMode#LAST_KNOWN()) mode:

    // Define the configuration object to enable tracking device pose.
    val newConfig = session.config.copy(
        deviceTrackingMode = DeviceTrackingMode.LAST_KNOWN
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

Not all XR devices support the `DeviceTrackingMode.LAST_KNOWN` mode. If
[`Session.configure()`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)) succeeds, the device supports this mode.

> [!NOTE]
> **Note:** Enabling this mode on immersive devices requires the `android.permission.HEAD_TRACKING` \[runtime permission\]\[requesting-permissions\] to be granted to your app.

## Obtain the device pose

Once the session is configured, you can obtain the device's pose within the AR
coordinate system using the [`ArDevice`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/ArDevice) object:

    // Get the ArDevice instance
    val arDevice = ArDevice.getInstance(session)

    // Collect the state to process the device pose
    arDevice.state.collect { state ->
          // processDevicePose gets called automatically when a new pose is available.
          processDevicePose(state.devicePose)
    }

    // Or, get the current device Pose from the AR Device's state.
    // This is the device's position and orientation relative to the tracking origin.
    val devicePose = ArDevice.getInstance(session).state.value.devicePose

## Get the device pose's translation and rotation

The device `Pose` represents the device's position (translation) and orientation
(rotation) relative to the tracking origin. Use this information in your app to
enhance your app's experience:

1. **Provide positionally accurate navigation instructions**: Positional data
   can be used to help a user orient themselves and navigate their surroundings
   with help from overlaid digital content.

2. **Intermediate world alignment** : This pose is consumed by the [Geospatial
   API](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial) to calculate the real-world location.

    fun processDevicePose(pose: Pose) {

        // Extract Translation and Rotation
        val translation = pose.translation // Vector3(x, y, z)
        val rotation = pose.rotation // Quaternion (x, y, z, w)

        TODO(/* Use the translation and rotation in your app. */)
    }

## Convert the device pose to a geospatial pose

Once you have the device pose, you can obtain a geospatial pose from it.
Converting to a geospatial pose takes your AR content from a temporary, isolated
experience to a permanent, universally shared, and context-aware feature in the
real world.

Learn how to [convert a device pose to a geospatial pose](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial#convert-device-pose) in our Geospatial
API documentation.