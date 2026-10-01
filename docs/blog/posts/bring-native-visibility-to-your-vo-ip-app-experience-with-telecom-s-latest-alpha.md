---
title: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
url: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha

2 min read ![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_2ewsGa.webp) 14 May 2026 [![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp)](https://developer.android.com/blog/authors/nataraj-k-r) [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r) Developer Relations Engineer, Android Developer Engineering The initial launch of the Jetpack Telecom library introduced [`CallsManager`](https://developer.android.com/reference/androidx/core/telecom/CallsManager), replacing the legacy `ConnectionService` API to simplify VoIP integration. CallsManager streamlines call lifecycle management and audio routing while enabling interactions with remote surfaces like smartwatches, Bluetooth devices, and Android Auto. Additionally, it supports call extensions for richer features---such as participant handling, custom icons, call silencing and meeting summary on remote surfaces ---all while maintaining backward compatibility down to Android O (API Level 26).

Building on this foundation, **Jetpack Telecom v1.1.0** brings native-level visibility and convenience to third-party VoIP apps. This latest release introduces powerful new capabilities, including unified call history, call log exclusion, and native callback functionality, making call management more seamless than ever for users.

Here is a closer look at what's new and how you can implement these features in your applications.

### **Bridging the Dialer Gap: Unified call history and Callbacks**

Historically, users have had to open individual third-party apps to view their VoIP call history or return a missed call. With the new integrated call logging feature, system dialer apps can now surface call logs directly from third-party VoIP apps.

Even better, users can now initiate a callback to a VoIP contact straight from their native system dialer, streamlining the communication experience.

**How it works:**

To opt-in to this feature, do the following:

1. **Register for Callbacks:** Your VoIP app must register a new system-protected intent: `TelecomManager.ACTION_CALL_BACK`.
2. **Log the Call:** Use `TelecomManager.addCall` (or related Jetpack APIs) to ensure the system automatically logs the call.
3. **Manage Call IDs:** When a call is registered, `CallControlScope.getCallId` provides a unique UUID. The system dialer uses this exact `TelecomManager.EXTRA_UUID` when creating the callback intent.
4. **Initiate the Callback:** Your application must store and manage the call details associated with this UUID. When the system dialer fires the callback intent with the `EXTRA_UUID`, your app can seamlessly resolve the ID and initiate the call with the correct details.

![integrated_call_log.png](https://developer.android.com/static/blog/assets/integrated_call_log_2d23491534_o7kba.webp)

### **Fine-Grained Control: Call Log Exclusion**

We recognize that not every VoIP call should be visible in the system's native dialer history. Whether for privacy reasons, ephemeral communication, or app-specific behavior, you need control over what gets surfaced.

To address this, we are introducing **Call Log Exclusion** . You can now prevent specific calls from being logged into the system call logs by setting the `isLogExcluded` boolean to `true` within `CallAttributesCompat`. By configuring this flag, the call remains completely hidden from the system logs, and the native dialer will not display it.

### **Important Note on Compatibility**

These integrated logging and callback features are available for devices running **Android 16.1 (SDK 36.1)** and higher. Refer [here](https://developer.android.com/build#module-level) to compile your app with Android SDK 36.1.

### **Get Started**

We encourage developers to test these integrations and explore how unified call history and callbacks can improve the daily user experience of your VoIP applications.

To help you get started and see these APIs in action, we have put together a sample application demonstrating the new integrations.

- **View the sample app here:** <https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom>

Check out the [release notes](https://developer.android.com/jetpack/androidx/releases/core#core-telecom_version_11_2) and [documentation](https://developer.android.com/develop/connectivity/telecom/call-log-integration) to start implementing these features today!

**Note:** : Although Jetpack Telecom v1.1.0 APIs are accessible for integration, the system dialer's ability to render native call logs is being introduced in phases, beginning with Google Meet. To safeguard against spam, native dialers utilize secure package allowlists to control VoIP display. For local testing of your callback and logging implementations, we recommend using the open-source [Telecom Sample Dialer app](https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom) as your emulator environment.
Written by:

-

  ## [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/nataraj-k-r) ![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp) ![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp)
Continue reading
- [![View Sheenam Mittal's profile](https://developer.android.com/static/blog/assets/unnamed_24_1859332bf9_Z2nsiJr.webp)](https://developer.android.com/blog/authors/sheenam-mittal) 29 Sep 2026 29 Sep 2026 ![](https://developer.android.com/static/blog/assets/ABL_0137_Strapi_1331188d3a_Z17ea85.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Driving growth on Google Play: The next era of subscriptions](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions)

  [arrow_forward](https://developer.android.com/blog/posts/driving-growth-on-google-play-the-next-era-of-subscriptions) On Google Play, we are continuously expanding our subscription platform to help you drive growth, adapt to new business models, and meet your users exactly where they are.
  [Sheenam Mittal](https://developer.android.com/blog/authors/sheenam-mittal) • 4 min read
  - [#Google Play subscriptions](https://developer.android.com/blog/topics/google-play-subscriptions)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 24 Sep 2026 24 Sep 2026 ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build your way: Use any AI agent of your choice in Android Studio](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio) Last year, Android Studio opened up to any AI model. Today, we're taking the next step by introducing support for your choice of coding agents.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)