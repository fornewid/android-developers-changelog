---
title: https://developer.android.com/topic/performance/memory/bitmaps
url: https://developer.android.com/topic/performance/memory/bitmaps
source: md.txt
---

> Documentation index: https://developer.android.com/topic/performance/memory/llms.txt

Decoded bitmaps are frequently the largest contributors to an Android app's
memory footprint. Even when compressed image files on disk or over the network
are only tens of kilobytes, the system must inflate them into uncompressed pixel
buffers before rendering them on screen.

Unbounded bitmap decoding, duplicate caches, and unreleased UI assets drive
out-of-memory (`OutOfMemoryError`) crashes, low-memory killer daemon (`lmkd`)
terminations, zRAM swap thrashing, and degraded multitasking across the device.
This guide explains why bitmap memory grows across device RAM tiers, the four
architectural layers where bitmap defects occur, how to apply the **Reduce,
Reuse, and Recycle (3Rs)** framework, and how to verify fixes locally and in
production.

## Why bitmap memory governs stability

Memory is the silent foundation behind visible app performance metrics such as
smooth scrolling, fast startup, and long battery life. Understanding how excess
bitmap allocations affect the system---and how they scale across hardware
tiers---helps you prioritize the highest-impact optimizations.

### How excess bitmap memory causes jank, battery drain, and kills

When decoded pixel buffers consume a large share of physical RAM, the system
must work continuously to reclaim space:

- **UI jank and dropped frames**: Decoding and scaling oversized bitmaps contend with frame rendering on the critical path, while rapid allocation churn triggers frequent garbage collection pauses that visibly stutter scrolling.
- **Battery drain and ANRs**: Unlike clean file-backed pages (such as compiled code) that the kernel can discard and re-read from storage, anonymous heap pages holding decoded bitmaps must stay in RAM or be compressed into zRAM swap. Continuous kernel page reclaim and zRAM compression consume significant CPU power, draining battery and causing unpredictable Application Not Responding (ANR) delays.
- **Slow cold starts and lost state** : When free memory drops critically low, `lmkd` terminates cached processes---forcing slow cold starts when users return---and can abruptly stop perceptible background services such as active audio playback or uploads.
- **Broader device reach**: Keeping bitmap memory lean lets you ship a responsive experience across every device tier and form factor, while leaving headroom for new features.

### Uncompressed pixel math and native storage

