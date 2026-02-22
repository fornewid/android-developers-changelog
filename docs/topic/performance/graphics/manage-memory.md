---
title: https://developer.android.com/topic/performance/graphics/manage-memory
url: https://developer.android.com/topic/performance/graphics/manage-memory
source: md.txt
---

**Note:** For most cases, we recommend that you use the
[Glide](https://github.com/bumptech/glide) library to fetch, decode, and
display bitmaps in your app. Glide abstracts out most of
the complexity in handling these and
other tasks related to working with bitmaps and other images on Android.
For information about using and downloading Glide, visit the
[Glide repository](https://github.com/bumptech/glide) on GitHub.

In addition to the steps described in [Caching Bitmaps](https://developer.android.com/topic/performance/graphics/cache-bitmap),
there are specific things you can do to facilitate garbage collection
and bitmap reuse. The recommended strategy depends on which version(s)
of Android you are targeting. The `BitmapFun` sample app included with
this class shows you how to design your app to work efficiently across
different versions of Android.

To set the stage for this lesson, here is how Android's management of
bitmap memory has evolved:

- On Android 2.2 (API level 8) and lower, when garbage collection occurs, your app's threads get stopped. This causes a lag that can degrade performance. Android 2.3 adds concurrent garbage collection, which means that the memory is reclaimed soon after a bitmap is no longer referenced.
- On Android 2.3.3 (API level 10) and lower, the backing pixel data for a bitmap is stored in native memory. It is separate from the bitmap itself, which is stored in the Dalvik heap. The pixel data in native memory is not released in a predictable manner, potentially causing an application to briefly exceed its memory limits and crash. From Android 3.0 (API level 11) through Android 7.1 (API level 25), the pixel data is stored on the Dalvik heap along with the associated bitmap. In Android 8.0 (API level 26), and higher, the bitmap pixel data is stored in the native heap.

The following sections describe how to optimize bitmap memory
management for different Android versions.

## Manage Memory on Android 2.3.3 and Lower

On Android 2.3.3 (API level 10) and lower, using
`https://developer.android.com/reference/android/graphics/Bitmap#recycle()`
is recommended. If you're displaying large amounts of bitmap data in your app,
you're likely to run into
`https://developer.android.com/reference/java/lang/OutOfMemoryError` errors. The
`https://developer.android.com/reference/android/graphics/Bitmap#recycle()` method allows an app
to reclaim memory as soon as possible.

**Caution:** You should use
`https://developer.android.com/reference/android/graphics/Bitmap#recycle()` only when you are sure that the
bitmap is no longer being used. If you call `https://developer.android.com/reference/android/graphics/Bitmap#recycle()`
and later attempt to draw the bitmap, you will get the error:
`"Canvas: trying to use a recycled bitmap"`.

The following code snippet gives an example of calling
`https://developer.android.com/reference/android/graphics/Bitmap#recycle()`. It uses reference counting
(in the variables `mDisplayRefCount` and `mCacheRefCount`) to track
whether a bitmap is currently being displayed or in the cache. The
code recycles the bitmap when these conditions are met:

- The reference count for both `mDisplayRefCount` and `mCacheRefCount` is 0.
- The bitmap is not `null`, and it hasn't been recycled yet.

### Kotlin

```kotlin
private var cacheRefCount: Int = 0
private var displayRefCount: Int = 0
...
// Notify the drawable that the displayed state has changed.
// Keep a count to determine when the drawable is no longer displayed.
fun setIsDisplayed(isDisplayed: Boolean) {
    synchronized(this) {
        if (isDisplayed) {
            displayRefCount++
            hasBeenDisplayed = true
        } else {
            displayRefCount--
        }
    }
    // Check to see if recycle() can be called.
    checkState()
}

// Notify the drawable that the cache state has changed.
// Keep a count to determine when the drawable is no longer being cached.
fun setIsCached(isCached: Boolean) {
    synchronized(this) {
        if (isCached) {
            cacheRefCount++
        } else {
            cacheRefCount--
        }
    }
    // Check to see if recycle() can be called.
    checkState()
}

@Synchronized
private fun checkState() {
    // If the drawable cache and display ref counts = 0, and this drawable
    // has been displayed, then recycle.
    if (cacheRefCount <= 0
            && displayRefCount <= 0
            && hasBeenDisplayed
            && hasValidBitmap()
    ) {
        getBitmap()?.recycle()
    }
}

@Synchronized
private fun hasValidBitmap(): Boolean =
        getBitmap()?.run {
            !isRecycled
        } ?: false
```

### Java

```java
private int cacheRefCount = 0;
private int displayRefCount = 0;
...
// Notify the drawable that the displayed state has changed.
// Keep a count to determine when the drawable is no longer displayed.
public void setIsDisplayed(boolean isDisplayed) {
    synchronized (this) {
        if (isDisplayed) {
            displayRefCount++;
            hasBeenDisplayed = true;
        } else {
            displayRefCount--;
        }
    }
    // Check to see if recycle() can be called.
    checkState();
}

// Notify the drawable that the cache state has changed.
// Keep a count to determine when the drawable is no longer being cached.
public void setIsCached(boolean isCached) {
    synchronized (this) {
        if (isCached) {
            cacheRefCount++;
        } else {
            cacheRefCount--;
        }
    }
    // Check to see if recycle() can be called.
    checkState();
}

private synchronized void checkState() {
    // If the drawable cache and display ref counts = 0, and this drawable
    // has been displayed, then recycle.
    if (cacheRefCount <= 0 && displayRefCount <= 0 && hasBeenDisplayed
            && hasValidBitmap()) {
        getBitmap().recycle();
    }
}

private synchronized boolean hasValidBitmap() {
    Bitmap bitmap = getBitmap();
    return bitmap != null && !bitmap.isRecycled();
}
```

## Manage Memory on Android 3.0 and Higher

Android 3.0 (API level 11) introduces the
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap`
field. If this option is set, decode methods that take the
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options` object
will attempt to reuse an existing bitmap when loading content. This means
that the bitmap's memory is reused, resulting in improved performance, and
removing both memory allocation and de-allocation. However, there are certain restrictions with how
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap` can be used. In particular, before Android
4.4 (API level 19), only equal sized bitmaps are supported. For details, please see the
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap` documentation.

### Save a bitmap for later use

The following snippet demonstrates how an existing bitmap is stored for possible
later use in the sample app. When an app is running on Android 3.0 or higher and
a bitmap is evicted from the `https://developer.android.com/reference/android/util/LruCache`,
a soft reference to the bitmap is placed
in a `https://developer.android.com/reference/java/util/HashSet`, for possible reuse later with
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap`:

### Kotlin

```kotlin
var reusableBitmaps: MutableSet<SoftReference<Bitmap>>? = null
private lateinit var memoryCache: LruCache<String, BitmapDrawable>
// If you're running on Honeycomb or newer, create a
// synchronized HashSet of references to reusable bitmaps.
if (Utils.hasHoneycomb()) {
    reusableBitmaps = Collections.synchronizedSet(HashSet<SoftReference<Bitmap>>())
}

memoryCache = object : LruCache<String, BitmapDrawable>(cacheParams.memCacheSize) {

    // Notify the removed entry that is no longer being cached.
    override fun entryRemoved(
            evicted: Boolean,
            key: String,
            oldValue: BitmapDrawable,
            newValue: BitmapDrawable
    ) {
        if (oldValue is RecyclingBitmapDrawable) {
            // The removed entry is a recycling drawable, so notify it
            // that it has been removed from the memory cache.
            oldValue.setIsCached(false)
        } else {
            // The removed entry is a standard BitmapDrawable.
            if (Utils.hasHoneycomb()) {
                // We're running on Honeycomb or later, so add the bitmap
                // to a SoftReference set for possible use with inBitmap later.
                reusableBitmaps?.add(SoftReference(oldValue.bitmap))
            }
        }
    }
}
```

### Java

```java
Set<SoftReference<Bitmap>> reusableBitmaps;
private LruCache<String, BitmapDrawable> memoryCache;

// If you're running on Honeycomb or newer, create a
// synchronized HashSet of references to reusable bitmaps.
if (Utils.hasHoneycomb()) {
    reusableBitmaps =
            Collections.synchronizedSet(new HashSet<SoftReference<Bitmap>>());
}

memoryCache = new LruCache<String, BitmapDrawable>(cacheParams.memCacheSize) {

    // Notify the removed entry that is no longer being cached.
    @Override
    protected void entryRemoved(boolean evicted, String key,
            BitmapDrawable oldValue, BitmapDrawable newValue) {
        if (RecyclingBitmapDrawable.class.isInstance(oldValue)) {
            // The removed entry is a recycling drawable, so notify it
            // that it has been removed from the memory cache.
            ((RecyclingBitmapDrawable) oldValue).setIsCached(false);
        } else {
            // The removed entry is a standard BitmapDrawable.
            if (Utils.hasHoneycomb()) {
                // We're running on Honeycomb or later, so add the bitmap
                // to a SoftReference set for possible use with inBitmap later.
                reusableBitmaps.add
                        (new SoftReference<Bitmap>(oldValue.getBitmap()));
            }
        }
    }
....
}
```

### Use an existing bitmap

In the running app, decoder methods check to see if there is an existing
bitmap they can use. For example:

### Kotlin

```kotlin
fun decodeSampledBitmapFromFile(
        filename: String,
        reqWidth: Int,
        reqHeight: Int,
        cache: ImageCache
): Bitmap {

    val options: BitmapFactory.Options = BitmapFactory.Options()
    ...
    BitmapFactory.decodeFile(filename, options)
    ...

    // If we're running on Honeycomb or newer, try to use inBitmap.
    if (Utils.hasHoneycomb()) {
        addInBitmapOptions(options, cache)
    }
    ...
    return BitmapFactory.decodeFile(filename, options)
}
```

### Java

```java
public static Bitmap decodeSampledBitmapFromFile(String filename,
        int reqWidth, int reqHeight, ImageCache cache) {

    final BitmapFactory.Options options = new BitmapFactory.Options();
    ...
    BitmapFactory.decodeFile(filename, options);
    ...

    // If we're running on Honeycomb or newer, try to use inBitmap.
    if (Utils.hasHoneycomb()) {
        addInBitmapOptions(options, cache);
    }
    ...
    return BitmapFactory.decodeFile(filename, options);
}
```

The next snippet shows the `addInBitmapOptions()` method that is called in the
above snippet. It looks for an existing bitmap to set as the value for
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap`. Note that this
method only sets a value for `https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap`
if it finds a suitable match (your code should never assume that a match will be found):

### Kotlin

```kotlin
private fun addInBitmapOptions(options: BitmapFactory.Options, cache: ImageCache?) {
    // inBitmap only works with mutable bitmaps, so force the decoder to
    // return mutable bitmaps.
    options.inMutable = true

    // Try to find a bitmap to use for inBitmap.
    cache?.getBitmapFromReusableSet(options)?.also { inBitmap ->
        // If a suitable bitmap has been found, set it as the value of
        // inBitmap.
        options.inBitmap = inBitmap
    }
}

// This method iterates through the reusable bitmaps, looking for one
// to use for inBitmap:
fun getBitmapFromReusableSet(options: BitmapFactory.Options): Bitmap? {
    mReusableBitmaps?.takeIf { it.isNotEmpty() }?.let { reusableBitmaps ->
        synchronized(reusableBitmaps) {
            val iterator: MutableIterator<SoftReference<Bitmap>> = reusableBitmaps.iterator()
            while (iterator.hasNext()) {
                iterator.next().get()?.let { item ->
                    if (item.isMutable) {
                        // Check to see it the item can be used for inBitmap.
                        if (canUseForInBitmap(item, options)) {
                            // Remove from reusable set so it can't be used again.
                            iterator.remove()
                            return item
                        }
                    } else {
                        // Remove from the set if the reference has been cleared.
                        iterator.remove()
                    }
                }
            }
        }
    }
    return null
}
```

### Java

```java
private static void addInBitmapOptions(BitmapFactory.Options options,
        ImageCache cache) {
    // inBitmap only works with mutable bitmaps, so force the decoder to
    // return mutable bitmaps.
    options.inMutable = true;

    if (cache != null) {
        // Try to find a bitmap to use for inBitmap.
        Bitmap inBitmap = cache.getBitmapFromReusableSet(options);

        if (inBitmap != null) {
            // If a suitable bitmap has been found, set it as the value of
            // inBitmap.
            options.inBitmap = inBitmap;
        }
    }
}

// This method iterates through the reusable bitmaps, looking for one
// to use for inBitmap:
protected Bitmap getBitmapFromReusableSet(BitmapFactory.Options options) {
        Bitmap bitmap = null;

    if (reusableBitmaps != null && !reusableBitmaps.isEmpty()) {
        synchronized (reusableBitmaps) {
            final Iterator<SoftReference<Bitmap>> iterator
                    = reusableBitmaps.iterator();
            Bitmap item;

            while (iterator.hasNext()) {
                item = iterator.next().get();

                if (null != item && item.isMutable()) {
                    // Check to see it the item can be used for inBitmap.
                    if (canUseForInBitmap(item, options)) {
                        bitmap = item;

                        // Remove from reusable set so it can't be used again.
                        iterator.remove();
                        break;
                    }
                } else {
                    // Remove from the set if the reference has been cleared.
                    iterator.remove();
                }
            }
        }
    }
    return bitmap;
}
```

Finally, this method determines whether a candidate bitmap
satisfies the size criteria to be used for
`https://developer.android.com/reference/android/graphics/BitmapFactory.Options#inBitmap`:

### Kotlin

```kotlin
private fun canUseForInBitmap(candidate: Bitmap, targetOptions: BitmapFactory.Options): Boolean {
    return if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
        // From Android 4.4 (KitKat) onward we can re-use if the byte size of
        // the new bitmap is smaller than the reusable bitmap candidate
        // allocation byte count.
        val width = ceil((targetOptions.outWidth * 1.0f / targetOptions.inSampleSize).toDouble()).toInt()
        val height = ceil((targetOptions.outHeight * 1.0f / targetOptions.inSampleSize).toDouble()).toInt()
        val byteCount: Int = width * height * getBytesPerPixel(candidate.config)
        byteCount <= candidate.allocationByteCount
    } else {
        // On earlier versions, the dimensions must match exactly and the inSampleSize must be 1
        candidate.width == targetOptions.outWidth
                && candidate.height == targetOptions.outHeight
                && targetOptions.inSampleSize == 1
    }
}

/**
 * A helper function to return the byte usage per pixel of a bitmap based on its configuration.
 */
private fun getBytesPerPixel(config: Bitmap.Config): Int {
    return when (config) {
        Bitmap.Config.ARGB_8888 -> 4
        Bitmap.Config.RGB_565, Bitmap.Config.ARGB_4444 -> 2
        Bitmap.Config.ALPHA_8 -> 1
        else -> 1
    }
}
```

### Java

```java
static boolean canUseForInBitmap(
        Bitmap candidate, BitmapFactory.Options targetOptions) {

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
        // From Android 4.4 (KitKat) onward we can re-use if the byte size of
        // the new bitmap is smaller than the reusable bitmap candidate
        // allocation byte count.
        int width = (int) Math.ceil(targetOptions.outWidth * 1.0f / targetOptions.inSampleSize);
        int height = (int) Math.ceil(targetOptions.outHeight * 1.0f / targetOptions.inSampleSize);
        int byteCount = width * height * getBytesPerPixel(candidate.getConfig());
        return byteCount <= candidate.getAllocationByteCount();
    }

    // On earlier versions, the dimensions must match exactly and the inSampleSize must be 1
    return candidate.getWidth() == targetOptions.outWidth
            && candidate.getHeight() == targetOptions.outHeight
            && targetOptions.inSampleSize == 1;
}

/**
 * A helper function to return the byte usage per pixel of a bitmap based on its configuration.
 */
static int getBytesPerPixel(Config config) {
    if (config == Config.ARGB_8888) {
        return 4;
    } else if (config == Config.RGB_565) {
        return 2;
    } else if (config == Config.ARGB_4444) {
        return 2;
    } else if (config == Config.ALPHA_8) {
        return 1;
    }
    return 1;
}
```