---
title: https://developer.android.com/ndk/guides/audio/opensl/android-extensions
url: https://developer.android.com/ndk/guides/audio/opensl/android-extensions
source: md.txt
---

# Android extensions

WARNING: OpenSL ES is**deprecated** . Developers should use the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles[AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio). Oboe calls AAudio when AAudio is available, and falls back to OpenSL ES if AAudio is not available.

OpenSL ES for Android extends the reference OpenSL ES specification to make it compatible with Android, and to take advantage of the power and flexibility of the Android platform.

The definition of the API for the Android extensions resides in`OpenSLES_Android.h`and the header files that it includes. Consult`OpenSLES_Android.h`for details about these extensions. This file is located under your installation root, in the`sysroot/usr/include/SLES`directory. Unless otherwise noted, all interfaces are explicit.

These extensions limit your application's portability to other OpenSL ES implementations, because they are Android-specific. You can mitigate this issue by avoiding use of the extensions or by using`#ifdef`to exclude them at compile time.

The following table shows the Android-specific interfaces and data locators that Android OpenSL ES supports for each object type. The*Yes*values in the cells indicate the interfaces and data locators that are available for each object type.

|                 Feature                  |              Audio player               | Audio recorder | Engine | Output mix |
|------------------------------------------|-----------------------------------------|----------------|--------|------------|
| Android buffer queue                     | Yes: Source (decode)                    | No             | No     | No         |
| Android configuration                    | Yes                                     | Yes            | No     | No         |
| Android effect                           | Yes                                     | No             | No     | Yes        |
| Android effect capabilities              | No                                      | No             | Yes    | No         |
| Android effect send                      | Yes                                     | No             | No     | No         |
| Android simple buffer queue              | Yes: Source (playback) or sink (decode) | Yes            | No     | No         |
| Android buffer queue data locator        | Yes: Source (decode)                    | No             | No     | No         |
| Android file descriptor data locator     | Yes: Source                             | No             | No     | No         |
| Android simple buffer queue data locator | Yes: Source (playback) or sink (decode) | Yes: Sink      | No     | No         |

## Android configuration interface

The Android configuration interface provides a means to set platform-specific parameters for objects. This interface is different from other OpenSL ES 1.0.1 interfaces in that your app can use it before instantiating the corresponding object; thus, you can configure the object before instantiating it. The`OpenSLES_AndroidConfiguration.h`header file, which resides at`/sysroot/usr/include/SLES`, documents the following available configuration keys and values:

- Stream type for audio players (default`SL_ANDROID_STREAM_MEDIA`).
- Record profile for audio recorders (default`SL_ANDROID_RECORDING_PRESET_GENERIC`).

The following code snippet shows an example of how to set the Android audio stream type on an audio player:  

```c++
// CreateAudioPlayer and specify SL_IID_ANDROIDCONFIGURATION
// in the required interface ID array. Do not realize player yet.
// ...
SLAndroidConfigurationItf playerConfig;
result = (*playerObject)->GetInterface(playerObject,
    SL_IID_ANDROIDCONFIGURATION, &playerConfig);
assert(SL_RESULT_SUCCESS == result);
SLint32 streamType = SL_ANDROID_STREAM_ALARM;
result = (*playerConfig)->SetConfiguration(playerConfig,
    SL_ANDROID_KEY_STREAM_TYPE, &streamType, sizeof(SLint32));
assert(SL_RESULT_SUCCESS == result);
// ...
// Now realize the player here.
```

You can use similar code to configure the preset for an audio recorder:  

```c++
// ... obtain the configuration interface as the first four lines above, then:
SLuint32 presetValue = SL_ANDROID_RECORDING_PRESET_VOICE_RECOGNITION;
result = (*playerConfig)->SetConfiguration(playerConfig,
    RECORDING_PRESET, &presetValue, sizeof(SLuint32));
```

## Android effects interfaces

Android's effect, effect send, and effect capabilities interfaces provide a generic mechanism for an application to query and use device-specific audio effects. Device manufacturers should document any available device-specific audio effects that they provide.

Portable applications should use the OpenSL ES 1.0.1 APIs for audio effects instead of the Android effect extensions.

## Android file descriptor data locator

The Android file descriptor data locator permits you to specify the source for an audio player as an open file descriptor with read access. The data format must be MIME.

This extension is especially useful in conjunction with the native asset manager, because the app reads assets from the APK via a file descriptor.

## Android simple buffer queue data locator and interface

In the OpenSL ES 1.0.1 reference specification, buffer queues can be used for audio players only, and they are compatible with PCM and other data formats. The Android simple buffer queue data locator and interface specs are identical to the reference specification, with two exceptions:

