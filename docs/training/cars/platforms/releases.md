---
title: https://developer.android.com/training/cars/platforms/releases
url: https://developer.android.com/training/cars/platforms/releases
source: md.txt
---

# Releases

With each[Android release](https://developer.android.com/about/versions), API and behavior changes impact how apps work on Android Auto and Android Automotive OS. This page details many of these impacts and provides information on how to update your app to support new versions of Android.

## Android 16

- Android Auto makes uses of[virtual device owner overrides](https://developer.android.com/about/versions/16/behavior-changes-all#virtual-device-owner-overrides)to ignore orientation, aspect ratio, and resizability restrictions when running[parked apps](https://developer.android.com/training/cars/platforms/android-auto#parked-apps)
- If your app uses the Android 16 updates for[safer intents](https://developer.android.com/about/versions/16/behavior-changes-16#safer-intents), you might need to specify the[`android:intentMatchingFlags`](https://developer.android.com/reference/android/R.attr#intentMatchingFlags)attribute of the`<service>`element for your`CarAppService`as`allowNullAction`to allow Android Auto and Android Automotive OS to connect to your service.

## Android 15

- Because of the[window inset changes](https://developer.android.com/about/versions/15/behavior-changes-15#window-insets)for apps targeting Android 15 or higher, you should test apps distributed to Android Automotive OS to verify that activities implemented by your app render as intended. See[Work with window insets and display cutouts](https://developer.android.com/training/cars/parked/automotive-os#insets-and-cutouts)for more details on the considerations unique to Android Automotive OS.

## Android 14

- Because of the requirement for apps targeting Android 14 or higher that[foreground service types are required](https://developer.android.com/about/versions/14/behavior-changes-14#fgs-types), check that you specify a foreground service type for any foreground services your app has, such as those for navigation and media playback.
- Because of the requirement for apps targeting Android 14 or higher that[runtime-registered broadcast receivers must specify export behavior](https://developer.android.com/about/versions/14/behavior-changes-14#runtime-receivers-exported), apps that use the`CarConnection`API should update to`androidx.car.app:app:1.3.0-beta01`or later. See[Connection API](https://developer.android.com/training/cars/apps#car-connection).
- Because of changes in Android Auto when running on Android 14 and higher devices, launching activities on the phone screen from the Android Auto app requires providing an[`ActivityOptions`](https://developer.android.com/reference/android/app/ActivityOptions)with the display ID set to that of the phone display ([`DEFAULT_DISPLAY`](https://developer.android.com/reference/android/view/Display#DEFAULT_DISPLAY)) when calling[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent,%20android.os.Bundle)).
  - Apps that use the[`CarContext.requestPermissions()`](https://developer.android.com/reference/androidx/car/app/CarContext#requestPermissions(java.util.List%3Cjava.lang.String%3E,androidx.car.app.OnRequestPermissionsListener))method should update to`androidx.car.app:app:1.7.0-alpha01`or later, which includes this fix.

## Android 13

<br />

- For apps built using the Android for Cars App Library, the locale of the`Configuration`provided by the`CarContext`reflects the[Per-application language preferences](https://developer.android.com/guide/topics/resources/app-languages)for the host app, not that of your app.

## Android 12

- On devices running Android 12 or higher, Android Auto doesn't change the[UI mode](https://developer.android.com/reference/android/content/res/Configuration#uiMode)of the device when running. See[How can I detect if Android Auto is running?](https://developer.android.com/training/cars/platforms/android-auto#detect-connection).
- Because of the[safer component exporting](https://developer.android.com/about/versions/12/behavior-changes-12#exported)requirements for apps targeting Android 12 or higher, you must explicitly declare the`android:exported`attribute on the`<service>`element for`MediaBrowserService`and`CarAppService`services.
- Because of the[pending intents mutability](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability)requirements for apps targeting Android 12 or higher, you must explicitly specify the mutability of any pending intent created by your app. For example, this includes the pending intents messaging apps use to handle replying to messages or marking them as read.