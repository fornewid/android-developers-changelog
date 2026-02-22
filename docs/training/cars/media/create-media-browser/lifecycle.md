---
title: https://developer.android.com/training/cars/media/create-media-browser/lifecycle
url: https://developer.android.com/training/cars/media/create-media-browser/lifecycle
source: md.txt
---

# Media browser service lifecycle

This section describes how Android Automotive OS (AAOS) and Android Auto interact with your media browser service during a typical user workflow:

1. The user launches your app on AAOS or Android Auto.

2. The host app binds to your media browser service, which the OS starts if it isn't already running. In your implementation of the`onCreate()`method, you must create and register a[`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat)object and its callback object. To learn more, see[Register a media session](https://developer.android.com/training/cars/media/enable-playback#registering_mediasession).

3. AAOS or Android Auto calls your service's[`onGetRoot`](https://developer.android.com/training/cars/media/content-hierarchy#onGetRoot)method to retrieve the root in your content hierarchy. The root is not displayed. Instead, it retrieves more content from your app in subsequent steps.

4. AAOS or Android Auto calls your service's[`onLoadChildren()`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onLoadChildren(java.lang.String,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E)%5D)method to retrieve the descendants of the root media item. AAOS and Android Auto display these media items as the top level of content items. See[Structure the root menu](https://developer.android.com/training/cars/media/content-media-browser/content-hierarchy#root-menu-structure)to learn more about what the system expects.

5. When the user selects a**browsable** media item, your service's`onLoadChildren()`method is called again.

6. If the user selects a**playable**media item, AAOS or Android Auto calls the appropriate media session callback method to perform the action.

7. If supported by your app, the user can also search your content. In this case, AAOS or Android Auto call your service's[`onSearch()`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat#onSearch(java.lang.String,android.os.Bundle,androidx.media.MediaBrowserServiceCompat.Result%3Cjava.util.List%3Candroid.support.v4.media.MediaBrowserCompat.MediaItem%3E%3E))method. To learn more, see[Display browsable search results](https://developer.android.com/training/cars/media/create-media-browser/browsable-search).