- You can use Android simple buffer queues with audio recorders and audio players.
- You can only use the PCM data format with these queues.

For recording, your app should enqueue empty buffers. When a registered callback sends a notification that the system has finished writing data to a buffer, the app can read from that buffer.

Playback works in the same way. For future source code compatibility, however, we suggest that applications use Android simple buffer queues instead of OpenSL ES 1.0.1 buffer queues.

## Buffer queue behavior

The Android implementation does not include the reference specification's requirement that the play cursor return to the beginning of the currently playing buffer when playback enters the`SL_PLAYSTATE_STOPPED`state. This implementation can conform to that behavior, or it can leave the location of the play cursor unchanged. As a result, your app cannot assume that either behavior occurs. Therefore, you should explicitly call the`BufferQueue::Clear()`method after a transition to`SL_PLAYSTATE_STOPPED`. Doing so sets the buffer queue to a known state.

Similarly, there is no specification governing whether the trigger for a buffer queue callback must be a transition to`SL_PLAYSTATE_STOPPED`or an execution of`BufferQueue::Clear()`. Therefore, we recommend that you do not create a dependency on one or the other; instead, your app should be able to handle both.

## Dynamic interfaces at object creation

For convenience, the Android implementation of OpenSL ES 1.0.1 permits your app to specify dynamic interfaces when it instantiates an object. This is an alternative to using`DynamicInterfaceManagement::AddInterface()`to add these interfaces after instantiation.

## Reporting of extensions

There are three methods for querying whether the platform supports Android extensions. These methods are:

- `Engine::QueryNumSupportedExtensions()`
- `Engine::QuerySupportedExtension()`
- `Engine::IsExtensionSupported()`

Any of these methods returns`ANDROID_SDK_LEVEL_<API-level>`, where`API-level`is the platform API level; for example,`ANDROID_SDK_LEVEL_23`. A platform API level of 9 or higher means that the platform supports the extensions.

## Decode audio to PCM

This section describes a deprecated Android-specific extension to OpenSL ES 1.0.1 for decoding an encoded stream to PCM without immediate playback. The table below gives recommendations for use of this extension and alternatives.

|  API level   |                                                                                          Alternatives                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 15 and below | An open-source codec with a suitable license                                                                                                                                                    |
| 16 to 20     | The[MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)class or an open-source codec with a suitable license                                                          |
| 21 and above | NDK MediaCodec in the`<media/NdkMedia*.h>`header files, the[MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)class, or an open-source codec with a suitable license |

