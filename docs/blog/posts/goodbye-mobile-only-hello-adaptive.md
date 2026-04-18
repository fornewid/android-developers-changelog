---
title: https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive
url: https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Goodbye Mobile Only, Hello Adaptive: Three essential updates from 2025 for building adaptive apps

###### 2-min read

![](https://developer.android.com/static/blog/assets/Android_adaptives_festivity_01_blog_f70d48134f_Z2lMDgd.webp) 19 Dec 2025 [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) [##### Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

###### Senior Product Manager

### **Goodbye Mobile Only, Hello Adaptive: Three essential updates from 2025 for building adaptive apps**

In 2025 the Android ecosystem has grown far beyond the phone. Today, developers have the opportunity to reach over 500 million active devices, including foldables, tablets, XR, Chromebooks, and compatible cars.
![9x.png](https://developer.android.com/static/blog/assets/9x_fe972fcca6_XjGI9.webp)

These aren't just additional screens; they represent a higher-value audience. We've seen that users who own both a phone and a tablet spend 9x more on apps and in-app purchases than those with just a phone. For foldable users, that average spend jumps to roughly 14x more\*.

This engagement signals a necessary shift in development: [goodbye mobile apps, hello adaptive apps](https://developer.android.com/adaptive-apps).
![adaptive-apps.png](https://developer.android.com/static/blog/assets/adaptive_apps_11b88516c3_Z1CoNWu.webp)

<br />

To help you build for that future, we spent this year releasing tools that make[adaptive the default way to build](https://developer.android.com/develop/ui/compose/build-adaptive-apps). Here are three key updates from 2025 designed to help you build these experiences.

### **Standardizing adaptive behavior with Android 16**

To support this shift, [Android 16 introduced significant changes](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html) to how apps can restrict orientation and resizability. On displays of at least 600dp, manifest and runtime restrictions are ignored, meaning apps can no longer lock themselves to a specific orientation or size. Instead, they fill the entire display window, ensuring your UI scales seamlessly across portrait and landscape modes.

Because this means your app context will change more frequently, it's important to verify that you are preserving UI state during configuration changes. While Android 16 offers a temporary opt-out to help you manage this transition, Android 17 (SDK37) will make this behavior mandatory. To ensure your app behaves as expected under these new conditions, use the resizable emulator in Android Studio to [test your adaptive layouts today](https://developer.android.com/training/testing/different-screens).

### **Supporting screens beyond the tablet with Jetpack WindowManager 1.5.0**

As devices evolve, our existing definitions of "large" need to evolve with them. In October, we [released Jetpack WindowManager 1.5.0](https://android-developers.googleblog.com/2025/10/jetpack-windowmanager-15-is-stable.html) to better support the growing number of very large screens and desktop environments.

On these surfaces, the standard "Expanded" layout, which usually fits two panes comfortably, often isn't enough. On a 27-inch monitor, two panes can look stretched and sparse, leaving valuable screen real estate unused. To solve this, WindowManager 1.5.0 introduced two new width window size classes: Large (1200dp to 1600dp) and Extra-large (1600dp+).
![window_size_classes_width.png](https://developer.android.com/static/blog/assets/window_size_classes_width_fc5a56047b_1Vja4S.webp)

These new breakpoints signal when to switch to high-density interfaces. Instead of stretching a typical list-detail view, you can take advantage of the width to show three or even four panes simultaneously. Imagine an email client that comfortably displays your folders, the inbox list, the open message, and a calendar sidebar, all in a single view. Support for these window size classes was added to [Compose Material 3 adaptive](https://developer.android.com/develop/ui/compose/layouts/adaptive)in the [1.2 release](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.2.0).

### **Rethinking user journeys with Jetpack Navigation 3**

Building a UI that morphs from a single phone screen to a multi-pane tablet layout used to require complex state management. This often meant forcing a navigation graph designed for single destinations to handle simultaneous views. First [announced at I/O 2025](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html), Jetpack Navigation 3 [is now stable](https://android-developers.googleblog.com/2025/11/jetpack-navigation-3-is-stable.html), introducing a new approach to handling user journeys in adaptive apps.

Built for Compose, [Nav3](https://developer.android.com/guide/navigation/navigation-3) moves away from the monolithic graph structure. Instead, it provides decoupled building blocks that give you full control over your back stack and state. This solves the single source of truth challenge common in split-pane layouts. Because Nav3 uses the Scenes API, you can display multiple panes simultaneously without managing conflicting back stacks, simplifying the transition between compact and expanded views.

### **A foundation for an adaptive future**

![unnamed (1).png](https://developer.android.com/static/blog/assets/unnamed_1_35df31a846_28qm56.webp)

<br />

This year delivered the tools you need, from optimizing for expansive layouts to the granular controls of [WindowManager](https://developer.android.com/jetpack/androidx/releases/window#version_15_2) and [Navigation 3](https://developer.android.com/guide/navigation/navigation-3). And, Android 16 began the shift toward truly flexible UI, with updates coming next year to deliver excellent adaptive experiences across all form factors. To learn more about [adaptive development principles](https://android-developers.googleblog.com/2025/05/adaptiveapps-io25.html) and get started, head over to [d.android.com/adaptive-apps](http://d.android.com/adaptive-apps).

The tools are ready, and the users are waiting. We can't wait to see what you build!

\*Source: internal Google data
- [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)
- [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
- [#Compose](https://developer.android.com/blog/topics/compose)
- [#Android 16](https://developer.android.com/blog/topics/android-16)

###### Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/don_bccb8c3f75_1ufD8A.webp)](https://developer.android.com/blog/authors/don-turner) 19 Nov 2025 19 Nov 2025 ![](https://developer.android.com/static/blog/assets/jetpack_navigation_d1257f9ca2_Z1dRNOI.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Jetpack Navigation 3 is stable](https://developer.android.com/blog/posts/jetpack-navigation-3-is-stable)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-navigation-3-is-stable) Jetpack Navigation 3 version 1.0 is stable!

  ###### [Don Turner](https://developer.android.com/blog/authors/don-turner) •
  3 min read

  - [#Nav3](https://developer.android.com/blog/topics/nav3)
  - [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)
- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 03 Sep 2025 03 Sep 2025 ![](https://developer.android.com/static/blog/assets/yt_MBG_2_a56f169e60_ZSoFHF.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Unfold new possibilities with Compose Adaptive Layouts 1.2 beta](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts)

  [arrow_forward](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts) With new form factors like the Pixel 10 Pro Fold joining the Android ecosystem, adaptive app development is essential for creating high-quality user experiences across phones, tablets, and foldables.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 10 Jun 2025 10 Jun 2025 ![](https://developer.android.com/static/blog/assets/across_Devices_1742e15ff4_ZE5L7I.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A product manager's guide to adapting Android apps across devices](https://developer.android.com/blog/posts/product-manager-guide-to-adapting-android-apps-across-devices)

  [arrow_forward](https://developer.android.com/blog/posts/product-manager-guide-to-adapting-android-apps-across-devices) This includes the start of Android 16's rollout, with details for both developers and users, a Developer Preview for enhanced Android desktop experiences with connected displays, and updates for Android users across Google apps and more, plus the June Pixel Drop.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) •
  6 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)