---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/position-indicator
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/position-indicator
source: md.txt
---

# Position indicator

![](https://developer.android.com/static/wear/images/position-indicator/positoin-indicator-hero.png)

The[PositionIndicator](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#PositionIndicator(androidx.compose.foundation.ScrollState,androidx.compose.ui.Modifier,kotlin.Boolean))component displays the user's location in a list or range value.  
![](https://developer.android.com/static/wear/images/position-indicator/position-indicator.png)  
Use position indicators in list or for other contexts when you can use the rotating side button (RSB) to scroll, adjust settings, control volume, or do other actions.

<br />

<br />

## Anatomy

![](https://developer.android.com/static/wear/images/position-indicator/position-indicator-anatomy.png)  
A. Track  
B. Indicator

<br />

<br />

## Usage

See the following examples of position indicators.

![](https://developer.android.com/static/wear/images/position-indicator/position-indicator-usage2.png)

## Large screens

![](https://developer.android.com/static/wear/images/position-indicator/position-indicator-adaptive-layouts-usage.png)

### **Responsive behavior**

The position indicator will remain the same size across screen sizes, this means the angle of the curve will change slightly to match.

![](https://developer.android.com/static/wear/images/position-indicator/position-indicator-adaptive-layouts-anatomy.png)

**Position indicator**

The arc of the indicator is always 50 dp high (doesn't scale proportionally) meaning only the degree changes as you go up in size.  

It's possible to manually adjust the margin down to 2 dp to match SysUI. The height will remain fixed at 50 dp.

![](https://developer.android.com/static/wear/images/position-indicator/position-indicator-control-rsb-adaptive-layouts.png)

**Control/RSB indicator**

The arc of the indicator is always 76 dp high (doesn't scale proportionally) meaning only the degree changes as you go up in size.  

It's possible to:

- Manually adjust the margin down to 2 dp to match SysUI. The height will remain fixed at 50 dp.
- Have the indicator sit on the left or right side of the screen.