**Note:** There is currently no documentation for the NDK version of the`MediaCodec`API. However, you can refer to the[native-codec](https://github.com/android/ndk-samples/tree/main/native-codec)sample code for an example.

A standard audio player plays back to an audio device, specifying the output mix as the data sink. The Android extension differs in that an audio player instead acts as a decoder if the app has specified the data source either as a URI or as an Android file descriptor data locator described using the MIME data format. In such a case, the data sink is an Android simple buffer queue data locator that uses the PCM data format.

This feature is primarily intended for games to pre-load their audio assets when changing to a new game level, which is similar to the functionality that the[SoundPool](https://developer.android.com/reference/android/media/SoundPool)class provides.

The application should initially enqueue a set of empty buffers in the Android simple buffer queue. After that, the app fills the buffers with PCM data. The Android simple buffer queue callback fires after each buffer is filled. The callback handler processes the PCM data, re-enqueues the now-empty buffer, and then returns. The application is responsible for keeping track of decoded buffers; the callback parameter list does not include sufficient information to indicate the buffer that contains data or the buffer that should be enqueued next.

The data source implicitly reports the end of stream (EOS) by delivering a`SL_PLAYEVENT_HEADATEND`event at the end of the stream. After the app has decoded all of the data it received, it makes no further calls to the Android simple buffer queue callback.

The sink's PCM data format typically matches that of the encoded data source with respect to sample rate, channel count, and bit depth. However, you can decode to a different sample rate, channel count, or bit depth. For information about a provision to detect the actual PCM format, see[Determine the format of decoded PCM data via metadata](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#meta).

OpenSL ES for Android's PCM decoding feature supports pause and initial seek; it does not support volume control, effects, looping, or playback rate.

Depending on the platform implementation, decoding may require resources that cannot be left idle. Therefore, we recommend that you make sure to provide sufficient numbers of empty PCM buffers; otherwise, the decoder starves. This may happen, for example, if your app returns from the Android simple buffer queue callback without enqueueing another empty buffer. The result of decoder starvation is unspecified, but may include: dropping the decoded PCM data, pausing the decoding process, or terminating the decoder outright.

**Note:** To decode an encoded stream to PCM but not play back immediately, for apps running on Android 4.x (API levels 16--20), we recommend using the[MediaCodec](https://developer.android.com/reference/android/media/MediaCodec)class. For new applications running on Android 5.0 (API level 21) or higher, we recommend using the NDK equivalent,`<NdkMedia*.h>`. These header files reside in the`media/`directory under your installation root.

## Decode streaming ADTS AAC to PCM

An audio player acts as a streaming decoder if the data source is an Android buffer queue data locator that uses the MIME data format, and the data sink is an Android simple buffer queue data locator that uses the PCM data format. Configure the MIME data format as follows:

- Container:`SL_CONTAINERTYPE_RAW`
- MIME type string:`SL_ANDROID_MIME_AACADTS`

This feature is primarily intended for streaming media applications that deal with AAC audio but need to perform custom audio processing prior to playback. Most applications that need to decode audio to PCM should use the method that[Decode audio to PCM](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#decode-audio)describes, as that method is simpler and handles more audio formats. The technique described here is a more specialized approach, to be used only if both of these conditions apply:

- The compressed audio source is a stream of AAC frames contained in ADTS headers.
- The application manages this stream. The data is*not*located within a network resource whose identifier is a URI or within a local file whose identifier is a file descriptor.

The application should initially enqueue a set of filled buffers in the Android buffer queue. Each buffer contains one or more complete ADTS AAC frames. The Android buffer queue callback fires after each buffer is emptied. The callback handler should refill and re-enqueue the buffer, and then return. The application need not keep track of encoded buffers; the callback parameter list includes sufficient information to indicate the buffer that should be enqueued next. The end of stream is explicitly marked by enqueuing an EOS item. After EOS, no more enqueues are permitted.

We recommend that you make sure to provide full ADTS AAC buffers, to avoid starving the decoder. This may happen, for example, if your app returns from the Android buffer queue callback without enqueueing another full buffer. The result of decoder starvation is unspecified.

In all respects except for the data source, the streaming decode method is the same as the one that[Decode audio to PCM](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#decode-audio)describes.

Despite the similarity in names, an Android buffer queue is*not* the same as an[Android simple buffer queue](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#simple). The streaming decoder uses both kinds of buffer queues: an Android buffer queue for the ADTS AAC data source, and an Android simple buffer queue for the PCM data sink. For more information about the Android simple buffer queue API, see[Android simple buffer queue data locator and interface](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#simple). For more information about the Android buffer queue API, see the`index.html`file in the`docs/Additional_library_docs/openmaxal/`directory under the installation root.

## Determine the format of decoded PCM data via metadata

The`SLMetadataExtractionItf`interface is part of the reference specification. However, the metadata keys that indicate the actual format of decoded PCM data are specific to Android. The`OpenSLES_AndroidMetadata.h`header file defines these metadata keys. This header file resides under your installation root, in the`/sysroot/usr/include/SLES`directory.

The metadata key indices are available immediately after the`Object::Realize()`method finishes executing. However, the associated values are not available until after the app decodes the first encoded data. A good practice is to query for the key indices in the main thread after calling the`Object::Realize`method, and to read the PCM format metadata values in the Android simple buffer queue callback handler when calling it for the first time. Consult the[example code in the NDK package](https://github.com/googlesamples/android-ndk)for examples of working with this interface.

Metadata key names are stable, but the key indices are not documented, and are subject to change. An application should not assume that indices are persistent across different execution runs, and should not assume that multiple object instances share indices within the same run.

## Floating-point data

An app running on Android 5.0 (API level 21) and higher can supply data to an AudioPlayer in single-precision, floating-point format.

In following example code, the`Engine::CreateAudioPlayer()`method creates an audio player that uses floating-point data:  

```c++
#include <SLES/OpenSLES_Android.h>
...
SLAndroidDataFormat_PCM_EX pcm;
pcm.formatType = SL_ANDROID_DATAFORMAT_PCM_EX;
pcm.numChannels = 2;
pcm.sampleRate = SL_SAMPLINGRATE_44_1;
pcm.bitsPerSample = 32;
pcm.containerSize = 32;
pcm.channelMask = SL_SPEAKER_FRONT_LEFT | SL_SPEAKER_FRONT_RIGHT;
pcm.endianness = SL_BYTEORDER_LITTLEENDIAN;
pcm.representation = SL_ANDROID_PCM_REPRESENTATION_FLOAT;
...
SLDataSource audiosrc;
audiosrc.pLocator = ...
audiosrc.pFormat = &pcm;
```
Read more about[floating-point audio](https://developer.android.com/ndk/guides/audio/sampling-audio#floating-point)on the Sampling Audio page.