---
title: https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0
url: https://developer.android.com/blog/posts/introducing-fast-and-reliable-wireless-debugging-with-android-debug-bridge-adb-wi-fi-2-0
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Introducing Fast and Reliable Wireless Debugging with Android Debug Bridge (ADB) Wi-Fi 2.0

1 min read ![](https://developer.android.com/static/blog/assets/Introducing_Fast_and_Reliable_Wireless_Debugging_Strapi_cf55ad145b_2vFLdh.webp) 09 Sep 2026 3 Authors [Steven Jenkins,](https://developer.android.com/blog/authors/steven-jenkins) [Sherif Eid,](https://developer.android.com/blog/authors/sherif-eid) [Fabien Sanglard](https://developer.android.com/blog/authors/fabien-sanglard) Wireless debugging on Android is now faster, more reliable, and easier to set up than ever. With ADB Wi-Fi 2.0, we've introduced a new server stack and smarter network handling to directly address developer feedback around usability gaps.

## How ADB Wi-Fi 2.0 Improves Wireless Debugging

To ensure ADB Wi-Fi 2.0 is even more reliable, we reworked all three core components of the stack: the adb server, the adbd daemon, and Android Studio.

Here are the new features:

- **A new server stack (adb):** Previously, wireless device connections would sever when network configurations changed or devices were turned off. This meant that connections would drop for common occurrences. With our new mDNS stack, we've replaced both Bonjour and legacy mDNS so that your wireless devices more reliably stay connected as you go about your day.
- **Smarter network handling (adbd):** Previously, the workstation's mDNS client would sporadically drop services. Now, the daemon automatically turns off ADB Wi-Fi when it detects an untrusted network and re-enables itself once running on a user-allowed network.
- **Improved discoverability in Android Studio:** Previously, Wi-Fi pairing was difficult to find. Now, you simply enable wireless debugging on your phone and it will show in Android Studio's Device Manager.

With ADB Wi-Fi 2.0, auto-connection success rates improved by 32% and connection speeds increased by 66% for 90% of connections.
![adb-metric.png](https://developer.android.com/static/blog/assets/adb_metric_28f66239c0_15N6xk.webp)

## Getting Started

You can use ADB Wi-Fi 2.0 on your phone, tablet, Wear OS, and TV. Here's how to get started:

1. Update to **Android 17** , **Android SDK Platform-Tools 37.0.0** , and **Android Studio Quail 3** or later.
2. Ensure your workstation and your Android device are connected to the **same Wi-Fi network**.
3. On your device, navigate to [**Developer Options**](https://developer.android.com/studio/debug/dev-options) and **enable Wireless debugging**.
4. Open the Android Studio Device Manager and click the **pair over Wi-Fi** icon.
5. **Scan the QR code** with your device or use a pairing code, and you're all set!

For more information, see the [documentation](https://developer.android.com/studio/run/device#wireless) or watch the [presentation](https://www.youtube.com/watch?v=_CR44gRhad4) at Android Makers by droidcon 2026.

As always, we appreciate any feedback. If you find a bug or issue, please [report it](https://developer.android.com/studio/report-bugs). Also, you can be part of our vibrant Android developer community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://x.com/androidstudio).
- [#Wireless Debugging](https://developer.android.com/blog/topics/wireless-debugging)
- [#ADB Wi-Fi 2.0](https://developer.android.com/blog/topics/adb-wi-fi-2-0)
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Written by:

-

  ## [Steven Jenkins](https://developer.android.com/blog/authors/steven-jenkins)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/steven-jenkins) ![View Steven Jenkins's profile](https://developer.android.com/static/blog/assets/headshot_e042d23f90_dYVWq.webp) ![View Steven Jenkins's profile](https://developer.android.com/static/blog/assets/headshot_e042d23f90_dYVWq.webp)
-

  ## [Sherif Eid](https://developer.android.com/blog/authors/sherif-eid)

  ###### Senior Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/sherif-eid) ![View Sherif Eid's profile](https://developer.android.com/static/blog/assets/unnamed_21_15c8771770_1MKUKC.webp) ![View Sherif Eid's profile](https://developer.android.com/static/blog/assets/unnamed_21_15c8771770_1MKUKC.webp)
-

  ## [Fabien Sanglard](https://developer.android.com/blog/authors/fabien-sanglard)

  ###### Staff Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/fabien-sanglard) ![View Fabien Sanglard's profile](https://developer.android.com/static/blog/assets/unnamed_22_2cb6a389f1_Poh5q.webp) ![View Fabien Sanglard's profile](https://developer.android.com/static/blog/assets/unnamed_22_2cb6a389f1_Poh5q.webp)
Continue reading
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_Z1CHwnO.webp)](https://developer.android.com/blog/authors/amman-asfaw) 01 Sep 2026 01 Sep 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_ZqnmK9.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Leverage Android skills and Gemma 4 in Android Studio Quail 4](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4)

  [arrow_forward](https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4) This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 5 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - [#Android Skills](https://developer.android.com/blog/topics/android-skills)
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_Z1CHwnO.webp)](https://developer.android.com/blog/authors/amman-asfaw) 16 Jul 2026 16 Jul 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_1b91Ge.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent) Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 3 min read
  - [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
  - [# Quail 2](https://developer.android.com/blog/topics/quail-2)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_2bzRoq.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)