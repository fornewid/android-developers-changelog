---
title: Color themes  |  Wear  |  Android Developers
url: https://developer.android.com/design/ui/wear/guides/patterns/media/color
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [UI Design](https://developer.android.com/design/ui)
* [Wear](https://developer.android.com/design/ui/wear)
* [Guides](https://developer.android.com/design/ui/wear/guides/get-started)

# Color themes Stay organized with collections Save and categorize content based on your preferences.




The system creates a theme for your app's media controls by sourcing a seed
color from the current media entity's artwork. The Material 3 Expressive dynamic
theme algorithm generates a secondary, tertiary and neutral palette. This theme
reflects across the rest of the app screens.

## Examples of color themes

The following sections show examples of color themes.

### Example 1

![](/static/wear/images/design/media-theme-palette-1.png)

Color palette (from artwork seed color)

![](/static/wear/images/design/media-theme-controls-1.png)

Media controls

![](/static/wear/images/design/media-theme-overflow-1.png)

Overflow app screen

### Example 2

![](/static/wear/images/design/media-theme-palette-2.png)

Color palette (from artwork seed color)

![](/static/wear/images/design/media-theme-controls-2.png)

Media controls

![](/static/wear/images/design/media-theme-overflow-2.png)

Overflow app screen

### Example 3

![](/static/wear/images/design/media-theme-palette-3.png)

Color palette (from artwork seed color)

![](/static/wear/images/design/media-theme-controls-3.png)

Media controls

![](/static/wear/images/design/media-theme-overflow-3.png)

Overflow app screen

## Fallback theme

To prepare for an instance where there is no artwork, or seed color available,
the system uses a fallback theme based on the user's current watch face.

You can also choose to use a monochrome palette and seed color in your media
app. In this case, the media entity's artwork doesn't appear on the media
controls screen.

### System media controls (fallback)

![](/static/wear/images/design/media-theme-palette-system-fallback.png)

Color palette (from Watchface/SysUI color)

![](/static/wear/images/design/media-theme-controls-system-theme-fallback.png)

Media controls

![](/static/wear/images/design/media-theme-overflow-system-theme-fallback.png)

Overflow app screen

### Media app controls (fallback) - mono

![](/static/wear/images/design/media-theme-palette-mono-fallback.png)

Color palette (monochrome color palette)

![](/static/wear/images/design/media-theme-controls-mono-fallback.png)

Media controls

![](/static/wear/images/design/media-theme-overflow-mono-fallback.png)

Overflow app screen