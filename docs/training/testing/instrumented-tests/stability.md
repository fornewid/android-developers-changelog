---
title: https://developer.android.com/training/testing/instrumented-tests/stability
url: https://developer.android.com/training/testing/instrumented-tests/stability
source: md.txt
---

# Big test stability

The asynchronous nature of mobile applications and frameworks oftentimes makes it challenging to write reliable and repeatable tests. When a user event is injected, the testing framework must wait for the app to finish reacting to it, which could range from changing some text on screen to a complete recreation of an activity. When a test doesn't have a deterministic behavior, it's*flaky*.

Modern frameworks like Compose or Espresso are designed with testing in mind so there's a certain guarantee that the UI will be idle before the next test action or assertion. This is*synchronization*.

### Test synchronization

Issues can still arise when you run asynchronous or background operations unknown to the test, such as loading data from a database or showing infinite animations.
![flow diagram showing a loop that checks if the app is idle before making a test pass](https://developer.android.com/static/training/testing/instrumented-tests/sync.png)**Figure 1**: Test synchronization.

To increase the reliability of your test suite, you can install a way to track background operations, such as[Espresso Idling Resources](https://developer.android.com/training/testing/espresso/idling-resource). Also, you can replace modules for testing versions that you can query for idleness or that improve synchronization, such as[TestDispatcher](https://developer.android.com/kotlin/coroutines/coroutines-best-practices#test-coroutine-dispatcher)for coroutines or[RxIdler](https://github.com/square/RxIdler)for RxJava.
| **Warning:** You should avoid pausing your tests for an arbitrary period (sleep) to let the app run and stabilize. This makes tests unnecessary slow or flaky, because running the same test in different environments might need more or less time to execute.
![Diagram showing a test failure when the synchronization is based on waiting for a fixed time](https://developer.android.com/static/training/testing/instrumented-tests/flaky.png)**Figure 2**: Using sleep in tests leads to slow or flaky tests.

## Ways to improve stability

Big tests can catch lots of regressions at the same time because they test multiple components of an app. They typically run on emulators or devices, which means they have high fidelity. While large end-to-end tests provide comprehensive coverage, they are more prone to occasional failures.

The primary measures you can take to reduce flakiness are the following:

- Configure devices correctly
- Prevent synchronization issues
- Implement retries

To create big tests using[Compose](https://developer.android.com/develop/ui/compose/testing)or[Espresso](https://developer.android.com/training/testing/espresso), you typically start one of your activities and navigate as a user would, verifying that the UI behaves correctly using assertions or screenshot tests.

Other frameworks, such as[UI Automator](https://developer.android.com/training/testing/other-components/ui-automator), allow for a bigger scope, as you can interact with the system UI and other apps. However, UI Automator tests might require more manual synchronization so they tend to be less reliable.
| **Note:** Many third-party testing frameworks use UI Automator to run tests, so the same principles apply. Prefer Espresso and Compose Test APIs to create UI tests.

## Configure devices

First, to improve the reliability of your tests, you should make sure that the device's operating system doesn't unexpectedly interrupt the execution of the tests. For example, when a system update dialog is shown on top of other apps or when the space on disk is insufficient.

Device farm providers configure their devices and emulators so normally you don't have to take any action. However, they might have their own configuration directives for special cases.

### Gradle-managed devices

If you manage emulators yourself you can use[Gradle-managed devices](https://developer.android.com/studio/test/gradle-managed-devices)to define what devices to use to run your tests:  

    android {
      testOptions {
        managedDevices {
          localDevices {
            create("pixel2api30") {
              // Use device profiles you typically see in Android Studio.
              device = "Pixel 2"
              // Use only API levels 27 and higher.
              apiLevel = 30
              // To include Google services, use "google".
              systemImageSource = "aosp"
            }
          }
        }
      }
    }

With this configuration, the following command will create an emulator image, start an instance, run the tests and shut it down.  

    ./gradlew pixel2api30DebugAndroidTest

Gradle-managed devices contain mechanisms to retry in the event of device disconnections and other improvements.

## Prevent synchronization issues

Components that do background or asynchronous operations can lead to test failures because a test statement was executed before the UI was ready for it. As a test grows in scope, it increases the chances of becoming flaky. These synchronization issues are a primary source of flakiness because the test frameworks need to deduce if an activity is*done*loading or if it should wait longer.
| **Warning:** Adding arbitrary sleep commands should be avoided because they slow down the execution of the tests and don't eliminate flakiness.

### Solutions

You can use[Espresso's idling resources](https://developer.android.com/training/testing/espresso/idling-resource)to indicate when an app is busy, but it's hard to track every asynchronous operation, especially in very big end-to-end tests. Also, idling resources can be hard to install without polluting the code under test.

Instead of estimating whether an activity is busy or not, you can make your tests wait until specific conditions have been met. For example, you can wait until a specific text or component is shown in the UI.
![A wait-until mechanism works by asking whether a condition is met before continuing.](https://developer.android.com/static/training/testing/instrumented-tests/waitfor.png)**Figure 3.**Waiting for conditions to be met reduces flakiness.

Compose has a collection of testing APIs as part of the[`ComposeTestRule`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitUntil(kotlin.Long,kotlin.Function0))to wait for different matchers:  

    fun waitUntilAtLeastOneExists(matcher: SemanticsMatcher, timeout: Long = 1000L)

    fun waitUntilDoesNotExist(matcher: SemanticsMatcher, timeout: Long = 1000L)

    fun waitUntilExactlyOneExists(matcher: SemanticsMatcher,  timeout: Long = 1000L)

    fun waitUntilNodeCount(matcher: SemanticsMatcher, count: Int, timeout: Long = 1000L)

And a generic API that takes any function that returns a boolean:  

    fun waitUntil(timeoutMillis: Long, condition: () -> Boolean): Unit

Example usage:  

    composeTestRule.waitUntilExactlyOneExists(hasText("Continue")</code>)</p></td>

| **Key Point:** Use Idling Resources if needed in small UI tests, and wait-until APIs in bigger UI tests.

## Retry mechanisms

You should fix flaky tests, but sometimes the conditions that make them fail are so improbable that they are hard to reproduce. While you should always keep track of and fix flaky tests, a retrying mechanism can help maintain developer productivity by running the test a number of times until it passes.

Retries need to happen at multiple levels to prevent issues, such as:

- Connection to the device timed out or lost connection
- Single test failure

Installing or configuring retries depends on your testing frameworks and infrastructure, but typical mechanisms include:

- A JUnit rule that retries any test a number of times
- A retry*action* or*step*in your CI workflow
- A system to restart an emulator when it's unresponsive, such as Gradle-managed devices.

| **Key Point:** Add retrying mechanisms to big tests, but always fix flaky tests.