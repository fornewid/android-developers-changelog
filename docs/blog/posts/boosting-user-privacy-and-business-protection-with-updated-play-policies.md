---
title: https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies
url: https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Boosting user privacy and business protection with updated Play policies

###### 3-min read

![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_2u7Yfb.webp) 15 Apr 2026 [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel) [##### Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel)

###### Group Product Manager

We strive to make Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud. By providing better features for users and easy-to-integrate tools for you, we're making **it simpler to build** **safer apps**so you can focus on creating great experiences.

We're also expanding our features to help you manage new contact and location policy changes, so you have a smoother, more predictable app review experience. By October, Play policy insights in Android Studio can help you proactively identify if your app should use these new features and guide you on the exact steps to take. Additionally, new pre-review checks in the Play Console will be available starting October 27 to flag potential contacts or location permissions policy issues so you can fix them before you submit your app for review.

Here is what is new and how you can prepare.

### Contact Picker: A privacy-friendly way to access contacts

![contact picker.png](https://developer.android.com/static/blog/assets/contact_picker_1f58b5e6d5_2wDTSI.webp)

Android is introducing the [Android Contact Picker](https://android-developers.googleblog.com/2026/03/contact-picker-privacy-first-contact.html) as the new standard for accessing contact information (e.g., for invites, sharing, or one-time lookups). This picker lets users share only the specific contacts they want to, helping build trust and protect privacy. Alongside this tool, we are updating our [policy](https://support.google.com/googleplay/android-developer/answer/16909972#contacts-permissions) to require that all applicable apps use the picker, or other privacy-focused alternatives like [Sharesheet](https://developer.android.com/training/sharing/send), as the primary way to access users' contacts. `READ_CONTACTS` will be reserved for apps that can't function without it.

#### What you'll need to do

- If your app asks for access to contacts for features like sharing or inviting, you should update your code to use the picker and remove the `READ_CONTACTS` permission entirely (if targeting Android 17 and above).
- If your app requires full, ongoing access to a user's contact list to function, you must justify this need by submitting a Play Developer Declaration in the Play Console. This form will be available before October.

### Location button: More privacy-friendly way to access location

Android is introducing a [new, streamlined location button](https://android-developers.googleblog.com/2026/03/location-privacy.html) to make requesting precise data easier for one-time actions, like finding a store or tagging a photo. This feature replaces complex permission dialogs with a single tap, helping users make clearer choices about how much information they share and for how long. We're updating our [policy](https://support.google.com/googleplay/android-developer/answer/16909972#location-permissions) to require apps to use this button for one-time precise location access unless they require persistent, always-on location access. This creates a faster, more predictable experience for your users and reduces the friction of traditional permission requests.

#### What you'll need to do:

- Review your app's location usage to ensure you are requesting the minimum amount of location data needed for your app to work.
- If your app targets Android 17 and above and uses precise location for discrete, temporary actions, implement the location button by adding the `onlyForLocationButton` flag in your manifest.
- If your app requires persistent precise location to function, you will need to submit a Play Developer Declaration in Play Console to show why the new button or coarse location isn't sufficient for your app's core features. This form will be available before October.

### Account Transfer: Protecting your business

You asked for a secure way to transfer app ownership during business changes, and we listened. We're launching an official account transfer feature directly in Play Console that's designed to help you easily transfer ownership during sales and mergers while also protecting your business from fraud. Starting May 27, account ownership changes must use this official feature. That means that unofficial transfers (like sharing login credentials or buying and selling accounts on third-party marketplaces) which leave your business vulnerable are not permitted.

#### What you'll need to do:

- Initiate any future account owner changes through the "Users and permissions" page in Play Console.
- Every transfer will include a mandatory 7-day security cool-down period. This gives your team time to spot and cancel any unauthorized attempts to take over your account. See [Transferring ownership of a Play Console developer account](https://support.google.com/googleplay/android-developer/answer/16909862) for more guidance.

### What's next

We want to give you plenty of time to review these changes and update your apps. For more information, deadlines, and the full list of Google Play policy updates we're announcing today, please visit the [Policy Announcements](https://support.google.com/googleplay/android-developer/answer/16926792)page.

Thank you for your partnership in keeping Play safe for everyone.

###### Written by:

-

  ## [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/bennet-manuel) ![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp) ![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_MydbH.webp)](https://developer.android.com/blog/authors/bennet-manuel)[![](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_N2ze5.webp)](https://developer.android.com/blog/authors/robert-clifford) 11 Dec 2025 11 Dec 2025 ![](https://developer.android.com/static/blog/assets/a11y_rev_37216d57dc_Z211KeA.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhancing Android security: Stop malware from snooping on your app data](https://developer.android.com/blog/posts/enhancing-android-security-stop-malware-from-snooping-on-your-app-data)

  [arrow_forward](https://developer.android.com/blog/posts/enhancing-android-security-stop-malware-from-snooping-on-your-app-data) Security is foundational to Android. We partner with you to keep the platform safe and protect user data by offering powerful security tools and features, like Credential Manager and FLAG_SECURE.

  ###### [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel), [Robert Clifford](https://developer.android.com/blog/authors/robert-clifford) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.

  ###### [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) •
  2 min read

  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.

  ###### [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) •
  4 min read

  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)