---
title: https://developer.android.com/develop/ui/compose/testing/synchronization
url: https://developer.android.com/develop/ui/compose/testing/synchronization
source: md.txt
---

Compose tests are synchronized by default with your UI. When you call an
assertion or an action with the [`ComposeTestRule`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule), the test is synchronized
beforehand, waiting until the UI tree is idle.

Normally, you don't have to take any action. However, there are some edge cases
you should know about.

When a test is synchronized, your Compose app is advanced in time using a
virtual clock. This means Compose tests don't run in real time, so they can pass
as fast as possible.

However, if you don't use the methods that synchronize your tests, no
recomposition will occur and the UI will appear to be paused.

    @Test
    fun counterTest() {
        val myCounter = mutableStateOf(0) // State that can cause recompositions.
        var lastSeenValue = 0 // Used to track recompositions.
        composeTestRule.setContent {
            Text(myCounter.value.toString())
            lastSeenValue = myCounter.value
        }
        myCounter.value = 1 // The state changes, but there is no recomposition.

        // Fails because nothing triggered a recomposition.
    assertTrue(lastSeenValue == 1)

        // Passes because the assertion triggers recomposition.
        composeTestRule.onNodeWithText("1").assertExists()
    }

Note that this requirement only applies to Compose hierarchies and not to the
rest of the app.

### Disable automatic synchronization

When you call an assertion or action through the `ComposeTestRule` such as
`assertExists()`, your test is synchronized with the Compose UI. In some cases
you might want to stop this synchronization and control the clock yourself. For
example, you can control time to take accurate screenshots of an animation at a
point where the UI would still be busy. To disable automatic synchronization,
set the `autoAdvance` property in the `mainClock` to `false`:

    composeTestRule.mainClock.autoAdvance = false

Typically you will then advance the time yourself. You can advance exactly one
frame with `advanceTimeByFrame()` or by a specific duration with
`advanceTimeBy()`:

    composeTestRule.mainClock.advanceTimeByFrame()
    composeTestRule.mainClock.advanceTimeBy(milliseconds)

| **Note:** [`MainTestClock`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/MainTestClock) is responsible for driving all the recompositions, animations, and gestures. The API doesn't control [Android's measure and draw
| passes](https://developer.android.com/guide/topics/ui/how-android-draws).

### Idle resources

Compose can synchronize tests and the UI so that every action and assertion is
done in an idle state, waiting or advancing the clock as needed. However, some
asynchronous operations whose results affect the UI state can be run in the
background while the test is unaware of them.

Create and register these *idling resources* in your test so that they're taken
into account when deciding whether the app under test is busy or idle. You don't
have to take action unless you need to register additional idling resources, for
example, if you run a background job that is not synchronized with Espresso or
Compose.

This API is very similar to Espresso's [Idling Resources](https://developer.android.com/training/testing/espresso/idling-resource) to indicate whether
the subject under test is idle or busy. Use the Compose test rule to register
the implementation of the [`IdlingResource`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/IdlingResource).

    composeTestRule.registerIdlingResource(idlingResource)
    composeTestRule.unregisterIdlingResource(idlingResource)

### Manual synchronization

In certain cases, you have to synchronize the Compose UI with other parts of
your test or the app you're testing.

The [`waitForIdle()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitForIdle()) function waits for Compose to be idle, but the function
depends on the `autoAdvance` property:

    composeTestRule.mainClock.autoAdvance = true // Default
    composeTestRule.waitForIdle() // Advances the clock until Compose is idle.

    composeTestRule.mainClock.autoAdvance = false
    composeTestRule.waitForIdle() // Only waits for idling resources to become idle.

Note that in both cases, `waitForIdle()` also waits for pending [draw and layout
passes](https://developer.android.com/guide/topics/ui/how-android-draws#:%7E:text=When%20an%20Activity%20receives%20focus,and%20draw%20the%20layout%20tree.).

Also, you can advance the clock until a certain condition is met with
[`advanceTimeUntil()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/MainTestClock#advanceTimeUntil(kotlin.Long,kotlin.Function0)).

    composeTestRule.mainClock.advanceTimeUntil(timeoutMs) { condition }

Note that the given condition should be checking the state that can be affected
by this clock (it only works with Compose state).

### Wait for conditions

Any condition that depends on external work, such as data loading or Android's
measure or draw (that is, measure or draw external to Compose), should use a
more general concept such as [`waitUntil()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitUntil(kotlin.Long,kotlin.Function0)):

    composeTestRule.waitUntil(timeoutMs) { condition }

You can also use any of the
[`waitUntil` helpers](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/junit4/ComposeTestRule#waitUntilAtLeastOneExists(androidx.compose.ui.test.SemanticsMatcher,kotlin.Long)):

    composeTestRule.waitUntilAtLeastOneExists(matcher, timeoutMs)

    composeTestRule.waitUntilDoesNotExist(matcher, timeoutMs)

    composeTestRule.waitUntilExactlyOneExists(matcher, timeoutMs)

    composeTestRule.waitUntilNodeCount(matcher, count, timeoutMs)

| **Warning:** In some cases, using mechanisms in a test like an external `CountDownLatch` instead of the `waitUntil` APIs could behave unexpectedly, since the test clock won't be advanced.

## Additional Resources

- **[Test apps on Android](https://developer.android.com/training/testing)**: The main Android testing landing page provides a broader view of testing fundamentals and techniques.
- **[Fundamentals of testing](https://developer.android.com/training/testing/fundamentals):** Learn more about the core concepts behind testing an Android app.
- **[Local tests](https://developer.android.com/training/testing/local-tests):** You can run some tests locally, on your own workstation.
- **[Instrumented tests](https://developer.android.com/training/testing/instrumented-tests):** It is good practice to also run instrumented tests. That is, tests that run directly on-device.
- **[Continuous integration](https://developer.android.com/training/testing/continuous-integration):** Continuous integration lets you integrate your tests into your deployment pipeline.
- **[Test different screen sizes](https://developer.android.com/training/testing/different-screens):** With some many devices available to users, you should test for different screen sizes.
- **[Espresso](https://developer.android.com/training/testing/espresso)**: While intended for View-based UIs, Espresso knowledge can still be helpful for some aspects of Compose testing.