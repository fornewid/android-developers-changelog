---
title: Buttons in Jetpack Compose Glimmer  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Buttons in Jetpack Compose Glimmer Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

In Jetpack Compose Glimmer, the [`Button`](/reference/kotlin/androidx/xr/glimmer/Button.composable#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.xr.glimmer.ButtonSize,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)) component is an interactive
component that's optimized for AI glasses input, offering clear visual feedback
for their enabled, hovered, and pressed states to guide user actions.

![](/static/images/design/ui/glasses/guides/glasses_components_buttons.png)


**Figure 1.** An example of some different styles of buttons in Jetpack Compose Glimmer.

## Example: Button variations

```
@Composable
fun GlimmerButtonExample() {
    Column(
        verticalArrangement = Arrangement.spacedBy(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier.fillMaxWidth()
    ) {
        // Basic Button
        Button(onClick = { /* Do something */ }) {
            Text("Test Button 1")
        }

        // Button with a leading icon
        Button(
            onClick = { /* Do something */ },
            leadingIcon = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_favorite),
                    contentDescription = "Favorite icon"
                )
            }
        ) {
            Text("Test Button 2")
        }

        // Button with leading and trailing icons
        Button(
            onClick = { /* Do something */ },
            leadingIcon = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_favorite),
                    contentDescription = "Favorite icon"
                )
            },
            trailingIcon = {
                Icon(
                    painter = painterResource(id = R.drawable.ic_favorite),
                    contentDescription = "Favorite icon"
                )
            }
        ) {
            Text("Test Button 3")
        }
    }
}
```

### Key points about the code

* The button icons source local XML vector drawables
  (`R.drawable.ic_favorite`) using [`painterResource`](/reference/kotlin/androidx/compose/ui/res/painterResource.composable#painterResource(kotlin.Int)), replacing the
  `Icons.Default` library dependency for optimized asset loading.
* The `leadingIcon` and `trailingIcon` parameters are utilized to inject icon
  Composables into the button layout, demonstrating Jetpack Compose Glimmer's
  support for flexible icon positioning.
* The buttons use the default sizing configuration, which automatically
  manages internal padding and text scaling to align with standard Jetpack
  Compose Glimmer design specifications without explicit size modifiers.