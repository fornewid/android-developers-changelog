---
title: https://developer.android.com/design/ui/wear/guides/m2-5/styles/color
url: https://developer.android.com/design/ui/wear/guides/m2-5/styles/color
source: md.txt
---

# Color

Material design for Wear OS uses a darker color palette. In particular, you must use a black background for your app and tile.

## Color scheme

The Wear OS color scheme is created based on the baseline[Material Design color theme](https://material.io/design/color/the-color-system.html). You can use that theme as-is, or customize for your app.

This theme includes default colors for:

- Primary and secondary colors
- Variants of primary and secondary colors
- Additional UI colors, such as colors for backgrounds, surfaces, errors, typography, and iconography

![colors](https://developer.android.com/static/wear/images/design/color_3.png)

## Dark theme

All dark-theme colors should display elements with sufficient contrast, meeting[WCAG's AA standard](https://www.w3.org/WAI/standards-guidelines/wcag/)of at least 4.5:1 for body text when applied to all elevation surfaces.

### Use desaturated colors for accessibility

A dark theme should avoid using saturated colors, as they don't meet WCAG's accessibility standard of at least 4.5:1 for body text against dark surfaces. Saturated colors also produce optical vibrations against a dark background, which can cause eye strain. Instead, use desaturated colors as a more legible alternative.

![](https://developer.android.com/static/wear/images/design/color_4.png)

**Figure 1.**Less saturated colors from your color palette improve legibility.

![](https://developer.android.com/static/wear/images/design/color_4.png)

**Figure 2.**Avoid using saturated colors on a dark background.

### Primary color

A primary color is the color displayed most frequently across your app's screens and components. The baseline Material Design dark theme uses the 200 tone as a primary color. This meets the WCAG's AA standard of at least 4.5:1 for normal text, at all elevation surfaces.

![](https://developer.android.com/static/wear/images/design/color_6.png)

**Figure 3.**A sample primary palette in a dark theme. 1. Primary color indicator 2. Tonal variants

### Secondary color

A secondary color can be used to accent specific parts of your UI. In a dark theme, a secondary color can be desaturated to meet the 4.5:1 contrast level.

In figure 4, 1) indicates a secondary color indicator, and 2) indicates tonal variants.

![](https://developer.android.com/static/wear/images/design/color_5.png)

**Figure 4.**A sample secondary palette in a dark theme.

### Accent color

In a dark theme, dark surfaces occupy the majority of the UI. Accent colors are typically light (desaturated pastels) or bright (saturated, vivid colors). This helps accented elements stand out. Use accent colors sparingly to accent key elements, such as text or buttons.

**Finding accent colors** Use the[color palette generator](https://material.io/design/color/the-color-system.html#tools-for-picking-colors)to create or view a color theme. The color palette generator also creates tonal palettes, which are a range of light to dark color variations, created from your primary and secondary colors. Select variations of these for your dark theme.

In figure 5, 1) indicates a default theme primary color indicator and 2) indicates a dark theme primary color indicator.

![](https://developer.android.com/static/wear/images/design/color_2.png)

**Figure 5.**To provide more flexibility and usability in a dark theme, it's recommended to use lighter tones (200-50), rather than saturated tones (900-500).
| **Note:** To derive different colors from a source color, adjust the brightness value of the source color.

Use the darker spectrum of colors for large parts of the UI, such as the background color. Reserve lighter colors for accents and UI elements.