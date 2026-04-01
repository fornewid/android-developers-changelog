---
title: Add a custom page indicator  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/custom-page-indicator
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Add a custom page indicator Stay organized with collections Save and categorize content based on your preferences.



Using page indicators, you can help your users understand their current position
within your app's content, providing a visual indication of progress. These
navigational cues are useful when you present content sequentially, such as
carousel implementations, image galleries and slideshows, or pagination in
lists.

## Results

[

](/static/develop/ui/compose/quick-guides/content/page_indicator.mp4)


**Figure 1.** Pager showing a circle indicator under the content.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a horizontal pager with a custom page indicator

The following code creates a horizontal pager that has a page indicator, giving
the user visual cues for how many pages there are and which page is
visible:

```
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

PagerSnippets.kt
```

### Key points about the code

* The code implements a [`HorizontalPager`](/reference/kotlin/androidx/compose/foundation/pager/HorizontalPager.composable), which lets you swipe
  horizontally between different pages of content. In this case, each page
  displays the page number.
* The `rememberPagerState()` function initializes the pager and sets the
  number of pages to 4. This function creates a state object that tracks the
  current page, and lets you control the pager.
* The [`pagerState.currentPage`](/reference/kotlin/androidx/compose/foundation/pager/PagerState#currentPage()) property is used to determine which page
  indicator should be highlighted.
* The page indictator appears in a pager overlaid by a [`Row`](/reference/kotlin/androidx/compose/foundation/layout/Row.composable#Row(androidx.compose.ui.Modifier,androidx.compose.foundation.layout.Arrangement.Horizontal,androidx.compose.ui.Alignment.Vertical,kotlin.Function1))
  implementation.
* A 16 dp circle is drawn for each page in the pager. The indicator for the
  current page is displayed as `DarkGray`, while the rest of the indicator
  circles are `LightGray`.
* The [`Text`](/reference/kotlin/androidx/compose/material/Text.composable#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) composable within the `HorizontalPager` displays the text
  "Page: [page number]" on each page.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display a list or grid

Lists and grids allow your app to display collections in a
visually pleasing form that's easy for users to consume.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-a-list-or-grid)

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Display interactive components

Learn how composable functions can enable you to easily
create beautiful UI components based on the Material Design design
system.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/display-interactive-components)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)