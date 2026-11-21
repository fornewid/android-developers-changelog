---
title: https://developer.android.com/studio/preview/test-suites
url: https://developer.android.com/studio/preview/test-suites
source: md.txt
---

> Documentation index: https://developer.android.com/studio/preview/llms.txt

> [!WARNING]
> **Experimental:** Test suites are in active development, and their APIs and DSL syntax might change between releases. Report feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).

The Android Gradle plugin (AGP) lets you organize tests into named test suites
in your module's [`testOptions`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestOptions.md.txt) block. Each suite defines its own
source sets, dependencies, JUnit Platform test engines, and target build
variants.

## Why use test suites

By default, an Android module provides one `test` source set for local unit
tests and one `androidTest` source set for instrumented tests. Test suites
decouple test organization from those two source sets so that you can do the
following:

- **Separate tests by purpose** : Keep unit, Robolectric, UI, screenshot, and backup tests in dedicated `src/{suiteName}/` directories instead of mixing them in the `src/test/` or `src/androidTest/` directories.
- **Isolate dependencies and engines** : Configure each suite's classpath and JUnit Platform test engine without adding dependencies to your app or the `testImplementation` and `androidTestImplementation` configurations.
- **Target specific variants and devices**: Select build variants and devices per suite so that fast checks run locally and longer suites run in continuous integration.

## Suite types

AGP includes built-in test suites for specialized workflows and the
[`AgpTestSuite`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt) interface for custom suites. The following
table lists the available suite types:

