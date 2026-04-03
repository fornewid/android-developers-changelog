---
title: https://developer.android.com/ndk/guides/audio/opensl/opensl-for-android
url: https://developer.android.com/ndk/guides/audio/opensl/opensl-for-android
source: md.txt
---

# OpenSL ES for Android

WARNING: OpenSL ES is**deprecated** . Developers should use the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles[AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio). Oboe calls AAudio when AAudio is available, and falls back to OpenSL ES if AAudio is not available.

This page provides details about how the[NDK](https://developer.android.com/tools/sdk/ndk)implementation of OpenSL ES™ differs from the reference specification for OpenSL ES 1.0.1. When using sample code from the specification, you may need to modify it to work on Android.

Unless otherwise noted, all features are available at Android 2.3 (API level 9) and higher. Some features are only available for Android 4.0 (API level 14); these are noted.

**Note:** The Android Compatibility Definition Document (CDD) enumerates the hardware and software requirements of a compatible Android device. See[Android Compatibility](https://source.android.com/compatibility/)for more information on the overall compatibility program, and[CDD](https://source.android.com/compatibility/android-cdd.pdf)for the actual CDD document.

[OpenSL ES](https://www.khronos.org/opensles/)provides a C language interface that is also accessible using C++. It exposes features similar to the audio portions of these Android Java APIs:

- [android.media.MediaPlayer](https://developer.android.com/reference/android/media/MediaPlayer)
- [android.media.MediaRecorder](https://developer.android.com/reference/android/media/MediaRecorder)

As with all of the Android Native Development Kit (NDK), the primary purpose of OpenSL ES for Android is to facilitate the implementation of shared libraries to be called using the Java Native Interface ([JNI](https://en.wikipedia.org/wiki/Java_Native_Interface)). NDK is not intended for writing pure C/C++ applications. However, OpenSL ES is a full-featured API, and we expect that you should be able to accomplish most of your audio needs using only this API, without up-calls to code running in the Android runtime.

**Note:** Though based on OpenSL ES, the Android native audio (high-performance audio) API is not a conforming implementation of any OpenSL ES 1.0.1 profile (game, music, or phone). This is because Android does not implement all of the features required by any one of the profiles. Any known cases where Android behaves differently than the specification are described in the[Android extensions](https://developer.android.com/ndk/guides/audio/opensl/android-extensions)page.

## Features inherited from the reference specification

The Android NDK implementation of OpenSL ES inherits much of the feature set from the reference specification, with certain limitations.

### Global entry points

OpenSL ES for Android supports all of the global entry points in the Android specification. These entry points include:

- `slCreateEngine`
- `slQueryNumSupportedEngineInterfaces`
- `slQuerySupportedEngineInterfaces`

### Objects and interfaces

The following table shows the objects and interfaces that the Android NDK implementation of OpenSL ES supports. If a*Yes*appears in the cell, then the feature is available in this implementation.

Android NDK support for objects and interfaces.

|           Feature            |    Audio player    | Audio recorder | Engine | Output mix |
|------------------------------|--------------------|----------------|--------|------------|
| Bass boost                   | Yes                | No             | No     | Yes        |
| Buffer queue                 | Yes                | No             | No     | No         |
| Buffer queue data locator    | Yes: Source        | No             | No     | No         |
| Dynamic interface management | Yes                | Yes            | Yes    | Yes        |
| Effect send                  | Yes                | No             | No     | No         |
| Engine                       | No                 | No             | Yes    | No         |
| Environmental reverb         | No                 | No             | No     | Yes        |
| Equalizer                    | Yes                | No             | No     | Yes        |
| I/O device data locator      | No                 | Yes: Source    | No     | No         |
| Metadata extraction          | Yes: Decode to PCM | No             | No     | No         |
| Mute solo                    | Yes                | No             | No     | No         |
| Object                       | Yes                | Yes            | Yes    | Yes        |
| Output mix locator           | Yes: Sink          | No             | No     | No         |
| Play                         | Yes                | No             | No     | No         |
| Playback rate                | Yes                | No             | No     | No         |
| Prefetch status              | Yes                | No             | No     | No         |
| Preset reverb                | No                 | No             | No     | Yes        |
| Record                       | No                 | Yes            | No     | No         |
| Seek                         | Yes                | No             | No     | No         |
| URI data locator             | Yes: Source        | No             | No     | No         |
| Virtualizer                  | Yes                | No             | No     | Yes        |
| Volume                       | Yes                | No             | No     | No         |

The next section explains the limitations for some of these features.

### Limitations

Certain limitations apply to the features in Table 1. These limitations represent differences from the reference specification. The rest of this section provides information about these differences.

#### Dynamic interface management

OpenSL ES for Android does not support`RemoveInterface`or`ResumeInterface`.

#### Effect combinations: environment reverb and preset reverb

You cannot have both environmental reverb and preset reverb on the same output mix.

The platform might ignore effect requests if it estimates that the CPU load would be too high.

#### Effect send

`SetSendLevel()`supports a single send level per audio player.

#### Environmental reverb

Environmental reverb does not support the`reflectionsDelay`,`reflectionsLevel`, or`reverbDelay`fields of the`SLEnvironmentalReverbSettings`struct.

#### MIME data format

You can use the MIME data format only with the URI data locator, and only for an audio player. You cannot use this data format for an audio recorder.

The Android implementation of OpenSL ES requires you to initialize`mimeType`to either`NULL`or a valid UTF-8 string. You must also initialize`containerType`to a valid value. In the absence of other considerations, such as portability to other implementations or content formats that an app cannot identify by header, we recommend that you set`mimeType`to`NULL`and`containerType`to`SL_CONTAINERTYPE_UNSPECIFIED`.

OpenSL ES for Android supports the following audio formats, so long as the Android platform supports them as well:

- [WAV](https://en.wikipedia.org/wiki/WAV)PCM.
- WAV alaw.
- WAV ulaw.
- MP3 Ogg Vorbis.
- AAC LC.
- HE-AACv1 (AAC+).
- HE-AACv2 (enhanced AAC+).
- AMR.
- FLAC.

**Note:** For a list of audio formats that Android supports, see[Supported media formats](https://developer.android.com/guide/appendix/media-formats).

The following limitations apply to the handling of these and other formats in this implementation of OpenSL ES:

- [AAC](https://en.wikipedia.org/wiki/Advanced_Audio_Coding)formats must reside within an MP4 or ADTS container.
- OpenSL ES for Android does not support[MIDI](https://source.android.com/devices/audio/midi.html).
- WMA is not part of[AOSP](https://source.android.com/), and we have not verified its compatibility with OpenSL ES for Android.
- The Android NDK implementation of OpenSL ES does not support direct playback of DRM or encrypted content. To play back protected audio content, you must decrypt it in your application before playing, with your app enforcing any DRM restrictions.

#### Object-related methods

OpenSL ES for Android does not support the following methods for manipulating objects:

- `Resume()`
- `RegisterCallback()`
- `AbortAsyncOperation()`
- `SetPriority()`
- `GetPriority()`
- `SetLossOfControlInterfaces()`

#### PCM data format

PCM is the only data format you can use with buffer queues. Supported PCM playback configurations have the following characteristics:

- 8-bit unsigned or 16-bit signed.
- Mono or stereo.
- Little-endian byte ordering.
- Sample rates of:
  - 8,000 Hz.
  - 11,025 Hz.
  - 12,000 Hz.
  - 16,000 Hz.
  - 22,050 Hz.
  - 24,000 Hz.
  - 32,000 Hz.
  - 44,100 Hz.
  - 48,000 Hz.

The configurations that OpenSL ES for Android supports for recording are device-dependent; usually, 16,000 Hz mono/16-bit signed is available regardless of the device.

The value of the`samplesPerSec`field is in units of milliHz, despite the misleading name. To avoid accidentally using the wrong value, we recommend that you initialize this field using one of the symbolic constants defined for this purpose, such as`SL_SAMPLINGRATE_44_1`.

Android 5.0 (API level 21) and above support[floating-point data](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#floating-point).

#### Playback rate

An OpenSL ES*playback rate* indicates the speed at which an object presents data, expressed in thousandths of normal speed, or*per mille* . For example, a playback rate of 1,000 per mille is 1,000/1,000, or normal speed. A*rate range*is a closed interval that expresses a range of possible playback rates.

Support for playback rate ranges and other capabilities may vary depending on the platform version and implementation. Your app can determine these capabilities at runtime by using`PlaybackRate::GetRateRange()`or`PlaybackRate::GetCapabilitiesOfRate()`to query the device.

A device typically supports the same rate range for a data source in PCM format, and a unity rate range of 1000 per mille to 1000 per mille for other formats; that is, the unity rate range is effectively a single value.

#### Record

OpenSL ES for Android does not support the`SL_RECORDEVENT_HEADATLIMIT`or`SL_RECORDEVENT_HEADMOVING`events.

#### Seek

The`SetLoop()`method enables whole-file looping. To enable looping, set the`startPos`parameter to 0, and the`endPos`parameter to`SL_TIME_UNKNOWN`.

#### Buffer queue data locator

An audio player or recorder with a data locator for a buffer queue supports the PCM data format only.

#### I/O device data locator

OpenSL ES for Android only supports use of an I/O device data locator when you have specified the locator as the data source for`Engine::CreateAudioRecorder()`. Initialize the device data locator using the values contained in the following code snippet:  

```c++
SLDataLocator_IODevice loc_dev =
  {SL_DATALOCATOR_IODEVICE, SL_IODEVICE_AUDIOINPUT,
  SL_DEFAULTDEVICEID_AUDIOINPUT, NULL};
```

#### URI data locator

OpenSL ES for Android can only use the URI data locator with the MIME data format, and only for an audio player. You cannot use a URI data locator for an audio recorder. The URI can only use the`http:`and`file:`schemes. Other schemes, such as`https:`,`ftp:`, or`content:`are not allowed.

We have not verified support for`rtsp:`with audio on the Android platform.

#### Data structures

Android supports these OpenSL ES 1.0.1 data structures:

- `SLDataFormat_MIME`
- `SLDataFormat_PCM`
- `SLDataLocator_BufferQueue`
- `SLDataLocator_IODevice`
- `SLDataLocator_OutputMix`
- `SLDataLocator_URI`
- `SLDataSink`
- `SLDataSource`
- `SLEngineOption`
- `SLEnvironmentalReverbSettings`
- `SLInterfaceID`

#### Platform configuration

OpenSL ES for Android is designed for multi-threaded applications and is thread-safe. It supports a single engine per application and up to 32 objects per engine. Available device memory and CPU may further restrict the usable number of objects.

These engine options are recognized, but they're ignored by`slCreateEngine`:

- `SL_ENGINEOPTION_THREADSAFE`
- `SL_ENGINEOPTION_LOSSOFCONTROL`

OpenMAX AL and OpenSL ES may be used together in the same application. In this case, there is a single shared engine object internally, and the 32 object limit is shared between OpenMAX AL and OpenSL ES. The application should create both engines, use both engines, and finally destroy both engines. The implementation maintains a reference count on the shared engine so that it is correctly destroyed during the second destroy operation.

## Programming notes

[OpenSL ES programming notes](https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes)provides supplemental information to ensure proper implementation of OpenSL ES.

**Note:** For your convenience, we have included a copy of the OpenSL ES 1.0.1 specification with the NDK in`docs/opensles/OpenSL_ES_Specification_1.0.1.pdf`.

## Platform issues

This section describes known issues in the initial platform release that supports these APIs.

### Dynamic interface management

`DynamicInterfaceManagement::AddInterface`does not work. Instead, specify the interface in the array that is passed to`Create()`, as shown in the example code for environmental reverb.

## Plan for future versions of OpenSL ES

The Android high-performance audio APIs are based on[Khronos Group OpenSL ES 1.0.1](https://www.khronos.org/registry/sles/). Khronos has released a revised version 1.1 of the standard. The revised version includes new features, clarifications, corrections of typographical errors, and some incompatibilities. Most of the expected incompatibilities are relatively minor or are in areas of OpenSL ES that are not supported by Android.

An application developed with this version should work on future versions of the Android platform, provided that you follow the guidelines that are outlined in the[Plan for binary compatibility](https://developer.android.com/ndk/guides/audio/opensl/opensl-for-android#binary-compat)section below.

**Note:**Future source compatibility is not a goal. That is, if you upgrade to a newer version of the NDK, you may need to modify your application source code to conform to the new API. We expect that most such changes will be minor; see details below.

### Plan for binary compatibility

We recommend that your application follow these guidelines to improve future binary compatibility:

- Use only the documented subset of Android-supported features from OpenSL ES 1.0.1.
- Do not depend on a particular result code for an unsuccessful operation; be prepared to deal with a different result code.
- Application callback handlers generally run in a restricted context. They should be written to perform their work quickly, and then return as soon as possible. Do not run complex operations within a callback handler. For example, within a buffer queue completion callback, you can enqueue another buffer, but do not create an audio player.
- Callback handlers should be prepared to be called more or less frequently, to receive additional event types, and should ignore event types that they do not recognize. Callbacks that are configured with an event mask made of enabled event types should be prepared to be called with multiple event type bits set simultaneously. Use "\&" to test for each event bit rather than a switch case.
- Use prefetch status and callbacks as general indications of progress, but do not depend on specific hard-coded fill levels or callback sequences. The meaning of the prefetch status fill level, and the behavior for errors that are detected during prefetch, may change.

**Note:** See the[Buffer queue behavior](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#bq-behavior)section below for more details.

### Plan for source compatibility

As mentioned, source code incompatibilities are expected in the next version of OpenSL ES from Khronos Group. The likely areas of change include:

- The buffer queue interface is expected to have significant changes, especially in the areas of`BufferQueue::Enqueue`, the parameter list for`slBufferQueueCallback`, and the name of field`SLBufferQueueState.playIndex`. We recommend that your application code use Android simple buffer queues instead. In the example code that is supplied with the NDK, we have used Android simple buffer queues for playback for this reason. (We also use Android simple buffer queue for recording and decoding to PCM, but that is because standard OpenSL ES 1.0.1 does not support record or decode to a buffer queue data sink.)
- There will be an addition of`const`to the input parameters passed by reference, and to`SLchar *`struct fields used as input values. This should not require any changes to your code.
- There will be a substitution of unsigned types for some parameters that are currently signed. You may need to change a parameter type from`SLint32`to`SLuint32`or similar, or add a cast.
- `Equalizer::GetPresetName`copies the string to application memory instead of returning a pointer to implementation memory. This will be a significant change, so we recommend that you either avoid calling this method, or isolate your use of it.
- There will be additional fields in the struct types. For output parameters, these new fields can be ignored, but for input parameters the new fields will need to be initialized. Fortunately, all of these fields are expected to be in areas that are not supported by Android.
- Interface[GUIDs](https://en.wikipedia.org/wiki/Globally_unique_identifier)will change. Refer to interfaces by symbolic name rather than GUID to avoid a dependency.
- `SLchar`will change from`unsigned char`to`char`. This primarily affects the URI data locator and MIME data format.
- `SLDataFormat_MIME.mimeType`will be renamed to`pMimeType`, and`SLDataLocator_URI.URI`will be renamed to`pURI`. We recommend that you initialize the`SLDataFormat_MIME`and`SLDataLocator_URI`data structures using a brace-enclosed, comma-separated list of values, rather than by field name, to isolate your code from this change. This technique is used in the example code.
- `SL_DATAFORMAT_PCM`does not permit the application to specify the representation of the data as signed integer, unsigned integer, or floating-point. The Android implementation assumes that 8-bit data is unsigned integer and 16-bit is signed integer. In addition, the field`samplesPerSec`is a misnomer, as the actual units are milliHz. These issues are expected to be addressed in the next OpenSL ES version, which will introduce a new extended PCM data format that permits the application to explicitly specify the representation and corrects the field name. As this will be a new data format, and the current PCM data format will still be available (though deprecated), it should not require any immediate changes to your code.