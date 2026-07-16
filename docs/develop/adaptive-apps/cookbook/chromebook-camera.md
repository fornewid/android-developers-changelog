---
title: https://developer.android.com/develop/adaptive-apps/cookbook/chromebook-camera
url: https://developer.android.com/develop/adaptive-apps/cookbook/chromebook-camera
source: md.txt
---

![Three star rating icon](https://developer.android.com/static/develop/adaptive-apps/cookbook/images/shared/three-star-rating.png)

Get noticed on Google Play by Chromebook users.

If your camera app can function with only basic camera features, don't let app
stores prevent Chromebook users from installing the app just because you
inadvertently specified advanced camera features found on high-end phones.

Chromebooks have a built-in front (user-facing) camera that works well for video
conferencing, snapshots, and other applications. But not all Chromebooks have a
back (world-facing) camera, and most user-facing cameras on Chromebooks don't
support autofocus or flash.

## Best practices

Versatile camera apps support all devices regardless of camera
configuration---devices with front cameras, back cameras, external cameras
connected by USB.

To ensure apps stores make your app available to the greatest number of devices,
always declare all camera features used by your app and explicitly indicate
whether or not the features are required.

## Ingredients

- [`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA) permission: Gives your app access to a device's cameras
- [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element) manifest element: Informs app stores of the features used by your app
- [`required`](https://developer.android.com/guide/topics/manifest/uses-feature-element#required) attribute: Indicates to app stores whether your app can function without a specified feature

## Steps

Declare the `CAMERA` permission. Declare camera features that provide basic
camera support. Specify whether or not each feature is required.

### 1. Declare the `CAMERA` permission

Add the following permission to the app manifest:

    <uses-permission android:name="android.permission.CAMERA" />

### 2. Declare basic camera features

Add the following features to the app manifest:

    <uses-feature android:name="android.hardware.camera.any" android:required="false" />
    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
    <uses-feature android:name="android.hardware.camera.flash" android:required="false" />

> [!NOTE]
> **Note:** The `android.hardware.camera` feature specifically refers to a back (world-facing) camera.

### 3. Specify whether each feature is required

Set `android:required="false"` for the `android.hardware.camera.any` feature to
enable access to your app by devices that have any kind of built-in or external
camera---or no camera at all.

> [!NOTE]
> **Note:** If your app must have a camera to function, specify `"true"` for the `required` attribute of `android.hardware.camera.any`. That way, devices that don't have a camera won't have access to your app.

For the other features, set `android:required="false"` to ensure devices such as
Chromebooks that don't have back cameras, autofocus, or flash can access your
app on app stores.

## Results

Chromebook users can download and install your app from Google Play and other
app stores. And devices with full‑featured camera support, like phones,
won't be restricted in their camera functionality.

By explicitly setting the camera features supported by your app and specifying
the features your app requires, you've made your app available to as many
devices as possible.

## Additional resources

For more information, see [Camera hardware features](https://developer.android.com/guide/topics/manifest/uses-feature-element#camera-hw-features)
in the `<uses-feature>` documentation.