---
title: https://developer.android.com/ndk/guides/audio/midi
url: https://developer.android.com/ndk/guides/audio/midi
source: md.txt
---

The [AMidi](https://developer.android.com/ndk/reference/group/midi) API is
available in Android NDK r20b and later. It gives app
developers the ability to send and receive MIDI data with C/C++code.

Android MIDI apps usually use the
[`midi`](https://developer.android.com/reference/android/media/midi/package-summary) API to communicate with the
Android MIDI service. MIDI apps primarily depend on the
[`MidiManager`](https://developer.android.com/reference/android/media/midi/MidiManager) to discover, open,
and close one or more
[`MidiDevice`](https://developer.android.com/reference/android/media/midi/MidiDevice) objects, and
pass data to and from each device via the device's
MIDI [input](https://developer.android.com/reference/android/media/midi/MidiInputPort)
and [output](https://developer.android.com/reference/android/media/midi/MidiOutputPort) ports:

![](https://developer.android.com/static/ndk/images/midi/midi.svg)

When you use AMidi you pass the address of a `MidiDevice` to the native code
layer with a JNI call. From there, AMidi creates a reference to an `AMidiDevice`
which has most of the functionality of a `MidiDevice`. Your native code uses
[AMidi functions](https://developer.android.com/ndk/reference/group/midi#functions_1) that communicate
directly with an `AMidiDevice` The `AMidiDevice` connects directly to the
MIDI service:

![](https://developer.android.com/static/ndk/images/midi/amidi.svg)

Using AMidi calls, you can integrate your app's C/C++ audio/control logic closely
with MIDI transmission. There is less need for JNI calls, or callbacks to the
Java side of your app. For example, a digital synthesizer implemented in C code could
receive key events directly from an `AMidiDevice`, rather than waiting for a JNI
call to send the events down from the Java side. Or an algorithmic composing
process could send a MIDI performance directly to an `AMidiDevice` without calling
back up to the Java side to transmit the key events.

Although AMidi improves the direct connection to MIDI devices, apps must still
use the `MidiManager` to discover and open `MidiDevice` objects. AMidi can
take it from there.

Sometimes you might need to pass information from the UI layer down to the
native code. For example, when MIDI events are sent in response to buttons on
the screen. To do this create custom JNI calls to your native logic. If you
need to send data back to update the UI, you can call back from the native layer
as usual.

This document shows how to set up an AMidi native code app, giving examples
of both sending and receiving MIDI commands.
For a complete working example check out the
[NativeMidi](https://github.com/android/ndk-samples/tree/main/native-midi)
sample app.

## Use AMidi

All apps that use AMidi have the same setup and closing steps, whether they
send or receive MIDI, or both.

### Start AMidi

On the Java side, the app must discover an
attached piece of MIDI hardware, create a corresponding `MidiDevice`,
and pass it to the native code.

1. Discover MIDI hardware with the Java `MidiManager` class.
2. Obtain a Java `MidiDevice` object corresponding to the MIDI hardware.
3. Pass the Java `MidiDevice` to native code with JNI.

#### Discover hardware and ports

The input and output port objects do not belong to the app. They represent ports
*on the midi device* . To send MIDI data to a device, an app opens a
`MIDIInputPort` and then writes data to it. Conversely, to receive data, an app
opens a `MIDIOutputPort`. To work properly, the app must be sure the ports it
opens are the correct type. Device and port discovery are done on the Java side.

Here is a method which discovers each MIDI device and looks at its
ports. It returns either a list of devices with output ports for receiving
data, or a list of devices with input ports for sending data. A MIDI device can
have both input ports and output ports.

### Kotlin

```kotlin
private fun getMidiDevices(isOutput: Boolean) : List {
    if (isOutput) {
        return mMidiManager.devices.filter { it.outputPortCount > 0 }
    } else {
        return mMidiManager.devices.filter { it.inputPortCount > 0 }
    }
}
```

### Java

```java
private List getMidiDevices(boolean isOutput){
  ArrayList filteredMidiDevices = new ArrayList<>();

  for (MidiDeviceInfo midiDevice : mMidiManager.getDevices()){
    if (isOutput){
      if (midiDevice.getOutputPortCount() > 0) filteredMidiDevices.add(midiDevice);
    } else {
      if (midiDevice.getInputPortCount() > 0) filteredMidiDevices.add(midiDevice);
    }
  }
  return filteredMidiDevices;
}
```

To use AMidi functions in your C/C++ code you must include
`AMidi/AMidi.h` and link against the `amidi` library. These can be both be found
in the [Android NDK](https://developer.android.com/ndk).

The Java side should pass one or more `MidiDevice` objects and port numbers to
the native layer via a JNI call. The native layer should then perform the
following steps:

1. For each Java `MidiDevice` obtain an `AMidiDevice` using `AMidiDevice_fromJava()`.
2. Obtain an `AMidiInputPort` and/or `AMidiOutputPort` from the `AMidiDevice` with `AMidiInputPort_open()` and/or `AMidiOutputPort_open()`.
3. Use the obtained ports to send and/or receive MIDI data.

### Stop AMidi

The Java app should signal the native layer to release resources when it is no
longer using the MIDI device. This could be because the MIDI device was
disconnected or because the app is exiting.

To release MIDI resources, your code should perform these tasks:

1. Stop reading and/or writing to MIDI ports. If you were using a reading thread to poll for input (see [Implement a polling loop](https://developer.android.com/ndk/guides/audio/midi#polling) below), stop the thread.
2. Close any open `AMidiInputPort` and/or `AMidiOutputPort` objects with `AMidiInputPort_close()` and/or `AMidiOutputPort_close()` functions.
3. Release the `AMidiDevice` with `AMidiDevice_release()`.

## Receive MIDI data

A typical example of a MIDI app that receives MIDI is a "virtual synthesizer"
that receives MIDI performance data to control audio synthesis.

Incoming MIDI data is received asynchronously. Therefore, it's best to read MIDI
in a separate thread that continuously polls one or MIDI output ports. This
could be a background thread, or an audio thread. AMidi
does not block when reading from a port and is therefore safe to use inside
an audio callback.

### Set up a MidiDevice and its output ports

An app reads incoming MIDI data from a device's output ports. The Java side
of your app must determine which device and ports to use.

This snippet creates the
`MidiManager` from Android's MIDI service and opens
a `MidiDevice` for the first device it finds. When the `MidiDevice` has been
opened a callback is received to an instance of
`MidiManager.OnDeviceOpenedListener()`. The `onDeviceOpened` method of this
listener is called which then calls `startReadingMidi()` to open output port 0
on the device. This
is a JNI function defined in `AppMidiManager.cpp`. This function is
explained in the next snippet.

### Kotlin

```kotlin
//AppMidiManager.kt
class AppMidiManager(context : Context) {
  private external fun startReadingMidi(midiDevice: MidiDevice,
  portNumber: Int)
  val mMidiManager : MidiManager = context.getSystemService(Context.MIDI_SERVICE) as MidiManager

  init {
    val midiDevices = getMidiDevices(true) // method defined in snippet above
    if (midiDevices.isNotEmpty()){
      midiManager.openDevice(midiDevices[0], {
        startReadingMidi(it, 0)
      }, null)
    }
  }
}
```

### Java

```java
//AppMidiManager.java
public class AppMidiManager {
  private native void startReadingMidi(MidiDevice device, int portNumber);
  private MidiManager mMidiManager;
  AppMidiManager(Context context){
    mMidiManager = (MidiManager)
      context.getSystemService(Context.MIDI_SERVICE);
    List midiDevices = getMidiDevices(true); // method defined in snippet above
    if (midiDevices.size() > 0){
      mMidiManager.openDevice(midiDevices.get(0),
        new MidiManager.OnDeviceOpenedListener() {
        @Override
        public void onDeviceOpened(MidiDevice device) {
          startReadingMidi(device, 0);
        }
      },null);
    }
  }
}
```

The native code translates the Java-side MIDI device and its ports into
references used by AMidi functions.

Here is the JNI function that creates an `AMidiDevice` by calling
`AMidiDevice_fromJava()`, and then calls `AMidiOutputPort_open()` to open
an output port on the device:

**AppMidiManager.cpp**

    AMidiDevice midiDevice;
    static pthread_t readThread;

    static const AMidiDevice* midiDevice = AMIDI_INVALID_HANDLE;
    static std::atomic<AMidiOutputPort*> midiOutputPort(AMIDI_INVALID_HANDLE);

    void Java_com_nativemidiapp_AppMidiManager_startReadingMidi(
            JNIEnv* env, jobject, jobject deviceObj, jint portNumber) {
        AMidiDevice_fromJava(j_env, deviceObj, &midiDevice);

        AMidiOutputPort* outputPort;
        int32_t result =
          AMidiOutputPort_open(midiDevice, portNumber, &outputPort);
        // check for errors...

        // Start read thread
        int pthread_result =
          pthread_create(&readThread, NULL, readThreadRoutine, NULL);
        // check for errors...

    }

### Implement a polling loop

Apps that receive MIDI data must poll the output port and respond when
`AMidiOutputPort_receive()` returns a number greater than zero.

For low-bandwidth apps, like a MIDI scope, you can poll in a low-priority
background thread (with appropriate sleeps).

For apps that generate audio and have stricter realtime performance
requirements, you can poll in the main audio generation callback (the
`BufferQueue` callback for OpenSL ES, the AudioStream data callback in AAudio).
Since `AMidiOutputPort_receive()` is non-blocking, there is very little
performance impact.

The function `readThreadRoutine()` called from the `startReadingMidi()` function
above might look like this:

    void* readThreadRoutine(void * /*context*/) {
        uint8_t inDataBuffer[SIZE_DATABUFFER];
        int32_t numMessages;
        uint32_t opCode;
        uint64_t timestamp;
        reading = true;
        while (reading) {
            AMidiOutputPort* outputPort = midiOutputPort.load();
            numMessages =
                  AMidiOutputPort_receive(outputPort, &opCode, inDataBuffer,
                                    sizeof(inDataBuffer), &timestamp);
            if (numMessages >= 0) {
                if (opCode == AMIDI_OPCODE_DATA) {
                    // Dispatch the MIDI data....
                }
            } else {
                // some error occurred, the negative numMessages is the error code
                int32_t errorCode = numMessages;
            }
      }
    }

An app using a native audio API (like OpenSL ES, or
AAudio) can add MIDI receive code to the audio generation callback like this:

    void bqPlayerCallback(SLAndroidSimpleBufferQueueItf bq, void */*context*/)
    {
        uint8_t inDataBuffer[SIZE_DATABUFFER];
        int32_t numMessages;
        uint32_t opCode;
        uint64_t timestamp;

        // Read MIDI Data
        numMessages = AMidiOutputPort_receive(outputPort, &opCode, inDataBuffer,
            sizeof(inDataBuffer), &timestamp);
        if (numMessages >= 0 && opCode == AMIDI_OPCODE_DATA) {
            // Parse and respond to MIDI data
            // ...
        }

        // Generate Audio...
        // ...
    }

The following diagram illustrates the flow of a MIDI reading app:

![](https://developer.android.com/static/ndk/images/midi/midi-reading-flow.png)

## Send MIDI data

A typical example of a MIDI writing app is a MIDI controller or sequencer.

### Set up a MidiDevice and its input ports

An app writes outgoing MIDI data to a MIDI device's input ports. The Java side
of your app must determine which MIDI device and ports to use.

This setup code below is a variation on the receiving example above. It creates the `MidiManager`
from Android's MIDI service. It then opens the first`MidiDevice` it finds and
calls `startWritingMidi()` to open the first input port on the device. This is a
JNI call defined in `AppMidiManager.cpp`. The function is explained in the
next snippet.

### Kotlin

```kotlin
//AppMidiManager.kt
class AppMidiManager(context : Context) {
  private external fun startWritingMidi(midiDevice: MidiDevice,
  portNumber: Int)
  val mMidiManager : MidiManager = context.getSystemService(Context.MIDI_SERVICE) as MidiManager

  init {
    val midiDevices = getMidiDevices(false) // method defined in snippet above
    if (midiDevices.isNotEmpty()){
      midiManager.openDevice(midiDevices[0], {
        startWritingMidi(it, 0)
      }, null)
    }
  }
}
```

### Java

```java
//AppMidiManager.java
public class AppMidiManager {
  private native void startWritingMidi(MidiDevice device, int portNumber);
  private MidiManager mMidiManager;

  AppMidiManager(Context context){
    mMidiManager = (MidiManager)
      context.getSystemService(Context.MIDI_SERVICE);
    List midiDevices = getMidiDevices(false); // method defined in snippet above
    if (midiDevices.size() > 0){
      mMidiManager.openDevice(midiDevices.get(0),
        new MidiManager.OnDeviceOpenedListener() {
        @Override
        public void onDeviceOpened(MidiDevice device) {
          startWritingMidi(device, 0);
        }
      },null);
    }
  }
}
```

Here is the JNI function that creates an `AMidiDevice` by calling
`AMidiDevice_fromJava()`, and then calls `AMidiInputPort_open()` to open
an input port on the device:

**AppMidiManager.cpp**

    void Java_com_nativemidiapp_AppMidiManager_startWritingMidi(
           JNIEnv* env, jobject, jobject midiDeviceObj, jint portNumber) {
       media_status_t status;
       status = AMidiDevice_fromJava(
         env, midiDeviceObj, &sNativeSendDevice);
       AMidiInputPort *inputPort;
       status = AMidiInputPort_open(
         sNativeSendDevice, portNumber, &inputPort);

       // store it in a global
       sMidiInputPort = inputPort;
    }

### Send MIDI data

Since the timing of the outgoing MIDI data is well understood and controlled by
the app itself, the data transmission can be done in the MIDI app's main thread.
However, for performance reasons (as in a sequencer) the generation and
transmission of MIDI can be done in a separate thread.

Apps can send MIDI data whenever required. Note that AMidi blocks when
writing data.

Here is an example JNI method that receives a buffer of MIDI commands and
writes it out:

    void Java_com_nativemidiapp_TBMidiManager_writeMidi(
    JNIEnv* env, jobject, jbyteArray data, jint numBytes) {
       jbyte* bufferPtr = env->GetByteArrayElements(data, NULL);
       AMidiInputPort_send(sMidiInputPort, (uint8_t*)bufferPtr, numBytes);
       env->ReleaseByteArrayElements(data, bufferPtr, JNI_ABORT);
    }

The following diagram illustrates the flow of a MIDI writing app:

![](https://developer.android.com/static/ndk/images/midi/midi-producing-flow.png)

## Callbacks

Though not strictly an AMidi feature, your native code may need to pass data
back to the Java side (to update the UI for example). To do that, you must
write code in the Java side and the native layer:

- Create a callback method on the Java side.
- Write a JNI function that stores the information needed to invoke the callback.

When its time to callback, your native code can construct

Here is the Java-side callback method, `onNativeMessageReceive()`:

### Kotlin

```kotlin
//MainActivity.kt
private fun onNativeMessageReceive(message: ByteArray) {
  // Messages are received on some other thread, so switch to the UI thread
  // before attempting to access the UI
  runOnUiThread { showReceivedMessage(message) }
}
```

### Java

```java
//MainActivity.java
private void onNativeMessageReceive(final byte[] message) {
        // Messages are received on some other thread, so switch to the UI thread
        // before attempting to access the UI
        runOnUiThread(new Runnable() {
            public void run() {
                showReceivedMessage(message);
            }
        });
}
```

Here is the C code for the JNI function that sets up thea callback to
`MainActivity.onNativeMessageReceive()`. Java `MainActivity` calls
`initNative()` at startup:

**MainActivity.cpp**

    /**
     * Initializes JNI interface stuff, specifically the info needed to call back into the Java
     * layer when MIDI data is received.
     */
    JNICALL void Java_com_example_nativemidi_MainActivity_initNative(JNIEnv * env, jobject instance) {
        env->GetJavaVM(&theJvm);

        // Setup the receive data callback (into Java)
        jclass clsMainActivity = env->FindClass("com/example/nativemidi/MainActivity");
        dataCallbackObj = env->NewGlobalRef(instance);
        midDataCallback = env->GetMethodID(clsMainActivity, "onNativeMessageReceive", "([B)V");
    }

When it's time to send data back to Java, the native code retrieves the callback
pointers and constructs the callback:

**AppMidiManager.cpp**

    // The Data Callback
    extern JavaVM* theJvm;              // Need this for allocating data buffer for...
    extern jobject dataCallbackObj;     // This is the (Java) object that implements...
    extern jmethodID midDataCallback;   // ...this callback routine

    static void SendTheReceivedData(uint8_t* data, int numBytes) {
        JNIEnv* env;
        theJvm->AttachCurrentThread(&env, NULL);
        if (env == NULL) {
            LOGE("Error retrieving JNI Env");
        }

        // Allocate the Java array and fill with received data
        jbyteArray ret = env->NewByteArray(numBytes);
        env->SetByteArrayRegion (ret, 0, numBytes, (jbyte*)data);

        // send it to the (Java) callback
        env->CallVoidMethod(dataCallbackObj, midDataCallback, ret);
    }

## Additional resources

- [AMidi reference](https://developer.android.com/ndk/reference/group/midi)
- See the complete [Native MIDI sample app](https://github.com/android/ndk-samples/tree/main/native-midi) on github.