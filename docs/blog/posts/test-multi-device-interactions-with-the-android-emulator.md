---
title: Test Multi-Device Interactions with the Android Emulator  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/test-multi-device-interactions-with-the-android-emulator
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Test Multi-Device Interactions with the Android Emulator

###### 2-min read

![](/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

13

Apr
2026

[![](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](/blog/authors/steven-jenkins)

[##### Steven Jenkins](/blog/authors/steven-jenkins)

###### Product Manager, Android Studio

Testing multi-device interactions is now easier than ever with the Android Emulator. Whether you are building a multiplayer game, extending your mobile application across form factors, or launching virtual devices that require a device connection, the Android Emulator now natively supports these developer experiences.

Previously, interconnecting multiple Android Virtual Devices (AVDs) caused significant friction. It required manually managing complex port forwarding rules just to get two emulators to connect.

Now you can take advantage of a new networking stack for the Android Emulator which brings zero-configuration peer-to-peer connectivity across all your AVDs.

### Interconnecting emulator instances

The new networking stack for the Android Emulator transforms how emulators communicate. Previously, each virtual device operated on its own local area network (LAN), effectively isolating it from other AVDs. The new Wi-Fi network stack changes this by creating a shared virtual network backplane that bridges all running instances on the same host machine.

#### Key benefits:

* **Zero-configuration:** No more manual port forwarding or scripting `adb` commands. AVDs on the same host appear on the same virtual network.
* **Peer-to-peer connectivity:** Critical protocols like Wi-Fi Direct and Network Service Discovery (NSD) work out of the box between emulators.
* **Improved stability:** Resolves long-standing stability issues, such as data loss and connection drops found in the legacy stack.
* **Cross-platform consistency:** Works the same across Windows, macOS, and Linux.

### Use Cases

The enhanced emulator networking supports a wide range of multi-device development scenarios:

* **Multi-device apps:** Test file sharing, local multiplayer gaming, or control flows between a phone and another Android device.
* **Continuous integration:** Create robust, automated multi-device test pipelines without flaky network scripts.
* **Android XR & AI glasses:** Easily test companion app pairing and data streaming between a phone and glasses within Android Studio.
* **Automotive & Wear OS:** Validate connectivity flows between a mobile device and a vehicle head unit or smartwatch.

[](/static/blog/assets/videos/netsim_demo_918a409c3b/netsim_demo_918a409c3b.mov)

*The new emulator networking stack allows multiple AVDs to share a virtual network, enabling direct peer-to-peer communication with zero configuration.*

### Get Started

The new networking capability is enabled by default in the latest Android Emulator release (36.5), which is available via the [Android Studio SDK Manager](/studio/intro/update#sdk-manager). Just update your emulator and launch multiple devices!

If you need to disable this feature or want to learn more, please refer to our [documentation](/studio/run/emulator-networking-interconnect).  
  
As always, we appreciate any feedback. If you find a bug or issue, please [file an issue](/studio/report-bugs). Also you can be part of our vibrant Android developer community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Medium](https://medium.com/androiddevelopers), [Youtube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://x.com/androidstudio).

###### Written by:

* ## [Steven Jenkins](/blog/authors/steven-jenkins)

  ###### Product Manager

  [read\_more
  View profile](/blog/authors/steven-jenkins)

  ![](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)

  ![](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)

## Continue reading

* [![](/static/blog/assets/Ataul_Munim_cf0796f68c_r1HY2.webp)](/blog/authors/ataul-munim)

  02

  Jun
  2026

  02

  Jun
  2026

  ![](/static/blog/assets/MM_Differentiated_Experiences_Strapi_bbe8e7618b_19k3ww.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Building Premium Android Experiences at Google I/O ‘26](/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  [arrow\_forward](/blog/posts/building-premium-android-experiences-at-google-i-o-26)

  At Google I/O ‘26, we showcased how the latest advancements in the Android ecosystem can help you elevate your app's quality while maximizing development efficiency.

  ###### [Ataul Munim](/blog/authors/ataul-munim) • 3 min read

  + [#Performance](/blog/topics/performance)
  + [#Memory](/blog/topics/memory)
  + [#R8](/blog/topics/r8)
  + [#Wear OS](/blog/topics/wear-os)
  + [#Automotive OS](/blog/topics/automotive-os)
  + +3
    ↩
* [![](/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](/blog/authors/jingyu-shi)

  26

  May
  2026

  26

  May
  2026

  ![](/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O ‘26](/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow\_forward](/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  At Google I/O 2026, we introduced Android’s shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google’s AI into your apps.

  ###### [Jingyu Shi](/blog/authors/jingyu-shi) • 2 min read

  + [#Google I/O](/blog/topics/google-i-o)
  + [#Android](/blog/topics/android)
  + [#AppFunctions](/blog/topics/app-functions)
  + [#On-device](/blog/topics/on-device)
  + +2
    ↩
* [![](/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](/blog/authors/luke-hopkins)[![](/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](/blog/authors/ryan-bartley)

  19

  May
  2026

  19

  May
  2026

  ![](/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow\_forward](/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](/blog/authors/luke-hopkins), [Ryan Bartley](/blog/authors/ryan-bartley) • 4 min read

  + [#Android XR](/blog/topics/android-xr)
  + [#Google I/O](/blog/topics/google-i-o)
  + [#Game engine development](/blog/topics/game-engine-development)
  + +1
    ↩

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)