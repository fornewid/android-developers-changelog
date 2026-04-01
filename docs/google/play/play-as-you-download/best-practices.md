---
title: https://developer.android.com/google/play/play-as-you-download/best-practices
url: https://developer.android.com/google/play/play-as-you-download/best-practices
source: md.txt
---

# Play as you Download best practices

These best practices can improve install latency when Play as you Download is enabled for your app.

## Use the latest SDKs

Use the latest SDKs for your app, especially if you are using the following SDKs:

- Facebook Core SDK: 11.2.0 or higher

- FB Audience Network (ads): 6.5.1 or higher

The latest SDKs are optimized for Play as you Download to operate without scanning the entire app binary. This lets users start your app more quickly the first time they launch.

## Use install-time asset packs

Use[install-time](https://developer.android.com/guide/playcore/asset-delivery#delivery-modes)asset packs to store large game assets. Google Play optimizes downloads by analyzing use patterns of install-time asset packs. This helps the game launch much faster while only downloading data that users need during the initial game launch.

The following table shows what code and resources are optimized by Play as you download when games use an[Android App Bundle with Play Assets Delivery](https://developer.android.com/guide/app-bundle/app-bundle-format).

|      Resource format      |                            Optimized by Play as you Download                            |                         Not optimized by Play as you Download                         |
|---------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Android App Bundle files  | Base Module and install-time dynamic features (except 'res/' and 'values/' directories) | \`res/\` and \`values/\` directories of base module and install-time dynamic features |
| Android App Bundle files  |                                                                                         | On-demand dynamic features                                                            |
| Play Asset Delivery files | Install-time asset packs                                                                | Fast-follow asset packs                                                               |
| Play Asset Delivery files |                                                                                         | On-demand asset packs                                                                 |

## Limit preloaded assets

Instead of preloading all app assets at once, only load what's needed for the current user experience such as the menu or level. Loading too many assets during the initial experience uses more network data up front.

Here are some additional recommendations for Unity games:

- See[Loading resources at runtime](https://docs.unity3d.com/2022.2/Documentation/Manual/LoadingResourcesatRuntime.html).

- Split large scenes into multiple scenes to avoid loading large amounts of asset data at once.

- Use an asset loading profiler (such as the[Asset Loading Profiler module in Unity](https://docs.unity3d.com/2022.2/Documentation/Manual/profiler-asset-loading-module.html)) to identify asset loading optimizations for your game.

## Fix ANRs

By fixing[ANRs](https://developer.android.com/topic/performance/vitals/anr)(Application Not Responding errors) in your app, you can also improve the Play as you Download experience of the app. For example, by removing[IO operations from the main thread](https://developer.android.com/topic/performance/vitals/anr#io_on_the_main_thread), you can minimize ANRs from occurring while Play is downloading app assets in background.