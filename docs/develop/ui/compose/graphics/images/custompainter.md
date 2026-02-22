---
title: https://developer.android.com/develop/ui/compose/graphics/images/custompainter
url: https://developer.android.com/develop/ui/compose/graphics/images/custompainter
source: md.txt
---

In Compose, a `Painter` object is used to represent something that can be drawn
(a replacement to the `Drawable` APIs defined in Android) and influence
measurement and layout of the corresponding composable that is using it . A
`BitmapPainter` takes an `ImageBitmap` that can draw a `Bitmap` on screen.

For most use cases, using the `painterResource()` above returns the correct
painter for the asset (i.e. `BitmapPainter` or `VectorPainter`). For more
information on the differences between the two - read the [ImageBitmap vs ImageVector](https://developer.android.com/develop/ui/compose/graphics/images/compare) section.

A `Painter` is different from a `DrawModifier`, which strictly draws within the
bounds that are given to it and has no influence on the measurement or layout of
the composable.

To create a custom painter, extend the `Painter` class, and implement the
`onDraw` method, which allows access to the `DrawScope` to draw custom
graphics. You can also override the `intrinsicSize`, which will be used to
influence the Composable that it is contained in:


```kotlin
class OverlayImagePainter constructor(
    private val image: ImageBitmap,
    private val imageOverlay: ImageBitmap,
    private val srcOffset: IntOffset = IntOffset.Zero,
    private val srcSize: IntSize = IntSize(image.width, image.height),
    private val overlaySize: IntSize = IntSize(imageOverlay.width, imageOverlay.height)
) : Painter() {

    private val size: IntSize = validateSize(srcOffset, srcSize)
    override fun DrawScope.onDraw() {
        // draw the first image without any blend mode
        drawImage(
            image,
            srcOffset,
            srcSize,
            dstSize = IntSize(
                this@onDraw.size.width.roundToInt(),
                this@onDraw.size.height.roundToInt()
            )
        )
        // draw the second image with an Overlay blend mode to blend the two together
        drawImage(
            imageOverlay,
            srcOffset,
            overlaySize,
            dstSize = IntSize(
                this@onDraw.size.width.roundToInt(),
                this@onDraw.size.height.roundToInt()
            ),
            blendMode = BlendMode.Overlay
        )
    }

    /**
     * Return the dimension of the underlying [ImageBitmap] as it's intrinsic width and height
     */
    override val intrinsicSize: Size get() = size.toSize()

    private fun validateSize(srcOffset: IntOffset, srcSize: IntSize): IntSize {
        require(
            srcOffset.x >= 0 &&
                srcOffset.y >= 0 &&
                srcSize.width >= 0 &&
                srcSize.height >= 0 &&
                srcSize.width <= image.width &&
                srcSize.height <= image.height
        )
        return srcSize
    }
}
```

<br />

Now that we have our custom `Painter`, we can overlay any image on top of our
source image as follows:


```kotlin
val rainbowImage = ImageBitmap.imageResource(id = R.drawable.rainbow)
val dogImage = ImageBitmap.imageResource(id = R.drawable.dog)
val customPainter = remember {
    OverlayImagePainter(dogImage, rainbowImage)
}
Image(
    painter = customPainter,
    contentDescription = stringResource(id = R.string.dog_content_description),
    contentScale = ContentScale.Crop,
    modifier = Modifier.wrapContentSize()
)
```

<br />

The output of combining the two images with a custom painter can be seen below:
![Custom Painter that overlays two images on top of each other](https://developer.android.com/static/develop/ui/compose/images/graphics-rainbowoverlay.jpg) **Figure 1**: Custom Painter that overlays two images on top of each other

A custom painter can also be used with the [`Modifier.paint(customPainter)`](https://developer.android.com/reference/kotlin/androidx/compose/ui/draw/package-summary#(androidx.compose.ui.Modifier).paint(androidx.compose.ui.graphics.painter.Painter,kotlin.Boolean,androidx.compose.ui.Alignment,androidx.compose.ui.layout.ContentScale,kotlin.Float,androidx.compose.ui.graphics.ColorFilter))
to draw the content to a composable as follows:


```kotlin
val rainbowImage = ImageBitmap.imageResource(id = R.drawable.rainbow)
val dogImage = ImageBitmap.imageResource(id = R.drawable.dog)
val customPainter = remember {
    OverlayImagePainter(dogImage, rainbowImage)
}
Box(
    modifier =
    Modifier.background(color = Color.Gray)
        .padding(30.dp)
        .background(color = Color.Yellow)
        .paint(customPainter)
) { /** intentionally empty **/ }
```

<br />

> [!NOTE]
> **Note:** The above custom Painter can also be implemented using a `DrawModifier`. If you need to influence measurement or layout, then you should use a `Painter`. If you are only expecting to render in the bounds you are given, then you should use a `DrawModifier` instead.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [ImageBitmap vs ImageVector {:#bitmap-vs-vector}](https://developer.android.com/develop/ui/compose/graphics/images/compare)
- [Graphics in Compose](https://developer.android.com/develop/ui/compose/graphics/draw/overview)
- [Loading images {:#loading-images}](https://developer.android.com/develop/ui/compose/graphics/images/loading)