---
title: Work with geospatial poses using ARCore for Jetpack XR  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Work with geospatial poses using ARCore for Jetpack XR Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

With the Geospatial API in ARCore for Jetpack XR, your app can remotely attach
content to any area covered by Google [Street View](https://www.google.com/streetview/) and create AR
experiences on a global scale. The Geospatial API uses device sensor and GPS
data to detect the device's environment, then matches the recognizable parts of
that environment to a localization model provided by Google's Visual Positioning
System (VPS) to determine the precise location of a user's device. The API also
takes care of merging the user's local coordinates with the geographic
coordinates from VPS so that you can work within a single coordinate system.

## Enable the ARCore API

Before using the Visual Positioning System (VPS) in your app, you must first
enable the [ARCore API](https://developers.google.com/ar/develop/authorization?platform=java) in a new or existing Google Cloud
project. This service is responsible for hosting, storing, and resolving
Geospatial anchors.

**Preview:** For ARCore in Jetpack XR, only API Key authorization is supported.
Keyless authorization isn't enabled yet.

## Add additional library dependencies

Using the Geospatial API requires some additional library dependencies. Add
these to your app's `build.gradle.kts` file:

### Groovy

```
dependencies {
  // ... Other required dependencies for the Jetpack XR SDK
  implementation "com.google.android.gms:play-services-location:21.3.0"
}
```

### Kotlin

```
dependencies {
  // ... Other required dependencies for the Jetpack XR SDK
  implementation("com.google.android.gms:play-services-location:21.3.0")
}
```

## Request required permissions

To use the Geospatial API in ARCore with Jetpack XR, your app needs to request
the following runtime permissions:

* [`ACCESS_INTERNET`](/training/basics/network-ops/connecting): Required to contact the ARCore Geospatial API cloud
  service.
* [`ACCESS_COARSE_LOCATION`](/training/location/permissions): Required to determine a user's [approximate
  location](/develop/sensors-and-location/location/permissions#accuracy).
* [`ACCESS_FINE_LOCATION`](/training/location/permissions): Required to determine a user's [precise
  location](/develop/sensors-and-location/location/permissions#accuracy).

### Declare app permissions

Before you can request these permissions at runtime, you need to [declare
them](/training/permissions/declaring) in your app's manifest:

```
<manifest ... >
  <uses-permission android:name="android.permission.INTERNET" />
  <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
  <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
</manifest>
```

### Request permissions

After declaring the required permissions, your app must [request them at
runtime](/training/permissions/requesting). Make sure to [explain why your app needs the permissions](/training/permissions/requesting#explain).

The Geospatial API can't function unless it can determine the user's precise
location. Because of this, follow the guidance for [requesting location
permissions at runtime](/develop/sensors-and-location/location/permissions/runtime) so that your app can be granted both the
`ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` permissions.

**Preview:** There is a known issue where the Android XR system doesn't enforce
these location permissions. We are working on a fix for this issue.

## Access a session

Access geospatial information through a Jetpack XR Runtime [`Session`](/reference/kotlin/androidx/xr/runtime/Session),
which your [app must create](/develop/xr/jetpack-xr-sdk/arcore#access-session-runtime).

## Configure the session

Device pose information is not enabled by default on XR sessions. To enable your
app to retrieve device pose information, configure the session and set both the
[`GeospatialMode.VPS_AND_GPS`](/reference/kotlin/androidx/xr/runtime/GeospatialMode#VPS_AND_GPS()) and [`DeviceTrackingMode.LAST_KNOWN`](/reference/kotlin/androidx/xr/runtime/DeviceTrackingMode#LAST_KNOWN())
modes:

```
// Define the configuration object to enable Geospatial features.
val newConfig = Config(
    // Set the GeospatialMode to VPS_AND_GPS.
    geospatial = GeospatialMode.VPS_AND_GPS,
    // Set the DeviceTrackingMode to LAST_KNOWN.
    deviceTracking = DeviceTrackingMode.LAST_KNOWN
)
// Apply the configuration to the session.
try {
    when (val configResult = session.configure(newConfig)) {
        is SessionConfigureSuccess -> {
            // The session is now configured to use the Geospatial API.
        }
        else -> {
            // Handle other configuration errors (e.g., missing library dependencies).
        }
    }
} catch (e: UnsupportedOperationException) {
    // Handle configuration failure if the mode is not supported.
}

Geospatial.kt
```

The `GeospatialMode.VPS_AND_GPS` mode leverages both **Visual Positioning System
(VPS)** and
**Global Positioning System (GPS)** data to accurately determine the device's
geospatial position.

Not all XR devices support the `GeospatialMode.VPS_AND_GPS` and
`DeviceTrackingMode.LAST_KNOWN` modes. If [`Session.configure()`](/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)) succeeds,
the device supports these modes.

## Prompt user to allow usage of device data

Apps that use the Geospatial API with ARCore for Jetpack XR must present the
user with a prompt to acknowledge and allow the use of data from their device.
See the [user privacy requirements](https://developers.google.com/ar/develop/privacy-requirements) for more information.

## Obtain the Geospatial object

Once the session is configured, obtain the [`Geospatial`](/reference/kotlin/androidx/xr/arcore/Geospatial) object using
[`Geospatial.getInstance(session)`](/reference/kotlin/androidx/xr/arcore/Geospatial#getInstance(androidx.xr.runtime.Session)):

```
// Get the Geospatial instance for the current session.
val geospatial = Geospatial.getInstance(session)

Geospatial.kt
```

The `Geospatial` object should only be used when its state is
[`State.RUNNING`](/reference/kotlin/androidx/xr/arcore/Geospatial.State#RUNNING()). You can monitor the state using the
[`Geospatial.state`](/reference/kotlin/androidx/xr/arcore/Geospatial#state()) `StateFlow<Geospatial.State>`.

## Check VPS availability

Because the Geospatial API uses a combination of [VPS](https://developers.google.com/ar/develop/geospatial#global_localization_with_vps) and GPS
to determine a Geospatial pose, the API is available whenever the device can
determine its location. In areas with low GPS accuracy, such as indoor spaces
and dense urban environments, the API relies on VPS coverage to generate
high-accuracy poses.

Under typical conditions, you can expect VPS to provide positional accuracy of
approximately 5 meters and rotational accuracy of 5 degrees. You can check if a
location has VPS coverage using the suspend function
[`Geospatial.checkVpsAvailability(latitude, longitude)`](/reference/kotlin/androidx/xr/arcore/Geospatial#checkVpsAvailability(kotlin.Double,kotlin.Double)). This call is an
asynchronous operation and doesn't require the session to be configured with
the [`GeospatialMode.VPS_AND_GPS`](/reference/kotlin/androidx/xr/runtime/GeospatialMode#VPS_AND_GPS()) mode.

The following code demonstrates how to check the VPS availability from a
specified latitude and longitude:

```
// You can query the GPS to get the current device's location.
val latitude = 37.422
val longitude = -122.084

// Use the geospatial instance to check VPS availability for a specific location.
val result = geospatial.checkVpsAvailability(latitude, longitude)
when (result) {
    is VpsAvailabilityAvailable -> {
        // VPS is available at this location.
    }
    is VpsAvailabilityErrorInternal -> {
        // VPS availability check failed with an internal error.
    }
    is VpsAvailabilityNetworkError -> {
        // VPS availability check failed due to a network error.
    }
    is VpsAvailabilityNotAuthorized -> {
        // VPS availability check failed due to an authorization error.
    }
    is VpsAvailabilityResourceExhausted -> {
        // VPS availability check failed due to resource exhaustion.
    }
    is VpsAvailabilityUnavailable -> {
        // VPS is not available at this location.
    }
}

Geospatial.kt
```

Your app must be [properly set up to communicate with the ARCore API on Google
Cloud](https://developers.google.com/ar/develop/authorization?platform=android); otherwise, your app receives a
[`VpsAvailabilityNotAuthorized`](/reference/kotlin/androidx/xr/runtime/VpsAvailabilityNotAuthorized) result.

## Convert a device pose to a geospatial pose

You can convert a device pose to a geospatial pose to enable AI glasses to
interact with and generate location-aware data. This pipeline translates the
device's current position and orientation in its local coordinate system (device
pose) into globally-recognized coordinates.

This can help you:

* Author persistent AR content, where a user's placed virtual object is
  accurately anchored to a global location for later retrieval.
* Trigger location-based experiences by continuously updating the user's
  position on a map to enable real-time navigation or geo-fenced gameplay.
* Determine the user's precise real-world context for triggering
  location-relevant application logic.

To convert a [device pose](/develop/xr/jetpack-xr-sdk/arcore/device-pose) to a geospatial pose using
[`Geospatial.createGeospatialPoseFromPose()`](/reference/kotlin/androidx/xr/arcore/Geospatial#createGeospatialPoseFromPose(androidx.xr.runtime.math.Pose)):

```
// Get the current device Pose from the AR Session's state.
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
}

Geospatial.kt
```

## Convert a geospatial pose to a device pose

You can convert a geospatial pose to a device pose to help deliver contextual,
location-aware experiences on AI glasses. This transformation
takes information defined by real-world coordinates—such as the location of a
landmark, a navigation path, or persistent AR content—and converts it into the
precise visual space of the user's glasses.

To convert a geospatial pose to a device pose using
[`Geospatial.createPoseFromGeospatialPose()`](/reference/kotlin/androidx/xr/arcore/Geospatial#createPoseFromGeospatialPose(androidx.xr.runtime.math.GeospatialPose)):

```
// Convert a GeospatialPose (lat/long/alt) back to a device-space Pose.
when (val result = geospatial.createPoseFromGeospatialPose(geoPose)) {
    is CreatePoseFromGeospatialPoseSuccess -> {
        val devicePose: Pose = result.pose
        // devicePose is now ready to be used relative to the tracking origin.
    }
    is CreatePoseFromGeospatialPoseNotTracking -> {
        // Geospatial is not currently tracking.
    }
}

Geospatial.kt
```