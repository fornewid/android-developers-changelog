---
title: https://developer.android.com/about/versions/lollipop
url: https://developer.android.com/about/versions/lollipop
source: md.txt
---

# Android Lollipop

![Assorted display of devices including a watch, mobile, and landscape-oriented tablet showcasing Android 5.0](https://developer.android.com/static/images/home/l-hero_2x.png)

Welcome to Android 5.0 Lollipop---the largest and most ambitious release for Android yet!

This release is packed with new features for users and thousands of new APIs for developers. It extends Android even further, from phones, tablets, and wearables, to TVs and cars.

For a closer look at the new developer APIs, see the[Android 5.0 API Overview](https://developer.android.com/about/versions/android-5.0). Or, read more about Android 5.0 for consumers at[www.android.com](https://www.android.com/versions/lollipop-5-0/).

**Note:** The Android 5.1 Lollipop MR1 update is available with additional features and fixes. For more information, see the[Android 5.1 API Overview](https://developer.android.com/about/versions/android-5.1).

## Material design

Android 5.0 brings[Material design](http://www.google.com/design/spec)to Android and gives you an expanded UI toolkit for integrating the new design patterns easily in your apps.

New**3D views** let you set a z-level to raise elements off of the view hierarchy and cast**realtime shadows**, even as they move.

Built-in**activity transitions** take the user seamlessly from one state to another with beautiful, animated motion. The material theme adds transitions for your activities, including the ability to use**shared visual elements**across activities.  

*To replay the movie, click on the device screen*

Ripple animations are available for buttons, checkboxes, and other touch controls in your app.

You can also define vector drawables in XML and animate them in a variety of ways. Vector drawables scale without losing definition, so they are perfect for single-color in-app icons.

A new system-managed processing thread called**RenderThread**keeps animations smooth even when there are delays in the main UI thread.

## Performance focus

Android 5.0 provides a faster, smoother and more powerful computing experience.

Android now runs exclusively on the new**ART runtime**, built from the ground up to support a mix of ahead-of-time (AOT), just-in-time (JIT), and interpreted code. It's supported on ARM, x86, and MIPS architectures and is fully 64-bit compatible.

ART improves app performance and responsiveness. Efficient garbage collection reduces the number and duration of pauses for GC events, which fit comfortably within the v-sync window so your app doesn't skip frames. ART also dynamically moves memory to optimize performance for foreground uses.

Android 5.0 introduces platform support for**64-bit architectures**---used by the Nexus 9's NVIDIA Tegra K1. Optimizations provide larger address space and improved performance for certain compute workloads. Apps written in the Java language run as 64-bit apps automatically---no modifications are needed. If your app uses native code, we've extended the NDK to support new ABIs for ARM v8, and x86-64, and MIPS-64.

Continuing the focus on smoother performance, Android 5.0 offers improved A/V sync. The audio and graphics pipelines have been instrumented for more accurate timestamps, enabling video apps and games to display smooth synchronized content.

## Notifications

![Top section of mobile showing heads-up notification alert](https://developer.android.com/static/images/versions/notification-headsup.png)

Notifications in Android 5.0 are more visible, accessible, and configurable.

Varying notification details may appear**on the lock screen**if desired by the user. Users may elect to allow none, some, or all notification content to be shown on a secure lock screen.

Key notification alerts such as incoming calls appear in a**heads-up notification**---a small floating window that allows the user to respond or dismiss without leaving the current app.

You can now add**new metadata**to notifications to collect associated contacts (for ranking), category, and priority.

A new media notification template provides consistent media controls for notifications with up to 6 action buttons, including custom controls such as "thumbs up"---no more need for RemoteViews!

## Your apps on the big screen

[Android TV](https://developer.android.com/tv/index.html)provides a complete TV platform for your app's big screen experience. Android TV is centered around a simplified home screen experience that allows users to discover content easily, with personalized recommendations and voice search.

With Android TV you can now**create big, bold experiences** for your app or game content and support interactions with game controllers and other input devices. To help you build cinematic, 10-foot UIs for television, Android provides a**leanback UI framework** in the[v17 support library](https://developer.android.com/tools/support-library/features#v17-leanback).

The**Android TV Input Framework**(TIF) allows TV apps to handle video streams from sources such as HDMI inputs, TV tuners, and IPTV receivers. It also enables live TV search and recommendations via metadata published by the TV Input and includes an HDMI-CEC Control Service to handle multiple devices with a single remote.

The TV Input Framework provides access to a wide variety of live TV input sources and brings them together in a single user interface for users to browse, view, and enjoy content. Building a TV input service for your content can help make your content more accessible on TV devices.

## Document-centric apps

![Mobile showing the new redesigned Overview space - formerly called Recents](https://developer.android.com/static/images/versions/recents_screen_2x.png)

Document-centric recents.

Android 5.0 introduces a redesigned Overview space (formerly called Recents) that's more versatile and useful for multitasking.

New APIs allow you to show separate activities in your app as individual documents alongside other recent screens.

You can take advantage of concurrent documents to provide users instant access to more of your content or services. For example, you might use concurrent documents to represent files in a productivity app, player matches in a game, or chats in a messaging app.

## Advanced connectivity

Android 5.0 adds new APIs that allow apps to perform concurrent operations with**Bluetooth Low Energy**(BLE), allowing both scanning (central mode) and advertising (peripheral mode).

New**multi-networking**features allow apps to query available networks for available features such as whether they are Wi-Fi, cellular, metered, or provide certain network features. Then the app can request a connection and respond to connectivity loss or other network changes.

**NFC**APIs now allow apps to register an NFC application ID (AID) dynamically. They can also set the preferred card emulation service per active service and create an NDEF record containing UTF-8 text data.

## High-performance graphics

Support for**[Khronos OpenGL ES 3.1](http://www.khronos.org/opengles/3_X/)**now provides games and other apps the highest-performance 2D and 3D graphics capabilities on supported devices.  
![Tablet showing Gameloft's Rival Knights gameplay](https://developer.android.com/static/images/versions/rivalknights.png)

Gameloft's Rival Knights uses ASTC (Adaptive Scalable Texture Compression) from AEP and Compute Shaders from ES 3.1 to deliver HDR (High Dynamic Range) Bloom effects and provide more graphical detail.

OpenGL ES 3.1 adds compute shaders, stencil textures, accelerated visual effects, high quality ETC2/EAC texture compression, advanced texture rendering, standardized texture size and render-buffer formats, and more.

Android 5.0 also introduces the**Android Extension Pack**(AEP), a set of OpenGL ES extensions that give you access to features like tessellation shaders, geometry shaders, ASTC texture compression, per-sample interpolation and shading, and other advanced rendering capabilities. With AEP you can deliver high-performance graphics across a range of GPUs.

## More powerful audio

A new audio-capture design offers**low-latency audio input**. The new design includes: a fast capture thread that never blocks except during a read; fast track capture clients at native sample rate, channel count, and bit depth; and normal capture clients offer resampling, up/down channel mix, and up/down bit depth.

Multi-channel**audio stream mixing**allows professional audio apps to mix up to eight channels including 5.1 and 7.1 channels.

Apps can expose their media content and**browse media**from other apps, then request playback. Content is exposed through a queryable interface and does not need to reside on the device.

Apps have finer-grain control over**text-to-speech synthesis**through voice profiles that are associated with specific locales, quality and latency rating. New APIs also improve support for synthesis error checking, network synthesis, language discovery, and network fallback.

Android now includes support for standard**USB audio** peripherals, allowing users to connect USB headsets, speakers, microphones, or other high performance digital peripherals. Android 5.0 also adds support for**Opus**audio codecs.

New**[MediaSession](https://developer.android.com/reference/android/media/session/MediaSession)**APIs for controlling media playback now make it easier to provide consistent media controls across screens and other controllers.

## Enhanced camera \& video

Android 5.0 introduces**all new camera APIs**that let you capture raw formats such as YUV and Bayer RAW, and control parameters such as exposure time, ISO sensitivity, and frame duration on a per-frame basis. The new fully-synchronized camera pipeline allows you to capture uncompressed full-resolution YUV images at 30 FPS on supported devices.

In addition to giving greater control over image capture, the new APIs also expose detailed information about the camera's properties and capabilities and provide metadata that describes the capture settings of each frame.

Apps sending video streams over the network can now take advantage of H.265**High Efficiency Video Coding (HEVC)**for optimized encoding and decoding of video data.

Android 5.0 also adds support for**multimedia tunneling**to provide the best experience for ultra-high definition (4K) content and the ability to play compressed audio and video data together.

## Android in the workplace

![Mobile displaying unified view of user's personal and work apps, which are badged for easy identification](https://developer.android.com/static/images/android-5.0/managed_apps_launcher@2x.png)

Users have a unified view of their personal and work apps, which are badged for easy identification.

To enable bring-your-own-device for enterprise environments, a new[managed provisioning process](https://developer.android.com/about/versions/android-5.0#Enterprise)creates a secure work profile on the device. In the launcher, apps are shown with a Work badge to indicate that the app and its data are administered inside of the work profile by an IT administrator.

Notifications for both the personal and work profile are visible in a unified view. The data for each profile is always kept separate and secure from each other, including when the same app is used by both profiles.

For company-owned devices, IT administrators can start with a new device and configure it with a[device owner](https://developer.android.com/about/versions/android-5.0#DeviceOwner). Employers can issue these devices with a device owner app already installed that can configure global device settings.

## Screen capturing and sharing

Android 5.0 lets you add screen capturing and screen sharing capabilities to your app.

With user permission, you can capture non-secure video from the display and deliver it over the network if you choose.

## New types of sensors

In Android 5.0, a new**tilt detector** sensor helps improve activity recognition on supported devices, and a**heart rate sensor**reports the heart rate of the person touching the device.

New**interaction composite sensors** are now available to detect special interactions such as a*wake up* gesture, a*pick up* gesture, and a*glance*gesture.

## Chromium WebView

![Chromium WebView logo](https://developer.android.com/static/images/kk-chromium-icon.png)

The initial release for Android 5.0 includes a version of Chromium for[WebView](https://developer.android.com/reference/android/webkit/WebView)based on the Chromium M37 release, adding support for**WebRTC** ,**WebAudio** , and**WebGL**.

Chromium M37 also includes native support for all of the**Web Components** specifications: Custom Elements, Shadow DOM, HTML Imports, and Templates. This means you can use[Polymer](http://polymer-project.org/)and its[material design elements](https://www.polymer-project.org/docs/elements/material.html)in a WebView without needing polyfills.

Although WebView has been based on Chromium since Android 4.4, the Chromium layer is now updatable from Google Play.

As new versions of Chromium become available, users can update from Google Play to ensure they get the latest enhancements and bug fixes for WebView, providing the latest web APIs and bug fixes for apps using WebView on Android 5.0 and higher.

## Accessibility \& input

New accessibility APIs can retrieve detailed information about the properties of windows on the screen that sighted users can interact with and define standard or customized input actions for UI elements.

New Input method editor (IME) APIs enable faster switching to other IMEs directly from the input method.

## Tools for building battery-efficient apps

New**job scheduling**APIs allow you optimize battery life by deferring jobs for the system to run at a later time or under specified conditions, such as when the device is charging or connected to Wi-Fi.

A new`dumpsys batterystats`command generates**battery usage statistics**that you can use to understand system-wide power use and understand the impact of your app on the device battery. You can look at a history of power events, approximate power use per UID and system component, and more.
![Visualization for battery-related debugging using the new Battery Historian tool](https://developer.android.com/static/images/versions/battery_historian.png)

Battery Historian is a new tool to convert the statistics from`dumpsys batterystats`into a visualization for battery-related debugging. You can find it at<https://github.com/google/battery-historian>.