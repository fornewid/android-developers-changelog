---
title: https://developer.android.com/develop/ui/compose/graphics/images/optimization
url: https://developer.android.com/develop/ui/compose/graphics/images/optimization
source: md.txt
---

Working with images can quickly introduce performance issues if you aren't
careful. Even a small graphic in a compressed format like JPG or PNG can turn
into a large bitmap when it's decoded for display.If you aren't efficient
with how you use graphics, you can run into memory problems
which can hurt the performance of your app and other apps on the device.
Follow these best practices to ensure your app performs at its best.

## Use image loading libraries

You can improve your app's efficiency by using image loading libraries
like [Coil](https://coil-kt.github.io/coil/api/coil-core/coil3.request/-image-request/) (for Kotlin-first projects) or [Glide](https://bumptech.github.io/glide/javadocs/470/com/bumptech/glide/load/DecodeFormat.html) (for Java projects).
These libraries reduce your app's memory usage by doing things like caching
images, resizing graphics when needed, and recycling graphic objects.

## Resize images when appropriate

Make sure to use the appropriate image size for your needs. For example, you
should never load a large image into a small thumbnail. Instead, use a method
like [`inSampleSize`](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inSampleSize) to load a resampled version of the image.

Image-loading libraries like Coil and Glide handle this resampling for you
automatically by default. You can configure their downsampling strategies by
using [`ImageLoader`](https://coil-kt.github.io/coil/image_loaders/) (for Coil) or [`DownsampleStrategy`](https://bumptech.github.io/glide/javadocs/470/com/bumptech/glide/load/resource/bitmap/DownsampleStrategy.html) (for Glide).

### Supply alternative resources for different screen sizes

If you are shipping images with your app, consider supplying different sized
assets for different device resolutions. This can help reduce the download size
of your app on devices, and improve performance as it'll load up a lower
resolution image on a lower resolution device. For more information on providing
alternative bitmaps for different device sizes, [check out the alternative
bitmap documentation](https://developer.android.com/training/multiscreen/screendensities#TaskProvideAltBmp).

## Don't apply padding directly

Sometimes you might need to add padding to an image. For example, you might
want to have the image surrounded by a transparent border for letterboxing.
In those situations, *don't* add the padding directly to the image, changing
the image's dimensions. Instead, leave the image's dimensions as they are,
and adjust the image's location on the screen by using [`InsetDrawable`](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable).
Alternatively, you can add padding into the Composable or View holding the
image.

## Choose the right pixel format

Balance memory and quality by choosing the right pixel format. Use `RGB_565`
when you don't need transparency; this format uses half the memory of the
default `ARGB_8888` format.

In Glide you can configure this by using [`DecodeFormat`](https://bumptech.github.io/glide/javadocs/470/com/bumptech/glide/load/DecodeFormat.html). In Coil, you can
use the [`bitmapConfig`](https://coil-kt.github.io/coil/api/coil-core/coil3.request/-image-request/) property.

## Use vectors where possible

For images made up of geometric shapes, a vector graphic is much smaller than a
bitmap and scales smoothly for any display density. When suitable, use elements
like [`ShapeDrawable`](https://developer.android.com/reference/android/graphics/drawable/ShapeDrawable) to represent graphics.

## Release and reuse bitmaps when you can

Large graphic files can take up a lot of memory. To reduce their impact, you
should release or reuse the graphic objects whenever you can.

If you use an image loading library, make sure to release
bitmaps to the library's managed pool when you no longer need them. The
library can reuse the objects when needed, and keeps a memory buffer available
for future needs.

If you're managing graphics manually, you should release
bitmaps when you're done with them by calling [`Bitmap.recycle`](https://developer.android.com/reference/android/graphics/Bitmap#recycle())
and immediately discarding the `Bitmap` reference, instead
of relying on garbage collection.

## Other tips and tricks

This section lists a few other ways to improve your app's performance when
handling graphics.

### Don't package large images with your AAB/APK file

One of the top causes for large app download size is graphics that are
packaged inside the AAB or APK file. Use the [APK analyzer](https://developer.android.com/studio/debug/apk-analyzer) tool to ensure
that you aren't packaging larger than required image files. Reduce the sizes or
consider placing the images on a server and only downloading them when required.

### Find redundant bitmaps

If you have several copies of the same image, that wastes memory. You can use
the Android Studio profiler to identify redundant graphics. Use the [heap dump
analyzer](https://developer.android.com/studio/profile/capture-heap-dump) to capture a heap dump, and filter the results by choosing the
**duplicate bitmaps** setting.

### When using `ImageBitmap`, call `prepareToDraw` before drawing

When using `ImageBitmap`, to start the process of uploading the texture to the
GPU, call [`ImageBitmap#prepareToDraw()`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap#prepareToDraw()) before actually drawing it. This
helps the GPU prepare the texture and improve the performance of showing a
visual on screen. Most image loading libraries already do this optimization, but
if you are working with the `ImageBitmap` class yourself, it is something to
keep in mind.

### Prefer passing a `Int` `DrawableRes` or URL as parameters into your composable instead of `Painter`

Due to the complexities of dealing with images (for example, writing an equals
function for `Bitmaps` would be computationally expensive), the `Painter` API is
explicitly not marked as stable with the [`@Stable`](https://medium.com/androiddevelopers/jetpack-compose-stability-explained-79c10db270c8)
annotation. Unstable classes can lead to unnecessary recompositions because the
compiler cannot easily infer if the data has changed.

Therefore, we recommend passing a URL or drawable resource ID as parameters
to your composable, instead of passing a `Painter` as a parameter.

    // Prefer this:
    @Composable
    fun MyImage(url: String) {

    }
    // Over this:
    @Composable
    fun MyImage(painter: Painter) {

    }

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [ImageBitmap versus ImageVector {:#bitmap-vs-vector}](https://developer.android.com/develop/ui/compose/graphics/images/compare)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving)
- [Jetpack Compose Phases](https://developer.android.com/develop/ui/compose/phases)