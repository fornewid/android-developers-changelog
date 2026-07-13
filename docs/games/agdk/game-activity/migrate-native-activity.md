---
title: https://developer.android.com/games/agdk/game-activity/migrate-native-activity
url: https://developer.android.com/games/agdk/game-activity/migrate-native-activity
source: md.txt
---

# Migrate from NativeActivity
Part of [Android Game Development Kit](https://developer.android.com/games/agdk/overview).

This page describes how to migrate from
[`NativeActivity`](https://developer.android.com/reference/android/app/NativeActivity) to
[`GameActivity`](https://developer.android.com/games/agdk/game-activity) in your Android game project.

`GameActivity` is based on `NativeActivity` from the Android
framework, with enhancements and new features:

- Supports `Fragment` from Jetpack.
- Adds `TextInput` support to facilitate soft keyboard integration.
- Handles touch and key events in the `GameActivity` Java class rather than the `NativeActivity` `onInputEvent` interface.

Before migrating, we recommend reading the
[get started guide](https://developer.android.com/games/agdk/game-activity/get-started), which describes how
to set up and integrate `GameActivity` in your project.

## Java build script updates

`GameActivity` is [distributed](https://developer.android.com/games/agdk/game-activity#releases) as a
Jetpack library. Make sure to apply the Gradle script updating steps described
in the [get started guide](https://developer.android.com/games/agdk/game-activity/get-started):

1. Enable Jetpack library in your project's `gradle.properties` file:

       android.useAndroidX=true

2. Optionally, specify a Prefab version, in the same `gradle.properties` file,
   for example:

       android.prefabVersion=2.0.0

3. Enable Prefab feature in your app's `build.gradle` file:

       android {
           ... // other configurations
           buildFeatures.prefab true
       }

4. Add the `GameActivity` dependency to your application:

   1. Add the `core` and `games-activity` libraries.
   2. If your current minimum supported API level is less than 16, update it to at least 16.
   3. Update the compiled SDK version to the one that the `games-activity` library requires. Jetpack typically requires the latest SDK version at the release build time.

   Your updated `build.gradle` file might look something like this:

       android {
           compiledSdkVersion 33
           ... // other configurations.
           defaultConfig {
               minSdkVersion 16
           }
           ... // other configurations.

           buildFeatures.prefab true
       }
       dependencies {
           implementation 'androidx.core:core:1.9.0'
           implementation 'androidx.games:games-activity:1.2.2'
       }

## Kotlin or Java code updates

`NativeActivity` can be used as a startup activity and creates a full screen
application. At present, GameActivity *cannot* be used as the startup
activity. Apps must derive a class from `GameActivity` and use that as
the startup activity. You must also make additional configuration changes to
create a full screen app.

The following steps assume your application uses `NativeActivity` as the startup
activity. If that is not the case, you can skip most of them.

1. Create a Kotlin or Java file to host the new startup activity. For example,
   the following code creates the `MainActivity` as the startup activity and
   loads the application's main native library, `libAndroidGame.so`:

   ### Kotlin

   ```kotlin
   class MainActivity : GameActivity() {
      override fun onResume() {
          super.onResume()
          // Use the function recommended from the following page:
          // https://d.android.com/training/system-ui/immersive
          hideSystemBars()
      }
      companion object {
          init {
              System.loadLibrary("AndroidGame")
          }
      }
   }
   ```

   ### Java

   ```java
     public class MainActivity extends GameActivity {
         protected void onResume() {
             super.onResume();
             // Use the function recommended from
             // https://d.android.com/training/system-ui/immersive
             hideSystemBars();
         }
         static {
             System.loadLibrary("AndroidGame");
         }
     }
   ```
2. Create a full screen app theme in the `res\values\themes.xml` file:

       <resources xmlns:tools="http://schemas.android.com/tools">
           <!-- Base application theme. -->
           <style name="Application.Fullscreen" parent="Theme.AppCompat.Light.NoActionBar">
               <item name="android:windowFullscreen">true</item>
               <item name="android:windowContentOverlay">@null</item>"
           </style>
       </resources>

3. Apply the theme to the application in the `AndroidManifest.xml` file:

       <application  android:theme="@style/Application.Fullscreen">
            <!-- other configurations not listed here. -->
       </application>

   For detailed instructions for full screen mode, see to [the
   immersive guide](https://developer.android.com/training/system-ui/immersive) and example implementation in
   [the games-samples repo](https://github.com/android/games-samples/blob/main/agdk/agdktunnel/app/src/main/java/com/google/sample/agdktunnel/AGDKTunnelActivity.java).

This migration guide does not change the native library name. If you do change
it, ensure the native library names are consistent in the following three
locations:

- Kotlin or Java code:

      System.loadLibrary("AndroidGame")

- `AndroidManifest.xml`:

      <meta-data android:name="android.app.lib_name"
              android:value="AndroidGame" />

- Inside the C/C++ build script file, for example `CMakeLists.txt`:

      add_library(AndroidGame ...)

## C/C++ build script updates

The instructions in this section use `cmake` as the example. If your application
uses `ndk-build`, you need to map them to the equivalent commands described in
[ndk-build documentation page](https://developer.android.com/ndk/guides/ndk-build).

GameActivity's C/C++ implementation has been providing a source code release.
For version 1.2.2 a later, a static library release is provided. The static
library is the recommended release type.

The release is packed inside the AAR with the
[`prefab`](https://developer.android.com/studio/build/dependencies#using-native-dependencies)
utility. The native code includes GameActivity's C/C++ sources and the
`native_app_glue` code. They need to be built together with your
application's C/C++ code.

`NativeActivity` applications already use the `native_app_glue`
code shipped inside NDK. You must replace it with GameActivity's version
of `native_app_glue`. Other than that, all `cmake` steps documented inside
the getting started guide apply:

- Import either the C/C++ static library or the C/++ source code into your
  project as follows.

  ### Static library

  In your project's `CMakeLists.txt` file, import the `game-activity` static
  library into the `game-activity_static` prefab module:

      find_package(game-activity REQUIRED CONFIG)
      target_link_libraries(${PROJECT_NAME} PUBLIC log android
      game-activity::game-activity_static)

  ### Source code

  In your project's `CMakeLists.txt` file, import the `game-activity`
  package and add it to your target. The `game-activity` package requires
  `libandroid.so`, so if it's missing, you must also import it.

      find_package(game-activity REQUIRED CONFIG)
      ...
      target_link_libraries(... android game-activity::game-activity)

- *Remove* all references to NDK's `native_app_glue` code, such as:

      ${ANDROID_NDK}/sources/android/native_app_glue/android_native_app_glue.c
          ...
      set(CMAKE_SHARED_LINKER_FLAGS
          "${CMAKE_SHARED_LINKER_FLAGS} -u ANativeActivity_onCreate")

- If you are using the source code release, include the `GameActivity` source
  files. Otherwise, skip this step.

      get_target_property(game-activity-include
                          game-activity::game-activity
                          INTERFACE_INCLUDE_DIRECTORIES)
      add_library(${PROJECT_NAME} SHARED
          main.cpp
          ${game-activity-include}/game-activity/native_app_glue/android_native_app_glue.c
          ${game-activity-include}/game-activity/GameActivity.cpp
          ${game-activity-include}/game-text-input/gametextinput.cpp)

### Work around the UnsatisfiedLinkError issue

If you encounter an `UnsatsifiedLinkError` for the
`com.google.androidgamesdk.GameActivity.initializeNativeCode()` function, add
this code to your `CMakeLists.txt` file:

    set(CMAKE_SHARED_LINKER_FLAGS
        "${CMAKE_SHARED_LINKER_FLAGS} -u \
        Java_com_google_androidgamesdk_GameActivity_initializeNativeCode")

## C/C++ source code updates

Follow these steps to replace `NativeActivity` references in your
application with `GameActivity`:

- Use the `native_app_glue` released with `GameActivity`. Search and
  replace all `android_native_app_glue.h` usage with:

      #include <game-activity/native_app_glue/android_native_app_glue.h>

- Set both motion event filter and key event filter to `NULL` so your app can
  receive input events from all input devices. You typically do this inside
  `android_main()` function:

      void android_main(android_app* app) {
          ... // other init code.

          android_app_set_key_event_filter(app, NULL);
          android_app_set_motion_event_filter(app, NULL);

          ... // additional init code, and game loop code.
      }

- Remove `AInputEvent` related code, and replace it with GameActivity's
  `InputBuffer` implementation:

      while (true) {
          // Read all pending events.
          int events;
          struct android_poll_source* source;

          // If not animating, block forever waiting for events.
          // If animating, loop until all events are read, then continue
          // to draw the next frame of animation.
          while ((ALooper_pollOnce(engine.animating ? 0 : -1, nullptr, &events,
                                  (void**)&source)) >= 0) {
             // Process this app cycle or inset change event.
             if (source) {
                 source->process(source->app, source);
             }

                ... // Other processing.

             // Check if app is exiting.
             if (state->destroyRequested) {
                 engine_term_display(&engine);
                 return;
             }
          }
          // Process input events if there are any.
          engine_handle_input(state);

         if (engine.animating) {
             // Draw a game frame.
         }
      }

      // Implement input event handling function.
      static int32_t engine_handle_input(struct android_app* app) {
         auto* engine = (struct engine*)app->userData;
         auto ib = android_app_swap_input_buffers(app);
         if (ib && ib->motionEventsCount) {
             for (int i = 0; i < ib->motionEventsCount; i++) {
                 auto *event = &ib->motionEvents[i];
                 int32_t ptrIdx = 0;
                 switch (event->action & AMOTION_EVENT_ACTION_MASK) {
                     case AMOTION_EVENT_ACTION_POINTER_DOWN:
                     case AMOTION_EVENT_ACTION_POINTER_UP:
                         // Retrieve the index for the starting and the ending of any secondary pointers
                         ptrIdx = (event->action & AMOTION_EVENT_ACTION_POINTER_INDEX_MASK) >>
                                  AMOTION_EVENT_ACTION_POINTER_INDEX_SHIFT;
                     case AMOTION_EVENT_ACTION_DOWN:
                     case AMOTION_EVENT_ACTION_UP:
                         engine->state.x = GameActivityPointerAxes_getAxisValue(
                             &event->pointers[ptrIdx], AMOTION_EVENT_AXIS_X);
                         engine->state.y = GameActivityPointerAxes_getAxisValue(
                             &event->pointers[ptrIdx], AMOTION_EVENT_AXIS_Y);
                         break;
                      case AMOTION_EVENT_ACTION_MOVE:
                      // Process the move action: the new coordinates for all active touch pointers
                      // are inside the event->pointers[]. Compare with our internally saved
                      // coordinates to find out which pointers are actually moved. Note that there is
                      // no index embedded inside event->action for AMOTION_EVENT_ACTION_MOVE (there
                      // might be multiple pointers moved at the same time).
                          ...
                         break;
                 }
             }
             android_app_clear_motion_events(ib);
         }

         // Process the KeyEvent in a similar way.
             ...

         return 0;
      }

- Review and update logic that attached to NativeActivity's
  `AInputEvent`. As shown in the previous step, GameActivity's `InputBuffer`
  processing is outside the `ALooper_pollOnce()` loop.

- Replace `android_app::activity->clazz` usage with
  `android_app:: activity->javaGameActivity`. GameActivity renames the
  Java `GameActivity` instance.

## Additional steps

The previous steps cover NativeActivity's functionality, but `GameActivity` has
additional features that you might want to use:

- [TextInput](https://developer.android.com/games/agdk/add-support-for-text-input).
- [Game Controller](https://developer.android.com/games/sdk/game-controller).
- [Fragment](https://developer.android.com/guide/fragments).
- New window InSets commands defined in [NativeAppGlueAppCmd](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/master/game-activity/prefab-src/modules/game-activity/include/game-activity/native_app_glue/android_native_app_glue.h#302).

We recommend exploring these features and adopting them as appropriate for your
games.

If you have any questions or recommendations for GameActivity or other AGDK
libraries, create [a bug](https://issuetracker.google.com/issues/new?component=897320&pli=1&template=1456805) to let us know.