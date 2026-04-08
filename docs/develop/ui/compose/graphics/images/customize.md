---
title: Customize an image  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/graphics/images/customize
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Customize an image Stay organized with collections Save and categorize content based on your preferences.



You can customize images using properties on an `Image` composable
(`contentScale`, `colorFilter`). You can also apply existing [modifiers](/develop/ui/compose/modifiers-list)
to apply different effects to your `Image`. Modifiers can be used on **any
composable**, not just the `Image` composable, whereas `contentScale` and
`colorFilter` are explicit parameters on the `Image` composable.

## Content scale

Specify a `contentScale` option to crop or change how an image is scaled inside
its bounds. By default, if you don't specify a `contentScale` option,
`ContentScale.Fit` is used.

In the following example, the `Image` composable is restricted to a 150dp size
with a border, and the background is set to yellow on the `Image` composable to
showcase the different `ContentScale` options in the table below.

```
val imageModifier = Modifier
    .size(150.dp)
    .border(BorderStroke(1.dp, Color.Black))
    .background(Color.Yellow)
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Fit,
    modifier = imageModifier
)

CustomizeImageSnippets.kt
```

Setting different `ContentScale` options results in different outputs. The
following table helps you choose the correct `ContentScale` mode:

|  |  |  |
| --- | --- | --- |
| **Source image** | The portrait source, which shows a dog. | The landscape source, which shows a different dog. |
| `ContentScale` | Result - Portrait Image: | Result - Landscape Image: |
| `ContentScale.Fit`: Scale the image uniformly, keeping the aspect ratio (default). If content is smaller than the size, the image is scaled up to fit the bounds. | A dog portrait scaled uniformly. | A dog landscape scaled uniformly. |
| `ContentScale.Crop`: Center crop the image into the available space. | A portrait image cropped to fill a square frame, showing only the central part of the image. | A landscape image cropped to fill a square frame, showing only the central part of the image. |
| `ContentScale.FillHeight`: Scale the source maintaining the aspect ratio so that the bounds match the destination height. | A portrait image scaled to fill the height of a square frame, showing the full image with yellow background visible on the left and right. | A landscape image scaled to fill the height of a square frame, with the sides cropped. |
| `ContentScale.FillWidth`: Scale the source maintaining the aspect ratio so that the bounds match the destination width. | A portrait image scaled to fill the width of a square frame, with the top and bottom cropped. | A landscape image scaled to fill the width of a square frame, showing the full image with yellow background visible on the top and bottom. |
| `ContentScale.FillBounds`: Scale the content vertically and horizontally **non-uniformly** to fill the destination bounds. (Note: This distorts images if you place them in containers that don't match the exact ratio of the image). | A portrait image distorted to completely fill a square frame, stretching the image. | A landscape image distorted to completely fill a square frame, stretching the image. |
| `ContentScale.Inside`: Scale the source to maintain the aspect ratio inside the destination bounds. If the source is smaller than or equal to the destination in both dimensions, it behaves similarly to `None`. Content will always be contained within the bounds. If content is smaller than bounds, no scaling will apply. | Source image bigger than bounds: A portrait image, originally larger than its square bounds, scaled down to fit while maintaining aspect ratio, showing yellow background on the sides. Source image smaller than bounds: A portrait image, originally smaller than its square bounds, displayed at its original size within the frame, showing a yellow background around it. | Source image bigger than bounds: A landscape image, originally larger than its square bounds, scaled down to fit while maintaining aspect ratio, showing yellow background on the top and bottom. Source image smaller than bounds: A landscape image, originally smaller than its square bounds, displayed at its original size within the frame, showing a yellow background around it. |
| `ContentScale.None`: Don't apply any scaling to the source. If the content is smaller than destination bounds, it won't be scaled up to fit the area. | Source image bigger than bounds: A portrait image, originally larger than its square bounds, displayed at its original size, with parts extending beyond the top and bottom of the frame. Source image smaller than bounds: A portrait image, originally smaller than its square bounds, displayed at its original size within the frame, showing a yellow background around it. | Source image bigger than bounds: A landscape image, originally larger than its square bounds, displayed at its original size, with parts extending beyond the left and right of the frame. Source image smaller than bounds: A landscape image, originally smaller than its square bounds, displayed at its original size within the frame, showing a yellow background around it. |

## Clip an `Image` composable to a shape

To make an image fit into a shape, use the built-in `clip` modifier.
To crop an image into a circle shape, use `Modifier.clip(CircleShape)`:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(200.dp)
        .clip(CircleShape)
)

