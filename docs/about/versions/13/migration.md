---
title: https://developer.android.com/about/versions/13/migration
url: https://developer.android.com/about/versions/13/migration
source: md.txt
---

<br />

This document offers a high-level view of typical development and testing phases
that can help you make a plan for readiness that's well-aligned with the
platform release timeline and ensures a great experience for your users on
Android 13.

With each release of Android, we introduce new features as well as behavior
changes aimed at making Android more helpful, more secure, and more performant.
In many cases your app will work exactly as expected out-of-the-box, while in
other cases you might need to update your app to adapt to the platform changes.

Users can start receiving the new platform as soon as the source code is
released to AOSP (Android Open Source Project), so it's important for your apps
to be ready, performing as expected for users and ideally taking advantage of
new features and APIs to get the most out of the new platform.

A typical migration has two phases, which can be concurrent:

- Ensuring app compatibility (by Android 13 final release)
- Targeting the new platform features and APIs (as soon as possible after final release)

## Ensure compatibility with Android 13

It's important to test the functionality of your existing app against
Android 13 to ensure a great experience for users updating to the
latest version of Android. Some platform changes can affect the way your app
behaves, so it's important to test early and thoroughly and make any needed
adjustments to your app.

You can usually adjust your app and publish an update without needing to change
the app's `targetSdkVersion`. Similarly, you shouldn't need to use new APIs or
change the app's `compileSdkVersion`, although this can depend on the way your
app is built and the platform functionality it's using.

