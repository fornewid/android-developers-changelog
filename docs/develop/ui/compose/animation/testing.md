---
title: https://developer.android.com/develop/ui/compose/animation/testing
url: https://developer.android.com/develop/ui/compose/animation/testing
source: md.txt
---

Compose offers `ComposeTestRule` that allows you to write tests for animations
in a deterministic manner with full control over the test clock. This allows you
to verify intermediate animation values. In addition, a test can run quicker
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

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Testing your Compose layout](https://developer.android.com/develop/ui/compose/testing)
- [Other considerations](https://developer.android.com/develop/ui/compose/migrate/other-considerations)
- [Customize animations {:#customize-animations}](https://developer.android.com/develop/ui/compose/animation/customize)