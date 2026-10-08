---
title: https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences
url: https://developer.android.com/blog/posts/whats-new-in-android-for-cars-unifying-platforms-and-unlocking-premium-experiences
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# What's new in Android for Cars: Unifying platforms and unlocking premium experiences

3 min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp) 19 May 2026 3 Authors [Jan Kleinert,](https://developer.android.com/blog/authors/jan-kleinert) [Noam Gefen,](https://developer.android.com/blog/authors/noam-gefen) [Thomas Weathers](https://developer.android.com/blog/authors/thomas-weathers) We're thrilled to see developers continuing to bring their apps and experiences to Android for Cars! Over the past year, we've continued to see strong growth and momentum in the app ecosystem on Android Auto and cars with Google built-in. This year at Google I/O, we're introducing [updates](https://blog.google/products-and-platforms/platforms/android/android-in-cars-updates/) that benefit both drivers and developers by enabling richer, more differentiated in-car experiences. With new features and templates that allow you to build once to reach users across different infotainment screens and car platforms, it's easier than ever to build for the road.

### What's new in the Car App Library

We're bringing more flexibility, new components, and new template capabilities to the Car App Library. [Car App Library 1.8.0-beta01](https://developer.android.com/jetpack/androidx/releases/car-app#version_18_2) and Car App Library [1.9.0-alpha01](https://developer.android.com/jetpack/androidx/releases/car-app#version_19_2) are now available.

## Build templated media apps for both Android Auto and Android Automotive OS

Developers can now build customized, distraction-optimized, media browsing and playback experiences for Android Automotive OS, making it easier to build once and deliver these [templated media apps](https://developer.android.com/training/cars/apps/media) to more users and more cars.

To help you test the experiences on Android Automotive OS, we'll be launching updated system images for the [Android Automotive OS emulator](https://developer.android.com/training/cars/testing/emulator#generic-images). Beginning with revision 3, the API level 35-ext15 system images will support apps built using the Car App Library media templates.

## Unlocking developer creativity with Car App Library 1.9.0 alpha

With the [1.9.0-alpha01](https://developer.android.com/jetpack/androidx/releases/car-app#version_19_2) release of the Car App Library, we're bringing features to help you build more differentiated, expressive experiences across Android Auto and cars with Google built-in.
![MediaHero1.gif](https://developer.android.com/static/blog/assets/Media_Hero1_a40e272f55_ZnIfBd.webp)

We're increasing the modularity of existing templates to give developers more flexibility and options for laying out content. These improvements include expanded headers for better visual emphasis, such as on detail pages, spotlight sections that can be placed in scrollable areas to highlight specific content, and grid item variations to support different content types and states.
![NewComponents.png](https://developer.android.com/static/blog/assets/New_Components_9ada36cd00_Z1y7poV.webp)

We're introducing new [components](https://developer.android.com/design/ui/cars/guides/components/overview) and template capabilities to help developers build even more engaging experiences. For media apps, we're introducing an adaptive mini-player, so users can browse while still easily managing playback. Finally, we're adding more component types including [Chip](https://developer.android.com/reference/kotlin/androidx/car/app/model/Chip) and [CondensedItem](https://developer.android.com/reference/kotlin/androidx/car/app/model/CondensedItem) to increase the ways that content can be displayed and interacted with.
![HomePage.png](https://developer.android.com/static/blog/assets/Home_Page_4a3eacd161_Zy07rq.webp)

App developers, including those shown below, have already begun building upgraded media experiences using these new Car App Library features. You can join these developers and prepare to distribute your own media apps built with the Car App Library templates by applying to participate in our [early-access beta program](https://goo.gle/Media-Comms-EAP).

### Distribute your adaptive video apps to more cars with minimal effort

You've already built the apps, now we're helping you reach more users. For the first time in Android Auto, users will be able to sit back, relax, and watch videos while parked. Apps, like YouTube, will be able to deliver smooth, 60fps HD video playback. This brings the Android Auto parked experience in line with the high-fidelity, immersive experiences users already enjoy in cars with Google built-in.

This capability will start rolling out to compatible vehicles later this year, for users with phones running Android 17 and higher. If your video app is already adaptive, making it available for parked use cases in cars requires minimal effort. To express interest in making your video app available on Android Auto, fill out [this form](https://forms.gle/VsXEdDEBidxw8q8u8).

### Widgets are coming to cars

The [next generation of Android Auto](https://blog.google/products-and-platforms/platforms/android/android-in-cars-updates/) brings a more expansive user interface and the [Material 3 Expressive](https://m3.material.io/) design system you know from the phone into the car, built to seamlessly fill larger screens no matter what shape they are. With this new design, the investments you've already made in mobile widgets will be available to users of Android Auto this year, and cars with Google built-in later on, opening up new ways to reach and engage with your users while they're on the road. We're excited to unlock these new glanceable user journeys!

### The road ahead

You can look forward to even more updates coming to cars later this year.

- To deliver a more continuous user experience, we're making it possible for you to provide a templated experience while driving that can seamlessly transition to a native, adaptive app experience when the vehicle is parked.
- New components and conversational templates will be coming to the Car App Library, so you can integrate agentic and voice-based flows more seamlessly in apps.
- Improved app brand expression across all car surfaces allow experiences built with the Car App Library to feel easily recognizable by your users.
- Google Maps SDK support is coming to cars with Google built-in. With this change, you'll be able to use the Google Maps SDK to [render map-based content](https://developer.android.com/training/cars/apps/library/draw-maps) with the [MapWithContentTemplate](https://developer.android.com/reference/androidx/car/app/navigation/model/MapWithContentTemplate) in point-of-interest (POI) and Weather apps on both Android Auto and cars with Google built-in.

Stay updated on these features and start building with the latest at [goo.gle/cars-whats-new](http://goo.gle/cars-whats-new).

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
Written by:

-

  ## [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jan-kleinert) ![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp) ![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)
-

  ## [Noam Gefen](https://developer.android.com/blog/authors/noam-gefen)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/noam-gefen) ![View Noam Gefen's profile](https://developer.android.com/static/blog/assets/PXL_20250405_073558833_2_6db88dff58_46HBa.webp) ![View Noam Gefen's profile](https://developer.android.com/static/blog/assets/PXL_20250405_073558833_2_6db88dff58_46HBa.webp)
-

  ## [Thomas Weathers](https://developer.android.com/blog/authors/thomas-weathers)

  ###### Developer Relations Engineer, Android for Cars

  [read_more
  View profile](https://developer.android.com/blog/authors/thomas-weathers) ![View Thomas Weathers's profile](https://developer.android.com/static/blog/assets/DSC_0714_1_d2ffa1fb8f_Z1ktX8N.webp) ![View Thomas Weathers's profile](https://developer.android.com/static/blog/assets/DSC_0714_1_d2ffa1fb8f_Z1ktX8N.webp)
Continue reading
- [![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)](https://developer.android.com/blog/authors/jan-kleinert) 21 Sep 2026 21 Sep 2026 ![](https://developer.android.com/static/blog/assets/Games_for_car_Strapi_1_c55588726e_Z2cIhWx.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring your Android game to the car screen today](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today)

  [arrow_forward](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today) Today, the games category for Android Auto and cars powered by Android Automotive OS with Google built-in is officially graduating from beta to general availability.
  [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert) • 3 min read
  - [#Android Automotive OS](https://developer.android.com/blog/topics/android-automotive-os)
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_21k6io.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android UI Development is Compose First](https://developer.android.com/blog/posts/android-ui-development-is-compose-first)

  [arrow_forward](https://developer.android.com/blog/posts/android-ui-development-is-compose-first) In the almost-5-years since Jetpack Compose launched, we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices.
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 2 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated)
- [![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)](https://developer.android.com/blog/authors/simona-milanovic) 02 Oct 2026 02 Oct 2026 ![](https://developer.android.com/static/blog/assets/ABL_135_Android_CLI_and_Android_skills_Strapi_d22702426a_ZIUXgH.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Device Streaming and Android skills - available in Android CLI](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills) As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build.
  [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) • 4 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)