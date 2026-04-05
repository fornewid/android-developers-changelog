---
title: https://developer.android.com/build/releases/agp-8-7-0-release-notes
url: https://developer.android.com/build/releases/agp-8-7-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.7.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.7 supports is API level 35.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| "Gradle" | 8.9 | 8.9 | "To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle)." |
| SDK Build Tools | 34.0.0 | 34.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | "[Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK." |
| JDK | 17 | 17 | "To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk)." |

<br />

## Lint behavior change

Starting with Android Gradle Plugin 8.7.0-alpha08, if there is a `LintError`
when running lint using Gradle, the lint analysis task throws an exception.
This change prevents rare errors from being cached in the build cache.

Unfortunately, this change breaks builds for projects with genuine `LintError`
instances in their lint baseline files. The error message contains information
about which lint checks are causing the problem. In some cases, updating the
corresponding library dependency might resolve the problem. If not, you can
disable the problematic lint check until the library author fixes it.

## Fixed issues


### Android Gradle plugin 8.7.3

| Fixed Issues ||
|---|---|
| **Lint** | |---| | [Issue #374488858](https://issuetracker.google.com/issues/374488858) Many missing analysis API method warnings when running lint | | [Issue #375352607](https://issuetracker.google.com/issues/375352607) False positive lint check android.permission.SCHEDULE_EXACT_ALARM is only granted to system apps | |

### Android Gradle plugin 8.7.2

| Fixed Issues ||
|---|---|
| **Lint** | |---| | [Issue #370694831](https://issuetracker.google.com/issues/370694831) AGP 8.7.0 - Lint False Positive RestrictedApi on NavOptionsBuilder.popUpTo | |
| **Shrinker (R8)** | |---| | [Issue #363492038](https://issuetracker.google.com/issues/363492038) \[R8 8.6.27\] Method implementation replaced with \`throw null\` | | [Issue #372749733](https://issuetracker.google.com/issues/372749733) Default android proguard files throw a warning when used with current Version of R8 | | [Issue #370937458](https://issuetracker.google.com/issues/370937458) MissingStartupProfileItemsDiagnostic crashes the Gradle client with an out-of-memory error if the message is too large | |

### Android Gradle plugin 8.7.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #364967835](https://issuetracker.google.com/issues/364967835) agp docs have a lot of TBD | |
| **Lint** | |---| | [Issue #367752734](https://issuetracker.google.com/issues/367752734) AGP 8.6.1: Regression - WrongConstant lint failure when using \[Int\].toLong() inside a @LongDef in Kotlin | | [Issue #365376495](https://issuetracker.google.com/issues/365376495) "At least one host must be specified" lint error when setting http or https intent-filter scheme | |

### Android Gradle plugin 8.7.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #344016691](https://issuetracker.google.com/issues/344016691) AGP should claim that it supports API 35 that is about to ship | | [Issue #355397971](https://issuetracker.google.com/issues/355397971) AGP 8.5: Many more "mergeDebugResources" tasks are run, slowing down builds | | [Issue #353579998](https://issuetracker.google.com/issues/353579998) Make ndk 27 the default NDK in AGP. | | [Issue #344016691](https://issuetracker.google.com/issues/344016691) AGP should claim that it supports API 35 that is about to ship | | [Issue #344016691](https://issuetracker.google.com/issues/344016691) AGP should claim that it supports API 35 that is about to ship | | [Issue #230685896](https://issuetracker.google.com/issues/230685896) Running Android lint failed with NoSuchFileException | | [Issue #307784512](https://issuetracker.google.com/issues/307784512) BuildType#initWith copies postprocessing block but proguard configuration is not applied | | [Issue #359245746](https://issuetracker.google.com/issues/359245746) Cannot merge for foregroundServiceType tags | | [Issue #230685896](https://issuetracker.google.com/issues/230685896) Running Android lint failed with NoSuchFileException | |
| **Lint** | |---| | [Issue #36981231](https://issuetracker.google.com/issues/36981231) Lint should check for invalid objects used as ViewGroups | | [Issue #62810553](https://issuetracker.google.com/issues/62810553) "android:host is missing" for uris with null host | | [Issue #360840930](https://issuetracker.google.com/issues/360840930) KtAnalysisSessionProvider incompatibility with lint checks introduced in 8.7.0-alpha04 | | [Issue #364261817](https://issuetracker.google.com/issues/364261817) "False positive" WrongConstant when using PackageManager.ResolveInfoFlags.of with Kotlin | |

<br />