---
title: Handling bitmaps  |  Views  |  Android Developers
url: https://developer.android.com/develop/ui/views/graphics
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)

# Handling bitmaps Stay organized with collections Save and categorize content based on your preferences.




Try the Compose way

Jetpack Compose is the recommended UI toolkit for Android. Learn how to display graphics in Compose.

[ImageBitmap →](https://developer.android.com/jetpack/compose/graphics/images/compare)

![](/static/images/android-compose-ui-logo.png)

There are a number of reasons why loading bitmaps in your Android app is tricky:

* Bitmaps can very easily exhaust an app's memory budget. For example, the
  camera on the [Pixel](https://www.android.com/phones/pixel/) phone takes
  photos of up to 4048x3036 pixels (12 megapixels).
  If the bitmap configuration used is `ARGB_8888`,
  the default for Android 2.3 (API level 9) and higher, loading a single
  photo into memory takes about 48MB of memory (4048\*3036\*4 bytes). Such a large
  memory demand can immediately use up all the memory available to the app.
* Loading bitmaps on the UI thread can degrade your app's performance, causing
  slow responsiveness or even ANR messages. It is therefore important to manage threading
  appropriately when working with bitmaps.
* If your app is loading multiple bitmaps into memory, you need to skillfully manage
  memory and disk caching. Otherwise, the responsiveness and fluidity of your app's UI
  may suffer.

For most cases, we recommend that you use the [Glide](https://github.com/bumptech/glide)
library to fetch, decode, and display bitmaps in your app. Glide abstracts out most of
the complexity in handling these and
other tasks related to working with bitmaps and other images on Android.
For information about using and downloading Glide, visit the
[Glide repository](https://github.com/bumptech/glide) on GitHub.

You can also opt to work directly with the lower-level APIs built into the Android framework.
For more information on doing so, refer to
[Loading Large Bitmaps Efficiently](/topic/performance/graphics/load-bitmap),
[Caching Bitmaps](/topic/performance/graphics/cache-bitmap), and
[Managing Bitmap Memory](/topic/performance/graphics/manage-memory).

## More resources