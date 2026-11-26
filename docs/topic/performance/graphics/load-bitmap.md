---
title: https://developer.android.com/topic/performance/graphics/load-bitmap
url: https://developer.android.com/topic/performance/graphics/load-bitmap
source: md.txt
---

**Note:** To load UI images, use an image-loading
library such as [Coil](https://coil-kt.github.io/coil/)
or [Glide](https://github.com/bumptech/glide)
instead of manual bitmap decoding. For end-to-end guidance on bitmap memory
architecture, adaptive cache sizing, and lifecycle eviction, see
[Optimize bitmap memory](https://developer.android.com/topic/performance/memory/bitmaps.md.txt).

Images come in all shapes and sizes. In many cases they are larger than required for a typical
application user interface (UI). For example, the system Gallery application displays photos taken
using your Android device's camera which are typically much higher resolution than the screen
density of your device.

Given that you are working with limited memory, ideally you only want to load a lower resolution
version in memory. The lower resolution version should match the size of the UI component that
displays it. An image with a higher resolution does not provide any visible benefit, but still takes
up precious memory and incurs additional performance overhead due to additional on-the-fly
scaling.

This guide shows how to decode scaled bitmaps manually. It covers
`ImageDecoder`
on Android 9 (API level 28) and higher,
`BitmapRegionDecoder`
for large zoomable images, and
`BitmapFactory`
on Android 8.1 (API level 27) and lower.

## Decode scaled hardware bitmaps with `ImageDecoder`

On Android 9 (API level 28) and higher, use
`ImageDecoder`
instead of two-pass `BitmapFactory` decoding. Pass an
`OnHeaderDecodedListener`
to read the encoded image size and scale the output within your target bounds.
Set `ALLOCATOR_HARDWARE` to place immutable UI bitmaps in graphics
memory. Hardware bitmaps still count toward the Android vitals bitmap memory
metric, so size them to the container bounds:

```kotlin
val source = ImageDecoder.createSource(resources, R.drawable.myimage)
val bitmap = ImageDecoder.decodeBitmap(source) { decoder, info, _ ->
    decoder.allocator = ImageDecoder.ALLOCATOR_HARDWARE
    val scale = minOf(
        reqWidth.toFloat() / info.size.width,
        reqHeight.toFloat() / info.size.height,
        1f,
    )
    if (scale < 1f) {
        decoder.setTargetSize(
            (info.size.width * scale).roundToInt().coerceAtLeast(1),
            (info.size.height * scale).roundToInt().coerceAtLeast(1),
        )
    }
}
```

## Decode visible tiles with `BitmapRegionDecoder`

For large zoomable images such as maps, floor plans, or product previews, use
`BitmapRegionDecoder`.
Call `decodeRegion`
(with `BitmapFactory.Options.inSampleSize` when zoomed out) to decode
only the visible viewport `Rect` instead of the full-resolution image
in RAM.

## Read bitmap dimensions and type (`BitmapFactory`)

The `BitmapFactory` class provides several decoding methods (`decodeByteArray()`, `decodeFile()`, `decodeResource()`, etc.) for creating a `Bitmap` from various sources. Choose
the most appropriate decode method based on your image data source. These methods attempt to
allocate memory for the constructed bitmap and therefore can easily result in an `OutOfMemory`
exception. Each type of decode method has additional signatures that let you specify decoding
options via the `BitmapFactory.Options` class. Setting the `inJustDecodeBounds` property to `true` while decoding
avoids memory allocation, returning `null` for the bitmap object but setting `outWidth`, `outHeight` and `outMimeType`. This technique allows you to read the
dimensions and type of the image data prior to construction (and memory allocation) of the
bitmap.

### Kotlin

```kotlin
val options = BitmapFactory.Options().apply {
    inJustDecodeBounds = true
}
BitmapFactory.decodeResource(resources, R.id.myimage, options)
val imageHeight: Int = options.outHeight
val imageWidth: Int = options.outWidth
val imageType: String = options.outMimeType
```

### Java

```java
BitmapFactory.Options options = new BitmapFactory.Options();
options.inJustDecodeBounds = true;
BitmapFactory.decodeResource(getResources(), R.id.myimage, options);
int imageHeight = options.outHeight;
int imageWidth = options.outWidth;
String imageType = options.outMimeType;
```

To avoid `java.lang.OutOfMemory` exceptions, check the dimensions of a bitmap before
decoding it, unless you absolutely trust the source to provide you with predictably sized image data
that comfortably fits within the available memory.

## Load a Scaled Down Version into Memory

Now that the image dimensions are known, they can be used to decide if the full image should be
loaded into memory or if a subsampled version should be loaded instead. Here are some factors to
consider:

- Estimated memory usage of loading the full image in memory.
- Amount of memory you are willing to commit to loading this image given any other memory requirements of your application.
- Dimensions of the target `ImageView` or UI component that the image is to be loaded into.
- Screen size and density of the current device.

For example, it's not worth loading a 1024x768 pixel image into memory if it will eventually be
displayed in a 128x96 pixel thumbnail in an `ImageView`.

To subsample the image into a smaller bitmap, set `inSampleSize` to a power-of-two sample size in your `BitmapFactory.Options` object. For example, an image with resolution 2048x1536 that
is decoded with an `inSampleSize` of 4 produces a
bitmap of approximately 512x384. Loading this into memory uses 0.75MB rather than 12MB for the full
image (assuming a bitmap configuration of `ARGB_8888`). Here's
a method to calculate a sample size value that is a power of two based on a target width and
height:

### Kotlin

```kotlin
fun calculateInSampleSize(options: BitmapFactory.Options, reqWidth: Int, reqHeight: Int): Int {
    // Raw height and width of image
    val (height: Int, width: Int) = options.run { outHeight to outWidth }
    var inSampleSize = 1

    if (height > reqHeight || width > reqWidth) {

        val halfHeight: Int = height / 2
        val halfWidth: Int = width / 2

        // Calculate the largest inSampleSize value that is a power of 2 and keeps both
        // height and width larger than the requested height and width.
        while (halfHeight / inSampleSize >= reqHeight && halfWidth / inSampleSize >= reqWidth) {
            inSampleSize *= 2
        }
    }

    return inSampleSize
}
```

### Java

```java
public static int calculateInSampleSize(
            BitmapFactory.Options options, int reqWidth, int reqHeight) {
    // Raw height and width of image
    final int height = options.outHeight;
    final int width = options.outWidth;
    int inSampleSize = 1;

    if (height > reqHeight || width > reqWidth) {

        final int halfHeight = height / 2;
        final int halfWidth = width / 2;

        // Calculate the largest inSampleSize value that is a power of 2 and keeps both
        // height and width larger than the requested height and width.
        while ((halfHeight / inSampleSize) >= reqHeight
                && (halfWidth / inSampleSize) >= reqWidth) {
            inSampleSize *= 2;
        }
    }

    return inSampleSize;
}
```

**Note:** A power of two value is calculated because the decoder uses
a final value by rounding down to the nearest power of two, as per the `inSampleSize` documentation.

To use this method, first decode with `inJustDecodeBounds` set to `true`, pass the options
through and then decode again using the new `inSampleSize` value and `inJustDecodeBounds` set to `false`:

### Kotlin

```kotlin
fun decodeSampledBitmapFromResource(
        res: Resources,
        resId: Int,
        reqWidth: Int,
        reqHeight: Int
): Bitmap {
    // First decode with inJustDecodeBounds=true to check dimensions
    return BitmapFactory.Options().run {
        inJustDecodeBounds = true
        BitmapFactory.decodeResource(res, resId, this)

        // Calculate inSampleSize
        inSampleSize = calculateInSampleSize(this, reqWidth, reqHeight)

        // Decode bitmap with inSampleSize set
        inJustDecodeBounds = false

        BitmapFactory.decodeResource(res, resId, this)
    }
}
```

### Java

```java
public static Bitmap decodeSampledBitmapFromResource(Resources res, int resId,
        int reqWidth, int reqHeight) {

    // First decode with inJustDecodeBounds=true to check dimensions
    final BitmapFactory.Options options = new BitmapFactory.Options();
    options.inJustDecodeBounds = true;
    BitmapFactory.decodeResource(res, resId, options);

    // Calculate inSampleSize
    options.inSampleSize = calculateInSampleSize(options, reqWidth, reqHeight);

    // Decode bitmap with inSampleSize set
    options.inJustDecodeBounds = false;
    return BitmapFactory.decodeResource(res, resId, options);
}
```

This method makes it easy to load a bitmap of arbitrarily large size into an `ImageView` that displays a 100x100 pixel thumbnail, as shown in the following example
code:

### Kotlin

```kotlin
imageView.setImageBitmap(
        decodeSampledBitmapFromResource(resources, R.id.myimage, 100, 100)
)
```

### Java

```java
imageView.setImageBitmap(
    decodeSampledBitmapFromResource(getResources(), R.id.myimage, 100, 100));
```

You can follow a similar process to decode bitmaps from other sources, by substituting the
appropriate `BitmapFactory.decode*` method as needed.