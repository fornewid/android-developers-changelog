---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included
source: md.txt
---

<br />

<br />

Applicable XR devices  
This guidance helps you build experiences for these types of XR devices.  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)  
![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg)AI Glasses[](https://developer.android.com/develop/xr/devices#ai-glasses)  
[Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Jetpack Compose Glimmer is built on[Jetpack Compose](https://developer.android.com/compose)and includes composables, components, behaviors, and a theme that are[designed for AI glasses with a display](https://developer.android.com/design/ui/ai-glasses/guides/foundations/design-principles). With Glimmer, you can build native UI for AI glasses using Compose, bringing your app experiences to life with less code, powerful tools, and intuitive Kotlin APIs.

## Jetpack Compose Glimmer composables

Jetpack Compose Glimmer provides[`@Composable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable)functions tailored for AI glasses displays, such as[`Text`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#Text(kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.font.FontStyle,androidx.compose.ui.text.font.FontWeight,androidx.compose.ui.text.font.FontFamily,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextDecoration,androidx.compose.ui.text.style.TextAlign,androidx.compose.ui.unit.TextUnit,androidx.compose.ui.text.style.TextOverflow,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Function1,androidx.compose.foundation.text.TextAutoSize,androidx.compose.ui.text.TextStyle)),[`Button`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#Button(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Boolean,androidx.xr.glimmer.ButtonSize,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function1)), and[`ListItem`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#ListItem(androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.layout.PaddingValues,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function0)). Here are some unique characteristics of Jetpack Compose Glimmer composables:

- **Simplified styling** : The`Surface`components, for example, default to black or transparent backgrounds for optical display optimization.
- **Optimized color defaults**: Jetpack Compose Glimmer calculates content color based on background color by default, so developers rarely need to manually set text colors, enhancing legibility without any additional work.
- **Differentiated focus**: Focus is indicated using outline-based visual feedback instead of the ripple effect, which promotes clear visibility.

  ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_ixd_inputs_focus.png)**Figure 1.**Three focus states in Jetpack Compose Glimmer, which are differentiated using outline-based visual feedback.
- **Optimized Elevation**: Jetpack Compose Glimmer uses limited box-shadows for visual separation

  ![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_surface_depth.png)**Figure 2.**Five levels of elevation in Jetpack Compose Glimmer, which are differentiated using limited box-shadows.

## Jetpack Compose Glimmer components

Jetpack Compose Glimmer features its own set of custom-designed components, similar to the[components in Jetpack Compose](https://developer.android.com/develop/ui/compose/components), but specifically optimized for the unique visual and interactive demands of AI glasses. Jetpack Compose Glimmer components are customizable with[Jetpack Compose Glimmer's theme](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#theme)and build on lower-level Compose features to support user input methods like tap and swipe by default.

To learn more about using a specific component, see the following guides:

- [Text](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/text)
- [Icons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/icons)
- [Title Chips](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/title-chips)
- [Cards](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/cards)
- [Lists](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/lists)
- [Buttons](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/buttons)

If one of these high-level components doesn't work for your use case, you can use a[`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#(androidx.compose.ui.Modifier).surface(kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.xr.glimmer.SurfaceDepth,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource))to build a custom component. Surfaces are the most-basic building block in Jetpack Compose Glimmer---a blank canvas for any specific, custom designs or interactions that you want to build.

## Jetpack Compose Glimmer modifiers

Modifiers in Jetpack Compose Glimmer function identically to[Compose modifiers](https://developer.android.com/develop/ui/compose/modifiers), allowing you to augment composables by customizing their layout, appearance, and behavior. Jetpack Compose Glimmer might introduce specific modifiers or apply unique defaults for glasses-specific visual feedback and performance.

## Jetpack Compose Glimmer depth

Jetpack Compose Glimmer components use*depth* to represent hierarchy, which helps to visually distinguish elements that display above (on top of) other cards. Depth on AI glasses is the combination of placement in z-space and shadows. For most high-level components, such as list items, depth is automatically applied based on focus state. When a component is focused, it gains depth; when it loses focus, it returns to its normal state. However for working with custom components, you can use the depth parameter on[`Modifier.surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#(androidx.compose.ui.Modifier).surface(kotlin.Boolean,androidx.compose.ui.graphics.Shape,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.xr.glimmer.SurfaceDepth,androidx.compose.foundation.BorderStroke,androidx.compose.foundation.interaction.MutableInteractionSource)), or[`Modifier.depth`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/package-summary#(androidx.compose.ui.Modifier).depth(androidx.xr.glimmer.Depth,androidx.compose.ui.graphics.Shape)).

## Jetpack Compose Glimmer's theme

Jetpack Compose Glimmer features a dedicated theming system for AI glasses. Jetpack Compose Glimmer's theme implements a simplified and optimized palette of colors, typography, and shapes. This promotes maximum visibility and conciseness for AI glasses. All Jetpack Compose Glimmer components are designed for automatic integration with AI glasses' specific input methods. Jetpack Compose Glimmer's theme is exposed using the[`GlimmerTheme`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/GlimmerTheme)class.

Like other[themes in Jetpack Compose](https://developer.android.com/develop/ui/compose/designsystems/anatomy),`GlimmerTheme`includes several subsystems: colors, shapes, typography, and icons (symbolography). Jetpack Compose Glimmer's theme also includes[Jetpack Compose Glimmer components](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#components)that you can customize.

### Colors

Jetpack Compose Glimmer's color system includes seven colors in its optimized palette, designed for maximum visibility and conciseness on AI glasses displays where black values don't render.
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_color_colorscheme.png)**Figure 3.** An overview of the colors in`GlimmerTheme`.

Note that "On ..." colors are not exposed through`GlimmerTheme`. These colors are automatically calculated by the system based on the background color.

These colors are exposed through[`GlimmerTheme.colors.primary`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#primary()), with values for each color role as described in the following table:

|   Color Role   | Defaults |
|----------------|----------|
| primary        | #A8C7FA  |
| secondary      | #4C88E9  |
| positive       | #4CE995  |
| negative       | #F57084  |
| surface        | #000000  |
| outline        | #606460  |
| outlineVariant | #42434A  |

Note that while[`surface`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#surface()),[`outline`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#outline())and[`outlineVariant`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Colors#outlineVariant())are marked as customizable, we strongly recommend that you don't customize these values.

### Shapes

Jetpack Compose Glimmer's shape system defines a set of standard corner treatments and geometric forms for components, designed to create a consistent and minimalist visual language on AI glasses UIs, with all shapes exposed through[`GlimmerTheme.shapes`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Shapes).
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_style_shapes.png)**Figure 4.**An example of large, medium, and small shapes in Jetpack Compose Glimmer.

### Typography

Jetpack Compose Glimmer's typography system includes six typography styles for legibility and conciseness on AI glasses displays. These styles are designed to maximize contrast and improve text readability through bolder weights, wider letter spacing, and appropriate line heights. These styles are exposed through[`GlimmerTheme.typography`](https://developer.android.com/reference/kotlin/androidx/xr/glimmer/Typography).
![](https://developer.android.com/static/images/design/ui/glasses/guides/glasses_styles_type_scale.png)**Figure 5.**An example of Jetpack Compose Glimmer's six typography styles.**Tip:** You can use[Google Sans Flex](https://fonts.google.com/specimen/Google+Sans+Flex?query=google+sans), which is optimized for displays on AI glasses. For custom fonts, see our[design guidance](https://developer.android.com/design/ui/ai-glasses/guides/styles/type#customize_fonts).

### Icons

Jetpack Compose Glimmer's icon system is designed to coherently integrate with the simplified visual language of AI glasses UIs, often leveraging rounded forms like[Material Symbols Rounded](https://fonts.google.com/icons?icon.style=Rounded)for optimal readability.