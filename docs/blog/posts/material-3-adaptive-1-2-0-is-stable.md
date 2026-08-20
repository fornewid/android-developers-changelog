---
title: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
url: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Material 3 Adaptive 1.2.0 is stable

1 min read ![](https://developer.android.com/static/blog/assets/material3adaptive_72cc7e27f6_Z1Stpt5.webp) 27 Oct 2025 [![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)](https://developer.android.com/blog/authors/rob-orgiu) [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu) Developer Relations Engineer We're excited to announce that Material 3 Adaptive 1.2.0 is now stable!

This release continues to build on the foundations of previous versions, expanding support to more breakpoints for window size classes and new strategies to place display panes automatically.

## What's new in Material 3 Adaptive 1.2.0

This stable release is built on top of WindowManager 1.5.0 support for large and extra large breakpoints, and introduces the new reflow and levitate strategies for `ListDetailPaneScaffold` and `SupportingPaneScaffold`.

## New window size classes: Large and Extra-large

![newwindow.png](https://developer.android.com/static/blog/assets/newwindow_fd436dbcaf_1LgrTp.webp)

<br />

[WindowManager 1.5.0 introduced two new breakpoints](https://android-developers.googleblog.com/2025/10/jetpack-windowmanager-15-is-stable.html) for width window size class to support even bigger windows than the Expanded window size class. The Large (L) and Extra-large (XL) breakpoints can be enabled by adding the following parameter to the `currentWindowAdaptiveInfo()` call in your codebase:

`currentWindowAdaptiveInfo(supportLargeAndXLargeWidth = true)`

This flag enables the library to also return L and XL breakpoints whenever they're needed.

## New adaptive strategies: reflow and levitate

Arranging content and display panes in a window is a complex task that needs to take into account many factors, starting with window size. With the new Material 3 Adaptive library, two new technologies can help you achieve an adaptive layout with minimal effort.

With **reflow**, panes are rearranged when window size or aspect ratio changes, placing a second pane to the side of the first one when the window is wide enough, or reflow the second pane underneath the first pane whenever the window is taller. This technique applies also when the window becomes smaller: content reflows to the bottom.
![material.jpg](https://developer.android.com/static/blog/assets/material_dd16fc956e_Z9aKm6.webp)

*Reflowing a pane based on the window size*

While reflowing is an incredible option in many cases, there might be situations in which the content might need to be either docked to a side of the window or *levitated* on top of it. The levitate strategy not only docks the content, but also allows you to customize features like draggability, resizability, and even the background scrim.

<br />

![material2.jpg](https://developer.android.com/static/blog/assets/material2_c8c506bd91_1mCTJO.webp)

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
  View profile](https://developer.android.com/blog/authors/rob-orgiu) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp) ![View Rob Orgiu's profile](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)
Continue reading
- [![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)](https://developer.android.com/blog/authors/blair-harmon) 19 Aug 2026 19 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_116_Preparing_your_app_for_expanded_memory_limits_strapi_0aac62fa12_1hkk5a.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Preparing your app for broader memory limits](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits)

  [arrow_forward](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits) A great user experience is central to Android's mission, and delivering on that promise requires keeping devices fast, responsive, and reliable.
  [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon) • 2 min read
  - [#App Memory Limits](https://developer.android.com/blog/topics/app-memory-limits)
  - [#Android Vitals](https://developer.android.com/blog/topics/android-vitals)
  - [#Multi-Process Architecture](https://developer.android.com/blog/topics/multi-process-architecture)
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +3 ↩
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_Z1YdYO1.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Jetpack XR SDK core libraries reach beta: The next milestone for Android XR](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr) Since introducing the Android XR SDK, developers have transformed their ideas into innovative immersive experiences across headsets and wired XR glasses.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld), [Greg Underwood](https://developer.android.com/blog/authors/greg-underwood), [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen) • 2 min read
  - [#Jetpack XR SDK](https://developer.android.com/blog/topics/jetpack-xr-sdk)
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)