---
title: https://developer.android.com/training/cars/media/create-media-browser
url: https://developer.android.com/training/cars/media/create-media-browser
source: md.txt
---

# Media browser service overview

You create a media browser service by extending the supported[`MediaBrowserServiceCompat`](https://developer.android.com/reference/androidx/media/MediaBrowserServiceCompat)or[`MediaLibraryService`](https://developer.android.com/media/media3/session/serve-content)classes. Android Auto and Android Automotive OS (AAOS) can then use your service to:

- Browse your app's content hierarchy to present a menu to the user.

- Get the token for your app's[`MediaSessionCompat`](https://developer.android.com/reference/android/support/v4/media/session/MediaSessionCompat)object to control audio playback.

You can also use your media browser service to let other clients access media content from your app. These media clients might be other apps on a user's phone, or they can be other remote clients.

## Contents

These pages detail how to work with the media browser:

- [Media browser lifecycle](https://developer.android.com/training/cars/media/create-media-browsers/workflow)
- [Build content hierarchy](https://developer.android.com/training/cars/media/create-media-browser/content-hierarchy)
- [Apply content styles](https://developer.android.com/training/cars/media/create-media-browser/content-styles)
- [Display media artwork](https://developer.android.com/training/cars/media/create-media-browser/media-artwork)
- [Display browsable search results](https://developer.android.com/training/cars/media/create-media-browser/browsable-search)
- [Implement custom browse actions](https://developer.android.com/training/cars/media/create-media-browser/custom-browse-actions)

## Design guidelines

To learn more about design guidelines, see:

- [Plan navigation tabs](https://developers.google.com/cars/design/create-apps/media-apps/navigation-tabs)
- [Plan browsing views](https://developers.google.com/cars/design/create-apps/media-apps/browsing-views)