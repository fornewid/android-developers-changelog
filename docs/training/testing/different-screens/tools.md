---
title: https://developer.android.com/training/testing/different-screens/tools
url: https://developer.android.com/training/testing/different-screens/tools
source: md.txt
---

Android provides a variety of tools and APIs that can help you create tests for
different screen and window sizes.

### DeviceConfigurationOverride

The [`DeviceConfigurationOverride`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/DeviceConfigurationOverride) composable lets you override
configuration attributes to test multiple screen and window sizes in Compose
layouts. The [`ForcedSize`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/DeviceConfigurationOverride.Companion#(androidx.compose.ui.test.DeviceConfigurationOverride.Companion).ForcedSize(androidx.compose.ui.unit.DpSize) override fits any layout in the available space,
which lets you to run any
UI test on any screen size. For example, you can use a small phone form factor
to run all your UI tests, including UI tests for big phones, foldables, and
tablets.  

       DeviceConfigurationOverride(
            DeviceConfigurationOverride.ForcedSize(DpSize(1280.dp, 800.dp))
        ) {
            MyScreen() // Will be rendered in the space for 1280dp by 800dp without clipping.
        }

![](https://developer.android.com/static/images/training/testing/different-screens/nia_DeviceConfigurationOverride.png) **Figure 1.** Using DeviceConfigurationOverride to fit a tablet layout inside a smaller form factor device, as in \\\*Now in Android\*.

Additionally, you can use this composable to set font scale, themes, and other
properties that you might want to test on different window sizes.

## Robolectric

Use [Robolectric](https://robolectric.org/) to run Compose or view-based UI tests on the JVM
[locally](https://developer.android.com/training/testing/local-tests)---no devices or emulators required. You can [configure](https://robolectric.org/device-configuration/)
Robolectric to use specific screen sizes, among other useful properties.

In the following [example](https://github.com/android/nowinandroid/blob/main/app/src/testDemo/kotlin/com/google/samples/apps/nowinandroid/ui/NiaAppScreenSizesScreenshotTests.kt) from *Now in Android*, Robolectric is configured
to emulate a screen size of 1000x1000 dp with a resolution of 480 dpi:  

    @RunWith(RobolectricTestRunner::class)
    // Configure Robolectric to use a very large screen size that can fit all of the test sizes.
    // This allows enough room to render the content under test without clipping or scaling.
    @Config(qualifiers = "w1000dp-h1000dp-480dpi")
    class NiaAppScreenSizesScreenshotTests { ... }

You can also set the qualifiers from the test body as done in this snippet from
the [*Now in Android*](https://github.com/android/nowinandroid/blob/main/core/testing/src/main/kotlin/com/google/samples/apps/nowinandroid/core/testing/util/ScreenshotHelper.kt#L61) example:  

    val (width, height, dpi) = ...

    // Set qualifiers from specs.
    RuntimeEnvironment.setQualifiers("w${width}dp-h${height}dp-${dpi}dpi")

Note that `RuntimeEnvironment.setQualifiers()` updates the system and
application resources with the new configuration but does not trigger any action
on active activities or other components.

You can read more in the Robolectric [Device Configuration](https://robolectric.org/device-configuration/) documentation.

## Gradle-managed devices

The [Gradle-managed devices](https://developer.android.com/studio/test/gradle-managed-devices) (GMD) Android Gradle plugin
lets you define the specifications of the emulators and real devices where
your [instrumented](https://developer.android.com/training/testing/instrumented-tests) tests run. Create specifications for devices with
different screen sizes to implement a testing strategy where certain tests must
be run on certain screen sizes. By using GMD with [Continuous Integration](https://developer.android.com/training/testing/continuous-integration)
(CI), you can make sure that the appropriate tests run when required,
provisioning and launching emulators and simplifying your CI setup.  

    android {
        testOptions {
            managedDevices {
                devices {
                    // Run with ./gradlew nexusOneApi30DebugAndroidTest.
                    nexusOneApi30(com.android.build.api.dsl.ManagedVirtualDevice) {
                        device = "Nexus One"
                        apiLevel = 30
                        // Use the AOSP ATD image for better emulator performance
                        systemImageSource = "aosp-atd"
                    }
                    // Run with ./gradlew  foldApi34DebugAndroidTest.
                    foldApi34(com.android.build.api.dsl.ManagedVirtualDevice) {
                        device = "Pixel Fold"
                        apiLevel = 34
                        systemImageSource = "aosp-atd"
                    }
                }
            }
        }
    }

You can find multiple examples of GMD in the [testing-samples](https://github.com/android/testing-samples/blob/main/ui/espresso/BasicSample/app/build.gradle) project.

## Firebase Test Lab

Use [Firebase Test Lab](https://firebase.google.com/docs/test-lab) (FTL), or a similar device farm service, to run your
tests on specific real devices that you might not have access to, such as
foldables or tablets of varying sizes. Firebase Test Lab is a [paid
service with a free tier](https://firebase.google.com/docs/test-lab/usage-quotas-pricing). FTL also supports running tests on emulators.
These services improve the reliability and speed of instrumented testing because
they can provision devices and emulators ahead of time.

For information about using FTL with GMD, see [Scale your tests with
Gradle-managed devices](https://developer.android.com/studio/test/gradle-managed-devices).

## Test filtering with the test runner

An optimal test strategy shouldn't verify the same thing twice, so most of your
UI tests don't need to run on multiple devices. Typically, you filter your UI
tests by running all or most of them on a phone form factor and only a subset on
devices with different screen sizes.

You can annotate certain tests to be run only with certain devices and then pass
an argument to the [AndroidJUnitRunner](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner) using the command that runs the
tests.

For example, you can create different annotations:  

    annotation class TestExpandedWidth
    annotation class TestCompactWidth

And use them on different tests:  

    class MyTestClass {

        @Test
        @TestExpandedWidth
        fun myExample_worksOnTablet() {
            ...
        }

        @Test
        @TestCompactWidth
        fun myExample_worksOnPortraitPhone() {
            ...
        }

    }

You can then use the `android.testInstrumentationRunnerArguments.annotation`
property when running the tests to filter specific ones. For example, if you're
using Gradle-managed devices:  

    $ ./gradlew pixelTabletApi30DebugAndroidTest -Pandroid.testInstrumentationRunnerArguments.annotation='com.sample.TestExpandedWidth'

If you don't use GMD and you manage emulators on CI, first make sure that the
correct emulator or device is ready and connected, and then pass the parameter
to one of the Gradle commands to run instrumented tests:  

    $ ./gradlew connectedAndroidTest -Pandroid.testInstrumentationRunnerArguments.annotation='com.sample.TestExpandedWidth'

Note that Espresso Device (see next section) can also filter tests by using
device properties.

## Espresso Device

Use [Espresso Device](https://developer.android.com/reference/androidx/test/espresso/device/package-summary) to perform actions on emulators in tests using any
type of instrumented tests, including Espresso, Compose, or UI Automator tests.
These actions might include setting the screen size or toggling foldable states
or postures. For example, you can control a foldable emulator and set it to
tabletop mode. Espresso Device also contains JUnit rules and annotations to
require certain features:  

    @RunWith(AndroidJUnit4::class)
    class OnDeviceTest {

        @get:Rule(order=1) val activityScenarioRule = activityScenarioRule<MainActivity>()

        @get:Rule(order=2) val screenOrientationRule: ScreenOrientationRule =
            ScreenOrientationRule(ScreenOrientation.PORTRAIT)

        @Test
        fun tabletopMode_playerIsDisplayed() {
            // Set the device to tabletop mode.
            onDevice().setTabletopMode()
            onView(withId(R.id.player)).check(matches(isDisplayed()))
        }
    }

Note that [Espresso Device](https://developer.android.com/reference/androidx/test/espresso/device/package-summary) is still in alpha stage and has the following
requirements:

- Android Gradle Plugin 8.3 or higher
- Android Emulator 33.1.10 or higher
- Android virtual device that runs API level 24 or higher

### Filter tests

Espresso Device can read the properties of connected devices to enable you to
filter tests using [annotations](https://developer.android.com/reference/androidx/test/espresso/device/filter/package-summary). If the annotated requirements are not met,
the tests are skipped.

#### RequiresDeviceMode annotation

The [`RequiresDeviceMode`](https://developer.android.com/reference/androidx/test/espresso/device/filter/RequiresDeviceMode) annotation can be used multiple times to indicate
a test that will run only if *all* the [`DeviceMode`](https://developer.android.com/reference/androidx/test/espresso/device/controller/DeviceMode) values are supported
on the device.  

    class OnDeviceTest {
        ...
        @Test
        @RequiresDeviceMode(TABLETOP)
        @RequiresDeviceMode(BOOK)
        fun tabletopMode_playerIdDisplayed() {
            // Set the device to tabletop mode.
            onDevice().setTabletopMode()
            onView(withId(R.id.player)).check(matches(isDisplayed()))
        }
    }

#### RequiresDisplay annotation

The [`RequiresDisplay`](https://developer.android.com/reference/androidx/test/espresso/device/filter/RequiresDisplay) annotation lets you specify the width and height of
the device screen using [size classes](https://developer.android.com/reference/androidx/test/espresso/device/sizeclass/package-summary), which define dimension buckets
following the official [window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/window-size-classes).  

    class OnDeviceTest {
        ...
        @Test
        @RequiresDisplay(EXPANDED, COMPACT)
        fun myScreen_expandedWidthCompactHeight() {
            ...
        }
    }

### Resize displays

Use the [`setDisplaySize()`](https://developer.android.com/reference/androidx/test/espresso/device/action/DeviceActions#setDisplaySize(androidx.test.espresso.device.sizeclass.WidthSizeClass,androidx.test.espresso.device.sizeclass.HeightSizeClass)) method to resize the dimensions of the screen
at runtime. Use the method in conjunction with the [`DisplaySizeRule`](https://developer.android.com/reference/androidx/test/espresso/device/rules/DisplaySizeRule)
class, which makes sure that any changes made during tests are undone before the
next test.  

    @RunWith(AndroidJUnit4::class)
    class ResizeDisplayTest {

        @get:Rule(order = 1) val activityScenarioRule = activityScenarioRule<MainActivity>()

        // Test rule for restoring device to its starting display size when a test case finishes.
        @get:Rule(order = 2) val displaySizeRule: DisplaySizeRule = DisplaySizeRule()

        @Test
        fun resizeWindow_compact() {
            onDevice().setDisplaySize(
                widthSizeClass = WidthSizeClass.COMPACT,
                heightSizeClass = HeightSizeClass.COMPACT
            )
            // Verify visual attributes or state restoration.
        }
    }

When you resize a display with `setDisplaySize()`, you don't affect the density
of the device, so if a dimension doesn't fit in the target device, the test
fails with an [`UnsupportedDeviceOperationException`](https://developer.android.com/reference/java/lang/UnsupportedOperationException). To prevent tests from
being run in this case, use the `RequiresDisplay` annotation to filter them out:  

    @RunWith(AndroidJUnit4::class)
    class ResizeDisplayTest {

        @get:Rule(order = 1) var activityScenarioRule = activityScenarioRule<MainActivity>()

        // Test rule for restoring device to its starting display size when a test case finishes.
        @get:Rule(order = 2) var displaySizeRule: DisplaySizeRule = DisplaySizeRule()

        /**
         * Setting the display size to EXPANDED would fail in small devices, so the [RequiresDisplay]
         * annotation prevents this test from being run on devices outside the EXPANDED buckets.
         */
        @RequiresDisplay(
            widthSizeClass = WidthSizeClassEnum.EXPANDED,
            heightSizeClass = HeightSizeClassEnum.EXPANDED
        )
        @Test
        fun resizeWindow_expanded() {
            onDevice().setDisplaySize(
                widthSizeClass = WidthSizeClass.EXPANDED,
                heightSizeClass = HeightSizeClass.EXPANDED
            )
            // Verify visual attributes or state restoration.
        }
    }

## StateRestorationTester

The [`StateRestorationTester`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/StateRestorationTester) class is used to test the state restoration
for composable components without recreating activities. This makes tests faster
and more reliable, as activity recreation is a complex process with multiple
synchronization mechanisms:  

    @Test
    fun compactDevice_selectedEmailEmailRetained_afterConfigChange() {
        val stateRestorationTester = StateRestorationTester(composeTestRule)

        // Set content through the StateRestorationTester object.
        stateRestorationTester.setContent {
            MyApp()
        }

        // Simulate a config change.
        stateRestorationTester.emulateSavedInstanceStateRestore()
    }

## Window Testing library

The Window Testing library contains utilities to help you write tests that rely
on or verify features related to window management, such as [activity
embedding](https://developer.android.com/develop/ui/views/layout/activity-embedding) or foldable features. The artifact is available through [Google's
Maven Repository](https://maven.google.com/web/index.html?q=window-testing#androidx.window:window-testing).

For example, you can use the [`FoldingFeature()`](https://developer.android.com/reference/kotlin/androidx/window/testing/layout/package-summary#FoldingFeature(android.app.Activity,kotlin.Int,kotlin.Int,androidx.window.layout.FoldingFeature.State,androidx.window.layout.FoldingFeature.Orientation)) function to generate a
custom [`FoldingFeature`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature), which you can use in Compose previews. In Java,
use the [`createFoldingFeature()`](https://developer.android.com/reference/androidx/window/testing/layout/DisplayFeatureTesting#createFoldingFeature(android.app.Activity,kotlin.Int,kotlin.Int,androidx.window.layout.FoldingFeature.State,androidx.window.layout.FoldingFeature.Orientation)) function.

In a Compose preview, you might implement `FoldingFeature` in the following way:  

    @Preview(showBackground = true, widthDp = 480, heightDp = 480)
    @Composable private fun FoldablePreview() =
        MyApplicationTheme {
            ExampleScreen(
                displayFeatures = listOf(FoldingFeature(Rect(0, 240, 480, 240)))
            )
     }

Also, you can emulate display features in UI tests using the
[`TestWindowLayoutInfo()`](https://developer.android.com/reference/kotlin/androidx/window/testing/layout/package-summary#TestWindowLayoutInfo(kotlin.collections.List)) function.
The following example simulates a `FoldingFeature` with a
[`HALF_OPENED`](https://developer.android.com/reference/kotlin/androidx/window/layout/FoldingFeature.State#HALF_OPENED())
vertical hinge in the screen's center, then checks whether the
layout is the one expected:  

### Compose

    import androidx.window.layout.FoldingFeature.Orientation.Companion.VERTICAL
    import androidx.window.layout.FoldingFeature.State.Companion.HALF_OPENED
    import androidx.window.testing.layout.FoldingFeature
    import androidx.window.testing.layout.TestWindowLayoutInfo
    import androidx.window.testing.layout.WindowLayoutInfoPublisherRule

    @RunWith(AndroidJUnit4::class)
    class MediaControlsFoldingFeatureTest {

        @get:Rule(order=1)
        val composeTestRule = createAndroidComposeRule<ComponentActivity>()

        @get:Rule(order=2)
        val windowLayoutInfoPublisherRule = WindowLayoutInfoPublisherRule()

        @Test
        fun foldedWithHinge_foldableUiDisplayed() {
            composeTestRule.setContent {
                MediaPlayerScreen()
            }

            val hinge = FoldingFeature(
                activity = composeTestRule.activity,
                state = HALF_OPENED,
                orientation = VERTICAL,
                size = 2
            )

            val expected = TestWindowLayoutInfo(listOf(hinge))
            windowLayoutInfoPublisherRule.overrideWindowLayoutInfo(expected)

            composeTestRule.waitForIdle()

            // Verify that the folding feature is detected and media controls shown.
            composeTestRule.onNodeWithTag("MEDIA_CONTROLS").assertExists()
        }
    }

### Views

    import androidx.window.layout.FoldingFeature.Orientation
    import androidx.window.layout.FoldingFeature.State
    import androidx.window.testing.layout.FoldingFeature
    import androidx.window.testing.layout.TestWindowLayoutInfo
    import androidx.window.testing.layout.WindowLayoutInfoPublisherRule

    @RunWith(AndroidJUnit4::class)
    class MediaControlsFoldingFeatureTest {

        @get:Rule(order=1)
        val activityRule = ActivityScenarioRule(MediaPlayerActivity::class.java)

        @get:Rule(order=2)
        val windowLayoutInfoPublisherRule = WindowLayoutInfoPublisherRule()

        @Test
        fun foldedWithHinge_foldableUiDisplayed() {
            activityRule.scenario.onActivity { activity ->
                val feature = FoldingFeature(
                    activity = activity,
                    state = State.HALF_OPENED,
                    orientation = Orientation.VERTICAL)
                val expected = TestWindowLayoutInfo(listOf(feature))
                windowLayoutInfoPublisherRule.overrideWindowLayoutInfo(expected)
            }

            // Verify that the folding feature is detected and media controls shown.
            onView(withId(R.id.media_controls)).check(matches(isDisplayed()))
        }
    }

| **Note:** This test must run on a display large enough to lay out the elements on screen as expected.

You can find more samples in the [WindowManager project](https://github.com/android/platform-samples/tree/main/samples/user-interface/windowmanager/src/main/java/com/example/platform/ui/windowmanager).

## Additional resources

Documentation

- [Large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality)
- [Test apps on Android](https://developer.android.com/training/testing)
- [Testing your Compose layout](https://developer.android.com/jetpack/compose/testing)

Samples

- [WindowManager sample](https://github.com/android/platform-samples/tree/main/samples/user-interface/windowmanager/src/main/java/com/example/platform/ui/windowmanager)
- [Espresso Device samples](https://github.com/android/testing-samples/tree/main/ui/espresso/EspressoDeviceSample)
- [Now In Android](https://github.com/android/nowinandroid)
  - Uses screenshot testing to verify different screen sizes

Codelabs

- [Support foldable and dual-screen devices with Jetpack WindowManager](https://developer.android.com/codelabs/android-window-manager-dual-screen-foldables)