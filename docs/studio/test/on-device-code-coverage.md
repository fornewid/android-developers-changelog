---
title: https://developer.android.com/studio/test/on-device-code-coverage
url: https://developer.android.com/studio/test/on-device-code-coverage
source: md.txt
---

> [!WARNING]
> **Experimental:** On-device code coverage is in active development, and its behavior and Gradle properties might change between releases.

The Android Gradle plugin (AGP) can create code coverage reports for your
[instrumented tests](https://developer.android.com/training/testing/instrumented-tests) with an on-device coverage agent. By
default, AGP instruments your app's classes with JaCoCo when it builds your
app, which means that it adds code that records which parts of your app your
tests run. With the on-device coverage agent, AGP builds your app without this
extra code, and the agent instruments your app's classes on the test device
while your tests run. This page describes how to enable on-device code coverage
and generate reports.

Compared with build-time code coverage, on-device code coverage offers the
following benefits:

- **Faster builds**: AGP doesn't run the JaCoCo instrumentation step on your app's classes and their dependencies, which can reduce build times by 10-20%.
- **Smaller debug APKs**: AGP doesn't add coverage-tracking code to your app's classes, which can make your debug APK 20-25% smaller.
- **No unused generated classes in reports**: Generated classes that your tests don't use don't lower your coverage numbers.

The actual build time and APK size improvements depend on your project.

## Prerequisites

To use on-device code coverage, make sure that your project and your test
devices meet the following requirements:

- AGP 9.6.0-alpha01 or higher.
- A device or emulator that runs Android 9 (API level 28) or higher.
- A debuggable build type for the variant that you test, such as the default `debug` build type. The agent can attach only to debuggable apps.
- Instrumented tests that run with [`AndroidJUnitRunner`](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner) or a custom test runner that extends it.

## Enable on-device code coverage

On-device code coverage uses the same `enableAndroidTestCoverage` property as
build-time code coverage. Set `enableAndroidTestCoverage` to `true` in the
module-level build files for each variant you want to get coverage reports for:

### Kotlin

    android {
        // ...
        buildTypes {
            debug {
                // Enable coverage for instrumentation tests
                enableAndroidTestCoverage = true
            }
        }
    }

### Groovy

    android {
        // ...
        buildTypes {
            debug {
                // Enable coverage for instrumentation tests
                enableAndroidTestCoverage true
            }
        }
    }

Then, enable the on-device coverage agent and report aggregation in your
project's `gradle.properties` file:

    android.experimental.androidTest.coverage.useOnDeviceAgent=true
    android.experimental.reportAggregationSupport=true

On-device code coverage generates its HTML report with the same renderer as
[unified code coverage reports](https://developer.android.com/studio/test/coverage-report#unified), so it requires both
properties.

## Generate on-device code coverage reports

To run your instrumented tests and generate coverage reports, connect a device
or start an emulator, and then run the following task:

| Coverage scope | Command | Report location |
|---|---|---|
| One variant | `./gradlew :module-name:createVariantNameAndroidTestCoverageReport` | `path-to-your-project/module-name/build/reports/coverage/androidTest/variant/connected/index.html` |

## Differences from build-time code coverage

On-device and build-time coverage reports can show different results for the
same tests. Keep the following differences in mind when you compare the two
reports, or when you move coverage thresholds from one to the other:

| Area | Build-time code coverage | On-device code coverage |
|---|---|---|
| **When classes are instrumented** | When AGP builds your app, using JaCoCo | On the test device while your tests run, using the coverage agent |
| **Classes in the report** | All classes in your module | Only the classes in your module's namespace that load while your tests run, so coverage percentages can be higher |
| **Instruction counts** | Java bytecode instructions | DEX bytecode instructions |
| **Branch counts** | Branches in Java bytecode | Branches in DEX bytecode. D8 can compile conditions into different branches, and each tool leaves out different compiler-generated branches, so counts can differ. |
| **Counters** | Instructions, branches, lines, complexity, methods, and classes | Instructions, branches, lines, methods, and classes. Complexity counters aren't supported yet. |
| **Test devices** | All API levels that your app supports | Android 9 (API level 28) and higher |
| **Raw coverage data** | `.ec` files | `coverage_metadata.pb` and `coverage_hits.pb` files |

To switch back to build-time code coverage, set
`android.experimental.androidTest.coverage.useOnDeviceAgent=false` or remove
the property. You don't need to change your build files or the tasks that you
run.

## Known issues

On-device code coverage has the following known issues:

- **Classes that don't load:** Classes that never load while your tests run don't appear in the report. Build-time code coverage reports list them with 0% coverage.
- **Aggregated reports:** If your project also collects coverage from host tests, such as unit tests, the aggregated coverage report that the `testAllSuites` and `testAllSuitesWithDependencies` tasks create combines Java bytecode counts from those tests with DEX bytecode counts from the agent. Because of the [differences between the two](https://developer.android.com/studio/test/on-device-code-coverage#differences), the aggregated instruction and branch numbers can differ from the numbers in build-time code coverage reports.

Report any other feedback and issues through the [issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).