---
title: https://developer.android.com/media/camera/camerax/take-photo/zsl
url: https://developer.android.com/media/camera/camerax/take-photo/zsl
source: md.txt
---

# Reduce latency with Zero-Shutter Lag

| **Note:** Zero-Shutter Lag is an experimental feature. To leave feedback on Zero-Shutter Lag, join the[Android CameraX Discussion Group](https://groups.google.com/a/android.com/g/camerax-developers).

Starting in[CameraX 1.2](https://developer.android.com/jetpack/androidx/releases/camera), Zero-Shutter Lag is available as a capture mode. Enable Zero-Shutter Lag to significantly reduce latency compared to the[default capture mode](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MINIMIZE_LATENCY()), so you never miss the shot.

## Enable Zero-Shutter Lag

To enable Zero-Shutter Lag, pass[`CAPTURE_MODE_ZERO_SHOT_LAG`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_ZERO_SHUTTER_LAG())to[`ImageCapture.Builder.setCaptureMode()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder#setCaptureMode(int)). If unsuccessful,`setCaptureMode()`falls back to`CAPTURE_MODE_MINIMIZE_LATENCY`.

For more on capture modes, see the[Image capture guide](https://developer.android.com/media/camera/camerax/take-photo#set-capture-mode).

## How it works

Zero-Shutter Lag uses a ring buffer that stores the three most recent capture frames. When a user presses the capture button, CameraX invokes[`takePicture()`](https://developer.android.com/reference/android/hardware/Camera#takePicture(android.hardware.Camera.ShutterCallback,%20android.hardware.Camera.PictureCallback,%20android.hardware.Camera.PictureCallback,%20android.hardware.Camera.PictureCallback)), and the ring buffer retrieves the captured frame with the timestamp that is closest to that of the button press. CameraX then[reprocesses](https://developer.android.com/reference/android/hardware/camera2/CameraDevice#reprocessing)the capture session to generate an image from that frame, which saves to disk in JPEG format.

## Prerequisites

Before you enable Zero-Shutter Lag, use[`isZslSupported()`](https://developer.android.com/reference/androidx/camera/core/CameraInfo#isZslSupported())to determine if your device meets the following requirements:

- Targets Android 6.0+ (API level 23 and higher).
- Supports[`PRIVATE`reprocessing](https://developer.android.com/reference/android/hardware/camera2/CameraMetadata#REQUEST_AVAILABLE_CAPABILITIES_PRIVATE_REPROCESSING).

For devices that don't meet the minimum requirements, CameraX falls back to`CAPTURE_MODE_MINIMIZE_LATENCY`.

Zero-Shutter Lag is only available for[Image capture](https://developer.android.com/training/camerax/take-photo). You cannot enable it for[Video capture](https://developer.android.com/training/camerax/video-capture)or with[Camera extensions](https://developer.android.com/training/camera/camera-extensions).

Finally, because using flash results in greater latency, Zero-Shutter Lag does not work when flash is ON or in AUTO mode. For more information about setting the flash mode, see[`setFlashMode()`](https://developer.android.com/media/camera/camerax/take-photo#set-flash-mode).