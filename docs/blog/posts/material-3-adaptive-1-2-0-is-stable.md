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

- [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) 13 Apr 2026 13 Apr 2026 ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Test Multi-Device Interactions with the Android Emulator](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator)

  [arrow_forward](https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator) Testing multi-device interactions is now easier than ever with the Android Emulator.

  ###### [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)