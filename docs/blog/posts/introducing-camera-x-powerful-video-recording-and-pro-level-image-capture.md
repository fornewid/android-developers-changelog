---
title: https://developer.android.com/blog/posts/introducing-camera-x-powerful-video-recording-and-pro-level-image-capture
url: https://developer.android.com/blog/posts/introducing-camera-x-powerful-video-recording-and-pro-level-image-capture
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Introducing CameraX 1.5: Powerful Video Recording and Pro-level Image Capture

###### 7-min read

![](https://developer.android.com/static/blog/assets/camera_X1_5_9f8216fa59_1XU56O.webp) 13 Nov 2025 [![](https://developer.android.com/static/blog/assets/scottnien_c517be4920_F68BQ.webp)](https://developer.android.com/blog/authors/scott-nien) [##### Scott Nien](https://developer.android.com/blog/authors/scott-nien)

###### Software Engineer

The CameraX team is thrilled to announce the release of version 1.5! This latest update focuses on bringing professional-grade capabilities to your fingertips while making the camera session easier to configure than ever before.

For **video recording** , users can now effortlessly capture stunning slow-motion or high-frame-rate videos. More importantly, the new [Feature Group API](https://developer.android.com/reference/androidx/camera/core/SessionConfig.Builder#setPreferredFeatureGroup(kotlin.Array)) allows you to confidently enable complex combinations like **10-bit HDR and 60 FPS**, ensuring consistent results across supported devices.

On the **image capture** front, you gain maximum flexibility with support for capturing unprocessed, uncompressed DNG (RAW) files. Plus, you can now leverage Ultra HDR output even when using powerful Camera Extensions.

Underpinning these features is the new [**SessionConfig API**](https://developer.android.com/reference/androidx/camera/core/SessionConfig), which streamlines camera setup and reconfiguration. Now, let's dive into the details of these exciting new features.

## Powerful Video Recording: High-Speed and Feature Combinations

CameraX 1.5 significantly expands its video capabilities, enabling more creative and robust recording experiences.

### Slow Motion \& High Frame Rate Video

One of our most anticipated features, slow-motion video, is now available. You can now capture high-speed video (e.g., 120 or 240 fps) and encode it directly into a dramatic slow-motion video. Alternatively, you can record at the same high frame rate to produce exceptionally smooth video.

Implementing this is straightforward if you're familiar with the [VideoCapture](https://developer.android.com/media/camera/camerax/video-capture) API.

**1. Check for High-Speed Support:** Use the new [Recorder.getHighSpeedVideoCapabilities()](https://developer.android.com/reference/androidx/camera/video/Recorder#getHighSpeedVideoCapabilities(androidx.camera.core.CameraInfo))method to query if the device supports this feature.

```
val cameraInfo = cameraProvider.getCameraInfo(cameraSelector)

val highSpeedCapabilities = Recorder.getHighSpeedVideoCapabilities(cameraInfo)

if (highSpeedCapabilities == null) {
    // This camera device does not support high-speed video.
    return
}
```

**2. Configure and Bind the Use Case:** Use the returned `videoCapabilities` (which contains supported video quality information) to build a [HighSpeedVideoSessionConfig](https://developer.android.com/reference/kotlin/androidx/camera/video/HighSpeedVideoSessionConfig). You must then query the supported frame rate ranges via [cameraInfo.getSupportedFrameRateRanges()](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getSupportedFrameRateRanges(androidx.camera.core.SessionConfig)) and set the desired range. Invoke [setSlowMotionEnabled(true)](https://developer.android.com/reference/kotlin/androidx/camera/video/HighSpeedVideoSessionConfig.Builder?_gl=1*1eperjw*_up*MQ..*_ga*NTc4Mzk5NDgzLjE3NjIyMzgyNzY.*_ga_6HH9YJMN9M*czE3NjIyMzgyNzYkbzEkZzAkdDE3NjIyMzgyNzYkajYwJGwwJGgxMzAyMzMwOTk4#setSlowMotionEnabled(kotlin.Boolean)) to record slow motion videos, otherwise it will record high-frame-rate videos. The final step is to use the regular `Recorder.prepareRecording().start()` to begin recording the video.

```
val preview = Preview.Builder().build()
val quality = highSpeedCapabilities
        .getSupportedQualities(DynamicRange.SDR).first()

val recorder = Recorder.Builder()
      .setQualitySelector(QualitySelector.from(quality)))
      .build()

val videoCapture = VideoCapture.withOutput(recorder)

val frameRateRange = cameraInfo.getSupportedFrameRateRanges(      
       HighSpeedVideoSessionConfig(videoCapture, preview)
).first()

val sessionConfig = HighSpeedVideoSessionConfig(
    videoCapture, 
    preview, 
    frameRateRange = frameRateRange, 
    // Set true for slow-motion playback, or false for high-frame-rate
    isSlowMotionEnabled = true
)

cameraProvider.bindToLifecycle(
     lifecycleOwner, cameraSelector, sessionConfig)

// Start recording slow motion videos. 
val recording = recorder.prepareRecording(context, outputOption)
      .start(executor, {})
```

**Compatibility and Limitations**

High-speed recording requires specific [CameraConstrainedHighSpeedCaptureSession](https://developer.android.com/reference/android/hardware/camera2/CameraConstrainedHighSpeedCaptureSession) and [CamcorderProfile](https://developer.android.com/reference/android/media/CamcorderProfile) support. Always perform the capability check, and enable high-speed recording only on supported devices to prevent bad user experience. Currently, this feature is supported on the rear cameras of almost all Pixel devices and select models from other manufacturers.

Check the [blog post](https://android-developers.googleblog.com/2025/10/high-speed-capture-and-slow-motion.html) for more details.

### Combine Features with Confidence: The Feature Group API

CameraX 1.5 introduces the **Feature Group API** , which eliminates the guesswork of feature compatibility. Based on Android 15's feature combination query [API](https://source.android.com/docs/core/camera/stream-config#feature-combinations-api), you can now confidently enable multiple features together, guaranteeing a stable camera session. The Feature Group currently supports: **HDR (HLG), 60 fps, Preview Stabilization, and Ultra HDR**. For instance, you can enable HDR, 60 fps, and Preview Stabilization simultaneously on Pixel 10 and Galaxy S25 series. Future enhancements are planned to include 4K recording and ultra-wide zoom.

The feature group API enables two essential use cases:

**Use Case 1: Prioritizing the Best Quality**

If you want to capture using the best possible combination of features, you can provide a prioritized list. CameraX will attempt to enable them in order, selecting the first combination the device fully supports.

```
val sessionConfig = SessionConfig(
    useCases = listOf(preview, videoCapture),
    preferredFeatureGroup = listOf(
        GroupableFeature.HDR_HLG10,
        GroupableFeature.FPS_60,
        GroupableFeature.PREVIEW_STABILIZATION
    )
).apply {
    // (Optional) Get a callback with the enabled features to update your UI.
    setFeatureSelectionListener { selectedFeatures ->
        updateUiIndicators(selectedFeatures)
    }
}
processCameraProvider.bindToLifecycle(activity, cameraSelector, sessionConfig)
```

In this example, CameraX tries to enable features in this order:

1. HDR + 60 FPS + Preview Stabilization
2. HDR + 60 FPS
3. HDR + Preview Stabilization
4. HDR
5. 60 FPS + Preview Stabilization
6. 60 FPS
7. Preview Stabilization
8. None

**Use Case 2: Building a User-Facing Settings UI**

You can now accurately reflect which feature combinations are supported in your app's settings UI, disabling toggles for unsupported options like the picture below.
![unsupported-features-disabled.gif](https://developer.android.com/static/blog/assets/unsupported_features_disabled_3da0c273f4_ZOJN6L.webp)

To determine whether to gray out a toggle, use the following codes to check for feature combination support. Initially, query the status of every individual feature. Once a feature is enabled, re-query the remaining features with the enabled features to see if their toggles must now be grayed out due to compatibility constraints.

```
fun disableFeatureIfNotSuported(
   enabledFeatures: Set<GroupableFeature>,     
   featureToCheck:GroupableFeature
) {
 val sessionConfig = SessionConfig(
     useCases = useCases,
     requiredFeatureGroup = enabledFeatures + featureToCheck
 )
 val isSupported = cameraInfo.isFeatureGroupSupported(sessionConfig)

 if (!isSupported) {
     // disable the toggle for featureToCheck
 }
}
```

Please refer to the [Feature Group blog post](https://android-developers.googleblog.com/2025/10/beyond-single-features-guaranteeing.html)for more information.

### More Video Enhancements

- **Concurrent Camera Improvements:** With CameraX 1.5.1, you can now bind Preview + ImageCapture + VideoCapture use cases concurrently for each [SingleCameraConfig](https://developer.android.com/reference/androidx/camera/core/ConcurrentCamera.SingleCameraConfig) in **non-composition mode** . Additionally, in **composition mode** (same use cases with [CompositionSettings](https://developer.android.com/reference/kotlin/androidx/camera/core/CompositionSettings)), you can now set the `CameraEffect` that is applied to the final composition result.
- **Dynamic Muting:** You can now start a recording in a muted state using `PendingRecording.withAudioEnabled(boolean initialMuted)` and allow the user to unmute later using `Recording.mute(boolean muted)`.
- **Improved Insufficient Storage Handling:** CameraX now reliably dispatches the `VideoRecordEvent.Finalize.ERROR_INSUFFICIENT_STORAGE` error, allowing your app to gracefully handle low storage situations and inform the user.
- **Low Light Boost:** On supported devices (like the Pixel 10 series), you can enable [CameraControl.enableLowLightBoostAsync](https://developer.android.com/reference/androidx/camera/core/CameraControl#enableLowLightBoostAsync(boolean)) to automatically brighten the preview and video streams in dark environments.

## Professional-Grade Image Capture

CameraX 1.5 brings major upgrades to [ImageCapture](https://developer.android.com/reference/androidx/camera/core/ImageCapture) for developers who demand maximum quality and flexibility.

### Unleash Creative Control with DNG (RAW) Capture

For complete control over post-processing, CameraX now supports DNG (RAW) capture. This gives you access to the unprocessed, uncompressed image data directly from the camera sensor, enabling professional-grade editing and color grading. The API supports capturing the DNG file alone, or capturing simultaneous JPEG and DNG outputs. See the sample code below for how to capture JPEG and DNG files simultaneously.

```
val capabilities = ImageCapture.getImageCaptureCapabilities(cameraInfo)
val imageCapture = ImageCapture.Builder().apply {
    if (capabilities.supportedOutputFormats
             .contains(OUTPUT_FORMAT_RAW_JPEG)) {
        // Capture both RAW and JPEG formats.
        setOutputFormat(OUTPUT_FORMAT_RAW_JPEG)
    }
}.build()
// ... bind imageCapture to lifecycle ...


// Provide separate output options for each format.
val outputOptionRaw = /* ... configure for image/x-adobe-dng ... */
val outputOptionJpeg = /* ... configure for image/jpeg ... */
imageCapture.takePicture(
    outputOptionRaw,
    outputOptionJpeg,
    executor,
    object : ImageCapture.OnImageSavedCallback {
        override fun onImageSaved(results: OutputFileResults) {
            // This callback is invoked twice: once for the RAW file
            // and once for the JPEG file.
        }

        override fun onError(exception: ImageCaptureException) {}
    }
)
```

### Ultra HDR for Camera Extensions

Get the best of both worlds: the stunning computational photography of Camera Extensions (like Night Mode) combined with the brilliant color and dynamic range of Ultra HDR. This feature is now supported on many recent premium Android phones, such as the Pixel 9/10 series and Samsung S24/S25 series.

```
// Support UltraHDR when Extension is enabled. 

val extensionsEnabledCameraSelector = extensionsManager
     .getExtensionEnabledCameraSelector(
        CameraSelector.DEFAULT_BACK_CAMERA, ExtensionMode.NIGHT)

val imageCapabilities = ImageCapture.getImageCaptureCapabilities(
               cameraProvider.getCameraInfo(extensionsEnabledCameraSelector)

val imageCapture = ImageCapture.Builder()
     .apply {
       if (imageCapabilities.supportedOutputFormats
                .contains(OUTPUT_FORMAT_JPEG_ULTRA_HDR) {
           setOutputFormat(OUTPUT_FORMAT_JPEG_ULTRA_HDR)

       }

     }.build()
```

## Core API and Usability Enhancements

### A New Way to Configure: `SessionConfig`

As seen in the examples above, [SessionConfig](https://developer.android.com/reference/androidx/camera/core/SessionConfig) is a new concept in CameraX 1.5. It centralizes configuration and simplifies the API in two key ways:

1. **No More Manual** `unbind()`**Calls:** CameraX APIs are lifecycle-aware. It will implicitly "unbind" your use cases when the activity or other `LifecycleOwner` is destroyed. But updating use cases or switching cameras still requires you to call `unbind()` or `unbindAll()` before rebinding. Now with CameraX 1.5, when you bind a new `SessionConfig`, CameraX seamlessly updates the session for you, eliminating the need for unbind calls.
2. **Deterministic Frame Rate Control:** The new `SessionConfig` API introduces a deterministic way to manage the frame rate. Unlike the previous `setTargetFrameRate`, which was only a hint, this new method **guarantees** the specified frame rate range will be applied upon successful configuration. To ensure accuracy, you must query supported frame rates using `CameraInfo.getSupportedFrameRateRanges(SessionConfig)`. By passing the full `SessionConfig`, CameraX can accurately determine the supported ranges based on stream configurations.

### Camera-Compose is Now Stable

We know how much you enjoy Jetpack Compose, and we're excited to announce that the `camera-compose`**library is now stable at version** `1.5.1`**!** This release includes critical bug fixes related to [CameraXViewfinder](https://developer.android.com/reference/kotlin/androidx/camera/compose/package-summary?_gl=1*6zjzmt*_up*MQ..*_ga*MjA5MDY4MTQyNy4xNzYxOTEyNzg4*_ga_6HH9YJMN9M*czE3NjE5MTI3ODckbzEkZzAkdDE3NjE5MTI3ODckajYwJGwwJGg4MDk5ODEyOTc.#CameraXViewfinder(androidx.camera.core.SurfaceRequest,androidx.compose.ui.Modifier,androidx.camera.viewfinder.core.ImplementationMode,androidx.camera.viewfinder.compose.MutableCoordinateTransformer,androidx.compose.ui.Alignment,androidx.compose.ui.layout.ContentScale)) usage with Compose features like `moveableContentOf` and `Pager`, as well as resolving a preview stretching issue. We will continue to add more features to `camera-compose` in future releases.

### ImageAnalysis and CameraControl Improvements

- **Torch Strength Adjustment:** Gain fine-grained control over the device's torch with new APIs. You can query the maximum supported strength using [CameraInfo.getMaxTorchStrengthLevel()](https://developer.android.com/reference/androidx/camera/core/CameraInfo#getMaxTorchStrengthLevel()) and then set the desired level with [CameraControl.setTorchStrengthLevel()](https://developer.android.com/reference/androidx/camera/core/CameraControl#setTorchStrengthLevel(int)).
- **NV21 Support in** `ImageAnalysis`**:** You can now request the NV21 image format directly from `ImageAnalysis`, simplifying integration with other libraries and APIs. This is enabled by invoking `ImageAnalysis.Builder.setOutputImageFormat(OUTPUT_IMAGE_FORMAT_NV21)`.

## Get Started Today

**Update your dependencies to CameraX 1.5 today** and explore the exciting new features. We can't wait to see what you build.

To use CameraX 1.5, please add the following dependencies to your libs.versions.toml. (We recommend using 1.5.1 which contains many critical bug fixes and concurrent camera improvements.)

```
[versions]

camerax = "1.5.1"


[libraries]

..

androidx-camera-core = { module = "androidx.camera:camera-core", version.ref = "camerax" }

androidx-camera-compose = { module = "androidx.camera:camera-compose", version.ref = "camerax" }

androidx-camera-view = { module = "androidx.camera:camera-view", version.ref = "camerax" }

androidx-camera-lifecycle = { group = "androidx.camera", name = "camera-lifecycle", version.ref = "camerax" }

androidx-camera-camera2 = { module = "androidx.camera:camera-camera2", version.ref = "camerax" }

androidx-camera-extensions = { module = "androidx.camera:camera-extensions", version.ref = "camerax" }
```

And then add these to your module build.gradle.kts dependencies:

```
dependencies {

  ..

  implementation(libs.androidx.camera.core)
  implementation(libs.androidx.camera.lifecycle)

  implementation(libs.androidx.camera.camera2)

  implementation(libs.androidx.camera.view) // for PreviewView 
  implementation(libs.androidx.camera.compose) // for compose UI

  implementation(libs.androidx.camera.extensions) // For Extensions 

}
```

Have questions or want to connect with the CameraX team? Join the CameraX developer discussion group or file a bug report:

- [CameraX developers discussion group](https://groups.google.com/a/android.com/g/camerax-developers)
- [File a bug](https://www.google.com/search?q=https://issuetracker.google.com/issues/new?component%3D618491%26template%3D1257717%26hl%3Dzh-tw)

###### Written by:

-

  ## [Scott Nien](https://developer.android.com/blog/authors/scott-nien)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/scott-nien) ![](https://developer.android.com/static/blog/assets/scottnien_c517be4920_F68BQ.webp) ![](https://developer.android.com/static/blog/assets/scottnien_c517be4920_F68BQ.webp)

## Continue reading

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

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)