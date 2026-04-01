---
title: https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection
url: https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection
source: md.txt
---

![Tier 3 adaptive ready icon](https://developer.android.com/static/images/guide/topics/large-screens/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 --- Adaptive ready
| **Objective:** Make your app [adaptive ready](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#adaptive_ready) by meeting the [Media:Camera_Preview](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Camera_Preview) and [Media:Projection](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality#Media:Projection) requirements of the [Adaptive
| app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality) guidelines.

## Camera preview

Camera is one of the most important Android apps. The camera viewfinder is a
window into the app, a rendering of the camera sensor output (the camera
preview).

Camera sensors have a fixed position and fixed aspect ratio and typically output
their image data in landscape orientation. The viewfinder, however, must conform
to portrait and landscape device orientations, folded and unfolded states of
foldable devices, and different window sizes in multi‑window mode.

In multi‑window mode and on foldables, the viewfinder can be portrait on
landscape devices or landscape on portrait devices. Camera apps often must
rotate the image preview to match the orientation of the viewfinder. And even
when the viewfinder and camera sensor are in the same orientation, their aspect
ratios can differ.

Your app has the challenge of orienting and scaling the camera sensor image to
match the orientation and aspect ratio of the app's UI as the UI changes
orientation and size.

To learn how to manage camera preview, see the following developer guides:

- [Camera preview](https://developer.android.com/training/camera2/camera-preview)
- [CameraX overview](https://developer.android.com/training/camerax)

## Media projection

Media projection captures the contents of a device screen or app window and
displays the captured content on another device, such as a TV.

Media projection apps must register a service permission, manage user consent,
orient and scale the captured content to match the orientation and aspect ratio
of the target device, and enable customization of the projection.

For implementation details, see [Media projection](https://developer.android.com/media/grow/media-projection).