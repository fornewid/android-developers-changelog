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
- 3 Authors 09 Sep 2026 09 Sep 2026 ![](https://developer.android.com/static/blog/assets/Introducing_Fast_and_Reliable_Wireless_Debugging_Strapi_cf55ad145b_1bHKv4.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing Fast and Reliable Wireless Debugging with Android Debug Bridge (ADB) Wi-Fi 2.0](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0) Wireless debugging on Android is now faster, more reliable, and easier to set up than ever. With ADB Wi-Fi 2.0, we've introduced a new server stack and smarter network handling to directly address developer feedback around usability gaps.
  [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins), [Sherif Eid](https://developer.android.com/blog/authors/sherif-eid), [Fabien Sanglard](https://developer.android.com/blog/authors/fabien-sanglard) • 1 min read
  - [#Wireless Debugging](https://developer.android.com/blog/topics/wireless-debugging)
  - [#ADB Wi-Fi 2.0](https://developer.android.com/blog/topics/adb-wi-fi-2-0)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- 3 Authors 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Android_X_Security_State_Library_Strapi_d3ecf61180_ZGGaOR.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Introducing the AndroidX Security State Libraries: A Unified View of Device Security](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security)

  [arrow_forward](https://developer.android.com/blog/posts/introducing-the-android-x-security-state-libraries-a-unified-view-of-device-security) Today, we're thrilled to announce the stable release of the AndroidX Security State version 1.1.0 and Security State Provider version 1.0.0 libraries.
  [Maunik Shah](https://developer.android.com/blog/authors/maunik-shah), [Alec Garcia](https://developer.android.com/blog/authors/alec-garcia), [Joseph Yong](https://developer.android.com/blog/authors/joseph-yong) • 4 min read
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Bench_2_0_Strapi_bench_8767d57564_Z1ywTQ0.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks)

  [arrow_forward](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks) Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)