---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included
source: md.txt
---

Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) Display Glasses [](https://developer.android.com/develop/xr/devices#audio-display) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Jetpack Compose Glimmer is built on [Jetpack Compose](https://developer.android.com/compose) and includes
composables, components, behaviors, and a theme that are [designed for AI
glasses with a display](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles). With Glimmer, you can build native UI for display
glasses using Compose, bringing your app experiences to life with less code,
powerful tools, and intuitive Kotlin APIs.

> [!TIP]
> **Tip:** We released an agent skill to help you work with Jetpack Compose Glimmer. Try out the skill from the [Android skills repository](https://github.com/android/skills).

## Jetpack Compose Glimmer composables

Jetpack Compose Glimmer provides [`@Composable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable) functions tailored for AI
glasses displays, such as [`Text`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Text.composable), [`Button`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Button.composable), and [`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/ListItem.composable). Here
are some unique characteristics of Jetpack Compose Glimmer composables:

- **Simplified styling** : The `Surface` components, for example, default to black or transparent backgrounds for optical display optimization.
- **Optimized color defaults**: Jetpack Compose Glimmer calculates content color based on background color by default, so developers rarely need to manually set text colors, enhancing legibility without any additional work.
- **Differentiated focus**: Focus is indicated using outline-based visual
  feedback instead of the ripple effect, which promotes clear visibility.

  ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_ixd_inputs_focus.png) **Figure 1.** Three focus states in Jetpack Compose Glimmer, which are differentiated using outline-based visual feedback.
- **Optimized Elevation**: Jetpack Compose Glimmer uses limited box-shadows
  for visual separation

  ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_surface_depth.png) **Figure 2.** Five levels of elevation in Jetpack Compose Glimmer, which are differentiated using limited box-shadows.

## Jetpack Compose Glimmer components

Jetpack Compose Glimmer features its own set of custom-designed components,
similar to the [components in Jetpack Compose](https://developer.android.com/develop/ui/compose/components), but specifically optimized
for the unique visual and interactive demands of display glasses. Jetpack
Compose Glimmer components are customizable with [Jetpack Compose Glimmer's
theme](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#theme) and build on lower-level Compose features to support user input
methods like tap and swipe by default.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_components_overview.png) **Figure 3.** Jetpack Compose Glimmer includes a variety of components to help you build app experiences that are optimized for display glasses.

To learn more about using a specific component, see the following guides:

- [Buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons)
- [Cards](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards)
- [Icons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons)
- [Icon buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icon-buttons)
- [Lists](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists)
- [List items](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/list-items)
- [Surfaces](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/surfaces)
- [Text](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text)
- [Toggle buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/toggle-buttons)
- [Title Chips](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)
- [Vertical stacks](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/vertical-stacks)

If one of these high-level components doesn't work for your use case, you can
use a [`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/surface.composable) to build a custom component. Surfaces are the most-basic
building block in Jetpack Compose Glimmer---a blank canvas for any specific,
custom designs or interactions that you want to build.

## Jetpack Compose Glimmer modifiers

Modifiers in Jetpack Compose Glimmer function identically to [Compose
modifiers](https://developer.android.com/develop/ui/compose/modifiers), which let you augment composables by customizing their layout,
appearance, and behavior. Jetpack Compose Glimmer includes modifiers and unique
defaults for glasses-specific visual feedback and performance.

## Jetpack Compose Glimmer's theme

Jetpack Compose Glimmer features a dedicated theming system for display glasses.
Jetpack Compose Glimmer's theme implements a simplified and optimized palette of
colors, typography, and shapes. This promotes maximum visibility and conciseness
for display glasses. All Jetpack Compose Glimmer components are designed for
automatic integration with glasses-specific input methods. Jetpack Compose
Glimmer's theme is exposed using the [`GlimmerTheme`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/GlimmerTheme) class.

Like other [themes in Jetpack Compose](https://developer.android.com/develop/ui/compose/designsystems/anatomy), `GlimmerTheme` includes several
subsystems which are briefly outlined in the following sections along with their
customizable attributes:

- Colors
- Typography
- Component spacing values
- Shapes
- Depth effect levels
- Icon sizes

### Colors

Jetpack Compose Glimmer's [color system](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/colors) is designed for additive displays
and real environments. Unlike standard Android themes, the `GlimmerTheme`
[`Colors`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors) prioritize dark backgrounds with semi-transparency and vibrant
accents to ensure content is legible against unpredictable real-world lighting.

The system uses a three-part palette with primary, secondary, and neutral
colors. Neutral colors often serve as the physical surfaces of the spatial UI,
while the primary and secondary colors provide clear visual cues for interaction
and branding.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_colorscheme.png) **Figure 4.** An overview of the colors in `GlimmerTheme`.

### Typography

Jetpack Compose Glimmer's typography system includes various typography styles
for legibility and conciseness on display glasses. These styles are designed to
maximize contrast and improve text readability through bolder weights, wider
letter spacing, and appropriate line heights. These styles are exposed through
[`GlimmerTheme.typography`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Typography).
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_type_scale.png) **Figure 5.** An example of Jetpack Compose Glimmer's six typography styles.

> [!TIP]
> **Tip:** You can use [Google Sans Flex](https://fonts.google.com/specimen/Google+Sans+Flex?query=google+sans), which is optimized for display glasses. For more information, see the section in the [text component
> documentation](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text#google-sans-flex). For custom fonts, see our [design guidance](https://developer.android.com/design/ui/ai-glasses/guides/styles/type#customize_fonts).

### Component spacing values

These values are used to ensure consistent spacing across Jetpack Compose
Glimmer components. This includes component paddings, spacing between
components, and other spacing elements. Note that changing these values affects
the default sizing of most components.

### Shapes

Jetpack Compose Glimmer's shape system defines a set of standard corner
treatments and geometric forms for components, designed to create a consistent
and minimalist visual language on display glasses UIs, with all shapes exposed
through [`GlimmerTheme.shapes`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Shapes).
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_shapes.webp) **Figure 6.** An example of large, medium, and small shapes in Jetpack Compose Glimmer.

### Depth effect levels

Jetpack Compose Glimmer components use *depth* to represent hierarchy, which
helps to visually distinguish elements that display above (on top of) other
cards. Depth on display glasses is the combination of placement in z-space and
shadows. For most high-level components, such as list items, depth is
automatically applied based on focus state. When a component is focused, it
gains depth; when it loses focus, it returns to its normal state. However for
working with custom components, you can use the `depthEffect` parameter on
[`Modifier.surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/surface.composable#(androidx.compose.ui.Modifier).surface(kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.xr.glimmer.SurfaceDepthEffect,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)), or [`depthEffect`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/depthEffect.modifier).

### Icon sizes

Jetpack Compose Glimmer's icon system is designed to coherently integrate with
the simplified visual language of display glasses UIs, often leveraging rounded
forms like [Material Symbols Rounded](https://fonts.google.com/icons?icon.style=Rounded) for optimal readability.