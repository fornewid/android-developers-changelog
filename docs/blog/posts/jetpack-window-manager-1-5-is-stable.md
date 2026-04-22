---
title: https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable
url: https://developer.android.com/blog/posts/jetpack-window-manager-1-5-is-stable
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Jetpack WindowManager 1.5 is stable

###### 3-min read

![](https://developer.android.com/static/blog/assets/jetpack_Window_Manager_931d67ec18_Z20PMAS.webp) 10 Oct 2025 [![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)](https://developer.android.com/blog/authors/francesco-romano) [##### Francesco Romano](https://developer.android.com/blog/authors/francesco-romano)

###### Developer Relations Engineer, Android

We're excited to announce that[Jetpack WindowManager 1.5.0](https://developer.android.com/jetpack/androidx/releases/window#version_15_2) is now stable!

This release builds on the strong foundation of adaptability in WindowManager, making it even easier to create polished, adaptive UIs that look great on all screen sizes. As the Android ecosystem continues to grow, users are engaging with apps on a wider variety of devices than ever before: from phones and foldables to tablets, connected displays, Chromebooks, and even car displays in parked mode.

WindowManager 1.5 focuses on providing better tools for this diverse device environment.

## What's new in WindowManager 1.5

This stable release introduces new breakpoints for very large screens, enhances the activity embedding API, and provides more flexibility for calculating window metrics.

## New window size classes: Large and Extra-large

The biggest update in 1.5 is the addition of two new width window size classes: Large and Extra-large.

Window size classes are our official, opinionated set of viewport breakpoints that help you design and develop adaptive layouts. With 1.5, we're extending this guidance for screens that go beyond typical tablets.

Here are the new width breakpoints:

- **Large:** For widths between 1200dp and 1600dp
- **Extra-large:** For widths ≥1600dp

![window_size_classes_width.png](https://developer.android.com/static/blog/assets/window_size_classes_width_99888c6d9f_Z1z4M9.webp)

*The different window size classes based on display width. *

### Why are these important?

Starting with Android 16 QPR1 Beta 2, Android supports [connected displays](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-connected-displays), enabling users to attach an external display to their device and transform it into a desktop-like tool with a large screen.
![ADB_5350_asset.gif](https://developer.android.com/static/blog/assets/ADB_5350_asset_b3a38e5a7b_Z1HIJW5.webp)

*Phone connected to an external display, with a desktop session on the external display. *

With this new feature available, opinionated guidance to include bigger displays is crucial.

On these very large surfaces, simply scaling up a tablet's Expanded layout isn't always the best user experience. An email client, for example, might comfortably show two panes (a mailbox and a message) in the Expanded window size class. But on an Extra-large desktop monitor, the email client could elegantly display **three or even four panes**---perhaps a mailbox, a message list, the full message content, and a calendar/tasks panel, all at once.

By providing official breakpoints for very large display sizes, WindowManager 1.5 gives you a clear signal to introduce layouts specifically designed for a productive, information-dense desktop experience.

The window size classes can be calculated using [computeWindowSizeClass()](https://developer.android.com/reference/kotlin/androidx/window/core/layout/package-summary#(kotlin.collections.Set).computeWindowSizeClass(kotlin.Float,kotlin.Float)), which is an `androidx.window.core.layout` library extension function that extends the `Set<WindowSizeClass>` type.

To include the new window size classes in your project, simply call the function from the [WindowSizeClass.BREAKPOINTS_V2](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass#BREAKPOINTS_V2()) set instead of [WindowSizeClass.BREAKPOINTS_V1](https://developer.android.com/reference/androidx/window/core/layout/WindowSizeClass#BREAKPOINTS_V1()):

```
val currentWindowMetrics =

    WindowMetricsCalculator.getOrCreate()

    .computeCurrentWindowMetrics(LocalContext.current)


val sizeClass = WindowSizeClass.BREAKPOINTS_V2

    .computeWindowSizeClass(currentWindowMetrics)
```

<br />

Then apply the correct layout when you're sure your app has at least that much space:

```
if(sizeClass.isWidthAtLeastBreakpoint(

    WindowSizeClass.WIDTH_DP_LARGE_LOWER_BOUND)){

    ...

    // window is at least 1200 dp wide


}
```

## Adaptive libraries

The [Compose Material 3 Adaptive library](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) helps you create adaptive UIs that adapt themselves automatically according to the current window configurations like window size classes or device postures.

The good news is that the library is already up to date with the new breakpoints! Starting from [version 1.2](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive#compose_material3_adaptive_version_12_2) (now in Release Candidate stage), the default pane scaffold directive functions support Large and Extra-large window width size classes.

You only need to opt-in by declaring in your Gradle build file that you want to use the new breakpoints:

```
currentWindowAdaptiveInfo(

    supportLargeAndXLargeWidth = true)
```

## Additional improvements

- **Activity embedding --- auto-save and restore** : WindowManager can now automatically save and restore the state of your activity embedding splits. This helps preserve the user's layout across process recreation, leading to a more stable and consistent experience. Developers don't have to save and restore the state manually anymore, but they can simply opt-in auto by setting the [EmbeddingConfiguration#isAutoSaveEmbeddingState](https://developer.android.com/reference/kotlin/androidx/window/embedding/EmbeddingConfiguration#isAutoSaveEmbeddingState()) property.
- **Expanded WindowMetrics**: You can now calculate WindowMetrics from an Application context, not just an Activity context. This provides more flexibility for accessing window information from different parts of your app.

## How to get started

To start using the new Large and Extra-large size classes and other 1.5 features in your Android projects, update your app dependencies in *build.gradle.kts* to the latest stable version:

```
dependencies {
    implementation("androidx.window:window:1.5.0") 

    // or, if you're using the WindowManager testing library:

    testImplementation("androidx.window:window-testing:1.5.0")

}
```

WindowManager 1.5 is another step forward for creating [fully adaptive apps](https://developer.android.com/adaptive-apps) that run across Android form factors. Check out the [official release notes](https://developer.android.com/jetpack/androidx/releases/window#version_15_2) for a complete list of changes and bug fixes.

Happy coding!

###### Written by:

-

  ## [Francesco Romano](https://developer.android.com/blog/authors/francesco-romano)

  ###### Developer Relations Engineer, Android

  [read_more
  View profile](https://developer.android.com/blog/authors/francesco-romano) ![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp) ![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/unnamed_fd9e15f738_1EHxqW.webp)](https://developer.android.com/blog/authors/francesco-romano) 03 Mar 2026 03 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Connected_34a0ae66a4_1A0pVS.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android devices extend seamlessly to connected displays](https://developer.android.com/blog/posts/android-devices-extend-seamlessly-to-connected-displays)

  [arrow_forward](https://developer.android.com/blog/posts/android-devices-extend-seamlessly-to-connected-displays) We are excited to announce a major milestone in bringing mobile and desktop computing closer together on Android: connected display support has reached general availability with the Android 16 QPR3 release!

  ###### [Francesco Romano](https://developer.android.com/blog/authors/francesco-romano) •
  7 min read

- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)