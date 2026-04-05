---
title: https://developer.android.com/build/releases/agp-8-2-0-release-notes
url: https://developer.android.com/build/releases/agp-8-2-0-release-notes
source: md.txt
---

Android Gradle plugin 8.2.0 is a major release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 8.2 supports is API level 34.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.2 | 8.2 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 34.0.0 | 34.0.0 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 25.1.8937393 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## New macro to specify JDK path

`#GRADLE_LOCAL_JAVA_HOME` is a new macro that you can use to specify the JDK
path. This makes it safer and easier to specify the Java home path used for the
Gradle daemon (background process) execution for your project. The path
selection is stored in the `java.home` field in the `.gradle/config.properties`
file. Set this field through Gradle JDK settings in Android Studio: **File** (or
**Android Studio** on macOS) **\> Settings \> Build, Execution, Deployment \> Build
Tools \> Gradle**.

New projects will use `#GRADLE_LOCAL_JAVA_HOME` by default. Existing projects
will automatically be migrated to the new macro after a successful sync unless
you're already using a macro like `#JAVA_HOME`.

The main benefits of the new macro are as follows:

- You can manually modify the JDK path to trigger sync without opening your project first.
- Fewer errors related to incompatible Gradle and project JDK versions since there is a single source of truth for your Gradle JDK selection.

## Fixed issues

