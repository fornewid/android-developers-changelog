---
title: https://developer.android.com/blog/posts/the-first-beta-of-android-17
url: https://developer.android.com/blog/posts/the-first-beta-of-android-17
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# The First Beta of Android 17

###### 7-min read

![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp) 13 Feb 2026 [![](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_Z1Fsr5h.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [##### Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

###### Vice President, Product Management, Android Developer

Today we're releasing the first beta of [Android 17](https://developer.android.com/about/versions), continuing our work to build a platform that prioritizes privacy, security, and refined performance. This build continues our work for more adaptable Android apps, introduces significant enhancements to camera and media capabilities, new tools for optimizing connectivity, and expanded profiles for companion devices. This release also highlights a fundamental shift in the way we're bringing new releases to the developer community, [from the traditional Developer Preview model to the Android Canary program](https://android-developers.googleblog.com/2025/07/android-canary.html)

## Beyond the Developer Preview

Android has replaced the traditional "Developer Preview" with a **continuous Canary channel**. This new "always-on" model offers three main benefits:

- **Faster Access:** Features and APIs land in Canary as soon as they pass internal testing, rather than waiting for a quarterly release.
- **Better Stability:** Early "battle-testing" in Canary results in a more polished Beta experience with new APIs and behavior changes that are closer to being final.
- **Easier Testing:** Canary supports OTA updates (no more manual flashing) and, as a separate update channel, more easily integrates with CI workflows and gives you the earliest window to give immediate feedback on upcoming potential changes.

### **The Android 17 schedule**

We're going to be moving quickly from this Beta to our Platform Stability milestone, targeted for March. At this milestone, we'll deliver final SDK/NDK APIs and largely final app-facing behaviors. From that time you'll have several months before the final release to complete your testing.
![timeline1.png](https://developer.android.com/static/blog/assets/timeline1_c4ad756745_2vHLX7.webp)

**A year of releases**

We plan for Android 17 to continue to get updates in a series of quarterly releases. The upcoming release in Q2 is the only one where we introduce planned app breaking behavior changes. We plan to have a minor SDK release in Q4 with additional APIs and features.
![timeline2.png](https://developer.android.com/static/blog/assets/timeline2_8a877c6add_2fkhVO.webp)

### **Orientation and resizability restrictions**

With the release of the Android 17 Beta, we're moving to the next phase of our adaptive roadmap: **Android 17 (API level 37) removes the developer opt-out for orientation and resizability restrictions on** [**large screen devices**](https://developer.android.com/guide/topics/large-screens) (sw \> 600 dp).

When your app targets SDK 37, it must be ready to adapt. Users expect their apps to work everywhere---whether multitasking on a tablet, unfolding a device, or using a desktop windowing environment---and they expect the UI to fill the space and respect their device posture.

#### **Key Changes for SDK 37**

Apps targeting Android 17 must ensure compatibility with the phase-out of manifest attributes and runtime APIs introduced in Android 16. When running on a large screen (smaller dimension ≥ 600dp), the following attributes and APIs will be ignored:

|---|---|
| **Manifest attributes/API** | **Ignored values** |
| [screenOrientation](https://developer.android.com/guide/topics/manifest/activity-element#screen) | portrait, reversePortrait, sensorPortrait, userPortrait, landscape, reverseLandscape, sensorLandscape, userLandscape |
| [setRequestedOrientation()](https://developer.android.com/reference/android/app/Activity#setRequestedOrientation%28int%29) | portrait, reversePortrait, sensorPortrait, userPortrait, landscape, reverseLandscape, sensorLandscape, userLandscape |
| [resizeableActivity](https://developer.android.com/guide/topics/manifest/application-element#resizeableActivity) | all |
| [minAspectRatio](https://developer.android.com/reference/android/R.attr#minAspectRatio) | all |
| [maxAspectRatio](https://developer.android.com/reference/android/R.attr#maxAspectRatio) | all |

#### **Exemptions and User Control**

These changes are specific to large screens; they **do not apply** to screens smaller than sw600dp (including traditional slate form factor phones). Additionally, apps categorized as games (based on the [android:appCategory](https://developer.android.com/guide/topics/manifest/application-element#appCategory) flag) are exempt from these restrictions.

It is also important to note that users remain in control. They can explicitly opt-in/out to using an app's default behavior via the system's aspect ratio settings.

#### **Updates to configuration changes**

To improve app compatibility and help minimize interrupted video playback, dropped input, and other types of disruptive state loss, we are updating the default behavior for Activity recreation. Starting with Android 17, the system will no longer restart activities by default for specific configuration changes that typically do not require a UI recreation, including [`CONFIG_KEYBOARD`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD), [`CONFIG_KEYBOARD_HIDDEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_KEYBOARD_HIDDEN), [`CONFIG_NAVIGATION`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_NAVIGATION), [`CONFIG_UI_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_UI_MODE) (when only `UI_MODE_TYPE_DESK` is changed), [`CONFIG_TOUCHSCREEN`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_TOUCHSCREEN), and [`CONFIG_COLOR_MODE`](https://developer.android.com/reference/android/content/pm/ActivityInfo#CONFIG_COLOR_MODE). Instead, running activities will simply receive these updates via [`onConfigurationChanged`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)). If your application relies on a full restart to reload resources for these changes, you must now explicitly opt-in using the new `android:recreateOnConfigChanges` manifest attribute, which allows you to specify which configuration changes should trigger a complete activity lifecycle (from stop, to destroy and creation again), together with the related constants [mcc](https://developer.android.com/reference/android/content/res/Configuration#mcc), [mnc](https://developer.android.com/reference/android/content/res/Configuration#mnc), and the new ones [keyboard](https://developer.android.com/reference/android/content/res/Configuration#keyboard), [keyboardHidden](https://developer.android.com/reference/android/content/res/Configuration#keyboardHidden), [navigation](https://developer.android.com/reference/android/content/res/Configuration#navigation), [touchscreen](https://developer.android.com/reference/android/content/res/Configuration#touchscreen) and [colorMode](https://developer.android.com/reference/android/content/res/Configuration#colorMode).

#### **Prepare Your App**

We've released tools and documentation to make it easy for you. [Our focused blog post has more guidance](https://android-developers.googleblog.com/2026/02/prepare-your-app-for-resizability-and.html), with strategies to address common issues. Apps will need to support landscape and portrait layouts for window sizes across the full range of aspect ratios, as restricting orientation or aspect ratio will no longer be an option. We recommend testing your app using the [Android 17](https://developer.android.com/about/versions) Beta 1 with Pixel Tablet or Pixel Fold emulators (configured to `targetSdkPreview = "CinnamonBun"`) or by using the [app compatibility framework](https://developer.android.com/guide/topics/large-screens/large-screen-compatibility-mode) to enable `UNIVERSAL_RESIZABLE_BY_DEFAULT` on Android 16 devices.

### **Performance**

#### **Lock-free MessageQueue**

In [Android 17](https://developer.android.com/about/versions), apps targeting SDK 37 or higher will receive a new implementation of [android.os.MessageQueue](https://developer.android.com/reference/android/os/MessageQueue) where the implementation is lock-free. The new implementation improves performance and reduces missed frames, but may break clients that reflect on [MessageQueue](https://developer.android.com/reference/android/os/MessageQueue) private fields and methods.

#### **Generational garbage collection**

[Android 17](https://developer.android.com/about/versions) introduces generational garbage collection to [ART](https://developer.android.com/guide/platform#art)'s Concurrent Mark-Compact collector. This optimization introduces more frequent, less resource-intensive young-generation collections alongside full-heap collections. aiming to reduce overall garbage collection CPU cost and time duration. ART improvements are also available to over a billion devices running Android 12 (API level 31) and higher through Google Play System updates.

#### **Static final fields now truly final**

Starting from Android 17 apps targeting Android 17 or later won't be able to modify "static final" fields, allowing the runtime to apply performance optimizations more aggressively. An attempt to do so via reflection (and deep reflection) will always lead to IllegalAccessException being thrown. Modifying them via JNI's SetStatic\<Type\>Field methods family will immediately crash the application.

#### **Custom Notification View Restrictions**

To reduce memory usage we are restricting the size of [custom notification views](https://developer.android.com/develop/ui/views/notifications/custom-notification). This update closes a loophole that allows apps to bypass existing limits using URIs. This behavior is gated by the target SDK version and takes effect for apps targeting API 37 and higher.

#### **New performance debugging ProfilingManager triggers**

We've introduced several new system triggers to [ProfilingManager](https://developer.android.com/topic/performance/tracing/profiling-manager/overview) to help you collect in-depth data to debug performance issues. These triggers are [TRIGGER_TYPE_COLD_START,](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_COLD_START)[TRIGGER_TYPE_OOM,](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_OOM)and [TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE.](https://developer.android.com/reference/android/os/ProfilingTrigger#TRIGGER_TYPE_KILL_EXCESSIVE_CPU_USAGE)

To understand how to set up the new system triggers, check out the [trigger-based profiling](https://developer.android.com/topic/performance/tracing/profiling-manager/trigger-based-capture) and [retrieve and analyze profiling data](https://developer.android.com/topic/performance/tracing/profiling-manager/retrieve-and-analyze) documentation.

### **Media and Camera**

Android 17 brings professional-grade tools to media and camera apps, with features like seamless transitions and standardized loudness.

#### **Dynamic Camera Session Updates**

We have introduced `updateOutputConfigurations`[`()`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession) to [`CameraCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession). This allows you to dynamically attach and detach output surfaces without the need to reconfigure the entire camera capture session. This change enables seamless transitions between camera use cases and modes (such as shooting still images vs shooting videos) without the memory cost and code complexity of configuring and holding onto all camera output surfaces that your app might need during camera start up. This helps to eliminate user-visible glitches or freezes during operation.

```
  fun updateCameraSession(session: CameraCaptureSession, newOutputConfigs:  List<OutputConfiguration>)) {
    // Dynamically update the session without closing and reopening
    try {
        
        // Update the output configurations
        session.updateOutputConfigurations(newOutputConfigs)
    } catch (e: CameraAccessException) {
        // Handle error
    }
}
```

#### **Logical multi-camera device metadata**

When working with logical cameras that combine multiple physical camera sensors, you can now request additional metadata from all active physical cameras involved in a capture, not just the primary one. Previously, you had to implement workarounds, sometimes allocating unnecessary physical streams, to obtain metadata from secondary active cameras (e.g., during a lens switch for zoom where a follower camera is active). This feature introduces a new key, [LOGICAL_MULTI_CAMERA_ADDITIONAL_RESULTS](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#LOGICAL_MULTI_CAMERA_ADDITIONAL_RESULTS), in [CaptureRequest](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest) and [CaptureResult](https://developer.android.com/reference/android/hardware/camera2/CaptureResult). By setting this key to ON in your [CaptureRequest](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest), the [TotalCaptureResult](https://developer.android.com/reference/android/hardware/camera2/TotalCaptureResult) will include metadata from these additional active physical cameras. You can access this comprehensive metadata using [TotalCaptureResult.getPhysicalCameraTotalResults()](https://developer.android.com/reference/android/hardware/camera2/TotalCaptureResult#getPhysicalCameraTotalResults()) to get more detailed information that may enable you to optimize resource usage in your camera applications.

### Versatile Video Coding (VVC) Support

[Android 17](https://developer.android.com/about/versions) adds support for the [Versatile Video Coding (VVC)](https://developer.android.com/guide/topics/media/media-formats#video-formats) standard. This includes defining the [video/vvc](https://developer.android.com/guide/topics/media/media-formats#video-formats) MIME type in [MediaFormat](https://developer.android.com/reference/android/media/MediaFormat), adding new VVC profiles in [MediaCodecInfo](https://developer.android.com/reference/android/media/MediaCodecInfo), and integrating support into [MediaExtractor](https://developer.android.com/reference/android/media/MediaExtractor). This feature will be coming to devices with hardware decode support and capable drivers.

#### **Constant Quality for Video Recording**

We have added [setVideoEncodingQuality()](https://developer.android.com/reference/android/media/MediaRecorder#setVideoQuality(int)) to [MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder). This allows you to configure a constant quality (CQ) mode for video encoders, giving you finer control over video quality beyond simple bitrate settings.

#### **Background Audio Hardening**

Starting in Android 17, the audio framework will enforce restrictions on background audio interactions including audio playback, [audio focus](https://developer.android.com/media/optimize/audio-focus) requests, and [volume change](https://developer.android.com/reference/android/media/AudioManager#adjustStreamVolume(int,%20int,%20int)) APIs to ensure that these changes are started intentionally by the user.

If the app tries to call audio APIs while the application is not in a valid lifecycle, the audio playback and volume change APIs will fail silently without an exception thrown or failure message provided. The audio focus API will fail with the result code AUDIOFOCUS_REQUEST_FAILED.

### **Privacy and Security**

#### **Deprecation of Cleartext Traffic Attribute**

The [android:usesCleartextTraffic](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic) attribute is now deprecated. If your app targets (Android 17) or higher and relies on usesCleartextTraffic="true" without a corresponding [Network Security Configuration](https://developer.android.com/training/articles/security-config), it will default to disallowing cleartext traffic. You are encouraged to migrate to [Network Security Configuration](https://developer.android.com/training/articles/security-config) files for granular control.

#### **HPKE Hybrid Cryptography**

We are introducing a public [Service Provider Interface (SPI)](https://developer.android.com/reference/android/crypto/hpke/HpkeSpi) for an implementation of HPKE hybrid cryptography, enabling secure communication using a combination of public key and symmetric encryption ([AEAD](http://developer.android.com/reference/android/crypto/hpke/AeadParameterSpec)).

### **Connectivity and Telecom**

#### **Enhanced VoIP Call History**

We are introducing user preference management for app VoIP call history integration. This includes support for caller and participant avatar URIs in the system dialer, enabling granular user control over call log privacy and enriching the visual display of integrated VoIP call logs.

#### **Wi-Fi Ranging and Proximity**

[Wi-Fi Ranging](https://developer.android.com/guide/topics/connectivity/wifi-rtt) has been enhanced with new Proximity Detection capabilities, supporting continuous ranging and secure peer-to-peer discovery. Updates to [Wi-Fi Aware](https://developer.android.com/guide/topics/connectivity/wifi-aware) ranging include new APIs for peer handles and PMKID caching for 11az secure ranging.

### **Developer Productivity and Tools**

#### **Updates for companion device apps**

We have introduced two new profiles to the [CompanionDeviceManager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) to improve device distinction and permission handling:

- **Medical Devices:** This profile allows medical device mobile applications to request all necessary permissions with a single tap, simplifying the setup process.
- **Fitness Trackers:** The [DEVICE_PROFILE_FITNESS_TRACKER](https://developer.android.com/reference/android/companion/AssociationRequest#DEVICE_PROFILE_FITNESS_TRACKER) profile allows companion apps to explicitly indicate they are managing a fitness tracker. This ensures accurate user experiences with distinct icons while reusing existing watch role permissions.

Also, the [CompanionDeviceManager](https://developer.android.com/guide/topics/connectivity/companion-device-pairing) now offers a unified dialog for device association and Nearby permission requests. You can leverage the new [setExtraPermissions](https://developer.android.com/reference/android/companion/AssociationRequest.Builder#setExtraPermissions(java.util.Set%3Cjava.lang.String%3E)) method in [AssociationRequest.Builder](https://developer.android.com/reference/android/companion/AssociationRequest.Builder) to bundle nearby permission prompts within the existing association flow, reducing the number of dialogs presented to the user.

### **Get started with Android 17**

You can [enroll any supported Pixel device](https://www.google.com/android/beta) to get this and future Android Beta updates over-the-air. If you don't have a Pixel device, you can [use the 64-bit system images with the Android Emulator](https://developer.android.com/about/versions/17/get#on_emulator) in Android Studio.

If you are currently in the Android Beta program, you will be offered an over-the-air update to Beta 1.

If you have Android 26Q1 Beta and would like to take the final stable release of 26Q1 and exit Beta, you need to ignore the over-the-air update to 26Q2 Beta 1 and wait for the release of 26Q1.

We're looking for your feedback so please [report issues and submit feature requests](https://developer.android.com/about/versions/17/feedback) on the [feedback page](https://developer.android.com/about/versions/16/feedback). The earlier we get your feedback, the more we can include in our work on the final release.

For the best development experience with Android 17, we recommend that you use the latest preview of [Android Studio (Panda)](https://developer.android.com/studio/preview). Once you're set up, here are some of the things you should do:

- Compile against the new SDK, test in CI environments, and report any issues in our tracker on the [feedback page](https://developer.android.com/about/versions/17/feedback).
- Test your current app for compatibility, learn whether your app is affected by changes in Android 17, and install your app onto a device or emulator running Android 17 and extensively test it.

We'll update the [preview/beta system images](https://developer.android.com/about/versions/17/download) and SDK regularly throughout the Android 17 release cycle. Once you've installed a beta build, you'll automatically get future updates over-the-air for all later previews and Betas.

For complete information, visit the [Android 17 developer site](https://developer.android.com/about/versions/17).

### **Join the conversation**

As we move toward **Platform Stability** and the final stable release of Android 17 later this year, your feedback remains our most valuable asset. Whether you're an [early adopter on the Canary channel](https://www.reddit.com/r/android_canary/) or an [app developer testing on Beta 1](https://www.reddit.com/r/android_beta/), consider joining our communities and filing feedback. We're listening.

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