CustomizeImageSnippets.kt
```

![An image of a dog clipped into a perfect circle.](/static/develop/ui/compose/images/graphics-clipcircle.png)


**Figure 1**. Clipping an image with `CircleShape`.

For a rounded corner shape, use `Modifier.clip(RoundedCornerShape(16.dp)`), with
the size of the corners you want to be rounded:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(200.dp)
        .clip(RoundedCornerShape(16.dp))
)

CustomizeImageSnippets.kt
```

![A square image of a dog clipped with rounded corners.](/static/develop/ui/compose/images/graphics-roundedcorners.png)


**Figure 2**. Clipping an image with `RoundedCornerShape`.

You can also create your own clipping shape by extending `Shape`, and providing
a `Path` for the shape to clip around:

```
class SquashedOval : Shape {
    override fun createOutline(
        size: Size,
        layoutDirection: LayoutDirection,
        density: Density
    ): Outline {
        val path = Path().apply {
            // We create an Oval that starts at ¼ of the width, and ends at ¾ of the width of the container.
            addOval(
                Rect(
                    left = size.width / 4f,
                    top = 0f,
                    right = size.width * 3 / 4f,
                    bottom = size.height
                )
            )
        }
        return Outline.Generic(path = path)
    }
}

Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(200.dp)
        .clip(SquashedOval())
)

CustomizeImageSnippets.kt
```

![A square image of a dog clipped into a custom, oval shape.](/static/develop/ui/compose/images/graphics-customcrop.png)


**Figure 3**. Clipping an image with a custom path shape.

## Add a border to an `Image` composable

A common operation is to combine the `Modifier.border()` with `Modifier.clip()`
to create a border around an image:

```
val borderWidth = 4.dp
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(150.dp)
        .border(
            BorderStroke(borderWidth, Color.Yellow),
            CircleShape
        )
        .padding(borderWidth)
        .clip(CircleShape)
)

CustomizeImageSnippets.kt
```

![A square image of a dog, clipped into a circle, with a yellow border around the circular shape.](/static/develop/ui/compose/images/graphics-border.png)


**Figure 4**. A clipped image with a border around it.

To create a gradient border, you can use the [`Brush`](/reference/kotlin/androidx/compose/ui/graphics/Brush) API to
draw a rainbow gradient border around the image:

```
val rainbowColorsBrush = remember {
    Brush.sweepGradient(
        listOf(
            Color(0xFF9575CD),
            Color(0xFFBA68C8),
            Color(0xFFE57373),
            Color(0xFFFFB74D),
            Color(0xFFFFF176),
            Color(0xFFAED581),
            Color(0xFF4DD0E1),
            Color(0xFF9575CD)
        )
    )
}
val borderWidth = 4.dp
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(150.dp)
        .border(
            BorderStroke(borderWidth, rainbowColorsBrush),
            CircleShape
        )
        .padding(borderWidth)
        .clip(CircleShape)
)

CustomizeImageSnippets.kt
```

![A circular image of a dog with a rainbow gradient border around the circular shape.](/static/develop/ui/compose/images/graphics-gradientborder.png)


**Figure 5**. Rainbow gradient circle border.

## Set a custom aspect ratio

To transform an image into a custom aspect ratio, use
`Modifier.aspectRatio(16f/9f)` to provide a custom ratio for an image (or any
composable).

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    modifier = Modifier.aspectRatio(16f / 9f)
)

CustomizeImageSnippets.kt
```

![A square image of a dog, transformed to a 16:9 aspect ratio, making it wider and shorter.](/static/develop/ui/compose/images/graphics-aspectratio.png)


**Figure 6**. Using `Modifier.aspectRatio(16f/9f)` on an `Image`.

## Color filter: transform pixel colors of image

The `Image` composable has a `colorFilter` parameter that can change the output
of individual pixels of your image.

### Tint images

Using `ColorFilter.tint(color, blendMode)` applies a blend mode with the
given color onto your `Image` composable. `ColorFilter.tint(color, blendMode)`
uses `BlendMode.SrcIn` to tint content, meaning that the color supplied is
shown where the image is displayed on screen. This is useful for icons and
vectors that need to be themed differently.

```
Image(
    painter = painterResource(id = R.drawable.baseline_directions_bus_24),
    contentDescription = stringResource(id = R.string.bus_content_description),
    colorFilter = ColorFilter.tint(Color.Yellow)
)

CustomizeImageSnippets.kt
```

![An image of a bus with a yellow tint applied.](/static/develop/ui/compose/images/graphics-bus.png)


**Figure 7**. `ColorFilter.tint` applied with `BlendMode.SrcIn`.

Other `BlendMode`s result in different effects. For example, setting
`BlendMode.Darken` with a `Color.Green` on an image produces the following
result:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    colorFilter = ColorFilter.tint(Color.Green, blendMode = BlendMode.Darken)
)

CustomizeImageSnippets.kt
```

![A a dog with a green tint applied using BlendMode.Darken, resulting in darker green shades.](/static/develop/ui/compose/images/graphics-blendmode.png)


**Figure 8**. `Color.Green tint` with `BlendMode.Darken`.

