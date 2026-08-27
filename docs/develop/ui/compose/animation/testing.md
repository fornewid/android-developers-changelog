---
title: https://developer.android.com/develop/ui/compose/animation/testing
url: https://developer.android.com/develop/ui/compose/animation/testing
source: md.txt
---

Compose offers `ComposeTestRule` that lets you write tests for animations
in a deterministic manner with full control over the test clock. This lets you
verify intermediate animation values. In addition, a test can run quicker
than the actual duration of the animation.

`ComposeTestRule` exposes its test clock as `mainClock`. You can set the
`autoAdvance` property to false to control the clock in your test code. After
initiating the animation you want to test, the clock can be moved forward with
`advanceTimeBy`.

One thing to note here is that `advanceTimeBy` doesn't move the clock exactly by
the specified duration. Rather, it rounds it up to the nearest duration that is
a multiplier of the frame duration.


```kotlin
@get:Rule
val rule = createComposeRule()

@Test
fun testAnimationWithClock() {
    // Pause animations
    rule.mainClock.autoAdvance = false
    var enabled by mutableStateOf(false)
    rule.setContent {
        val color by animateColorAsState(
            targetValue = if (enabled) Color.Red else Color.Green,
            animationSpec = tween(durationMillis = 250)
        )
        Box(Modifier.size(64.dp).background(color))
    }

    // Initiate the animation.
    enabled = true

    // Let the animation proceed.
    rule.mainClock.advanceTimeBy(50L)

    // Compare the result with the image showing the expected result.
    // `assertAgainGolden` needs to be implemented in your code.
    rule.onRoot().captureToImage().assertAgainstGolden()
}
```

<br />

## Optimize animation tests

> [!NOTE]
> **Note:** The `runWithoutImplicitWait` API is included in [`androidx.compose.ui:ui-test-junit4:1.12.0-alpha03+`](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.0-alpha03) and [`androidx.compose.ui:ui-test:1.12.0-alpha03+`](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.12.0-alpha03).

When testing high-fidelity animations, you often need to disable auto-advance
and manually step through frames to assert intermediate UI states. For these
specific frame-by-frame loops, use the [`runWithoutImplicitWait`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#runWithoutImplicitWait(kotlin.Function0)) method to
execute your assertions. Standard node queries (like [`onNodeWithTag`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteractionsProvider#(androidx.compose.ui.test.SemanticsNodeInteractionsProvider).onNodeWithTag(kotlin.String,kotlin.Boolean)) or
[`fetchSemanticsNode`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/SemanticsNodeInteraction#fetchSemanticsNode(kotlin.String)))) trigger implicit synchronizations that are redundant
when you are manually controlling the clock, so bypassing them significantly
speeds up your test runtimes.

> [!NOTE]
> **Note:** This API is a specialized performance optimization designed strictly for manual frame-by-frame animation testing. It is not intended for general-purpose UI tests and won't provide meaningful performance improvements outside of manual clock advancement loops.

#### Usage guidelines

- **Manual clock management** : Use this API when [`mainClock.autoAdvance`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/MainTestClock#autoAdvance()) is set to `false` and the UI is in a known, stable state for the current frame.
- **UI thread execution** : To ensure the stability of the UI tree, call [`runWithoutImplicitWait`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#runWithoutImplicitWait(kotlin.Function0)) on the UI thread, such as with [`runOnUiThread`](https://developer.android.com/reference/kotlin/androidx/compose/ui/test/ComposeUiTest#runOnUiThread(kotlin.Function0)). Running it off the UI thread exposes your test to race conditions and stale state reads.
- **Read-only assertions**: The block should strictly contain read-only assertions. Any actions that mutate state should be performed outside of this block.

#### Example


```kotlin
@Test
fun runWithoutImplicitWaitSample() = runComposeUiTest {
    setContent { MainScreen() }
    mainClock.autoAdvance = false

    // Trigger an animation
    onNodeWithText("Start Animation").performClick()

    // Step through the animation frame-by-frame
    while (hasPendingWork()) {
        mainClock.advanceTimeByFrame()
        waitForIdle()
        runOnUiThread {
            // Suppress implicit synchronization inside this block to avoid redundant
            // waits on each node query, making the frame assertions execute much faster.
            runWithoutImplicitWait {
                val box1 = onNodeWithTag("Box1").fetchSemanticsNode()
                val box2 = onNodeWithTag("Box2").fetchSemanticsNode()
                val box3 = onNodeWithTag("Box3").fetchSemanticsNode()

                // Assert the exact intermediate state of all three properties for this frame
                assert(box1.boundsInRoot.right <= box2.boundsInRoot.left)
                assert(box2.boundsInRoot.right <= box3.boundsInRoot.left)
            }
        }
    }
}
```

<br />

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing)
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)
- [Customize animations](https://developer.android.com/develop/ui/compose/animation/customize)