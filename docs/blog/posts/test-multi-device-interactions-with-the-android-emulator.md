---
title: https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator
url: https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Test Multi-Device Interactions with the Android Emulator

###### 2-min read

![](https://developer.android.com/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp) 13 Apr 2026 [![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](https://developer.android.com/blog/authors/steven-jenkins) [##### Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins)

###### Product Manager, Android Studio

Testing multi-device interactions is now easier than ever with the Android Emulator. Whether you are building a multiplayer game, extending your mobile application across form factors, or launching virtual devices that require a device connection, the Android Emulator now natively supports these developer experiences.

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

###### Written by:

-

  ## [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/steven-jenkins) ![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp) ![](https://developer.android.com/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  3 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang)[![](https://developer.android.com/static/blog/assets/David_Chou_226df78370_tqGIk.webp)](https://developer.android.com/blog/authors/david-chou) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/announcing_gemma4_aicore_ce479292b9_Z15e7FP.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Announcing Gemma 4 in the AICore Developer Preview](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  [arrow_forward](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview) At Google, we're committed to bringing the most capable AI models directly to the Android devices in your pocket. Today, we're thrilled to announce the release of our latest state-of-the-art open model: Gemma 4.

  ###### [Caren Chang](https://developer.android.com/blog/authors/caren-chang), [David Chou](https://developer.android.com/blog/authors/david-chou) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)