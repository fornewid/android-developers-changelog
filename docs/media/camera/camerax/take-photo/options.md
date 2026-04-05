---
title: Configure for optimization, flash, and file format  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/camerax/take-photo/options
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Configure for optimization, flash, and file format Stay organized with collections Save and categorize content based on your preferences.




There are a few additional ways you can configure a device's camera with
`ImageCapture`. You do so with `ImageCapture.Builder` methods.

**Note:** For a general overview of how to capture images with CameraX see the
[Image capture guide](/media/camera/camerax/take-photo).

## Set capture mode

Use [`ImageCapture.Builder.setCaptureMode()`](/reference/androidx/camera/core/ImageCapture.Builder#setCaptureMode(int)) to configure the capture mode
when taking a photo:

* [`CAPTURE_MODE_MINIMIZE_LATENCY`](/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MINIMIZE_LATENCY()): optimize image capture for latency.
* [`CAPTURE_MODE_MAXIMIZE_QUALITY`](/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MAXIMIZE_QUALITY()): optimize image capture for image
  quality.

The capture mode defaults to [`CAPTURE_MODE_MINIMIZE_LATENCY`](/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_MINIMIZE_LATENCY()). For more
information, see the [`setCaptureMode()`](/reference/androidx/camera/core/ImageCapture.Builder#setCaptureMode(int)) reference documentation.

**Note:** There is also an experimental [Zero-Shutter Lag mode](/media/camera/camerax/zsl) available
through [`CAPTURE_MODE_ZERO_SHOT_LAG`](/reference/androidx/camera/core/ImageCapture#CAPTURE_MODE_ZERO_SHUTTER_LAG()).

## Set flash mode

The default flash mode is [`FLASH_MODE_OFF`](/reference/androidx/camera/core/ImageCapture#FLASH_MODE_OFF()). To set the flash mode, use
[`ImageCapture.Builder.setFlashMode()`](/reference/androidx/camera/core/ImageCapture.Builder#setFlashMode(int)):

* [`FLASH_MODE_ON`](/reference/androidx/camera/core/ImageCapture#FLASH_MODE_ON()): Flash is always on.
* [`FLASH_MODE_AUTO`](/reference/androidx/camera/core/ImageCapture#FLASH_MODE_AUTO()): Flash is automatically on for low-light shots.

## File types

This workflow demonstrated in this document fully supports the [`JPEG`](/reference/android/graphics/ImageFormat#JPEG)
format. For sample code that shows how to convert a [`Media.Image`](/reference/android/media/Image) object
from `YUV_420_888` format to an RGB [`Bitmap`](/reference/android/graphics/Bitmap) object, see
[`YuvToRgbConverter.kt`](https://github.com/android/camera-samples/blob/3730442b49189f76a1083a98f3acf3f5f09222a3/CameraUtils/lib/src/main/java/com/example/android/camera/utils/YuvToRgbConverter.kt).