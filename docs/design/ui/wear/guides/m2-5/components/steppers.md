---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/steppers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/steppers
source: md.txt
---

# Steppers

![](https://developer.android.com/static/wear/images/steppers/steppers-hero.png)

The[Stepper](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#Stepper(kotlin.Float,kotlin.Function1,kotlin.Int,kotlin.Function0,kotlin.Function0,androidx.compose.ui.Modifier,kotlin.ranges.ClosedFloatingPointRange,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1))allow users to make a selection from a range of values.  
![](https://developer.android.com/static/wear/images/steppers/stepper-visual.png)  
Use steppers for a full-screen control experience that allows users to make a selection from a range of values.

<br />

<br />

## Anatomy

![](https://developer.android.com/static/wear/images/steppers/steppers-anatomy.png)  
**A. Increase button
B. Label or chip
C. Decrease button**

<br />

<br />

## Usage

See the following examples of how to use steppers.

![](https://developer.android.com/static/wear/images/steppers/stepper-usage.png)

Check out the[Horologist library](https://github.com/google/horologist#-audio-and-ui)on GitHub that offers an implementation of a volume control screen.

## Adaptive layouts

![](https://developer.android.com/static/wear/images/steppers/stepper-adaptive-layouts-usage.png)

## Responsive behavior

The stepper component fills available height and width, therefore the gap between elements is determined by the screen size and the available height.

![](https://developer.android.com/static/wear/images/steppers/steppers-adaptive-layout-anatomy.png)