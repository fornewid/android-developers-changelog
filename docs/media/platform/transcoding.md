---
title: https://developer.android.com/media/platform/transcoding
url: https://developer.android.com/media/platform/transcoding
source: md.txt
---

On Android 12 (API level 31) and higher, the system can automatically convert
videos recorded in formats such as HEVC (H.265) to AVC (H.264) when the videos
are opened by an app that does not support HEVC. This feature allows video
capture apps to utilize more modern, storage-efficient encoding for videos
recorded on the device without sacrificing compatibility with other apps.

The following formats can be automatically transcoded for content that's
created on-device:

| Media format | XML Attribute | MediaFormat mime type |
|---|---|---|
| HEVC (H.265) | HEVC | MediaFormat.MIMETYPE_VIDEO_HEVC |
| HDR10 | HDR10 | MediaFeature.HdrType.HDR10 |
| HDR10+ | HDR10Plus | MediaFeature.HdrType.HDR10_PLUS |

Android assumes that apps can support playback of all media formats, so
compatible media transcoding is off by default.

## When to use transcoding

Transcoding is a computationally expensive operation and adds a significant
delay when opening a video file. For example, a one minute HEVC video file takes
roughly 20 seconds to transcode into AVC on a Pixel 3 phone. For this reason,
you should transcode a video file only when you are sending it off the
device. For example, when sharing a video file with other users of the same
app, or a cloud server which does not support modern video
formats.

Do not transcode when opening video files for on-device playback or for creating thumbnail images.

## Configuring transcoding

Apps can control their transcoding behavior by declaring their media
capabilities. There are two ways to declare these capabilities: in code,
or in a resource.

### Declare capabilities in code

You can declare media capabilities in code by constructing an instance of an
`ApplicationMediaCapabilities` object using a builder:

### Kotlin

```kotlin
val mediaCapabilities = ApplicationMediaCapabilities.Builder()
    .addSupportedVideoMimeType(MediaFormat.MIMETYPE_VIDEO_HEVC)
    .addUnsupportedHdrType(MediaFeature.HdrType.HDR10)
    .addUnsupportedHdrType(MediaFeature.HdrType.HDR10_PLUS)
    .build()
```

### Java

```java
ApplicationMediaCapabilities mediaCapabilities = new ApplicationMediaCapabilities.Builder()
        .addSupportedVideoMimeType(MediaFormat.MIMETYPE_VIDEO_HEVC)
        .addUnsupportedHdrType(MediaFeature.HdrType.HDR10)
        .addUnsupportedHdrType(MediaFeature.HdrType.HDR10_PLUS)
        .build();
```

Use this object when accessing media content via methods such as
`ContentResolver#openTypedAssetFileDescriptor()`:

### Kotlin

```kotlin
val providerOptions = Bundle().apply {
    putParcelable(MediaStore.EXTRA_MEDIA_CAPABILITIES, mediaCapabilities)
}
contentResolver.openTypedAssetFileDescriptor(mediaUri, mediaMimeType, providerOptions)
    .use { fileDescriptor ->
        // Content will be transcoded based on values defined in the
        // ApplicationMediaCapabilities provided.
    }
```

### Java

```java
Bundle providerOptions = new Bundle();
providerOptions.putParcelable(MediaStore.EXTRA_MEDIA_CAPABILITIES, mediaCapabilities);
try (AssetFileDescriptor fileDescriptor =  contentResolver.openTypedAssetFileDescriptor(mediaUri, mediaMimeType, providerOptions)) {
    // Content will be transcoded based on values defined in the
    // ApplicationMediaCapabilities provided.
}
```

This method allows granular control for particular code paths, such
as invoking transcoding only when transferring a video file off-device. It takes precedence over the method described below.

### Declare capabilities in a resource

Declaring capabilities in a resource allows blanket control over transcoding.
This method should only be used in very specific cases. For example, if your app
only receives video files from other apps (rather than opening them directly)
and uploads them to a server which does not support modern video codecs (see
example scenario 1 below).

Using this method when not absolutely necessary might invoke transcoding in unintended scenarios, such as when thumbnailing videos, resulting in a degraded user experience.

To use this method, create a `media_capabilities.xml` resource file:

    <?xml version="1.0" encoding="utf-8"?>
    <media-capabilities xmlns:android="http://schemas.android.com/apk/res/android">
        <format android:name="HEVC" supported="true"/>
        <format android:name="HDR10" supported="false"/>
        <format android:name="HDR10Plus" supported="false"/>
    </media-capabilities>

In this example, HDR videos recorded on the device are seamlessly transcoded to
AVC SDR (standard dynamic range) video, while HEVC videos are not.

