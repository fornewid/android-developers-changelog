---
title: https://developer.android.com/blog/posts/google-play-adaptive-quality-standards
url: https://developer.android.com/blog/posts/google-play-adaptive-quality-standards
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Elevating apps: New adaptive quality standards on Google Play

4 min read ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) 18 Nov 2026 [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) GM, Google Play Apps Since Android first announced platform support for foldable devices, consumer adoption of premium foldable Android phones has continued to grow at a rapid pace. Foldable devices in the Android ecosystem evolved from an emerging innovation into premium mainstream hardware, with a range of sizes that match the diverse needs of users. When users invest in these top-tier devices, they expect their favorite apps and games to provide a seamless and smooth transition as they switch between folded and unfolded states, and unlock new experiences possible only on foldable screens.
Unlocking new experiences possible only on foldables.

Building with modern UI toolkits like [Jetpack Compose](https://developer.android.com/develop/ui) enables app developers to build adaptive layouts that scale gracefully from smartphones to foldables and tablets. By adopting adaptive design standards, you optimize your apps for foldables, while simultaneously elevating app quality across an ecosystem of over 580 million large screen devices in the hands of users today, delivering unique experiences on devices ranging from Amazon's [Alexa tablets](https://www.amazon.com/alexa/shop-alexa-tablets) and [Googlebook](https://googlebook.google/) laptops to Android XR devices like [XREAL Aura](https://www.xreal.com/aura).

To give users the premium experience they expect and ensure your apps shine across every screen size, **Google Play is introducing new adaptive app quality requirements that go into effect April 2027:**

- Meet the baseline (Tier 3) [adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality.md.txt).
- Publish foldable device screenshots on your Google Play Store listings.

Read on for full details on each requirement, upcoming milestones, and tools available today to get your app ready. If you're a game developer, see our dedicated [large-screen quality requirements tailored specifically to games](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) on Google Play.

## **Meeting Android's adaptive app quality guidelines**

Starting April 2027, apps on Google Play will need to meet at least Tier 3 of the [Android adaptive app quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality.md.txt) for foldables. Apps that do not meet this quality bar will no longer be able to publish or update on Google Play, and may have reduced visibility on the store. While our April 2027 enforcement establishes Tier 3 adaptive quality as the mandatory baseline for foldables, Google Play's quality framework will progressively expand to incorporate Tier 2 and Tier 1 standards across foldables, tablets, Googlebooks, and Android XR. Developers should build their apps now for these higher tiers to maintain compliance and unlock premier store badging, editorial spotlighting, and enhanced merchandising across Google Play as the platform bar elevates.

Here is a quick refresher on Android's adaptive app quality tiers:

- [**Tier 3: Adaptive ready**](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3.md.txt)**---**Apps must fill the available display area without letterboxing or compatibility modes. Apps must preserve state (scroll position, text input, media playback) during rotation, folding/unfolding, and resizing, while supporting multi-window environments.

![letterbox_states_foldable.png](https://developer.android.com/static/blog/assets/letterbox_states_foldable_33dc54f480_Z2kPfxi.webp) Full screen app content.

- [**Tier 2: Adaptive optimized**](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2.md.txt)**---**Evaluates responsive multi-pane layouts, avoiding stretched UI elements, as well as basic support for external keyboard, mouse, trackpad, and stylus input across foldables, tablets, and other large screen devices.

![multi-pane-layout.png](https://developer.android.com/static/blog/assets/multi_pane_layout_cb6124023a_XpSjy.webp) Multi-pane layouts.

- [**Tier 1: Adaptive differentiated**](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables.md.txt)**---** Evaluates tabletop and book postures, camera continuity, interactive picture-in-picture, and multi-instance support for media, video, reading, and multitasking apps.

Foldable postures aware.

## **Publishing foldable screenshots on Play Store listings**

Starting today, you can upload screenshots for foldable devices on Play Console to showcase the adaptive support for your app. Beginning in April 2027, you will be required to provide **3 foldable screenshots** in addition to the standard **2 phone screenshots.**Providing foldable screenshots by April 2027 will become a standard submission requirement when publishing new apps or updating your store listing.

Play Console allows you to upload dedicated foldable screenshots, showcasing both unfolded inner displays and folded outer screens. Screenshots can come from physical Android devices or by using the Android Emulator. Supporting the formats shown below accounts for the full range of standard phone and foldable devices across the Android ecosystem:

- **Standard phone landscape screenshot** --- Showcase the adaptive support built into your app with the option to now include a landscape screenshot (16:9) in addition to the existing requirement of portrait screenshots (9:16). Devices in this category include the [Samsung Galaxy S26](https://www.samsung.com/us/smartphones/galaxy-s26/) and [Google Pixel 11 Pro](https://store.google.com/product/pixel_11_pro).

![Blog_Foldables_StandardPhoneLandscapeScreenshot_alignedtext.png](https://developer.android.com/static/blog/assets/Blog_Foldables_Standard_Phone_Landscape_Screenshot_alignedtext_d77826c868_CMaiI.webp)

* Use Android CLI and Android Emulator to capture *  
* Play Console *[*ready screenshots*](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt)*.*

- **Foldable devices with 1:1 inner display** ---Include at least one screenshot for an unfolded inner screen with an aspect ratio of 1:1. Devices in this category include the [Samsung Galaxy Z Fold8 Ultra](https://www.samsung.com/us/smartphones/galaxy-z-fold8-ultra/) and [Google Pixel 11 Pro Fold](https://store.google.com/product/pixel_11_pro_fold).

![Blog_Foldables_FoldableDeviceswith 1_1_InnerDisplay_1920.png](https://developer.android.com/static/blog/assets/Blog_Foldables_Foldable_Deviceswith_1_1_Inner_Display_1920_35b4956788_1JOECf.webp)

- **Foldable devices with 4:3 inner display** ---Provide at least one screenshot with an unfolded inner screen aspect ratio of 4:3 and at least one portrait screenshot with a folded outer screen aspect ratio of 10:16. You can optionally add a 16:10 landscape as well. Devices in this category include the [Samsung Galaxy Z Fold8](https://www.samsung.com/us/smartphones/galaxy-z-fold8/).

![Blog_Foldables_FoldableDeviceswith_4_3_InnerDisplay_alignedtext.png](https://developer.android.com/static/blog/assets/Blog_Foldables_Foldable_Deviceswith_4_3_Inner_Display_alignedtext_d63f4e6441_Z1tqHzK.webp)

## **Upcoming key milestones**

In addition to updated screenshot requirements and adaptive design standards, Google Play will require apps to [target API level 37 (Android 17)](https://android-developers.googleblog.com/2026/02/prepare-your-app-for-resizability-and.html), removing developer opt-outs for orientation and resizability restrictions on large screens, ensuring apps adapt seamlessly to any screen.

Plan your roadmap around the upcoming milestones is key to keeping your app optimized and compliant:

- **November 2026 (Live today)**
  - Developers can begin publishing foldable screenshots through Google Play Console. These screenshots will appear in Play Store listings over the next few weeks.
  - Apps that meet [Tier 2](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2.md.txt) and [Tier 1](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables.md.txt) support for adaptive quality can [apply for badging](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality.md.txt#:~:text=Google%20Play%20Large%20Screen%20Badge) and enhanced merchandising on Google Play.
- **April 2027**
  - New apps and updates are required to include dedicated foldable screenshots at submission.
  - Baseline Tier 3 adaptive quality support takes effect for standard applications.
  - Existing un-updated apps will remain downloadable.
- **August 2027**
  - New and updated apps are required to target API level 37 (Android 17).

## **Next steps to prepare your app**

To help you prepare, we've broken down the immediate next steps and resources available to get your app ready.

1. **Review design guidelines** --- Review the [UI Design Guidelines](https://developer.android.com/develop/adaptive-apps#get-started-with-android-adaptive-design), [Figma UI Templates](https://developer.android.com/develop/adaptive-apps#get-started-with-android-adaptive-design), and the [Adaptive app quality guidelines](https://developer.android.com/develop/adaptive-apps/quality-guidelines/adaptive-app-quality.md.txt).
2. **Optimize your app** ---Use the [Jetpack Compose adaptive skill](https://github.com/android/skills/blob/main/jetpack-compose/adaptive/SKILL.md) in [Android Studio](https://developer.android.com/tools/agents/android-skills.md.txt#use-android-skills) or [Android CLI](https://developer.android.com/tools/agents) with your AI agent of choice to optimize your app.
3. **Test on Android device or Android Emulator** --- Use physical devices, physical devices hosted on [Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming.md.txt), or virtual Android Emulator devices to test 1:1 and 4:3 foldable device types, verifying adaptive layouts and continuity during folding, unfolding, and rotation.
4. **Upload screenshot assets** --- To get ahead of the April 2027 deadline, you have the option of capturing and uploading your adaptive screens starting today. You can upload them on [Play Console](https://play.google.com/console/) by going to **Grow \> Store presence \> Store listings** . Note, [screenshots taken from the foldable](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt) (1:1 inner display) and foldable (4:3 inner display) Android Emulators are fully compliant with the new screenshot requirements for Play Console, but you are welcome to customize per the [Google Play guidelines](https://support.google.com/googleplay/android-developer/answer/9866151#screenshots).

Meeting these adaptive app quality requirements is a crucial step toward building a more versatile, reliable experience across form factors in the Android ecosystem. We appreciate your partnership and everything you do to delight hundreds of millions of users across phones, foldables, and large screens.

*** ** * ** ***

### **Helpful resources \& references**

**Design**

- [Adaptive App UI Design Gallery](https://developer.android.com/design/ui/gallery)
- [Adaptive App UI Design Guidelines](https://developer.android.com/develop/adaptive-apps#get-started-with-android-adaptive-design)
- [Android Figma Templates](https://www.figma.com/@androiddesign)

**Develop**

- [Tier 3 --- Adaptive Ready Guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-3.md.txt)
- [Tier 2 --- Adaptive Optimized Guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/tier-2.md.txt)
- [Tier 1 --- Foldables Quality \& Posture Guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality/experiences/foldables.md.txt)
- [Get Started with Large Screens \& Window Size Classes](https://developer.android.com/guide/topics/large-screens)
- [Capture app screenshots for Google Play](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt)
- [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
- [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
- [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
Written by:

-

  ## [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt)

  ###### GM, Google Play Apps

  [read_more
  View profile](https://developer.android.com/blog/authors/mekka-okereke) ![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp) ![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)
Continue reading
- [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating games: New large screens and foldables quality standards on Google Play](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play.md.txt) To give these experiences to players and ensure your games shine across every screen size, Google Play is introducing new large screen quality requirements for games
  [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) • 4 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
  - +3 ↩
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_1JLHid.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google.md.txt) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston.md.txt), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang.md.txt) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7.md.txt)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google.md.txt)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4.md.txt)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose.md.txt)
  - +5 ↩
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Combo_IO_Strapi_2000x1000_0370ff6d2c_Z14DWX.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Adaptive development for the expanding Android ecosystem](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/adaptive-development-for-the-expanding-android-ecosystem.md.txt) With the release of Android 17, we are transitioning into an adaptive first development standard. Your users no longer rely on a single form factor; they transition between phones, foldables, tablets, laptops, automotive displays, and immersive XR environments throughout their day.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz.md.txt) • 3 min read
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o.md.txt)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)