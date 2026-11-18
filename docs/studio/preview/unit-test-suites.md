---
title: https://developer.android.com/studio/preview/unit-test-suites
url: https://developer.android.com/studio/preview/unit-test-suites
source: md.txt
---

> Documentation index: https://developer.android.com/studio/preview/llms.txt

> [!WARNING]
> **Experimental:** Unit test suites are in active development, and their APIs and DSL syntax might change between releases. Report feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).

Unit test suites run local JVM tests in isolated [`hostJar`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#hostJar(kotlin.Function1)) source
sets outside your module's default `src/test/` directory. Configure them with
the Android Gradle plugin (AGP) [test suites](https://developer.android.com/studio/preview/test-suites.md.txt) DSL to isolate JUnit
5, JUnit 4, or Robolectric tests per variant.

## Requirements

To use unit test suites, make sure that your project meets the following
requirements:

- [Android Studio](https://developer.android.com/studio/preview) Rabbit 3 Canary 3 or higher
- AGP 9.6.0-alpha03 or higher
- Gradle 9.7.1 or higher and JDK 17 or higher
- A `com.android.application` or `com.android.library` module

For more information about preview version matching, see [Compatibility with
Android Gradle plugin previews](https://developer.android.com/studio/preview/features#agp-previews).

## Set up a unit test suite

To add a unit test suite to an app or library module, complete the following
steps:

### Enable test suites

In your project's `gradle.properties` file, enable test suite support:

```properties
android.experimental.testSuiteSupport=true
```

### Configure the suite

In your module's `build.gradle.kts` file, create a suite inside the
`testOptions.customSuites` block with the `hostJar` and
[`useJunitEngine`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#useJunitEngine(kotlin.Function1)) blocks:

```kotlin
android {
    testOptions {
        customSuites {
            create("unitSuite") {
                // Exact variant names to test, such as "debug" or "demoDebug".
                targetVariants += listOf("debug")

                hostJar {
                    dependencies {
                        // JUnit 5 API for @org.junit.jupiter.api.Test.
                        implementation(
                            "org.junit.jupiter:junit-jupiter-api:5.10.2"
                        )
                        // Optional: JUnit 4 API for @org.junit.Test.
                        implementation("junit:junit:4.13.2")
                    }
                }

                useJunitEngine {
                    // Add "junit-jupiter" (JUnit 5), "junit-vintage" (JUnit 4),
                    // or both.
                    includeEngines += listOf("junit-jupiter", "junit-vintage")
                    enginesDependencies.add(
                        "org.junit.jupiter:junit-jupiter-engine:5.10.2"
                    )
                    enginesDependencies.add(
                        "org.junit.vintage:junit-vintage-engine:5.10.2"
                    )
                    enginesDependencies.add(
                        "org.junit.platform:junit-platform-launcher:1.10.2"
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

Your suite accesses the target variant's classes and dependencies automatically
without inheriting dependencies from the `testImplementation` configuration.

### Create tests

Put your unit tests in the `{module}/src/{suiteName}/kotlin/` or `java/`
directory and Java test resources in the `{module}/src/{suiteName}/resources/`
directory. For example, create the
`app/src/unitSuite/kotlin/com/example/myapp/CalculatorSuiteTest.kt` file:

```kotlin
package com.example.myapp

import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class CalculatorSuiteTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }
}
```

> [!NOTE]
> **Note:** Android Studio support for custom test suites isn't available, so verify and run suite code with Gradle. For more information, see [Known issues and
> limitations](https://developer.android.com/studio/preview/test-suites#known-issues).

## Include Android resources and Robolectric

To access merged Android resources, assets, manifests, and `R` classes, such as
for [Robolectric](https://developer.android.com/training/testing/local-tests/robolectric.md.txt) tests, set the
[`enableAndroidResources`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestSuiteHostJarSpec.md.txt#enableAndroidResources()) property of the
[`TestSuiteHostJarSpec`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestSuiteHostJarSpec.md.txt) interface to `true`:

```kotlin
android {
    testOptions {
        customSuites {
            create("roboSuite") {
                targetVariants += listOf("debug")

                hostJar {
                    enableAndroidResources = true
                    dependencies {
                        implementation("junit:junit:4.13.2")
                        implementation("org.robolectric:robolectric:4.14.1")
                        implementation("androidx.test:core-ktx:1.6.1")
                    }
                }

                useJunitEngine {
                    includeEngines += listOf("junit-vintage")
                    enginesDependencies.add(
                        "org.junit.vintage:junit-vintage-engine:5.10.2"
                    )
                    enginesDependencies.add(
                        "org.junit.platform:junit-platform-launcher:1.10.2"
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

## Customize tasks and coverage

Enable JaCoCo coverage on a suite with the [`codeCoverage`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#codeCoverage())
property. To customize Gradle `Test` options per target, pass a configuration
lambda to the [`AgpTestSuiteTarget.configureTestTasks`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuiteTarget.md.txt#configureTestTasks(kotlin.Function2))
method, which provides a [`TestTaskContext`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/TestTaskContext.md.txt) instance. To
attach verification tasks to the `check` task, use the
[`withTestTaskProviders`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#withTestTaskProviders(kotlin.Function2)) method:

```kotlin
android {
    testOptions {
        customSuites {
            named("unitSuite") {
                // Generates JaCoCo HTML and XML coverage reports.
                codeCoverage = true

                targets.named("default") {
                    configureTestTasks { context ->
                        systemProperty("suite.variant", context.targetedVariant)
                        maxParallelForks = 2
                    }
                }

                withTestTaskProviders { context ->
                    if (!context.isUpdateTask) {
                        tasks.named("check") {
                            dependsOn(this@withTestTaskProviders)
                        }
                    }
                }
            }
        }
    }
}
```

To apply `Test` task settings across every target in a suite, call the
[`AgpTestSuite.configureTestTasks`](https://developer.android.com/reference/tools/gradle-api/9.6/com/android/build/api/dsl/AgpTestSuite.md.txt#configureTestTasks(kotlin.Function2)) method on the suite
instead.

## Run tests and inspect reports

Run your suite from the command line with the generated
`test{Variant}{SuiteName}{Target}TestSuite` task:

```bash
./gradlew :app:testDebugUnitSuiteDefaultTestSuite
```

To run a single test class or method, pass Gradle's
[`--tests` option](https://docs.gradle.org/current/userguide/java_testing.html#test_filtering):

```bash
./gradlew :app:testDebugUnitSuiteDefaultTestSuite \
    --tests "com.example.myapp.CalculatorSuiteTest.addition_isCorrect"
```

After a test run completes, AGP generates reports at the following paths:

- **HTML test report** : `{module}/build/reports/tests/{taskName}/index.html`
- **JUnit XML results** : `{module}/build/test-results/{taskName}/`
- **JaCoCo coverage report** : `{module}/build/reports/coverage/{suiteName}/index.html`