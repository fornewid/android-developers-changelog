---
title: https://developer.android.com/training/permissions/explaining-access
url: https://developer.android.com/training/permissions/explaining-access
source: md.txt
---

The permissions related to location, microphone, and camera grant your app
access to particularly sensitive information about users. The platform includes
several mechanisms, described on this page, to help users stay informed and in
control over which apps can access location, microphone, and camera.

These privacy-preserving system features shouldn't affect how your app handles
the permissions related to location, microphone, and camera, as long as you
[follow privacy best practices](https://developer.android.com/privacy/best-practices).

In particular, make sure you do the following in your app:

- Wait to access the device's camera until the user has granted the [`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) permission to your app.
- Wait to access the device's microphone until the user has granted the [`RECORD_AUDIO`](https://developer.android.com/reference/android/Manifest.permission#RECORD_AUDIO) permission to your app.
- Wait until the user interacts with a feature in your app that requires location before you request the [`ACCESS_COARSE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_COARSE_LOCATION) permission or the [`ACCESS_FINE_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_FINE_LOCATION) permission, as described in the guide on how to [request location
  permissions](https://developer.android.com/training/location/permissions#request-location-access-runtime).
- Wait until the user grants your app either the `ACCESS_COARSE_LOCATION` permission or the `ACCESS_FINE_LOCATION` permission before you request the [`ACCESS_BACKGROUND_LOCATION`](https://developer.android.com/reference/android/Manifest.permission#ACCESS_BACKGROUND_LOCATION) permission.

## Privacy Dashboard

![A vertical timeline shows the different apps that have
accessed location information, and at what time the accesses occurred](https://developer.android.com/static/images/training/permissions/privacy-dashboard.svg) **Figure 1.** Location usage screen, part of the Privacy Dashboard.

On supported devices that run Android 12 or higher, a Privacy
Dashboard screen appears in system settings. On this screen, users can access
separate screens that show when apps access location, camera, and microphone
information. Each screen shows a timeline of when different apps have accessed a
particular type of data. Figure 1 shows the data access timeline for location
information.

### Show rationale for data access

Your app can provide a rationale for users to help them understand why your app
accesses location, camera, or microphone information. This rationale can appear
on the new Privacy Dashboard screen, your app's permissions screen, or both.

To explain why your app accesses location, camera, and microphone information,
complete the following steps:

1. Add an activity that, when started, provides some rationale for why your app
   performs a particular type of data access action. Within this activity, set the
   [`android:permission`](https://developer.android.com/guide/topics/manifest/activity-element#prmsn) attribute
   to [`START_VIEW_PERMISSION_USAGE`](https://developer.android.com/reference/android/Manifest.permission#START_VIEW_PERMISSION_USAGE).

   If your app targets Android 12 or higher, you must explicitly
   [define a value for the `android:exported`
   attribute](https://developer.android.com/about/versions/12/behavior-changes-12#exported).
2. Add the following intent filter to the newly-added activity:

   ```xml
   <!-- android:exported required if you target Android 12. -->
   <activity android:name=".DataAccessRationaleActivity"
             android:permission="android.permission.START_VIEW_PERMISSION_USAGE"
             android:exported="true">
          <!-- VIEW_PERMISSION_USAGE shows a selectable information icon on
               your app permission's page in system settings.
               VIEW_PERMISSION_USAGE_FOR_PERIOD shows a selectable information
               icon on the Privacy Dashboard screen. -->
       <intent-filter>
          <action android:name="android.intent.action.VIEW_PERMISSION_USAGE" />
          <action android:name="android.intent.action.VIEW_PERMISSION_USAGE_FOR_PERIOD" />
          <category android:name="android.intent.category.DEFAULT" />
          ...
       </intent-filter>
   </activity>
   ```
3. Decide what your data access rationale activity should show. For example, you
   might show your app's website or a help center article. To provide a more
   detailed explanation about the types of data that your app accesses, as well as
   when the access occurred, handle the extras that the system includes when it
   invokes the permission usage intent:

   - If the system invokes `ACTION_VIEW_PERMISSION_USAGE`, your app can retrieve a value for [`EXTRA_PERMISSION_GROUP_NAME`](https://developer.android.com/reference/android/content/Intent#EXTRA_PERMISSION_GROUP_NAME).
   - If the system invokes `ACTION_VIEW_PERMISSION_USAGE_FOR_PERIOD`, your app can retrieve values for `EXTRA_PERMISSION_GROUP_NAME`, [`EXTRA_ATTRIBUTION_TAGS`](https://developer.android.com/reference/android/content/Intent#EXTRA_ATTRIBUTION_TAGS), [`EXTRA_START_TIME`](https://developer.android.com/reference/android/content/Intent#EXTRA_START_TIME), and [`EXTRA_END_TIME`](https://developer.android.com/reference/android/content/Intent#EXTRA_END_TIME).

Depending on which intent filters you add, users see an information icon
next to your app's name on certain screens:

- If you add the intent filter that contains the `VIEW_PERMISSION_USAGE` action, users see the icon on your app's permissions page in system settings. You can apply this action to all runtime permissions.
- If you add the intent filter that contains the `VIEW_PERMISSION_USAGE_FOR_PERIOD` action, users see the icon next to your app's name whenever your app appears in the Privacy Dashboard screen.

When users select that icon, your app's rationale activity is started.  
![A rounded rectangle in the upper-right corner, which
includes a camera icon and a microphone icon](https://developer.android.com/static/images/training/permissions/mic-camera-indicators.svg) **Figure 2.** Microphone and camera indicators, which show recent data access.

## Indicators

| **Note:** The icon mentioned in this section shouldn't require changes to your app's logic, as long as you [follow privacy best
| practices](https://developer.android.com/privacy/best-practices).

On devices that run Android 12 or higher, when an app accesses
the microphone or camera, an icon appears in the status bar. If the app is in
[immersive mode](https://developer.android.com/training/system-ui/immersive#immersive), the icon appears in
the upper-right corner of the screen. Users can open Quick Settings and select
the icon to view which apps are currently using the microphone or camera.
Figure 2 shows an example screenshot that contains the icons.

### Identify the screen location of indicators

If your app supports immersive mode or a full-screen UI, the indicators might
momentarily overlap your app's UI. To help adapt your UI to these indicators,
the system introduces the
[`getPrivacyIndicatorBounds()`](https://developer.android.com/reference/android/view/WindowInsets.Builder#setPrivacyIndicatorBounds(android.graphics.Rect))
method, which the following code snippet demonstrates. Using this API, you can
identify the bounds where the indicators might appear. You might then decide to
organize your screen's UI differently.  

### Kotlin

```kotlin
view.setOnApplyWindowInsetsListener { view, windowInsets ->
    val indicatorBounds = windowInsets.getPrivacyIndicatorBounds()
    // change your UI to avoid overlapping
    windowInsets
}
```

## Toggles

| **Note:** The toggles mentioned in this section shouldn't require changes to your app's logic, as long as you [follow privacy best
practices](https://developer.android.com/privacy/best-practices).  
![Quick settings tiles are labeled 'Camera access' and
'Mic access'](https://developer.android.com/static/images/training/permissions/mic-camera-toggles.svg) **Figure 3.** Microphone and camera toggles in Quick Settings.

On [supported devices](https://developer.android.com/training/permissions/explaining-access#toggles-check-device-support) that run
Android 12 or higher, users can enable and disable camera and
microphone access for all apps on the device by pressing a single toggle
option. Users can access the toggleable options from [Quick
Settings](https://support.google.com/android/answer/9083864), as shown in
figure 3, or from the Privacy screen in system settings.

The camera and microphone toggles affect all apps on the device:

- When the user turns off camera access, your app receives a blank camera feed.
- When the user turns off microphone access, your app receives silent audio.
  Additionally, [motion sensors are
  rate-limited](https://developer.android.com/guide/topics/sensors/sensors_overview#sensors-rate-limiting),
  regardless of whether you declare the
  [`HIGH_SAMPLING_RATE_SENSORS`](https://developer.android.com/reference/android/Manifest.permission#HIGH_SAMPLING_RATE_SENSORS)
  permission.

  | **Note:** When the user places a call to emergency services, such as 911, the system turns on microphone access. This behavior preserves user safety.

When the user turns off access to camera or microphone, then
launches an app that needs access to camera or microphone information, the
system reminds the user that the device-wide toggle is turned off.

### Check device support

To check whether a device supports microphone and camera toggles, add the logic
that appears in the following code snippet:  

### Kotlin

```kotlin
val sensorPrivacyManager = applicationContext
        .getSystemService(SensorPrivacyManager::class.java)
        as SensorPrivacyManager
val supportsMicrophoneToggle = sensorPrivacyManager
        .supportsSensorToggle(Sensors.MICROPHONE)
val supportsCameraToggle = sensorPrivacyManager
        .supportsSensorToggle(Sensors.CAMERA)
```

### Java

```java
SensorPrivacyManager sensorPrivacyManager = getApplicationContext()
        .getSystemService(SensorPrivacyManager.class);
boolean supportsMicrophoneToggle = sensorPrivacyManager
        .supportsSensorToggle(Sensors.MICROPHONE);
boolean supportsCameraToggle = sensorPrivacyManager
        .supportsSensorToggle(Sensors.CAMERA);
```