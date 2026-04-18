---
title: https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts
url: https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Unfold new possibilities with Compose Adaptive Layouts 1.2 beta

###### 3-min read

![](https://developer.android.com/static/blog/assets/yt_MBG_2_a56f169e60_ZSoFHF.webp) 03 Sep 2025 [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor)

##### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)
\&
[Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

[Video](https://www.youtube.com/watch?v=-9zVrVmnbO4)

With new form factors like the [Pixel 10 Pro Fold](https://android-developers.googleblog.com/2025/08/build-your-app-to-meet-users-on-newest-pixel-devices.html) joining the Android ecosystem, [adaptive app development](https://developer.android.com/develop/ui/compose/build-adaptive-apps#why_build_adaptive_uis) is essential for creating high-quality user experiences across phones, tablets, and foldables. Users expect your app's UI to seamlessly adapt to these different sizes and postures.

To help you build these dynamic experiences more efficiently, we are announcing that the [Compose Adaptive Layouts Library 1.2](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.2.0-beta01) is officially entering beta. This release provides powerful new tools to create polished, responsive UIs for this expanding device ecosystem.

## Powerful new tools for a bigger canvas

The [Compose Adaptive Layouts library](https://developer.android.com/develop/ui/compose/build-adaptive-apps#compose_material_3_adaptive) is our foundational toolkit for building UIs that adapt across different window sizes. This new beta release is packed with powerful features to help you create sophisticated layouts with less code. Key additions include:

- **Powerful new layout strategies:** The beta introduces new layout strategies like [reflow](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/AdaptStrategy.Reflow) and [levitate](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/AdaptStrategy.Levitate), designed to help you build dynamic layouts that look great on both the outer and inner displays of a device like the [Pixel 10 Pro Fold](https://blog.google/products/pixel/google-pixel-10-pro-fold/), [Galaxy Z Fold7 and Z Flip7](https://news.samsung.com/global/design-story-the-next-chapter-in-innovation-galaxy-z-fold7-and-galaxy-z-flip7).
- **New Window Size Classes:** The release adds built-in support for the new Large and Extra-Large [window size classes](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes). These new breakpoints are essential for designing and triggering rich, multi-pane UI changes on expansive screens like tablets and large foldables.

![new-pane-adaptation.webp](https://developer.android.com/static/blog/assets/new_pane_adaptation_e6d40f43ac_1tj7qu.webp)

*Two new pane adaptation strategies: reflow (left) and levitate (right)*

For a full list of changes, check out the [official release documentation](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#1.2.0-beta01). Explore our guides on [canonical layouts](https://developer.android.com/develop/ui/compose/layouts/adaptive/canonical-layouts) and [building a supporting pane layout](https://developer.android.com/develop/ui/compose/layouts/adaptive/build-a-supporting-pane-layout).

## Engage more users on every screen

Embracing an [adaptive mindset](https://developer.android.com/develop/ui/compose/build-adaptive-apps#why_build_adaptive_uis) is more than a best practice, it's a strategy for growth. The goal isn't just to make your app work on a larger screen, but to make it shine by becoming more intuitive for users. Instead of simply stretching a single-column layout, think about how you can use the extra space to create more efficient and immersive experiences.
![adaptive2.png](https://developer.android.com/static/blog/assets/adaptive2_788bbb555d_YU6Ao.webp)

This is the core principle behind dynamic layout strategies like [`reflow`](https://developer.android.com/reference/kotlin/androidx/compose/material3/adaptive/layout/AdaptStrategy.Reflow), a powerful new feature in the Compose Adaptive Layouts 1.2 beta designed to help you build these UIs. For example, a great starting point is adopting a multi-pane layout. By showing a list and its corresponding detail view side-by-side, you reduce taps and allow users to accomplish tasks more quickly.

This kind of thoughtful adaptive development is what truly boosts engagement. And, as we highlighted during the latest episode of [#TheAndroidShow](https://youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3pwazNzY2hIc0Y0S0owbjV0YUdpTjFPc19EZ3xBQ3Jtc0trVWcwV1RFSUlIWlV1REVMYzlvX3M1SXdKdEUxM2pMN3JKN0hRWkpmbkltZ2k3WHZWR3JrTkNlQ1FqdGFFQ0ZNRlhkZ21adFdLSzhFSWh6ak1HUVBGUk1vN3ZPblBmdzl2TDRtZ0p0UnRxbmFTOHk1RQ&q=http://goo.gle/45Fl2fx&v=BXH6ZiLBT8A), this is why we see that users who use an app on both their phone and a larger screen are almost three times more engaged. Building adaptively doesn't just make your current users happier; it creates a more valuable and compelling experience that builds lasting loyalty and helps you reach new users.

## The expanding Android ecosystem, from foldables to desktops

This shift toward adaptive design extends across the entire Android ecosystem. From the new Pixel 10 Pro Fold to the latest Samsung Galaxy foldables, developers have the opportunity to engage a large and growing user base on over 500 million large-screen devices.
![material.png](https://developer.android.com/static/blog/assets/material_3f86236eeb_Xwexu.webp)

This is also why we're continuing to invest in forward-looking experiences like [Connected Displays](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-connected-displays), currently available to try in [developer preview](https://android-developers.googleblog.com/2025/06/developer-preview-enhanced-android-desktop-experiences-connected-displays.html). This feature opens up new surfaces and interaction models for apps to run on, enabling true desktop-class features and multi-instance workflows. We've previously shared details on how you can get started with the [Connected Displays developer preview](https://android-developers.googleblog.com/2025/06/developer-preview-enhanced-android-desktop-experiences-connected-displays.html) and see how it's shaping the future of multi-device experiences.

## Putting adaptive principles into practice

For developers who want to get their apps ready for this adaptive future, here are a few key [best practices](https://android-developers.googleblog.com/2025/05/adaptiveapps-io25.html) to keep in mind:

- **Take inventory:** The first step is to see where you are today. [Test your app](https://developer.android.com/training/testing/different-screens) on a large screen device or with the resizable emulator in Android Studio to identify areas for improvement, like stretched UIs or usability issues.
- **Support optimized layouts:** Use libraries like [Compose Adaptive Layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps#compose_material_3_adaptive) to build UI that adapts to different window sizes and device postures. Your app should work well in both portrait and landscape, without [restricting orientation](https://developer.android.com/develop/ui/compose/layouts/adaptive/app-orientation-aspect-ratio-resizability).
- **Think beyond touch:** A great adaptive experience means supporting all input methods. This goes beyond basic functionality to include thoughtful details that users expect, like hover states for mouse cursors, context menus on right-click, and support for [keyboard shortcuts](https://developer.android.com/develop/ui/compose/touch-input/keyboard-input/keyboard-shortcuts-helper).

Your app's potential is no longer confined to a single screen. Explore the [large screen design gallery](https://developer.android.com/large-screens/gallery) and app quality guidelines today to envision where your app can go. Get inspired and find design patterns, official guidance, and sample apps you need to build for every fold, flip, and screen at [developer.android.com/adaptive-apps](https://developer.android.com/adaptive-apps).

###### Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)
-

  ## [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/miguel-montemayor) ![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp) ![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 13 Feb 2026 13 Feb 2026 ![](https://developer.android.com/static/blog/assets/a17beta_bfff40b895_20Bzrw.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Prepare your app for the resizability and orientation changes in Android 17](https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17) With the release of Android 16 in 2025, we shared our vision for a device ecosystem where apps adapt seamlessly to any screen---whether it's a phone, foldable, tablet, desktop, car display, or XR. Users expect their apps to work everywhere.

  ###### [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) •
  6 min read

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