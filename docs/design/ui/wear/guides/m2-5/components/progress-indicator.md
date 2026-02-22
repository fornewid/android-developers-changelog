---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/progress-indicator
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/progress-indicator
source: md.txt
---

# Progress indicator

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-hero.png)

[Progress indicators](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#CircularProgressIndicator(kotlin.Float,androidx.compose.ui.Modifier,kotlin.Float,kotlin.Float,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp))are circular displays of the length of a process or an otherwise unspecified wait time.  
![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-main.png)  
Use progress indicators to show the proportion of a task that is complete. To show progress an indicator is animated along a circular track in a clockwise direction.  
You can apply progress indicators to components such as a play button.

<br />

<br />

## Anatomy

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-anatomy.png)  
Use progress indicators to show the proportion of a task that is complete. To show progress an indicator is animated along a circular track in a clockwise direction.  
You can apply progress indicators to components such as a play button.

<br />

<br />

## **Design recommendations**

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-design-recommendations.png)  
**Progress indicator with gap**

<br />

Create progress indicators with a gap to leave space for important information such as the time. To create a gap, change the progress indicator's startAngle and endAngle.

<br />

<br />

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-design-recommendations-small.png)  
**Small progress indicator**

<br />

Create progress indicators with a gap to leave space for important information such as the time. Create a gap by changing the progress indicator's start and end angle.

<br />

<br />

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-design-recommendations-indeterminate.png)  
**Indeterminate progress indicator**

<br />

When using the progress indicator for situations where there is no set time, use a progress indicator with animated value. This can also be called a spinner. Use spinners sparingly as they can increase perceived wait time.

<br />

<br />

## Usage

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-usage.png)

## Adaptive layouts

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-adaptive-layouts-usage.png)

## Responsive behavior

The circumference of the progress indicator fills the screen/element (for on button) width and height, proportionally, while the stroke width remains the same across all breakpoints.  

The gap degree for full screen stays at 51°, but the sweep will increase in dp based on the screen size.  
The ring width and starting and end points are customisable.

![](https://developer.android.com/static/wear/images/progress-indicator/progress-indicator-anatomy-adaptive-layout.png)