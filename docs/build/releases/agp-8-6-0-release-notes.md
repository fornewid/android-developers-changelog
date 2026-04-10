---
title: https://developer.android.com/build/releases/agp-8-6-0-release-notes
url: https://developer.android.com/build/releases/agp-8-6-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.6.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.6 supports is API level 35.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.7 | 8.7 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 34.0.0 | 34.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 26.1.10909125 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.6.1

| Fixed Issues ||
|---|---|
| **Dexer (D8)** | |---| | [Issue #359616078](https://issuetracker.google.com/issues/359616078) Dexing task/transform generates non-deterministic classes.dex contents | |
| **Shrinker (R8)** | |---| | [Issue #355238622](https://issuetracker.google.com/issues/355238622) R8 8.5.x StackOverflowError in SimpleInliningConstraintAnalysis | | [Issue #359385828](https://issuetracker.google.com/issues/359385828) Task :xxxx:minifyXXXReleaseWithR8 ERROR: R8: java.util.ConcurrentModificationException | | [Issue #358913905](https://issuetracker.google.com/issues/358913905) java.lang.NullPointerException: Cannot invoke "com.android.tools.r8.ir.analysis.type.TypeElement.asClassType()" | |

### Android Gradle plugin 8.6.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #183423660](https://issuetracker.google.com/issues/183423660) AGP 7.0.0-alpha10 regression: Failed to apply plugin 'com.android.internal.library' when databinding is enabled | | [Issue #337848180](https://issuetracker.google.com/issues/337848180) Errors when running lint with and without K2 UAST | | [Issue #341124476](https://issuetracker.google.com/issues/341124476) Manifest not generated for Variant's androidTest configuration | | [Issue #339313346](https://issuetracker.google.com/issues/339313346) AGP 8.4 tries to set up Startup Profiles on debug builds | | [Issue #341266993](https://issuetracker.google.com/issues/341266993) \[Koala 2024.1.2 Canary 2\] Error running a baseline profile module on a split APK | | [Issue #202449978](https://issuetracker.google.com/issues/202449978) Clean up / remove ProjectInfo | | [Issue #322519675](https://issuetracker.google.com/issues/322519675) Update outdated kdoc for \`isIncludeAndroidResources\` in AGP DSL | | [Issue #337776938](https://issuetracker.google.com/issues/337776938) Lint uses res directory without adding task dependency | | [Issue #355397971](https://issuetracker.google.com/issues/355397971) AGP 8.5: Many more "mergeDebugResources" tasks are run, slowing down builds | | [Issue #352352252](https://issuetracker.google.com/issues/352352252) Adding srcs dir via Variant API not working as expected | |
| **Dexer (D8)** | |---| | [Issue #343127842](https://issuetracker.google.com/issues/343127842) Update API database to Android 15 (API level 35) | | [Issue #343136777](https://issuetracker.google.com/issues/343136777) java.lang.VerifyError: Verifier rejected class com.pax.log.LogUtils: java.lang.StackTraceElement com.pax.log.LogUtils.getCaller(com.pax.log.b, java.lang.StackTraceElement\[\], int) failed to verify | |
| **Lint** | |---| | [Issue #313699428](https://issuetracker.google.com/issues/313699428) Lint does not call visitAnnotationUsage for usages of annotated annotations | | [Issue #345452195](https://issuetracker.google.com/issues/345452195) UnknownNullness lint error when using type-use annotations | | [Issue #327670482](https://issuetracker.google.com/issues/327670482) \[library desugar\] lint shows false positive warning NewApi warnings with desugaring enabled | | [Issue #339363983](https://issuetracker.google.com/issues/339363983) Credential Manager Lint warning incorrect on Wear | | [Issue #347356457](https://issuetracker.google.com/issues/347356457) Lint: SetTextI18n complains about assigning an empty string. | |
| **Lint Integration** | |---| | [Issue #327670497](https://issuetracker.google.com/issues/327670497) Lint tasks fails with included build | |
| **Shrinker (R8)** | |---| | [Issue #348785664](https://issuetracker.google.com/issues/348785664) \[r8 8.5\]r8 horizontal class merge causes verify error on Android5 when disable api modeling | | [Issue #347676160](https://issuetracker.google.com/issues/347676160) A Wear OS release built with Gradle Plugin 8.4.0/8.5.0 may cause java.lang.IllegalAccessError | | [Issue #323136645](https://issuetracker.google.com/issues/323136645) R8 implicitly replaces an empty member clause with a match of () | | [Issue #348202700](https://issuetracker.google.com/issues/348202700) \[r8 8.5\] vertical class merger causing runtime NPE | | [Issue #348499741](https://issuetracker.google.com/issues/348499741) R8 Processing Error Possibly Due to Right Shift Operator | | [Issue #354878031](https://issuetracker.google.com/issues/354878031) R8 (AGP 8.5.0+) fails with error "Unexpected rewriting of item: ... to two distinct items:..." | | [Issue #354625681](https://issuetracker.google.com/issues/354625681) The dex file generated by R8 shows "Unable to find static main(String\[\]) in 'Test'" when executed | | [Issue #354625682](https://issuetracker.google.com/issues/354625682) Different Behavior Between Programs packed by R8 and D8 | | [Issue #353475583](https://issuetracker.google.com/issues/353475583) R8 NullPointer after updating to Kotlin 2.0 | |

<br />