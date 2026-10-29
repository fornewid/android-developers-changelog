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
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Mesa_de_trabajo_1_copy_8_3f8cf8a935_Z1799P4.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Agentic and Flexible: A next era of Android development](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development)

  [arrow_forward](https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development) Today, at the Android Dev Summit, we are announcing the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Rabbit2_Strapi_27563aeaf4_1BAzRM.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Your favorite agents are now integrated in Android Studio](https://developer.android.com/blog/posts/ai-agents-android-studio-integration)

  [arrow_forward](https://developer.android.com/blog/posts/ai-agents-android-studio-integration) Android Studio Rabbit 2 is now stable and ready for you to use in production. This release includes key features to improve your development such as Bring Your Own Agent, new XR Emulator features, a LeakCanary update, a new agent skills manager tool, AI code review, and more.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)](https://developer.android.com/blog/authors/roxanna-walker) 21 Oct 2026 21 Oct 2026 ![](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A more reliable way to add and edit contacts on Android](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)

  [arrow_forward](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android) Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission.
  [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) • 6 min read
  - [#Android](https://developer.android.com/blog/topics/android)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)