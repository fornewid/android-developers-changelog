---
title: https://developer.android.com/media/camera/camerax/take-photo/options
url: https://developer.android.com/media/camera/camerax/take-photo/options
source: md.txt
---

# Configure for optimization, flash, and file format

There are a few additional ways you can configure a device's camera with`ImageCapture`. You do so with`ImageCapture.Builder`methods.
| **Note:** For a general overview of how to capture images with CameraX see the[Image capture guide](https://developer.android.com/media/camera/camerax/take-photo).

## Set capture mode

Use[`ImageCapture.Builder.setCaptureMode()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder#setCaptureMode(int))to configure the capture mode when taking a photo:

- [`CAPTURE_MODE_MINIMIZE_LATENCY`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MINIMIZE_LATENCY()): optimize image capture for latency.
- [`CAPTURE_MODE_MAXIMIZE_QUALITY`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MAXIMIZE_QUALITY()): optimize image capture for image quality.

The capture mode defaults to[`CAPTURE_MODE_MINIMIZE_LATENCY`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MINIMIZE_LATENCY()). For more information, see the[`setCaptureMode()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder#setCaptureMode(int))reference documentation.
| **Note:** There is also an experimental[Zero-Shutter Lag mode](https://developer.android.com/media/camera/camerax/zsl)available through[`CAPTURE_MODE_ZERO_SHOT_LAG`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_ZERO_SHUTTER_LAG()).

## Set flash mode

The default flash mode is[`FLASH_MODE_OFF`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#FLASH_MODE_OFF()). To set the flash mode, use[`ImageCapture.Builder.setFlashMode()`](https://developer.android.com/reference/androidx/camera/core/ImageCapture.Builder#setFlashMode(int)):

- [`FLASH_MODE_ON`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#FLASH_MODE_ON()): Flash is always on.
- [`FLASH_MODE_AUTO`](https://developer.android.com/reference/androidx/camera/core/ImageCapture#FLASH_MODE_AUTO()): Flash is automatically on for low-light shots.

## File types

This workflow demonstrated in this document fully supports the[`JPEG`](https://developer.android.com/reference/android/graphics/ImageFormat#JPEG)format. For sample code that shows how to convert a[`Media.Image`](https://developer.android.com/reference/android/media/Image)object from`YUV_420_888`format to an RGB[`Bitmap`](https://developer.android.com/reference/android/graphics/Bitmap)object, see[`YuvToRgbConverter.kt`](https://github.com/android/camera-samples/blob/3730442b49189f76a1083a98f3acf3f5f09222a3/CameraUtils/lib/src/main/java/com/example/android/camera/utils/YuvToRgbConverter.kt).