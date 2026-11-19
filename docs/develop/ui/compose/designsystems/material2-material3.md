---
title: https://developer.android.com/develop/ui/compose/designsystems/material2-material3
url: https://developer.android.com/develop/ui/compose/designsystems/material2-material3
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/designsystems/llms.txt

> [!CAUTION]
> **Caution:** Compose Material 2 (`androidx.compose.material:material`) is deprecated. Migrate your app to [Compose Material 3](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt) (`androidx.compose.material3:material3` 1.5.0 or later).

[Material Design 3](https://m3.material.io/) is the next evolution of Material Design. It includes
updated theming, components, and Material You personalization features like
dynamic color. It's an update to [Material Design 2](https://material.io/) and is cohesive with the
new visual style and system UI on Android 12 and higher.

This guide focuses on migrating from the [Compose Material
(androidx.compose.material) Jetpack library](https://developer.android.com/jetpack/androidx/releases/compose-material) to the [Compose Material 3
(androidx.compose.material3) Jetpack library](https://developer.android.com/jetpack/androidx/releases/compose-material3).

> [!NOTE]
> **Note:** This guide uses abbreviation "M3" to refer to the interchangeable terms: "Material 3", "Material Design 3", "Material You", and the Compose Material 3 (androidx.compose.material3) Jetpack library. The abbreviation "M2" is used to refer to the interchangeable terms: "Material 2", "Material Design 2", and the Compose Material (`androidx.compose.material`) Jetpack library.

## Approaches

In general, **you should not use both M2 and M3 in a single app long-term**.
This is because the two design systems and respective libraries differ
significantly in terms of their UX/UI designs and Compose implementations.

Your app may use a design system, such as one created using Figma. In such
cases, we also highly recommend that you or your design team migrate it from M2
to M3 *before* starting the Compose migration. It doesn't make sense to migrate
an app to M3 if its UX/UI design is based on M2.

Furthermore, your approach to migration should take your app's
size, complexity, and UX/UI design into account. Doing so helps you to
minimize the impact on your codebase. Take a phased approach to
migration.

> [!NOTE]
> **Note:** If you're starting a new app instead of migrating an existing app from M2 to M3, we recommend that you use M3 from the beginning.

### When to migrate

You should ideally start the migration as soon as possible. However, it's
important to consider whether your app is in a realistic position to
**fully** migrate from M2 to M3. There are some *blocker* scenarios to
consider investigating before you start:

| Scenario | Recommended approach |
|---|---|
| Your app has no significant blockers. | Begin phased migration. |
| Your app uses a component from M2 that isn't available in M3 yet. See the [Components and layouts](https://developer.android.com/develop/ui/compose/designsystems/material2-material3.md.txt#components-and) section. | Begin phased migration. |
| You or your design team haven't migrated the app's design system from M2 to M3. | Migrate the design system from M2 to M3, then begin phased migration. |

Even if you're affected by the preceding scenarios, you should take a phased
approach to migration before committing and releasing an app update. In these
cases, you would use M2 and M3 side-by-side, and gradually phase out M2 while
migrating to M3.

### Phased approach

The general steps to a phased migration are as follows:

1. Add the M3 dependency alongside the M2 dependency.
2. Add the M3 versions of your app's themes alongside the M2 versions of your app's themes.
3. Migrate individual modules, screens, or composables to M3, depending on the size and complexity of your app (see the following sections for details).
4. Once fully migrated, remove the M2 versions of your app's themes.
5. Remove the M2 dependency.

## Dependencies

M3 has a separate package and version from M2:

### M2

```kotlin
implementation "androidx.compose.material:material:$m2-version"
```

### M3

```kotlin
implementation "androidx.compose.material3:material3:$m3-version"
```

See the latest M3 versions on the [Compose Material 3 releases page](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt).

Related Material artifacts outside of the main `material3` library use the
following packages and versions:

| Library | Package and version |
|---|---|
| [Compose Material Icons](https://developer.android.com/reference/kotlin/androidx/compose/material/icons/package-summary.md.txt) | `androidx.compose.material:material-icons-*:$m2-version` |
| [Compose Material 3 Ripple](https://developer.android.com/reference/kotlin/androidx/compose/material3/ripple/package-summary.md.txt) | `androidx.compose.material3:material3-ripple:$m3-version` |

In Material 3 1.5.0, [Compose Material 3 Ripple](https://developer.android.com/reference/kotlin/androidx/compose/material3/ripple/package-summary.md.txt)
(`androidx.compose.material3:material3-ripple`) replaces
`androidx.compose.material:material-ripple` and adds inset focus ring support
through [`RippleNodeConfiguration.FocusConfiguration.InsetRing`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ripple/RippleNodeConfiguration.FocusConfiguration.InsetRing.md.txt). If your
M2 app customizes ripples using the deprecated `RippleTheme` or
`rememberRipple` APIs, see [Migrate to `Indication` and `Ripple` APIs](https://developer.android.com/develop/ui/compose/touch-input/user-interactions/migrate-indication-ripple.md.txt).

## Experimental APIs

Some M3 APIs are considered experimental. In such cases, you need to opt
in at the function or file level using the
[`ExperimentalMaterial3Api`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ExperimentalMaterial3Api.md.txt) annotation:

```kotlin
import androidx.compose.material3.ExperimentalMaterial3Api

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun AppComposable() {
    // M3 composables
}
```

## Theming

In both M2 and M3, the theme composable is named `MaterialTheme` but the import
packages and parameters differ:

### M2

```kotlin
import androidx.compose.material.MaterialTheme

MaterialTheme(
    colors = AppColors,
    typography = AppTypography,
    shapes = AppShapes
) {
    // M2 content
}
```

### M3

```kotlin
import androidx.compose.material3.MaterialTheme

MaterialTheme(
    colorScheme = AppColorScheme,
    typography = AppTypography,
    shapes = AppShapes
) {
    // M3 content
}
```

> [!NOTE]
> **Note:** The parameters are different for the two types of `MaterialTheme`. This results in errors after the change. See the [Color](https://developer.android.com/develop/ui/compose/designsystems/material2-material3.md.txt#color), [Typography](https://developer.android.com/develop/ui/compose/designsystems/material2-material3.md.txt#typography) and [Shape](https://developer.android.com/develop/ui/compose/designsystems/material2-material3.md.txt#shape) sections on how to resolve this.

### Color

![Comparison of the M2 to M3 color systems](https://developer.android.com/static/develop/ui/compose/images/migration-color-update.png) **Figure 1**. M2 color system (left) versus M3 color system (right).

The [color system](https://m3.material.io/styles/color/overview) in M3 is significantly different to M2. The
number of color parameters has increased, they have different names, and they
map differently to M3 components. In Compose, this applies to the M2
[`Colors`](https://developer.android.com/reference/kotlin/androidx/compose/material/Colors.md.txt) class, the M3 [`ColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ColorScheme.md.txt) class, and related functions:

### M2

```kotlin
import androidx.compose.material.lightColors
import androidx.compose.material.darkColors

val AppLightColors = lightColors(
    // M2 light Color parameters
)
val AppDarkColors = darkColors(
    // M2 dark Color parameters
)
val AppColors = if (darkTheme) {
    AppDarkColors
} else {
    AppLightColors
}
```

### M3

```kotlin
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.darkColorScheme

val AppLightColorScheme = lightColorScheme(
    // M3 light Color parameters
)
val AppDarkColorScheme = darkColorScheme(
    // M3 dark Color parameters
)
val AppColorScheme = if (darkTheme) {
    AppDarkColorScheme
} else {
    AppLightColorScheme
}
```

Given the significant differences between the M2 and M3 color systems, there's
no reasonable mapping for [`Color`](https://developer.android.com/reference/kotlin/androidx/compose/material/Colors.md.txt#isLight()) parameters. Instead, use the [Material
Theme Builder tool](https://m3.material.io/theme-builder) to generate an M3 color scheme. Use the M2
colors as *core* source colors in the tool, which the tool expands into tonal
palettes used by the M3 color scheme. The following mappings are recommended as
a starting point:

| M2 | Material Theme Builder |
|---|---|
| `primary` | Primary |
| `primaryVariant` | Secondary |
| `secondary` | Tertiary |
| `surface` or `background` | Neutral |

> [!NOTE]
> **Note:** Some M2 and M3 colors are named the same, such as primary and secondary. However, their hex code values may not be the same. This is because Material Theme Builder uses an algorithm to generate tonal palettes from the M2 colors, which the tools use in the M3 color scheme.

![M2 colors used in Material Theme Builder to generate an M3 color scheme](https://developer.android.com/static/develop/ui/compose/images/migration-colorscheme-update.png) **Figure 2**. Jetchat's M2 colors used in Material Theme Builder to generate an M3 color scheme.

You can copy the color hex code values for light and dark themes from the tool
and use them to implement an M3 ColorScheme instance. Alternatively, Material
Theme Builder can export Compose code.

#### `isLight`

Unlike the M2 `Colors` class, the M3 `ColorScheme` class doesn't include an
[`isLight`](https://developer.android.com/reference/kotlin/androidx/compose/material/Colors.md.txt#isLight()) parameter. In general, you should try and model whatever needs
this information at the theme level. For example:

### M2

```kotlin
import androidx.compose.material.lightColors
import androidx.compose.material.darkColors
import androidx.compose.material.MaterialTheme

@Composable
private fun AppTheme(
  darkTheme: Boolean = isSystemInDarkTheme(),
  content: @Composable () -> Unit
) {
  val colors = if (darkTheme) darkColors(...) else lightColors(...)
  MaterialTheme(
      colors = colors,
      content = content
  )
}

@Composable
fun AppComposable() {
    AppTheme {
        val cardElevation = if (MaterialTheme.colors.isLight) 0.dp else 4.dp
        ...
    }
}
```

### M3

```kotlin
import androidx.compose.material3.lightColorScheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.MaterialTheme

val LocalCardElevation = staticCompositionLocalOf { Dp.Unspecified }
@Composable
private fun AppTheme(
   darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
   val cardElevation = if (darkTheme) 4.dp else 0.dp
    CompositionLocalProvider(LocalCardElevation provides cardElevation) {
        val colorScheme = if (darkTheme) darkColorScheme(...) else lightColorScheme(...)
        MaterialTheme(
            colorScheme = colorScheme,
            content = content
        )
    }
}

@Composable
fun AppComposable() {
    AppTheme {
        val cardElevation = LocalCardElevation.current
        ...
    }
}
```

See the [Custom design systems in Compose guide](https://developer.android.com/develop/ui/compose/designsystems/custom.md.txt) for more information.

#### Dynamic color

A new feature in M3 is [dynamic color](https://m3.material.io/styles/color/dynamic-color/overview). Instead of using custom
colors, an M3 `ColorScheme` can make use of device wallpaper colors on Android
12 and higher, using the following functions:

- [`dynamicLightColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#dynamiclightcolorscheme)
- [`dynamicDarkColorScheme`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#dynamicdarkcolorscheme)

> [!NOTE]
> **Note:** Even if you choose to use a dynamic color scheme, you almost always need a fallback custom color scheme given the Android 12 and higher restriction. See [Jetchat](https://github.com/android/compose-samples/blob/main/Jetchat/app/src/main/java/com/example/compose/jetchat/theme/Themes.kt#L91) as an example.

### Typography

![Comparison of M2 and M3 typography systems](https://developer.android.com/static/develop/ui/compose/images/migration-typography-update.png) **Figure 3**. M3 typography system (left) versus M2 typography system (right)

The [typography system](https://m3.material.io/styles/typography/overview) in M3 is different to M2. The number of
typography parameters is roughly the same, but they have different names and
they map differently to M3 components. In Compose, this applies to the M2
[`Typography`](https://developer.android.com/reference/kotlin/androidx/compose/material/Typography.md.txt) class and the M3 [`Typography`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Typography.md.txt) class:

### M2

```kotlin
import androidx.compose.material.Typography

val AppTypography = Typography(
    // M2 TextStyle parameters
)
```

### M3

```kotlin
import androidx.compose.material3.Typography

val AppTypography = Typography(
    // M3 TextStyle parameters
)
```

The following [`TextStyle`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/TextStyle.md.txt) parameter mappings are recommended as a starting
point:

| M2 | M3 |
|---|---|
| `h1` | `displayLarge` |
| `h2` | `displayMedium` |
| `h3` | `displaySmall` |
| N/A | `headlineLarge` |
| `h4` | `headlineMedium` |
| `h5` | `headlineSmall` |
| `h6` | `titleLarge` |
| `subtitle1` | `titleMedium` |
| `subtitle2` | `titleSmall` |
| `body1` | `bodyLarge` |
| `body2` | `bodyMedium` |
| `caption` | `bodySmall` |
| `button` | `labelLarge` |
| N/A | `labelMedium` |
| `overline` | `labelSmall` |

> [!NOTE]
> **Note:** Unlike the M2 `Typography` class, the M3 `Typography` class doesn't include a `defaultFontFamily` parameter. You'll need to use the `fontFamily` parameter in each of the individual `TextStyles` instead.

### Shape

![Comparison of M2 and M3 shape systems](https://developer.android.com/static/develop/ui/compose/images/migration-shape-update.png) **Figure 4**. M2 shape system (left) versus M3 shape system (right).

The [shape system](https://m3.material.io/styles/shape/overview) in M3 is different to M2. The number of shape
parameters has increased, they're named differently and they map differently to
M3 components. In Compose, this applies to the M2 [`Shapes`](https://developer.android.com/reference/kotlin/androidx/compose/material/Shapes.md.txt) class and the
M3 [`Shapes`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Shapes.md.txt) class:

### M2

```kotlin
import androidx.compose.material.Shapes

val AppShapes = Shapes(
    // M2 Shape parameters
)
```

### M3

```kotlin
import androidx.compose.material3.Shapes

val AppShapes = Shapes(
    // M3 Shape parameters
)
```

The following [`Shape`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/Shape.md.txt) parameter mappings are recommended as a starting
point:

| M2 | M3 |
|---|---|
| N/A | `extraSmall` |
| `small` | `small` |
| `medium` | `medium` |
| `large` | `large` |
| N/A | `extraLarge` |

> [!NOTE]
> **Note:** The M3 shape system also defines `none` and `full` styles which are constant and not part of the `Shapes` class. Use [`RectangleShape`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/package-summary.md.txt#RectangleShape()) and [`CircleShape`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/shape/package-summary.md.txt#CircleShape()) respectively for these.

## Components and layouts

Most components and layouts from M2 are available in M3. There are, however,
some missing as well as new ones that didn't exist in M2. Furthermore, some M3
components have more variations than their equivalents in M2. In general, the M3
API surfaces are designed to be as similar as possible to their closest
equivalents in M2.

Given the updated color, typography and shape systems, M3 components tend to map
differently to the new theming values. It's a good idea to check out the [tokens
directory](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens/) in the Compose Material 3 source code as a source of
truth for these mappings.

While some components require special considerations, the following function
mappings are recommended as a starting point:

**Missing APIs**:

| M2 | M3 |
|---|---|
| [`androidx.compose.material.swipeable`](https://developer.android.com/reference/kotlin/androidx/compose/material/swipeable.modifier) | Not available yet |

**Replaced APIs**:

| M2 | M3 |
|---|---|
| [`androidx.compose.material.BackdropScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/BackdropScaffold.composable.md.txt) | No M3 equivalent, migrate to [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Scaffold.composable.md.txt) or [`BottomSheetScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/BottomSheetScaffold.composable.md.txt) instead |
| [`androidx.compose.material.BottomDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomDrawer.composable) | No M3 equivalent, migrate to [`ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable.md.txt) instead |

**Renamed APIs**:

| M2 | M3 |
|---|---|
| [`androidx.compose.material.BottomNavigation`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomNavigation.composable.md.txt) | [`androidx.compose.material3.NavigationBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationBar.composable.md.txt) |
| [`androidx.compose.material.BottomNavigationItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomNavigationItem.composable.md.txt) | [`androidx.compose.material3.NavigationBarItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationBarItem.composable.md.txt) |
| [`androidx.compose.material.Chip`](https://developer.android.com/reference/kotlin/androidx/compose/material/Chip.composable.md.txt) | [`androidx.compose.material3.AssistChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/AssistChip.composable.md.txt) or [`androidx.compose.material3.SuggestionChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SuggestionChip.composable.md.txt) |
| [`androidx.compose.material.ModalBottomSheetLayout`](https://developer.android.com/reference/kotlin/androidx/compose/material/ModalBottomSheetLayout.composable) | [`androidx.compose.material3.ModalBottomSheet`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalBottomSheet.composable.md.txt) |
| [`androidx.compose.material.ModalDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material/ModalDrawer.composable.md.txt) | [`androidx.compose.material3.ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalNavigationDrawer.composable.md.txt) |

**All other APIs**:

| M2 | M3 |
|---|---|
| [`androidx.compose.material.AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material/AlertDialog.composable) | [`androidx.compose.material3.AlertDialog`](https://developer.android.com/reference/kotlin/androidx/compose/material3/AlertDialog.composable.md.txt) |
| [`androidx.compose.material.Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material/Badge.composable.md.txt) | [`androidx.compose.material3.Badge`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Badge.composable) |
| [`androidx.compose.material.BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material/BadgedBox.composable.md.txt) | [`androidx.compose.material3.BadgedBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/BadgedBox.composable.md.txt) |
| [`androidx.compose.material.BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomAppBar.composable.md.txt) | [`androidx.compose.material3.BottomAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/BottomAppBar.composable.md.txt) |
| [`androidx.compose.material.BottomSheetScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomSheetScaffold.composable.md.txt) | [`androidx.compose.material3.BottomSheetScaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/BottomSheetScaffold.composable.md.txt) |
| [`androidx.compose.material.Button`](https://developer.android.com/reference/kotlin/androidx/compose/material/Button.composable.md.txt) | [`androidx.compose.material3.Button`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Button.composable.md.txt) |
| [`androidx.compose.material.Card`](https://developer.android.com/reference/kotlin/androidx/compose/material/Card.composable) | [`androidx.compose.material3.Card`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Card.composable.md.txt) |
| [`androidx.compose.material.Checkbox`](https://developer.android.com/reference/kotlin/androidx/compose/material/Checkbox.composable) | [`androidx.compose.material3.Checkbox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Checkbox.composable.md.txt) |
| [`androidx.compose.material.CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material/CircularProgressIndicator.composable) | [`androidx.compose.material3.CircularProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/CircularProgressIndicator.composable.md.txt) |
| [`androidx.compose.material.Divider`](https://developer.android.com/reference/kotlin/androidx/compose/material/Divider.composable.md.txt) | [`androidx.compose.material3.Divider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Divider.composable.md.txt) |
| [`androidx.compose.material.DropdownMenu`](https://developer.android.com/reference/kotlin/androidx/compose/material/DropdownMenu.composable.md.txt) | [`androidx.compose.material3.DropdownMenu`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DropdownMenu.composable.md.txt) |
| [`androidx.compose.material.DropdownMenuItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/DropdownMenuItem.composable.md.txt) | [`androidx.compose.material3.DropdownMenuItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/DropdownMenuItem.composable.md.txt) |
| [`androidx.compose.material.ExposedDropdownMenuBox`](https://developer.android.com/reference/kotlin/androidx/compose/material/ExposedDropdownMenuBox.composable.md.txt) | [`androidx.compose.material3.ExposedDropdownMenuBox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ExposedDropdownMenuBox.composable.md.txt) |
| [`androidx.compose.material.ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/ExtendedFloatingActionButton.composable.md.txt) | [`androidx.compose.material3.ExtendedFloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ExtendedFloatingActionButton.composable.md.txt) |
| [`androidx.compose.material.FilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material/FilterChip.composable.md.txt) | [`androidx.compose.material3.FilterChip`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FilterChip.composable.md.txt) |
| [`androidx.compose.material.FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/FloatingActionButton.composable.md.txt) | [`androidx.compose.material3.FloatingActionButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/FloatingActionButton.composable.md.txt) |
| [`androidx.compose.material.Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material/Icon.composable.md.txt) | [`androidx.compose.material3.Icon`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Icon.composable.md.txt) |
| [`androidx.compose.material.IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/IconButton.composable.md.txt) | [`androidx.compose.material3.IconButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconButton.composable.md.txt) |
| [`androidx.compose.material.IconToggleButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/IconToggleButton.composable) | [`androidx.compose.material3.IconToggleButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/IconToggleButton.composable.md.txt) |
| [`androidx.compose.material.LeadingIconTab`](https://developer.android.com/reference/kotlin/androidx/compose/material/LeadingIconTab.composable.md.txt) | [`androidx.compose.material3.LeadingIconTab`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LeadingIconTab.composable.md.txt) |
| [`androidx.compose.material.LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material/LinearProgressIndicator.composable.md.txt) | [`androidx.compose.material3.LinearProgressIndicator`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LinearProgressIndicator.composable.md.txt) |
| [`androidx.compose.material.ListItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/ListItem.composable.md.txt) | [`androidx.compose.material3.ListItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ListItem.composable.md.txt) |
| [`androidx.compose.material.NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material/NavigationRail.composable.md.txt) | [`androidx.compose.material3.NavigationRail`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRail.composable.md.txt) |
| [`androidx.compose.material.NavigationRailItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/NavigationRailItem.composable) | [`androidx.compose.material3.NavigationRailItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationRailItem.composable.md.txt) |
| [`androidx.compose.material.OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/OutlinedButton.composable.md.txt) | [`androidx.compose.material3.OutlinedButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/OutlinedButton.composable.md.txt) |
| [`androidx.compose.material.OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/OutlinedTextField.composable.md.txt) | [`androidx.compose.material3.OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/OutlinedTextField.composable.md.txt) |
| [`androidx.compose.material.RadioButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/RadioButton.composable) | [`androidx.compose.material3.RadioButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/RadioButton.composable.md.txt) |
| [`androidx.compose.material.RangeSlider`](https://developer.android.com/reference/kotlin/androidx/compose/material/RangeSlider.composable) | [`androidx.compose.material3.RangeSlider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/RangeSlider.composable.md.txt) |
| [`androidx.compose.material.Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/Scaffold.composable.md.txt) | [`androidx.compose.material3.Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Scaffold.composable.md.txt) |
| [`androidx.compose.material.ScrollableTabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material/ScrollableTabRow.composable.md.txt) | [`androidx.compose.material3.ScrollableTabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ScrollableTabRow.composable.md.txt) |
| [`androidx.compose.material.Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material/Slider.composable.md.txt) | [`androidx.compose.material3.Slider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Slider.composable.md.txt) |
| [`androidx.compose.material.Snackbar`](https://developer.android.com/reference/kotlin/androidx/compose/material/Snackbar.composable.md.txt) | [`androidx.compose.material3.Snackbar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Snackbar.composable.md.txt) |
| [`androidx.compose.material.Switch`](https://developer.android.com/reference/kotlin/androidx/compose/material/Switch.composable.md.txt) | [`androidx.compose.material3.Switch`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Switch.composable.md.txt) |
| [`androidx.compose.material.Tab`](https://developer.android.com/reference/kotlin/androidx/compose/material/Tab.composable) | [`androidx.compose.material3.Tab`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Tab.composable.md.txt) |
| [`androidx.compose.material.TabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material/TabRow.composable.md.txt) | [`androidx.compose.material3.TabRow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TabRow.composable.md.txt) |
| [`androidx.compose.material.Text`](https://developer.android.com/reference/kotlin/androidx/compose/material/Text.composable.md.txt) | [`androidx.compose.material3.Text`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Text.composable.md.txt) |
| [`androidx.compose.material.TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material/TextButton.composable.md.txt) | [`androidx.compose.material3.TextButton`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextButton.composable.md.txt) |
| [`androidx.compose.material.TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/TextField.composable.md.txt) | [`androidx.compose.material3.TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable.md.txt) |
| [`androidx.compose.material.TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material/TopAppBar.composable) | [`androidx.compose.material3.TopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TopAppBar.composable.md.txt) |
| [`androidx.compose.material.TriStateCheckbox`](https://developer.android.com/reference/kotlin/androidx/compose/material/TriStateCheckbox.composable.md.txt) | [`androidx.compose.material3.TriStateCheckbox`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TriStateCheckbox.composable.md.txt) |

See the latest M3 components and layouts on the [Compose Material 3 API
reference overview](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#overview), and keep an eye out on the [releases page](https://developer.android.com/jetpack/androidx/releases/compose-material3.md.txt) for new
and updated APIs.

### Scaffold, snackbars and navigation drawer

![Comparison of M2 and M3 scaffold with snackbar and navigation drawer](https://developer.android.com/static/develop/ui/compose/images/migration-scaffold-update.gif) **Figure 5**. M2 scaffold with snackbar and navigation drawer (left) versus M3 scaffold with snackbar and navigation drawer (right).

Scaffold in M3 is different to M2. In both M2 and M3, the main layout composable
is named `Scaffold` but the import packages and parameters differ:

### M2

```kotlin
import androidx.compose.material.Scaffold

Scaffold(
    // M2 scaffold parameters
)
```

### M3

```kotlin
import androidx.compose.material3.Scaffold

Scaffold(
    // M3 scaffold parameters
)
```

The M2 [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material/Scaffold.composable.md.txt) contains a `backgroundColor` parameter is now named to
`containerColor` in the M3 [`Scaffold`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Scaffold.composable.md.txt):

### M2

```kotlin
import androidx.compose.material.Scaffold

Scaffold(
    backgroundColor = ...,
    content = { ... }
)
```

### M3

```kotlin
import androidx.compose.material3.Scaffold

Scaffold(
    containerColor = ...,
    content = { ... }
)
```

The M2 [`ScaffoldState`](https://developer.android.com/reference/kotlin/androidx/compose/material/ScaffoldState.md.txt) class no longer exists in M3 as it contains a
[`drawerState`](https://developer.android.com/reference/kotlin/androidx/compose/material/ScaffoldState.md.txt#drawerState()) parameter which is no longer needed. To show snackbars with
the M3 `Scaffold`, use [`SnackbarHostState`](https://developer.android.com/reference/kotlin/androidx/compose/material/SnackbarHostState.md.txt) instead:

### M2

```kotlin
import androidx.compose.material.Scaffold
import androidx.compose.material.rememberScaffoldState

val scaffoldState = rememberScaffoldState()
val scope = rememberCoroutineScope()

Scaffold(
    scaffoldState = scaffoldState,
    content = {
        ...
        scope.launch {
            scaffoldState.snackbarHostState.showSnackbar(...)
        }
    }
)
```

### M3

```kotlin
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState

val snackbarHostState = remember { SnackbarHostState() }
val scope = rememberCoroutineScope()

Scaffold(
    snackbarHost = { SnackbarHost(snackbarHostState) },
    content = {
        ...
        scope.launch {
            snackbarHostState.showSnackbar(...)
        }
    }
)
```

> [!NOTE]
> **Note:** The [`SnackbarData`](https://developer.android.com/reference/kotlin/androidx/compose/material/SnackbarData.md.txt) class in M2 has been split into [`SnackbarData`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarData.md.txt) and [`SnackbarVisuals`](https://developer.android.com/reference/kotlin/androidx/compose/material3/SnackbarVisuals.md.txt) in M3.

All of the `drawer*` parameters from the M2 `Scaffold` have been removed from
the M3 `Scaffold`. These include parameters such as `drawerShape` and
`drawerContent`. To show a drawer with the M3 `Scaffold`, use a navigation
drawer composable, such as [`ModalNavigationDrawer`](https://developer.android.com/reference/kotlin/androidx/compose/material3/ModalNavigationDrawer.composable.md.txt), instead:

### M2

```kotlin
import androidx.compose.material.DrawerValue
import
import androidx.compose.material.Scaffold
import androidx.compose.material.rememberDrawerState
import androidx.compose.material.rememberScaffoldState

val scaffoldState = rememberScaffoldState(
    drawerState = rememberDrawerState(DrawerValue.Closed)
)
val scope = rememberCoroutineScope()

Scaffold(
    scaffoldState = scaffoldState,
    drawerContent = { ... },
    drawerGesturesEnabled = ...,
    drawerShape = ...,
    drawerElevation = ...,
    drawerBackgroundColor = ...,
    drawerContentColor = ...,
    drawerScrimColor = ...,
    content = {
        ...
        scope.launch {
            scaffoldState.drawerState.open()
        }
    }
)
```

### M3

```kotlin
import androidx.compose.material3.DrawerValue
import androidx.compose.material3.ModalDrawerSheet
import androidx.compose.material3.ModalNavigationDrawer
import androidx.compose.material3.Scaffold
import androidx.compose.material3.rememberDrawerState

val drawerState = rememberDrawerState(DrawerValue.Closed)
val scope = rememberCoroutineScope()

ModalNavigationDrawer(
    drawerState = drawerState,
    drawerContent = {
        ModalDrawerSheet(
            drawerShape = ...,
            drawerTonalElevation = ...,
            drawerContainerColor = ...,
            drawerContentColor = ...,
            content = { ... }
        )
    },
    gesturesEnabled = ...,
    scrimColor = ...,
    content = {
        Scaffold(
            content = {
                ...
                scope.launch {
                    drawerState.open()
                }
            }
        )
    }
)
```

### Top app bar

![Comparison of M2 and M3 scaffold with top app bar and scrolled list](https://developer.android.com/static/develop/ui/compose/images/migration-topbar-update.png) **Figure 6**. M2 scaffold with top app bar and scrolled list (left) versus M3 scaffold with top app bar and scrolled list (right)

[Top app bars](https://m3.material.io/components/top-app-bar/overview) in M3 are different to those in M2. In both M2
and M3, the main top app bar composable is named `TopAppBar` but the import
packages and parameters differ:

### M2

```kotlin
import androidx.compose.material.TopAppBar

TopAppBar(...)
```

### M3

```kotlin
import androidx.compose.material3.TopAppBar

TopAppBar(...)
```

Consider using the M3 [`CenterAlignedTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/CenterAlignedTopAppBar.composable.md.txt) if you were previously
centering content within the M2 `TopAppBar`. It's good to be aware of the
[`MediumTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/MediumTopAppBar.composable.md.txt) and [`LargeTopAppBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/LargeTopAppBar.composable.md.txt) as well.

M3 top app bars contain a new `scrollBehavior` parameter to provide different
functionality on scroll through the [`TopAppBarScrollBehavior`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TopAppBarScrollBehavior.md.txt) class, such
as changing elevation. This works in conjunction with scrolling content using
[`Modifier.nestedScroll`](https://developer.android.com/reference/kotlin/androidx/compose/ui/input/nestedscroll/package-summary.md.txt#nestedscroll). This was possible in the M2 `TopAppBar` by
manually changing the `elevation` parameter:

### M2

```kotlin
import androidx.compose.material.AppBarDefaults
import androidx.compose.material.Scaffold
import androidx.compose.material.TopAppBar

val state = rememberLazyListState()
val isAtTop by remember {
    derivedStateOf {
        state.firstVisibleItemIndex == 0 && state.firstVisibleItemScrollOffset == 0
    }
}

Scaffold(
    topBar = {
        TopAppBar(
            elevation = if (isAtTop) {
                0.dp
            } else {
                AppBarDefaults.TopAppBarElevation
            },
            ...
        )
    },
    content = {
        LazyColumn(state = state) { ... }
    }
)

```

### M3

```kotlin
import androidx.compose.material3.Scaffold
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.TopAppBarDefaults

val scrollBehavior = TopAppBarDefaults.pinnedScrollBehavior()

Scaffold(
    modifier = Modifier.nestedScroll(scrollBehavior.nestedScrollConnection),
    topBar = {
        TopAppBar(
            scrollBehavior = scrollBehavior,
            ...
        )
    },
    content = {
        LazyColumn { ... }
    }
)

```

### Bottom navigation and the navigation bar

![Comparison of M2 bottom navigation and M3 navigation bar](https://developer.android.com/static/develop/ui/compose/images/migration-bottomnav-update.png) **Figure 7**. M2 bottom navigation (left) versus M3 navigation bar (right).

Bottom navigation in M2 has been renamed to [navigation bar](https://m3.material.io/components/navigation-bar/overview) in
M3. In M2 there are the [`BottomNavigation`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomNavigation.composable.md.txt) and
[`BottomNavigationItem`](https://developer.android.com/reference/kotlin/androidx/compose/material/BottomNavigationItem.composable.md.txt) composables, while in M3 there are the
[`NavigationBar`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationBar.composable.md.txt) and [`NavigationBarItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/NavigationBarItem.composable.md.txt) composables:

### M2

```kotlin
import androidx.compose.material.BottomNavigation
import androidx.compose.material.BottomNavigationItem

BottomNavigation {
    BottomNavigationItem(...)
    BottomNavigationItem(...)
    BottomNavigationItem(...)
}

```

### M3

```kotlin
import androidx.compose.material3.NavigationBar
import androidx.compose.material3.NavigationBarItem

NavigationBar {
    NavigationBarItem(...)
    NavigationBarItem(...)
    NavigationBarItem(...)
}

```

### Buttons, icon buttons and FABs

![Comparison of M2 and M3 buttons](https://developer.android.com/static/develop/ui/compose/images/migration-buttons-update.png) **Figure 8**. M2 buttons (left) versus M3 buttons (right)

[Buttons, icon buttons and floating action buttons (FABs)](https://m3.material.io/components/all-buttons) in M3
are different to those in M2. M3 includes all of the M2 button composables:

### M2

```kotlin
import androidx.compose.material.Button
import androidx.compose.material.ExtendedFloatingActionButton
import androidx.compose.material.FloatingActionButton
import androidx.compose.material.IconButton
import androidx.compose.material.IconToggleButton
import androidx.compose.material.OutlinedButton
import androidx.compose.material.TextButton

// M2 buttons
Button(...)
OutlinedButton(...)
TextButton(...)
// M2 icon buttons
IconButton(...)
IconToggleButton(...)
// M2 FABs
FloatingActionButton(...)
ExtendedFloatingActionButton(...)
```

### M3

```kotlin
import androidx.compose.material3.Button
import androidx.compose.material3.ExtendedFloatingActionButton
import androidx.compose.material3.FloatingActionButton
import androidx.compose.material3.IconButton
import androidx.compose.material3.IconToggleButton
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.TextButton

// M3 buttons
Button(...)
OutlinedButton(...)
TextButton(...)
// M3 icon buttons
IconButton(...)
IconToggleButton(...)
// M3 FABs
FloatingActionButton(...)
ExtendedFloatingActionButton(...)
```

M3 also includes new button variations. Check them out on the [Compose Material
3 API reference overview](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#components).

### Switch

![Comparison of M2 and M3 switches](https://developer.android.com/static/develop/ui/compose/images/migration-switch-update.png) **Figure 9**. M2 switch (left) versus M3 switch (right).

[Switch](https://m3.material.io/components/switch/overview) in M3 is different to M2. In both M2 and M3, the switch
composable is named `Switch` but the import packages differ:

### M2

```kotlin
import androidx.compose.material.Switch

Switch(...)
```

### M3

```kotlin
import androidx.compose.material3.Switch

Switch(...)
```

### Text fields

In Compose 1.13, M2's value-based [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/TextField.composable.md.txt) and
[`OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material/OutlinedTextField.composable.md.txt) overloads (which take `value` and `onValueChange`)
are deprecated. While M3's value-based [`TextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/TextField.composable.md.txt) and
[`OutlinedTextField`](https://developer.android.com/reference/kotlin/androidx/compose/material3/OutlinedTextField.composable.md.txt) overloads remain undeprecated in Material 3 1.5.0,
migrate M2 text fields directly to M3's state-based overloads that accept a
[`TextFieldState`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/text/input/TextFieldState.md.txt).

For detailed migration steps, see [Migrate to state-based text fields](https://developer.android.com/develop/ui/compose/text/migrate-state-based.md.txt).

## Surfaces and elevation

![Comparison of M2 surface elevation and M3 surface elevation in light and dark themes](https://developer.android.com/static/develop/ui/compose/images/migration-elevation-update.png) **Figure 10**. M2 surface elevation versus M3 surface elevation in light theme (left) and dark theme (right).

The surface and elevation systems in M3 are different to M2. There are two types
of elevation in M3:

- Shadow elevation (casts a shadow, same as M2)
- Tonal elevation (overlays a color, new to M3)

In Compose, this applies to the M2 [`Surface`](https://developer.android.com/reference/kotlin/androidx/compose/material/Surface.composable.md.txt) function and the M3
[`Surface`](https://developer.android.com/reference/kotlin/androidx/compose/material3/Surface.composable.md.txt) function:

### M2

```kotlin
import androidx.compose.material.Surface

Surface(
    elevation = ...
) { ... }
```

### M3

```kotlin
import androidx.compose.material3.Surface

Surface(
    shadowElevation = ...,
    tonalElevation = ...
) { ... }
```

You can use the `elevation` [`Dp`](https://developer.android.com/reference/kotlin/androidx/compose/ui/unit/Dp.md.txt) values in M2 for both `shadowElevation`
and/or `tonalElevation` in M3, depending on the UX/UI design preference.
`Surface` is the backing composable behind most components, so component
composables might also expose elevation parameters you must migrate in the same
way.

> [!NOTE]
> **Note:** The default color used by `tonalElevation` in M3 is `primary`. You can override this by using the `surfaceTint` parameter in the `ColorScheme` class.

Tonal elevation in M3 replaces the concept of elevation overlays in M2 dark
themes. As a result, [`ElevationOverlay`](https://developer.android.com/reference/kotlin/androidx/compose/material/ElevationOverlay.md.txt) and [`LocalElevationOverlay`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary.md.txt#LocalElevationOverlay())
don't exist in M3, and [`LocalAbsoluteElevation`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary.md.txt#LocalAbsoluteElevation()) in M2 has changed to
[`LocalAbsoluteTonalElevation`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt#LocalAbsoluteTonalElevation()) in M3.

## Emphasis and content alpha

![Comparison of M2 and M3 icon and text emphasis](https://developer.android.com/static/develop/ui/compose/images/migration-emphasis-update.png) **Figure 11**. M2 icon and text emphasis (left) versus M3 icon and text emphasis (right)

Emphasis in M3 is significantly different to M2. In M2, emphasis involved using
*on* colors with certain alpha values to differentiate content like text and
icons. In M3, there are now a couple different approaches:

- Using *on* colors alongside their *variant on* colors from the expanded M3 color system.
- Using different font weights for text.

As a result, [`ContentAlpha`](https://developer.android.com/reference/kotlin/androidx/compose/material/ContentAlpha.md.txt) and [`LocalContentAlpha`](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary.md.txt#LocalContentAlpha()) don't exist in
M3 and need to be replaced.

> [!NOTE]
> **Note:** For disabled states in M3, it's still acceptable to use *on* colors with alpha values, like in M2. For more information, see [Color roles](https://m3.material.io/styles/color/roles#19e75989-7485-4f5b-a769-940c4e4364bc).

The following mappings are recommended as a starting point:

| M2 | M3 |
|---|---|
| `onSurface` with [`ContentAlpha.high`](https://developer.android.com/reference/kotlin/androidx/compose/material/ContentAlpha.md.txt#high()) | `onSurface` in general, [`FontWeight.Medium`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight.md.txt#Medium()) - [`FontWeight.Black`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight.md.txt#Black()) for text |
| `onSurface` with [`ContentAlpha.medium`](https://developer.android.com/reference/kotlin/androidx/compose/material/ContentAlpha.md.txt#medium()) | `onSurfaceVariant` in general, [`FontWeight.Thin`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight.md.txt#Thin()) - [`FontWeight.Normal`](https://developer.android.com/reference/kotlin/androidx/compose/ui/text/font/FontWeight.md.txt#Normal()) for text |
| `onSurface` with [`ContentAlpha.disabled`](https://developer.android.com/reference/kotlin/androidx/compose/material/ContentAlpha.md.txt#high()) | `onSurface.copy(alpha = 0.38f)` |

Here's an example of icon emphasis in M2 versus M3:

### M2

```kotlin
import androidx.compose.material.ContentAlpha
import androidx.compose.material.LocalContentAlpha

// High emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.high) {
    Icon(...)
}
// Medium emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.medium) {
    Icon(...)
}
// Disabled emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.disabled) {
    Icon(...)
}
```

### M3

```kotlin
import androidx.compose.material3.LocalContentColor

// High emphasis
CompositionLocalProvider(LocalContentColor provides MaterialTheme.colorScheme.onSurface) {
    Icon(...)
}
// Medium emphasis
CompositionLocalProvider(LocalContentColor provides MaterialTheme.colorScheme.onSurfaceVariant) {
    Icon(...)
}
// Disabled emphasis
CompositionLocalProvider(LocalContentColor provides MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f)) {
    Icon(...)
}
```

Here are examples of text emphasis in M2 and M3:

### M2

```kotlin
import androidx.compose.material.ContentAlpha
import androidx.compose.material.LocalContentAlpha

// High emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.high) {
    Text(...)
}
// Medium emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.medium) {
    Text(...)
}
// Disabled emphasis
CompositionLocalProvider(LocalContentAlpha provides ContentAlpha.disabled) {
    Text(...)
}
```

### M3

```kotlin
import androidx.compose.material3.LocalContentColor

// High emphasis
Text(
    ...,
    fontWeight = FontWeight.Bold
)
// Medium emphasis
Text(
    ...,
    fontWeight = FontWeight.Normal
)
// Disabled emphasis
CompositionLocalProvider(LocalContentColor provides MaterialTheme.colorScheme.onSurface.copy(alpha = 0.38f)) {
    Text(
        ...,
        fontWeight = FontWeight.Normal
    )
}
```

## Backgrounds and containers

Backgrounds in M2 are named containers in M3. In general, you can replace
`background*` parameters in M2 with `container*` in M3, using the same values.
For example:

### M2

```kotlin
Badge(
    backgroundColor = MaterialTheme.colors.primary
) { ... }
```

### M3

```kotlin
Badge(
    containerColor = MaterialTheme.colorScheme.primary
) { ... }
```

## Useful links

To learn more about migrating from M2 to M3 in Compose, consult the following
additional resources.

### Docs

- [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3.md.txt)

### Sample apps

- [Reply M3 sample app](https://github.com/android/compose-samples/tree/main/Reply)
- Jetchat sample app M2 to M3 migration
  - [Initial alpha01 migration](https://github.com/android/compose-samples/pull/690)
  - [Follow-up alpha10 update](https://github.com/android/compose-samples/pull/798)
- [Jetnews sample app M2 to M3 migration](https://github.com/android/compose-samples/pull/964)
- [Now in Android M3 hero app :core-designsystem module](https://github.com/android/nowinandroid/tree/main/core/designsystem)

### Videos

- [Implementing Material You Using Jetpack Compose](https://www.youtube.com/watch?v=jrfuHyMlehc&t=5s)

### API reference and source code

- [Compose Material 3 API reference](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary.md.txt)
- [Compose Material 3 samples in source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/samples/src/main/java/androidx/compose/material3/samples/)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Material Design 2 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material.md.txt)
- [Material Design 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3.md.txt)
- [Custom design systems in Compose](https://developer.android.com/develop/ui/compose/designsystems/custom.md.txt)