---
title: https://developer.android.com/media/media3/exoplayer/glossary
url: https://developer.android.com/media/media3/exoplayer/glossary
source: md.txt
---

## General - Media

ABR
:   Adaptive Bitrate. An ABR algorithm is an algorithm that selects between a number of[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)during playback, where each track presents the same media but at different bitrates.

Adaptive streaming
:   In adaptive streaming, multiple[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)are available that present the same media at different bitrates. The selected track is chosen dynamically during playback using an[ABR](https://developer.android.com/media/media3/exoplayer/glossary#abr)algorithm.

Access unit
:   A data item within a media[container](https://developer.android.com/media/media3/exoplayer/glossary#container). Generally refers to a small piece of the compressed media bitstream that can be decoded and presented to the user (a video picture or fragment of playable audio).

AV1

:   AOMedia Video 1[codec](https://developer.android.com/media/media3/exoplayer/glossary#codec).

    For more information, see the[Wikipedia page](https://en.wikipedia.org/wiki/AV1).

AVC

:   Advanced Video Coding, also known as the H.264 video[codec](https://developer.android.com/media/media3/exoplayer/glossary#codec).

    For more information, see the[Wikipedia page](https://en.wikipedia.org/wiki/Advanced_Video_Coding).

Codec

:   This term is overloaded and has multiple meanings depending on the context. The two following definitions are the most-commonly used:

    - Hardware or software component for encoding or decoding[access units](https://developer.android.com/media/media3/exoplayer/glossary#access-unit).
    - Audio or video sample format specification.

Container

:   A media container format such as MP4 and Matroska. Such formats are called container formats because they contain one or more[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)of media, where each track uses a particular[codec](https://developer.android.com/media/media3/exoplayer/glossary#codec)(for example, AAC audio and H.264 video in an MP4 file). Note that some media formats are both a container format and a codec (for example, MP3).

DASH

:   Dynamic[Adaptive Streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming)over HTTP. An industry driven adaptive streaming protocol. It is defined by ISO/IEC 23009, which can be found on the[ISO Publicly Available Standards page](https://standards.iso.org/ittf/PubliclyAvailableStandards/).

DRM

:   Digital Rights Management.

    For more information, see the[Wikipedia page](https://en.wikipedia.org/wiki/Digital_rights_management).

Gapless playback

:   Process by which the end of a[track](https://developer.android.com/media/media3/exoplayer/glossary#track)and/or the beginning of the next track are skipped to avoid a silent gap between tracks.

    For more information, see the[Wikipedia page](https://en.wikipedia.org/wiki/Gapless_playback).

HEVC

:   High Efficiency Video Coding, also known as the H.265 video[codec](https://developer.android.com/media/media3/exoplayer/glossary#codec).

HLS

:   HTTP Live Streaming. Apple's[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming)protocol.

    For more information, see the[Apple documentation](https://developer.apple.com/streaming/).

Manifest

:   A file that defines the structure and location of media in[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming)protocols. Examples include[DASH](https://developer.android.com/media/media3/exoplayer/glossary#dash)[MPD](https://developer.android.com/media/media3/exoplayer/glossary#mpd)files,[HLS](https://developer.android.com/media/media3/exoplayer/glossary#hls)multivariant playlist files and[Smooth Streaming](https://developer.android.com/media/media3/exoplayer/glossary#smooth-streaming)manifest files. Not to be confused with an AndroidManifest XML file.

MPD

:   Media Presentation Description. The[manifest](https://developer.android.com/media/media3/exoplayer/glossary#manifest)file format used in the[DASH](https://developer.android.com/media/media3/exoplayer/glossary#dash)[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming)protocol.

PCM

:   Pulse-Code Modulation.

    For more information, see the[Wikipedia page](https://en.wikipedia.org/wiki/Pulse-code_modulation).

Smooth Streaming

:   Microsoft's[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming)protocol.

    For more information, see the[Microsoft documentation](https://www.iis.net/downloads/microsoft/smooth-streaming).

Track

:   A single audio, video, text, or metadata stream within a piece of media. A media file will often contain multiple tracks. For example, a video track and an audio track in a video file, or multiple audio tracks in different languages. In[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming), there are also multiple tracks containing the same content at different bitrates.

## General - Android

AudioTrack

:   An Android API for playing audio.

    For more information, see the[Javadoc](https://developer.android.com/reference/android/media/AudioTrack).

CDM

:   Content Decryption Module. A component in the Android platform responsible for decrypting[DRM](https://developer.android.com/media/media3/exoplayer/glossary#drm)-protected content. CDMs are accessed using Android's[`MediaDrm`](https://developer.android.com/media/media3/exoplayer/glossary#mediadrm)API.

    For more information, see the[Javadoc](https://developer.android.com/reference/android/media/MediaDrm).

IMA

:   Interactive Media Ads. IMA is an SDK that makes it easy to integrate multimedia ads into an app.

    For more information, see the[IMA documentation](https://developers.google.com/interactive-media-ads).

MediaCodec

:   An Android API for accessing media[codecs](https://developer.android.com/media/media3/exoplayer/glossary#codec)(i.e. encoder and decoder components) in the platform.

    For more information, see the[Javadoc](https://developer.android.com/reference/android/media/MediaCodec).

MediaDrm

:   An Android API for accessing[CDMs](https://developer.android.com/media/media3/exoplayer/glossary#cdm)in the platform.

    For more information, see the[Javadoc](https://developer.android.com/reference/android/media/MediaDrm).

Audio offload

:   The ability to send compressed audio directly to a digital signal processor (DSP) provided by the device. Audio offload functionality is useful for low power audio playback.

    For more information, see the[Android interaction documentation](https://source.android.com/devices/tv/multimedia-tunneling).

Passthrough

:   The ability to send compressed audio directly over HDMI, without decoding it first. This is for example used to play 5.1 surround sound on an Android TV.

    For more information, see the[Android interaction documentation](https://source.android.com/devices/tv/multimedia-tunneling).

Surface

:   See the[Javadoc](https://developer.android.com/reference/android/view/Surface)and the[Android graphics documentation](https://source.android.com/devices/graphics/arch-sh).

Tunneling

:   Process by which the Android framework receives compressed video and either compressed or[PCM](https://developer.android.com/media/media3/exoplayer/glossary#pcm)audio data and assumes the responsibility for decoding, synchronizing and rendering it, taking over some tasks usually handled by the application. Tunneling may improve audio-to-video (AV) synchronization, may smooth video playback and can reduce the load on the application processor. It is mostly used on Android TVs.

    For more information, see the[Android interaction documentation](https://source.android.com/devices/tv/multimedia-tunneling)and the[ExoPlayer article](https://medium.com/google-exoplayer/tunneled-video-playback-in-exoplayer-84f084a8094d).

## ExoPlayer

![ExoPlayer architecture overview](https://developer.android.com/static/guide/topics/media/exoplayer/images/glossary-exoplayer-architecture.png)

![ExoPlayer rendering overview](https://developer.android.com/static/guide/topics/media/exoplayer/images/glossary-rendering-architecture.png)

BandwidthMeter

:   Component that estimates the network bandwidth, for example by listening to data transfers. In[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming), bandwidth estimates can be used to select between different bitrate[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)during playback.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/upstream/BandwidthMeter).

DataSource

:   Component for requesting data (which may be over HTTP, from a local file, etc).

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/datasource/DataSource).

Extractor

:   Component that parses a media[container](https://developer.android.com/media/media3/exoplayer/glossary#container)format, outputting[track](https://developer.android.com/media/media3/exoplayer/glossary#track)information and individual[access units](https://developer.android.com/media/media3/exoplayer/glossary#access-unit)belonging to each track suitable for consumption by a decoder.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/extractor/Extractor).

LoadControl

:   Component that decides when to start and stop loading, and when to start playback.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/LoadControl).

MediaSource

:   Provides high-level information about the structure of media (as a[`Timeline`](https://developer.android.com/media/media3/exoplayer/glossary#timeline)) and creates[`MediaPeriod`](https://developer.android.com/media/media3/exoplayer/glossary#mediaperiod)instances (corresponding to periods of the`Timeline`) for playback.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/MediaSource).

MediaPeriod

:   Loads a single piece of media (such as an audio file, an ad, content interleaved between two ads, etc.), and allows the loaded media to be read (typically by[`Renderers`](https://developer.android.com/media/media3/exoplayer/glossary#renderer)). The decisions about which[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)within the media are loaded and when loading starts and stops are made by the[`TrackSelector`](https://developer.android.com/media/media3/exoplayer/glossary#trackselector)and the[`LoadControl`](https://developer.android.com/media/media3/exoplayer/glossary#loadcontrol)respectively.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/MediaPeriod).

Renderer

:   Component that reads, decodes, and renders media samples.[`Surface`](https://developer.android.com/media/media3/exoplayer/glossary#surface)and[`AudioTrack`](https://developer.android.com/media/media3/exoplayer/glossary#audiotrack)are the standard Android platform components to which video and audio data are rendered.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/Renderer).

Timeline

:   Represents the structure of media, from simple cases like a single media file through to complex compositions of media such as playlists and streams with inserted ads.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/common/Timeline).

TrackGroup

:   Group containing one or more representations of the same video, audio, or text content, normally at different bitrates for[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming).

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/common/TrackGroup).

TrackSelection

:   A selection consisting of a static subset of[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)from a[`TrackGroup`](https://developer.android.com/media/media3/exoplayer/glossary#trackgroup)and a possibly varying selected track from the subset. For[adaptive streaming](https://developer.android.com/media/media3/exoplayer/glossary#adaptive-streaming), the`TrackSelection`is responsible for selecting the appropriate track whenever a new media chunk starts being loaded.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/common/TrackSelection).

TrackSelector

:   Selects[tracks](https://developer.android.com/media/media3/exoplayer/glossary#track)for playback. Given track information for the[`MediaPeriod`](https://developer.android.com/media/media3/exoplayer/glossary#mediaperiod)to be played, along with the capabilities of the player's[`Renderers`](https://developer.android.com/media/media3/exoplayer/glossary#renderer), a`TrackSelector`will generate a[`TrackSelection`](https://developer.android.com/media/media3/exoplayer/glossary#trackselection)for each`Renderer`.

    For more information, see the component[Javadoc](https://developer.android.com/reference/androidx/media3/exoplayer/trackselection/TrackSelector).