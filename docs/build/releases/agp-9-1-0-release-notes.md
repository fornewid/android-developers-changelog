---
title: https://developer.android.com/build/releases/agp-9-1-0-release-notes
url: https://developer.android.com/build/releases/agp-9-1-0-release-notes
source: md.txt
---

<br />

Android Gradle plugin 9.1 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.1 supports is API level 36.1.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.3.1 | 9.3.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## R8 changes

The following R8 changes are included in AGP 9.1.0.

### Enable repackaging to unnamed (default) package when compiling to DEX

R8 now repackages classes into the unnamed (default) package when compiling
to DEX by default. This effectively adds the rule `-repackageclasses` to
builds that use neither `-flattenpackagehierarchy` or
`-repackageclasses` explicitly.

Repackaging by default ensures consistency with obfuscation, optimization and
shrinking, which are all opt-out rather than opt-in, and thereby
mitigates suboptimal configurations that are not explicitly opting in to
repackaging.

In order to opt out of this behavior, use the new `-dontrepackage` rule.

### Support named levels for -maximumremovedandroidloglevel

When using `-maximumremovedandroidloglevel`, you can now specify the log
level names instead of the numbers. The following table shows the names
and the corresponding numeric log level.

| Name | Level |
|---|---|
| `ASSERT` | 7 |
| `ERROR` | 6 |
| `WARN` | 5 |
| `INFO` | 4 |
| `DEBUG` | 3 |
| `VERBOSE` | 2 |
| `NONE` | 1 |

You must specify the log level names in all caps.

## Fixed issues


### Android Gradle plugin 9.1.0-rc01

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.1.0-rc01 ||

### Android Gradle plugin 9.1.0-alpha09

| Fixed Issues ||
|---|---|
| **Lint** | |---| | [Issue #454429194](https://issuetracker.google.com/issues/454429194) Lint in Otter.2 does not recognize the new compileSdk and targetSdk DSL from AGP 9.0 | |

### Android Gradle plugin 9.1.0-alpha08

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #473854532](https://issuetracker.google.com/issues/473854532) Clean Project menu runs a sub-project target instead of just "clean" | | [Issue #460470375](https://issuetracker.google.com/issues/460470375) Incremental dex desugaring bug in AGP | | [Issue #272344409](https://issuetracker.google.com/issues/272344409) Config cache: avoid accessing task extensions and conventions at execution time | | [Issue #448452488](https://issuetracker.google.com/issues/448452488) AGP does not know about canary platforms and complains | |
| **Lint Integration** | |---| | [Issue #478976180](https://issuetracker.google.com/issues/478976180) Android Lint using K1 when applied to a java-library project | | [Issue #197146610](https://issuetracker.google.com/issues/197146610) "Lint check for lint checks" not running | |

### Android Gradle plugin 9.1.0-alpha07

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #474099556](https://issuetracker.google.com/issues/474099556) beforeVariants for KMP needs to be implemented. | |

### Android Gradle plugin 9.1.0-alpha06

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.1.0-alpha06 ||

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

### Android Gradle plugin 9.1.0

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 9.1.0 ||

<br />