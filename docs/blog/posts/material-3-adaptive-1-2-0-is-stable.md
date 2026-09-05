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
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)