A decoded bitmap's memory footprint depends on its pixel dimensions (`width` ×
`height`) and its [`Bitmap.Config`](https://developer.android.com/reference/android/graphics/Bitmap.Config.md.txt), not its compressed file
size:

    Memory (bytes) = width × height × bytes_per_pixel

Most UI images decode into `ARGB_8888` at **4 bytes per pixel** , while
wide-gamut or HDR images using `RGBA_F16` require **8 bytes per pixel** . A
120 KB JPEG decoded at 2000 × 1500 pixels in `ARGB_8888` consumes 12,000,000
bytes (\~11.44 MiB binary, where 1 MiB = 1,048,576 bytes, or 12.0 MB decimal,
where 1 MB = 1,000,000 bytes).

In Android 8.0 (API level 26) and higher, standard heap bitmap pixel buffers
reside in the **native heap** , while only a small wrapper object (\~56 to 74
bytes) sits on the Java heap. Because those small wrappers add minimal pressure
to the Java heap, routine garbage collection might not reclaim unreferenced
native pixel buffers before system memory limits intervene. By
contrast, [`Bitmap.Config.HARDWARE`](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt#hardware-bitmaps) stores immutable pixel
buffers directly in graphics memory (`DMA-BUF` or `gralloc`) outside both the
Java and native heaps. For low-level storage details, see [Bitmaps and
memory](https://developer.android.com/topic/performance/memory/guide/bitmaps).

### Foreground discipline protects background survival

Keeping your active foreground bitmap working set lean is your strongest defense
against background terminations. Apps that accumulate tens or hundreds of
megabytes of decoded bitmaps during normal browsing carry that footprint
directly into background and foreground-service states whenever the user
switches tasks, answers a call, or opens an external payment or sign-in sheet.
If lifecycle or trim listeners miss even one cache, an oversized foreground
working set pushes the process past [Android 17 app memory
limits](https://developer.android.com/about/versions/17/behavior-changes-all#app-memory-limits) and [Android vitals bad behavior
thresholds](https://developer.android.com/google/play/vitals#core-vitals).

### Scaling across device RAM tiers

Static image pipelines fail in opposite ways across the hardware spectrum. They
waste scarce heap on entry-level phones and inflate GPU graphics buffers on
high-density screens and foldables. [Android vitals bitmap
thresholds](https://developer.android.com/google/play/vitals#core-vitals) don't vary by RAM tier, but align your cache
sizing and test coverage across these four device tiers:

| Device RAM tier | Typical display and form factor | One full-screen `ARGB_8888` frame | Primary bitmap failure mode |
|---|---|---|---|
| **4 GB** (and \<= 3 GB `isLowRamDevice`) | Entry-level HD+ (\~720 × 1600) | \~4.4 MiB (4.6 MB) | **Oversized decode waste and `lmkd` kills**: Fixed high-resolution CDN assets that skip downsampling exhaust scarce RAM during startup or external payment and sign-in app switches. |
| **6-8 GB** | Mainstream FHD+ (\~1080 × 2400) | \~9.9 MiB (10.4 MB) | **Backstack churn and multi-loader collisions**: Cumulative retention across deep feed-to-detail navigation flows or coexisting View and Compose image caches. |
| **12 GB** | Flagship QHD+ (\~1344 × 2992 to 1440 × 3120) | \~15.3-17.1 MiB (16.1-18.0 MB) | **High-DPI viewport and `RGBA_F16` overhead** : Large full-bleed buffers and allocation churn during 120 Hz scrolling when wide-gamut (`8 B/px`) decodes aren't restricted to HDR content. |
| **16 GB+** | High-RAM flagships, tablets, and unfolded foldables (`sw >= 600dp`, \~2076 × 2152) | \~17.0 MiB (17.9 MB) | **Full-width graphics buffer spikes**: Stretching single-column phone layouts across an unfolded canvas (\~3.9× the pixel area of a 720 × 1600 screen) rapidly inflates GPU buffers. |

### How platform limits and Android vitals count bitmaps

Different platform mechanisms and production metrics account for bitmap memory
in distinct ways:

- **Android vitals bitmap memory usage** : [Android vitals](https://developer.android.com/google/play/vitals/bitmap-memory-usage.md.txt) evaluates your app's bitmap footprint across four process states (**Foreground** for leak diagnostics, plus three non-foreground states with [bad behavior thresholds](https://developer.android.com/google/play/vitals.md.txt#core-vitals)):
  - **User-perceived services** (foreground services, expedited jobs, and user-initiated data transfer jobs) and **Background**: 200 MB bad behavior threshold.
  - **Cached**: 400 MB bad behavior threshold.
- **Heap versus graphics and shared buffers** : Standard `malloc`-backed heap bitmaps count toward [Android vitals anonymous RSS + swap](https://developer.android.com/google/play/vitals/memory-usage.md.txt), [Android 17 app memory limits](https://developer.android.com/about/versions/17/behavior-changes-all.md.txt#app-memory-limits), and declarative [app
  memory budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets). Hardware bitmaps (`DMA-BUF`) and shared bitmaps (`ashmem` or `memfd`) sit outside heap budgets, **but count** toward the Android vitals bitmap memory metric.

> [!NOTE]
> **Note:** Android vitals bad behavior thresholds use binary megabytes (`1 MB = 1,024
> KiB = 1 MiB`), so they compare directly with `dumpsys meminfo` (`KiB` divided by 1,024) and heap dump `MiB` totals.

## Four architectural layers of bitmap defects

Before changing code, identify which architectural layer of your app is
producing excess bitmap retention. Common bitmap defects fall into four layers:

### Layer 1: Asset and pixel-level inefficiencies

Defects inside the decoded pixel buffers themselves waste memory regardless of
which UI toolkit you use:

- **Oversized container decodes** : Decoding an image at full screen width (or original camera or CDN dimensions) when rendering inside a smaller card wastes memory **quadratically** : `(decode_width / view_width)^2`. Decoding at full screen width for a two-column grid allocates **4×** the required pixel RAM.
- **Trimmable uniform borders** : Product cutouts, badges, and stickers exported with wide uniform transparent or solid-color outer margins bake layout padding directly into uncompressed `4 B/px` pixel buffers.
- **Bitwise duplicate and empty bitmaps**: Unkeyed custom decodes, repeated icon inflation inside list items, and software-allocated solid or transparent placeholder canvases keep identical or blank pixel buffers resident where shared caches or zero-byte drawables suffice.
- **Inverted low-DPI branches and unintended `RGBA_F16` decodes** : Faulty conditional sizing logic can downsample on high-DPI devices yet fall back to original dimensions on `720p` displays. Similarly, decoders that respect embedded Display P3 ICC profiles on standard sRGB feeds allocate `RGBA_F16` (`8 B/px`), doubling memory without visible benefit.

### Layer 2: Image pipeline and framework architecture

How you configure third-party image, animation, and web libraries determines
how many caches coexist in your process:

- **Multi-loader cache collisions** : Apps migrating incrementally from Views to Jetpack Compose (or across major library versions) often bundle two or more image loaders simultaneously---such as Glide plus Coil, Glide plus Picasso, or Coil 2 plus Coil 3. Because each library initializes an independent in-memory `LruCache` (typically 15% to 25% of heap), running multiple loaders fragments cache memory and stores duplicate decoded copies of the same URLs across separate pools.
- **Vector animation raster frame caches** : Animations that embed raster image layers (such as Lottie `assets` arrays) often pre-render full-resolution `ARGB_8888` frames into static composition caches that register no [`ComponentCallbacks2`](https://developer.android.com/reference/android/content/ComponentCallbacks2.md.txt) listener, pinning large frame buffers across background transitions.
- **Disabled hardware bitmaps** : Leaving static UI images in mutable software configs---either because a library disables `Bitmap.Config.HARDWARE` by default (as Glide does) or because CPU bitmap transformations force software allocation---keeps pixel buffers in the native heap and duplicates memory when uploaded as GPU textures.
- **WebView compositor offloading** : Hybrid screens that offload image-heavy catalogs to `WebView` might show minimal `android.graphics.Bitmap` instances in the app heap while accumulating substantial native and swap memory in the WebView compositor process if `WebView.destroy` is omitted on exit. See [Manage and diagnose WebView memory](https://developer.android.com/topic/performance/memory/guide/webview-memory.md.txt).

### Layer 3: Lifecycle, process state, and navigation

Even well-sized bitmaps can push your app over [Android vitals bad behavior
thresholds](https://developer.android.com/google/play/vitals#core-vitals) if your app retains them after the UI leaves the
screen:

- **`TRIM_MEMORY_UI_HIDDEN` deafness** : Starting in Android 14 (API level 34), the system no longer sends `TRIM_MEMORY_RUNNING_*`, `TRIM_MEMORY_MODERATE`, or `TRIM_MEMORY_COMPLETE` callbacks (formally deprecated in Android 15, API level 35). Apps must rely on the [`TRIM_MEMORY_UI_HIDDEN`](https://developer.android.com/reference/android/content/ComponentCallbacks2.md.txt#TRIM_MEMORY_UI_HIDDEN) and [`TRIM_MEMORY_BACKGROUND`](https://developer.android.com/reference/android/content/ComponentCallbacks2.md.txt#TRIM_MEMORY_BACKGROUND) constants. However, most image and animation libraries retain 50% to 100% of their in-memory caches on `TRIM_MEMORY_UI_HIDDEN` unless explicitly configured.
- **The `ForegroundService` UI-retention trap** : When a user leaves your UI while a foreground service (such as media playback, location, connected-device sync, or an upload) runs in the same process, the system keeps the process at [`IMPORTANCE_FOREGROUND_SERVICE`](https://developer.android.com/reference/android/app/ActivityManager.RunningAppProcessInfo.md.txt#IMPORTANCE_FOREGROUND_SERVICE) (`oom_score_adj` 200 to 249). It delivers `TRIM_MEMORY_UI_HIDDEN`, **but
  never delivers `TRIM_MEMORY_BACKGROUND`**, leaving UI-hidden-deaf bitmap caches pinned in RAM for the lifetime of the service.
- **Backstack churn and negative eviction** : Destroyed detail screens that retain view references ratchet memory upward on repeated navigation, while uncanceled asynchronous scroll decodes completing after `onStop` cause background memory to *grow* after the user leaves the app.

### Layer 4: Hardware tier, window, and multi-process scaling

Apps that size caches once at startup using physical display metrics or a fixed
Java heap percentage over-allocate on `720p` entry-level phones, fail to adapt
when a foldable unfolds or enters split-screen mode, and duplicate caches when
tabs run in separate processes.

## Apply the 3Rs principles

Address all four architectural layers systematically using three engineering
principles: **Reduce** , **Reuse** , and **Recycle**.

### Reduce: Decode only the pixels you render

Minimize the initial byte footprint of every image before it enters memory.

#### Match container bounds on both server and client

Request exact pixel dimensions from your image CDN whenever supported, and
always supply bounded target dimensions to your client-side image loader or
decoder so it never falls back to decoding the full-resolution source.

- **Jetpack Compose** : Give image composables explicit layout bounds (such as
  `Modifier.size` or `Modifier.fillMaxWidth().aspectRatio(...)`) rather than
  unconstrained `wrapContentSize`. Load raster photos and remote URLs
  asynchronously with an image loader (`AsyncImage`) instead of calling
  `painterResource` on large raster drawables inside lazy lists, which decodes
  full-resolution bitmaps synchronously on the main thread. On large screens
  and unfolded foldables (`sw >= 600dp`), use adaptive multi-column grids so
  individual cards stay compact. For Compose-specific UI patterns, see
  [Optimizing bitmap images](https://developer.android.com/develop/ui/compose/graphics/images/optimization.md.txt).

  ```kotlin
  @Composable
  fun ProductGrid(items: List<ProductItem>, modifier: Modifier = Modifier) {
      // Adaptive columns prevent single-column full-width buffer blowouts on foldables.
      LazyVerticalGrid(
          columns = GridCells.Adaptive(minSize = 160.dp),
          contentPadding = PaddingValues(12.dp),
          modifier = modifier,
      ) {
          items(items = items, key = { it.id }) { item ->
              AsyncImage(
                  model = item.imageUrl,
                  contentDescription = item.title,
                  contentScale = ContentScale.Crop,
                  // Explicit bounds let the loader downsample before decoding.
                  modifier = Modifier
                      .fillMaxWidth()
                      .aspectRatio(1f)
                      .clip(RoundedCornerShape(12.dp)),
              )
          }
      }
  }
  ```
- **Manual decoding with `ImageDecoder`** : On Android 9 (API level 28) and
  higher, use [`ImageDecoder`](https://developer.android.com/reference/android/graphics/ImageDecoder.md.txt) with an
  [`OnHeaderDecodedListener`](https://developer.android.com/reference/android/graphics/ImageDecoder.OnHeaderDecodedListener.md.txt) to scale down large local
  files or resources during the decode pass and allocate directly into
  hardware memory when mutation isn't needed:

  ```kotlin
  val source = ImageDecoder.createSource(resources, R.drawable.hero_banner)
  val bitmap = ImageDecoder.decodeBitmap(source) { decoder, info, _ ->
      decoder.allocator = ImageDecoder.ALLOCATOR_HARDWARE
      val scale = minOf(
          targetWidthPx.toFloat() / info.size.width,
          targetHeightPx.toFloat() / info.size.height,
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
- **Tiled decoding for zoomable media** : For large zoomable images (such as
  maps, floor plans, or high-resolution product previews), use
  [`BitmapRegionDecoder`](https://developer.android.com/reference/android/graphics/BitmapRegionDecoder.md.txt) to decode only the visible
  viewport tiles instead of loading the entire full-resolution image into RAM.

#### Trim transparent margins and replace blank bitmaps

- **Crop baked-in margins** : Strip uniform transparent or white letterboxing borders in your asset build pipeline or CDN, and position elements at runtime using Compose `Modifier.padding` or View [`InsetDrawable`](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable.md.txt).
- **Eliminate solid-color bitmaps** : Never allocate `ARGB_8888` bitmaps for shimmer skeletons, dividers, or flat backdrops. Use `Modifier.background`, `ColorPainter`, or XML `<shape>` or `ColorDrawable`, which allocate zero bitmap bytes.
- **Use vectors for icons with tight viewports** : Prefer `ImageVector` or `VectorDrawable` for icons and simple illustrations. When using `AnimatedVectorDrawable`, keep `android:width` and `android:height` matched to the drawn bounds so the system doesn't allocate an oversized backing bitmap.

#### Prefer `HARDWARE` configs over blanket `RGB_565`

- **Enable `Bitmap.Config.HARDWARE` for static UI** : Coil enables hardware
  bitmaps by default on API level 26 and higher. In Glide, hardware bitmaps
  are disabled by default (`Downsampler.ALLOW_HARDWARE_CONFIG = false`); opt
  in globally in your `AppGlideModule`, and apply rounded corners using
  Compose `Modifier.clip` or View `ViewOutlineProvider` instead of CPU bitmap
  transformations that force software copies:

  ```kotlin
  @GlideModule
  class AppBitmapGlideModule : AppGlideModule() {
      override fun applyOptions(context: Context, builder: GlideBuilder) {
          builder.setDefaultRequestOptions(
              RequestOptions().set(Downsampler.ALLOW_HARDWARE_CONFIG, true)
          )
      }
  }
  ```
- **Avoid blanket `RGB_565` on photo feeds** : `RGB_565` uses 2 bytes per
  pixel, but forcing it across general photo feeds can cause color banding. It
  can also allocate temporary `4 B/px` conversion buffers during wide-gamut
  color-space transforms and lower bitmap-pool hit rates alongside `ARGB_8888`
  requests. Reserve `RGB_565` for verified opaque surfaces (such as downscaled
  `PdfRenderer` previews or `RemoteViews` thumbnails), and restrict `RGBA_F16`
  (`8 B/px`) to surfaces that render HDR content.

#### Bound parallel decodes and tight frame loops

Limit concurrent custom decode tasks (for example, with
`Dispatchers.IO.limitedParallelism(2)`) so dozens of uncompressed pixel and
scratch buffers don't peak simultaneously. In camera, OCR, or ML frame loops,
reuse pre-allocated buffers or call [`Bitmap.recycle`](https://developer.android.com/reference/android/graphics/Bitmap.md.txt#recycle()) immediately
on superseded transient frames. For examples, see [Common bitmap memory
pitfalls](https://developer.android.com/topic/performance/memory/guide/bitmaps#common-bitmap-pitfalls).

### Reuse: Consolidate pipelines and right-size caches

Prevent fragmented caches and redundant decodes across screens.

#### Standardize on a single image loader per process

Audit your merged dependencies to ensure your app runs **one** shared
`ImageLoader` or `Glide` singleton per process. During an incremental
View-to-Compose migration, use your existing loader's Compose integration (or
load into Views from Coil) rather than initializing two separate 20% heap
`LruCache` instances side by side. If two loaders must coexist temporarily,
divide your total cache budget between them.

#### Size memory caches to the active window and RAM tier

Sizing an in-memory cache as a flat 20% of a 256 MiB Java heap (`memoryClass`)
reserves \~51 MiB on a 720 × 1600 device, even though two full screens of
`ARGB_8888` pixels need only \~8.8 MiB (9.2 MB). Startup `DisplayMetrics` sizing
also fails to adapt when a foldable unfolds or enters split-screen mode.

Size your strong memory cache dynamically from the active window bounds
(`WindowMetricsCalculator`), clamped by `memoryClass` and scaled by process
visibility:

    cache_bytes = state_multiplier × min(2 × window_width × window_height × 4, 0.20 × memory_class_bytes)

- **`window_width × window_height × 4`** : Bytes for one window of `ARGB_8888` pixels (`K = 2` windows covers on-screen content plus scroll lookahead).
- **`0.20 × memory_class_bytes`** : Upper heap guardrail (using standard `ActivityManager.memoryClass`, or tightening further when [`ActivityManager.isLowRamDevice`](https://developer.android.com/reference/android/app/ActivityManager.md.txt#isLowRamDevice()) is `true`).
- **`state_multiplier`** : `1.0` while any activity in the process is started; `0.0` when all UI is stopped (or `0.25` briefly if your app frequently resumes from short external payment or share-sheet hops, dropping to `0.0` on `TRIM_MEMORY_BACKGROUND`).

```kotlin
object AdaptiveBitmapCacheBudget {
    private const val LOOKAHEAD_WINDOWS = 2.0
    private const val BYTES_PER_PIXEL = 4L
    private const val MAX_HEAP_FRACTION = 0.20

    fun computeForegroundBytes(windowBounds: Rect, activityManager: ActivityManager): Long {
        val windowBytes = windowBounds.width().toLong() * windowBounds.height() * BYTES_PER_PIXEL
        val heapBytes = activityManager.memoryClass.toLong() * 1024L * 1024L
        val heapFraction = if (activityManager.isLowRamDevice) 0.12 else MAX_HEAP_FRACTION
        return minOf(
            (LOOKAHEAD_WINDOWS * windowBytes).toLong(),
            (heapFraction * heapBytes).toLong(),
        )
    }
}
```

> [!TIP]
> **Tip:** Enlarging an in-memory `LruCache` beyond two windows rarely improves p90 image load latency on modern flash storage. Instead, align requested dimensions and URLs across feed and detail screens so cached entries match keys, and rely on the disk cache for off-screen assets.

#### Key and bound vector animation caches

Always pass an explicit cache key when loading reusable vector compositions,
remove unused or duplicate raster layers when exporting animation JSON files,
and enable hardware rendering where supported so animations don't pin
per-instance software frame bitmaps.

### Recycle: Release UI bitmaps when the UI is hidden

Proactively return UI memory to the system whenever your app has no visible
windows---including while running background or foreground services.

#### Configure libraries for `TRIM_MEMORY_UI_HIDDEN` and process stop

Image and animation libraries handle `TRIM_MEMORY_UI_HIDDEN` differently by
default:

| Library | Default behavior on `TRIM_MEMORY_UI_HIDDEN` | Recommended configuration |
|---|---|---|
| **Coil 3** | **0% evicted** : `memoryCacheMaxSizePercentWhileInBackground` defaults to `1.0` (100%). | Set `.memoryCacheMaxSizePercentWhileInBackground(0.0)` on `ImageLoader.Builder`. |
| **Coil 2** | **0% evicted** : Default trim range excludes `TRIM_MEMORY_UI_HIDDEN`, clearing only at `TRIM_MEMORY_BACKGROUND` or higher. | Call `imageLoader.memoryCache?.clear()` on `TRIM_MEMORY_UI_HIDDEN` or process `ON_STOP`. |
| **Glide 4 / 5** | **Partial** : Halves `LruResourceCache` and clears `LruBitmapPool`; full `clearMemory` waits for `TRIM_MEMORY_BACKGROUND`. | Call `Glide.get(appContext).clearMemory()` on process `ON_STOP` (and clear custom pools). |
| **Fresco** | **0% evicted** : Uses a no-op `MemoryTrimmableRegistry` unless wired by the app. | Register a `MemoryTrimmableRegistry` or call `Fresco.getImagePipeline().clearMemoryCaches()`. |
| **Lottie** | **0% evicted** : Registers no `ComponentCallbacks2` listener on static composition caches. | Call `LottieCompositionFactory.clearCache(appContext, false)` (Lottie 6.6.0+) to clear only the in-memory cache without synchronous disk-cache deletion, and release custom image-asset holders. |

#### Defeat the `ForegroundService` trap with `ProcessLifecycleOwner`

Because an active `ForegroundService` keeps your process at perceptible
priority (`IMPORTANCE_FOREGROUND_SERVICE`) and prevents the system from sending
`TRIM_MEMORY_BACKGROUND`, gating cache cleanup on `TRIM_MEMORY_BACKGROUND`
leaves UI bitmaps pinned indefinitely. Conversely, clearing caches inside a
single `Activity.onStop` wipes your cache during normal in-app
activity-to-activity navigation.

Observe [`ProcessLifecycleOwner`](https://developer.android.com/reference/androidx/lifecycle/ProcessLifecycleOwner.md.txt) (which dispatches
`ON_STOP` only when **zero** activities in your process remain started)
alongside `ComponentCallbacks2` on your `Application` class:

```kotlin
class MyApplication : Application(), SingletonImageLoader.Factory {

    override fun newImageLoader(context: PlatformContext): ImageLoader {
        val am = context.getSystemService(ActivityManager::class.java)
        // context is a non-UI Application; seed from display metrics, then
        // update from active Activities using WindowMetricsCalculator below.
        val dm = context.resources.displayMetrics
        val initialBounds = Rect(0, 0, dm.widthPixels, dm.heightPixels)
        val maxCacheBytes = AdaptiveBitmapCacheBudget.computeForegroundBytes(initialBounds, am)

        return ImageLoader.Builder(context)
            .memoryCache {
                MemoryCache.Builder()
                    .maxSizeBytes(maxCacheBytes)
                    .build()
            }
            // Evict 100% of the strong memory cache as soon as all Activities stop.
            .memoryCacheMaxSizePercentWhileInBackground(0.0)
            .build()
    }

    override fun onCreate() {
        super.onCreate()
        // Adapt cache ceiling to active split-screen, desktop, or foldable window bounds.
        registerActivityLifecycleCallbacks(
            object : ActivityLifecycleCallbacks {
                override fun onActivityResumed(activity: Activity) {
                    val bounds = WindowMetricsCalculator.getOrCreate()
                        .computeCurrentWindowMetrics(activity).bounds
                    val am = activity.getSystemService(ActivityManager::class.java)
                    SingletonImageLoader.get(activity).memoryCache?.maxSize =
                        AdaptiveBitmapCacheBudget.computeForegroundBytes(bounds, am)
                }
                override fun onActivityCreated(a: Activity, s: Bundle?) = Unit
                override fun onActivityStarted(a: Activity) = Unit
                override fun onActivityPaused(a: Activity) = Unit
                override fun onActivityStopped(a: Activity) = Unit
                override fun onActivitySaveInstanceState(a: Activity, s: Bundle) = Unit
                override fun onActivityDestroyed(a: Activity) = Unit
            }
        )
        // Process-level ON_STOP fires even when a ForegroundService keeps oom_score_adj at 200 to 249.
        ProcessLifecycleOwner.get().lifecycle.addObserver(
            object : DefaultLifecycleObserver {
                override fun onStop(owner: LifecycleOwner) {
                    SingletonImageLoader.get(this@MyApplication).memoryCache?.clear()
                    // If using Glide: Glide.get(this@MyApplication).clearMemory()
                }
            }
        )
    }
}
```

> [!CAUTION]
> **Caution:** Keep `onStop` and `onTrimMemory` handlers strictly lightweight and non-blocking. Never perform synchronous disk I/O or block on contended cache locks on the main thread during lifecycle transitions, as doing so can cause Application Not Responding (ANR) errors.

If your app runs long-lived media, sync, or connected-device foreground
services, consider isolating headless service work into a dedicated lightweight
process (`android:process=":bg"`), gating `Application.onCreate` with
[`Application.getProcessName`](https://developer.android.com/reference/android/app/Application.md.txt#getProcessName()) so the service process
never initializes UI or image-loading pools. Make sure background services don't
bind back into your UI process with priority-elevating flags:

- [Keep background work alive with a lean process](https://developer.android.com/topic/performance/memory/guide/process-splitting.md.txt)
- [Service bindings and process states](https://developer.android.com/topic/performance/memory/guide/service-bindings.md.txt)
- [Set app memory budgets](https://developer.android.com/topic/performance/memory/app-memory-budgets.md.txt)

#### Cancel in-flight requests, clean backstacks, and bound widgets

- **Prevent negative eviction** : Scope image requests to the `View`, `Fragment`, or Compose lifecycle---never `applicationContext` for UI images---so rapid scroll decodes cancel immediately when the screen stops instead of populating the cache in the background.
- **Release detail and WebView state on back navigation** : Clear custom drawable references in `onDestroyView`, avoid holding `Bitmap` or `ImageBitmap` objects in long-lived shared `ViewModel` singletons after detail flows pop, and call `WebView.destroy` when tearing down hybrid screens.
- **Respect Android 17 `RemoteViews` widget limits** : Targeting Android 17 (API level 37) and higher, [`AppWidgetManager.updateAppWidget` enforces a
  total bitmap memory ceiling](https://developer.android.com/develop/ui/views/appwidgets#remoteviews-bitmap-memory) across widget states (`1.5×` screen bytes). Downsample widget bitmaps to exact widget bounds, hoist bitmap loading outside `provideContent` in Jetpack Glance so size buckets share one instance, and avoid `partiallyUpdateAppWidget` when replacing bitmaps.

## Measure, diagnose, and prevent regressions

Verify your optimizations with tools that measure actual native and graphics
allocations across realistic user journeys.

### Avoid four common measurement traps

1. **Check `Native Allocations`, not `Graphics` alone** : In `dumpsys meminfo`,
   `Graphics` primarily reflects GPU window surfaces (`EGL mtrack`, `GL
   mtrack`, and `DMA-BUF` allocations), while standard heap bitmaps live in the
   native heap. On Android 16 (API level 36) and higher, inspect the `Native
   Allocations` section (`Bitmap (malloced)` and `Bitmap (nonmalloced)`), and
   on rooted or `userdebug` builds use `adb shell dmabuf_dump` to inspect
   `HARDWARE` buffers:

   ```bash
   adb shell dumpsys meminfo -s com.example.app
   ```
2. **Always compare against a `HOME` no-trim baseline** : Pressing `HOME` tears
   down window surfaces and substantially reduces `Graphics` memory even when
   zero `onTrimMemory` callbacks fire. Furthermore,
   `adb shell am send-trim-memory` only ratchets a process's trim level upward
   until the app relaunches. Measure true `TRIM_MEMORY_UI_HIDDEN` release
   using a clean pass: settle your user journey (`T0`), press `HOME` and
   record `HOME_NO_TRIM`, send `UI_HIDDEN`, wait 3 seconds, and compare
   `HOME_NO_TRIM` against `BG_UI_HIDDEN` (plus a 10-second follow-up check to
   catch background inflation):

   ```bash
   # 1. After driving a realistic scroll journey, move to HOME and let surfaces settle:
   adb shell input keyevent KEYCODE_HOME
   sleep 5
   adb shell dumpsys meminfo com.example.app

   # 2. Deliver TRIM_MEMORY_UI_HIDDEN to the main process, wait 3s, and re-measure:
   adb shell am send-trim-memory com.example.app UI_HIDDEN
   sleep 3
   adb shell dumpsys meminfo com.example.app

   # 3. Re-check 10s later to catch uncanceled background decode inflation:
   sleep 10
   adb shell dumpsys meminfo com.example.app
   ```
3. **Confirm pixel waste with lossless PNG heap dumps** : Grouping heap bitmaps
   solely by `(width, height, config)` frequently misclassifies distinct
   thumbnails sharing a uniform grid card size as duplicates. On Android 15
   (API level 35) and higher, capture heap dumps from a debuggable build (or
   on a `userdebug` device) with `-g -b png` so tools can inspect exact
   lossless pixel content for true duplicates, empty canvases, and trimmable
   borders:

   ```bash
   adb shell am dumpheap -g -b png com.example.app /data/local/tmp/heap.hprof
   adb shell ls -lh /data/local/tmp/heap.hprof
   adb pull /data/local/tmp/heap.hprof .
   adb shell rm /data/local/tmp/heap.hprof
   ```
4. **Drive real user journeys on physical devices** : Measuring only an initial
   landing or sign-in screen misses the peak bitmap footprint accumulated
   during catalog scrolling and detail navigation. Emulators also report
   `Graphics: 0.0` because the host handles GPU rendering. Benchmark footprints
   on physical devices across low-RAM and high-density tiers.

### Local, CI, and production tooling

- **Local heap and trace analysis** : Inspect retained `Bitmap` dominator paths and flagged duplicate bitmaps (with inline image previews) in the [Android
  Studio heap dump analyzer](https://developer.android.com/studio/profile/capture-heap-dump), or catch retained UI leaks in the IDE using LeakCanary integration. Explore heap dumps in [Perfetto Heap Dump
  Explorer](https://perfetto.dev/docs/visualization/heap-dump-explorer), track live `Bitmap Memory` and `Bitmap
  Count` counters with the `gfx` category in Perfetto (see [Hands-on bitmap
  exploration](https://developer.android.com/topic/performance/memory/guide/bitmaps#hands-on-exercise-bitmap-exploration)), or automate two-arm `onTrimMemory` and heap-dump audits with [Android Skills](https://github.com/android/skills).
- **Continuous integration** : Lock in improvements with [Jetpack
  Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) memory metrics across critical scroll and backstack journeys.
- **Production observability** : Track field regressions by process state in [Android vitals](https://developer.android.com/google/play/vitals/bitmap-memory-usage.md.txt), and capture field heap dumps before out-of-memory or memory-limiter terminations using [`ProfilingManager`
  triggers](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) (`TRIGGER_TYPE_OOM` and `TRIGGER_TYPE_ANOMALY`).

## Additional resources

- [Bitmaps and memory](https://developer.android.com/topic/performance/memory/guide/bitmaps.md.txt)
- [Optimizing bitmap images](https://developer.android.com/develop/ui/compose/graphics/images/optimization.md.txt)
- [Manage your app's memory](https://developer.android.com/topic/performance/memory/manage-app-memory.md.txt)
- [Bitmap memory usage](https://developer.android.com/google/play/vitals/bitmap-memory-usage.md.txt)
- [Actionable strategies for reducing your app's Bitmap memory
  footprint](https://developer.android.com/events/dev-summit/talks/actionable-strategies-for-reducing-your-apps-bitmap-memory-footprint)