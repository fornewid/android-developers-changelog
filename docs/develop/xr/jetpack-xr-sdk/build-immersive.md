---
title: Get started building immersive experiences  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Get started building immersive experiences Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

[Learn about XR device types →](/develop/xr/devices)

After you've [installed and configured Android Studio](/develop/xr/jetpack-xr-sdk/get-studio), [created a
project](/develop/xr/jetpack-xr-sdk/create-project), and [set up the Jetpack XR SDK](/develop/xr/jetpack-xr-sdk/set-up-sdk), you're ready to start building
immersive experiences.

Before you [start exploring all the ways you can build](/develop/xr/jetpack-xr-sdk/add-xr-to-existing), review the
information and complete any tasks in the following sections to make sure your
app is configured for immersive XR development.

## Configure your app's manifest file

As with other Android app projects, your Android XR app must have an
`AndroidManifest.xml` file with specific manifest settings. The manifest file
describes essential information about your app to the Android build tools, the
Android operating system, and Google Play. See the [app manifest overview
guide](/guide/topics/manifest/manifest-intro) for more information.

For [XR differentiated apps](/docs/quality-guidelines/android-xr#android-xr-differentiated), your manifest file
must contain the following elements and attributes:

### PROPERTY\_XR\_ACTIVITY\_START\_MODE property

The `android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"` property
lets the system know that an activity should be launched in a specific mode when
the activity is started.

This property has the following values:

* `XR_ACTIVITY_START_MODE_HOME_SPACE` (Jetpack XR SDK only)
* `XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED` (Jetpack XR SDK only)

#### XR\_ACTIVITY\_START\_MODE\_HOME\_SPACE

Use this start mode to launch your app in Home Space. In Home Space, multiple
apps can run side-by-side, so users can multitask. Any mobile or large screen
Android app can operate in Home Space, as well as XR apps built using the
Jetpack XR SDK.

```
<manifest ... >

   <application ... >
       <property
           android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
           android:value="XR_ACTIVITY_START_MODE_HOME_SPACE" />
       <activity
           android:name="com.example.myapp.MainActivity" ... >

           <intent-filter>
               <action android:name="android.intent.action.MAIN" />

               <category android:name="android.intent.category.LAUNCHER" />
           </intent-filter>
       </activity>
   </application>
</manifest>
```

#### XR\_ACTIVITY\_START\_MODE\_FULL\_SPACE\_MANAGED

Use this start mode to launch your app in Full Space. In Full Space, only one
app runs at a time, with no space boundaries, and all other apps are hidden.

```
<manifest ... >

   <application ... >
       <property
           android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"
           android:value="XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED" />
       <activity
           android:name="com.example.myapp.MainActivity" ... >

           <intent-filter>
               <action android:name="android.intent.action.MAIN" />

               <category android:name="android.intent.category.LAUNCHER" />
           </intent-filter>
       </activity>
   </application>
</manifest>
```

### PROPERTY\_XR\_BOUNDARY\_TYPE\_RECOMMENDED property

The `android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"`
property indicates that the application should be launched with a specific type
of boundary. Your app needs to specify
[`XR_BOUNDARY_TYPE_LARGE`](/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_LARGE()) if it's designed to let
users move around their physical space. Specifying
[`XR_BOUNDARY_TYPE_NO_RECOMMENDATION`](/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_NO_RECOMMENDATION()) provides no
recommendations for the type of safety boundary, so the system uses the type
that is already in use.

```
<manifest ... >

   <application ... >
       <property
           android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"
           android:value="XR_BOUNDARY_TYPE_LARGE" />
   </application>
</manifest>
```

### PackageManager features for XR apps

When you
[distribute apps through the Google Play Store](/develop/xr/package-and-distribute),
you can specify required hardware or software features in the app manifest. The
[`uses-feature`](/guide/topics/manifest/uses-feature-element) element allows the Play Store to
appropriately filter apps shown to users.

The following features are specific to XR-differentiated apps.

#### android.software.xr.api.spatial

Apps that are built using the [Jetpack XR SDK](/develop/xr/jetpack-xr-sdk) must
include this feature in the app manifest. The value you set for the
`android:required` attribute depends on your app's
[release track](/develop/xr/package-and-distribute#choose-release).

If your app bundles XR-differentiated features or content into an existing
mobile APK and is published on the mobile release track, then set the
`android:required` attribute to `false`:

```
<!-- If you are publishing an existing mobile APK using the mobile release track, set android:required to false.-->
<uses-feature android:name="android.software.xr.api.spatial" android:required="false" />
```

If your app is built specifically for XR-enabled devices and is published to the
Android XR dedicated release track, then set the `android:required` attribute to
`true`:

```
<!-- If you are publishing a separate APK for XR using the dedicated Android XR release track, set android:required to true.-->
<uses-feature android:name="android.software.xr.api.spatial" android:required="true" />
```

#### android.hardware.xr.input.controller

This feature indicates that the app requires input from a high precision, 6DoF
(degrees of freedom) motion controller to function correctly. If your app
supports controllers and can't function without them, set the value to `true`.
If your app supports controllers but can operate without them, set it to
`false`.

**Note:** 6DoF motion controllers are a pair of hardware controllers, one for each
hand. Each controller is tracked independently in space through six degrees of
freedom - both linear and rotational movements. These controllers typically have
several hardware buttons, including a trigger as well as haptic feedback.

```
<!-- Sets android:required to true, indicating that your app can't function on devices without controllers. -->
<uses-feature android:name="android.hardware.xr.input.controller" android:required="true" />
```

#### android.hardware.xr.input.hand\_tracking

This flag indicates that the app requires high fidelity hand tracking to
function correctly, including position, orientation, and velocity of joints in
the user's hand. If your app supports hand tracking and can't function without
it, set the value to `true`. If your app supports hand tracking, but can operate
without it, set it to `false`.

**Note:** This flag is not required for detecting basic gestures such as pinching,
poking, aiming, and gripping.

```
<!-- Sets android:required to true, indicating that your app can't function on devices without hand tracking. -->
<uses-feature android:name="android.hardware.xr.input.hand_tracking" android:required="true" />
```

#### android.hardware.xr.input.eye\_tracking

This flag indicates that the app requires high-fidelity eye tracking for input
to function correctly. If your app supports eye tracking for input and can't
function without it, set the value to `true`. If your app supports eye tracking
for input, but can operate without it, set it to `false`.

```
<!-- Sets android:required to true, indicating that your app can't function on devices without eye tracking. -->
<uses-feature android:name="android.hardware.xr.input.eye_tracking" android:required="true" />
```

**Note:** Hand tracking and eye tracking are privacy-sensitive input methods and
require the apps to request special permissions. See [Understand permissions for
XR](/develop/xr/permissions) on this page for more information on declaring
permissions.

## App manifest compatibility considerations for mobile and large screen apps

**Important:** This section applies only to mobile or large screen apps that haven't
been optimized for XR. By default, these kinds of Android apps will run on
Android XR. However, if your app requires one or more of the features in this
section, the app won't be shown in the Play Store on Android XR.

As described in the [PackageManager features for XR apps](/develop/xr/jetpack-xr-sdk/build-immersive#packagemanager-features) section, apps
declare that they use a feature by declaring it in a [`<uses-feature>`](/guide/topics/manifest/uses-feature-element)
element in the app manifest. Some features, such as telephony or GPS, might not
be compatible with all devices.

To get a listing of the features that are enabled for a device, run `adb
shell pm list features`.

### Unsupported features

The [Google Play store filters applications](/guide/topics/manifest/uses-feature-element#market-feature-filtering) available
for installation on a device by using the following Android feature
declarations.

**Caution:** If your app requires a feature that is not supported on the device,
then that app won't be available for installation from the Play Store
for XR devices. If your app uses the feature, but is designed to run
without it, you should set `android:required="false`". For example,
`<uses-feature android:name="android.hardware.location.gps"
android:required="false" />`.

#### Camera Hardware

[`android.hardware.camera.ar`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AR)

[`android.hardware.camera.autofocus`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AUTOFOCUS)

[`android.hardware.camera.capability.manual_post_processing`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING)

[`android.hardware.camera.capability.manual_sensor`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR)

[`android.hardware.camera.capability.raw`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_RAW)

[`android.hardware.camera.concurrent`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CONCURRENT)

[`android.hardware.camera.external`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_EXTERNAL)

[`android.hardware.camera.flash`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_FLASH)

[`android.hardware.camera.level.full`](/reference/android/content/pm/PackageManager#FEATURE_CAMERA_LEVEL_FULL)

#### Connectivity

[`android.hardware.ethernet`](/reference/android/content/pm/PackageManager#FEATURE_ETHERNET)

[`android.hardware.uwb`](/reference/android/content/pm/PackageManager#FEATURE_UWB)

[`android.hardware.ipsec_tunnel_migration`](/reference/android/content/pm/PackageManager#FEATURE_IPSEC_TUNNEL_MIGRATION)

#### Device Configuration

[`android.hardware.ram.low`](/reference/android/content/pm/PackageManager#FEATURE_RAM_LOW)

#### Form Factor Configuration

[`android.hardware.type.automotive`](/reference/android/content/pm/PackageManager#FEATURE_AUTOMOTIVE)

[`android.hardware.type.embedded`](/reference/android/content/pm/PackageManager#FEATURE_EMBEDDED)

[`android.hardware.type.pc`](/reference/android/content/pm/PackageManager#FEATURE_PC)

[`android.hardware.type.television`](/reference/android/content/pm/PackageManager#FEATURE_TELEVISION)

[`android.hardware.type.watch`](/reference/android/content/pm/PackageManager#FEATURE_WATCH)

[`android.software.leanback`](/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)

[`android.software.leanback_only`](/reference/android/content/pm/PackageManager#FEATURE_LEANBACK_ONLY)

[`android.software.live_tv`](/reference/android/content/pm/PackageManager#FEATURE_LIVE_TV)

#### Input

[`android.hardware.consumerir`](/reference/android/content/pm/PackageManager#FEATURE_CONSUMER_IR)

[`android.software.input_methods`](/reference/android/content/pm/PackageManager#FEATURE_INPUT_METHODS)

#### Location

[`android.hardware.location.gps`](/reference/android/content/pm/PackageManager#FEATURE_LOCATION_GPS)

#### Near Field Communication

[`android.hardware.nfc`](/reference/android/content/pm/PackageManager#FEATURE_NFC)

[`android.hardware.nfc.ese`](/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE)

[`android.hardware.nfc.hce`](/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION)

[`android.hardware.nfc.hcef`](/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION_NFCF)

[`android.hardware.nfc.uicc`](/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC)

[`android.hardware.nfc.beam`](/reference/android/content/pm/PackageManager#FEATURE_NFC_BEAM)

#### Security Configuration and Hardware

[`android.hardware.se.omapi.ese`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_ESE)

[`android.hardware.se.omapi.sd`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_SD)

[`android.hardware.se.omapi.uicc`](/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_UICC)

[`android.hardware.biometrics.face`](/reference/android/content/pm/PackageManager#FEATURE_FACE)

[`android.hardware.fingerprint`](/reference/android/content/pm/PackageManager#FEATURE_FINGERPRINT)

[`android.hardware.identity_credential`](/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE)

[`android.hardware.identity_credential_direct_access`](/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS)

[`android.hardware.keystore.limited_use_key`](/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_LIMITED_USE_KEY)

[`android.hardware.keystore.single_use_key`](/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_SINGLE_USE_KEY)

[`android.hardware.strongbox_keystore`](/reference/android/content/pm/PackageManager#FEATURE_STRONGBOX_KEYSTORE)

#### Sensors

[`android.hardware.sensor.accelerometer_limited_axes`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES)

[`android.hardware.sensor.accelerometer_limited_axes_uncalibrated`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED)

[`android.hardware.sensor.ambient_temperature`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_AMBIENT_TEMPERATURE)

[`android.hardware.sensor.barometer`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_BAROMETER)

[`android.hardware.sensor.gyroscope_limited_axes`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES)

[`android.hardware.sensor.gyroscope_limited_axes_uncalibrated`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED)

[`android.hardware.sensor.heading`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEADING)

[`android.hardware.sensor.heartrate`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE)

[`android.hardware.sensor.heartrate.ecg`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE_ECG)

[`android.hardware.sensor.hinge_angle`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HINGE_ANGLE)

[`android.hardware.sensor.light`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_LIGHT)

[`android.hardware.sensor.relative_humidity`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_RELATIVE_HUMIDITY)

[`android.hardware.sensor.stepcounter`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_COUNTER)

[`android.hardware.sensor.stepdetector`](/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_DETECTOR)

#### Software Configuration

[`android.software.backup`](/reference/android/content/pm/PackageManager#FEATURE_BACKUP)

[`android.software.connectionservice`](/reference/android/content/pm/PackageManager#FEATURE_CONNECTION_SERVICE)

[`android.software.expanded_picture_in_picture`](/reference/android/content/pm/PackageManager#FEATURE_EXPANDED_PICTURE_IN_PICTURE)

[`android.software.live_wallpaper`](/reference/android/content/pm/PackageManager#FEATURE_LIVE_WALLPAPER)

[`android.software.picture_in_picture`](/reference/android/content/pm/PackageManager#FEATURE_PICTURE_IN_PICTURE)

[`android.software.telecom`](/reference/android/content/pm/PackageManager#FEATURE_TELECOM)

[`android.software.wallet_location_based_suggestions`](/reference/android/content/pm/PackageManager#FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS)

#### Telephony

[`android.hardware.telephony`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

[`android.hardware.telephony.calling`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CALLING)

[`android.hardware.telephony.cdma`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CDMA)

[`android.hardware.telephony.data`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_DATA)

[`android.hardware.telephony.euicc`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC)

[`android.hardware.telephony.euicc.mep`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC_MEP)

[`android.hardware.telephony.gsm`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_GSM)

[`android.hardware.telephony.ims`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_IMS)

[`android.hardware.telephony.mbms`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MBMS)

[`android.hardware.telephony.messaging`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MESSAGING)

[`android.hardware.telephony.radio.access`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)

[`android.hardware.telephony.subscription`](/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)

[`android.software.sip`](/reference/android/content/pm/PackageManager#FEATURE_SIP)

[`android.software.sip.voip`](/reference/android/content/pm/PackageManager#FEATURE_SIP_VOIP)

#### Virtual Reality (Legacy)

[`android.hardware.vr.headtracking`](/reference/android/content/pm/PackageManager#FEATURE_VR_HEADTRACKING)

[`android.hardware.vr.high_performance`](/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)

[`android.software.vr.mode`](/reference/android/content/pm/PackageManager#FEATURE_VR_MODE)

#### Widgets

[`android.software.app_widgets`](/reference/android/content/pm/PackageManager#FEATURE_APP_WIDGETS)

## Next steps

Now that you've finished configuring your app's manifest and reviewing important
information, explore ways that you can build immersive experiences:

* [Bring your Android app into 3D with XR](/develop/xr/jetpack-xr-sdk/add-xr-to-existing)
* [Develop spatial UI with Jetpack Compose for XR](/develop/xr/jetpack-xr-sdk/ui-compose)
* [Implement Material Design for your spatial UI](/develop/xr/jetpack-xr-sdk/material-design)
* [Add spatial environments to your app](/develop/xr/jetpack-xr-sdk/add-environments)
* [Create, control, and manage entities](/develop/xr/jetpack-xr-sdk/work-with-entities)