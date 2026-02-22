---
title: https://developer.android.com/media/media3/transformer/troubleshooting
url: https://developer.android.com/media/media3/transformer/troubleshooting
source: md.txt
---

# Troubleshooting

- [Why can't I access local files in the demo app?](https://developer.android.com/media/media3/transformer/troubleshooting#local-files)
- [Why does exporting fail on a specific device?](https://developer.android.com/media/media3/transformer/troubleshooting#device-specific)
- [Does Transformer support transforming (or recording) remote media](https://developer.android.com/media/media3/transformer/troubleshooting#remote-media)
- [Does Transformer support 8k input?](https://developer.android.com/media/media3/transformer/troubleshooting#8k-media)
- [How does Transformer relate to platform compatible media transcoding?](https://developer.android.com/media/media3/transformer/troubleshooting#compatible-transcoding)
- [How can I reduce export latency or increase throughput?](https://developer.android.com/media/media3/transformer/troubleshooting#throughput)

*** ** * ** ***

#### Why can't I access local files in the demo app?

[Scoped storage enforcement](https://developer.android.com/about/versions/11/privacy/storage)from Android 11 (API level 30) prevents direct file system access. For manual testing during development, it's possible to access local files by adding the manage external storage permission in the demo app manifest:  

    <uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>

Then grant the permission via adb:  

```
adb shell appops set --uid androidx.media3.demo.transformer \
    MANAGE_EXTERNAL_STORAGE allow
```

#### Why does exporting fail on a specific device?

Please file an issue on the[Media3 issue tracker](https://github.com/androidx/media/issues)with enough information to reproduce the issue. Workarounds for device-specific issues can be added to the library to improve compatibility over time.

#### Does Transformer support transforming (or recording) remote media?

Transformer supports remote progressive streams, including media file containers like MP4.

In very poor network conditions, exporting may fail because buffering remote media for too long triggers checks in the muxer that are intended to identify that the pipeline is stuck. You can override the default behavior by setting`maxDelayBetweenMuxerSamplesMs`on`Transformer.Builder`:  

### Kotlin

```kotlin
Transformer.Builder(context)
    .setMaxDelayBetweenMuxerSamplesMs(C.TIME_UNSET)
    .build()
```

### Java

```java
new Transformer.Builder(context)
    .setMaxDelayBetweenMuxerSamplesMs(C.TIME_UNSET)
    .build();
```

<br />

Passing in`C.TIME_UNSET`removes the timeout entirely, but if your app runs on chipsets where`MediaCodec`can get stuck you may want to set a larger non-zero timeout.
| **[Known Issue #10943:](https://github.com/google/ExoPlayer/issues/10943)**Feature request to officially support transforming remote live streams with unknown duration using protocols like DASH and HLS.

#### Does Transformer support 8k input?

Transformer is implemented in a format-agnostic way, so it doesn't limit handling of 8k video, but hardware capabilities on the device may mean that exporting can't succeed. For example, even on devices that can capture 8k, it might not be possible to decode and re-encode an 8k video due to exceeding the available hardware codec or RAM resources.

#### How does Transformer relate to platform compatible media transcoding?

[Compatible media transcoding](https://developer.android.com/guide/topics/media-apps/video-app/compatible-media-transcoding)is an Android platform feature from Android 12 (API level 31) that converts media up to one minute in length into formats supported by the app. If you opt-in to using this feature, reading a media file in an incompatible format causes it to be transcoded on demand, and the result is cached for later read operations.

Transformer also supports[format conversion](https://developer.android.com/guide/topics/media/transformer/transformations#transcode), but it's available as a support library and the app has full control over the transcoding operation.

#### How can I reduce export latency or increase throughput?

Transformer relies on`MediaCodec`for hardware-accelerated decoding and encoding, and OpenGL for processing video frames. Based on our measurements on typical devices, the limiting factor in Transformer's throughput is hardware`MediaCodec`encoder throughput for use cases without heavyweight effects processing. This is likely to impact other implementations in the same way. For example, the platform compatible transcoding feature has similar performance to Transformer.

The demo app's debug preview significantly reduces throughput, so turn off the preview feature when testing with a release build of the demo app to get a realistic idea of performance.