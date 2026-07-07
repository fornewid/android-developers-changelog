---
title: https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen
url: https://developer.android.com/blog/posts/eclipsa-video-hdr-that-looks-right-on-every-screen
source: md.txt
---

# Eclipsa Video: HDR That Looks Right on Every Screen

2-min read ![](https://developer.android.com/static/blog/assets/Eclipsa_Video_V01_White_Strapi_10c5296e18_R3bTD.webp) 29 Jun 2026 [![View Tibian Elsheikh's profile](https://developer.android.com/static/blog/assets/unnamed_7_643878a583_gdebU.webp)](https://developer.android.com/blog/authors/tibian-elsheikh)[![View Jeffrey Jose's profile](https://developer.android.com/static/blog/assets/unnamed_8_3d27b8b0cb_ZRl3Ng.webp)](https://developer.android.com/blog/authors/jeffrey-jose) [Tibian Elsheikh](https://developer.android.com/blog/authors/tibian-elsheikh) \& [Jeffrey Jose](https://developer.android.com/blog/authors/jeffrey-jose) We've all been there: You're scrolling through your favorite social media feed in a dim room, and suddenly an HDR video pops up. It's so intensely bright that you have to squint, or maybe you find yourself turning down your screen brightness just to read the caption. Other times, a video that looks vibrant on your phone looks flat, dark, or washed out when you watch it on your living room TV.

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
- 3 Authors 22 Jun 2026 22 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Geospatial_V02_Strapi_5c55395a9c_UkzvN.webp)

  ## [Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini)

  [arrow_forward](https://developer.android.com/blog/posts/building-a-mixed-reality-tour-guide-with-android-xr-the-geospatial-api-and-gemini) At this year's Google I/O, we announced an update for spatial experiences: the Geospatial API is now available as a preview in ARCore for Jetpack XR.
  [Coco Fatus](https://developer.android.com/blog/authors/coco-fatus), [Alon Hetzroni](https://developer.android.com/blog/authors/alon-hetzroni), [Azin Mehrnoosh](https://developer.android.com/blog/authors/blog-author-1) • 7 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 16 Jun 2026 16 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_Hero_White_e4dbee04d8_Z1qQbv3.webp)

  ## [Android 17 is Here](https://developer.android.com/blog/posts/android-17-is-here)

  [arrow_forward](https://developer.android.com/blog/posts/android-17-is-here) Today we're releasing Android 17 and making it available on most supported Pixel devices. Look for new devices running Android 17 in the coming months.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 13 min read
  - [#Android 17](https://developer.android.com/blog/topics/android-17)
- [![View Steph Pio's profile](https://developer.android.com/static/blog/assets/security_pass_photo_b9ab37d5bf_1fkXBh.webp)](https://developer.android.com/blog/authors/steph-pio) 06 Jul 2026 06 Jul 2026 ![](https://developer.android.com/static/blog/assets/IG_Fund26_Strapi_Header_716b75cbab_1E2Dt5.webp) [Community](https://developer.android.com/blog/categories/community)

  ## [Google Play launches the first Indie Games Fund in Africa](https://developer.android.com/blog/posts/google-play-launches-the-first-indie-games-fund-in-africa)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-launches-the-first-indie-games-fund-in-africa) Google Play is launching the first Indie Games Fund in Africa, investing $1 million to empower 10 indie game studios across Sub-Saharan Africa.
  [Steph Pio](https://developer.android.com/blog/authors/steph-pio) • 1 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)