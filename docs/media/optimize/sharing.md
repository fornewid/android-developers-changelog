---
title: https://developer.android.com/media/optimize/sharing
url: https://developer.android.com/media/optimize/sharing
source: md.txt
---

# Best practices for sharing video

Many people share videos using their Android device. The quality of the received video is often inferior to the original because of processing that's performed by the sharing app. This document describes how to optimize the quality of shared videos and some common video processing pitfalls to avoid. To optimize for sharing HDR video content, see[Use the Transformer module to transcode HDR to SDR](https://developer.android.com/guide/topics/media/sharing-video#hdr_to_sdr)on this page.

The main thing to do is to maintain a constant resolution and keep the video quality as high as possible for as long as possible while preparing to share a video.
| **Note:** Many sharing apps use the AVC encoding format; the examples on this page are written assuming the operations use AVC. The same principles apply to other encoding standards.

## The sharing pipeline

Figure 1 illustrates a typical flow for sharing a video:

![Sharing video pipeline](https://developer.android.com/static/media/images/sharing-video-pipeline.svg)**Figure 1.**The video sharing pipeline.

The pipeline includes these steps:

1. Capture and encode a video, possibly adding effects during the capture. Alternatively, the user can skip this step and select a video from storage that was prerecorded from another app.
2. Edit, filter, touch up, or otherwise process the video.
3. Scale or resize the video in preparation for transcoding.
4. Transcode the video for sharing. The filtering in step 2 is often applied as part of this step.

There are two steps in the pipeline where you have the opportunity to set parameters that determine the quality of your video: encoding during the initial recording, and transcoding before sharing. In addition, you might need to rescale the video before the final transcode step, which can affect quality too.

## Recommendations

Table 1 shows the five main parameters for video quality, and indicates which steps can use them.

|-----------------------------|----------|-------|
| Parameter                   | Capture  | Share |
| Profile                     | Y        | Y     |
| Resolution                  | Y        | Y     |
| Bitrate                     | Y        | Y     |
| Quantization Parameter (QP) | (rarely) | Y     |
| B frames                    | N        | Y     |

**Table 1.**Main parameters that determine video quality

### Profile

For better results, use the more advanced profiles provided by the particular codec. For AVC encoding, select High profile and level 4.

### Resolution, cropping, and scaling

You can change the initial resolution of the captured video in the scaling step before transcoding for sharing, but scaling can degrade the quality of the video. We recommend you avoid scaling and select a resolution for the initial encoding that you can use throughout the pipeline. Also remember that extreme cropping results in a low quality image, especially if you upscale the cropped image. Follow these guidelines:

- Choose a resolution at least as large as the final sharing resolution.
- The capture resolution should not greatly exceed the sharing resolution unless all of the intermediate steps are designed to support the larger resolution (such as the higher bitrate during initial capture).

  - If the sharing encoding produces a 720x1280 resolution, we recommend a 720x1280 capture resolution.
  - If intermediate steps between capture and sharing include cropping, use a higher capture resolution such as 1080x1920, and increase the capture bitrate to handle the extra pixels.
- Extreme cropping results in a low quality image, especially if the cropped image is upscaled.

- Avoid upscaling from lower resolution to higher resolution. Upscaling tries to create detail that is not present. Carry the desired higher resolution along from the beginning.

- If you must upscale, adjust the encoding parameters. For instance, if the upscaled resolution has twice as many pixels, double the bitrate.

Resolution and bitrate are interrelated. For example, carrying a high-resolution video through a sharing pipeline that ultimately transcodes to a low bitrate produces a lower-quality image than starting with a lower resolution. As the bitrate decreases, there are crossover points at which smaller resolutions start to yield better results:

|------------------|-----------------------------------------------------------------------------|
| Bitrate          | Resolution                                                                  |
| 5+ Mbps          | 1080x1920                                                                   |
| 1.5 - 5+ Mbps    | 720x1280                                                                    |
| 1.5 Mbps or less | SD-equivalent. The same pixel count in a 9:16 aspect ratio is about 416x736 |

**Table 2.**Bitrate versus Resolution

Many popular apps share video at resolution 720p or lower. The data indicates that 720p resolution is an appropriate choice for bitrate targets between 1.5 and 5 Mbps.

### Bitrate

#### Recording

Using a higher encoding bitrate provides the largest improvement in video quality. We recommend choosing bitrates that match the native camera apps. For a 720x1280 resolution, we recommend a capture bitrate of 10 Mbps.

Since the capture encoding is done on-device, you can use a higher bitrate to compensate for most of the sharing step transformations with little negative impact. The larger resulting files are used only for on-device manipulation.

You can reduce the bitrate at the final transcoding step, as shown in table 2.

#### Sharing

Bitrate has the most impact at share time, because it directly relates to the size of the video that will be uploaded. There is a tradeoff between video quality, file transmission time, and cloud storage costs.

The choice of encoding profile, B-frames and QP bounding values is also more important at this stage than it is during capture.

We recommend a bitrate between 4-5 Mbps (for 720x1280 resolution) to ensure good visual quality.

### Quantization Parameter (QP)

On Android 12 and higher, the QP keys are standardized and are available in the[`MediaFormat`](https://developer.android.com/reference/android/media/MediaFormat#KEY_VIDEO_QP_B_MAX)API and in the[NDK Media library](https://developer.android.com/ndk/reference/group/media). On earlier Android versions, QP manipulation is available only through framework functions using vendor-specific keys in the`MediaFormat`configuration.

#### Recording

During video capture, use the bitrate control rather than QP settings, which are not always available.

We don't recommend adjusting the QP settings for capture bitrates of 10Mbps (for 720x1280). If the capture bitrate is significantly lower, under 5 Mbps for 720x1280, a QP setting of 40 is a good compromise between increased quality without forcing the codec into over-shooting the target bitrate too often.

#### Sharing

We recommend a max QP bound of 40, especially when the bitrate is below 4 Mbps. While this ensures a minimum quality for the encoded videos, it can produce a result with a higher bitrate. The increase in bitrate depends on the video's complexity. Although a sharing app might tolerate some variance in the bitrate of the generated video, it might not tolerate an increase beyond a certain threshold.

You can limit the bitrate increase by re-encoding the video for sharing with a less restrictive (higher) max QP bound. This gives the codec more freedom to sacrifice quality and preserve other parts of the video. You can re-encode the video for sharing because it is a transcoding operation; you have already captured the video you intend to share.

The drawback is that repeating the transcoding step with these different parameters increases the time it takes to share the video. One way to reduce this latency is to look at the partially transcoded video to decide if it is not within your tolerance for bitrate overage. If it is not, you can stop the transcoding and try again with more-appropriate QP parameters.

### B-frames and encoding profiles

Consider using B-frames only during the sharing step, and only when running Android 10 or higher.

Apps should check the supported encoding profiles using[`CodecCapabilities`](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecCapabilities), since not all devices support main or high profiles. Use the highest profile supported by the AVC encoder: High \> Main \> Baseline. For safest results, do not configure B-frames ([`KEY_LATENCY`](https://developer.android.com/reference/android/media/MediaFormat#KEY_LATENCY)or[`KEY_MAX_B_FRAMES`](https://developer.android.com/reference/android/media/MediaFormat#KEY_MAX_B_FRAMES)) when using the baseline profile as some encoders may fail configuration.

The following code segments assume a`'MediaFormat format'`that will be used to configure the AVC encoder

#### Android 10

API 29 or higher

Use the highest supported profile and set the B-frame parameter to 1:  

    format.setInt32(KEY_PROFILE, AVCProfileHigh);
    format.setInt32(KEY_MAX_B_FRAMES, 1);

Do not set`KEY_LATENCY`in this situation.

#### Android 8, 8.1, and 9

APIs 26, 27, 28

Use the highest-supported profile, but disable the generation of B-frames. This accommodates some limitations in the[`MediaMuxer`](https://developer.android.com/reference/android/media/MediaMuxer)in these system versions  

    format.setInt32(KEY_PROFILE, AVCProfileHigh);
    format.setInt32(KEY_LATENCY, 1);

The`KEY_LATENCY`value prohibits the codecs from generating B-frames, but still takes advantage of other codec efficiencies.

If your app does not use`MediaMuxer`to assemble the final output file, you may enable B-frames by setting the`KEY_LATENCY`value to 2 instead of 1. This should allow the codec to produce B-frames.

#### Android 7.1 and earlier

API 25 and earlier

Use the baseline profile for safest results.  

    format.setInt32(KEY_PROFILE, AVCProfileBaseline);

Prior to version 7, Android AOSP supports only the baseline profile. However, it is likely that OEMs enabled a main/high profile on some devices, perhaps by using a vendor-specific profile.

If your app does not use`MediaMuxer`, you can use the main or high profile when the codec supports it. There is no public format key to control the number of B- frames.

## Use the Transformer module to transcode HDR to SDR

Starting with Android 13 (API level 33), we recommend using Jetpack Media3's[Transformer](https://github.com/androidx/media/tree/main/libraries/transformer)module to share HDR content to apps, services, and devices that do not support HDR. The Transformer module works by tone-mapping an input HDR video stream to SDR and saving the result as an MP4, which enables successful playback without loss of detail or image brightness.

**Note**: On devices targeting system versions between Android 12 (API level 32) down to Android 7.0 (API level 24), the Transformer module works differently. If the device supports HDR, your app plays back the content without tone-mapping. If the device doesn't support HDR, it throws an error indicating that HDR tone-mapping is not supported.

The following code sets up a Transformer that tone maps the input to SDR and re-encodes it in the input format (such as H.264/AVC):  

### Kotlin

```kotlin
val transformer = Transformer.Builder(context)
    .setTransformationRequest(
        TransformationRequest.Builder()
            .setHdrMode(TransformationRequest.HDR_MODE_TONE_MAP_HDR_TO_SDR)
            .build())
    .addListener(/* ... */)
    .build()
```

### Java

```java
Transformer transformer = new Transformer.Builder(context)
    .setTransformationRequest(
        new TransformationRequest.Builder()
            .setHdrMode(TransformationRequest.HDR_MODE_TONE_MAP_HDR_TO_SDR)
            .build())
    .addListener(/* ... */)
    .build();
```

To try out the tone mapping functionality, see the[Transformer demo app](https://github.com/androidx/media/tree/release/demos/transformer).

You can also set up tone mapping using[`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec), although the implementation is more complex. For more information, see the[`MediaCodec`](https://developer.android.com/reference/android/media/MediaCodec)reference documentation.