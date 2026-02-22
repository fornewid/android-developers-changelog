---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

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

> [!WARNING]
> **Preview:** For ARCore in Jetpack XR, only API Key authorization is supported. Keyless authorization isn't enabled yet.

## Add additional library dependencies

Using the Geospatial API requires some additonal library dependencies. Add these
to your app's `build.gradle.kts` file:

### Groovy

```groovy
dependencies {
  // ... Other https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk#augmented
  implementation "com.google.android.gms:play-services-location:21.3.0"
}
```

### Kotlin

```kotlin
dependencies {
  // ... Other https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk#augmented
  implementation("com.google.android.gms:play-services-location:21.3.0")
}
```

## Request required permissions

To use the Geospatial API in ARCore with Jetpack XR, your app needs to request
the following runtime permissions:

- [`ACCESS_INTERNET`](https://developer.android.com/training/basics/network-ops/connecting): Required to contact the ARCore Geospatial API cloud service.
- [`ACCESS_COARSE_LOCATION`](https://developer.android.com/training/location/permissions): Required to determine a user's [approximate
  location](https://developer.android.com/develop/sensors-and-location/location/permissions#accuracy).
- [`ACCESS_FINE_LOCATION`](https://developer.android.com/training/location/permissions): Required to determine a user's [precise
  location](https://developer.android.com/develop/sensors-and-location/location/permissions#accuracy).

### Declare app permissions

Before you can request these permissions at runtime, you need to [declare
them](https://developer.android.com/training/permissions/declaring) in your app's manifest:

    <manifest ... >
      <uses-permission android:name="android.permission.INTERNET" />
      <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
      <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    </manifest>

### Request permissions

After declaring the required permissions, your app must [request them at
runtime](https://developer.android.com/training/permissions/requesting). Make sure to [explain why your app needs the permissions](https://developer.android.com/training/permissions/requesting#explain).

The Geospatial API can't function unless it can determine the user's precise
location. Because of this, follow the guidance for [requesting location
permissions at runtime](https://developer.android.com/develop/sensors-and-location/location/permissions/runtime) so that your app can be granted both the
`ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION` permissions.

> [!WARNING]
> **Preview:** There is a known issue where the Android XR system doesn't enforce these location permissions. We are working on a fix for this issue.

## Access a session

Access geospatial information through a Jetpack XR Runtime [`Session`](https://developers.google.com/ar/develop/fundamentals),
which your [app must create](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore#access-session-runtime).

## Configure the session

Device pose information is not enabled by default on XR sessions. To enable your
app to retrieve device pose information, configure the session and set both the
[`GeospatialMode.VPS_AND_GPS`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.GeospatialMode#VPS_AND_GPS()) and [`DeviceTrackingMode.LAST_KNOWN`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.DeviceTrackingMode#LAST_KNOWN())
modes:

    // Define the configuration object to enable Geospatial features.
    val newConfig = session.config.copy(
      // Set the GeospatialMode to VPS_AND_GPS.
      geospatial = Config.GeospatialMode.VPS_AND_GPS
      // Set the DeviceTrackingMode to LAST_KNOWN.
      deviceTracking = Config.DeviceTrackingMode.LAST_KNOWN
    )

    // Apply the configuration to the session.
    try {
        when (val configResult = session.configure(newConfig)) {
            is SessionConfigureGooglePlayServicesLocationLibraryNotLinked -> {
                // This case generally indicates a missing library dependency.
            }
            is SessionConfigureSuccess -> {
                // The session is now configured to use the Geospatial API.
            }
            else -> {
                // Catch-all for other configuration errors returned using the result class.
            }
        }
    } catch (e: UnsupportedOperationException) {
        // Handle configuration failure. For example, if the specific mode is not supported on the current device or API version.
    }

The `GeospatialMode.VPS_AND_GPS` mode leverages both **Visual Positioning System
(VPS)** and
**Global Positioning System (GPS)** data to accurately determine the device's
geospatial position.

Not all XR devices support the `GeospatialMode.VPS_AND_GPS` and
`DeviceTrackingMode.LAST_KNOWN` modes. If [`Session.configure()`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)) succeeds,
the device supports these modes.

## Prompt user to allow usage of device data

Apps that use the Geospatial API with ARCore for Jetpack XR must present the
user with a prompt to acknowledge and allow the use of data from their device.
See the [user privacy requirements](https://developers.google.com/ar/develop/privacy-requirements) for more information.

## Obtain the Geospatial object

Once the session is configured, obtain the [`Geospatial`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial) object using
[`Geospatial.getInstance(session)`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#getInstance(androidx.xr.runtime.Session)):

    // Get the Geospatial instance
    var geospatial = Geospatial.getInstance(session)

The `Geospatial` object should only be used when its state is
[`State.RUNNING`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.State#RUNNING()). You can monitor the state using the
[`Geospatial.state`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#state()) `StateFlow<Geospatial.State>`.

## Check VPS availability

Because the Geospatial API uses a combination of [VPS](https://developers.google.com/ar/develop/geospatial#global_localization_with_vps) and GPS
to determine a Geospatial pose, the API can be used as long as the device is
able to determine its location. In areas with low GPS accuracy, such as indoor
spaces and dense urban environments, the API relies on VPS coverage to generate
high accuracy poses.

Under typical conditions, you can expect VPS to provide positional accuracy of
approximately 5 meters, and rotational accuracy of 5 degrees. You can check if a
location has VPS coverage using the suspend function
[`Geospatial.checkVpsAvailability(latitude, longitude)`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#checkVpsAvailability(kotlin.Double,kotlin.Double)). This call is an
asynchronous operation and does not require the session to be configured with
the [`GeospatialMode.VPS_AND_GPS`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Config.GeospatialMode#VPS_AND_GPS()) mode.

The following code demonstrates how to check the VPS availability from a
specified latitude and longitude:

    // You can query the GPS to get the current device's location and check if it has VPS
    val latitude = getLatitudeFromGPS()
    val longitude = getLongitudeFromGPS()

    // Must be called from a coroutine.
    val result = geospatial.checkVpsAvailability(latitude, longitude)
    if (result is VpsAvailabilityAvailable) {
      // VPS is available
    } else if (result is VpsAvailabilityUnavailable) {
      // VPS is not available
    }

Your app must be [properly set up to communicate with the ARCore API on Google
Cloud](https://developers.google.com/ar/develop/authorization?platform=android); otherwise, your app will receive a
[`VpsAvailabilityNotAuthorized`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/VpsAvailabilityNotAuthorized) result.

## Convert a device pose to a geospatial pose

You can convert a device pose to a geospatial pose to enable AI glasses to
interact with and generate location-aware data. This pipeline translates the
device's current position and orientation in its local coordinate system (device
pose) into globally-recognized coordinates.

This can help you:

- Author persistent AR content, where a user's placed virtual object is accurately anchored to a global location for later retrieval.
- Trigger location-based experiences by continuously updating the user's position on a map to enable real-time navigation or geo-fenced gameplay.
- Determine the user's precise real-world context for triggering location-relevant application logic.

To convert a [device pose](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose) to a geospatial pose using
[`Geospatial.createGeospatialPoseFromPose()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createGeospatialPoseFromPose(androidx.xr.runtime.math.Pose)):

    // Get the current https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose from the AR Session's state
    // This is the device's position and orientation relative to the AR tracking origin.
    val devicePose = ArDevice.getInstance(session).state.value.devicePose

    // Convert the device Pose into a GeospatialPose
    when (val geospatialPoseResult = geospatial.createGeospatialPoseFromPose(devicePose)) {
        is CreateGeospatialPoseFromPoseSuccess -> {
            val currentGeospatialPose = geospatialPoseResult.pose
            val horizontalAccuracy = geospatialPoseResult.horizontalAccuracy
            // ... use pose and accuracy
         val latitude = currentGeospatialPose.latitude
         val longitude = currentGeospatialPose.longitude
        // The orientation is stored as a Quaternion in the EUS (East-Up-South) system. The EUS coordinate system has X+ pointing east, Y+ pointing up, and Z+ pointing south. True North is aligned with the -Z axis.
         val eusQuaternion = currentGeospatialPose.eastUpSouthQuaternion

        }
        is CreateGeospatialPoseFromPoseNotTracking -> {
            // Geospatial is not currently tracking
        }
    }

## Convert a geospatial pose to a device pose

You can convert a geospatial pose to a device pose to help deliver contextual,
location-aware experiences on AI glasses. This transformation
takes information defined by real-world coordinates---such as the location of a
landmark, a navigation path, or persistent AR content---and converts it into the
precise visual space of the user's glasses.

To convert a geospatial pose to a device pose using
[`Geospatial.createPoseFromGeospatialPose()`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#createPoseFromGeospatialPose(androidx.xr.runtime.math.GeospatialPose)):

    when (val poseResult = geospatial.createPoseFromGeospatialPose(geospatialPose)) {
        is CreatePoseFromGeospatialPoseSuccess -> {
            val devicePose = poseResult.pose
        // devicePose is now ready to be used
        }
        is CreatePoseFromGeospatialPoseNotTracking -> {
            // Geospatial is not currently tracking
        }
    }