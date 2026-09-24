---
title: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
url: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Material 3 Adaptive 1.2.0 is stable

1 min read ![](https://developer.android.com/static/blog/assets/material3adaptive_72cc7e27f6_ZlWmpA.webp) 27 Oct 2025 [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp)](https://developer.android.com/blog/authors/rob-orgiu) [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) Developer Relations Engineer We're excited to announce that Material 3 Adaptive 1.2.0 is now stable!

This release continues to build on the foundations of previous versions, expanding support to more breakpoints for window size classes and new strategies to place display panes automatically.

## What's new in Material 3 Adaptive 1.2.0

This stable release is built on top of WindowManager 1.5.0 support for large and extra large breakpoints, and introduces the new reflow and levitate strategies for `ListDetailPaneScaffold` and `SupportingPaneScaffold`.

## New window size classes: Large and Extra-large

![newwindow.png](https://developer.android.com/static/blog/assets/newwindow_fd436dbcaf_Z1QxAC8.webp)

<br />

[WindowManager 1.5.0 introduced two new breakpoints](https://android-developers.googleblog.com/2025/10/jetpack-windowmanager-15-is-stable.html) for width window size class to support even bigger windows than the Expanded window size class. The Large (L) and Extra-large (XL) breakpoints can be enabled by adding the following parameter to the `currentWindowAdaptiveInfo()` call in your codebase:

`currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true)`

This flag enables the library to also return L and XL breakpoints whenever they're needed.

## New adaptive strategies: reflow and levitate

Arranging content and display panes in a window is a complex task that needs to take into account many factors, starting with window size. With the new Material 3 Adaptive library, two new technologies can help you achieve an adaptive layout with minimal effort.

With **reflow**, panes are rearranged when window size or aspect ratio changes, placing a second pane to the side of the first one when the window is wide enough, or reflow the second pane underneath the first pane whenever the window is taller. This technique applies also when the window becomes smaller: content reflows to the bottom.
![material.jpg](https://developer.android.com/static/blog/assets/material_dd16fc956e_xGHua.webp)

*Reflowing a pane based on the window size*

While reflowing is an incredible option in many cases, there might be situations in which the content might need to be either docked to a side of the window or *levitated* on top of it. The levitate strategy not only docks the content, but also allows you to customize features like draggability, resizability, and even the background scrim.

<br />

![material2.jpg](https://developer.android.com/static/blog/assets/material2_c8c506bd91_Z2gb8LI.webp)

*Levitating a pane from the side to the center based on the aspect ratio*

Both the flow and levitate strategies can be declared inside the `Navigator` constructor using the adaptStrategies parameter, and both strategies can be applied to list-detail and supporting pane `scaffolds`:

```
val navigator = rememberListDetailPaneScaffoldNavigator<Nothing>(
        adaptStrategies = ListDetailPaneScaffoldDefaults.adaptStrategies(
            detailPaneAdaptStrategy = AdaptStrategy.Reflow(
                reflowUnder = ListDetailPaneScaffoldRole.List
            ),
            extraPaneAdaptStrategy = AdaptStrategy.Levitate(
                alignment = Alignment.Center
            )
        )
    )
```

<br />

To learn more about how to leverage these new adaptive strategies, see the [Material website](https://m3.material.io/foundations/layout/applying-layout/pane-layouts#d692ea5e-2dda-4071-a1f6-8c1dc5a82f5d) and the complete [sample code](https://github.com/androidx/androidx/blob/8bb7d5cbce10c0c5cf62a24d79ce1337ff1727be/compose/material3/adaptive/samples/src/main/java/androidx/compose/material3/adaptive/samples/ThreePaneScaffoldSample.kt) on GitHub.
Written by:

-

  ## [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/rob-orgiu) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_Z2l461S.webp)
Continue reading
- 3 Authors 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Android_X_Security_State_Library_Strapi_d3ecf61180_YYwl5.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing the AndroidX Security State Libraries: A Unified View of Device Security](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security) Today, we're thrilled to announce the stable release of the AndroidX Security State version 1.1.0 and Security State Provider version 1.0.0 libraries.
  [Maunik Shah](https://developer.android.com/blog/authors/maunik-shah), [Alec Garcia](https://developer.android.com/blog/authors/alec-garcia), [Joseph Yong](https://developer.android.com/blog/authors/joseph-yong) • 4 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Bench_2_0_Strapi_bench_8767d57564_ZmnAe.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks)

  [arrow_forward](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks) Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- 3 Authors 09 Sep 2026 09 Sep 2026 ![](https://developer.android.com/static/blog/assets/Introducing_Fast_and_Reliable_Wireless_Debugging_Strapi_cf55ad145b_2vFLdh.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing Fast and Reliable Wireless Debugging with Android Debug Bridge (ADB) Wi-Fi 2.0](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0) Wireless debugging on Android is now faster, more reliable, and easier to set up than ever. With ADB Wi-Fi 2.0, we've introduced a new server stack and smarter network handling to directly address developer feedback around usability gaps.
  [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins), [Sherif Eid](https://developer.android.com/blog/authors/sherif-eid), [Fabien Sanglard](https://developer.android.com/blog/authors/fabien-sanglard) • 1 min read
  - [#Wireless Debugging](https://developer.android.com/blog/topics/wireless-debugging)
  - [#ADB Wi-Fi 2.0](https://developer.android.com/blog/topics/adb-wi-fi-2-0)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)