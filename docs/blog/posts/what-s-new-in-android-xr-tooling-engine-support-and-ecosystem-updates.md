---
title: https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates
url: https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates

2 min read ![](https://developer.android.com/static/blog/assets/MM_Android_XR_Meta_a489e757ed_Z1JMs6H.webp) 15 Jun 2026 [![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp)](https://developer.android.com/blog/authors/stevan-silva.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva.md.txt) \& [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today. Alongside the latest updates from [Google I/O](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4.md.txt) and this week's Augmented World Expo (AWE), we are rolling out new tooling, broader engine support, and ecosystem resources to help you build and scale experiences for Android XR.

To get a quick look at what's new, check out our video recap!
[Video](https://www.youtube.com/watch?v=otzSN5pSNZk)

Ready to dive deeper? Let's jump into the major updates that will streamline your XR development workflow.

### Build, Prototype, and Iterate with Developer Preview 4

[Developer Preview 4 of the Android XR SDK](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4.md.txt) delivers the APIs and tools you need to design and build right from your laptop. This update includes the specific libraries required to target both immersive and augmented experiences. Check out the video below for a comprehensive breakdown of the latest in Android XR:
[Video](https://www.youtube.com/watch?v=1KOO2lqsdaA)

To test all of these interactions without needing physical hardware, you can emulate and iterate on your code entirely within [Android Studio](https://developer.android.com/studio/preview). Check out our tooling deep dive to see how you can use XR emulator today:
[Video](https://www.youtube.com/watch?v=saRE0t11KJY)

#### Extending your mobile apps for intelligent eyewear

Building for audio and display glasses doesn't mean starting from scratch. With the [Jetpack Projected library](https://developer.android.com/develop/xr/jetpack-xr-sdk.md.txt#jetpack-projected), you can take your existing mobile app to create a complementary augmented experience. The new release includes a [Device Availability API](https://developer.android.com/develop/xr/jetpack-xr-sdk/glasses/check-availability.md.txt) that hooks into standard Android Lifecycle states, allowing your app to natively adapt its behavior based on whether the glasses are being worn.

To accelerate your development journey, use [Android CLI](https://developer.android.com/tools/agents) and the [display glasses skil](https://github.com/android/skills)l to extend your mobile app into an augmented experience. The skill is packed with specialized knowledge of Jetpack Compose Glimmer, enabling it to build your UI using our recommended design patterns.

We've also updated [Jetpack Compose Glimmer](https://developer.android.com/develop/xr/jetpack-xr-sdk/jetpack-compose-glimmer) to optimize text legibility on optical see-through displays and provide touchpad-optimized navigation components.

See how it looks in action: Developers at [NAVER Papago](https://play.google.com/store/apps/details?id=com.naver.labs.translator) are already exploring how to seamlessly bring their [mobile experience directly to display glasses.](https://blog.naver.com/nv_papago/224314256256)
[Video](https://www.youtube.com/watch?v=bYvAvQs3f8o)

To learn how to leverage these tools, watch this session on extending mobile apps for AI glasses:
[Video](https://www.youtube.com/watch?v=83CF7AhozJ8)

#### Building global, location-based immersive experiences

For developers focused on immersive experiences, Developer Preview 4 brings modern, Kotlin-first architectural upgrades across our core perception libraries. We have also introduced an early preview of the Geospatial API for wired XR glasses. By combining [ARCore for Jetpack XR](https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore.md.txt) with Google's Visual Positioning System (VPS), you can anchor digital content to high-precision real-world locations.

### Leverage the Platforms You Know with Expanded Engine Support

We want you to build using the ecosystems and workflows you already know best. To make it easier to bring your existing XR experiences over to Android XR, we are thrilled to introduce [official support for Unreal Engine and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot.md.txt) alongside [Unity's support for wired XR glasses](https://unity.com/blog/unity-android-xr-wired-glasses-support).

With this expansion, we are introducing the [Android XR Engine Hub,](https://developer.android.com/develop/xr/engine-hub) a desktop tool for Windows that shortens iteration cycles by bringing real-time testing directly into your engines viewport. Catch the full breakdown of our engine updates here:
[Video](https://www.youtube.com/watch?v=nmbBWSX8l54)

### Apply Today for the Android XR Developer Catalyst Program

In addition to providing the platform, we want to fuel your innovation directly through ecosystem resources. The [Android XR Developer Catalyst Program](https://developer.android.com/develop/xr/catalyst) is designed to support developers with access to pre-release hardware, including display glasses, and wired XR glasses.

Accepted developers will receive resources, support forums, and launch guidance to prepare their apps for Google Play. Applications are open right now, so don't wait to [submit your project ideas](https://developer.android.com/develop/xr/catalyst).

### Start Building!

The ecosystem is growing rapidly, and the tools are ready for you to explore. Samsung Galaxy XR is available now, and you can dive in today with [Developer Preview 4 of the Android XR SDK](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4.md.txt). If you don't have hardware yet, check out the tools and to get started with the [XR Emulator in Android Studio](http://google.com/url?sa=j&url=http://goo.gle/xr-setup&uct=1765473974&usg=L4MkW244XAfYytuJciS39GjuDv0.&opi=73833047&source=chat).

For a complete look at all of our technical sessions, browse the full [Android XR Playlist on YouTube](https://youtube.com/playlist?list=PLWz5rJ2EKKc-feGl0F3rXtUste_8TkvZJ&si=zggz4T3eiQmH5xL2) to see what else is possible. We can't wait to see what you build!
- [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
- [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4.md.txt)
Written by:

-

  ## [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva.md.txt)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/stevan-silva) ![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp) ![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp)
-

  ## [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/vinny-da-silva) ![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp) ![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)
Continue reading
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Stevan Silva's profile](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_ZaY4rR.webp)](https://developer.android.com/blog/authors/stevan-silva.md.txt) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Text_Strapi_2000x1000_2d4221d884_2cdxMf.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 4](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-4.md.txt) We're excited to launch Developer Preview 4 of the Android XR SDK, continuing our focus on unifying cross-device development for headsets, wired XR glasses, and intelligent eyewear.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva.md.txt) • 5 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk.md.txt)
  - [#Developer Preview](https://developer.android.com/blog/topics/developer-preview.md.txt)
  - [#Unity](https://developer.android.com/blog/topics/unity.md.txt)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o.md.txt)
  - +3 ↩
- 3 Authors 18 Aug 2026 18 Aug 2026 ![](https://developer.android.com/static/blog/assets/Android_XR_beta_release_Strapi_a23ed1d892_2wR9tl.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Jetpack XR SDK core libraries reach beta: The next milestone for Android XR](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/jetpack-xr-sdk-core-libraries-reach-beta-the-next-milestone-for-android-xr.md.txt) Since introducing the Android XR SDK, developers have transformed their ideas into innovative immersive experiences across headsets and wired XR glasses.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Greg Underwood](https://developer.android.com/blog/authors/greg-underwood.md.txt), [Yasmine Evjen](https://developer.android.com/blog/authors/yasmine-evjen.md.txt) • 2 min read
  - [#Jetpack XR SDK](https://developer.android.com/blog/topics/jetpack-xr-sdk.md.txt)
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
  - [#Android XR SDK](https://developer.android.com/blog/topics/android-xr-sdk.md.txt)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)