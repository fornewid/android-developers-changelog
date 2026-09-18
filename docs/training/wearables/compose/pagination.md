---
title: https://developer.android.com/training/wearables/compose/pagination
url: https://developer.android.com/training/wearables/compose/pagination
source: md.txt
---

Paging lets users swipe horizontally or vertically between distinct, full-screen
pages on Wear OS devices. Common use cases include swiping between workout
metrics and media controls in an exercise app, or stepping through multi-page
flows.

In Compose for Wear OS Material 3, [`HorizontalPagerScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/HorizontalPagerScaffold.composable) and
[`VerticalPagerScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/VerticalPagerScaffold.composable) coordinate the pager layout, automatically
positioning the page indicator and managing transitions with [`TimeText`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/TimeText.composable).
Each page is wrapped in an [`AnimatedPage`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/AnimatedPage.composable) composable, which applies
scaling, rounded corner morphing, and scrim effects as pages transition across
the round display.

The following animation shows how `HorizontalPagerScaffold` and `AnimatedPage`
scale and animate pages during horizontal swipes:

## Scaffold hierarchy for paging

When designing paginated screen layouts in Material 3---whether swiping
left or right (`HorizontalPager`) or up or down (`VerticalPager`)---use the
following component hierarchy from outer container to inner content:

