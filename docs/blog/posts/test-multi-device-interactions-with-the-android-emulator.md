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
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Raghavendra Hareesh Pottamsetty's profile](https://developer.android.com/static/blog/assets/Raghavendra_Hareesh_Pottamsetty_72fdb063a0_1h0S85.webp)](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) 26 Aug 2026 26 Aug 2026 ![](https://developer.android.com/static/blog/assets/Raising_the_bar_Google_Play_Strapi_2_a80695bf12_Z2jxf1k.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating app quality: Reducing memory usage and improving device migration](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-app-quality-reducing-memory-usage-and-improving-device-migration) Maintaining a healthy Android ecosystem is a shared commitment where every app and game has a role to play.
  [Raghavendra Hareesh Pottamsetty](https://developer.android.com/blog/authors/raghavendra-hareesh-pottamsetty) • 4 min read
- [![View Ron Aquino's profile](https://developer.android.com/static/blog/assets/unnamed_18_8bd07de9bd_9wUet.webp)](https://developer.android.com/blog/authors/ron-aquino) 25 Aug 2026 25 Aug 2026 ![](https://developer.android.com/static/blog/assets/Ensuring_a_safe_Gen_AI_ecosystem_on_Google_Play_Scrapi_a8fa6da415_ZsHups.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Ensuring Safety in the Generative AI Ecosystem: Protecting Users from Non-Consensual Intimate Content](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content)

  [arrow_forward](https://developer.android.com/blog/posts/ensuring-safety-in-the-generative-ai-ecosystem-protecting-users-from-non-consensual-intimate-content) At Google Play, user safety and developer success go hand in hand. We continue to see growth in apps with AI generated features, and indeed, adding generative AI into your apps is a great way to unlock incredible creative possibilities.
  [Ron Aquino](https://developer.android.com/blog/authors/ron-aquino) • 4 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)