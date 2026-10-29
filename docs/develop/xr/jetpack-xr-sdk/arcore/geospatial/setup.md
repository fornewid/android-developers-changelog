---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/setup
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/setup
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

To use the Geospatial API in your app, your app must be set up to access the
[ARCore API](https://console.cloud.google.com/apis/library/arcore) on Google Cloud. This API contains the [Visual
Positioning Service](https://research.google/blog/using-global-localization-to-improve-navigation/) that provides accurate positioning using
data from Google Street View.

This guide helps you set up a Google Cloud project that has enabled the correct
API and authorization methods to access the API.

## Set up a Google Cloud project or use an existing project

If you have an existing Google Cloud project, select it.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

If you don't have an existing project, create one.

[Create new project](https://console.cloud.google.com/projectcreate)

### Enable the ARCore API

To use the ARCore API, you must enable it in your project.

[Enable the ARCore API](https://console.cloud.google.com/apis/library/arcore)

### Set up authorization for Google Cloud

An Android application can communicate with the ARCore API using two different
authorization methods: Keyless authorization (OAuth 2.0), which is the
recommended method, and API Key authorization:

- Keyless authorization uses a combination of the application's package name and the fingerprint of the signing key to authorize your application.
- An API key is a string that identifies a Google Cloud project. API keys are
  generally not considered secure as they are typically accessible to clients.
  Consider using Keyless authorization to communicate with the ARCore API.

### Keyless authorization

To authorize your app using **Keyless authentication**, create OAuth 2.0
client IDs.

1. In Google Cloud, go to the **Credentials** page.

   [Go to Credentials](https://console.cloud.google.com/apis/credentials)
2. Click **Create credentials** , and then select **OAuth client ID** from
   the menu.

3. Fill in the required fields as follows:

   - **Application type** : choose **Android**.
   - **Package name** : use the package name as declared in your `AndroidManifest.xml`.
   - **SHA-1 certificate fingerprint** : obtain SHA-1 certificate fingerprints using instructions at [Client authentication](https://developers.google.com/android/guides/client-auth).
4. Press **Create**.

> [!IMPORTANT]
> **Important:** It is common to sign your application with different signing keys. You must create a Client ID for each signing key you plan to use. Commonly, this is a [debug signing key](https://developer.android.com/studio/publish/app-signing#debug-mode) and release signing key(s). See the [troubleshooting guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/troubleshooting) if the authorization fails.

### API Key

Create an API key from the Google Cloud Console by following these steps:

1. In the Google Cloud console, go to the **Credentials** page:

   [Go to Credentials](https://console.cloud.google.com/apis/credentials)
2. Click **Create credentials** , and then select **API key** from the menu.

3. Add an API Restriction for the **ARCore API** . For more information, see
   [Apply API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).

4. Click **Create** . The **API key created** dialog displays the string for
   your newly created key.

In Android Studio, add the new API key to your project. Include the API key
in a [`<meta-data>`](https://developer.android.com/guide/topics/manifest/meta-data-element) element in the
[`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element in your app's
`AndroidManifest.xml`:

    <meta-data
      android:name="com.google.android.ar.API_KEY"
      android:value="API_KEY"/>

## Request required permissions

To use the Geospatial API in ARCore with Jetpack XR, your app needs to request
the following runtime permissions:

- [`ACCESS_FINE_LOCATION`](https://developer.android.com/training/location/permissions): Required to determine a user's [precise location](https://developer.android.com/develop/sensors-and-location/location/permissions#accuracy).

On mobile devices, the Geospatial API also requires the following permissions:

- [`android.permission.CAMERA`](https://developer.android.com/reference/kotlin/android/Manifest.permission#CAMERA): Required to access the device's camera.
- [`android.permission.INTERNET`](https://developer.android.com/training/basics/network-ops/connecting): Required to communicate with Google Cloud services.

## Access a session

Access Geospatial information through a Jetpack XR Runtime [`Session`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session),
which your [app must create](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore#access-session-runtime).

## Configure the session

The Geospatial API is not enabled by default on XR sessions. Your app must
explicitly enable it by configuring a `GeospatialMode` on the `Session`. The
following modes are available:

- [`GeospatialMode.SPATIAL`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/GeospatialMode#SPATIAL()): The Geospatial API is enabled. The Geospatial API uses **Visual Positioning System (VPS)** , **Global Positioning System (GPS)** data, and the [device's motion
  sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview) to determine the device's geospatial pose. This mode is not available on Intelligent Eyewear devices.
- [`GeospatialMode.INERTIAL`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/GeospatialMode#INERTIAL()): The Geospatial API is enabled in low-power mode. The Geospatial API only uses GPS and the [device's motion sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_overview) to determine the device's geospatial pose. This mode is only available on Intelligent Eyewear devices.
- [`GeospatialMode.DISABLED`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/GeospatialMode#DISABLED()): Geospatial API is disabled; when transitioning from another mode to this mode, the Geospatial API releases all acquired resources and stop tracking.

Not all devices support all Geospatial modes. See
[`GeospatialMode`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/GeospatialMode) for more information. Use
[`XrDevice.isGeospatialSupported`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/XrDevice#isGeospatialModeSupported(androidx.xr.runtime.GeospatialMode)) to whether a
given `GeospatialMode` is supported.

The following code sample demonstrates how to set a `GeospatialMode` using
[`Session.configure`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/Session#configure(androidx.xr.runtime.Config)).


```kotlin
// Define the configuration object to enable Geospatial features.
val newConfig = Config.Builder(session.config)
    .setGeospatial(GeospatialMode.SPATIAL)
    .build()
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
```

<br />

## Prompt user to allow usage of device data

Apps that use the Geospatial API with ARCore for Jetpack XR must present the
user with a prompt to acknowledge and allow the use of data from their device.
See the [user privacy requirements](https://developers.google.com/ar/develop/privacy-requirements) for more
information.

## Use the Geospatial object

Once the session is configured, obtain the [`Geospatial`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial) object
using [`Geospatial.getInstance`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#getInstance(androidx.xr.runtime.Session)). Only use the
`Geospatial` object when its state is
[`GeospatialTrackingState.RUNNING`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.GeospatialTrackingState#RUNNING()).

The following code samples demonstrate how to monitor the Geospatial state using
[`Geospatial.state`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#state()).

### Compose XR


```kotlin
val geospatial = remember { Geospatial.getInstance(session) }
val geospatialState by geospatial.state.collectAsStateWithLifecycle()
if (geospatialState.geospatialTrackingState == Geospatial.GeospatialTrackingState.RUNNING) {
    // Queries to the Geospatial API are only valid when the state is RUNNING.
}
```

<br />

### SceneCore


```kotlin
val geospatial = Geospatial.getInstance(session)
lifecycleScope.launch {
    geospatial.state.collect { geospatialState ->
        if (geospatialState == Geospatial.GeospatialTrackingState.RUNNING) {
            // Queries to the Geospatial API are only valid when the state is RUNNING.
        }
    }
}
```

<br />

> [!NOTE]
> **Note:** If the `GeospatialTrackingState` object never becomes `GeospatialTrackingState.RUNNING`, see the [troubleshooting guide](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/troubleshooting) for possible solutions.

## Understand accuracy values

While the Geospatial API is enabled, it provides three accuracy values:
horizontal, vertical, and orientation accuracy. These accuracy values are
updated over time and can be made more precise as more data is acquired. Larger
values indicate lower accuracy, and are defined as the radius of a 68%
confidence level. In other words, there is a 68% probability that the true value
is within the given radius of the estimated value.

Use
[`Geospatial.State.horizontalAccuracy`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.State#horizontalAccuracy()),
[`verticalAccuracy`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.State#verticalAccuracy()), and
[`orientationYawAccuracy`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial.State#orientationYawAccuracy()) to get the
current accuracy values.

Your app might require a specific level of precision to function correctly. For
example, your app may want to wait until the horizontal accuracy is less than 5
meters before rendering virtual content. To increase the likelihood of obtaining
higher accuracy data, your app should instruct users to look around their
surroundings, preferably at buildings or other features with high visual detail
that are present in Google Street View. Use
[`Geospatial.checkVpsAvailability`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Geospatial#checkVpsAvailability(kotlin.Double,kotlin.Double)) to
determine whether VPS is available at the given location.

## What's next

When the Geospatial API is correctly set up in your app, your app can do the
following:

- [Convert between device-local poses and Geospatial poses](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/positioning),
- [Render content at Geospatial poses](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial/anchors)