---
title: https://developer.android.com/blog/posts/introducing-android-xr-sdk-developer-preview
url: https://developer.android.com/blog/posts/introducing-android-xr-sdk-developer-preview
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Introducing Android XR SDK Developer Preview

###### 5-min read

![](https://developer.android.com/static/blog/assets/Android_XR_Unlocked_2a393b1726_2cbGb7.webp) 12 Dec 2024 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

Today, we're launching the developer preview of the [**Android XR SDK**](http://developer.android.com/xr) - a comprehensive development kit for [Android XR](https://blog.google/products/android/android-xr). It's the newest platform in the Android family built for extended reality (XR) headsets (and glasses in the future!). You'll have endless opportunities to create and develop experiences that blend digital and physical worlds, using familiar Android APIs, tools and open standards created for XR. All of this means: if you build for Android, you're already building for XR! Read on to get started with development for headsets.

With the Android XR SDK you can:

- Break free of traditional screens by spatializing your app with rich 3D elements, spatial panels, and spatial audio that bring a natural sense of depth, scale, and tangible realism
- Transport your users to a fantastical virtual space, or engage with them in their own homes or workplaces
- Take advantage of natural, multimodal interaction capabilities such as hands and eyes

*"We believe Android XR is a game-changer for storytelling. It allows us to merge narrative depth with advanced interactive features, creating an immersive world where audiences can engage with characters and stories like never before."*   
- Jed Weintrob, Partner at [**30 Ninjas**](https://30ninjas.com/)

### Your apps on Android XR

The Android XR SDK is built on the existing foundations of Android app development. We're also bringing the Play Store to Android XR, where [**most Android**](https://developer.android.com/develop/xr/get-started#app-manifest)**apps will automatically be made available** without any additional development effort. Users will be able to discover and use your existing apps in a whole new dimension. To differentiate your existing Compose app, you may [opt-in](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design#use-enablexrcomponentoverrides), to automatically spatialize Material Design (M3) components and [Compose for adaptive layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive) in XR.
![apps_optimized.webp](https://developer.android.com/static/blog/assets/apps_optimized_9427c22aa9_Z1rpw7o.webp)

*Apps optimized for large screens take advantage of sizing capabilities in Android XR*

The Android XR SDK has something for every developer:

Building with Kotlin and Android Studio? You'll feel right at home with the **Jetpack XR SDK**, a suite of familiar libraries and tools to simplify development and accelerate productivity.

- Using [Unity's real-time 3D engine](https://unity.com/)? The **Android XR Extensions for Unity** provides the packages you need to build or port powerful, immersive experiences.
- Developing on the web? Use **WebXR** to add immersive experiences supported on Chrome.
- Working with native languages like C/C++? Android XR supports the **OpenXR** 1.1 standard.

### Creating with Jetpack XR SDK

The Jetpack XR SDK includes new [Jetpack](https://developer.android.com/jetpack) libraries purpose-built for XR. The highlights include:

- [**Jetpack Compose for XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk/develop-ui) - enables you to declaratively create spatial UI layouts and spatialize your existing 2D UI built with Compose or Views
- [**Material Design for XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk/material-design) - includes components and layouts that automatically adapt for XR
- [**Jetpack SceneCore**](https://developer.android.com/develop/xr/jetpack-xr-sdk#jetpack-scenecore) - provides the foundation for building custom 3D experiences
- [**ARCore for Jetpack XR**](https://developer.android.com/develop/xr/jetpack-xr-sdk/work-with-arcore) - brings powerful perception capabilities for your app to understand the real world

*"With Android XR, we can bring Calm directly into your world, capturing the senses and allowing you to experience it in a deeper and more transformative way. By collaborating closely with the Android XR team on this cutting-edge technology, we've reimagined how to create a sense of depth and space, resulting in a level of immersion that instantly helps you feel more present, focused, and relaxed."*   
- Dan Szeto, Vice President at [**Calm Studios**](https://www.calm.com/)

Kickstart your Jetpack XR SDK journey with the [**Hello XR Sample**](https://github.com/android/xr-samples), a straightforward introduction to the essential features of Jetpack Compose for XR.

Learn more about [developing with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk).
![jetnews.webp](https://developer.android.com/static/blog/assets/jetnews_6820eb2c7d_Z1cnsAA.webp)

*The JetNews sample app is an Android large-screen app adapted for Android XR*

We're also introducing new tools and capabilities to the latest preview of [Android Studio Meerkat](https://developer.android.com/studio/preview) to boost productivity and simplify your creation process for Android XR.

- Use the new **Android XR Emulator** to create a virtualized XR device for deploying and testing apps built with the Jetpack XR SDK. The emulator includes XR-specific controls for using a keyboard and mouse to navigate an emulated virtual space.
- Use the Android XR template to get a jump-start on creating an app with Jetpack Compose for XR.
- Use the updated Layout Inspector to inspect and debug spatialized UI components created with Jetpack Compose for XR.

Learn more about the XR enabled tools in [Android Studio and the Android XR Emulator](https://developer.android.com/develop/xr/jetpack-xr-sdk/studio-tools).
![xr_emulator2.webp](https://developer.android.com/static/blog/assets/xr_emulator2_0d97fadcd3_6dHpr.webp)

*The Android XR Emulator in Android Studio has new controls to explore 3D space within the emulator*

### Creating with Unity

We've partnered with Unity to natively integrate their real-time 3D engine with Android XR starting with [Unity 6](https://unity.com/releases/unity-6). Unity is introducing the [Unity OpenXR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@latest) package for bringing your multi-platform XR experiences to Android XR.

Unity is adding Android XR support to these popular XR packages:

- [OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/index.html)
- [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/index.html)
- [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/index.html)
- [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.5/manual/index.html)
- [XR Composition Layers](https://docs.unity3d.com/Packages/com.unity.xr.compositionlayers@1.0/manual/usage-guide.html)

We're also rolling out the Android XR Extensions for Unity with samples and innovative features such as mouse interaction profile, environment blend mode, personalized hand mesh, object tracking, and more.

*"Having already brought Demeo to most commercially available platforms, it's safe to say we were impressed with the process of adapting the game to run on Android XR."*   
-- Johan Gastrin, CTO at [**Resolution Games**](https://www.resolutiongames.com/)

Check out our [getting started guide for unity](https://developer.android.com/develop/xr/unity) and [Unity's blog post](https://on.unity.com/3DdnxJW) to learn more.
![vacation_simulator.webp](https://developer.android.com/static/blog/assets/vacation_simulator_65f68eaafa_VwB4c.webp)

[*Vacation Simulator*](https://owlchemylabs.com/blog/owlchemy-labs-announces-android-xr-support-for-job-simulator-vacation-simulator)* has been updated to Unity 6 and supports Android XR*

### Creating for the Web

Chrome on Android XR supports the **WebXR** standard. If you're building for the web, you can enhance existing sites with 3D content or build new immersive experiences. You can also use full-featured frameworks like [three.js](https://threejs.org/), [A-Frame](https://aframe.io/), or [PlayCanvas](https://github.com/playcanvas/engine) to create virtual worlds, or you can use a simpler API like [model-viewer](https://modelviewer.dev/) so your users can visualize products in an e-commerce site. And because WebXR is an [open standard](https://www.w3.org/TR/webxr/), the same experiences you build for mobile AR devices or dedicated VR hardware seamlessly work on Android XR.

Learn more about [developing with WebXR](https://developer.android.com/develop/xr/develop-with-webxr).
![webxr_blur.webp](https://developer.android.com/static/blog/assets/webxr_blur_fe9ecfa326_1zv9Yg.webp)

*Chrome on Android XR supports WebXR features including depth maps allowing virtual objects to interact with real world surfaces*

### Built on Open Standards

We're continuing the Android tradition of building with open standards. At the heart of the Android perception stack is **OpenXR** - a high-performance, cross-platform API focused on portability. Android XR is compliant with [OpenXR 1.1](https://registry.khronos.org/OpenXR/specs/1.1/html/xrspec.html), and we're also expanding the Open XR standards with leading-edge [vendor extensions](https://developer.android.com/develop/xr/openxr/extensions) to introduce powerful world-sensing capabilities such as:

- AI-powered [hand mesh](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_hand_mesh), designed to adapt to the shape and size of hands to better represent the diversity of your users
- [Detailed depth textures](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_depth_texture) that allow real world objects to occlude virtual content
- Sophisticated [light estimation](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_light_estimation), for lighting your digital content to match real-world lighting conditions
- [New trackables](https://developer.android.com/develop/xr/openxr/extensions/XR_ANDROID_trackables_object) that let you bring real world objects like laptops, phones, keyboards, and mice into a virtual environment

The Android XR SDK also supports open standard formats such as [glTF 2.0](https://www.khronos.org/gltf/) for 3D models and [OpenEXR](https://openexr.com/en/latest/TechnicalIntroduction.html) for high-dynamic-range environments.

### Building the future together

We couldn't be more proud or excited to be announcing the Developer Preview of the Android XR SDK. We're releasing this developer preview, because we want to build the future of XR together with you. We welcome your [feedback](https://developer.android.com/develop/xr/support) and can't wait to work with you and build your ideas and suggestions into the platform. Your passion, expertise, and bold ideas are absolutely essential as we continue to build Android XR.

We look forward to interacting with your apps, reimagined to take advantage of the unique spatial capabilities of Android XR, using familiar tools like Android Studio and Jetpack Compose. We're eager to visit the amazing 3D worlds you build using powerful tools and open standards like Unity and OpenXR. Most of all, we can't wait to go on this journey with all of you that make up the amazing community of Android and Unity developers.

To get started creating and developing for Android XR, check out [developer.android.com/develop/xr](https://developer.android.com/develop/xr) where you will find all of the tools, libraries and resources you need to create with the Android XR SDK! If you are interested in getting access to prerelease hardware and collaborating with the Android XR team, express your interest to participate in an **Android XR Developer Bootcamp** in 2025 by filling out this [form](https://developer.android.com/develop/xr#bootcamp).

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