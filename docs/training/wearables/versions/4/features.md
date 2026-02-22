---
title: https://developer.android.com/training/wearables/versions/4/features
url: https://developer.android.com/training/wearables/versions/4/features
source: md.txt
---

# Explore features in Wear OS 4

Wear OS 4 introduces several features to help enhance your Wear OS app experience. Before you add these features to your app,[prepare your app](https://developer.android.com/training/wearables/versions/4/test)for compatibility with Wear OS 4.

## Watch Face Format

A watch face is the first thing that a user sees when they take a look at their watch, making it the most frequently used surface of Wear OS. Users rely on watch faces to customize their watch to suit their style and meet their needs.

Created in partnership with Samsung, the[Watch Face Format](https://developer.android.com/training/wearables/wff)is a declarative XML format to configure the appearance and behavior of watch faces. This means that there is no executable code involved in creating a watch face, and there is no code embedded in your watch face APK.

The Wear OS platform takes care of the logic needed to render the watch face so you can focus on your creative ideas, rather than code optimizations or battery performance.

Watch faces that are built using the Watch Face Format require less maintenance and fewer updates than the ones built using the Jetpack Watch Face libraries. For example, you don't need to update your watch face to benefit from improvements in performance or battery consumption, or to get the latest bug fixes.

The Watch Face Format is supported on all devices that run Wear OS 4 or higher.

## Tiles

[Tiles 1.2](https://developer.android.com/jetpack/androidx/releases/wear-tiles#version_12_2)introduces support for platform data bindings. This means that---if your tile uses platform data sources such as heart rate, step count, or time---your tile is updated once per second.

The new version of tiles also adds support for[animations](https://developer.android.com/training/wearables/tiles/animations). You can use tween animations to create smooth transitions on changes to part of your layout, and transition animations can animate new or disappearing elements from the tile.

## Splash screens

Starting in Wear OS 4, the system always[applies the default splash screen](https://developer.android.com/about/versions/12/features/splash-screen)on both cold and warm app starts. This experience works automatically for all apps running on Wear OS 4 or higher.

The default splash screen icon uses the same specifications as[adaptive icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive). For visual consistency, use an adaptive icon for your launcher icon.

If your app implements a custom splash screen or uses a launcher theme, migrate your app to use the[`SplashScreen`](https://developer.android.com/reference/kotlin/androidx/core/splashscreen/SplashScreen)library, available in Jetpack. That way, your splash screen can appear correctly on all Wear OS versions. For full instructions, see the[implementation guide](https://developer.android.com/training/wearables/apps/splash-screen).

## Transfer Wear OS data to a new mobile device

Starting in Wear OS 4, users can request that the system transfer their Wear OS data from one mobile device to another. When the system connects the user's Wear OS device to the new mobile device, any data that's stored in the wearable network is transferred to this new mobile device. The system then disconnects the Wear OS device from the old mobile device.

As long as your mobile app is already installed and[properly configured](https://developer.android.com/training/wearables/data/transfer-to-new-mobile)on the new mobile device, your mobile app receives a callback containing the Wear OS data that was associated with the old mobile device.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate your splash screen implementation to Android 12 and later](https://developer.android.com/develop/ui/views/launch/splash-screen/migrate)
- [Splash screens](https://developer.android.com/develop/ui/views/launch/splash-screen)
- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)