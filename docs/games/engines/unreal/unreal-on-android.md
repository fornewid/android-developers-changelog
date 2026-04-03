---
title: https://developer.android.com/games/engines/unreal/unreal-on-android
url: https://developer.android.com/games/engines/unreal/unreal-on-android
source: md.txt
---

The Unreal Engine developer documentation contains most of what you'll need to
use Unreal Engine to target Android devices.

## Getting started

The [Android Quick Start](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Android/GettingStarted/)
guide covers most of what you'll need to begin Android development, including:

- Creating a mobile project
- Configuring the project to target Android
- Setting up the editor for mobile renderer previews
- Launching on an Android target device
- Packaging your Android build into an APK for testing

If you're using Windows as your development platform, Unreal integrates with the
[Android Game Development Extension](https://developer.android.com/games/agde) for Visual Studio.

## Packaging your project

The [Packaging Android Projects](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Android/PackagingAndroidProject/)
guide not only covers packaging your Android build into an APK file, it also
covers getting your build ready for distribution using [Android App Bundle](https://developer.android.com/platform/technology/app-bundle).

## Play Asset Delivery

The [Google Play Asset Delivery](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Android/Distribution/GooglePlayAssetDeliveryReference/)
reference covers how to enable [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) in your project, how to
designate rules to create asset chunks that will become asset packs in the
Android App Bundle, and how to take advantage of install-time, fast-follow, and
on-demand assets.

## Play Integrity API

Play Integrity API helps you check that your game is unmodified, installed by
Google Play, and running on either a genuine Android-powered device or a genuine
instance of Google Play Games for PC. Your game's backend server can respond
when you detect risky traffic to prevent unauthorized access and cheating. Refer
to the [documentation](https://developer.android.com/google/play/integrity/setup#unreal-engine) and [Runtime API reference](https://developer.android.com/reference/unreal-engine/play/core/group/play-integrity) on how to integrate
this feature with the Unreal Engine plugin.

## Play In-app Updates

Play In-app Updates lets you prompt users to update to the latest version of
your game, when a new version is available, without the user needing to visit
the Play Store. Refer to the [documentation](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine) and [Runtime API reference](https://developer.android.com/reference/unreal-engine/play/core/group/play-in-app-updates)
on how to integrate this feature with the Unreal Engine plugin.

## Play In-app Reviews

Play In-app Reviews lets you prompt users to submit Play Store ratings and
reviews without leaving your game. Refer to the [documentation](https://developer.android.com/guide/playcore/in-app-review/unreal-engine) and [Runtime
API reference](https://developer.android.com/reference/unreal-engine/play/core/group/play-in-app-reviews) on how to integrate this feature with the Unreal Engine
plugin.

## Google Play Billing

The [In-app Purchases](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Android/InAppPurchases/)
guide covers how to configure your game for [Google Play's billing system](https://developer.android.com/google/play/billing),
how to read purchase information, and how to make purchases.

## Vulkan API

[Vulkan](https://developer.android.com/games/develop/use-vulkan) is a cross-platform, high-performance 3D graphics API that has low
overhead compared with OpenGL ES.

To enable the Vulkan graphics API, navigate to
**Project Settings \> Platforms \> Android \> Build** and select
**Support Vulkan** . When you select both **Support Vulkan** and
**Support OpenGL ES3.2**, Unreal uses Vulkan by default. If the device doesn't
support Vulkan, Unreal falls back to OpenGL ES 3.2.
![Support Vulkan and Support OpenGL ES3.2 selected in Project Settings > Platforms > Android > Build](https://developer.android.com/static/images/games/engines/unreal/unreal-vulkan.png) **Figure 1.** Enable Vulkan by default and OpenGL ES 3.2 as a fallback.

## Frame pacing

Unreal 4.25 and higher integrates the [Android Frame Pacing Library](https://developer.android.com/games/sdk/frame-pacing), which
is part of the [Android Game Development Kit](https://developer.android.com/games/agdk). The [Mobile Frame
Pacing](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Rendering/MobileFramePacing/)
article explains how to enable the Android Frame Pacing Library, and how to
control frame pacing from C++ code.

## Rendering optimization

The [Rendering Optimization for Mobile](https://docs.unrealengine.com/SharingAndReleasing/Mobile/Performance/TipsAndTricks/)
guide covers guidelines and best practices for optimizing mobile performance,
including when to use normal maps versus high-vertex meshes. It covers the
basics for reducing draw calls, mesh count and material ID count, as well as
material complexity, optimizing texture resolution, boot time, and package size.

## Best practices

We also have best practice articles around [art assets](https://developer.android.com/games/optimize/geometry), [identity](https://developer.android.com/games/distribute/pgs),
[distribution](https://play.google.com/console/about/), and more that will help you as you navigate the
Android ecosystem with Unreal Engine.

## 16 KB page support

A page is the granularity at which an operating system manages [memory](https://android-developers.googleblog.com/2024/08/adding-16-kb-page-size-to-android.html).
To improve the operating system performance overall and to give device
manufacturers an option to make this trade-off, Android 15 (API level 35)
and higher can run with 4 KB or 16 KB page sizes. Devices configured
with 16 KB page sizes use slightly more memory on average but also gain
various performance improvements.

[Unreal 5.6](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-6-release-notes#android-2) and higher support 16 KB page sizes.