### Android Gradle plugin 8.2.2

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #298703884](https://issuetracker.google.com/issues/298703884) Unable to set JaCoCo version in AGP 8.2.0 | |
| **Dexer (D8)** | |---| | [Issue #319604744](https://issuetracker.google.com/issues/319604744) \[desugared library\] Desugared library version 2.1 is not compatible with previous versions of R8 | | [Issue #316744331](https://issuetracker.google.com/issues/316744331) Optimizations running even just with D8? | |
| **Shrinker (R8)** | |---| | [Issue #316100042](https://issuetracker.google.com/issues/316100042) \[R8 8.3.21\] R8 8.3.21 is 1.57MB larger than R8 8.1.56 | | [Issue #318787479](https://issuetracker.google.com/issues/318787479) class.getInterfaces() return empty | |

### Android Gradle plugin 8.2.1

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #310252873](https://issuetracker.google.com/issues/310252873) Do not run dexing task on subprojects' classes when they are already dex'd through artifact transforms | | [Issue #294137077](https://issuetracker.google.com/issues/294137077) Android Gradle Plugin failed with JavaVersion.VERSION_11 and OpenJDK 21 ea | |
| **Dexer (D8)** | |---| | [Issue #312443509](https://issuetracker.google.com/issues/312443509) Desugar records for Android U | |
| **Shrinker (R8)** | |---| | [Issue #307987907](https://issuetracker.google.com/issues/307987907) R8 generates broken dex resulting in class cast exception at runtime | | [Issue #309727365](https://issuetracker.google.com/issues/309727365) R8 causing interface change to inaccessible interface | | [Issue #315877832](https://issuetracker.google.com/issues/315877832) R8 Flurry SDK crash with AGP 8.2.0 | | [Issue #314984596](https://issuetracker.google.com/issues/314984596) Android - R8 causes subclass of LinearLayoutManager to crash | | [Issue #310939676](https://issuetracker.google.com/issues/310939676) ClassCastException in R8 when repackaging is on and shrinking, obfuscation and optimization is turned off | | [Issue #307761442](https://issuetracker.google.com/issues/307761442) R8 stuck in BridgeAnalyzer.analyzeMethod | | [Issue #315186101](https://issuetracker.google.com/issues/315186101) R8 v8.2.33, "java.lang.VerifyError: Bad type on operand stack" runtime crash after upgrade | |

### Android Gradle plugin 8.2.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #268192807](https://issuetracker.google.com/issues/268192807) Custom source types should create multi-flavor sourcesets | | [Issue #276807774](https://issuetracker.google.com/issues/276807774) SDK version check does not handle users of SDK extensions | | [Issue #274913388](https://issuetracker.google.com/issues/274913388) DependenciesInfoBuilder needs API update + doc | | [Issue #266599585](https://issuetracker.google.com/issues/266599585) DexingNoClasspathTransform (minSdk \>= 24) with Java 11 target fails due to missing nest members | | [Issue #260100335](https://issuetracker.google.com/issues/260100335) DslExtension.Builder.extendProjectWith() not working as described in Groovy | | [Issue #265336046](https://issuetracker.google.com/issues/265336046) Add VariantSelector.withFlavor API that doesn't use kotlin.Pair | | [Issue #266403349](https://issuetracker.google.com/issues/266403349) AndroidLintAnalysisTask (:lintAnalyzeExternalRelease) has a cache miss because \`proguard.txt\` has changed | | [Issue #272553504](https://issuetracker.google.com/issues/272553504) App merged manifest contains extractNativeLibs and useEmbeddedDex attributes from dependencies | | [Issue #236167971](https://issuetracker.google.com/issues/236167971) AIDL fails with build-tools 33.0.0 | | [Issue #268237729](https://issuetracker.google.com/issues/268237729) AGP: Expose path to AIDL tool and framework AIDL file as public API | | [Issue #274016286](https://issuetracker.google.com/issues/274016286) Request: let the IDE offer a fix for "PermittedSubclasses requires ASM9" | | [Issue #274742629](https://issuetracker.google.com/issues/274742629) Target bytecode 17 when compiling AGP | | [Issue #277118749](https://issuetracker.google.com/issues/277118749) Remove VariantManager.getModifiedName | | [Issue #228846664](https://issuetracker.google.com/issues/228846664) AndroidTest.packaging.jniLibs.keepDebugSymbols doesn't affect androidTest packaging | | [Issue #265998900](https://issuetracker.google.com/issues/265998900) GMD instrumentation test tasks hang and upon retrying start failing | | [Issue #281825213](https://issuetracker.google.com/issues/281825213) generateLocaleConfig in agp 8.1.0 uses non-deterministic ordering, breaking reproducible builds | | [Issue #281425351](https://issuetracker.google.com/issues/281425351) ProcessApplicationManifest.navigationJsons has files with absolute paths | | [Issue #270731522](https://issuetracker.google.com/issues/270731522) Accessing GradleBuildProject.Builder through AnalyticsConfiguratorService is not allowed after AnalyticsService is created | | [Issue #228846664](https://issuetracker.google.com/issues/228846664) AndroidTest.packaging.jniLibs.keepDebugSymbols doesn't affect androidTest packaging | | [Issue #280475500](https://issuetracker.google.com/issues/280475500) Compilation allowed for illegal color values | | [Issue #281942489](https://issuetracker.google.com/issues/281942489) Incorrect "ReplaceWith" for VariantBuilder | | [Issue #278767328](https://issuetracker.google.com/issues/278767328) Gradle 8.1 breaks configuration caching due to .gradle/.android/analytics.settings | | [Issue #170650361](https://issuetracker.google.com/issues/170650361) Deprecation messages doesn't use \`ReplaceWith\` | | [Issue #170131595](https://issuetracker.google.com/issues/170131595) Expose a way to get the default NDK version | | [Issue #284029820](https://issuetracker.google.com/issues/284029820) Android Gradle plugin requires Java 17 to run. | | [Issue #285170632](https://issuetracker.google.com/issues/285170632) ASM Transform and toAppend() incompatibility | | [Issue #286593642](https://issuetracker.google.com/issues/286593642) Fix LintErrors when running lint with K2 UAST via Gradle on a KMP project | | [Issue #238447946](https://issuetracker.google.com/issues/238447946) Support for Variant level missingDimensionStrategy, and possibly build type/flavor matchingFallback | | [Issue #280831521](https://issuetracker.google.com/issues/280831521) \`android.injected.studio.version\` was removed in Android Studio Giraffe | | [Issue #278602339](https://issuetracker.google.com/issues/278602339) Add ability to disable AndroidXDependencyCheck | | [Issue #281825213](https://issuetracker.google.com/issues/281825213) generateLocaleConfig in agp 8.1.0 uses non-deterministic ordering, breaking reproducible builds | | [Issue #203113147](https://issuetracker.google.com/issues/203113147) Advertise R8 / D8 version requirements in AAR metadata (e.g. for coreLibraryDesugaring and new API out-of-lining) | | [Issue #286859043](https://issuetracker.google.com/issues/286859043) Sync warning: "GradleBuildProject.Builder should not be accessed through AnalyticsConfiguratorService after AnalyticsService is created" | | [Issue #282119683](https://issuetracker.google.com/issues/282119683) Update to Gradle 8.2 milestone or RC | | [Issue #287967703](https://issuetracker.google.com/issues/287967703) Cannot access 'java.lang.Comparable' | | [Issue #294771624](https://issuetracker.google.com/issues/294771624) androidResources is not available in the android library module | | [Issue #295205663](https://issuetracker.google.com/issues/295205663) Execution failed for task ':app:mergeReleaseClasses' after Updating AGP from 8.0.2 to 8.1.0 | | [Issue #278767328](https://issuetracker.google.com/issues/278767328) Gradle 8.1 breaks configuration caching due to .gradle/.android/analytics.settings | | [Issue #293547829](https://issuetracker.google.com/issues/293547829) \[AGP 8.1.0\] ./gradlew test fails with "Unable to find manifest output" if both splits.abi.isEnable and testOptions.unitTests.isIncludeAndroidResources are true | | [Issue #296250245](https://issuetracker.google.com/issues/296250245) Android Studio Giraffe does not respect versionCodeOverride with AGP 8.1 | | [Issue #295039976](https://issuetracker.google.com/issues/295039976) AGP 8.1.0 uninstalls app after running instrumented tests - 7.4.2 does not | | [Issue #303641463](https://issuetracker.google.com/issues/303641463) Tranforming an APK leads to a error with ListingFileRedirectTask | | [Issue #303737186](https://issuetracker.google.com/issues/303737186) HEDGEHOG REGRESSION: Run button is delayed by a few seconds (Creating spec) | |
| **Dexer (D8)** | |---| | [Issue #293592205](https://issuetracker.google.com/issues/293592205) Enable native record and sealed classes when dexing for min-api 34 and above | |
| **Lint** | |---| | [Issue #243267012](https://issuetracker.google.com/issues/243267012) Instantiated lint check does not handle AppComponentFactory well | | [Issue #283693338](https://issuetracker.google.com/issues/283693338) Lint 8.2.0 alphas still do not support top-level function imports in kotlin | | [Issue #269759189](https://issuetracker.google.com/issues/269759189) Add an option to not include line and column numbers in lint baseline | | [Issue #269759189](https://issuetracker.google.com/issues/269759189) Add an option to not include line and column numbers in lint baseline | | [Issue #283693337](https://issuetracker.google.com/issues/283693337) Lint tests do not support Java 17 language features | | [Issue #218605730](https://issuetracker.google.com/issues/218605730) Bumblebee 2021.1.1 Patch 1 is saying an old version (20030203.000550) of commons-io is newer than 2.11.0. | | [Issue #283693338](https://issuetracker.google.com/issues/283693338) Lint 8.2.0 alphas still do not support top-level function imports in kotlin | | [Issue #218605730](https://issuetracker.google.com/issues/218605730) Bumblebee 2021.1.1 Patch 1 is saying an old version (20030203.000550) of commons-io is newer than 2.11.0. | | [Issue #257726238](https://issuetracker.google.com/issues/257726238) Android Studio improperly marks specified version as out-of-date. | | [Issue #285413332](https://issuetracker.google.com/issues/285413332) Lint ignores UseValueOf issue when using K2 UAST | | [Issue #294279964](https://issuetracker.google.com/issues/294279964) Unexpected issues from another project flagged by Android Lint | | [Issue #293900782](https://issuetracker.google.com/issues/293900782) Android Lint fails on a KMP library with \`property 'variantInputs.name' doesn't have a configured value.\` | |
| **Lint Integration** | |---| | [Issue #294385251](https://issuetracker.google.com/issues/294385251) DuplicatePlatformClasses lint error from testImplementation dependency | |
| **Shrinker (R8)** | |---| | [Issue #293501981](https://issuetracker.google.com/issues/293501981) java.lang.VerifyError: Verifier rejected class | | [Issue #295349278](https://issuetracker.google.com/issues/295349278) Build gets stuck on :minifyReleaseWithR8 when using Apache POI library | | [Issue #295576241](https://issuetracker.google.com/issues/295576241) Kotlin 1.9 causes Kotlin lambdas to be destroyed by R8 if nullchecks are stripped | |

<br />