---
title: https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem
url: https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Adaptive development for the expanding Android ecosystem

4-min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_ZQaFMJ.webp) 19 May 2026 [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) Senior Product Manager, Android Developer Experience With the release of Android 17, we are transitioning into an [adaptive first development](https://developer.android.com/adaptive-apps) standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.

Now, with over **580 million large screen devices** in the hands of users, adaptive is no longer just a technical goal. It's a massive opportunity to reach highly engaged users. To thrive in this multi-device ecosystem, your app must be resilient, responsive, and ready for virtually any surface.

### The multi-device opportunity

The Android device universe is now a multi device reality. Users are buying into entire ecosystems, moving from handhelds to foldables, tablets, and cars. And the data is clear: users with multiple devices often spend more than users with only a phone.

- **Drive higher revenue:** Multi-device users spend **9x more** on average than phone only users. On foldables, that engagement multiplier can reach 14x. *(Source: Google Internal Data, 2026)*
- **Capture high-value segments:** Large-screen users (tablets, foldables, and Chromebooks) typically spend roughly **5x more** than phone-only users.

To help amplify your reach with these users, we've rolled out a new badge in Google Play. Apps meeting adaptive quality standards now earn an "Optimized for large screens" badge, making it easier for users to discover high quality experiences.
![image5.png](https://developer.android.com/static/blog/assets/image5_506f2d57fd_Z7e1im.webp)

### Latest in adaptive Android development from Google I/O

Android 17, new Jetpack updates and advanced tools help you build apps that feel native across diverse surfaces, from pocket-sized foldables to [Googlebooks](https://developer.android.com/googlebook).

**Adaptive by default: Android 17 updates**

In Android 16, we [introduced significant changes](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html) to orientation and resizability APIs to facilitate adaptive behavior, while providing a temporary opt-out to help you make the transition. Android 17 (API level 37) sets a new quality baseline by removing that developer opt-out for orientation and resizability restrictions on large screen devices (sw \> 600 dp). When you target API level 37, your app must be capable of adapting to a variety of display sizes. This helps your app deliver an experience that matches the users' expectations.
![image1.png](https://developer.android.com/static/blog/assets/image1_f0544ba938_1S4Wev.webp)

**Your app on even more surfaces**

In addition to your mobile app running on large screens devices including foldables, tablets, Chromebooks and XR, we are also expanding the Android surface area for your mobile apps:

- **Connected Displays:** Now in stable as of Android 16 QPR3, Connected Displays support enables supported Pixel and Samsung mobile devices to transform into a desktop environment via external display support.
- **Automotive \& TV:** With the [Car Ready Mobile Apps program](https://developer.android.com/training/cars/car-ready-mobile-apps) and enhanced [pointer support for Android TV](http://android-developers.googleblog.com/2026/05/increase-google-tv-app-discovery.html), your adaptive app can now benefit from engagement on the infotainment system and the living room with ease.

![image4.png](https://developer.android.com/static/blog/assets/image4_87419e4a30_2v7wPp.webp)

**Googlebook: Evolving desktop computing**

Talking about more surfaces, we're evolving our work in the desktop space with Googlebook, the next generation of ChromeOS. Built with parts of the Android stack, we are enabling your apps to achieve a "laptop-class" feel with native level performance.

Building with adaptive principles today helps ensure your app is ready for this new generation of high performance hardware.

To help you prepare for this new generation of devices, we've released comprehensive new documentation including comprehensive [design guidance](https://developer.android.com/design/ui/desktop) and [developer guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/desktop). Built on the principles of adaptive, these guidelines offer a playbook for transitioning your mobile apps to offer a premium desktop class experience.

Try out the new Desktop Emulator, available now in the Android Studio Canary to get started today.
![google_aluminium_hype_film_hp_sh18019_main_design_v04_00068 (1).png](https://developer.android.com/static/blog/assets/google_aluminium_hype_film_hp_sh18019_main_design_v04_00068_1_5add00913d_2evn14.webp)

**Beyond layouts: non-touch input**

Adaptive app quality goes beyond window dimensions, including handling non-touch input paradigms e.g. keyboard, trackpad, mouse, stylus that are primary input methods on large screens.

- **Trackpad support:** [Compose 1.11](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) now brings trackpad support on par with mouse, and provides new APIs to automate non-touch input testing including `TrackpadInjectionScope` and `performTrackpadInput`.
- **Focus indicators:** Enhance accessibility with built-in support for standard focus rings in Compose.

**Building adaptive layouts with Jetpack Compose**

We are now [Compose first](https://goo.gle/Compose_IO26) and Jetpack Compose is our recommended way to build modern, adaptive UIs to help you manage layout complexity efficiently.

- **New layout primitives:** We're introducing [Grid](https://developer.android.com/develop/ui/compose/layouts/adaptive/grid) and [FlexBox](https://developer.android.com/develop/ui/compose/layouts/adaptive/flexbox) layouts, bringing powerful, CSS-inspired capabilities to Compose for both 1D and 2D layouts.
- **Navigation 3:** The [1.1 release](https://developer.android.com/jetpack/androidx/releases/navigation3) for compose-navigation3 introduces [Scene Decorators](https://developer.android.com/guide/navigation/navigation-3/scenes/scene-decorators), allowing you to wrap your screens with other content, such as bars, rails and dialogs.
- **MediaQuery API:** The new experimental [MediaQuery API](https://developer.android.com/reference/kotlin/androidx/compose/ui/mediaQuery.composable) provides observable device UI capabilities, such as window size and pointer precision, that allow you to adapt and optimize your app's UI for the current device configuration.
- **Styles API:** Dynamically evolve the visual properties of your app using the new state-based experimental [Styles API](https://developer.android.com/develop/ui/compose/styles).

![morph-to-tablet.gif](https://developer.android.com/static/blog/assets/morph_to_tablet_bce353ffb9_sf8cy.webp)

<br />

**AI-Powered developer tools**

Android Studio and [Android CLI](https://developer.android.com/tools/agents/android-cli) are evolving to help you architect adaptive apps faster than ever.

- **Android Skills:** These modular AI instructions are designed to assist any LLM through complex architectural tasks, including helping you with View-to-Compose migrations, implementing adaptive layouts, Navigation 2 to Navigation 3 transformation, and migrating off of legacy camera libraries to CameraX. Get started with these latest skills on the Android Skills [Github repo](https://github.com/android/skills) and [via Android CLI.](https://developer.android.com/tools/agents/android-cli#skills-add)
- **New Project Agent:** Available in Android Studio Panda 2, this agent initializes new projects with adaptive best practices by default.

![O26_315_PKLS_Adaptive development for the expanding Android ecosystem.png](https://developer.android.com/static/blog/assets/O26_315_PKLS_Adaptive_development_for_the_expanding_Android_ecosystem_081c6533be_2ejjaD.webp)

For developers working with cross-platform frameworks, we continue to provide full support for Web, Qt, and Unity. Whether you are building from scratch or modernizing a legacy codebase, these tools are designed to meet your users exactly where they are.

We're excited to see how you bring these new adaptive capabilities to your apps. By moving to an adaptive first approach, you're not just reaching more users but you're delivering the seamless, high quality experiences they expect across the entire Android device landscape.

Get started with [adaptive development](https://developer.android.com/adaptive-apps) and start shaping the future of your apps.

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
- [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
Written by:

-

  ## [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz)

  ###### Senior Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/fahd-imtiaz) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp) ![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz) 19 Dec 2025 19 Dec 2025 ![](https://developer.android.com/static/blog/assets/Android_adaptives_festivity_01_blog_f70d48134f_Z2lMDgd.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Goodbye Mobile Only, Hello Adaptive: Three essential updates from 2025 for building adaptive apps](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive)

  [arrow_forward](https://developer.android.com/blog/posts/goodbye-mobile-only-hello-adaptive) In 2025 the Android ecosystem has grown far beyond the phone. Today, developers have the opportunity to reach over 500 million active devices, including foldables, tablets, XR, Chromebooks, and compatible cars.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz) • 2 min read
  - [#Jetpack Navigation](https://developer.android.com/blog/topics/jetpack-navigation)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps)
  - [#Compose](https://developer.android.com/blog/topics/compose)
  - [#Android 16](https://developer.android.com/blog/topics/android-16)
  - +2 ↩
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) • 2 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![View Luke Hopkins's profile](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![View Ryan Bartley's profile](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.
  [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) • 4 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)