Use a `property` tag within the `application` tag to add a reference to the media
capabilities file. Add these properties to your `AndroidManifest.xml` file:

    <property
        android:name="android.media.PROPERTY_MEDIA_CAPABILITIES"
        android:resource="@xml/media_capabilities" />

## Using another app's media capabilities to open a video file

If your app shares a video file with another app, the video file might need to
be transcoded before the receiving app can open it.

You can handle this case by opening a video file using [`openTypedAssetFileDescriptor`](https://developer.android.com/reference/android/content/ContentResolver#openTypedAssetFileDescriptor(android.net.Uri,%20java.lang.String,%20android.os.Bundle))
and specifying the UID of the receiving app, which can be obtained using [`Binder.getCallingUid`](https://developer.android.com/reference/android/os/Binder#getCallingUid()).
The platform then uses the receiving app's media capabilities to determine
whether the video file should be transcoded.

### Kotlin

```kotlin
val providerOptions = Bundle().apply {
    putParcelable(MediaStore.EXTRA_MEDIA_CAPABILITIES_UID, Binder.getCallingUid())
}
contentResolver.openTypedAssetFileDescriptor(mediaUri, mediaMimeType, providerOptions)
    .use { fileDescriptor ->
        // Content will be transcoded based on the media capabilities of the
        // calling app.
    }
```

### Java

```java
Bundle providerOptions = new Bundle();
providerOptions.putParcelable(MediaStore.EXTRA_MEDIA_CAPABILITIES_UID, Binder.getCallingUid());
try (AssetFileDescriptor fileDescriptor =  contentResolver.openTypedAssetFileDescriptor(mediaUri, mediaMimeType, providerOptions)) {
    // Content will be transcoded based on the media capabilities of the
    // calling app.
}
```

## Example scenarios

The following diagrams demonstrate the two common use cases. In both cases the original video is stored in HEVC format and the video sharing app does not
support HEVC.

**Example 1.** Transcoding is initiated by video capture app.
![Example 1](https://developer.android.com/static/images/guide/topics/media-apps/video-app/media-transcode-ex1.svg)
The video sharing app declares that it does not support HEVC in its media
capabilities resource file. It then requests a video from the video capture app. The video capture
app handles the request and opens the file using [`openTypedAssetFileDescriptor`](https://developer.android.com/reference/android/content/ContentResolver#openTypedAssetFileDescriptor(android.net.Uri,%20java.lang.String,%20android.os.Bundle)), specifying the sharing app's UID. This initiates the transcoding process.
When the transcoded video is received it is supplied to the sharing app, which uploads it to a server in the cloud.

**Example 2.** Transcoding is initiated by video sharing app.
![Example 2](https://developer.android.com/static/images/guide/topics/media-apps/video-app/media-transcode-ex2.svg)
The video capture app shares a video with the video sharing app using a
`MediaStore` URI. The video sharing app opens the video file using [`openTypedAssetFileDescriptor`](https://developer.android.com/reference/android/content/ContentResolver#openTypedAssetFileDescriptor(android.net.Uri,%20java.lang.String,%20android.os.Bundle)), specifying that it does not support HEVC in its media capabilities. This
initiates the transcoding process, and once complete, the file is uploaded to
a server in the cloud.

## Undeclared formats

Compatible media transcoding is enabled for all formats that are declared
unsupported, and is disabled for all formats that are declared supported. For
other formats that are not declared, the platform decides whether to transcode
or not. In Android 12 transcoding is disabled
for all undeclared formats. This behavior might change for new formats in the
future.

## Developer options

You can use the following developer options to override Android's default
transcoding behavior:

- **Override transcoding defaults** This setting determines whether or not
  the platform controls automatic transcoding. When override
  is enabled, the platform defaults are ignored and the **enable
  transcoding** setting controls automatic transcoding. This option is disabled by
  default.

- **Enable transcoding** This setting specifies whether or not undeclared
  formats are automatically transcoded. It is enabled by default, but it only
  has an effect if **override transcoding defaults** is also enabled.

- **Assume apps support modern formats** This setting controls what happens when
  the app tries to play an undeclared format. This happens when the manifest does
  not declare whether or not the app supports a particular format, or Google
  hasn't added the app to the server-side force-transcode list. When the setting
  is enabled, the app does not transcode, when it's disabled, the app does
  transcode. This option is enabled by default.

- **Show transcoding notifications** When enabled, the app displays a
  transcoding progress notification when transcoding is triggered by reading an
  unsupported media file. This option is enabled by default.

- **Disable transcoding cache** If enabled, apps that require transcoding do not
  use the transcoding cache. This can be helpful during development to easily
  trigger transcoding on an unsupported media file, but can cause poor device
  performance. This option is disabled by default.