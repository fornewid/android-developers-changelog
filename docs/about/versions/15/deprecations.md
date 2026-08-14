---
title: https://developer.android.com/about/versions/15/deprecations
url: https://developer.android.com/about/versions/15/deprecations
source: md.txt
---

With each release, specific Android APIs might become obsolete or need to be
refactored to provide a better developer experience or support new platform
capabilities. In these cases, we officially deprecate the obsolete APIs and
direct developers to alternative APIs to use instead.

Deprecation means that we've ended official support for the APIs, but they will
continue to remain available to developers. This page highlights some of the
notable deprecations in this release of Android. To see other deprecations,
refer to the [API diff report](https://developer.android.com/sdk/api_diff/35/changes).

## Use Spatializer instead of Virtualizer

First added in Android 12 (API level 32), the [`Spatializer`](https://developer.android.com/reference/android/media/Spatializer)
class lets apps query the capabilities and behavior of sound spatialization on
the device. In Android 15, the [`Virtualizer`](https://developer.android.com/reference/android/media/audiofx/Virtualizer) class is
deprecated. Use
[`AudioAttributes.Builder.setSpatializationBehavior`](https://developer.android.com/reference/android/media/AudioAttributes.Builder#setSpatializationBehavior(int)) instead
to characterize how you want your content to be played when spatialization is
supported.

AndroidX media3 ExoPlayer 1.0 enables spatial audio by default for multichannel
audio when the device supports it. See this
[recent blog post](https://android-developers.googleblog.com/2023/04/delivering-immersive-sound-experience-with-spatial-audio.html) and the
[spatial audio documentation](https://developer.android.com/media/grow/spatial-audio#exoplayer) for more information, including
APIs to control the feature.

## WebSQL deprecated in Android WebView

The [`setDatabaseEnabled`](https://developer.android.com/reference/android/webkit/WebSettings#setDatabaseEnabled(boolean)) and [`getDatabaseEnabled`](https://developer.android.com/reference/android/webkit/WebSettings#getDatabaseEnabled())
methods from `WebSettings` are now deprecated. These settings activated support
for WebSQL inside Webview. WebSQL is now removed in Chrome and is now deprecated
on Android Webview. These methods will become a no-op on all Android versions in
the next 12 months.

The World Wide Web Consortium (W3C) [encourages](https://www.w3.org/TR/webdatabase/#:%7E:text=The%20Web%20Applications%20Working%20Group%20continues%20work%20on%20two%20other%20storage%2Drelated%20specifications%3A%20Web%20Storage%20and%20Indexed%20Database%20API.)
apps needing web databases to adopt [Web Storage API](https://developer.mozilla.org/docs/Web/API/Web_Storage_API)
technologies like [localStorage](https://developer.mozilla.org/docs/Web/API/Window/localStorage)
and [sessionStorage](https://developer.mozilla.org/docs/Web/API/Window/sessionStorage), or
[IndexedDB](https://developer.mozilla.org/docs/Web/API/IndexedDB_API/Using_IndexedDB). [SQLite Wasm in the browser backed by the
Origin Private File System](https://developer.chrome.com/blog/sqlite-wasm-in-the-browser-backed-by-the-origin-private-file-system)
outlines a replacement set of technologies based on the
[SQLite](https://sqlite.org/) database,
[compiled to Web Assembly](https://sqlite.org/wasm) (Wasm), and backed by the
[origin private file system](https://developer.mozilla.org/docs/Web/API/File_System_Access_API#origin_private_file_system)
to enable more [direct migration](https://developer.chrome.com/blog/from-web-sql-to-sqlite-wasm/)
of WebSQL code.