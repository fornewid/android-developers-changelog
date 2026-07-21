---
title: https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv
url: https://developer.android.com/blog/posts/increasing-app-discovery-and-engagement-on-google-tv
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Increasing app discovery and engagement on Google TV

4-min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_ZtW7eg.webp) 19 May 2026 [![View Paul Lammertsma's profile](https://developer.android.com/static/blog/assets/Paul_Lammertsma_2f7e1baf32_Z28iSTy.webp)](https://developer.android.com/blog/authors/paul-lammertsma) [Paul Lammertsma](https://developer.android.com/blog/authors/paul-lammertsma) Developer Relations Engineer, Android With over 300 million monthly active devices across Google TV and Android TV, it's clear that the living room is a massive, distinct platform for apps to accelerate growth. Today, we're excited to share Google TV features and developer tools designed to increase the discoverability of your content and prepare your app for future TV experiences.

### Drive discovery and engagement with Gemini

Last year, we brought our AI voice assistant, [Gemini](https://blog.google/products-and-platforms/platforms/google-tv/gemini-google-tv/), to our platform, so that people can easily find what to watch, learn something new on the big screen, and get everyday tasks done with just their voice.

Since launch, we've made [improvements](https://blog.google/products-and-platforms/platforms/google-tv/new-gemini-features-march-2026/) to how Gemini provides tailored responses to questions. Gemini shares a mix of visuals, videos, and text to help users find what they need, when they need it. For our streaming partners, Gemini is a helpful discovery engine---pulling from your app's metadata to surface your relevant content to viewers.

### Declare support for pointing modality

The TV experience that we once knew is changing. Gemini is changing the way we discover and stream content with voice, but how we use the remote is evolving, too.
![GTV Pointer Remote Demo_SHELL (1).gif](https://developer.android.com/static/blog/assets/GTV_Pointer_Remote_Demo_SHELL_1_0c03db4156_xvSkx.webp)

Pointer remotes bring motion-controlled input to the big screen, unlocking faster user navigation across the Google TV Home page and within content-heavy apps. To ensure your app is ready for this shift and provides a great experience for all users, now is the time to start thinking about pointing input. Here's how to get started:

#### 1. Adapt your TV app UI Library

You'll need support for hover states, scrollable containers, and cursor clicks to enable pointer remote interactions for your app on Google TV. While implementation varies by UI stack, Jetpack Compose streamlines this transition, as most core components handle these multi-modal interactions natively out of the box.

- **Hover state:** Every focusable element on your screen (buttons, movie posters, setting toggles) needs a clear visual feedback mechanism for a hover state. This is often subtler than a focus state but critical for feedback.
- **Scrollable containers:**Pointer remotes will also have a small circular touchpad for scrolling. Users can use this touchpad to scroll up or down, or left or right in your app. Your app will need to respond to touch events to scroll.
- **Cursor clicks:** Many TV apps today expect a simple D-pad OKAY button "click." With a pointer remote, a user may "click" on an element that's not the D-pad focus state, but is instead from a hovered state (similar to a mouse click).

#### 2. Test pointing interactions with a mouse today

To see how your app handles hover, scroll, and clicks, simply connect a bluetooth mouse or wired mouse to your Google TV. Keep in mind that a mouse has more precise control, since users are closer to the screen and typically rest the mouse in a stable position. Pointer remotes can often be less precise, since users are sometimes 10 feet away from the screen, making rough gestures with the remote from their couch. As a TV designer or developer, you can mitigate this lack of input precision by having larger hover targets for elements.

#### 3. Declare TV app support for pointer remotes on Google Play

Finally, tell Google Play that your TV app is designed to work with a pointer. This ensures that users with pointer remotes will be able to easily find, install, and interact with your app.

Within your AndroidManifest.xml, declare the meta-data tag, `android.software.leanback.supports_touch`. This tag informs the platform that your TV app "spatially supports touch," since pointer remotes simulate touch events from a distance.

***AndroidManifest.xml***

```xml
<manifest ...>
    <!-- Signal whether the app is adaptive or built just for TV –->
    <uses-feature android:name="android.software.leanback" android:required="true|false" />

    <!-- Ensure the app can be installed on conventional TVs –->
    <uses-feature android:name="android.hardware.touchscreen" android:required="false" />

    <!-- Signal whether the app supports pointer remotes –->
    <meta-data android:name="android.software.leanback.supports_touch" android:value="true|false"/>

    <application ...>
        ...
    </application>
</manifest>
```

***Tips:***

- The `android.software.leanback` feature declaration indicates that your app supports D-pad navigation and is intended for distribution only on TV devices via Google Play.
- The new software attribute of `android.software.leanback.supports_touch` declares that in addition to D-pad, you have ensured that your TV app works well for pointer/cursor experiences via mouse (of today) and pointer remotes (of future).
- If you haven't already, now is the time to adopt [Jetpack Compose](https://developer.android.com/compose). Hover, scroll, and clicks are common input modalities that are supported on various form factors, and building your app with an adaptive UI framework enables code reusability and reduced maintenance.

### Onboard the Engage SDK

The Engage SDK, formerly known as the Video Discovery API, optimizes Resumption, Entitlements, and Recommendations across all Google TV form factors to boost app discovery and engagement.

- **Resumption**: Partners can easily display a user's paused video within the 'Continue Watching' row from the Home page.
- **Entitlements**: The Engage SDK streamlines entitlement management, which matches app content to user eligibility. Users appreciate this because they can enjoy personalized recommendations without needing to manually update all their subscription details. This allows partners to connect with users across multiple discovery points on Google TV.
- **Recommendations**: The Engage SDK even highlights personalized recommendations based on content that users watched inside apps.

It's a great time to start onboarding the Engage SDK now, since the legacy Watch Next API, which has been powering your continue watching 1.0 experience, will lose support in the 2nd half of 2027. To get started, head to [goo.gle/engage-tv](https://goo.gle/engage-tv) to learn more.

We're excited to see how our latest Gemini experience and developer tools will optimize your discovery and drive user engagement on our platform.

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Gemini features](https://developer.android.com/blog/topics/gemini-features)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [#Engage SDK](https://developer.android.com/blog/topics/engage-sdk)
Written by:

-

  ## [Paul Lammertsma](https://developer.android.com/blog/authors/paul-lammertsma)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/paul-lammertsma) ![View Paul Lammertsma's profile](https://developer.android.com/static/blog/assets/Paul_Lammertsma_2f7e1baf32_Z28iSTy.webp) ![View Paul Lammertsma's profile](https://developer.android.com/static/blog/assets/Paul_Lammertsma_2f7e1baf32_Z28iSTy.webp)
Continue reading
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
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)