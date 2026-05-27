---
title: https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot
url: https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android XR Updates for Unity, Unreal, and Godot

###### 4-min read

![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp) 19 May 2026 [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley)

##### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins)
\&
[Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley)

Today, we are excited to announce that official support for [**Unreal Engine**](https://www.unrealengine.com/) and [**Godot**](https://godotengine.org/) has arrived for Android XR. Alongside these engine expansions, we are also launching new tools designed to boost your productivity and enable new XR capabilities: the **Android XR Engine Hub** and the**Android XR Interaction Framework**.

## Android XR Engine Hub

The [**Android XR Engine Hub**](https://developer.android.com/develop/xr/engine-hub) is currently available for Windows and is your mission control for development. It unifies your workflow across Unity, Unreal Engine, and Godot by serving as a high-speed bridge thatstreams device-created perception data straight from your device into the engine of your choice.
![DirectPreview_Low.gif](https://developer.android.com/static/blog/assets/Direct_Preview_Low_5bb20ac62c_Zf6Hp9.webp)

### **Real-Time Streaming via OpenXR**

The Hub bridges the gap between desktop power and mobile sensor data. Instead of requiring a full build to see how your app reacts to the world, the Hub**streams OpenXR extensions** from the physical Android XR device directly to your Windows machine.

This means you can iterate on complex interactions in "Play Mode" while receiving live, high-fidelity data from the headset's sensors. Without this streaming capability, testing even a minor change to eye-tracking or spatial mapping would require a full APK export and installation.

The Hub enables low-latency testing for the following streamed extensions:

**Core \& Interaction Support**

- **XR_EXT_hand_tracking \& hand_interaction:** Streams 26-point hand meshes and joint data for immediate interaction testing.
- **XR_EXT_eye_gaze_interaction:** Virtualizes eye-gaze data to test UI and foveated logic on your PC.
- **XR_EXT_palm_pose \& XR_EXT_uuid:** Real-time precision tracking and persistent object ID streaming.

**Android XR Vendor Extensions**

- **Eye \& Face Tracking (** `XR_ANDROID`**):** Stream expressive avatar data to your editor to refine social presence without building.
- **Passthrough \& Trackables:** Access live environmental understanding---like plane detection and hit testing---directly within the engine's viewport.

By virtualizing the device's hardware capabilities and streaming them over a low-latency desktop bridge, the Android XR Engine Hub allows for game engine developers to quickly iterate.

**Download the Hub:**

- [Learn more about Direct Preview](https://developer.android.com/develop/xr/engine-hub)

## Expanding Game Engine Support

Through our commitments to OpenXR standards, we are ensuring that whether you are a veteran studio or an indie developer, you have best-in-class tools to help bring your creative vision to life.

### Unreal Engine

Unreal Engine support is now available in developer preview, targeting [**version 5.6.1**](https://www.unrealengine.com/download). This integration is built directly on using OpenXR with the support for AndroidXR vendor specific API using the [**Android XR vendor plugin for Unreal**,](https://github.com/android-xr/android-xr-unreal-vendor-plugin) you can access platform-specific extensions for advanced hand tracking, face tracking, and scene understanding (like plane detection and depth) whilst making use of Unreal blueprints or C++ support.
![ue5_1-02-ue-project-creation.png](https://developer.android.com/static/blog/assets/ue5_1_02_ue_project_creation_05b09f41b6_ZeLC3Q.webp)

**Get Started with Unreal:**

- [Download the Android XR Extension Plugin for Unreal](https://github.com/android-xr/android-xr-unreal-vendor-plugin)
- [Official Unreal Engine Website](https://www.unrealengine.com/)
- [View the Unreal Engine Developer Guide](https://developer.android.com/develop/xr/unreal)

### Godot

In partnership with the [Godot Foundation](https://godot.foundation/) and[W4 Games](https://www.w4games.com/), we are bringing official Godot support to Android XR for **Godot 4.6.2 and higher**.

We are already seeing incredible momentum from W4 as they have ported experiences like[MoAT](https://play.google.com/store/apps/details?id=as.may.moat) and[Expedition to Blobotopia](https://play.google.com/store/apps/details?id=com.snopekgames.gwj81) that are already live on Google Play, proving that Godot is ready for production-grade spatial experiences today.

To unlock the full potential of the platform, use the [**Godot OpenXR Vendors plugin 5.1**](https://github.com/GodotVR/godot_openxr_vendors/tree/master/plugin), which provides the necessary Android XR vendor extensions for features like [scene meshing](https://github.com/GodotVR/godot_openxr_vendors/tree/c8f4c9fd38c10cec1b3dddc76229587fb2ed21c4/samples/androidxr-scenemeshing-sample), [dynamic resolutio](https://github.com/GodotVR/godot_openxr_vendors/blob/c8f4c9fd38c10cec1b3dddc76229587fb2ed21c4/samples/androidxr-dynamic-resolution-sample/main.gd#L22)n, [light estimation](https://github.com/GodotVR/godot_openxr_vendors/blob/c8f4c9fd38c10cec1b3dddc76229587fb2ed21c4/samples/androidxr-light-estimation-sample/main.gd#L56) and much more. We're collaborating with Godot to optimize the OpenXR implementation for the Android XR power profile and input standards.

**Get Started with Godot:**

- [Download the Godot OpenXR Vendors Plugin](https://github.com/GodotVR/godot_openxr_vendors)
- [Official Godot Engine Website](https://godotengine.org/)
- [View the Godot Developer Guide](https://developer.android.com/develop/xr/godot)

### Unity

The **Unity OpenXR: Android XR 1.13 package** is now available for **Unity 6.5 Beta** . Unity has expanded **Application SpaceWarp** support to include both **uGUI and TextMeshPro**. Keep an eye out for the general release of Unity 6.5 and more platform enhancements arriving this summer.

#### Android XR Extensions v1.3.1 for Unity

Everything else you need for comprehensive platform integration is available in our latest[Android XR Extensions release](https://github.com/android/android-xr-unity-package/releases/tag/v1.3.0):

- **Spatial API Support:** You can now manage the `android.software.xr.api.SPATIAL` manifest tag directly through XRSessionFeature settings, making it easier than ever to define your app's Spatial API requirements and target levels.
- **Fine Eye Face Tracking:** A new Fine Eye Poses feature provides high-precision eye poses using the `TryGetFineEyePoses` extension method.
- **Direct Preview Support:** The **Android XR Streaming** feature enables Direct Preview support within Unity Editor's PlayMode (Windows only).

**Note:** `Android XR (Extensions)`: `Hand Mesh` has been removed; you should now use the unified **Hand Mesh Data** within the [extensions package](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@1.2/manual/features/hand-mesh-data.html).

#### Android XR Interaction Framework for Unity

The Android XR Interaction Framework (AXRIF) is now available in developer preview. AXRIF is an unstyled, opinionated input toolkit that abstracts the complex logic required to build interfaces that are consistent with Android XR system interactions.

Instead of focusing on UI visuals, AXRIF prioritizes the underlying mechanics of the Android XR user experience. At its core is the same Transition Manager that powers the system's rich multimodal inputs, enabling state switching between 6DoF controllers, 3D mouse, hand tracking, and eye gaze. By leveraging this framework, developers can significantly reduce the implementation burden required to bring Android XR's full complement of robust interactions to their apps.

At launch, the framework provides three core capabilities:

- **Automated Multimodal Input Transitions**: The framework manages the state machine for switching between input modalities. For example, it handles the transition logic when a user moves from gaze-targeting an object to directly touching it, simplifying simultaneous support for hands, controllers, and mice.
- **Gaze-Assisted Gesture Interaction**: AXRIF combines gaze vector targeting with hand gesture recognition (such as pinch-to-select) for precise distant interaction, matching the system's default behavior.
- **Physics-Based 2D UI Interaction**: The framework maps high-fidelity hand tracking to 2D plane interactions, enabling intuitive poke and swipe gestures on floating panels while respecting physical boundary constraints.

By adopting AXRIF, your app inherits the platform's native interaction model, ensuring your app feels consistent with the rest of the OS.

**Explore the Toolkit:**

- [Interaction Framework Documentation](https://developer.android.com/develop/xr/axrif)
- [Download the Unity Package](http://github.com/android-xr/android-xr-interaction-framework-unity-package)

## **Get Started Today:**

There has never been a better time to dive into Android XR development. With support across **Unity, Unreal, and Godot**, the platform is ready for your creative vision, no matter which engine you call home. Explore our official engine partners to get started:

- [Unity Developer Portal](https://unity.com/)
- [Unreal Engine Developer Community](https://www.unrealengine.com/)
- [Official Godot Engine Website](https://godotengine.org/)

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Android XR](https://developer.android.com/blog/topics/android-xr)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)

###### Written by:

-

  ## [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/luke-hopkins) ![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp) ![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)
-

  ## [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/ryan-bartley) ![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp) ![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z1LAQnM.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld)[![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 4](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4)

  [arrow_forward](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4) We're excited to launch Developer Preview 4 of the Android XR SDK, continuing our focus on unifying cross-device development for headsets, wired XR glasses, and intelligent eyewear.

  ###### [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld), [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva) •
  5 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
  - [#Developer Preview](https://developer.android.com/blog/topics/developer-preview)
  - [#Unity](https://developer.android.com/blog/topics/unity)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +3 ↩
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
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  4 min read

  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)