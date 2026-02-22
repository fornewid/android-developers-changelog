---
title: https://developer.android.com/design/ui/wear/guides/patterns/media/color
url: https://developer.android.com/design/ui/wear/guides/patterns/media/color
source: md.txt
---

# Color themes

The system creates a theme for your app's media controls by sourcing a seed color from the current media entity's artwork. The Material 3 Expressive dynamic theme algorithm generates a secondary, tertiary and neutral palette. This theme reflects across the rest of the app screens.

## Examples of color themes

The following sections show examples of color themes.

### Example 1

![](https://developer.android.com/static/wear/images/design/media-theme-palette-1.png)

<br />

Color palette (from artwork seed color)  
![](https://developer.android.com/static/wear/images/design/media-theme-controls-1.png)

<br />

Media controls  
![](https://developer.android.com/static/wear/images/design/media-theme-overflow-1.png)

<br />

Overflow app screen

<br />

### Example 2

![](https://developer.android.com/static/wear/images/design/media-theme-palette-2.png)

<br />

Color palette (from artwork seed color)  
![](https://developer.android.com/static/wear/images/design/media-theme-controls-2.png)

<br />

Media controls  
![](https://developer.android.com/static/wear/images/design/media-theme-overflow-2.png)

<br />

Overflow app screen

<br />

### Example 3

![](https://developer.android.com/static/wear/images/design/media-theme-palette-3.png)

<br />

Color palette (from artwork seed color)  
![](https://developer.android.com/static/wear/images/design/media-theme-controls-3.png)

<br />

Media controls  
![](https://developer.android.com/static/wear/images/design/media-theme-overflow-3.png)

<br />

Overflow app screen

<br />

## Fallback theme

To prepare for an instance where there is no artwork, or seed color available, the system uses a fallback theme based on the user's current watch face.

You can also choose to use a monochrome palette and seed color in your media app. In this case, the media entity's artwork doesn't appear on the media controls screen.

### System media controls (fallback)

![](https://developer.android.com/static/wear/images/design/media-theme-palette-system-fallback.png)

<br />

Color palette (from Watchface/SysUI color)  
![](https://developer.android.com/static/wear/images/design/media-theme-controls-system-theme-fallback.png)

<br />

Media controls  
![](https://developer.android.com/static/wear/images/design/media-theme-overflow-system-theme-fallback.png)

<br />

Overflow app screen

<br />

### Media app controls (fallback) - mono

![](https://developer.android.com/static/wear/images/design/media-theme-palette-mono-fallback.png)

<br />

Color palette (monochrome color palette)  
![](https://developer.android.com/static/wear/images/design/media-theme-controls-mono-fallback.png)

<br />

Media controls  
![](https://developer.android.com/static/wear/images/design/media-theme-overflow-mono-fallback.png)

<br />

Overflow app screen

<br />