---
title: https://developer.android.com/media/media3/exoplayer/rtsp
url: https://developer.android.com/media/media3/exoplayer/rtsp
source: md.txt
---

ExoPlayer supports both live and on demand RTSP. Supported sample formats and
network types are listed below.

### Supported sample formats

- H264 (the SDP media description must include SPS/PPS data in the fmtp attribute for decoder initialization).
- AAC (with ADTS bitstream).
- AC3.

> [!NOTE]
> **Note:** Please comment on [this issue](https://github.com/google/ExoPlayer/issues/9210) to request support for additional sample formats.

### Supported network types

- RTP over UDP unicast (multicast is not supported).
- Interleaved RTSP, RTP over RTSP using TCP.

## Using MediaItem

To play an RTSP stream, you need to depend on the RTSP module.

### Kotlin

```kotlin
implementation("androidx.media3:media3-exoplayer-rtsp:1.9.2")
```

### Groovy

```groovy
implementation "androidx.media3:media3-exoplayer-rtsp:1.9.2"
```

You can then create a `MediaItem` for an RTSP URI and pass it to the player.

### Kotlin

```kotlin
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(rtspUri))
// Prepare the player.
player.prepare()
```

### Java

```java
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media item to be played.
player.setMediaItem(MediaItem.fromUri(rtspUri));
// Prepare the player.
player.prepare();
```

### Authentication

ExoPlayer supports playback with RTSP BASIC and DIGEST authentication. To play
protected RTSP content, the `MediaItem`'s URI must be configured with the
authentication info. Specifically, the URI should be of the form
`rtsp://<username>:<password>@<host address>`.

## Using RtspMediaSource

For more customization options, you can create an `RtspMediaSource` and pass it
directly to the player instead of a `MediaItem`.

### Kotlin

```kotlin
// Create an RTSP media source pointing to an RTSP uri.
val mediaSource: MediaSource =
  RtspMediaSource.Factory().createMediaSource(MediaItem.fromUri(rtspUri))
// Create a player instance.
val player = ExoPlayer.Builder(context).build()
// Set the media source to be played.
player.setMediaSource(mediaSource)
// Prepare the player.
player.prepare()
```

### Java

```java
// Create an RTSP media source pointing to an RTSP uri.
MediaSource mediaSource =
    new RtspMediaSource.Factory().createMediaSource(MediaItem.fromUri(rtspUri));
// Create a player instance.
ExoPlayer player = new ExoPlayer.Builder(context).build();
// Set the media source to be played.
player.setMediaSource(mediaSource);
// Prepare the player.
player.prepare();
```

## Using RTSP behind a NAT (RTP/TCP support)

ExoPlayer uses UDP as the default protocol for RTP transport.

When streaming RTSP behind a NAT layer, the NAT might not be able to forward the
incoming RTP/UDP packets to the device. This occurs if the NAT lacks the
necessary UDP port mapping. If ExoPlayer detects there have not been incoming
RTP packets for a while and the playback has not started yet, ExoPlayer tears
down the current RTSP playback session, and retries playback using RTP-over-RTSP
(transmitting RTP packets using the TCP connection opened for RTSP).

The timeout for retrying with TCP can be customized by calling the method
`RtspMediaSource.Factory.setTimeoutMs()`. For example, if the timeout is set to
four seconds, the player will retry with TCP after four seconds of UDP
inactivity.

Setting the timeout also affects the end-of-stream detection logic. That is,
ExoPlayer will report the playback has ended if nothing is received for the
duration of the set timeout. Setting this value too small may lead to an early
end-of-stream signal under poor network conditions.

RTP/TCP offers better compatibility under some network setups. You can configure
ExoPlayer to use RTP/TCP by default with
`RtspMediaSource.Factory.setForceUseRtpTcp()`.

### Passing a custom SocketFactory

Custom `SocketFactory` instances can be useful when particular routing is
required (for example, when RTSP traffic needs to pass a specific interface, or the
socket needs additional connectivity flags).

By default, `RtspMediaSource` will use Java's standard socket factory
(`SocketFactory.getDefault()`) to create connections to the remote endpoints.
This behavior can be overridden using
`RtspMediaSource.Factory.setSocketFactory()`.

### Kotlin

```kotlin
// Create an RTSP media source pointing to an RTSP uri and override the socket
// factory.
val mediaSource: MediaSource =
  RtspMediaSource.Factory()
    .setSocketFactory(socketFactory)
    .createMediaSource(MediaItem.fromUri(rtspUri))
```

### Java

```java
// Create an RTSP media source pointing to an RTSP uri and override the socket
// factory.
MediaSource mediaSource =
    new RtspMediaSource.Factory()
        .setSocketFactory(socketFactory)
        .createMediaSource(MediaItem.fromUri(rtspUri));
```