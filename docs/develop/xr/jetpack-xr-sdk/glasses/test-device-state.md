---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/test-device-state
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/test-device-state
source: md.txt
---

projectedtestrule, virtual device management

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

It's difficult to automate tests when the code depends on physical hardware. For
example, you might need to manually connect and disconnect the physical device
to verify connection states. With all the [different types](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/support-different-types),
[capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-capabilities), and [device states](https://developer.android.com/develop/xr/jetpack-xr-sdk/ai-glasses/check-availability) of audio glasses and display glasses,
this challenge can become even more complex. To test for this diverse set of
cases, use the [Projected Test Rule](https://developer.android.com/reference/kotlin/androidx/xr/projected/testing/ProjectedTestRule) APIs to automate the setup and
management of a projected test environment. The library handles projected device
creation, connection states, and capability verification, so you can focus on
testing your app's core logic. Use these APIs to build robust test suites
without writing boilerplate code.

## Add library dependencies

To use the test rule, add the testing artifact to your app's `build.gradle`
file:

### Groovy

    dependencies {
    // JXR Projected testing library
    testImplementation "androidx.xr.projected:projected-testing:1.0.0-alpha07"
    }

### Kotlin

    dependencies {
      // JXR Projected testing library
      testImplementation("androidx.xr.projected:projected-testing:1.0.0-alpha07")
    }

## Set up the test rule

To set up the basic test rule, annotate the rule in your test class. By default,
the rule connects a projected device and enables its visual capabilities before
each test is run.


```kotlin
@get:Rule
val projectedTestRule = ProjectedTestRule()

private val context: Context
    get() = ApplicationProvider.getApplicationContext()

@Test
fun testWithConnectedDevice() {
    val projectedContext = ProjectedContext.createProjectedDeviceContext(context)

    assertThat(ProjectedContext.isProjectedDeviceContext(projectedContext)).isTrue()
}
```

<br />

## Test other common scenarios

Now that you've set up your projected test environment with a basic test rule,
test other common scenarios for audio glasses and display glasses to verify your
app's functionality.

### Test device disconnection

To test how your app reacts when the connection with the glasses is lost, use
the `isDeviceConnected` property:


```kotlin
@Test
fun testDeviceDisconnection() {
    // manually disconnect the device via the rule
    projectedTestRule.isDeviceConnected = false

    assertThrows(IllegalStateException::class.java) {
        ProjectedContext.createProjectedDeviceContext(context)
    }
}
```

<br />

### Key points about the code

- The rule resets properties like `isDeviceConnected` to their defaults before every test. You don't need to manually reset these properties in `@After` methods.

### Test different device capabilities

Display glasses can show UIs built with Jetpack Compose Glimmer. By default, the
[`ProjectedTestRule`](https://developer.android.com/reference/kotlin/androidx/xr/projected/testing/ProjectedTestRule) enables `CAPABILITY_VISUAL_UI`. To define exactly what
the projected device supports, use the `capabilities` set. This is useful for
verifying that your app correctly checks for hardware support before attempting
to project content to the glasses.


```kotlin
@Test
fun testAppBehaviorWithoutDisplayCapabilities() = projectedTestRule.launchTestProjectedDeviceActivity { activity ->
    // disable display capability
    projectedTestRule.capabilities = setOf()

    runBlocking {
        // create the controller
        val controller = ProjectedDeviceController.create(activity)

        // verify the app recognizes the lack of visual UI support
        assertThat(controller.capabilities).doesNotContain(ProjectedDeviceController.Capability.CAPABILITY_VISUAL_UI)
    }
}
```

<br />

### Key points about the code

- The rule resets properties like `capabilities` to their defaults before every test. You don't need to manually reset these properties in `@After` methods.
- When you need to verify behavior specifically for an activity that is projected to display glasses, use `launchTestProjectedDeviceActivity`.