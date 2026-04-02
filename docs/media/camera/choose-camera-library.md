---
title: Choose a camera library  |  Android media  |  Android Developers
url: https://developer.android.com/media/camera/choose-camera-library
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Choose a camera library Stay organized with collections Save and categorize content based on your preferences.



**Note:** If you want to perform basic camera actions like capturing a photo or video using the device's default camera application, see [Camera intents](/training/camera/camera-intents).

If you want to add camera functionality to an Android app, you have three main options:

* [CameraX](/media/camera/camerax)
* [Camera2](/media/camera/camera2)
* [Camera](/media/camera/camera-deprecated) (deprecated)

For most developers, [CameraX](/training/camerax) is recommended. CameraX is a Jetpack library that supports the vast majority of Android devices (Android 5.0 and higher) and provides a consistent, high-level API designed around common use cases. CameraX resolves device compatibility issues for you so that you don't have to add device-specific code to your app.

CameraX is built on top of the [Camera2](/training/camera2) package. If you need low-level camera control to support complex use cases, Camera2 is a good option, but the API is more complex than CameraX. It requires you to manage device-specific configurations. Like CameraX, Camera2 works on Android 5.0 (API level 21) and higher.

The original Android [Camera](/training/camera-deprecated) class is deprecated. New apps should use CameraX (recommended) or Camera2, and existing apps should migrate to take advantage of new features and to avoid losing compatibility with future devices.