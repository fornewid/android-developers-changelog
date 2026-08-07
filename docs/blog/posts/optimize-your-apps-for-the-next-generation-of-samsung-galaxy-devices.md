---
title: https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices
url: https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Optimize your apps for the next generation of Samsung Galaxy devices

3 min read ![](https://developer.android.com/static/blog/assets/MM_Adaptive_and_device_Meta_18e67bafd8_Z1BKgnT.webp) 22 Jul 2026 [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) \& [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) Today at Galaxy Unpacked, Samsung [unveiled](https://blog.google/products-and-platforms/platforms/android/galaxy-unpacked-2026) its latest lineup of foldable and wearable devices. For developers, this means that the variety of form factors, screen sizes, and device postures your app needs to support is expanding once again.

With devices like the Galaxy Z Fold8, the ecosystem is expanding to include hardware with a landscape-first natural orientation and a wider aspect ratio in its main display state. Whether a user is unfolding a large display, flipping open a cover screen, or glancing at their wrist, users expect a flawless experience. To help you meet this moment, we're sharing actionable guidance and new tooling updates to enable you to build adaptively proactively.

<br />

[Video](https://www.youtube.com/watch?v=pLNJ-fNYTKU)

<br />

## Rethink layout architecture for dynamic displays, including ultra-wide foldables

Building for the latest foldables means dropping assumptions about display orientation and size. This is especially true for the Galaxy Z Fold8, which adopts an ultra-wide display, adding to the variety of aspect ratios to account for. Devices with this landscape-first natural orientation show the limitations of hardcoded layout rules when users unfold the device. That's why we've introduced [dedicated guidance for building for landscape foldables and trifolds.](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables)

To build a responsive UI that handles these physics seamlessly, focus on the following core pillars:

- **Build fluid, adaptive layouts:** Wide aspect ratios and compact vertical heights require fluid UIs that scale responsively. Our updated [adaptive design guidance](https://developer.android.com/design/ui/mobile/guides/layout-and-content/adapt-layout) advises considering the window class width first to determine layout changes, then adjusting for height. To let individual components fluidly adapt to the grid, structure your layout using flexible containers that allow your content to automatically wrap, span, and reflow. For design inspiration browse our [adaptive sample app](https://developer.android.com/design/ui/gallery/social/pawparazzi) and [dual-screen](https://developer.android.com/design/ui/gallery/social/dual-screen) design galleries.
- **Track actual app space:** Your app's display space rarely matches the physical device size, especially on an ultra-wide screen during multi-window, split-screen, or multitasking states. Sometimes even the orientations differ. Leverage [Window Size Classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes) using the [Jetpack Window Manager library](https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable) to calculate the exact space your app occupies.

<br />

[Video](https://www.youtube.com/watch?v=thfNTC9x_Ys)

<br />

- **Leverage the latest Jetpack Compose Update:** Start by adopting the stable [Jetpack Compose April '26 release](https://android-developers.googleblog.com/2026/04/jetpack-compose-april-2026-updates.html) ([Compose BOM](https://developer.android.com/develop/ui/compose/bom) version `2026.04.01`).Take advantage of the new structural layout tools to manage complex architectures. The new [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) API allows you to define dynamic tracks and column spans without the performance overhead of a lazy list. Pair Grid with the new [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox) layout API to easily handle multi-axis alignment and dynamic item wrapping. You can also use the new [MediaQuery](https://developer.android.com/develop/ui/compose/layouts/adaptive/mediaquery) API to adapt your UI to its environment, using conditions to detect signals like device posture, window size, and keyboard types.
- **Make your app fold aware:** Use the Jetpack WindowManager library, which provides an API surface for foldable device window features such as folds and hinges. When your app is[fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware), it can adapt its layout to avoid placing important content in the area of folds or hinges and use folds and hinges as natural separators.
- **Maintain app continuity:** Avoid breaking the user journey when the device configuration shifts. Retain your UI state using [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) to ensure smooth transitions when a user folds or unfolds their device.

## Ensure seamless camera capture on foldable devices

Camera implementation on foldables brings unique hardware quirks. Moving from a compact outer display to an expanded inner display introduces distinct layout aspect ratios while device rotation remains unchanged. If an app assumes a fixed portrait relationship between the camera sensor and the device layout, the app will likely suffer from sideways, stretched, or cropped previews during these folding transitions.

When optimizing your app's media pipeline, migrate your capture experiences to [CameraX](https://developer.android.com/media/camera/camerax) using the CameraX migration [skill](https://github.com/android/skills/blob/main/camera/camerax/SKILL.md). The library's [PreviewView](https://developer.android.com/reference/kotlin/androidx/camera/view/PreviewView) automatically handles sensor orientation, device rotation, and scaling behind the scenes. This guarantees a clean, stable preview regardless of how the user holds or positions the device. If you are maintaining an existing Camera2 codebase, integrate the [CameraViewfinder](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables#solution_2_cameraviewfinder) library to apply these complex aspect ratio and rotation transformations automatically without needing a total architecture overhaul.

## Extend glanceable interactions to Wear OS 7

The opportunity to build for this new generation of devices extends right to the wrist. Launching with Wear OS 7, Wear Widgets give you a fresh surface to provide users with instant, glanceable access to their essential updates. You can build these highly expressive experiences using [Jetpack Glance](https://developer.android.com/jetpack/androidx/releases/glance-wear) and [RemoteCompose](https://developer.android.com/jetpack/androidx/releases/compose-remote). Crucially, Widgets built with this framework can now populate multi-widget tiles that were previously reserved for first-party widgets.

<br />

[Video](https://www.youtube.com/watch?v=VnjgKzAa0ws)

<br />

## Build intelligent features

[Gemini intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)already completes tasks on users' behalf, and you can [experiment](https://developer.android.com/ai/appfunctions?_gl=1*1jms098*_up*MQ..*_ga*MjY0OTY0MDI3LjE3ODQzMzI1NDk.*_ga_6HH9YJMN9M*czE3ODQzMzI1NDkkbzEkZzAkdDE3ODQzMzI1NDkkajYwJGwwJGgxNjE0MTMzNjEz) with the intelligence system by sharing your apps capabilities.

Samsung's new foldable devices come with Gemini Nano 4, our latest on-device model. Nano 4 provides support for over 140 languages, better multimodal understanding, and [much more](https://developers.google.com/ml-kit/release-notes#july_14_2026). Use [ML Kit's Prompt API](https://developers.google.com/ml-kit/genai/prompt/android) with advanced features like s[tructured output](https://developers.google.com/ml-kit/genai/prompt/android/structured-output) and [thinking mode](https://developers.google.com/ml-kit/genai/prompt/android/thinking-mode) to build intelligent features on-device.

## Start optimizing today

The tools and frameworks are ready to help you optimize your app for all screen sizes. Begin by exploring our guidance for [building adaptive apps](https://developer.android.com/develop/adaptive-apps)to learn more about core adaptive design principles.

To dive deeper, check out our comprehensive [YouTube playlist](https://www.youtube.com/playlist?list=PLD2U7gd1-ieo). Finally, ensure your app delivers a flawless, premium experience on the newest form factors by reviewing our dedicated quality guidelines for [trifolds and landscape foldables](https://developer.android.com/develop/adaptive-apps/guides/foldables/trifolds-and-landscape-foldables) and [WearOS](https://developer.android.com/design/ui/wear/guides/get-started).

Unfold the future today!

<br />


Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)
-

  ## [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

  ###### Developer Relations Engineer

  [read_more View profile](https://developer.android.com/blog/authors/miguel-montemayor) ![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp) ![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 03 Sep 2025 03 Sep 2025 ![](https://developer.android.com/static/blog/assets/yt_MBG_2_a56f169e60_ZSoFHF.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Unfold new possibilities with Compose Adaptive Layouts 1.2 beta](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts)

  [arrow_forward](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts) With new form factors like the Pixel 10 Pro Fold joining the Android ecosystem, adaptive app development is essential for creating high-quality user experiences across phones, tablets, and foldables.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) • 3 min read
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩
- [![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 13 Feb 2026 13 Feb 2026 ![](https://developer.android.com/static/blog/assets/a17beta_bfff40b895_20Bzrw.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Prepare your app for the resizability and orientation changes in Android 17](https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17) With the release of Android 16 in 2025, we shared our vision for a device ecosystem where apps adapt seamlessly to any screen---whether it's a phone, foldable, tablet, desktop, car display, or XR. Users expect their apps to work everywhere.
  [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) • 6 min read
Stay in the loop

Get the latest Android development insights delivered to your inbox weekly.
[mail Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)