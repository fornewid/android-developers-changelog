---
title: https://developer.android.com/media/media3/exoplayer/shrinking
url: https://developer.android.com/media/media3/exoplayer/shrinking
source: md.txt
---

Minimizing APK size is an important aspect of developing a good Android
app. This is particularly true when targeting developing markets, and
also when developing an Android Instant App. For such cases, it may be desirable
to minimize the size of the ExoPlayer library that's included in the APK. This
page outlines some simple steps that can help to achieve this.

## Use only required dependencies

Depend only on the library modules that you actually need. For example, the
following will add dependencies on the ExoPlayer, DASH, and UI library modules,
as might be required for an app that only plays DASH content:

### Kotlin

```kotlin
implementation("androidx.media3:media3-exoplayer:1.9.2")
implementation("androidx.media3:media3-exoplayer-dash:1.9.2")
implementation("androidx.media3:media3-ui:1.9.2")
```

### Groovy

```groovy
implementation "androidx.media3:media3-exoplayer:1.9.2"
implementation "androidx.media3:media3-exoplayer-dash:1.9.2"
implementation "androidx.media3:media3-ui:1.9.2"
```

## Enable code and resource shrinking

You should enable code and resource shrinking for your app's release
builds. ExoPlayer is structured in a way that allows code shrinking to
effectively remove unused functionality. For example, for an app that
plays DASH content, ExoPlayer's contribution to APK size can be reduced by
approximately 40% by enabling code shrinking.

Read [Shrink, obfuscate, and optimize your app](https://developer.android.com/studio/build/shrink-code) to learn how to enable
code and resource shrinking.

## Specify which renderers your app needs

By default, the player's renderers will be created using
`DefaultRenderersFactory`. `DefaultRenderersFactory` depends on all of the
`Renderer` implementations provided in the ExoPlayer library, and as a result
none of them will be removed by code shrinking. If you know that your app only
needs a subset of renderers, you can specify your own `RenderersFactory`
instead. For example, an app that only plays audio can define a factory like
this when instantiating `ExoPlayer` instances:

### Kotlin

```kotlin
val audioOnlyRenderersFactory =
  RenderersFactory {
    handler: Handler,
    videoListener: VideoRendererEventListener,
    audioListener: AudioRendererEventListener,
    textOutput: TextOutput,
    metadataOutput: MetadataOutput ->
    arrayOf<Renderer>(
      MediaCodecAudioRenderer(context, MediaCodecSelector.DEFAULT, handler, audioListener)
    )
  }
val player = ExoPlayer.Builder(context, audioOnlyRenderersFactory).build()
```

### Java

```java
RenderersFactory audioOnlyRenderersFactory =
    (handler, videoListener, audioListener, textOutput, metadataOutput) ->
        new Renderer[] {
          new MediaCodecAudioRenderer(
              context, MediaCodecSelector.DEFAULT, handler, audioListener)
        };
ExoPlayer player = new ExoPlayer.Builder(context, audioOnlyRenderersFactory).build();
```

This will allow other `Renderer` implementations to be removed by code
shrinking. In this particular example video, text and metadata renderers are
removed (which means any subtitles or in-stream metadata (e.g.
[ICY](https://cast.readme.io/docs/icy)) won't be processed or emitted by the
player).

## Specify which extractors your app needs

By default, the player creates `Extractor` instances to play progressive media using
`DefaultExtractorsFactory`. `DefaultExtractorsFactory` depends on all of the
`Extractor` implementations provided in the ExoPlayer library, and as a result
none of them will be removed by code shrinking. If you know that your app only
needs to play a small number of container formats, or doesn't play progressive
media at all, you can specify your own `ExtractorsFactory` instead. For example,
an app that only needs to play mp4 files can provide a factory like:

### Kotlin

```kotlin
val mp4ExtractorFactory = ExtractorsFactory {
  arrayOf<Extractor>(Mp4Extractor(DefaultSubtitleParserFactory()))
}
val player =
  ExoPlayer.Builder(context, DefaultMediaSourceFactory(context, mp4ExtractorFactory)).build()
```

### Java

```java
ExtractorsFactory mp4ExtractorFactory =
    () -> new Extractor[] {new Mp4Extractor(new DefaultSubtitleParserFactory())};
ExoPlayer player =
    new ExoPlayer.Builder(context, new DefaultMediaSourceFactory(context, mp4ExtractorFactory))
        .build();
```

This will allow other `Extractor` implementations to be removed by code
shrinking, which can result in a significant reduction in size.

If your app is not playing progressive content at all, you should pass
`ExtractorsFactory.EMPTY` to the `DefaultMediaSourceFactory` constructor, then
pass that `mediaSourceFactory` to the `ExoPlayer.Builder` constructor.

### Kotlin

```kotlin
val player =
  ExoPlayer.Builder(context, DefaultMediaSourceFactory(context, ExtractorsFactory.EMPTY))
    .build()
```

### Java

```java
ExoPlayer player =
    new ExoPlayer.Builder(
            context, new DefaultMediaSourceFactory(context, ExtractorsFactory.EMPTY))
        .build();
```

## Custom MediaSource instantiation

If your app is using a custom `MediaSource.Factory` and you want
`DefaultMediaSourceFactory` to be removed by code stripping, you should pass
your `MediaSource.Factory` directly to the `ExoPlayer.Builder` constructor.

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context, customMediaSourceFactory).build()
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context, mediaSourceFactory).build();
```

If your app is using `MediaSource` directly instead of `MediaItem` you should
pass `MediaSource.Factory.UNSUPPORTED` to the `ExoPlayer.Builder` constructor,
to ensure `DefaultMediaSourceFactory` and `DefaultExtractorsFactory` can be
stripped by code shrinking.

### Kotlin

```kotlin
val player = ExoPlayer.Builder(context, MediaSource.Factory.UNSUPPORTED).build()
val mediaSource =
  ProgressiveMediaSource.Factory(dataSourceFactory, customExtractorsFactory)
    .createMediaSource(MediaItem.fromUri(uri))
```

### Java

```java
ExoPlayer player = new ExoPlayer.Builder(context, MediaSource.Factory.UNSUPPORTED).build();
ProgressiveMediaSource mediaSource =
    new ProgressiveMediaSource.Factory(dataSourceFactory, customExtractorsFactory)
        .createMediaSource(MediaItem.fromUri(uri));
```