---
title: Android Studio  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-2-1-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

Stay organized with collections

Save and categorize content based on your preferences.




# Android Studio 2.1 (April 2016)

The primary changes in this update provide support for development with the
Android N Preview.

```
<div class="android-updates-box">
<p><b>2.1.3 (August 2016)</b>
</p>
<p>
  This update adds compatibility with Gradle 2.14.1, which includes performance
  improvements, new features, and an important <a href=
  "https://docs.gradle.org/2.14/release-notes#local-privilege-escalation-when-using-the-daemon"
  class="external-link">security fix</a>. For more details, see the <a href=
  "https://docs.gradle.org/2.14.1/release-notes" class="external-link">Gradle
  release notes</a>.
</p>
<p>
  By default, new projects in Android Studio 2.1.3 use Gradle 2.14.1. For
  existing projects, the IDE prompts you to upgrade to Gradle 2.14.1 and
  <a href="/studio/releases/gradle-plugin.html#revisions">Android plugin
  for Gradle 2.1.3</a>, which is required when using Gradle 2.14.1 and
  higher.
</p>
```

**2.1.2 (June 2016)**

This update includes a number of small changes and bug fixes:

* [Instant Run](/studio/run#instant-run) updates and bug fixes.
* Improvements to LLDB performance and crash notifications.
* Fixed a regression in the Android Studio 2.1.1 security update that
  caused `git rebase` to fail.

**2.1.1 (May 2016)**

Security release update.

The Android N platform adds support for [Java 8 language features](/studio/write/java8-support), which
require a new experimental compiler called Jack. The latest version of Jack is
currently supported only in Android Studio 2.1. So if you want to use Java 8
language features, you need to use Android Studio 2.1 to build your app.

**Note:** [Instant Run](/tools/building/building-studio#instant-run)
is disabled when you enable the Jack compiler because they currently are not
compatible.

Although Android Studio 2.1 is now stable, the Jack compiler is still
experimental and you must enable it with the `jackOptions`
property in your `build.gradle` file.

Other than the changes to support the N Preview, Android Studio 2.1
includes minor bug fixes and the following enhancements:

* The Java-aware C++ debugger is now enabled by default when you're
  using an N device or emulator and select **Native** debugger mode
  (in the **Debugger** tab for your run/debug configuration).

For other build enhancements, including incremental Java compilation
and dexing-in-process,update your [Android plugin for
Gradle](/tools/revisions/gradle-plugin) to version 2.1.0.