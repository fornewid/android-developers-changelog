---
title: Position indicator  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/position-indicator
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Position indicator Stay organized with collections Save and categorize content based on your preferences.



![](/static/wear/images/position-indicator/positoin-indicator-hero.png)

The [PositionIndicator](/reference/kotlin/androidx/wear/compose/material/package-summary#PositionIndicator(androidx.compose.foundation.ScrollState,androidx.compose.ui.Modifier,kotlin.Boolean)) component displays the user’s location in a list or range value.

![](/static/wear/images/position-indicator/position-indicator.png)

Use position indicators in list or for other contexts when you can use the rotating side button (RSB) to scroll, adjust settings, control volume, or do other actions.

## Anatomy

![](/static/wear/images/position-indicator/position-indicator-anatomy.png)

A. Track  
B. Indicator

## Usage

See the following examples of position indicators.

![](/static/wear/images/position-indicator/position-indicator-usage2.png)

## Large screens

![](/static/wear/images/position-indicator/position-indicator-adaptive-layouts-usage.png)

### **Responsive behavior**

The position indicator will remain the same size across screen sizes, this means the angle of the curve will change slightly to match.

![](/static/wear/images/position-indicator/position-indicator-adaptive-layouts-anatomy.png)

**Position indicator**

The arc of the indicator is always 50 dp high (doesn’t scale proportionally) meaning only the degree changes as you go up in size.  
  
It’s possible to manually adjust the margin down to 2 dp to match SysUI. The height will remain fixed at 50 dp.

![](/static/wear/images/position-indicator/position-indicator-control-rsb-adaptive-layouts.png)

**Control/RSB indicator**

The arc of the indicator is always 76 dp high (doesn’t scale proportionally) meaning only the degree changes as you go up in size.  
  
It’s possible to:

* Manually adjust the margin down to 2 dp to match SysUI. The height will remain fixed at 50 dp.
* Have the indicator sit on the left or right side of the screen.