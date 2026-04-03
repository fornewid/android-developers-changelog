---
title: Steppers  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/steppers
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Steppers Stay organized with collections Save and categorize content based on your preferences.



![](/static/wear/images/steppers/steppers-hero.png)

The [Stepper](/reference/kotlin/androidx/wear/compose/material/package-summary#Stepper(kotlin.Float,kotlin.Function1,kotlin.Int,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.ranges.ClosedFloatingPointRange,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1)) allow users to make a selection from a range of values.

![](/static/wear/images/steppers/stepper-visual.png)

Use steppers for a full-screen control experience that allows users to make a selection from a range of values.

## Anatomy

![](/static/wear/images/steppers/steppers-anatomy.png)

**A. Increase button  
B. Label or chip  
C. Decrease button**

## Usage

See the following examples of how to use steppers.

![](/static/wear/images/steppers/stepper-usage.png)

Check out the [Horologist library](https://github.com/google/horologist#-audio-and-ui) on GitHub that offers an implementation of a volume control screen.

## Adaptive layouts

![](/static/wear/images/steppers/stepper-adaptive-layouts-usage.png)

## Responsive behavior

The stepper component fills available height and width, therefore the gap between elements is determined by the screen size and the available height.

![](/static/wear/images/steppers/steppers-adaptive-layout-anatomy.png)