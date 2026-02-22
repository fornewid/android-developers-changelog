---
title: https://developer.android.com/media/media3/exoplayer/media-items
url: https://developer.android.com/media/media3/exoplayer/media-items
source: md.txt
---

The [playlist API](https://developer.android.com/guide/topics/media/exoplayer/playlists) is based on `MediaItem` instances, which can be conveniently built
using `MediaItem.Builder`. Inside the player, a `MediaItem` is converted into
a playable `MediaSource` by a `MediaSource.Factory`. Without
[custom configuration](https://developer.android.com/guide/topics/media/exoplayer/media-sources#customizing-media-source-creation),
this conversion is carried out by a `DefaultMediaSourceFactory`, which is
capable of building complex media sources corresponding to the properties of the
media item. Some of the properties that can be set on media items are outlined
below.

## Simple media items

A media item consisting only of the stream URI can be built with the `fromUri`
convenience method:

### Kotlin

```kotlin
val mediaItem = MediaItem.fromUri(videoUri)
```

### Java

```java
MediaItem mediaItem = MediaItem.fromUri(videoUri);
```

For all other cases, a `MediaItem.Builder` can be used. In the following example, a
media item is built with an ID and some attached metadata:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder().setMediaId(mediaId).setTag(myAppData).setUri(videoUri).build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder().setMediaId(mediaId).setTag(myAppData).setUri(videoUri).build();
```

Attaching metadata can be useful for
[updating your app's UI](https://developer.android.com/guide/topics/media/exoplayer/playlists#detecting-transitions)
when playlist transitions occur.

## Images

Playback of images requires a duration in the media item to specify for how long
the image should be shown during playback. See the
[Images](https://developer.android.com/media/media3/exoplayer/images) guide page for more information on
[Motion Photos](https://developer.android.com/media/media3/exoplayer/images#motion-photos) and
[Image Loading Libraries](https://developer.android.com/media/media3/exoplayer/images#image-loading-libraries)
(for example, Glide).

### Kotlin

```kotlin
val mediaItem = MediaItem.Builder().setUri(imageUri).setImageDurationMs(3000).build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder().setUri(imageUri).setImageDurationMs(3_000).build();
```

## Non-standard file extensions for adaptive media

ExoPlayer provides adaptive media sources for DASH, HLS, and
SmoothStreaming. If the URI of such an adaptive media item ends with a standard
file extension, the corresponding media source is automatically created. If the
URI has a non-standard extension or no extension at all, then the MIME type can
be set explicitly to indicate the type of the media item:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder().setUri(hlsUri).setMimeType(MimeTypes.APPLICATION_M3U8).build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder().setUri(hlsUri).setMimeType(MimeTypes.APPLICATION_M3U8).build();
```

For progressive media streams a MIME type is not required.

## Protected content

For protected content, the media item's DRM properties should be set. The UUID
is required, all the other properties are optional.

An example config for playing an item protected with Widevine DRM where the
license URI is not available directly in the media (e.g. in a DASH playlist) and
multiple sessions are required (e.g. due to key rotation):

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setUri(videoUri)
    .setDrmConfiguration(
      MediaItem.DrmConfiguration.Builder(C.WIDEVINE_UUID)
        .setLicenseUri(licenseUri)
        .setMultiSession(true)
        .setLicenseRequestHeaders(httpRequestHeaders)
        .build()
    )
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setDrmConfiguration(
            new MediaItem.DrmConfiguration.Builder(C.WIDEVINE_UUID)
                .setLicenseUri(licenseUri)
                .setMultiSession(true)
                .setLicenseRequestHeaders(httpRequestHeaders)
                .build())
        .build();
```

Inside the
player, `DefaultMediaSourceFactory` will pass these properties to a
`DrmSessionManagerProvider` to obtain a `DrmSessionManager`, which is then
injected into the created `MediaSource`. DRM behaviour can be
[further customized](https://developer.android.com/guide/topics/media/exoplayer/drm#using-a-custom-drmsessionmanager)
to your needs.

## Sideloading subtitle tracks

To sideload subtitle tracks, `MediaItem.Subtitle` instances can be added when
building a media item:

### Kotlin

```kotlin
val subtitle =
  MediaItem.SubtitleConfiguration.Builder(subtitleUri)
    .setMimeType(mimeType) // The correct MIME type (required).
    .setLanguage(language) // The subtitle language (optional).
    .setSelectionFlags(selectionFlags) // Selection flags for the track (optional).
    .build()
val mediaItem =
  MediaItem.Builder().setUri(videoUri).setSubtitleConfigurations(listOf(subtitle)).build()
```

### Java

```java
MediaItem.SubtitleConfiguration subtitle =
    new MediaItem.SubtitleConfiguration.Builder(subtitleUri)
        .setMimeType(mimeType) // The correct MIME type (required).
        .setLanguage(language) // The subtitle language (optional).
        .setSelectionFlags(selectionFlags) // Selection flags for the track (optional).
        .build();
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setSubtitleConfigurations(ImmutableList.of(subtitle))
        .build();
```

Internally, `DefaultMediaSourceFactory` will use a `MergingMediaSource` to
combine the content media source with a `SingleSampleMediaSource` for each
subtitle track. `DefaultMediaSourceFactory` does not support sideloading
subtitles for multi-period DASH.

## Clipping a media stream

To clip the content referred to by a media item, set custom
start and end positions:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setUri(videoUri)
    .setClippingConfiguration(
      MediaItem.ClippingConfiguration.Builder()
        .setStartPositionMs(startPositionMs)
        .setEndPositionMs(endPositionMs)
        .build()
    )
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setClippingConfiguration(
            new ClippingConfiguration.Builder()
                .setStartPositionMs(startPositionMs)
                .setEndPositionMs(endPositionMs)
                .build())
        .build();
```

Internally, `DefaultMediaSourceFactory` will use a `ClippingMediaSource` to wrap
the content media source. There are additional clipping properties. See the
[`MediaItem.Builder` Javadoc](https://developer.android.com/reference/androidx/media3/common/MediaItem.Builder) for more details.

> [!NOTE]
> **Note:** When clipping the start of a video file, try to align the start position with a keyframe if possible. If the start position is not aligned with a keyframe then the player will need to decode and discard data from the previous keyframe up to the start position before playback can begin. This will introduce a short delay at the start of playback, including when the player transitions to playing a clipped media source as part of a playlist or due to looping.

## Ad insertion

To insert ads, a media item's ad tag URI property should be set:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setUri(videoUri)
    .setAdsConfiguration(MediaItem.AdsConfiguration.Builder(adTagUri).build())
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setAdsConfiguration(new MediaItem.AdsConfiguration.Builder(adTagUri).build())
        .build();
```

Internally, `DefaultMediaSourceFactory` will wrap the content media source in an
`AdsMediaSource` to insert ads as defined by the ad tag. For this to work, the
player also needs to have its `DefaultMediaSourceFactory`
[configured accordingly](https://developer.android.com/guide/topics/media/exoplayer/ad-insertion#declarative-ad-support).

> [!CAUTION]
> **[Known issue #185:](https://github.com/androidx/media/issues/185)** Subtitles, clipping and ad insertion are only supported if you use `DefaultMediaSourceFactory`.