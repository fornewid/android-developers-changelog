---
title: https://developer.android.com/build/releases/agp-8-1-0-release-notes
url: https://developer.android.com/build/releases/agp-8-1-0-release-notes
source: md.txt
---

Android Gradle plugin 8.1.0 is a major release that includes a variety of new
features and improvements.

## Compatibility


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 8.0 | 8.0 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 33.0.1 | 33.0.1 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 25.1.8937393 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Kotlin DSL is the default for build configuration

New projects now use the Kotlin DSL (`build.gradle.kts`) by default for build
configuration. This offers a better editing experience than the Groovy DSL
(`build.gradle`) with syntax highlighting, code completion, and navigation to
declarations. Note that if you're using AGP 8.1 and the Kotlin DSL for build
configuration, you should use Gradle 8.1 for the best experience. To learn more,
see the [Kotlin DSL migration guide](https://developer.android.com/build/migrate-to-kotlin-dsl).

## Automatic per-app language support

> [!NOTE]
> **Note:** This feature won't make changes to your project in the same way as the [manual setup process](https://developer.android.com/guide/topics/resources/app-languages). All changes from the automatic process are done in generated files. For example, you won't see an `android:localeConfig` entry in your app's manifest or a file at `res/xml/locales_config.xml`. That is expected since all of the changes are generated automatically when the app is built.

Starting with Android Studio Giraffe Canary 7 and AGP 8.1.0-alpha07, you can
configure your app to support [per-app language
preferences](https://developer.android.com/guide/topics/resources/app-languages) automatically. Based on your
project resources, the Android Gradle plugin generates the `LocaleConfig` file
and adds a reference to it in the final manifest file, so you no longer have to
do it manually. AGP uses the resources in the `res` folders of your app modules
and any library module dependencies to determine the locales to include in the
`LocaleConfig` file.

Note that the automatic per-app language feature supports apps that run Android
13 (API level 33) or higher. To use the feature, you must set
`compileSdkVersion` to 33 or higher. To configure per-app language preferences
for prior versions of Android, you still need to
[use the APIs and in-app language pickers](https://developer.android.com/guide/topics/resources/app-languages#api-implementation).

> [!CAUTION]
> **Caution:** If you turn on automatic per-app language support for an app in production, make sure that all the locales in your app and library module dependency resources are also ready to be published with your app.

To enable automatic per-app language support, specify a default locale:

1. In the app module's `res` folder, create a new file called `resources.properties`.
2. In the `resources.properties` file, set the default locale with
   the `unqualifiedResLocale` label. To form the locale names, combine
   the language code with the optional script and region codes, separating each
   with a dash:

   - Language: Use the two- or three-letter [ISO 639-1](http://www.loc.gov/standards/iso639-2/php/code_list.php) code.
   - Script (optional): Use the [ISO 15924](https://unicode.org/iso15924/iso15924-codes.html)code.
   - Region (optional): Use either the two-letter [ISO 3166-1-alpha-2](https://www.iso.org/obp/ui/#iso:pub:PUB500001:en) code or three-digit [UN_M.49](https://unstats.un.org/unsd/methodology/m49/overview/) code.

   For example if your default locale is American English:

   ```groovy
       unqualifiedResLocale=en-US
       
   ```

AGP adds this default locale and any
[alternative locales](https://developer.android.com/guide/topics/resources/localization#creating-alternatives)
you've specified, using `values-*` directories in the `res` folder, to the
auto-generated `LocaleConfig` file.

> [!CAUTION]
> **Caution:** If automatic per-app language support is on, the build fails if you **do** manually create a `LocaleConfig` file. You must remove your manually created `LocaleConfig` file before you enable automatic per-app language support and build your app.

Automatic per-app language support is off by default. To turn the feature on,
use the `generateLocaleConfig` setting in the `androidResources {}` block of the
module-level `build.gradle.kts` file (`build.gradle` file if you're using
Groovy):

### Kotlin

```kotlin
android {
  androidResources {
    generateLocaleConfig = true
  }
}
```

### Groovy

```groovy
android {
  androidResources {
    generateLocaleConfig true
  }
}
```

## Android Lint contains bytecode targeting JVM 17

Starting with AGP 8.1.0-alpha04, Android Lint contains bytecode targeting JVM
17. If you write custom lint checks, you need to compile with JDK 17 or higher
and specify `jvmTarget = '17'` in your Kotlin compiler options.

To learn more about the lint tool, see
[Improve your code with lint checks](https://developer.android.com/studio/write/lint).

## Native library compression setting moved to DSL

Starting with AGP 8.1.0-alpha10, you'll get a warning if you don't configure
native library compression using the DSL instead of the manifest. The
following guidance explains how to update your configuration to use the DSL. To
get help making these updates, use the AGP Upgrade Assistant
(**Tools \> AGP Upgrade Assistant**).

> [!NOTE]
> **Note:** The `useLegacyPackaging` DSL only supports APK-producing modules. To configure native library compression for library modules, keep using the `extractNativeLibs` manifest attribute; you don't need to add anything using the DSL.

To use uncompressed native libraries, remove the `android::extractNativeLibs`
attribute from the manifest and add the following code to the module-level
`build.gradle.kts` file (`build.gradle` file if you're using Groovy):

### Kotlin

```kotlin
android {
  packagingOptions {
    jniLibs {
      useLegacyPackaging = false
    }
  }
}
```

### Groovy

```groovy
android {
  packagingOptions {
    jniLibs {
      useLegacyPackaging false
    }
  }
}
```

## Experimental build flags

These are experimental flags for configuring your build available in AGP 8.1.

| Flag | Added in | Default value | Notes |
|---|---|---|---|
| `android.experimental.useDefaultDebugSigningConfigForProfileableBuildtypes` | AGP 8.0 | `false` | Enabling this with no signing configs specified causes AGP to use the default debug signing config when running a profileable or debuggable build. This flag is disabled by default to encourage build authors to declare specific profiling signing configs. |
| `android.experimental.library.desugarAndroidTest` | AGP 8.0 | `false` | This flag lets library builders enable core library desugaring for test APKs without affecting the AAR produced, for example through linting. We plan to eventually support this behavior in the Variant API. |
| `android.experimental.testOptions.managedDevices.customDevice` | AGP 8.0 | `false` | If enabled, Gradle Managed Devices allows a user-defined custom device type that can be provided by a plugin. This flag must be enabled if you want to use the Firebase Test Lab plugin. |
| `android.lint.printStackTrace` | AGP 8.0 | `false` | If enabled, Android lint prints a stacktrace if it crashes. This flag has the same capabilities as the `LINT_PRINT_STACKTRACE` environment variable. |
| `android.experimental.testOptions.managedDevices.maxConcurrentDevices` | AGP 8.0 | None | Specifies the maximum number of concurrent Gradle Managed Devices (AVDs) to be active at any one point in time. If the value is 0 or negative, there is no maximum number of devices. |
| `android.experimental.testOptions.installApkTimeout` | AGP 8.0 | None | The timeout duration in seconds to install an APK. If the value is 0 or negative, it will be set to a default value by UTP. |

## Fixed issues

### Android Gradle plugin 8.1.4

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #310252873](https://issuetracker.google.com/issues/310252873) Do not run dexing task on subprojects' classes when they are already dex'd through artifact transforms | |

### Android Gradle plugin 8.1.3

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #293547829](https://issuetracker.google.com/issues/293547829) \[AGP 8.1.0\] ./gradlew test fails with "Unable to find manifest output" if both splits.abi.isEnable and testOptions.unitTests.isIncludeAndroidResources are true | | [Issue #304082728](https://issuetracker.google.com/issues/304082728) Build failure after updating to AGP 8.1 | |

### Android Gradle plugin 8.1.2

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #294771624](https://issuetracker.google.com/issues/294771624) androidResources is not available in the android library module | | [Issue #293547829](https://issuetracker.google.com/issues/293547829) \[AGP 8.1.0\] ./gradlew test fails with "Unable to find manifest output" if both splits.abi.isEnable and testOptions.unitTests.isIncludeAndroidResources are true | |
| **Shrinker (R8)** | |---| | [Issue #295576241](https://issuetracker.google.com/issues/295576241) Kotlin 1.9 causes Kotlin lambdas to be destroyed by R8 if nullchecks are stripped | | [Issue #296654327](https://issuetracker.google.com/issues/296654327) R8 fails with "Undefined value encountered during compilation" for play-services-measurement-21.3.0-runtime.jar | |

### Android Gradle plugin 8.1.1

| Fixed Issues ||
|---|---|
| **Dexer (D8)** | |---| | [Issue #289237734](https://issuetracker.google.com/issues/289237734) Java 16 Records: equals(null) throws NullPointerException | |
| **Shrinker (R8)** | |---| | [Issue #293501981](https://issuetracker.google.com/issues/293501981) java.lang.VerifyError: Verifier rejected class | | [Issue #295349278](https://issuetracker.google.com/issues/295349278) Build gets stuck on :minifyReleaseWithR8 when using Apache POI library | | [Issue #291130232](https://issuetracker.google.com/issues/291130232) Rejecting invocation when enable r8 optimize | | [Issue #289361079](https://issuetracker.google.com/issues/289361079) NoClassDefFoundError for java.lang.reflect.Executable | |

### Android Gradle plugin 8.1.0

| Fixed Issues ||
|---|---|
| **Android Gradle Plugin** | |---| | [Issue #263576736](https://issuetracker.google.com/issues/263576736) \`com.android.build.gradle.tasks.ShaderCompile\` issues with configuration cache | | [Issue #263469991](https://issuetracker.google.com/issues/263469991) Adding to Java resources using AGP APIs breaks configuration cache | | [Issue #257976107](https://issuetracker.google.com/issues/257976107) \[Android Studio : Flamingo \| 2022.2.1 Canary 8\] liblog.so is packaged inside the APK | | [Issue #263575963](https://issuetracker.google.com/issues/263575963) KGP reads manifest during configuration, invalidating configuration cache on manifest change | | [Issue #259995135](https://issuetracker.google.com/issues/259995135) Build warning message unclear when problem in merged manifest | | [Issue #265385297](https://issuetracker.google.com/issues/265385297) Upgrading to AGP 7.4 results in a StackOverflowError | | [Issue #246326007](https://issuetracker.google.com/issues/246326007) ClassNotFoundException in dynamic feature that depends directly on Kotlin library subproject | | [Issue #266967487](https://issuetracker.google.com/issues/266967487) processDebugUnitTestManifest is failing with manifest placeholders for test variants | | [Issue #266967487](https://issuetracker.google.com/issues/266967487) processDebugUnitTestManifest is failing with manifest placeholders for test variants | | [Issue #266135619](https://issuetracker.google.com/issues/266135619) namespace property probably belongs to HasAndroidResources | | [Issue #242051158](https://issuetracker.google.com/issues/242051158) Can't disable "Gradle files have changed since last project sync" message | | [Issue #227796082](https://issuetracker.google.com/issues/227796082) "We recommend using a newer Android Gradle plugin" when there isn't a newer one | | [Issue #266967487](https://issuetracker.google.com/issues/266967487) processDebugUnitTestManifest is failing with manifest placeholders for test variants | | [Issue #269759002](https://issuetracker.google.com/issues/269759002) Boolean flag for disabling compile SDK check in CheckAarMetadataTask | | [Issue #269598545](https://issuetracker.google.com/issues/269598545) Build error refers to API level 34, which does not exist | | [Issue #260059413](https://issuetracker.google.com/issues/260059413) Setting JVM toolchain does not affect JavaCompile targetCompatibility value | | [Issue #268128036](https://issuetracker.google.com/issues/268128036) Navigation deepLink entries with wildcard domains don't have an \`android:host\` attribute in merged manifest | | [Issue #270201653](https://issuetracker.google.com/issues/270201653) processDebugMainManifest task is failed since Android Gradle Plugin 8.1 | | [Issue #269758603](https://issuetracker.google.com/issues/269758603) Can we remove AnalyticsRecordingTask? | | [Issue #258621110](https://issuetracker.google.com/issues/258621110) Content of output-metadata.json is not consistent | | [Issue #269758603](https://issuetracker.google.com/issues/269758603) Can we remove AnalyticsRecordingTask? | | [Issue #258621110](https://issuetracker.google.com/issues/258621110) Content of output-metadata.json is not consistent | | [Issue #260059413](https://issuetracker.google.com/issues/260059413) Setting JVM toolchain does not affect JavaCompile targetCompatibility value | | [Issue #268128036](https://issuetracker.google.com/issues/268128036) Navigation deepLink entries with wildcard domains don't have an \`android:host\` attribute in merged manifest | | [Issue #270201653](https://issuetracker.google.com/issues/270201653) processDebugMainManifest task is failed since Android Gradle Plugin 8.1 | | [Issue #213266836](https://issuetracker.google.com/issues/213266836) Android Studio doesn't respect the STUDIO_GRADLE_JDK environment variable | | [Issue #268192807](https://issuetracker.google.com/issues/268192807) Custom source types should create multi-flavor sourcesets | | [Issue #274913388](https://issuetracker.google.com/issues/274913388) DependenciesInfoBuilder needs API update + doc | | [Issue #266599585](https://issuetracker.google.com/issues/266599585) DexingNoClasspathTransform (minSdk \>= 24) with Java 11 target fails due to missing nest members | | [Issue #260100335](https://issuetracker.google.com/issues/260100335) DslExtension.Builder.extendProjectWith() not working as described in Groovy | | [Issue #265336046](https://issuetracker.google.com/issues/265336046) Add VariantSelector.withFlavor API that doesn't use kotlin.Pair | | [Issue #266403349](https://issuetracker.google.com/issues/266403349) AndroidLintAnalysisTask (:lintAnalyzeExternalRelease) has a cache miss because \`proguard.txt\` has changed | | [Issue #272553504](https://issuetracker.google.com/issues/272553504) App merged manifest contains extractNativeLibs and useEmbeddedDex attributes from dependencies | | [Issue #268237729](https://issuetracker.google.com/issues/268237729) AGP: Expose path to AIDL tool and framework AIDL file as public API | | [Issue #274016286](https://issuetracker.google.com/issues/274016286) Request: let the IDE offer a fix for "PermittedSubclasses requires ASM9" | | [Issue #279954562](https://issuetracker.google.com/issues/279954562) Bug: "Enable KSP and use the KSP processor for this dependency instead" just goes to a website | | [Issue #278767328](https://issuetracker.google.com/issues/278767328) Gradle 8.1 breaks configuration caching due to .gradle/.android/analytics.settings | | [Issue #281825213](https://issuetracker.google.com/issues/281825213) generateLocaleConfig in agp 8.1.0 uses non-deterministic ordering, breaking reproducible builds | |
| **Dexer (D8)** | |---| | [Issue #266687543](https://issuetracker.google.com/issues/266687543) Core library desugaring crashing app after recent updates. | | [Issue #279780940](https://issuetracker.google.com/issues/279780940) agp 8.1.0 regression with API 21 - F/dex2oat ( 4176): art/compiler/driver/compiler_driver.cc:1181\] Check failed: !method-\>IsAbstract() | |
| **Lint** | |---| | [Issue #263526184](https://issuetracker.google.com/issues/263526184) Lint only checks safe casts for directly implemented interfaces, not inherited ones | | [Issue #263526227](https://issuetracker.google.com/issues/263526227) Lint doesn't check valid casts for call receivers | | [Issue #262851206](https://issuetracker.google.com/issues/262851206) TypedArray#close (API 31) not desugared but AS does not display warning when used in try-with-resources | | [Issue #263115741](https://issuetracker.google.com/issues/263115741) Bug: false positive warning of "The 'BC' provider is deprecated and as of Android P..." | | [Issue #263887242](https://issuetracker.google.com/issues/263887242) Lint false positive about remember after Kotlin upgrade to 1.8.0 | | [Issue #239767506](https://issuetracker.google.com/issues/239767506) False positive Lint warning for SDK_INT checks performed inside a method with a enum parameter | | [Issue #269323652](https://issuetracker.google.com/issues/269323652) TypographyQuotes lint check does not work on escaped quotes | | [Issue #270065082](https://issuetracker.google.com/issues/270065082) TrustAllX509TrustManager lint check incorrectly flags interfaces that extends X509TrustManager | | [Issue #242557502](https://issuetracker.google.com/issues/242557502) Reformatting just the inserted code of a replace fix | | [Issue #271575376](https://issuetracker.google.com/issues/271575376) Lint: intention preview throws exception for ReplaceStringQuickFix | |
| **Shrinker (R8)** | |---| | [Issue #278573402](https://issuetracker.google.com/issues/278573402) VerifyError: Verifier rejected class when using R8 with Kotlin 1.8.20 | | [Issue #280659987](https://issuetracker.google.com/issues/280659987) R8 on AGP 8 breaks Google Fit service | | [Issue #279702361](https://issuetracker.google.com/issues/279702361) Including source file information with residual names that overlap input names is not correctly represented | | [Issue #280904554](https://issuetracker.google.com/issues/280904554) R8 fails during Compose build with ArrayIndexOutOfBoundsException | | [Issue #280958704](https://issuetracker.google.com/issues/280958704) Simple StringBuilder related code misses tail call to append in release or debuggable=false mode | | [Issue #284188592](https://issuetracker.google.com/issues/284188592) A corner case in VirtualDispatchMethodArgumentPropagator.shouldActivateMethodStateGuardedByBounds() method | | [Issue #284334258](https://issuetracker.google.com/issues/284334258) dex-startup-optimization results in java.lang.VerifyError: Rejecting class | | [Issue #283715197](https://issuetracker.google.com/issues/283715197) Crash with Verification error on Android 12+ | |

<br />