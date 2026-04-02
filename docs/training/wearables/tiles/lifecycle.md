---
title: Lifecycle and analytics events  |  Wear OS  |  Android Developers
url: https://developer.android.com/training/wearables/tiles/lifecycle
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Wear OS](https://developer.android.com/training/wearables)

# Lifecycle and analytics events Stay organized with collections Save and categorize content based on your preferences.



`TileService` is a [bound service](/guide/components/bound-services). Your `TileService` is bound as a result
of your app request or if the system needs to communicate with it. A typical
[bound-service lifecycle](/guide/components/bound-services#Lifecycle) contains the following four callback methods:
[`onCreate()`](/reference/android/app/Service#onCreate()), [`onBind()`](/reference/android/app/Service#onBind(android.content.Intent)), [`onUnbind()`](/reference/android/app/Service#onUnbind(android.content.Intent)), and [`onDestroy()`](/reference/android/app/Service#onDestroy()).
The system invokes these methods each time the service enters a new lifecycle
phase.

However, `TileService` differs from most other bound services because it also
contains `TileService`-specific lifecycle methods. The `Service` lifecycle
methods and the `TileService` lifecycle methods are called in two separate
asynchronous threads.

There are two categories of `TileService` methods:

* **Methods relating to core Tile functionality.** [`onTileRequest()`](/reference/androidx/wear/tiles/TileService#onTileRequest(androidx.wear.tiles.RequestBuilders.TileRequest))
  (mandatory to implement) and [`onTileResourcesRequest()`](/reference/androidx/wear/tiles/TileService#onTileResourcesRequest(androidx.wear.tiles.RequestBuilders.ResourcesRequest)) are in this
  category.
* **Methods relating to analytics and visibility.** This includes methods such
  as:
  + [`onTileAddEvent()`](/reference/androidx/wear/tiles/TileService#onTileAddEvent(androidx.wear.tiles.EventBuilders.TileAddEvent)) called when when the user adds your tile to the
    carousel
  + [`onTileRemoveEvent()`](/reference/androidx/wear/tiles/TileService#onTileRemoveEvent(androidx.wear.tiles.EventBuilders.TileRemoveEvent)) called when the user removes your tile from
    the carousel
  + [`onRecentInteractionEventsAsync()`](/reference/androidx/wear/tiles/TileService#onRecentInteractionEventsAsync(java.util.List%3Candroidx.wear.tiles.EventBuilders.TileInteractionEvent%3E)) provides information about
    recent user and system interactions with tiles

See the [`TileService`](/reference/androidx/wear/tiles/TileService) documentation for more information about these
methods and events.

### Query which tiles are active

*Active tiles* are tiles which have been added for display on the watch. Use
`TileService`'s static method [`getActiveTilesAsync()`](/reference/androidx/wear/tiles/TileService#getActiveTilesAsync(android.content.Context,java.util.concurrent.Executor)) to query which tiles
*belonging to your app* are active.

**Caution:** The result reflects the list of active tiles at the time the call was
made, which might have changed by the time the result is received. Use
`onTileAddEvent()` and `onTileRemoveEvent()` callbacks for scheduling actions
that need to happen when your tile becomes either active or inactive.