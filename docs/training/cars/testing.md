---
title: Test Android apps for cars  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/testing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Test Android apps for cars Stay organized with collections Save and categorize content based on your preferences.




While developing your app, there are a variety of tools available to run Android
Auto and Android Automotive OS:

* See [Test your app using the Desktop Head Unit](/training/cars/testing/dhu) for details on how to
  install and use the Desktop Head Unit to run Android Auto apps.
* See [Test your app using the Android Automotive OS emulator](/training/cars/testing/emulator) for details
  on how to install and run Android Automotive OS images.
* See [Test using Android Automotive OS on Pixel Tablet](/training/cars/testing/aaos-on-pixel) for details on how
  to install Android Automotive OS on a Pixel Tablet. Certain images also
  support use as an Android Auto receiver.
* See [Access Android Automotive OS devices through Firebase Test Lab](/training/cars/testing/firebase) for
  details on how to test on real car hardware using Firebase Test Lab.
* See [Test interoperability with Google Services](/training/cars/testing/gas-intents) on how to test the
  interoperability of Google Assistant and Google Maps with custom apps on
  Android Automotive OS.

**Important:** Before submitting your app to Google Play for review, test its user
experience. Also, check that your app meets all the criteria for its category
listed on the [Android app quality for cars](/docs/quality-guidelines/car-app-quality) page.

## Test in real vehicles

To test your app in real vehicles, you must install it from a trusted source
such as the Play Store, with one exception detailed in
[Allow unknown sources](#unknown-sources). You can use [Internal App Sharing](https://play.google.com/console/about/internalappsharing/) or an
[Internal Test Track](https://play.google.com/console/about/internal-testing/) to distribute your app to devices without going through
the Play Store review process.

### Allow unknown sources

Android Auto has a [developer option](#developer-mode) that lets you run apps that aren't
installed from a trusted source. This setting applies to [media](/training/cars/media), [messaging
notifications](/training/cars/communication/notification-messaging), and [parked](/training/cars/parked) apps but doesn't apply to apps built using
the [Android for Cars App Library](/training/cars/apps).

## Enable Android Auto developer mode

In addition to the [Android developer options](/studio/debug/dev-options) (usable on both Android Auto
and Android Automotive OS), Android Auto has its own developer mode. To enable
it, follow these steps:

1. Open the Android Auto settings.

   * Android 10 or higher: on the device, tap **Settings > Apps &
     notifications > See all apps > Android Auto > Advanced > Additional
     settings in the app**.
   * Android 9 or lower: in the Android Auto app, tap the menu, then tap
     **Settings**.
2. Go to the **About** section near the bottom and tap **Version** to display
   the version and permission information.
3. Tap the **Version and permission info** section 10 times.

   The **Allow development settings?** dialog appears.
4. Tap **OK**.

   Developer mode is now enabled, and you can access developer options in the
   overflow menu. You only need to enable developer mode once. To quit
   developer mode, use the option from the drop-down menu in the app bar.

## Additional testing requirements for media apps

If you are testing a [media app](/training/cars#media), test for the scenarios that are covered in
this section in addition to testing your app on Android Auto, Android Automotive
OS, or both.

### Test MediaBrowserService startup scenarios

To help keep drivers and passengers safe, users have additional restrictions on
how they can interact with apps while driving. For this reason, Android Auto and
Android Automotive OS have [`MediaBrowserService`](/reference/androidx/media/MediaBrowserServiceCompat) startup scenarios that
your app must handle.

Test your app to make sure it can handle each of the following scenarios:

* The `MediaBrowserService` is run before any `Activity` is opened.
* The `MediaBrowserService` is run when no `Activity` can be shown.
* The `MediaBrowserService` is run when the user is not signed in.

While testing for these scenarios, be sure to try the following methods:

* Force stop the app, and then launch it.
* Clear the app data, and then launch it.

Also make sure to [set an appropriate error message](/training/cars/media/errors) when necessary.

### Use the Media Controller Test app

The [Media Controller Test](https://github.com/googlesamples/android-media-controller) app lets you test the intricacies of media
playback on Android and helps verify your media session implementation. To get
started with this tool, see [Using the media controller test app](/guide/topics/media-apps/audio-app/media-controller-test).