---
title: https://developer.android.com/blog/posts/google-i-o-2025-build-adaptive-android-apps-that-shine-across-form-factors
url: https://developer.android.com/blog/posts/google-i-o-2025-build-adaptive-android-apps-that-shine-across-form-factors
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Google I/O 2025: Build adaptive Android apps that shine across form factors

###### 5-min read

![](https://developer.android.com/static/blog/assets/yt_adaptive_b9097334d4_Z1poFG.webp) 20 May 2025 [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) [##### Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

###### Senior Product Manager

[Video](https://www.youtube.com/watch?v=15oPNK1W0Tw)

If your app isn't built to adapt, you're missing out on the opportunity to reach a giant swath of users across 500 million devices! At Google I/O this year, we are exploring how adaptive development isn't just a good idea, but essential to building apps that shine across the expanding Android device ecosystem. This is your guide to meeting users wherever they are, with experiences that are perfectly tailored to their needs.

## The advantage of building adaptive

In today's multi-device world, users expect their favorite applications to work flawlessly and intuitively, whether they're on a smartphone, tablet, or Chromebook. This expectation for seamless experiences isn't just about convenience; it's an important factor for user engagement and retention.

For example, entertainment apps (including Prime Video, Netflix, and Hulu) users on both phone and tablet spend almost 200% more time in-app (nearly 3x engagement) than phone-only users in the US\*.

[Peacock, NBCUniversal's streaming service](https://android-developers.googleblog.com/2025/05/peacock-optimizes-streaming-jetpack-compose.html) has seen a trend of users moving between mobile and large screens and building adaptively enables a single build to work across the different form factors.

*"This allows Peacock to have more time to innovate faster and deliver more value to its customers."*  
**-- Diego Valente, Head of Mobile, Peacock and Global Streaming**

Adaptive Android development offers the strategic solution, enabling apps to perform effectively across an expanding array of devices and contexts through intelligent design choices that emphasize code reuse and scalability. With Android's continuous growth into new form factors and upcoming enhancements such as desktop windowing and connected displays in Android 16, an app's ability to seamlessly adapt to different screen sizes is becoming increasingly crucial for retaining users and staying competitive.

Beyond direct user benefits, designing adaptively also translates to increased visibility. The Google Play Store actively helps promote developers whose apps excel on different form factors. If your application delivers a great experience on tablets or is excellent on ChromeOS, users on those devices will have an easier time discovering your app. This creates a win-win situation: better quality apps for users and a broader audience for you.
![android-adaptive-google-io.png](https://developer.android.com/static/blog/assets/android_adaptive_google_io_c3dae35526_ZxA8v0.webp)

## Latest in adaptive Android development from Google I/O

To help you more effectively build compelling adaptive experiences, we shared several key updates at I/O this year.

### Build for the expanding Android device ecosystem

Your mobile apps can now reach users beyond phones on over **500 million** active devices, including foldables, tablets, Chromebooks, and even compatible cars, with minimal changes. Android 16 introduces significant advancements in desktop windowing for a true desktop-like experience on large screens and when devices are connected to external displays. And, Android XR is opening a new dimension, allowing your existing mobile apps to be available in immersive virtual environments.

### The mindset shift to Adaptive

With the expanding Android device ecosystem, adaptive app development is a fundamental strategy. It's about how the same mobile app runs well across phones, foldables, tablets, Chromebooks, connected displays, XR, and cars, laying a strong foundation for future devices and differentiating for specific form factors. You don't need to rebuild your app for each form factor; but rather make small, iterative changes, as needed, when needed. Embracing this adaptive mindset today isn't just about keeping pace; it's about leading the charge in delivering exceptional user experiences across the entire Android ecosystem.
![adaptive-collage-google-io.png](https://developer.android.com/static/blog/assets/adaptive_collage_google_io_c5c1dfcb7e_1Dl49g.webp)

### Leverage powerful tools and libraries to build adaptive apps:

- [**Compose Adaptive Layouts library**](https://developer.android.com/develop/ui/compose/build-adaptive-apps#compose_material_3_adaptive): This library makes adaptive development easier by allowing your app code to fit into canonical layout patterns like list-detail and supporting pane, that automatically reflow as your app is resized, flipped or folded. In the 1.1 release, we introduced pane expansion, allowing users to resize panes. The Socialite demo app showcased how one codebase using this library can adapt across six form factors. New adaptation strategies like "Levitate" (elevating a pane, e.g., into a dialog or bottom sheet) and "Reflow" (reorganizing panes on the same level) were also announced in 1.2 (alpha). For XR, component overrides can automatically spatialize UI elements.
- [**Jetpack Navigation 3 (Alpha)**](http://goo.gle/nav3): This new navigation library simplifies defining user journeys across screens with less boilerplate code, especially for multi-pane layouts in Compose. It helps handle scenarios where list and detail panes might be separate destinations on smaller screens but shown together on larger ones. Check out the new Jetpack Navigation library in alpha.
- [**Jetpack Compose input enhancements**](https://developer.android.com/develop/ui/compose/touch-input): Compose's layered architecture, strong input support, and single location for layout logic simplify creating adaptive UIs. Upcoming in Compose 1.9 are right-click context menus and enhanced trackpad/mouse functionality.
- [**Window Size Classes**](https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes): Use window size classes for top-level layout decisions. AndroidX.window 1.5 introduces two new width size classes -- "large" (1200dp to 1600dp) and "extra-large" (1600dp and larger) -- providing more granular breakpoints for large screens. This helps in deciding when to expand navigation rails or show three panes of content. Support for these new breakpoints was also announced in the Compose adaptive layouts library 1.2 alpha, along with [design guidance](https://m3.material.io/foundations/layout/applying-layout/window-size-classes).
- [**Compose previews**](https://developer.android.com/develop/ui/compose/tooling/previews): Get quick feedback by visualizing your layouts across a wide variety of screen sizes and aspect ratios. You can also specify different devices by name to preview your UI on their respective sizes and with their inset values.
- [**Testing adaptive layouts**](https://developer.android.com/training/testing/different-screens): Validating your adaptive layouts is crucial and Android Studio offers various tools for testing -- including previews for different sizes and aspect ratios, a resizable emulator to test across different screen sizes with a single AVD, screenshot tests, and instrumental behavior tests. And with Journeys with Gemini in Android Studio, you can define tests using natural language for even more robust testing across different window sizes.

### Ensuring app availability across devices

Avoid [unnecessarily declaring required features](https://android-developers.googleblog.com/2023/12/increase-your-apps-availability-across-device-types.html) (like specific cameras or GPS) in your manifest, as this can prevent your app from appearing in the Play Store on devices that lack those specific hardware components but could otherwise run your app perfectly.

### Handling different input methods

Remember to [handle various input methods](https://developer.android.com/develop/ui/compose/touch-input/input-compatibility-on-large-screens) like touch, keyboard, and mouse, especially with Chromebook detachables and connected displays.

### Prepare for orientation and resizability API changes in Android 16

[Beginning in Android 16](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html), for apps targeting SDK 36, manifest and runtime restrictions on orientation, resizability, and aspect ratio will be ignored on displays that are at least 600dp in both dimensions. To meet user expectations, your apps will need layouts that work for both portrait and landscape windows, and support resizing at runtime. There's a temporary opt-out manifest flag at both the application and activity level to delay these changes until targetSdk 37, and these changes currently do not apply to apps categorized as "Games". Learn more about these [API changes](https://developer.android.com/about/versions/16/behavior-changes-16#adaptive-layouts).

### Adaptive considerations for games

[Games need to be adaptive too](https://developer.android.com/games/develop/multiplatform/overview) and Unity 6 will add enhanced support for configuration handling, including APIs for screenshots, aspect ratio, and density. Success stories like Asphalt Legends Unite show significant user retention increases on foldables after implementing adaptive features.
![adaptive-android-examples-form-factors-banner.png](https://developer.android.com/static/blog/assets/adaptive_android_examples_form_factors_banner_7b4f2212ac_Z2slLqR.webp)

## Start building adaptive today

Now is the time to elevate your Android apps, making them intuitively responsive across form factors. With the latest tools and updates we're introducing, you have the power to build experiences that seamlessly flow across all devices, from foldables to cars and beyond. Implementing these strategies will allow you to expand your reach and delight users across the Android ecosystem.

Get inspired by the "[Adaptive Android development makes your app shine across devices](https://youtu.be/15oPNK1W0Tw)" talk, and explore all the resources you'll need to start your journey at [developer.android.com/adaptive-apps](http://developer.android.com/adaptive-apps)!

Explore this announcement and all Google I/O 2025 updates on [io.google](https://io.google/2025/?utm_source=blogpost&utm_medium=pr&utm_campaign=event&utm_content) starting May 22.

<br />

\**Source: internal Google data*

###### Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)

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