---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/positioning
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/positioning
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

A [`GeospatialPose`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/GeospatialPose) describes a position in space relative to
the Earth. It is composed of the following components:

- Latitude and longitude, which is specified in degrees as defined by the [WGS84 specification](https://nsgreg.nga.mil/doc/view?i=4085).
- Altitude, which is specified in meters above the WGS84 ellipsoid, or roughly equivalent to meters above sea level.
- Orientation, which approximates the direction the pose is facing in the EUS coordinate system. The EUS coordinate system has X+ pointing east, Y+ pointing up, and Z+ pointing south.

The Geospatial API provides access to the device's Geospatial pose and provides
conversions between Geospatial poses and [device-local poses](https://developer.android.com/reference/kotlin/androidx/xr/runtime/math/pose).

## Prerequisites

In order to obtain and convert Geospatial poses, your app must be [set up to use
the Geospatial API](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/setup). Geospatial poses can only be obtained
when [the Geospatial API has a `RUNNING` state](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/setup#geospatial-instance).

## Convert a device-local pose to a Geospatial pose

A device-local `Pose` can be converted to a `GeospatialPose`, for example, to
determine the position of the user's device relative to Earth. This can help
you:

- Author persistent AR content, where a user's placed virtual object is accurately anchored to a global location for later retrieval.
- Trigger location-based experiences by continuously updating the user's position on a map to enable real-time navigation or geo-fenced gameplay.
- Determine the user's precise real-world context for triggering location-relevant application logic.

The following code sample demonstrates how to convert a `Pose` to a
`GeospatialPose` using
[`Geospatial.createGeospatialPoseFromPose()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createGeospatialPoseFromPose(androidx.xr.runtime.math.Pose)).


```kotlin
val devicePose = ArDevice.getInstance(session).state.value.devicePose

// Convert the device Pose into a GeospatialPose.
when (val result = geospatial.createGeospatialPoseFromPose(devicePose)) {
    is CreateGeospatialPoseFromPoseSuccess -> {
        val geoPose = result.pose
        val lat = geoPose.latitude
        val lon = geoPose.longitude
        val alt = geoPose.altitude
        // Orientation is in the EUS (East-Up-South) coordinate system.
        val orientation = geoPose.eastUpSouthQuaternion
    }
    is CreateGeospatialPoseFromPoseNotTracking -> {
        // Geospatial is not currently tracking.
    }

    else -> {
        // A newer exception was added, but your app is using an old version of the library
    }
}
```

<br />

## Convert a Geospatial pose to a device-local pose

You can also convert a `GeospatialPose` to a device-local `Pose`. This
transformation takes information defined by real-world coordinates, such as the
location of a landmark, a navigation path, or persistent AR content, and
converts it into the precise visual space of the user's device.

> [!NOTE]
> **Note:** To anchor 3D content to a Geospatial pose, use a [Geospatial anchor](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/anchors) instead. Geospatial anchors automatically update their device-local pose as the quality of the Geospatial tracking increases.

The following code sample demonstrates how to use
[`Geospatial.createPoseFromGeospatialPose()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createPoseFromGeospatialPose(androidx.xr.runtime.math.GeospatialPose))
to convert a Geospatial pose to a device-local pose.


```kotlin
// Convert a GeospatialPose (lat/long/alt) back to a device-space Pose.
when (val result = geospatial.createPoseFromGeospatialPose(geoPose)) {
    is CreatePoseFromGeospatialPoseSuccess -> {
        val devicePose: Pose = result.pose
        // devicePose is now ready to be used relative to the tracking origin.
    }
    is CreatePoseFromGeospatialPoseNotTracking -> {
        // Geospatial is not currently tracking.
    }
    is CreatePoseFromGeospatialPoseInternalError -> {
        // An internal error occurred.
    }
    else -> {
        // A newer exception was added, but your app is using an old version of the library
    }
}
```

<br />