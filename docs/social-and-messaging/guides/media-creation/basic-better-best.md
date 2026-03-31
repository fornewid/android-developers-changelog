---
title: Take your media creation to the next level — basic, better, and best  |  Android social  |  Android Developers
url: https://developer.android.com/social-and-messaging/guides/media-creation/basic-better-best
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Social & Messaging Dev Center](https://developer.android.com/social-and-messaging)
* [Guides](https://developer.android.com/social-and-messaging/guides)

# Take your media creation to the next level — basic, better, and best Stay organized with collections Save and categorize content based on your preferences.




This guide charts the optimal progression of a media creation-focused app from a
likely starting place to best-in-class. It's designed to help you think about
scaling your app over time, and what features to implement when. While every
media creation app is different, consider these recommendations to achieve a
best-in-class app.

## Basic media creation

A basic media creation app provides users with a foundational experience, which
may include doing the following:

* Use [photo picker](/training/data-storage/shared/photopicker) to access existing photos and videos.
* Support [in-app image](/training/camerax/take-photo) and [in app video](/training/camerax/video-capture) capture using CameraX.
* Handle [camera orientation](/training/camerax/orientation-rotation).
* Support [automatic resolution](/media/camera/camerax/configuration#automatic-resolution).
* [Switch](/reference/androidx/camera/core/CameraSelector) between [front](/reference/androidx/camera/core/CameraSelector#DEFAULT_FRONT_CAMERA()) and [back](/reference/androidx/camera/core/CameraSelector#DEFAULT_BACK_CAMERA()) camera.
* Support [zoom](/reference/androidx/camera/core/ZoomState) and [tap-to-focus](/reference/kotlin/androidx/camera/view/CameraController#setTapToFocusEnabled(boolean)).
* Support hardware [flash](/training/camerax/take-photo#set-flash-mode).
* Handle [multi-window camera access](/develop/ui/compose/layouts/adaptive/support-multi-window-mode#exclusive_resource_access).
* Use the [Android Sharesheet](/training/sharing/send#why-to-use-system-sharesheet) to share with other apps and targets.

## Better media creation

A better media creation app gives users access to premium camera hardware,
camera software, and media-editing features that:

**Capture**

* Use [camera extensions](/training/camerax/extensions-api): [night mode](/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_NIGHT), [HDR](/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_HDR), or [bokeh](/reference/android/hardware/camera2/CameraExtensionCharacteristics#EXTENSION_BOKEH).
* Have [zero shutter lag](/training/camerax/take-photo#zero-shutter-lag).
* Support [screen-based flash](/reference/kotlin/androidx/camera/view/ScreenFlashView) for selfie cameras.
* Use manual [flash](/reference/android/hardware/camera2/CameraCharacteristics#FLASH_SINGLE_STRENGTH_DEFAULT_LEVEL) or [torch](/reference/android/hardware/camera2/CameraCharacteristics#FLASH_TORCH_STRENGTH_DEFAULT_LEVEL) controls.
* Use [target resolutions](/media/camera/camerax/configuration#specify-resolution).
* Have [exposure compensation](/media/camera/camerax/configuration#exposure-compensation).
* Add an [app widget](/develop/ui/views/appwidgets/overview) so users can get start a capture flow from their home
  screen.

**Edit**

* With video [trimming](/media/media3/transformer/transformations#trim), [cropping](/reference/androidx/media3/effect/Crop), and other built-in [Media3
  transformer](/guide/topics/media/transformer) [effects](/reference/androidx/media3/common/Effect).
* [UltraHDR images](/media/grow/ultra-hdr-edit#basic-edits), rotation, cropping, and scaling.
* Use [image filters](/develop/ui/compose/graphics/images/customize#color-filter) and transformations.
* Audio with [audio effects](/reference/androidx/media3/common/audio/AudioProcessor).

## Best media creation

A best-in-class media creation app gives users access to advanced features that
really make the app stand out, such as:

**Capture**

* Use concurrent cameras: [front-and-back simultaneous capture](/media/camera/camera2/multiple-camera-streams-simultaneously).
* Stream live with adaptive live streaming. Consider using [performance
  class](/topic/performance/performance-class) to help determine if the device can support concurrent camera
  capture.

**Edit**

* Support [custom effects](/media/media3/transformer/transformations#custom-video) using [Media3 transformer](/media/media3/transformer/getting-started).
* [UltraHDR images](/media/grow/ultra-hdr-edit#advanced-edits), transforming the [gain-map](/guide/topics/media/platform/hdr-image-format#gain_map-generation) appropriately for image
  filters and other operations.
* Audio with [custom audio effects](/reference/androidx/media3/common/audio/BaseAudioProcessor).