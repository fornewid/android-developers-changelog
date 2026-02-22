---
title: https://developer.android.com/social-and-messaging/guides/media-creation
url: https://developer.android.com/social-and-messaging/guides/media-creation
source: md.txt
---

# About media creation, capture, and sharing

Capturing videos, editing photos, and processing media content are fundamental features of social and messaging apps, and Android has created APIs that support the latest device hardware features, along with libraries that simplify integration into your app. This page connects you to resources to both help you get started and level up your app.

## Know key media creation concepts

Android has APIs and libraries that help your app best adapt to device capabilities while handling the diversity of the Android ecosystem.

### Capture media within your app

You can perform basic camera capture using the device's built-in camera application[using an Intent](https://developer.android.com/media/camera/camera-intents). For social and communications apps, having built-in support for high-quality media capture can provide a competitive advantage. Learn how:

- [CameraX](https://developer.android.com/media/camera/camerax)--- The recommended option for most developers, a library providing easy-to-use support for most common camera use cases with consistent, compatible behavior.
- [Camera2](https://developer.android.com/media/camera/camera2)--- The low-level Android camera API that the CameraX library wraps. Use this class when you need low-level control.
- [Camera extensions](https://developer.android.com/media/camera/camera-extensions)--- Lets your app access advanced camera capabilities such as night, bokeh, face retouch, and HDR.
- [Camera viewfinder](https://developer.android.com/reference/androidx/camera/viewfinder/CameraViewfinder)--- Simplifies Camera2 integration by providing a base viewfinder widget to display the camera feed.
- [Camera](https://developer.android.com/media/camera/camera-deprecated)--- The deprecated original class used to control the camera on Android.

### Browse, share, and edit media

Make sure that your users have easy access to edit and share the media they've created and captured in the best possible quality:

- [Media3 Transformer APIs](https://developer.android.com/media/media3/transformer)--- This API lets users edit media with ease. Edit capabilities include converting between formats (transcoding), applying changes like trimming a clip from a longer video, cropping a portion of the video frame, applying custom effects, and other editing operations.
- [Photo Picker](https://developer.android.com/training/data-storage/shared/photopicker)--- This component provides a safe, built-in way for users to grant your app access to only selected images and videos, instead of their entire media library.
- [Android Sharesheet](https://developer.android.com/training/sharing/send#using-android-system-sharesheet)--- This component lets users send content from one app to another.
- [Ultra HDR Image Format](https://developer.android.com/media/platform/hdr-image-format)--- The JPEG-based file format used to encode images with a logarithmic-range gain map that can render in high dynamic range on compatible displays.

## Level up your app

You'll want your app to support features that meet and surpass user expectations. One way to do that is to support the advanced media features provided by premium devices. Here are some specific ways to help your app stand out:

- Capture[UltraHDR images](https://github.com/android/platform-samples/blob/main/samples/camera/camera2/src/main/java/com/example/platform/camera/imagecapture/Camera2UltraHDRCapture.kt)and[HDR video](https://developer.android.com/media/camera/camera2/hdr-video-capture)
- Utilize[camera extensions](https://developer.android.com/media/camera/camera-extensions)such as night mode or bokeh (for portrait shots)
- Support[zero shutter lag](https://developer.android.com/media/camera/camerax/take-photo#zero-shutter-lag)
- Edit video with[custom effects](https://developer.android.com/media/media3/transformer/transformations#custom-video)
- Capture from[front and back cameras concurrently](https://developer.android.com/media/camera/camera2/multiple-camera-streams-simultaneously)(your user can narrate what they're recording in the viewfinder)

See the[full guide](https://developer.android.com/social-and-messaging/guides/media-creation/basic-better-best)for features to consider to take your media capture and editing experience to the next level and impress your users.