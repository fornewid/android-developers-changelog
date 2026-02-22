---
title: https://developer.android.com/studio/releases/past-releases/as-1-5-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-1-5-0-release-notes
source: md.txt
---

<br />

# Android Studio v1.5.0 (November 2015)

Fixes and enhancements:

- Added new Memory Monitor analysis abilities to Android Monitor. When you view an HPROF file captured from this monitor, the display is now more helpful so you can more quickly locate problems, such as memory leaks. To use this monitor, click **Android Monitor** at the bottom of the main window. In Android Monitor, click the **Memory** tab. While the monitor is running, click the **Dump Java Heap** icon, and then click **Captures** in the main window and double-click the file to view it. Click *Capture Analysis* on the right. (The Android Device Monitor can't be running at the same time as Android Monitor.)
- Added new deep link and app link support. The Code Editor can automatically create an intent filter for deep linking in the `AndroidManifest.xml` file. It can also generate code to help you integrate with the [App Indexing API](http://developers.google.com/app-indexing/android/publish) in an activity in a Java file. A deep link testing feature helps you verify that a specified deep link can launch an app. In the **General** tab of the *Run/Debug Configurations* dialog, you can specify deep link launch options. You can also test App Indexing API calls in an activity by using the Android Monitor **logcat** display. The Android `lint` tool now has warnings for certain issues involving deep links and the App Indexing API.
- Added the ability to use short names when code-completing custom views in the Code Editor.
- Added support for more [VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable) elements to [Vector Asset Studio](https://developer.android.com/tools/help/vector-asset-studio) for backward-compatibility. Vector Asset Studio can use these elements to convert vector drawables into PNG raster images to use with Android 4.4 (API level 20) and lower.
- Added new `lint` checks for Android TV and Android Auto to give you immediate, actionable feedback in Android Studio, along with several quick fixes. For example, for Android TV, it can report and provide a quick fix for permissions, unsupported hardware, `uses-feature` element, and missing banner issues. For Android Auto, it can validate the correct usage in the descriptor file referred from your `AndroidManifest.xml` file, report if there isn't an intent filter for the `MediaBrowserService` class, and identify certain voice actions issues.
- Added new `lint` checks for insecure broadcast receivers, `SSLCertificateSocketFactory` and `HostnameVerifier` class uses, and `File.setReadable()` and `File.setWritable()` calls. It also detects invalid manifest resource lookups, especially for resources that vary by configuration.
- Fixed a number of stability issues.

<br />