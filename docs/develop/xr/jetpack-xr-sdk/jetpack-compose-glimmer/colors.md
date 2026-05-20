---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/colors
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/colors
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, the color system is designed for additive displays
and real environments. Unlike standard Android themes, the [`Colors`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors) in
`GlimmerTheme` prioritize dark backgrounds with semi-transparency and vibrant
accents to ensure content is legible against unpredictable real-world lighting.

The system uses a three-part palette with primary, secondary, and neutral
colors. Neutral colors often serve as the physical surfaces of the spatial UI,
while the primary and secondary colors provide clear visual cues for interaction
and branding.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_colorscheme.png) **Figure 1.** An overview of the colors in the Jetpack Compose Glimmer theme.

Note that "On ..." colors such as *On Surface* aren't exposed through
`GlimmerTheme`. These colors are automatically calculated by the system based on
the background color.

However, the other colors are exposed through [`GlimmerTheme.colors`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors), with
values for each color role as described in the following table:

| Color role | Defaults |
|---|---|
| primary | #79ACFE |
| secondary | #4C88E9 |
| positive | #58FFA5 |
| negative | #FF8981 |
| background | [`Color.Black`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Color#Black()) |
| surface | #303030 |
| outline | #CBC9C8 |
| outlineVariant | #42434A |

Note that while [`background`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#background()), [`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#surface()), [`outline`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#outline()), and
[`outlineVariant`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#outlineVariant()) are marked as customizable, we strongly recommend that you
don't customize these values.