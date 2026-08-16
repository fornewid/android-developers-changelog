---
title: https://developer.android.com/media/media3/transformer/customization
url: https://developer.android.com/media/media3/transformer/customization
source: md.txt
---

To control Transformer's behavior, you can configure options in the API surface
or replace pieces of functionality completely by writing custom implementations
of interfaces and passing those in. This page describes some examples.

## Control codec configuration

By default, Transformer will fall back to a supported resolution if the
device's hardware encoder doesn't accept the requested output resolution. For
example, Transformer can align the output width and height to be a multiple of 2
or 16 as is often required by hardware encoders. You can turn off this behavior
so that Transformer instead throws an error if it can't produce the required
output resolution:


### Kotlin

```kotlin
transformerBuilder.setEncoderFactory(
  DefaultEncoderFactory.Builder(context).setEnableFallback(false).build()
)
```

### Java

```java
transformerBuilder.setEncoderFactory(
    new DefaultEncoderFactory.Builder(context).setEnableFallback(false).build());
```

<br />

Similarly, the `DefaultEncoderFactory` also supports using custom encoding
settings with the `setRequestedVideoEncoderSettings` option.

You can also completely replace the factories for encoders and decoders to get
full control over how the codecs are set up.

## Custom muxers

You can set a custom muxer for writing media containers by calling
`Transformer.setMuxerFactory`. For example, if you implement your own muxer at
the application level, you can write a wrapper that implements the `Muxer`
interface and then use `setMuxerFactory` to inject it into Transformer.

If your custom muxer supports writing negative timestamps in MP4 edit lists, you
should ensure that
[`Muxer.Factory#supportsWritingNegativeTimestampsInEditList`](https://developer.android.com/reference/androidx/media3/muxer/Muxer.Factory#supportsWritingNegativeTimestampsInEditList()) returns
`true`. This enables Transformer to perform optimizations, such as trim-only
edits using MP4 edit lists, without needing to re-encode the video. For the
default `InAppMp4Muxer`, this is already supported.