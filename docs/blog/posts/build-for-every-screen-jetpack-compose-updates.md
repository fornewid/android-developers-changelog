---
title: https://developer.android.com/blog/posts/build-for-every-screen-jetpack-compose-updates
url: https://developer.android.com/blog/posts/build-for-every-screen-jetpack-compose-updates
source: md.txt
---

[Events \& Programs](https://developer.android.com/blog/categories/events-and-programs)

# Build for every screen with the latest Jetpack Compose updates from Android Developer Summit

3 min read ![](https://developer.android.com/static/blog/assets/ADS_Compose_blog_1_9a0f711253_Z2jewd5.webp) 04 Nov 2026 [![View Rebecca Gutteridge's profile](https://developer.android.com/static/blog/assets/unnamed_28_42b5e825ea_1MlfGM.webp)](https://developer.android.com/blog/authors/rebecca-gutteridge) [Rebecca Gutteridge](https://developer.android.com/blog/authors/rebecca-gutteridge) Developer Relations Manager The Android ecosystem is a multi-device reality that spans phones, foldables, tablets, wearables, in-car displays, XR, and Googlebook. In this landscape, [adaptive development](https://developer.android.com/adaptive-apps) is foundational to reaching users wherever they are.

[Jetpack Compose](https://developer.android.com/develop/ui/compose/first) is the standard for building all UI across Android. Moving beyond the legacy View system gives you a single, unified development target that eliminates the friction of maintaining fragmented codebases across different form factors. But building adaptive layouts is only half the picture. When screens fold, windows resize, or apps transition across form factors, traditional layout assumptions may break down, and it is easy for apps to lose state or feel disjointed.

At the [Android Developer Summit,](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development) we shared how we are advancing app foundations across both UI and architecture by bringing Compose deeper into your data layer with [Jetpack AppState](https://developer.android.com/topic/libraries/architecture/appstate), while giving you adaptive building blocks like [FlexBox](https://developer.android.com/develop/adaptive-apps/guides/flexbox) and [Grid](http://g/), and agent-ready tooling to scale across screens every screen.

Check out some highlights of our recent announcements below or also head to our [Android Developer site](https://developer.android.com/events/dev-summit) to catch over 50 on-demand sessions, including best practices for app foundations.

### **Advancing core foundations and bringing Compose beyond the UI**

The upcoming Compose 1.13 stable release is expanding the toolkit with built-in support for adaptive layouts through Grid and Flexbox and new functionality like Progressive Blur and Formatted Text. To see the latest features with Graphics like mesh gradients and progressive blurs without sacrificing battery life or frame rates, watch[Elevate your apps with the latest graphics features in Jetpack Compose and Android.](https://youtu.be/TirZPDPV8Dw?si=fO6HQc8XtTdFt0tg)
[Video](https://www.youtube.com/watch?v=TirZPDPV8Dw)

Alongside visual rendering, Compose text editing now features a completely rewritten `BasicTextField` with a buffer-driven architecture and `TextFieldState`, eliminating IME race conditions and supporting rich text formatted editing mechanics. Watch[**Building reliable text editing experiences in Compose,](https://youtu.be/1DvjkRYGs2g?si=6nAqcLrfabpIdLIU) to learn more about this shift.

As you introduce these rich visual and interactive experiences, maintaining smooth frame rates and low startup latency is critical. Check out [Outperform yourself in Compose](https://youtu.be/t5ujT_o8qj0?si=ACMj9McGgt4sBYIc) to explore how to profile with Perfetto and recomposition tracing, identify costly anti-patterns, and keep your UI running smoothly.
[Video](https://www.youtube.com/watch?v=t5ujT_o8qj0)

Compose is also expanding into the architecture layer with [Jetpack AppState](https://developer.android.com/topic/libraries/architecture/appstate), now in alpha. `AppState` brings Compose's snapshot system into your app's architecture: `Transform` lets you derive reactive state from State and Flow inputs using automatic read tracking and plain Kotlin control flow, while `StateStore` gives you a keyed container to share observable state across activities, background services, widgets, and App Functions---with optional `DataStore` persistence. Watch [Taking Compose State Beyond the UI with Jetpack AppState](https://youtu.be/69QYEXymfVo?si=OZ7FRL6lHrrDxF5v)to see how moving Compose state up your stack simplifies complex state pipelines and keeps every surface of your app in sync.
[Video](https://www.youtube.com/watch?v=69QYEXymfVo)

### **Designing robust navigation and input systems for across form factors**

As apps grow more modular, navigation and user input need to stay predictable across every entry point and screen size. With version 1.2, [Jetpack Navigation 3](https://developer.android.com/guide/navigation/navigation-3) brings built-in, type-safe deep linking to its developer-owned back stack. Using Kotlin Serialization, you can map incoming URIs and intents directly to strongly typed navigation keys, customize how complex arguments are parsed, and lazily build synthetic back stacks so back navigation always feels natural. To see these APIs in action, check out [Building type-safe deep links with Jetpack Navigation 3.](https://youtu.be/cgmY14gf4zg?si=V_2LnP8wF7PCnzR8)
[Video](https://www.youtube.com/watch?v=cgmY14gf4zg)

Input handling has also evolved to support multi-modal interactions across devices. Compose's layered input system extends seamlessly beyond touch to support trackpads, mice, and physical controls. To see how to manage pointer lifecycles, hover states, and hardware events across form factors, watch [Scaling input interactions beyond the touchscreen with Jetpack Compose.](https://youtu.be/iztM_PgoCjw?si=q9R1_4QodBvQofKG)

### **Scaling interfaces across large screens, desktop, and beyond**

When moving across foldables, tablets, and laptops, interfaces must adapt naturally rather than simply stretching content to fill larger displays. Building adaptively with Compose development combines Navigation 3, `WindowManager`, and agentic workflows to help you refactor mobile layouts into responsive multi-pane experiences with minimal manual overhead. For developers looking to take their existing layouts further,[Scale your app for every screen with Compose](https://youtu.be/SGTkTKX7qq4?si=zkT0oYk_zahYNYan) walks through these multi-pane architecture patterns and demonstrates how to optimize navigation flows as window sizes change.
[Video](https://www.youtube.com/watch?v=SGTkTKX7qq4)

Expanding beyond mobile form factors also unlocks new opportunities like with Googlebook. Building desktop-class experiences requires physical peripheral support, windowing environments and more. In [Inside the first wave on Googlebook with Notability and Logitech,](https://youtu.be/aZjbDY3UXws?si=NQNxceLeOrBOXCng)early partners share practical engineering strategies on optimizing for pointer interactions, external hardware, and desktop-grade workflows.

### **Get started with our Android skills**

To help you implement these patterns even faster, you can leverage [Android skills](https://developer.android.com/tools/agents/android-skills) to help your coding agents. Whether you use Gemini in Android Studio or run the [Android CLI](https://developer.android.com/tools/agents)with other agents, these skills handle the heavy lifting for you and be compliant with the [Adaptive Quality Guidelines.](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality)For Compose we currently have:

- The updated [Adaptive skill](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) helps agents transform compact screens into responsive multi-pane layouts and handle state and configuration change. It now adds foldable and desktop support, automatically handling windowing, keyboard shortcuts, tooltips, and trackpad hover states.
- New [Compose performance](https://github.com/android/skills/blob/main/jetpack-compose/jetpack-compose-performance/SKILL.md) skill to help optimize your codebase
- [XML to Compose migration](https://github.com/android/skills/blob/main/jetpack-compose/migration/migrate-xml-views-to-jetpack-compose/SKILL.md) skill
- New [Ink](https://github.com/android/skills/tree/main/jetpack-compose/ink) skill

Beyond core architecture and adaptive layouts, you can explore technical deep dives covering Media3 playback, CameraX pipelines, in-car experiences, rich graphics, and lessons from migrating Google Play to Compose at scale. Check out the full collection of technical walkthroughs in the[Android Developer Summit App Foundations session playlist](https://goo.gle/ADS26-Apps-Foundation) to explore the architectures, code walkthroughs, and practical guidance.
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Rebecca Gutteridge](https://developer.android.com/blog/authors/rebecca-gutteridge)

  ###### Developer Relations Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/rebecca-gutteridge) ![View Rebecca Gutteridge's profile](https://developer.android.com/static/blog/assets/unnamed_28_42b5e825ea_1MlfGM.webp) ![View Rebecca Gutteridge's profile](https://developer.android.com/static/blog/assets/unnamed_28_42b5e825ea_1MlfGM.webp)
Continue reading
- [![View Adarsh Fernando's profile](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_Z1Axs64.webp)](https://developer.android.com/blog/authors/adarsh-fernando) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/ABL_146_ADS_Spotlight_Tools_and_Performance_47f52bd6b1_Zi3DUW.webp) [Events \& Programs](https://developer.android.com/blog/categories/events-and-programs)

  ## [What's new in Android developer tools and performance at Android Dev Summit](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance)

  [arrow_forward](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance) This year at Android Dev Summit we shared how Android's developer tools are evolving to help you be more productive alongside your agents.
  [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando) • 10 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp) [Events \& Programs](https://developer.android.com/blog/categories/events-and-programs)

  ## [Build for the future with the Android XR Developer Catalyst Program --- Apply now!](https://developer.android.com/blog/posts/build-for-the-future-with-the-android-xr-developer-catalyst-program-apply-now)

  [arrow_forward](https://developer.android.com/blog/posts/build-for-the-future-with-the-android-xr-developer-catalyst-program-apply-now) We're opening applications for the Android XR Developer Catalyst Program, a dedicated initiative to accelerate the development of Android XR apps ready to launch within the next year.
  1 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#intelligent eyewear](https://developer.android.com/blog/topics/intelligent-eyewear)
  - [#Wired XR glasses](https://developer.android.com/blog/topics/wired-xr-glasses)
  - +1 ↩
- 14 Apr 2026 14 Apr 2026 ![](https://developer.android.com/static/blog/assets/Blog_banner_Dark_2000x1000_B_c6418d3a5c_Z20LEeM.webp) [Events \& Programs](https://developer.android.com/blog/categories/events-and-programs)

  ## [Get ready for Google I/O: Livestream schedule revealed](https://developer.android.com/blog/posts/get-ready-for-google-io-livestream-schedule-revealed)

  [arrow_forward](https://developer.android.com/blog/posts/get-ready-for-google-io-livestream-schedule-revealed) The Google I/O schedule is here!
  1 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Generative AI](https://developer.android.com/blog/topics/generative-ai)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)