| Suite type | DSL container | Purpose |
|---|---|---|
| [Unit test suites](https://developer.android.com/studio/preview/unit-test-suites.md.txt) | `testOptions.customSuites` | Run JUnit 5, JUnit 4, or Robolectric tests on the local JVM with the `hostJar` block. |
| [Instrumented test suites](https://developer.android.com/studio/preview/instrumented-test-suites.md.txt) | `testOptions.customSuites` | Run device tests on connected or build-managed devices with the `testApk` block and the `android-test-engine` test engine. |
| [Screenshot testing with test suites](https://developer.android.com/studio/preview/compose-screenshot-testing-with-testsuites.md.txt) | [`testOptions.screenshotTests`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestOptions.md.txt#screenshotTests()) | Render and compare `@PreviewTest` Compose previews on the host. |
| [Automated backup and restore testing](https://developer.android.com/studio/preview/backup-restore-testing.md.txt) | [`testOptions.backupTests`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestOptions.md.txt#backupTests()) | Verify app data across local, cloud, and device-to-device transfers. |
| [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys.md.txt) | `testOptions.customSuites` | Run AI-driven XML user journeys on connected devices. |
| [Custom asset or mixed suites](https://developer.android.com/studio/preview/test-suites.md.txt#custom-suites) | `testOptions.customSuites` | Run static test definitions with a custom engine or combine the `hostJar`, `testApk`, and `assets` blocks in one suite. |

> [!NOTE]
> **Note:** Use the `testOptions.customSuites` block instead of the deprecated [`testOptions.suites`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestOptions.md.txt#suites()) block.

## Requirements

To use custom test suites, make sure that your project meets the following
requirements:

- [Android Studio](https://developer.android.com/studio/preview.md.txt) Rabbit 3 Canary 3 or higher
- AGP 9.6.0-alpha03 or higher
- Gradle 9.7.1 or higher and JDK 17 or higher
- A `com.android.application` or `com.android.library` module

Test suites aren't supported in `com.android.kotlin.multiplatform.library` or
`com.android.test` modules. For more information about preview version matching,
see [Compatibility with Android Gradle plugin previews](https://developer.android.com/studio/preview/features.md.txt#agp-previews).

## Set up a custom test suite

For step-by-step setup guides, see [Unit test suites](https://developer.android.com/studio/preview/unit-test-suites.md.txt) and
[Instrumented test suites](https://developer.android.com/studio/preview/instrumented-test-suites.md.txt). To define your own custom
suite, first enable test suites in your project's `gradle.properties` file:

```properties
android.experimental.testSuiteSupport=true
```

Next, declare a suite in the `testOptions.customSuites` block of your module's
`build.gradle.kts` file. Specify the [`targetVariants`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#targetVariants())
property, one or more source blocks, the [`useJunitEngine`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#useJunitEngine(kotlin.Function1))
block, and at least one target in the [`targets`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#targets()) block:

```kotlin
import com.android.build.api.dsl.AgpTestSuiteInputParameters

android {
    testOptions {
        customSuites {
            create("mySuite") {
                // Exact variant names to test, such as "debug" or "demoDebug".
                targetVariants += listOf("debug")

                // Add one or more blocks: hostJar {}, testApk {}, or assets {}.
                assets {}

                useJunitEngine {
                    includeEngines += listOf("my-custom-engine")
                    enginesDependencies.add(
                        "com.example:my-custom-junit-engine:1.0.0"
                    )
                    enginesDependencies.add(
                        "org.junit.platform:junit-platform-launcher:1.10.2"
                    )

                    // Request build and SDK artifacts read by your engine.
                    inputs += listOf(
                        AgpTestSuiteInputParameters.STATIC_FILES,
                        // Omit TESTED_APKS in com.android.library modules.
                        AgpTestSuiteInputParameters.TESTED_APKS,
                        AgpTestSuiteInputParameters.ADB_EXECUTABLE,
                    )
                }

                targets {
                    create("default")
                }
            }
        }
    }
}
```

Inside a custom `TestEngine` implementation, use the
[`TestSuiteExecutionClient.default`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/testsuites/TestSuiteExecutionClient.md.txt#default()) property to read
[`AgpTestSuiteInputParameters`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteInputParameters.md.txt) enum values and standard
[`TestEngineInputProperty`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/testsuites/TestEngineInputProperty.md.txt) constants such as
`SERIAL_IDS` and `RESULTS_DIR`.

### Source set directories

Each suite's directory layout depends on whether it declares one source block or
[combines multiple source blocks](https://developer.android.com/studio/preview/instrumented-test-suites.md.txt#mixed-suites). The following table lists the
default paths under the `{module}/src/{suiteName}/` directory:

| Source block | Single-source suite | Mixed suite |
|---|---|---|
| [`hostJar`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#hostJar(kotlin.Function1)) | `kotlin/`, `java/`, `resources/` | `test/kotlin/`, `test/java/`, `test/resources/` |
| [`testApk`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#testApk(kotlin.Function1)) | `kotlin/`, `java/`, `res/`, `assets/`, `AndroidManifest.xml` | `androidTest/kotlin/`, `androidTest/java/`, `androidTest/res/`, `androidTest/assets/`, `androidTest/AndroidManifest.xml` |
| [`assets`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#assets(kotlin.Function1)) | Suite root directory | `assetsTest/` |

Don't reuse built-in source set, flavor, build type, or variant names such as
`main`, `androidTest`, or `debug` as a suite name.

### Control targets per variant

To enable or disable a suite target for specific variants, configure the
[`TestSuiteTargetBuilder`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/variant/TestSuiteTargetBuilder.md.txt) interface through the
[`HasTestSuitesBuilder.suites`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/variant/HasTestSuitesBuilder.md.txt#suites()) property in the
`beforeVariants` block:

```kotlin
androidComponents {
    beforeVariants { variantBuilder ->
        if (variantBuilder.buildType == "release") {
            variantBuilder.suites["mySuite"]
                ?.targets
                ?.get("default")
                ?.enable = false
        }
    }
}
```

## Run suites and inspect reports

AGP creates a Gradle task for each combination of variant, suite, and target.
The following table lists the task patterns:

| Task type | Naming pattern | Example command |
|---|---|---|
| Standard suite target | `test{Variant}{SuiteName}{Target}TestSuite` | `./gradlew :app:testDebugMySuiteDefaultTestSuite` |
| Target with the `targetDevices` property | `test{Variant}{SuiteName}{Target}{Devices}TestSuite` | `./gradlew :app:testDebugAndroidSuiteManagedCiPhonesTestSuite` |
| Baseline update (`requiresUpdateTask = true`) | `update{Variant}{SuiteName}{Target}TestSuite` | `./gradlew :app:updateDebugScreenshotTestDefaultTestSuite` |
| Module report aggregation | `testAllSuites` | `./gradlew :app:testAllSuites` |
| Module and dependency aggregation | `testAllSuitesWithDependencies` | `./gradlew :app:testAllSuitesWithDependencies` |

The `test`, `connectedCheck`, and `check` tasks don't run custom suites unless
you wire them with the [`withTestTaskProviders`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#withTestTaskProviders(kotlin.Function2)) method. To
enable the `testAllSuites` and `testAllSuitesWithDependencies` tasks, set the
`android.experimental.reportAggregationSupport=true` property in your
`gradle.properties` file.

Each suite run writes outputs to the following locations:

- **HTML test report** : `{module}/build/reports/tests/{taskName}/index.html`
- **JUnit XML results** : `{module}/build/test-results/{taskName}/`
- **Code coverage report** : `{module}/build/reports/coverage/{suiteName}/index.html`
- **Aggregated reports** : `{module}/build/reports/{aggregationTask}/test-report/index.html` and `coverage-report/index.html`

To generate code coverage reports, set the [`codeCoverage`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#codeCoverage())
property to `true` on the suite. For Compose screenshot suites, configure the
suite in your `build.gradle.kts` file with
`testOptions.customSuites.named("{suiteName}") { codeCoverage = true }`.

## Known issues and limitations

Test suites have the following limitations:

- **IDE integration**: Android Studio support for custom test suites isn't available. The code editor might show unresolved reference errors in suite source files even when your build is configured properly. Build and run test suites from the command line using Gradle instead.
- **Task caching** : Test suite tasks always rerun when invoked and aren't loaded from the Gradle build cache. Suites with no test files are skipped with the `NO-SOURCE` status.