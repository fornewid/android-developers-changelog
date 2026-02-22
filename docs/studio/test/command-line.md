---
title: https://developer.android.com/studio/test/command-line
url: https://developer.android.com/studio/test/command-line
source: md.txt
---

# Test from the command line

This document describes how to run tests directly from the command line. This document assumes that you already know how to create an Android app and write tests for your app. For more information on how to build tests for your app, see[Test apps on Android](https://developer.android.com/training/testing).

When you build your app using the Gradle build system, the[Android Gradle plugin](https://developer.android.com/tools/building/plugin-for-gradle)lets you run tests from your Gradle project using the command line. For more fine-grained control, you can choose to run your tests through an[Android Debug Bridge (adb)](https://developer.android.com/tools/help/adb)shell. This can be useful when running tests in a[continuous integration](https://developer.android.com/studio/projects/continuous-integration)environment.

To learn how to run automated instrumented tests from the command line using virtual devices that Gradle manages for you, see[Scale your tests with Gradle Managed Devices](https://developer.android.com/studio/test/gradle-managed-devices).

## Run tests with Gradle

The Android Gradle plugin lets you run tests from your Gradle project using the command line.

The table below summarizes how to run your tests with Gradle:

**Table 1.**Different ways to run your tests with Gradle

|     Unit test type     |                          Command to run                           |                                                                                                                                                          Test result location                                                                                                                                                           |
|------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Local unit test        | Run the`test`task: ./gradlew test                                 | HTML test result files: <var translate="no">path_to_your_project</var>`/`<var translate="no">module_name</var>`/build/reports/tests/`directory. XML test result files: <var translate="no">path_to_your_project</var>`/`<var translate="no">module_name</var>`/build/test-results/`directory.                                           |
| Instrumented unit test | Run the`connectedAndroidTest`task: ./gradlew connectedAndroidTest | HTML test result files: <var translate="no">path_to_your_project</var>`/`<var translate="no">module_name</var>`/build/reports/androidTests/connected/`directory. XML test result files: <var translate="no">path_to_your_project</var>`/`<var translate="no">module_name</var>`/build/outputs/androidTest-results/connected/`directory. |

Gradle supports[task name abbreviations](https://docs.gradle.org/current/userguide/command_line_interface.html#sec:name_abbreviation). For example, you can initiate the`connectedAndroidTest`task by entering the following command:  

    ./gradlew cAT

You can also choose to run the Gradle tasks`check`and`connectedCheck`. These tasks run your local or instrumented tests, respectively, but include other checks added by other Gradle plugins.

### Run tests on a module

The`test`and`connectedAndroidTest`tasks run tests on each module in your project. You can run tests on a specific module by prefixing the`test`or`connectedAndroidTest`task with the module name and a colon (:). For example, the following command runs instrumented tests for just the`mylibrary`module:  

    ./gradlew mylibrary:connectedAndroidTest

### Run tests on a build variant

The`test`and`connectedAndroidTest`tasks run tests on each[build variant](https://developer.android.com/studio/build/build-variants)in your project. You can target a specific build variant using the following syntax:

- For local unit tests:  

      ./gradlew testVariantNameUnitTest

- For instrumented tests:  

      ./gradlew connectedVariantNameAndroidTest

| **Note:** To further restrict the tests that run, target a specific build variant within a specific module. For example, use`./gradlew
| `**mylibrary** `:connected`**VariantName**`UnitTest`to run all unit tests for the`VariantName`variant inside the`mylibrary`module.

### Run specific test methods or classes

When running local unit tests, Gradle lets you target specific tests using the`--tests`flag. For example, the following command runs only the`sampleTestMethod`tests for the specified build variant. To learn more about using the`--tests`flag, read Gradle's documentation on[test filtering](https://docs.gradle.org/current/userguide/java_testing.html#test_filtering).  


    ./gradlew testVariantNameUnitTest --tests '*.sampleTestMethod'

| **Note:** To run specific test methods or classes for your instrumented tests,[run your tests with adb](https://developer.android.com/studio/test/command-line#run-tests-with-adb).

## Run tests with adb

When you run tests from the command line with[Android Debug Bridge (adb)](https://developer.android.com/tools/help/adb), there are more options for choosing the tests to run than with any other method. You can select individual test methods, filter tests according to a custom annotation, or specify testing options. Since the test run is controlled entirely from the command line, you can customize your testing with shell scripts in various ways.

To run a test from the command line, run`adb shell`to start a command-line shell on your device or emulator. Inside that shell you can interact with the[activity manager](https://developer.android.com/studio/command-line/adb#am)using the`am`command and use its`instrument`subcommand to run your tests.

As a shortcut, you can start an adb shell, call`am instrument`, and specify command-line flags all on one input line. The shell opens on the device or emulator, runs your tests, produces output, and then returns to the command line on your computer.

To run a test with`am instrument`:

1. [Build](https://developer.android.com/studio/build/building-cmdline)or rebuild your main application and test package.
2. [Install](https://developer.android.com/studio/command-line/adb#move)your test package and main application Android package files (APK files) to your current Android device or emulator.
3. At the command line, enter:

       adb shell am instrument -w <test_package_name>/<runner_class>

   Where`<test_package_name>`is the Android package name of your test application, and`<runner_class>`is the name of the Android test runner class you are using. The Android package name is the value of the manifest element's package attribute in your test package's manifest file (`AndroidManifest.xml`).

   The Android test runner class is usually[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner):  

       adb shell am instrument -w com.android.example/androidx.test.runner.AndroidJUnitRunner

Your test results appear in`STDOUT`.

### am instrument flags

To find a list of all the flags to use with the`am instrument`command, run`adb shell am help`. Some important flags are described in the following table:

**Table 2.** Important`am instrument`flags

|           Flag           |      Value       |                                                                                                                                                                                                                                                                                                                                                                                                          Description                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-w`                     | (none)           | Forces`am instrument`to wait until the instrumentation terminates before terminating itself. This keeps the shell open until the tests have finished. This flag is required to see the results of your tests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `-r`                     | (none)           | Outputs results in raw format. Use this flag when you want to collect performance measurements so that they are not formatted as test results. This flag is designed for use with the flag`-e perf true`(documented in the[am instrument options](https://developer.android.com/studio/test/command-line#am-instrument-options)) section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `-e`                     | `<test_options>` | Provides testing options as key-value pairs. The`am instrument`tool passes these to the specified instrumentation class using its[`onCreate()`](https://developer.android.com/reference/android/test/InstrumentationTestRunner#onCreate(android.os.Bundle))method. You can specify multiple occurrences of`-e <test_options>`. The keys and values are described in the[am instrument options](https://developer.android.com/studio/test/command-line#am-instrument-options)section. You can only use these key-value pairs with[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner)or with[`InstrumentationTestRunner`](https://developer.android.com/reference/android/test/InstrumentationTestRunner)and its subclasses. Using them with any other class has no effect. |
| `--no-hidden-api-checks` | (none)           | Disables restrictions on the use of hidden APIs. For more information on what hidden APIs are and how this can affect your app, read[Restrictions on non-SDK interfaces](https://developer.android.com/guide/app-compatibility/restrictions-non-sdk-interfaces).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### am instrument options

The`am instrument`tool passes testing options to`AndroidJUnitRunner`or`InstrumentationTestRunner`in the form of key-value pairs, using the`-e`flag, with this syntax:  

    -e <key> <value>

Some keys accept multiple values. You specify multiple values in a comma-separated list. For example, this invocation of`AndroidJUnitRunner`provides multiple values for the`package`key:  

    adb shell am instrument -w -e package com.android.test.package1,com.android.test.package2 \
    > com.android.test/androidx.test.runner.AndroidJUnitRunner

The following table lists the key-value pairs you can use with your test runner:

**Table 3.**-e flag key-value pairs to use with your test runner

|      Key       |              Value               |                                                                                                                                                                    Description                                                                                                                                                                    |
|----------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `package`      | `<Java_package_name>`            | The fully qualified*Java* package name for one of the packages in the test application. Any test case class that uses this package name is executed. Notice that this is not an*Android*package name; a test package has a single Android package name but may have several Java packages within it.                                              |
| `class`        | `<class_name>`                   | The fully qualified Java class name for one of the test case classes. Only this test case class is executed.                                                                                                                                                                                                                                      |
| `class`        | `<class_name>`**#**`method name` | A fully qualified test case class name and one of its methods. Only this method is executed. Note the hash mark (#) between the class name and the method name.                                                                                                                                                                                   |
| `func`         | `true`                           | Runs all test classes that extend[InstrumentationTestCase](https://developer.android.com/reference/android/test/InstrumentationTestCase).                                                                                                                                                                                                         |
| `unit`         | `true`                           | Runs all test classes that do*not* extend either`InstrumentationTestCase`or[PerformanceTestCase](https://developer.android.com/reference/android/test/PerformanceTestCase).                                                                                                                                                                       |
| `size`         | \[`small`\|`medium`\|`large`\]   | Runs a test method annotated by size. The annotations are`@SmallTest`,`@MediumTest`, and`@LargeTest`.                                                                                                                                                                                                                                             |
| `perf`         | `true`                           | Runs all test classes that implement`PerformanceTestCase`. When you use this option, specify the`-r`flag for`am instrument`so that the output is kept in raw format and not reformatted as test results.                                                                                                                                          |
| `debug`        | `true`                           | Runs tests in debug mode.                                                                                                                                                                                                                                                                                                                         |
| `log`          | `true`                           | Loads and logs all specified tests but doesn't run them. The test information appears in`STDOUT`. Use this to verify combinations of other filters and test specifications.                                                                                                                                                                       |
| `emma`         | `true`                           | Runs an EMMA code coverage analysis and writes the output to`/data/<app_package>/coverage.ec`on the device. To override the file location, use the`coverageFile`key that is described in the following entry. **Note:** This option requires an EMMA-instrumented build of the test application, which you can generate with the`coverage`target. |
| `coverageFile` | `<filename>`                     | Overrides the default location of the EMMA coverage file on the device. Specify this value as a path and filename in UNIX format. The default filename is described in the entry for the`emma`key.                                                                                                                                                |

When using the`-e`flag, be aware of the following:

- `am instrument`invokes[`onCreate(Bundle)`](https://developer.android.com/reference/android/test/InstrumentationTestRunner#onCreate(android.os.Bundle))with a[`Bundle`](https://developer.android.com/reference/android/os/Bundle)containing the key-value pairs.
- The`package`key takes precedence over the`class`key. If you specify a package and then separately specify a class within that package, Android runs all the tests in the package and ignores the class key.
- The`func`key and`unit`key are mutually exclusive.

### Usage examples

The following sections provide examples of using`am instrument`to run tests. They are based on the following structure:

- The test package has the Android package name`com.android.demo.app.tests`.
- Two instrumented test classes:
  - `TestClass1`, which contains the test method`testMethod1`.
  - `TestClass2`, which contains test methods`testMethod2`and`testMethod3`.
- The test runner is[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner).

#### Run the entire test package

To run all of the test classes in the test package, enter:  

    adb shell am instrument -w com.android.demo.app.tests/androidx.test.runner.AndroidJUnitRunner

#### Run all tests in a test case class

To run all of the tests in the class`TestClass1`, enter:  

    adb shell am instrument -w  \
    > -e class com.android.demo.app.tests.TestClass1 \
    > com.android.demo.app.tests/androidx.test.runner.AndroidJUnitRunner

#### Select a subset of tests

To run all of the tests in the`TestClass1`class and the`testMethod3`method in`TestClass2`, enter:  

    adb shell am instrument -w \
    > -e class com.android.demo.app.tests.TestClass1,com.android.demo.app.tests.TestClass2#testMethod3 \
    > com.android.demo.app.tests/androidx.test.runner.AndroidJUnitRunner

You can find more use cases in the[`AndroidJUnitRunner`](https://developer.android.com/reference/androidx/test/runner/AndroidJUnitRunner#execution-options:)API reference.