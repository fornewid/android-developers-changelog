---
title: Media items  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/exoplayer/media-items
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media items Stay organized with collections Save and categorize content based on your preferences.




The [playlist API](/guide/topics/media/exoplayer/playlists) is based on `MediaItem` instances, which can be conveniently built
using `MediaItem.Builder`. Inside the player, a `MediaItem` is converted into
a playable `MediaSource` by a `MediaSource.Factory`. Without
[custom configuration](/guide/topics/media/exoplayer/media-sources#customizing-media-source-creation),
this conversion is carried out by a `DefaultMediaSourceFactory`, which is
capable of building complex media sources corresponding to the properties of the
media item. Some of the properties that can be set on media items are outlined
below.

## Simple media items

A media item consisting only of the stream URI can be built with the `fromUri`
convenience method:

### Kotlin

```
val mediaItem = MediaItem.fromUri(videoUri)

MediaItems.kt
```

### Java

```
MediaItem mediaItem = MediaItem.fromUri(videoUri);

MediaItems.java
```

For all other cases, a `MediaItem.Builder` can be used. In the following example, a
media item is built with an ID and some attached metadata:

### Kotlin

```
val mediaItem =
  MediaItem.Builder().setMediaId(mediaId).setTag(myAppData).setUri(videoUri).build()

MediaItems.kt
```

### Java

```
MediaItem mediaItem =
    new MediaItem.Builder().setMediaId(mediaId).setTag(myAppData).setUri(videoUri).build();

MediaItems.java
```

Attaching metadata can be useful for
[updating your app's UI](/guide/topics/media/exoplayer/playlists#detecting-transitions)
when playlist transitions occur.

## Images

Playback of images requires a duration in the media item to specify for how long
the image should be shown during playback. See the
[Images](/media/media3/exoplayer/images) guide page for more information on
[Motion Photos](/media/media3/exoplayer/images#motion-photos) and
[Image Loading Libraries](/media/media3/exoplayer/images#image-loading-libraries)
(for example, Glide).

### Kotlin

```
val mediaItem = MediaItem.Builder().setUri(imageUri).setImageDurationMs(3000).build()

MediaItems.kt
```

### Java

```
MediaItem mediaItem =
    new MediaItem.Builder().setUri(imageUri).setImageDurationMs(3_000).build();

MediaItems.java
```

## Non-standard file extensions for adaptive media

ExoPlayer provides adaptive media sources for DASH, HLS, and
SmoothStreaming. If the URI of such an adaptive media item ends with a standard
file extension, the corresponding media source is automatically created. If the
URI has a non-standard extension or no extension at all, then the MIME type can
be set explicitly to indicate the type of the media item:

### Kotlin

```
val mediaItem =
  MediaItem.Builder().setUri(hlsUri).setMimeType(MimeTypes.APPLICATION_M3U8).build()

MediaItems.kt
```

### Java

```
MediaItem mediaItem =
    new MediaItem.Builder().setUri(hlsUri).setMimeType(MimeTypes.APPLICATION_M3U8).build();

MediaItems.java
```

For progressive media streams a MIME type is not required.

## Protected content

For protected content, the media item's DRM properties should be set. The UUID
is required, all the other properties are optional.

An example config for playing an item protected with Widevine DRM where the
license URI is not available directly in the media (e.g. in a DASH playlist) and
multiple sessions are required (e.g. due to key rotation):

### Kotlin

```
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

MediaItems.kt
```

### Java

```
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

MediaItems.java
```

Inside the
player, `DefaultMediaSourceFactory` will pass these properties to a
`DrmSessionManagerProvider` to obtain a `DrmSessionManager`, which is then
injected into the created `MediaSource`. DRM behaviour can be
[further customized](/guide/topics/media/exoplayer/drm#using-a-custom-drmsessionmanager)
to your needs.

## Sideloading subtitle tracks

To sideload subtitle tracks, `MediaItem.Subtitle` instances can be added when
building a media item:

### Kotlin

```
val subtitle =
  MediaItem.SubtitleConfiguration.Builder(subtitleUri)
    .setMimeType(mimeType) // The correct MIME type (required).
    .setLanguage(language) // The subtitle language (optional).
    .setSelectionFlags(selectionFlags) // Selection flags for the track (optional).
    .build()
val mediaItem =
  MediaItem.Builder().setUri(videoUri).setSubtitleConfigurations(listOf(subtitle)).build()

MediaItems.kt
```

### Java

```
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

MediaItems.java
```

Internally, `DefaultMediaSourceFactory` will use a `MergingMediaSource` to
combine the content media source with a `SingleSampleMediaSource` for each
subtitle track. `DefaultMediaSourceFactory` does not support sideloading
subtitles for multi-period DASH.

## Clipping a media stream

To clip the content referred to by a media item, set custom
start and end positions:

### Kotlin

```
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

MediaItems.kt
```

### Java

```
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setClippingConfiguration(
            new ClippingConfiguration.Builder()
                .setStartPositionMs(startPositionMs)
                .setEndPositionMs(endPositionMs)
                .build())
        .build();

MediaItems.java
```

Internally, `DefaultMediaSourceFactory` will use a `ClippingMediaSource` to wrap
the content media source. There are additional clipping properties. See the
[`MediaItem.Builder` Javadoc](/reference/androidx/media3/common/MediaItem.Builder) for more details.

**Note:** When clipping the start of a video file, try to align the start position with a
keyframe if possible. If the start position is not aligned with a keyframe then
the player will need to decode and discard data from the previous keyframe up to
the start position before playback can begin. This will introduce a short delay
at the start of playback, including when the player transitions to playing a
clipped media source as part of a playlist or due to looping.

## Ad insertion

To insert ads, a media item's ad tag URI property should be set:

### Kotlin

```
val mediaItem =
  MediaItem.Builder()
    .setUri(videoUri)
    .setAdsConfiguration(MediaItem.AdsConfiguration.Builder(adTagUri).build())
    .build()

MediaItems.kt
```

### Java

```
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(videoUri)
        .setAdsConfiguration(new MediaItem.AdsConfiguration.Builder(adTagUri).build())
        .build();

MediaItems.java
```

Internally, `DefaultMediaSourceFactory` will wrap the content media source in an
`AdsMediaSource` to insert ads as defined by the ad tag. For this to work, the
player also needs to have its `DefaultMediaSourceFactory`
[configured accordingly](/guide/topics/media/exoplayer/ad-insertion#declarative-ad-support).

**[Known issue #185:](https://github.com/androidx/media/issues/185)** Subtitles, clipping and ad insertion are only supported if you use `DefaultMediaSourceFactory`.