---
title: https://developer.android.com/media/platform/xhe-aac-encoding
url: https://developer.android.com/media/platform/xhe-aac-encoding
source: md.txt
---

Starting in Android 17 QPR1 (API level 37.1 or
`Build.VERSION_CODES_FULL.CINNAMON_BUN_1`), Android introduces platform support
for [Extended High Efficiency Advanced Audio Coding (xHE-AAC)](https://www.iis.fraunhofer.de/en/ff/amm/broadcast-streaming/xheaac.html)
encoding.

Defined in [ISO/IEC 23003-3 (MPEG-D USAC)](https://www.iso.org/standard/76385.html) and
[ISO/IEC 23003-4 (MPEG-D DRC)](https://www.iso.org/standard/89036.html), xHE-AAC combines Unified Speech and
Audio Coding with mandatory loudness normalization and built-in dynamic range
control. While xHE-AAC *decoding* has been supported and mandated by the
[Android Compatibility Definition Document (CDD)](https://source.android.com/docs/compatibility/cdd) across multiple
platform versions, the addition of an xHE-AAC **encoder**
(`c2.android.xheaac.encoder` and OEM hardware implementations) lets you record
low-bitrate voice and audio messages, live audio streams, and communication
payloads with superior speech clarity and consistent volume across devices.

## Benefits of xHE-AAC

Traditional voice recording in Android messaging apps typically uses the older
AAC-LC (AAC Low Complexity) at 28 kbps. At low bitrates (\<32 kbps), AAC-LC
exhibits noticeable band-limiting artifacts, fuzzy speech quality, and
suboptimal compression efficiency. For end users, this results in muffled,
tinny audio where consonants are hard to distinguish, requiring listeners to
replay messages or strain to understand speech in noisy environments.
Additionally, inconsistent volume levels across voice clips force users to
frequently adjust device volume.

xHE-AAC overcomes these limitations by applying more advanced audio coding
algorithms, for example dynamically switching between dedicated speech coding
and general audio coding tools while extending frequency range with enhanced
Spectral Band Replication (eSBR) and providing parametric stereo coding
capability with very little additional coding overhead.

Built-in MPEG-D DRC provides mandatory loudness control for xHE-AAC to play
back content at a consistent volume and offers dynamic range control processing
to provide the best possible user experience for listening on any platform and
in any environment.

### Target use cases

- **Rich Communication Services (RCS) and voice messaging:** Complies with **GSMA RCC.71 Universal Profile version 3.1** and later, which mandates xHE-AAC for low-bitrate audio messaging.
- **Live audio streaming and podcasts:** Delivers resilient audio quality over degraded mobile or satellite network connections.

## Platform availability (API level 37.1+)

Platform xHE-AAC encoding support requires **API level 37.1**
(`Build.VERSION.SDK_INT_FULL >= Build.VERSION_CODES_FULL.CINNAMON_BUN_1` /
SDK `3700001` or higher).

> [!NOTE]
> **Note:** While the software xHE-AAC encoder component (`c2.android.xheaac.encoder`) was initially included in Android 17 (API level 37), a defect in the platform MP4/M4A container muxer prevented media players from scrubbing or seeking within recorded audio attachments. Full, seek-compatible MP4 muxing support was verified and re-enabled in **Android 17 QPR1 (API level 37.1 / `CINNAMON_BUN_1`)**.

## Query for xHE-AAC encoder support

You must not assume xHE-AAC encoding is available on every device
by calling [`MediaCodec.createByCodecName(...)`](https://developer.android.com/reference/android/media/MediaCodec#createByCodecName(java.lang.String))
with `"c2.android.xheaac.encoder"`.

- Some devices may provide a hardware-accelerated xHE-AAC encoder from the chipset vendor rather than the platform software encoder.
- Older OS releases or customized ROMs lack xHE-AAC encoding support.
- Before encoding an attachment for peer-to-peer messaging (such as RCS or chat), apps should also check if the receiving client advertises USAC/xHE-AAC decoding support (for example, using SDP capability discovery `profile-level-id=55` / `object=42`) to prevent interoperability failures on legacy receivers.

### Inspect MediaCodecList capabilities

To inspect whether the current device supports xHE-AAC
encoding, inspect the `profileLevels` of encoders supporting
`MediaFormat.MIMETYPE_AUDIO_AAC`:

### Kotlin

```kotlin
import android.media.MediaCodecInfo.CodecProfileLevel
import android.media.MediaCodecList
import android.media.MediaFormat
import android.os.Build

/**
 * Checks if the current device supports xHE-AAC audio encoding.
 */
fun isXheAacEncodingSupported(): Boolean {
    // Verify API Level >= 37.1 (CINNAMON_BUN_1 / SDK 3700001)
    if (Build.VERSION.SDK_INT_FULL < Build.VERSION_CODES_FULL.CINNAMON_BUN_1) {
        return false
    }

    val codecList = MediaCodecList(MediaCodecList.REGULAR_CODECS)
    for (codecInfo in codecList.codecInfos) {
        if (!codecInfo.isEncoder) continue

        if (MediaFormat.MIMETYPE_AUDIO_AAC in codecInfo.supportedTypes) {
            val capabilities =
                codecInfo.getCapabilitiesForType(MediaFormat.MIMETYPE_AUDIO_AAC)
            // Check if AACObjectXHE (42) is present in profileLevels
            val supportsXhe = capabilities.profileLevels.any { profileLevel ->
                profileLevel.profile == CodecProfileLevel.AACObjectXHE
            }
            if (supportsXhe) {
                return true
            }
        }
    }
    return false
}
```

### Java

```java
import android.media.MediaCodecInfo;
import android.media.MediaCodecInfo.CodecProfileLevel;
import android.media.MediaCodecList;
import android.media.MediaFormat;
import android.os.Build;

/**
 * Checks if the current device supports xHE-AAC audio encoding.
 */
public boolean isXheAacEncodingSupported() {
    // Verify API Level >= 37.1 (CINNAMON_BUN_1 / SDK 3700001)
    if (Build.VERSION.SDK_INT_FULL < Build.VERSION_CODES_FULL.CINNAMON_BUN_1) {
        return false;
    }

    MediaCodecList codecList = new MediaCodecList(MediaCodecList.REGULAR_CODECS);
    for (MediaCodecInfo codecInfo : codecList.getCodecInfos()) {
        if (!codecInfo.isEncoder()) continue;

        for (String type : codecInfo.getSupportedTypes()) {
            if (MediaFormat.MIMETYPE_AUDIO_AAC.equals(type)) {
                MediaCodecInfo.CodecCapabilities capabilities =
                        codecInfo.getCapabilitiesForType(MediaFormat.MIMETYPE_AUDIO_AAC);
                for (CodecProfileLevel profileLevel : capabilities.profileLevels) {
                    if (profileLevel.profile == CodecProfileLevel.AACObjectXHE) {
                        return true;
                    }
                }
            }
        }
    }
    return false;
}
```

## Configure and instantiate the xHE-AAC encoder

After you have verified xHE-AAC support, configure your `MediaFormat` with
`KEY_AAC_PROFILE` set to
[`MediaCodecInfo.CodecProfileLevel.AACObjectXHE`](https://developer.android.com/reference/android/media/MediaCodecInfo.CodecProfileLevel#AACObjectXHE)
(value `42`).

### Kotlin

```kotlin
fun setupXheAacEncoder(): MediaCodec? {
    if (!isXheAacEncodingSupported()) {
        return null
    }

    val mimeType = MediaFormat.MIMETYPE_AUDIO_AAC
    val sampleRate = 48000
    val channelCount = 1 // Mono voice recording
    val bitRate = 20000  // 20 kbps delivers superior speech clarity

    val format = MediaFormat.createAudioFormat(mimeType, sampleRate, channelCount).apply {
        setInteger(MediaFormat.KEY_BIT_RATE, bitRate)
        setInteger(MediaFormat.KEY_AAC_PROFILE, CodecProfileLevel.AACObjectXHE)
    }

    // Find the hardware or software encoder supporting this format and profile
    val codecList = MediaCodecList(MediaCodecList.REGULAR_CODECS)
    val encoderName = codecList.findEncoderForFormat(format) ?: return null
    val encoder = MediaCodec.createByCodecName(encoderName)
    encoder.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE)
    return encoder
}
```

### Java

```java
public MediaCodec setupXheAacEncoder() throws IOException {
    if (!isXheAacEncodingSupported()) {
        return null;
    }

    String mimeType = MediaFormat.MIMETYPE_AUDIO_AAC;
    int sampleRate = 48000;
    int channelCount = 1; // Mono voice recording
    int bitRate = 20000;  // 20 kbps delivers superior speech clarity

    MediaFormat format = MediaFormat.createAudioFormat(mimeType, sampleRate, channelCount);
    format.setInteger(MediaFormat.KEY_BIT_RATE, bitRate);
    format.setInteger(MediaFormat.KEY_AAC_PROFILE, CodecProfileLevel.AACObjectXHE);

    // Find the hardware or software encoder supporting this format and profile
    MediaCodecList codecList =
            new MediaCodecList(MediaCodecList.REGULAR_CODECS);
    String encoderName = codecList.findEncoderForFormat(format);
    if (encoderName == null) {
        return null;
    }

    MediaCodec encoder = MediaCodec.createByCodecName(encoderName);
    encoder.configure(format, null, null, MediaCodec.CONFIGURE_FLAG_ENCODE);
    return encoder;
}
```

### Supported software encoder limits (`c2.android.xheaac.encoder`)

When using the system-provided software xHE-AAC encoder
(`c2.android.xheaac.encoder`), the component advertises the following
capability limits:

- **Channel count:** Up to `2` channels (Mono / Stereo).
- **Sample rates:** `44100 Hz`, `48000 Hz`.
- **Bitrate range:** `12,000 bps` to `400,000 bps` (12 kbps -- 400 kbps).
- **Container muxing:** Compatible with raw MP4A elementary streams and platform MP4/M4A container muxing (`MediaMuxer.OutputFormat.MUXER_OUTPUT_MPEG_4`).