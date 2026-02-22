---
title: https://developer.android.com/ndk/guides/audio
url: https://developer.android.com/ndk/guides/audio
source: md.txt
---

# High-performance audio

High performance audio apps typically require more functionality than the simple ability to play or record sound. They demand responsive realtime system behavior. Some typical use cases include:

- Digital audio workstations
- Synthesizers
- Drum machines
- Music learning apps
- Karaoke apps
- DJ mixing
- Audio effects
- Video/audio conferencing

This section explains the general principles of minimizing[audio latency](https://developer.android.com/ndk/guides/audio/audio-latency). It also provides[advice about audio sampling](https://developer.android.com/ndk/guides/audio/sampling-audio), to help you choose the optimal sample rate and consider the pros and cons of using floating-point numbers to represent your audio data.

The rest of the section describes the two libraries that are available for writing high-performance audio applications:

- [OpenSL ES](https://developer.android.com/ndk/guides/audio/opensl)is an Android-specific implementation of the OpenSL ES™ API specification from the Khronos Group. OpenSL ES is not recommended for new designs. App developers and middleware providers should target either Oboe or AAudio as the native audio interface.
- [AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio)was developed as a lightweight, native Android alternative to the OpenSL ES library. The AAudio API is smaller and easier to use than OpenSL ES.

| **Note:** Developers should consider using the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles AAudio. It calls AAudio when it is available, and falls back to OpenSL ES if AAudio is not available.

## Additional resources

To learn more, take advantage of the following resources:

<br />

### Sample

- [Oboe Samples](https://github.com/google/oboe/tree/master/samples)

<br />

<br />

### Codelabs

- [Making Waves Part 1 - Build a Synthesizer](https://developer.android.com/codelabs/making-waves-1-synth)
- [Making More Waves - Sampler](https://developer.android.com/codelabs/making-waves-2-sampler)
- [Build a Musical Game using Oboe](https://developer.android.com/codelabs/musicalgame-using-oboe)

<br />

<br />

### Videos

- [Getting Started with Oboe](http://bit.ly/Introducing-Oboe)
- [Best Practices for Android Audio (Google I/O '17)](https://www.youtube.com/watch?v=C0BPXZIvG-Q)

<br />