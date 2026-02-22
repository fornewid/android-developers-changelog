---
title: https://developer.android.com/topic/performance/appstartup/best-practices
url: https://developer.android.com/topic/performance/appstartup/best-practices
source: md.txt
---

# Best practices for app optimization

The following best practices help optimize your app without sacrificing quality.

## Use Baseline Profiles

[Baseline Profiles](https://developer.android.com/topic/performance/baselineprofiles/overview)can improve code execution speed by 30% from the first launch, and can make all user interactions---such as app startup, navigating between screens, or scrolling through content---smoother from the first time they run. Increasing the speed and responsiveness of an app leads to more daily active users and a higher average return visit rate.

## Use a startup profile

A[startup profile](https://developer.android.com/topic/performance/baselineprofiles/dex-layout-optimizations#startup-profiless)is similar to a Baseline Profile, but it is run at compile time to optimize the DEX layout for faster app startup.

## Use the App Startup library

The[App Startup library](https://developer.android.com/topic/libraries/app-startup)lets you define component initializers that share a single content provider, instead of defining separate content providers for each component you need to initialize. This can significantly improve app startup time.

## Lazily load libraries or disable auto-initialization

Apps consume many libraries, some of which might be mandatory for startup. However, there can be many libraries where initialization can be delayed until after the first frame is drawn. Some libraries have an option to disable auto-initialization on startup or have an on-demand initialization. Use this option to postpone initialization until necessary to help boost performance. For example, you can use[on-demand initialization](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration)to only invoke WorkManager when the component is required.

## Use ViewStubs

A[`ViewStub`](https://developer.android.com/reference/android/view/ViewStub)is an invisible, zero-sized`View`that you can use to lazily inflate layout resources at runtime. This lets you delay inflating views that aren't necessary at startup until a later time.

If you are using Jetpack Compose, you can get similar behavior to`ViewStub`using state to defer loading some components:  

    var shouldLoad by remember {mutableStateOf(false)}

    if (shouldLoad) {
       MyComposable()
    }

Load the composeables inside the conditional block by modifying`shouldLoad`:  

    LaunchedEffect(Unit) {
       shouldLoad = true
    }

This triggers a recomposition that includes the code inside the conditional block in the first snippet.

## Optimize your splash screen

Splash screens are a major part of app startup, and using a well-designed splash screen can help improve the overall app startup experience. Android 12 (API level 31) and later includes a splash screen designed to improve performance. For more information, see[Splash screen](https://developer.android.com/about/versions/12/features/splash-screen).

## Use scalable image types

We recommend using[vector drawables](https://developer.android.com/develop/ui/views/graphics/vector-drawable-resources)for images. Where it's not possible, use[WebP images](https://developers.google.com/speed/webp/). WebP is a image format that provides superior lossless and lossy compression for images on the web. You can convert existing BMP, JPG, PNG or static GIF images to WebP format using Android Studio. For more information, see[Create WebP images](https://developer.android.com/studio/write/convert-webp).

Additionally, minimize the number and size of images loaded during startup.

## Use Performance APIs

The[performance API for media playback](https://developer.android.com/about/versions/12/features/performance-class)is available on Android 12 (API level 31) and later. You can use this API to understand device capabilities and perform operations accordingly.

## Prioritize cold startup traces

A[cold start](https://developer.android.com/topic/performance/vitals/launch-time#cold)refers to an app starting from scratch. Meaning, the system's process doesn't yet create the app's process. Your app typically starts cold if you launch it for the first time since the device booted or since the system force-stopped the app. Cold starts are much slower because the app and system must perform more work that isn't required on other startup types---like warm and hot starts. System tracing cold startups gives you better oversight into app performance.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [App startup analysis and optimization {:#app-startup-analysis-optimization}](https://developer.android.com/topic/performance/appstartup/analysis-optimization)
- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)
- [Frozen frames](https://developer.android.com/topic/performance/vitals/frozen)