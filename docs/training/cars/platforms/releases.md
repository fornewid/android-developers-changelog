---
title: Releases  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/platforms/releases
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Releases Stay organized with collections Save and categorize content based on your preferences.




With each [Android release](/about/versions), API and behavior changes impact how apps work on
Android Auto and Android Automotive OS. This page details many of these impacts
and provides information on how to update your app to support new versions of
Android.

## Android 16

* Android Auto makes uses of [virtual device owner overrides](/about/versions/16/behavior-changes-all#virtual-device-owner-overrides) to ignore
  orientation, aspect ratio, and resizability restrictions when running [parked
  apps](/training/cars/platforms/android-auto#parked-apps)
* If your app uses the Android 16 updates for [safer intents](/about/versions/16/behavior-changes-16#safer-intents), you might
  need to specify the [`android:intentMatchingFlags`](/reference/android/R.attr#intentMatchingFlags) attribute of the
  `<service>` element for your `CarAppService` as `allowNullAction` to allow
  Android Auto and Android Automotive OS to connect to your service.

## Android 15

* Apps for Android Automotive OS that use the Android for Cars App Library must
  update to [version 1.7.0-rc01](/jetpack/androidx/releases/car-app#1.7.0-rc01) or later. This prevents crashes when running
  on Android 15 or higher, that can be caused by the
  [secured background activity launch changes](/about/versions/15/behavior-changes-15#secured-bal) when permission dialogs are
  triggered.
* Because of the [window inset changes](/about/versions/15/behavior-changes-15#window-insets) for apps targeting Android 15 or
  higher, you should test apps distributed to Android Automotive OS to verify that
  activities implemented by your app render as intended. See [Work with window
  insets and display cutouts](/training/cars/parked/automotive-os#insets-and-cutouts) for more details on the considerations unique to
  Android Automotive OS.

## Android 14

* Because of the requirement for apps targeting Android 14 or higher that
  [foreground service types are required](/about/versions/14/behavior-changes-14#fgs-types), check that you specify a foreground
  service type for any foreground services your app has, such as those for
  navigation and media playback.
* Because of the requirement for apps targeting Android 14 or higher that
  [runtime-registered broadcast receivers must specify export behavior](/about/versions/14/behavior-changes-14#runtime-receivers-exported), apps
  that use the `CarConnection` API should update to
  `androidx.car.app:app:1.3.0-beta01` or later. See [Connection API](/training/cars/apps#car-connection).
* Because of changes in Android Auto when running on Android 14 and higher
  devices, launching activities on the phone screen from the Android Auto app
  requires providing an [`ActivityOptions`](/reference/android/app/ActivityOptions) with the display ID set to that of
  the phone display ([`DEFAULT_DISPLAY`](/reference/android/view/Display#DEFAULT_DISPLAY)) when calling [`startActivity()`](/reference/android/content/Context#startActivity(android.content.Intent,%20android.os.Bundle)).
  + Apps that use the [`CarContext.requestPermissions()`](/reference/androidx/car/app/CarContext#requestPermissions(java.util.List%3Cjava.lang.String%3E,androidx.car.app.OnRequestPermissionsListener)) method should
    update to `androidx.car.app:app:1.7.0-alpha01` or later, which includes this
    fix.

## Android 13

* For apps built using the Android for Cars App Library, the locale of the
  `Configuration` provided by the `CarContext` reflects the [Per-application
  language preferences](/guide/topics/resources/app-languages) for the host app, not that of your app.

## Android 12

* On devices running Android 12 or higher, Android Auto doesn't change the
  [UI mode](/reference/android/content/res/Configuration#uiMode) of the device when running. See [How can I detect if Android Auto
  is running?](/training/cars/platforms/android-auto#detect-connection).
* Because of the [safer component exporting](/about/versions/12/behavior-changes-12#exported) requirements for apps targeting
  Android 12 or higher, you must explicitly declare the `android:exported`
  attribute on the `<service>` element for `MediaBrowserService` and
  `CarAppService` services.
* Because of the [pending intents mutability](/about/versions/12/behavior-changes-12#pending-intent-mutability) requirements for apps targeting
  Android 12 or higher, you must explicitly specify the mutability of any pending
  intent created by your app. For example, this includes the pending intents
  messaging apps use to handle replying to messages or marking them as read.