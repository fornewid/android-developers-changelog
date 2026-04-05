---
title: Anatomy of a theme in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/designsystems/anatomy
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Anatomy of a theme in Compose Stay organized with collections Save and categorize content based on your preferences.



Themes in Jetpack Compose are made up of a number of lower-level constructs
and related APIs. These can be seen in the
[source code](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/MaterialTheme.kt)
of `MaterialTheme` and can also be applied in custom design systems.

## Theme system classes

A theme is typically made up of a number of subsystems that group common visual and
behavioral concepts. These systems can be modeled with classes which have
theming values.

For example, `MaterialTheme` includes
[`ColorScheme`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/ColorScheme.kt)
(color system),
[`Typography`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Typography.kt)
(typography system), and
[`Shapes`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/Shapes.kt)
(shape system).

**Note:** Classes should be annotated with
[`Stable`](/reference/kotlin/androidx/compose/runtime/Stable)
or
[`@Immutable`](/reference/kotlin/androidx/compose/runtime/Immutable)
to provide information to the Compose compiler. To learn more, check out the
[Lifecycle of composables guide](/develop/ui/compose/lifecycle#skipping).

```
@Immutable
data class ColorSystem(
    val color: Color,
    val gradient: List<Color>
    /* ... */
)

@Immutable
data class TypographySystem(
    val fontFamily: FontFamily,
    val textStyle: TextStyle
)
/* ... */

@Immutable
data class CustomSystem(
    val value1: Int,
    val value2: String
    /* ... */
)

/* ... */

ThemeAnatomySnippets.kt
```

## Theme system composition locals

Theme system classes are implicitly provided to the composition tree as
[`CompositionLocal`](/reference/kotlin/androidx/compose/runtime/CompositionLocal)
instances. This allows theming values to be statically referenced in composable
functions.

To learn more about `CompositionLocal`, check out the
[Locally scoped data with CompositionLocal guide](/develop/ui/compose/compositionlocal).

**Note:** You can create a class's `CompositionLocal` with
[`compositionLocalOf`](/reference/kotlin/androidx/compose/runtime/package-summary#compositionlocalof)
or
[`staticCompositionLocalOf`](/reference/kotlin/androidx/compose/runtime/package-summary#staticcompositionlocalof).
These functions have a `defaultFactory` trailing lambda to provide fallback
values of the same type that they're providing. It's a good idea to use
reasonable defaults like `Color.Unspecified`, `TextStyle.Default`, etc.

```
val LocalColorSystem = staticCompositionLocalOf {
    ColorSystem(
        color = Color.Unspecified,
        gradient = emptyList()
    )
}

val LocalTypographySystem = staticCompositionLocalOf {
    TypographySystem(
        fontFamily = FontFamily.Default,
        textStyle = TextStyle.Default
    )
}

val LocalCustomSystem = staticCompositionLocalOf {
    CustomSystem(
        value1 = 0,
        value2 = ""
    )
}

/* ... */

ThemeAnatomySnippets.kt
```

## Theme function

The theme function is the entry point and primary API. It constructs instances
of the theme system `CompositionLocal`s — using real values any logic
required — that are provided to the composition tree with
[`CompositionLocalProvider`](/reference/kotlin/androidx/compose/runtime/package-summary#compositionlocalprovider).
The `content` parameter allows nested composables to access theming values
relative to the hierarchy.

```
@Composable
fun Theme(
    /* ... */
    content: @Composable () -> Unit
) {
    val colorSystem = ColorSystem(
        color = Color(0xFF3DDC84),
        gradient = listOf(Color.White, Color(0xFFD7EFFF))
    )
    val typographySystem = TypographySystem(
        fontFamily = FontFamily.Monospace,
        textStyle = TextStyle(fontSize = 18.sp)
    )
    val customSystem = CustomSystem(
        value1 = 1000,
        value2 = "Custom system"
    )
    /* ... */
    CompositionLocalProvider(
        LocalColorSystem provides colorSystem,
        LocalTypographySystem provides typographySystem,
        LocalCustomSystem provides customSystem,
        /* ... */
        content = content
    )
}

ThemeAnatomySnippets.kt
```

## Theme object

Accessing theme systems is done using an object with convenience properties. For
consistency, the object tends to be named the same as the theme function. The
properties simply get the current composition local.

```
// Use with eg. Theme.colorSystem.color
object Theme {
    val colorSystem: ColorSystem
        @Composable
        get() = LocalColorSystem.current
    val typographySystem: TypographySystem
        @Composable
        get() = LocalTypographySystem.current
    val customSystem: CustomSystem
        @Composable
        get() = LocalCustomSystem.current
    /* ... */
}

ThemeAnatomySnippets.kt
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Locally scoped data with CompositionLocal](/develop/ui/compose/compositionlocal)
* [Custom design systems in Compose](/develop/ui/compose/designsystems/custom)
* [Material Design 3 in Compose](/develop/ui/compose/designsystems/material3)