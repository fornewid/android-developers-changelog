---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/testing
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/testing
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Audio \&  
Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Augmented reality apps often depend on specific real-world situations to
function. For example, your app might require a detected surface, like a table,
in order to place a virtual game board. To test your app against different
scenarios, use the [ARCore test rule](https://developer.android.com/reference/kotlin/androidx/xr/arcore/testing/ArCoreTestRule) APIs to write tests in a
controlled ARCore test environment. The APIs handle session setup and state, so
you can focus on testing your app's core logic.

## Add library dependencies

To use the ARCore test rule, add these dependencies to your app's `build.gradle`
file:

### Kotlin

```kotlin
dependencies {
    testImplementation("androidx.xr.arcore:arcore-testing:1.0.0-alpha14")
}
```

### Groovy

```groovy
dependencies {
    testImplementation "androidx.xr.arcore:arcore-testing:1.0.0-alpha14"
}
```

If your app depends on [XR SceneCore](https://developer.android.com/jetpack/androidx/releases/xr-scenecore), also include the
[XR SceneCore testing](https://developer.android.com/jetpack/androidx/releases/xr-scenecore#declaring_dependencies) dependency:

### Kotlin

```kotlin
dependencies {
    testImplementation("androidx.xr.scenecore:scenecore-testing:1.0.0-alpha15")
}
```

### Groovy

```groovy
dependencies {
    testImplementation "androidx.xr.scenecore:scenecore-testing:1.0.0-alpha15"
}
```

## Set up the test rule

In your [JUnit test](https://developer.android.com/training/testing/local-tests), use a
[`AndroidJUnit4` test runner](https://developer.android.com/training/testing/local-tests/robolectric) to set up a test:


```kotlin
@Rule @JvmField val arCoreTestRule = ArCoreTestRule()
private lateinit var activityController: ActivityController<ComponentActivity>
private lateinit var activity: ComponentActivity
private lateinit var testDispatcher: TestDispatcher
private lateinit var testScope: TestScope
private lateinit var session: Session

@Before
fun setUp() {
    testDispatcher = StandardTestDispatcher()
    testScope = TestScope(testDispatcher)
    activityController = Robolectric.buildActivity(ComponentActivity::class.java)
    activity = activityController.get()

    // Set up the activity permissions.
    shadowOf(activity.application).grantPermissions(HAND_TRACKING)

    activityController.create().start().resume()

    val sessionCreateResult = Session.create(activity = activity, coroutineContext = testDispatcher)
    session = (sessionCreateResult as SessionCreateSuccess).session

    // Configure the session.
    session.configure(session.config.copy(handTracking = HandTrackingMode.BOTH))
}
```

<br />

In the `@Before` step, set up your testing environment, including required
permissions and session configuration.

## Create test cases

[Create a test case](https://developer.android.com/training/testing/local-tests/robolectric#ui-testing) in order to test a certain scenario. In
this example, we test whether a [hand tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/hands) gesture detector
works with our test data:


```kotlin
@Test
fun test_thumbsUp() = runTest(testDispatcher) {
    arCoreTestRule.rightHand.isVisible = true
    arCoreTestRule.rightHand.handJointMap = gestureThumbsUp
    advanceUntilIdle()
    val handState = Hand.right(session)?.state?.value ?: fail("Did not detect a right hand")

    val isThumbsUp = detectThumbsUp(handState)
    assertThat(isThumbsUp).isTrue()
}
```

<br />

A unit test often contains the following steps:

1. To set up the test, use the [`ArCoreTestRule`](https://developer.android.com/reference/kotlin/androidx/xr/arcore/testing/ArCoreTestRule) to inject test data. This object contains the environment data that your app reads from the session. Use [`TestScope.advanceUntilIdle`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/advance-until-idle.html) to ensure the system is ready to perform the test. In this example, the right hand is enabled, and pose data is used to populate the hand joint data.
2. Then, perform the test. Your app doesn't need special behavior to use the injected data: the `Session` uses data that was injected into the `ArCoreTestRule`.
3. Finally, check the results.

## Additional resources

For more information about testing on Android, consult the following resources:

- [Test apps on Android](https://developer.android.com/training/testing)
- [Fundamentals of testing Android apps](https://developer.android.com/training/testing/fundamentals)