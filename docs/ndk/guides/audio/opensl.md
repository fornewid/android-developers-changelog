---
title: OpenSL ES  |  Android NDK  |  Android Developers
url: https://developer.android.com/ndk/guides/audio/opensl
source: html-scrape
---

* [Home](https://developer.android.com/)
* [NDK](https://developer.android.com/ndk)
* [Develop](https://developer.android.com/develop)
* [Guides](https://developer.android.com/ndk/guides)

# OpenSL ES Stay organized with collections Save and categorize content based on your preferences.



WARNING: OpenSL ES is **deprecated**. Developers should use the open source
Oboe library which is available on [GitHub](https://github.com/google/oboe).
Oboe is a C++ wrapper that provides an API that closely resembles
[AAudio](/ndk/guides/audio/aaudio/aaudio). Oboe calls AAudio when AAudio is
available, and falls back to OpenSL ES if AAudio is not available.

The NDK package includes an Android-specific implementation of the
[OpenSL ES™](https://www.khronos.org/opensles/) 1.0.1 API
specification from the [Khronos Group](https://www.khronos.org).
This library lets you use C or C++ to implement high-performance, low-latency audio, whether
you are writing a synthesizer, digital audio workstation, karaoke, game,
or other real-time app.

The OpenSL ES™ standard exposes audio features
similar to those in the `MediaPlayer` and `MediaRecorder`
APIs in the Android Java framework. OpenSL ES provides a C language interface as well as
C++ bindings, allowing you to call the API from code written in either language.

The OpenSL ES APIs are available to help you develop and improve your app's audio performance.

The standard OpenSL ES headers <SLES/OpenSLES.h> and
<SLES/OpenSLES\_Platform.h> allow audio input and output. Additional
Android-specific functionality is in <SLES/OpenSLES\_Android.h> and
<SLES/OpenSLES\_AndroidConfiguration.h>.

This section begins by explaining
[how to incorporate OpenSL ES into your app](/ndk/guides/audio/opensl/getting-started).
Next, it explains what you need to know
about the Android implementation of OpenSL ES, focusing first on the
[differences](/ndk/guides/audio/opensl/opensl-for-android) between this implementation and the
reference specification and then
[additional extensions](/ndk/guides/audio/opensl/android-extensions)
for Android compatibility. This section concludes with some supplemental
 [programming notes](/ndk/guides/audio/opensl/opensl-prog-notes) to ensure proper
implementation of OpenSL ES.