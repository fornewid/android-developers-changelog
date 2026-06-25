---
title: https://developer.android.com/distribute/aep/aep-req-camera-x
url: https://developer.android.com/distribute/aep/aep-req-camera-x
source: md.txt
---

Integrate the [Jetpack CameraX library](https://developer.android.com/jetpack/androidx/releases/camera) to ensure high-quality, consistent
camera capture across the diverse Android-powered device ecosystem. Adopting
this library provides a stable, feature-rich experience across various form
factors, such as phones, tablets, foldables, and XR devices. By migrating to
modern camera APIs, apps can achieve better quality and maintain a more reliable
user experience regardless of the device hardware.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- The app must not use the legacy *android.hardware.Camera API* (Camera1). You
  should migrate to use CameraX (or Camera2).

  **Note** : Using the [Camera2 framework](https://developer.android.com/media/camera/camera2) is a valid alternative for apps
  that require a custom camera stack.

## Guideline applicability

This guideline applies to:

- Apps that support media capture (images or video).
- Phone, tablet, foldable, and XR form factors.

## Exemptions

Apps can use an equivalent alternative framework that provides similar quality,
user capabilities, stability and compatibility across the ecosystem.
[Contact support](https://developer.android.com/distribute/aep/aep-get-support) if you have a suitable framework for consideration.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the **CameraX** feature. These resources are for your reference only and don't
contain additional program requirements.

- [Jetpack CameraX overview](https://developer.android.com/media/camera/camerax)
- [Getting started with CameraX](https://developer.android.com/codelabs/camerax-getting-started#0)
- [Migrate Camera1 to CameraX](https://developer.android.com/media/camera/camerax/camera1-to-camerax)