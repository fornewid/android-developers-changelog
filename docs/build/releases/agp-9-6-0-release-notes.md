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
| SDK Build Tools | 36.0.0 | 36.0.0 | [Install](https://developer.android.com/studio/intro/update.md.txt#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools.md.txt) SDK Build Tools. |
| NDK | N/A | 28.2.13676358 | [Install](https://developer.android.com/studio/projects/install-ndk.md.txt#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk.md.txt#apply-specific-version) a different version of the NDK. |
| JDK | 17 | 17 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config.md.txt#jdk). |

<br />

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

## Fixed issues


### Android Gradle plugin 9.6.0-alpha03

Fixed Issues **Android Gradle Plugin** [Issue #376975539](https://issuetracker.google.com/issues/376975539) Ladybug UI is slower than Koala [Issue #567487269](https://issuetracker.google.com/issues/567487269) Make analyzeReleaseR8Config output print out link to the report [Issue #396148600](https://issuetracker.google.com/issues/396148600) IDE Performance Slows to a Crawl During Gradle Build in large project **Lint Integration** [Issue #566069554](https://issuetracker.google.com/issues/566069554) \[AGP 9.x\] Broken Gradle cache: Moving sources fails Lint analysis

### Android Gradle plugin 9.6.0-alpha02

Fixed Issues **Android Gradle Plugin** [Issue #567815521](https://issuetracker.google.com/issues/567815521) Unsafe system properties read for R8 tasks

### Android Gradle plugin 9.6.0-alpha01

Fixed Issues **Android Gradle Plugin** [Issue #206104792](https://issuetracker.google.com/issues/206104792) shrinkresources does not work with library apks due to recent aapt2 change **Lint** [Issue #575549246](https://issuetracker.google.com/issues/575549246) Lint ThreadConstraint partial results are not deterministic across JVMs, which breaks build cache for lintAnalyze

<br />