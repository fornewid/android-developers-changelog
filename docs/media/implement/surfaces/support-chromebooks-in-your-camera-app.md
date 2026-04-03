---
title: https://developer.android.com/media/implement/surfaces/support-chromebooks-in-your-camera-app
url: https://developer.android.com/media/implement/surfaces/support-chromebooks-in-your-camera-app
source: md.txt
---

# Support Chromebooks in your camera app

Get noticed on Google Play by Chromebook users.

Chromebooks have a built-in front (user-facing) camera. But not all Chromebooks have a back (world-facing) camera. And most user-facing cameras on Chromebooks don't support autofocus or flash.

Versatile camera apps support all devices regardless of camera configuration---devices with front cameras, back cameras, and external cameras connected by USB.

Don't let app stores prevent Chromebook users from installing your app just because you specified advanced camera features found on high-end phones.

## Configure the app manifest

To ensure apps stores make your app available to the greatest number of devices, declare all camera features used by your app and explicitly indicate whether or not the features are required:

- Declare the`CAMERA`permission
- Declare camera features
- Specify whether or not each feature is required

### 1. Declare the`CAMERA`permission

Add the following permission to the app manifest:  

    <uses-permission android:name="android.permission.CAMERA" />

### 2. Declare camera features

Add the following features to the app manifest:  

    <uses-feature android:name="android.hardware.camera.any" android:required="false" />
    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />
    <uses-feature android:name="android.hardware.camera.flash" android:required="false" />

| **Caution:** The`android.hardware.camera`feature applies only to back (world-facing) cameras.

### 3. Specify whether each feature is required

Set`android:required="false"`for the`android.hardware.camera.any`feature to enable access to your app by devices that have any kind of built-in or external camera---or no camera at all.
| **Note:** If your app requires a camera, specify`required="true"`for`android.hardware.camera.any`. That way, devices that don't have a camera won't have access to your app.

For the other features, set`android:required="false"`to ensure devices such as Chromebooks that don't have back cameras, autofocus, or flash can access your app on app stores.

## Key points

- [`CAMERA`](https://developer.android.com/reference/android/Manifest.permission#CAMERA)permission: Gives your app access to a device's cameras
- [`<uses-feature>`](https://developer.android.com/guide/topics/manifest/uses-feature-element)manifest element: Informs app stores of the features used by your app
- [`required`](https://developer.android.com/guide/topics/manifest/uses-feature-element#required)attribute: Indicates to app stores whether your app can function without a specified feature

## Results

You've made your app available to as many devices as possible by explicitly setting the camera features supported by your app and specifying the features your app requires. Chromebook users can download and install your app from Google Play and other app stores. Users of devices with full‑featured camera support, like phones, can also download the app.