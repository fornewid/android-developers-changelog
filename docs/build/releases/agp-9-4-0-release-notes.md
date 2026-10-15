---
title: Android Gradle plugin 9.4.0 (September 2026)  |  Android Studio  |  Android Developers
url: https://developer.android.com/build/releases/agp-9-4-0-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/gradle-build-overview)

# Android Gradle plugin 9.4.0 (September 2026) Stay organized with collections Save and categorize content based on your preferences.





Android Gradle plugin 9.4 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.4 supports is API level 37.
Here is other compatibility info:

|  | Minimum version | Default version | Notes |
| --- | --- | --- | --- |
| Gradle | 9.6.0 | 9.6.0 | To learn more, see [updating Gradle](/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](/studio/intro/update#sdk-manager) or [configure](/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](/studio/projects/install-ndk#specific-version) or [configure](/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](/studio/intro/studio-config#jdk). |

## Variant API module opt-out

Starting with AGP 10, the new Variant API is mandatory for all projects. To
support a gradual migration, you can temporarily opt specific modules out of
this requirement before AGP 10 by applying the following to your
`gradle.properties` file.

```
android.newDsl.optOut=:example-lib1
```

## Strict 1:1 variant parity between dynamic feature and android apps

Starting in AGP 9.4, the build system checks for strict 1:1 flavor dimension
parity between Android app modules and dynamic feature modules,
reporting any missing, extra, or mismatched dimensions as build warnings.
To help you prepare for stricter validation without breaking existing
build pipelines, this check operates in warning mode by default, but can be
promoted to an execution error by enabling the
`android.enforceDynamicFeatureVariantMatching=true` Gradle option.
From AGP 10.0 onwards, strict 1:1 variant parity will become enforced by
default, turning all dimension mismatches between base apps and their
dynamic feature modules into fatal build failures.

## Fixed issues

### Android Gradle plugin 9.4.0-alpha04

| Fixed Issues | |
| --- | --- |
| No public issues were marked as fixed in AGP 9.4.0-alpha04 | |

### Android Gradle plugin 9.4.0-alpha03

| Fixed Issues | |
| --- | --- |
| **Shrinker (R8)** | |  | | --- | | [Issue #146403477](https://issuetracker.google.com/issues/146403477)  L8 obfucation mapping not included in app mapping.txt | |

### Android Gradle plugin 9.4.0-alpha02

| Fixed Issues | |
| --- | --- |
| **Android Gradle Plugin** | |  | | --- | | [Issue #499166350](https://issuetracker.google.com/issues/499166350)  AGP SigningConfig is too eager | | [Issue #257765153](https://issuetracker.google.com/issues/257765153)  "Unable to get provider" (ClassNotFoundException) when running `./gradlew :app:connectedDebugAndroidTest` with a provider defined in a dynamic feature module | |

### Android Gradle plugin 9.4.0-alpha01

| Fixed Issues | |
| --- | --- |
| **Android Gradle Plugin** | |  | | --- | | [Issue #499166350](https://issuetracker.google.com/issues/499166350)  AGP SigningConfig is too eager | |