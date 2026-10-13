---
title: https://developer.android.com/build/releases/agp-9-5-0-release-notes
url: https://developer.android.com/build/releases/agp-9-5-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.5 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.5 supports is API level 37.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.6.0 | 9.6.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Automated backup and restore testing

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.testSuiteSupport=true` and `android.experimental.enableBackupTest=true` in your `gradle.properties` file.

AGP 9.5.0-alpha09 adds automated backup and restore tests to help you catch
missing or unusable restored data before you release. Declare a test suite in
the `testOptions.backupTests` block. AGP then builds and runs JUnit 5 tests that
add test data to your app on connected devices, back up and restore the app, and
check that the data is intact. You can test local, cloud, and device-to-device
transfers, and the results appear in an HTML test report. For more information,
see [Automated backup and restore testing](https://developer.android.com/studio/preview/backup-restore-testing) and the
[backup and restore testing release
notes](https://developer.android.com/studio/preview/backup-restore-testing-release-notes).

## Fixed issues


### Android Gradle plugin 9.5.0-alpha09

Fixed Issues **Android Gradle Plugin** [Issue #565740572](https://issuetracker.google.com/issues/565740572) Gradle 9.8.0 reports Configuration.setVisible() deprecations with AGP 9.4.1

### Android Gradle plugin 9.5.0-alpha08

Fixed Issues **Android Gradle Plugin** [Issue #553121473](https://issuetracker.google.com/issues/553121473) Warning in generateReleaseRFile task when using JDK 25 [Issue #555796808](https://issuetracker.google.com/issues/555796808) AGP 8.11+ / 9.0 blocks build due to ANDROID_PREFS_ROOT even after removal

### Android Gradle plugin 9.5.0-alpha07

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.5.0-alpha07 ||

### Android Gradle plugin 9.5.0-alpha06

Fixed Issues **Android Gradle Plugin** [Issue #549072996](https://issuetracker.google.com/issues/549072996) KMP AndroidX sources are not downloaded without a separate non-KMP module [Issue #560282299](https://issuetracker.google.com/issues/560282299) The Configuration.setVisible(boolean) method has been deprecated [Issue #556343682](https://issuetracker.google.com/issues/556343682) AGP 9.3.0's new optimization { enable = true } DSL does not set isMinifyEnabled in the ApplicationVariant object

### Android Gradle plugin 9.5.0-alpha05

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.5.0-alpha05 ||

### Android Gradle plugin 9.5.0-alpha04

Fixed Issues **Android Gradle Plugin** [Issue #549199023](https://issuetracker.google.com/issues/549199023) BouncyCastle dependency should use BOM

### Android Gradle plugin 9.5.0-alpha03

Fixed Issues **Android Gradle Plugin** [Issue #550220873](https://issuetracker.google.com/issues/550220873) AGP 9.2.0 regression: \`LibraryExtension.getSourceSets()\` is typed on an interface the source-set implementation no longer implements, causing ClassCastException [Issue #548314106](https://issuetracker.google.com/issues/548314106) CommonExtension.resourcePrefix has incomplete docs

### Android Gradle plugin 9.5.0-alpha02

Fixed Issues **Lint** [Issue #546124524](https://issuetracker.google.com/issues/546124524) AGP's SarifReporter generates invalid JSON when LintFix has an ending alternative that produces no edits

### Android Gradle plugin 9.5.0-alpha01

Fixed Issues **Android Gradle Plugin** [Issue #533547933](https://issuetracker.google.com/issues/533547933) Add a test that validate relocation does not affect task execution

<br />