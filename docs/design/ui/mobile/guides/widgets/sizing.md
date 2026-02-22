---
title: https://developer.android.com/design/ui/mobile/guides/widgets/sizing
url: https://developer.android.com/design/ui/mobile/guides/widgets/sizing
source: md.txt
---

# Sizing

Design adaptable Android widgets that scale seamlessly. Use our recommended default sizes as a starting point, and test your layouts across different dimensions to ensure optimal readability and user experience.

## Default sizes

Deliver a polished widget experience by optimizing your layout for at least one of our recommended sizes. Ensure correct placement and visibility in the widget picker by defining`targetCellWidth`and`targetCellHeight`attributes for both handheld and tablet devices.

These values are based off Pixel devices. Use these sizes as a starting point for your widget design. Thoroughly test your widget at different sizes and on various devices to ensure a quality user experience.  

### Handheld

<br />

| Sizes | Min width | Max width | Min height | Max height |
|-------|-----------|-----------|------------|------------|
| 2x1   | 109       | 306       | 56         | 130        |
| 2x2   | 109       | 306       | 115        | 276        |
| 2x3   | 109       | 306       | 185        | 422        |
| 4x1   | 245       | 624       | 56         | 130        |
| 4x2   | 245       | 624       | 115        | 276        |
| 4x3   | 245       | 624       | 185        | 422        |

<br />

### Tablet

<br />

| Sizes | Min width | Max width | Min height | Max height |
|-------|-----------|-----------|------------|------------|
| 2x1   | 180       | 304       | 64         | 120        |
| 2x2   | 180       | 304       | 184        | 304        |
| 2x3   | 180       | 304       | 304        | 488        |
| 3x1   | 328       | 488       | 64         | 120        |
| 3x2   | 298       | 488       | 184        | 304        |
| 3x3   | 298       | 488       | 304        | 488        |
| 3x4   | 298       | 488       | 424        | 672        |

<br />

| **Note:** Widget dimensions in the table encompass all device orientations, including landscape mode on phones, to ensure optimal functionality in a variety of scenarios.

## Breakpoints

Breakpoints are essential for crafting adaptable, user-friendly resizable widgets. By testing your design, you can pinpoint size thresholds where layout adjustments are necessary. Implement breakpoints to trigger these changes, ensuring your widget maintains visual appeal and functionality at any size.

Breakpoints also offer the flexibility to conditionally include or exclude supplemental content, optimizing space utilization based on the widget's dimensions.
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Breakpoints.jpg)**Figure 1:**Use breakpoints to make layout changes at different sizes.

## Fill the bounds

One of the primary reasons users remove widgets is due to misalignment with other home screen elements. To prevent this, ensure your widget always fills its allocated grid space completely.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/01_Fill_the_Bounds.jpg)  
check_circle

### Do

Make sure the container stretches edge-to-edge at all sizes.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/02_Fill_the_Bounds.jpg)  
cancel

### Don't

Add custom padding. Your widget should go seamlessly edge-to-edge.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/03_Fill_the_Bounds.jpg)  
check_circle

### Do

Ensure your non-rectangular shape touches the grid on either the vertical or horizontal axis for visual consistency.  
![](https://developer.android.com/static/images/design/ui/mobile/widgets/04_Fill_the_Bounds.jpg)  
cancel

### Don't

Use fixed square shapes. Instead, use responsive rectangular containers that adapt to various grid dimensions.