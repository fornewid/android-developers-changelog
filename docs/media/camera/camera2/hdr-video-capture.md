---
title: https://developer.android.com/media/camera/camera2/hdr-video-capture
url: https://developer.android.com/media/camera/camera2/hdr-video-capture
source: md.txt
---

# HDR video capture

<br />

**Note:** This page refers to the[Camera2](https://developer.android.com/reference/android/hardware/camera2/package-summary)package. Unless your app requires specific, low-level features from Camera2, we recommend using[CameraX](https://developer.android.com/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

<br />

The[Camera2 APIs](https://developer.android.com/reference/android/hardware/camera2/package-summary)support High Dynamic Range (HDR) video capture, which enables you to preview and record HDR video content using your camera. Compared to Standard Dynamic Range (SDR), HDR offers a wider range of colors and increases the dynamic range of the luminance component (from the current 100 cd/m2 to 1000s of cd/m2). This results in video quality that more closely matches real life, with richer colors, brighter highlights, and darker shadows.

See how HDR video captures a sunset in more vibrant detail.
![](https://developer.android.com/static/images/training/camera/camera2/sdr_comparison.png)![](https://developer.android.com/static/images/training/camera/camera2/hdr_comparison.png)**Figure 1.**SDR (top) vs. HDR (bottom) video quality comparison.**Note:** Starting in Android 13, camera devices with 10-bit camera output must support the HLG10 format for HDR capture and playback. For more information, see[HDR formats](https://developer.android.com/media/camera/camera2/hdr-video-capture#hdr_formats).

## Device prerequisites

Not all Android devices support HDR video capture. Before capturing HDR video in your app, determine if your device meets the following prerequisites:

- Targets Android 13 (API level 33).
- Has a 10-bit or higher capable camera sensor. For more information about HDR Support, see[Check for HDR support](https://developer.android.com/media/camera/camera2/hdr-video-capture#check_for_hdr_support).

Because not all devices meet the prerequisites, you can add a separate code path when setting up HDR video capture in your app. This lets your app fall back to SDR on incompatible devices. Also, consider adding a UI option for SDR. The user can then toggle between SDR and HDR for their video recording needs.

## HDR capture architecture

The following diagram shows the main components of the HDR capture architecture.
![HDR capture architecture diagram.](https://developer.android.com/static/images/training/camera/camera2/hdr_capture_architecture_diagram.png)**Figure 2.**HDR capture architecture diagram.

When a camera device captures a frame in HDR, the Camera2 framework allocates a buffer that stores the processed camera sensor output. It also attaches the respective HDR metadata if required by the HDR profile. The Camera2 framework then queues the populated buffer for the output surface referenced in the[`CaptureRequest`](https://developer.android.com/training/camera2/capture-sessions-requests#repeating-capture-requests), such as a display or video encoder, as shown in the diagram.
| **Note:** Camera apps don't have access to HDR metadata via the Camera2 APIs or any[Media APIs](https://developer.android.com/reference/android/media/package-summary)in Android 13.

## Check for HDR support

Before capturing HDR video in your app, determine if the device supports your desired HDR profile.

Use the[`CameraManager`](https://developer.android.com/reference/android/hardware/camera2/CameraManager)[`getCameraCharacteristics()`](https://developer.android.com/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics(java.lang.String))method to obtain a[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics)instance, which you can query for your device's HDR capabilities.

The following steps check if a device supports HLG10. HLG10 is the baseline HDR standard that device makers must support on cameras with 10-bit output.

1. First, check if the device supports 10-bit profiles (the bit-depth for HLG10):

   ### Kotlin

   ```kotlin
   private fun isTenBitProfileSupported(cameraId: String): Boolean {
     val cameraCharacteristics = cameraManager.getCameraCharacteristics(cameraId)
     val availableCapabilities = cameraCharacteristics.get(CameraCharacteristics.REQUEST_AVAILABLE_CAPABILITIES)
     for (capability in availableCapabilities!!) {
         if (capability == CameraMetadata.REQUEST_AVAILABLE_CAPABILITIES_DYNAMIC_RANGE_TEN_BIT) {
             return true
         }
     }
     return false
   }
   ```
2. Next, check if the device supports HLG10 (or[another supported profile](https://developer.android.com/reference/android/hardware/camera2/params/DynamicRangeProfiles)):

   ### Kotlin

   ```kotlin
   @RequiresApi(api = 33)
   private fun isHLGSupported(cameraId: String): Boolean {
   if (isTenBitProfileSupported(cameraId)) {
     Val cameraCharacteristics = cameraManager.getCameraCharacteristics(cameraId)
     val availableProfiles = cameraCharacteristics
     .get(CameraCharacteristics.REQUEST_AVAILABLE_DYNAMIC_RANGE_PROFILES)!!
     .getSupportedProfiles()

     // Checks for the desired profile, in this case HLG10
     return availableProfiles.contains(DynamicRangeProfiles.HLG10)
   }
   return false;
   }
   ```

If the device supports HDR,`isHLGSupported()`always return`true`. For more information, see the[`CameraCharacteristics`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics)reference documentation.

## Set up HDR capture

After ensuring that your device supports HDR, set up your app to capture a raw HDR video stream from the camera. Use[`setDynamicRangeProfile()`](https://developer.android.com/reference/android/hardware/camera2/params/OutputConfiguration#setDynamicRangeProfile(long))to provide the stream's[`OutputConfiguration`](https://developer.android.com/reference/android/hardware/camera2/params/OutputConfiguration)with a device-supported HDR profile, which is then passed to the[`CameraCaptureSession`](https://developer.android.com/reference/android/hardware/camera2/CameraCaptureSession)upon creation. See the[list](https://developer.android.com/reference/android/hardware/camera2/params/DynamicRangeProfiles#constants_1)of supported HDR profiles.

In the following code sample,`setupSessionDynamicRangeProfile()`first checks that the device is running Android 13. Then, it sets up the`CameraCaptureSession`with the device-supported HDR profile as an`OutputConfiguration`:

<br />

### Kotlin

```kotlin
  /**
  * Creates a [CameraCaptureSession] with a dynamic range profile.
  */
  private fun setupSessionWithDynamicRangeProfile(
          dynamicRange: Long,
          device: CameraDevice,
          targets: List,
          handler: Handler? = null,
          stateCallback: CameraCaptureSession.StateCallback
  ): Boolean {
      if (android.os.Build.VERSION.SDK_INT >=
              android.os.Build.VERSION_CODES.TIRAMISU) {
          val outputConfigs = mutableListOf()
              for (target in targets) {
                  val outputConfig = OutputConfiguration(target)
                  //sets the dynamic range profile, for example DynamicRangeProfiles.HLG10
                  outputConfig.setDynamicRangeProfile(dynamicRange)
                  outputConfigs.add(outputConfig)
              }

<br />




              device.createCaptureSessionByOutputConfigurations(
                      outputConfigs, stateCallback, handler)
              return true
          } else {
              device.createCaptureSession(targets, stateCallback, handler)
              return false
          }
      }




}
  
```

<br />

When your camera app initializes the camera, it sends a repeating[`CaptureRequest`](https://developer.android.com/training/camera2/capture-sessions-requests#repeating-capture-requests)to preview the recording:  

### Kotlin

```kotlin
session.setRepeatingRequest(previewRequest, null, cameraHandler)
```

And also to start the video recording:  

### Kotlin

```kotlin
// Start recording repeating requests, which stops the ongoing preview
//  repeating requests without having to explicitly call
//  `session.stopRepeating`
session.setRepeatingRequest(recordRequest,
        object : CameraCaptureSession.CaptureCallback() {
    override fun onCaptureCompleted(session: CameraCaptureSession,
            request: CaptureRequest, result: TotalCaptureResult) {
        if (currentlyRecording) {
            encoder.frameAvailable()
        }
    }
}, cameraHandler)
```

## Encode the HDR camera stream

To encode the HDR camera stream and write the file to disk, use[`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec#createPersistentInputSurface()).

First, get the[`OutputSurface`](https://developer.android.com/reference/kotlin/androidx/camera/core/impl/OutputSurface), which maps to a buffer that stores raw video data. For`MediaCodec`, use[`createInputSurface()`](https://developer.android.com/reference/android/media/MediaCodec#createInputSurface()).

To initialize`MediaCodec`, an app must create a[`MediaFormat`](https://developer.android.com/reference/android/media/MediaFormat)with a specified codec profile, color space, color range, and transfer function:  

### Kotlin

```kotlin
val mimeType = when {
    dynamicRange == DynamicRangeProfiles.STANDARD -> MediaFormat.MIMETYPE_VIDEO_AVC
    dynamicRange < DynamicRangeProfiles.PUBLIC_MAX ->
            MediaFormat.MIMETYPE_VIDEO_HEVC
    else -> throw IllegalArgumentException("Unknown dynamic range format")
}

val codecProfile = when {
    dynamicRange == DynamicRangeProfiles.HLG10 ->
            MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10
    dynamicRange == DynamicRangeProfiles.HDR10 ->
            MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10HDR10
    dynamicRange == DynamicRangeProfiles.HDR10_PLUS ->
            MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10HDR10Plus
    else -> -1
}
// Failing to correctly set color transfer causes quality issues
// for example, washout and color clipping
val transferFunction = when (codecProfile) {
    MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10 ->
            MediaFormat.COLOR_TRANSFER_HLG
    MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10HDR10 ->
            MediaFormat.COLOR_TRANSFER_ST2084
    MediaCodecInfo.CodecProfileLevel.HEVCProfileMain10HDR10Plus ->
            MediaFormat.COLOR_TRANSFER_ST2084
    else -> MediaFormat.COLOR_TRANSFER_SDR_VIDEO
}

val format = MediaFormat.createVideoFormat(mimeType, width, height)

// Set some properties.  Failing to specify some of these can cause the MediaCodec
// configure() call to throw an exception.
format.setInteger(MediaFormat.KEY_COLOR_FORMAT,
        MediaCodecInfo.CodecCapabilities.COLOR_FormatSurface)
format.setInteger(MediaFormat.KEY_BIT_RATE, bitRate)
format.setInteger(MediaFormat.KEY_FRAME_RATE, frameRate)
format.setInteger(MediaFormat.KEY_I_FRAME_INTERVAL, IFRAME_INTERVAL)

if (codecProfile != -1) {
    format.setInteger(MediaFormat.KEY_PROFILE, codecProfile)
    format.setInteger(MediaFormat.KEY_COLOR_STANDARD,
            MediaFormat.COLOR_STANDARD_BT2020)
    format.setInteger(MediaFormat.KEY_COLOR_RANGE, MediaFormat.COLOR_RANGE_LIMITED)
    format.setInteger(MediaFormat.KEY_COLOR_TRANSFER, transferFunction)
    format.setFeatureEnabled(MediaCodecInfo.CodecCapabilities.FEATURE_HdrEditing,
            true)
}

mediaCodec.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
```

For more details about implementation, see the Camera2Video sample app's[`EncoderWrapper.kt`](https://github.com/android/camera-samples/blob/main/Camera2Video/app/src/main/java/com/example/android/camera2/video/EncoderWrapper.kt).

## HDR formats

Starting in Android 13, camera devices with 10-bit output capabilities must support HLG10 for HDR capture and[playback](https://source.android.com/devices/tech/display/hdr). In addition, device makers can enable any HDR format of their choosing using the[HDR capture architecture](https://developer.android.com/media/camera/camera2/hdr-video-capture#hdr_capture_architecture).

The following table sums up the available HDR formats and their capabilities for HDR video capture.

|      Format      | Transfer Function (TF) | Metadata | Codec | Bit Depth |
|------------------|------------------------|----------|-------|-----------|
| HLG10            | HLG                    | No       | HEVC  | 10-bit    |
| HDR10            | PQ                     | Static   | HEVC  | 10-bit    |
| HDR10+           | PQ                     | Dynamic  | HEVC  | 10-bit    |
| Dolby Vision 8.4 | HLG                    | Dynamic  | HEVC  | 10-bit    |

## Resources

For a working app with HDR video capture functionality, see the[Camera2Video sample](https://github.com/android/camera-samples/tree/main/Camera2Video)on GitHub.