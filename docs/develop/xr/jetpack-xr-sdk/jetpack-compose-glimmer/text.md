---
title: Text in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Text in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.




Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`Text`](/reference/kotlin/androidx/xr/glimmer/package-summary#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.text.TextStyle)) component builds upon the basic text
and lets you set various text properties like color, font size, font style, font
weight, font family, letter spacing, and text alignment. The Jetpack Compose
Glimmer `Text` component is unique in that it intelligently manages color
matching. For example, if no color override is specified, the text defaults to
the content color provided by the nearest surface in the UI hierarchy.

## Example: Create a text heading in a box

```
@Composable
fun GlimmerStyleSample() {
    GlimmerTheme {
        Box(
            modifier = Modifier.fillMaxSize(),
            contentAlignment = Alignment.Center
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Text(
                    text = "This is a sample heading",
                    color = GlimmerTheme.colors.secondary
                )
                Spacer(modifier = Modifier.height(16.dp))
                Button(onClick = { /* Handle Click */ }) {
                    Text(text = "Sample Button")
                }
            }
        }
    }
}
```

### Key points about the code

* The [`Button`](/reference/kotlin/androidx/xr/glimmer/Button.composable#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.xr.glimmer.ButtonSize,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) composable is automatically interactable, has a
  [`Colors.surface`](/reference/kotlin/androidx/xr/glimmer/Colors#surface()) background, and the text is automatically set to:

  + style = [`GlimmerTheme.typography.bodyMedium`](/reference/kotlin/androidx/xr/glimmer/Typography#bodyMedium())
  + color = [`GlimmerTheme.Colors.surface`](/reference/kotlin/androidx/xr/glimmer/Colors#surface())