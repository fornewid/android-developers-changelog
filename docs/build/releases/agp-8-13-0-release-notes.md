---
title: https://developer.android.com/build/releases/agp-8-13-0-release-notes
url: https://developer.android.com/build/releases/agp-8-13-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.13.0 is a major release that includes a variety of new
features and improvements.

## Android Gradle plugin 8.13.2

**Kotlin 2.3 support** : Android Gradle plugin 8.13.2 uses R8 8.13.19 which
[supports Kotlin 2.3](https://developer.android.com/build/kotlin-support).

## Compatibility

The maximum API level that Android Gradle Plugin 8.13 supports is API level 36.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.13 | 8.13 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.13.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #231712094](https://issuetracker.google.com/issues/231712094) Run CheckAarMetadataTask in library projects when building an AAR | | [Issue #426351548](https://issuetracker.google.com/issues/426351548) Fused Library Plugin cannot process resource references from external library | | [Issue #426351547](https://issuetracker.google.com/issues/426351547) Fused Library plugin should allow to use overrideLibrary | | [Issue #280674230](https://issuetracker.google.com/issues/280674230) Change the app's targetSdk default value to be based on compileSdk instead of minSdk | | [Issue #436887358](https://issuetracker.google.com/issues/436887358) \`com.android.kotlin.multiplatform.library\` crashes with Gradle Managed Devices | |
| **Shrinker (R8)** | |---| | [Issue #435466316](https://issuetracker.google.com/issues/435466316) ClassCastException from impossible class with R8 | | [Issue #437005995](https://issuetracker.google.com/issues/437005995) ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0 since 8.10.0 | | [Issue #436817591](https://issuetracker.google.com/issues/436817591) Parsing of patterns in enableExperimentalPartialShrinking API is very strict | |

<br />