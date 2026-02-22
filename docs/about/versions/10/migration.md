---
title: https://developer.android.com/about/versions/10/migration
url: https://developer.android.com/about/versions/10/migration
source: md.txt
---

Welcome! Android 10 has many new APIs for building new experiences, as well as
updated system behaviors that can affect your app when it's running on Android
10 devices.

To get started, we recommend reviewing the [system behavior changes](https://developer.android.com/about/versions/10/behavior-changes-all),
[privacy changes](https://developer.android.com/about/versions/10/privacy/changes), and [new features and APIs](https://developer.android.com/about/versions/10/highlights), then migrating your apps
in these two phases:

1. [Ensure basic compatibility](https://developer.android.com/about/versions/10/migration#compat). As soon as possible, make sure your existing published app is ready for users who are updating or purchasing new devices running Android 10. Test your app to verify that it's fully functional, then publish the compatible version of the app to users.
2. [Build with Android 10 features and APIs](https://developer.android.com/about/versions/10/migration#use_apis). Next, explore the new features and APIs in Android 10. Set up your development environment, change your app's `targetSdkVersion`, and build with the new APIs that are relevant for your app.

The following sections highlight what you'll need to do in each of these phases.
Before you get started, make sure you've [prepared a hardware device](https://developer.android.com/about/versions/10/get) or
emulator) to run and test your app.

## Phase 1: Basic compatibility

The goal of this phase is to identify any functionality regressions or other
impacts when your app is running on Android 10, then address them and publish an
updated version to users. In many cases you shouldn't need to change your app's
`targetSdkVersion` or use new APIs, although you can optionally change your
`compileSdkVersion` to support compatibility.

It's important to test the functionality of your existing app through all flows,
because some platform changes can affect the way your app behaves. When you
publish the compatible version of your app, we recommend notifying users of
Android 10 support in your update notes.


To give your users a smooth transition to Android 10, we recommend publishing a
compatible version of your app as early as possible --- ideally before
devices begin receiving Android 10 updates.

![](https://developer.android.com/static/images/about/versions/10/q-compat-flow.png)

### Perform testing

Compatibility testing entails the same type of testing you perform when
preparing to release your app. This is a good time to review the [core app
quality guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and [best practices for testing](https://developer.android.com/training/testing).

Make sure to familiarize yourself with the known behavior changes that can
affect your app. [These behavior changes](https://developer.android.com/about/versions/10/behavior-changes-all) will apply to your app, even if you
haven't changed your `targetSdkVersion`. Reviewing the changes in advance will
help you to identify possible impact areas and debug any issues more quickly.

Android 10 includes extensive changes for privacy, so make sure you also [review
the key privacy changes](https://developer.android.com/about/versions/10/privacy/changes) and understand the possible impacts on your app.

## Phase 2: Build with Android 10

Whenever you are ready, you can explore the new features and APIs in Android 10
and enhance your app with new experiences. To start developing with the new
APIs, you'll need to set up the Android 10 (API 29) SDK in Android Studio and
change both your `targetSdkVersion` and `compileSdkVersion` to `29`.

When you change your `targetSdkVersion`, you'll also need to account for [system
behavior changes](https://developer.android.com/about/versions/10/behavior-changes-10) that apply to your app when you are targeting Android 10
(API 29) or higher.

Some behavior changes might cause regressions or crashes, so make sure to review
the changes and test thoroughly before publishing an app update that changes
your `targetSdkVersion`.
| **Note:** The previously described steps to [ensure platform compatibility](https://developer.android.com/about/versions/10/migration#compat) are prerequisite to targeting your app to Android 10, so be sure to complete those steps first.

![](https://developer.android.com/static/images/about/versions/10/q-building-flow.png)

### Get the SDK

To get the SDK packages to build your app with Android 10, first make sure
you're using the latest version of [Android Studio](https://developer.android.com/studio). To learn more, read
[Set up the SDK](https://developer.android.com/about/versions/10/setup-sdk).

### Perform testing

With the previously described preparations complete, you can build your app and
then test it further to make sure it works properly when targeting Android 10.
This is another good time to review the [core app quality guidelines](https://developer.android.com/develop/quality-guidelines/core-app-quality) and
[best practices for testing](https://developer.android.com/training/testing).

When you build your app with the `targetSdkVersion` set to `29`, there are
specific platform changes you should be aware of. Some of these changes, which
are described on the [Android 10 behavior changes](https://developer.android.com/about/versions/10/behavior-changes-10) page, can significantly
affect your app's behavior or cause crashes --- even if you don't yet use new
APIs.