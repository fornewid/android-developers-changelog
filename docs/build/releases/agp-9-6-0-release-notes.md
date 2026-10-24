---
title: https://developer.android.com/build/releases/agp-9-6-0-release-notes
url: https://developer.android.com/build/releases/agp-9-6-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.6 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.6 supports is API level 37.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.6.0 | 9.6.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## On-device code coverage for instrumented tests

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.androidTest.coverage.useOnDeviceAgent=true` and `android.experimental.reportAggregationSupport=true` in your `gradle.properties` file.

AGP 9.6.0-alpha01 adds on-device code coverage for instrumented tests. Instead
of instrumenting your app's classes with JaCoCo at build time, AGP adds a
coverage agent to your test APK, and the agent instruments the classes on the
test device while your tests run. This removes the JaCoCo instrumentation step
from builds that have `enableAndroidTestCoverage` enabled, and keeps
coverage-tracking code out of your app's APK. You run the same
`create{Variant}AndroidTestCoverageReport` task, and AGP generates the HTML and
XML reports in the same location. On-device code coverage requires a debuggable
app and a device that runs Android 9 (API level 28) or higher.

AGP adds the coverage agent library, `com.android.tools.test:coverage-agent`,
with the same version as AGP. For more information, see [View code coverage
reports (with on-device agent)](https://developer.android.com/studio/test/on-device-code-coverage).

## Fixed issues


### Android Gradle plugin 9.6.0-alpha01

Fixed Issues **Android Gradle Plugin** [Issue #206104792](https://issuetracker.google.com/issues/206104792) shrinkresources does not work with library apks due to recent aapt2 change **Lint** [Issue #575549246](https://issuetracker.google.com/issues/575549246) Lint ThreadConstraint partial results are not deterministic across JVMs, which breaks build cache for lintAnalyze

<br />