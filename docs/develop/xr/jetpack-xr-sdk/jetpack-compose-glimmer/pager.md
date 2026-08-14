---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/pager
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/pager
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, [`GlimmerHorizontalPager`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPager.composable) is a lazily
composed, horizontally scrollable layout that arranges its pages sequentially.
It's similar to the standard [`HorizontalPager`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/pager/HorizontalPager.composable) found in Compose
Foundation, but tailored for display glasses with Glimmer behaviors and
default values.

By default, only one page is prominently displayed at a time.
To provide a polished experience, the pager uses snap animations to ensure that
a page always settles exactly into the viewport boundaries after a user's
scrolling gesture ends.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_pager_opacity_do.png) **Figure 1.** An example of \`GlimmerHorizontalPager\`.

## Key parameters and layout options

A `GlimmerHorizontalPager` provides customizable parameters to control spacing,
layout alignment, and lazy loading. Some of these parameters are:

| Parameter | Description |
|---|---|
| `state` | A [`GlimmerPagerState`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/GlimmerPagerState) object that manages, observes, and programmatically controls the pager's scroll position and active page. |
| `contentPadding` | Padding applied around the overall content boundaries after clipping, useful for adding leading or trailing edge padding before the first page or after the last page. |
| `pageSpacing` | The horizontal spacing between individual pages in the pager. |
| `pageIndicator` | A composable slot rendering the active page indicator. Defaults to [`GlimmerHorizontalPagerDefaults.PageIndicator(state)`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPagerDefaults#PageIndicator(androidx.xr.glimmer.pager.GlimmerPagerState,androidx.compose.ui.Modifier)). |
| `beyondViewportPageCount` | The number of pages to compose and lay out beyond the visible viewport as a pre-loading optimization. Avoid setting large values to preserve lazy composition efficiency. |

See the full [reference documentation](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPager.composable) for information on all available
parameters.

## Animated text motion recommendation

> [!CAUTION]
> **Caution:** When rendering text inside a `GlimmerHorizontalPager`, We recommended setting [`textMotion`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()) on text styles to [`TextMotion.Animated`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/style/TextMotion#Animated()).

During pager snap animations and transitions on display glasses, default
text rendering can exhibit pixel-snapping artifacts. Setting
`TextMotion.Animated` ensures smooth rendering throughout layout animations:


```kotlin
Text(
    text = "Page: $page",
    style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
)
```

<br />

## Example: Horizontal pager

The following code demonstrates how to create a basic horizontal pager with
10 pages, placing a Card inside each page:


```kotlin
// Hoist the pager state, specifying the total page count with a lambda.
val pagerState = rememberGlimmerPagerState(pageCount = { 10 })

GlimmerHorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize(),
) { page ->
    // Use Glimmer components like Card and Text for optimized glasses styling.
    Card(modifier = Modifier.fillMaxWidth()) {
        Text(
            text = "Page: $page",
            // Recommended: use TextMotion.Animated for smooth transitions in a pager.
            style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
        )
    }
}
```

<br />

### Key points about the code

- **State** : Initializes a [`GlimmerPagerState`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/rememberGlimmerPagerState.composable) using `rememberGlimmerPagerState(pageCount = { 10 })` to manage the state of the pager.
- **Page slot content** : Receives the page index `page` inside the `GlimmerPagerScope` lambda to render each card.
- **Smooth animation text style** : Copies `LocalTextStyle.current` and explicitly enables `TextMotion.Animated`.
- **Automatic page indicator** : Unlike standard Compose pagers that require an external indicator component, `GlimmerHorizontalPager` automatically embeds a dot-style page indicator by default.

## Page indicators

By default, `GlimmerHorizontalPager` renders a dot-based page indicator using
[`GlimmerHorizontalPagerDefaults.PageIndicator`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/pager/GlimmerHorizontalPagerDefaults). The indicator automatically
adapts its color scheme:

- The active dot uses the content color resolved from the nearest surrounding [`surface`](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces).

You can pass a customized `PageIndicator` to specify explicit colors, or
replace the dot with your own custom layout:


```kotlin
GlimmerHorizontalPager(
    state = pagerState,
    modifier = Modifier.fillMaxSize(),
    // Use a page numbers instead of the default dot-indicator
    pageIndicator = {
        Text(
            text = "${pagerState.currentPage + 1} / ${pagerState.pageCount}",
            style = LocalTextStyle.current.copy(textMotion = TextMotion.Animated),
        )
    }
)
```

<br />