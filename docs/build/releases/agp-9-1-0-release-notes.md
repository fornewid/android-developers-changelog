---
title: https://developer.android.com/build/releases/agp-9-1-0-release-notes
url: https://developer.android.com/build/releases/agp-9-1-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.1 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.1 supports is API level 36.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.3.1 | 9.3.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 9.1.0-alpha05

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #471410336](https://issuetracker.google.com/issues/471410336) AGP 9.0.0-rc01 doesn't resolve Kotlin libraries via kotlin() function | |

### Android Gradle plugin 9.1.0-alpha04

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #398173037](https://issuetracker.google.com/issues/398173037) \`\*.xml.flat\` files contain absolute file paths | |

### Android Gradle plugin 9.1.0-alpha03

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.1.0-alpha03 ||

### Android Gradle plugin 9.1.0-alpha02

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #458708710](https://issuetracker.google.com/issues/458708710) Add ability to turn ManifestProcessorTask warnings into errors | |

### Android Gradle plugin 9.1.0-alpha01

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #458708710](https://issuetracker.google.com/issues/458708710) Add ability to turn ManifestProcessorTask warnings into errors | | [Issue #469745905](https://issuetracker.google.com/issues/469745905) Transforming \`OBFUSCATION_MAPPING_FILE\` artifact results in outputs of R8 task missing from the output folder | |

<br />