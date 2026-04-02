---
title: https://developer.android.com/media/platform/supported-formats
url: https://developer.android.com/media/platform/supported-formats
source: md.txt
---

# Supported media formats

This document describes the media codec, container, and network protocol support provided by the Android platform.

The tables below describe the media format support built into the Android platform. YES means the format is available on handhelds and tablets running all Android versions. Where a specific Android platform is specified, the format is available on handsets and tablets running that version and all later versions. The format might also be available in earlier versions, but this is not guaranteed. On form factors other than handsets and tablets, media format support may vary.

Note that a particular mobile device might support additional formats or file types that are not listed in these tables. In addition, if you use a[MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)directly, you can access any of the available media formats regardless of the supported file types and container formats.

## Audio support

|              Format              |   Encoder    |   Decoder    |                                                                                                                  File Types Container Formats                                                                                                                   ||                                                                                                                        Details                                                                                                                        |
|              Format              |   Encoder    |   Decoder    |                                                         Extractor                                                         |                                                                Muxer                                                                 |                                                                                                                        Details                                                                                                                        |
|----------------------------------|--------------|--------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAC LC                           | YES          | YES          | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (.ts, not seekable, Android 3.0+) | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (not sure) (.ts, not seekable, Android 3.0+) | Support for mono/stereo/5.0/5.1 content with standard sampling rates from 8 to 48 kHz.                                                                                                                                                                |
| HE-AACv1 (AAC+)                  | Android 4.1+ | YES          | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (.ts, not seekable, Android 3.0+) | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (not sure) (.ts, not seekable, Android 3.0+) | Support for mono/stereo/5.0/5.1 content with standard sampling rates from 8 to 48 kHz.                                                                                                                                                                |
| HE-AACv2 (enhanced AAC+)         |              | YES          | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (.ts, not seekable, Android 3.0+) | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (not sure) (.ts, not seekable, Android 3.0+) | Support for stereo/5.0/5.1 content with standard sampling rates from 8 to 48 kHz.                                                                                                                                                                     |
| xHE-AAC                          |              | Android 9+   | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (.ts, not seekable, Android 3.0+) | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (not sure) (.ts, not seekable, Android 3.0+) | Support for up to 8ch content with standard sampling rates from 8 to 48 kHz                                                                                                                                                                           |
| AAC ELD (enhanced low delay AAC) | Android 4.1+ | Android 4.1+ | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (.ts, not seekable, Android 3.0+) | • 3GPP (.3gp) • MPEG-4 (.mp4, .m4a) • ADTS raw AAC (.aac, ADIF not supported) • MPEG-TS (not sure) (.ts, not seekable, Android 3.0+) | Support for mono/stereo content with standard sampling rates from 16 to 48 kHz                                                                                                                                                                        |
| AMR-NB                           | YES          | YES          | • 3GPP (.3gp) • AMR (.amr)                                                                                                | • 3GPP (.3gp) • AMR (.amr)                                                                                                           | 4.75 to 12.2 kbps sampled @ 8kHz                                                                                                                                                                                                                      |
| AMR-WB                           | YES          | YES          | • 3GPP (.3gp) • AMR (.amr)                                                                                                | • 3GPP (.3gp) • AMR (.amr)                                                                                                           | 9 rates from 6.60 kbit/s to 23.85 kbit/s sampled @ 16kHz                                                                                                                                                                                              |
| FLAC                             | Android 4.1+ | Android 3.1+ | • FLAC (.flac) • MPEG-4 (.mp4, .m4a, Android 10+) • Matroska (.mkv)                                                       |                                                                                                                                      | Mono/Stereo (no multichannel). Sample rates up to 48 kHz (but up to 44.1 kHz is recommended on devices with 44.1 kHz output, as the 48 to 44.1 kHz downsampler does not include a low-pass filter). 16-bit recommended; no dither applied for 24-bit. |
| MIDI                             |              | YES          | • Type 0 and 1 (.mid, .xmf, .mxmf) • RTTTL/RTX (.rtttl, .rtx) • OTA (.ota) • iMelody (.imy)                               |                                                                                                                                      | MIDI Type 0 and 1. DLS Version 1 and 2. XMF and Mobile XMF. Support for ringtone formats RTTTL/RTX, OTA, and iMelody                                                                                                                                  |
| MP3                              |              | YES          | • MP3 (.mp3) • MPEG-4 (.mp4, .m4a, Android 10+) • Matroska (.mkv, Android 10+)                                            |                                                                                                                                      | Mono/Stereo 8-320Kbps constant (CBR) or variable bit-rate (VBR)                                                                                                                                                                                       |
| Opus                             | Android 10+  | Android 5.0+ | • Ogg (.ogg) • MPEG-4 (.mp4) • Matroska (.mkv)                                                                            | • Ogg (.ogg) •[WebM](http://www.webmproject.org/)(.webm)                                                                             |                                                                                                                                                                                                                                                       |
| PCM/WAVE                         | Android 4.1+ | YES          | WAVE (.wav)                                                                                                               |                                                                                                                                      | 8- and 16-bit linear PCM (rates up to limit of hardware). Sampling rates for raw PCM recordings at 8000, 16000 and 44100 Hz.                                                                                                                          |
| Vorbis                           |              | YES          | • Ogg (.ogg) • Matroska (.mkv, Android 4.0+) • MPEG-4 (.mp4, .m4a, Android 10+)                                           | •[WebM](http://www.webmproject.org/)(.webm)                                                                                          |                                                                                                                                                                                                                                                       |

## Video support

### Video formats

|             Format              |   Encoder    |    Decoder     |                                                               File Types Container Formats                                                               ||                                      Details                                      |
|             Format              |   Encoder    |    Decoder     |                                                  Extractor                                                  |                    Muxer                    |                                      Details                                      |
|---------------------------------|--------------|----------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------|-----------------------------------------------------------------------------------|
| H.263                           | YES          | YES            | • 3GPP (.3gp) • MPEG-4 (.mp4) • Matroska (.mkv)                                                             | • 3GPP (.3gp) • MPEG-4 (.mp4)               | Support for H.263 is optional in Android 7.0+                                     |
| H.264 AVC Baseline Profile (BP) | Android 3.0+ | YES            | • 3GPP (.3gp) • MPEG-4 (.mp4) • MPEG-TS (.ts, AAC audio only, not seekable, Android 3.0+) • Matroska (.mkv) | • 3GPP (.3gp) • MPEG-4 (.mp4)               |                                                                                   |
| H.264 AVC Main Profile (MP)     | Android 6.0+ | YES            | • 3GPP (.3gp) • MPEG-4 (.mp4) • MPEG-TS (.ts, AAC audio only, not seekable, Android 3.0+) • Matroska (.mkv) | • 3GPP (.3gp) • MPEG-4 (.mp4)               | The decoder is required, the encoder is recommended.                              |
| H.265 HEVC                      |              | Android 5.0+   | • MPEG-4 (.mp4) • Matroska (.mkv)                                                                           | • MPEG-4 (.mp4)                             | Main Profile Level 3 for mobile devices and Main Profile Level 4.1 for Android TV |
| MPEG-4 SP                       |              | YES            | • MPEG-4 (.mp4)                                                                                             | • MPEG-4 (.mp4)                             |                                                                                   |
| VP8                             | Android 4.3+ | Android 2.3.3+ | •[WebM](http://www.webmproject.org/)(.webm) • Matroska (.mkv, Android 4.0+)                                 | •[WebM](http://www.webmproject.org/)(.webm) | Streamable only in Android 4.0 and above                                          |
| VP9                             |              | Android 4.4+   | •[WebM](http://www.webmproject.org/)(.webm) • Matroska (.mkv) • MPEG-4 (.mp4)                               | •[WebM](http://www.webmproject.org/)(.webm) |                                                                                   |
| AV1                             | Android 14+  | Android 10+    | • MPEG-4 (.mp4) • Matroska (.mkv)                                                                           | • MPEG-4 (.mp4)                             | Encoder and decoder are mandatory beginning with Android 14.                      |
| APV                             | Android 16+  | Android 16+    | • MPEG-4 (.mp4)                                                                                             | • MPEG-4 (.mp4)                             | Encoder and decoder are mandatory beginning with Android 16.                      |

### Video encoding recommendations

The table below lists the Android media framework video encoding profiles and parameters recommended for playback using the H.264 Baseline Profile codec. The same recommendations apply to the Main Profile codec, which is only available in Android 6.0 and later.

|                  | SD(Low quality) | SD(High quality) | HD 720p(N/A on all devices) |
| Video resolution |  176 x 144 px   |   480 x 360 px   |        1280 x 720 px        |
| Video frame rate |     12 fps      |      30 fps      |           30 fps            |
|  Video bitrate   |     56 Kbps     |     500 Kbps     |           2 Mbps            |
|   Audio codec    |     AAC-LC      |      AAC-LC      |           AAC-LC            |
|  Audio channels  |    1 (mono)     |    2 (stereo)    |         2 (stereo)          |
|  Audio bitrate   |     24 Kbps     |     128 Kbps     |          192 Kbps           |
|------------------|-----------------|------------------|-----------------------------|

The table below lists the Android media framework video encoding profiles and parameters recommended for playback using the VP8 media codec.

|                  | SD(Low quality) | SD(High quality) | HD 720p(N/A on all devices) | HD 1080p(N/A on all devices) |
| Video resolution |  320 x 180 px   |   640 x 360 px   |        1280 x 720 px        |        1920 x 1080 px        |
| Video frame rate |     30 fps      |      30 fps      |           30 fps            |            30 fps            |
|  Video bitrate   |    800 Kbps     |      2 Mbps      |           4 Mbps            |           10 Mbps            |
|------------------|-----------------|------------------|-----------------------------|------------------------------|

### Video decoding recommendations

Device implementations must support dynamic video resolution and frame rate switching through the standard Android APIs within the same stream for all VP8, VP9, H.264, and H.265 codecs in real time and up to the maximum resolution supported by each codec on the device.

Implementations that support the Dolby Vision decoder must follow these guidelines:

- Provide a Dolby Vision-capable extractor.
- Properly display Dolby Vision content on the device screen or on a standard video output port (e.g., HDMI).
- Set the track index of backward-compatible base-layer(s) (if present) to be the same as the combined Dolby Vision layer's track index.

### Video streaming requirements

For video content that is streamed over HTTP or RTSP, there are additional requirements:

- For 3GPP and MPEG-4 containers, the`moov`atom must precede any`mdat`atoms, but must succeed the`ftyp`atom.
- For 3GPP, MPEG-4, and WebM containers, audio and video samples corresponding to the same time offset may be no more than 500 KB apart. To minimize this audio/video drift, consider interleaving audio and video in smaller chunk sizes.

## Image support

|         Format          |                             Encoder                             |                              Decoder                               |                                 Details                                 | File Types Container Formats |
|-------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------|
| BMP                     |                                                                 | YES                                                                |                                                                         | BMP (.bmp)                   |
| GIF                     |                                                                 | YES                                                                |                                                                         | GIF (.gif)                   |
| JPEG                    | YES                                                             | YES                                                                | Base+progressive                                                        | JPEG (.jpg)                  |
| PNG                     | YES                                                             | YES                                                                |                                                                         | PNG (.png)                   |
| WebP                    | Android 4.0+ Lossless: Android 10+ Transparency: Android 4.2.1+ | Android 4.0+ Lossless: Android 4.2.1+ Transparency: Android 4.2.1+ | Lossless encoding can be achieved on Android 10 using a quality of 100. | WebP (.webp)                 |
| HEIF                    |                                                                 | Android 8.0+                                                       |                                                                         | HEIF (.heic; .heif)          |
| AVIF (baseline profile) | Android 14+                                                     | Android 14+                                                        | Encoder and decoder are mandatory beginning with Android 14.            | AVIF (.avif)                 |

## Network protocols

The following network protocols are supported for audio and video playback:

- RTSP (RTP, SDP)
- HTTP/HTTPS progressive streaming
- HTTP/HTTPS live streaming[draft protocol](http://tools.ietf.org/html/draft-pantos-http-live-streaming):
  - MPEG-2 TS media files only
  - Protocol version 3 Android 4.0 and above
  - Protocol version 2 Android 3.x
  - Not supported before Android 3.0

**Note:**HTTPS is not supported before Android 3.1.

## HDR video formats

OEMs can enable any HDR format they choose with the Android HDR architecture, which provides the core needs of HDR formats: 10-bit buffers, metadata (static, dynamic, and none), transfer function, and color space handling.

To ensure consistency for developers and address key HDR use cases, we require OEMs to support a few base formats on devices that support HDR:

- For professional content playback, such as streaming movies, we require HDR10.
- For user-generated content capture and playback, we require HLG10 to provide a consistent experience across Android devices.

OEMs that add HDR support must support these formats, but can also support additional formats like HDR10+ or Dolby Vision.

|      Format      | Transfer Function | Metadata | Codec | Bit Depth |
|------------------|-------------------|----------|-------|-----------|
| HLG10            | HLG               | No       | HEVC  | 10-bit    |
| HDR10            | PQ                | Static   | HEVC  | 10-bit    |
| HDR10+           | PQ                | Static   | HEVC  | 10-bit    |
| Dolby Vision 8.4 | HLG               | Dynamic  | HEVC  | 10-bit    |

### Format handling recommendations

<br />

|----------------|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Capture format | Upload format               | Delivery format                                                                                                                                                                                                    |
| HLG            | App Backend support HDR HLG | Devices supporting HDR (HLG): HLG Devices support HDR (no HLG support only PQ): SDR (Tone map from HLG to SDR in the backend) Devices that don't do not support HDR: SDR (Tone map from HLG to SDR in the backend) |

Use case 2: Native camera capture or import from user's gallery (App backend supports HDR)

|----------------|--------------------------------------------------------------------------------------|---------------------------------|
| Capture format | Upload format                                                                        | Delivery format                 |
| HLG            | HLG                                                                                  | Same as in-app capture use case |
| HDR10+         | HLG Tone map from HDR10+ (PQ) to HLG before upload using transformer APIs            | Same as in-app capture use case |
| DV8.4          | HLG (DV8.4 uses HLG and bitstream will behave as HLG hence no tone mapping required) | Same as in-app capture use case |

Use case 3: App backend does not support HDR

|----------------|-------------------------------------------------------------------|-----------------|
| Capture format | Upload format                                                     | Delivery format |
| Any format     | SDR Tone map from HLG to SDR before upload using transformer APIs | SDR             |