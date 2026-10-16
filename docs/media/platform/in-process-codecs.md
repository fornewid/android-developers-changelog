---
title: https://developer.android.com/media/platform/in-process-codecs
url: https://developer.android.com/media/platform/in-process-codecs
source: md.txt
---

Starting in Android 17 (API level 37) and updated through Google Play System
Updates (Mainline APEX modules), Android introduces **in-process software
audio decoders** for compressed audio formats, including **Opus** and **AAC**.

By running audio decoders directly within the app's process rather than in a
separate sandboxed system process, apps can reduce audio decoding latency by
**approximately 40%**, reduce CPU utilization, and extend battery life during
continuous media playback, voice messaging, and gaming.

## Out-of-process versus in-process decoding

Historically, Android ran all platform software media decoders inside a
dedicated, sandboxed system daemon (`mediaswcodec`) to protect apps and the
OS from malformed media bitstreams. However, out-of-process sandboxing
introduces measurable performance overhead:

- **Inter-process communication (IPC) latency:** Every audio input frame queued to the decoder and every decoded PCM audio buffer returned requires cross-process Binder IPC serialization and context switching.
- **Shared memory overhead:** Inter-process buffer handoffs require shared-memory (`C2Buffer`) synchronization and cache management.
- **Scheduling contention:** Under heavy CPU load, thread scheduling contention between the app process and `mediaswcodec` can cause buffer starvation and audio stuttering in low-latency audio pipelines (such as DAWs, VoIP communication, and interactive games).

Running media decoders in-process directly resolves these performance
bottlenecks:

- **Eliminates IPC latency:** Bypasses Binder IPC transactions and context switches, reducing end-to-end decoding latency by approximately 40%.
- **Minimizes buffer overhead:** Passes audio buffers directly within the local app memory space without requiring cross-process shared memory mappings.
- **Prevents scheduling jitter:** Executes decoding on the app's own priority threads (such as realtime AAudio or Oboe threads), preventing audio dropouts and buffer underruns under heavy system load.

## Memory safety with Rust

Historically, Android isolated software decoders in a separate process
(`mediaswcodec`) because decoders process untrusted bitstreams from external
media files, making memory-corruption exploits (such as buffer overflows) a
major security concern.

Android can safely move software decoders directly into the calling app process
by implementing them in memory-safe languages like Rust or isolating them with
Lightweight Fault Isolation (LFI).

To safely eliminate out-of-process sandboxing overhead for **AAC**
(`c2.android.inproc.aac.decoder`), Android provides a decoder implemented in
**pure Rust** or protected by safe Rust Foreign Function Interface (FFI)
harnesses.

Rust is deemed secure for in-process decoding for the following reasons:

- **Compile-time memory safety:** Rust's strict ownership, borrowing, and lifetime checking ensure that memory can't be accessed after it is freed or mutated while shared.
- **Elimination of common vulnerabilities:** Rust completely prevents heap buffer overflows, stack smashes, out-of-bounds array reads and writes, use-after-free errors, and double-free vulnerabilities at compile time.
- **Zero runtime sandboxing tax:** Because memory safety is mathematically proven at compile time and verified through bounds checking, Rust decoders execute at native speed inside the app process without requiring page table transitions or hardware sandbox contexts.

## Memory safety with Lightweight Fault Isolation (LFI)

