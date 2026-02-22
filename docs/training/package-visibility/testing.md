---
title: https://developer.android.com/training/package-visibility/testing
url: https://developer.android.com/training/package-visibility/testing
source: md.txt
---

If your app relies on interactions with other apps to complete its use cases,
it's useful to test how [package visibility](https://developer.android.com/training/package-visibility)
changes in Android 11 (API level 30) and higher affect your app.

This guide also gives some suggestions on how to test the behavior changes
and helps you configure log messages to determine at a more granular
level how your app might be affected.

## Test the behavior changes

To test whether this behavior change affects your app, complete the
following steps:

1. Install [Android Studio 3.6.1](https://developer.android.com/studio) or higher.
2. Install the latest version of Gradle that Android Studio supports.
3. Set your app's `targetSdkVersion` to `30` or higher.
4. Don't include the `<queries>` element in your app's manifest file.
5. Call [`getInstalledApplications()`](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledApplications(int)) or [`getInstalledPackages()`](https://developer.android.com/reference/android/content/pm/PackageManager#getInstalledPackages(int)). Both methods return a filtered list when they are successful.
6. See which features of your app aren't working.
7. Introduce appropriate [`<queries>`](https://developer.android.com/guide/topics/manifest/queries-element) entries to fix those features.

## Configure log messages for package filtering

To discover more details about how the default visibility of apps affects your
app, you can enable log messages for package filtering. If you're developing a
test app or debuggable app in Android Studio, the [system log provides this
capability](https://developer.android.com/studio/debug#systemLog) for you. Otherwise, you can run the
following command in a terminal window to enable it manually:  

```
adb shell pm log-visibility --enable PACKAGE_NAME
```

Then, whenever packages are filtered out of a `PackageManager` object's return
values, you see a message similar to the following in Logcat:  

```
I/AppsFilter: interaction: PackageSetting{7654321 \
  com.example.myapp/12345} -> PackageSetting{...} BLOCKED
```
| **Caution:** Your app's performance is affected when this flag is enabled. Unless you're testing how package visibility affects your app, disable the logging of messages related to package visibility.