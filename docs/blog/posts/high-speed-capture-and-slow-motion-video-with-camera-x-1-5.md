---
title: https://developer.android.com/blog/posts/high-speed-capture-and-slow-motion-video-with-camera-x-1-5
url: https://developer.android.com/blog/posts/high-speed-capture-and-slow-motion-video-with-camera-x-1-5
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# High-Speed Capture and Slow-Motion Video with CameraX 1.5

###### 6-min read

![](https://developer.android.com/static/blog/assets/25_Android_Camera_X_High_speed_Slomo_Blog_1_fc4509cdb7_1dTrfW.webp) 28 Oct 2025 [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/leo-huang) [##### Leo Huang](https://developer.android.com/blog/authors/leo-huang)

###### Software Engineer

Capturing fast-moving action with clarity is a key feature for modern camera apps. This is achieved through **high-speed capture** ---the process of acquiring frames at rates like 120 or 240 fps. This high-fidelity capture can be used for two distinct purposes: creating a **high-frame-rate video** for detailed, frame-by-frame analysis, or generating a **slow-motion video** where action unfolds dramatically on screen.

Previously, implementing these features with the Camera2 API was a more hands-on process. Now, with the new [**high-speed API**](https://developer.android.com/reference/androidx/camera/video/HighSpeedVideoSessionConfig) in CameraX 1.5, the entire process is simplified, giving you the flexibility to create either true high-frame-rate videos or ready-to-play slow-motion clips. This post will show you how to master both. For those new to CameraX, you can get up to speed with the [**CameraX Overview**](https://developer.android.com/media/camera/camerax).

*** ** * ** ***

## The Principle Behind Slow-Motion

The fundamental principle of slow-motion is to capture video at a much higher frame rate than it is played back. For instance, if you record a one-second event at **120 frames per second (fps)** and then play that recording back at a standard 30 fps, the video will take four seconds to play. This "stretching" of time is what creates the dramatic slow-motion effect, allowing you to see details that are too fast for the naked eye.

To ensure the final output video is smooth and fluid, it should typically be rendered at a minimum of 30 fps. This means that to create a 4x slow-motion video, the original capture frame rate must be at least 120 fps (120 capture fps ÷ 4 = 30 playback fps).

Once the high-frame-rate footage is captured, there are two primary ways to achieve the desired outcome:

- **Player-handled Slow-Motion (High-Frame-Rate Video):** The high-speed recording (e.g., 120 fps) is saved directly as a high-frame-rate video file. It is then the video player's responsibility to slow down the playback speed. This gives the user flexibility to toggle between normal and slow-motion playback.
- **Ready-to-play Slow-Motion (Re-encoded Video):** The high-speed video stream is processed and re-encoded into a file with a standard frame rate (e.g., 30 fps). The slow-motion effect is "baked in" by adjusting the frame timestamps. The resulting video will play in slow motion in any standard video player without special handling. While the video plays in slow motion by default, video players can still provide playback speed controls that allow the user to increase the speed and watch the video at its original speed.

The CameraX API simplifies this by giving you a unified way to choose which approach you want, as you'll see below.

*** ** * ** ***

## The New High-Speed Video API

The new CameraX solution is built on two main components:

- [`Recorder#getHighSpeedVideoCapabilities(CameraInfo)`](https://developer.android.com/reference/kotlin/androidx/camera/video/Recorder#getHighSpeedVideoCapabilities(androidx.camera.core.CameraInfo)): This method lets you check if the camera can record in high-speed and, if so, which resolutions (`Quality` objects) are supported.
- [`HighSpeedVideoSessionConfig`](https://developer.android.com/reference/androidx/camera/video/HighSpeedVideoSessionConfig): This is a special configuration object that groups your `VideoCapture` and `Preview` use cases, telling CameraX to create a unified high-speed camera session. Note that while the VideoCapture stream will operate at the configured high frame rate, the Preview stream will typically be limited to a standard rate of at least 30 FPS by the camera system to ensure a smooth display on the screen.

### Getting Started

Before you start, make sure you have added the necessary CameraX dependencies to your app's `build.gradle.kts` file. You will need the `camera-video` artifact along with the core CameraX libraries.

```
// build.gradle.kts (Module: app)

dependencies {

    val camerax_version = "1.5.1"


    implementation("androidx.camera:camera-core:$camerax_version")

    implementation("androidx.camera:camera-camera2:$camerax_version")

    implementation("androidx.camera:camera-lifecycle:$camerax_version")

    implementation("androidx.camera:camera-video:$camerax_version")

    implementation("androidx.camera:camera-view:$camerax_version")

}
```

### A Note on Experimental APIs

It's important to note that the high-speed recording APIs are currently experimental. This means they are subject to change in future releases. To use them, you must opt-in by adding the following annotation to your code:

```
@kotlin.OptIn(ExperimentalSessionConfig::class, ExperimentalHighSpeedVideo::class)
```

*** ** * ** ***

## Implementation

The implementation for both outcomes starts with the same setup steps. The choice between creating a high-frame-rate video or a slow-motion video comes down to a single setting.

### 1. Set up High-Speed Capture

First, regardless of your goal, you need to get the [`ProcessCameraProvider`](https://developer.android.com/reference/androidx/camera/lifecycle/ProcessCameraProvider), check for device capabilities, and create your use cases.

The following code block shows the complete setup flow within a suspend function. You can call this function from a coroutine scope, like `lifecycleScope.launch`.

```
// Add the OptIn annotation at the top of your function or class

@kotlin.OptIn(ExperimentalSessionConfig::class, ExperimentalHighSpeedVideo::class)

private suspend fun setupCamera() {

    // Asynchronously get the CameraProvider

    val cameraProvider = ProcessCameraProvider.awaitInstance(this)



    // -- CHECK CAPABILITIES --

    val cameraInfo = cameraProvider.getCameraInfo(CameraSelector.DEFAULT_BACK_CAMERA)

    val videoCapabilities = Recorder.getHighSpeedVideoCapabilities(cameraInfo)

    if (videoCapabilities == null) {

        // This camera device does not support high-speed video.

        return

    }




    // -- CREATE USE CASES --

    val preview = Preview.Builder().build()    


    // You can create a Recorder with default settings.

    // CameraX will automatically select a suitable quality.

    val recorder = Recorder.Builder().build()


    // Alternatively, to use a specific resolution, you can configure the
    // Recorder with a QualitySelector. This is useful if your app has
    // specific resolution requirements or you want to offer user
    // preferences. 

    // To use a specific quality, you can uncomment the following lines.

    // Get the list of qualities supported for high-speed video. 

    // val supportedQualities = videoCapabilities.getSupportedQualities(DynamicRange.SDR)

    // Build the Recorder using the quality from the supported list.

    // val recorderWithQuality = Recorder.Builder()

    //     .setQualitySelector(QualitySelector.from(supportedQualities.first()))

    //     .build()



    // Create the VideoCapture use case, using either recorder or recorderWithQuality

    val videoCapture = VideoCapture.withOutput(recorder)

    // Now you are ready to configure the session for your desired output...

}
```

*** ** * ** ***

### 2. Choosing Your Output

Now, you decide what kind of video you want to create. This code would run inside the `setupCamera() suspend` function shown above.

#### Option A: Create a High-Frame-Rate Video

Choose this option if you want the final file to have a high frame rate (e.g., a 120fps video).

```
// Create a builder for the high-speed session

val sessionConfigBuilder = HighSpeedVideoSessionConfig.Builder(videoCapture)

    .setPreview(preview)


// Query and apply a supported frame rate. Common supported frame rates include 120 and 240 fps.

val supportedFrameRateRanges =

    cameraInfo.getSupportedFrameRateRanges(sessionConfigBuilder.build())


sessionConfigBuilder.setFrameRateRange(supportedFrameRateRanges.first())
```

#### **Option B: Create a Ready-to-play Slow-Motion Video**

Choose this option if you want a video that plays in slow motion automatically in any standard video player.

```
// Create a builder for the high-speed session

val sessionConfigBuilder = HighSpeedVideoSessionConfig.Builder(videoCapture)

    .setPreview(preview)



// This is the key: enable automatic slow-motion!

sessionConfigBuilder.setSlowMotionEnabled(true)



// Query and apply a supported frame rate. Common supported frame rates include 120, 240, and 480 fps.

val supportedFrameRateRanges =

   cameraInfo.getSupportedFrameRateRanges(sessionConfigBuilder.build())

sessionConfigBuilder.setFrameRateRange(supportedFrameRateRanges.first())
```

This single flag is the key to creating a ready-to-play slow-motion video. When `setSlowMotionEnabled` is true, CameraX processes the high-speed stream and saves it as a standard **30 fps** video file. The slow-motion speed is determined by the ratio of the capture frame rate to this standard playback rate.

For example:

- Recording at **120 fps** will produce a video that plays back at **1/4x speed** (120 ÷ 30 = 4).
- Recording at **240 fps** will produce a video that plays back at **1/8x speed** (240 ÷ 30 = 8).

*** ** * ** ***

## Putting It All Together: Recording the Video

Once you have configured your `HighSpeedVideoSessionConfig` and bound it to the lifecycle, the final step is to start the recording. The process of preparing output options, starting the recording, and handling video events is the same as it is for a standard video capture.

This post focuses on high-speed configuration, so we won't cover the recording process in detail. For a comprehensive guide on everything from preparing a `FileOutputOptions` or `MediaStoreOutputOptions` object to handling the `VideoRecordEvent` callbacks, please refer to the [VideoCapture documentation](https://developer.android.com/media/camera/camerax/video-capture#videocapture-api-overview).

```
// Bind the session config to the lifecycle

cameraProvider.bindToLifecycle(

    this as LifecycleOwner,

    CameraSelector.DEFAULT_BACK_CAMERA,

    sessionConfigBuilder.build() // Bind the config object from Option A or B

)



// Start the recording using the VideoCapture use case

val recording = videoCapture.output

    .prepareRecording(context, outputOptions) // See docs for creating outputOptions

    .start(ContextCompat.getMainExecutor(context)) { recordEvent ->

        // Handle recording events (e.g., Start, Pause, Finalize)

    }
```

*** ** * ** ***

## Google Photos Support for Slow-Motion Videos

When you enable `setSlowMotionEnabled(true)` in CameraX, the resulting video file is designed to be instantly recognizable and playable as slow-motion in standard video players and gallery apps. Google Photos, in particular, offers enhanced functionality for these slow-motion videos, when the capture frame rate is 120, 240, 360, 480 or 960fps:

- **Distinct UI Recognition in Thumbnail:** In your Google Photos library, slow-motion videos can be identified by specific UI elements, distinguishing them from normal videos.

|---|---|
| ![normal.png](https://developer.android.com/static/blog/assets/normal_e584da1c42_Z9i5AN.webp) | ![slowmotion.png](https://developer.android.com/static/blog/assets/slowmotion_af17b75fb9_Z1l2CLu.webp) |
| Normal video thumbnail | Slow-motion video thumbnail |

- **Adjustable Speed Segments during Playback:** When playing a slow-motion video, Google Photos provides controls to adjust which parts of the video play at slow speed and which play at normal speed, giving users creative control. The edited video can then be exported as a new video file using the **Share** button, preserving the slow-motion segments you defined.

|---|---|
| ![normal2.png](https://developer.android.com/static/blog/assets/normal2_865208c389_utnXO.webp) | ![slowmotion2.png](https://developer.android.com/static/blog/assets/slowmotion2_2378e880d0_ZqsQxG.webp) |
| Normal video playback | Slow-motion video playback with editing controls |

*** ** * ** ***

### A Note on Device Support

CameraX's high-speed API relies on the underlying Android [CamcorderProfile](https://developer.android.com/reference/android/media/CamcorderProfile) system to determine which high-speed resolutions and frame rates a device supports. CamcorderProfiles are validated by the [Android Compatibility Test Suite (CTS)](https://source.android.com/docs/compatibility/cts), which means you can be confident in the device's reported video recording capabilities.

This means that a device's ability to record slow-motion video with its built-in camera app does not guarantee that the CameraX high-speed API will function. This discrepancy occurs because device manufacturers are responsible for populating the `CamcorderProfile` entries in their device's firmware, and sometimes necessary high-speed profiles like `CamcorderProfile.QUALITY_HIGH_SPEED_1080P` and `CamcorderProfile.QUALITY_HIGH_SPEED_720P` are not included. When these profiles are missing, `Recorder.getHighSpeedVideoCapabilities()` will return `null`.

Therefore, it's essential to always use `Recorder.getHighSpeedVideoCapabilities()` to check for supported features programmatically, as this is the most reliable way to ensure a consistent experience across different devices. If you try to bind a `HighSpeedVideoSessionConfig` on a device where `Recorder.getHighSpeedVideoCapabilities()` returns null, the operation will fail with an `IllegalArgumentException`. You can confirm support on **Google Pixel devices**, as they consistently include these high-speed profiles. Additionally, various devices from other manufacturers, such as the Motorola Edge 30, OPPO Find N2 Flip, and Sony Xperia 1 V, also support the high-speed video capabilities.

*** ** * ** ***

### Conclusion

The CameraX high-speed video API is both powerful and flexible. Whether you need true high-frame-rate footage for technical analysis or want to add cinematic slow-motion effects to your app, the `HighSpeedVideoSessionConfig` provides a unified and simple solution. By understanding the role of the `setSlowMotionEnabled` flag, you can easily support both use cases and give your users more creative control.

###### Written by:

-

  ## [Leo Huang](https://developer.android.com/blog/authors/leo-huang)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/leo-huang) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

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