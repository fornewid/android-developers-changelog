---
title: https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices
url: https://developer.android.com/blog/posts/optimize-your-apps-for-the-next-generation-of-samsung-galaxy-devices
source: md.txt
---

# Optimize your apps for the next generation of Samsung Galaxy devices

3-min read ![](https://developer.android.com/static/blog/assets/MM_Adaptive_and_device_Meta_18e67bafd8_Z1BKgnT.webp) 23 Jul 2026 [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) \& [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) Today at Galaxy Unpacked, Samsung [unveiled](https://blog.google/products-and-platforms/platforms/android/galaxy-unpacked-2026) its latest lineup of foldable and wearable devices. For developers, this means that the variety of form factors, screen sizes, and device postures your app needs to support is expanding once again.

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

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)
-

  ## [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/miguel-montemayor) ![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp) ![View Miguel Montemayor's profile](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)
Continue reading
- [![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp)](https://developer.android.com/blog/authors/tibian-elsheikh)[![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp)](https://developer.android.com/blog/authors/jeffrey-jose) 29 Jun 2026 29 Jun 2026 ![](https://developer.android.com/static/blog/assets/Eclipsa_Video_V01_White_Strapi_10c5296e18_R3bTD.webp)

  ## [Eclipsa Video: HDR That Looks Right on Every Screen](https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen)

  [arrow_forward](https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen) We've all been there: You're scrolling through your favorite social media feed in a dim room, and suddenly an HDR video pops up. It's so intensely bright that you have to squint, or maybe you find yourself turning down your screen brightness just to read the caption.
  [Tibian Elsheikh](https://developer.android.com/blog/authors/tibian-elsheikh), [Jeffrey Jose](https://developer.android.com/blog/authors/jeffrey-jose) • 2 min read
- 3 Authors 22 Jun 2026 22 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_5c55395a9c_UkzvN.webp)

  ## [Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini)

  [arrow_forward](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini) At this year's Google I/O, we announced an update for spatial experiences: the Geospatial API is now available as a preview in ARCore for Jetpack XR.
  [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus), [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni), [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1) • 7 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 16 Jun 2026 16 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_Hero_White_e4dbee04d8_Z1qQbv3.webp)

  ## [Android 17 is Here](https://developer.android.com/blog/posts/android-17-is-here)

  [arrow_forward](https://developer.android.com/blog/posts/android-17-is-here) Today we're releasing Android 17 and making it available on most supported Pixel devices. Look for new devices running Android 17 in the coming months.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 13 min read
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)