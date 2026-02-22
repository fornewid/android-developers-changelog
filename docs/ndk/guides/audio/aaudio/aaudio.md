---
title: https://developer.android.com/ndk/guides/audio/aaudio/aaudio
url: https://developer.android.com/ndk/guides/audio/aaudio/aaudio
source: md.txt
---

| **Note:** Developers should consider using the open source Oboe library which is available on [GitHub](https://github.com/google/oboe). Oboe is a C++ wrapper that provides an API that closely resembles AAudio. It calls AAudio when it is available, and falls back to [OpenSL ES](https://developer.android.com/ndk/guides/audio/opensl) if AAudio is not available.

AAudio is a new Android C API introduced in the Android O release. It is designed for high-performance audio applications that require low latency. Apps communicate with AAudio by reading and writing data to streams.

The AAudio API is minimal by design,
it doesn't perform these functions:

- Audio device enumeration
- Automated routing between audio endpoints
- File I/O
- Decoding of compressed audio
- Automatic presentation of all input/streams in a single callback.

## Getting started

You can call AAudio from C++ code. To add the AAudio feature set to your app, include the AAudio.h header file:

    #include <aaudio/AAudio.h>

## Audio streams

AAudio moves audio data between your app and the audio inputs and outputs on your Android device. Your app passes data in and out by reading from and writing to *audio streams*, represented by the structure AAudioStream. The read/write calls can be blocking or non-blocking.

A stream is defined by the following:

- The *audio* *device* that is the source or sink for the data in the stream.
- The *sharing mode* that determines whether a stream has exclusive access to an audio device that might otherwise be shared among multiple streams.
- The *format* of the audio data in the stream.

### Audio device

Each stream is attached to a single audio device.

An audio device is a hardware interface or virtual endpoint that acts as a source or sink for a continuous stream of digital audio data. Don't confuse an *audio device*
(a built-in mic or bluetooth headset) with the *Android device* (the phone or watch) that is running your app.

You can use the `AudioManager` method `https://developer.android.com/reference/android/media/AudioManager#getDevices(int)` to discover the audio devices that are available on your Android device. The method returns information about the `https://developer.android.com/reference/android/media/AudioDeviceInfo` of each device.

Each audio device has a unique ID on the Android device. You can use the ID to bind an audio stream to a specific audio device. However, in most cases you can let AAudio choose the default primary device rather than specifying one yourself.

The audio device attached to a stream determines whether the stream is for input or output. A stream can only move data in one direction. When you define a stream you also set its direction. When you open a stream Android checks to ensure that the audio device and stream direction agree.

### Sharing mode

A stream has a sharing mode:

- `AAUDIO_SHARING_MODE_EXCLUSIVE` means the stream has exclusive access to its audio device; the device cannot be used by any other audio stream. If the audio device is already in use, it might not be possible for the stream to have exclusive access. Exclusive streams are likely to have lower latency, but they are also more likely to get disconnected. You should close exclusive streams as soon as you no longer need them, so that other apps can access the device. Exclusive streams provide the lowest possible latency.
- `AAUDIO_SHARING_MODE_SHARED` allows AAudio to mix audio. AAudio mixes all the shared streams assigned to the same device.

You can set the sharing mode explicitly when you create a stream. By default,
the sharing mode is `SHARED`.

### Audio format

The data passed through a stream has the usual digital audio attributes. These are as follows:

- Sample data format
- Channel count (samples per frame)
- Sample rate

AAudio permits these sample formats:

| aaudio_format_t | C data type | Notes |
|---|---|---|
| AAUDIO_FORMAT_PCM_I16 | int16_t | common 16-bit samples, [Q0.15 format](https://source.android.com/devices/audio/data_formats#androidFormats) |
| AAUDIO_FORMAT_PCM_FLOAT | float | -1.0 to +1.0 |
| AAUDIO_FORMAT_PCM_I24_PACKED | uint8_t in groups of 3 | packed 24-bit samples, [Q0.23 format](https://source.android.com/devices/audio/data_formats#androidFormats) |
| AAUDIO_FORMAT_PCM_I32 | int32_t | common 32-bit samples, [Q0.31 format](https://source.android.com/devices/audio/data_formats#androidFormats) |
| AAUDIO_FORMAT_IEC61937 | uint8_t | compressed audio wrapped in IEC61937 for HDMI or S/PDIF passthrough |

If you request a specific sample format then the stream will use that format,
even if the format is not optimal for the device.
If you do not specify a sample format, AAudio will choose one that is optimal.
After the stream is opened you must query the sample data format and then
convert data if necessary, as in this example:

    aaudio_format_t dataFormat = AAudioStream_getDataFormat(stream);
    //... later
    if (dataFormat == AAUDIO_FORMAT_PCM_I16) {
         convertFloatToPcm16(...)
    }

## Creating an audio stream

The AAudio library follows a [builder design pattern](https://en.wikipedia.org/wiki/Builder_pattern) and provides AAudioStreamBuilder.

<br />

1. Create an AAudioStreamBuilder:<br />

       AAudioStreamBuilder *builder;
       aaudio_result_t result = AAudio_createStreamBuilder(&builder);

   <br />

2. Set the audio stream configuration in the builder, using the builder functions that correspond to the stream parameters. These optional set functions are available:<br />

       AAudioStreamBuilder_setDeviceId(builder, deviceId);
       AAudioStreamBuilder_setDirection(builder, direction);
       AAudioStreamBuilder_setSharingMode(builder, mode);
       AAudioStreamBuilder_setSampleRate(builder, sampleRate);
       AAudioStreamBuilder_setChannelCount(builder, channelCount);
       AAudioStreamBuilder_setFormat(builder, format);
       AAudioStreamBuilder_setBufferCapacityInFrames(builder, frames);

   Note that these methods do not report errors, such as an undefined constant or value out of range.

   If you do not specify the deviceId, the default is the primary output device.
   If you do not specify the stream direction, the default is an output stream.
   For all other parameters, you can explicitly set a value, or let the system
   assign the optimal value by not specifying the parameter at all or setting
   it to `AAUDIO_UNSPECIFIED`.

   To be safe, check the state of the audio stream after you create it, as explained in step 4, below.

   <br />

3. When the AAudioStreamBuilder is configured, use it to create a stream:<br />

       AAudioStream *stream;
       result = AAudioStreamBuilder_openStream(builder, &stream);

   <br />

4. After creating the stream, verify its configuration. If you specified sample format, sample rate, or samples per frame they will not change. If you specified sharing mode or buffer capacity, they might change depending on the capabilities of the stream's audio device and the Android device on which it's running. As a matter of good defensive programming, you should check the stream's configuration before using it. There are functions to retrieve the stream setting that corresponds to each builder setting:<br />

   <br />

   |---|---|
   | [`AAudioStreamBuilder_setDeviceId()`](https://developer.android.com/ndk/reference/group___audio#gaab12dd029554b2928cac6bb057903525) | [`AAudioStream_getDeviceId()`](https://developer.android.com/ndk/reference/group___audio#ga1914721c39f9400c6a7e32b11908b066) |
   | [`AAudioStreamBuilder_setDirection()`](https://developer.android.com/ndk/reference/group___audio#ga22a61c42068a5733d0d4c7b4114c3333) | [`AAudioStream_getDirection()`](https://developer.android.com/ndk/reference/group___audio#ga8845709a1ea64e18eed9255c15a8402b) |
   | [`AAudioStreamBuilder_setSharingMode()`](https://developer.android.com/ndk/reference/group___audio#gaa5edd7941e1dc11cc7dbf5b35dd54841) | [`AAudioStream_getSharingMode()`](https://developer.android.com/ndk/reference/group___audio#ga51b7db27bdd331c22d8443a50033a17a) |
   | [`AAudioStreamBuilder_setSampleRate()`](https://developer.android.com/ndk/reference/group___audio#ga8b7930b6b7251e6a73c601030c7ce2b2) | [`AAudioStream_getSampleRate()`](https://developer.android.com/ndk/reference/group___audio#ga2f3f5739425578c6c8e61c02f53528ce) |
   | [`AAudioStreamBuilder_setChannelCount()`](https://developer.android.com/ndk/reference/group___audio#ga8d7461d982bbff630dea6546ec7e9844) | [`AAudioStream_getChannelCount()`](https://developer.android.com/ndk/reference/group___audio#gac04633015b26345d2f2fa97d32e0d643) |
   | [`AAudioStreamBuilder_setFormat()`](https://developer.android.com/ndk/reference/group___audio#gacdf4cd79e60923c300bc81e7ab032713) | [`AAudioStream_getFormat()`](https://developer.android.com/ndk/reference/group___audio#ga90831503bace94aa6a650baba29aec36) |
   | [`AAudioStreamBuilder_setBufferCapacityInFrames()`](https://developer.android.com/ndk/reference/group___audio#ga4dbce24e8b60b733ddbe2a76052e66f0) | [`AAudioStream_getBufferCapacityInFrames()`](https://developer.android.com/ndk/reference/group___audio#ga887c8e56710452305f229907be60a046) |

5. You can save the builder and reuse it in the future to make more streams. But if you don't plan to use it any more, you should delete it.<br />

       AAudioStreamBuilder_delete(builder);

   <br />

<br />

## Using an audio stream

### State transitions

An AAudio stream is usually in one of five stable states (the error state, Disconnected, is described at the end of this section):

- Open
- Started
- Paused
- Flushed
- Stopped

Data only flows through a stream when the stream is in the Started state. To
move a stream between states, use one of the functions that request a state
transition:

    aaudio_result_t result;
    result = AAudioStream_requestStart(stream);
    result = AAudioStream_requestStop(stream);
    result = AAudioStream_requestPause(stream);
    result = AAudioStream_requestFlush(stream);

Note that you can only request pause or flush on an output stream:

These functions are asynchronous, and the state change doesn't happen
immediately. When you request a state change, the stream moves one of the
corresponding transient states:

- Starting
- Pausing
- Flushing
- Stopping
- Closing

The state diagram below shows the stable states as rounded rectangles, and the transient states as dotted rectangles.
Though it's not shown, you can call `close()` from any state

![AAudio Lifecycle](https://developer.android.com/static/ndk/guides/images/aaudio-lifecycle.png)

AAudio doesn't provide callbacks to alert you to state changes. One special
function,
`https://developer.android.com/ndk/reference/group___audio#ga6ae9b716d703eaf350c03a60c36b8d8b` can be used to wait for a state change.

The function does not detect a state change on its own, and does not wait for a
specific state. It waits until the current state
is *different* than `inputState`, which you specify.

For example, after requesting to pause, a stream should immediately enter
the transient state Pausing, and arrive sometime later at the Paused state - though there's no guarantee it will.
Since you can't wait for the Paused state, use `waitForStateChange()` to wait for *any state
other than Pausing*. Here's how that's done:

    aaudio_stream_state_t inputState = AAUDIO_STREAM_STATE_PAUSING;
    aaudio_stream_state_t nextState = AAUDIO_STREAM_STATE_UNINITIALIZED;
    int64_t timeoutNanos = 100 * AAUDIO_NANOS_PER_MILLISECOND;
    result = AAudioStream_requestPause(stream);
    result = AAudioStream_waitForStateChange(stream, inputState, &nextState, timeoutNanos);

If the stream's state is not Pausing (the `inputState`, which we assumed was the
current state at call time), the function returns immediately. Otherwise, it
blocks until the state is no longer Pausing or the timeout expires. When the
function returns, the parameter `nextState` shows the current state of the
stream.

You can use this same technique after calling request start, stop, or flush,
using the corresponding transient state as the inputState. Do not call
`waitForStateChange()` after calling `AAudioStream_close()` since the stream
will be deleted as soon as it closes. And do not call `AAudioStream_close()`
while `waitForStateChange()` is running in another thread.

### Reading and writing to an audio stream

There are two ways to process the data in a stream after it is started:

- Use a [high priority callback](https://developer.android.com/ndk/guides/audio/aaudio/aaudio#high-priority-callback).
- Use the functions [`AAudioStream_read(stream, buffer, numFrames, timeoutNanos)`](https://developer.android.com/ndk/reference/group___audio#gaaab7b0aa16105267b27e0a1ae2d13652) and [`AAudioStream_write(stream, buffer, numFrames, timeoutNanos)`](https://developer.android.com/ndk/reference/group___audio#ga12c6681893f9ce2df479c67334f41d21). to read or write the stream.

For a blocking read or write that transfers the specified number of frames, set timeoutNanos greater than zero.
For a non-blocking call, set timeoutNanos to zero. In this case the result is the actual number of frames transferred.

When you read input, you should verify the correct number of
frames was read. If not, the buffer might contain unknown data that could cause an
audio glitch. You can pad the buffer with zeros to create a
silent dropout:

    aaudio_result_t result =
        AAudioStream_read(stream, audioData, numFrames, timeout);
    if (result < 0) {
      // Error!
    }
    if (result != numFrames) {
      // pad the buffer with zeros
      memset(static_cast<sample_type*>(audioData) + result * samplesPerFrame, 0,
          sizeof(sample_type) * (numFrames - result) * samplesPerFrame);
    }

You can prime the stream's buffer before starting the stream by writing data or silence into it. This must be done in a non-blocking call with timeoutNanos set to zero.

The data in the buffer must match the data format returned by `AAudioStream_getDataFormat()`.

### Closing an audio stream

When you are finished using a stream, close it:

    AAudioStream_close(stream);

After you close a stream you cannot use the stream pointer with any AAudio
stream-based function.

Closing a stream is not thread safe!
Do NOT try to close a stream in one thread while using the stream in another
thread.
If you are using multiple threads then they must be carefully synchronized.
You may want to put all your stream handling code in a single thread and then
send it commands using an atomic queue.

### Disconnected audio stream

An audio stream can become disconnected at any time if one of these events happens:

- The associated audio device is no longer connected (for example when headphones are unplugged).
- An error occurs internally.
- An audio device is no longer the primary audio device.

When a stream is disconnected, it has the state "Disconnected" and any attempts to execute AAudioStream_write() or other functions will return an error.
You must always stop and close a disconnected stream, regardless of the error code.

If you are using a data callback (as opposed to one of the direct read/write methods)
then you will not receive any return code when the stream is disconnected.
To be informed when this happens write an [AAudioStream_errorCallback](https://developer.android.com/ndk/reference/group___audio.html#gab747ce9806538a0ec00827fc51bad4c9)
function and register it using
[AAudioStreamBuilder_setErrorCallback()](https://developer.android.com/ndk/reference/group___audio.html#ga7f42413b553bbd92bfe9565c1851e760).

If you are notified of the disconnect in an error callback thread then the stopping and closing
of the stream must be done from another thread. Otherwise you may have a deadlock.

Note that if you open a new stream it might have different settings
from the original stream (for example framesPerBurst):

    void errorCallback(AAudioStream *stream,
                       void *userData,
                       aaudio_result_t error) {
        // Launch a new thread to handle the disconnect.
        std::thread myThread(my_error_thread_proc, stream, userData);
        myThread.detach(); // Don't wait for the thread to finish.
    }

## Optimizing performance

You can optimize the performance of an audio application by adjusting its internal buffers and by using special high-priority threads.

### Tuning buffers to minimize latency

AAudio passes data in and out of internal buffers that it maintains, one for each audio device.
| **Note:** Don't confuse AAudio's internal buffers with the buffer parameter of the AAudio stream read and write functions.

The buffer's *capacity* is the total amount of data a buffer can hold. You can call
[`AAudioStreamBuilder_setBufferCapacityInFrames()`](https://developer.android.com/ndk/reference/group___audio#ga4dbce24e8b60b733ddbe2a76052e66f0)
to set the capacity. The method limits the capacity you can allocate to the maximum value that the device permits. Use
[`AAudioStream_getBufferCapacityInFrames()`](https://developer.android.com/ndk/reference/group___audio#ga887c8e56710452305f229907be60a046)
to verify the actual capacity of the buffer.

An app doesn't have to use the entire capacity of a buffer. AAudio fills a buffer up to a *size* which you can set. The size of a buffer can be no larger than its capacity, and it is often smaller. By controlling the buffer size you determine the number of bursts needed to fill it, and thus control latency. Use the methods [`AAudioStreamBuilder_setBufferSizeInFrames()`](https://developer.android.com/ndk/reference/group___audio#ga4774390a0e5382847898e20bfc46b1db)
and
[`AAudioStreamBuilder_getBufferSizeInFrames()`](https://developer.android.com/ndk/reference/group___audio#gafa81996dc35f841a9d461e7122e83290)
to work with the buffer size.

When an application plays audio out, it writes to a buffer and blocks until the write is complete. AAudio reads from the buffer in discrete bursts. Each burst contains a multiple number of audio frames and is usually smaller than the size of the buffer being read.
The system controls burst size and rate, these properties are typically dictated by the audio device's circuitry.
Though you can't change the size of a burst or the burst rate, you can set the size of the internal buffer according to the number of bursts it contains.
Generally, you get the lowest latency if your AAudioStream's buffer size is a multiple of the reported burst size.

![AAudio Buffering](https://developer.android.com/static/ndk/guides/images/aaudio-buffering.png)

One way to optimize the buffer size is to start with a large buffer and gradually lower it until underruns begin, then nudge it back up. Alternatively, you can start with a small buffer size and if that produces underruns, increase the buffer size until the output flows cleanly again.

This process can take place very quickly, possibly before the user plays the first sound. You may want to perform the initial buffer sizing first, using silence, so that the user won't hear any audio glitches. System performance may change over time (for example, the user might turn off airplane mode). Since buffer tuning adds very little overhead, your app
can do it continuously while the app reads or writes data to a stream.

Here is an example of a buffer optimization loop:

    int32_t previousUnderrunCount = 0;
    int32_t framesPerBurst = AAudioStream_getFramesPerBurst(stream);
    int32_t bufferSize = AAudioStream_getBufferSizeInFrames(stream);

    int32_t bufferCapacity = AAudioStream_getBufferCapacityInFrames(stream);

    while (go) {
        result = writeSomeData();
        if (result < 0) break;

        // Are we getting underruns?
        if (bufferSize < bufferCapacity) {
            int32_t underrunCount = AAudioStream_getXRunCount(stream);
            if (underrunCount > previousUnderrunCount) {
                previousUnderrunCount = underrunCount;
                // Try increasing the buffer size by one burst
                bufferSize += framesPerBurst;
                bufferSize = AAudioStream_setBufferSize(stream, bufferSize);
            }
        }
    }

There is no advantage to using this technique to optimize the buffer size for an input stream.
Input streams run as fast as possible, trying to keep the amount
of buffered data to a minimum, and then filling up when the app is preempted.

### Using a high priority callback

If your app reads or writes audio data from an ordinary thread, it may be preempted or experience timing jitter. This can cause audio glitches.
Using larger buffers might guard against such glitches, but a large buffer also introduces longer audio latency.
For applications that require low latency, an audio stream can use an asynchronous callback function to transfer data to and from your app.
AAudio executes the callback in a higher-priority thread that has better performance.

The callback function has this prototype:

    typedef aaudio_data_callback_result_t (*AAudioStream_dataCallback)(
            AAudioStream *stream,
            void *userData,
            void *audioData,
            int32_t numFrames);

Use the stream building to register the callback:

    AAudioStreamBuilder_setDataCallback(builder, myCallback, myUserData);

In the simplest case, the stream periodically executes the callback function to
acquire the data for its next burst.

The callback function should not perform a read or write on the stream that
invoked it. If the callback belongs to an input stream, your code should process
the data that is supplied in the audioData buffer (specified as the third
argument). If the callback belongs to an output stream, your code should place
data into the buffer.

For example, you could use a callback to continuously generate a sine wave output
like this:

    aaudio_data_callback_result_t myCallback(
            AAudioStream *stream,
            void *userData,
            void *audioData,
            int32_t numFrames) {
        int64_t timeout = 0;

        // Write samples directly into the audioData array.
        generateSineWave(static_cast<float *>(audioData), numFrames);
        return AAUDIO_CALLBACK_RESULT_CONTINUE;
    }

It is possible to process more than one stream using AAudio. You can use one stream as the master, and
pass pointers to other streams in the user data. Register a callback for the master stream. Then use non-blocking I/O on the other streams. Here is an example of a round-trip callback that passes an input stream to an output stream.
The master calling stream is the output stream. The input stream is included in the user data.

The callback does a non-blocking read from the input stream placing the data into the buffer of the output stream:

    aaudio_data_callback_result_t myCallback(
            AAudioStream *stream,
            void *userData,
            void *audioData,
            int32_t numFrames) {
        AAudioStream *inputStream = (AAudioStream *) userData;
        int64_t timeout = 0;
        aaudio_result_t result =
            AAudioStream_read(inputStream, audioData, numFrames, timeout);

      if (result == numFrames)
          return AAUDIO_CALLBACK_RESULT_CONTINUE;
      if (result >= 0) {
          memset(static_cast<sample_type*>(audioData) + result * samplesPerFrame, 0,
              sizeof(sample_type) * (numFrames - result) * samplesPerFrame);
          return AAUDIO_CALLBACK_RESULT_CONTINUE;
      }
      return AAUDIO_CALLBACK_RESULT_STOP;
    }

Note that in this example it is assumed the input and output streams have the same number of channels, format and sample rate. The format of the streams can be mismatched - as long as the code handles the translations properly.

### Setting performance mode

Every AAudioStream has a *performance mode* which has a large effect on your app's behavior. There are three modes:

- `AAUDIO_PERFORMANCE_MODE_NONE` is the default mode. It uses a basic stream that balances latency and power savings.
- `AAUDIO_PERFORMANCE_MODE_LOW_LATENCY` uses smaller buffers and an optimized data path for reduced latency.
- `AAUDIO_PERFORMANCE_MODE_POWER_SAVING` uses larger internal buffers and a data path that trades off latency for lower power.

You can select the performance mode by calling [setPerformanceMode()](https://developer.android.com/ndk/reference/group___audio.html#ga9e8b3c88f78cc8d5a4aaa3af57a46407),
and discover the current mode by calling [getPerformanceMode()](https://developer.android.com/ndk/reference/group___audio.html#gaff802df793c10331b73a706c5f5f45e8).

If low latency is more important than power savings in your application, use `AAUDIO_PERFORMANCE_MODE_LOW_LATENCY`.
This is useful for apps that are very interactive, such as games or keyboard synthesizers.

If saving power is more important than low latency in your application, use `AAUDIO_PERFORMANCE_MODE_POWER_SAVING`.
This is typical for apps that play back previously generated music, such as streaming audio or MIDI file players.

In the current version of AAudio, in order to achieve the lowest possible latency you must use the `AAUDIO_PERFORMANCE_MODE_LOW_LATENCY` performance mode along with a high-priority callback. Follow this example:

    // Create a stream builder
    AAudioStreamBuilder *streamBuilder;
    AAudio_createStreamBuilder(&streamBuilder);
    AAudioStreamBuilder_setDataCallback(streamBuilder, dataCallback, nullptr);
    AAudioStreamBuilder_setPerformanceMode(streamBuilder, AAUDIO_PERFORMANCE_MODE_LOW_LATENCY);

    // Use it to create the stream
    AAudioStream *stream;
    AAudioStreamBuilder_openStream(streamBuilder, &stream);

## Thread safety

The AAudio API is not completely [thread safe](https://en.wikipedia.org/wiki/Thread_safety).
You cannot call some of the AAudio functions concurrently from more than one thread at a time.
This is because AAudio avoids using mutexes, which can cause thread preemption and glitches.

To be safe, don't call `AAudioStream_waitForStateChange()` or read or write to the same stream from two different threads. Similarly, don't close a stream in one thread while reading or writing to it in another thread.

Calls that return stream settings, like `AAudioStream_getSampleRate()` and `AAudioStream_getChannelCount()`, are thread safe.

These calls are also thread safe:

- `AAudio_convert*ToText()`
- `AAudio_createStreamBuilder()`
- `AAudioStream_get*()` except for `AAudioStream_getTimestamp()`

| **Note:** When a stream uses a callback function, it's safe to read/write from the callback thread while also closing the stream from the thread in which it is running.

## Known issues

- Audio latency is high for blocking write() because the Android O DP2 release doesn't use a FAST track. Use a callback to get lower latency.

## Additional resources

To learn more, take advantage of the following resources:

<br />

### API Reference

- [AAudio](https://developer.android.com/ndk/reference/group/audio)

<br />

<br />

### Codelabs

- [Making Waves Part 1 - Build a Synthesizer](https://codelabs.developers.google.com/codelabs/making-waves-1-synth/index.html)
- [Making More Waves - Sampler](https://codelabs.developers.google.com/codelabs/making-waves-2-sampler/index.html)

<br />

<br />

### Videos

- [Best Practices for Android Audio (Google I/O '17)](https://www.youtube.com/watch?v=C0BPXZIvG-Q)

<br />