---
title: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
url: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha

2 min read ![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_2ewsGa.webp) 14 May 2026 [![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp)](https://developer.android.com/blog/authors/nataraj-k-r.md.txt) [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r.md.txt) Developer Relations Engineer, Android Developer Engineering The initial launch of the Jetpack Telecom library introduced [`CallsManager`](https://developer.android.com/reference/androidx/core/telecom/CallsManager.md.txt), replacing the legacy `ConnectionService` API to simplify VoIP integration. CallsManager streamlines call lifecycle management and audio routing while enabling interactions with remote surfaces like smartwatches, Bluetooth devices, and Android Auto. Additionally, it supports call extensions for richer features---such as participant handling, custom icons, call silencing and meeting summary on remote surfaces ---all while maintaining backward compatibility down to Android O (API Level 26).

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

These integrated logging and callback features are available for devices running **Android 16.1 (SDK 36.1)** and higher. Refer [here](https://developer.android.com/build.md.txt#module-level) to compile your app with Android SDK 36.1.

### **Get Started**

We encourage developers to test these integrations and explore how unified call history and callbacks can improve the daily user experience of your VoIP applications.

To help you get started and see these APIs in action, we have put together a sample application demonstrating the new integrations.

- **View the sample app here:** <https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom>

Check out the [release notes](https://developer.android.com/jetpack/androidx/releases/core.md.txt#core-telecom_version_11_2) and [documentation](https://developer.android.com/develop/connectivity/telecom/call-log-integration.md.txt) to start implementing these features today!

**Note:** : Although Jetpack Telecom v1.1.0 APIs are accessible for integration, the system dialer's ability to render native call logs is being introduced in phases, beginning with Google Meet. To safeguard against spam, native dialers utilize secure package allowlists to control VoIP display. For local testing of your callback and logging implementations, we recommend using the open-source [Telecom Sample Dialer app](https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom) as your emulator environment.
Written by:

-

  ## [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/nataraj-k-r) ![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp) ![View Nataraj K R's profile](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_2qRRKe.webp)
Continue reading
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi.md.txt) 05 Nov 2026 05 Nov 2026 ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [What's new in intelligent apps at the Android Developer Summit](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads.md.txt) In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt) • 4 min read
  - [#Android MCP](https://developer.android.com/blog/topics/android-mcp.md.txt)
  - [#Gemini Nano](https://developer.android.com/blog/topics/gemini-nano.md.txt)
  - [#ML Kit](https://developer.android.com/blog/topics/ml-kit.md.txt)
  - [#Connected Apps](https://developer.android.com/blog/topics/connected-apps.md.txt)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)