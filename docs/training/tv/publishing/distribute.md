---
title: https://developer.android.com/training/tv/publishing/distribute
url: https://developer.android.com/training/tv/publishing/distribute
source: md.txt
---

If your apps meet the core app quality guidelines on Android devices and provide
a high-quality experience for Android TV devices, your apps appear on Google
Play and can be discovered on Android TV and Google TV.

This guide describes how to distribute your app to Android TV by performing the
following tasks:

- Prepare your app for distribution.
- Opt in to Android TV and publish using the Play Console.
- Track your review and approval status.

## Prerequisites

Before you distribute your app to Android TV users, verify that you meet the
following requirements.

### Meet quality guidelines

Verify that your app meets the [Android TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality)
guidelines. Meeting these criteria helps your app provide a high-quality
experience and makes it eligible for discovery on Google Play.

For general information about preparing for launch on Google Play, see the
[Launch Checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist).

### Check 64-bit compatibility

From August 1, 2026, your TV app must support both
[64-bit architectures](https://developer.android.com/google/play/requirements/64-bit) and [16 KB page sizes](https://developer.android.com/guide/practices/page-sizes).

### Check package names

If you have an existing app on Google Play for mobile devices, you can continue
to use the same package name for your Android TV app. Using the same package
name for your mobile app and Android TV app is strongly recommended for the
following reasons:

- Doing so makes it easier for you to manage your store listings and releases for both apps. You can reuse your app description and other assets from your mobile app for your TV app. You can use [a dedicated TV track](https://support.google.com/googleplay/android-developer/answer/13295490) to control the release of your TV app separately from your mobile app.
- If your app is built using [adaptive app principles](https://developer.android.com/adaptive-apps), or if you do so in the future, using the same package name for both apps lets you update your app to support different form factors using a single app bundle.

## Opt in to Android TV and publish

When you are ready to publish, follow these steps in the Play Console to opt in
to Android TV and submit your app for review.

1. **Upload your app bundle:** Upload your Android app bundle (AAB) that includes support for Android TV.
2. **Update your store listing:**
   - **Screenshots:** Add at least one Android TV screenshot. These must comply with the [screenshot requirements](https://support.google.com/googleplay/android-developer/answer/9866151#zippy=%2Cscreenshots).
   - **Banner:** Add an [Android TV banner graphic](https://developer.android.com/training/tv/start/start#banner).
   - **Description:** Mention "Android TV" in your app's description.
3. **Opt in to Android TV:**
   1. Go to **Setup \> Advanced Settings**.
   2. Select the **Form Factors** tab.
   3. Click **Add Release Type** and select **Android TV**.
   4. Confirm your opt-in and agree to the review policy.
4. **Start rollout:** You can now begin rolling out your TV app.

| **Note:** Check that your app meets all requirements to avoid being rejected after it's reviewed for Android TV quality.

### Results

After you opt in and publish, Google Play submits your app for review against
the [Android TV app quality criteria](https://developer.android.com/docs/quality-guidelines/tv-app-quality) and notifies you of the
result.

If your app meets the technical and quality criteria for Android TV, as
described in this document, your app becomes discoverable for users on Android
TV devices. If your app doesn't meet the criteria, you receive a notification
email that is sent to your developer account address with a summary of the areas
that you need to address. When you've made the necessary adjustments, you can
upload a new version of your app for review.

At any time, you can check the review and approval status of your app in the
Play Console, under **Android TV** in the app's **Pricing and Distribution**
page.

There are three approval states:

- **Pending:** Your app was sent for review and the review is not yet complete.
- **Approved:** Your app was reviewed and approved. The app becomes discoverable to Android TV users.
- **Not approved:** Your app was reviewed and not approved. Check the notification email for information about why the app was not approved. You can address any issues and opt in and publish again to initiate another review.

## See also

- [Android TV app quality](https://developer.android.com/docs/quality-guidelines/tv-app-quality)
- [Launch checklist](https://developer.android.com/distribute/best-practices/launch/launch-checklist)