---
title: https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen
url: https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Eclipsa Video: HDR That Looks Right on Every Screen

2 min read ![](https://developer.android.com/static/blog/assets/Eclipsa_Video_V01_White_Strapi_10c5296e18_R3bTD.webp) 29 Jun 2026 [![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp)](https://developer.android.com/blog/authors/tibian-elsheikh)[![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp)](https://developer.android.com/blog/authors/jeffrey-jose) [Tibian Elsheikh](https://developer.android.com/blog/authors/tibian-elsheikh) \& [Jeffrey Jose](https://developer.android.com/blog/authors/jeffrey-jose) We've all been there: You're scrolling through your favorite social media feed in a dim room, and suddenly an HDR video pops up. It's so intensely bright that you have to squint, or maybe you find yourself turning down your screen brightness just to read the caption. Other times, a video that looks vibrant on your phone looks flat, dark, or washed out when you watch it on your living room TV.

While High Dynamic Range (HDR) technology was designed to make videos look richer and more lifelike, the lack of unified industry guidelines means that the exact same clip can render in unexpected and jarring ways depending on the display you're using.

To solve this, we're introducing Eclipsa Video---a new standard built to make your favorite videos look consistent, balanced, and comfortable on every screen. Eclipsa Video builds on the open [SMPTE ST 2094-50 specification](https://github.com/SMPTE/st2094-50), which Google developed in collaboration with Apple and NBCUniversal.
![Eclipsa_9-16_Transparent (2).gif](https://developer.android.com/static/blog/assets/Eclipsa_9_16_Transparent_2_7c4afb39db_1IHzLl.webp) Sudden brightness spikes during feed scrolling---fixed with Eclipsa Video.

### **More consistency, comfort, and creative control**

Eclipsa Video moves past individual display guesswork. Instead of leaving it up to your device to interpret a video's brightness on its own, our format carries precise guidelines that tell compatible displays exactly how to render the image.

Designed to scale with your hardware, Eclipsa Video provides three core benefits:

- **A consistent baseline:** Eclipsa Video introduces a shared rulebook for screens. It establishes a consistent benchmark for normal brightness---known as the **HDR reference white**. This ensures standard text, app interfaces, and standard-range colors remain vibrant and readable without causing uncomfortable screen glare.
- **Adaptive headroom:** Screens have different physical brightness limits, or "headroom." Eclipsa Video guides how displays handle highlights dynamically. Bright details remain brilliant on a premium television, while being scaled intelligently on a mobile screen to prevent sudden blinding transitions.
- **Preserved creative intent:** Rather than applying a single static setting to an entire video, Eclipsa Video carries adaptive, frame-by-frame instructions. Think of it as a set of digital notes from the creator traveling with the video, ensuring the exact colors, contrast, and mood they graded are preserved on your display.

![Eclpsa Blog post image-AlphaB.png](https://developer.android.com/static/blog/assets/Eclpsa_Blog_post_image_Alpha_B_cde0e1f2c6_1HyJ5A.webp) Eclipsa Video preserves true highlight detail on any screen you watch.

### **Built natively into Android 17**

Starting with **Android 17**, support for Eclipsa Video is built directly into the platform. This means a more comfortable, true-to-life HDR experience is coming natively to the phones, tablets, and TVs you rely on every day. The video you capture carries its creative intent with it, and the video you watch is shown exactly the way it was meant to be seen.

### **Guidelines for developers \& creators**

We're inviting the developer and creator ecosystem to help build a more reliable HDR environment:

- **Get started with implementation:** Learn how to configure playback and capture in your apps with our [official guide.](https://developer.android.com/media/platform/integrate-eclipsa-video)
- **ExoPlayer \& Media3 integration:** Standard playback handling built directly into [Jetpack Media3](https://developer.android.com/media/media3/exoplayer), allowing ExoPlayer to support Eclipsa Video metadata automatically with no additional player configuration.
- **Explore open source tools:** View and inspect [SMPTE ST 2094-50](https://github.com/SMPTE/st2094-50) metadata and dynamic gain curves in real time using [HDR Explorer](https://webmproject.github.io/hdr-explorer/).

### **What's next**

Eclipsa Video is rolling out now, and you'll see more apps and devices supporting it over time. Because it's an open standard, any app developer or hardware manufacturer can integrate it to elevate the viewing experience.

Try out the new tools in Android 17, explore the open-source metadata, and let us know what you think on our developer channels. We can't wait to see what you create.

#### **Notes \& Availability**

1. **Device Compatibility:** Eclipsa Video playback and capture are supported natively on devices running Android 17 (API level 37) and above with HDR displays passing Eclipsa Video Compliance tests.
2. **Developer Resources:** The[SMPTE ST 2094-50 Specification](https://github.com/SMPTE/st2094-50) is openly accessible for technical evaluation.
Written by:

-

  ## [Tibian Elsheikh](https://developer.android.com/blog/authors/tibian-elsheikh)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/tibian-elsheikh) ![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp) ![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp)
-

  ## [Jeffrey Jose](https://developer.android.com/blog/authors/jeffrey-jose)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/jeffrey-jose) ![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp) ![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp)
Continue reading
- [![View Blair Harmon's profile](https://developer.android.com/static/blog/assets/unnamed_16_ca18834db7_Z1URmUI.webp)](https://developer.android.com/blog/authors/blair-harmon) 19 Aug 2026 19 Aug 2026 ![](https://developer.android.com/static/blog/assets/ABL_116_Preparing_your_app_for_expanded_memory_limits_strapi_0aac62fa12_1hkk5a.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Preparing your app for broader memory limits](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits)

  [arrow_forward](https://developer.android.com/blog/posts/preparing-your-app-for-broader-memory-limits) A great user experience is central to Android's mission, and delivering on that promise requires keeping devices fast, responsive, and reliable.
  [Blair Harmon](https://developer.android.com/blog/authors/blair-harmon) • 2 min read
  - [#App Memory Limits](https://developer.android.com/blog/topics/app-memory-limits)
  - [#Android Vitals](https://developer.android.com/blog/topics/android-vitals)
  - [#Multi-Process Architecture](https://developer.android.com/blog/topics/multi-process-architecture)
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#Performance](https://developer.android.com/blog/topics/performance)
  - +3 ↩
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_Z1YdYO1.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Jetpack XR SDK core libraries reach beta: The next milestone for Android XR](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr) Since introducing the Android XR SDK, developers have transformed their ideas into innovative immersive experiences across headsets and wired XR glasses.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld), [Greg Underwood](https://developer.android.com/blog/authors/greg-underwood), [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen) • 2 min read
  - [#Jetpack XR SDK](https://developer.android.com/blog/topics/jetpack-xr-sdk)
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)