---
title: https://developer.android.com/blog/posts/jetpack-navigation-3-is-stable
url: https://developer.android.com/blog/posts/jetpack-navigation-3-is-stable
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Jetpack Navigation 3 is stable

###### 3-min read

![](https://developer.android.com/static/blog/assets/jetpack_navigation_d1257f9ca2_Z1dRNOI.webp) 19 Nov 2025 [![](https://developer.android.com/static/blog/assets/don_bccb8c3f75_1ufD8A.webp)](https://developer.android.com/blog/authors/don-turner) [##### Don Turner](https://developer.android.com/blog/authors/don-turner)

###### Developer Relations Engineer

[Jetpack Navigation 3](https://developer.android.com/guide/navigation/navigation-3) version 1.0 is stable 🎉. Go ahead and use it in your production apps today. JetBrains are [already using it in their KotlinConf app](https://github.com/JetBrains/kotlinconf-app/pull/504).

Navigation 3 is a new navigation library built from the ground up to embrace Jetpack Compose [state](https://developer.android.com/develop/ui/compose/state#state-in-composables). It gives you full control over your back stack, helps you retain navigation state, and allows you to easily create adaptive layouts (like list-detail). [There's even a cross-platform version from JetBrains](https://kotlinlang.org/docs/multiplatform/whats-new-compose-110.html#support-for-navigation-3).

**Why a new library?**

The original Jetpack Navigation library (now Nav2) was designed 7 years ago and, while it serves its original goals well and has been improved iteratively, the way apps are now built has fundamentally changed.

Reactive programming with a declarative UI is now the norm. Nav3 embraces this approach. For example, NavDisplay (the Nav3 UI component that [displays your screens](https://developer.android.com/guide/navigation/navigation-3/basics#display-back)) simply observes a list of keys (each one representing a screen) backed by Compose state and updates its UI when that list changes.
![nav-display.png](https://developer.android.com/static/blog/assets/nav_display_6244a3347c_POUFz.webp)

Nav2 can also make it difficult to have a [single source of truth](https://developer.android.com/topic/architecture#single-source-of-truth) for your navigation state because it has its own internal state. With Nav3, you supply your own state, which gives you complete control.

Lastly, you asked for more flexibility and customizability. Rather than having a single, monolithic API, Nav3 provides smaller, decoupled APIs (or "building blocks") that can be combined together to create complex functionality. Nav3 itself uses these building blocks to provide sensible defaults for well-defined navigation use cases.

This approach allows you to:

- [Customize screen animations](https://developer.android.com/guide/navigation/navigation-3/animate-destinations) at both a global and individual level
- Display multiple panes at the same time, and [create flexible layouts using the Scenes API](https://developer.android.com/guide/navigation/navigation-3/custom-layouts)
- Easily replace Nav3 components with your own implementations if you want custom behavior

Read more about its design and features in the [launch blog](https://android-developers.googleblog.com/2025/05/announcing-jetpack-navigation-3-for-compose.html).

**Migrating from Navigation 2**

If you're already using Nav2, specifically [Navigation Compose](https://developer.android.com/develop/ui/compose/navigation), you should consider migrating to Nav3. To assist you with this, there is a [migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide). The key steps are:

1. Add the [navigation 3 dependencies](https://developer.android.com/guide/navigation/navigation-3/get-started).
2. Update your navigation routes to implement NavKey. Your routes don't have to implement this interface to use Nav3, but if they do, you can take advantage of Nav3's rememberNavBackStack function to create a persistent back stack.
3. Create classes to hold and modify your navigation state - this is where your back stacks are held.
4. Replace NavController with these classes.
5. Move your destinations from NavHost's NavGraph into an entryProvider.
6. Replace NavHost with NavDisplay.

*Experimenting with AI agent migration*

You may want to experiment with using an AI agent to read the migration guide and perform the steps on your project. To try this with [Gemini in Android Studio's Agent Mode](https://developer.android.com/studio/gemini/agent-mode):

- Save [this markdown version of the guide](https://raw.githubusercontent.com/android/nav3-recipes/refs/heads/main/docs/migration-guide.md) into your project.
- Paste this prompt to the agent (but don't hit enter): "Migrate this project to Navigation 3 using ".
- Type @migration-guide.md - this will supply the guide as context to the agent.

As always, make sure you carefully review the changes made by the AI agent - it can make mistakes!

We'd love to hear how you or your agent performed, please [send your feedback here](https://issuetracker.google.com/issues/new?component=1750212&template=2102223&title=%5BMigration%5D).

**Tasty navigation recipes for common scenarios**

For common but nuanced use cases, we have [a recipes repository](https://github.com/android/nav3-recipes). This shows how to combine the Nav3 APIs in a particular way, allowing you to choose or modify the recipe to your particular needs. If a recipe turns out to be popular, we'll consider "graduating" the non-nuanced parts of it into the core Nav3 library or add-on libraries.
![code-recipes.png](https://developer.android.com/static/blog/assets/code_recipes_fba1048f97_28Geau.webp)

There are currently 19 recipes, including for:

- [Multiple back stacks](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/multiplestacks)
- [Modularization and dependency injection](https://github.com/android/nav3-recipes/tree/main/app/src/main/java/com/example/nav3recipes/modular/hilt)
- [Passing navigation arguments to ViewModels](https://github.com/android/nav3-recipes?tab=readme-ov-file#passing-navigation-arguments-to-viewmodels) (including using Koin)
- [Returning results from screens](https://github.com/android/nav3-recipes?tab=readme-ov-file#returning-results) by events and by shared state

We're [currently working on a deeplinks recipe](https://github.com/android/nav3-recipes/pull/97), plus a [Koin integration](https://github.com/android/nav3-recipes/pull/118), and have plenty of others planned. An [engineer from JetBrains](https://github.com/terrakok) has also published a [Compose Multiplatform version of the recipes](https://github.com/terrakok/nav3-recipes).

If you have a common use case that you'd like to see a recipe for, please [file a recipe request](https://github.com/android/nav3-recipes/issues/new?title=%5BRecipe+request%5D).

**Summary**

To get started with Nav3, check out [the docs](https://developer.android.com/guide/navigation/navigation-3) and [the recipes](https://github.com/android/nav3-recipes). Plus, keep an eye out for a whole week of technical content including:

- A deep dive video on the API covering modularization, animations and adaptive layouts.
- A live Ask Me Anything (AMA) with the engineers who built Nav3.

Nav3 Spotlight Week starts Dec 1st 2025.

<br />

As always, if you find any issues, please [file them here](https://issuetracker.google.com/issues/new?component=1750212&template=2102223).
- [#Nav3](https://developer.android.com/blog/topics/nav3)
- [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)

###### Written by:

-

  ## [Don Turner](https://developer.android.com/blog/authors/don-turner)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/don-turner) ![](https://developer.android.com/static/blog/assets/don_bccb8c3f75_1ufD8A.webp) ![](https://developer.android.com/static/blog/assets/don_bccb8c3f75_1ufD8A.webp)

## Continue reading

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

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)