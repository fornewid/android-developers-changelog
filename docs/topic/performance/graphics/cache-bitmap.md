---
title: https://developer.android.com/topic/performance/graphics/cache-bitmap
url: https://developer.android.com/topic/performance/graphics/cache-bitmap
source: md.txt
---

# Caching Bitmaps

**Note:** For most cases, we recommend that you use the[Glide](https://github.com/bumptech/glide)library to fetch, decode, and display bitmaps in your app. Glide abstracts out most of the complexity in handling these and other tasks related to working with bitmaps and other images on Android. For information about using and downloading Glide, visit the[Glide repository](https://github.com/bumptech/glide)on GitHub.

Loading a single bitmap into your user interface (UI) is straightforward, however things get more complicated if you need to load a larger set of images at once. In many cases (such as with components like[ListView](https://developer.android.com/reference/android/widget/ListView),[GridView](https://developer.android.com/reference/android/widget/GridView)or[ViewPager](https://developer.android.com/reference/androidx/viewpager/widget/ViewPager)), the total number of images on-screen combined with images that might soon scroll onto the screen are essentially unlimited.

Memory usage is kept down with components like this by recycling the child views as they move off-screen. The garbage collector also frees up your loaded bitmaps, assuming you don't keep any long lived references. This is all good and well, but in order to keep a fluid and fast-loading UI you want to avoid continually processing these images each time they come back on-screen. A memory and disk cache can often help here, allowing components to quickly reload processed images.

This lesson walks you through using a memory and disk bitmap cache to improve the responsiveness and fluidity of your UI when loading multiple bitmaps.

## Use a Memory Cache

A memory cache offers fast access to bitmaps at the cost of taking up valuable application memory. The[LruCache](https://developer.android.com/reference/android/util/LruCache)class (also available in the[Support Library](https://developer.android.com/reference/androidx/collection/LruCache)for use back to API Level 4) is particularly well suited to the task of caching bitmaps, keeping recently referenced objects in a strong referenced[LinkedHashMap](https://developer.android.com/reference/java/util/LinkedHashMap)and evicting the least recently used member before the cache exceeds its designated size.

**Note:** In the past, a popular memory cache implementation was a[SoftReference](https://developer.android.com/reference/java/lang/ref/SoftReference)or[WeakReference](https://developer.android.com/reference/java/lang/ref/WeakReference)bitmap cache, however this is not recommended. Starting from Android 2.3 (API Level 9) the garbage collector is more aggressive with collecting soft/weak references which makes them fairly ineffective. In addition, prior to Android 3.0 (API Level 11), the backing data of a bitmap was stored in native memory which is not released in a predictable manner, potentially causing an application to briefly exceed its memory limits and crash.

In order to choose a suitable size for a[LruCache](https://developer.android.com/reference/android/util/LruCache), a number of factors should be taken into consideration, for example:

- How memory intensive is the rest of your activity and/or application?
- How many images will be on-screen at once? How many need to be available ready to come on-screen?
- What is the screen size and density of the device? An extra high density screen (xhdpi) device like[Galaxy Nexus](https://www.android.com/devices/detail/galaxy-nexus)will need a larger cache to hold the same number of images in memory compared to a device like[Nexus S](https://www.android.com/devices/detail/nexus-s)(hdpi).
- What dimensions and configuration are the bitmaps and therefore how much memory will each take up?
- How frequently will the images be accessed? Will some be accessed more frequently than others? If so, perhaps you may want to keep certain items always in memory or even have multiple[LruCache](https://developer.android.com/reference/android/util/LruCache)objects for different groups of bitmaps.
- Can you balance quality against quantity? Sometimes it can be more useful to store a larger number of lower quality bitmaps, potentially loading a higher quality version in another background task.

There is no specific size or formula that suits all applications, it's up to you to analyze your usage and come up with a suitable solution. A cache that is too small causes additional overhead with no benefit, a cache that is too large can once again cause`java.lang.OutOfMemory`exceptions and leave the rest of your app little memory to work with.

Here's an example of setting up a[LruCache](https://developer.android.com/reference/android/util/LruCache)for bitmaps:  

### Kotlin

```kotlin
private lateinit var memoryCache: LruCache<String, Bitmap>

override fun onCreate(savedInstanceState: Bundle?) {
    ...
    // Get max available VM memory, exceeding this amount will throw an
    // OutOfMemory exception. Stored in kilobytes as LruCache takes an
    // int in its constructor.
    val maxMemory = (Runtime.getRuntime().maxMemory() / 1024).toInt()

    // Use 1/8th of the available memory for this memory cache.
    val cacheSize = maxMemory / 8

    memoryCache = object : LruCache<String, Bitmap>(cacheSize) {

        override fun sizeOf(key: String, bitmap: Bitmap): Int {
            // The cache size will be measured in kilobytes rather than
            // number of items.
            return bitmap.byteCount / 1024
        }
    }
    ...
}
```

### Java

```java
private LruCache<String, Bitmap> memoryCache;

@Override
protected void onCreate(Bundle savedInstanceState) {
    ...
    // Get max available VM memory, exceeding this amount will throw an
    // OutOfMemory exception. Stored in kilobytes as LruCache takes an
    // int in its constructor.
    final int maxMemory = (int) (Runtime.getRuntime().maxMemory() / 1024);

    // Use 1/8th of the available memory for this memory cache.
    final int cacheSize = maxMemory / 8;

    memoryCache = new LruCache<String, Bitmap>(cacheSize) {
        @Override
        protected int sizeOf(String key, Bitmap bitmap) {
            // The cache size will be measured in kilobytes rather than
            // number of items.
            return bitmap.getByteCount() / 1024;
        }
    };
    ...
}

public void addBitmapToMemoryCache(String key, Bitmap bitmap) {
    if (getBitmapFromMemCache(key) == null) {
        memoryCache.put(key, bitmap);
    }
}

public Bitmap getBitmapFromMemCache(String key) {
    return memoryCache.get(key);
}
```

**Note:** In this example, one eighth of the application memory is allocated for our cache. On a normal/hdpi device this is a minimum of around 4MB (32/8). A full screen[GridView](https://developer.android.com/reference/android/widget/GridView)filled with images on a device with 800x480 resolution would use around 1.5MB (800\*480\*4 bytes), so this would cache a minimum of around 2.5 pages of images in memory.

When loading a bitmap into an[ImageView](https://developer.android.com/reference/android/widget/ImageView), the[LruCache](https://developer.android.com/reference/android/util/LruCache)is checked first. If an entry is found, it is used immediately to update the[ImageView](https://developer.android.com/reference/android/widget/ImageView), otherwise a background thread is spawned to process the image:  

### Kotlin

```kotlin
fun loadBitmap(resId: Int, imageView: ImageView) {
    val imageKey: String = resId.toString()

    val bitmap: Bitmap? = getBitmapFromMemCache(imageKey)?.also {
        mImageView.setImageBitmap(it)
    } ?: run {
        mImageView.setImageResource(R.drawable.image_placeholder)
        val task = BitmapWorkerTask()
        task.execute(resId)
        null
    }
}
```

### Java

```java
public void loadBitmap(int resId, ImageView imageView) {
    final String imageKey = String.valueOf(resId);

    final Bitmap bitmap = getBitmapFromMemCache(imageKey);
    if (bitmap != null) {
        mImageView.setImageBitmap(bitmap);
    } else {
        mImageView.setImageResource(R.drawable.image_placeholder);
        BitmapWorkerTask task = new BitmapWorkerTask(mImageView);
        task.execute(resId);
    }
}
```

The[`BitmapWorkerTask`](https://developer.android.com/topic/performance/graphics/process-bitmap#BitmapWorkerTask)also needs to be updated to add entries to the memory cache:  

### Kotlin

```kotlin
private inner class BitmapWorkerTask : AsyncTask<Int, Unit, Bitmap>() {
    ...
    // Decode image in background.
    override fun doInBackground(vararg params: Int?): Bitmap? {
        return params[0]?.let { imageId ->
            decodeSampledBitmapFromResource(resources, imageId, 100, 100)?.also { bitmap ->
                addBitmapToMemoryCache(imageId.toString(), bitmap)
            }
        }
    }
    ...
}
```

### Java

```java
class BitmapWorkerTask extends AsyncTask<Integer, Void, Bitmap> {
    ...
    // Decode image in background.
    @Override
    protected Bitmap doInBackground(Integer... params) {
        final Bitmap bitmap = decodeSampledBitmapFromResource(
                getResources(), params[0], 100, 100));
        addBitmapToMemoryCache(String.valueOf(params[0]), bitmap);
        return bitmap;
    }
    ...
}
```

## Use a Disk Cache

A memory cache is useful in speeding up access to recently viewed bitmaps, however you cannot rely on images being available in this cache. Components like[GridView](https://developer.android.com/reference/android/widget/GridView)with larger datasets can easily fill up a memory cache. Your application could be interrupted by another task like a phone call, and while in the background it might be killed and the memory cache destroyed. Once the user resumes, your application has to process each image again.

A disk cache can be used in these cases to persist processed bitmaps and help decrease loading times where images are no longer available in a memory cache. Of course, fetching images from disk is slower than loading from memory and should be done in a background thread, as disk read times can be unpredictable.

**Note:** A[ContentProvider](https://developer.android.com/reference/android/content/ContentProvider)might be a more appropriate place to store cached images if they are accessed more frequently, for example in an image gallery application.

The sample code of this class uses a`DiskLruCache`implementation that is pulled from the[Android source](https://android.googlesource.com/platform/libcore/+/jb-mr2-release/luni/src/main/java/libcore/io/DiskLruCache.java). Here's updated example code that adds a disk cache in addition to the existing memory cache:  

### Kotlin

```kotlin
private const val DISK_CACHE_SIZE = 1024 * 1024 * 10 // 10MB
private const val DISK_CACHE_SUBDIR = "thumbnails"
...
private var diskLruCache: DiskLruCache? = null
private val diskCacheLock = ReentrantLock()
private val diskCacheLockCondition: Condition = diskCacheLock.newCondition()
private var diskCacheStarting = true

override fun onCreate(savedInstanceState: Bundle?) {
    ...
    // Initialize memory cache
    ...
    // Initialize disk cache on background thread
    val cacheDir = getDiskCacheDir(this, DISK_CACHE_SUBDIR)
    InitDiskCacheTask().execute(cacheDir)
    ...
}

internal inner class InitDiskCacheTask : AsyncTask<File, Void, Void>() {
    override fun doInBackground(vararg params: File): Void? {
        diskCacheLock.withLock {
            val cacheDir = params[0]
            diskLruCache = DiskLruCache.open(cacheDir, DISK_CACHE_SIZE)
            diskCacheStarting = false // Finished initialization
            diskCacheLockCondition.signalAll() // Wake any waiting threads
        }
        return null
    }
}

internal inner class  BitmapWorkerTask : AsyncTask<Int, Unit, Bitmap>() {
    ...

    // Decode image in background.
    override fun doInBackground(vararg params: Int?): Bitmap? {
        val imageKey = params[0].toString()

        // Check disk cache in background thread
        return getBitmapFromDiskCache(imageKey) ?:
                // Not found in disk cache
                decodeSampledBitmapFromResource(resources, params[0], 100, 100)
                        ?.also {
                            // Add final bitmap to caches
                            addBitmapToCache(imageKey, it)
                        }
    }
}

fun addBitmapToCache(key: String, bitmap: Bitmap) {
    // Add to memory cache as before
    if (getBitmapFromMemCache(key) == null) {
        memoryCache.put(key, bitmap)
    }

    // Also add to disk cache
    synchronized(diskCacheLock) {
        diskLruCache?.apply {
            if (!containsKey(key)) {
                put(key, bitmap)
            }
        }
    }
}

fun getBitmapFromDiskCache(key: String): Bitmap? =
        diskCacheLock.withLock {
            // Wait while disk cache is started from background thread
            while (diskCacheStarting) {
                try {
                    diskCacheLockCondition.await()
                } catch (e: InterruptedException) {
                }

            }
            return diskLruCache?.get(key)
        }

// Creates a unique subdirectory of the designated app cache directory. Tries to use external
// but if not mounted, falls back on internal storage.
fun getDiskCacheDir(context: Context, uniqueName: String): File {
    // Check if media is mounted or storage is built-in, if so, try and use external cache dir
    // otherwise use internal cache dir
    val cachePath =
            if (Environment.MEDIA_MOUNTED == Environment.getExternalStorageState()
                    || !isExternalStorageRemovable()) {
                context.externalCacheDir.path
            } else {
                context.cacheDir.path
            }

    return File(cachePath + File.separator + uniqueName)
}
```

### Java

```java
private DiskLruCache diskLruCache;
private final Object diskCacheLock = new Object();
private boolean diskCacheStarting = true;
private static final int DISK_CACHE_SIZE = 1024 * 1024 * 10; // 10MB
private static final String DISK_CACHE_SUBDIR = "thumbnails";

@Override
protected void onCreate(Bundle savedInstanceState) {
    ...
    // Initialize memory cache
    ...
    // Initialize disk cache on background thread
    File cacheDir = getDiskCacheDir(this, DISK_CACHE_SUBDIR);
    new InitDiskCacheTask().execute(cacheDir);
    ...
}

class InitDiskCacheTask extends AsyncTask<File, Void, Void> {
    @Override
    protected Void doInBackground(File... params) {
        synchronized (diskCacheLock) {
            File cacheDir = params[0];
            diskLruCache = DiskLruCache.open(cacheDir, DISK_CACHE_SIZE);
            diskCacheStarting = false; // Finished initialization
            diskCacheLock.notifyAll(); // Wake any waiting threads
        }
        return null;
    }
}

class BitmapWorkerTask extends AsyncTask<Integer, Void, Bitmap> {
    ...
    // Decode image in background.
    @Override
    protected Bitmap doInBackground(Integer... params) {
        final String imageKey = String.valueOf(params[0]);

        // Check disk cache in background thread
        Bitmap bitmap = getBitmapFromDiskCache(imageKey);

        if (bitmap == null) { // Not found in disk cache
            // Process as normal
            final Bitmap bitmap = decodeSampledBitmapFromResource(
                    getResources(), params[0], 100, 100));
        }

        // Add final bitmap to caches
        addBitmapToCache(imageKey, bitmap);

        return bitmap;
    }
    ...
}

public void addBitmapToCache(String key, Bitmap bitmap) {
    // Add to memory cache as before
    if (getBitmapFromMemCache(key) == null) {
        memoryCache.put(key, bitmap);
    }

    // Also add to disk cache
    synchronized (diskCacheLock) {
        if (diskLruCache != null && diskLruCache.get(key) == null) {
            diskLruCache.put(key, bitmap);
        }
    }
}

public Bitmap getBitmapFromDiskCache(String key) {
    synchronized (diskCacheLock) {
        // Wait while disk cache is started from background thread
        while (diskCacheStarting) {
            try {
                diskCacheLock.wait();
            } catch (InterruptedException e) {}
        }
        if (diskLruCache != null) {
            return diskLruCache.get(key);
        }
    }
    return null;
}

// Creates a unique subdirectory of the designated app cache directory. Tries to use external
// but if not mounted, falls back on internal storage.
public static File getDiskCacheDir(Context context, String uniqueName) {
    // Check if media is mounted or storage is built-in, if so, try and use external cache dir
    // otherwise use internal cache dir
    final String cachePath =
            Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState()) ||
                    !isExternalStorageRemovable() ? getExternalCacheDir(context).getPath() :
                            context.getCacheDir().getPath();

    return new File(cachePath + File.separator + uniqueName);
}
```

**Note:**Even initializing the disk cache requires disk operations and therefore should not take place on the main thread. However, this does mean there's a chance the cache is accessed before initialization. To address this, in the above implementation, a lock object ensures that the app does not read from the disk cache until the cache has been initialized.

While the memory cache is checked in the UI thread, the disk cache is checked in the background thread. Disk operations should never take place on the UI thread. When image processing is complete, the final bitmap is added to both the memory and disk cache for future use.

## Handle Configuration Changes

Runtime configuration changes, such as a screen orientation change, cause Android to destroy and restart the running activity with the new configuration (For more information about this behavior, see[Handling Runtime Changes](https://developer.android.com/guide/topics/resources/runtime-changes)). You want to avoid having to process all your images again so the user has a smooth and fast experience when a configuration change occurs.

Luckily, you have a nice memory cache of bitmaps that you built in the[Use a Memory Cache](https://developer.android.com/topic/performance/graphics/cache-bitmap#memory-cache)section. This cache can be passed through to the new activity instance using a[Fragment](https://developer.android.com/reference/android/app/Fragment)which is preserved by calling[setRetainInstance(true)](https://developer.android.com/reference/android/app/Fragment#setRetainInstance(boolean)). After the activity has been recreated, this retained[Fragment](https://developer.android.com/reference/android/app/Fragment)is reattached and you gain access to the existing cache object, allowing images to be quickly fetched and re-populated into the[ImageView](https://developer.android.com/reference/android/widget/ImageView)objects.

Here's an example of retaining a[LruCache](https://developer.android.com/reference/android/util/LruCache)object across configuration changes using a[Fragment](https://developer.android.com/reference/android/app/Fragment):  

### Kotlin

```kotlin
private const val TAG = "RetainFragment"
...
private lateinit var mMemoryCache: LruCache<String, Bitmap>

override fun onCreate(savedInstanceState: Bundle?) {
    ...
    val retainFragment = RetainFragment.findOrCreateRetainFragment(supportFragmentManager)
    mMemoryCache = retainFragment.retainedCache ?: run {
        LruCache<String, Bitmap>(cacheSize).also { memoryCache ->
            ... // Initialize cache here as usual
            retainFragment.retainedCache = memoryCache
        }
    }
    ...
}

class RetainFragment : Fragment() {
    var retainedCache: LruCache<String, Bitmap>? = null

    companion object {
        fun findOrCreateRetainFragment(fm: FragmentManager): RetainFragment {
            return (fm.findFragmentByTag(TAG) as? RetainFragment) ?: run {
                RetainFragment().also {
                    fm.beginTransaction().add(it, TAG).commit()
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        retainInstance = true
    }
}
```

### Java

```java
private LruCache<String, Bitmap> memoryCache;

@Override
protected void onCreate(Bundle savedInstanceState) {
    ...
    RetainFragment retainFragment =
            RetainFragment.findOrCreateRetainFragment(getFragmentManager());
    memoryCache = retainFragment.retainedCache;
    if (memoryCache == null) {
        memoryCache = new LruCache<String, Bitmap>(cacheSize) {
            ... // Initialize cache here as usual
        }
        retainFragment.retainedCache = memoryCache;
    }
    ...
}

class RetainFragment extends Fragment {
    private static final String TAG = "RetainFragment";
    public LruCache<String, Bitmap> retainedCache;

    public RetainFragment() {}

    public static RetainFragment findOrCreateRetainFragment(FragmentManager fm) {
        RetainFragment fragment = (RetainFragment) fm.findFragmentByTag(TAG);
        if (fragment == null) {
            fragment = new RetainFragment();
            fm.beginTransaction().add(fragment, TAG).commit();
        }
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setRetainInstance(true);
    }
}
```

To test this out, try rotating a device both with and without retaining the[Fragment](https://developer.android.com/reference/android/app/Fragment). You should notice little to no lag as the images populate the activity almost instantly from memory when you retain the cache. Any images not found in the memory cache are hopefully available in the disk cache, if not, they are processed as usual.