---
title: https://developer.android.com/studio/test/espresso-api
url: https://developer.android.com/studio/test/espresso-api
source: md.txt
---

Use the Espresso Device API to test your app when the device undergoes common
configuration changes, such as rotation and screen unfolding. The Espresso
Device API is the recommended tool for simulating device-level actions
alongside your Jetpack Compose testing rules. If you're new to writing UI tests
for Jetpack Compose, see [Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing).

The Espresso
Device API lets you simulate configuration changes on a virtual device and
executes your tests synchronously, so only one UI action or assertion happens at
a time and your test results are more reliable. If you're new to writing UI
tests with Espresso, see its [documentation](https://developer.android.com/training/testing/espresso).

To use the Espresso Device API, you need the following:

- Android Studio Iguana or higher
- Android Gradle plugin 8.3 or higher
- Android Emulator 33.1.10 or higher
- Android virtual device that runs API level 24 or higher

## Set up your project for the Espresso Device API

To set up your project so it supports the Espresso Device API, do the following:

1. To let the test pass commands to the test device, add the `INTERNET` and
   `ACCESS_NETWORK_STATE` permissions to the manifest file in the
   `androidTest` source set:

         <uses-permission android:name="android.permission.INTERNET" />
         <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

2. Enable the `enableEmulatorControl` experimental flag in the
   `gradle.properties` file:

         android.experimental.androidTest.enableEmulatorControl=true

3. Enable the `emulatorControl` option in the module-level build script:

   ### Kotlin

   ```kotlin
     testOptions {
       emulatorControl {
         enable = true
       }
     }
     
   ```

   ### Groovy

   ```groovy
     testOptions {
       emulatorControl {
         enable = true
       }
     }
     
   ```
4. In the module-level build script, import the Espresso Device library into
   your project:

   ### Kotlin

   ```kotlin
   dependencies {
     androidTestImplementation("androidx.test.espresso:espresso-device:1.0.1")
   }
   ```

   ### Groovy

   ```groovy
   dependencies {
     androidTestImplementation 'androidx.test.espresso:espresso-device:1.0.1'
   }
   ```

## Test against common configuration changes

The Espresso Device API has multiple screen orientation and foldable states that
you can use to simulate device configuration changes. The following examples
show how to trigger these device states and verify the resulting UI changes
using Compose test rules.

### Test against screen rotation

Here's an example of how to test what happens to your app when the device screen
rotates:

1. First, define your Compose test rule and set the device to a consistent
   starting state (like portrait mode):

       import androidx.compose.ui.test.assertIsDisplayed
       import androidx.compose.ui.test.assertDoesNotExist
       import androidx.compose.ui.test.junit4.createComposeRule
       import androidx.compose.ui.test.onNodeWithTag
       import androidx.test.espresso.device.EspressoDevice.onDevice
       import androidx.test.espresso.device.action.ScreenOrientation
       import androidx.test.espresso.device.rules.ScreenOrientationRule
       import org.junit.Rule
       import org.junit.Test

       class MyConfigurationTest {

           // 1. Define the Compose test rule
           @get:Rule
           val composeTestRule = createComposeRule()

           // 2. Define the Espresso Device rule for a consistent starting state
           @get:Rule
           val screenOrientationRule = ScreenOrientationRule(ScreenOrientation.PORTRAIT)
       }

2. Create a test that sets the device to landscape orientation during test
   execution:

       @Test
       fun myRotationTest() {
         ...
         // Sets the device to landscape orientation during test execution.
         onDevice().setScreenOrientation(ScreenOrientation.LANDSCAPE)
         ...
       }

3. After the screen rotates, use `composeTestRule` to check that your
   composables adapt to the new state as expected.

       @Test
       fun myRotationTest() {
         ...
         // Sets the device to landscape orientation during test execution.
         onDevice().setScreenOrientation(ScreenOrientation.LANDSCAPE)
         composeTestRule.onNodeWithTag("NavRail").assertIsDisplayed()
         composeTestRule.onNodeWithTag("BottomBar").assertDoesNotExist()
       }

### Test against screen unfolding

Here's an example of how to test what happens to your app if it's on a foldable
device and the screen unfolds:

1. First, test with the device in the folded state by calling
   `onDevice().setClosedMode()`. Make sure that your composables adapt to the
   compact screen width.

       @Test
       fun myUnfoldedTest() {
         onDevice().setClosedMode()
         composeTestRule.onNodeWithTag("BottomBar").assertIsDisplayed()
         composeTestRule.onNodeWithTag("NavRail").assertDoesNotExist()
         ...
       }

2. To transition to a fully unfolded state, call
   `onDevice().setFlatMode()`. Check that the composables adapt to the
   expanded size class.

       @Test
       fun myUnfoldedTest() {
         onDevice().setClosedMode()
         ...
         onDevice().setFlatMode()
         composeTestRule.onNodeWithTag("NavRail").assertIsDisplayed()
         composeTestRule.onNodeWithTag("BottomBar").assertDoesNotExist()
       }

## Specify what devices your tests need

If you're running a test that performs folding actions on a device that isn't
foldable, the test will likely fail. To execute only the tests that are relevant
to the running device, use the `@RequiresDeviceMode` annotation. The test runner
automatically skips running tests on devices that don't support the
configuration being tested. You can add the device requirement rule to each test
or an entire test class.

For example, to specify that a test should only be run on devices that support
unfolding to a flat configuration, add the following `@RequiresDeviceMode` code
to your test:

    @Test
    @RequiresDeviceMode(mode = FLAT)
    fun myUnfoldedTest() {
      ...
    }