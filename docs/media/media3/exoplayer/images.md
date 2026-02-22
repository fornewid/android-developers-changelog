---
title: https://developer.android.com/media/media3/exoplayer/images
url: https://developer.android.com/media/media3/exoplayer/images
source: md.txt
---

ExoPlayer supports the following image formats. See
[Image Loading Libraries](https://developer.android.com/media/media3/exoplayer/images#image-loading-libraries)
for how to integrate with external libraries that may provide support for a
different set of formats.

| Image format | Supported | Notes |
|---|---|---|
| BMP | YES |   |
| GIF | NO | No Extractor support |
| JPEG | YES |   |
| JPEG Motion Photo | YES | Still image and video supported |
| JPEG Ultra HDR | YES | Falls back to SDR before Android 14 or on non-HDR displays |
| PNG | YES |   |
| WebP | YES |   |
| HEIF/HEIC | YES |   |
| HEIC Motion Photo | YES |   |
| AVIF (baseline) | YES | Decoded on Android 14+ only |

## Using MediaItem

To play an image as part of a playlist, create a `MediaItem` with the image URI
and pass it to the player. The `MediaItem` must have a `imageDurationMs` to
specify for how long the image should be displayed.

### Kotlin

```kotlin
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played with the desired duration.
player.setMediaItem(MediaItem.Builder().setUri(imageUri).setImageDurationMs(2000).build())
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played with the desired duration.
player.setMediaItem(new MediaItem.Builder().setUri(imageUri).setImageDurationMs(2000).build());
// Prepare the player.
player.prepare();
```

### Motion Photos

Motion photos are files combining a still image with a short video.

- If the image duration is defined with `setImageDuration`, the motion photo is displayed for the declared duration as a still image.
- If the image duration is undefined, the motion photo is played as a video.

## Using ProgressiveMediaSource

For more customization options, you can create a `ProgressiveMediaSource` and
pass it directly to the player instead of a `MediaItem`.

### Kotlin

```kotlin
// Create a data source factory.
val dataSourceFactory: DataSource.Factory = DefaultHttpDataSource.Factory()
// Create a media item with the image URI and the desired duration.
val mediaItem = MediaItem.Builder().setUri(imageUri).setImageDurationMs(2000).build()
// Create a progressive media source for this media item.
val mediaSource = ProgressiveMediaSource.Factory(dataSourceFactory).createMediaSource(mediaItem)
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media source to be played.
player.setMediaSource(mediaSource)
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a data source factory.
DataSource.Factory dataSourceFactory = new DefaultHttpDataSource.Factory();
// Create a media item with the image URI and the desired duration.
MediaItem mediaItem = new MediaItem.Builder().setUri(imageUri).setImageDurationMs(2000).build();
// Create a progressive media source for this media item.
MediaSource mediaSource =
    new ProgressiveMediaSource.Factory(dataSourceFactory).createMediaSource(mediaItem);
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media source to be played.
player.setMediaSource(mediaSource);
// Prepare the player.
player.prepare();
```

## Customizing playback

ExoPlayer provides multiple ways for you to tailor playback experience to your
app's needs. See the [Customization page](https://developer.android.com/guide/topics/media/exoplayer/customization) for examples.

## Image Loading Libraries

Images are often managed by external image loading libraries, for example
[Glide](https://bumptech.github.io/glide/) or
[Coil](https://coil-kt.github.io/coil/).

Integrating these libraries into the playback pipeline requires 3 steps:

1. Define a `MediaItem` with `APPLICATION_EXTERNALLY_LOADED_IMAGE` MIME type.
2. Provide an image decoder to retrieve a `Bitmap` from the image loading library.
3. Provide an external loader to trigger caching and preloading.

### MediaItem with externally loaded image MIME type

The `MediaItem` added to the `Player` must define the
`APPLICATION_EXTERNALLY_LOADED_IMAGE` MIME type explicitly to use the image
loading library code paths:

### Kotlin

```kotlin
val mediaItem =
  MediaItem.Builder()
    .setUri(imageUri)
    .setMimeType(MimeTypes.APPLICATION_EXTERNALLY_LOADED_IMAGE)
    .build()
```

### Java

```java
MediaItem mediaItem =
    new MediaItem.Builder()
        .setUri(imageUri)
        .setMimeType(MimeTypes.APPLICATION_EXTERNALLY_LOADED_IMAGE)
        .build();
```

### Image decoder using an image loading library

The image renderer needs an `ExternallyLoadedImageDecoder` to retrieve the
`Bitmap` from the `Uri`. This decoder can be provided by overriding
`DefaultRenderersFactory.getImageDecoderFactory`.

The following example uses Glide to load an image, limiting the output to
the display size to avoid creating very large `Bitmap` objects:

### Kotlin

```kotlin
val glideImageDecoderFactory: ImageDecoder.Factory =
  ExternallyLoadedImageDecoder.Factory { request: ExternalImageRequest ->
    val displaySize = Util.getCurrentDisplayModeSize(context)
    GlideFutures.submit(
      Glide.with(context)
        .asBitmap()
        .load(request.uri)
        .override(max(displaySize.x, displaySize.y))
    )
  }
val player: Player =
  ExoPlayer.Builder(context)
    .setRenderersFactory(
      object : DefaultRenderersFactory(context) {
        override fun getImageDecoderFactory(context: Context): ImageDecoder.Factory {
          return glideImageDecoderFactory
        }
      }
    )
    .build()
```

### Java

```java
ImageDecoder.Factory glideImageDecoderFactory =
    new ExternallyLoadedImageDecoder.Factory(
        request -> {
          Point displaySize = Util.getCurrentDisplayModeSize(context);
          return GlideFutures.submit(
              Glide.with(context)
                  .asBitmap()
                  .load(request.uri)
                  .override(max(displaySize.x, displaySize.y)));
        });
Player player =
    new ExoPlayer.Builder(context)
        .setRenderersFactory(
            new DefaultRenderersFactory(context) {
              @Override
              protected ImageDecoder.Factory getImageDecoderFactory(Context context) {
                return glideImageDecoderFactory;
              }
            })
        .build();
```

### Image preloading with an image loading library

During playback, the player requests to preload the next image once the previous
item in the playlist has fully loaded. When using an external image loading
library, you must specify an `ExternalLoader` to trigger this preloading. If no
preloading is possible or required, this loader still needs to be provided, but
can do nothing.

The following example uses Glide to ensure that the requested image is preloaded
to disk:

### Kotlin

```kotlin
val glidePreloader = ExternalLoader { request: LoadRequest ->
  GlideFutures.submit(
    Glide.with(context)
      .asFile()
      .apply(
        RequestOptions.diskCacheStrategyOf(DiskCacheStrategy.DATA)
          .priority(Priority.HIGH)
          .skipMemoryCache(true)
      )
      .load(request.uri)
  )
}
val player: Player =
  ExoPlayer.Builder(context)
    .setMediaSourceFactory(
      DefaultMediaSourceFactory(context).setExternalImageLoader(glidePreloader)
    )
    .build()
```

### Java

```java
ExternalLoader glidePreloader =
    request ->
        GlideFutures.submit(
            Glide.with(context)
                .asFile()
                .apply(
                    diskCacheStrategyOf(DiskCacheStrategy.DATA)
                        .priority(Priority.HIGH)
                        .skipMemoryCache(true))
                .load(request.uri));
Player player =
    new ExoPlayer.Builder(context)
        .setMediaSourceFactory(
            new DefaultMediaSourceFactory(context).setExternalImageLoader(glidePreloader))
        .build();
```