See the [`BlendMode` reference documentation](/reference/kotlin/androidx/compose/ui/graphics/BlendMode) for more information on the
different blend modes available.

### Apply an `Image` filter with color matrix

Transform your image using the color matrix `ColorFilter` option. For example,
to apply a black and white filter onto your images you could use the
[`ColorMatrix`](/reference/kotlin/androidx/compose/ui/graphics/ColorMatrix) and set the saturation to `0f`.

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    colorFilter = ColorFilter.colorMatrix(ColorMatrix().apply { setToSaturation(0f) })
)

CustomizeImageSnippets.kt
```

![A dog with a black and white filter applied, removing all color saturation.](/static/develop/ui/compose/images/graphics-bw.png)


**Figure 9**. Color matrix with saturation 0 (black and white image).

#### Adjust contrast or brightness of an `Image` composable

To change the contrast and brightness of an image, you can use the
[`ColorMatrix`](/reference/kotlin/androidx/compose/ui/graphics/ColorMatrix) to change the values:

```
val contrast = 2f // 0f..10f (1 should be default)
val brightness = -180f // -255f..255f (0 should be default)
val colorMatrix = floatArrayOf(
    contrast, 0f, 0f, 0f, brightness,
    0f, contrast, 0f, 0f, brightness,
    0f, 0f, contrast, 0f, brightness,
    0f, 0f, 0f, 1f, 0f
)
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    colorFilter = ColorFilter.colorMatrix(ColorMatrix(colorMatrix))
)

CustomizeImageSnippets.kt
```

![A dog with increased brightness and contrast, making it appear more vivid.](/static/develop/ui/compose/images/graphics-colormatrix.png)


**Figure 10**. Adjusted image brightness and contrast using `ColorMatrix`.

#### Invert colors of an `Image` composable

To invert the colors of an image, set the [`ColorMatrix`](/reference/kotlin/androidx/compose/ui/graphics/ColorMatrix) to invert the
colors:

```
val colorMatrix = floatArrayOf(
    -1f, 0f, 0f, 0f, 255f,
    0f, -1f, 0f, 0f, 255f,
    0f, 0f, -1f, 0f, 255f,
    0f, 0f, 0f, 1f, 0f
)
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    colorFilter = ColorFilter.colorMatrix(ColorMatrix(colorMatrix))
)

CustomizeImageSnippets.kt
```

![A dog with its colors inverted, showing a negative-like effect.](/static/develop/ui/compose/images/graphics-inverted.png)


**Figure 11**. Inverted colors on image.

## Blur an `Image` composable

To blur an image, use `Modifier.blur()`, supplying the `radiusX` and `radiusY`,
which specifies the blur radius in the horizontal and vertical direction
respectively.

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(150.dp)
        .blur(
            radiusX = 10.dp,
            radiusY = 10.dp,
            edgeTreatment = BlurredEdgeTreatment(RoundedCornerShape(8.dp))
        )
)

CustomizeImageSnippets.kt
```

![A dog with a strong blur effect applied, making it appear indistinct and out of focus.](/static/develop/ui/compose/images/graphics-blur.png)


**Figure 12**. `BlurEffect` applied to an image.

When blurring `Images`, it is recommended to use `BlurredEdgeTreatment(Shape)`,
instead of `BlurredEdgeTreatment.Unbounded`, as the latter is used for blurring
of arbitrary renderings that are expected to render outside the bounds of the
original content. For images, it is likely that they won't render outside the
bounds of the content, whereas blurring a rounded rectangle may require this
distinction.

For example, if we set the `BlurredEdgeTreatment` to `Unbounded` on the
preceding image, the edges of the image appear blurred instead of sharp:

```
Image(
    painter = painterResource(id = R.drawable.dog),
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier
        .size(150.dp)
        .blur(
            radiusX = 10.dp,
            radiusY = 10.dp,
            edgeTreatment = BlurredEdgeTreatment.Unbounded
        )
        .clip(RoundedCornerShape(8.dp))
)

CustomizeImageSnippets.kt
```

![A blurred image of a dog, where the blur extends beyond the original image boundaries, making the edges fuzzy.](/static/develop/ui/compose/images/graphics-unbounded.png)


**Figure 13**. `BlurEdgeTreatment.Unbounded`.

**Note:** The blur effect is only supported on Android 12 and later. Attempts to use
this modifier on older Android versions are ignored.


## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Graphics Modifiers](/develop/ui/compose/graphics/draw/modifiers)
* [Loading images](/develop/ui/compose/graphics/images/loading)
* [Material icons](/develop/ui/compose/graphics/images/material)

[Previous

arrow\_back

Material icons](/develop/ui/compose/graphics/images/material)

[Next

Custom painter

arrow\_forward](/develop/ui/compose/graphics/images/custompainter)