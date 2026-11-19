---
title: https://developer.android.com/blog/posts/android-ui-development-is-compose-first
url: https://developer.android.com/blog/posts/android-ui-development-is-compose-first
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Android UI Development is Compose First

2 min read ![](https://developer.android.com/static/blog/assets/Compose_first_Meta_04fd0498ba_21k6io.webp) 19 May 2026 [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher.md.txt) [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher.md.txt) Product Manager In the almost-5-years since Jetpack Compose [launched](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html), we've invested in bringing you all the features, performance and tools that you need to build amazing UIs across the variety of Android devices. Compose helps you to build beautiful, adaptive UIs that meet the demands of modern UI design.

- **Rich feature set:**With a powerful library of layouts, input, graphics, animation APIs, and the latest Material Design components, Compose empowers you to build anything.
- **Highly performant:**Out of the box, Compose offers native performance, delivering a delightful experience to your users.
- **Adaptive:**Compose offers the easiest way to build adaptive apps that work across the range of Android form factors.
- **Productive:**With powerful tools like Previews and Live Edit and the full expressiveness of Kotlin, teams tell us that they move much faster when building with Jetpack Compose, reducing the time to market.

Compose has matured into the standard for Android UI development---we believe that **all Android UI should be built with Compose** ; we call this going [Compose First](http://developer.android.com/develop/ui/compose/first.md.txt). From today, we'll provide all APIs, libraries, tools and guidance in Compose. We now consider the View components that Compose replaces (components in the android.widget package) to be in **maintenance mode**. We have no plans to deprecate or remove View components and will continue to support them with critical bug fixes, but they will receive no new features.

### View-based Jetpack Libraries

The same goes for View based libraries like Fragments, RecyclerView or Viewpager --- we consider them complete and will only publish critical bugfixes. For a complete list of libraries now in maintenance mode, [see here](http://developer.android.com/develop/ui/compose/first.md.txt).

### Tools

Any new Android Studio UI tools will be built for Jetpack Compose only. Existing view-based tools (such as the Navigation Editor and Layout Editor) are now in maintenance mode and will not receive new features.

### Guidance

Documentation, codelabs, and samples will focus on building UI with Jetpack Compose. You can still find Views-specific documentation linked from pages that contain generic and Compose information, where relevant.

## Happy Composing

We recommend that you build all new features with Compose and convert existing features when you touch them to gain the many Compose benefits. Check out our [XML to Compose migration skill](https://github.com/android/skills) to help you convert existing layouts to Compose.

<br />

To learn about the latest Compose release, check out [What's new in the Jetpack Compose April '26 release](https://android-developers.googleblog.com/2026/04/jetpack-compose-april-2026-updates.html) blog and the [roadmap](https://developer.android.com/jetpack/androidx/compose-roadmap.md.txt) for what's planned ahead.

Thank you for all of the feature-requests and feedback that have helped shape Compose to become our recommended UI toolkit. As always, if you have any more [feedback](http://goo.gle/compose-feedback), let us know. Happy composing!
- [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
Written by:

-

  ## [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher.md.txt)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/nick-butcher) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp) ![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)
Continue reading
- [![View Meghan Mehta's profile](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z2r6wan.webp)](https://developer.android.com/blog/authors/meghan-mehta.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_812f851abd_WuQ5h.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in the Jetpack Compose November '26 release](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-compose-november-2026-release.md.txt) The Jetpack Compose November '26 release is stable! This release brings version 1.13 across core Compose modules (see the full BOM mapping), introducing updates to text, graphics, layouts, performance, and more---along with a few important deprecations and behavior changes to be aware of.
  [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta.md.txt) • 10 min read
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
- [![View Jan Kleinert's profile](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_va23A.webp)](https://developer.android.com/blog/authors/jan-kleinert.md.txt) 21 Sep 2026 21 Sep 2026 ![](https://developer.android.com/static/blog/assets/Games_for_car_Strapi_1_c55588726e_Z2cIhWx.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Bring your Android game to the car screen today](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/bring-your-android-game-to-the-car-screen-today.md.txt) Today, the games category for Android Auto and cars powered by Android Automotive OS with Google built-in is officially graduating from beta to general availability.
  [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert.md.txt) • 3 min read
  - [#Android Automotive OS](https://developer.android.com/blog/topics/android-automotive-os.md.txt)
  - [#Adaptive \& Differentiated](https://developer.android.com/blog/topics/adaptive-and-differentiated.md.txt)
  - [#Android Auto](https://developer.android.com/blog/topics/android-auto.md.txt)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher.md.txt) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_ZrjgNw.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release.md.txt) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher.md.txt) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)