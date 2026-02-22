---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/sliders
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/sliders
source: md.txt
---

# Sliders

![](https://developer.android.com/static/wear/images/sliders/sliders-hero.png)

The[Inline sliders](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#InlineSlider(kotlin.Float,kotlin.Function1,kotlin.Int,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.ranges.ClosedFloatingPointRange,kotlin.Boolean,androidx.wear.compose.material.InlineSliderColors))allow users to make selections from a range of values.  
![](https://developer.android.com/static/wear/images/sliders/sliders-visual.png)  
Use inline sliders to select a value from a range, such as setting screen brightness or font size. Changes made with sliders are immediate, allowing the user to continue to make adjustments until they are satisfied. Don't use sliders in situations where adjustments are not immediate.

<br />

<br />

## Anatomy

![](https://developer.android.com/static/wear/images/sliders/sliders-anatomy.png)  
**A. Progress bar
B. Progress track
C. Container
D. Decrease icon
E. Increase icon
F. Spacer**

<br />

<br />

## Design recommendations

![](https://developer.android.com/static/wear/images/sliders/sliders-segmented-sliders.png)  
**Segmented slider**

Consider using a segmented slider if the range of values is between three and nine. If the range is greater than eight, segments will be too small to be visible.

<br />

<br />

## Usage

![](https://developer.android.com/static/wear/images/sliders/sliders-usage-settings.png)

## Adaptive layouts

The step segments fills the available width, so it will appear longer depending on the size of the screen.

![](https://developer.android.com/static/wear/images/sliders/sliders-adaptive-layouts-usage.png)  
![](https://developer.android.com/static/wear/images/sliders/sliders-anatomy-large-screen.png)  
**Fills available width**

Sliders stretch to fill the available width on larger screens.

Icon (24 x 24 dp)  
Container (52 x XX dp)

<br />

<br />