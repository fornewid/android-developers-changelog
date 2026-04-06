---
title: Test animations  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/animation/testing
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Test animations Stay organized with collections Save and categorize content based on your preferences.




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

```
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

AnimationTestingSnippets.kt
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Testing your Compose layout](/develop/ui/compose/testing)
* [Other considerations](/develop/ui/compose/migrate/other-considerations)
* [Customize animations {:#customize-animations}](/develop/ui/compose/animation/customize)

[Previous

arrow\_back

Customize animations](/develop/ui/compose/animation/customize)

[Next

Tools

arrow\_forward](/develop/ui/compose/animation/tooling)