1. **[`AppScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/AppScaffold.composable)** : The outermost container at the root of your app (use only one per app). It anchors the global `TimeText` overlay so that the clock remains stationary at the top of the screen during page transitions and swipe-to-dismiss gestures.
2. **[`HorizontalPagerScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/HorizontalPagerScaffold.composable) or [`VerticalPagerScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/VerticalPagerScaffold.composable)** : Placed inside `AppScaffold` at the pager level. It coordinates transitions between `TimeText` and the `HorizontalPageIndicator` or `VerticalPageIndicator`.
3. **[`HorizontalPager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/pager/package-summary#HorizontalPager(androidx.wear.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.wear.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,kotlin.Function2)) or [`VerticalPager`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/pager/package-summary#VerticalPager(androidx.wear.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.wear.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,kotlin.Function2))** : The foundation pager container that manages swipe gestures, fling physics, and rotary input snapping using a shared `PagerState`.
4. **[`AnimatedPage`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/AnimatedPage.composable)** : Placed inside the pager's page content lambda. It wraps each individual page to apply Material 3 transition animations (scaling and scrim effects) based on the page's offset in `PagerState`.
5. **[`ScreenScaffold`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/ScreenScaffold.composable)** : Placed *inside* `AnimatedPage` for each individual page. Because each page can contain its own vertically scrollable list (such as a [`TransformingLazyColumn`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/lazy/package-summary#TransformingLazyColumn(androidx.compose.ui.Modifier,androidx.compose.foundation.lazy.TransformingLazyColumnState,androidx.compose.foundation.layout.PaddingValues,kotlin.Boolean,androidx.compose.foundation.layout.Arrangement.Vertical,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Boolean,androidx.wear.compose.foundation.rotary.RotaryScrollableBehavior,androidx.compose.foundation.OverscrollEffect,kotlin.Function1))) or its own [`EdgeButton`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/EdgeButton.composable), nesting `ScreenScaffold` inside each page ensures that vertical scroll indicators, edge buttons, and `contentPadding` belong to that specific page and animate smoothly with it.

    AppScaffold (1 per app: anchors global TimeText)
     └── HorizontalPagerScaffold / VerticalPagerScaffold (manages PageIndicator)
          └── HorizontalPager / VerticalPager (manages PagerState & fling behavior)
               └── AnimatedPage (applies scaling & scrim transitions per page)
                    └── ScreenScaffold (1 per page: ScrollIndicator & EdgeButton)
                         └── Page Content (Column or TransformingLazyColumn)

> [!WARNING]
> **Warning:** Always pass the `contentPadding` provided by `ScreenScaffold` to your page's content container (such as `TransformingLazyColumn`) to prevent content from clipping on circular displays.

## Implement a horizontal pager

To implement a horizontal pager in Material 3, nest `HorizontalPagerScaffold`,
`HorizontalPager`, `AnimatedPage`, and `ScreenScaffold` inside your app's
`AppScaffold`.

Use [`PagerScaffoldDefaults.snapWithSpringFlingBehavior`](https://developer.android.com/reference/kotlin/androidx/wear/compose/material3/PagerScaffoldDefaults#snapWithSpringFlingBehavior(androidx.wear.compose.foundation.pager.PagerState)) for
`flingBehavior` to apply Material 3 spring motion physics and responsive page
snapping (`HighSnapPositionalThreshold`). By default, `HorizontalPager` disables
rotary page scrolling (`rotaryScrollableBehavior = null`), allowing rotating
crown or bezel input to scroll vertical lists (such as a
`TransformingLazyColumn`) inside the active page.

The following sample demonstrates a complete `HorizontalPagerScaffold` setup:

```kotlin
@Composable
fun HorizontalPagerScaffoldSample(navigateBack: () -> Unit) {
    AppScaffold {
        val pagerState = rememberPagerState(pageCount = { 10 })

        HorizontalPagerScaffold(pagerState = pagerState) {
            HorizontalPager(
                state = pagerState,
                flingBehavior =
                    PagerScaffoldDefaults.snapWithSpringFlingBehavior(
                        state = pagerState
                    ),
            ) { page ->
                AnimatedPage(pageIndex = page, pagerState = pagerState) {
                    ScreenScaffold {
                        Column(
                            modifier = Modifier.fillMaxSize(),
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.Center,
                        ) {
                            Text(text = "Page #$page")
                            Spacer(modifier = Modifier.height(8.dp))
                            Text(text = "Swipe left and right")
                            if (page == 0) {
                                Spacer(modifier = Modifier.height(16.dp))
                                Button(onClick = navigateBack) { Text("Exit") }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

If a page inside your horizontal pager contains a `TransformingLazyColumn`,
create a separate `rememberTransformingLazyColumnState()` inside that page's
scope and pass it to the inner `ScreenScaffold` and `TransformingLazyColumn`:

```kotlin
AppScaffold {
    val pagerState = rememberPagerState(pageCount = { 10 })

    HorizontalPagerScaffold(pagerState = pagerState) {
        HorizontalPager(
            state = pagerState,
            flingBehavior =
                PagerScaffoldDefaults.snapWithSpringFlingBehavior(
                    state = pagerState
                ),
        ) { page ->
            AnimatedPage(pageIndex = page, pagerState = pagerState) {
                val columnState = rememberTransformingLazyColumnState()
                val transformationSpec = rememberTransformationSpec()

                ScreenScaffold(
                    scrollState = columnState,
                ) { contentPadding ->
                    TransformingLazyColumn(
                        state = columnState,
                        contentPadding = contentPadding,
                    ) {
                        item {
                            ListHeader(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .transformedHeight(this, transformationSpec)
                                    .minimumVerticalContentPadding(
                                        ListHeaderDefaults.minimumTopListContentPadding
                                    ),
                                transformation = SurfaceTransformation(transformationSpec),
                            ) {
                                Text(text = "Pager sample")
                            }
                        }
                        item {
                            Card(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .transformedHeight(this, transformationSpec)
                                    .minimumVerticalContentPadding(
                                        CardDefaults.minimumVerticalListContentPadding
                                    ),
                                transformation = SurfaceTransformation(transformationSpec),
                            ) {
                                if (page == 0) {
                                    Text(text = "Page #$page. Swipe right")
                                } else {
                                    Text(text = "Page #$page. Swipe left and right")
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Implement a vertical pager

A vertical pager lets users swipe up and down between pages or step through them
using the watch's rotating side button or bezel.

Unlike `HorizontalPager`, `VerticalPager` enables rotary page snapping by
default (`RotaryScrollableDefaults.snapBehavior(state)`). Pass
`PagerScaffoldDefaults.snapWithSpringFlingBehavior` to `flingBehavior` and wrap
each page in `AnimatedPage` and `ScreenScaffold`:

```kotlin
@Composable
fun VerticalPagerScaffoldSample() {
    AppScaffold {
        val pagerState = rememberPagerState(pageCount = { 10 })

        VerticalPagerScaffold(pagerState = pagerState) {
            VerticalPager(
                state = pagerState,
                flingBehavior =
                    PagerScaffoldDefaults.snapWithSpringFlingBehavior(
                        state = pagerState
                    ),
            ) { page ->
                AnimatedPage(pageIndex = page, pagerState = pagerState) {
                    ScreenScaffold {
                        Column(
                            modifier = Modifier.fillMaxSize(),
                            horizontalAlignment = Alignment.CenterHorizontally,
                            verticalArrangement = Arrangement.Center,
                        ) {
                            Text(text = "Page #$page")
                            Spacer(modifier = Modifier.height(8.dp))
                            Text(text = "Swipe up and down")
                        }
                    }
                }
            }
        }
    }
}
```

## Customize pager behavior

You can customize the snapping sensitivity of `HorizontalPagerScaffold` and
`VerticalPagerScaffold` to match your app's interaction needs.

### Adjust snap sensitivity for workouts

During workouts or high-motion activities where the user's gross motor control
is limited, accidental touches or slight crown rotations can unintentionally
switch pages. For these screens, configure your pager with low snap sensitivity:

- Pass [`PagerDefaults.snapFlingBehavior`](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/pager/PagerDefaults#snapFlingBehavior(androidx.wear.compose.foundation.pager.PagerState,kotlin.Int,androidx.compose.animation.core.DecayAnimationSpec,androidx.compose.animation.core.AnimationSpec,kotlin.Float)) with `maxFlingPages = 0` and `snapPositionalThreshold = PagerScaffoldDefaults.LowSnapPositionalThreshold` so a deliberate drag across a larger portion of the screen is required to turn the page.
- If you enable rotary page snapping, set `snapSensitivity = RotaryScrollableDefaults.LowSnapSensitivity` in `RotaryScrollableDefaults.snapBehavior` to require more rotation before snapping to the next page.

```kotlin
@Composable
fun HorizontalPagerScaffoldWithLowSensitivitySample(navigateBack: () -> Unit) {
    AppScaffold {
        val pagerState = rememberPagerState(pageCount = { 3 })

        HorizontalPagerScaffold(pagerState = pagerState) {
            HorizontalPager(
                state = pagerState,
                flingBehavior =
                    PagerDefaults.snapFlingBehavior(
                        state = pagerState,
                        maxFlingPages = 0,
                        snapPositionalThreshold =
                            PagerScaffoldDefaults.LowSnapPositionalThreshold,
                    ),
                rotaryScrollableBehavior =
                    RotaryScrollableDefaults.snapBehavior(
                        pagerState = pagerState,
                        snapSensitivity =
                            RotaryScrollableDefaults.LowSnapSensitivity,
                    ),
            ) { page ->
                AnimatedPage(pageIndex = page, pagerState = pagerState) {
                    ScreenScaffold {
                        // Page content
                    }
                }
            }
        }
    }
}
```

For full sample implementations, see [`Pager.kt`](https://github.com/android/snippets/blob/main/wear/src/main/java/com/example/wear/snippets/m3/pager/Pager.kt) in the `android/snippets`
repository and [`PagerScaffoldSample.kt`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:wear/compose/compose-material3/samples/src/main/java/androidx/wear/compose/material3/samples/PagerScaffoldSample.kt) in the AndroidX repository.