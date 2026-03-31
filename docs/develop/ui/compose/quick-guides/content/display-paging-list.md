---
title: Display a paging list  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-paging-list
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Quick Guides](https://developer.android.com/develop/ui/compose/quick-guides)

# Display a paging list Stay organized with collections Save and categorize content based on your preferences.




Create a paging list so that users can scroll to access content too large to fit
on a single screen. Horizontal paging lists can help users navigate through
content such as images, slideshows, or product carousels. Vertical paging lists
are useful for content-heavy apps where users may need to scroll through a large
number of items, such as articles.

## Results

[

](/static/develop/ui/compose/quick-guides/content/horizintal_pager_compose.mp4)


**Figure 1.** Demo of `HorizontalPager`.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

## Create a paging list

You can configure a horizontal or vertical paging list, depending on the
orientation required for your app. The following code creates a horizontal
paging list displaying 10 items:

### Key points about the code

* The [`HorizontalPager`](/reference/kotlin/androidx/compose/foundation/pager/HorizontalPager.composable) composable provides a horizontally
  scrollable list of items.
  + To create a vertical paging list, use the [`VerticalPager`](/reference/kotlin/androidx/compose/foundation/pager/VerticalPager.composable)
    composable instead.
* Each page in the list contains a [`Text`](/reference/kotlin/androidx/compose/material/Text.composable#Text(androidx.compose.ui.text.AnnotatedString,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.collections.Map,kotlin.Function1,androidx.compose.ui.text.TextStyle)) object that displays the string
  "Page" and the page index number.
* An instance of [`rememberPagerState()`](/reference/kotlin/androidx/compose/foundation/pager/package-summary#rememberPagerState(kotlin.Int,kotlin.Float)) persists a page's state
  when the user navigates away, and displays the same page when the user
  returns to it.

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

![](/static/images/quick-guides/collection-illustration.png)

![](/static/images/picto-icons/collection.svg)

### Compose basics (video collection)

This series of videos introduces various Compose APIs,
quickly showing you what’s available and how to use them.

[Quick guide collection](/develop/ui/compose/quick-guides/collections/compose-basics)

![](/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts.

[Go to FAQ](/quick-guides/faq)
[Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)