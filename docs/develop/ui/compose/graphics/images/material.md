---
title: Icons  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/graphics/images/material
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Icons Stay organized with collections Save and categorize content based on your preferences.




The `Icon` composable is a convenient way to draw a single color icon on screen
that follows [Material Design guidelines](https://material.io/design/iconography/system-icons.html#grid-and-keyline-shapes). To use `Icon`, include
the [Compose Material](/jetpack/androidx/releases/compose-material) library (or the [Compose Material 3](/jetpack/androidx/releases/compose-material3) library).

For example, if you had a vector drawable that you wanted to load up with
Material defaults, you can use the `Icon` composable as follows:

```
Icon(
    painter = painterResource(R.drawable.baseline_directions_bus_24),
    contentDescription = stringResource(id = R.string.bus_content_description)
)

MaterialIconsSnippets.kt
```

By default, the `Icon` composable is tinted with `LocalContentColor.current` and
is `24.dp` in size. It also exposes a `tint` color parameter (which leverages
the same mechanism for tinting as described in the [Image tint](/develop/ui/compose/graphics/images/customize#tint-image) section). The
`Icon` composable is intended for use for small icon elements. You should use
the `Image` composable for more customization options.

**Note:** With Material there are two different styles of icons, Material Symbols
(New) and Material Icons (`material-icons`). The [Material Icon library](/reference/kotlin/androidx/compose/material/icons/package-summary)
includes a set of predefined `Icons` that can be used in Compose without needing
to import an SVG manually. However, this artifact is no longer maintained or
recommended for use in your apps, as it contains an older look and feel and can
also increase the build time of your apps
*significantly*. Instead, we recommend using [Google Font Icons](https://fonts.google.com/icons) and download
the XML file from the Android Tab to create an up-to-date Material Symbols style
Icon.


## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Resources in Compose](/develop/ui/compose/resources)
* [Accessibility in Compose](/develop/ui/compose/accessibility)
* [Loading images {:#loading-images}](/develop/ui/compose/graphics/images/loading)

[Previous

arrow\_back

ImageBitmap vs ImageVector](/develop/ui/compose/graphics/images/compare)

[Next

Customize an image

arrow\_forward](/develop/ui/compose/graphics/images/customize)