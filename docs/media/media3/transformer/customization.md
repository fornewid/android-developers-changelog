---
title: Customization  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/transformer/customization
source: html-scrape
---

Media3 Transformer is actively under development and we are looking to hear from you! We welcome your feedback, feature requests and bug reports in the [issue tracker](https://github.com/androidx/media/issues). Follow the [ExoPlayer blog](https://medium.com/google-exoplayer) for the latest updates.

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Customization Stay organized with collections Save and categorize content based on your preferences.



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

```
transformerBuilder.setEncoderFactory(
  DefaultEncoderFactory.Builder(context).setEnableFallback(false).build()
)

Customization.kt
```

### Java

```
transformerBuilder.setEncoderFactory(
    new DefaultEncoderFactory.Builder(context).setEnableFallback(false).build());

Customization.java
```

Similarly, the `DefaultEncoderFactory` also supports using custom encoding
settings with the `setRequestedVideoEncoderSettings` option.

You can also completely replace the factories for encoders and decoders to get
full control over how the codecs are set up.

## Custom muxers

You can set a custom muxer for writing media containers by calling
`Transformer.setMuxerFactory`. For example, if you implement your own muxer at
the application level, you can write a wrapper that implements the `Muxer`
interface and then use `setMuxerFactory` to inject it into Transformer.