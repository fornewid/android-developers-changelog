---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/custom-page-indicator
url: https://developer.android.com/develop/ui/compose/quick-guides/content/custom-page-indicator
source: md.txt
---

<br />

Using page indicators, you can help your users understand their current position
within your app's content, providing a visual indication of progress. These
navigational cues are useful when you present content sequentially, such as
carousel implementations, image galleries and slideshows, or pagination in
lists.

## Results

**Figure 1.** Pager showing a circle indicator under the content.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/custom-page-indicator_a1e19bb9399af83328f4f119460605b05ca7b024e7aa299476e2a91b55b09539.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Create a horizontal pager with a custom page indicator

The following code creates a horizontal pager that has a page indicator, giving
the user visual cues for how many pages there are and which page is
visible:


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

### Key points about the code

- The code implements a [`HorizontalPager`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/package-summary#HorizontalPager(androidx.compose.foundation.pager.PagerState,androidx.compose.ui.Modifier,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.pager.PageSize,kotlin.Int,androidx.compose.ui.unit.Dp,androidx.compose.ui.Alignment.Vertical,androidx.compose.foundation.gestures.TargetedFlingBehavior,kotlin.Boolean,kotlin.Boolean,kotlin.Function1,androidx.compose.ui.input.nestedscroll.NestedScrollConnection,androidx.compose.foundation.gestures.snapping.SnapPosition,kotlin.Function2)), which lets you swipe horizontally between different pages of content. In this case, each page displays the page number.
- The `rememberPagerState()` function initializes the pager and sets the number of pages to 4. This function creates a state object that tracks the current page, and lets you control the pager.
- The [`pagerState.currentPage`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/PagerState#currentPage()) property is used to determine which page indicator should be highlighted.
- The page indictator appears in a pager overlaid by a [`Row`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1)) implementation.
- A 16 dp circle is drawn for each page in the pager. The indicator for the current page is displayed as `DarkGray`, while the rest of the indicator circles are `LightGray`.
- The [`Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable within the `HorizontalPager` displays the text "Page: \[page number\]" on each page.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a visually pleasing form that's easy for users to consume. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-a-list-or-grid) ![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily create beautiful UI components based on the Material Design design system. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-interactive-components) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)