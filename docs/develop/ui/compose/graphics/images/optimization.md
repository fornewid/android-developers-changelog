---
title: https://developer.android.com/develop/ui/compose/graphics/images/optimization
url: https://developer.android.com/develop/ui/compose/graphics/images/optimization
source: md.txt
---

> Documentation index: https://developer.android.com/develop/ui/compose/graphics/images/llms.txt

Working with images can quickly introduce performance issues if you aren't
careful. Even a small graphic in a compressed format like JPEG or PNG inflates
into a large uncompressed bitmap in memory when decoded for display. Unbounded
decoding and retained caches drive UI jank, `OutOfMemoryError` crashes, and
low-memory kills across the device.

> [!NOTE]
> **Note:** This page focuses on Jetpack Compose image mechanics. For end-to-end guidance on bitmap memory architecture, device RAM tiers, window-adaptive cache sizing, and lifecycle eviction (including foreground services), see [Optimize
> bitmap memory](https://developer.android.com/topic/performance/memory/bitmaps).

## Use image loading libraries

Improve your app's efficiency by using an image loading library such as
[Coil](https://coil-kt.github.io/coil/compose/) (for Kotlin-first and Compose projects) or [Glide](https://bumptech.github.io/glide/int/compose.html). These libraries
handle asynchronous decoding, downsampling, and in-memory pooling automatically.

Standardize on *one* shared image loader singleton per process. During an
incremental View-to-Compose migration, use your existing loader's Compose
integration (or load into Views from Coil). Don't initialize two in-memory
caches side by side. See [Standardize on a single image
loader](https://developer.android.com/topic/performance/memory/bitmaps#single-loader).

## Downsample images

Decode only the pixels you render. Don't load a full-resolution asset into a
small container such as a feed card or thumbnail. Scale the image down before
you decode it into memory.

### Client-side downsampling

Image loading libraries such as Coil and Glide downsample automatically when
given bounded target sizes. Configure downsampling behavior using
[`ImageLoader`](https://coil-kt.github.io/coil/image_loaders/) (for Coil) or [`RequestOptions`](https://bumptech.github.io/glide/doc/options.html) (for Glide).

If you decode local bitmaps manually, prefer [`ImageDecoder`](https://developer.android.com/reference/android/graphics/ImageDecoder.md.txt)
on Android 9 (API level 28) and higher. Compute a uniform scale factor for
`setTargetSize` inside an `OnHeaderDecodedListener` so images don't stretch or
upscale, and use `ALLOCATOR_HARDWARE` for immutable UI images. On
lower API levels, use [`inJustDecodeBounds`](https://developer.android.com/reference/android/graphics/BitmapFactory.Options.md.txt#inJustDecodeBounds) and [`inSampleSize`](https://developer.android.com/reference/android/graphics/BitmapFactory.Options.md.txt#inSampleSize) with
`BitmapFactory.Options`.

### Prefer server-side resizing

Where possible, request the exact image dimensions you need directly from your
image CDN or backend server. This reduces network usage and disk cache size
while avoiding the memory overhead of decoding oversized assets on the device.

Configure your image loader to append target dimensions to image URLs
dynamically---for example, using custom interceptors in Coil or custom model
loaders in Glide.

### Avoid unconstrained layout sizes

For image loaders to downsample (client-side or server-side) effectively, they
must know the target size *before* executing the request.

- **Provide explicit Compose bounds** : Avoid `wrapContentSize` or unconstrained modifiers on composables that load remote images. When a loader can't infer target bounds, it falls back to decoding the original full-size image. Set explicit dimensions using `Modifier.size` or `Modifier.fillMaxWidth().aspectRatio(...)` so the layout engine calculates the exact pixel target upfront.
- **Use `AsyncImage` or `GlideImage` instead of `painterResource` for large
  rasters** : Load photos and large raster assets asynchronously with your image loader. Calling `painterResource` decodes a full-resolution software bitmap synchronously on the main thread without downsampling to the composable's bounds.
- **Use adaptive columns on large screens** : On tablets and unfolded foldables (`sw >= 600dp`), use multi-column layouts such as `GridCells.Adaptive(minSize = 160.dp)`. Multi-column grids keep image cards from stretching full-width and inflating GPU graphics buffers.

### Supply alternative resources for different screen sizes

If you ship raster images inside your app, supply density-specific assets.
Density-specific assets reduce download size and avoid oversized decodes on
lower-density displays. For more information, see [Provide alternative
bitmaps](https://developer.android.com/training/multiscreen/screendensities#TaskProvideAltBmp).

## Don't apply padding directly

Don't bake transparent or solid-color letterboxing margins into image files,
which wastes uncompressed `4 B/px` pixel memory on invisible borders. Trim
uniform margins in your asset pipeline or CDN and apply runtime spacing using
Compose `Modifier.padding` or View [`InsetDrawable`](https://developer.android.com/reference/android/graphics/drawable/InsetDrawable.md.txt).

## Choose the right pixel format

- **Prefer `Bitmap.Config.HARDWARE` for static UI** : Hardware bitmaps store immutable pixel buffers in graphics memory instead of on the native heap. Coil enables hardware bitmaps by default on Android 8.0 (API level 26) and higher. In Glide on Android 9 (API level 28) and higher, opt in globally with `Downsampler.ALLOW_HARDWARE_CONFIG`. Apply rounded corners with `Modifier.clip` instead of CPU bitmap transformations. Hardware bitmaps still count toward Android vitals bitmap memory usage, so pair them with downsampling and cache eviction.
- **Avoid blanket `RGB_565` on photo feeds** : `RGB_565` uses 2 bytes per pixel, but forcing it across photo feeds can cause color banding and reduce bitmap-pool reuse. Wide-gamut color transforms can also allocate temporary 4-byte conversion buffers. Reserve `RGB_565` for verified opaque thumbnails, and restrict `RGBA_F16` (`8 B/px`) to surfaces that render HDR content. See [Prefer `HARDWARE` configs over blanket
  `RGB_565`](https://developer.android.com/topic/performance/memory/bitmaps#pixel-configs).

## Use vectors and zero-byte backgrounds where possible

For icons and simple geometric illustrations, prefer `ImageVector` or
`VectorDrawable`, which scale cleanly across display densities with minimal
memory overhead. For solid backdrops, dividers, or shimmer loading skeletons,
use `Modifier.background`, `ColorPainter`, or [`ShapeDrawable`](https://developer.android.com/reference/android/graphics/drawable/ShapeDrawable.md.txt) instead of
allocating solid-color software bitmaps.

## Release and reuse bitmaps when you can

Size strong in-memory caches to the active window, capped by a heap guardrail,
rather than a fixed heap percentage alone. Release UI caches when your app has
no visible windows, including while a foreground service runs:

- **Configure `TRIM_MEMORY_UI_HIDDEN` eviction** : Popular loaders don't clear their full strong memory caches on `TRIM_MEMORY_UI_HIDDEN` by default (for example, Coil 3 defaults `memoryCacheMaxSizePercentWhileInBackground` to `1.0`). Configure explicit background eviction and observe `ProcessLifecycleOwner` `ON_STOP` so caches release even when a foreground service keeps the process perceptible. See [Release UI bitmaps when the UI
  is hidden](https://developer.android.com/topic/performance/memory/bitmaps#recycle).
- **Manual bitmap loops** : If you decode transient bitmaps manually in camera or ML loops, reuse pre-allocated buffers. Otherwise, call [`Bitmap.recycle`](https://developer.android.com/reference/android/graphics/Bitmap.md.txt#recycle()) on superseded frames and drop each reference.

## Other tips and tricks

This section lists additional Compose-specific practices for image performance.

### Don't package large images with your AAB or APK file

Bundled graphics are a frequent contributor to large app download sizes. Use the
[APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer.md.txt) to verify that you don't package oversized raster assets.
Compress them or serve appropriately sized variants from your backend.

### Find redundant bitmaps

Use the [Android Studio Memory Profiler](https://developer.android.com/studio/profile/capture-heap-dump.md.txt) to capture a heap dump and inspect
flagged duplicate bitmaps with inline previews. On Android 15 (API level 35)
and higher, capture lossless PNG heap dumps from a debuggable build
(`adb shell am dumpheap -g -b png com.example.app /data/local/tmp/heap.hprof`)
to verify exact pixel duplicates, empty canvases, and trimmable borders. See
[Measure, diagnose, and prevent regressions](https://developer.android.com/topic/performance/memory/bitmaps.md.txt#verify).

### When using `ImageBitmap`, call `prepareToDraw` before drawing

When working directly with `ImageBitmap`, call
[`ImageBitmap.prepareToDraw`](https://developer.android.com/reference/kotlin/androidx/compose/ui/graphics/ImageBitmap.md.txt#prepareToDraw()) before drawing to begin uploading the texture
to the GPU. Image loading libraries handle this automatically, so you only need
to call it for custom `ImageBitmap` pipelines.

### Prefer passing a `DrawableRes` ID or URL instead of `Painter`

Because comparing `Bitmap` contents is computationally expensive, `Painter`
isn't marked [`@Stable`](https://medium.com/androiddevelopers/jetpack-compose-stability-explained-79c10db270c8). Passing an unstable `Painter` directly
into a composable can trigger unnecessary recompositions.

Pass a stable URL string or `@DrawableRes` `Int` into your composable instead:

```kotlin
// Prefer this:
@Composable
fun MyImage(url: String) {

}
// Over this:
@Composable
fun MyImage(painter: Painter) {

}
```

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Optimize bitmap memory](https://developer.android.com/topic/performance/memory/bitmaps.md.txt)
- [ImageBitmap versus ImageVector {:#bitmap-vs-vector}](https://developer.android.com/develop/ui/compose/graphics/images/compare.md.txt)
- [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving.md.txt)
- [Jetpack Compose Phases](https://developer.android.com/develop/ui/compose/phases.md.txt)