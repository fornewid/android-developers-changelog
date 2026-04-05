---
title: HDR video capture  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/camera2/hdr-video-capture
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# HDR video capture Stay organized with collections Save and categorize content based on your preferences.



**Note:** This page refers to the [Camera2](/reference/android/hardware/camera2/package-summary) package. Unless your app requires specific, low-level features from Camera2, we recommend using [CameraX](/camerax). Both CameraX and Camera2 support Android 5.0 (API level 21) and higher.

The [Camera2 APIs](/reference/android/hardware/camera2/package-summary) support
High Dynamic Range (HDR) video capture, which enables you to preview and
record HDR video content using your camera. Compared to Standard Dynamic
Range (SDR), HDR offers a wider range of colors and increases the dynamic
range of the luminance component (from the current 100 cd/m2 to 1000s of cd/m2).
This results in video quality that more closely matches real life, with
richer colors, brighter highlights, and darker shadows.

See how HDR video captures a sunset in more vibrant detail.

![](/static/images/training/camera/camera2/sdr_comparison.png)
![](/static/images/training/camera/camera2/hdr_comparison.png)


**Figure 1.** SDR (top) vs. HDR (bottom) video quality comparison.

**Note:** Starting in Android 13, camera devices with 10-bit camera output
must support the HLG10 format for HDR capture and playback.
For more information, see [HDR formats](#hdr_formats).

## Device prerequisites

Not all Android devices support HDR video capture.
Before capturing HDR video in your app, determine if your device meets
the following prerequisites:

* Targets Android 13 (API level 33).
* Has a 10-bit or higher capable camera sensor. For more information about HDR
  Support, see [Check for HDR support](#check_for_hdr_support).

Because not all devices meet the prerequisites, you can add a separate code
path when setting up HDR video capture in your app.
This lets your app fall back to SDR on incompatible devices.
Also, consider adding a UI option for SDR. The user can then toggle
between SDR and HDR for their video recording needs.

## HDR capture architecture

The following diagram shows the main components of the HDR capture architecture.

![HDR capture architecture diagram.](/static/images/training/camera/camera2/hdr_capture_architecture_diagram.png)


**Figure 2.** HDR capture architecture diagram.

When a camera device captures a frame in HDR, the Camera2 framework allocates
a buffer that stores the processed camera sensor output.
It also attaches the respective HDR metadata if required by the HDR profile.
The Camera2 framework then queues the populated buffer for the output surface
referenced in the [`CaptureRequest`](/training/camera2/capture-sessions-requests#repeating-capture-requests), such as a display or
video encoder, as shown in the diagram.

**Note:** Camera apps don't have access to HDR metadata via the Camera2 APIs or any
[Media APIs](https://developer.android.com/reference/android/media/package-summary)
in Android 13.

## Check for HDR support

Before capturing HDR video in your app, determine if the device supports
your desired HDR profile.

Use the [`CameraManager`](/reference/android/hardware/camera2/CameraManager) [`getCameraCharacteristics()`](/reference/android/hardware/camera2/CameraManager#getCameraCharacteristics(java.lang.String)) method to obtain a
[`CameraCharacteristics`](/reference/android/hardware/camera2/CameraCharacteristics)
instance, which you can query for your device’s HDR capabilities.

The following steps check if a device supports HLG10.
HLG10 is the baseline HDR standard that device makers must support
on cameras with 10-bit output.

1. First, check if the device supports 10-bit profiles (the bit-depth for HLG10):

   ### Kotlin

   ```
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
2. Next, check if the device supports HLG10 (or [another supported profile](/reference/android/hardware/camera2/params/DynamicRangeProfiles)):

   ### Kotlin

   ```
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

If the device supports HDR, `isHLGSupported()` always return `true`.
For more information, see the
[`CameraCharacteristics`](/reference/android/hardware/camera2/CameraCharacteristics)
reference documentation.

## Set up HDR capture

After ensuring that your device supports HDR, set up your app to capture
a raw HDR video stream from the camera.
Use [`setDynamicRangeProfile()`](/reference/android/hardware/camera2/params/OutputConfiguration#setDynamicRangeProfile(long)) to provide the stream’s [`OutputConfiguration`](/reference/android/hardware/camera2/params/OutputConfiguration)
with a device-supported HDR profile, which is then passed
to the [`CameraCaptureSession`](/reference/android/hardware/camera2/CameraCaptureSession)
upon creation.
See the [list](/reference/android/hardware/camera2/params/DynamicRangeProfiles#constants_1) of supported HDR profiles.

In the following code sample, `setupSessionDynamicRangeProfile()` first checks
that the device is running Android 13.
Then, it sets up the `CameraCaptureSession` with the device-supported
HDR profile as an `OutputConfiguration`:

### Kotlin

```
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
```

```
          device.createCaptureSessionByOutputConfigurations(
                  outputConfigs, stateCallback, handler)
          return true
      } else {
          device.createCaptureSession(targets, stateCallback, handler)
          return false
      }
  }
```

}