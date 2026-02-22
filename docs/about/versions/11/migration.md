---
title: https://developer.android.com/about/versions/11/migration
url: https://developer.android.com/about/versions/11/migration
source: md.txt
---

With each release of Android, we introduce new features as well as behavior
changes aimed at making the Android more helpful, more secure, and better
performing. In many cases your app will work exactly as expected out of the box,
while in other cases you might need to make changes to your app to adapt to the
platform changes.

Since users can start receiving the new platform as soon as the source code is
released to AOSP (Android Open Source Project), it's important for apps to be
ready, performing as expected for users and ideally taking advantage of new
features and APIs to get the most out of the new platform.

This document offers a high-level view of typical development and testing phases
that can help you make a plan for readiness that's well-aligned with the
platform release timeline and ensures a great experience for your users on
Android 11.

A typical migration has two phases, which can be concurrent:

- Ensuring app compatibility (by Android 11 final release)
- Targeting the new platform features and APIs (as soon as possible after final release)

This page outlines the general steps for each of those phases. When you're ready
to get started, read [Get Android 11](https://developer.android.com/about/versions/11/get).

## Ensure compatibility with Android 11

It's important to test the functionality of your existing app against
Android 11 to ensure a great experience for users updating to the
latest version of Android. Some platform changes can affect the way your app
behaves, so it's important to test early and thoroughly, then make any needed
adjustments to your app.

Typically you can adjust your app and publish an update without needing to
change the app's `targetSdkVersion`. Similarly, you shouldn't need to use new
APIs or change the app's `compileSdkVersion`, although this can depend on the
way your app is built and the platform functionality it's using. The following
sections outline the steps.

Before you get started, make sure to familiarize yourself with the [behavior
changes](https://developer.android.com/about/versions/11/behavior-changes-all) that might affect your app, even if you don't change its
`targetSdkVersion`.

![](https://developer.android.com/static/images/about/versions/11/android-11-compatibility-flow.svg)

### Perform compatibility testing

For the most part, testing compatibility with Android 11 is
similar to the type of testing you otherwise perform when preparing to release
your app. This is a good time to review the [core app quality guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and
[best practices for testing](https://developer.android.com/training/testing).

Just install your current published app on a device running
Android 11 and work through all the flows and functionality
looking for issues. To help you focus your testing, **review the [behavior
changes](https://developer.android.com/about/versions/11/behavior-changes-all)** introduced in Android 11 that can affect your app's
function or cause the app to crash. In particular, make sure to review the [key
privacy changes](https://developer.android.com/about/versions/11/privacy) and test any fixes that you implement to accommodate the
changes.

Also make sure to review and **test for uses of restricted non-SDK interfaces**
and move to public SDK or NDK equivalents instead. Watch for logcat warnings
that highlight these accesses and use the StrictMode method
[`detectNonSdkApiUsage()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectNonSdkApiUsage()) to catch them programmatically.

Last, make sure to fully **test the libraries and SDKs in your app** to make
sure they work as expected on Android 11 and follow best
practices for privacy, performance, UX, data handling, and permissions. If you
find an issue, try updating to the latest version of the SDK, or reach out to
the SDK developer for help.

When you've finished your testing and made any updates, we recommend publishing
your compatible app right away. This lets your users test the app early, and
helps you to deliver a smooth transition to users as they update to
Android 11.

## Update the app's targeting and build with new APIs

Once you've published the compatible version of your app as described
previously, the next step is to add full support for Android 11
by updating its `targetSdkVersion` and taking advantage of new aPIs and
capabilities Android 11. You can do these as soon as you are
ready, keeping in mind the [Google Play requirement](https://support.google.com/googleplay/android-developer/answer/113469#targetsdk) for targeting the new
platform.

As you plan your work to fully support Android 11, a good place
to start is reviewing the [behavior changes that apply to apps targeting
Android 11](https://developer.android.com/about/versions/11/behavior-changes-11). These *targeted behavior changes* may cause
functional issues that you may need to address. In some cases, they can require
significant development, so it's best to learn about them early. To help you
assess the impacts, you can also use the [compatibility toggles](https://developer.android.com/about/versions/11/migration#using_app_compatibility_toggles) to test
your current app with selected changes enabled.

The following steps describe how to fully support Android 11.

![](https://developer.android.com/static/images/about/versions/11/android-11-building-flow.svg)

### Get the SDK, change targeting, build with new APIs

To get started with full Android 11 support, first download the
Android 11 SDK (and any other tools needed) into Android Studio.
Next change the app's `targetSdkVersion` and `compileSdkVersion` to `"30"`and
re-compile the app. See the [setup guide](https://developer.android.com/about/versions/11/setup-sdk) for details.

### Test your Android 11 app

Once you've compiled the app and installed it on a device running
Android 11, begin testing to ensure that the app works properly
when targeting Android 11. Some behavior changes apply only when
your app is targeting the new platform, so you'll want to [review those
changes](https://developer.android.com/about/versions/11/behavior-changes-11) before getting started.

As with basic compatibility testing, work through all the flows and
functionality looking for issues. Focus your testing on the
**[behavior changes for apps targeting Android 11](https://developer.android.com/about/versions/11/behavior-changes-11)** . In
particular, make sure to review the [privacy changes](https://developer.android.com/about/versions/11/privacy) and test any fixes that
you implement to accommodate the changes. It's also a good time to check your
app against the [core app quality guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [best practices for
testing](https://developer.android.com/training/testing).

Make sure to review and **test for uses of [restricted non-SDK interfaces](https://developer.android.com/about/versions/11/non-sdk-11)**
that may apply. Watch for logcat warnings that highlight these accesses and use
the StrictMode method [`detectNonSdkApiUsage()`](https://developer.android.com/reference/android/os/StrictMode.VmPolicy.Builder#detectNonSdkApiUsage()) to catch them
programmatically.

Last, make sure to fully **test the libraries and SDKs in your app** to make
sure they work as expected on Android 11 and follow best
practices for privacy, performance, UX, data handling, and permissions. If you
find an issue, try updating to the latest version of the SDK, or reach out to
the SDK developer for help.

### Test using app compatibility toggles

Android 11 introduces a new feature for developers that makes it easier to test
your app with targeted behavior changes. For a debuggable app, the toggles let
you:

- **Test targeted changes without actually changing the app's
  targetSdkVersion**. You can use the toggles to force-enable specific targeted behavior changes to evaluate the impact on your existing app.
- **Focus your testing on specific changes only**. Rather than having to address all targeted changes at once, the toggles let you disable all targeted changes except the ones you want to test against.
- **Manage toggles through adb**. You can use adb commands to enable and disable the toggleable changes in your automated test environment.
- **Debug faster using standard change IDs**. Toggleable changes each have a unique ID and name that you can use to quickly debug root cause in log output.

As you prepare for changing your app's targeting, or while you in active
development for Android 11 support, the toggles can help. See the [corresponding
documentation for more details](https://developer.android.com/guide/app-compatibility/test-debug).