Before you start testing, be sure to familiarize yourself with the [behavior
changes for all apps](https://developer.android.com/about/versions/13/behavior-changes-all). These changes might affect your app, even if you don't
change its `targetSdkVersion`.
Get Android 13 Flash an Android 13 system image to your device, or download
a system image for the Android emulator.
Review changes Review system behavior changes to identify areas where your app
might be affected.
Test Install your app on your device or emulator, and run tests. Focus
on system behavior changes, and work through all app flows.
Update Make only the code changes required to adapt to behavior
changes or resolve issues. Recompile with the same API level
that your app originally targeted - no need to target Android 13.
Publish Sign, upload, and publish your updated Android App Bundle
or APK.

### Perform compatibility testing

For the most part, testing compatibility with Android 13 is
similar to ordinary app testing. This is a good time to review the [core app
quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality) and [best practices for testing](https://developer.android.com/training/testing).

To test, install your current published app on a device running
Android 13, and work through all the flows and functionality
while looking for issues. To help you focus your testing,
**review the [behavior changes for all apps](https://developer.android.com/about/versions/13/behavior-changes-all)** introduced in
Android 13 that can affect how your app functions or cause your
app to crash.

Also make sure to **review and test for uses of [restricted non-SDK
interfaces](https://developer.android.com/about/versions/13/changes/non-sdk-13)** . You should replace any restricted interface your app uses with
a public SDK or NDK equivalent. Watch for logcat warnings that highlight these
accesses, and use the `StrictMode` method [`detectNonSdkApiUsage()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectNonSdkApiUsage()) to catch
them programmatically.

Last, make sure to fully **test the libraries and SDKs in your app** to make
sure they work as expected on Android 13 and follow best
practices for privacy, performance, UX, data handling, and permissions. If you
find an issue, try updating to the latest version of the SDK, or reach out to
the SDK developer for help.

When you've finished your testing and made any updates, we recommend publishing
your compatible app right away. This lets your users test the app early and
helps ensure a smooth transition for your users as they update to
Android 13.

## Update the app's targeting and build with new APIs

Once you've published a compatible version of your app, the next step is to add
full support for Android 13 by updating its `targetSdkVersion`
and taking advantage of new APIs and capabilities in Android 13.
You can make these updates as soon as you're ready, keeping in mind the [Google
Play requirements](https://developer.android.com/distribute/play-policies) for targeting the new platform.

As you plan your work to fully support Android 13, review the
[behavior changes that affect apps targeting Android 13](https://developer.android.com/about/versions/13/behavior-changes-13).
These *targeted behavior changes* might cause functional issues you then need to
address. In some cases, these changes require significant development, so we
recommend learning about and addressing them as early as possible. To help
identify specific behavior changes that affect your app, use the [compatibility
toggles](https://developer.android.com/about/versions/13/migration#using_app_compatibility_toggles) to test your app with selected changes enabled.

The following steps describe how to fully support Android 13.
Get Android 13 SDK Install the latest version of Android Studio preview to build
with Android 13. Make sure you have an Android 13 device or
emulator.  

Update your `targetSdkVersion` and other build
configurations.
Review behavior changes Review the behavior changes that apply to apps targeting
Android 13. Identify areas where your app might be affected,
and plan how to support them.
Check against new privacy changes Make code and architecture changes needed to support Android 13's
user privacy changes.
Adopt Android 13 features Take advantage of Android 13 APIs to bring new features and
capabilities to your apps. Recompile for Android 13.
Test Test on an Android 13 device or emulator. Focus on areas
where behavior changes might affect your app. Try out
functionality that uses new APIs. Provide platform and API
feedback. Report any platform, API, or third-party SDK issues.
Final update Once Android 13 APIs are final, update your
`targetSdkVersion` and other build configurations
again, make any additional updates, and test your app.
Publish Sign, upload, and publish your updated Android App Bundle
or APK.

### Get the SDK, change targeting, build with new APIs

To start testing for full Android 13 support, use the latest
preview version of Android Studio to download the Android 13 SDK
and any other tools you need. Next, update your app's `targetSdkVersion` and
`compileSdkVersion`, and re-compile the app. See the [SDK setup guide](https://developer.android.com/about/versions/13/setup-sdk) for
details.

### Test your Android 13 app

Once you've compiled the app and installed it on a device running
Android 13, begin testing to ensure that the app works properly
when targeting Android 13. Some behavior changes apply only when
your app is targeting the new platform, so you'll want to [review those
changes](https://developer.android.com/about/versions/13/behavior-changes-13) before getting started.

As with basic compatibility testing, work through all the flows and
functionality looking for issues. Focus your testing on the
**[behavior changes for apps targeting Android 13](https://developer.android.com/about/versions/13/behavior-changes-13)** . It's
also a good time to check your app against the [core app quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality)
and [best practices for testing](https://developer.android.com/training/testing).

Make sure to review and **test for uses of [restricted non-SDK interfaces](https://developer.android.com/about/versions/13/changes/non-sdk-13)**
that may apply. Watch for logcat warnings that highlight these accesses and use
the StrictMode method [`detectNonSdkApiUsage()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectNonSdkApiUsage()) to catch them
programmatically.

Last, make sure to fully **test the libraries and SDKs in your app** to make
sure they work as expected on Android 13 and follow best
practices for privacy, performance, UX, data handling, and permissions. If you
find an issue, try updating to the latest version of the SDK, or reach out to
the SDK developer for help.

### Test using app compatibility toggles

Android 13 includes compatibility toggles that make it easier to test your app
with targeted behavior changes. For a debuggable app, the toggles let you:

- **Test targeted changes without actually changing the app's
  targetSdkVersion**. You can use the toggles to force-enable specific targeted behavior changes to evaluate the impact on your existing app.
- **Focus your testing on specific changes only**. Rather than having to address all targeted changes at once, the toggles let you disable all targeted changes except the ones you want to test against.
- **Manage toggles through adb**. You can use adb commands to enable and disable the toggleable changes in your automated test environment.
- **Debug faster using standard change IDs**. Toggleable changes each have a unique ID and name that you can use to quickly debug root cause in log output.

As you prepare for changing your app's targeting, or while you in active
development for Android 13 support, the toggles can help. For more information,
see [Compatibility framework changes (Android 13)](https://developer.android.com/about/versions/13/reference/compat-framework-changes).