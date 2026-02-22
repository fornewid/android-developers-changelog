---
title: https://developer.android.com/training/wearables/tiles/versioning
url: https://developer.android.com/training/wearables/tiles/versioning
source: md.txt
---

On Wear OS devices, tiles are rendered by two key components with independent
versioning. To help your app's tiles function correctly across all devices,
it's important to understand this underlying architecture.

- **Jetpack tile-related libraries** : These libraries (including Wear Tiles and Wear ProtoLayout) are embedded in your app, and you, as the developer, control their versions. Your app uses these libraries to construct a [`TileBuilder.Tile`](https://developer.android.com/reference/kotlin/androidx/wear/tiles/TileBuilders.Tile) object (the data structure representing your Tile) in response to the system's [`onTileRequest()`](https://developer.android.com/reference/kotlin/androidx/wear/tiles/TileService#onTileRequest(androidx.wear.tiles.RequestBuilders.TileRequest)) call.
- **ProtoLayout Renderer:** This system component is responsible for rendering the `Tile` object on the display and handling user interactions. The version of the renderer is not controlled by the app developer and can vary across devices, even those with identical hardware.

A Tile's appearance or behavior can vary based on both your app's Jetpack Tiles
library versions and the ProtoLayout Renderer version on the user's device. For
example, one device might support [rotation](https://developer.android.com/training/wearables/tiles/animations#rotation) or the display of heart rate
data, while another might not.

This document explains how to make your app compatible with different versions
of the Tiles library and ProtoLayout Renderer. It also explains how to migrate
to higher Jetpack library versions.

## Consider compatibility

To create a Tile that functions correctly across a range of devices, consider
accounting for varying feature support. You can do this through two main
strategies: detecting renderer capabilities at runtime and providing built-in
fallbacks.

### Detect renderer capabilities

You can dynamically change your tile's layout based on the features available on
a given device.

#### Detect the renderer version

- Use the [`getRendererSchemaVersion()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/DeviceParametersBuilders.DeviceParameters#getRendererSchemaVersion()) method of the [`DeviceParameters`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/DeviceParametersBuilders.DeviceParameters) object passed to your [`onTileRequest()`](https://developer.android.com/reference/kotlin/androidx/wear/tiles/TileService#onTileRequest(androidx.wear.tiles.RequestBuilders.TileRequest)) method. This method returns the major and minor version numbers of the ProtoLayout Renderer on the device.
- You can then use conditional logic in your `onTileRequest()` implementation to adapt your Tile's design or behavior based on the detected renderer version.

#### The `@RequiresSchemaVersion` annotation

- The `@RequiresSchemaVersion` annotation on ProtoLayout methods indicates the minimum renderer schema version required for that method to behave as documented ([example](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/LayoutModifier#(androidx.wear.protolayout.modifiers.LayoutModifier).clip(kotlin.Float,kotlin.Float))).
  - While calling a method that requires a higher renderer version than is available on the device won't cause your app to crash, it could lead to content not being displayed or the feature being ignored.

#### Example of version detection

```kotlin
val rendererVersion = requestParams.deviceConfiguration.rendererSchemaVersion

val arcElement =
    // DashedArcLine has the annotation @RequiresSchemaVersion(major = 1, minor = 500)
    // and so is supported by renderer versions 1.500 and greater
    if (
        rendererVersion.major > 1 ||
        (rendererVersion.major == 1 && rendererVersion.minor >= 500)
    ) {
        // Use DashedArcLine if the renderer supports it ...
        DashedArcLine.Builder()
            .setLength(degrees(270f))
            .setThickness(8f)
            .setLinePattern(
                LayoutElementBuilders.DashedLinePattern.Builder()
                    .setGapSize(8f)
                    .setGapInterval(10f)
                    .build()
            )
            .build()
    } else {
        // ... otherwise use ArcLine.
        ArcLine.Builder().setLength(degrees(270f)).setThickness(dp(8f)).build()
    }
```

### Provide fallbacks

Some resources allow you to define a fallback directly in the builder. This is
often simpler than checking the renderer version and is the preferred approach
when available.

A common use case is providing a static image as a fallback for a Lottie
animation. If the device doesn't support Lottie animations, it will render the
static image instead.

```kotlin
val lottieImage =
    ResourceBuilders.ImageResource.Builder()
        .setAndroidLottieResourceByResId(
            ResourceBuilders.AndroidLottieResourceByResId.Builder(R.raw.lottie)
                .setStartTrigger(createOnVisibleTrigger())
                .build()
        )
        // Fallback if lottie is not supported
        .setAndroidResourceByResId(
            ResourceBuilders.AndroidImageResourceByResId.Builder()
                .setResourceId(R.drawable.lottie_fallback)
                .build()
        )
        .build()
```

### Test with different renderer versions

To test your tiles against different renderer versions, deploy them to different
versions of the Wear OS emulator. (On physical devices, ProtoLayout Renderer
updates are delivered by the Play Store or system updates. It's not possible to
force a specific renderer version to be installed.)

Android Studio's Tile Preview feature makes use of a renderer embedded in the
Jetpack ProtoLayout library your code depends on, so another approach is to
depend on different Jetpack library versions when testing tiles.

## Migrate to Tiles 1.5 / ProtoLayout 1.3 (Material 3 Expressive)

Update your Jetpack Tile libraries to take advantage of the latest enhancements,
including UI changes to make your Tiles integrate seamlessly with the system.

> [!NOTE]
> **Note:** This guide uses the abbreviation "M3" to refer to the interchangeable terms "Material 3", "Material Design 3" and "Material You". The abbreviation "M2.5" is used to refer to the interchangeable terms "Material 2.5" and "Material Design 2.5".

Jetpack Tiles 1.5 and Jetpack ProtoLayout 1.3 introduce several notable
improvements and changes. These include:

- A Compose-like API for describing the UI.
- [Material 3 Expressive](https://m3.material.io/) components, including the bottom-hugging edge button and support for enhanced visuals: Lottie animations, more gradient types, and new arc line styles. - Note: some of these features can also be used without migrating to the new API.

### Recommendations

Follow these recommendations when migrating your tiles:

- **Migrate all your tiles simultaneously.** Avoid mixing tiles versions within your app. While the Material 3 components reside in a separate artifact (`androidx.wear.protolayout:protolayout-material3`)---making it technically possible to use both M2.5 and M3 Tiles in the same app---we strongly advise against this approach unless absolutely necessary (for example, if your app has a large number of tiles that cannot all be migrated at once).
- **Adopt Tiles UX guidance.** Given the highly structured and templated nature of tiles, use the designs in the [existing samples](https://github.com/android/wear-os-samples/tree/main/WearTilesKotlin) as starting points for your own designs.
- **Test across a variety of screen and font sizes.** Tiles are often information-dense, making text (especially when placed on buttons) susceptible to overflow and clipping. To minimize this, use the prebuilt components and avoid extensive customization. Test using [Android Studio's
  tile preview feature](https://developer.android.com/training/wearables/tiles/debug#preview-tiles) as well as on multiple real devices.

### Migration process

To migrate your tiles, follow these steps:

#### Update dependencies

First, update your `build.gradle.kts` file. Update the versions and change the
`protolayout-material` dependency to `protolayout-material3`, as shown:

    // In build.gradle.kts

    //val tilesVersion = "1.4.1"
    //val protoLayoutVersion = "1.2.1"

    // Use these versions for M3.
    val tilesVersion = "1.5.0"
    val protoLayoutVersion = "1.3.0"

     dependencies {
         // Use to implement support for wear tiles
         implementation("androidx.wear.tiles:tiles:$tilesVersion")

         // Use to utilize standard components and layouts in your tiles
         implementation("androidx.wear.protolayout:protolayout:$protoLayoutVersion")

         // Use to utilize components and layouts with Material Design in your tiles
         // implementation("androidx.wear.protolayout:protolayout-material:$protoLayoutVersion")
         implementation("androidx.wear.protolayout:protolayout-material3:$protoLayoutVersion")

         // Use to include dynamic expressions in your tiles
         implementation("androidx.wear.protolayout:protolayout-expression:$protoLayoutVersion")

         // Use to preview wear tiles in your own app
         debugImplementation("androidx.wear.tiles:tiles-renderer:$tilesVersion")

         // Use to fetch tiles from a tile provider in your tests
         testImplementation("androidx.wear.tiles:tiles-testing:$tilesVersion")
     }

#### TileService remains largely unchanged

The primary changes in this migration affect the UI components. Consequently,
your `TileService` implementation, including any resource-loading mechanisms,
should require minimal to no modifications.

The main exception involves tile activity tracking: if your app uses
[`onTileEnterEvent()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileEnterEvent(androidx.wear.tiles.EventBuilders.TileEnterEvent)) or [`onTileLeaveEvent()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileLeaveEvent(androidx.wear.tiles.EventBuilders.TileLeaveEvent)), we recommend that you
migrate to [`onRecentInteractionEventsAsync()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onRecentInteractionEventsAsync(java.util.List%3Candroidx.wear.tiles.EventBuilders.TileInteractionEvent%3E)). Starting with API 36, these
events will be batched.

#### Adapt your layout-generation code

In ProtoLayout 1.2 (M2.5), the [`onTileRequest()`](https://developer.android.com/reference/androidx/wear/tiles/TileService#onTileRequest(androidx.wear.tiles.RequestBuilders.TileRequest)) method returns a
[`TileBuilders.Tile`](https://developer.android.com/reference/androidx/wear/tiles/TileBuilders.Tile). This object contained various elements, including a
[`TimelineBuilders.Timeline`](https://developer.android.com/reference/androidx/wear/tiles/TimelineBuilders.Timeline), which in turn held the [`LayoutElement`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders.LayoutElement)
describing the tile's UI.

With ProtoLayout 1.3 (M3), while the overall data structure and flow have not
changed, the `LayoutElement` is now constructed using a Compose-inspired
approach with a layout based on defined *slots* which are (from top to bottom)
the `titleSlot` (optional; typically for a primary title or header), `mainSlot`
(mandatory; for the core content), and `bottomSlot` (optional; often for actions
like an edge button or supplemental information like short text). This layout is
constructed by the [`primaryLayout()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).primaryLayout(kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.material3.PrimaryLayoutMargins)) function.
![The layout of a tile showing mainSlot, titleSlot, bottomSlot](https://developer.android.com/static/wear/images/tiles/m3-layout.png) **Figure 1.**: A tile's slots.

> [!NOTE]
> **Note:** [`primaryLayout()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).primaryLayout(kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.material3.PrimaryLayoutMargins)) arranges for your tile's icon to be drawn at the top of the screen, so make sure your design can accommodate this. In particular, remove code that explicitly draws your tile's logo into this area so it only appears once.

##### Comparison of M2.5 and M3 layout functions

### M2.5


```kotlin
fun myLayout(
    context: Context,
    deviceConfiguration: DeviceParametersBuilders.DeviceParameters
) =
    PrimaryLayout.Builder(deviceConfiguration)
        .setResponsiveContentInsetEnabled(true)
        .setContent(
            Text.Builder(context, "Hello World!")
                .setTypography(Typography.TYPOGRAPHY_BODY1)
                .build()
        )
        .build()
```

<br />

### M3


```kotlin
fun myLayout(
    context: Context,
    deviceConfiguration: DeviceParametersBuilders.DeviceParameters,
) =
    materialScope(context, deviceConfiguration) {
        primaryLayout(mainSlot = { text("Hello, World!".layoutString) })
    }
```

<br />

To highlight the key differences:

1. **Elimination of builders**. The previous builder pattern for Material UI components is replaced by a more declarative, Compose-inspired syntax. (Non-UI components such as String/Color/Modifiers also get new Kotlin wrappers.)
2. **Standardized initialization and layout functions** . M3 layouts rely on standardized initialization and structure functions: [`materialScope()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#materialScope(android.content.Context,androidx.wear.protolayout.DeviceParametersBuilders.DeviceParameters,kotlin.Boolean,androidx.wear.protolayout.material3.ColorScheme,kotlin.Function1)) and [`primaryLayout()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).primaryLayout(kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.material3.PrimaryLayoutMargins)). These mandatory functions initialize the M3 environment (theming, component scope using `materialScope`) and define the primary slot-based layout (using `primaryLayout`). Both must be called exactly once per layout.

### Theming

Material 3 introduces several changes to theming, including dynamic color and an
expanded set of typography and shape options.

#### Color

A standout feature of Material 3 Expressive is "dynamic theming:" tiles which
enable this feature (on by default) will be displayed in system-provided theme
(availability dependent on the user's device and configuration).

Another change in M3 is an expansion of the number of color tokens, which has
increased from 4 to 29. The new color tokens can be found in the
[`ColorScheme`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/ColorScheme) class.

##### Typography

Similar to M2.5, M3 relies heavily on predefined font size constants---directly
specifying a font size is discouraged. These constants are located in the
[`Typography`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/Typography) class and offer a slightly expanded range of more expressive
options.

> [!NOTE]
> **Note:** On Wear OS 6 (API level 36) and higher, all tiles in a carousel use the same font. The font may vary across devices.

For full details, refer to the [Typography documentation](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/Typography).

#### Shape

Most M3 components can vary along the dimension of shape as well as color.

A [`textButton`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).textButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,androidx.wear.protolayout.material3.TextButtonStyle,androidx.wear.protolayout.ModifiersBuilders.Padding)) (in the `mainSlot`) with shape [`full`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/Shapes#full()):
![Tile with 'full' shape (more rounded corners)](https://developer.android.com/static/wear/images/tiles/m3-shape-full.png) **Figure 2.**: Tile with 'full' shape

The same textButton with shape [`small`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/Shapes#small()):
![Tile with 'small' shape (less rounded corners)](https://developer.android.com/static/wear/images/tiles/m3-shape-small.png) **Figure 3.**: Tile with 'small' shape

### Components

M3 components are more flexible and configurable than their M2.5 counterparts.
M2.5 often required distinct components for varied visual treatments, while M3
frequently uses a generalized, highly configurable base component with good
defaults.

This principle also applies to the root layout. In M2.5, this was either a
[`PrimaryLayout`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material/layouts/PrimaryLayout) or an [`EdgeContentLayout`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material/layouts/EdgeContentLayout). In M3, after you
establish a single top-level `MaterialScope`, you call the
[`primaryLayout()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).primaryLayout(kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.material3.PrimaryLayoutMargins)) function. This function returns the root layout
directly---no builders needed---and accepts `LayoutElements` for several slots, such
as `titleSlot`, `mainSlot`, and `bottomSlot`. You can populate these slots with
concrete UI components---such as those returned by [`text()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).text(androidx.wear.protolayout.types.LayoutString,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Int,androidx.wear.protolayout.types.LayoutColor,kotlin.Boolean,kotlin.Boolean,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List)),
[`button()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).button(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,kotlin.Function1,androidx.wear.protolayout.material3.ButtonStyle,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)), or [`card()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).card(androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Padding,kotlin.Function1))---or with layout structures, such as `Row` or
`Column` from [`LayoutElementBuilders`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders).

Themes are another key M3 enhancement. By default, UI elements automatically
adhere to M3 styling specifications and support dynamic theming.

| M2.5 | M3 |
|---|---|
| **Interactive Elements** |   |
| [`Button`](https://developer.android.com/reference/androidx/wear/protolayout/material/Button) or [`Chip`](https://developer.android.com/reference/androidx/wear/protolayout/material/Chip) | - Buttons: [`button`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).button(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,kotlin.Function1,androidx.wear.protolayout.material3.ButtonStyle,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`avatarButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).avatarButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,androidx.wear.protolayout.material3.AvatarButtonStyle,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`compactButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).compactButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`iconEdgeButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).iconEdgeButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.material3.ButtonColors,kotlin.Function1)), [`imageButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).imageButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension)), [`textButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).textButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.ButtonColors,androidx.wear.protolayout.material3.TextButtonStyle,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`textEdgeButton()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).textEdgeButton(androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.material3.ButtonColors,kotlin.Function1)). - Cards: [`card()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).card(androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Padding,kotlin.Function1)), [`appCard()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).appCard(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.CardColors,kotlin.Function1,androidx.wear.protolayout.material3.AppCardStyle,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`graphicDataCard()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).graphicDataCard(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.CardColors,androidx.wear.protolayout.material3.GraphicDataCardStyle,kotlin.Int,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`iconDataCard()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).iconDataCard(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.CardColors,kotlin.Function1,androidx.wear.protolayout.material3.DataCardStyle,androidx.wear.protolayout.material3.TitleContentPlacementInDataCard,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`textDataCard()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).textDataCard(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.CardColors,kotlin.Function1,androidx.wear.protolayout.material3.DataCardStyle,androidx.wear.protolayout.ModifiersBuilders.Padding)), [`titleCard()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).titleCard(androidx.wear.protolayout.ModifiersBuilders.Clickable,kotlin.Function1,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.ModifiersBuilders.Corner,androidx.wear.protolayout.material3.CardColors,kotlin.Function1,androidx.wear.protolayout.material3.TitleCardStyle,androidx.wear.protolayout.ModifiersBuilders.Padding,kotlin.Int)). |
| **Text** |   |
| [`Text`](https://developer.android.com/reference/androidx/wear/protolayout/material/Text) | [`text()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).text(androidx.wear.protolayout.types.LayoutString,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Int,androidx.wear.protolayout.types.LayoutColor,kotlin.Boolean,kotlin.Boolean,kotlin.Boolean,kotlin.Int,kotlin.Int,kotlin.Int,kotlin.collections.List)) |
| **Progress Indicators** |   |
| [`CircularProgressIndicator`](https://developer.android.com/reference/androidx/wear/protolayout/material/CircularProgressIndicator) | [`circularProgressIndicator()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).circularProgressIndicator(kotlin.Float,androidx.wear.protolayout.expression.DynamicBuilders.DynamicFloat,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,androidx.wear.protolayout.material3.ProgressIndicatorColors,androidx.wear.protolayout.DimensionBuilders.ContainerDimension)) or [`segmentedCircularProgressIndicator()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).segmentedCircularProgressIndicator(kotlin.Int,kotlin.Float,androidx.wear.protolayout.expression.DynamicBuilders.DynamicFloat,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Float,kotlin.Float,kotlin.Float,kotlin.Float,androidx.wear.protolayout.material3.ProgressIndicatorColors,androidx.wear.protolayout.DimensionBuilders.ContainerDimension)) |
| **Layout** |   |
| [`PrimaryLayout`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material/layouts/PrimaryLayout) or [`EdgeContentLayout`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material/layouts/EdgeContentLayout) | [`primaryLayout()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).primaryLayout(kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,androidx.wear.protolayout.ModifiersBuilders.Clickable,androidx.wear.protolayout.material3.PrimaryLayoutMargins)) |
| --- | [`buttonGroup()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/package-summary#(androidx.wear.protolayout.material3.MaterialScope).buttonGroup(androidx.wear.protolayout.DimensionBuilders.ContainerDimension,androidx.wear.protolayout.DimensionBuilders.ContainerDimension,kotlin.Float,kotlin.Function1)) |
| **Images** |   |
| --- | [`icon()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).icon(kotlin.String,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.types.LayoutColor)), [`avatarImage()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).avatarImage(kotlin.String,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.modifiers.LayoutModifier,kotlin.Int)) or [`backgroundImage()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/material3/MaterialScope#(androidx.wear.protolayout.material3.MaterialScope).backgroundImage(kotlin.String,androidx.wear.protolayout.modifiers.LayoutModifier,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.DimensionBuilders.ImageDimension,androidx.wear.protolayout.types.LayoutColor,kotlin.Int)) |

#### Modifiers

In M3, [`Modifiers`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/package-summary), which you use to decorate or augment a component, are
more Compose-like. This change can reduce boilerplate by automatically
constructing the appropriate internal types. (This change is orthogonal to the
use of M3 UI components; if necessary, you can use builder-style modifiers from
ProtoLayout 1.2 with M3 UI components, and the other way around.)

### M2.5


```kotlin
// Uses Builder-style modifier to set opacity
fun myModifier(): ModifiersBuilders.Modifiers =
    ModifiersBuilders.Modifiers.Builder()
        .setOpacity(TypeBuilders.FloatProp.Builder(0.5F).build())
        .build()
```

<br />

### M3


```kotlin
// Uses Compose-like modifiers to set opacity
fun myModifier(): LayoutModifier = LayoutModifier.opacity(0.5F)
```

<br />

You can construct modifiers using either API style, and you can also use the
[`toProtoLayoutModifiers()`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/modifiers/LayoutModifier#(androidx.wear.protolayout.modifiers.LayoutModifier).toProtoLayoutModifiers()) extension function to convert a
`LayoutModifier` to a `ModifiersBuilders.Modifier`.

#### Helper Functions

While ProtoLayout 1.3 allows many UI components to be expressed using a
Compose-inspired API, foundational layout elements like [rows](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders.Row.Builder) and
[columns](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders.Column.Builder) from [`LayoutElementBuilders`](https://developer.android.com/reference/kotlin/androidx/wear/protolayout/LayoutElementBuilders) continue to use the builder
pattern. To bridge this stylistic gap and promote consistency with the new M3
component APIs, consider using helper functions.

### Without Helpers


```kotlin
primaryLayout(
    mainSlot = {
        Column.Builder()
            .setWidth(expand())
            .setHeight(expand())
            .addContent(text("A".layoutString))
            .addContent(text("B".layoutString))
            .addContent(text("C".layoutString))
            .build()
    }
)
```

<br />

### With Helpers


```kotlin
// Function literal with receiver helper function
fun column(builder: Column.Builder.() -> Unit) =
    Column.Builder().apply(builder).build()

primaryLayout(
    mainSlot = {
        column {
            setWidth(expand())
            setHeight(expand())
            addContent(text("A".layoutString))
            addContent(text("B".layoutString))
            addContent(text("C".layoutString))
        }
    }
)
```

<br />

## Migrate to Tiles 1.2 / ProtoLayout 1.0

As of version 1.2, most Tiles layout APIs are in the `androidx.wear.protolayout`
namespace. To use the latest APIs, complete the following migration steps in
your code.

### Update dependencies

In your app module's build file, make the following changes:

### Groovy

```groovy
  // Remove
  implementation 'androidx.wear.tiles:tiles-material:version'

  // Include additional dependencies
  implementation "androidx.wear.protolayout:protolayout:1.3.0"
  implementation "androidx.wear.protolayout:protolayout-material:1.3.0"
  implementation "androidx.wear.protolayout:protolayout-expression:1.3.0"

  // Update
  implementation "androidx.wear.tiles:tiles:1.5.0"
```

### Kotlin

```kotlin
  // Remove
  implementation("androidx.wear.tiles:tiles-material:version")

  // Include additional dependencies
  implementation("androidx.wear.protolayout:protolayout:1.3.0")
  implementation("androidx.wear.protolayout:protolayout-material:1.3.0")
  implementation("androidx.wear.protolayout:protolayout-expression:1.3.0")

  // Update
  implementation("androidx.wear.tiles:tiles:1.5.0")
```

### Update namespaces

In your app's Kotlin- and Java-based code files, make the following updates:
Alternatively, you can execute this [namespace renaming
script](https://gist.github.com/NedaTop/5c3b72cda4c6450df3670eb6300db4e4).

1. Replace all `androidx.wear.tiles.material.*` imports with `androidx.wear.protolayout.material.*`. Complete this step for the `androidx.wear.tiles.material.layouts` library, too.
2. Replace most other `androidx.wear.tiles.*` imports with
   `androidx.wear.protolayout.*`.

   Imports for `androidx.wear.tiles.EventBuilders`,
   `androidx.wear.tiles.RequestBuilders`, `androidx.wear.tiles.TileBuilders`,
   and `androidx.wear.tiles.TileService` should stay the same.
3. Rename a few deprecated methods from TileService and TileBuilder classes:

   1. `TileBuilders`: `getTimeline()` to `getTileTimeline()`, and `setTimeline()` to `setTileTimeline()`
   2. `TileService`: `onResourcesRequest()` to `onTileResourcesRequest()`
   3. `RequestBuilders.TileRequest`: `getDeviceParameters()` to `getDeviceConfiguration()`, `setDeviceParameters()` to `setDeviceConfiguration()`, `getState()` to `getCurrentState()`, and `setState()` to `setCurrentState()`

   > [!NOTE]
   > **Note:** Starting in version 1.2 of the library, there are `getState()` and `setState()` methods in the `TileBuilders` class and these are the correct ones to use. These are different from the `RequestBuilders.getState()` and `RequestBuilders.setState()` methods.