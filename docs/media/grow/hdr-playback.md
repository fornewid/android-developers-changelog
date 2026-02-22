---
title: https://developer.android.com/media/grow/hdr-playback
url: https://developer.android.com/media/grow/hdr-playback
source: md.txt
---

HDR, or High Dynamic Range, provides a wider range of colors and greater
contrast between the brightest whites and darkest shadows, resulting in video
quality that more closely resembles what the naked eye perceives.

You can set up HDR video playback in your app to preview and play back HDR video
content.

This article assumes that you've already added basic video playback support to
your app. See the [ExoPlayer](https://developer.android.com/guide/topics/media/exoplayer) documentation for
more details on playback.

## Device prerequisites

Not all Android devices support HDR playback. Before playing back HDR
video content in your app, determine if your device meets the following
prerequisites:

- Targets Android 7.0 or higher (API layer 24).
- Has a HDR-capable decoder and access to a HDR-capable display.

## Check for HDR playback support

Use [`Display.getHdrCapabilities()`](https://developer.android.com/reference/android/view/Display#getHdrCapabilities()) to query a display's HDR capabilities. The method returns information about the supported HDR profiles and luminance range for the display.

The following code checks if the device supports HLG10 playback. Starting in Android 13, HLG10 is the minimum standard that device makers must support if the device is capable of HDR playback:

### Kotlin

```kotlin
// Check if display supports the HDR type
val capabilities = display?.hdrCapabilities?.supportedHdrTypes ?: intArrayOf()
if (!capabilities.contains(HDR_TYPE_HLG)) {
  throw RuntimeException("Display does not support desired HDR type");
}
```

### Java

```java
// Check if display supports the HDR type
int[] list = getDisplay().getHdrCapabilities().getSupportedHdrTypes();
List capabilities = Arrays.stream(list).boxed().collect(Collectors.toList());
if (!capabilities.contains(HDR_TYPE_HLG)) {
 throw new RuntimeException("Display does not support desired HDR type");
}
```

## Set up HDR playback in your app

If your app uses [ExoPlayer](https://exoplayer.dev/), it supports HDR playback by default. See [Check for HDR playback support](https://developer.android.com/media/grow/hdr-playback#check_for_hdr_playback_support) for next steps.

If your app does not use ExoPlayer, set up HDR playback using `MediaCodec` via `SurfaceView`.
| **Note:** HDR playback has limited support on [`TextureView`](https://developer.android.com/reference/android/view/TextureView) in Android 13 (API layer 33) and higher. When playing back HDR video content, `TextureView` transcodes the video from HDR to SDR, resulting in playback with possible loss of detail including clipped colors and video banding. If at all possible, you should use `SurfaceView` for HDR playback.

### Set up MediaCodec using SurfaceView

Set up a standard [`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec) playback flow using [`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView). This allows you to display HDR video content without any special handling for HDR playback:

- `MediaCodec`: Decodes HDR video content.
- `SurfaceView`: Displays HDR video content.

The following code checks if the codec supports the HDR profile, then sets up `MediaCodec` using `SurfaceView`:

### Kotlin

```kotlin
// Check if there's a codec that supports the specific HDR profile
val list = MediaCodecList(MediaCodecList.REGULAR_CODECS) var format = MediaFormat() /* media format from the container */;
format.setInteger(MediaFormat.KEY_PROFILE, MediaCodecInfo.CodecProfileLevel.AV1ProfileMain10)
val codecName = list.findDecoderForFormat (format) ?: throw RuntimeException ("No codec supports the format")

// Here is a standard MediaCodec playback flow
val codec: MediaCodec = MediaCodec.createByCodecName(codecName);
val surface: Surface = surfaceView.holder.surface
val callback: MediaCodec.Callback = (object : MediaCodec.Callback() {
   override fun onInputBufferAvailable(codec: MediaCodec, index: Int) {
      queue.offer(index)
   }

   override fun onOutputBufferAvailable(
      codec: MediaCodec,
      index: Int,
      info: MediaCodec.BufferInfo
   ) {
      codec.releaseOutputBuffer(index, timestamp)
   }

   override fun onError(codec: MediaCodec, e: MediaCodec.CodecException) {
      // handle error
   }

   override fun onOutputFormatChanged(
      codec: MediaCodec, format: MediaFormat
   ) {
      // handle format change
   }
})

codec.setCallback(callback)
codec.configure(format, surface, crypto, 0 /* flags */)
codec.start()
while (/* until EOS */) {
   val index = queue.poll()
   val buffer = codec.getInputBuffer(index)
   buffer?.put(/* write bitstream */)
   codec.queueInputBuffer(index, offset, size, timestamp, flags)
}
codec.stop()
codec.release()
```

### Java

```java
// Check if there's a codec that supports the specific HDR profile
MediaCodecList list = new MediaCodecList(MediaCodecList.REGULAR_CODECS);
MediaFormat format = /* media format from the container */;
format.setInteger(
    MediaFormat.KEY_PROFILE, CodecProfileLevel.AV1ProfileMain10);
String codecName = list.findDecoderForFormat(format);
if (codecName == null) {
    throw new RuntimeException("No codec supports the format");
}

// Below is a standard MediaCodec playback flow
MediaCodec codec = MediaCodec.getCodecByName(codecName);
Surface surface = surfaceView.getHolder().getSurface();
MediaCodec.Callback callback = new MediaCodec.Callback() {
    @Override
    void onInputBufferAvailable(MediaCodec codec, int index) {
        queue.offer(index);
    }

    @Override
    void onOutputBufferAvailable(MediaCodec codec, int index) {
        // release the buffer for render
        codec.releaseOutputBuffer(index, timestamp);
    }

    @Override
    void onOutputFormatChanged(MediaCodec codec, MediaFormat format) {
        // handle format change
    }

    @Override
    void onError(MediaCodec codec, MediaCodec.CodecException ex) {
        // handle error
    }

};
codec.setCallback(callback);
codec.configure(format, surface, crypto, 0 /* flags */);
codec.start();
while (/* until EOS */) {
    int index = queue.poll();
    ByteBuffer buffer = codec.getInputBuffer(index);
    buffer.put(/* write bitstream */);
    codec.queueInputBuffer(index, offset, size, timestamp, flags);
}
codec.stop();
codec.release();
```

For more `MediaCodec` implementations using `SurfaceView`, see the [Android Camera samples](https://github.com/android/camera-samples).
| **Note:** Android takes screenshots in SDR. HDR content is tonemapped to SDR in screenshots.

## Resources

For more information related to HDR playback, see the following resources:

### HDR

- [HDR video capture](https://developer.android.com/training/camera2/hdr-video-capture): learn how to set up HDR video capture using the Camera2 APIs.
- [Camera2Video sample on Github](https://github.com/android/camera-samples/tree/main/Camera2Video): see a working app with HDR capture and playback functionality.

### Media

- [Media API reference](https://developer.android.com/reference/android/media/package-summary): learn more about the Media APIs.
- [ExoPlayer](https://exoplayer.dev/): learn how to set up your app with the ExoPlayer library.