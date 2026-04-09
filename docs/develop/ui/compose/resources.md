---
title: Resources in Compose  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/resources
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Resources in Compose Stay organized with collections Save and categorize content based on your preferences.




Jetpack Compose can access the resources defined in your Android project. This
document explains some of the APIs Compose offers to do so.

Resources are the additional files and static content that your code uses, such
as bitmaps, layout definitions, user interface strings, animation instructions,
and more. If you're not familiar with resources in Android, check out the [App
resources overview guide](/guide/topics/resources/providing-resources).

## Strings

The most common type of resource are your Strings. Use the `stringResource` API
to retrieve a string statically defined in your XML resources.

```
// In the res/values/strings.xml file
// <string name="compose">Jetpack Compose</string>

// In your Compose code
Text(
    text = stringResource(R.string.compose)
)

ResourcesSnippets.kt
```

`stringResource` also works with positional formatting.

```
// In the res/values/strings.xml file
// <string name="congratulate">Happy %1$s %2$d</string>

// In your Compose code
Text(
    text = stringResource(R.string.congratulate, "New Year", 2021)
)

ResourcesSnippets.kt
```

### String plurals (experimental)

Use the `pluralStringResource` API to load up a plural with a certain quantity.

```
// In the res/strings.xml file
// <plurals name="runtime_format">
//    <item quantity="one">%1$d minute</item>
//    <item quantity="other">%1$d minutes</item>
// </plurals>

// In your Compose code
Text(
    text = pluralStringResource(
        R.plurals.runtime_format,
        quantity,
        quantity
    )
)

ResourcesSnippets.kt
```

When using the `pluralStringResource` method, you need to pass the count twice
if your string includes string formatting with a number. For example, for the
string `%1$d minutes`, the first count parameter selects the appropriate plural
string and the second count parameter is inserted into the `%1$d` placeholder.
If your plural strings don't include string formatting, you don't need to pass
the third parameter to `pluralStringResource`.

