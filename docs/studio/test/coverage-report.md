---
title: View code coverage reports  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/test/coverage-report
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# View code coverage reports Stay organized with collections Save and categorize content based on your preferences.



The Android Gradle plugin can create code coverage reports that track the
percentage of your code that your tests cover. This page describes how to
enable coverage reporting and generate reports.

You can generate coverage reports for each test type (unit and instrumentation)
for each variant. You can also generate unified coverage reports across
different test types, modules, and build variants.

## Enable code coverage

Code coverage must be enabled by setting `enableAndroidTestCoverage` and
`enableUnitTestCoverage` to `true` in the module-level build files for each
variant you want to get coverage reports for:

### Kotlin

```
android {
    // ...
    buildTypes {
        debug {
            // Enable coverage for unit tests
            enableUnitTestCoverage = true
            // Enable coverage for instrumentation tests
            enableAndroidTestCoverage = true
        }
    }
}
```

### Groovy

```
android {
    // ...
    buildTypes {
        debug {
            // Enable coverage for unit tests
            enableUnitTestCoverage true
            // Enable coverage for instrumentation tests
            enableAndroidTestCoverage true
        }
    }
}
```

### Change Jacoco version (optional)

AGP automatically applies Jacoco when you enable coverage on your modules.
However, if you need to use a specific version of Jacoco, you can specify it in
your module-level build file:

### Kotlin

```
android {
    jacoco {
        version = "JACOCO_VERSION"
    }
}
```

### Groovy

```
android {
    jacoco {
        version = 'JACOCO_VERSION'
    }
}
```

## Generate variant specific coverage reports

To generate coverage reports for only unit tests or only instrumented tests for
a specific variant, run the corresponding tasks.

| Test type | Command | Report location |
| --- | --- | --- |
| Unit tests | `./gradlew :module-name:createVariantNameUnitTestCoverageReport` | `path-to-your-project/module-name/build/reports/coverage/test/variant/index.html` |
| Instrumented tests | `./gradlew :module-name:createVariantNameAndroidTestCoverageReport` | `path-to-your-project/module-name/build/reports/coverage/androidTest/variant/connected/index.html` |

## Generate unified code coverage reports

You can generate unified code coverage reports using the `createCoverageReport`
and `createAggregatedCoverageReport` Gradle tasks. You can use these tasks to
generate a single HTML report that consolidates coverage data from different
test types (unit and instrumentation), modules, and build variants.
This provides a comprehensive view of your project's code coverage in a
single dashboard.

### Prerequisites

* Android Gradle Plugin 9.2.0-alpha07 or higher

To generate a unified report, run one of the following tasks from the command
line:

| Coverage scope | Command | Description | Report location |
| --- | --- | --- | --- |
| Current module | `./gradlew :module-name:createCoverageReport` | Generates a unified coverage report for the current module, merging data from all test types. | `path-to-your-project/module-name/build/reports/code_coverage_html_report/` |
| Current module and dependencies | `./gradlew :module-name:createAggregatedCoverageReport` | Generates a unified coverage report for the current module and all its dependencies. This task is available for app modules and [library modules with publication enabled](/build/publish-library). | `path-to-your-project/module-name/build/reports/aggregated_code_coverage_html_report/` |

The generated HTML report landing page shows a high-level summary of all
modules. You can drill down from module to package, from package to class, and
from class to source file.
Click any file to see code with highlighting for line and branch coverage:

* Green: Covered lines.
* Red: Uncovered lines.
* Yellow: Partial coverage (some instructions or branches missed).

[](/static/studio/videos/unified-coverage-report.mp4)