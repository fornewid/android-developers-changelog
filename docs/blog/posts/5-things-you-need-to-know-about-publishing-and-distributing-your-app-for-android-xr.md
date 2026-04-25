---
title: https://developer.android.com/blog/posts/5-things-you-need-to-know-about-publishing-and-distributing-your-app-for-android-xr
url: https://developer.android.com/blog/posts/5-things-you-need-to-know-about-publishing-and-distributing-your-app-for-android-xr
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# 5 things you need to know about publishing and distributing your app for Android XR

###### 4-min read

![](https://developer.android.com/static/blog/assets/xr_Week3_12c745cd96_23Hnge.webp) 24 Oct 2025 [![](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_1Ce4cO.webp)](https://developer.android.com/blog/authors/jan-kleinert) [##### Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert)

###### Developer Relations Engineer

[*Samsung Galaxy XR is here*](https://android-developers.googleblog.com/2025/10/giving-your-apps-new-home-on-samsung.html)*, powered by Android XR! This blog post is part of our *[*Android XR Spotlight Week*](https://android-developers.googleblog.com/2025/10/welcome-to-android-xr-spotlight-week.html)*, where we provide resources---blog posts, videos, sample code, and more---all designed to help you learn, build, and prepare your apps for Android XR. *

Today, we're focusing on one of the last steps in your development journey, ensuring these experiences successfully reach your users. Publishing correctly ensures your app is packaged efficiently, discovered by the right devices, and presented in the best possible light.

Here are 5 things you need to know about publishing and distributing your app for Android XR on Google Play.

## 1. Uphold quality with the Android XR app quality guidelines

One of the most important steps before publishing is ensuring your app delivers a safe, comfortable, and performant user experience.

Following the[Android XR App Quality Guidelines](https://developer.android.com/docs/quality-guidelines/android-xr) helps ensure that your app provides users with a great experience on devices like the Galaxy XR.

## Why quality matters

These guidelines build upon the [large screen app quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality), and focus on critical XR-specific criteria including:

- **Safety and comfort:** This is paramount. These guidelines help you avoid causing motion sickness by setting standards for camera movement and frame rates, and by limiting visual elements like strobing.
- **Performance:** Your app must hit performance metrics, such as target frame rates, to prevent lag and ensure a fluid, comfortable experience.
- **Interaction:** The guidelines specify recommended minimum sizes for interactive targets (e.g., 48dp minimum, 56dp recommended) to work well with eye-tracking and hand-tracking inputs.

*** ** * ** ***

## 2. Configure your app manifest correctly

The [AndroidManifest.xml file](https://developer.android.com/guide/topics/manifest/manifest-intro) describes important information about your app. The Android build tools, Android system, and Google Play use this information to know what kind of experience you've built and which hardware features it requires. Proper configuration is vital for correct device targeting and app launch.

## Specify which Android XR SDK your app uses

In your app manifest, include `android.software.xr.api.spatial` or `android.software.xr.api.openxr` to indicate whether you're building with the Jetpack XR SDK or building with OpenXR or Unity.

|---|---|
| **SDK used** | **Manifest declaration** |
| Jetpack XR SDK | [`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/get-started#android.software.xr.api.spatial) |
| OpenXR or Unity | [`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/get-started#android.software.xr.api.openxr) |

If your app is built using OpenXR or Unity, you must set the `android:required` attribute to `true`**.** For apps built with the Jetpack XR SDK, set `android:required` attribute to `true` if your app is published to the Android XR dedicated release track and set `android:required` attribute to `false`if your app is published to the mobile release track.

## Set the activity start mode

Use the `android.window.PROPERTY_XR_ACTIVITY_START_MODE` property on your main activity to define the default user environment:

|---|---|---|
| **Start mode** | **Purpose** | **SDK** |
| `XR_ACTIVITY_START_MODE_HOME_SPACE` | Launches your app in Home Space, the shared multitasking environment. | Jetpack XR SDK |
| `XR_ACTIVITY_START_MODE_FULL_SPACE_MANAGED` | Launches in Full Space, a full-immersion, single-app environment. | Jetpack XR SDK |
| `XR_ACTIVITY_START_MODE_FULL_SPACE_UNMANAGED` | Launches in Full Space, a full-immersion, single-app environment. Note that apps built with OpenXR or Unity **always** run in Full Space. | OpenXR or Unity |

## Check for optional hardware features at runtime

Avoid setting optional XR features (like hand tracking or controllers) to `android:required="true"` unless they are truly required for your app. If a device doesn't support a required feature, Google Play will hide your app from that device. If you have features set as required but your app could operate without them, then you could unnecessarily limit your audience.

Instead, check for advanced features dynamically at runtime using the `PackageManager` class with `hasSystemFeature()`:

```kotlin
Kotlin

val hasHandTracking = packageManager.hasSystemFeature("android.hardware.xr.input.hand_tracking")

if (hasHandTracking) {

    // Enable high-fidelity hand tracking features

} else {

    // Provide a fallback experience

}
```

This ensures your app is broadly compatible and leverages advanced features when they're available.

*** ** * ** ***

## 3. Use Play Asset Delivery (PAD) to deliver large assets

Immersive apps and games often contain large assets that might exceed the standard [size limits](https://support.google.com/googleplay/android-developer/answer/9859372#size_limits). Use[Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery) (PAD) to manage large, high-fidelity assets. PAD offers flexible delivery modes: install-time, fast follow, and on demand for progressive download of content. Apps that are built for Android XR are allowed to deliver additional asset packs: instead of a cumulative total of 4 GB for asset packs delivered on demand or fast follow, these apps are afforded a higher cumulative total of 30 GB.

For developers building with Unity, use [Unity Addressables](https://developer.android.com/guide/playcore/asset-delivery/integrate-unity) along with Play Asset Delivery to manage asset packs.

*** ** * ** ***

## 4. Showcase your app with spatial video previews

To capture the attention of users browsing the Play Store on their XR headsets, you can provide an immersive preview of your app using a [spatial video asset](https://support.google.com/googleplay/android-developer/answer/9866151#zippy=%2Cpreview-video). This must be a 180°, 360°, or stereoscopic video. On Android XR devices, the Play Store will automatically display this as an immersive 3D preview, allowing users to experience the depth and scale of your content before they install the app.

*** ** * ** ***

## 5. Choose your Google Play release track

Google Play provides two pathways for publishing your Android XR app, both using the same Play Console account:

## Option A: Continue on the mobile release track (for spatialized mobile apps)

If you are adding spatial XR features to an existing mobile app, you can often bundle the XR features or content into your existing Android App Bundle (AAB).

This approach is ideal if your app maintains most of its core functionality across both mobile and XR devices, and you can continue publishing the same AAB to the mobile track. Review [this guidance](https://developer.android.com/develop/xr/package-and-distribute#mobile-track) to be sure you are properly configuring your app's manifest file to support this use case.

## Option B: Publish to the dedicated Android XR release track

If you are building a brand-new app for XR or if the XR version is functionally too different for a single AAB, you should [publish to the Android XR dedicated release track](https://developer.android.com/develop/xr/package-and-distribute#xr-track).

Apps published to the Android XR dedicated release track are only visible to Android XR devices that support the [`android.software.xr.api.spatial`](https://developer.android.com/develop/xr/get-started#android.software.xr.api.spatial) feature or the [`android.software.xr.api.openxr`](https://developer.android.com/develop/xr/get-started#android.software.xr.api.openxr) feature, giving you control over distribution.

By following this guidance, you can help ensure your innovative Android XR apps provide a quality user experience, are packaged efficiently, are delivered smoothly using PAD, and are targeted to the devices that can run them. Happy publishing!

###### Written by:

-

  ## [Jan Kleinert](https://developer.android.com/blog/authors/jan-kleinert)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jan-kleinert) ![](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_1Ce4cO.webp) ![](https://developer.android.com/static/blog/assets/Jan_Kleinert_044ab3d483_1Ce4cO.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/niharika_2910f6d612_C99s1.webp)](https://developer.android.com/blog/authors/niharika-arora)[![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/jean-pierre-pralle) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/Streamline_user_animation_V02_Strapi_abd12985d7_SvAX9.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Streamline User Journeys with Verified Email via Credential Manager](https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager)

  [arrow_forward](https://developer.android.com/blog/posts/streamline-user-journeys-with-verified-email-via-credential-manager) Today, we're excited to announce a new verified email credential issued by Google, which developers can now retrieve directly from Android's Credential Manager Digital Credential API.

  ###### [Niharika Arora](https://developer.android.com/blog/authors/niharika-arora), [Jean-Pierre Pralle](https://developer.android.com/blog/authors/jean-pierre-pralle) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Android CLI and skills: Build Android apps 3x faster using any agent](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent) Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.

  ###### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando), [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal) •
  4 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)