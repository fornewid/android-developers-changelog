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



[Product News](/blog/categories/product-news)

# Test Multi-Device Interactions with the Android Emulator

2-min read

![](/static/blog/assets/Multi_Device_Interactions_with_Android_Emulator_Strapi_5d6ea711e7_Z1AYEiA.webp)

13

Apr
2026

[![View Steven Jenkins's profile](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)](/blog/authors/steven-jenkins)

[Steven Jenkins](/blog/authors/steven-jenkins)

Product Manager, Android Studio

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

Written by:

* ## [Steven Jenkins](/blog/authors/steven-jenkins)

  ###### Product Manager

  [read\_more
  View profile](/blog/authors/steven-jenkins)

  ![View Steven Jenkins's profile](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)

  ![View Steven Jenkins's profile](/static/blog/assets/headshot_e042d23f90_2x0LLK.webp)

Continue reading

* [![View Zoe Lopez-Latorre 's profile](/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1QyLll.webp)](/blog/authors/zoe-lopez-latorre)

  08

  Jul
  2026

  08

  Jul
  2026

  ![](/static/blog/assets/Bench_July_releas_V01_Strapi_6ee24bdb6b_1NrCN7.webp)

  [Product News](/blog/categories/product-news)

  ## [Evolving how LLMs are measured for Android: the next era of Android Bench](/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench)

  [arrow\_forward](/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench)

  Back in March, we introduced Android Bench—our LLM leaderboard for real-world Android development tasks. Since then, we have enhanced the benchmark based on your feedback, including evaluating open-weight models and adding cost and efficiency dimensions to the leaderboard.

  [Zoe Lopez-Latorre](/blog/authors/zoe-lopez-latorre) 
  •
  3 min read
  + [#Agentic Android development](/blog/topics/agentic-android-development)
* [![View Paul Feng's profile](/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](/blog/authors/paul-feng)

  24

  Jun
  2026

  24

  Jun
  2026

  ![](/static/blog/assets/Apps_Experience_Play_Blog_Header_2000x1000_8c3a95404a_lYfpd.webp)

  [Product News](/blog/categories/product-news)

  ## [Expanded billing choice and lower fees on Google Play](/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play)

  [arrow\_forward](/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play)

  At Google Play, we are committed to delivering the best possible experience to users, while ensuring developers have the tools and adaptability to succeed.

  [Paul Feng](/blog/authors/paul-feng)
  •
  3 min read
* [![View Matthew Forsythe's profile](/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](/blog/authors/matthew-forsythe)

  18

  Jun
  2026

  18

  Jun
  2026

  ![](/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  [Product News](/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow\_forward](/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  [Matthew Forsythe](/blog/authors/matthew-forsythe)
  •
  2 min read

Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)