---
title: https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator
url: https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Test Multi-Device Interactions with the Android Emulator

1 min read ![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp) 13 Apr 2026 [![View Steven Jenkins's profile](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins) Product Manager, Android Studio Testing multi-device interactions is now easier than ever with the Android Emulator. Whether you are building a multiplayer game, extending your mobile application across form factors, or launching virtual devices that require a device connection, the Android Emulator now natively supports these developer experiences.

Previously, interconnecting multiple Android Virtual Devices (AVDs) caused significant friction. It required manually managing complex port forwarding rules just to get two emulators to connect.

Now you can take advantage of a new networking stack for the Android Emulator which brings zero-configuration peer-to-peer connectivity across all your AVDs.

### Interconnecting emulator instances

The new networking stack for the Android Emulator transforms how emulators communicate. Previously, each virtual device operated on its own local area network (LAN), effectively isolating it from other AVDs. The new Wi-Fi network stack changes this by creating a shared virtual network backplane that bridges all running instances on the same host machine.

#### Key benefits:

- **Zero-configuration:** No more manual port forwarding or scripting `adb` commands. AVDs on the same host appear on the same virtual network.
- **Peer-to-peer connectivity:** Critical protocols like Wi-Fi Direct and Network Service Discovery (NSD) work out of the box between emulators.
- **Improved stability:** Resolves long-standing stability issues, such as data loss and connection drops found in the legacy stack.
- **Cross-platform consistency:** Works the same across Windows, macOS, and Linux.

### Use Cases

The enhanced emulator networking supports a wide range of multi-device development scenarios:

- **Multi-device apps:** Test file sharing, local multiplayer gaming, or control flows between a phone and another Android device.
- **Continuous integration:** Create robust, automated multi-device test pipelines without flaky network scripts.
- **Android XR \& AI glasses:** Easily test companion app pairing and data streaming between a phone and glasses within Android Studio.
- **Automotive \& Wear OS:** Validate connectivity flows between a mobile device and a vehicle head unit or smartwatch.

*The new emulator networking stack allows multiple AVDs to share a virtual network, enabling direct peer-to-peer communication with zero configuration.*

### Get Started

The new networking capability is enabled by default in the latest Android Emulator release (36.5), which is available via the [Android Studio SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager). Just update your emulator and launch multiple devices!

If you need to disable this feature or want to learn more, please refer to our [documentation](https://developer.android.com/studio/run/emulator-networking-interconnect).  

As always, we appreciate any feedback. If you find a bug or issue, please [file an issue](https://developer.android.com/studio/report-bugs). Also you can be part of our vibrant Android developer community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [Youtube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://x.com/androidstudio).
Written by:

-

  ## [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/steven-jenkins) ![View Steven Jenkins's profile](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp) ![View Steven Jenkins's profile](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)
Continue reading
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_19h6h7.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_1w4qDC.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_Z1hF7qE.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
- [![View Chiara Chiappini's profile](https://developer.android.com/static/blog/assets/unnamed_14_383c39c2c2_Derb5.webp)](https://developer.android.com/blog/authors/chiara-chiappini) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Bring_one_handed_gestures_Strapi_defff06599_Z1FDx9g.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bring one-handed gestures to your Wear OS app](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app)

  [arrow_forward](https://developer.android.com/blog/posts/bring-one-handed-gestures-to-your-wear-os-app) First introduced on Pixel Watch with Wear OS 6.1, one-handed gestures made quick interactions effortless, such as starting and stopping a timer, accepting calls, and controlling media.
  [Chiara Chiappini](https://developer.android.com/blog/authors/chiara-chiappini) • 3 min read
  - [#Wear OS](https://developer.android.com/blog/topics/wear-os)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#pixel watch](https://developer.android.com/blog/topics/pixel-watch)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)