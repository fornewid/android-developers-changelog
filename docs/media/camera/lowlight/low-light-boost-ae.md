---
title: https://developer.android.com/media/camera/lowlight/low-light-boost-ae
url: https://developer.android.com/media/camera/lowlight/low-light-boost-ae
source: md.txt
---

# Low Light Boost Auto Exposure Mode

Android 15 introduces*Low Light Boost Auto Exposure (AE) Mode* , a new auto-exposure mode available to both[Camera 2](https://developer.android.com/media/camera/camera2)and the[night mode camera extension](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT). Low Light Boost AE Mode automatically adjusts the brightness of the Preview stream in low-light conditions. This is different from how the night mode camera extension creates still images, because night mode combines a burst of photos to create a single, enhanced image. While night mode works very well for creating a still image, it can't create a continuous stream of frames, but Low Light Boost AE Mode can. Thus, Low Light Boost AE Mode enables new camera capabilities, such as the following:

- Providing an enhanced image preview, so users are better able to frame their low-light pictures.
- Scanning QR codes in low light.

If you enable Low Light Boost AE Mode, it automatically turns on when there's a low light level, and turns off when there's more light.

Apps can record off the Preview stream in low-light conditions to save a brightened video.
| **Note:** Because Low Light Boost AE Mode uses a different mechanism than night mode still capture, the two images won't look identical. Night mode still capture provides a better result when you just want to capture a single image, but Low Light Boost AE Mode is able to show you enhanced images in real time.

You can use Low Light Boost AE Mode either in[Camera2](https://developer.android.com/media/camera/camera2)or through[camera extensions](https://developer.android.com/media/camera/camera2/extensions-api). This document covers how to use Low Light Boost AE Mode with Camera2. You can also use Low Light Boost AE Mode with the Night Mode camera extension if it is supported by the device.

## Check for availability

Before using Low Light Boost AE Mode, check that it's supported on the device. If it's available, Low Light Boost AE Mode is one of the exposure modes listed in[`camera2.CameraCharacteristics.CONTROL_AE_AVAILABLE_MODES`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#CONTROL_AE_AVAILABLE_MODES). (Low Light Boost is its own auto exposure setting, since other auto exposure settings aren't compatible with the preview brightening performed by Low Light Boost AE Mode.)

So, to check if Low Light Boost AE Mode is available, call[`CameraCharacteristics.get(CameraCharacteristics.CONTROL_AE_AVAILABLE_MODES)`](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#get(android.hardware.camera2.CameraCharacteristics.Key%3CT%3E))and check if the returned modes include[`ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY):  

### Kotlin

```kotlin
val characteristics = cameraManager.getCameraCharacteristics(cameraId)
val autoExposureModes =
    characteristics.get(CameraCharacteristics.CONTROL_AE_AVAILABLE_MODES)!!
val lowLightBoostSupported = autoExposureModes.contains(
        CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY)

if (lowLightBoostSupported) {
  // Enable Low Light Boost AE Mode (next section)
} else {
  // Proceed without Low Light Boost AE Mode
}
```

### Java

```java
CameraCharacteristics characteristics =
    mCameraManager.getCameraCharacteristics(cameraId);
int[] autoExposureModes =
    characteristics.get(CameraCharacteristics.CONTROL_AE_AVAILABLE_MODES);
boolean lowLightBoostSupported = autoExposureModes.contains(
        CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY);

if (lowLightBoostSupported) {
  // Enable Low Light Boost AE Mode (next section)
} else {
  // Proceed without Low Light Boost AE Mode
}
```

## Enable Low Light Boost AE Mode

To enable Low Light Boost AE Mode in a Camera2 session, set[`CaptureRequest.CONTROL_AE_MODE`](https://developer.android.com/reference/android/hardware/camera2/CaptureRequest#CONTROL_AE_MODE)to[`ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY). After you do so, you'll need to confirm that Low Light Boost AE Mode was turned on; you can do this by checking the[`CaptureResult.CONTROL_AE_MODE`](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#CONTROL_AE_MODE)field. You need to check because Low Light Boost is not compatible with all camera configurations. For example, high-speed recording doesn't support Low Light Boost AE Mode, due to FPS considerations. If Low Light Boost AE Mode is not turned on, you may need to change the camera configuration and try again.  

### Kotlin

```kotlin
val captureRequestBuilder = camera.createCaptureRequest(
  CameraDevice.TEMPLATE_PREVIEW)
if (isLowLightBoostAvailable(cameraId)) {
  captureRequestBuilder.set(
    CaptureRequest.CONTROL_AE_MODE,
    CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY
  )
}
// other capture request params

session.setRepeatingRequest(
  captureRequestBuilder.build(),
  object : CaptureCallback() {
    @Override
    fun onCaptureCompleted(session: CameraCaptureSession,
        request: CaptureRequest, result: TotalCaptureResult) {
      // verify Low Light Boost AE Mode AE mode set successfully
      result.get(CaptureResult.CONTROL_AE_MODE) ==
          CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY
    }
  },
  cameraHandler
)
```

### Java

```java
CaptureRequest.Builder captureRequestBuilder =
  mCamera.createCaptureRequest(CameraDevice.TEMPLATE_PREVIEW);
if (isLowLightBoostAvailable(cameraId)) {
  captureRequestBuilder.set(
    CaptureRequest.CONTROL_AE_MODE,
    CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY);
}
// other capture request params

mSession.setRepeatingRequest(
  captureRequestBuilder.build(),
  new CaptureCallback() {
    @Override
    public void onCaptureCompleted(CameraCaptureSession session,
        CaptureRequest request, TotalCaptureResult result) {
      // verify Low Light Boost AE Mode AE mode set successfully
      result.get(CaptureResult.CONTROL_AE_MODE) ==
          CameraMetadata.CONTROL_AE_MODE_ON_LOW_LIGHT_BOOST_BRIGHTNESS_PRIORITY;
    }
  },
  mCameraHandler
);
```

## Monitor Low Light Boost AE Mode

Low Light Boost AE Mode brightens the preview stream in low-light conditions, and doesn't have any effect if the environment is already bright enough for normal capture. You can confirm whether Low Light Boost AE Mode is currently active by checking the[`CaptureResult.CONTROL_LOW_LIGHT_BOOST_STATE`](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#CONTROL_LOW_LIGHT_BOOST_STATE)field. If you've turned Low Light Boost AE Mode on*and* it's currently active, the field is set to[`CameraMetadata.CONTROL_LOW_LIGHT_BOOST_STATE_ACTIVE`](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#CONTROL_LOW_LIGHT_BOOST_STATE_ACTIVE). You might then show a moon icon or some other indication that the preview is being brightened.  

### Kotlin

```kotlin
session.setRepeatingRequest(
  captureRequestBuilder.build(),
  object : CaptureCallback() {
    @Override
    fun onCaptureCompleted(session: CameraCaptureSession,
        request: CaptureRequest, result: TotalCaptureResult) {
      // check if Low Light Boost AE Mode is active or inactive
      if (result.get(CaptureResult.CONTROL_LOW_LIGHT_BOOST_STATE) ==
        CameraMetadata.CONTROL_LOW_LIGHT_BOOST_STATE_ACTIVE) {
        // Low Light Boost AE Mode state is active
        // Show Moon Icon
      } else {
        // Low Light Boost AE Mode state is inactive or AE mode is not set
        // to Low Light Boost AE Mode
        // Hide Moon Icon
      }
    }
  },
  cameraHandler
)
```

### Java

```java
mSession.setRepeatingRequest(
  captureRequestBuilder.build(),
  new CaptureCallback() {
    @Override
    public void onCaptureCompleted(CameraCaptureSession session,
        CaptureRequest request, TotalCaptureResult result) {
      // check if Low Light Boost AE Mode is active or inactive
      if (result.get(CaptureResult.CONTROL_LOW_LIGHT_BOOST_STATE) ==
        CameraMetadata.CONTROL_LOW_LIGHT_BOOST_STATE_ACTIVE) {
        // Low Light Boost AE Mode state is active
        // Show Moon Icon
      } else {
        // Low Light Boost AE Mode state is inactive or AE mode is not set
        // to Low Light Boost AE Mode
        // Hide Moon Icon
      }
    }
  },
  mCameraHandler
);
```