---
title: Get started with FlexBox  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox/get-started
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Get started with FlexBox Stay organized with collections Save and categorize content based on your preferences.




This page describes how to implement basic `FlexBox` layouts.

## Set up project

1. Add the [`androidx.compose.foundation.layout`](/jetpack/androidx/versions) library to your project's
   `lib.versions.toml`.

   ```
   [versions]
   compose = "1.11.0-beta02"

   [libraries]
   androidx-compose-foundation-layout = { group = "androidx.compose.foundation", name = "foundation-layout", version.ref = "compose" }
   ```
2. Add the library dependency to your app's `build.gradle.kts`.

   ```
   dependencies {
       implementation(libs.androidx.compose.foundation.layout)
   }
   ```

## Create basic FlexBox layouts

**Example 1**: `FlexBox` lays out two `Text` elements that are centrally
aligned.

```
FlexBox(
    config = {
        direction(FlexDirection.Column)
        alignItems(FlexAlignItems.Center)
    }
) {
    Text(text = "Hello", fontSize = 48.sp)
    Text(text = "World!", fontSize = 48.sp)
}

FlexBoxSnippets.kt
```

![Hello World text composables stacked on top of each other in a basic FlexBox implementation.](/static/develop/ui/compose/images/layouts/adaptive/flexbox/basic-flexbox.png)

**Example 2**: `FlexBox` wraps five items onto two rows and grows them unequally
to fill the available space on each row. There is an `8.dp`
gap, both vertically and horizontally, between the items.

```
FlexBox(
    config = {
        wrap(FlexWrap.Wrap)
        gap(8.dp)
    }
) {
    // All boxes have an intrinsic width of 100.dp
    // Some grow to fill any remaining space on the row.
    RedRoundedBox()
    BlueRoundedBox()
    GreenRoundedBox(modifier = Modifier.flex { grow(1.0f) })
    OrangeRoundedBox(modifier = Modifier.flex { grow(1.0f) })
    PinkRoundedBox(modifier = Modifier.flex { grow(1.0f) })
}

FlexBoxSnippets.kt
```

![Two rows of colored items, with three unequally sized items distributed across the top row and two unequally sized items across the bottom row.](/static/develop/ui/compose/images/layouts/adaptive/flexbox/basic-flexbox-2.png)

To learn more about `FlexBox` behavior, see [Set container behavior](/develop/ui/compose/layouts/adaptive/flexbox/container-behavior) and [Set
item behavior](/develop/ui/compose/layouts/adaptive/flexbox/item-behavior).

[Previous

arrow\_back

Overview](/develop/ui/compose/layouts/adaptive/flexbox)

[Next

Set container behavior

arrow\_forward](/develop/ui/compose/layouts/adaptive/flexbox/container-behavior)