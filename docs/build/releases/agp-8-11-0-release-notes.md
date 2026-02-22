---
title: https://developer.android.com/build/releases/agp-8-11-0-release-notes
url: https://developer.android.com/build/releases/agp-8-11-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.11.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle Plugin 8.11 supports is API level 36.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.13 | 8.13 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.11.1

| Fixed Issues ||
|---|---|
| No public issues were marked as fixed in AGP 8.11.1 ||

### Android Gradle plugin 8.11.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #400492927](https://issuetracker.google.com/issues/400492927) Isolated project: DeclarativeSchemaModel serialization error | | [Issue #327770434](https://issuetracker.google.com/issues/327770434) Request: for the deprecation of zipAlignEnabled, tell why it's deprecated and what to use instead | | [Issue #406464766](https://issuetracker.google.com/issues/406464766) \[AGP 8.9.0+\] BuiltinKotlinCompilation exposed to all Kotlin Compiler Plugins | | [Issue #405419218](https://issuetracker.google.com/issues/405419218) Update Kotlin dependencies to version 2.1.20 when building AGP 8.11 | | [Issue #372269616](https://issuetracker.google.com/issues/372269616) Don't enforce com.android.internal.version-check when updating Gradle distribution | | [Issue #294183018](https://issuetracker.google.com/issues/294183018) Fail build when proguard file does not exist | |
| **Dexer (D8)** | |---| | [Issue #418143856](https://issuetracker.google.com/issues/418143856) AutoClosable desugaring breaks AGP builds from within Android Studio | |
| **Lint** | |---| | [Issue #343347272](https://issuetracker.google.com/issues/343347272) Lint rule BuildListAdds does not detect usage of operator fun plusAssign (+=) in buildList | | [Issue #399428893](https://issuetracker.google.com/issues/399428893) UseSdkSuppress false positives on test helper code | | [Issue #398924424](https://issuetracker.google.com/issues/398924424) Warn potential conflict of member and extension | | [Issue #406935594](https://issuetracker.google.com/issues/406935594) False positive for lint issue \`MemberExtensionConflict\` if extension function receiver is nullable | | [Issue #405442664](https://issuetracker.google.com/issues/405442664) \`WrongGradleMedthod\` inspection false positive | | [Issue #405654866](https://issuetracker.google.com/issues/405654866) SyntheticAccessor false positive for data class's synthetic member call | | [Issue #406739378](https://issuetracker.google.com/issues/406739378) TestMode.SUPPRESSIBLE error for issue reported on label-able expression | | [Issue #406991279](https://issuetracker.google.com/issues/406991279) New MemberExtensionConflict lint issues starting in AGP 8.11.0-alpha03 - how to solve? | | [Issue #409716542](https://issuetracker.google.com/issues/409716542) Lint inspection in 'libs.versions.toml' file suggests upgrade to non-supported AGP version. | |
| **Shrinker (R8)** | |---| | [Issue #402800800](https://issuetracker.google.com/issues/402800800) Unable to Generate Signed AAB after updating to AGP 8.9.0 | | [Issue #418568424](https://issuetracker.google.com/issues/418568424) R8 Crashes with min-api 24 When Processing JavaFuzzer Code | |

<br />