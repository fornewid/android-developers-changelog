---
title: https://developer.android.com/build/releases/agp-9-4-0-release-notes
url: https://developer.android.com/build/releases/agp-9-4-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.4 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.4 supports is API level 37.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.6.0 | 9.6.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Variant API module opt-out

Starting with AGP 10, the new Variant API is mandatory for all projects. To
support a gradual migration, you can temporarily opt specific modules out of
this requirement before AGP 10 by applying the following to your
`gradle.properties` file.

    android.newDsl.optOut=:example-lib1

## Fixed issues


### Android Gradle plugin 9.4.0-alpha04

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.4.0-alpha04 ||

### Android Gradle plugin 9.4.0-alpha03

| Fixed Issues ||
|---|---|
| **Shrinker (R8)** | |---| | [Issue #146403477](https://issuetracker.google.com/issues/146403477) L8 obfucation mapping not included in app mapping.txt | |

### Android Gradle plugin 9.4.0-alpha02

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #499166350](https://issuetracker.google.com/issues/499166350) AGP SigningConfig is too eager | | [Issue #257765153](https://issuetracker.google.com/issues/257765153) "Unable to get provider" (ClassNotFoundException) when running \`./gradlew :app:connectedDebugAndroidTest\` with a provider defined in a dynamic feature module | |

### Android Gradle plugin 9.4.0-alpha01

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #499166350](https://issuetracker.google.com/issues/499166350) AGP SigningConfig is too eager | |

<br />