For more information on plurals, check out the
[quantity string documentation](/guide/topics/resources/string-resource#Plurals).

## Dimensions

Similarly, use the `dimensionResource` API to get dimensions from a resource XML
file.

```
// In the res/values/dimens.xml file
// <dimen name="padding_small">8dp</dimen>

// In your Compose code
val smallPadding = dimensionResource(R.dimen.padding_small)
Text(
    text = "...",
    modifier = Modifier.padding(smallPadding)
)

ResourcesSnippets.kt
```

## Colors

If you're adopting Compose incrementally in your app, use the `colorResource`
API to get colors from a resource XML file.

```
// In the res/colors.xml file
// <color name="purple_200">#FFBB86FC</color>

// In your Compose code
HorizontalDivider(color = colorResource(R.color.purple_200))

ResourcesSnippets.kt
```

`colorResource` works as expected with static colors, but it flattens [color
state list resources](/guide/topics/resources/color-list-resource).

**Warning:** Prefer colors from the theme rather than hard-coded colors. Even though
it's possible to access colors using the `colorResource` function, it's
recommended that the colors of your app are defined in a `MaterialTheme` which
can be accessed from your composables like `MaterialTheme.colors.primary`. Learn
more about this in the [Design systems in Compose
documentation](/develop/ui/compose/designsystems).

## Vector assets and image resources

Use the `painterResource` API to load either vector drawables or rasterized
asset formats like PNGs. You don't need to know the type of the drawable, simply
use `painterResource` in `Image` composables or `paint` modifiers.

```
// Files in res/drawable folders. For example:
// - res/drawable-nodpi/ic_logo.xml
// - res/drawable-xxhdpi/ic_logo.png

// In your Compose code
Icon(
    painter = painterResource(id = R.drawable.ic_logo),
    contentDescription = null // decorative element
)

ResourcesSnippets.kt
```

`painterResource` decodes and parses the content of the resource on the main
thread.

**Note:** Unlike
[`Context.getDrawable`](/reference/android/content/Context#getDrawable(int)),
`painterResource` can only load
[`BitmapDrawable`](/reference/android/graphics/drawable/BitmapDrawable) and
[`VectorDrawable`](/reference/android/graphics/drawable/VectorDrawable) platform
[`Drawable`](/reference/android/graphics/drawable/Drawable) types.

## Animated Vector Drawables

Use the `AnimatedImageVector.animatedVectorResource` API to load an animated
vector drawable XML. The method returns an `AnimatedImageVector` instance. In
order to display the animated image, use the `rememberAnimatedVectorPainter`
method to create a `Painter` that can be used in `Image` and `Icon` composables.
The boolean `atEnd` parameter of the `rememberAnimatedVectorPainter` method
indicates whether the image should be drawn at the end of all the animations.
If used with a mutable state, changes to this value trigger the corresponding
animation.

```
// Files in res/drawable folders. For example:
// - res/drawable/ic_hourglass_animated.xml

// In your Compose code
val image =
    AnimatedImageVector.animatedVectorResource(R.drawable.ic_hourglass_animated)
val atEnd by remember { mutableStateOf(false) }
Icon(
    painter = rememberAnimatedVectorPainter(image, atEnd),
    contentDescription = null // decorative element
)

ResourcesSnippets.kt
```

## Icons

Jetpack Compose comes with the `Icons` object that is the entry point for using
[Material Icons](https://material.io/resources/icons/?style=baseline) in
Compose. There are five distinct icon themes:
[Filled](/reference/kotlin/androidx/compose/material/icons/Icons.Filled),
[Outlined](/reference/kotlin/androidx/compose/material/icons/Icons.Outlined),
[Rounded](/reference/kotlin/androidx/compose/material/icons/Icons.Rounded),
[TwoTone](/reference/kotlin/androidx/compose/material/icons/Icons.TwoTone), and
[Sharp](/reference/kotlin/androidx/compose/material/icons/Icons.Sharp). Each
theme contains the same icons, but with a distinct visual style. You should
typically choose one theme and use it across your application for consistency.

To draw an icon, you can use the
[`Icon`](/reference/kotlin/androidx/compose/material/Icon.composable#Icon(androidx.compose.ui.graphics.vector.ImageVector,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color))
composable which applies tint and provides layout size matching the icon.

```
Icon(Icons.Rounded.Menu, contentDescription = "Localized description")

ResourcesSnippets.kt
```

Some of the most commonly used icons are available as part of the
`androidx.compose.material` dependency. To use any of the other Material icons,
add the `material-icons-extended` dependency to the `build.gradle` file.

```
dependencies {
  def composeBom = platform('androidx.compose:compose-bom:2026.03.00')
  implementation composeBom

  implementation 'androidx.compose.material:material-icons-extended'
}
```

**Note:** Icons maintain the same names defined by Material, but with their
snake\_case name converted to PascalCase. For example, add\_alarm becomes
`AddAlarm`. Icons that start with a number, such as 360, are prefixed with `_`,
becoming `_360`.**Warning:** `material-icons-extended` is a large library and can affect your APK
size. For that reason, consider using R8/Proguard in production builds to remove
the resources that aren't used. Furthermore due to the large size, your
project's build time and Android Studio's previews loading time could increase
during development. On the other hand, `material-icons-extended` lets you
iterate more rapidly through quick access to the latest versions of all icons.
You can also use this library to copy the source code of the icon to have a
fixed copy in your app, or alternatively, import the icons using [Android
Studio's Import vector asset
feature](/studio/write/vector-asset-studio#materialicon).

## Fonts

To use fonts in Compose, download and bundle the font files directly in your
APKs by placing them in the `res/font` folder.

Load each font using the
[`Font`](/reference/kotlin/androidx/compose/ui/text/font/Font) API and create a
[`FontFamily`](/reference/kotlin/androidx/compose/ui/text/font/FontFamily) with
them that you can use in
[`TextStyle`](/reference/kotlin/androidx/compose/ui/text/TextStyle) instances to
create your own
[`Typography`](/reference/kotlin/androidx/compose/material/Typography). The
following is code taken from the
[Crane](https://github.com/android/compose-samples/tree/main/Crane)
compose sample and its
[`Typography.kt`](https://github.com/android/compose-samples/blob/main/Crane/app/src/main/java/androidx/compose/samples/crane/ui/Typography.kt)
file.

```
// Define and load the fonts of the app
private val light = Font(R.font.raleway_light, FontWeight.W300)
private val regular = Font(R.font.raleway_regular, FontWeight.W400)
private val medium = Font(R.font.raleway_medium, FontWeight.W500)
private val semibold = Font(R.font.raleway_semibold, FontWeight.W600)

// Create a font family to use in TextStyles
private val craneFontFamily = FontFamily(light, regular, medium, semibold)

// Use the font family to define a custom typography
val craneTypography = Typography(
    titleLarge = TextStyle(
        fontFamily = craneFontFamily
    ) /* ... */
)

// Pass the typography to a MaterialTheme that will create a theme using
// that typography in the part of the UI hierarchy where this theme is used
@Composable
fun CraneTheme(content: @Composable () -> Unit) {
    MaterialTheme(typography = craneTypography) {
        content()
    }
}

ResourcesSnippets.kt
```

For using downloadable fonts in Compose, see the
[Downloadable fonts](/develop/ui/compose/text#downloadable-fonts) page.

Learn more about typography in the [Theming in Compose
documentation](/develop/ui/compose/designsystems/material3#typography)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Loading images {:#loading-images}](/develop/ui/compose/graphics/images/loading)
* [Material Design 2 in Compose](/develop/ui/compose/designsystems/material)
* [Custom design systems in Compose](/develop/ui/compose/designsystems/custom)