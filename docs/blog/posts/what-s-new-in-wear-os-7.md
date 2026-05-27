---
title: https://developer.android.com/blog/posts/what-s-new-in-wear-os-7
url: https://developer.android.com/blog/posts/what-s-new-in-wear-os-7
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# What's New in Wear OS 7

###### 9-min read

![](https://developer.android.com/static/blog/assets/Developer_Blog_2_1_1440x720_6_64da0326e3_Z1M1YEl.webp) 19 May 2026 [![](https://developer.android.com/static/blog/assets/John_Zoeller_photo_15badd5d35_aN1yx.webp)](https://developer.android.com/blog/authors/john-zoeller) [##### John Zoeller](https://developer.android.com/blog/authors/john-zoeller)

###### Developer Relations Engineer, Wear OS

Today, we are excited to introduce Wear OS 7, a major update that brings a new era of power efficiency and intelligence to users and developers alike.

We recognize that watches are essential, all-day companions to your users. That's why we're continuing to invest in power optimizations so your users can do more with their favorite apps. For watches upgrading from Wear OS 6 to Wear OS 7, average users can expect up to 10% improvement in battery life.

And as part of a broader rollout to the Android ecosystem, select watches arriving later this year will come with [Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/), providing proactive and personalized help to users so they can focus on what matters.

With Wear OS 7, we're introducing new system capabilities and enhanced developer tools. New user-facing features like Live Updates, and enhanced media controls deliver a smarter, more intuitive experience on the wrist. And with enhancements to our developer toolkit such as Wear Compose 1.6 and AppFunctions, developers will be able to streamline their app experiences for the wrist.

Let's dive right in!

## Wear OS 7 Canary

You can now try out the next version of Google's smartwatch platform, [Wear OS 7 Canary Emulator](https://developer.android.com/training/wearables/versions/7/setup), based on Android 17 that's arriving later this year.

The new emulator allows you to get hands-on with the developer features and tools mentioned above while testing your app for compatibility with the upcoming platform.

Check out [what's changed](https://developer.android.com/training/wearables/versions/7/changes) and start testing your app today.

## Explore new Wear OS features

### Wear OS Widgets

![Widgets (1).png](https://developer.android.com/static/blog/assets/Widgets_1_9385fff276_Z2hx7Dz.webp)

Full-screen Tiles have been a go-to surface on Wear OS, providing users with instant, glanceable access to their essential updates. As the Android ecosystem moves toward a unified vision for widgets, we're bringing the watch closer to the rest of the Android family with the goal of minimizing efforts for developers.

Today, we're excited to introduce the next step in the evolution of Tiles: flexible and dynamic [*Wear Widgets*](https://developer.android.com/training/wearables/widgets).

Powered by [Jetpack Glance](https://developer.android.com/jetpack/androidx/releases/glance-wear) and the new [RemoteCompose](https://developer.android.com/jetpack/androidx/releases/compose-remote) framework, Wear Widgets offer greater expressiveness and consistency with Compose than the Tiles ProtoLayout libraries. Wear Widgets support two new card layouts---small and large, that align perfectly with the 2x1 and 2x2 formats on mobile, ensuring your designs feel cohesive across devices, while still allowing you to [optimize your designs for the wrist](https://developer.android.com/design/ui/wear/guides/get-started/design-for-wearables/principles#optimize-for-wrist).

It's easy to adapt the UI from the mainSlot of your full-screen tile to a 2x2 Widget. Take a look!
![widgets code (1).png](https://developer.android.com/static/blog/assets/widgets_code_1_92a293da4f_2ka43r.webp)

Check out the Widgets I/O Talk later this week for full details on the new features, and try out our Widgets Getting Started Guide to add a Widget to your Wear OS experience.

### Live Updates

![Live Updates Blog post (1).png](https://developer.android.com/static/blog/assets/Live_Updates_Blog_post_1_9cbb36aa43_CP84Y.webp)

Wear OS 7 brings [Live Updates](https://developer.android.com/develop/ui/views/notifications/live-update) to watches!

You can use Live Updates to surface real-time, important information from your watch or mobile app, providing your users with timely updates at a glance.

In your watch app, use Live Updates instead of the Ongoing Activities API to provide local update publishing on all Wear 7 devices. For supporting OEMs, Live Updates published by your phone app will also be bridged to users' watches.

Check out how Just Eat provides updates to their users, above!

For more information, check out [Notifications on Wear OS](https://developer.android.com/training/wearables/notifications).

### Connect your app to the intelligence system

We're working on several ways for developers to provide agentic experiences on the watch, from AppFunctions to task automation tools.

We'll announce these on our developer blog when they're ready, and provide an all-encompassing developer guide to help you choose the right one and craft a robust implementation. For now, here's a quick look.

#### **AppFunctions**

![Watch_IO26_Samsung_App_Functions (1).gif](https://developer.android.com/static/blog/assets/Watch_IO_26_Samsung_App_Functions_1_bfa1da8f03_TA6BG.webp)

The [AppFunctions API](http://d.android.com/ai/appfunctions) allows developers to integrate their apps with agents and assistants, like Google Gemini, enabling users to complete tasks using voice, often replacing the need for step-by-step, manual navigation with your UI.

For example, to start a run with the Samsung Health app, users are able to tell Gemini: "Start tracking my run."

We're currently running an Early Access Program for any developers who are interested. Sign up [in our form](http://goo.gle/eap-af) to express your interest.

#### **Task automation**

![Watch_IO26_RemoteBonobo_Doordash_onBG_a22_GIF (1).gif](https://developer.android.com/static/blog/assets/Watch_IO_26_Remote_Bonobo_Doordash_on_BG_a22_GIF_1_577472e37a_17Aj1y.webp)

Also coming soon, without any development effort at all, users will be able to invoke and track [automated app tasks](https://developer.android.com/ai/computer-control), for selected phone apps, directly from their watch, like placing an order with DoorDash!

Keep an eye out for these flexible options on how to prepare and connect your app to the Android intelligence system on our [developer blog](https://developer.android.com/ai).

### Wear Workout Tracker

![Watch_IO26_SystemFitnessTracker_onBG_a05 (1).gif](https://developer.android.com/static/blog/assets/Watch_IO_26_System_Fitness_Tracker_on_BG_a05_1_e25471e0b7_SoScG.webp)

We know that building a full-featured, high-quality fitness tracking experience on Wear OS from scratch is resource-intensive, so we built the all new Wear Workout Tracker experience for exercise apps. It will be included in Wear OS later in the year.

The workout tracker provides a rich standardized workout tracking experience which includes heart rate monitoring, media control, and a collection of other useful features to help you reduce development investment while guaranteeing a high-quality experience for your users.

We've been working closely with ASICS Runkeeper to bring it to their users, check it out!

### Enhanced System Media Controls in Wear OS 7

Wear OS 7 enhances the System Media Controls, giving users more control and seamless experiences for their media.

#### Per-App media auto-launch controls

![Watch_IO26_AutoLaunch_Media_onBG_a05 (1).gif](https://developer.android.com/static/blog/assets/Watch_IO_26_Auto_Launch_Media_on_BG_a05_1_03bf6ae666_2vNW1O.webp)

Users can now personalize their media auto-launch experience per-app directly from the System Media Controls on the watch.

For any app where the user has 'Auto-launch Settings' toggled on, media controls will automatically appear on the watch when media is started on the phone.

Developers with an existing implementation of [media apps that extend on the watch](https://developer.android.com/media/implement) can benefit from this feature without additional effort.

#### Seamless audio routing with the Remote Output Switcher

![Remote Output Switcher (1).png](https://developer.android.com/static/blog/assets/Remote_Output_Switcher_1_1590390663_1scbtb.webp)

Managing audio output is now easier than ever with the new Remote Output Switcher integrated into the System Media Controls.

When listening to media on a paired phone, users can effortlessly switch the device the media is played back on directly from their wrist.

## UI Library updates

To go along with all these new features for users, we're introducing some powerful enhancements to our developer toolkits to help developers prepare for the future of Wear OS!

### Compose for Wear OS 1.6

As the foundation for Wear OS development, [Compose for Wear OS 1.6](https://developer.android.com/jetpack/androidx/releases/wear-compose#wear_compose_version_16_2) has arrived.

It includes powerful updates including:

#### **Streamlined navigation with Navigation 3**

Developers can Integrate with [Navigation 3](https://developer.android.com/training/wearables/compose/navigation?version=3) to provide a more flexible and Compose-idiomatic way to handle navigation on Wear OS.

```kotlin
@Composable
fun WearApp() {
    val backStack = rememberNavBackStack(MenuScreen)

    WearAppTheme {
        AppScaffold {
            val entryProvider = remember {
                entryProvider<NavKey> {
                    entry<MenuScreen> { GreetingScreen() }
                    entry<ListNavScreen> { ListScreen() }
                }
            }

            val swipeDismissableSceneStrategy = 
                rememberSwipeDismissableSceneStrategy<NavKey>()

            NavDisplay(
                backStack = backStack,
                entryProvider = entryProvider,
                sceneStrategies = listOf(swipeDismissableSceneStrategy)
            )
        }
    }
}
```

#### **List management improvements for TransformingLazyColumn**

Significant improvements are here for advanced list management with [TransformingLazyColumn](https://developer.android.com/training/wearables/compose/lists?version=3), including enhanced padding support via the new minimumVerticalContentPadding modifier, and other new features like snapping and reverse layout.

```kotlin
val listState = rememberTransformingLazyColumnState()
val transformationSpec = rememberTransformationSpec()

/*
 * TransformingLazyColumn takes care of the horizontal and vertical
 * padding for the list and handles scrolling.
 */
ScreenScaffold(scrollState = listState) { contentPadding ->
    TransformingLazyColumn(
        state = listState,
        contentPadding = contentPadding
    ) {
        item {
            ListHeader(
                modifier = Modifier
                    .fillMaxWidth()
                    .transformedHeight(this, transformationSpec)
                    .minimumVerticalContentPadding(
                        ListHeaderDefaults.minimumTopListContentPadding
                    ),
                    transformation = SurfaceTransformation(transformationSpec)
            ) { Text(text = "Header") }
        }
    }
}
```

#### **Optimize ambient experiences with LocalAmbientModeManager**

The all new [LocalAmbientModeManager](https://developer.android.com/reference/kotlin/androidx/wear/compose/foundation/rememberAmbientModeManager.composable) is optimized for handling ambient flows, giving developers greater control over how their ambient experiences are presented to users.

```kotlin
 
override fun onCreate(savedInstanceState: Bundle?) {
    setContent {
        val ambientModeManager = rememberAmbientModeManager()
        CompositionLocalProvider(LocalAmbientModeManager provides ambientModeManager) {
            val localAmbientModeManager = LocalAmbientModeManager.current
            val ambientMode = localAmbientModeManager?.currentAmbientMode

            Column(
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally,
                modifier = Modifier.fillMaxSize(),
            ) {
                val ambientModeName =
                    when (ambientMode) {
                        is AmbientMode.Interactive -> "Interactive"
                        is AmbientMode.Ambient -> "Ambient"
                        else -> "Unknown"
                    }

                val color = if (ambientMode is AmbientMode.Ambient) Color.Gray
                    else Color.Yellow
                Text(text = "$ambientModeName Mode", color = color)
            }
        }
    }
}
```

### Protolayout \& Tiles updates

While we encourage developers to adopt the new Wear Widgets, we will continue to support our Protolayout and Tiles libraries for some time, and we've got new stable versions of both.

[Protolayout 1.4](https://developer.android.com/jetpack/androidx/releases/wear-protolayout) and [Tiles 1.6](https://developer.android.com/jetpack/androidx/releases/wear-tiles#1.6.0) work together to provide several notable new features including:

- **Inlined Image Resources:** ImageResource can now be directly inlined within a layout, and Tiles now support automatic resource collection through ProtoLayoutScope, removing the need for manual resource mapping and splitting into separate methods. In addition to better code quality, this improves Tiles loading latency via consolidation into a single binder call from system to the provider service.
- **Material3TileService**: Tiles can be implemented as a Material3TileService -- an all-encompassing suspend function which returns both tile layout and resources, while automatically managing the MaterialScope and ProtoLayoutScope to simplify the development experience.
- **Dynamic Service Switching:**On Wear 7, multiple TileService instances can now be grouped in the manifest to enable dynamic switching between different services that represent the same tile.

Check out the new Tiles sample [here](https://github.com/android/wear-os-samples/tree/main/WearTilesKotlin).

### WFF 5

Watch Face Format version 5 (WFF5) is now available with a host of new features to make it easier to build watch faces, including:

- **Enhanced Alignment Options:** Text elements like TextCircular will now have additional alignment options, including verticalAlign on the same baseline for multiple text elements.
- **Auto-Size Enhancements:** isAutoSize can now be used on TextCircular, and a new attribute, minSize, has been added to the Font element to limit the minimum size when autosizing is enabled.
- **Blend Modes:** Group and ComplicationSlot elements now support [blend mode](https://developer.android.com/training/wearables/wff/effects#blend-mode), in addition to existing support on Part\* elements.
- **Stroke Joins:** Stroke and WeightedStroke elements now include a join attribute.
- **Hierarchical settings:** User Styles can now be structured as a hierarchy, where some settings are visible only when other settings have specific values. User Styles can now enable or disable complication slots as well. These can be configured using the childSettingIds and complicationSlotIds on User Style Options.

Check out our [new developer guidance](https://developer.android.com/reference/wear-os/wff/watch-face?version=5) to learn more about WFF 5.

## Start building for Wear OS 7 now

With these updates, there's never been a better time to develop an app on Wear OS. These technical resources are a great place to learn more about how to get started:

- [Learn about designing and developing for Wear OS](https://developer.android.com/training/wearables)
- [Check out Wear OS samples on Github](https://github.com/android/wear-os-samples/tree/main)
- [Get started with the latest Wear OS](https://developer.android.com/training/wearables/versions/7/setup)[7](http://link/)[emulator](https://developer.android.com/training/wearables/versions/7/setup)

We're looking forward to seeing the experiences that you build on Wear OS!
- [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
- [#Wear OS](https://developer.android.com/blog/topics/wear-os)
- [#Compose](https://developer.android.com/blog/topics/compose)

###### Written by:

-

  ## [John Zoeller](https://developer.android.com/blog/authors/john-zoeller)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/john-zoeller) ![](https://developer.android.com/static/blog/assets/John_Zoeller_photo_15badd5d35_aN1yx.webp) ![](https://developer.android.com/static/blog/assets/John_Zoeller_photo_15badd5d35_aN1yx.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 Dec 2025 19 Dec 2025 ![](https://developer.android.com/static/blog/assets/Android_adaptives_festivity_01_blog_f70d48134f_Z2lMDgd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Goodbye Mobile Only, Hello Adaptive: Three essential updates from 2025 for building adaptive apps](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive)

  [arrow_forward](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive) In 2025 the Android ecosystem has grown far beyond the phone. Today, developers have the opportunity to reach over 500 million active devices, including foldables, tablets, XR, Chromebooks, and compatible cars.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  2 min read

  - [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#Android 16](https://developer.android.com/blog/topics/android-16)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)