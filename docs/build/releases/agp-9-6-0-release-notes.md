---
title: https://developer.android.com/build/releases/agp-9-6-0-release-notes
url: https://developer.android.com/build/releases/agp-9-6-0-release-notes
source: md.txt
---

> Documentation index: https://developer.android.com/build/llms.txt

<br />

Android Gradle plugin 9.6 is a minor release that includes a variety of new
features and improvements.

## Compatibility

The maximum API level that Android Gradle plugin 9.6 supports is API level 37.
Here is other compatibility info:


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 9.8.2 | 9.8.2 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 37.0.0 | 37.0.0 | [Install](https://developer.android.com/studio/intro/update.md.txt#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools.md.txt) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk.md.txt#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk.md.txt#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config.md.txt#jdk). |
| Kotlin Gradle plugin (KGP) | 2.2.10 | 2.4.20 | To learn more, see [Runtime dependency on Kotlin Gradle plugin](https://developer.android.com/build/releases/agp-9-0-0-release-notes.md.txt#runtime-dependency-on-kotlin-gradle-plugin). |

<br />

## Separate default and minimum Kotlin Gradle plugin versions

Starting with AGP 9.6.0-alpha04, AGP separates its default Kotlin Gradle plugin
(KGP) version (**2.4.20** ) from its minimum supported KGP version (**2.2.10** ).
In its published Gradle module metadata, AGP declares its runtime dependency on
KGP using Gradle [rich version constraints](https://docs.gradle.org/current/userguide/dependency_versions.html#sec:rich-version-constraints)
with `prefer("2.4.20")` and `reject("(,2.2.10)")`:

- **Default KGP version (2.4.20)** : If your build doesn't declare a KGP version---for example, when you use [built-in Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin.md.txt) without applying any Kotlin Gradle plugin---Gradle resolves KGP 2.4.20 automatically.
- **Supported KGP range (2.2.10 or higher)**: If your build declares any KGP version of 2.2.10 or higher, including versions lower than the 2.4.20 default (such as 2.2.10 or 2.3.10) or versions higher than 2.4.20, Gradle uses your declared version with built-in Kotlin enabled instead of forcing an upgrade to 2.4.20.
- **Unsupported KGP versions (lower than 2.2.10)** : AGP 9.6 rejects KGP versions lower than 2.2.10. If your build or a plugin requests a KGP version lower than 2.2.10, buildscript dependency resolution fails, even if you set `android.builtInKotlin=false` in `gradle.properties`. Gradle's error output lists which plugin or dependency requested the lower version; upgrade that plugin or declare KGP 2.2.10 or higher.

> [!IMPORTANT]
> **Important:** If you upgrade from AGP 9.0 through 9.5, the following KGP behavior changes apply:

- **Default KGP moves from 2.2.10 to 2.4.20** : Builds that don't declare a KGP version move from KGP 2.2.10 to 2.4.20. To keep compiling with KGP 2.2.10 (or another supported version), [declare that KGP version
  explicitly](https://developer.android.com/build/releases/agp-9-6-0-release-notes#specify-kgp-version).
- **KGP versions lower than 2.2.10 fail resolution instead of
  auto-upgrading**: In AGP 9.0 through 9.5, Gradle automatically upgraded KGP versions lower than 2.2.10 to 2.2.10. Starting with AGP 9.6, KGP versions lower than 2.2.10 fail dependency resolution.
- **Downgrading below 2.2.10 with `strictly` and
  `android.builtInKotlin=false` is no longer supported** : The AGP 9.0 through 9.5 workaround of opting out of built-in Kotlin and using `version { strictly(...) }` to use KGP versions lower than 2.2.10 fails dependency resolution in AGP 9.6 and higher.

### Specify a KGP version

Starting with AGP 9.6.0-alpha06, if your build uses the
[Android settings plugin](https://developer.android.com/build/android-settings-plugin.md.txt#configure-kgp-version), you can set the incubating
`kotlinGradlePluginVersion` property in your `settings.gradle` file to pin a
single KGP version across all projects in the build:

### Kotlin

    // settings.gradle.kts file
    android {
        kotlinGradlePluginVersion = "KGP_VERSION"
    }

### Groovy

```groovy
// settings.gradle file
android {
    kotlinGradlePluginVersion = 'KGP_VERSION'
}
```

When you set `kotlinGradlePluginVersion`:

- Kotlin Gradle plugins applied in `plugins` blocks use that version automatically, so you don't need to declare a version on each plugin.
- KGP dependencies on `buildscript` classpaths, including AGP's runtime dependency for built-in Kotlin, align to that version through `org.jetbrains.kotlin:kotlin-gradle-plugins-bom`, which must be available in your plugin or `buildscript` repositories.
- Gradle logs a warning if this overrides a different version in a `plugins` block or a higher version on a `buildscript` classpath.
- The setting requires a concrete version of 2.2.10 or higher and doesn't apply to `buildSrc` or included builds. AGP logs a warning if a project uses a different KGP version (for example, because `buildSrc` depends on it).

If you don't use the Android settings plugin and your top-level `plugins` block
already declares a Kotlin Gradle plugin---such as
`org.jetbrains.kotlin.plugin.compose`,
`org.jetbrains.kotlin.plugin.serialization`, `org.jetbrains.kotlin.jvm`, or
`org.jetbrains.kotlin.multiplatform`---with a version of 2.2.10 or higher, Gradle
aligns KGP to that version automatically through
`org.jetbrains.kotlin:kotlin-gradle-plugins-bom`.

If you don't use the Android settings plugin or apply other Kotlin Gradle
plugins and you want to use a KGP version other than the 2.4.20 default, add
`org.jetbrains.kotlin:kotlin-gradle-plugin` to the `buildscript` block in your
top-level build file:

### Kotlin

    // Top-level build.gradle.kts file
    buildscript {
        dependencies {
            classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:KGP_VERSION")
        }
    }

### Groovy

```groovy
// Top-level build.gradle file
buildscript {
    dependencies {
        classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:KGP_VERSION'
    }
}
```

Replace `KGP_VERSION` with the KGP version that you want to use, which must be
2.2.10 or higher (for example, `2.2.10` or `2.3.10`). You don't need
`version { strictly(...) }` or `android.builtInKotlin=false` to use a supported
KGP version lower than the 2.4.20 default.

### Considerations when pinning lower KGP versions

If you pin a KGP version lower than the 2.4.20 default, keep the following
Gradle compatibility considerations in mind (see
[Compatibility](https://developer.android.com/build/releases/agp-9-6-0-release-notes.md.txt#compatibility) for the required Gradle version):

- **Kotlin convention plugins in `buildSrc` or included builds** : Starting with AGP 9.6.0-alpha04, AGP requires Gradle 9.8.2. Gradle 9.8.2 bundles Kotlin 2.4, so `gradleApi()` contains classes with Kotlin 2.4 metadata. Because KGP 2.2.x can read Kotlin metadata only up to version 2.3, Kotlin convention plugins in `buildSrc` or included builds that apply `org.jetbrains.kotlin.jvm` at KGP 2.2.x and compile against `gradleApi()` fail with an incompatible metadata version error. Configure those plugin builds to use KGP 2.3.0 or higher (precompiled script plugins that use Gradle's bundled `kotlin-dsl` plugin are unaffected), even if your Android modules pin KGP 2.2.10.
- **Deprecation warnings with `--warning-mode=fail`** : KGP versions lower than 2.3.20 (including 2.2.10 and 2.3.10) call Gradle APIs that are deprecated in Gradle 9.8.2, which causes builds to fail when you run Gradle with `--warning-mode=fail`. To avoid these KGP deprecation warnings, use the default KGP version (2.4.20). Other plugins, such as KSP, might still emit Gradle 9 deprecation warnings independently.

## Removed runtime version constraint on KSP

Starting with AGP 9.6.0-alpha04, AGP removes its runtime dependency constraint
on `com.google.devtools.ksp:symbol-processing-gradle-plugin` (which AGP 9.0
through 9.5 constrained to `2.2.10-2.0.2`). Starting with KSP 2.3.0,
[Kotlin Symbol Processing (KSP)](https://developer.android.com/build/migrate-to-ksp.md.txt) versions are no longer tied to a
Kotlin version. You can declare and upgrade the `com.google.devtools.ksp` plugin
independently in your build files without AGP overriding the KSP version or
requiring `version { strictly(...) }`.

Because AGP 9.6 no longer upgrades KSP automatically and raises the default KGP
version to 2.4.20, projects that declare a Kotlin-prefixed KSP version (such as
`2.2.10-2.0.2`) must upgrade KSP to a version compatible with their KGP version
(see [KSP releases](https://github.com/google/ksp/releases)), or
[pin KGP](https://developer.android.com/build/releases/agp-9-6-0-release-notes.md.txt#specify-kgp-version) to a compatible version.

## Unified coverage and test reports

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.reportAggregationSupport=true` in your `gradle.properties` file.

AGP 9.6.0-alpha05 introduces tasks to generate HTML dashboards that consolidate
test results and coverage from various test types (unit and instrumentation),
modules, and build variants, providing a comprehensive overview in a single
dashboard. For more information, see [Generate unified code coverage reports](https://developer.android.com/studio/test/coverage-report.md.txt#unified)
and [View unified test reports](https://developer.android.com/studio/test/command-line.md.txt#view-test-reports).

## On-device code coverage for instrumented tests

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.androidTest.coverage.useOnDeviceAgent=true` and `android.experimental.reportAggregationSupport=true` in your `gradle.properties` file.

AGP 9.6.0-alpha01 adds on-device code coverage for instrumented tests. Instead
of instrumenting your app's classes with JaCoCo at build time, AGP adds a
coverage agent to your test APK, and the agent instruments the classes on the
test device while your tests run. This removes the JaCoCo instrumentation step
from builds that have `enableAndroidTestCoverage` enabled, and keeps
coverage-tracking code out of your app's APK. You run the same
`create{Variant}AndroidTestCoverageReport` task, and AGP generates the HTML and
XML reports in the same location. On-device code coverage requires a debuggable
app and a device that runs Android 9 (API level 28) or higher.

AGP adds the coverage agent library, `com.android.tools.test:coverage-agent`,
with the same version as AGP. For more information, see [View code coverage
reports (with on-device agent)](https://developer.android.com/studio/test/on-device-code-coverage).

## Test suites

> [!WARNING]
> **Experimental:** Test suites are in active development. To enable them, set the `android.experimental.testSuiteSupport=true` property in your `gradle.properties` file.

AGP 9.6 adds the following updates for the `testOptions.customSuites` block:

- Access merged Android resources and run Robolectric tests on the JVM by setting the [`enableAndroidResources`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestSuiteHostJarSpec.md.txt#enableAndroidResources()) property in the `hostJar` block.
- Run `testApk` suites in `com.android.library` modules, target build-managed device groups in the [`targetDevices`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteTarget.md.txt#targetDevices()) property, filter tests with the `--tests` option, and use automatic manifest runner configuration.
- Customize Gradle `Test` tasks per target with the [`AgpTestSuiteTarget.configureTestTasks`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteTarget.md.txt#configureTestTasks(kotlin.Function2)) method.
- Collect code coverage with the [`codeCoverage`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#codeCoverage()) property for Compose screenshot suites through the `testOptions.customSuites` block and for instrumented and mixed suites with the [on-device coverage
  agent](https://developer.android.com/build/releases/agp-9-6-0-release-notes#on-device-coverage).
- Match the `com.android.tools.androidtest:android-test-engine` and `android-test-engine-result-listener` dependency versions directly to the AGP version.

For more information, see [Test suites in the Android Gradle
plugin](https://developer.android.com/studio/preview/test-suites), [Unit test suites](https://developer.android.com/studio/preview/unit-test-suites.md.txt), and [Instrumented
test suites](https://developer.android.com/studio/preview/instrumented-test-suites).

## Markdown test reports

> [!WARNING]
> **Experimental:** This is an experimental feature. To enable this feature, set `android.experimental.testOptions.enableMarkdownReport=true` and `android.experimental.reportAggregationSupport=true` in your `gradle.properties` file.

AGP 9.6.0-alpha04 adds a Markdown version of the test report, `report.md`, to
help you and AI coding agents read test results without opening the HTML report
or parsing JUnit XML files. AGP writes `report.md` next to each HTML test report
and prints its location after the tests run. The report lists the test counts
and the failed tests with their stack traces. For screenshot tests, it also says
whether the images differ or the reference image is missing, and links to the
images. To get one report for all the test suites in a module, run
`testAllSuites`. For more information, see [View unified test reports](https://developer.android.com/studio/test/command-line.md.txt#view-test-reports).

## Fixed issues


### Android Gradle plugin 9.6.0-alpha03

Fixed Issues **Android Gradle Plugin** [Issue #376975539](https://issuetracker.google.com/issues/376975539) Ladybug UI is slower than Koala [Issue #567487269](https://issuetracker.google.com/issues/567487269) Make analyzeReleaseR8Config output print out link to the report [Issue #396148600](https://issuetracker.google.com/issues/396148600) IDE Performance Slows to a Crawl During Gradle Build in large project **Lint Integration** [Issue #566069554](https://issuetracker.google.com/issues/566069554) \[AGP 9.x\] Broken Gradle cache: Moving sources fails Lint analysis

### Android Gradle plugin 9.6.0-alpha02

Fixed Issues **Android Gradle Plugin** [Issue #567815521](https://issuetracker.google.com/issues/567815521) Unsafe system properties read for R8 tasks

### Android Gradle plugin 9.6.0-alpha01

Fixed Issues **Android Gradle Plugin** [Issue #206104792](https://issuetracker.google.com/issues/206104792) shrinkresources does not work with library apks due to recent aapt2 change **Lint** [Issue #575549246](https://issuetracker.google.com/issues/575549246) Lint ThreadConstraint partial results are not deterministic across JVMs, which breaks build cache for lintAnalyze

<br />