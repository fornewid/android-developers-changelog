---
title: https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder
url: https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder
source: md.txt
---

The Espresso Test Recorder tool lets you create UI tests for your app without writing any test code. By recording a test scenario, you can record your interactions with a device and add assertions to verify UI elements in particular snapshots of your app. Espresso Test Recorder then takes the saved recording and automatically generates a corresponding UI test that you can run to test your app.

Espresso Test Recorder writes tests based on the[Espresso Testing framework](https://developer.android.com/training/testing/espresso), an API in AndroidX Test. The Espresso API encourages you to create concise and reliable UI tests based on user actions. By stating expectations, interactions, and assertions without directly accessing the underlying app's activities and views, this structure prevents test flakiness and optimizes test run speed.  

## Turn off animations on your test device

Before using Espresso Test Recorder, make sure you turn off animations on your test device to prevent unexpected results. Follow the[Espresso setup instructions](https://developer.android.com/training/testing/espresso/setup), but note that you do not need to manually set a dependency reference to the Espresso library because Test Recorder does this automatically when you[save a recording](https://developer.android.com/studio/test/other-testing-tools/espresso-test-recorder#save-a-recording). These steps only need to be done once for a given project.

## Record an Espresso test

Espresso tests consist of two primary components: UI interactions and assertions on View elements. UI interactions include tap and type actions that a person may use to interact with your app. Assertions verify the existence or contents of visual elements on the screen. For example, an Espresso test for the[Notes testing app](https://github.com/googlecodelabs/android-testing)might include UI interactions for clicking on a button and writing a new note but would use assertions to verify the existence of the button and the contents of the note.

This section will go over how to create both of these test components using Espresso Test Recorder, as well as how to save your finished recording to generate the test.

### Record UI interactions

To start recording a test with Espresso Test Recorder, proceed as follows:

1. Click**Run** \>**Record Espresso Test**.
2. In the**Select Deployment Target** window, choose the device on which you want to record the test. If necessary,[create a new Android Virtual Device](https://developer.android.com/studio/run/managing-avds). Click**OK**.
3. Espresso Test Recorder triggers a build of your project, and the app must install and launch before Espresso Test Recorder allows you to interact with it. The**Record Your Test**window appears after the app launches, and since you have not interacted with the device yet, the main panel reads "No events recorded yet." Interact with your device to start logging events such as "tap" and "type" actions.

**Note** : Before you can begin logging interactions, you may see a dialog on your device that says "Waiting for Debugger" or "Attaching Debugger." Espresso Test Recorder uses the debugger to log UI events. When the debugger attaches, the dialog will close automatically; do not hit**Force Close**.

Recorded interactions will appear in the main panel in the**Record Your Test**window, as shown in figure 1 below. When you run the test, the Espresso test will try executing these actions in the same order.
![](https://developer.android.com/static/studio/images/test/espresso-test-recorder-window_2-2_2x.png)

**Figure 1.** The**Record Your Test**window with logged UI interactions.

### Add assertions to verify UI elements

Assertions verify the existence or contents of a[View](https://developer.android.com/reference/android/view/View)element through three main types:

- **text is**: Checks the text content of the selected View element
- **exists**: Checks that the View element is present in the current View hierarchy visible on the screen
- **does not exist**: Checks that the View element is not present in the current View hierarchy

To add an assertion to your test, proceed as follows:

1. Click**Add Assertion** . A**Screen Capture**dialog appears while Espresso gets the UI hierarchy and other information about the current app state. The dialog closes automatically once Espresso has captured the screenshot.
2. A layout of the current screen appears in a panel on the right of the**Record Your Test** window. To select a View element on which to create an assertion, click on the element in the screenshot or use the first drop-down menu in the**Edit assertion**box at the bottom of the window. The selected View object is highlighted in a red box.
3. Select the assertion you want to use from the second drop-down menu in the**Edit assertion** box. Espresso populates the menu with valid assertions for the selected View element.
   - If you choose the "text is" assertion, Espresso automatically inserts the text currently inside the selected View element. You can edit the text to match your desired assertion using the text field in the**Edit assertion**box.
4. Click**Save and Add Another** to create another assertion or click**Save Assertion**to close the assertion panels.

The screenshot in figure 2 shows a "text is" assertion being created to verify that the title of the note is "Happy Testing!":
![](https://developer.android.com/static/studio/images/test/espresso-test-recorder-assertion_2-2_2x.png)

**Figure 2.** The**Edit assertion**box after a View element is selected (in red).

While creating an assertion, you can continue interacting with your app, even with the assertion panels still open within the**Record Your Test** window. Espresso Test Recorder will keep logging your actions, but the assertion you are editing will appear before these interactions once it's saved. The screenshot for the assertion also retains the layout that the device or emulator had at the time you hit the**Add Assertion**button.

### Save a recording

Once you finish interacting with your app and adding assertions, use the following steps to save your recording and generate the Espresso test:

1. Click**Complete Recording** . The**Pick a test class name for your test**window appears.
2. Espresso Test Recorder gives your test a unique name within its package based on the name of the launched activity. Use the**Test class name** text field if you want to change the suggested name. Click**Save** .
   - If you have not added the Espresso dependencies to your app, a**Missing Espresso dependencies** dialog appears when you try to save your test. Click**Yes** to automatically add the dependencies to your`build.gradle`file.
3. The file automatically opens after Espresso Test Recorder generates it, and Android Studio shows the test class as selected in the**Project** window of the IDE.
   - Where the test saves depends on the location of your[instrumentation test](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests)root, as well as the package name of the launched activity. For example, tests for the[Notes testing app](https://github.com/googlecodelabs/android-testing)save in the**src** \>**androidTest** \>**java** \>**com.example.username.appname**folder of the app module on which you recorded the test.

## Run an Espresso test locally

To run an Espresso test, use the**Project** ![](https://developer.android.com/static/studio/images/studio-icon.png)window on the left side of the Android Studio IDE:

1. Open the desired app module folder and navigate to the test you want to run. The test's location depends on the location of your[instrumentation test](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests)root and the package name of the launched activity. The following examples demonstrate where a test would save for the[Notes testing app](https://github.com/googlecodelabs/android-testing):
   - If you are using the**[Android view](https://developer.android.com/studio/projects#ProjectFiles)** within the window, navigate to**java** \>**com.example.username.appname (androidTest)**.
   - If you are using the**Project** view inside the window, navigate to**src** \>**androidTest** \>**java** \>**com.example.username.appname**within the module folder.
2. Right-click on the test and click**Run 'testName.'**
   - Alternatively, you can open the test file and right-click on the generated test class or method. Read more about how to run tests on the[Test Your App](https://developer.android.com/studio/test#run_a_test)page.
3. In the**Select Deployment Target** window, choose the device on which you want to run the test. If necessary,[create a new Android Virtual Device](https://developer.android.com/studio/run/managing-avds). Click**OK**.

Monitor the progress of your test in the**Run** window at the bottom of the IDE. Android Studio runs a full build of your project and opens a tab with the name of your test in the**Run**window, as shown in figure 3. You can check whether your test passes or fails in this tab, as well as how long the test took to run. When the test finishes, the tab will log "Tests ran to completion."
![](https://developer.android.com/static/studio/images/test/run-window-espresso-test_2-2-preview-7_2x.png)

**Figure 3** . Sample output in the**Run**window after running an Espresso test locally.

To learn more about writing test run configurations, read the "Defining a test configuration for a class or method" section in[Create and Edit Run/Debug Configurations](https://developer.android.com/studio/run/rundebugconfig#creating).

## Run an Espresso test with Firebase Test Lab for Android

You can use tests generated by Espresso Test Recorder with[Firebase Test Lab](https://firebase.google.com/docs/test-lab/)to test your app in the cloud on hundreds of device configurations. There is no charge to test your app with Test Lab within the[free daily quota on the Spark plan](https://firebase.google.com/docs/test-lab/overview#quota_for_spark_and_flame_plans). To run Espresso tests with Firebase Test Lab,[create a Firebase project](https://firebase.google.com/docs/test-lab/web-ui#create_a_firebase_project)for your app and then follow the instructions to[Run your tests with Firebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests#run-ctl)from Android Studio.
![](https://developer.android.com/static/images/training/ctl-test-results.png)

**Figure 4** . Sample output in the**Run**window after running a test with Firebase Test Lab on multiple devices.