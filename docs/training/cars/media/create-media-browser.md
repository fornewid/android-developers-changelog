---
title: Media browser service overview  |  Android for Cars  |  Android Developers
url: https://developer.android.com/training/cars/media/create-media-browser
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android for Cars](https://developer.android.com/training/cars)

# Media browser service overview Stay organized with collections Save and categorize content based on your preferences.



You create a media browser service by extending the supported
[`MediaBrowserServiceCompat`](/reference/androidx/media/MediaBrowserServiceCompat) or [`MediaLibraryService`](/media/media3/session/serve-content) classes. Android
Auto and Android Automotive OS (AAOS) can then use your service to:

* Browse your app's content hierarchy to present a menu to the user.
* Get the token for your app's [`MediaSessionCompat`](/reference/android/support/v4/media/session/MediaSessionCompat) object to control
  audio playback.

You can also use your media browser service to let other clients access media
content from your app. These media clients might be other apps on a user's
phone, or they can be other remote clients.

## Contents

These pages detail how to work with the media browser:

* [Media browser lifecycle](/training/cars/media/create-media-browsers/workflow)
* [Build content hierarchy](/training/cars/media/create-media-browser/content-hierarchy)
* [Apply content styles](/training/cars/media/create-media-browser/content-styles)
* [Display media artwork](/training/cars/media/create-media-browser/media-artwork)
* [Display browsable search results](/training/cars/media/create-media-browser/browsable-search)
* [Implement custom browse actions](/training/cars/media/create-media-browser/custom-browse-actions)

## Design guidelines

To learn more about design guidelines, see:

* [Plan navigation tabs](https://developers.google.com/cars/design/create-apps/media-apps/navigation-tabs)
* [Plan browsing views](https://developers.google.com/cars/design/create-apps/media-apps/browsing-views)

[Next

Media browser lifecycle

arrow\_forward](/training/cars/media/create-media-browser/lifecycle)