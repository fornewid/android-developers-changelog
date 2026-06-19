---
title: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
url: https://developer.android.com/blog/posts/bring-native-visibility-to-your-vo-ip-app-experience-with-telecom-s-latest-alpha
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha

###### 2-min read

![](https://developer.android.com/static/blog/assets/Bring_Native_Visibilityto_Your_Vo_IP_App_Experience_Strapi_4359a69748_Z2wOXhv.webp) 14 May 2026 [![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp)](https://developer.android.com/blog/authors/nataraj-k-r) [##### Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r)

###### Developer Relations Engineer, Android Developer Engineering

The initial launch of the Jetpack Telecom library introduced [`CallsManager`](https://developer.android.com/reference/androidx/core/telecom/CallsManager), replacing the legacy `ConnectionService` API to simplify VoIP integration. CallsManager streamlines call lifecycle management and audio routing while enabling interactions with remote surfaces like smartwatches, Bluetooth devices, and Android Auto. Additionally, it supports call extensions for richer features---such as participant handling, custom icons, call silencing and meeting summary on remote surfaces ---all while maintaining backward compatibility down to Android O (API Level 26).

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

![integrated_call_log.png](https://developer.android.com/static/blog/assets/integrated_call_log_2d23491534_gNJuR.webp)

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

###### Written by:

-

  ## [Nataraj K R](https://developer.android.com/blog/authors/nataraj-k-r)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/nataraj-k-r) ![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp) ![](https://developer.android.com/static/blog/assets/Nataraj_K_work_profile_20e513e403_Z1TR4EY.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_9c798f0c1d_Z1m5WWD.webp)](https://developer.android.com/blog/authors/matthew-forsythe) 18 Jun 2026 18 Jun 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2x_325a484212_1BGPPB.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android developer verification: Building a safer ecosystem together](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together)

  [arrow_forward](https://developer.android.com/blog/posts/android-developer-verification-building-a-safer-ecosystem-together) Last year, we introduced Android developer verification to strengthen ecosystem security and stop malicious actors from hiding behind anonymity to release harmful apps.

  ###### [Matthew Forsythe](https://developer.android.com/blog/authors/matthew-forsythe) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Stevan_Silva_7661118077_V4WGm.webp)](https://developer.android.com/blog/authors/stevan-silva)[![](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_2kh65s.webp)](https://developer.android.com/blog/authors/vinny-da-silva) 15 Jun 2026 15 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_D_Android_XR_Strapi_39d27725e6_Zhwmdd.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-android-xr-tooling-engine-support-and-ecosystem-updates) From augmented overlays to fully immersive environments, the Android XR ecosystem is expanding rapidly, with the Samsung Galaxy XR already available today.

  ###### [Stevan Silva](https://developer.android.com/blog/authors/stevan-silva), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva) •
  3 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Developer Preview 4](https://developer.android.com/blog/topics/developer-preview-4)
- [![](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_ZDTMlF.webp)](https://developer.android.com/blog/authors/simona-milanovic) 09 Jun 2026 09 Jun 2026 ![](https://developer.android.com/static/blog/assets/MM_Dev_Productivity_Strapi_b7e79722e6_45umk.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top 3 updates for Android developer productivity](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity)

  [arrow_forward](https://developer.android.com/blog/posts/top-3-updates-for-android-developer-productivity) Every year, Google I/O brings new announcements and resources across ecosystems and products, including Android development. As development shifts toward AI and agent-assisted tooling, we've expanded our offerings to better support you, however you decide to build for Android.

  ###### [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)