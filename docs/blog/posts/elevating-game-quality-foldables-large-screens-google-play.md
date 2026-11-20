---
title: https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play
url: https://developer.android.com/blog/posts/elevating-game-quality-foldables-large-screens-google-play
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Elevating games: New large screens and foldables quality standards on Google Play

4 min read ![](https://developer.android.com/static/blog/assets/ABL_162_2000x1000_1_ce7dba8d2a_72W03.webp) 18 Nov 2026 [![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt) VP and GM, Google Play Games As the Android ecosystem continues to evolve, more players are choosing foldable devices for gaming. Foldables offer two distinct ways to play on a single device: quick, one-handed on the go gaming, and a spacious, tablet-sized experience when unfolded. When switching between folded and unfolded states, players expect a seamless and smooth transition, without mid-session restarts, unsaved level progress, or a UI that's stretched or cut off.
Angry Birds 2 transitions seamlessly from on-the-go play to spacious unfolded views.

The good news is that if your game runs on a modern game engine, much of the foundational support is already available. Android has partnered closely with major game engines like [Unity](https://developer.android.com/games/engines/unity/unity-large-screen.md.txt) and [Unreal](https://developer.android.com/games/develop/multiplatform/support-large-screen-resizability.md.txt) to expand native resizing and configuration-change handling so you can build dynamic layouts that scale gracefully across screen orientations.

To give these experiences to players and ensure your games shine across every screen size, Google Play is **introducing new large screen quality requirements for games:**

- Meet the baseline (Tier 3) [large screen and foldables quality guidelines](https://developer.android.com/games/large-screen/build-large-screen-games.md.txt) (*effective Aug. 2027)*.
- Publish foldable screenshots on your Play Store listings (*effective Apr. 2027).*

Read on for full details on each requirement, upcoming milestones, and tools available today to start preparing your game. If you're an app developer, see our dedicated [adaptive quality requirements tailored specifically to apps](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) on Google Play.

## **Meeting Android's large screens and foldables quality guidelines**

Android is introducing [new large screen and foldables quality guidelines](https://developer.android.com/games/large-screen/build-large-screen-games.md.txt) for games, built specifically around how game engines, in-game viewports, and touch controls work on unfolded foldables and tablets. The guidelines are organized into three progressive tiers, from meeting baseline readiness to delivering the highest level of performance and differentiating your game.

**Beginning August 2027, Google Play will require games to meet at minimum the baseline, Tier 3 (Ready)** ,level of support large screens and foldables.

- [**Tier 3: Ready**](https://developer.android.com/games/large-screen/tier-3.md.txt)**:** The baseline required for seamless play on foldables and tablets. Games render full screen in their supported orientation(s) with unobstructed HUD safe areas, cleanly letterbox or pillarbox in-engine when rotated to an unsupported orientation, and preserve state and touch alignment across folding, unfolding, rotation, and multi-window resizing.
- [**Tier 2: Optimized**](https://developer.android.com/games/large-screen/tier-2.md.txt)**:** Builds on Tier 3 to deliver an elevated experience across foldables and tablets, featuring high-resolution graphics and proportional HUD scaling, styled visual framing when letterboxing, smooth frame pacing, and full playability with external controllers, keyboards, and mice.
- [**Tier 1: Differentiated**](https://developer.android.com/games/large-screen/foldables.md.txt)**:** Defines flagship showcase experiences tailored to each form factor. On foldables, Tier 1 focuses on sustained high-frame-rate performance (60 FPS, and 120 FPS on supported displays), thermal and battery stability across extended unfolded sessions, efficient modern graphics rendering, and dynamic resolution scaling between inner and cover screens.

Gossip Harbor delivers full-screen continuity across postures and orientations.

## **Publishing foldable screenshots on Play Store listings**

Starting today, you can upload screenshots for foldable devices on Play Console to showcase the large screen support for your game. **Beginning in April 2027, you will be required to provide at least 3 foldable screenshots,** in addition to the standard **1 phone screenshot**, in your games primary orientation. Providing foldable screenshots by April 2027 will become a standard submission requirement when publishing new games or updating your store listing.

Play Console allows you to upload dedicated foldable screenshots, showcasing both unfolded inner displays and folded outer screens. Supporting the below formats accounts for the full range of standard phone and foldable devices across the Android ecosystem:

- **Standard phones:** Games must continue to provide screenshots of their primary supported orientation, for an aspect ratio of 16:9 (landscape) or 9:16 (portrait). Devices in this category include [Samsung Galaxy S26](https://www.samsung.com/us/smartphones/galaxy-s26/), [Google Pixel 11 Pro](https://store.google.com/product/pixel_11_pro).

![Blog_Foldables_StandardPhones_TrivialKart_Alignedtext.png](https://developer.android.com/static/blog/assets/Blog_Foldables_Standard_Phones_Trivial_Kart_Alignedtext_7b374dc0e5_hN6kv.webp)

- **Foldable devices with 1:1 inner display:** At least one screenshot for an inner display with an aspect ratio of 1:1. Given the folded outer screen has the same aspect ratio as standard phones, no dedicated screenshot is required for the outer screen. Devices in this category include the [Samsung Galaxy Z Fold8 Ultra](https://www.samsung.com/us/smartphones/galaxy-z-fold8-ultra/) and [Google Pixel 11 Pro Fold](https://store.google.com/product/pixel_11_pro_fold).

![1:1 square unfolded inner display](https://developer.android.com/static/blog/assets/Updated_Foldable_display_fc55c47977_25y3xW.webp)

- **Foldable devices with 4:3 inner display:** At least one screenshot with an inner display aspect ratio of 4:3 (landscape) or 3:4 (portrait), and at least one screenshot with an outer screen aspect ratio of 16:10 (landscape) or 10:16 (portrait). Screenshots should be in your game's primary supported orientation. Devices in this category include the [Samsung Galaxy Z Fold8](https://www.samsung.com/us/smartphones/galaxy-z-fold8/).

![Unfolded and folded displays](https://developer.android.com/static/blog/assets/Blog_Foldables_4_3_f76fc52562_Z1uhp6C.webp)

## **Upcoming key milestones**

Planning your roadmap around the upcoming milestones is key to keeping your game optimized and compliant:

- **November 2026 (Live today)**
  - Developers can begin publishing foldable screenshots through Google Play Console. These screenshots will appear in Play Store listings over the next few weeks.
- **April 2027**
  - New games and updates are required to include dedicated foldable screenshots at submission through Play Console.
- **August 2027**
  - Games will be required to meet [baseline Tier 3 (Ready)](https://developer.android.com/games/large-screen/tier-3.md.txt) for large screen and foldables quality guidelines to publish new and updates to games on Google Play.

While our August 2027 milestone focuses on foldables, doing this foundational work will also position your game to scale more easily across tablets, Googlebook laptops, and other large screens as we extend these requirements in future phases.

## **Next steps to prepare your Game**

To help you prepare, we've broken down the immediate next steps and resources available to get your game ready.

1. **Strive for excellence:** Review the [large screen quality guidelines](https://developer.android.com/games/large-screen/build-large-screen-games.md.txt) and standout by designing toward the highest quality Tier 1 (Differentiated). Building for Tier 1 (Differentiated) and Tier 2 (Optimized) unlocks foldable Play Store badging and enhanced merchandising, while also covering Tier 3 (Ready) requirements and setting you up for [Google Play Games Level Up](https://google.play/business/levelup/).
2. **Test on Android devices or Android Emulator:** Use [physical devices](https://developer.android.com/games/large-screen/build-large-screen-games.md.txt#game_large_screen_quality_tests), physical devices hosted on [Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming.md.txt), your game engine's device simulator (such as Unity Device Simulator or Unreal Engine viewport profiles) or virtual [Android Emulator](https://developer.android.com/studio/run/emulator-take-screenshots.md.txt) devices to test 1:1 and 4:3 foldable devices types, verifying layout framing and continuity during folding, unfolding, and rotation.
3. **Upload screenshot assets:** [Capture and upload your foldable screenshots](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt) to Google Play Console. You can upload them on the [Google Play Console](https://play.google.com/console/) by going to **Grow \> Store presence \> Store listings** . Note, screenshots taken from the Foldable (1:1 unfolded inner screen) and Foldable (4:3 unfolded inner screen) Android Emulators are fully compliant to the new screenshot requirements for the Google Play Console, but you are welcome to customize per the [Google Play guidelines](https://support.google.com/googleplay/android-developer/answer/9866151#screenshots).

Delivering a seamless experience on foldables rewards some of your most engaged players while setting your game up to succeed across phones, foldables, tablets, and desktops on Google Play. Thank you for partnering with us to build unforgettable gaming experiences across every screen in the Android ecosystem.

*** ** * ** ***

### **Helpful resources \& references**

- [Tier 3- Ready guidelines](https://developer.android.com/games/large-screen/tier-3.md.txt)
- [Tier 2 - Optimized guidelines](https://developer.android.com/games/large-screen/tier-2.md.txt)
- [Tier 1 -Differentiated guidelines](https://developer.android.com/games/large-screen/tier-1.md.txt)
- [Optimize Unity games for large screens and foldables](https://developer.android.com/games/engines/unity/unity-large-screen.md.txt)
- [Google Play Games Level Up program guidelines](https://developer.android.com/games/guidelines.md.txt)
- [Capture game screenshots for Google Play](https://developer.android.com/google/play/requirements/screenshots-android-cli.md.txt)
- [#Google Play](https://developer.android.com/blog/topics/google-play.md.txt)
- [#Android](https://developer.android.com/blog/topics/android.md.txt)
- [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
- [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
- [#Large Screens](https://developer.android.com/blog/topics/large-screens.md.txt)
Written by:

-

  ## [Aurash Mahbod](https://developer.android.com/blog/authors/aurash-mahbod.md.txt)

  ###### VP and GM, Google Play Games

  [read_more
  View profile](https://developer.android.com/blog/authors/aurash-mahbod) ![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp) ![View Aurash Mahbod's profile](https://developer.android.com/static/blog/assets/image3_98854eb3dd_Z2kItkm.webp)
Continue reading
- [![View Mekka Okereke's profile](https://developer.android.com/static/blog/assets/unnamed_32_974e21c6be_Z1qBCTw.webp)](https://developer.android.com/blog/authors/mekka-okereke.md.txt) 18 Nov 2026 18 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_163_Elevating_Adaptive_App_Quality_Blue_30a2165ec7_Z1hsFPv.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Elevating apps: New adaptive quality standards on Google Play](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-adaptive-quality-standards.md.txt) To give users the premium experience they expect and ensure your apps shine across every screen size, Google Play is introducing new adaptive app quality requirements that go into effect April 2027.
  [Mekka Okereke](https://developer.android.com/blog/authors/mekka-okereke.md.txt) • 4 min read
  - [#Adaptive Games](https://developer.android.com/blog/topics/adaptive-games.md.txt)
  - [#Foldables](https://developer.android.com/blog/topics/foldables.md.txt)
  - [#Adaptive apps](https://developer.android.com/blog/topics/adaptive-apps.md.txt)
  - +1 ↩
- [![View Matthew Forsythe's profile](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_1FlQLe.webp)](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) 19 Nov 2026 19 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_139_Android_developer_verification_Going_global_together_Strapi_01_png_12aa1e5aae_ZkNaef.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Expanding Android developer verification in 2027](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-2027.md.txt) After over a year of joint preparation with industry leaders, regional partners, app distributors, and Android communities, our user protections successfully went live on September 30 for participating stores across Brazil, Indonesia, Singapore, and Thailand.
  [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe.md.txt) • 2 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough.md.txt) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Mesa_de_trabajo_1_copy_8_3f8cf8a935_Z1799P4.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Agentic and Flexible: A next era of Android development](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development.md.txt) Today, at the Android Dev Summit, we are announcing the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough.md.txt) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)