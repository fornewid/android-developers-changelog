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