---
title: https://developer.android.com/media/media3/exoplayer/supported-formats
url: https://developer.android.com/media/media3/exoplayer/supported-formats
source: md.txt
---

# Supported formats

When defining the formats that ExoPlayer supports, it's important to note that "media formats" are defined at multiple levels. From the lowest level to the highest, these are:

- The format of the individual media samples (such as a frame of video or a frame of audio). These are*sample formats*. Note that a typical video file will contain media in at least two sample formats; one for video (for example, H.264) and one for audio (for example, AAC).
- The format of the container that houses the media samples and associated metadata. These are*container formats*. A media file has a single container format (for example, MP4), which is commonly indicated by the file extension. Note that for some audio-only formats (for example, MP3), the sample and container formats may be the same.
- Adaptive streaming technologies such as DASH, SmoothStreaming and HLS. These are not media formats as such, however it's still necessary to define what level of support ExoPlayer provides.

The following sections define ExoPlayer's support at each level, from highest to lowest. The last two sections describe support for standalone subtitle formats and HDR video playback.

## Adaptive streaming

### DASH

ExoPlayer supports DASH with multiple container formats. Media streams must be demuxed, meaning that video, audio, and text must be defined in distinct`AdaptationSet`elements in the DASH manifest (CEA-608 is an exception as described in the table below). The contained audio and video sample formats must also be supported (see the[sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats)section for details).

