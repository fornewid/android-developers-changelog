---
title: https://developer.android.com/ndk/samples/sample_teapot
url: https://developer.android.com/ndk/samples/sample_teapot
source: md.txt
---

# Sample: Teapot

The Teapot sample is located under in the`samples/Teapot/`directory, under the NDK installation's root directory. This sample uses the OpenGL library to render the iconic[Utah teapot](http://math.hws.edu/bridgeman/courses/324/s06/doc/opengl.html#basic). In particular, it showcases the`ndk_helper`helper class, a collection of native helper functions required for implementing games and similar applications as native applications. This class provides:

- An abstraction layer,`GLContext`, that handles certain NDK-specific behaviors.
- Helper functions that are useful but not present in the NDK, such as tap detection.
- Wrappers for JNI calls for platform features such as texture loading.

## AndroidManifest.xml

The activity declaration here is not[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)itself, but a subclass of it:`TeapotNativeActivity`.  

```xml
<activity android:name="com.sample.teapot.TeapotNativeActivity"
        android:label="@string/app_name"
        android:configChanges="orientation|keyboardHidden">
```

Ultimately, the name of the shared-object file that the build system builds is`libTeapotNativeActivity.so`. The build system adds the`lib`prefix and the`.so`extension; neither is part of the value that the manifest originally assigns to`android:value`.  

```xml
<meta-data android:name="android.app.lib_name"
        android:value="TeapotNativeActivity" />
```

## Application.mk

