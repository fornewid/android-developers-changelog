---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

After you've [installed and configured Android Studio](https://developer.android.com/develop/xr/jetpack-xr-sdk/get-studio), [created a
project](https://developer.android.com/develop/xr/jetpack-xr-sdk/create-project), and [set up the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk), you're ready to start building
immersive experiences.

Before you [start exploring all the ways you can build](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing), review the
information and complete any tasks in the following sections to make sure your
app is configured for immersive XR development.

## Configure your app's manifest file

As with other Android app projects, your Android XR app must have an
`AndroidManifest.xml` file with specific manifest settings. The manifest file
describes essential information about your app to the Android build tools, the
Android operating system, and Google Play. See the [app manifest overview
guide](https://developer.android.com/guide/topics/manifest/manifest-intro) for more information.

For [XR differentiated apps](https://developer.android.com/docs/quality-guidelines/android-xr#android-xr-differentiated), your manifest file
must contain the following elements and attributes:

### PROPERTY_XR_ACTIVITY_START_MODE property

The `android:name="android.window.PROPERTY_XR_ACTIVITY_START_MODE"` property
lets the system know that an activity should be launched in a specific mode when
the activity is started.

This property has the following values:

- `XR_ACTIVITY_START_MODE_HOME_SPACE` (Jetpack XR SDK only)
- `XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED` (Jetpack XR SDK only)

#### XR_ACTIVITY_START_MODE_HOME_SPACE

Use this start mode to launch your app in Home Space. In Home Space, multiple
apps can run side-by-side, so users can multitask. Any mobile or large screen
Android app can operate in Home Space, as well as XR apps built using the
Jetpack XR SDK.

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

#### XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED

Use this start mode to launch your app in Full Space. In Full Space, only one
app runs at a time, with no space boundaries, and all other apps are hidden.


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

### PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED property

The `android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"`
property indicates that the application should be launched with a specific type
of boundary. Your app needs to specify
[`XR_BOUNDARY_TYPE_LARGE`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_LARGE()) if it's designed to let
users move around their physical space. Specifying
[`XR_BOUNDARY_TYPE_NO_RECOMMENDATION`](https://developer.android.com/reference/kotlin/androidx/xr/runtime/manifest/package-summary#XR_BOUNDARY_TYPE_NO_RECOMMENDATION()) provides no
recommendations for the type of safety boundary, so the system uses the type
that is already in use.

    <manifest ... >

       <application ... >
           <property
               android:name="android.window.PROPERTY_XR_BOUNDARY_TYPE_RECOMMENDED"
               android:value="XR_BOUNDARY_TYPE_LARGE" />
       </application>
    </manifest>

### PackageManager features for XR apps

When you
[distribute apps through the Google Play Store](https://developer.android.com/develop/xr/package-and-distribute),
you can specify required hardware or software features in the app manifest. The
[`uses-feature`](https://developer.android.com/guide/topics/manifest/uses-feature-element) element allows the Play Store to
appropriately filter apps shown to users.

The following features are specific to XR-differentiated apps.

#### android.software.xr.api.spatial

Apps that are built using the [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk) must
include this feature in the app manifest. The value you set for the
`android:required` attribute depends on your app's
[release track](https://developer.android.com/develop/xr/package-and-distribute#choose-release).

If your app bundles XR-differentiated features or content into an existing
mobile APK and is published on the mobile release track, then set the
`android:required` attribute to `false`:

    <!-- If you are publishing an existing mobile APK using the mobile release track, set android:required to false.-->
    <uses-feature android:name="android.software.xr.api.spatial" android:required="false" />

If your app is built specifically for XR-enabled devices and is published to the
Android XR dedicated release track, then set the `android:required` attribute to
`true`:

    <!-- If you are publishing a separate APK for XR using the dedicated Android XR release track, set android:required to true.-->
    <uses-feature android:name="android.software.xr.api.spatial" android:required="true" />

#### android.hardware.xr.input.controller

This feature indicates that the app requires input from a high precision, 6DoF
(degrees of freedom) motion controller to function correctly. If your app
supports controllers and can't function without them, set the value to `true`.
If your app supports controllers but can operate without them, set it to
`false`.

> [!NOTE]
> **Note:** 6DoF motion controllers are a pair of hardware controllers, one for each hand. Each controller is tracked independently in space through six degrees of freedom - both linear and rotational movements. These controllers typically have several hardware buttons, including a trigger as well as haptic feedback.

    <!-- Sets android:required to true, indicating that your app can't function on devices without controllers. -->
    <uses-feature android:name="android.hardware.xr.input.controller" android:required="true" />

#### android.hardware.xr.input.hand_tracking

This flag indicates that the app requires high fidelity hand tracking to
function correctly, including position, orientation, and velocity of joints in
the user's hand. If your app supports hand tracking and can't function without
it, set the value to `true`. If your app supports hand tracking, but can operate
without it, set it to `false`.

> [!NOTE]
> **Note:** This flag is not required for detecting basic gestures such as pinching, poking, aiming, and gripping.

    <!-- Sets android:required to true, indicating that your app can't function on devices without hand tracking. -->
    <uses-feature android:name="android.hardware.xr.input.hand_tracking" android:required="true" />

#### android.hardware.xr.input.eye_tracking

This flag indicates that the app requires high-fidelity eye tracking for input
to function correctly. If your app supports eye tracking for input and can't
function without it, set the value to `true`. If your app supports eye tracking
for input, but can operate without it, set it to `false`.

    <!-- Sets android:required to true, indicating that your app can't function on devices without eye tracking. -->
    <uses-feature android:name="android.hardware.xr.input.eye_tracking" android:required="true" />

> [!NOTE]
> **Note:** Hand tracking and eye tracking are privacy-sensitive input methods and require the apps to request special permissions. See [Understand permissions for
> XR](https://developer.android.com/develop/xr/permissions) on this page for more information on declaring permissions.

## App manifest compatibility considerations for mobile and large screen apps

> [!IMPORTANT]
> **Important:** This section applies only to mobile or large screen apps that haven't been optimized for XR. By default, these kinds of Android apps will run on Android XR. However, if your app requires one or more of the features in this section, the app won't be shown in the Play Store on Android XR.

As described in the [PackageManager features for XR apps](https://developer.android.com/develop/xr/jetpack-xr-sdk/build-immersive#packagemanager-features) section, apps
declare that they use a feature by declaring it in a [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)
element in the app manifest. Some features, such as telephony or GPS, might not
be compatible with all devices.

To get a listing of the features that are enabled for a device, run `adb
shell pm list features`.

### Unsupported features

The [Google Play store filters applications](https://developer.android.com/guide/topics/manifest/uses-feature-element#market-feature-filtering) available
for installation on a device by using the following Android feature
declarations.

> [!CAUTION]
> **Caution:** If your app requires a feature that is not supported on the device, then that app won't be available for installation from the Play Store for XR devices. If your app uses the feature, but is designed to run without it, you should set `android:required="false`". For example, `<uses-feature android:name="android.hardware.location.gps"
> android:required="false" />`.

#### Camera Hardware

[`android.hardware.camera.ar`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AR)

[`android.hardware.camera.autofocus`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_AUTOFOCUS)

[`android.hardware.camera.capability.manual_post_processing`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_POST_PROCESSING)

[`android.hardware.camera.capability.manual_sensor`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_MANUAL_SENSOR)

[`android.hardware.camera.capability.raw`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CAPABILITY_RAW)

[`android.hardware.camera.concurrent`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_CONCURRENT)

[`android.hardware.camera.external`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_EXTERNAL)

[`android.hardware.camera.flash`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_FLASH)

[`android.hardware.camera.level.full`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CAMERA_LEVEL_FULL)

#### Connectivity

[`android.hardware.ethernet`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_ETHERNET)

[`android.hardware.uwb`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_UWB)

[`android.hardware.ipsec_tunnel_migration`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IPSEC_TUNNEL_MIGRATION)

#### Device Configuration

[`android.hardware.ram.low`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_RAM_LOW)

#### Form Factor Configuration

[`android.hardware.type.automotive`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_AUTOMOTIVE)

[`android.hardware.type.embedded`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_EMBEDDED)

[`android.hardware.type.pc`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PC)

[`android.hardware.type.television`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEVISION)

[`android.hardware.type.watch`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WATCH)

[`android.software.leanback`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK)

[`android.software.leanback_only`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LEANBACK_ONLY)

[`android.software.live_tv`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LIVE_TV)

#### Input

[`android.hardware.consumerir`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CONSUMER_IR)

[`android.software.input_methods`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_INPUT_METHODS)

#### Location

[`android.hardware.location.gps`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LOCATION_GPS)

#### Near Field Communication

[`android.hardware.nfc`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC)

[`android.hardware.nfc.ese`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_ESE)

[`android.hardware.nfc.hce`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION)

[`android.hardware.nfc.hcef`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_HOST_CARD_EMULATION_NFCF)

[`android.hardware.nfc.uicc`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_OFF_HOST_CARD_EMULATION_UICC)

[`android.hardware.nfc.beam`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_NFC_BEAM)

#### Security Configuration and Hardware

[`android.hardware.se.omapi.ese`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_ESE)

[`android.hardware.se.omapi.sd`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_SD)

[`android.hardware.se.omapi.uicc`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SE_OMAPI_UICC)

[`android.hardware.biometrics.face`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FACE)

[`android.hardware.fingerprint`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_FINGERPRINT)

[`android.hardware.identity_credential`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE)

[`android.hardware.identity_credential_direct_access`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_IDENTITY_CREDENTIAL_HARDWARE_DIRECT_ACCESS)

[`android.hardware.keystore.limited_use_key`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_LIMITED_USE_KEY)

[`android.hardware.keystore.single_use_key`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_KEYSTORE_SINGLE_USE_KEY)

[`android.hardware.strongbox_keystore`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_STRONGBOX_KEYSTORE)

#### Sensors

[`android.hardware.sensor.accelerometer_limited_axes`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES)

[`android.hardware.sensor.accelerometer_limited_axes_uncalibrated`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_ACCELEROMETER_LIMITED_AXES_UNCALIBRATED)

[`android.hardware.sensor.ambient_temperature`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_AMBIENT_TEMPERATURE)

[`android.hardware.sensor.barometer`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_BAROMETER)

[`android.hardware.sensor.gyroscope_limited_axes`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES)

[`android.hardware.sensor.gyroscope_limited_axes_uncalibrated`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_GYROSCOPE_LIMITED_AXES_UNCALIBRATED)

[`android.hardware.sensor.heading`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEADING)

[`android.hardware.sensor.heartrate`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE)

[`android.hardware.sensor.heartrate.ecg`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HEART_RATE_ECG)

[`android.hardware.sensor.hinge_angle`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_HINGE_ANGLE)

[`android.hardware.sensor.light`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_LIGHT)

[`android.hardware.sensor.relative_humidity`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_RELATIVE_HUMIDITY)

[`android.hardware.sensor.stepcounter`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_COUNTER)

[`android.hardware.sensor.stepdetector`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SENSOR_STEP_DETECTOR)

#### Software Configuration

[`android.software.backup`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_BACKUP)

[`android.software.connectionservice`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_CONNECTION_SERVICE)

[`android.software.expanded_picture_in_picture`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_EXPANDED_PICTURE_IN_PICTURE)

[`android.software.live_wallpaper`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_LIVE_WALLPAPER)

[`android.software.picture_in_picture`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_PICTURE_IN_PICTURE)

[`android.software.telecom`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELECOM)

[`android.software.wallet_location_based_suggestions`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_WALLET_LOCATION_BASED_SUGGESTIONS)

#### Telephony

[`android.hardware.telephony`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY)

[`android.hardware.telephony.calling`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CALLING)

[`android.hardware.telephony.cdma`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_CDMA)

[`android.hardware.telephony.data`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_DATA)

[`android.hardware.telephony.euicc`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC)

[`android.hardware.telephony.euicc.mep`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_EUICC_MEP)

[`android.hardware.telephony.gsm`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_GSM)

[`android.hardware.telephony.ims`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_IMS)

[`android.hardware.telephony.mbms`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MBMS)

[`android.hardware.telephony.messaging`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_MESSAGING)

[`android.hardware.telephony.radio.access`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_RADIO_ACCESS)

[`android.hardware.telephony.subscription`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_TELEPHONY_SUBSCRIPTION)

[`android.software.sip`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SIP)

[`android.software.sip.voip`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_SIP_VOIP)

#### Virtual Reality (Legacy)

[`android.hardware.vr.headtracking`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_HEADTRACKING)

[`android.hardware.vr.high_performance`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE_HIGH_PERFORMANCE)

[`android.software.vr.mode`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VR_MODE)

#### Widgets

[`android.software.app_widgets`](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_APP_WIDGETS)

## Next steps

Now that you've finished configuring your app's manifest and reviewing important
information, explore ways that you can build immersive experiences:

- [Bring your Android app into 3D with XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-xr-to-existing)
- [Develop spatial UI with Jetpack Compose for XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/ui-compose)
- [Implement Material Design for your spatial UI](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design)
- [Add spatial environments to your app](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-environments)
- [Create, control, and manage entities](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-entities)