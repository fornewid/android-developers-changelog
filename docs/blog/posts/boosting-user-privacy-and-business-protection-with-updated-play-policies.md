---
title: https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies
url: https://developer.android.com/blog/posts/boosting-user-privacy-and-business-protection-with-updated-play-policies
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Boosting user privacy and business protection with updated Play policies

3 min read ![](https://developer.android.com/static/blog/assets/260409_Uyo_policy_bundle_Header_dae9a057fb_ZJmed6.webp) 15 Apr 2026 [![View Bennet Manuel's profile](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_1rYOvj.webp)](https://developer.android.com/blog/authors/bennet-manuel) [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel) Group Product Manager We strive to make Google Play the safest and most trusted experience possible. Today, we're announcing a new set of policy updates and an account transfer feature to boost user privacy and protect your business from fraud. By providing better features for users and easy-to-integrate tools for you, we're making **it simpler to build** **safer apps**so you can focus on creating great experiences.

We're also expanding our features to help you manage new contact and location policy changes, so you have a smoother, more predictable app review experience. By October, Play policy insights in Android Studio can help you proactively identify if your app should use these new features and guide you on the exact steps to take. Additionally, new pre-review checks in the Play Console will be available starting October 27 to flag potential contacts or location permissions policy issues so you can fix them before you submit your app for review.

Here is what is new and how you can prepare.

### Contact Picker: A privacy-friendly way to access contacts

![contact picker.png](https://developer.android.com/static/blog/assets/contact_picker_1f58b5e6d5_Z1abkm7.webp)

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
Written by:

-

  ## [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/bennet-manuel) ![View Bennet Manuel's profile](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_1rYOvj.webp) ![View Bennet Manuel's profile](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_1rYOvj.webp)
Continue reading
- [![View Bennet Manuel's profile](https://developer.android.com/static/blog/assets/Bennet_Manuel_4be9960838_1rYOvj.webp)](https://developer.android.com/blog/authors/bennet-manuel)[![View Robert Clifford's profile](https://developer.android.com/static/blog/assets/robert_clifford_a139ee8d05_Z2wbL3d.webp)](https://developer.android.com/blog/authors/robert-clifford) 11 Dec 2025 11 Dec 2025 ![](https://developer.android.com/static/blog/assets/a11y_rev_37216d57dc_Z1j9hnk.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhancing Android security: Stop malware from snooping on your app data](https://developer.android.com/blog/posts/enhancing-android-security-stop-malware-from-snooping-on-your-app-data)

  [arrow_forward](https://developer.android.com/blog/posts/enhancing-android-security-stop-malware-from-snooping-on-your-app-data) Security is foundational to Android. We partner with you to keep the platform safe and protect user data by offering powerful security tools and features, like Credential Manager and FLAG_SECURE.
  [Bennet Manuel](https://developer.android.com/blog/authors/bennet-manuel), [Robert Clifford](https://developer.android.com/blog/authors/robert-clifford) • 2 min read
- [![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)](https://developer.android.com/blog/authors/jason-buchel) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Blog_0140_strapi_8d85f71a6e_ZvGJv2.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bringing our latest frontier model to Android Developers](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli)

  [arrow_forward](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli) As agentic development accelerates, Android engineering is reaching an exciting new frontier: moving from assistive code completion to agents executing end-to-end under your direction. You have total choice and flexibility in the models and agents you use.
  [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_ZnD5Di.webp)](https://developer.android.com/blog/authors/paul-feng) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Developer_Strapi_Banner_2000x1000_c21932c96a_1wEPmN.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [New ways to drive smarter discovery, deeper engagement, and business growth on Google Play](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth)

  [arrow_forward](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth) Today, we shared how we're taking our "more than a store" vision into its next chapter. From You tab, now the personal home base for over 250M monthly active users, to our unified gaming platform connecting over 700M gamer profiles, Google Play is meeting users wherever they are.
  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 3 min read
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)