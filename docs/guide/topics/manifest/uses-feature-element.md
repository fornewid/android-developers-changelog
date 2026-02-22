---
title: https://developer.android.com/guide/topics/manifest/uses-feature-element
url: https://developer.android.com/guide/topics/manifest/uses-feature-element
source: md.txt
---

# &lt;uses-feature>

Google Play uses the`<uses-feature>`elements declared in your app manifest to filter your app from devices that don't meet its hardware and software feature requirements.

By specifying the features that your application requires, you enable Google Play to present your application only to users whose devices meet the application's feature requirements, rather than presenting it to all users.

For important information about how Google Play uses features as the basis for filtering, see the[Google Play and feature-based filtering](https://developer.android.com/guide/topics/manifest/uses-feature-element#market-feature-filtering)section.

syntax:
:

    ```xml
    <uses-feature
      android:name="string"
      android:required=["true" | "false"]
      android:glEsVersion="integer" />
    ```

contained in:
:   [<manifest>](https://developer.android.com/guide/topics/manifest/manifest-element)

description:

:   Declares a single hardware or software feature that is used by the application.

    The purpose of a`<uses-feature>`declaration is to inform any external entity of the set of hardware and software features your application depends on. The element offers a`required`attribute that lets you specify whether your application requires and can't function without the declared feature or prefers to have the feature but can function without it.

    Because feature support can vary across Android devices, the`<uses-feature>`element serves an important role in letting an application describe the device-variable features that it uses.

    The set of available features that your application declares corresponds to the set of feature constants made available by the Android[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager). Feature constants are listed in the[Features reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference)section in this document.

    You must specify each feature in a separate`<uses-feature>`element, so if your application requires multiple features, it declares multiple`<uses-feature>`elements. For example, an application that requires both Bluetooth and camera features in the device declares these two elements:  

    ```xml
    <uses-feature android:name="android.hardware.bluetooth" android:required="true" />
    <uses-feature android:name="android.hardware.camera.any" android:required="true" />
    ```

    In general, always declare`<uses-feature>`elements for all the features that your application requires.

    Declared`<uses-feature>`elements are informational only, meaning that the Android system itself doesn't check for matching feature support on the device before installing an application.

    However, other services, such as Google Play, and applications can check your application's`<uses-feature>`declarations as part of handling or interacting with your application. For this reason, it's very important that you declare all of the features that your application uses.

    For some features, there might be a specific attribute that lets you define a version of the feature, such as the version of Open GL used (declared with[`glEsVersion`](https://developer.android.com/guide/topics/manifest/uses-feature-element#glEsVersion)). Other features that either do or don't exist for a device, such as a camera, are declared using the[`name`](https://developer.android.com/guide/topics/manifest/uses-feature-element#name)attribute.

    Although the`<uses-feature>`element is only activated for devices running API Level 4 or higher, include these elements for all applications, even if the[`minSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#min)is 3 or lower. Devices running older versions of the platform ignore the element.

    **Note:** When declaring a feature, remember that you must also request permissions as appropriate. For example, you need to request the[CAMERA](https://developer.android.com/reference/android/Manifest.permission#CAMERA)permission before your application can access the camera API. Requesting the permission grants your application access to the appropriate hardware and software. Declaring the features used by your application helps ensure proper device compatibility.

attributes:
:

    `android:name`
    :   Specifies a single hardware or software feature used by the application as a descriptor string. Valid attribute values are listed in the[Hardware features](https://developer.android.com/guide/topics/manifest/uses-feature-element#hw-features)and[Software features](https://developer.android.com/guide/topics/manifest/uses-feature-element#sw-features)sections. These attribute values are case-sensitive.

    `android:required`
    :   Boolean value that indicates whether the application requires the feature specified in`android:name`.

        - Declaring`android:required="true"`for a feature indicates that the application*can't function, or isn't designed to function*, when the specified feature isn't present on the device.
        - Declaring`android:required="false"`for a feature indicates that the application*uses the feature if present* on the device, but that it*is designed to function without the specified feature*if necessary.

        The default value for`android:required`is`"true"`.

    `android:glEsVersion`

    :   The OpenGL ES version required by the application. The higher 16 bits represent the major number and the lower 16 bits represent the minor number. For example, to specify OpenGL ES version 2.0, you set the value as "0x00020000", or to specify OpenGL ES 3.2, you set the value as "0x00030002".<br />

        An application specifies at most one`android:glEsVersion`attribute in its manifest. If it specifies more than one, the`android:glEsVersion`with the numerically highest value is used and any other values are ignored.

        If an application doesn't specify an`android:glEsVersion`attribute, then it is assumed that the application requires only OpenGL ES 1.0, which is supported by all Android-powered devices.

        An application can assume that if a platform supports a given OpenGL ES version, it also supports all numerically lower OpenGL ES versions. Therefore, for an application that requires both OpenGL ES 1.0 and OpenGL ES 2.0, specify that it requires OpenGL ES 2.0.

        For an application that can work with any of several OpenGL ES versions, only specify the numerically lowest version of OpenGL ES that it requires. It can check at runtime whether a higher level of OpenGL ES is available.

        For more information about using OpenGL ES, including how to check the supported OpenGL ES version at runtime, see the[OpenGL ES API guide](https://developer.android.com/develop/ui/views/graphics/opengl).

introduced in:
:   API Level 4

see also:
:
    - [PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager)
    - [FeatureInfo](https://developer.android.com/reference/android/content/pm/FeatureInfo)
    - [ConfigurationInfo](https://developer.android.com/reference/android/content/pm/ConfigurationInfo)
    - [`<uses-permission>`](https://developer.android.com/guide/topics/manifest/uses-permission-element)
    - [Filters on Google Play](https://developer.android.com/google/play/filters)

## Google Play and feature-based filtering

Google Play filters the applications that are visible to users so that users can see and download only those applications that are compatible with their device. One of the ways it filters applications is by feature compatibility.

To determine an application's feature compatibility with a given user's device, Google Play compares:

- Features required by the application, as declared in`<uses-feature>`elements in the application's manifest.
- Features available on the device, in hardware or software, as reported using read-only system properties.

To accurately compare features, the Android Package Manager provides a shared set of feature constants that both applications and devices use to declare feature requirements and support. The available feature constants are listed in the[Features reference](https://developer.android.com/guide/topics/manifest/uses-feature-element#features-reference)section in this document and in the class documentation for[PackageManager](https://developer.android.com/reference/android/content/pm/PackageManager).

When the user launches Google Play, the application queries the package manager for the list of features available on the device by calling[getSystemAvailableFeatures()](https://developer.android.com/reference/android/content/pm/PackageManager#getSystemAvailableFeatures()). The Store application then passes the features list up to Google Play when establishing the session for the user.

Each time you upload an application to the Google Play Console, Google Play scans the application's manifest file. It looks for`<uses-feature>`elements and evaluates them in combination with other elements, in some cases, such as`<uses-sdk>`and`<uses-permission>`elements. After establishing the application's set of required features, it stores that list internally as metadata associated with the application APK and the application version.

When a user searches or browses for applications using the Google Play application, the service compares the features needed by each application with the features available on the user's device. If all of an application's required features are present on the device, Google Play lets the user see the application and potentially download it.

If any required feature isn't supported by the device, Google Play filters the application so that it isn't visible to the user or available for download.

Because the features you declare in`<uses-feature>`elements directly affect how Google Play filters your application, it's important to understand how Google Play evaluates the application's manifest and establishes the set of required features. The following sections provide more information.

### Filtering based on explicitly declared features

An explicitly declared feature is one that your application declares in a`<uses-feature>`element. The feature declaration can include an`android:required=["true" | "false"]`attribute if you are compiling against API level 5 or higher.

This lets you specify whether the application requires the feature and can't function properly without it (`"true"`) or uses the feature if available, but is designed to run without it (`"false"`).

Google Play handles explicitly declared features in this way:

- If a feature is explicitly declared as being required, as shown in the following example, Google Play adds the feature to the list of required features for the application. It then filters the application from users on devices that don't provide that feature.  

  ```xml
  <uses-feature android:name="android.hardware.camera.any" android:required="true" />
  ```
- If a feature is explicitly declared as*not* being required, as shown in the following example, Google Play*doesn't* add the feature to the list of required features. For that reason, an explicitly declared non-required feature is never considered when filtering the application. Even if the device doesn't provide the declared feature, Google Play still considers the application compatible with the device and shows it to the user, unless other filtering rules apply.  

  ```xml
  <uses-feature android:name="android.hardware.camera" android:required="false" />
  ```
- If a feature is explicitly declared, but without an`android:required`attribute, Google Play assumes that the feature is required and sets up filtering on it.

In general, if your application is designed to run on Android 1.6 and lower, the`android:required`attribute isn't available in the API, and Google Play assumes that all`<uses-feature>`declarations are required.

**Note:** By declaring a feature explicitly and including an`android:required="false"`attribute, you can effectively disable all filtering on Google Play for the specified feature.

### Filter based on implicit features

An*implicit* feature is one that an application requires in order to function properly, but which is*not* declared in a`<uses-feature>`element in the manifest file. Strictly speaking, it is best for every application to*always*declare all features that it uses or requires, and the absence of a declaration for a feature used by an application can be considered an error.

However, as a safeguard for users and developers, Google Play looks for implicit features in each application and sets up filters for those features, as it does for explicitly declared features.

An application might require a feature but not declare it for reasons like the following:

- The application was compiled against an older version of the Android library (Android 1.5 or earlier), for which the`<uses-feature>`element isn't available.
- The developer incorrectly assumes that the feature is present on all devices and a declaration is unnecessary.
- The developer omits the feature declaration accidentally.
- The developer declares the feature explicitly, but the declaration isn't valid. For example, a spelling error in the`<uses-feature>`element name or an unrecognized string value for the`android:name`attribute invalidates the feature declaration.

To account for these cases, Google Play attempts to discover an application's implied feature requirements by examining*other elements* declared in the manifest file, specifically`<uses-permission>`elements.

If an application requests hardware-related permissions, Google Play assumes that the application uses the underlying hardware features and therefore requires those features, even if there are no corresponding`<uses-feature>`declarations. For such permissions, Google Play adds the underlying hardware features to the metadata that it stores for the application and sets up filters for them.

For example, if an application requests the`CAMERA`permission, Google Play assumes the application requires a back (world-facing) camera even if the app doesn't declare a`<uses-feature>`element for`android.hardware.camera`. As a result, Google Play filters devices that don't have a back camera.

If you don't want Google Play to filter based on a specific implied feature, explicitly declare the feature in a`<uses-feature>`element and include the`android:required="false"`attribute. For example, to disable filtering implied by the`CAMERA`permission, declare the following features:  

```xml
<uses-feature android:name="android.hardware.camera" android:required="false" />
<uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
```

**Caution:** Permissions that you request in`<uses-permission>`elements can directly affect how Google Play filters your application. The[Permissions that imply feature requirements](https://developer.android.com/guide/topics/manifest/uses-feature-element#permissions)section lists the full set of permissions that imply feature requirements and therefore trigger filtering.

### Special handling for Bluetooth feature

Google Play applies slightly different rules than described in the preceding example when determining filtering for Bluetooth.

If an application declares a Bluetooth permission in a`<uses-permission>`element but doesn't explicitly declare the Bluetooth feature in a`<uses-feature>`element, Google Play checks the version(s) of the Android platform on which the application is designed to run, as specified in the`<uses-sdk>`element.

As shown in the following table, Google Play enables filtering for the Bluetooth feature only if the application declares its lowest or targeted platform as Android 2.0 (API level 5) or higher. However, note that Google Play applies the normal rules for filtering when the application explicitly declares the Bluetooth feature in a`<uses-feature>`element.

**Table 1.** How Google Play determines the Bluetooth feature requirement for an application that requests a Bluetooth permission but doesn't declare the Bluetooth feature in a`<uses-feature>`element.

|      If`minSdkVersion`is ...       | and`targetSdkVersion`is |                                                                   Result                                                                   |
|------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| \<=4, or`<uses-sdk>`isn't declared | \<=4                    | Google Play*doesn't* filter the application from any devices based on their reported support for the`android.hardware.bluetooth`feature.   |
| \<=4                               | \>=5                    | Google Play filters the application from any devices that don't support the`android.hardware.bluetooth`feature (including older releases). |
| \>=5                               | \>=5                    | Google Play filters the application from any devices that don't support the`android.hardware.bluetooth`feature (including older releases). |

The following examples illustrate the different filtering effects based on how Google Play handles the Bluetooth feature.
: *Result:*Google Play doesn't filter the application from any device.  

```xml
<manifest ...>
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-sdk android:minSdkVersion="3" />
    ...
</manifest>
```
: *Result:*Google Play now assumes that the feature is required and filters the application from all devices that don't report Bluetooth support, including devices running older versions of the platform.  

```xml
<manifest ...>
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-sdk android:minSdkVersion="3" android:targetSdkVersion="5" />
    ...
</manifest>
```
: *Result:*Identical to the previous example: filtering is applied.  

```xml
<manifest ...>
    <uses-feature android:name="android.hardware.bluetooth" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-sdk android:minSdkVersion="3" android:targetSdkVersion="5" />
    ...
</manifest>
```
: *Result:*Google Play disables filtering based on Bluetooth feature support for all devices.  

```xml
<manifest ...>
    <uses-feature android:name="android.hardware.bluetooth" android:required="false" />
    <uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
    <uses-sdk android:minSdkVersion="3" android:targetSdkVersion="5" />
    ...
</manifest>
```

### Test the features required by your application

You can use the`aapt2`tool, included in the Android SDK, to determine how Google Play filters your application based on its declared features and permissions. To do so, run`aapt2`with the`dump
badging`command. This causes`aapt2`to parse your application's manifest and apply the same rules used by Google Play to determine the features that your application requires.

To use the tool, follow these steps:

1. Build and export your application as an unsigned APK. If you are developing in Android Studio, build your application with Gradle, as follows:
   1. Open the project and select**Run \> Edit Configurations**.
   2. Select the plus sign near the top-left corner of the**Run/Debug Configurations**window.
   3. Select**Gradle.**
   4. Enter "Unsigned APK" in**Name**.
   5. Choose your module from the**Gradle project**section.
   6. Enter "assemble" in**Tasks**.
   7. Select**OK**to complete the new configuration.
   8. Make sure the**Unsigned APK** run configuration is selected in the toolbar, and then select**Run \> Run 'Unsigned APK'**.

   You can find your unsigned APK in the`<`*ProjectName*`>/app/build/outputs/apk/`directory.
2. Locate the`aapt2`tool, if it isn't already in your PATH. If you are using SDK Tools r8 or higher, you can find`aapt2`in the`<`*SDK* `>/build-tools/<`*tools version number*`>`directory.

   **Note:** You must use the version of`aapt2`that is provided for the latest Build-Tools component available. If you don't have the latest Build-Tools component, download it using the[Android SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager).
3. Run`aapt2`using this syntax:

```
$ aapt2 dump badging <path_to_exported_.apk>
```

Here's an example of the command output for the second Bluetooth example shown previously:  

```
$ ./aapt2 dump badging BTExample.apk
package: name='com.example.android.btexample' versionCode='' versionName=''
uses-permission:'android.permission.BLUETOOTH_ADMIN'
uses-feature:'android.hardware.bluetooth'
sdkVersion:'3'
targetSdkVersion:'5'
application: label='BT Example' icon='res/drawable/app_bt_ex.png'
launchable activity name='com.example.android.btexample.MyActivity'label='' icon=''
uses-feature:'android.hardware.touchscreen'
main
supports-screens: 'small' 'normal' 'large'
locales: '--_--'
densities: '160'
```

## Features reference

The following sections provide reference information about hardware features, software features, and sets of permissions that imply specific feature requirements.

### Hardware features

This section presents the hardware features supported by the most current platform release. To indicate that your app uses or requires a hardware feature, declare the corresponding value, beginning with`"android.hardware"`, in an`android:name`attribute. Each time you declare a hardware feature, use a separate`<uses-feature>`element.

#### Audio hardware features

`android.hardware.audio.low_latency`
:   The app uses the device's low-latency audio pipeline, which reduces lag and delays when processing sound input or output.

`android.hardware.audio.output`
:   The app transmits sound using the device's speakers, audio jack, Bluetooth streaming capabilities, or a similar mechanism.

`android.hardware.audio.pro`
:   The app uses the device's high-end audio functionality and performance capabilities.

`android.hardware.microphone`
:   The app records audio using the device's microphone.

#### Bluetooth hardware features

`android.hardware.bluetooth`
:   The app uses the device's Bluetooth features, usually to communicate with other Bluetooth-enabled devices.

`android.hardware.bluetooth_le`
:   The app uses the device's Bluetooth Low Energy radio features.

#### Camera hardware features

**Note:** To prevent unnecessary filtering of your app by Google Play, add`android:required="false"`to any camera feature your app can function without. Otherwise, Google Play assumes the feature is required and prevents devices that don't support the feature from accessing your app.

##### Large screen support

Some large screen devices don't support all camera features. Chromebooks typically don't have back (world-facing) cameras, autofocus, or flash. But Chromebooks do have front (user-facing) cameras and are often connected to external cameras.

To provide basic camera support and make your app available to as many devices as possible, add the following camera feature settings to your app manifest:  

```xml
<uses-feature android:name="android.hardware.camera.any" android:required="false" />
<uses-feature android:name="android.hardware.camera" android:required="false" />
<uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
<uses-feature android:name="android.hardware.camera.flash" android:required="false" />
```

Adjust the feature settings to support your app's use cases. But, to make your app available to the greatest number of devices, always include the`required`attribute to explicitly specify whether a feature is a must‑have.

##### Feature list

`android.hardware.camera.any`

:   The app uses one of the device's cameras or an external camera connected to the device. Use this feature instead of`android.hardware.camera`or`android.hardware.camera.front`if your app doesn't*require*the camera to be back (world) facing or front (user) facing, respectively.

    The`CAMERA`permission implies that your app also uses`android.hardware.camera`. A back camera is a required feature unless`android.hardware.camera`is declared with`android:required="false"`.

`android.hardware.camera`

:   The app uses the device's back (world-facing) camera.

    **Caution:** Devices such as Chromebooks that have only a front (user-facing) camera don't support this feature. Use`android.hardware.camera.any`if your app can use any camera, regardless of the direction the camera faces.  
    **Note:** The[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA)permission implies that a back camera is a required feature. To help ensure proper filtering on Google Play when your app manifest includes the`CAMERA`permission, explicitly specify that your app uses the`camera`feature and indicate whether it's required, such as:  
    `<uses-feature android:name="android.hardware.camera" android:required="false" />`

`android.hardware.camera.front`

:   The app uses the device's front (user-facing) camera.

    The`CAMERA`permission implies that your app also uses`android.hardware.camera`. A back camera is a required feature unless`android.hardware.camera`is declared with`android:required="false"`.

    **Caution:** If your app uses`android.hardware.camera.front`but doesn't explicitly declare`android.hardware.camera`with`android.required="false"`, devices that don't have a back camera (like Chromebooks) are filtered by Google Play. If your app supports devices with only front cameras, declare`android.hardware.camera`with`android.required="false"`to prevent unnecessary filtering.

`android.hardware.camera.external`

:   The app communicates with an external camera the user connects to the device. This feature doesn't guarantee that an external camera is available for your app to use.

    The`CAMERA`permission implies that your app also uses`android.hardware.camera`. A back camera is a required feature unless`android.hardware.camera`is declared with`android:required="false"`.

`android.hardware.camera.autofocus`

:   The app uses the autofocus feature supported by the device's camera.

    **Note:** The[`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA)permission implies that autofocus is a required feature. To help ensure proper filtering on Google Play when your app manifest includes the`CAMERA`permission, explicitly specify that your app uses theautofocusfeature and indicate whether it is required or not, such as:  
    `<uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />`.

`android.hardware.camera.flash`

:   The app uses the flash feature supported by the device's camera.

`android.hardware.camera.capability.manual_post_processing`

:   The app uses the`MANUAL_POST_PROCESSING`feature supported by the device's camera.

    This feature lets your app override the camera's auto white balance functionality. Use`android.colorCorrection.transform`,`android.colorCorrection.gains`, and an`android.colorCorrection.mode`of`TRANSFORM_MATRIX`.

`android.hardware.camera.capability.manual_sensor`

:   The app uses the`MANUAL_SENSOR`feature supported by the device's camera.

    This feature implies support for auto exposure locking (`android.control.aeLock`), which enables the camera's exposure time and sensitivity to remain fixed at specific values.

`android.hardware.camera.capability.raw`

:   The app uses the`RAW`feature supported by the device's camera.

    This feature implies that the device can save DNG (raw) files. The device's camera provides the DNG-related metadata necessary for your app to process the raw images directly.

`android.hardware.camera.level.full`
:   The app uses the`FULL`level of image capture support provided by at least one of the device's cameras.`FULL`support includes burst-capture capabilities, per frame control, and manual post-processing control. See[`INFO_SUPPORTED_HARDWARE_LEVEL_FULL`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#INFO_SUPPORTED_HARDWARE_LEVEL_FULL).

#### Device UI hardware features

`android.hardware.type.automotive`

:   The app is designed to show its UI on a set of screens inside a vehicle. The user interacts with the app using hard buttons, touch, rotary controllers, and mouse-like interfaces. The vehicle's screens usually appear in the center console or the instrument cluster of a vehicle.

    **Note:** See[Distribute to cars](https://developer.android.com/training/cars/distribute#declare_the_automotive_hardware_feature_in_your_apps_manifest)for more information on this feature's usage and guidance for building apps for cars.

`android.hardware.type.television`

:   (Deprecated; use[`android.software.leanback`](https://developer.android.com/guide/topics/manifest/uses-feature-element#media-sw-features)instead.)

    The app is designed to show its UI on a television. This feature defines "television" as a typical living-room television experience: the app displaying on a big screen, the user sitting far away, and the dominant form of input being something like a D-pad, rather than a mouse, pointer, or touch device.

`android.hardware.type.watch`
:   The app is designed to show its UI on a watch. A watch is worn on the body, such as on the wrist. The user is very close to the device while interacting with it.

`android.hardware.type.pc`

:   The app is designed to show its UI on Chromebooks. This feature disables input emulation for mouse and touchpad, since Chromebooks use mouse and touchpad hardware. See[Mouse input](https://developer.android.com/games/playgames/input-mouse#disable_input_translation_mode).

    **Note:** Set`required="false"`for this element; otherwise, Google Play Store makes your app unavailable to devices other than Chromebooks.

#### Fingerprint hardware features

`android.hardware.fingerprint`
:   The app reads fingerprints using the device's biometric hardware.

#### Gamepad hardware features

`android.hardware.gamepad`
:   The app captures game controller input, either from the device itself or from a connected gamepad.

#### Infrared hardware features

`android.hardware.consumerir`
:   The app uses the device's infrared (IR) capabilities, usually to communicate with other consumer IR devices.

#### Location hardware features

`android.hardware.location`
:   The app uses one or more features on the device for determining location, such as GPS location, network location, or cell location.

`android.hardware.location.gps`

:   The app uses precise location coordinates obtained from a Global Positioning System (GPS) receiver on the device.

    By using this feature, an app implies that it also uses the`android.hardware.location`feature, unless this parent feature is declared with the attribute`android:required="false"`.

`android.hardware.location.network`

:   The app uses coarse location coordinates obtained from a network-based geolocation system supported on the device.

    By using this feature, an app implies that it also uses the`android.hardware.location`feature, unless this parent feature is declared with the attribute`android:required="false"`.

#### NFC hardware features

`android.hardware.nfc`
:   The app uses the device's Near-Field Communication (NFC) radio features.

`android.hardware.nfc.hce`

:   The app uses NFC card emulation that is hosted on the device.

#### OpenGL ES hardware features

`android.hardware.opengles.aep`
:   The app uses the[OpenGL ES Android Extension Pack](http://www.khronos.org/registry/gles/extensions/ANDROID/ANDROID_extension_pack_es31a.txt)that is installed on the device.

#### Sensor hardware features

`android.hardware.sensor.accelerometer`
:   The app uses motion readings from the device's accelerometer to detect the device's current orientation. For example, an app might use accelerometer readings to determine when to switch between portrait and landscape orientations.

`android.hardware.sensor.ambient_temperature`
:   The app uses the device's ambient (environmental) temperature sensor. For example, a weather app can report indoor or outdoor temperature.

`android.hardware.sensor.barometer`
:   The app uses the device's barometer. For example, a weather app might report air pressure.

`android.hardware.sensor.compass`
:   The app uses the device's magnetometer (compass). For example, a navigation app might show the current direction a user faces.

`android.hardware.sensor.gyroscope`
:   The app uses the device's gyroscope to detect rotation and twist, creating a six-axis orientation system. By using this sensor, an app can detect more smoothly when it needs to switch between portrait and landscape orientations.

`android.hardware.sensor.hifi_sensors`
:   The app uses the device's high fidelity (Hi-Fi) sensors. For example, a gaming app might detect the user's high-precision movements.

`android.hardware.sensor.heartrate`
:   The app uses the device's heart rate monitor. For example, a fitness app might report trends in a user's heart rate over time.

`android.hardware.sensor.heartrate.ecg`
:   The app uses the device's electrocardiogram (ECG) heart rate sensor. For example, a fitness app might report more detailed information about a user's heart rate.

`android.hardware.sensor.light`
:   The app uses the device's light sensor. For example, an app might display one of two color schemes based on the ambient lighting conditions.

`android.hardware.sensor.proximity`
:   The app uses the device's proximity sensor. For example, a telephony app might turn off the device's screen when the app detects that the user is holding the device close to their body.

`android.hardware.sensor.relative_humidity`
:   The app uses the device's relative humidity sensor. For example, a weather app might use the humidity to calculate and report the current dewpoint.

`android.hardware.sensor.stepcounter`
:   The app uses the device's step counter. For example, a fitness app might report the number of steps a user needs to take to achieve their daily step count goal.

`android.hardware.sensor.stepdetector`
:   The app uses the device's step detector. For example, a fitness app might use the time interval between steps to infer the type of exercise that the user is doing.

#### Screen hardware features

`android.hardware.screen.landscape`
`android.hardware.screen.portrait`

:   The app requires the device to use the portrait or landscape orientation. If your app supports both orientations, then you don't need to declare either feature.

    For example, if your app requires portrait orientation, declare the following feature so that only the devices that support portrait orientation, always or by user choice, can run your app:  

    ```xml
    <uses-feature android:name="android.hardware.screen.portrait" />
    ```

    Both orientations are assumed to not be required by default, so your app can install on devices that support one or both orientations. However, if any of your activities request that they run in a specific orientation, using the[`android:screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen)attribute, then this declaration implies that your app requires that orientation.

    For example, if you declare`android:screenOrientation`with either`"landscape"`,`"reverseLandscape"`, or`"sensorLandscape"`, then your app is available only on devices that support landscape orientation.

    As a best practice, declare your requirement for this orientation using a`<uses-feature>`element. If you declare an orientation for your activity using`android:screenOrientation`but don't actually require it, you can disable the requirement by declaring the orientation with a`<uses-feature>`element and include`android:required="false"`.

    For backward compatibility, any device running Android 3.1 (API level 12) or lower supports both landscape and portrait orientations.

#### Telephony hardware features

`android.hardware.telephony`
:   The app uses the device's telephony features, such as telephony radio with data communication services.

`android.hardware.telephony.cdma`

:   The app uses the Code Division Multiple Access (CDMA) telephony radio system.

    By using this feature, an app implies that it also uses the`android.hardware.telephony`feature, unless this parent feature is declared with`android:required="false"`.

`android.hardware.telephony.gsm`

:   The app uses the Global System for Mobile Communications (GSM) telephony radio system.

    By using this feature, an app implies that it also uses the`android.hardware.telephony`feature, unless this parent feature is declared with`android:required="false"`.

#### Touchscreen hardware features

`android.hardware.faketouch`

:   The app uses basic touch interaction events, such as tapping and dragging.

    When declared as required, this feature indicates that the app is compatible with a device only if that device has an emulated "fake touch" touchscreen or has an actual touchscreen.

    A device that offers a fake touch interface provides a user input system that emulates a subset of a touchscreen's capabilities. For example, a mouse or remote control might drive an on-screen cursor.

    If your app requires basic point and click interaction and doesn't work with only a D-pad controller, declare this feature. Because this is the minimum level of touch interaction, you can also use an app that declares this feature on devices that offer more complex touch interfaces.

    Apps require the`android.hardware.faketouch`feature by default. If you want your app to be limited to devices that only have a touchscreen, you must explicitly declare that touchscreen is required as follows:  

    ```xml
    <uses-feature android:name="android.hardware.touchscreen"
        android:required="true" />
    ```

    All apps that don't explicitly require`android.hardware.touchscreen`, as shown in the following example, also work on devices with`android.hardware.faketouch`.  

    ```xml
    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />
    ```

`android.hardware.faketouch.multitouch.distinct`

:   The app tracks two or more distinct "fingers" on a fake touch interface. This is a superset of the`android.hardware.faketouch`feature. When declared as required, this feature indicates that the app is compatible with a device only if that device emulates distinct tracking of two or more fingers or has an actual touchscreen.

    Unlike the distinct multitouch defined by`android.hardware.touchscreen.multitouch.distinct`, input devices that support distinct multitouch with a fake touch interface don't support all two-finger gestures, because the input is transformed to cursor movement on the screen. That is, single-finger gestures on such a device move a cursor, two-finger swipes cause single-finger touch events to occur, and other two-finger gestures trigger the corresponding two-finger touch events.

    A device that provides a two-finger touch trackpad for cursor movement can support this feature.

`android.hardware.faketouch.multitouch.jazzhand`

:   The app tracks five or more distinct "fingers" on a fake touch interface. This is a superset of the`android.hardware.faketouch`feature. When declared as required, this feature indicates that the app is compatible with a device only if that device emulates distinct tracking of five or more fingers or has an actual touchscreen.

    Unlike the distinct multitouch defined by`android.hardware.touchscreen.multitouch.jazzhand`, input devices that support jazzhand multitouch with a fake touch interface don't support all five-finger gestures, because the input is transformed to cursor movement on the screen. That is, single-finger gestures on such a device move a cursor, multi-finger gestures cause single-finger touch events to occur, and other multi-finger gestures trigger the corresponding multi-finger touch events.

    A device that provides a five-finger touch trackpad for cursor movement can support this feature.

`android.hardware.touchscreen`

:   The app uses the device's touchscreen capabilities for gestures that are more interactive than basic touch events, such as a fling. This is a superset of the`android.hardware.faketouch`feature.

    By default, all apps require this feature and therefore aren't available to devices that provide only an emulated "fake touch" interface. You can make your app available on devices that provide a fake touch interface, or even on devices that provide only a D-pad controller, by explicitly declaring that a touchscreen is not required using`android.hardware.touchscreen`with`android:required="false"`. Add this declaration if your app uses, but doesn't require, a real touchscreen interface. All apps that don't explicitly require`android.hardware.touchscreen`also work on devices with`android.hardware.faketouch`.

    If your app in fact requires a touch interface, such as to perform more advanced touch gestures like flings, then you don't need to declare any touch interface features, because they're required by default. However, it's best if you explicitly declare all features that your app uses.

    If you require more complex touch interaction, such as multi-finger gestures, declare that your app uses advanced touchscreen features.

`android.hardware.touchscreen.multitouch`

:   The app uses the device's basic two-point multitouch capabilities, such as for pinch gestures, but the app doesn't need to track touches independently. This is a superset of the`android.hardware.touchscreen`feature.

    By using this feature, an app implies that it also uses the`android.hardware.touchscreen`feature, unless this parent feature is declared with`android:required="false"`.

`android.hardware.touchscreen.multitouch.distinct`

:   The app uses the device's advanced multitouch capabilities for tracking two or more points independently. This feature is a superset of the`android.hardware.touchscreen.multitouch`feature.

    By using this feature, an app implies that it also uses the`android.hardware.touchscreen.multitouch`feature, unless this parent feature is declared with`android:required="false"`.

`android.hardware.touchscreen.multitouch.jazzhand`

:   The app uses the device's advanced multitouch capabilities for tracking five or more points independently. This feature is a superset of the`android.hardware.touchscreen.multitouch`feature.

    By using this feature, an app implies that it also uses the`android.hardware.touchscreen.multitouch`feature, unless this parent feature is declared with`android:required="false"`.

#### USB hardware features

`android.hardware.usb.accessory`
:   The app behaves as a USB device and connects to USB hosts.

`android.hardware.usb.host`
:   The app uses the USB accessories that are connected to the device. The device serves as the USB host.

#### Vulkan hardware features

`android.hardware.vulkan.compute`
:   The app uses Vulkan compute features. This feature indicates that the app requires the hardware-accelerated Vulkan implementation. The feature version indicates which level of optional compute features the app requires beyond the Vulkan 1.0 requirements. For example, if your app requires Vulkan compute level 0 support, declare the following feature:  

    ```xml
    <uses-feature
        android:name="android.hardware.vulkan.compute"
        android:version="0"
        android:required="true" />
    ```
    For more details about the feature version, see[FEATURE_VULKAN_HARDWARE_COMPUTE](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_COMPUTE).

`android.hardware.vulkan.level`
:   The app uses Vulkan level features. This feature indicates that the app requires the hardware-accelerated Vulkan implementation. The feature version indicates which level of optional hardware features the app requires. For example, if your app requires Vulkan hardware level 0 support, declare the following feature:  

    ```xml
    <uses-feature
        android:name="android.hardware.vulkan.level"
        android:version="0"
        android:required="true" />
    ```
    For more information about the feature version, see[FEATURE_VULKAN_HARDWARE_LEVEL](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_LEVEL).

`android.hardware.vulkan.version`
:   The app uses Vulkan. This feature indicates that the app requires the hardware-accelerated Vulkan implementation. The feature version indicates the minimum version of Vulkan API support the app requires. For example, if your app requires Vulkan 1.0 support, declare the following feature:  

    ```xml
    <uses-feature
        android:name="android.hardware.vulkan.version"
        android:version="0x400003"
        android:required="true" />
    ```
    For more details about the feature version, see[FEATURE_VULKAN_HARDWARE_VERSION](https://developer.android.com/reference/android/content/pm/PackageManager#FEATURE_VULKAN_HARDWARE_VERSION).

#### Wi-Fi hardware features

`android.hardware.wifi`
:   The app uses 802.11 networking (Wi-Fi) features on the device.

`android.hardware.wifi.direct`
:   The app uses the Wi-Fi Direct networking features on the device.

### Software features

This section presents the software features supported by the most current platform release. To indicate that your app uses or requires a software feature, declare the corresponding value, beginning with`"android.software"`, in an`android:name`attribute. Each time you declare a software feature, use a separate`<uses-feature>`element.

#### Communication software features

`android.software.sip`
:   The app uses Session Initiation Protocol (SIP) services. By using SIP, the app can support internet telephony operations, such as video conferencing and instant messaging.

`android.software.sip.voip`

:   The app uses SIP-based Voice Over Internet Protocol (VoIP) services. By using VoIP, the app can support real-time internet telephony operations, such as two-way video conferencing.

    By using this feature, an app implies that it also uses the`android.software.sip`feature, unless this parent feature is declared with`android:required="false"`.

`android.software.webview`
:   The app displays content from the internet.

#### Custom input software features

`android.software.input_methods`
:   The app uses a new input method, which the developer defines in an[`InputMethodService`](https://developer.android.com/reference/android/inputmethodservice/InputMethodService).

#### Device management software features

`android.software.backup`
:   The app includes logic to handle a backup and restore operation.

`android.software.device_admin`
:   The app uses device administrators to enforce a device policy.

`android.software.managed_users`
:   The app supports secondary users and managed profiles.

`android.software.securely_removes_users`
:   The app can**permanently**remove users and their associated data.

`android.software.verified_boot`
:   The app includes logic to handle results from the device's verified boot feature, which detects whether the device's configuration changes during a restart operation.

#### Media software features

`android.software.midi`
:   The app connects to musical instruments or outputs sound using the Musical Instrument Digital Interface (MIDI) protocol.

`android.software.print`
:   The app includes commands for printing documents displayed on the device.

`android.software.leanback`
:   The app is designed to run on Android TV devices.

`android.software.live_tv`
:   The app streams live television programs.

#### Screen interface software features

`android.software.app_widgets`
:   The app uses or provides App Widgets and is intended only for devices that include a Home screen or similar location where users can embed App Widgets.

`android.software.home_screen`
:   The app behaves as a replacement to the device's Home screen.

`android.software.live_wallpaper`
:   The app uses or provides wallpapers that include animation.

### Permissions that imply feature requirements

Some hardware and software feature constants are made available to applications after the corresponding API. Because of this, some apps might*use* the API before they can declare that they*require* the API using the`<uses-feature>`system.

To prevent those apps from being made available unintentionally, Google Play assumes that certain hardware-related permissions indicate that the underlying hardware features are required by default. For instance, applications that use Bluetooth must request the`BLUETOOTH`permission in a`<uses-permission>`element.

For legacy apps, Google Play assumes that the permission declaration means that the underlying`android.hardware.bluetooth`feature is required by the application and sets up filtering based on that feature. Table 2 lists permissions that imply feature requirements equivalent to those declared in`<uses-feature>`elements.

`<uses-feature>`declarations, including any declared`android:required`attribute, always take precedence over features implied by the permissions in table 2. For any of these permissions, you can disable filtering based on the implied feature by explicitly declaring the feature in a`<uses-feature>`element with the`required`attribute set to`false`.

For example, to disable filtering based on the`CAMERA`permission, add the following`<uses-feature>`declarations to the manifest file:  

```xml
<uses-feature android:name="android.hardware.camera" android:required="false" />
<uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
```

**Caution:** If your app targets Android 5.0 (API level 21) or higher and uses the`ACCESS_COARSE_LOCATION`or`ACCESS_FINE_LOCATION`permission to receive location updates from the network or a GPS, respectively, you must also explicitly declare that your app uses the`android.hardware.location.network`or`android.hardware.location.gps`hardware features.

**Table 2.**Device permissions that imply device hardware use.

|  Category  |            Permission            |                                                                              Implied feature requirement                                                                              |
|------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bluetooth  | `BLUETOOTH`                      | `android.hardware.bluetooth` See[Special handling for Bluetooth feature](https://developer.android.com/guide/topics/manifest/uses-feature-element#bt-permission-handling)for details. |
| Bluetooth  | `BLUETOOTH_ADMIN`                | `android.hardware.bluetooth`                                                                                                                                                          |
| Camera     | `CAMERA`                         | `android.hardware.camera` `android.hardware.camera.autofocus`                                                                                                                         |
| Location   | `ACCESS_MOCK_LOCATION`           | `android.hardware.location`                                                                                                                                                           |
| Location   | `ACCESS_LOCATION_EXTRA_COMMANDS` | `android.hardware.location`                                                                                                                                                           |
| Location   | `INSTALL_LOCATION_PROVIDER`      | `android.hardware.location`                                                                                                                                                           |
| Location   | `ACCESS_COARSE_LOCATION`         | `android.hardware.location` `android.hardware.location.network`(Only when target API level is 20 or lower.)                                                                           |
| Location   | `ACCESS_FINE_LOCATION`           | `android.hardware.location` `android.hardware.location.gps`(Only when target API level is 20 or lower.)                                                                               |
| Microphone | `RECORD_AUDIO`                   | `android.hardware.microphone`                                                                                                                                                         |
| Telephony  | `CALL_PHONE`                     | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `CALL_PRIVILEGED`                | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `MODIFY_PHONE_STATE`             | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `PROCESS_OUTGOING_CALLS`         | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `READ_SMS`                       | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `RECEIVE_SMS`                    | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `RECEIVE_MMS`                    | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `RECEIVE_WAP_PUSH`               | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `SEND_SMS`                       | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `WRITE_APN_SETTINGS`             | `android.hardware.telephony`                                                                                                                                                          |
| Telephony  | `WRITE_SMS`                      | `android.hardware.telephony`                                                                                                                                                          |
| Wi-Fi      | `ACCESS_WIFI_STATE`              | `android.hardware.wifi`                                                                                                                                                               |
| Wi-Fi      | `CHANGE_WIFI_STATE`              | `android.hardware.wifi`                                                                                                                                                               |
| Wi-Fi      | `CHANGE_WIFI_MULTICAST_STATE`    | `android.hardware.wifi`                                                                                                                                                               |