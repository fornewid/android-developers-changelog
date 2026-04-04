---
title: https://developer.android.com/games/agdk/game-activity/get-started
url: https://developer.android.com/games/agdk/game-activity/get-started
source: md.txt
---

# Get started with GameActivityPart of[Android Game Development Kit](https://developer.android.com/games/agdk/overview).

This guide describes how to set up and integrate[`GameActivity`](https://developer.android.com/games/agdk/game-activity)and handle events in your Android game.

[`GameActivity`](https://developer.android.com/reference/games/game-activity)helps you bring your C or C++ game to Android by simplifying the process of using critical APIs. Previously[`NativeActivity`](https://developer.android.com/reference/android/app/NativeActivity)was the recommended class for games.`GameActivity`replaces it as the recommended class for games, and is backwards compatible to API level 19.

For a sample that integrates GameActivity, see the[games-samples repository](https://github.com/android/games-samples).

## Before you start

See[`GameActivity`releases](https://developer.android.com/games/agdk/game-activity#releases)to obtain a distribution.

## Set up your build

On Android, an[`Activity`](https://developer.android.com/reference/android/app/Activity)serves as the entry point for your game, and also provides the[`Window`](https://developer.android.com/reference/android/view/Window)to draw within. Many games extend this`Activity`with their own Java or Kotlin class to defeat limitations in`NativeActivity`while using[`JNI`](https://developer.android.com/training/articles/perf-jni)code to bridge to their C or C++ game code.

`GameActivity`offers the following capabilities:

- Inherits from[`AppCompatActivity`](https://developer.android.com/reference/androidx/appcompat/app/AppCompatActivity), allowing you to use[Android Jetpack Architecture Components](https://developer.android.com/topic/libraries/architecture).

- Renders into a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView)that allows you to interface with any other Android UI element.

- Handles Java activity events. This allows any Android UI element (such as a[`EditText`](https://developer.android.com/reference/android/widget/EditText), a[`WebView`](https://developer.android.com/reference/android/webkit/WebView)or an[`Ad`](https://developers.google.com/admob/android/quick-start)) to be integrated to your game via a C interface.

- Offers a C API similar to[`NativeActivity`](https://developer.android.com/reference/android/app/NativeActivity), and[`android_native_app_glue`](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue)library.

`GameActivity`is distributed as an[Android Archive (AAR)](https://developer.android.com/studio/projects/android-library). This AAR contains the Java class that you use in your[`AndroidManifest.xml`](https://developer.android.com/guide/topics/manifest/manifest-intro), as well as the C and C++ source code that connects the Java side of`GameActivity`to the app's C/C++ implementation. If you're using`GameActivity`1.2.2 or later, the C/C++ static library is also provided. Whenever applicable, we recommend that you use the static library instead of the source code.

Include these source files or the static library as part of your build process through[`Prefab`](https://developer.android.com/studio/build/dependencies?agpversion=4.1#native-dependencies-aars), which exposes native libraries and source code to your[CMake project](https://developer.android.com/ndk/guides/cmake)or[NDK build](https://developer.android.com/ndk/guides).

1. Follow the instructions at the[Jetpack Android Games](https://developer.android.com/jetpack/androidx/releases/games)page to add the`GameActivity`library dependency to your game's`build.gradle`file.

2. Enable prefab by doing the following with[Android Plugin Version (AGP) 4.1+](https://developer.android.com/studio/releases/gradle-plugin):

   - Add the following to the`android`block of your module's`build.gradle`file:

       buildFeatures {
           prefab true
       }

   - Pick[a Prefab version](https://github.com/google/prefab/releases), and set it to the`gradle.properties`file:

       android.prefabVersion=2.0.0

   If you use earlier AGP versions, follow[the prefab documentation](https://developer.android.com/studio/build/dependencies?agpversion=4.0#native-dependencies-aars)for the corresponding configuration instructions.
3. Import either the C/C++ static library or the C/++ source code into your project as follows.

   ### Static library

   In your project's`CMakeLists.txt`file, import the`game-activity`static library into the`game-activity_static`prefab module:  

       find_package(game-activity REQUIRED CONFIG)
       target_link_libraries(${PROJECT_NAME} PUBLIC log android
       game-activity::game-activity_static)

   ### Source code

   In your project's`CMakeLists.txt`file, import the`game-activity`package and add it to your target. The`game-activity`package requires`libandroid.so`, so if it's missing, you must also import it.  

       find_package(game-activity REQUIRED CONFIG)
       ...
       target_link_libraries(... android game-activity::game-activity)

   Also, include the following files into your project's`CmakeLists.txt`:`GameActivity.cpp`,`GameTextInput.cpp`, and`android_native_app_glue.c`.

## How Android launches your Activity

The Android system executes code in your Activity instance by invoking callback methods that correspond to specific stages of the activity lifecycle. In order for Android to launch your activity and start your game, you need to declare your activity with the appropriate attributes in the Android Manifest. For more information, see[Introduction to Activities](https://developer.android.com/guide/components/activities/intro-activities).

### Android Manifest

Every app project must have an[AndroidManifest.xml](https://developer.android.com/guide/topics/manifest/manifest-intro)file at the root of the project source set. The manifest file describes essential information about your app to the Android build tools, the Android operating system, and Google Play. This includes:

- [Package name and app ID](https://developer.android.com/studio/configure-app-module#set-namespace)to uniquely identify your game on Google Play.

- [App Components](https://developer.android.com/guide/topics/manifest/manifest-intro#components)such as activities, services, broadcast receivers, and content providers.

- [Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro#perms)to access protected parts of the system or other apps.

- [Device compatibility](https://developer.android.com/guide/topics/manifest/manifest-intro#compatibility)to specify hardware and software requirements for your game.

- Native library name for`GameActivity`and`NativeActivity`([default is libmain.so](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/GameActivity/src/main/java/com/google/androidgamesdk/GameActivity.java#236)).

## Implement GameActivity in your game

1. Create or identify your main activity Java class (the one specified in the`activity`element inside your`AndroidManifest.xml`file). Change this class to extend`GameActivity`from the`com.google.androidgamesdk`package:

       import com.google.androidgamesdk.GameActivity;

       public class YourGameActivity extends GameActivity { ... }

2. Make sure your native library is loaded at the start using a static block:

       public class EndlessTunnelActivity extends GameActivity {
         static {
           // Load the native library.
           // The name "android-game" depends on your CMake configuration, must be
           // consistent here and inside AndroidManifect.xml
           System.loadLibrary("android-game");
         }
         ...
       }

3. Add your native library to[`AndroidManifest.xml`](https://github.com/android/games-samples/blob/f7adb2d0ce2e08268dab8b5cf8ebda89e72fe744/agdk/agdktunnel/app/src/main/AndroidManifest.xml#L39)if your library name is not the default name (`libmain.so`):

       <meta-data android:name="android.app.lib_name"
        android:value="android-game" />

### Implement android_main

1. The`android_native_app_glue`library is a source code library that your game uses to manage`GameActivity`lifecycle events in a separate thread in order to prevent blocking in your main thread. When using the library, you register the callback to handle lifecycle events, such as touch input events. The`GameActivity`archive includes its own version of the`android_native_app_glue`library, so you can not use the version included in NDK releases. If your games are using the`android_native_app_glue`library that's included in the NDK, switch to the`GameActivity`version.

   After you add the`android_native_app_glue`library source code to your project, it interfaces with`GameActivity`. Implement a function called[`android_main`](https://developer.android.com/ndk/samples/sample_na#mac), which is called by the library and used as the entry point for your game. It is passed a structure called[`android_app`](https://developer.android.com/reference/games/game-activity/struct/android-app). This may differ for your game and engine. Here's an example:  

       #include <game-activity/native_app_glue/android_native_app_glue.h>

       extern "C" {
           void android_main(struct android_app* state);
       };

       void android_main(struct android_app* app) {
           NativeEngine *engine = new NativeEngine(app);
           engine->GameLoop();
           delete engine;
       }

2. Process`android_app`in your main game loop, such as polling and handling app cycle events defined in[NativeAppGlueAppCmd](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue#nativeappglueappcmd). For example, the following snippet registers function`_hand_cmd_proxy`as the`NativeAppGlueAppCmd`handler, then polls app cycle events, and sends them to the registered handler(in`android_app::onAppCmd`) for processing:

       void NativeEngine::GameLoop() {
         mApp->userData = this;
         mApp->onAppCmd = _handle_cmd_proxy;  // register your command handler.
         mApp->textInputState = 0;

         while (1) {
           int events;
           struct android_poll_source* source;

           // If not animating, block until we get an event;
           // If animating, don't block.
           while ((ALooper_pollOnce(IsAnimating() ? 0 : -1, NULL, &events,
             (void **) &source)) >= 0) {
               if (source != NULL) {
                   // process events, native_app_glue internally sends the outstanding
                   // application lifecycle events to mApp->onAppCmd.
                   source->process(source->app, source);
               }
               if (mApp->destroyRequested) {
                   return;
               }
           }
           if (IsAnimating()) {
               DoFrame();
           }
         }
       }

3. For further reading, study the implementation of the[Endless Tunnel](https://github.com/android/ndk-samples/tree/master/endless-tunnel)NDK example. The main difference will be how to handle events as shown in the next section.

## Handle events

To enable input events to reach your app, create and register your event filters with[`android_app_set_motion_event_filter`](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue#android_app_set_motion_event_filter)and[`android_app_set_key_event_filter`](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue#android_app_set_key_event_filter). By default,`native_app_glue`library only allows motion events from[SOURCE_TOUCHSCREEN](https://developer.android.com/reference/android/view/InputDevice#SOURCE_TOUCHSCREEN)input. Make sure to check out[the reference doc](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue#android_motion_event_filter)and the`android_native_app_glue`implmenetation code for the details.

To handle input events, get a reference to the`android_input_buffer`with[`android_app_swap_input_buffers()`](https://developer.android.com/reference/games/game-activity/group/android-native-app-glue#android_app_swap_input_buffers)in your game loop. These contain[motion events](https://developer.android.com/reference/android/view/MotionEvent)and[key events](https://developer.android.com/reference/android/view/KeyEvent)that have happened since the last time it was polled. The number of events contained is stored in`motionEventsCount`, and`keyEventsCount`respectively.
| **Note:** In the platform's`NativeActivity`, the`AInputQueue* inputQueue`field was used to handle input events. With`GameActivity`, this field has been removed from the`android_app`and no longer used for handling input events.

1. Iterate and handle each event in your game loop. In this example, the following code iterates`motionEvents`and handles them via`handle_event`:

       android_input_buffer* inputBuffer = android_app_swap_input_buffers(app);
       if (inputBuffer && inputBuffer->motionEventsCount) {
           for (uint64_t i = 0; i < inputBuffer->motionEventsCount; ++i) {
               GameActivityMotionEvent* motionEvent = &inputBuffer->motionEvents[i];

               if (motionEvent->pointerCount > 0) {
                   const int action = motionEvent->action;
                   const int actionMasked = action & AMOTION_EVENT_ACTION_MASK;
                   // Initialize pointerIndex to the max size, we only cook an
                   // event at the end of the function if pointerIndex is set to a valid index range
                   uint32_t pointerIndex = GAMEACTIVITY_MAX_NUM_POINTERS_IN_MOTION_EVENT;
                   struct CookedEvent ev;
                   memset(&ev, 0, sizeof(ev));
                   ev.motionIsOnScreen = motionEvent->source == AINPUT_SOURCE_TOUCHSCREEN;
                   if (ev.motionIsOnScreen) {
                       // use screen size as the motion range
                       ev.motionMinX = 0.0f;
                       ev.motionMaxX = SceneManager::GetInstance()->GetScreenWidth();
                       ev.motionMinY = 0.0f;
                       ev.motionMaxY = SceneManager::GetInstance()->GetScreenHeight();
                   }

                   switch (actionMasked) {
                       case AMOTION_EVENT_ACTION_DOWN:
                           pointerIndex = 0;
                           ev.type = COOKED_EVENT_TYPE_POINTER_DOWN;
                           break;
                       case AMOTION_EVENT_ACTION_POINTER_DOWN:
                           pointerIndex = ((action & AMOTION_EVENT_ACTION_POINTER_INDEX_MASK)
                                          >> AMOTION_EVENT_ACTION_POINTER_INDEX_SHIFT);
                           ev.type = COOKED_EVENT_TYPE_POINTER_DOWN;
                           break;
                       case AMOTION_EVENT_ACTION_UP:
                           pointerIndex = 0;
                           ev.type = COOKED_EVENT_TYPE_POINTER_UP;
                           break;
                       case AMOTION_EVENT_ACTION_POINTER_UP:
                           pointerIndex = ((action & AMOTION_EVENT_ACTION_POINTER_INDEX_MASK)
                                          >> AMOTION_EVENT_ACTION_POINTER_INDEX_SHIFT);
                           ev.type = COOKED_EVENT_TYPE_POINTER_UP;
                           break;
                       case AMOTION_EVENT_ACTION_MOVE: {
                           // Move includes all active pointers, so loop and process them here,
                           // we do not set pointerIndex since we are cooking the events in
                           // this loop rather than at the bottom of the function
                           ev.type = COOKED_EVENT_TYPE_POINTER_MOVE;
                           for (uint32_t i = 0; i < motionEvent->pointerCount; ++i) {
                               _cookEventForPointerIndex(motionEvent, callback, ev, i);
                           }
                           break;
                       }
                       default:
                           break;
                   }

                   // Only cook an event if we set the pointerIndex to a valid range, note that
                   // move events cook above in the switch statement.
                   if (pointerIndex != GAMEACTIVITY_MAX_NUM_POINTERS_IN_MOTION_EVENT) {
                       _cookEventForPointerIndex(motionEvent, callback,
                                                 ev, pointerIndex);
                   }
               }
           }
           android_app_clear_motion_events(inputBuffer);
       }

   See the[GitHub sample](https://github.com/android/games-samples/blob/main/agdk/agdktunnel/app/src/main/cpp/input_util.cpp)for the implementation of the`_cookEventForPointerIndex()`and other related functions.
2. When you are done, remember to clear the queue of events that you have just handled:

       android_app_clear_motion_events(mApp);

## Additional resources

To learn more about`GameActivity`, see the following:

- [GameActivity and AGDK release notes](https://developer.android.com/games/agdk/release-notes).
- [Use the GameTextInput in GameActivity](https://developer.android.com/games/agdk/game-activity/use-text-input).
- [NativeActivity migration guide](https://developer.android.com/games/agdk/game-activity/migrate-native-activity).
- [GameActivity reference documentation](https://developer.android.com/reference/games/game-activity/group/game-activity).
- [GameActivity implementation](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/game-activity/).

To report bugs or request new features to GameActivity, use[the GameActivity issue tracker](https://issuetracker.google.com/issues/new?component=897320&template=1456805).