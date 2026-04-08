---
title: https://developer.android.com/build/releases/agp-8-8-0-release-notes
url: https://developer.android.com/build/releases/agp-8-8-0-release-notes
source: md.txt
---

Android Gradle Plugin 8.8.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.8 supports is API level 35.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.10.2 | 8.10.2 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 35.0.0 | 35.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 27.0.12077973 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Fixed issues


### Android Gradle plugin 8.8.2

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #394384907](https://issuetracker.google.com/issues/394384907) Initialization script 'C:\\Users\\mypc\\AppData\\Local\\Temp\\ijresolvers2.gradle' line: 162 | |
| **Shrinker (R8)** | |---| | [Issue #394185143](https://issuetracker.google.com/issues/394185143) Gson proguard is not working properly after upgrading to AGP 8.8 | | [Issue #391417819](https://issuetracker.google.com/issues/391417819) java.lang.VerifyError: Verifier rejected class | | [Issue #395489597](https://issuetracker.google.com/issues/395489597) Leanback crashes when minified with R8 included in AGP 8.10.0-alpha04 | |

### Android Gradle plugin 8.8.1

| Fixed Issues ||
|---|---|
| **Dexer (D8)** | |---| | [Issue #383073689](https://issuetracker.google.com/issues/383073689) Add OpenJDK 23 for testing | |
| **Shrinker (R8)** | |---| | [Issue #366932318](https://issuetracker.google.com/issues/366932318) java.lang.AbstractMethodError: Receiver class \[...\]$$Lambda$\[...\] does not define or inherit an implementation of the resolved method \[...\] of interface \[...\] | | [Issue #381812767](https://issuetracker.google.com/issues/381812767) NPE in Enqueuer releated to record DexCallSite | | [Issue #387258081](https://issuetracker.google.com/issues/387258081) R8 8.7.18 causes a runtime null pointer exception when calling job?.cancel | | [Issue #353279141](https://issuetracker.google.com/issues/353279141) java.lang.NoClassDefFoundError: Failed resolution of: Lkotlin/LazyThreadSafetyMode | | [Issue #378464445](https://issuetracker.google.com/issues/378464445) Monzo appears to be using excessive amount of time in tree shaking | | [Issue #389508413](https://issuetracker.google.com/issues/389508413) AGP 8.8 fail release build : R8: java.lang.NullPointerException: Cannot read field "b" because the return value of "com.android.tools.r8.internal.BS.a(com.android.tools.r8.internal.cR)" is null\` | |

### Android Gradle plugin 8.8.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #250664038](https://issuetracker.google.com/issues/250664038) Consider annotate input type for JacocoTransform as a @Classpath | | [Issue #328495232](https://issuetracker.google.com/issues/328495232) com.android.build.api.variant.GeneratesApk should expose minSdk | | [Issue #317358817](https://issuetracker.google.com/issues/317358817) com.android.settings plugin doesn't recognize targetSdk | | [Issue #327399383](https://issuetracker.google.com/issues/327399383) SourceDirectories.addGeneratedSourceDirectory is not friendly to multiple variants | | [Issue #295373352](https://issuetracker.google.com/issues/295373352) Implement flag to disable AGP minimum version checking | | [Issue #364331837](https://issuetracker.google.com/issues/364331837) AGP has confusing interactions with configuring kotlin compiler options | | [Issue #280680434](https://issuetracker.google.com/issues/280680434) AGP should expose a BuiltArtifactLoader for target project apk in com.android.test projects | | [Issue #368816424](https://issuetracker.google.com/issues/368816424) \[AGP\] Lazy SdkComponents.ndkDirectory provider fails to produce value, but eager android.ndkDirectory API works | | [Issue #229910761](https://issuetracker.google.com/issues/229910761) Build options: Add new "Build Run configuration" option and make it the default | | [Issue #363031540](https://issuetracker.google.com/issues/363031540) BuildConfig can not be resolved in unit tests when using android.enableBuildConfigAsBytecode=true | | [Issue #373609435](https://issuetracker.google.com/issues/373609435) Apks generated from Bundles does not consider privacy sandbox support | | [Issue #317358817](https://issuetracker.google.com/issues/317358817) com.android.settings plugin doesn't recognize targetSdk | |
| **Dexer (D8)** | |---| | [Issue #362339872](https://issuetracker.google.com/issues/362339872) Desugar library 2.1.0 does not work with AGP 8.5.2 | |
| **Lint** | |---| | [Issue #360840930](https://issuetracker.google.com/issues/360840930) KtAnalysisSessionProvider incompatibility with lint checks introduced in 8.7.0-alpha04 | | [Issue #364261817](https://issuetracker.google.com/issues/364261817) "False positive" WrongConstant when using PackageManager.ResolveInfoFlags.of with Kotlin | | [Issue #365376495](https://issuetracker.google.com/issues/365376495) "At least one host must be specified" lint error when setting http or https intent-filter scheme | | [Issue #362486222](https://issuetracker.google.com/issues/362486222) Handle type-use annotations in more cases for UnknownNullness lint | | [Issue #367752734](https://issuetracker.google.com/issues/367752734) AGP 8.6.1: Regression - WrongConstant lint failure when using \[Int\].toLong() inside a @LongDef in Kotlin | | [Issue #370694831](https://issuetracker.google.com/issues/370694831) AGP 8.7.0 - Lint False Positive RestrictedApi on NavOptionsBuilder.popUpTo | | [Issue #370778975](https://issuetracker.google.com/issues/370778975) WrongConstant lint appearing twice | | [Issue #363243416](https://issuetracker.google.com/issues/363243416) "MonochromeLauncherIcon: Monochrome icon is not defined" warning is not caught by Android Studio | | [Issue #371686443](https://issuetracker.google.com/issues/371686443) AbstractAnnotationDetector checks wrong overloaded functions/constructors | | [Issue #368059214](https://issuetracker.google.com/issues/368059214) Lint ImportAliasTestMode doesn't create import aliases for top level functions | | [Issue #370778975](https://issuetracker.google.com/issues/370778975) WrongConstant lint appearing twice | | [Issue #373506498](https://issuetracker.google.com/issues/373506498) New ObsoleteSdkInt lint warnings with AGP 8.8 | | [Issue #375352607](https://issuetracker.google.com/issues/375352607) False positive lint check android.permission.SCHEDULE_EXACT_ALARM is only granted to system apps | | [Issue #360354551](https://issuetracker.google.com/issues/360354551) K2 Mode throws RestrictedApi warning when using .hasRoute(Route::class) in Android Studio | |
| **Lint Integration** | |---| | [Issue #332755363](https://issuetracker.google.com/issues/332755363) Lint variant task is not found after evaluation | | [Issue #322437895](https://issuetracker.google.com/issues/322437895) Linting fails when importing AAR file with implemenation files | |

<br />