---
title: https://developer.android.com/social-and-messaging/guides/basic-better-best
url: https://developer.android.com/social-and-messaging/guides/basic-better-best
source: md.txt
---

# Take your social or messaging app to the next level — basic, better, and best

This guide links to three documents that chart the optimal progression of a social or messaging app from a likely starting place to best-in-class. These documents cover use cases around messaging, media creation, and media playback. They're designed to help you think about scaling your app over time, and what features to implement when. While every social or messaging app is different, consider these recommendations to achieve a best-in-class app.

## Messaging and communication

Communication is a critical part of social and messaging apps, and Android continues to evolve APIs and services to make the user experience more integrated and consistent.

### Level up your app

Ways to help your app stand out include:

- Support for receiving[rich content](https://developer.android.com/develop/ui/views/receive-rich-content), including stickers and images through Android's Image Keyboard, drag and drop, and clipboard.
- Support for browsing and selecting user photos and videos, either local or in the cloud, using Android's built-in[photo picker](https://developer.android.com/training/data-storage/shared/photopicker).

See the[full guide](https://developer.android.com/social-and-messaging/guides/communication/basic-better-best)for features to take your messaging and communication experience to the next level.

## Media creation, capture, and sharing

Capturing videos, editing photos, and processing media content are fundamental features of social and messaging apps, and Android has created APIs that support the latest device hardware features, along with libraries that simplify integration into your app.

### Level up your app

Ways to help your app stand out include:

- Capture[UltraHDR images](https://github.com/android/platform-samples/blob/main/samples/camera/camera2/src/main/java/com/example/platform/camera/imagecapture/Camera2UltraHDRCapture.kt)and[HDR video](https://developer.android.com/media/camera/camera2/hdr-video-capture).
- Utilize[camera extensions](https://developer.android.com/media/camera/camera-extensions)such as night mode or bokeh (for portrait shots).
- Support[zero shutter lag](https://developer.android.com/media/camera/camerax/take-photo#zero-shutter-lag).
- Edit video with[custom effects](https://developer.android.com/media/media3/transformer/transformations#custom-video).

See the[complete guide](https://developer.android.com/social-and-messaging/guides/media-creation/basic-better-best)for features to consider to take your media capture, editing, and sharing experience to the next level.

## Media display and playback

Whether your app integrates images and videos or delivers immersive audio experiences, media enriches user interactions and elevates app engagement. Android continues to evolve APIs to minimize the complexity of integrating media while making the user experience more integrated and consistent.

### Level up your app

Ways to help your app stand out include:

- Support[UltraHDR](https://developer.android.com/media/grow/ultra-hdr-display)images and[HDR](https://developer.android.com/media/grow/hdr-playback)video.
- Enable[picture-in-picture](https://developer.android.com/develop/ui/views/picture-in-picture)for video and audio playback.
- Implement a[MediaSession](https://developer.android.com/guide/topics/media/media3/getting-started/mediasession)--- made easy with[Media3s](https://developer.android.com/guide/topics/media/media3)[ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer)--- to enable playback integration across different apps, system components, and devices.

See the[full guide](https://developer.android.com/social-and-messaging/guides/media-display/basic-better-best)for features to consider to take your media display and playback experience to the next level.