For complex legacy C/C++ audio decoders that have not yet been rewritten in
Rust---specifically the **Opus** decoder (`c2.android.inproc.opus.decoder`
powered by `libopus`)---Android provides in-process safety using
[Lightweight Fault Isolation (LFI)](https://llvm.org/docs/LFI.html).

LFI is considered secure for C/C++ decoders for the following reasons:

- **Hardware-guarded linear memory sandboxing:** LFI compiles the C/C++ codec library into WebAssembly-derived linear machine code confined to a hardware-guarded 4 GB linear memory slot.
- **Linux Memory Protection Keys (`pku`):** LFI uses Linux Memory Protection Keys (`pku` / `pkey_mprotect`) to partition address space permissions. The isolated library can't read or write memory outside its assigned 4 GB sandbox slot.
- **System call interception:** Zero host OS system calls (such as file I/O, network access, or process control) are permitted inside the sandbox. Any unsupported library call is routed to minimal dummy stubs (`lfi_stubs.c`).
- **Safe fault recovery:** If a malformed or adversarial Opus bitstream attempts an out-of-bounds read or write inside the linear sandbox, the LFI runtime traps the fault safely in userspace and returns a clean `C2_CORRUPTED` decoding error without crashing the host app.

### Supported architectures and devices for LFI

LFI requires no custom CPU hardware instructions and is supported on
**ARM64 (`aarch64`)** and **x86_64** processor architectures:

- **ARM64 (`aarch64`) devices:** Most consumer mobile devices---including mobile phones (such as Pixel devices with Google Tensor SoCs, Qualcomm Snapdragon, and MediaTek SoCs), foldables, tablets, and automotive infotainment units---run on ARM64 processors and support LFI in-process decoders.
- **x86_64 devices:** Android emulators running on developer workstations with Intel or AMD CPUs, as well as ChromeOS Chromebooks running Android apps using ARC (Android Runtime for ChromeOS), execute on x86_64 architectures and support LFI sandboxing.

> [!NOTE]
> **Note:** All in-process audio decoders (both Rust and LFI) report [`SECURITY_MODEL_MEMORY_SAFE`](https://developer.android.com/reference/android/media/MediaCodecInfo#SECURITY_MODEL_MEMORY_SAFE) when queried using [`MediaCodecInfo.getSecurityModel()`](https://developer.android.com/reference/android/media/MediaCodecInfo#getSecurityModel()).

## Available in-process audio decoders

| Audio format | MIME type | In-process component name | Implementation |
|---|---|---|---|
| **Opus** | `audio/opus` | `c2.android.inproc.opus.decoder` | C/C++ `libopus` with LFI |
| **AAC** | `audio/mp4a-latm` | `c2.android.inproc.aac.decoder` | Memory-safe Rust (`C2ApexAacDec`) |

> [!NOTE]
> **Note:** By default, all in-process audio decoders output 16-bit PCM (`PCM_16`). Individual decoders, such as AAC, may be configured to output other data types, for example `PCM_FLOAT`. Format-specific stream handling includes:

- **AAC (`c2.android.inproc.aac.decoder`):** Handles ADTS streams (with dynamic ADTS header parsing) and raw Access Units (AUs) with accurate presentation timestamp tracking (only single-frame AU processing in case of `AAC_PACKAGING_RAW`).
- **Opus (`c2.android.inproc.opus.decoder`):** Decodes standard Ogg Opus or Matroska container packets with internal resampling to 48 kHz PCM.

## Opt in to in-process decoders

Currently, in-process decoders aren't the system default when calling
[`MediaCodec.createDecoderByType()`](https://developer.android.com/reference/android/media/MediaCodec#createDecoderByType(java.lang.String)).
The platform retains higher Codec 2.0 selection priority for legacy
out-of-process decoders during ecosystem verification.

To opt in to an in-process decoder today for low-latency playback or testing,
instantiate the codec explicitly by component name using
[`MediaCodec.createByCodecName()`](https://developer.android.com/reference/android/media/MediaCodec#createByCodecName(java.lang.String)).

### Instantiate by component name

The following example demonstrates how to explicitly instantiate the
in-process AAC decoder, falling back to the default decoder if the in-process
component is unavailable on the device:

### Kotlin

```kotlin
val INPROC_AAC_CODEC = "c2.android.inproc.aac.decoder"

fun createAudioDecoder(): MediaCodec {
    return try {
        // Attempt to opt in to the low-latency in-process AAC decoder
        MediaCodec.createByCodecName(INPROC_AAC_CODEC)
    } catch (e: IllegalArgumentException) {
        // Fall back to the default platform AAC decoder
        MediaCodec.createDecoderByType(MediaFormat.MIMETYPE_AUDIO_AAC)
    }
}
```

### Java

```java
private static final String INPROC_AAC_CODEC = "c2.android.inproc.aac.decoder";

public MediaCodec createAudioDecoder() throws IOException {
    try {
        // Attempt to opt in to the low-latency in-process AAC decoder
        return MediaCodec.createByCodecName(INPROC_AAC_CODEC);
    } catch (IllegalArgumentException e) {
        // Fall back to the default platform AAC decoder
        return MediaCodec.createDecoderByType(MediaFormat.MIMETYPE_AUDIO_AAC);
    }
}
```

### Configure Jetpack Media3 or ExoPlayer

If your app uses Jetpack Media3 or ExoPlayer, you can create a custom
`MediaCodecSelector` to prioritize in-process decoders when they are available
on the device:

### Kotlin

```kotlin
class InprocPreferredMediaCodecSelector : MediaCodecSelector {
    override fun getDecoderInfos(
        mimeType: String,
        requiresSecureDecoder: Boolean,
        requiresTunnelingDecoder: Boolean
    ): List<MediaCodecInfo> {
        val defaultInfos = MediaCodecUtil.getDecoderInfos(
            mimeType,
            requiresSecureDecoder,
            requiresTunnelingDecoder
        )
        val inprocNames = setOf(
            "c2.android.inproc.opus.decoder",
            "c2.android.inproc.aac.decoder"
        )
        // Sort in-process decoders to the top of the selection list
        return defaultInfos.sortedByDescending { it.name in inprocNames }
    }
}
```

### Java

```java
public class InprocPreferredMediaCodecSelector implements MediaCodecSelector {
    private static final Set<String> INPROC_NAMES = new HashSet<>(Arrays.asList(
        "c2.android.inproc.opus.decoder",
        "c2.android.inproc.aac.decoder"
    ));

    @Override
    public List<MediaCodecInfo> getDecoderInfos(
            String mimeType,
            boolean requiresSecureDecoder,
            boolean requiresTunnelingDecoder) throws MediaCodecUtil.DecoderQueryException {
        List<MediaCodecInfo> defaultInfos = new ArrayList<>(
            MediaCodecUtil.getDecoderInfos(mimeType, requiresSecureDecoder, requiresTunnelingDecoder)
        );
        // Sort in-process decoders to the top of the selection list
        defaultInfos.sort((a, b) -> {
            boolean aInproc = INPROC_NAMES.contains(a.name);
            boolean bInproc = INPROC_NAMES.contains(b.name);
            return Boolean.compare(bInproc, aInproc);
        });
        return defaultInfos;
    }
}
```

## Roadmap to default system decoders

Android is actively preparing to transition these memory-safe in-process
decoders to become the system default decoders for their respective audio MIME
types in upcoming platform releases (starting with Opus LFI and AAC Rust in
Android 18 or upcoming Mainline module updates).

Once an in-process decoder becomes the default Codec 2.0 component for its
MIME type, standard calls to `MediaCodec.createDecoderByType(...)` will
automatically route through the in-process implementation, providing
approximately 40% lower decoding latency without requiring any app code
changes.

> [!NOTE]
> **Note:** If your app currently bundles custom third-party audio decoding libraries inside its APK (such as FDK-AAC or `libopus` JNI libraries) solely to avoid out-of-process IPC latency, you can test opting in to `c2.android.inproc.*` decoders today and prepare to remove your custom bundled libraries to reduce APK size and benefit from automatic Mainline security updates.