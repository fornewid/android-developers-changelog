---
title: https://developer.android.com/develop/ui/compose/layouts/pager
url: https://developer.android.com/develop/ui/compose/layouts/pager
source: md.txt
---

[Video](https://www.youtube.com/watch?v=V2Ke-JJDnrU)

To flip through content horizontally or vertically, you can use the
[`HorizontalPager`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.foundation.pager.PagerState,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function1)) and [`VerticalPager`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#VerticalPager(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.foundation.pager.PagerState,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Horizontal,androidx.compose.foundation.gestures.snapping.SnapFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,kotlin.Function1)) composables. These have
similar functions to [`ViewPager`](https://developer.android.com/reference/kotlin/androidx/viewpager/widget/ViewPager) in the view system. By default,
`HorizontalPager` takes up the full screen width and `VerticalPager` takes up
the full height. The pagers also only fling one page at a time. All of these
defaults are configurable.

## HorizontalPager

To create a pager that scrolls horizontally left and right, use
`HorizontalPager`:
**Figure 1** . Demo of `HorizontalPager`


```kotlin
// Display 10 items
val pagerState = rememberPagerState(pageCount = {
    10
})
HorizontalPager(state = pagerState) { page ->
    // Our page content
    Text(
        text = "Page: $page",
        modifier = Modifier.fillMaxWidth()
    )
}
```

<br />

## VerticalPager

To create a pager that scrolls up and down, use `VerticalPager`:
**Figure 2** . Demo of `VerticalPager`

<br />


```kotlin
// Display 10 items
val pagerState = rememberPagerState(pageCount = {
    10
})
VerticalPager(state = pagerState) { page ->
    // Our page content
    Text(
        text = "Page: $page",
        modifier = Modifier.fillMaxWidth()
    )
}
```

<br />

## Lazy creation

Pages in both `HorizontalPager` and `VerticalPager` are [lazily composed](https://developer.android.com/develop/ui/compose/lists#lazy)
and laid-out when required. As the user scrolls through pages, the composable
removes any pages which are no longer required.

### Load more pages offscreen

By default, the pager only loads the visible pages on-screen. To load more pages
offscreen, set `beyondBoundsPageCount` to a value higher than zero.

## Scroll to an item in the pager

To scroll to a certain page in the pager, create a [`PagerState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState) object
using [`rememberPagerState()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#rememberPagerState(kotlin.Int,kotlin.Float)) and pass it as the `state` parameter to the
pager. You can call [`PagerState#scrollToPage()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#scrollToPage(kotlin.Int,kotlin.Float)) on this state, inside a
`CoroutineScope`:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    10
})
HorizontalPager(state = pagerState) { page ->
    // Our page content
    Text(
        text = "Page: $page",
        modifier = Modifier
            .fillMaxWidth()
            .height(100.dp)
    )
}

// scroll to page
val coroutineScope = rememberCoroutineScope()
Button(onClick = {
    coroutineScope.launch {
        // Call scroll to on pagerState
        pagerState.scrollToPage(5)
    }
}, modifier = Modifier.align(Alignment.BottomCenter)) {
    Text("Jump to Page 5")
}
```

<br />

If you want to animate to the page, use the
[`PagerState#animateScrollToPage()`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#animateScrollToPage(kotlin.Int,kotlin.Float,androidx.compose.animation.core.AnimationSpec)) function:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    10
})

HorizontalPager(state = pagerState) { page ->
    // Our page content
    Text(
        text = "Page: $page",
        modifier = Modifier
            .fillMaxWidth()
            .height(100.dp)
    )
}

// scroll to page
val coroutineScope = rememberCoroutineScope()
Button(onClick = {
    coroutineScope.launch {
        // Call scroll to on pagerState
        pagerState.animateScrollToPage(5)
    }
}, modifier = Modifier.align(Alignment.BottomCenter)) {
    Text("Jump to Page 5")
}
```

<br />

## Get notified about page state changes

[`PagerState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState) has three properties with information about pages:
[`currentPage`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#currentPage()), [`settledPage`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#settledPage()), and [`targetPage`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#targetPage()).

- `currentPage`: The closest page to the snap position. By default, the snap position is at the start of the layout.
- `settledPage`: The page number when no animation or scrolling is running. This is different from the `currentPage` property in that the `currentPage` immediately updates if the page is close enough to the snap position, but `settledPage` remains the same until all the animations are finished running.
- `targetPage`: The proposed stop position for a scrolling movement.

You can use the `snapshotFlow` function to observe changes to these variables
and react to them. For example, to send an analytics event on each page change,
you can do the following:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    10
})

LaunchedEffect(pagerState) {
    // Collect from the a snapshotFlow reading the currentPage
    snapshotFlow { pagerState.currentPage }.collect { page ->
        // Do something with each page change, for example:
        // viewModel.sendPageSelectedEvent(page)
        Log.d("Page change", "Page changed to $page")
    }
}

VerticalPager(
    state = pagerState,
) { page ->
    Text(text = "Page: $page")
}
```

<br />

## Add a page indicator

To add an indicator to a page, use the `PagerState` object to get information
about which page is selected out of the number of pages, and draw your custom
indicator.

For example, to create a circle indicator, you can repeat the number of
circles and change the circle color based on if the page is selected, using
`pagerState.currentPage`:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize()
) { page ->
    // Our page content
    Text(
        text = "Page: $page",
    )
}
Row(
    Modifier
        .wrapContentHeight()
        .fillMaxWidth()
        .align(Alignment.BottomCenter)
        .padding(bottom = 8.dp),
    horizontalArrangement = Arrangement.Center
) {
    repeat(pagerState.pageCount) { iteration ->
        val color = if (pagerState.currentPage == iteration) Color.DarkGray else Color.LightGray
        Box(
            modifier = Modifier
                .padding(2.dp)
                .clip(CircleShape)
                .background(color)
                .size(16.dp)
        )
    }
}
```

<br />

![Pager showing a circle indicator below the content](https://developer.android.com/static/develop/ui/compose/images/layouts/pager/indicator.png) **Figure 3**. Pager showing a circle indicator below the content

## Apply item scroll effects to content

A common use case is to use the scroll position to apply effects to your pager
items. To find out how far a page is from the selected page, you can use
[`PagerState.currentPageOffsetFraction`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#currentPageOffsetFraction()). You can then apply transformation
effects to your content based on the distance from the selected page.
**Figure 4**. Applying transformations to Pager content

For example, to adjust the opacity of items based on how far they are from the
center, change the `alpha` using [`Modifier.graphicsLayer`](https://developer.android.com/develop/ui/compose/graphics/draw/modifiers#graphicsLayer) on an item
inside the pager:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(state = pagerState) { page ->
    Card(
        Modifier
            .size(200.dp)
            .graphicsLayer {
                // Calculate the absolute offset for the current page from the
                // scroll position. We use the absolute value which allows us to mirror
                // any effects for both directions
                val pageOffset = (
                    (pagerState.currentPage - page) + pagerState
                        .currentPageOffsetFraction
                    ).absoluteValue

                // We animate the alpha, between 50% and 100%
                alpha = lerp(
                    start = 0.5f,
                    stop = 1f,
                    fraction = 1f - pageOffset.coerceIn(0f, 1f)
                )
            }
    ) {
        // Card content
    }
}
```

<br />

## Custom page sizes

By default, `HorizontalPager` and `VerticalPager` takes up the full width or
full height, respectively. You can set the `pageSize` variable to either have a
[`Fixed`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PageSize.Fixed), [`Fill`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PageSize.Fill) (default), or a custom size calculation.

For example, to set a fixed width page of `100.dp`:


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(
    state = pagerState,
    pageSize = PageSize.Fixed(100.dp)
) { page ->
    // page content
}
```

<br />

To size the pages based on the viewport size, use a custom page size
calculation. Create a custom [`PageSize`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PageSize) object and divide the
`availableSpace` by three, taking into account the spacing between the items:


```kotlin
private val threePagesPerViewport = object : PageSize {
    override fun Density.calculateMainAxisPageSize(
        availableSpace: Int,
        pageSpacing: Int
    ): Int {
        return (availableSpace - 2 * pageSpacing) / 3
    }
}
```

<br />

## Content padding

`HorizontalPager` and `VerticalPager` both support changing the content padding,
which lets you influence the maximum size and alignment of pages.

For example, setting the `start` padding aligns the pages towards the end:
![Pager with start padding showing the content aligned towards the end](https://developer.android.com/static/develop/ui/compose/images/layouts/pager/contentpadding-start.png) **Figure 5**. Pager with start padding.


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(
    state = pagerState,
    contentPadding = PaddingValues(start = 64.dp),
) { page ->
    // page content
}
```

<br />

Setting both the `start` and `end` padding to the same value centers the item
horizontally:
![Pager with start and end padding showing the content centered](https://developer.android.com/static/develop/ui/compose/images/layouts/pager/contentpadding-horizontal.png) **Figure 6**. Pager with horizontal padding.


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(
    state = pagerState,
    contentPadding = PaddingValues(horizontal = 32.dp),
) { page ->
    // page content
}
```

<br />

Setting the `end` padding aligns the pages towards the start:
![Pager with start and end padding showing the content aligned to the start](https://developer.android.com/static/develop/ui/compose/images/layouts/pager/contentpadding-end.png) **Figure 7**. Pager with end padding.


```kotlin
val pagerState = rememberPagerState(pageCount = {
    4
})
HorizontalPager(
    state = pagerState,
    contentPadding = PaddingValues(end = 64.dp),
) { page ->
    // page content
}
```

<br />

You can set the `top` and `bottom` values to achieve similar effects for
`VerticalPager`. The value `32.dp` is only used here as an example; you can set
each of the padding dimensions to any value.

## Customize scroll behavior

The default `HorizontalPager` and `VerticalPager` composables specify how
scrolling gestures work with the pager. However, you can customize and change
the defaults such as the `pagerSnapDistance` or the `flingBehavior`.

### Snap distance

By default, `HorizontalPager` and `VerticalPager` set the maximum number of
pages that a fling gesture can scroll past to one page at a time. To change
this, set [`pagerSnapDistance`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerSnapDistance) on the `flingBehavior`:


```kotlin
val pagerState = rememberPagerState(pageCount = { 10 })

val fling = PagerDefaults.flingBehavior(
    state = pagerState,
    pagerSnapDistance = PagerSnapDistance.atMost(10)
)

Column(modifier = Modifier.fillMaxSize()) {
    HorizontalPager(
        state = pagerState,
        pageSize = PageSize.Fixed(200.dp),
        beyondViewportPageCount = 10,
        flingBehavior = fling
    ) {
        PagerSampleItem(page = it)
    }
}
```

<br />

## Create an auto-advancing pager

This section describes how to create an auto-advancing pager with page
indicators in Compose. The collection of items automatically scroll
horizontally, but users can also manually swipe between items. If a user
interacts with the pager, it stops the automatic progression.

### Basic example

Together, the following snippets create a basic auto-advancing pager
implementation with a visual indicator, in which each page renders as a
different color:


```kotlin
@Composable
fun AutoAdvancePager(pageItems: List<Color>, modifier: Modifier = Modifier) {
    Box(modifier = Modifier.fillMaxSize()) {
        val pagerState = rememberPagerState(pageCount = { pageItems.size })
        val pagerIsDragged by pagerState.interactionSource.collectIsDraggedAsState()

        val pageInteractionSource = remember { MutableInteractionSource() }
        val pageIsPressed by pageInteractionSource.collectIsPressedAsState()

        // Stop auto-advancing when pager is dragged or one of the pages is pressed
        val autoAdvance = !pagerIsDragged && !pageIsPressed

        if (autoAdvance) {
            LaunchedEffect(pagerState, pageInteractionSource) {
                while (true) {
                    delay(2000)
                    val nextPage = (pagerState.currentPage + 1) % pageItems.size
                    pagerState.animateScrollToPage(nextPage)
                }
            }
        }

        HorizontalPager(
            state = pagerState
        ) { page ->
            Text(
                text = "Page: $page",
                textAlign = TextAlign.Center,
                modifier = modifier
                    .fillMaxSize()
                    .background(pageItems[page])
                    .clickable(
                        interactionSource = pageInteractionSource,
                        indication = LocalIndication.current
                    ) {
                        // Handle page click
                    }
                    .wrapContentSize(align = Alignment.Center)
            )
        }

        PagerIndicator(pageItems.size, pagerState.currentPage)
    }
}
```

<br />

#### Key points about the code

- The `AutoAdvancePager` function creates a horizontally paging view with automatic advancement. It takes a list of `Color` objects as input, which are used as background colors for each page.
- `pagerState` is created using [`rememberPagerState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#rememberPagerState(kotlin.Int,kotlin.Float,kotlin.Function0)), which holds the state of the pager.
- `pagerIsDragged` and `pageIsPressed` track user interaction.
- The [`LaunchedEffect`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary#LaunchedEffect(kotlin.Any,kotlin.coroutines.SuspendFunction1)) auto-advances the pager every two seconds unless the user drags the pager or presses one of the pages.
- [`HorizontalPager`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,androidx.compose.foundation.gestures.snapping.SnapPosition,androidx.compose.foundation.OverscrollEffect,kotlin.Function2)) displays a list of pages, each with a `Text` composable displaying the page number. The modifier fills the page, sets the background color from `pageItems`, and makes the page clickable.


```kotlin
@Composable
fun PagerIndicator(pageCount: Int, currentPageIndex: Int, modifier: Modifier = Modifier) {
    Box(modifier = Modifier.fillMaxSize()) {
        Row(
            modifier = Modifier
                .wrapContentHeight()
                .fillMaxWidth()
                .align(Alignment.BottomCenter)
                .padding(bottom = 8.dp),
            horizontalArrangement = Arrangement.Center
        ) {
            repeat(pageCount) { iteration ->
                val color = if (currentPageIndex == iteration) Color.DarkGray else Color.LightGray
                Box(
                    modifier = modifier
                        .padding(2.dp)
                        .clip(CircleShape)
                        .background(color)
                        .size(16.dp)
                )
            }
        }
    }
}
```

<br />

#### Key points about the code

- A [`Box`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Box(androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Boolean,kotlin.Function1)) composable acts as the root element and contains a [`Row`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) to arrange the page indicators horizontally.
- A custom page indicator is displayed as a row of circles, where each `Box` clipped to a `CircleShape` represents a page.
- The current page's circle is colored as a `DarkGray`, while the other circles are `LightGray`. The `currentPageIndex` parameter determines which circle renders in dark gray.

#### Result

This video displays the basic auto-advancing pager from the preceding
snippets:

<br />

**Figure 8**. An auto-advancing pager with a two second delay between each page progression.

<br />

## Additional resources

- [Display a paging list](https://developer.android.com/develop/ui/compose/quick-guides/content/display-paging-list?hl=en)