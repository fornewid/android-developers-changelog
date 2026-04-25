---
title: https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17
url: https://developer.android.com/blog/posts/prepare-your-app-for-the-resizability-and-orientation-changes-in-android-17
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Prepare your app for the resizability and orientation changes in Android 17

###### 6-min read

![](https://developer.android.com/static/blog/assets/a17beta_bfff40b895_20Bzrw.webp) 13 Feb 2026 [![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) [##### Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

###### Developer Relations Engineer

With the release of Android 16 in 2025, we shared our vision for a device ecosystem where apps adapt seamlessly to any screen---whether it's a phone, foldable, tablet, desktop, car display, or XR. Users expect their apps to work everywhere. Whether multitasking on a tablet, unfolding a device to read comfortably, or running apps in a desktop windowing environment, users expect the UI to fill the available display space and adapt to the device posture.

We [introduced significant changes](https://android-developers.googleblog.com/2025/01/orientation-and-resizability-changes-in-android-16.html) to orientation and resizability APIs to facilitate adaptive behavior, while providing a temporary opt-out to help you make the transition. We've already seen many developers successfully adapt to this transition when targeting API level 36.

Now with the release of the Android 17 Beta, we're moving to the next phase of our adaptive roadmap: **Android 17 (API level 37) removes the developer opt-out for orientation and resizability restrictions on large screen devices** (sw \> 600 dp). When you target API level 37, your app must be capable of adapting to a variety of display sizes.

The behavior changes ensure that the Android ecosystem offers a consistent, high-quality experience on all device form factors.

### **What's changing in Android 17**

Apps targeting Android 17 must ensure their compatibility with the phase out of manifest attributes and runtime APIs introduced in Android 16. We understand for some apps this may be a big transition, so we've included best practices and tools for helping avoid common issues later in this blog post.

No new changes have been introduced since Android 16, but the developer opt-out is no longer possible. As a reminder: when your app is running on a large screen---where *large screen* means that the smaller dimension of the display is greater than or equal to 600 dp---the following manifest attributes and APIs are ignored:

**Note:** As previously mentioned with Android 16, these changes do not apply for screens that are smaller than sw 600 dp or apps categorized as games based on the [android:appCategory](https://developer.android.com/guide/topics/manifest/application-element#appCategory) flag.

|---|---|
| **Manifest attributes/API** | **Ignored values** |
| [screenOrientation](https://developer.android.com/guide/topics/manifest/activity-element#screen) | portrait, reversePortrait, sensorPortrait, userPortrait, landscape, reverseLandscape, sensorLandscape, userLandscape |
| [setRequestedOrientation()](https://developer.android.com/reference/android/app/Activity#setRequestedOrientation%28int%29) | portrait, reversePortrait, sensorPortrait, userPortrait, landscape, reverseLandscape, sensorLandscape, userLandscape |
| [resizeableActivity](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity) | all |
| [minAspectRatio](https://developer.android.com/reference/android/R.attr#minAspectRatio) | all |
| [maxAspectRatio](https://developer.android.com/reference/android/R.attr#maxAspectRatio) | all |

Also, users retain control. In the [aspect ratio settings](https://developer.android.com/guide/practices/device-compatibility-mode#user_per-app_overrides), users can explicitly opt-in to using the app's requested behavior.

#### **Prepare your app**

Apps will need to support landscape and portrait layouts for display sizes in the full range of aspect ratios in which users can choose to use apps, including resizable windows, as there will no longer be a way to restrict the aspect ratio and orientation to portrait or to landscape.

#### **Test your app**

Your first step is to test your app with these changes to make sure the app works well across display sizes.

Use Android 17 Beta 1 with the Pixel Tablet and Pixel Fold series emulators in Android Studio, and set the `targetSdkPreview = "CinnamonBun"`. Alternatively, you can use the [app compatibility framework](https://developer.android.com/guide/app-compatibility/test-debug) by enabling the `UNIVERSAL_RESIZABLE_BY_DEFAULT` flag if your app does not target API level 36 yet.

We have additional tools to ensure your layouts adapt correctly. You can automatically audit your UI and get suggestions to make your UI more adaptive with [Compose UI Check](https://developer.android.com/develop/ui/compose/tooling/debug#compose_ui_check), and simulate specific display characteristics in your tests using [DeviceConfigurationOverride](https://developer.android.com/training/testing/different-screens/tools#deviceconfigurationoverride).

For apps that have historically restricted orientation and aspect ratio, we commonly see issues with skewed or misoriented camera previews, stretched layouts, inaccessible buttons, or loss of user state when handling configuration changes.

Let's take a look at some strategies for addressing these common issues.

#### **Ensure camera compatibility**

A common problem on landscape foldables or for aspect ratio calculations in scenarios like multi-window, desktop windowing, or connected displays, is when the camera preview appears stretched, rotated, or cropped.
![camera_preview_issue.png](https://developer.android.com/static/blog/assets/camera_preview_issue_463c9db9b7_Z1upkvI.webp)

*Ensure your camera preview isn't stretched or rotated.*

This issue often happens on large screen and foldable devices because apps assume fixed relationships between camera features (like aspect ratio and sensor orientation) and device features (like device orientation and natural orientation).

To ensure your camera preview adapts correctly to any window size or orientation, consider these four solutions:

#### ***Solution 1: Jetpack CameraX (preferred)***

The simplest and most robust solution is to use the Jetpack CameraX library. Its `PreviewView` UI element is designed to handle all preview complexities automatically:

- `PreviewView` correctly adjusts for sensor orientation, device rotation, and scaling
- PreviewView maintains the aspect ratio of the camera image, typically by centering and cropping (`FILL_CENTER`)
- You can set the scale type to `FIT_CENTER` to letterbox the preview if needed

For more information, see [Implement a preview](https://developer.android.com/training/camerax/preview) in the CameraX documentation.

#### ***Solution 2: CameraViewfinder***

If you are using an existing Camera2 codebase, the `CameraViewfinder` library (backward compatible to API level 21) is another modern solution. It simplifies displaying the camera feed by using a `TextureView` or `SurfaceView` and applying all the necessary transformations (aspect ratio, scale, and rotation) for you.

For more information, see the [Introducing Camera Viewfinder](https://android-developers.googleblog.com/2022/11/introducing-camera-viewfinder.html) blog post and [Camera preview](https://developer.android.com/media/camera/camera2/camera-preview#cameraviewfinder) developer guide.

#### ***Solution 3: Manual Camera2 implementation***

If you can't use CameraX or `CameraViewfinder`, you must manually calculate the orientation and aspect ratio and ensure the calculations are updated on each configuration change:

- Get the camera sensor orientation (for example, 0, 90, 180, 270 degrees) from `CameraCharacteristics`
- Get the device's current display rotation (for example, 0, 90, 180, 270 degrees)
- Use the camera sensor orientation and display rotation values to determine the necessary transformations for your `SurfaceView` or `TextureView`
- Ensure the aspect ratio of your output `Surface` matches the aspect ratio of the camera preview to prevent distortion

**Important:** Note the camera app might be running in a portion of the screen, either in multi-window or desktop windowing mode or on a connected display. For this reason, screen size should not be used to determine the dimensions of the camera viewfinder; use [window metrics](https://developer.android.com/media/camera/camera2/camera-preview#window_metrics) instead. Otherwise you risk a stretched camera preview.

For more information, see the [Camera preview](https://developer.android.com/media/camera/camera2/camera-preview) developer guide and [Your Camera app on different form factors](https://www.youtube.com/watch?v=XcJIrTedfus) video.

#### ***Solution 4: Perform basic camera actions using an Intent***

If you don't need many camera features, a simple and straightforward solution is to perform basic camera actions like capturing a photo or video using the device's default camera application. In this case, you can simply use an `Intent` instead of integrating with a camera library, for easier maintenance and adaptability.

For more information, see [Camera intents](https://developer.android.com/media/camera/camera-intents).

#### **Avoid stretched UI or inaccessible buttons**

If your app assumes a specific device orientation or display aspect ratio, the app may run into issues when it's now used across various orientations or window sizes.
![elementsLS.png](https://developer.android.com/static/blog/assets/elements_LS_738cafe7fa_j8SdL.webp)

*Ensure buttons, textfields, and other elements aren't stretched on large screens.*

You may have set buttons, text fields, and cards to `fillMaxWidth` or `match_parent`. On a phone, this looks great. However, on a tablet or foldable in landscape, UI elements stretch across the entire large screen. In Jetpack Compose, you can use the widthIn modifier to set a maximum width for components to avoid stretched content:

```
Box(
    contentAlignment = Alignment.Center,
    modifier = Modifier.fillMaxSize()
) {
    Column(
        modifier = Modifier
            .widthIn(max = 300.dp) // Prevents stretching beyond 300dp
            .fillMaxWidth()        // Fills width up to 300dp
            .padding(16.dp)
    ) {
        // Your content
    }
}
```

If a user opens your app in landscape orientation on a foldable or tablet, action buttons like **Save** or **Login** at the bottom of the screen may be rendered offscreen. If the container is not scrollable, the user can be blocked from proceeding. In Jetpack Compose, you can add a verticalScroll modifier to your component:

```
Column(
    modifier = Modifier
        .fillMaxSize()
        .verticalScroll(rememberScrollState())
        .padding(16.dp)
)
```

By combining max-width constraints with vertical scrolling, you ensure your app remains functional and usable, regardless of how wide or short the app window size becomes.

See our guide on [building adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps).

#### **Preserve state with configuration changes**

Removing orientation and aspect ratio restrictions means your app's window size will change much more frequently. Users may rotate their device, fold/unfold it, or resize your app dynamically in split-screen or desktop windowing modes.

By default, these configuration changes destroy and recreate your activity. If your app does not properly manage this lifecycle event, users will have a frustrating experience: scroll positions are reset to the top, half-filled forms are wiped clean, and navigation history is lost. To ensure a seamless adaptive experience, it's critical your app preserves state through these configuration changes. With Jetpack Compose, you can opt-out of recreation, and instead allow window size changes to recompose your UI to reflect the new amount of space available.

See our guide on [saving UI state](https://developer.android.com/topic/libraries/architecture/saving-states).

### **Targeting API level 37 by August 2027**

If your app previously opted out of these changes when targeting API level 36, your app will only be impacted by the Android 17 opt-out removal after your app targets API level 37. To help you plan ahead and make the necessary adjustments to your app, here's the timeline when these changes will take effect:

- Android 17: Changes described above will be the baseline experience for large screen devices (smallest screen width \> 600 dp) for **apps that target API level 37** . Developers *will not* have an option to opt-out.

The deadlines for targeting a specific API level are app-store specific. For Google Play, new apps and updates will be required to target API level 37, making this behavior mandatory for distribution in August 2027.

### **Preparing for Android 17**

Refer to the [Android 17 changes page](https://developer.android.com/about/versions/17/behavior-changes-17) for all changes impacting apps in Android 17. To test your app, download Android 17 Beta 1 and update to `targetSdkPreview = "CinnamonBun"` or use the [app compatibility framework](https://developer.android.com/guide/app-compatibility/test-debug) to enable specific changes.

The future of Android is adaptive, and we're here to help you get there. As you prepare for Android 17, we encourage you to review our guides for [building adaptive layouts](https://developer.android.com/develop/ui/compose/build-adaptive-apps) and our [large screen quality guidelines](https://developer.android.com/docs/quality-guidelines/large-screen-app-quality). These resources are designed to help you handle multiple form factors and window sizes with confidence.

Don't wait. Start getting ready for Android 17 today!

###### Written by:

-

  ## [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/miguel-montemayor) ![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp) ![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z15U8cx.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![](https://developer.android.com/static/blog/assets/miguel_montemayor_552207c1c6_Z1tItyG.webp)](https://developer.android.com/blog/authors/miguel-montemayor) 03 Sep 2025 03 Sep 2025 ![](https://developer.android.com/static/blog/assets/yt_MBG_2_a56f169e60_ZSoFHF.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Unfold new possibilities with Compose Adaptive Layouts 1.2 beta](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts)

  [arrow_forward](https://developer.android.com/blog/posts/unfold-new-possibilities-with-compose-adaptive-layouts) With new form factors like the Pixel 10 Pro Fold joining the Android ecosystem, adaptive app development is essential for creating high-quality user experiences across phones, tablets, and foldables.

  ###### [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Miguel Montemayor](https://developer.android.com/blog/authors/miguel-montemayor) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)