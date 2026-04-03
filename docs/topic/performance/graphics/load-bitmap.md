---
title: https://developer.android.com/topic/performance/graphics/load-bitmap
url: https://developer.android.com/topic/performance/graphics/load-bitmap
source: md.txt
---

# Loading Large Bitmaps Efficiently

**Note:** There are several libraries that follow best practices for loading images. You can use these libraries in your app to load images in the most optimized manner. We recommend the[Glide](https://github.com/bumptech/glide)library, which loads and displays images as quickly and smoothly as possible. Other popular image loading libraries include[Picasso](http://square.github.io/picasso/)from Square,[Coil](https://github.com/coil-kt/coil)from Instacart, and[Fresco](https://github.com/facebook/fresco)from Facebook. These libraries simplify most of the complex tasks associated with bitmaps and other types of images on Android.

Images come in all shapes and sizes. In many cases they are larger than required for a typical application user interface (UI). For example, the system Gallery application displays photos taken using your Android devices's camera which are typically much higher resolution than the screen density of your device.

Given that you are working with limited memory, ideally you only want to load a lower resolution version in memory. The lower resolution version should match the size of the UI component that displays it. An image with a higher resolution does not provide any visible benefit, but still takes up precious memory and incurs additional performance overhead due to additional on the fly scaling.

This lesson walks you through decoding large bitmaps without exceeding the per application memory limit by loading a smaller subsampled version in memory.

## Read Bitmap Dimensions and Type

The[BitmapFactory](https://developer.android.com/reference/android/graphics/BitmapFactory)class provides several decoding methods ([decodeByteArray()](https://developer.android.com/reference/android/graphics/BitmapFactory#decodeByteArray(byte[], int, int, android.graphics.BitmapFactory.Options)),[decodeFile()](https://developer.android.com/reference/android/graphics/BitmapFactory#decodeFile(java.lang.String, android.graphics.BitmapFactory.Options)),[decodeResource()](https://developer.android.com/reference/android/graphics/BitmapFactory#decodeResource(android.content.res.Resources, int, android.graphics.BitmapFactory.Options)), etc.) for creating a[Bitmap](https://developer.android.com/reference/android/graphics/Bitmap)from various sources. Choose the most appropriate decode method based on your image data source. These methods attempt to allocate memory for the constructed bitmap and therefore can easily result in an`OutOfMemory`exception. Each type of decode method has additional signatures that let you specify decoding options via the[BitmapFactory.Options](https://developer.android.com/reference/android/graphics/BitmapFactory.Options)class. Setting the[inJustDecodeBounds](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inJustDecodeBounds)property to`true`while decoding avoids memory allocation, returning`null`for the bitmap object but setting[outWidth](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#outWidth),[outHeight](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#outHeight)and[outMimeType](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#outMimeType). This technique allows you to read the dimensions and type of the image data prior to construction (and memory allocation) of the bitmap.  

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

To avoid`java.lang.OutOfMemory`exceptions, check the dimensions of a bitmap before decoding it, unless you absolutely trust the source to provide you with predictably sized image data that comfortably fits within the available memory.

## Load a Scaled Down Version into Memory

Now that the image dimensions are known, they can be used to decide if the full image should be loaded into memory or if a subsampled version should be loaded instead. Here are some factors to consider:

- Estimated memory usage of loading the full image in memory.
- Amount of memory you are willing to commit to loading this image given any other memory requirements of your application.
- Dimensions of the target[ImageView](https://developer.android.com/reference/android/widget/ImageView)or UI component that the image is to be loaded into.
- Screen size and density of the current device.

For example, it's not worth loading a 1024x768 pixel image into memory if it will eventually be displayed in a 128x96 pixel thumbnail in an[ImageView](https://developer.android.com/reference/android/widget/ImageView).

To tell the decoder to subsample the image, loading a smaller version into memory, set[inSampleSize](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inSampleSize)to`true`in your[BitmapFactory.Options](https://developer.android.com/reference/android/graphics/BitmapFactory.Options)object. For example, an image with resolution 2048x1536 that is decoded with an[inSampleSize](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inSampleSize)of 4 produces a bitmap of approximately 512x384. Loading this into memory uses 0.75MB rather than 12MB for the full image (assuming a bitmap configuration of[ARGB_8888](https://developer.android.com/reference/android/graphics/Bitmap.Config)). Here's a method to calculate a sample size value that is a power of two based on a target width and height:  

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

**Note:** A power of two value is calculated because the decoder uses a final value by rounding down to the nearest power of two, as per the[inSampleSize](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inSampleSize)documentation.

To use this method, first decode with[inJustDecodeBounds](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inJustDecodeBounds)set to`true`, pass the options through and then decode again using the new[inSampleSize](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inSampleSize)value and[inJustDecodeBounds](https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inJustDecodeBounds)set to`false`:  

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

This method makes it easy to load a bitmap of arbitrarily large size into an[ImageView](https://developer.android.com/reference/android/widget/ImageView)that displays a 100x100 pixel thumbnail, as shown in the following example code:  

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

You can follow a similar process to decode bitmaps from other sources, by substituting the appropriate[BitmapFactory.decode*](https://developer.android.com/reference/android/graphics/BitmapFactory#decodeByteArray(byte[], int, int, android.graphics.BitmapFactory.Options))method as needed.