|                 Feature                 | Supported |                                        Comments                                         |
|-----------------------------------------|-----------|-----------------------------------------------------------------------------------------|
| **Containers**                          |           |                                                                                         |
| FMP4                                    | YES       | Demuxed streams only                                                                    |
| WebM                                    | YES       | Demuxed streams only                                                                    |
| Matroska                                | YES       | Demuxed streams only                                                                    |
| MPEG-TS                                 | NO        | No support planned                                                                      |
| **Closed captions /** **subtitles**     |           |                                                                                         |
| TTML                                    | YES       | Raw, or embedded in FMP4 according to ISO/IEC 14496-30                                  |
| WebVTT                                  | YES       | Raw, or embedded in FMP4 according to ISO/IEC 14496-30                                  |
| CEA-608                                 | YES       | Embedded in FMP4 when signalled using SCTE Accessibility descriptors                    |
| CEA-708                                 | YES       | Embedded in FMP4 when signalled using SCTE Accessibility descriptors                    |
| **Metadata**                            |           |                                                                                         |
| EMSG metadata                           | YES       | Embedded in FMP4                                                                        |
| **Content protection**                  |           |                                                                                         |
| Widevine                                | YES       | "cenc" scheme: API 19+; "cbcs" scheme: API 25+                                          |
| PlayReady SL2000                        | YES       | Android TV, "cenc" scheme only                                                          |
| ClearKey                                | YES       | API 21+, "cenc" scheme only                                                             |
| **Ad insertion**                        |           |                                                                                         |
| Multi-period playback                   | YES       |                                                                                         |
| Server-guided ad insertion (xlinks)     | NO        |                                                                                         |
| IMA server-side and client-side ads     | YES       | [Ad insertion guide](https://developer.android.com/media/media3/exoplayer/ad-insertion) |
| **Live playback**                       |           |                                                                                         |
| Regular live playback                   | YES       |                                                                                         |
| Ultra low-latency CMAF live playback    | YES       |                                                                                         |
| **Common Media Client Data** **(CMCD)** | YES       | [CMCD integration guide](https://developer.android.com/media/media3/exoplayer/cmcd)     |

### SmoothStreaming

ExoPlayer supports SmoothStreaming with the FMP4 container format. Media streams must be demuxed, meaning that video, audio, and text must be defined in distinct StreamIndex elements in the SmoothStreaming manifest. The contained audio and video sample formats must also be supported (see the[sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats)section for details).

|               Feature               | Supported |                                       Comments                                       |
|-------------------------------------|-----------|--------------------------------------------------------------------------------------|
| **Containers**                      |           |                                                                                      |
| FMP4                                | YES       | Demuxed streams only                                                                 |
| **Closed captions/subtitles**       |           |                                                                                      |
| TTML                                | YES       | Embedded in FMP4                                                                     |
| **Content protection**              |           |                                                                                      |
| PlayReady SL2000                    | YES       | Android TV only                                                                      |
| **Live playback**                   |           |                                                                                      |
| Regular live playback               | YES       |                                                                                      |
| **Common Media Client Data (CMCD)** | YES       | [Integration Guide](https://developer.android.com/guide/topics/media/exoplayer/cmcd) |

### HLS

ExoPlayer supports HLS with multiple container formats. The contained audio and video sample formats must also be supported (see the[sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats)section for details). We strongly encourage HLS content producers to generate high quality HLS streams, as described[in this blog post](https://medium.com/google-exoplayer/hls-playback-in-exoplayer-a33959a47be7).

|                  Feature                   | Supported |                                        Comments                                         |
|--------------------------------------------|-----------|-----------------------------------------------------------------------------------------|
| **Containers**                             |           |                                                                                         |
| MPEG-TS                                    | YES       |                                                                                         |
| FMP4/CMAF                                  | YES       |                                                                                         |
| ADTS (AAC)                                 | YES       |                                                                                         |
| MP3                                        | YES       |                                                                                         |
| **Closed captions /** **subtitles**        |           |                                                                                         |
| CEA-608                                    | YES       |                                                                                         |
| CEA-708                                    | YES       |                                                                                         |
| WebVTT                                     | YES       |                                                                                         |
| **Metadata**                               |           |                                                                                         |
| ID3                                        | YES       |                                                                                         |
| SCTE-35                                    | NO        |                                                                                         |
| **Content protection**                     |           |                                                                                         |
| AES-128                                    | YES       |                                                                                         |
| Sample AES-128                             | NO        |                                                                                         |
| Widevine                                   | YES       | API 19+ ("cenc" scheme) and 25+ ("cbcs" scheme)                                         |
| PlayReady SL2000                           | YES       | Android TV only                                                                         |
| **Server control**                         |           |                                                                                         |
| Delta updates                              | YES       |                                                                                         |
| Blocking playlist reload                   | YES       |                                                                                         |
| Blocking load of preload hints             | YES       | Except for byteranges with undefined lengths                                            |
| **Ad insertion**                           |           |                                                                                         |
| Server-guided ad insertion (Interstitials) | Partially | Only VOD with`X-ASSET-URI`. Live streams and`X-ASSET-LIST`will be added later.          |
| IMA server-side and client-side ads        | YES       | [Ad insertion guide](https://developer.android.com/media/media3/exoplayer/ad-insertion) |
| **Live playback**                          |           |                                                                                         |
| Regular live playback                      | YES       |                                                                                         |
| Low-latency HLS (Apple)                    | YES       |                                                                                         |
| Low-latency HLS (Community)                | NO        |                                                                                         |
| **Common Media Client Data** **CMCD**      | YES       | [CMCD integration guide](https://developer.android.com/media/media3/exoplayer/cmcd)     |

## Progressive container formats

Streams in the following container formats can be played directly by ExoPlayer. The contained audio and video sample formats must also be supported (see the[Sample formats](https://developer.android.com/media/media3/exoplayer/supported-formats#sample-formats)section for details). For image container and format support, see[Images](https://developer.android.com/media/media3/exoplayer/images).

| Container format | Supported |                                                                                                        Comments                                                                                                         |
|------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MP4              | YES       |                                                                                                                                                                                                                         |
| M4A              | YES       |                                                                                                                                                                                                                         |
| FMP4             | YES       |                                                                                                                                                                                                                         |
| WebM             | YES       |                                                                                                                                                                                                                         |
| Matroska         | YES       |                                                                                                                                                                                                                         |
| MP3              | YES       | Some streams only seekable using constant bitrate seeking\*\*                                                                                                                                                           |
| Ogg              | YES       | Containing Vorbis, Opus and FLAC                                                                                                                                                                                        |
| WAV              | YES       |                                                                                                                                                                                                                         |
| MPEG-TS          | YES       |                                                                                                                                                                                                                         |
| MPEG-PS          | YES       |                                                                                                                                                                                                                         |
| FLV              | YES       | Not seekable\*                                                                                                                                                                                                          |
| ADTS (AAC)       | YES       | Only seekable using constant bitrate seeking\*\*                                                                                                                                                                        |
| FLAC             | YES       | Using the[FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac)or the FLAC extractor in the[ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer)\*\*\* |
| AMR              | YES       | Only seekable using constant bitrate seeking\*\*                                                                                                                                                                        |

\* Seeking is unsupported because the container does not provide metadata (for example, a sample index) to allow a media player to perform a seek in an efficient way. If seeking is required, we suggest using a more appropriate container format.

\*\* These extractors have`FLAG_ENABLE_CONSTANT_BITRATE_SEEKING`flags for enabling approximate seeking using a constant bitrate assumption. This functionality is not enabled by default. The simplest way to enable this functionality for all extractors that support it is to use`DefaultExtractorsFactory.setConstantBitrateSeekingEnabled`, as described[here](https://developer.android.com/media/media3/exoplayer/customization#enabling-constant-bitrate-seeking).

\*\*\* The[FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac)extractor outputs raw audio, which can be handled by the framework on all API levels. The[ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer)FLAC extractor outputs FLAC audio frames and so relies on having a FLAC decoder (for example, a`MediaCodec`decoder that handles FLAC (required from API level 27), or the[FFmpeg library](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg)with FLAC enabled). The`DefaultExtractorsFactory`uses the extension extractor if the application was built with the[FLAC library](https://github.com/androidx/media/tree/release/libraries/decoder_flac). Otherwise, it uses the[ExoPlayer library](https://github.com/androidx/media/tree/release/libraries/exoplayer)extractor.

## RTSP

ExoPlayer supports both live and on demand RTSP. Supported sample formats and network types are listed below.

### Supported sample formats

- H264 (the SDP media description must include SPS/PPS data in the fmtp attribute for decoder initialization).
- AAC (with ADTS bitstream).
- AC3.

| **Note:** Please comment on[this issue](https://github.com/google/ExoPlayer/issues/9210)to request support for additional sample formats.

### Supported network types

- RTP over UDP unicast (multicast is not supported).
- Interleaved RTSP, RTP over RTSP using TCP.

## Sample formats

By default ExoPlayer uses Android's platform decoders. Hence the supported sample formats depend on the underlying platform rather than on ExoPlayer. Refer to[Supported media formats](https://developer.android.com/guide/topics/media/media-formats#core)for documentation on sample formats supported by Android devices. Note that individual devices may support additional formats beyond those listed.

In addition to Android's platform decoders, ExoPlayer can also make use of software decoder extensions. These must be manually built and included in projects that wish to make use of them. We currently provide software decoder libraries for[AV1](https://github.com/androidx/media/tree/release/libraries/decoder_av1),[VP9](https://github.com/androidx/media/tree/release/libraries/decoder_vp9),[FLAC](https://github.com/androidx/media/tree/release/libraries/decoder_flac),[Opus](https://github.com/androidx/media/tree/release/libraries/decoder_opus),[FFmpeg](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg),[MIDI](https://github.com/androidx/media/tree/release/libraries/decoder_midi),[IAMF](https://github.com/androidx/media/tree/release/libraries/decoder_iamf)and[MPEG-H](https://github.com/androidx/media/tree/release/libraries/decoder_mpegh).

### FFmpeg library

The[FFmpeg library](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg)supports decoding a variety of different audio sample formats. You can choose which decoders to include when building the library, as documented in the library's[README.md](https://github.com/androidx/media/tree/release/libraries/decoder_ffmpeg/README.md). The following table provides a mapping from audio sample format to the corresponding FFmpeg decoder name.

| Sample format | Decoder name(s) |
|---------------|-----------------|
| Vorbis        | vorbis          |
| Opus          | opus            |
| FLAC          | flac            |
| ALAC          | alac            |
| PCM μ-law     | pcm_mulaw       |
| PCM A-law     | pcm_alaw        |
| MP1, MP2, MP3 | mp3             |
| AMR-NB        | amrnb           |
| AMR-WB        | amrwb           |
| AAC           | aac             |
| AC-3          | ac3             |
| E-AC-3        | eac3            |
| DTS, DTS-HD   | dca             |
| TrueHD        | mlp truehd      |

## Images

ExoPlayer supports the following image formats. See[Image Loading Libraries](https://developer.android.com/media/media3/exoplayer/images#image-loading-libraries)for how to integrate with external libraries that may provide support for a different set of formats.

|   Image format    | Supported |                           Notes                            |
|-------------------|-----------|------------------------------------------------------------|
| BMP               | YES       |                                                            |
| GIF               | NO        | No Extractor support                                       |
| JPEG              | YES       |                                                            |
| JPEG Motion Photo | YES       | Still image and video supported                            |
| JPEG Ultra HDR    | YES       | Falls back to SDR before Android 14 or on non-HDR displays |
| PNG               | YES       |                                                            |
| WebP              | YES       |                                                            |
| HEIF/HEIC         | YES       |                                                            |
| HEIC Motion Photo | Partially | Only still image supported\*                               |
| AVIF (baseline)   | YES       | Decoded on Android 14+ only                                |

\* The video part of HEIC motion photos can be obtained with[MetadataRetriever](https://developer.android.com/media/media3/exoplayer/retrieving-metadata#motion-photos)and played as a standalone file.

## Standalone subtitle formats

ExoPlayer supports standalone subtitle files in a variety of formats. Subtitle files can be side-loaded as described on the[media items page](https://developer.android.com/guide/topics/media/exoplayer/media-items#sideloading-subtitle-tracks).

|     Container format      | Supported |          MIME type           |
|---------------------------|-----------|------------------------------|
| WebVTT                    | YES       | MimeTypes.TEXT_VTT           |
| TTML / SMPTE-TT           | YES       | MimeTypes.APPLICATION_TTML   |
| SubRip                    | YES       | MimeTypes.APPLICATION_SUBRIP |
| SubStationAlpha (SSA/ASS) | YES       | MimeTypes.TEXT_SSA           |

## HDR video playback

ExoPlayer handles extracting high dynamic range (HDR) video in various containers, including Dolby Vision in MP4 and HDR10+ in Matroska/WebM. Decoding and displaying HDR content depends on support from the Android platform and device. See[HDR Video Playback](https://source.android.com/devices/tech/display/hdr.html)to learn about checking for HDR decoding/display capabilities and limitations of HDR support across Android versions.

When playing an HDR stream that requires support for a particular codec profile, ExoPlayer's default`MediaCodec`selector will pick a decoder that supports that profile (if available), even if another decoder for the same MIME type that doesn't support that profile appears higher up the codec list. This can result in selecting a software decoder in cases where the stream exceeds the capabilities of a hardware decoder for the same MIME type.