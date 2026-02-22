---
title: https://developer.android.com/studio/test/test-in-android-studio
url: https://developer.android.com/studio/test/test-in-android-studio
source: md.txt
---

# Test in Android Studio

Android Studio is designed to make testing simple. It contains many features to simplify how you create, run, and analyze tests. You can set up tests that run on your local machine or instrumented tests that run on a device. You can easily run a single test or a specific group of tests on one or more devices. The test results are shown directly inside Android Studio.

![](https://developer.android.com/static/studio/images/test/test-results-in-android-studio.png)

**Figure 1.**Android Studio showing test results overview.

<br />

This page is about how to manage tests in Android Studio. To learn how to write automated Android tests, see[Test apps on Android](https://developer.android.com/training/testing).

## Test types and locations

The location of your tests depends on the type of test you write. Android projects have default source code directories for local unit tests and instrumented tests.

**Local unit tests** are located at<var translate="no">module-name</var>`/src/`**test**`/java/`. These are tests that run on your machine's local Java Virtual Machine (JVM). Use these tests to minimize execution time when your tests have no Android framework dependencies or when you can create test doubles for the Android framework dependencies. For more information on how to write local unit tests, see[Build local unit tests](https://developer.android.com/training/testing/local-tests).
| **Note:** When you run local unit tests, the Android Gradle plugin includes a library that contains all the APIs of the Android framework, which allows for the use of test doubles.

**Instrumented tests** are located at<var translate="no">$module-name</var>`/src/`**androidTest**`/java/`. These tests run on a hardware device or emulator. They have access to[`Instrumentation`](https://developer.android.com/reference/android/app/Instrumentation)APIs that give you access to information, such as the[`Context`](https://developer.android.com/reference/android/content/Context)class, on the app you are testing, and let you control the app under test from your test code. Instrumented tests are built into a separate APK, so they have their own[`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro)file. This file is generated automatically, but you can create your own version at<var translate="no">$module-name</var>`/src/`**androidTest**`/AndroidManifest.xml`, which will be merged with the generated manifest. Use instrumented tests when writing integration and functional UI tests to automate user interaction, or when your tests have Android dependencies that you can't create test doubles for. For more information on how to write instrumented tests, see[Build instrumented tests](https://developer.android.com/training/testing/instrumented-tests)and[Automate UI tests](https://developer.android.com/training/testing/instrumented-tests/ui-tests).

You can place your tests in build variant specific directories to test only specific build variants. For example, you could place some local unit tests in<var translate="no">$module-name</var>`/src/`**testMyFlavor**`/java/`so the tests target your app built with this flavor's source code. For more information on how to create these tailored tests, see[Create an instrumented test for a build variant](https://developer.android.com/studio/test/advanced-test-setup#create-instrumented-test-for-build-variant).

When you create a new project or add an app module, Android Studio creates the test source sets listed earlier and includes an example test file in each. You can see them in the**Project**window as shown in figure 2.

![](https://developer.android.com/static/studio/images/test/project-window-tests_2-2_2x.png)

**Figure 2.** Your project's**(1)** instrumented tests and**(2)** local JVM tests are visible in either the**Project** view (left) or**Android**view (right).

<br />

## Create new tests

You can add a new test for a specific class or method directly from its source code by following these steps:

1. Open the source file that contains the code you want to test.
2. Put your cursor in the name of the class or method you want to test, and press<kbd>Control+Shift+T</kbd>(<kbd>Command+Shift+T</kbd>on macOS).
3. In the popup that appears, click**Create New Test...**
4. In the**Create Test** dialog, choose**JUnit4** , edit the fields and methods you want to generate, and then click**OK**.
5. In the**Choose Destination Directory** dialog, click the source set corresponding to the type of test you want to create:**androidTest** for an instrumented test or**test** for a local unit test. Then click**OK**.

Alternatively, you can create a generic test file in the appropriate test source set as follows:

1. In the**Project** window on the left, click the drop-down menu and select the**Android**view.
2. Right click on the**java** directory and select**New \> Java Class** or**New \> Kotlin Class/File** . Alternatively, you can select the**java** directory and use the<kbd>Control+N</kbd>(<kbd>Command+N</kbd>on macOS) shortcut.
3. In the**Choose Destination Directory** dialog, click the source set corresponding to the type of test you want to create:**androidTest** for an instrumented test or**test** for a local unit test. Then click**OK**.
4. Name the file and then click**OK**.

If your app doesn't compile after adding a test, make sure you have the right test library dependencies set up. See[Build local tests](https://developer.android.com/training/testing/local-tests#dependencies)and[Build instrumented tests](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#setup)for the correct dependencies.

## Run tests

Before running any tests, make sure your project is fully synchronized with Gradle by clicking**Sync Project** ![](https://developer.android.com/static/studio/images/buttons/toolbar-sync-gradle.png)in the toolbar. You can run tests with different levels of granularity:

- To**run all tests in a directory or file**, open the Project window and do either of the following:

  - Right-click on a directory or file and click**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).
  - Select the directory or file and use shortcut<kbd>Control+Shift+R</kbd>.
- To**run all tests in a class or a specific method**, open the test file in the Code Editor and do either of the following:

  - Press the**Run test** icon![](https://developer.android.com/static/studio/images/buttons/run-test-icon.png)in the[gutter](https://www.jetbrains.com/help/idea/settings-gutter-icons.html).
  - Right-click on the test class or method and click**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).
  - Select the test class or method and use shortcut<kbd>Control+Shift+R</kbd>.

Your instrumented tests will run on a physical device or emulator. To learn more about setting up physical devices, see[Run apps on a hardware device](https://developer.android.com/studio/run/device). To learn more about setting up emulators, see[Run apps on the Android Emulator](https://developer.android.com/studio/run/emulator).

### Configure the test run

By default, your tests run using Android Studio's default run configuration. If you need to change some run settings such as the instrumentation runner and deployment options, you can edit the run configuration in the**Run/Debug Configurations** dialog (click**Run \> Edit Configurations**).

### Unified Gradle test runner

Android Gradle plugin 7.1.0 and Android Studio Bumblebee and higher use Gradle's own implementation of the Android instrumented test runner to run instrumented tests. By using the same test runner, results are likely to be consistent whether you run using AGP from the command line, such as on a continuous integration server, or from Android Studio.

![](https://developer.android.com/static/studio/images/test/consolidated-test-runner.png)

**Figure 3.**The Unified Gradle test runner.

<br />

Previous versions of Android Studio use the IntelliJ Android instrumented test runner instead of Gradle's Android instrumented test runner. So if you're not using the latest version of Android Studio, depending on whether you run your tests from Android Studio or from the command line using the Gradle plugin, you might see different test results, such as tests passing using one runner and failing on another.

![](https://developer.android.com/static/studio/images/test/no-consolidated-test-runner.png)

**Figure 4.**Discrete test runners in older versions of Android Studio.

<br />

If you already have instrumented test configurations saved to your project, they'll use Gradle to run tests on your connected device. You can create a new instrumented test configuration using the gutter action next to your test class or method, as shown below.

![](https://developer.android.com/static/studio/images/test/run-test-from-gutter.png)

**Figure 5.**Run tests from gutter action.

<br />

When running your instrumented tests, you can confirm that Android Studio is using the Gradle test runner by inspecting the test output in the Test Matrix for Gradle task output.

### Run across multiple devices in parallel

Instrumented tests by default run on one physical device or emulator. If you want to see how your tests behave on a larger set of devices, you can select more devices by following these steps:

1. Before running your tests, open the**target device drop-down** menu, and select**Select Multiple Devices...**.

   ![](https://developer.android.com/static/studio/images/test/select-multiple-devices.png)

   **Figure 6.**Select Multiple Devices drop-down menu.

   <br />

2. Select the desired devices and click**OK**.

3. Make sure the text on the target drop-down menu is changed to**Multiple Devices** and click**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).

4. The Test Matrix tool window shows the test results for each selected device configuration.

   ![](https://developer.android.com/static/studio/images/test/test-matrix-test-results.png)

   **Figure 7.**Test results in the Test Matrix tool window.

   <br />

5. You can click on a specific test to inspect the result in the output pane. You can also sort the tests by clicking the various columns.

### Run with Firebase Test Lab

Using[Firebase Test Lab](https://firebase.google.com/docs/test-lab/), you can simultaneously test your app on many popular Android devices and device configurations (different combinations of locale, orientation, screen size, and platform version). These tests run on physical and virtual devices in remote Google data centers. Test results provide test logs and include the details of any app failures.

To start using Firebase Test Lab, you need to do the following:

1. [Create a Google Account](https://accounts.google.com/), if you don't have one already.
2. In the[Firebase console](https://console.firebase.google.com/), click**Create New Project**.

| **Note:** For information on Firebase Test Lab usage and associated costs (if any), see[Usage levels, quotas, and pricing for Test Lab](https://firebase.google.com/docs/test-lab/usage-quotas-pricing).

Android Studio provides integrated tools that allow you to configure how you want to deploy your tests to Firebase Test Lab. After you have created a Firebase project, you can create a test configuration and run your tests:

1. Click**Run** \>**Edit Configurations**from the main menu.
2. Click**Add New Configuration** ![](https://developer.android.com/static/studio/images/buttons/add-sign-icon.png)and select**Android Instrumented Tests**.
3. Enter or select the details of your test, such as the test name, module type, test type, and test class.
4. From the**Target** drop-down menu under**Deployment Target Options** , select**Firebase Test Lab Device Matrix**.
5. If you are not logged in, click**Sign in with Google**and allow Android Studio to access your account.
6. Next to**Cloud Project**, select your Firebase project from the list.
7. Next to**Matrix configuration** , select one of the default configurations from the drop-down or create your own by pressing**Open Dialog** ![](https://developer.android.com/static/studio/images/buttons/open-dialog-icon.png). You can select one or more devices, Android versions, locales and screen orientations that you want to test your app with. Firebase Test Lab will test your app against every combination of your selections when generating test results.
8. Click**OK** in the**Run/Debug Configurations**dialog to exit.
9. Run your tests by clicking**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).

![](https://developer.android.com/static/studio/images/test/firebase-run-debug-configurations.png)

**Figure 8.**Creating a test configuration for Firebase Test Lab.

<br />

#### Analyze test results

When Firebase Test Lab completes running your tests, the**Run** window will open to show the results, as shown in figure 9. You may need to click**Show Passed** ![](https://developer.android.com/static/studio/images/buttons/show-passed-check-icon.png)to see all your executed tests.

![](https://developer.android.com/static/studio/images/test/firebase-instrumented-test-results.png)

**Figure 9.**The results of instrumented tests using Firebase Test Lab.

<br />

You can also analyze your tests on the web by following the link displayed at the beginning of the test execution log in the**Run**window.

### View test coverage

The test coverage tool is available for local unit tests to track the percentage and areas of your app code that your unit tests have covered. Use the test coverage tool to determine whether you have adequately tested the elements, classes, methods, and lines of code that make up your app.

To run tests with coverage, follow the same steps as described in[Run tests](https://developer.android.com/studio/test/test-in-android-studio#run-tests), only instead of clicking**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png), click**Run test-name with coverage** ![](https://developer.android.com/static/studio/images/buttons/run-test-with- coverage-icon.png). In the**Project** window, this option might be hidden behind**More Run/Debug** . You can also configure the coverage settings in the**Run/Debug Configurations** dialog, under the**Code Coverage**tab.

![](https://developer.android.com/static/studio/images/test/code-coverage-percentages.png)

**Figure 10.**Code coverage percentages for an application.

<br />

## View test results

When you run one or more tests from Android Studio, the results appear in the**Run**window. Figure 11 shows a successful test run.

![](https://developer.android.com/static/studio/images/test/run-window-test-results.png)

**Figure 11.**Test results appear in the Run window.

<br />

The**Run**window displays the tests in a tree view on the left, and the results and messages for the current test suite in the output pane on the right. Use the toolbars, context menus, and status icons to manage the test results, as follows:

1. Use the**run toolbar**to rerun the current test, stop the current test, rerun failed tests (not shown because it is available for unit tests only), pause output, and dump threads.
2. Use the**testing toolbar**to filter and sort test results. You can also expand or collapse nodes, show test coverage, and import or export test results.
3. Click the**context menu**to track the running test, show inline statistics, scroll to the stack trace, open the source code at an exception, auto scroll to the source, and select the first failed test when the test run completes.
4. **Test status icons**indicate whether a test has an error, was ignored, failed, is in progress, has passed, is paused, was terminated, or was not run.
5. Right-click a line in the tree view to display a context menu that lets you run the tests in debug mode, open the test source code file, or jump to the line in the source code being tested.

### Analyze test failures

When one or more of your tests fails, the results window shows a warning sign and the number of failures (for example, "Tests failed: 1"):

![](https://developer.android.com/static/studio/images/test/failed-test.png)

**Figure 12.**Failed test details in the output pane.

<br />

When you click the failing test in the tree view on the left, the output pane on the right shows the details of that test. It shows the expected value next to the actual value, so you can compare them. The**Click to see difference**link opens a diff viewer where you can see the results side by side.

## Learn more

This page covers the basic steps to follow when creating and running your first test using Android Studio. You can also choose to[run tests from the command line](https://developer.android.com/studio/test/command-line). You can also check out the[IntelliJ documentation on testing](https://www.jetbrains.com/help/idea/testing.html). For more information on how to configure your tests when creating a larger test suite, see[Advanced test setup](https://developer.android.com/studio/test/advanced-test-setup).