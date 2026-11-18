---
title: https://developer.android.com/studio/preview/instrumented-test-suites
url: https://developer.android.com/studio/preview/instrumented-test-suites
source: md.txt
---

> Documentation index: https://developer.android.com/studio/preview/llms.txt

> [!WARNING]
> **Experimental:** Instrumented test suites are in active development, and their APIs and DSL syntax might change between releases. Report feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).

Instrumented test suites package device tests into isolated
[`testApk`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#testApk(kotlin.Function1)) APKs outside your module's default `src/androidTest/`
directory. Configure them with the Android Gradle plugin (AGP) [test
suites](https://developer.android.com/studio/preview/test-suites) DSL to separate UI, integration, or end-to-end checks with
dedicated dependencies, variants, and device targets.

## Requirements

To use instrumented test suites, make sure that your project meets the following
requirements:

- [Android Studio](https://developer.android.com/studio/preview) Rabbit 3 Canary 3 or higher
- AGP 9.6.0-alpha03 or higher
- Gradle 9.7.1 or higher and JDK 17 or higher
- A `com.android.application` or `com.android.library` module
- A device or emulator connected through Android Debug Bridge (adb) or a [build-managed device](https://developer.android.com/studio/test/managed-devices.md.txt) definition

For more information about preview version matching, see [Compatibility with
Android Gradle plugin previews](https://developer.android.com/studio/preview/features#agp-previews).

## Set up an instrumented test suite

To add an instrumented test suite to an app or library module, complete the
following steps:

### Enable test suites

In your project's `gradle.properties` file, enable test suite support:

```properties
android.experimental.testSuiteSupport=true
```

### Configure the suite

In your module's `build.gradle.kts` file, create a suite inside the
`testOptions.customSuites` block with the `testApk` and
[`useJunitEngine`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#useJunitEngine(kotlin.Function1)) blocks and
[`AgpTestSuiteInputParameters`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteInputParameters.md.txt) enum values:

```kotlin
import com.android.build.api.dsl.AgpTestSuiteInputParameters

android {
    testOptions {
        // Optional: define build-managed virtual devices and device groups.
        managedDevices {
            localDevices {
                create("api34Atd") {
                    // Use a device profile from Android Studio.
                    device = "Pixel 6"
                    apiLevel = 34
                    systemImageSource = "aosp-atd"
                }
            }
            groups {
                create("ciPhones") {
                    targetDevices.add(allDevices.getByName("api34Atd"))
                }
            }
        }

        customSuites {
            create("androidSuite") {
                targetVariants += listOf("debug")

                testApk {
                    dependencies {
                        implementation("junit:junit:4.13.2")
                        implementation("androidx.test.ext:junit:1.2.1")
                        implementation("androidx.test:runner:1.6.2")
                    }
                }

                useJunitEngine {
                    includeEngines += listOf("android-test-engine")
                    // Match the engine and listener versions to your AGP
                    // version.
                    enginesDependencies.add(
                        "com.android.tools.androidtest:" +
                            "android-test-engine:9.6.0-alpha03"
                    )
                    enginesDependencies.add(
                        "com.android.tools.androidtest:" +
                            "android-test-engine-result-listener:9.6.0-alpha03"
                    )
                    enginesDependencies.add(
                        "org.junit.platform:junit-platform-launcher:1.10.2"
                    )

                    inputs += listOf(
                        // Omit TESTED_APKS in com.android.library modules.
                        AgpTestSuiteInputParameters.TESTED_APKS,
                        AgpTestSuiteInputParameters.TEST_APKS,
                        AgpTestSuiteInputParameters.ADB_EXECUTABLE,
                        AgpTestSuiteInputParameters.AAPT2_EXECUTABLE,
                    )
                }

                targets {
                    // Runs on connected adb devices.
                    create("default")
                    // Optional: runs on build-managed devices or groups in
                    // targetDevices.
                    create("managed") {
                        targetDevices += listOf("ciPhones")
                    }
                }
            }
        }
    }
}
```

AGP configures the `AndroidJUnitRunner` test runner and package IDs
automatically without inheriting dependencies from the
`androidTestImplementation` configuration. To use a custom runner, set the
`android:name` attribute on the `instrumentation` element in your
`src/{suiteName}/AndroidManifest.xml` file.

### Create tests

Put your instrumented tests in the `{module}/src/{suiteName}/kotlin/` or `java/`
directory, along with any optional `res/` or `assets/` directories or an
`AndroidManifest.xml` file. For example, create the
`app/src/androidSuite/kotlin/com/example/myapp/AppContextSuiteTest.kt` file:

```kotlin
package com.example.myapp

import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Assert.assertEquals
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class AppContextSuiteTest {
    @Test
    fun useAppContext() {
        val appContext =
            InstrumentationRegistry.getInstrumentation().targetContext
        assertEquals("com.example.myapp", appContext.packageName)
    }
}
```

> [!NOTE]
> **Note:** Android Studio support for custom test suites isn't available, so verify and run suite code with Gradle. For more information, see [Known issues and
> limitations](https://developer.android.com/studio/preview/test-suites#known-issues).

## Combine unit and instrumented tests

To run local JVM tests and instrumented device tests in a single Gradle task,
declare both the [`hostJar`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#hostJar(kotlin.Function1)) and `testApk` blocks in one suite. Place
host tests in the `src/{suiteName}/test/` directory and device tests in the
`src/{suiteName}/androidTest/` directory:

```kotlin
import com.android.build.api.dsl.AgpTestSuiteInputParameters

android {
    testOptions {
        customSuites {
            create("combinedSuite") {
                targetVariants += listOf("debug")

                hostJar {
                    dependencies {
                        implementation(
                            "org.junit.jupiter:junit-jupiter-api:5.10.2"
                        )
                    }
                }

                testApk {
                    dependencies {
                        implementation("junit:junit:4.13.2")
                        implementation("androidx.test.ext:junit:1.2.1")
                        implementation("androidx.test:runner:1.6.2")
                    }
                }

                useJunitEngine {
                    includeEngines += listOf(
                        "junit-jupiter",
                        "android-test-engine",
                    )
                    enginesDependencies.add(
                        "org.junit.jupiter:junit-jupiter-engine:5.10.2"
                    )
                    enginesDependencies.add(
                        "com.android.tools.androidtest:" +
                            "android-test-engine:9.6.0-alpha03"
                    )
                    enginesDependencies.add(
                        "com.android.tools.androidtest:" +
                            "android-test-engine-result-listener:9.6.0-alpha03"
                    )
                    enginesDependencies.add(
                        "org.junit.platform:junit-platform-launcher:1.10.2"
                    )

                    inputs += listOf(
                        // Omit TESTED_APKS in com.android.library modules.
                        AgpTestSuiteInputParameters.TESTED_APKS,
                        AgpTestSuiteInputParameters.TEST_APKS,
                        AgpTestSuiteInputParameters.ADB_EXECUTABLE,
                        AgpTestSuiteInputParameters.AAPT2_EXECUTABLE,
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

## Run tests and collect coverage

Use Gradle to run instrumented suites, filter test cases, and generate coverage
reports.

### Run on connected or build-managed devices

Run a connected target on every online adb device, or run a target configured
with the [`targetDevices`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteTarget.md.txt#targetDevices()) property:

```bash
# Run on connected adb devices.
./gradlew :app:testDebugAndroidSuiteDefaultTestSuite
# Run on the ciPhones build-managed device group.
./gradlew :app:testDebugAndroidSuiteManagedCiPhonesTestSuite
```

> [!NOTE]
> **Note:** Suite targets run on every online adb device in addition to devices in the `targetDevices` property. To restrict which connected devices run, set the `ANDROID_SERIAL` environment variable to a comma-separated list of serials.

### Filter instrumented tests

Filter tests with Gradle's [`--tests` option](https://docs.gradle.org/current/userguide/java_testing.html#test_filtering)
or `AndroidJUnitRunner` arguments:

```bash
./gradlew :app:testDebugAndroidSuiteDefaultTestSuite \
    --tests "com.example.myapp.AppContextSuiteTest.useAppContext"
```

You can also pass `AndroidJUnitRunner` arguments on the command line with a
project property such as
`-Pandroid.testInstrumentationRunnerArguments.size=small`. To set default runner
arguments in the `useJunitEngine` block, call the `addInputProperty` method,
such as `addInputProperty("android-test.instrumentation-args", "size=small")`.

### Collect on-device code coverage

On-device code coverage requires a debuggable build and a device that runs
Android 9 (API level 28) or higher. To collect coverage for an instrumented or
mixed suite, complete the following steps:

1. Set the `android.experimental.androidTest.coverage.useOnDeviceAgent=true` property in your `gradle.properties` file.
2. Set the [`codeCoverage`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#codeCoverage()) property to `true` on the suite.
3. If multiple devices are connected, target one device with the `ANDROID_SERIAL` environment variable.

For more information about agent requirements, see [View code coverage reports
(with on-device agent)](https://developer.android.com/studio/test/on-device-code-coverage).

### Inspect reports

After a test run completes, AGP generates outputs at the following paths:

- **HTML test report** : `{module}/build/reports/tests/{taskName}/index.html`
- **JUnit XML results** : `{module}/build/test-results/{taskName}/`
- **Per-device XML and logcat** : `{module}/build/intermediates/{variant}/{taskName}/results/`
- **Code coverage report** : `{module}/build/reports/coverage/{suiteName}/index.html`