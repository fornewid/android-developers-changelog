---
title: Get started  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/layouts/adaptive/grid/get-started
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Get started Stay organized with collections Save and categorize content based on your preferences.



This page describes how to implement basic [`Grid`](/reference/kotlin/androidx/compose/foundation/layout/Grid.composable#Grid(kotlin.Function1,androidx.compose.ui.Modifier,kotlin.Function1)) layouts.

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

## Create a basic grid

The following example creates a basic 2x3 grid,
with the columns and rows having a fixed size of `100.dp`.

```
Grid(
    config = {
        repeat(2) {
            column(100.dp)
        }
        repeat(3) {
            row(100.dp)
        }
    }
) {
    Card1(containerColor = PastelRed)
    Card2(containerColor = PastelGreen)
    Card3(containerColor = PastelBlue)
    Card4(containerColor = PastelPink)
    Card5(containerColor = PastelOrange)
    Card6(containerColor = PastelYellow)
}

DefineGrid.kt
```

![A basic grid consists of rows and columns with fixed size.](/static/develop/ui/compose/images/layouts/adaptive/grid/six-cards-in-grid.png)


**Figure 1**.
A basic grid consists of rows and columns with fixed size.

To learn how to implement more advanced grids,
see [Set container properties](/develop/ui/compose/layouts/adaptive/grid/container-properties) and [Set item properties](/develop/ui/compose/layouts/adaptive/grid/item-properties).

[Previous

arrow\_back

Overview](/develop/ui/compose/layouts/adaptive/grid)

[Next

Set container properties

arrow\_forward](/develop/ui/compose/layouts/adaptive/grid/container-properties)