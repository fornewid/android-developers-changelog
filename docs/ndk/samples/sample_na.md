---
title: https://developer.android.com/ndk/samples/sample_na
url: https://developer.android.com/ndk/samples/sample_na
source: md.txt
---

# Sample: native-activity

The native-activity sample resides under the[NDK samples root](https://github.com/android/ndk-samples/), in folder`native-activity`. It is a very simple example of a purely native application, with no Java source code. In the absence of any Java source, the Java compiler still creates an executable stub for the virtual machine to run. The stub serves as a wrapper for the actual, native program, which is located in the`.so`file.

The app itself simply renders a color onto the entire screen, and then changes the color partly in response to movement that it detects.

## AndroidManifest.xml

An app with only native code must not specify an Android API level lower than 9, which introduced the[`NativeActivity`](https://developer.android.com/ndk/guides/concepts#naa)framework class.  

```xml
<uses-sdk android:minSdkVersion="9" />
```

The following line declares`android:hasCode`as`false`, as this app has only native code--no Java.  

```xml
<application android:label="@string/app_name"
android:hasCode="false">
```

The next line declares the`NativeActivity`class.  

```xml
<activity android:name="android.app.NativeActivity"
```

Finally, the manifest specifies`android:value`as the name of the shared library to be built, minus the initial`lib`and the`.so`extension. This value must be the same as the name of`LOCAL_MODULE`in`Android.mk`.  

```xml
<meta-data android:name="android.app.lib_name"
        android:value="native-activity" />
```

## Android.mk

This file begins by providing the name of the shared library to generate.  

```
LOCAL_MODULE    := native-activity
```

Next, it declares the name of the native source-code file.  

```
LOCAL_SRC_FILES := main.c
```

Next, it lists the external libraries for the build system to use in building the binary. The`-l`(link-against) option precedes each library name.

- `log`is a logging library.
- `android`encompasses the standard Android support APIs for NDK. For more information about the APIs that Android and the NDK support, see[Android NDK Native APIs](https://developer.android.com/ndk/guides/stable_apis).
- `EGL`corresponds to the platform-specific portion of the graphics API.
- `GLESv1_CM`corresponds to OpenGL ES, the version of OpenGL for Android. This library depends on EGL.

For each library:

- The actual file name starts with`lib`, and ends with the`.so`extension. For example, the actual file name for the`log`library is`liblog.so`.
- The library resides in the following directory, NDK root:`<ndk>/platforms/android-<sdk_version>/arch-<abi>/usr/lib/`.

```
LOCAL_LDLIBS    := -llog -landroid -lEGL -lGLESv1_CM
```

The next line provides the name of the static library,`android_native_app_glue`, which the application uses to manage`NativeActivity`lifecycle events and touch input.  

```
LOCAL_STATIC_LIBRARIES := android_native_app_glue
```

The final line tells the build system to build this static library. The`ndk-build`script places the built library (`libandroid_native_app_glue.a`) into the`obj`directory generated during the build process. For more information about the`android_native_app_glue`library, see its`android_native_app_glue.h`header and corresponding`.c`source file.  

```
$(call import-module,android/native_app_glue)
```

For more information about the`Android.mk`file, see[Android.mk](https://developer.android.com/ndk/guides/android_mk).

## main.c

This file essentially contains the entire progam.

The following includes correspond to the libraries, both shared and static, enumerated in`Android.mk`.  

```c++
#include <EGL/egl.h>
#include <GLES/gl.h>


#include <android/sensor.h>
#include <android/log.h>
#include <android_native_app_glue>
```

The`android_native_app_glue`library calls the following function, passing it a predefined state structure. It also serves as a wrapper that simplifies handling of`NativeActivity`callbacks.  

```c++
void android_main(struct android_app* state) {
```

Next, the program handles events queued by the glue library. The event handler follows the state structure.  

```c++
struct engine engine;



// Suppress link-time optimization that removes unreferenced code
// to make sure glue isn't stripped.
app_dummy();


memset(&engine, 0, sizeof(engine));
state->userData = &engine;
state->onAppCmd = engine_handle_cmd;
state->onInputEvent = engine_handle_input;
engine.app = state;
```

The application prepares to start monitoring the sensors, using the APIs in`sensor.h`.  

```c++
    engine.sensorManager = ASensorManager_getInstance();
    engine.accelerometerSensor =
                    ASensorManager_getDefaultSensor(engine.sensorManager,
                        ASENSOR_TYPE_ACCELEROMETER);
    engine.sensorEventQueue =
                    ASensorManager_createEventQueue(engine.sensorManager,
                        state->looper, LOOPER_ID_USER, NULL, NULL);
```

Next, a loop begins, in which the application polls the system for messages (sensor events). It sends messages to`android_native_app_glue`, which checks to see whether they match any`onAppCmd`events defined in`android_main`. When a match occurs, the message is sent to the handler for execution.  

```c++
while (1) {
        // Read all pending events.
        int ident;
        int events;
        struct android_poll_source* source;


        // If not animating, we will block forever waiting for events.
        // If animating, we loop until all events are read, then continue
        // to draw the next frame of animation.
        while ((ident=ALooper_pollAll(engine.animating ? 0 : -1, NULL,
                &events,
                (void**)&source)) >= 0) {


            // Process this event.
            if (source != NULL) {
                source->process(state, source);
            }


            // If a sensor has data, process it now.
            if (ident == LOOPER_ID_USER) {
                if (engine.accelerometerSensor != NULL) {
                    ASensorEvent event;
                    while (ASensorEventQueue_getEvents(engine.sensorEventQueue,
                            &event, 1) > 0) {
                        LOGI("accelerometer: x=%f y=%f z=%f",
                                event.acceleration.x, event.acceleration.y,
                                event.acceleration.z);
                    }
                }
            }


        // Check if we are exiting.
        if (state->destroyRequested != 0) {
            engine_term_display(&engine);
            return;
        }
    }
```

Once the queue is empty, and the program exits the polling loop, the program calls OpenGL to draw the screen.  

```c++
    if (engine.animating) {
        // Done with events; draw next animation frame.
        engine.state.angle += .01f;
        if (engine.state.angle > 1) {
            engine.state.angle = 0;
        }


        // Drawing is throttled to the screen update rate, so there
        // is no need to do timing here.
        engine_draw_frame(&engine);
    }
}
```