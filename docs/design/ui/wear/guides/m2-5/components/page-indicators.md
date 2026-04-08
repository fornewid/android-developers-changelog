---
title: Page indicators  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/page-indicators
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Page indicators Stay organized with collections Save and categorize content based on your preferences.




![](/static/wear/images/page-indicators/Page_Indicators-Hero.png)

The [HorizontalPageIndicator](/reference/kotlin/androidx/wear/compose/material/HorizontalPageIndicator.composable#HorizontalPageIndicator(androidx.wear.compose.material.PageIndicatorState,androidx.compose.ui.Modifier,androidx.wear.compose.material.PageIndicatorStyle,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Shape)) component is used to represent the currently active page and total pages of an overlay.

![](/static/wear/images/page-indicators/Anatomy.png)

On round displays, a page indicator is curved. This behavior is implemented in the `HorizontalPageIndicator` class. It is made up of one active indicator and at least one inactive indicator.  
  
**A. Inactive Indicator  
B. Active Indicator**

[](/static/wear/images/page-indicators/page-indicator-carousel.mp4)

Use indicators to show users where you are in a carousel. Orient content from left to right.

## **Usage**

![](/static/wear/images/page-indicators/Usage_View.png)

## **Adaptive layouts**

Centre of the dot (indicator) circumference aligns near or on the circular grid for optical balance, this means the curve angle changes slightly as the screen size increases.

![](/static/wear/images/page-indicators/page-indicators-adaptive-layouts-page-indicators.png)

![](/static/wear/images/page-indicators/Maximum_Example.png)

The pagination will always show a maximum of 6 dots, no matter the size of the screen.