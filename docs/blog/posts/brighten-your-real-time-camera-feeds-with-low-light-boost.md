---
title: https://developer.android.com/blog/posts/brighten-your-real-time-camera-feeds-with-low-light-boost
url: https://developer.android.com/blog/posts/brighten-your-real-time-camera-feeds-with-low-light-boost
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Brighten Your Real-Time Camera Feeds with Low Light Boost

###### 7-min read

![](https://developer.android.com/static/blog/assets/Brighten_Real_Time_0d4c07ef35_U1qMY.webp) 17 Dec 2025 [![](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_ZJ6yBx.webp)](https://developer.android.com/blog/authors/donovan-mcmurray) [##### Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray)

###### Developer Relations Engineer

We recently shared[how Instagram enabled users to take stunning low light photos](https://android-developers.googleblog.com/2024/12/instagram-on-android-low-light-photos.html) using Night Mode. That feature is perfect for still images, where there's time to combine multiple exposures to create a high-quality static shot. But what about the moments that happen *between* the photos? Users need to interact with the camera more than just the moment the shutter button is pressed. They also use the preview to compose their scene or scan QR codes.

Today, we're diving into [Low Light Boost (LLB)](https://developer.android.com/media/camera/lowlight), a powerful feature designed to brighten real-time camera streams. Unlike Night Mode, which requires a hold-still capture duration, Low Light Boost works instantaneously on your live preview and video recordings. LLB automatically adjusts how much brightening is needed based on available light, so it's optimized for every environment.

With a recent update, LLB allows Instagram users to line up the perfect shot, and then their existing Night Mode implementation results in the same high quality low-light photos their users have been enjoying for over a year.

## Why Real-time Brightness Matters

While Night Mode aims to improve final image quality, Low Light Boost is intended for usability and interactivity in dark environments. Another important factor to consider is that -- even though they work together very well -- you can use LLB and Night Mode independently, and you'll see with some of these use cases, LLB has value on its own when Night Mode photos aren't needed. Here is how LLB improves the user experience:

- **Better Framing \& Capture:** In dimly lit scenes, a standard camera preview can be pitch black. LLB brightens the viewfinder, allowing users to actually see what they are framing before they hit the shutter button. For this experience, you can use Night Mode for the best quality low-light photo result, or you can let LLB give the user a "what you see is what you get" photo result.
- **Reliable Scanning:** QR codes are ubiquitous, but scanning them in a dark restaurant or parking garage is often frustrating. With a significantly brighter camera feed, scanning algorithms can reliably detect and decode QR codes even in very dim environments.
- **Enhanced Interactions:** For apps involving live video interactions (like AI assistants or video calls) LLB increases the amount of perceivable information, ensuring the computer vision models have enough data to work with

## The Difference in Instagram

![LLB_IG_demo_white_background.gif](https://developer.android.com/static/blog/assets/LLB_IG_demo_white_background_c12989c682_k2r0k.webp)

The engineering team behind the Android Instagram app is always hard at work to provide a state-of-the-art camera experience for their users. You can see in the above example just what a difference LLB makes on a Pixel 10 Pro.
![lowlight.png](https://developer.android.com/static/blog/assets/lowlight_b6a40d505e_QudAb.webp)

It's easy to imagine the difference this makes in the user experience. If users aren't able to see what they're capturing, then there's a higher chance they'll abandon the capture.
![lowlight1.png](https://developer.android.com/static/blog/assets/lowlight1_136eb50ee9_ZIxJEY.webp)

## Choosing Your Implementation

There are two ways to implement Low Light Boost to provide the best experience across the widest range of devices:

1. **Low Light Boost AE Mode:** This is a hardware-layer auto-exposure mode. It offers the highest quality and performance because it fine-tunes the Image Signal Processor (ISP) pipeline directly. **Always check for this first.**
2. **Google Low Light Boost:** If the device doesn't support the AE mode, you can fall back to this software-based solution provided by Google Play services. It applies post-processing to the camera stream to brighten it. As an all-software solution, it is available on more devices, so this implementation helps you reach more devices with LLB.

### Low Light Boost AE Mode (Hardware)

**Mechanism:**   
This mode is supported on devices running Android 15 and newer and requires the OEM to have implemented the support in HAL (currently available on Pixel 10 devices). It integrates directly with the camera's Image Signal Processor (ISP). If you set [CaptureRequest.CONTROL_AE_MODE](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AE_MODE) to [CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY), the camera system takes control.

**Behavior:**   
The HAL/ISP analyzes the scene and adjusts sensor and processing parameters, often including increasing exposure time, to brighten the image. This can yield frames with a significantly improved signal-to-noise ratio (SNR) because the extended exposure time, rather than an increase in digital sensor gain (ISO), allows the sensor to capture more light information.

**Advantage:**   
Potentially better image quality and power efficiency as it leverages dedicated hardware pathways.

**Trade off:**   
May result in a lower frame rate in very dark conditions as the sensor needs more time to capture light. The frame rate can drop to as low as 10 FPS in very low light conditions.

### Google Low Light Boost (Software via Google Play Services)

**Mechanism:**   
This solution, distributed as an [optional module via Google Play services](https://developers.google.com/android/reference/com/google/android/gms/cameralowlight/package-summary), applies post-processing to the camera stream. It uses a sophisticated realtime image enhancement technology called HDRNet.

**Google HDRNet:**   
This deep learning model analyzes the image at a lower resolution to predict a compact set of parameters (a bilateral grid). This grid then guides the efficient, spatially-varying enhancement of the full-resolution image on the GPU. The model is trained to brighten and improve image quality in low-light conditions, with a focus on face visibility.

**Process Orchestration:**   
The HDRNet model and its accompanying logic are orchestrated by the Low Light Boost processor. This includes:

1. Scene Analysis:  
   A custom calculator that estimates the true scene brightness using camera metadata (sensor sensitivity, exposure time, etc.) and image content. This analysis determines the boost level.
2. HDRNet Processing:  
   Applies the HDRNet model to brighten the frame. The model used is tuned for low light scenes and optimized for realtime performance.
3. Blending:  
   The original and HDRNet processed frames are blended. The amount of blending applied is dynamically controlled by the scene brightness calculator, ensuring a smooth transition between boosted and unboosted states.

![low-light-boost-processor-diagram.png](https://developer.android.com/static/blog/assets/low_light_boost_processor_diagram_0dd70eed34_1IY9im.webp)

**Advantage:**   
Works on a broader range of devices (currently supports Samsung S22 Ultra, S23 Ultra, S24 Ultra, S25 Ultra, and Pixel 6 through Pixel 9) without requiring specific HAL support. Maintains the camera's frame rate as it's a post-processing effect.

**Trade-off:**   
As a post-processing method, the quality is limited by the information present in the frames delivered by the sensor. It cannot recover details lost due to extreme darkness at the sensor level.

By offering both hardware and software pathways, Low Light Boost provides a scalable solution to enhance low-light camera performance across the Android ecosystem. Developers should prioritize the AE mode where available and use the Google Low Light Boost as a robust fallback.

## Implementing Low Light Boost in Your App

Now let's look at how to implement both LLB offerings. You can implement the following whether you use CameraX or Camera2 in your app. For the best results, we recommend implementing both Step 1 and Step 2.

### Step 1: Low Light Boost AE Mode

Available on select devices running Android 15 and higher, LLB AE Mode functions as a specific Auto-Exposure (AE) mode.

#### 1. Check for Availability

First, check if the camera device supports LLB AE Mode.

```
val cameraInfo = cameraProvider.getCameraInfo(cameraSelector)
val isLlbSupported = cameraInfo.isLowLightBoostSupported
```

#### 2. Enable the Mode

If supported, you can enable LLB AE Mode using CameraX's CameraControl object.

```
// After setting up your camera, use the CameraInfo object to enable LLB AE Mode.
camera = cameraProvider.bindToLifecycle(...)

if (isLlbSupported) {
  try {
    // The .await() extension suspends the coroutine until the
    // ListenableFuture completes. If the operation fails, it throws
    // an exception which we catch below.
    camera?.cameraControl.enableLowLightBoostAsync(true).await()
  } catch (e: IllegalStateException) {
    Log.e(TAG, "Failed to enable low light boost: not available on this device or with the current camera configuration", e)
  } catch (e: CameraControl.OperationCanceledException) {
    Log.e(TAG, "Failed to enable low light boost: camera is closed or value has changed", e)
  }
}
```

#### 3. Monitor the State

Just because you requested the mode doesn't mean it's currently "boosting." The system only activates the boost when the scene is actually dark. You can set up an [Observer](https://developer.android.com/reference/androidx/lifecycle/Observer) to update your UI (like showing a moon icon) or convert to a Flow using the extension function asFlow().

```
if (isLlbSupported) {
  camera?.cameraInfo.lowLightBoostState.asFlow().collectLatest { state ->
    // Update UI accordingly
    updateMoonIcon(state == LowLightBoostState.ACTIVE)
  }
}
```

You can read the full guide on[Low Light Boost AE Mode here](https://developer.android.com/media/camera/lowlight/low-light-boost-ae).

### Step 2: Google Low Light Boost

For devices that don't support the hardware AE mode, Google Low Light Boost acts as a powerful fallback. It uses a LowLightBoostSession to intercept and brighten the stream.

#### 1. Add Dependencies

This feature is delivered via Google Play services.

```
implementation("com.google.android.gms:play-services-camera-low-light-boost:16.0.1-beta06")
// Add coroutines-play-services to simplify Task APIs
implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.10.2")
```

#### 2. Initialize the Client

Before starting your camera, use the LowLightBoostClient to ensure the module is installed and the device is supported.

```
val llbClient = LowLightBoost.getClient(context)

// Check support and install if necessary
val isSupported = llbClient.isCameraSupported(cameraId).await()
val isInstalled = llbClient.isModuleInstalled().await()

if (isSupported && !isInstalled) {
    // Trigger installation
    llbClient.installModule(installCallback).await()
}
```

#### 3. Create a LLB Session

Google LLB processes each frame, so you must give your display Surface to the `LowLightBoostSession`, and it gives you back a Surface that has the brightening applied. For Camera2 apps, you can add the resulting Surface with [CaptureRequest.Builder.addTarget()](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest.Builder#addTarget(android.view.Surface)). For CameraX, this processing pipeline aligns best with the [CameraEffect](https://developer.android.com/reference/androidx/camera/core/CameraEffect#CameraEffect(int,java.util.concurrent.Executor,androidx.camera.core.SurfaceProcessor,androidx.core.util.Consumer%3Cjava.lang.Throwable%3E)) class, where you can apply the effect with a [SurfaceProcessor](https://developer.android.com/reference/androidx/camera/core/SurfaceProcessor) and provide it back to your Preview with a [SurfaceProvider](https://developer.android.com/reference/androidx/camera/core/Preview.SurfaceProvider), as seen in this code.

```
// With a SurfaceOutput from SurfaceProcessor.onSurfaceOutput() and a
// SurfaceRequest from Preview.SurfaceProvider.onSurfaceRequested(),
// create a LLB Session.
suspend fun createLlbSession(surfaceRequest: SurfaceRequest, outputSurfaceForLlb: Surface) {
  // 1. Create the LLB Session configuration
  val options = LowLightBoostOptions(
    outputSurfaceForLlb,
    cameraId,
    surfaceRequest.resolution.width,
    surfaceRequest.resolution.height,
    true // Start enabled
  )

  // 2. Create the session.
  val llbSession = llbClient.createSession(options, callback).await()

  // 3. Get the surface to use.
  val llbInputSurface = llbSession.getCameraSurface()

  // 4. Provide the surface to the CameraX Preview UseCase.
  surfaceRequest.provideSurface(llbInputSurface, executor, resultListener)

  // 5. Set the scene detector callback to monitor how much boost is being applied.
  val onSceneBrightnessChanged = object : SceneDetectorCallback {
    override fun onSceneBrightnessChanged(
      session: LowLightBoostSession,
      boostStrength: Float
    ) {
      // Monitor the boostStrength from 0 (no boosting) to 1 (maximum boosting)
    }
  }
  llbSession.setSceneDetectorCallback(onSceneBrightnessChanged, null)
}
```

#### 4. Pass in the Metadata

For the algorithm to work, it needs to analyze the camera's auto-exposure state. You must pass capture results back to the LLB session. In CameraX, this can be done by extending your Preview.Builder with [Camera2Interop.Extender.setSessionCaptureCallback()](https://developer.android.com/reference/androidx/camera/camera2/interop/Camera2Interop.Extender#setSessionCaptureCallback(android.hardware.camera2.CameraCaptureSession.CaptureCallback)).

```
Camera2Interop.Extender(previewBuilder).setSessionCaptureCallback(
  object : CameraCaptureSession.CaptureCallback() {
    override fun onCaptureCompleted(
      session: CameraCaptureSession,
      request: CaptureRequest,
      result: TotalCaptureResult
    ) {
      super.onCaptureCompleted(session, request, result)
      llbSession?.processCaptureResult(result)
    }
  }
)
```

Detailed implementation steps for the client and session can be found in the[Google Low Light Boost guide](https://developer.android.com/media/camera/lowlight/low-light-boost-gp).

## Next Steps

By implementing these two options, you ensure that your users can see clearly, scan reliably, and interact effectively, regardless of the lighting conditions.

To see these features in action within a complete, production-ready codebase, check out the[**Jetpack Camera App**](https://github.com/google/jetpack-camera-app) on GitHub. It implements both [LLB AE Mode](https://github.com/google/jetpack-camera-app/blob/86f89d814ae5076b33a594e9b8f453020da0ed8a/core/camera/src/main/java/com/google/jetpackcamera/core/camera/CameraSession.kt#L460) and [Google LLB](https://github.com/google/jetpack-camera-app/blob/86f89d814ae5076b33a594e9b8f453020da0ed8a/core/camera/src/main/java/com/google/jetpackcamera/core/camera/CameraSession.kt#L184), giving you a reference for your own integration.

###### Written by:

-

  ## [Donovan McMurray](https://developer.android.com/blog/authors/donovan-mcmurray)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/donovan-mcmurray) ![](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_ZJ6yBx.webp) ![](https://developer.android.com/static/blog/assets/Donovan_Mc_Murray_9413499dd8_ZJ6yBx.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

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

- [![](https://developer.android.com/static/blog/assets/dgalpin_30033d2d42_Z1EXpfD.webp)](https://developer.android.com/blog/authors/daniel-galpin) 16 Apr 2026 16 Apr 2026 ![](https://developer.android.com/static/blog/assets/android17banner_359909419a_Z1HMAIH.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [The Fourth Beta of Android 17](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17)

  [arrow_forward](https://developer.android.com/blog/posts/the-fourth-beta-of-android-17) Android 17 has reached beta 4, the last scheduled beta of this release cycle, a critical milestone for app compatibility and platform stability.

  ###### [Daniel Galpin](https://developer.android.com/blog/authors/daniel-galpin) •
  4 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)