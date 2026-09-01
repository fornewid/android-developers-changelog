---
title: https://developer.android.com/games/agdk/game-activity
url: https://developer.android.com/games/agdk/game-activity
source: md.txt
---

# GameActivityPart of[Android Game Development Kit](https://developer.android.com/games/agdk/overview).

[`GameActivity`](https://developer.android.com/reference/games/game-activity)is a Jetpack library designed to assist Android games in processing app cycle commands, input events, and text input in the application's C/C++ code.`GameActivity`is a direct descendant of[`NativeActivity`](https://developer.android.com/reference/android/app/NativeActivity)and shares a similar architecture:

![alt_text](https://developer.android.com/static/games/agdk/game-activity/images/GameActivityArchitecture.png "GameActivity overview")

As illustrated in the above diagram,`GameActivity`performs the following functions:

- Interacting with Android framework through the Java-side component.
- Passing app cycle commands, input events, and input text to the native side.
- Modelling C/C++ source code into three logical components:
  - GameActivity's JNI functions, which directly support GameActivity's Java functionality and enqueue the events to`native_app_glue`.
  - `native_app_glue`, which runs mostly in its own native thread (different from the application's main thread), and executes tasks with its looper.
  - The application's game code, which polls and processes the events queued inside`native_app_glue`and executes game code within the`native_app_glue`thread.

With`GameActivity`, you can focus on your core game development and avoid spending excessive time dealing with the JNI code.

If you are already familiar with`NativeActivity`, the major differences between`GameActivity`and`NativeActivity`are as follows:

- `GameActivity`renders into a[`SurfaceView`](https://developer.android.com/reference/android/view/SurfaceView), making it much easier for games to interact with other UI components.
- For touch and key input events,`GameActivity`has a completely new implementation with the[`android_input_buffer`](https://developer.android.com/reference/games/game-activity/structandroid/input-buffer)interface, separate from the[`InputQueue`](https://developer.android.com/reference/android/view/InputQueue)that`NativeActivity`uses.
- `GameActivity`is a derived class of`AppCompatActivity`, which lets you seamlessly use other Jetpack components.[`ActionBar`](https://developer.android.com/reference/android/app/ActionBar),[`Fragment`](https://developer.android.com/guide/fragments), and others are all available.
- `GameActivity`adds text input functionality by integrating[the GameTextInput library](https://developer.android.com/games/agdk/add-support-for-text-input).
- Apps derived from`GameActivity`are expected to build all three parts of C/C++ code into one library. On the other hand,`NativeActivity`'s JNI functions are a part of the framework (always loaded by OS). Hence, only the`native_app_glue`and application's C/C++ code are expected to be built into one library.
- `NativeActivity`is a part of Android framework and follows its release cycle (typically yearly).`GameActivity`is a part of the Jetpack library, which has a much more frequent release cycle (typically biweekly); new features and bug fixes can arrive much more quickly.

| **Note:** We strongly recommend using`GameActivity`for new games and other C/C++ intensive applications. If you have an existing`NativeActivity`application, we recommend migrating to`GameActivity`.

## Release locations

The`GameActivity`library is available in the following channels:

- As a part of the[Android Jetpack library](https://developer.android.com/jetpack/androidx/releases/games)(recommended)
- As[AOSP](https://android.googlesource.com/platform/frameworks/opt/gamesdk/)source code

The C/C++ code is provided as source code in all release channels, using the[Prefab](https://developer.android.com/studio/build/dependencies?agpversion=4.0#native-dependencies-aars)format. GameActivity version 1.2.2 adds a static library to the distribution. Starting with this version and later, we recommend you use the static library instead of the source code.
| **Note:** Most of the documentation on this site is written from the perspective of AndroidX.

### Contents of Jetpack library

With the Jetpack library, GameActivity is released with an AAR. This AAR contains the following major components:

- A JAR file for Java code
- The C/C++static library`game-activity_static`is included with GameActivity version 1.2.2 and later.
- C/C++ source code (under the`/prefab`folder)

The integration instructions linked to from this page assume that you can use Prefab in your build system; otherwise, you can copy the source code packed under the`prefab/modules/game-activity/include`folder into your build system and perform the necessary integration steps. A similar file structure exists for the releases under`androidx`for the Android Jetpack library; by default, gradle unpacks AARs in its cache directory (\~/.gradle/caches/...). You can find the C/C++ source code by searching for`prefab/modules/game-activity/include`and picking up the location under your intended release version.

For instructions on integrating using the Jetpack library, see[Get started with GameActivity](https://developer.android.com/games/agdk/game-activity/get-started).

### Content of AOSP source code

AOSP always contains the most recent source code. Follow \[the build instructions\]\[GameActivity implementation\]{: .external} to create your own releases or directly integrate the source into your build environment. The C/C++ source code is saved in a file structure similar to the Jetpack library.

## Integration guides

Follow those guides to integrate`GameActivity`into your applications:

- [Get started](https://developer.android.com/games/agdk/game-activity/get-started)
- [Use game text input](https://developer.android.com/games/agdk/game-activity/use-text-input)
- [NativeActivity migration guide](https://developer.android.com/games/agdk/game-activity/migrate-native-activity)

## Additional resources

To learn more about`GameActivity`, see the following:

- [GameActivity and AGDK release notes](https://developer.android.com/games/agdk/release-notes).
- [Use GameTextInput in GameActivity](https://developer.android.com/games/agdk/game-activity/use-text-input).
- [NativeActivity migration guide](https://developer.android.com/games/agdk/game-activity/migrate-native-activity).
- [GameActivity reference documentation](https://developer.android.com/reference/games/game-activity/group/game-activity).
- [GameActivity implementation](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/refs/heads/gamesdk-main/game-activity/).

## Feedback

To report bugs or request new features to GameActivity, use[the GameActivity issue tracker](https://issuetracker.google.com/issues/new?component=897320&template=1456805).