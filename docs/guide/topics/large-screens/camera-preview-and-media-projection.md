---
title: Camera preview and media projection  |  Large screens  |  Android Developers
url: https://developer.android.com/guide/topics/large-screens/camera-preview-and-media-projection
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Large screens](https://developer.android.com/guide/topics/large-screens)
* [Guides](https://developer.android.com/guide/topics/large-screens/tier-3-overview)

# Camera preview and media projection Stay organized with collections Save and categorize content based on your preferences.



![Tier 3 adaptive ready icon](/static/images/docs/quality-guidelines/tier-3/tier_3_icon.png)

TIER 3 — Adaptive ready

**Objective:** Make your app [adaptive ready](/docs/quality-guidelines/adaptive-app-quality/tier-3) by meeting the
[Camera\_Preview](/docs/quality-guidelines/adaptive-app-quality/tier-3#Camera_Preview) and [Media\_Projection](/docs/quality-guidelines/adaptive-app-quality/tier-3#Media_Projection) requirements of the [Adaptive app quality guidelines](/docs/quality-guidelines/adaptive-app-quality).

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

* [Camera preview](/training/camera2/camera-preview)
* [CameraX overview](/training/camerax)

## Media projection

Media projection captures the contents of a device screen or app window and
displays the captured content on another device, such as a TV.

Media projection apps must register a service permission, manage user consent,
orient and scale the captured content to match the orientation and aspect ratio
of the target device, and enable customization of the projection.

For implementation details, see [Media projection](/media/grow/media-projection).