---
title: https://developer.android.com/social-and-messaging/guides/media-creation/basic-better-best
url: https://developer.android.com/social-and-messaging/guides/media-creation/basic-better-best
source: md.txt
---

# Take your media creation to the next level — basic, better, and best

This guide charts the optimal progression of a media creation-focused app from a likely starting place to best-in-class. It's designed to help you think about scaling your app over time, and what features to implement when. While every media creation app is different, consider these recommendations to achieve a best-in-class app.

## Basic media creation

A basic media creation app provides users with a foundational experience, which may include doing the following:

- Use[photo picker](https://developer.android.com/training/data-storage/shared/photopicker)to access existing photos and videos.
- Support[in-app image](https://developer.android.com/training/camerax/take-photo)and[in app video](https://developer.android.com/training/camerax/video-capture)capture using CameraX.
- Handle[camera orientation](https://developer.android.com/training/camerax/orientation-rotation).
- Support[automatic resolution](https://developer.android.com/media/camera/camerax/configuration#automatic-resolution).
- [Switch](https://developer.android.com/reference/androidx/camera/core/CameraSelector)between[front](https://developer.android.com/reference/androidx/camera/core/CameraSelector#DEFAULT_FRONT_CAMERA())and[back](https://developer.android.com/reference/androidx/camera/core/CameraSelector#DEFAULT_BACK_CAMERA())camera.
- Support[zoom](https://developer.android.com/reference/androidx/camera/core/ZoomState)and[tap-to-focus](https://developer.android.com/reference/kotlin/androidx/camera/view/CameraController#setTapToFocusEnabled(boolean)).
- Support hardware[flash](https://developer.android.com/training/camerax/take-photo#set-flash-mode).
- Handle[multi-window camera access](https://developer.android.com/develop/ui/compose/layouts/adaptive/support-multi-window-mode#exclusive_resource_access).
- Use the[Android Sharesheet](https://developer.android.com/training/sharing/send#why-to-use-system-sharesheet)to share with other apps and targets.

## Better media creation

A better media creation app gives users access to premium camera hardware, camera software, and media-editing features that:

**Capture**

- Use[camera extensions](https://developer.android.com/training/camerax/extensions-api):[night mode](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT),[HDR](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_HDR), or[bokeh](https://developer.android.com/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_BOKEH).
- Have[zero shutter lag](https://developer.android.com/training/camerax/take-photo#zero-shutter-lag).
- Support[screen-based flash](https://developer.android.com/reference/kotlin/androidx/camera/view/ScreenFlashView)for selfie cameras.
- Use manual[flash](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#FLASH_SINGLE_STRENGTH_DEFAULT_LEVEL)or[torch](https://developer.android.com/reference/android/hardware/camera2/CameraCharacteristics#FLASH_TORCH_STRENGTH_DEFAULT_LEVEL)controls.
- Use[target resolutions](https://developer.android.com/media/camera/camerax/configuration#specify-resolution).
- Have[exposure compensation](https://developer.android.com/media/camera/camerax/configuration#exposure-compensation).
- Add an[app widget](https://developer.android.com/develop/ui/views/appwidgets/overview)so users can get start a capture flow from their home screen.

**Edit**

- With video[trimming](https://developer.android.com/media/media3/transformer/transformations#trim),[cropping](https://developer.android.com/reference/androidx/media3/effect/Crop), and other built-in[Media3 transformer](https://developer.android.com/guide/topics/media/transformer)[effects](https://developer.android.com/reference/androidx/media3/common/Effect).
- [UltraHDR images](https://developer.android.com/media/grow/ultra-hdr-edit#basic-edits), rotation, cropping, and scaling.
- Use[image filters](https://developer.android.com/develop/ui/compose/graphics/images/customize#color-filter)and transformations.
- Audio with[audio effects](https://developer.android.com/reference/androidx/media3/common/audio/AudioProcessor).

## Best media creation

A best-in-class media creation app gives users access to advanced features that really make the app stand out, such as:

**Capture**

- Use concurrent cameras:[front-and-back simultaneous capture](https://developer.android.com/media/camera/camera2/multiple-camera-streams-simultaneously).
- Stream live with adaptive live streaming. Consider using[performance class](https://developer.android.com/topic/performance/performance-class)to help determine if the device can support concurrent camera capture.

**Edit**

- Support[custom effects](https://developer.android.com/media/media3/transformer/transformations#custom-video)using[Media3 transformer](https://developer.android.com/media/media3/transformer/getting-started).
- [UltraHDR images](https://developer.android.com/media/grow/ultra-hdr-edit#advanced-edits), transforming the[gain-map](https://developer.android.com/guide/topics/media/platform/hdr-image-format#gain_map-generation)appropriately for image filters and other operations.
- Audio with[custom audio effects](https://developer.android.com/reference/androidx/media3/common/audio/BaseAudioProcessor).