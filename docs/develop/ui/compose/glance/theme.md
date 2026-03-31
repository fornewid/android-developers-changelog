---
title: Implement a Glance theme  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/theme
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Implement a Glance theme Stay organized with collections Save and categorize content based on your preferences.



Glance provides an API to manage the color theme. For other style attributes,
such as [`TextStyle`](/reference/kotlin/androidx/compose/ui/text/TextStyle), declare top-level variables.

## Add colors

Glance provides an implementation of Material colors out of the box. To use the
built-in theme, wrap your top level composable with `GlanceTheme`, as shown in
the following example.

On devices that support dynamic colors, this theme is derived from the
user-specific platform colors. On other devices, this falls back to the Material
baseline theme. Use `GlanceTheme.colors` to style with colors from the wrapped
theme. You can use these values from the theme anywhere a color is needed.

```
override suspend fun provideGlance(context: Context, id: GlanceId) {

    provideContent {
        GlanceTheme {
            MyContent()
        }
    }
}

@Composable
private fun MyContent() {

    Image(
        colorFilter = ColorFilter.tint(GlanceTheme.colors.secondary),
        // ...

    )
}

GlanceSnippets.kt
```

To customize the theme, you can pass the `colors` to the `GlanceTheme`. Glance
provides the `androidx.glance:glance-material` interoperability library for
Material 2, and `androidx.glance:glance-material3` for Material 3 colors
support.

For example, provide your app's existing material colors to the `ColorProviders`
API to create a Glance color scheme, as shown in the following snippet:

```
// Remember, use the Glance imports
// import androidx.glance.material3.ColorProviders

// Example Imports from your own app
// import com.example.myapp.ui.theme.DarkColors
// import com.example.myapp.ui.theme.LightColors

object MyAppWidgetGlanceColorScheme {

    val colors = ColorProviders(
        light = LightColors,
        dark = DarkColors
    )
}

GlanceSnippets.kt
```

Provide the colors from the scheme to the `GlanceTheme` that wraps all your
composables, as shown in the following example:

```
override suspend fun provideGlance(context: Context, id: GlanceId) {
    // ...

    provideContent {
        GlanceTheme(colors = MyAppWidgetGlanceColorScheme.colors) {
            MyContent()
        }
    }
}

@Composable
private fun MyContent() {

    Image(
        colorFilter = ColorFilter.tint(GlanceTheme.colors.secondary),
        // ...
    )
}

GlanceSnippets.kt
```

If you prefer to use dynamic colors from the wallpaper when supported, and your
app's color scheme otherwise, you can conditionally pass your app's color scheme
in the `GlanceTheme`. This is shown in the following snippet:

```
override suspend fun provideGlance(context: Context, id: GlanceId) {

    provideContent {
        GlanceTheme(
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S)
                GlanceTheme.colors
            else
                MyAppWidgetGlanceColorScheme.colors
        ) {
            MyContent()
        }
    }
}

@Composable
private fun MyContent() {
    // ...
    Image(
        colorFilter = ColorFilter.tint(GlanceTheme.colors.secondary),
        // ...
    )
}

GlanceSnippets.kt
```

## Add shapes

To provide special shapes or shadows to your app widget, use the Android
Drawables API.

For example, the following snippet shows how to create a drawable (a shape):

```
<shape xmlns:android="http://schemas.android.com/apk/res/android">
    <corners android:radius="16dp"/>
    <stroke android:color="@color/outline_color" android:width="1dp"/>
</shape>

button_outline.xml
```

Provide it to the target composable:

```
GlanceModifier.background(
    imageProvider = ImageProvider(R.drawable.button_outline)
)

GlanceSnippets.kt
```

**Note:** You can use the Android resource folder structure to define different
shapes or other resources for any type of configuration (e.g.,
`values-night`).

[Previous

arrow\_back

Build UI with Glance](/develop/ui/compose/glance/build-ui)

[Next

Glance interoperability

arrow\_forward](/develop/ui/compose/glance/interoperability)