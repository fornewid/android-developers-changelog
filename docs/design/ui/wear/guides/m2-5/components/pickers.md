---
title: https://developer.android.com/design/ui/wear/guides/m2-5/components/pickers
url: https://developer.android.com/design/ui/wear/guides/m2-5/components/pickers
source: md.txt
---

# Pickers

![](https://developer.android.com/static/wear/images/pickers/picker-hero.png)

The[Picker](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#Picker(androidx.wear.compose.material.PickerState,androidx.compose.ui.Modifier,kotlin.Boolean,kotlin.Function1,androidx.wear.compose.material.ScalingParams,androidx.compose.ui.unit.Dp,kotlin.Float,androidx.compose.ui.graphics.Color,androidx.compose.foundation.gestures.FlingBehavior,kotlin.Function2))helps users select and set specific data.  
![](https://developer.android.com/static/wear/images/pickers/picker-single-column.png)  
**Picker**

Pickers should be used to let users choose amongst a finite number of items.  

By default items will be looped infinitely in both directions. Consider disabling this behaviour if order in the list is important, or to allow users to reach the first and last element with a quick swipe.

<br />

<br />

## Anatomy

![](https://developer.android.com/static/wear/images/pickers/picker-anatomy.png)  
**Anatomy**

A. Inactive Column  
B. Colon Breaker  
C. Picker Column  
D. Top Content  
E. Middle Content  
F. Bottom Content

<br />

<br />

![](https://developer.android.com/static/wear/images/pickers/picker-anatomy-widths.png)  
**Widths and heights**

The Picker Group fills the available height and width. There are four layout options for the picker columns. Each layout is centred and fills the available height. Column widths are defined by the width needed to accommodate the number of digits needed in the font, Date-picker is the exception, horizontally it fills the screen and bleeds off the edge.

For example numbers will work out width of '00' is and then set the width. For text fields, for the month field for example, will be worked out as the width of 'MMM' (which is the widest letter in the latin alphabet). The width and height (which is the line height of that type style used) will therefore be affected by the font used.

Picker items vary in size across the breakpoint.

<br />

<br />

## Usage

See the following examples of Date and Time Pickers

![](https://developer.android.com/static/wear/images/pickers/picker-usage.png)

For a prebuilt date and time picker implementation, check out the[Horologist Library](https://github.com/google/horologist#-composables)on GitHub.  

If you want to create a similar experience, where users choose a multi-part value across multiple pickers, use the built-in[PickerGroup](https://developer.android.com/reference/kotlin/androidx/wear/compose/material/package-summary#PickerGroup(kotlin.Array,androidx.compose.ui.Modifier,androidx.wear.compose.material.PickerGroupState,kotlin.Function1,kotlin.Boolean,kotlin.Boolean,androidx.wear.compose.material.TouchExplorationStateProvider,kotlin.Function1))component. This object uses a focus coordinator object to assign focus to the correct Picker element.

## Adaptive layouts

**TimePicker 24H**

![](https://developer.android.com/static/wear/images/pickers/picker-adaptive-layouts-time-picker-24.png)

**TimePicker 12H**

![](https://developer.android.com/static/wear/images/pickers/picker-large-screens-time-picker-24.png)

**Date Picker**

![](https://developer.android.com/static/wear/images/pickers/picker-large-screens-date-picker.png)

## **Responsive behavior**

### **Text size increase**

Past the 225+ Breakpoint, the Picker element's font size changes. Top and Bottom copy within the lazy scrolling column adjusts (A), as does the Middle copy. Below are some examples of this:

**Two column layout**  
![](https://developer.android.com/static/wear/images/pickers/picker-textsize-two-column-pre225.png)![](https://developer.android.com/static/wear/images/pickers/picker-textsize-two-column-post225.png)  
**Below the 225 dp breakpoint**

Font: Display 2  
**Above 225 dp breakpoint**

Font: Display 1

<br />

<br />

**Three column layout**  
![](https://developer.android.com/static/wear/images/pickers/picker-textsize-three-column-pre225.png)![](https://developer.android.com/static/wear/images/pickers/picker-textsize-three-column-post225.png)  
**Below the 225 dp breakpoint**

Font: Display 3  
**Above the 225 dp breakpoint**

Font: Display 2

<br />

<br />

## **Gradient size increase**

The gradient on the Picker column is defined in height by the available space. Both Top and Bottom Gradients are set at a third (33%) of the available height. This means at each available screen size, the gradient scales proportionally. Sitting independent of the column layout.  
![](https://developer.android.com/static/wear/images/pickers/picker-gradientsize-pre225.png)![](https://developer.android.com/static/wear/images/pickers/picker-gradientsize-post225.png)  
**Below the 225 dp breakpoint**

Size: 33% of column height  
**Above the 225 dp breakpoint**

Size: 33% of column height

<br />

<br />

## **Column spacing increase**

Column spacing scales past the 225+ Breakpoint, either starting at 2 dp or 4 dp and growing to 6 dp. This depends on which layout you've selected; either 2 or 3 column layouts

**Two column layout**  
![](https://developer.android.com/static/wear/images/pickers/picker-columnspacing-two-column-pre225.png)![](https://developer.android.com/static/wear/images/pickers/picker-columnspacing-two-column-post225.png)  
**Below the 225 dp breakpoint**

4 dp column gap  
**Above the 225 dp breakpoint**

6 dp column gap

<br />

<br />

### **Three column layout**

![](https://developer.android.com/static/wear/images/pickers/picker-columnspacing-three-column-pre225.png)![](https://developer.android.com/static/wear/images/pickers/picker-columnspacing-three-column-post225.png)  
**Below the 225 dp breakpoint**

2 dp column gap  
**Above the 225 dp breakpoint**

6 dp column gap

<br />

<br />