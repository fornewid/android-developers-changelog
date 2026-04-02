---
title: https://developer.android.com/build/releases/agp-8-12-0-release-notes
url: https://developer.android.com/build/releases/agp-8-12-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.12.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle Plugin 8.12 supports is API level 36.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.13 | 8.13 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.12.2

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 8.12.2 ||

### Android Gradle plugin 8.12.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #436887358](https://issuetracker.google.com/issues/436887358) \`com.android.kotlin.multiplatform.library\` crashes with Gradle Managed Devices | |

### Android Gradle plugin 8.12.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #414988521](https://issuetracker.google.com/issues/414988521) How to specify a boolean value for experimentalProperties | | [Issue #390602110](https://issuetracker.google.com/issues/390602110) Explicitly enabling device tests in a non-default build type using AGP does not work | | [Issue #416349489](https://issuetracker.google.com/issues/416349489) Move AGP to configurations.register to avoid eager realization of configurations | | [Issue #379732901](https://issuetracker.google.com/issues/379732901) Include nested MANIFEST.MF files in defaultExcludes | | [Issue #127986458](https://issuetracker.google.com/issues/127986458) Gradle plugin should merge test manifest when includeAndroidResources == true | | [Issue #423864097](https://issuetracker.google.com/issues/423864097) Source files from src/extraMain/java aren't added to the compiler using "built-in-kotlin" | | [Issue #327399383](https://issuetracker.google.com/issues/327399383) SourceDirectories.addGeneratedSourceDirectory is not friendly to multiple variants | | [Issue #380291901](https://issuetracker.google.com/issues/380291901) AGP 8.8.0-alpha09 causes some JaCoCo reporting issues | | [Issue #424419916](https://issuetracker.google.com/issues/424419916) \[fused lib - public\] adding kmp lib like coil does not work | | [Issue #425390382](https://issuetracker.google.com/issues/425390382) Cannot build tests with AGP 8.12.0-alpha05 due to package declaration in merged manifest | | [Issue #428189815](https://issuetracker.google.com/issues/428189815) AGP 8.12.0-alpha07 fails release builds with the Firebase Performance gradle plugin applied | | [Issue #427932312](https://issuetracker.google.com/issues/427932312) Add ExtractAnnotations to AGP KMP | | [Issue #429161295](https://issuetracker.google.com/issues/429161295) BuiltInKotlinJvmAndroidCompilation doesn't work with Kotlin compiler plugins such as Anvil and KSP | | [Issue #426156521](https://issuetracker.google.com/issues/426156521) Fused library plugin fails during \`:mergingArtifactAAR_METADATA\` task | |
| **Lint** | |---| | [Issue #371686443](https://issuetracker.google.com/issues/371686443) AbstractAnnotationDetector checks wrong overloaded functions/constructors | | [Issue #426553902](https://issuetracker.google.com/issues/426553902) Lint gives warning when using Config.OLDEST_SDK in test | | [Issue #426554247](https://issuetracker.google.com/issues/426554247) TypoDetector regularly crashes with IllegalArgumentException during quickfix | | [Issue #425974265](https://issuetracker.google.com/issues/425974265) Bug: Possible false positive of Android Studio about "die die" in German | | [Issue #426156517](https://issuetracker.google.com/issues/426156517) SupportAnnotationUsage rule should support KT-73255 | | [Issue #427761232](https://issuetracker.google.com/issues/427761232) \[Lint\] Excessive false positives of \`MemberExtensionConflict\` - issue description is incorrect | | [Issue #429730003](https://issuetracker.google.com/issues/429730003) \[lint\] MemberExtensionConflict false positive on parameter name conflict | | [Issue #429703136](https://issuetracker.google.com/issues/429703136) \[lint\] PropertyEscape false positive on valid properties file | |

<br />