An app that uses the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)framework class must not specify an Android API level lower than 9, which introduced that class. For more information about the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class, see[Native Activities and Applications](https://developer.android.com/ndk/guides/concepts#naa).  

```
APP_PLATFORM := android-9
```

The next line tells the build system to build for all supported architectures.  

```
APP_ABI := all
```

Next, the file tells the build system which[C++ runtime support library](https://developer.android.com/ndk/guides/cpp-support)to use.  

```
APP_STL := stlport_static
```

## Java-side Implementation

The`TeapotNativeActivity`file is located in`teapots/classic-teapot/src/com/sample/teapot`, under the[NDK repo root directory](https://github.com/android/ndk-samples)on GitHub. It handles activity lifecycle events, creates a popup window to display text on the screen with the function`ShowUI()`, and update frame rate dynamically with the function`updateFPS()`. The following code might be interesting to you in that it prepares the app's Activity to be full screen, immersive, and without system navigation bars, so that the whole screen could be used for displaying rendered teapot frames:

<br />

### Kotlin

```kotlin
fun setImmersiveSticky() {
    window.decorView.systemUiVisibility = (
            View.SYSTEM_UI_FLAG_FULLSCREEN
                    or View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                    or View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                    or View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                    or View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                    or View.SYSTEM_UI_FLAG_LAYOUT_STABLE
            )
}
```

### Java

```java
void setImmersiveSticky() {
    View decorView = getWindow().getDecorView();
    decorView.setSystemUiVisibility(View.SYSTEM_UI_FLAG_FULLSCREEN
            | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
            | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
            | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
            | View.SYSTEM_UI_FLAG_LAYOUT_STABLE);
}
```

## Native-side Implementation

This section explores the part of the Teapot app implemented in C++.

### TeapotRenderer.h

These function calls perform the actual rendering of the teapot. It uses`ndk_helper`for matrix calculation and to reposition the camera based on where the user taps.  

```c++
ndk_helper::Mat4 mat_projection_;
ndk_helper::Mat4 mat_view_;
ndk_helper::Mat4 mat_model_;


ndk_helper::TapCamera* camera_;
```

### TeapotNativeActivity.cpp

The following lines include`ndk_helper`in the native source file, and define the helper-class name.  

```c++
#include "NDKHelper.h"

//-------------------------------------------------------------------------
//Preprocessor
//-------------------------------------------------------------------------
#define HELPER_CLASS_NAME "com/sample/helper/NDKHelper" //Class name of helper
function
```

The first use of the`ndk_helper`class is to handle the EGL-related lifecycle, associating EGL context states (created/lost) with Android lifecycle events. The`ndk_helper`class enables the application to preserve context information so that the system can restore a destroyed activity. This ability is useful, for example, when the target machine is rotated (causing an activity to be destroyed, then immediately restored in the new orientation), or when the lock screen appears.  

```c++
ndk_helper::GLContext* gl_context_; // handles EGL-related lifecycle.
```

Next,`ndk_helper`provides touch control.  

```c++
ndk_helper::DoubletapDetector doubletap_detector_;
ndk_helper::PinchDetector pinch_detector_;
ndk_helper::DragDetector drag_detector_;
ndk_helper::PerfMonitor monitor_;
```

It also provides camera control (openGL view frustum).  

```c++
ndk_helper::TapCamera tap_camera_;
```

The app then prepares to use the device's sensors, using the native APIs provided in the NDK.  

```c++
ASensorManager* sensor_manager_;
const ASensor* accelerometer_sensor_;
ASensorEventQueue* sensor_event_queue_;
```

The app calls the following functions in response to various Android lifecycle events and EGL context state changes, using various functionalities provided by`ndk_helper`via the`Engine`class.  

```c++
void LoadResources();
void UnloadResources();
void DrawFrame();
void TermDisplay();
void TrimMemory();
bool IsReady();
```

Then, the following function calls back to the Java side to update the UI display.  

```c++
void Engine::ShowUI()
{
    JNIEnv *jni;
    app_->activity->vm->AttachCurrentThread( &jni, NULL );


    //Default class retrieval
    jclass clazz = jni->GetObjectClass( app_->activity->clazz );
    jmethodID methodID = jni->GetMethodID( clazz, "showUI", "()V" );
    jni->CallVoidMethod( app_->activity->clazz, methodID );


    app_->activity->vm->DetachCurrentThread();
    return;
}
```

Next, this function calls back to the Java side to draw a text box superimposed on the screen rendered on the native side, and showing frame count.  

```c++
void Engine::UpdateFPS( float fFPS )
{
    JNIEnv *jni;
    app_->activity->vm->AttachCurrentThread( &jni, NULL );


    //Default class retrieval
    jclass clazz = jni->GetObjectClass( app_->activity->clazz );
    jmethodID methodID = jni->GetMethodID( clazz, "updateFPS", "(F)V" );
    jni->CallVoidMethod( app_->activity->clazz, methodID, fFPS );


    app_->activity->vm->DetachCurrentThread();
    return;
}
```

The application gets the system clock and supplies it to the renderer for time-based animation based on real-time clock. This information is used, for example, in calculating momentum, where speed declines as a function of time.  

```c++
renderer_.Update( monitor_.GetCurrentTime() );
```

The application now flips the rendered frame to the front buffer for display through`GLcontext::Swap()`function; it also handles possible errors happened during the flipping process.  

```c++
if( EGL_SUCCESS != gl_context_->Swap() )  // swaps
buffer.
```

The program passes touch-motion events to the gesture detector defined in the`ndk_helper`class. The gesture detector tracks multitouch gestures, such as pinch-and-drag, and sends a notification when triggered by any of these events.  

```c++
if( AInputEvent_getType( event ) == AINPUT_EVENT_TYPE_MOTION )
{
    ndk_helper::GESTURE_STATE doubleTapState =
        eng->doubletap_detector_.Detect( event );
    ndk_helper::GESTURE_STATE dragState = eng->drag_detector_.Detect( event );
    ndk_helper::GESTURE_STATE pinchState = eng->pinch_detector_.Detect( event );

    //Double tap detector has a priority over other detectors
    if( doubleTapState == ndk_helper::GESTURE_STATE_ACTION )
    {
        //Detect double tap
        eng->tap_camera_.Reset( true );
    }
    else
    {
        //Handle drag state
        if( dragState & ndk_helper::GESTURE_STATE_START )
        {
             //Otherwise, start dragging
             ndk_helper::Vec2 v;
             eng->drag_detector_.GetPointer( v );
             eng->TransformPosition( v );
             eng->tap_camera_.BeginDrag( v );
        }
        // ...else other possible drag states...

        //Handle pinch state
        if( pinchState & ndk_helper::GESTURE_STATE_START )
        {
            //Start new pinch
            ndk_helper::Vec2 v1;
            ndk_helper::Vec2 v2;
            eng->pinch_detector_.GetPointers( v1, v2 );
            eng->TransformPosition( v1 );
            eng->TransformPosition( v2 );
            eng->tap_camera_.BeginPinch( v1, v2 );
        }
        // ...else other possible pinch states...
    }
    return 1;
}
```

The`ndk_helper`class also provides access to a vector-math library (`vecmath.h`), using it here to transform touch coordinates.  

```c++
void Engine::TransformPosition( ndk_helper::Vec2& vec )
{
    vec = ndk_helper::Vec2( 2.0f, 2.0f ) * vec
            / ndk_helper::Vec2( gl_context_->GetScreenWidth(),
            gl_context_->GetScreenHeight() ) - ndk_helper::Vec2( 1.f, 1.f );
}
```

The`HandleCmd()`method handles commands posted from the android_native_app_glue library. For more information about what the messages mean, refer to the comments in the`android_native_app_glue.h`and`.c`source files.  

```c++
void Engine::HandleCmd( struct android_app* app,
        int32_t cmd )
{
    Engine* eng = (Engine*) app->userData;
    switch( cmd )
    {
    case APP_CMD_SAVE_STATE:
        break;
    case APP_CMD_INIT_WINDOW:
        // The window is being shown, get it ready.
        if( app->window != NULL )
        {
            eng->InitDisplay();
            eng->DrawFrame();
        }
        break;
    case APP_CMD_TERM_WINDOW:
        // The window is being hidden or closed, clean it up.
        eng->TermDisplay();
        eng->has_focus_ = false;
        break;
    case APP_CMD_STOP:
        break;
    case APP_CMD_GAINED_FOCUS:
        eng->ResumeSensors();
        //Start animation
        eng->has_focus_ = true;
        break;
    case APP_CMD_LOST_FOCUS:
        eng->SuspendSensors();
        // Also stop animating.
        eng->has_focus_ = false;
        eng->DrawFrame();
        break;
    case APP_CMD_LOW_MEMORY:
        //Free up GL resources
        eng->TrimMemory();
        break;
    }
}
```

The`ndk_helper`class posts`APP_CMD_INIT_WINDOW`when`android_app_glue`receives an`onNativeWindowCreated()`callback from the system. Applications can normally perform window initializations, such as EGL initialization. They do this outside of the activity lifecycle, since the activity is not yet ready.  

```c++
//Init helper functions
ndk_helper::JNIHelper::Init( state->activity, HELPER_CLASS_NAME );

state->userData = &g_engine;
state->onAppCmd = Engine::HandleCmd;
state->onInputEvent = Engine::HandleInput;
```