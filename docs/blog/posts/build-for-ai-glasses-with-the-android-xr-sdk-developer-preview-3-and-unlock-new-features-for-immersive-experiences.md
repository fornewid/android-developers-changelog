---
title: https://developer.android.com/blog/posts/build-for-ai-glasses-with-the-android-xr-sdk-developer-preview-3-and-unlock-new-features-for-immersive-experiences
url: https://developer.android.com/blog/posts/build-for-ai-glasses-with-the-android-xr-sdk-developer-preview-3-and-unlock-new-features-for-immersive-experiences
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Build for AI Glasses with the Android XR SDK Developer Preview 3 and unlock new features for immersive experiences

###### 4-min read

![](https://developer.android.com/static/blog/assets/buildfor_A_Iglassesxr_5141a407fc_7gpQN.webp) 08 Dec 2025 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

In October, Samsung launched [Galaxy XR](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html) - the first device powered by [Android XR](http://d.android.com/xr). And it's been amazing seeing what some of you have been building! Here's what some of our developers have been saying about their journey into Android XR.

*Android XR gave us a whole new world to build our app within. Teams should ask themselves: What is the biggest, boldest version of your experience that you could possibly build? This is your opportunity to finally put into action what you've always wanted to do, because now, you have the platform that can make it real. - *[Kristen Coke, Calm, Lead Product Manager](https://android-developers.googleblog.com/2025/10/how-calm-reimagined-mindfulness-for.html)

You've also seen us share a first look at other upcoming devices that work with Android XR like Project Aura from [XREAL](http://www.xreal.com/aura) and [stylish glasses](https://blog.google/products/android/android-xr-gemini-glasses-headsets/) from Gentle Monster and Warby Parker.

To support the expanding selection of XR devices, we are announcing **Android XR SDK Developer Preview 3!**
![image.png](https://developer.android.com/static/blog/assets/image_8c8c9dea97_2r9k3z.webp)

With Android XR SDK Developer Preview 3, on top of building [**immersive experiences**](https://developer.android.com/develop/xr/explore/immersive) for devices such as Galaxy XR, you can also now build [**augmented experiences**](https://developer.android.com/develop/xr/explore/augmented) for upcoming AI Glasses with Android XR.

### New tools and libraries for augmented experiences

With developer preview 3, we are unlocking the tools and libraries you need to build intelligent and hands-free augmented experiences for AI Glasses. AI Glasses are lightweight and portable for all day wear. You can extend your existing mobile app to take advantage of the built-in speakers, camera, and microphone to provide new, thoughtful and helpful user interactions. With the addition of a small display on display AI Glasses, you can privately present information to users. AI Glasses are perfect for experiences that can help enhance a user's focus and presence in the real world.
![image.png](https://developer.android.com/static/blog/assets/image_4dc96f367c_ZfWgSV.webp)

To power augmented experiences on AI Glasses, we are introducing two new, purpose-built libraries to the Jetpack XR SDK:

- **Jetpack Projected** - built to bridge mobile devices and AI Glasses with features that allow you to [access sensors, speakers, and displays](https://developer.android.com/develop/xr/jetpack-xr-sdk/access-hardware) on glasses
- **Jetpack Compose Glimmer** - new design language and [UI components](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer/whats-included#components) for crafting and styling your augmented experiences on display AI Glasses

Jetpack Compose Glimmer is a demonstration of design best practices for beautiful, optical see-through augmented experiences. With UI components optimized for the input modality and styling requirements of display AI Glasses, Jetpack Compose Glimmer is designed for clarity, legibility, and minimal distraction.
![image.png](https://developer.android.com/static/blog/assets/image_266f9f13a9_SEuUo.webp)

To help visualize and test your Jetpack Compose Glimmer UI we are introducing the AI Glasses emulator in [Android Studio](https://developer.android.com/studio/preview). The new AI Glasses emulator can simulate glasses-specific interactions such as touchpad and voice input.
![AI Glasses Emulator.gif](https://developer.android.com/static/blog/assets/AI_Glasses_Emulator_301e46b50c_ZEknF2.webp)

Beyond the new Jetpack Projected and Jetpack Compose Glimmer libraries, we are also expanding **ARCore for Jetpack XR** to support AI Glasses. We are starting off with [motion tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/device-pose) and [geospatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/geospatial) for augmented experiences - the exact features that enable you to create helpful navigation experiences perfect for all-day-wear devices like AI Glasses.
![navigation.webp](https://developer.android.com/static/blog/assets/navigation_961934fb0b_Z2aCM5M.webp)

### Expanding support for immersive experiences

We continue to invest in the libraries and tooling that power immersive experiences for **XR Headsets** like Samsung Galaxy XR and wired **XR Glasses** like the upcoming Project Aura from XREAL. We've been listening to your feedback and have added several highly-requested features to the **Jetpack XR SDK** since developer preview 2.

**Jetpack SceneCore** now features dynamic [glTF model loading via URIs and improved materials](https://developer.android.com/develop/xr/tas-xr-gltf-model-materials) support for creating new PBR materials at runtime. Additionally, the [SurfaceEntity](https://developer.android.com/reference/androidx/xr/scenecore/SurfaceEntity) component has been [enhanced with full Widevine Digital Rights Management](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video#play-drm) (DRM) support and new shapes, allowing it to [render 360-degree and 180-degree videos](https://developer.android.com/develop/xr/jetpack-xr-sdk/add-spatial-video#play-180) in spheres and hemispheres.

In **Jetpack Compose for XR** , you'll find new features like the [UserSubspace](https://developer.android.com/develop/xr/tas-xr-user-subspace) component for follow behavior, ensuring content remains in the user's view regardless of where they look. Additionally, you can now use [spatial animations](https://developer.android.com/reference/kotlin/androidx/xr/compose/subspace/animation/SpatialTransitions) for smooth transitions like sliding or fading. And to support an expanding ecosystem of immersive devices with diverse display capabilities, you can now specify [layout sizes](https://developer.android.com/develop/xr/jetpack-xr-sdk/subspacemodifiers) as fractions of the user's comfortable field of view.

In **Material Design for XR** , new components automatically adapt spatially via [overrides](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#use-enablexrcomponentoverrides). These include [dialogs](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#dialogs) that elevate spatially, and [navigation bars](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#navigation-bar), which pop out into an Orbiter. Additionally, there is a new [SpaceToggleButton](https://developer.android.com/reference/kotlin/androidx/xr/compose/material3/package-summary#SpaceToggleButton(androidx.compose.ui.Modifier,androidx.compose.material3.IconToggleButtonColors,kotlin.Function1)) component for easily transitioning to and from full space.

<br />

And in **ARCore for Jetpack XR** , new perception capabilities have been added, including [face tracking](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/face) with 68 blendshape values unlocking a world of facial gestures. You can also use [eye tracking](https://developer.android.com/reference/kotlin/androidx/xr/arcore/Eye) to power virtual avatars, and [depth maps](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/depth) to enable more-realistic interactions with a user's environment.

For devices like Project Aura from XREAL, we are introducing the [XR Glasses emulator](https://developer.android.com/studio/releases/emulator) in Android Studio. This essential tool is designed to give you accurate content visualization, while matching real device specifications for Field of View (FoV), Resolution, and DPI to accelerate your development.
![xrglasses-emulator-haxr-cropped.webp](https://developer.android.com/static/blog/assets/xrglasses_emulator_haxr_cropped_b46d37d949_Z5ggmm.webp)

If you build immersive experiences with [Unity](https://unity.com/), we're also expanding your perception capabilities in the **Android XR SDK for Unity**. In addition to lots of bug fixes and other improvements, we are expanding tracking capabilities to include: QR and ArUco codes, planar images, and body tracking (experimental). We are also introducing a much-requested feature: scene meshing. It enables you to have much deeper interactions with your user's environment - your digital content can now bounce off of walls and climb up couches!

And that's just the tip of the iceberg! Be sure to check out our [immersive experiences](https://developer.android.com/develop/xr/explore/immersive) page for more information.

### Get Started Today!

The **Android XR SDK Developer Preview 3 is available today** ! Download the latest [Android Studio Canary](https://developer.android.com/studio/preview) (Otter 3, Canary 4 or later) and upgrade to the latest emulator version (36.4.3 Canary or later) and then visit [developer.android.com/xr](http://developer.android.com/xr) to get started with the latest libraries and [samples](https://developer.android.com/develop/xr/samples) you need to build for the growing selection of Android XR devices. We're building Android XR together with you! Don't forget to share your [feedback, suggestions, and ideas](https://developer.android.com/develop/xr/support) with our team as you progress on your journey in Android XR.

###### Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Third Beta of Android 17](https://developer.android.com/blog/posts/the-third-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-third-beta-of-android-17) Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  5 min read

  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#beta](https://developer.android.com/blog/topics/beta)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Bench_f2e4dd4fda_2816Hg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating AI-assisted Android development and improving LLMs with Android Bench](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench) We want to make it faster and easier for you to build high-quality Android apps, and one way we're helping you be more productive is by putting AI at your fingertips.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)