---
title: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
url: https://developer.android.com/blog/posts/material-3-adaptive-1-2-0-is-stable
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Material 3 Adaptive 1.2.0 is stable

###### 2-min read

![](https://developer.android.com/static/blog/assets/material3adaptive_72cc7e27f6_Z1Stpt5.webp) 27 Oct 2025 [![](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)](https://developer.android.com/blog/authors/rob-orgiu) [##### Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu)

###### Developer Relations Engineer

We're excited to announce that Material 3 Adaptive 1.2.0 is now stable!

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

###### Written by:

-

  ## [Rob Orgiu](https://developer.android.com/blog/authors/rob-orgiu)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/rob-orgiu) ![](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp) ![](https://developer.android.com/static/blog/assets/Rob_Orgiu_f45ebe80ce_22fyUM.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp)](https://developer.android.com/blog/authors/nataraj-k-r) 14 May 2026 14 May 2026 ![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_Z2wOXhv.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha)

  [arrow_forward](https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha) Building on this foundation, Jetpack Telecom v1.1.0 brings native-level visibility and convenience to third-party VoIP apps.

  ###### [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 12 May 2026 12 May 2026 ![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_Z2pmmBN.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building for the Intelligence System on Android](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android) Announced today during The Android Show, Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  4 min read

  - [#Android](https://developer.android.com/blog/topics/android)
- [![](https://developer.android.com/static/blog/assets/Vijaya_Kaza_38a0089092_1sYB49.webp)](https://developer.android.com/blog/authors/vijaya-kaza) 07 May 2026 07 May 2026 ![](https://developer.android.com/static/blog/assets/260429_A_look_ahead_to_2026_Banner_Strapi_2000_x_1000_px_b302a5104a_1L2cA4.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A look ahead: Making it easier and faster to publish safer apps](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps)

  [arrow_forward](https://developer.android.com/blog/posts/a-look-ahead-making-it-easier-and-faster-to-publish-safer-apps) The mobile ecosystem is always evolving, bringing both new opportunities and new threats. Through these changes, Android and Google Play remain committed to ensuring that billions of users can continue to enjoy their apps with confidence and developer innovation can thrive.

  ###### [Vijaya Kaza](https://developer.android.com/blog/authors/vijaya-kaza) •
  3 min read

  - [#Android](https://developer.android.com/blog/topics/android)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)