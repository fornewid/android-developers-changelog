---
title: https://developer.android.com/develop/ui/compose/quick-guides/content/display-layered-image
url: https://developer.android.com/develop/ui/compose/quick-guides/content/display-layered-image
source: md.txt
---

<br />

You can blend or overlay source images to display layered images on a canvas.
For example, you can replicate how the Android Framework generates app icons by
combining separate background and foreground drawables. To display layered
images, you must do the following:

- Layer images on a canvas.
- Overlay the source.

## Results

![Custom Painter that overlays two images on top of each other](https://developer.android.com/static/develop/ui/compose/images/graphics-rainbowoverlay.jpg) **Figure 1** : An `Image` that uses a custom `Painter` to overlay a semi-transparent rainbow image over the image of a dog.

## Version compatibility

This implementation requires that your project minSDK be set to API level 21 or
higher.

### Dependencies

<iframe src="https://android.devsite.google/frame/develop/ui/compose/quick-guides/content/display-layered-image_cb4c7009a37ca03bc38c7d51d0fd6bae5e3b84d0d59469b89f93ca70b3b96ba1.frame" class="framebox inherit-locale " allow="clipboard-write https://android.devsite.google" allowfullscreen is-upgraded></iframe>

## Layer images on a canvas

The following code layers two source images on top of each other, rendering a
blended image on the canvas:


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

### Key points about the code

- Uses `OverlayImagePainter`, which is a custom [`Painter`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/painter/Painter) implementation that you can use to overlay images over the source image. The blend mode controls how the images are combined. The first image is not overwriting anything else, so no blend mode is needed. The `Overlay` blend mode of the second image overwrites the areas of the first image that are covered by the second image.
- `DrawScope.onDraw()` is overridden and the two images are overlaid in this function.
- `intrinsicSize` is overridden to correctly report the intrinsic size of the combined image.

## Overlay source image

With this custom painter `Painter`, you can overlay an image on top of the
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

### Key points about the code

- The images to be combined are each loaded as [`ImageBitmap`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap) instances before being combined using `OverlayImagePainter`.
- The combined images are rendered by an [`Image`](https://developer.android.com/reference/kotlin/androidx/compose/foundation/package-summary#Image(androidx.compose.ui.graphics.ImageBitmap,kotlin.String,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,androidx.compose.ui.layout.ContentScale,kotlin.Float,androidx.compose.ui.graphics.ColorFilter,androidx.compose.ui.graphics.FilterQuality)) composable that uses the custom painter to combine the source images when rendering.

## Collections that contain this guide

This guide is part of these curated Quick Guide collections that cover
broader Android development goals:
![](https://developer.android.com/static/images/quick-guides/collection-illustration.png) ![](https://developer.android.com/static/images/picto-icons/collection.svg)

### Display images

Discover techniques for using bright, engaging visuals to give your Android app a beautiful look and feel. [Quick guide collection](https://developer.android.com/develop/ui/compose/quick-guides/collections/display-images) ![](https://developer.android.com/static/images/picto-icons/help.svg)

## Have questions or feedback

Go to our frequently asked questions page and learn about quick guides or reach out and let us know your thoughts. [Go to FAQ](https://developer.android.com/quick-guides/faq) [Leave feedback](https://issuetracker.google.com/issues/new?component=1573691&template=1993320)