---
title: https://developer.android.com/develop/ui/compose/graphics/images/optimization
url: https://developer.android.com/develop/ui/compose/graphics/images/optimization
source: md.txt
---

Working with images can quickly introduce performance issues if you aren't
careful. You can quite easily run into an `OutOfMemoryError` when working
with large bitmaps. Follow these best practices to ensure your app performs at
its best.

## Only load the size of the bitmap you need

Most smartphones have high resolution cameras that produce large image files. If
you're showing an image on screen, you must either reduce the resolution of the
image or only load the image up to the size of your image container. The
constant loading of larger than needed images can exhaust GPU caches, leading to
less performant UI rendering.

To manage image sizes:

- Scale down your image files to be as small as possible (without affecting output image).
- Consider [converting your images to WEBP](https://developer.android.com/studio/write/convert-webp) format instead of JPEG or PNGs.
- Supply smaller images for different screen resolutions (see [Tip #3](https://developer.android.com/develop/ui/compose/graphics/images/optimization#screen-sizes)),
- Use an [image loading library](https://developer.android.com/develop/ui/compose/graphics/images/loading#load_an_image_from_the_internet), which scales down your image to fit the size of your view on screen. This can help improve the loading performance of your screen.

| **Caution:** Using `painterResource` will **not** scale your image to the size of the Composable that is visible on screen. If you have a large image in a small Composable, be sure to use an image loading library which scales the image down for you to fit the bounds.

#### Use vectors over bitmaps where possible

When representing something visually on screen, you need to decide if it can be
represented as a vector or not. Prefer vector images over bitmaps, as they
don't pixelate when you scale them to different sizes. However, not everything
can be represented as a vector - images taken with a camera can't be converted
into a vector.

#### Supply alternative resources for different screen sizes

If you are shipping images with your app, consider supplying different sized
assets for different device resolutions. This can help reduce the download size
of your app on devices, and improve performance as it'll load up a lower
resolution image on a lower resolution device. For more information on providing
alternative bitmaps for different device sizes, [check out the alternative
bitmap documentation](https://developer.android.com/training/multiscreen/screendensities#TaskProvideAltBmp).

#### When using `ImageBitmap`, call `prepareToDraw` before drawing

When using `ImageBitmap`, to start the process of uploading the texture to the
GPU, call [`ImageBitmap#prepareToDraw()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap#prepareToDraw()) before actually drawing it. This
helps the GPU prepare the texture and improve the performance of showing a
visual on screen. Most image loading libraries already do this optimization, but
if you are working with the `ImageBitmap` class yourself, it is something to
keep in mind.

#### Prefer passing a `Int` `DrawableRes` or URL as parameters into your composable instead of `Painter`

Due to the complexities of dealing with images (for example, writing an equals
function for `Bitmaps` would be computationally expensive), the `Painter` API is
explicitly not marked as a [Stable](https://medium.com/androiddevelopers/jetpack-compose-stability-explained-79c10db270c8) class. Unstable classes can
lead to unnecessary recompositions because the compiler cannot easily infer if
the data has changed.

Therefore, it is preferable to pass a URL or drawable resource ID as parameters
to your composable, instead of passing a `Painter` as a parameter.  

    // Prefer this:
    @Composable
    fun MyImage(url: String) {

    }
    // Over this:
    @Composable
    fun MyImage(painter: Painter) {

    }

## Don't store a bitmap in memory longer than you need it

The more bitmaps you load into memory, the more likely it is that you could run
out of memory on the device. For instance, if loading a large list of Image
composables on screen, use `LazyColumn` or `LazyRow` to ensure that memory is
freed up when scrolling a large list.

## Don't package large images with your AAB/APK file

One of the top causes for large app download size is due to graphics that are
packaged inside the AAB or APK file. Use the [APK analyzer](https://developer.android.com/studio/debug/apk-analyzer) tool to ensure
that you aren't packaging larger than required image files. Reduce the sizes or
consider placing the images on a server and only downloading them when required.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [ImageBitmap vs ImageVector {:#bitmap-vs-vector}](https://developer.android.com/develop/ui/compose/graphics/images/compare)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)
- [Jetpack Compose Phases](https://developer.android.com/develop/ui/compose/phases)