---
title: https://developer.android.com/training/tv/get-started/hardware
url: https://developer.android.com/training/tv/get-started/hardware
source: md.txt
---

TV hardware is substantially different from other Android devices. TVs do not
include some of the hardware features found on other Android devices, such as touchscreens,
cameras, and GPS receivers. TVs are also completely dependent on secondary hardware devices:
for users to interact with TV apps, they must use a remote control or game pad. (To learn about
various input methods, see [Manage TV controllers](https://developer.android.com/training/tv/get-started/controllers).)


When you build an app for TV, carefully consider the hardware limitations and requirements of
operating on TV hardware. Check whether your app is running on a TV and handle unsupported
hardware features.

## Check for a TV device


If you are building an app that operates on both TV devices and other devices, you might need to
check what kind of device your app is running on and adjust the operation of your app. For
instance, if you have an app that can be started through an `https://developer.android.com/reference/android/content/Intent`,
check the device properties to determine whether to start a TV-oriented
activity or a phone activity.


The recommended way to determine whether your app is running on a TV device is to use the `https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)` method to check
whether the device is running in television mode. The following example code shows you how to check whether
your app is running on a TV device:

### Kotlin

```kotlin
const val TAG = "DeviceTypeRuntimeCheck"

val isTelevision = packageManager.hasSystemFeature(PackageManager.FEATURE_LEANBACK)
if (isTelevision) {
    Log.d(TAG, "Running on a TV Device")
} else {
    Log.d(TAG, "Running on a non-TV Device")
}
```

### Java

```java
public static final String TAG = "DeviceTypeRuntimeCheck";

boolean isTelevision = getPackageManager().hasSystemFeature(PackageManager.FEATURE_LEANBACK);
if (isTelevision) {
    Log.d(TAG, "Running on a TV Device");
} else {
    Log.d(TAG, "Running on a non-TV Device");
}
```

## Handle unsupported hardware features


Depending on the design and functionality of your app, you might be able to work around certain
hardware features being unavailable. This section discusses what hardware features are typically
not available for TV, how to detect missing hardware features, and what alternatives are suggested to
these features.

### Unsupported TV hardware features


TVs have a different purpose from other devices, so they do not have hardware features that
other Android-powered devices often have. For this reason, the Android system does not support
the following features for a TV device:

| Hardware | Android feature descriptor |
|---|---|
| Touchscreen | `android.hardware.touchscreen` |
| Touchscreen emulator | `android.hardware.faketouch` |
| Telephony | `android.hardware.telephony` |
| Camera | `android.hardware.camera` |
| Near Field Communications (NFC) | `android.hardware.nfc` |
| GPS | `android.hardware.location.gps` |
| Microphone | `android.hardware.microphone` |
| Sensors | `android.hardware.sensor` |
| Screen in portrait orientation | `android.hardware.screen.portrait` |


**Note:** Some TV controllers have a microphone, which is
not the same as the microphone hardware feature described here. The controller microphone is fully
supported.


See the [Features reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference) for a complete list of features, subfeatures, and their descriptors.

### Declare hardware requirements for TV


Android apps can declare hardware feature requirements in the app manifest to help ensure
that they aren't installed on devices that don't provide those features. If you are extending an existing
app for use on TV, closely review your app's manifest for any hardware requirement
declarations that might prevent it from being installed on a TV device.


If your app uses hardware features like a touchscreen or camera that are not available on
TV, but it can operate without the use of those features, modify your app's manifest to
indicate that these features are not required. The following manifest code snippet
demonstrates how to declare that your app does not require hardware features that are unavailable
on TV devices but uses those features on non-TV devices:

```xml
<uses-feature android:name="android.hardware.touchscreen"
        android:require>d<="false"/
uses-feature android:name="android.hardware.faketouch"
   > <    android:required="false"/
uses-feature android:name="android.hardware>.<telephony"
        android:required="false"/
uses-feature android:name>=<"android.hardware.camera"
        android:required="false"/
us>e<s-feature android:name="android.hardware.nfc"
        android:required="fals>e<"/
uses-feature android:name="android.hardware.location.gps"
        andro>i<d:required="false"/
uses-feature android:name="android.hardware.microp>h<one"
        android:required="false"/
u>s<es-feature android:name="android.hardware.sensor"
        android:require>d="false"/
!-- Some TV devices have an ethernet connection only --
uses-feature android:name="android.hardware.wifi"
        android:required="false"/
```

**Note:** Some features have subfeatures, like `android.hardware.camera.front`,
as described in the [Feature reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference). Be sure to mark any subfeatures also used in your app as `required="false"`.


All apps intended for use on TV devices must declare that the touchscreen feature is not required,
as described in [Get started with
TV apps](https://developer.android.com/training/tv/get-started). If your app normally uses one or more of the features not supported by TV devices, change the
`android:required` attribute setting to `false` for those features in your manifest.


**Caution:** Declaring a hardware feature as required by setting its
value to `true` prevents your app from being installed on TV
devices or appearing in the Android TV home screen launcher.

### Be aware of permissions that imply hardware features


Some [`uses-permission`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
manifest declarations *imply hardware features*. This behavior means that requesting some
permissions in your app manifest can exclude your app from from being installed and used on TV
devices. The following commonly requested permissions create an implicit hardware feature
requirement:

| Permission | Implied hardware feature |
|---|---|
| `https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO` | `android.hardware.microphone` |
| `https://developer.android.com/reference/android/Manifest.permission#CAMERA` | `android.hardware.camera` *and* `android.hardware.camera.autofocus` |
| `https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION` | `android.hardware.location` `android.hardware.location.network` (target API level 20 or lower only) |
| `https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION` | `android.hardware.location` `android.hardware.location.gps` (target API level 20 or lower only) |
| `https://developer.android.com/reference/android/Manifest.permission#ACCESS_WIFI_STATE` `https://developer.android.com/reference/android/Manifest.permission#CHANGE_WIFI_STATE` | `android.hardware.wifi` Some TV devices have an ethernet connection only. |


For a complete list of permission requests that imply a hardware feature requirement, see the
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element#permissions-features)
guide. If your app requests one of the features previously listed, include a
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element)
declaration in your manifest for the implied hardware feature that indicates it is not
required. `android:required="false"`.


**Note:** If your app targets Android 5.0 (API level 21) or
higher and uses the `ACCESS_COARSE_LOCATION` or
`ACCESS_FINE_LOCATION` permission, users can still install your
app on a TV device, even if the TV device doesn't have a network card or a GPS
receiver.


After you make hardware features optional for your app, you must check for the
availability of those features at runtime and then adjust your app's behavior. The next section
discusses how to check for hardware features and suggests some approaches for changing the
behavior of your app.


For more information on filtering and declaring features in the manifest, see the
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element)
guide.

### Check for hardware features


The Android framework can tell you if hardware features are not available on the device where
your app is running. Use the `https://developer.android.com/reference/android/content/pm/PackageManager#hasSystemFeature(java.lang.String)`
method to check for specific features at runtime. This method takes a single string argument that
specifies the feature you want to check.

The following code example demonstrates how to detect the availability of hardware features
at runtime:

### Kotlin

```kotlin
// Check whether the telephony hardware feature is available.
if (packageManager.hasSystemFeature(PackageManager.FEATURE_TELEPHONY)) {
    Log.d("HardwareFeatureTest", "Device can make phone calls")
}

// Check whether android.hardware.touchscreen feature is available.
if (packageManager.hasSystemFeature(PackageManager.FEATURE_TOUCHSCREEN)) {
    Log.d("HardwareFeatureTest", "Device has a touchscreen.")
}
```

### Java

```java
// Check whether the telephony hardware feature is available.
if (getPackageManager().hasSystemFeature(PackageManager.FEATURE_TELEPHONY)) {
    Log.d("HardwareFeatureTest", "Device can make phone calls");
}

// Check whether android.hardware.touchscreen feature is available.
if (getPackageManager().hasSystemFeature(PackageManager.FEATURE_TOUCHSCREEN)) {
    Log.d("HardwareFeatureTest", "Device has a touchscreen.");
}
```

#### Touchscreen


Since most TVs do not have touchscreens, Android does not support touchscreen interaction for
TV devices. Furthermore, using a touchscreen is not consistent with a viewing environment where
the user is seated 10 feet away from the display. Make sure that your UI elements and text do not
require or imply the use of a touchscreen.


For TV devices, design your app to support
navigation using a directional pad (D-pad) on a TV remote control. For more information on
properly supporting navigation using TV-friendly controls, see
[TV navigation](https://developer.android.com/training/tv/get-started/navigation).

#### Camera


Although a TV typically does not have a camera, you can still provide a photography-related
app on a TV. For example, if you have an app that takes, views, and edits photos, you can
disable its picture-taking functionality for TVs and still let users view and even edit
photos. If you decide to enable your camera-related app to work on a TV, add the
following feature declaration your app manifest:

```xml
<uses-feature android:name="android.hardware.camera" android:required>="false" /
```


If you enable your app to run without a camera, add code to your app
that detects whether the camera feature is available and makes adjustments to the operation of your
app. The following code example demonstrates how to detect the presence of a camera:

### Kotlin

```kotlin
// Check whether the camera hardware feature is available.
if (packageManager.hasSystemFeature(PackageManager.FEATURE_CAMERA)) {
    Log.d("Camera test", "Camera available!")
} else {
    Log.d("Camera test", "No camera available. View and edit features only.")
}
```

### Java

```java
// Check whether the camera hardware feature is available.
if (getPackageManager().hasSystemFeature(PackageManager.FEATURE_CAMERA)) {
    Log.d("Camera test", "Camera available!");
} else {
    Log.d("Camera test", "No camera available. View and edit features only.");
}
```

#### GPS


TVs are stationary, indoor devices and do not have built-in global positioning system (GPS)
receivers. If your app uses location information, you can still let users search for
a location or use a static location provider such as a postal code configured during the TV device
setup.

### Kotlin

```kotlin
// Request a static location from the location manager.
val locationManager = this.getSystemService(Context.LOCATION_SERVICE) as LocationManager
val location: Location = locationManager.getLastKnownLocation("static")

// Attempt to get postal code from the static location object.
val geocoder = Geocoder(this)
val address: Address? =
        try {
            geocoder.getFromLocation(location.latitude, location.longitude, 1)[0]
                    .apply {
                        Log.d(TAG, postalCode)
                    }
        } catch (e: IOException) {
            Log.e(TAG, "Geocoder error", e)
            null
        }
```

### Java

```java
// Request a static location from the location manager.
LocationManager locationManager = (LocationManager) this.getSystemService(
        Context.LOCATION_SERVICE);
Location location = locationManager.getLastKnownLocation("static");

// Attempt to get postal code from the static location object.
Geocoder geocoder = new Geocoder(this);
Address address = null;
try {
  address = geocoder.getFromLocation(location.getLatitude(),
          location.getLongitude(), 1).get(0);
  Log.d("Postal code", address.getPostalCode());

} catch (IOException e) {
  Log.e(TAG, "Geocoder error", e);
}
```

## Pause playback during low-power mode


Some TV devices support a low-power mode when the user switches the device off.
Instead of shutting down, the device disables the display and keeps Android
TV running in the background. Audio output is still enabled in this mode, so
stop any currently playing content when the device is in low-power mode.


To avoid playback during low-power mode, override
`https://developer.android.com/reference/android/app/Activity#onStop()`
and stop any currently playing content:

### Kotlin

```kotlin
override fun onStop() {
    // App-specific method to stop playback.
    stopPlayback()
    super.onStop()
}
```

### Java

```java
@Override
public void onStop() {
  // App-specific method to stop playback.
  stopPlayback();
  super.onStop();
}
```


When the user switches the power back on, `https://developer.android.com/reference/android/app/Activity#onStart()` is called
if your app is the active foreground app. For more information on starting and stopping
an activity, see
[The activity lifecycle](https://developer.android.com/guide/components/activities/activity-lifecycle).