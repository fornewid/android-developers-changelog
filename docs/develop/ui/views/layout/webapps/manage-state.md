---
title: https://developer.android.com/develop/ui/views/layout/webapps/manage-state
url: https://developer.android.com/develop/ui/views/layout/webapps/manage-state
source: md.txt
---

When managing an Android app's lifecycle, preserving user state during
background resource reclamation is a core component of a seamless user
experience. For apps incorporating web workflows, `WebView.saveState(Bundle)`
lets you serialize a WebView's navigation history and state into a `Bundle`.
This data can subsequently be restored using `WebView.restoreState(Bundle)`.

However, standard implementations can run into transaction size limitations
under heavy browsing sessions. This page describes these architectural
limitations and provides strategies to prevent memory-related exceptions while
maintaining navigation history.

## The 1MB transaction limit and state wiping

Android imposes a strict 1MB limit on the total volume of data that can be
stored within `savedInstanceState`. This 1MB budget is shared across the entire
app process. If an app incorporates multiple `WebView` instances, their
collective navigation state and history must fit within this single shared
allocation. Exceeding this boundary triggers a `TransactionTooLargeException`,
resulting in an app crash.

A common but problematic mitigation strategy involves monitoring the size of the
WebView state bundle and completely clearing the WebView history if it crosses
an arbitrary safety threshold (such as 300KB). While this prevents a crash, it
introduces severe regressions into the user experience:

- **Loss of backward navigation** : Android often terminates background app
  processes to reclaim memory for other tasks. You can use `saveState(Bundle)`
  within the `onSaveInstanceState()` lifecycle callback to preserve navigation
  history. If you wipe this history to avoid the 1MB transaction limit, the
  entire navigation stack is lost. When the user returns to the app, the system
  back button immediately exits the component or app because no historical
  context remains to support backward navigation, regardless of whether a
  process restart occurred.

- **BFCache invalidation**: Clearing history prevents the app from using the
  Back-Forward Cache (BFCache), removing the ability to instantly render
  previously visited pages.

- **Increased latency**: Users lose their current state within the WebView,
  requiring full re-navigation and re-initialization. This process significantly
  increases network overhead and transaction latency.

## Architectural mitigation strategies

To prevent [`TransactionTooLargeException`](https://developer.android.com/reference/android/os/TransactionTooLargeException) crashes without degrading the
user experience through complete history deletion, you must maintain a rigorous
balance between state retention and memory efficiency. By implementing the
following optimization strategies, you can safely manage the 1MB transaction
budget while preserving essential navigation history and session integrity.

### Enforce size limits on state serialization

Instead of completely wiping the navigation stack when it grows too large, a
more effective pattern is to truncate the historical data:

- **Targeted drop policy** : Use [`WebViewCompat.saveState()`](https://developer.android.com/reference/androidx/webkit/WebViewCompat#saveState(android.webkit.WebView,android.os.Bundle,int)) to serialize
  state while enforcing a specific byte limit (for example,
  `WebViewCompat.saveState(webView, outState, maxSizeBytes)`). This API
  automatically drops older navigation entries sequentially until the total
  payload fits within your defined allocation. Crucially, this only truncates
  the serialized `Bundle` without modifying or clearing the live history of the
  active `WebView`, ensuring immediate backward navigation remains completely
  intact.

- **Forward entry removal** : If the application interface provides a back button
  but lacks a dedicated forward navigation button, you can discard all forward
  navigation entries by setting the `saveState` API's `includeForwardState`
  parameter to `false`. This significantly reduces the payload size without
  impacting the user's available navigation paths.

### Manage resource latency with the HTTP Cache Quota API

While `saveState` manages the 1MB `Bundle` limit for ephemeral navigation
history, the HTTP Cache Quota API provides manual control over persisted web
resources (disk cache) on a per-profile basis. This creates a clear distinction
between short-term navigation context and long-term cached assets.

Choosing an appropriate quota involves a performance trade-off:

- **Higher quotas** improve offline availability and resource loading latency by keeping more assets on disk.
- **Lower quotas** minimize the app's disk footprint and prevent OS-led cache eviction of other critical app data.

These settings are persisted across app restarts and must be configured from the
main thread.

The following implementation demonstrates how to configure a disk cache quota
for the default profile:

### Kotlin

    if (WebViewFeature.isFeatureSupported(WebViewFeature.MULTI_PROFILE) &&
        WebViewFeature.isFeatureSupported(WebViewFeature.HTTP_CACHE)) {
        val defaultProfile = ProfileStore.getInstance()
            .getOrCreateProfile(Profile.DEFAULT_PROFILE_NAME)
        val httpCache = defaultProfile.httpCache

        // Set explicit cache size to 50MB (50 * 1024 * 1024 bytes)
        httpCache.setQuotaBytes(50L * 1024 * 1024)
    }

### Java

    if (WebViewFeature.isFeatureSupported(WebViewFeature.MULTI_PROFILE) &&
        WebViewFeature.isFeatureSupported(WebViewFeature.HTTP_CACHE)) {
        Profile defaultProfile = ProfileStore.getInstance()
            .getOrCreateProfile(Profile.DEFAULT_PROFILE_NAME);
        HttpCache httpCache = defaultProfile.getHttpCache();

        // Set explicit cache size to 50MB (50 * 1024 * 1024 bytes)
        httpCache.setQuotaBytes(50L * 1024 * 1024);
    }

For more information about quota sizing strategies, lifecycle management, and
profile boundaries, see [Manage HTTP cache quota in WebView](https://developer.android.com/develop/ui/views/layout/webapps/cache-quota-overview).

## Key performance considerations

The following points highlight the technical limitations and internal data
behaviors that govern WebView state behavior:

- **Opaque `PageState` blobs** : Approximately 70% of the data stored by
  `saveState` consists of internal `PageState` blobs from the rendering engine.
  This data captures granular session states, including form inputs and iframe
  scroll positions. Avoid attempting to manually parse or strip individual
  segments from these blobs, as doing so poses severe security risks and breaks
  session restoration integrity.

- **Granular history management** : The standard `WebBackForwardList` API doesn't
  natively support the arbitrary removal of individual historical elements. For
  strict state management, you must implement truncation strategies using the
  `maxSizeBytes` and `includeForwardState` parameters within
  `WebViewCompat.saveState()` to ensure architectural safety.