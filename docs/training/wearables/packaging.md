---
title: https://developer.android.com/training/wearables/packaging
url: https://developer.android.com/training/wearables/packaging
source: md.txt
---

This document contains directions and best practices for distributing Wear OS
apps on the Play Store.

## Play Store prerequisites

Wear OS APKs are separate from mobile APKs, and are uploaded and updated
independently from within the Play Console.

To be published on the Play Store, Wear OS APKs must meet the following
requirements.

### Unique version code

Since a watch APK's version code must be unique across all form factors, we
recommend that its version code scheme is independent of any other form factor
in your Play Console.

Here is an example scheme:

- First 2 numbers: [`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target):
  - `36[xxx][yy][zz]`
- Next numbers: product version:
  - `36152[yy][zz]`
- Next numbers: release number:
  - `3615202[zz]`
- Final numbers: your Wear OS app version:
  - `361520203`

If you have a phone APK in addition to a watch APK, you must use the [Multi-APK
delivery method](https://developer.android.com/training/wearables) to manage both. To learn more about versioning for multiple
APKs, see [Rules for Multiple APKs](https://developer.android.com/google/play/publishing/multiple-apks#Rules), and to verify that your gradle
configuration sets versions correctly, see [Set app version information](https://developer.android.com/studio/publish/versioning#appversioning).

### Set up targeting for a watch

For the Play Store to recognize your app as a Wear OS app, you must declare a
specific `<uses-feature>` tag in your app's manifest file. This element must be
a direct child of the root `<manifest>` tag, with its `android:name` attribute
set to `android.hardware.type.watch`:

<br />

```xml
<uses-feature android:name="android.hardware.type.watch" />
```

<br />

> [!CAUTION]
> **Caution:** Don't set the `required` attribute to `false` for this element, because this results in a single APK across devices that run Android and Wear OS, which isn't a supported configuration.

In addition to declaring the `android.hardware.type.watch` feature in your
manifest, you can also filter by criteria like SDK version, screen resolution,
and CPU architecture. See [Filters on Google Play](https://developer.android.com/google/play/filters) for details.

### Specify the standalone setting

Your `AndroidManifest.xml` file must declare whether your watch app is
standalone. A standalone app is fully usable without a paired phone. All of its
core functions, such as authentication, work locally on the watch.

To do this, add a `<meta-data>` element inside your `<application>` tag. Set the
name to `com.google.android.wearable.standalone` and the value to either true or
false.

<br />

```xml
<meta-data
    android:name="com.google.android.wearable.standalone"
    android:value="true" />
```

<br />

If the value of `com.google.android.wearable.standalone` is `false`, the app
is still downloadable from the Play Store, but it requires its
companion mobile app for it to be usable. To learn more about standalone Wear
development, see [Standalone versus Non-Standalone Wear OS Apps](https://developer.android.com/training/wearables/apps/standalone-apps).

## Development validation

To prepare for a successful launch on Wear OS, review the [Wear OS development
resources](https://developer.android.com/training/wearables) and the [Wear OS design](https://developer.android.com/design/ui/wear) guidance, and verify that your app
adheres to the [Wear OS quality standards](https://developer.android.com/docs/quality-guidelines/wear-app-quality).

### Valid packaging

If you have an existing mobile app, verify that you have used
**the same package name** for your Wear OS app.

We recommend that you use the same Play Store listing as your mobile app,
because this improves the discoverability of your Wear OS app by linking it to
the reviews and ratings of your mobile app.

### Comprehensive testing

To provide a great user experience, your app should be designed to perform well
and look great on all Wear OS devices.

Set up your testing environment as early as possible, and test on a variety of
devices, versions, and test types throughout design and development. We strongly
recommend testing on both emulators and physical devices from all major Wear OS
OEMs.

### Quality standards validation

Verify that your app adheres to all [Wear OS Quality Standards](https://developer.android.com/docs/quality-guidelines/wear-app-quality), and perform
user QA testing to verify ease of use and general quality.

If these standards are not met, your app will be rejected during the [Play Store
review](https://developer.android.com/training/wearables/packaging#play-store-reviews) process.

High-quality Wear OS apps are highlighted by the Play Store with top app charts
and curated featured collections. To be eligible for these, make sure your Wear
OS app functions as a standalone app, and meets all quality standards.

### Special topic: Requirements for kid-friendly experiences

Select devices on Wear OS support a kid-friendly experience, which enables the
watch and its associated apps to operate on a fully standalone basis using LTE
and, when available, Wi-Fi connectivity. This includes calling, texting, and
games. To publish a kid-friendly experience for your app or watch face on the
Play Store, it must meet the following additional requirements:

- **Age and content rating:** Apps and watch faces that are designed for kids must meet the [age and content requirements](https://support.google.com/googleplay/android-developer/answer/9867159#declare_target_age_group) that are appropriate to their functionality.
- **Standalone functionality:** Apps must set `com.google.android.wearable.standalone` to `true`, as described in the section about [specifying an app's standalone setting](https://developer.android.com/training/wearables/packaging#specifying-app-as-standalone). They must also meet all [associated requirements for standalone apps](https://developer.android.com/training/wearables/apps/standalone-apps#identify), which take effect when the watch is set up with a [child account](https://support.google.com/families/answer/7103338).
- **Watch Face Format:** If you are developing a watch face for kids, it must be created using [Watch Face Format](https://developer.android.com/training/wearables/wff).

For more information about creating kid-friendly experiences, see the
[development guidelines](https://developer.android.com/training/wearables/kids/develop).

> [!CAUTION]
> **Caution:** If you implement an authentication solution in a kid-friendly experience, you cannot use [Google Sign-in](https://developer.android.com/training/wearables/apps/auth-wear#Google-Sign-in) because it's not compatible with child accounts.

## Distribution

The following sections provide an overview of how to publish and distribute your
Wear OS app using the [Play Console](https://play.google.com/console/). For more detailed instructions, refer
to the steps in [Prepare and stage a release](https://support.google.com/googleplay/android-developer/answer/9859348).

If you are new to the Play Console, use the [Google Play Console overview](https://developer.android.com/distribute/console#manage) to
get started, and use the Play Store [Launch Checklist](https://play.google.com/console/about/guides/releasewithconfidence/) to stay on track.

### Set up the Play Console for Wear OS

To make your app listing appear in the Play Store, upload your Wear OS
APK in the Play Console. To set this up, follow these steps:

1. In the Play Console for your app, click the **Test and release** menu in the navigation panel.
2. Choose **Advanced Settings** , select the **Form factors** tab, and click **Add form factor**.
3. Click **Wear OS**, and follow the steps to add Wear OS screenshots to your Play Store listing.

### Release to a test track

To make your app available to users on the Play Store, you must complete closed
testing to test pre-release versions of your app with your own groups of
testers. See our [Closed testing guide](https://support.google.com/googleplay/android-developer/answer/9845334) to learn more.

After you release your app to a test track, the Play Console prepares a
pre-launch report. This report contains results from stability, accessibility,
and security tests on emulated and physical devices, and performance tests on
physical devices.

Use the results of this pre-launch report to improve your app quality.

### Opt-in and publish

Once you have a release in your closed testing track, you can opt in to Wear OS
and agree to the review policy in the **Advanced Settings** menu.

After opting in to Wear OS, select **Start rollout** to distribute your app.

#### Considerations

- Users can download Wear OS apps either directly from their watch, or
  remotely from the Play Store on their phone or desktop.

- When you push an update to the Play Console, the app updates automatically
  for users who have automatic updates enabled. Users can also update apps
  manually in the Play Store.

- If your app includes tiles or complications, you also need to mention your
  app's support for them in your listing.

## Play Store reviews

After you publish your app, the Play Store review process begins.

### Check review \& approval status

At any time, you can check the review and approval status of your app in the
Play Console, on your app's **Pricing and Distribution** page, under the Wear OS
section.

There are three approval states:

- **Pending:** Your app was sent for review and the review is not yet complete.
- **Approved:** Your app was reviewed and approved. The app becomes discoverable to Wear OS users.
- **Not approved:** Your app was reviewed and not approved. You'll receive a notification email sent to your developer account address with a summary of the issues that you need to address. After you fix the issues, opt in and then publish again to start another review.

### Most common Play Store rejection reasons

The following table contains the most common reasons for Play Store rejections.

| Reason | Explanation |
|---|---|
| **Doesn't mention "Wear OS" in the Play Store listing** | You must mention "Wear OS" in your app's store listing. |
| **Basic functionality is broken** | The app doesn't function as advertised, or the screenshots are inaccurate and don't reflect the actual app. Thoroughly test your app with an emulator and a physical device. |
| **No Wear screenshot** | You must upload at least one screenshot that shows the app running on a Wear OS device. This can be done [from Android Studio](https://developer.android.com/studio/debug/am-screenshot). |
| **Not formatted for round displays** | The app's layout renders incorrectly on a round display, and the Play Store listing doesn't specify this limitation. Use the [Open the Layout Inspector](https://developer.android.com/studio/debug/layout-inspector) in Android Studio to make sure that layouts render correctly |
| **Missing functionality requirements** | Commonly missed functionality requirements, such as malformatted Wear OS notifications or missing [`RemoteInput`](https://developer.android.com/reference/androidx/core/app/RemoteInput) for [messaging apps](https://developer.android.com/training/wearables/notifications#wearable-only-actions) replies. |