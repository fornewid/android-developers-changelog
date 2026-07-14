---
title: https://developer.android.com/build/releases/agp-9-3-0-release-notes
url: https://developer.android.com/build/releases/agp-9-3-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.3 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.3 supports is API level 37.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.5.0 | 9.5.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Standalone R8 Configuration Analyzer Gradle task

Android Gradle plugin 9.3 introduces a dedicated Gradle task for running the [R8
Configuration Analyzer](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer) in isolation. The R8 Configuration Analyzer helps
you optimize your app's code shrinking and obfuscation rules.

    ./gradlew :app:analyzeReleaseR8Config

The `:app:analyzeReleaseR8Config` task generates the report without completing
the APK or Bundle compilation pipeline. This provides a shorter feedback loop,
which speeds up developer iteration when refining keep rules. Alternatively,
you can generate the report automatically by running an R8 release build (such
as `assembleRelease` or `bundleRelease`).

For more information, see [Run the standalone Gradle task for generating
report](https://developer.android.com/topic/performance/app-optimization/r8-configuration-analyzer#run-standalone-task).

## Fixed issues


### Android Gradle plugin 9.3.0-rc02

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-rc02 ||

### Android Gradle plugin 9.3.0-rc01

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-rc01 ||

### Android Gradle plugin 9.3.0-alpha12

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #483853092](https://issuetracker.google.com/issues/483853092) Build Failure: File handle leak on classes.jar in compile_library_classes_jar prevents rebuilds on Windows until IDE restart | |
| **Lint** | |---| | [Issue #404190661](https://issuetracker.google.com/issues/404190661) Lint treats imported Java library as Android project, ignoring compile SDK version | |

### Android Gradle plugin 9.3.0-alpha11

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-alpha11 ||

### Android Gradle plugin 9.3.0-alpha10

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-alpha10 ||

### Android Gradle plugin 9.3.0-alpha09

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-alpha09 ||

### Android Gradle plugin 9.3.0-alpha08

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-alpha08 ||

### Android Gradle plugin 9.3.0-alpha07

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0-alpha07 ||

### Android Gradle plugin 9.3.0-alpha06

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #211725171](https://issuetracker.google.com/issues/211725171) JavaDocGenerationTask should use workers | |

### Android Gradle plugin 9.3.0-alpha05

| Fixed Issues ||
|---|---|
| **Shrinker (R8)** | |---| | [Issue #146403477](https://issuetracker.google.com/issues/146403477) L8 obfucation mapping not included in app mapping.txt | |

### Android Gradle plugin 9.3.0-alpha04

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #498736839](https://issuetracker.google.com/issues/498736839) KMP keepRules source set ignored without it.consumerKeepRules.publish = true | |

### Android Gradle plugin 9.3.0-alpha03

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #504996348](https://issuetracker.google.com/issues/504996348) java.lang.ClassNotFoundException: Didn't find class "com.android.tools.r8.RecordTag" after upgrading gradle to 9.2.0 | |
| **Lint** | |---| | [Issue #492589793](https://issuetracker.google.com/issues/492589793) Lint error when resource shrinking is disabled | |

### Android Gradle plugin 9.3.0-alpha02

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #445195675](https://issuetracker.google.com/issues/445195675) Feature request: Add native_libs_merge_blame_file support to Android Gradle Plugin | |
| **Lint** | |---| | [Issue #504284788](https://issuetracker.google.com/issues/504284788) Missing backtick in AnnotationDetector issue message | | [Issue #492589793](https://issuetracker.google.com/issues/492589793) Lint error when resource shrinking is disabled | |

### Android Gradle plugin 9.3.0-alpha01

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #497456771](https://issuetracker.google.com/issues/497456771) Isuue with auto generated version codes | | [Issue #495889752](https://issuetracker.google.com/issues/495889752) AGP: Migrate away from Project as dependency notation | |
| **Lint** | |---| | [Issue #492246721](https://issuetracker.google.com/issues/492246721) Lint false positive with UseKtx | |

### Android Gradle plugin 9.3.0

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.3.0 ||

<br />