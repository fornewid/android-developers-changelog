---
title: https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes
url: https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes
source: md.txt
---

# OpenSL ES programming notes

WARNING: OpenSL ES is**deprecated** . Developers should use the open source Oboe library which is available on[GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles[AAudio](https://developer.android.com/ndk/guides/audio/aaudio/aaudio). Oboe calls AAudio when AAudio is available, and falls back to OpenSL ES if AAudio is not available.

The notes in this section supplement the[OpenSL ES 1.0.1 specification](https://www.khronos.org/registry/sles/).

## Objects and interface initialization

Two aspects of the OpenSL ES programming model that may be unfamiliar to new developers are the distinction between objects and interfaces, and the initialization sequence.

Briefly, an OpenSL ES object is similar to the object concept in programming languages such as Java and C++, except an OpenSL ES object is only visible via its associated interfaces. This includes the initial interface for all objects, called`SLObjectItf`. There is no handle for an object itself, only a handle to the`SLObjectItf`interface of the object.

An OpenSL ES object is first*created* , which returns an`SLObjectItf`, then*realized*. This is similar to the common programming pattern of first constructing an object (which should never fail other than for lack of memory or invalid parameters), and then completing initialization (which may fail due to lack of resources). The realize step gives the implementation a logical place to allocate additional resources if needed.

As part of the API to create an object, an application specifies an array of desired interfaces that it plans to acquire later. Note that this array does not automatically acquire the interfaces; it merely indicates a future intention to acquire them. Interfaces are distinguished as*implicit* or*explicit* . An explicit interface must be listed in the array if it will be acquired later. An implicit interface need not be listed in the object create array, but there is no harm in listing it there. OpenSL ES has one more kind of interface called*dynamic* , which does not need to be specified in the object create array and can be added later after the object is created. The Android implementation provides a convenience feature to avoid this complexity, which is described in[Dynamic interfaces at object creation](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#dynamic-interfaces).

After the object is created and realized, the application should acquire interfaces for each feature it needs, using`GetInterface`on the initial`SLObjectItf`.

Finally, the object is available for use via its interfaces, though note that some objects require further setup. In particular, an audio player with URI data source needs a bit more preparation in order to detect connection errors. See the[Audio player prefetch](https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes#prefetch)section for details.

After your application is done with the object, you should explicitly destroy it; see the[Destroy](https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes#destroy)section below.

## Audio player prefetch

For an audio player with URI data source,`Object::Realize`allocates resources but does not connect to the data source (*prepare* ) or begin pre-fetching data. These occur once the player state is set to either`SL_PLAYSTATE_PAUSED`or`SL_PLAYSTATE_PLAYING`.

Some information may still be unknown until relatively late in this sequence. In particular, initially`Player::GetDuration`returns`SL_TIME_UNKNOWN`and`MuteSolo::GetChannelCount`either returns successfully with channel count zero or the error result`SL_RESULT_PRECONDITIONS_VIOLATED`. These APIs return the proper values once they are known.

Other properties that are initially unknown include the sample rate and actual media content type based on examining the content's header (as opposed to the application-specified MIME type and container type). These are also determined later during prepare/prefetch, but there are no APIs to retrieve them.

The prefetch status interface is useful for detecting when all information is available, or your application can poll periodically. Note that some information, such as the duration of a streaming MP3, may*never*be known.

The prefetch status interface is also useful for detecting errors. Register a callback and enable at least the`SL_PREFETCHEVENT_FILLLEVELCHANGE`and`SL_PREFETCHEVENT_STATUSCHANGE`events. If both of these events are delivered simultaneously, and`PrefetchStatus::GetFillLevel`reports a zero level, and`PrefetchStatus::GetPrefetchStatus`reports`SL_PREFETCHSTATUS_UNDERFLOW`, then this indicates a non-recoverable error in the data source. This includes the inability to connect to the data source because the local filename does not exist or the network URI is invalid.

The next version of OpenSL ES is expected to add more explicit support for handling errors in the data source. However, for future binary compatibility, we intend to continue to support the current method for reporting a non-recoverable error.

In summary, a recommended code sequence is:

1. `Engine::CreateAudioPlayer`
2. `Object:Realize`
3. `Object::GetInterface`for`SL_IID_PREFETCHSTATUS`
4. `PrefetchStatus::SetCallbackEventsMask`
5. `PrefetchStatus::SetFillUpdatePeriod`
6. `PrefetchStatus::RegisterCallback`
7. `Object::GetInterface`for`SL_IID_PLAY`
8. `Play::SetPlayState`to`SL_PLAYSTATE_PAUSED`, or`SL_PLAYSTATE_PLAYING`

**Note:**Preparation and prefetching occur here; during this time your callback is called with periodic status updates.

## Destroy

Be sure to destroy all objects when exiting from your application. Objects should be destroyed in reverse order of their creation, as it is not safe to destroy an object that has any dependent objects. For example, destroy in this order: audio players and recorders, output mix, and then finally the engine.

OpenSL ES does not support automatic garbage collection or[reference counting](https://en.wikipedia.org/wiki/Reference_counting)of interfaces. After you call`Object::Destroy`, all extant interfaces that are derived from the associated object become undefined.

The Android OpenSL ES implementation does not detect the incorrect use of such interfaces. Continuing to use such interfaces after the object is destroyed can cause your application to crash or behave in unpredictable ways.

We recommend that you explicitly set both the primary object interface and all associated interfaces to`NULL`as part of your object destruction sequence, which prevents the accidental misuse of a stale interface handle.

## Stereo panning

When`Volume::EnableStereoPosition`is used to enable stereo panning of a mono source, there is a 3-dB reduction in total[sound power level](https://en.wikipedia.org/wiki/Sound_power_level). This is needed to permit the total sound power level to remain constant as the source is panned from one channel to the other. Therefore, only enable stereo positioning if you need it. For more information see the Wikipedia article on[audio panning](https://en.wikipedia.org/wiki/Panning_(audio)).

## Callbacks and threads

Callback handlers are generally called synchronously when the implementation detects an event. This point is asynchronous with respect to the application, so you should use a non-blocking synchronization mechanism to control access to any variables shared between the application and the callback handler. In the example code, such as for buffer queues, we have either omitted this synchronization or used blocking synchronization in the interest of simplicity. However, proper non- blocking synchronization is critical for any production code.

Callback handlers are called from internal non-application threads that are not attached to the Android runtime, so they are ineligible to use JNI. Because these internal threads are critical to the integrity of the OpenSL ES implementation, a callback handler should also not block or perform excessive work.

If your callback handler needs to use JNI or execute work that is not proportional to the callback, the handler should instead post an event for another thread to process. Examples of acceptable callback workload include rendering and enqueuing the next output buffer (for an AudioPlayer), processing the just-filled input buffer and enqueueing the next empty buffer (for an AudioRecorder), or simple APIs such as most of the*Get* family. See the[Performance](https://developer.android.com/ndk/guides/audio/opensl/opensl-prog-notes#perform)section below regarding the workload.

Note that the converse is safe: an Android application thread that has entered JNI is allowed to directly call OpenSL ES APIs, including those that block. However, blocking calls are not recommended from the main thread, as they may result in*Application Not Responding*(ANR).

The determination regarding the thread that calls a callback handler is largely left up to the implementation. The reason for this flexibility is to permit future optimizations, especially on multi-core devices.

The thread on which the callback handler runs is not guaranteed to have the same identity across different calls. Therefore, do not rely on the`pthread_t`returned by`pthread_self()`or the`pid_t`returned by`gettid()`to be consistent across calls. For the same reason, do not use the thread local storage (TLS) APIs such as`pthread_setspecific()`and`pthread_getspecific()`from a callback.

The implementation guarantees that concurrent callbacks of the same kind, for the same object, does not occur. However, concurrent callbacks of different kinds for the same object are possible on different threads.

## Performance

As OpenSL ES is a native C API, non-runtime application threads that call OpenSL ES have no runtime-related overhead such as garbage collection pauses. With one exception described below, there is no additional performance benefit to the use of OpenSL ES other than this. In particular, the use of OpenSL ES does not guarantee enhancements such as lower audio latency and higher scheduling priority over that which the platform generally provides. On the other hand, as the Android platform and specific device implementations continue to evolve, an OpenSL ES application can expect to benefit from any future system performance improvements.

One such evolution is support for reduced[audio output latency](https://developer.android.com/ndk/guides/audio/audio-latency#output-latency). The underpinnings for reduced output latency were first included in Android 4.1 (API level 16), and then continued progress occurred in Android 4.2 (API level 17). These improvements are available via OpenSL ES for device implementations that claim feature`android.hardware.audio.low_latency`. If the device doesn't claim this feature but supports Android 2.3 (API level 9) or later, then you can still use the OpenSL ES APIs but the output latency may be higher. The lower output latency path is used only if the application requests a buffer size and sample rate that are compatible with the device's native output configuration. These parameters are device-specific and should be obtained as described below.

Beginning with Android 4.2 (API level 17), an application can query for the platform native or optimal output sample rate and buffer size for the device's primary output stream. When combined with the feature test just mentioned, an app can now configure itself appropriately for lower latency output on devices that claim support.

For Android 4.2 (API level 17) and earlier, a buffer count of two or more is required for lower latency. Beginning with Android 4.3 (API level 18), a buffer count of one is sufficient for lower latency.

All OpenSL ES interfaces for output effects preclude the lower latency path.

The recommended sequence is as follows:

1. Check for API level 9 or higher to confirm the use of OpenSL ES.
2. Check for the`android.hardware.audio.low_latency`feature using code such as this:  

   ### Kotlin

   ```kotlin
   import android.content.pm.PackageManager
   ...
   val pm: PackageManager = context.packageManager
   val claimsFeature: Boolean = pm.hasSystemFeature(PackageManager.FEATURE_AUDIO_LOW_LATENCY)
   ```

   ### Java

   ```java
   import android.content.pm.PackageManager;
   ...
   PackageManager pm = getContext().getPackageManager();
   boolean claimsFeature = pm.hasSystemFeature(PackageManager.FEATURE_AUDIO_LOW_LATENCY);
   ```
3. Check for API level 17 or higher to confirm the use of`android.media.AudioManager.getProperty()`.
4. Get the native or optimal output sample rate and buffer size for this device's primary output stream using code such as this:  

   ### Kotlin

   ```kotlin
   import android.media.AudioManager
   ...
   val am = getSystemService(Context.AUDIO_SERVICE) as AudioManager
   val sampleRate: String = am.getProperty(AudioManager.PROPERTY_OUTPUT_SAMPLE_RATE)
   val framesPerBuffer: String = am.getProperty(AudioManager.PROPERTY_OUTPUT_FRAMES_PER_BUFFER)
   ```

   ### Java

   ```java
   import android.media.AudioManager;
   ...
   AudioManager am = (AudioManager) getSystemService(Context.AUDIO_SERVICE);
   String sampleRate = am.getProperty(AudioManager.PROPERTY_OUTPUT_SAMPLE_RATE);
   String framesPerBuffer = am.getProperty(AudioManager.PROPERTY_OUTPUT_FRAMES_PER_BUFFER);
   ```
   Note that`sampleRate`and`framesPerBuffer`are*strings* . First check for null and then convert to int using`Integer.parseInt()`.
5. Now use OpenSL ES to create an AudioPlayer with PCM buffer queue data locator.

**Note:** You can use the[Audio Buffer Size](https://play.google.com/store/apps/details?id=com.levien.audiobuffersize)test app to determine the native buffer size and sample rate for OpenSL ES audio applications on your audio device. You can also visit GitHub to view[audio-buffer-size](https://github.com/gkasten/high-performance-audio/tree/master/audio-buffer-size)samples.

The number of lower latency audio players is limited. If your application requires more than a few audio sources, consider mixing your audio at the application level. Be sure to destroy your audio players when your activity is paused, as they are a global resource shared with other apps.

To avoid audible glitches, the buffer queue callback handler must execute within a small and predictable time window. This typically implies no unbounded blocking on mutexes, conditions, or I/O operations. Instead consider*try locks* , locks and waits with timeouts, and[non-blocking algorithms](https://source.android.com/devices/audio/avoiding_pi.html#nonBlockingAlgorithms).

The computation required to render the next buffer (for AudioPlayer) or consume the previous buffer (for AudioRecord) should take approximately the same amount of time for each callback. Avoid algorithms that execute in a non-deterministic amount of time or are*bursty*in their computations. A callback computation is bursty if the CPU time spent in any given callback is significantly larger than the average. In summary, the ideal is for the CPU execution time of the handler to have variance near zero, and for the handler to not block for unbounded times.

Lower latency audio is possible for these outputs only:

- On-device speakers.
- Wired headphones.
- Wired headsets.
- Line out.
- [USB digital audio](https://source.android.com/devices/audio/usb.html).

On some devices, speaker latency is higher than other paths due to digital signal processing for speaker correction and protection.

As of Android 5.0 (API Level 21),[lower latency audio input](https://developer.android.com/ndk/guides/audio/audio-latency#input-latency)is supported on select devices. To take advantage of this feature, first confirm that lower latency output is available as described above. The capability for lower latency output is a prerequisite for the lower latency input feature. Then, create an AudioRecorder with the same sample rate and buffer size as would be used for output. OpenSL ES interfaces for input effects preclude the lower latency path. The record preset`SL_ANDROID_RECORDING_PRESET_VOICE_RECOGNITION`must be used for lower latency; this preset disables device-specific digital signal processing that may add latency to the input path. For more information on record presets, see the[Android configuration interface](https://developer.android.com/ndk/guides/audio/opensl/android-extensions#configuration-interface)section above.

For simultaneous input and output, separate buffer queue completion handlers are used for each side. There is no guarantee of the relative order of these callbacks, or the synchronization of the audio clocks, even when both sides use the same sample rate. Your application should buffer the data with proper buffer synchronization.

One consequence of potentially independent audio clocks is the need for asynchronous sample rate conversion. A simple (though not ideal for audio quality) technique for asynchronous sample rate conversion is to duplicate or drop samples as needed near a zero-crossing point. More sophisticated conversions are possible.

### Performance modes

Starting with Android 7.1 (API Level 25) OpenSL ES introduced a way to specify a performance mode for the audio path. The options are:

- `SL_ANDROID_PERFORMANCE_NONE`: No specific performance requirement. Allows hardware and software effects.
- `SL_ANDROID_PERFORMANCE_LATENCY`: Priority is given to latency. No hardware or software effects. This is the default mode.
- `SL_ANDROID_PERFORMANCE_LATENCY_EFFECTS`: Priority is given to latency while still allowing hardware and software effects.
- `SL_ANDROID_PERFORMANCE_POWER_SAVING`: Priority given to conserving power. Allows hardware and software effects.

**Note:** If you do not require a low latency path and wish to take advantage of the device's built-in audio effects (for example to improve acoustic quality for video playback), you must explicitly set the performance mode to`SL_ANDROID_PERFORMANCE_NONE`.

To set the performance mode, you must call`SetConfiguration`using the Android configuration interface, as shown below:  

```c++
  // Obtain the Android configuration interface using a previously configured SLObjectItf.
  SLAndroidConfigurationItf configItf = nullptr;
  (*objItf)->GetInterface(objItf, SL_IID_ANDROIDCONFIGURATION, &configItf);

  // Set the performance mode.
  SLuint32 performanceMode = SL_ANDROID_PERFORMANCE_NONE;
    result = (*configItf)->SetConfiguration(configItf, SL_ANDROID_KEY_PERFORMANCE_MODE,
                                                     &performanceMode, sizeof(performanceMode));
```

## Security and permissions

As far as who can do what, security in Android is done at the process level. Java programming language code cannot do anything more than native code, nor can native code do anything more than Java programming language code. The only differences between them are the available APIs.

Applications using OpenSL ES must request the permissions that they would need for similar non-native APIs. For example, if your application records audio, then it needs the`android.permission.RECORD_AUDIO`permission. Applications that use audio effects need`android.permission.MODIFY_AUDIO_SETTINGS`. Applications that play network URI resources need`android.permission.NETWORK`. For more information see[Working with System Permissions](https://developer.android.com/training/permissions/index.html).

Depending on the platform version and implementation, media content parsers and software codecs may run within the context of the Android application that calls OpenSL ES (hardware codecs are abstracted but are device-dependent). Malformed content designed to exploit parser and codec vulnerabilities is a known attack vector. We recommend that you play media only from trustworthy sources or that you partition your application such that code that handles media from untrustworthy sources runs in a relatively*sandboxed*environment. For example, you could process media from untrustworthy sources in a separate process. Though both processes would still run under the same UID, this separation does make an attack more difficult.