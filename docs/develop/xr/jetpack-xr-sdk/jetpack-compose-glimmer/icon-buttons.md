---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icon-buttons
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icon-buttons
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

In Jetpack Compose Glimmer, an [`IconButton`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/IconButton.composable) is a compact, interactive
component used for exposing supplementary actions with a single tap.

Icon buttons appear smaller than standard buttons, but they maintain a physical
boundary to ensure ease of interaction on display glasses.

For other use cases, there are also [standard buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons) and [toggle
buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/toggle-buttons).
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_buttons_anatomy_icon.png) An example of some different styles of icon buttons in Jetpack Compose Glimmer. These examples show five icon button states: Enabled (1), Focused (2), Pressed (3), Disabled (4), Disabled and focused (5).

## Sizes and dimensions

| Element | Dimension |
|---|---|
| **Minimum container size** | 48 x 48 dp |
| **Internal icon size** | 32 x 32 dp |
| **Default content padding** | [`GlimmerTheme.componentSpacingValues.small`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/ComponentSpacingValues#small()) |

## States

Icon buttons in Jetpack Compose Glimmer change their appearance to communicate
their state.

- **Enabled**: The default interactive state.
- **Focused** : Applies [`GlimmerTheme.depthEffectLevels.level1`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/DepthEffectLevels#level1()) and a focused border highlight.
- **Pressed**: Applies a semi-transparent white overlay to the surface.
- **Disabled**: The button is non-interactive and visual feedback is removed.

## Icon button defaults

The following defaults apply to icon buttons:

- **Shape** : Defaults to [`GlimmerTheme.shapes.large`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Shapes#large()) (typically circular).
- **Color** : Defaults to [`GlimmerTheme.colors.surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#surface()).
- **Content color**: Automatically calculated from the background color unless explicitly provided.
- **Content padding**: Provides the default spacing between the icon and the container edge.
- **Minimum size** : A fixed `48.dp` value to prevent buttons from becoming too small to interact with.
- **Icon size** : Defaults to [`GlimmerTheme.iconSizes.small`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/IconSizes#small()) (`32.dp`).

## Example: Icon button

The following code creates an icon button with default characteristics:


```kotlin
@Composable
fun IconButtonSample() {
    IconButton(onClick = {}) { Icon(FavoriteIcon, "Localized description") }
}
```

<br />