---
title: https://developer.android.com/distribute/aep/aep-req-night-mode
url: https://developer.android.com/distribute/aep/aep-req-night-mode
source: md.txt
---

Adopt Night Mode to enable hardware-accelerated low light photo capture with the
in-app camera, ensuring your app leverages the same advanced image processing as
the native camera app for high-quality results in low-light environments.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- Support the Night Mode Camera Extension by using either the Jetpack CameraX Extensions API or the Android Camera2 Extensions API.
- Implement the platform-recommended Night Mode Indicator API (available in Android 16) to inform users when a low-light capture is recommended.

## Guideline applicability

This guideline applies to:

- Apps that support still image capture.
- Phone, tablet, and foldable form factors.

## Exemptions

The following exemptions apply for this guideline:

- Apps that **only** capture video content, as Night Mode is specifically for still image capture.
- Apps can use an equivalent alternative framework that provides similar quality, user capabilities, stability and compatibility across the ecosystem. [Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **Night Mode** feature. These resources are for your reference only and
don't contain additional program requirements.

- [Low light photography and videography solutions](https://developer.android.com/media/camera/lowlight)
- [CameraX Extensions API](https://developer.android.com/media/camera/camerax/extensions-api)
- [Real-time Capture Latency Estimate (CameraX)](https://developer.android.com/reference/kotlin/androidx/camera/core/ImageCapture#getRealtimeCaptureLatencyEstimate())
- [Night Mode Extension (Camera2)](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT)
- [Night Mode Indicator Result (Camera2)](https://developer.android.com/reference/android/hardware/camera2/CaptureResult#EXTENSION_NIGHT_MODE_INDICATOR)