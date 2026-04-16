---
title: https://developer.android.com/blog/posts/android-16-qpr-2-is-released
url: https://developer.android.com/blog/posts/android-16-qpr-2-is-released
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Android 16 QPR2 is Released

###### 4-min read

![](https://developer.android.com/static/blog/assets/a16released_7cb13cc79d_23qyL9.webp) 02 Dec 2025 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

Android 16 QPR2 is Released

Faster Innovation with Android's first Minor SDK Release

Today we're releasing Android 16 QPR2, bringing a host of enhancements to user experience, developer productivity, and media capabilities. It marks a significant milestone in the evolution of the Android platform as **the** [**first release to utilize a minor SDK version**](https://android-developers.googleblog.com/2024/10/android-sdk-release-update.html)**.**

## A Milestone for Platform Evolution: The Minor SDK Release

Minor SDK releases allow us to deliver APIs and features more rapidly outside of the major yearly platform release cadence, ensuring that the platform and your apps can innovate faster with new functionality. Unlike major releases that may include behavior changes impacting app compatibility, the changes in QPR2 are largely additive, minimizing the need for regression testing. Behavior changes in QPR2 are largely focused on security or accessibility, such as SMS OTP protection, or the support for the expanded dark theme.

To support this, we have introduced new fields to the `Build` class as of Android 16, allowing your app to check for these new APIs using `SDK_INT_FULL` and `VERSION_CODES_FULL`.

```
if ((Build.VERSION.SDK_INT >= Build.VERSION_CODES.BAKLAVA) && (Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.BAKLAVA_1)) {
    // Call new APIs from the Android 16 QPR2 release
}
```

## Enhanced User Experience and Customization

QPR2 improves Android's personalization and accessibility, giving users more control over how their devices look and feel.

## Expanded Dark Theme

To create a more consistent user experience for users who have low vision, photosensitivity, or simply those who prefer a dark system-wide appearance, QPR2 introduced an expanded option under dark theme.
![image.png](https://developer.android.com/static/blog/assets/image_d2ad547106_FLznI.webp)

The old Fitbit app showing the impact of expanded dark theme; the new Fitbit app directly supports a dark theme

When the expanded dark theme setting is enabled by a user, the system uses your app's isLightTheme theme attribute to determine whether to apply inversion. If your app [inherits from one of the standard DayNight themes](https://developer.android.com/develop/ui/views/theming/darktheme#support-dark-theme), this is done automatically for you. If it does not, make sure to declare `isLightTheme="false"` in your dark theme to ensure your app is not inadvertently inverted. Standard Android Views, Composables, and WebViews will be inverted, while custom rendering engines like Flutter will not.

This is largely intended as an accessibility feature. We strongly recommend implementing a native dark theme, which gives you full control over your app's appearance; you can protect your brand's identity, ensure text is readable, and prevent visual glitches from happening when your UI is automatically inverted, guaranteeing a polished, reliable experience for your users.

## Custom Icon Shapes \& Auto-Theming

In QPR2, users can select specific shapes for their app icons, which apply to all icons and folder previews. Additionally, if your app does not provide a dedicated themed icon, the system can now automatically generate one by applying a color filtering algorithm to your existing launcher icon.
![image.png](https://developer.android.com/static/blog/assets/image_929bed7f05_1nIksG.webp)

## Interactive Chooser Sessions

The sharing experience is now more dynamic. Apps can keep the UI interactive even when the system sharesheet is open, allowing for real-time content updates within the Chooser.

## Boosting Your Productivity and App Performance

We are introducing tools and updates designed to streamline your workflow and improve app performance.

## Linux Development Environment with GUI Applications

The Linux development environment feature has been expanded to support running Linux GUI applications directly within the terminal environment.
![image.png](https://developer.android.com/static/blog/assets/image_6ba40ffe74_ZytA5.webp)

Wilber, the GIMP mascot, designed by Aryeom Han, is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The screenshot of the GIMP interface is used with courtesy.

## Generational Garbage Collection

The Android Runtime (ART) now includes a Generational Concurrent Mark-Compact (CMC) Garbage Collector. This focuses collection on newly allocated objects, resulting in reduced CPU usage and improved battery efficiency.

## Widget Engagement Metrics

You can now [query user interaction events](https://developer.android.com/develop/ui/compose/glance/metrics)---such as clicks, scrolls, and impressions---to better understand how users engage with your widgets.

## 16KB Page Size Readiness

To help prepare for future architecture requirements, we have added early warning dialogs for debuggable apps that are not 16KB page-aligned.
![image.png](https://developer.android.com/static/blog/assets/image_93c4af378a_2d2xhB.webp)

## Media, Connectivity, and Health

QPR2 brings robust updates to media standards and device connectivity.

## IAMF and Audio Sharing

We have added software decoding support for Immersive Audio Model and Formats (IAMF), an open-source spatial audio format. Additionally, Personal Audio Sharing for Bluetooth LE Audio is now integrated directly into the system Output Switcher.
![image.png](https://developer.android.com/static/blog/assets/image_7428c09460_ZuCMrK.webp)

## **Health Connect Updates**

Health Connect now automatically tracks steps using the device's sensors. If your app has the READ_STEPS permission, this data will be available from the "android" package. Not only does this simplify the code needed to do step tracking, it's also more power efficient. It also can now track weight, set index, and Rate of Perceived Exertion (RPE) in exercise segments.

## Smoother Migrations

A new 3rd-party Data Transfer API enables more reliable data migration between Android and iOS devices.

## Strengthening Privacy and Security

Security remains a top priority with new features designed to protect user data and device integrity.

## Developer Verification

We introduced APIs to support developer verification during app installation along with new ADB commands to simulate verification outcomes. **As a developer, you are free to install apps without verification by using ADB, so you can continue to test apps that are not intended or not yet ready to distribute to the wider consumer population.**

## SMS OTP Protection

The delivery of messages containing an [SMS retriever hash](https://developers.google.com/identity/sms-retriever/verify) will be delayed for most apps for three hours to help prevent OTP hijacking. The [RECEIVE_SMS](https://developer.android.com/reference/android/Manifest.permission#RECEIVE_SMS) broadcast will be withheld and [sms provider](https://developer.android.com/reference/android/provider/Telephony.Sms) database queries will be filtered. The SMS will be available to these apps after the three hour delay.

## Secure Lock Device

A new system-level security state, Secure Lock Device, is being introduced. When enabled (e.g., remotely via "Find My Device"), the device locks immediately and requires the primary PIN, pattern, or password to unlock, heightening security. When active, notifications and quick affordances on the lock screen will be hidden, and biometric unlock may be temporarily disabled.

## Get Started

If you're not in the Beta or Canary programs, your Pixel device should get the Android 16 QPR2 release shortly. If you don't have a Pixel device, you can [use the 64-bit system images with the Android Emulator](https://developer.android.com/about/versions/16/get#on_emulator) in Android Studio. If you are currently on the Android 16 QPR2 Beta and have not yet installed the Android 16 QPR3 beta, you can opt out of the program and you will then be offered the release version of Android 16 QPR2 over the air.

For the best development experience with Android 16 QPR2, we recommend that you use the latest Canary build of [Android Studio Otter](https://developer.android.com/studio/preview).

Thank you again to everyone who participated in our Android beta program. We're looking forward to seeing how your apps take advantage of the updates in Android 16 QPR2.

For complete information on Android 16 QPR2 please visit the [Android 16 developer site](https://developer.android.com/about/versions/16).

###### Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp) ![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/Gemma_Android_2x1_2x_a6d27254c4_Z10SxJJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Gemma 4: The new standard for local agentic intelligence on Android](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/gemma-4-the-new-standard-for-local-agentic-intelligence-on-android) Today, we are enhancing Android development with Gemma 4, our latest state-of-the-art open model designed with complex reasoning and autonomous tool-calling capabilities.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 26 Mar 2026 26 Mar 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Third Beta of Android 17](https://developer.android.com/blog/posts/the-third-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-third-beta-of-android-17) Android 17 has officially reached platform stability today with Beta 3. That means that the API surface is locked; you can perform final compatibility testing and push your Android 17-targeted apps to the Play Store.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  5 min read

  - [#Android 17](https://developer.android.com/blog/topics/android-17)
  - [#beta](https://developer.android.com/blog/topics/beta)
- [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 05 Mar 2026 05 Mar 2026 ![](https://developer.android.com/static/blog/assets/android_Bench_f2e4dd4fda_2816Hg.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Elevating AI-assisted Android development and improving LLMs with Android Bench](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench)

  [arrow_forward](https://developer.android.com/blog/posts/elevating-ai-assisted-android-development-and-improving-ll-ms-with-android-bench) We want to make it faster and easier for you to build high-quality Android apps, and one way we're helping you be more productive is by putting AI at your fingertips.

  ###### [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) •
  2 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)