---
title: https://developer.android.com/jetpack/androidx/releases/games
url: https://developer.android.com/jetpack/androidx/releases/games
source: md.txt
---

# Android Games

[User Guide](https://developer.android.com/games/sdk)  
The android games library mirrors the Android Game SDK which is available as a binary download. You can use the androidx library instead of manually downloading and integrating the Android Game SDK into your build.

<br />

For more information about the Android Game SDK,
see the [SDK documentation](https://developer.android.com/games/sdk)
and the [SDK release notes](https://developer.android.com/games/sdk/release-notes).


This table lists all the artifacts in the `androidx.games` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| games-activity | [4.0.0](https://developer.android.com/jetpack/androidx/releases/games#games-activity-4.0.0) | [4.4.0-rc01](https://developer.android.com/jetpack/androidx/releases/games#games-activity-4.4.0-rc01) | - | - |
| games-controller | [2.0.2](https://developer.android.com/jetpack/androidx/releases/games#games-controller-2.0.2) | - | - | [2.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/games#games-controller-2.3.0-alpha01) |
| games-frame-pacing | [2.1.3](https://developer.android.com/jetpack/androidx/releases/games#games-frame-pacing-2.1.3) | - | - | [2.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/games#games-frame-pacing-2.3.0-alpha01) |
| games-memory-advice | [2.0.1](https://developer.android.com/jetpack/androidx/releases/games#games-memory-advice-2.0.1) | - | [2.1.0-beta01](https://developer.android.com/jetpack/androidx/releases/games#games-memory-advice-2.1.0-beta01) | [2.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/games#games-memory-advice-2.3.0-alpha01) |
| games-text-input | [4.0.0](https://developer.android.com/jetpack/androidx/releases/games#games-text-input-4.0.0) | [4.3.0-rc01](https://developer.android.com/jetpack/androidx/releases/games#games-text-input-4.3.0-rc01) | - | - |
| games-performance-tuner | [2.0.0](https://developer.android.com/jetpack/androidx/releases/games#games-performance-tuner-2.0.0) | - | - | [2.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/games#games-performance-tuner-2.3.0-alpha01) |

This library was last updated on: January 28, 2026

## Requirements

**games-memory-advice**

The MemoryAdvice API requires your application to be built with NDK version
r23.\* or newer.

## Declaring dependencies

To add a dependency on game, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module; `games-activity` library has integrated the same version of
the `game-text-input` library, hence `GameActivity` apps can not include the
`game-text-input` dependency again:  

### Groovy

```groovy
android {
    ...
    // To use the Android Frame Pacing or Android Performance Tuner libraries, enable
    // native dependencies to be imported. Libraries will be made available to your CMake build
    // as packages named "games-frame-pacing" and "games-performance-tuner".
    buildFeatures {
        prefab true
    }
}

dependencies {
    // To use the Android Frame Pacing library
    implementation "androidx.games:games-frame-pacing:2.1.3"

    // To use the Android Performance Tuner
    implementation "androidx.games:games-performance-tuner:2.0.0"

    // To use the Games Activity library
    implementation "androidx.games:games-activity:4.0.0"

    // To use the Games Controller Library
    implementation "androidx.games:games-controller:2.0.2"

    // To use the Games Text Input Library
    // Do not include this if games-activity has been included
    implementation "androidx.games:games-text-input:4.0.0"
}
```

### Kotlin

```kotlin
android {
    ...
    // To use the Android Frame Pacing or Android Performance Tuner libraries, enable
    // native dependencies to be imported. Libraries will be made available to your CMake build
    // as packages named "games-frame-pacing" and "games-performance-tuner".
    buildFeatures {
        prefab = true
    }
}

dependencies {
    // To use the Android Frame Pacing library
    implementation("androidx.games:games-frame-pacing:2.1.3")

    // To use the Android Performance Tuner
    implementation("androidx.games:games-performance-tuner:2.0.0")

    // To use the Games Activity library
    implementation("androidx.games:games-activity:4.0.0")

    // To use the Games Controller Library
    implementation("androidx.games:games-controller:2.0.2")

    // To use the Games Text Input Library
    // Do not include this if games-activity has been included
    implementation("androidx.games:games-text-input:4.0.0")
}
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Add Gradle properties

You may need to add properties to the `gradle.properties` file located in the
same directory as your app's (or module's) `build.gradle` file. If the
`gradle.properties` file does not exist, then create this file.

If you are using Android Studio 4.0, make sure `gradle.properties` contains the
following lines:  

    # Enables experimental Prefab
    android.enablePrefab=true
    # Tell Android Studio we are using AndroidX
    android.useAndroidX=true

If you are using Android Studio 4.1 or later, make sure `gradle.properties`
contains the following lines:  

    # Tell Android Studio we are using AndroidX
    android.useAndroidX=true

## Add packages with CMake

To make the imported Game SDK packages available, add the following to
your main app's `CMakeLists.txt` file:  

    # Add the packages from the Android Game SDK
    find_package(games-frame-pacing REQUIRED CONFIG)
    find_package(games-performance-tuner REQUIRED CONFIG)

This will allow you to include header files from the Android Game SDK in your
game code:  

    #include "swappy/swappyGL.h"
    #include "tuningfork/tuningfork.h"

In your main app's `CMakeLists.txt` file, find `target_link_libraries` for the
main shared library. Add the references to the Android Game SDK static libraries
to include them in your shared library:  

    target_link_libraries(...
      games-frame-pacing::swappy_static
      games-performance-tuner::tuningfork_static
      ...)

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:897320+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=897320&template=1456805)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Games-Memory-Advice version 2.1

### Version 2.1.0-beta01

November 29, 2023

`androidx.games:games-memory-advice:2.1.0-beta01` is released. [Version 2.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/d1f9f40d22248179ba6612beb8acec847bc5880d..3b94fe082e0e95399ed99b5a16ef8eeea307eee2/games-memory-advice)

### Version 2.1.0-alpha01

November 15, 2023

`androidx.games:games-memory-advice:2.1.0-alpha01` is released. [Version 2.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/77508803835f68c459c7191e2c741468fc0b7cc7..d1f9f40d22248179ba6612beb8acec847bc5880d/games-memory-advice)

**New Features**

- Updated the memory model of the library for better predictions.

**API Changes**

- Added a new API `getAvailableMemory()` that returns an estimate for the amount of memory that can safely be allocated, in bytes.

### Version 2.1.0-alpha01

July 26, 2023

`androidx.games:games-memory-advice:2.1.0-alpha01` is released. [Version 2.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/61b7df48b84d37584f6a2d706d892a1f592d43a6..6d48478dde57eed989d8910c3d91a0f6bce2bcc4/games-memory-advice)

**API Changes**

- Add`GetAvailableMemory` function

**Bug Fixes**

- Update Memory Advice model
- Fix shared `memory_advice` build target

## Games-Memory-Advice version 2.0

### Version 2.0.1

September 20, 2023

`androidx.games:games-memory-advice:2.0.1` is released. [Version 2.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/b0863eacb073497891e5e368a6152eb193191743..77508803835f68c459c7191e2c741468fc0b7cc7/games-memory-advice)

**Bug Fixes**

- Fix the crash happening in the state watcher thread due to the thread not being attached to the JVM.

### Version 2.0.0

September 6, 2023

`androidx.games:games-memory-advice:2.0.0` is released. [Version 2.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/f6ea10b7a71d1b3b451b3022e3171d182bbc2fdb..b0863eacb073497891e5e368a6152eb193191743/games-memory-advice)

**Major features of 2.0.0**

- A new ML model has been trained and released in this version.
- An API to predict the amount of free memory is implemented.

### Version 2.0.0-rc01

July 26, 2023

`androidx.games:games-memory-advice:2.0.0-rc01` is released. [Version 2.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/3643862ac9c7c2fe01ab511cc602e158db1dd21b..f6ea10b7a71d1b3b451b3022e3171d182bbc2fdb/games-memory-advice)

**New Features**

- Included a new model to better predict remaining memory.

**Bug Fixes**

- Fixed Memory Advice not working with a shared STL.

### Version 2.0.0-beta04

May 24, 2023

`androidx.games:games-memory-advice:2.0.0-beta04` is released. [Version 2.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/5262617d2206673e2e8548596331ead5c0ec41a8..3643862ac9c7c2fe01ab511cc602e158db1dd21b/games-memory-advice)

**New Features**

- Updated the machine learning model powering the library which'll allow improved results for newer phones

### Version 2.0.0-beta03

April 5, 2023

`androidx.games:games-memory-advice:2.0.0-beta03` is released. [Version 2.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/50bffff2cdd7305b4d245d1c222f808d8b8fc476..5262617d2206673e2e8548596331ead5c0ec41a8/games-memory-advice)

**Bug Fixes**

- Fixed a bug where the library couldn't load the required tensorflow lite assets properly

### Version 2.0.0-beta02

March 22, 2023

`androidx.games:games-memory-advice:2.0.0-beta02` is released. [Version 2.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/23a89ddabbe1a83ff9e70c106c1a7693537dad60..50bffff2cdd7305b4d245d1c222f808d8b8fc476/games-memory-advice)

**Bug Fixes**

- Fixed a bug that prevented the static version of the library to be linked properly

### Version 2.0.0-beta01

February 22, 2023

`androidx.games:games-memory-advice:2.0.0-beta01` is released. [Version 2.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/27573e27acd71cc7ba80ce592c76611edc3b6328..23a89ddabbe1a83ff9e70c106c1a7693537dad60/games-memory-advice)

**New Features**

- No new changes

### Version 2.0.0-alpha01

February 8, 2023

`androidx.games:games-memory-advice:2.0.0-alpha01` is released. [Version 2.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..27573e27acd71cc7ba80ce592c76611edc3b6328/games-memory-advice)

**API Changes**

- Major version increase due to build files refactoring.

**Bug Fixes**

- Incorrect configuration of library assets now gives an error instead of crashing.

## Games-Memory-Advice version 1.0.0

### Version 1.0.0-beta03

November 9, 2022

`androidx.games:games-memory-advice:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/1b8430a9c2955e29d8ea667cfcc0612a9896f01d..c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf/games-memory-advice)

**New Features**

- No new changes

### Version 1.0.0-beta01

March 9, 2022

`androidx.games:games-memory-advice:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e6bb74379ccaa6df74c4e6dff9479c244e5e8249..1b8430a9c2955e29d8ea667cfcc0612a9896f01d/src/memory_advice)

- No changes since 1.0.0-alpha01.

### Version 1.0.0-alpha01

February 23, 2022

`androidx.games:games-memory-advice:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/ac44a0dd8d5c0a5919346be5df11d473fdb87151/src/memory_advice)

**New Features**

- This C library gives the facility to query and receive callbacks for changes in the memory state of a device which is running a game.

**API Changes**

- This is the initial release of the memory advice library. See the header at include/memory_advice/memory_advice.h for the full API.

**External Contribution**

- The library depends on tensorflow, whose license and those of transitive dependencies can be found at <https://github.com/tensorflow/tensorflow>.

## Games-Text-Input Version 4.3

### Version 4.3.0-rc01

January 28, 2026

`androidx.games:games-text-input:4.3.0-rc01` is released. Version 4.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/8f89733591eaa8e79de6ddbbb5936c8ac8904ec0..3450aac6bad7ff5ecdf68d518d3bc0c9183641d9/game-text-input).

### Version 4.3.0-beta01

November 19, 2025

`androidx.games:games-text-input:4.3.0-beta01` is released. Version 4.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/2ae5d1f41c01ac94f38b46132b1f45f4346fa773..8f89733591eaa8e79de6ddbbb5936c8ac8904ec0/game-text-input).

- This release transitions `androidx.games:games-text-input` from alpha to beta.

## Games-Text-Input Version 3.0

### Version 3.0.4

August 7, 2024

`androidx.games:games-text-input:3.0.4` is released. Version 3.0.4 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/46870fe6d88c5d94752d592e5a93abb6a9a7123c..c61b621cdc6ba3026ecf8eaaf19bbb593698a448/game-text-input).

**Bug Fixes**

- Fixed functionality of deletion with and without text selection.

## Games-Activity Version 4

### Version 4.4.0-rc01

January 28, 2026

`androidx.games:games-activity:4.4.0-rc01` is released. Version 4.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/8f89733591eaa8e79de6ddbbb5936c8ac8904ec0..a0843d96af70d1044505bfb95f9ec3b2a68c5f99/game-activity).

### Version 4.4.0-beta01

November 19, 2025

`androidx.games:games-activity:4.4.0-beta01` is released. Version 4.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c28257b2c517145c01bca12b3af2531f5bf494d6..8f89733591eaa8e79de6ddbbb5936c8ac8904ec0/game-activity).

- This release transitions `androidx.games:games-activity` from alpha to beta.

### Version 4.4.0-alpha01

October 22, 2025

`androidx.games:games-activity:4.4.0-alpha01` is released. Version 4.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/2ae5d1f41c01ac94f38b46132b1f45f4346fa773..c28257b2c517145c01bca12b3af2531f5bf494d6/game-activity).

**Bug Fixes**

- Improved ANR protection in `native_app_glue`.
- Migrated from deprecated `ALooper_pollAll` to `ALooper_pollOnce`.

### Version 4.3.0-alpha01

August 13, 2025

`androidx.games:games-activity:4.3.0-alpha01` and `androidx.games:games-text-input:4.3.0-alpha01` are released. Version 4.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787..2ae5d1f41c01ac94f38b46132b1f45f4346fa773/game-activity).

**New Features**

- Support 16kb page sizes by default.
- Mouse support for GameActivity.

**Bug Fixes**

- Fixed a race condition between `onDestroy` and `onCreate` lifecycle events.
- Fixed an issue where apps needed to manually preserve a symbol to initialize native code.
- Improved `GameActivity` touch handling.
- Fixed `GameTextInput` generating as a shared library incorrectly.

### Version 4.2.0-alpha01

March 26, 2025

`androidx.games:games-activity:4.2.0-alpha01` and `androidx.games:games-text-input:4.2.0-alpha01` are released. Version 4.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/a34179b397368ee91f1352496e08c969e6246280..044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787/game-activity).

**New Features**

- Upgrade to Gradle 8.8.1 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))
- Upgrade to Java 17 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))

**Bug Fixes**

- Fix a bug in `GameActivity` in which `getLocaleScript`, `getLocaleCountry` and `getLocaleVariant` were reporting the locale language instead of the requested value ([1198bb0](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1198bb0))
- Fix a bug in `GameActivity` which caused us to misreport software keyboard open-close events. ([a63ecca](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/a63ecca))
- Fix a bug in `GameTextInput` with multibyte emoji handling ([9d54c68](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/9d54c68))

### Version 4.0.0

February 12, 2025

`androidx.games:games-activity:4.0.0` and `androidx.games:games-text-input:4.0.0` are released. Version 4.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/ec59a905b064856c71d43d731354de52b080e260..a34179b397368ee91f1352496e08c969e6246280/game-activity).

**Major features of 4.0.0**

- AAR files now contain prebuilt static libraries. Application code is now expected to use those libraries via prefabs and only include headers (like `#include "GameActivity.h"`) instead of including the implementation (like `#include "GameActivity.cpp"`).
- Also Android locale information is now available to the native code that uses `GameActivity`.

**Bug Fixes**

- Numerous bugs in `GameTextInput` have been fixed. The library is now more stable and works with many popular software and hardware keyboards.

### Version 4.0.0-rc01

January 29, 2025

`androidx.games:games-activity:4.0.0-rc01` and `androidx.games:games-text-input:4.0.0-rc01` are released. Version 4.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/f7656b84151dbc1570c8730861b7b5d3ed6be1db..ec59a905b064856c71d43d731354de52b080e260/game-activity).

### Version 4.0.0-beta01

January 15, 2025

`androidx.games:games-activity:4.0.0-beta01` and `androidx.games:games-text-input:4.0.0-beta01` are released. Version 4.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e79542803f1b999c03845ea18f070f53846869ce..f7656b84151dbc1570c8730861b7b5d3ed6be1db/game-activity).

**Bug Fixes**

- Better documented newly added locale-related functionality.
- Added backing types to all enumeration types.

### Version 4.0.0-alpha01

October 16, 2024

`androidx.games:games-activity:4.0.0-alpha01` and `androidx.games:games-text-input:4.0.0-alpha01` are released. Version 4.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c61b621cdc6ba3026ecf8eaaf19bbb593698a448..e79542803f1b999c03845ea18f070f53846869ce/game-activity).

**New Features**

- `GameTextInput` now supports Left/Right keys.

**API Changes**

- Obsolete Java interfaces of `GameTextInput` have been removed.
- Prefabs for both `GameActivity` and `GameTextInput` now include all source files. `#include <GameActivity.cpp>` is not recommended anymore. Please link to a proper static or dynamic library instead, like `game-activity::game-activity_static` in `CMake`. These libraries are shipped in the AAR file.

**Bug Fixes**

- Numerous fixes in `GameTextInput` have been made. Typing and removing functionality has been fixed.
- Compatibility with most popular software keyboards have been improved.
- Fixed handling of special characters on hardware keyboards.
- Fixed a rare null pointer access in `GameActivity`.

## Games-Activity Version 3.0

### Version 3.0.5

August 7, 2024

`androidx.games:games-activity:3.0.5` is released. Version 3.0.5 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e05ad224fd2ea838d44f48830e5b49f6dfe5dae3..94e486f81abfef906afd641b5abfe9511127d297/game-activity).

**Bug Fixes**

- New release of `GameActivity` to match the 3.0.4 release of `GameTextInput` (fixed functionality of text deletion in inputs).

### Version 3.0.4

July 10, 2024

`androidx.games:games-activity:3.0.4` is released. Version 3.0.4 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/287affdc5739c47077aab122c623606ec4f1aca8..e05ad224fd2ea838d44f48830e5b49f6dfe5dae3/game-activity).

**Bug Fixes**

- Fixed handling of null pointers.
- Fixed missing state updates for some states in `onConfiguration()` callback.

### Version 3.0.3

April 17, 2024

`androidx.games:games-activity:3.0.3` and `androidx.games:games-text-input:3.0.3` are released. Version 3.0.3 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/03a8625d48370f7dc5a45de1199ff1680182aab2..46870fe6d88c5d94752d592e5a93abb6a9a7123c/game-activity).

**Bug Fixes**

- Fixed compatibility issues with some software keyboards.

### Version 3.0.2

April 3, 2024

`androidx.games:games-activity:3.0.2` and `androidx.games:games-text-input:3.0.2` are released. Version 3.0.2 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/ced0d842e93aa4ec4090b7e018fc5a5d07151ec6..03a8625d48370f7dc5a45de1199ff1680182aab2/game-activity).

**Bug Fixes**

- We made several fixes to `GamesTextInput` which are aimed to improve software and hardware keyboards support. Also a bug has been fixed that was preventing `GameTextInput` from being used without `GameActivity`.

### Version 3.0.1

March 20, 2024

`androidx.games:games-activity:3.0.1` and `androidx.games:games-text-input:3.0.1` are released. Version 3.0.1 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/7d7660083229add4728d1fe607585bffc9ec937b..ced0d842e93aa4ec4090b7e018fc5a5d07151ec6/game-activity).

**Bug Fixes**

- Fixed a problem with special characters being typed and displayed.

### Version 3.0.0

March 6, 2024

`androidx.games:games-activity:3.0.0` and `androidx.games:games-text-input:3.0.0` are released. Version 3.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4880f53064c0abc7f2adaa4895e0c9e1c0ade08b..7d7660083229add4728d1fe607585bffc9ec937b/game-activity).

**Major features of 3.0.0**

- `GameTextInput` has been reworked to be ready to use in games.
- Some interfaces in both libraries have been changed with respect to version 2.0.0.

**Bug Fixes**

- Fixed compatibility issues with old NDKs
- Fixed Windows build problems

### Version 3.0.0-rc01

February 21, 2024

`androidx.games:games-activity:3.0.0-rc01` and `androidx.games:games-text-input:3.0.0-rc01` are released. [Version 3.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/3b94fe082e0e95399ed99b5a16ef8eeea307eee2..884a5e759b685bb3b07078461645c368cd7730b5/game-activity)

**Bug Fixes**

- Fixed the freeze where keyboard events were not properly handled by the looper.

### Version 3.0.0-beta01

November 29, 2023

`androidx.games:games-activity:3.0.0-beta01` and `androidx.games:games-text-input:3.0.0-beta01` are released. [Version 3.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/d1f9f40d22248179ba6612beb8acec847bc5880d..3b94fe082e0e95399ed99b5a16ef8eeea307eee2/game-activity)

### Version 3.0.0-alpha01

November 15, 2023

`androidx.games:games-activity:3.0.0-alpha01` and `androidx.games:games-text-input:3.0.0-alpha01` are released. [Version 3.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c9a97403705fcf46685d3655f8723bdaa7f434b9..d1f9f40d22248179ba6612beb8acec847bc5880d/game-activity)

**API Changes**

- `GameActivityMotionEvent` and `GameActivityCallbacks` structures changed their sizes.
- `onEditorAction` changes its return type from boolean to void.
- `setImeEditorInfo` now expects enum parameters, not integers.
- internal functions of `GameActivityEvents` are moved into `GameActivityEvents_internal.h`.
- `GameTextInput`'s input types are also enumerations, not integers.

## Games-Activity Version 2.1

### Version 2.1.0-alpha02

September 6, 2023

`androidx.games:games-activity:2.1.0-alpha02` and `androidx.games:games-text-input:2.1.0-alpha02` are released. [Version 2.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/6d48478dde57eed989d8910c3d91a0f6bce2bcc4..c9a97403705fcf46685d3655f8723bdaa7f434b9/game-activity)

**Bug Fixes**

- 32 bit devices compatibility has been improved.

### Version 2.1.0-alpha01

July 26, 2023

`androidx.games:games-activity:2.1.0-alpha01` is released. [Version 2.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/61b7df48b84d37584f6a2d706d892a1f592d43a6..6d48478dde57eed989d8910c3d91a0f6bce2bcc4/game-activity)

**New Features**

- Provide an ability to override the creation of the `SurfaceView` instance
- Add SDK version reporting

**API Changes**

- Use `int64_t` instead of `long` for `historicalEventTimes` to avoid overruning on 32bit systems
- Add `GameActivity_restartInput` method
- Add a native callback to handle software keyboard visibility change

**Bug Fixes**

- Optimize touch event handling
- Correct destruction of a `GameActivityMotionEven`
- Fix `GameActivityMotionEvent_getHistoricalAxisValue` index calculation
- Fix bitmasks for the motion filter

## Games-Activity Version 2.0

### Version 2.0.2

May 24, 2023

`androidx.games:games-activity:2.0.2` is released. [Version 2.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/94a33979d995c3ebf0cf9bc4080fb1eb85b84526..fef91e2206619b01a3be1f3df21f94e31155660e/game-activity)

**Bug Fixes**

- Stability fixes in `GameActivityEvents` ([b/278017467](https://issuetracker.google.com/issues/278017467))

### Version 2.0.1

April 5, 2023

`androidx.games:games-activity:2.0.1` is released. [Version 2.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/1aa62919bfcabf738925d194290c8afea2f4221f..94a33979d995c3ebf0cf9bc4080fb1eb85b84526/game-activity)

**Bug Fixes**

- Fixed early freeing of memory with `historicalEventTimes`.
- Fixed issue with `historicalEventTimesNanos` overflowing on 32bit systems

### Version 2.0.0

March 8, 2023

`androidx.games:games-activity:2.0.0` is released. [Version 2.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..e1e20061358fd38e7f014d4d02b9e2878c2169a9/game-activity)

**Major features of 2.0.0**

- Changed interface for historical event times to overcome the 32 bit limit.
- Provided user access to configuration changes, like orientation.
- Provided up-to-date information in the `contentRect` structure.
- Provided an easier way to customize default `SurfaceView`.
- Fixed default OS handling of touch events, like handling system buttons.
- Optimized out most JNI calls in touch event handling; this used to affect performance.

### Version 2.0.0-rc01

February 22, 2023

`androidx.games:games-activity:2.0.0-rc01` is released. [Version 2.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/27573e27acd71cc7ba80ce592c76611edc3b6328..83d676655ca28ed426bdaf0602bb3046cbf79ce8/game-activity)

### Version 2.0.0-beta01

February 8, 2023

`androidx.games:games-activity:2.0.0-beta01` is released. [Version 2.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/fd1ddaa12b110384031f09fb8fb6b96d80f896c4..27573e27acd71cc7ba80ce592c76611edc3b6328/game-activity)

**Bug Fixes**

- Fixed system buttons handling. ([2a103e](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/2a103e9985159a32bbe6db58ad69d6f4ed59a709))

### Version 2.0.0-alpha01

January 11, 2023

`androidx.games:games-activity:2.0.0-alpha01` is released with no changes. [Version 2.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..fd1ddaa12b110384031f09fb8fb6b96d80f896c4/game-activity)

## Games-Activity Version 1.2

### Version 1.2.2

December 7, 2022

`androidx.games:games-activity:1.2.2` is released. [Version 1.2.2 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..b1ca82f17b812cbf5bc4a2247d9cc1048504cccb/game-activity)

**Bug Fixes**

- The maximum number of motion events can now be set at runtime.

### Version 1.2.2-alpha01

November 9, 2022

`androidx.games:games-activity:1.2.2-alpha01` is released. [Version 1.2.2-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/df59ba84ac245cfd9db805acc925afd4b19c5566..c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf/game-activity)

**API Changes**

- API now also contains version information in the form of `GAMEACTIVITY_PACKED_VERSION`. ([I287e6](https://android-review.googlesource.com/q/I287e67f9069524ddf09ca3c83e2326d28ea6e5ba))
- Added `onContentRectChanged` callback which is called when the rectangle in the window where the content should be placed has changed. ([I81396](https://android-review.googlesource.com/q/I81396a966a723ad0ed9280313490aa8cd97a4d82))

**Bug Fixes**

- Fixed events buffer overflow. Both `inputBuffer`-\>`keyEvents` and `motionEvents` are now dynamically-allocated buffers. ([Ic00f6](https://android-review.googlesource.com/#/q/Ic00f68043e72b80ed3a6aee80fac04b9e20aaac1))
- Fails gracefully if out of memory. Added handling of `realloc()` errors during buffers resizing.

### Version 1.2.1

July 13, 2022

`androidx.games:games-activity:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/df59ba84ac245cfd9db805acc925afd4b19c5566/GameActivity)

**Bug Fixes**

- Fixed issues with missing .aar file in previous release.

### Version 1.2.0

June 15, 2022

`androidx.games:games-activity:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/ac44a0dd8d5c0a5919346be5df11d473fdb87151../GameActivity)

**Important changes since 1.1.0**

- Allow derived classes of GameActivity to handle native library loading.
- Always load the native library in GameActivity.onCreate.
- Fallback to loading library with name "main" if no other library found.

## Games-Activity Version 1.1

### Version 1.1.0

February 23, 2022

`androidx.games:games-activity:1.1.0` and `androidx.games:games-controller:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4f851ef851998ea2cb65dad519f595377fd73fcf..ac44a0dd8d5c0a5919346be5df11d473fdb87151/GameActivity)

**Important changes since 1.0.0**

Games Activity:

- WindowInsets listening and querying for notch and IME response
- Add key and motion event filters
- Bug fixes:
  - Add missing messages for compatibility with NativeActivity
  - Fix signature of onNativeWindowResized
  - Fix input event losses

### Version 1.1.0-rc01

February 9, 2022

`androidx.games:games-activity:1.1.0-rc01` and `androidx.games:games-controller:1.1.0-rc01` are released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/60b0ddc9b45463685713d52558c2fa62c4ca50bb..4f851ef851998ea2cb65dad519f595377fd73fcf/GameActivity)

### Version 1.1.0-beta03

January 26, 2022

`androidx.games:games-activity:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e8e9971ec507a219142344409f5176cc4aea8b3f..60b0ddc9b45463685713d52558c2fa62c4ca50bb/GameActivity)

**Bug Fixes**

- Fix signature of `onNativeWindowResized`
- Maintain handle to native window in `onSurfaceChanged`

### Version 1.1.0-beta02

December 15, 2021

`androidx.games:games-activity:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/10c777b19cf438d6e4e682dc275ccaa3974f78b7..e8e9971ec507a219142344409f5176cc4aea8b3f/GameActivity)

**Bug Fixes**

- Fix race condition in event filter setting.

### Version 1.1.0-beta01

November 17, 2021

`androidx.games:games-activity:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/90ec6911a1fa5e18d2e40b363d03de2dbd6fd912..10c777b19cf438d6e4e682dc275ccaa3974f78b7/GameActivity)

**New Features**

- Added support for querying window insets and listening for inset changes. This allows games to react to the IME popping-up and to deal with waterfall and camera cutout insets.

**API Changes**

- `void GameActivity_getWindowInsets(GameActivity* activity,
  enum GameCommonInsetsType type,
  GameCommonInsets* insets);`

**Bug Fixes**

- Avoid consuming all key events: volume, camera, etc. are now passed through to the system.

### Version 1.1.0-alpha01

September 29, 2021

`androidx.games:games-activity:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/565cb7b2f1f88bc527c07a1512ab6ae719b7990d..90ec6911a1fa5e18d2e40b363d03de2dbd6fd912/GameActivity)

**API Changes**

- `onContentRectChanged` callback added to `GameActivityCallbacks`

**Bug Fixes**

- Missing messages added to android_native_app_glue.h:
  - `APP_CMD_CONTENT_RECT_CHANGED`
  - `APP_CMD_WINDOW_REDRAW_NEEDED`

## Games Performance Tuner 2.0

### Version 2.0.0

August 7, 2024

`androidx.games:games-performance-tuner:2.0.0` is released. Version 2.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/17ce5e87964a3fd53662850262c2740b9b70cee8..2d7d35fc499735fa5de5990ec261c306b56462f5/games-performance-tuner).

**Major features of 2.0.0**

- No major changes since 2.0.0beta01, we're just marking this release as stable.

### Version 2.0.0-beta01

January 10, 2024

`androidx.games:games-performance-tuner:2.0.0-beta01` is released with no changes from the last alpha release. [Version 2.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/3b94fe082e0e95399ed99b5a16ef8eeea307eee2..12ef8dab8ec4a03116abce11081601d883d8170e/games-performance-tuner)

### Version 2.0.0-alpha07

November 29, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha07` is released. [Version 2.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e7cc630a269be37ff70185e013845ebd93bced9f..3b94fe082e0e95399ed99b5a16ef8eeea307eee2/games-performance-tuner)

**Bug Fixes**

- Fixed memory telemetry reporting sometimes reporting wrong values

### Version 2.0.0-alpha06

November 1, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha06` is released. [Version 2.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/d10c609303f8e9f75167e727b0f8fd58715117f3..e7cc630a269be37ff70185e013845ebd93bced9f/games-performance-tuner)

### Version 2.0.0-alpha05

August 23, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha05` is released. [Version 2.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c0b5cfbd59e5c47f65bad1301a37013efcf45bfa..d10c609303f8e9f75167e727b0f8fd58715117f3/games-performance-tuner)

**New Features**

- Migrated Protobuf library to Protobuf lite.

**Bug Fixes**

- Fixed issues with dangling pointer.

### Version 2.0.0-alpha04

April 19, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha04` is released. [Version 2.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/23a89ddabbe1a83ff9e70c106c1a7693537dad60..c0b5cfbd59e5c47f65bad1301a37013efcf45bfa/games-performance-tuner)

**New Features**

- Updated the telemetry collection features in the library, allowing for more granular reporting of frame rendering times.

**Bug Fixes**

- Fixed a bug where the library crashes if max instrumentation keys are more than histogram count.

### Version 2.0.0-alpha03

February 22, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha03` is released. [Version 2.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/27573e27acd71cc7ba80ce592c76611edc3b6328..23a89ddabbe1a83ff9e70c106c1a7693537dad60/games-performance-tuner)

**Bug Fixes**

- Games-Performance-Tuner has been moved to a new release process. There should be no behavior changes.

### Version 2.0.0-alpha02

February 8, 2023

`androidx.games:games-performance-tuner:2.0.0-alpha02` is released. [Version 2.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/fd1ddaa12b110384031f09fb8fb6b96d80f896c4..27573e27acd71cc7ba80ce592c76611edc3b6328/games-performance-tuner)

**API Changes**

- `TuningFork_predictQualityLevels` API added; which will help predict the correct quality level/fidelity parameters to use.

## Games Performance Tuner 1.6

### Version 1.6.1-alpha01

November 9, 2022

`androidx.games:games-performance-tuner:1.6.1-alpha01` is released. [Version 1.6.1-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf/games-performance-tuner)

**New Features**

- No new changes

### Version 1.6.0

June 15, 2022

`androidx.games:games-performance-tuner:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4f851ef851998ea2cb65dad519f595377fd73fcf../src/tuningfork)

**Important changes since 1.5.0**

- Fixed getpid returning 0 while trying to get memory telemetry.
- Stopped StopLoadingGroup from executing without an active loading group.

## Games Performance Tuner 1.5.0

### Version 1.5.0

February 9, 2022

`androidx.games:games-performance-tuner:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/60b0ddc9b45463685713d52558c2fa62c4ca50bb..4f851ef851998ea2cb65dad519f595377fd73fcf/src/tuningfork)

**Important changes since 1.4.0**

- Programmatically change the interval between uploads, rather than it being hard-coded in the initial settings.
  - Added function: `TuningFork_setAggregationStrategyInterval`
- Fix for memory corruption in API key on `API<=23`

### Version 1.5.0-rc01

January 26, 2022

`androidx.games:games-performance-tuner:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e8e9971ec507a219142344409f5176cc4aea8b3f..60b0ddc9b45463685713d52558c2fa62c4ca50bb/src/tuningfork)

**Bug Fixes**

- Fix for memory corruption in API key on API\<=23

### Version 1.5.0-beta02

December 15, 2021

`androidx.games:games-performance-tuner:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/90ec6911a1fa5e18d2e40b363d03de2dbd6fd912..e8e9971ec507a219142344409f5176cc4aea8b3f/src/tuningfork)

**API Changes**

- Remove ABI-breaking change from `TuningFork_Settings`.

### Version 1.5.0-beta01

September 29, 2021

`androidx.games:games-performance-tuner:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c8e6cfcfafe81d9deb1f499b3156e43a91123b7..90ec6911a1fa5e18d2e40b363d03de2dbd6fd912/src/tuningfork)

**New Features**

- No changes from alpha release. That release had:
  - Programmatically change the interval between uploads, rather than it being hard-coded in the initial settings.

**API Changes**

- No changes from alpha release. That release had:
  - New function: `TuningFork_setAggregationStrategyInterval`
  - New field in `TuningFork_Settings: aggregation_strategy_intervalms_or_count`

### Version 1.5.0-alpha01

August 18, 2021

`androidx.games:games-performance-tuner:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..4c8e6cfcfafe81d9deb1f499b3156e43a91123b7/src/tuningfork)

**New Features**

- It is now possible to set the interval between APT uploads programmatically, rather than using the settings file.

**API Changes**

- Added function: `TuningFork_setAggregationStrategyInterval`
- Added field to TuningFork_Settings struct: `aggregation_strategy_intervalms_or_count`

## Games-Activity Version 1.0.0

### Version 1.0.0

August 4, 2021

`androidx.games:games-activity:1.0.0`, `androidx.games:games-controller:1.0.0`, and `androidx.games:games-text-input:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..565cb7b2f1f88bc527c07a1512ab6ae719b7990d/GameActivity)

**Major features of 1.0.0**

This is the initial release to stable of Games-Activity, Games-Controller and Games-Text-Input. See the [AGDK Home Page](https://developer.android.com/games/agdk) for more information.

### Version 1.0.0-rc01

July 12, 2021

`androidx.games:games-activity:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc..c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8/GameActivity)

**Bug Fixes**

- Fix return type of `GameActivityCallbacks::onSaveInstanceState`

### Version 1.0.0-beta01

June 30, 2021

`androidx.games:games-activity:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c94374d6b144787f79e7202316388a97077c6c34..66204fc44cbcee003287d7a37f98eefd22bca9dc/GameActivity)

**API Changes**

- Rename `GameActivityInputInfo` to `GameActivityPointerAxes`.
- `onNativeWindowResized` callback now gives width and height of window.
- `onContentRectChanged` callback has been removed.
- `onLowMemory` was renamed to `onTrimMemory`.
- `GameActivity_setWindowFormat` removed.
- Improved ownership model for `GameActivityMotionEvents` and `GameActivityMotionEvent` pointers.
- Improved ownership model of user state in `onSaveInstanceState` callback.

### Version 1.0.0-alpha01

June 16, 2021

`androidx.games:games-activity:1.0.0-alpha01` is released.

**New Features**

- Games-Activity is a new library that replaces NativeActivity as the recommended way to integrate a C/C++ game with Android.

## Games-Controller Version 2.3

### Version 2.3.0-alpha01

August 13, 2025

`androidx.games:games-controller:2.3.0-alpha01`, `androidx.games:games-memory-advice:2.3.0-alpha01`, and `androidx.games:games-performance-tuner:2.3.0-alpha01` are released. Version 2.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787..2ae5d1f41c01ac94f38b46132b1f45f4346fa773/games-controller).

**New Features**

- Support 16kb page sizes by default.

## Games-Controller Version 2.2

### Version 2.2.0-alpha01

March 26, 2025

`androidx.games:games-controller:2.2.0-alpha01`, `androidx.games:games-memory-advice:2.2.0-alpha01`, and `androidx.games:games-performance-tuner:2.2.0-alpha01` are released. Version 2.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/2d7d35fc499735fa5de5990ec261c306b56462f5..044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787/games-controller).

**New Features**

- Upgrade to Gradle 8.8.1 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))
- Upgrade to Java 17 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))
- Change `targetSdk` to 35 ([eddf605](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/eddf605))

## Games-Controller Version 2.0

### Version 2.0.2

June 12, 2024

`androidx.games:games-controller:2.0.2` is released. Version 2.0.2 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/f1ebe620d10210d1ec538e250b6066c487a7f42b..b832f08a5a2c2785f393ae99ad9af81922c2a337/games-controller).

**Bug Fixes**

- Fixed issue where controller connected callbacks were not firing for controllers already connected before `Paddleboat_init`.
- Fixed issue where game controller touchpads were not registering touchpad presses in `Paddleboat_processGameActivityMotionInputEvent` without manually enabling the pressure axis.
- Fixed issue where game controller touchpad events were not being marked as consumed by `Paddleboat_processGameActivityMotionInputEvent`.

### Version 2.0.1

September 20, 2023

\`androidx.games:games-controller:2.0.1 ' is released. [Version 2.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e1e20061358fd38e7f014d4d02b9e2878c2169a9..f1ebe620d10210d1ec538e250b6066c487a7f42b/games-controller)

Games Controller Bug fixes:

- Fix rare `NullReferenceException` condition in `onInputDeviceChanged` handler.
- Fix to prevent certain USB keyboards from improperly registering as game controllers.

### Version 2.0.0

March 8, 2023

`androidx.games:games-controller:2.0.0` is released. [Version 2.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..e1e20061358fd38e7f014d4d02b9e2878c2169a9/games-controller)

**Major features of 2.0.0**

- Added ability to detect connection status of hardware keyboards.
- Added ability to report motion data (accelerometer/gyroscope) from the main device (i.e. handset) as well as controllers.
- Changed API and format for the controller definition database to reduce memory footprint and support additional features.

### Version 2.0.0-alpha01

January 11, 2023

`androidx.games:games-controller:2.0.0-alpha01` is released. [Version 2.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..fd1ddaa12b110384031f09fb8fb6b96d80f896c4/games-controller)

**New Features**

- Hardware keyboard detection
- Integrated sensor motion data reporting support (i.e. receiving gyroscope and accelerometer data from the phone itself)
- New optimized controller mapping data format

**API Changes**

- New API calls for hardware keyboard: `Paddleboat_getPhysicalKeyboardStatus` and `Paddleboat_setPhysicalKeyboardStatusCallback`
- New API calls for integrated sensor motion data reporting: `Paddleboat_getIntegratedMotionSensorFlags` and `Paddleboat_setMotionDataCallbackWithIntegratedFlags`
- New API calls for revised controller mapping data format: `Paddleboat_addControllerRemapDataFromFd`,`Paddleboat_addControllerRemapDataFromFileBuffer`
- Deprecated old mapping API calls: `Paddleboat_addControllerRemapData` and `Paddleboat_getControllerRemapTableData`

**Bug Fixes**

- Fixed compatibility issue with motion events from GameActivity 1.2.2 and higher

## Games-Controller Version 1.1.0

### Version 1.1.0

February 23, 2022

`androidx.games:games-activity:1.1.0` and `androidx.games:games-controller:1.1.0` are released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4f851ef851998ea2cb65dad519f595377fd73fcf..ac44a0dd8d5c0a5919346be5df11d473fdb87151/GameActivity)

**Important changes since 1.0.0**

Games Activity:

- WindowInsets listening and querying for notch and IME response
- Add key and motion event filters
- Bug fixes:
  - Add missing messages for compatibility with NativeActivity
  - Fix signature of onNativeWindowResized
  - Fix input event losses

### Version 1.1.0-rc01

February 9, 2022

`androidx.games:games-controller:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/60b0ddc9b45463685713d52558c2fa62c4ca50bb..4f851ef851998ea2cb65dad519f595377fd73fcf/GameActivity)

### Version 1.1.0-beta01

January 26, 2022

`androidx.games:games-controller:1.1.0-beta01` is released with no changes since `1.1.0-alpha01`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e8e9971ec507a219142344409f5176cc4aea8b3f..60b0ddc9b45463685713d52558c2fa62c4ca50bb/src/paddleboat)

### Version 1.1.0-alpha01

December 15, 2021

`androidx.games:games-controller:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/565cb7b2f1f88bc527c07a1512ab6ae719b7990d..e8e9971ec507a219142344409f5176cc4aea8b3f/src/paddleboat)

**New Features**

Added support for battery status, dual-motor vibration, light control and motion axis reporting on supported controllers when running on Android S or higher.

**API Changes**

- Added `Paddleboat_setMotionDataCallback` function for registering controller motion data callbacks
- Added `Paddleboat_setControllerLight` function for changing controller light settings.
- Added `Paddleboat_Controller_Battery` structure to `Paddleboat_Controller_Data`
- New structures:
  - `Paddleboat_Controller_Battery`
  - `Paddleboat_Motion_Data`
- New enums:
  - `Paddleboat_BatteryStatus`
  - `Paddleboat_LightType`
  - `Paddleboat_Motion_Type`
- New controller flags:
  - `PADDLEBOAT_CONTROLLER_FLAG_ACCELEROMETER`
  - `PADDLEBOAT_CONTROLLER_FLAG_GYROSCOPE`
  - `PADDLEBOAT_CONTROLLER_FLAG_LIGHT_PLAYER`
  - `PADDLEBOAT_CONTROLLER_FLAG_LIGHT_RGB`
  - `PADDLEBOAT_CONTROLLER_FLAG_BATTERY`

**Bug Fixes**

- Added alternate deviceId database entry for PS4 controller
- Added API \>=31 database entry for PS5 controller

## Games-Controller Version 1.0.0

### Version 1.0.0

August 4, 2021

`androidx.games:games-activity:1.0.0`, `androidx.games:games-controller:1.0.0`, and `androidx.games:games-text-input:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..565cb7b2f1f88bc527c07a1512ab6ae719b7990d/src/paddleboat)

**Major features of 1.0.0**

This is the initial release to stable of Games-Activity, Games-Controller and Games-Text-Input. See the [AGDK Home Page](https://developer.android.com/games/agdk) for more information.

### Version 1.0.0-rc02

July 21, 2021

`androidx.games:games-controller:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..c87dbd94f9a843d9a766afb6de82957457b96c05/src/paddleboat)

**Bug Fixes**

- Fixed packaging error that caused Prefab import to fail on empty, unused architecture/version permutations.

### Version 1.0.0-rc01

July 12, 2021

`androidx.games:games-controller:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc..c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8/GameController)

**Bug Fixes**

- Fixed an incompatibility issue with the latest `GameActivity`

### Version 1.0.0-beta01

June 30, 2021

`androidx.games:games-controller:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc/GameController)

**API Changes**

- Functions which returned a boolean for success or failure now return a `Paddleboat_Error_Code` enum.
- `Paddleboat_onPause` renamed to `Paddleboat_onStop`
- `Paddleboat_onResume` renamed to `Paddleboat_onStart`
- Paddleboat_processGameActivityEvent split into two functions: `Paddleboat_processGameActivityKeyInputEvent` and `Paddleboat_processGameActivityMotionInputEvent`
- Removed extended controller features that required building against a preview Android S SDK
- Added `Paddleboat_getBackButtonConsumed` function
- Controller and mouse status callbacks now have an optional parameter of a pointer to user defined data
- Moved controller name string out of device info structure, now accessed via `Paddleboat_getControllerName` function

**Bug Fixes**

- Fixed an issue where a controller that doesn't initially report itself as a controller, but later on does via an onInputDeviceChanged message, wasn't being properly detected as a controller connection.

### Version 1.0.0-alpha01

June 16, 2021

`androidx.games:games-controller:1.0.0-alpha01` is released.

**New Features**

- Games-Controller is a new library that provides a C API for detecting, reading input from, and interacting with game controller devices.

## Games-Text-Input 2.1

### Version 2.1.0-alpha01

July 26, 2023

`androidx.games:games-text-input:2.1.0-alpha01` is released. [Version 2.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/61b7df48b84d37584f6a2d706d892a1f592d43a6..6d48478dde57eed989d8910c3d91a0f6bce2bcc4/game-text-input)

**New Features**

- Add a support of multi-line and single-line modes

**API Changes**

- Add `isSoftwareKeyboardVisible` function
- Add bitfield definitions for `GameActivity_setImeEditorInfo`
- Add `onEditorAction` callback

**Bug Fixes**

- Fix for hardware and software keyboards being out of sync
- Clear focus when soft keyboard is hidden

## Games-Text-Input 2.0

### Version 2.0.0

March 8, 2023

`androidx.games:games-text-input:2.0.0` is released. [Version 2.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..e1e20061358fd38e7f014d4d02b9e2878c2169a9/games-text-input)

**Important changes since 1.1.1**

- Major version update due to the changes to the build system, there are no updates to the library/API itself.

## Games-Text-Input Version 1.1

### Version 1.1.2-alpha01

November 9, 2022

`androidx.games:games-text-input:1.1.2-alpha01` is released. [Version 1.1.2-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/df59ba84ac245cfd9db805acc925afd4b19c5566..c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf/game-text-input)

**New Features**

- No new changes

### Version 1.1.1

July 13, 2022

`androidx.games:games-text-input:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4f851ef851998ea2cb65dad519f595377fd73fcf..df59ba84ac245cfd9db805acc925afd4b19c5566/GameTextInput)

**Bug Fixes**

- Fixed issues with missing .aar file in previous release.

### Version 1.1.0

February 9, 2022

`androidx.games:games-text-input:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/60b0ddc9b45463685713d52558c2fa62c4ca50bb..4f851ef851998ea2cb65dad519f595377fd73fcf/GameTextInput)

**Important changes since 1.0.0**
- Added WindowInsets listening and querying functionality to GameTextInput
- Add missing `gamecommon.h` header

### Version 1.1.0-rc01

January 26, 2022

`androidx.games:games-text-input:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e8e9971ec507a219142344409f5176cc4aea8b3f..60b0ddc9b45463685713d52558c2fa62c4ca50bb/GameTextInput)

### Version 1.1.0-beta01

December 15, 2021

`androidx.games:games-text-input:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/91cc404409d0e732941ce0d13bbaf12739bb14a8..e8e9971ec507a219142344409f5176cc4aea8b3f/GameTextInput)

**Bug Fixes**

- Fix waterfall and IME insets
- Add missing gamecommon.h header

### Version 1.1.0-alpha01

October 13, 2021

`androidx.games:games-text-input:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/565cb7b2f1f88bc527c07a1512ab6ae719b7990d..91cc404409d0e732941ce0d13bbaf12739bb14a8/GameTextInput)

**API Changes**

- Added IME insets functionality to GameTextInput

## Games-Text-Input Version 1.0

### Version 1.0.0

August 4, 2021

`androidx.games:games-activity:1.0.0`, `androidx.games:games-controller:1.0.0`, and `androidx.games:games-text-input:1.0.0` are released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..565cb7b2f1f88bc527c07a1512ab6ae719b7990d/GameTextInput)

**Major features of 1.0.0**

This is the initial release to stable of Games-Activity, Games-Controller and Games-Text-Input. See the [AGDK Home Page](https://developer.android.com/games/agdk) for more information.

### Version 1.0.0-rc01

July 12, 2021

`androidx.games:games-text-input:1.0.0-rc01` is released with no changes. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc..c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8/GameTextInput)

### Version 1.0.0-beta01

June 30, 2021

`androidx.games:games-text-input:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c94374d6b144787f79e7202316388a97077c6c34..66204fc44cbcee003287d7a37f98eefd22bca9dc/GameTextInput)

**API Changes**

- Improved ownership model of GameTextInputState objects.
- Tidying of types to be consistent with NDK.

### Version 1.0.0-alpha01

June 16, 2021

`androidx.games:games-text-input:1.0.0-alpha01` is released.

**New Features**

- Games-Text-Input is a new library to help game developers use Android soft keyboard input from C/C++.

## Games Frame Pacing Version 2.3

### Version 2.3.0-alpha01

March 26, 2025

`androidx.games:games-frame-pacing:2.3.0-alpha01` is released. Version 2.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/a29e855e6f39df2ba1ef83eb7897c257ee717d66..044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787/games-frame-pacing).

**New Features**

- Upgrade to Gradle 8.8.1 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))
- Upgrade to Java 17 ([1ed0153](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/1ed0153))
- Change `targetSdk` to 35 ([eddf605](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+/eddf605))

**Bug Fixes**

- Various bug fixes ([List of fixes](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/a29e855e6f39df2ba1ef83eb7897c257ee717d66..044fd03c4a7d3b75aeb6ca2bd7fb6155d2cdb787/games-frame-pacing))

## Games Frame Pacing Version 2.1

### Version 2.1.3

July 2, 2025

`androidx.games:games-frame-pacing:2.1.3` is released. Version 2.1.3 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/a29e855e6f39df2ba1ef83eb7897c257ee717d66..f81f888fe11e9540dd580edf5993232172ed3cbe/games-frame-pacing).

**Bug Fixes**

- Enables support for 16KB page size.

### Version 2.1.2

July 24, 2024

`androidx.games:games-frame-pacing:2.1.2` is released. Version 2.1.2 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/394f81c696e264c403a8491dd6e37aa89e3da00d..a29e855e6f39df2ba1ef83eb7897c257ee717d66/games-frame-pacing).

**Bug Fixes**

- Swappy now uses `AChoreographer_postVsyncCallback` from API 33 to calculate the presentation time more accurately. This fixes a bug on 120hz devices where frames are dropped.

### Version 2.1.1

July 10, 2024

`androidx.games:games-frame-pacing:2.1.1` is released. Version 2.1.1 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4880f53064c0abc7f2adaa4895e0c9e1c0ade08b..394f81c696e264c403a8491dd6e37aa89e3da00d/games-frame-pacing).

**Bug Fixes**

- Properly unregister display listener from swappy to avoid a hang.
- Fix a crash in `ChoreographerFilter::onSettingsChanged` using destroyed mutex.

### Version 2.1.0

November 15, 2023

`androidx.games:games-frame-pacing:2.1.0` is released. [Version 2.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/408e113fbcd92d04fc5bd273bc2ba1f3a1109488..4880f53064c0abc7f2adaa4895e0c9e1c0ade08b/games-frame-pacing)

### Version 2.1.0-rc01

September 20, 2023

`androidx.games:games-frame-pacing:2.1.0-rc01` is released. [Version 2.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/3643862ac9c7c2fe01ab511cc602e158db1dd21b..408e113fbcd92d04fc5bd273bc2ba1f3a1109488/games-frame-pacing)

### Version 2.1.0-beta01

May 24, 2023

`androidx.games:games-frame-pacing:2.1.0-beta01` is released. [Version 2.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/5262617d2206673e2e8548596331ead5c0ec41a8..3643862ac9c7c2fe01ab511cc602e158db1dd21b/games-frame-pacing)

**Bug Fixes**

- Timeout in case `NDKChoreographer` initialization fails ([ef466d](https://android-review.googlesource.com/#/q/I02d718cb655ddf3d6a4fbf0ad74e5956dd3eeded))
- When using `SwappyGL_getSupportedRefreshPeriodsNS` query refresh rates explicitly from the system ([c85235](https://android-review.googlesource.com/#/q/I9e31c9ac4790c75e64338f497b67d2a72c33f301))

### Version 2.1.0-alpha01

April 5, 2023

`androidx.games:games-frame-pacing:2.1.0-alpha01` is released. [Version 2.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/6bd669c3efdee9b9c81e185d81ee21c8366b8b7d..5262617d2206673e2e8548596331ead5c0ec41a8/games-frame-pacing)

**New Features**

- New API to reset the frame-pacing state.
- New API to disable swappy's frame-pacing impact while still observing the CPU \& GPU times.

**API Changes**

- `SwappyGL_resetFramePacing/SwappyVk_resetFramePacing` can now be used to reset the internal frame-pacing state. The frame pacing will now only consider data from the point when the reset API is called.
- `SwappyGL_enableFramePacing/SwappyVk_enableFramePacing` can now be used to enable/disable swappy's frame pacing. When disabled,
- `SwappyGL_enableBlockingWait/SwappyVk_enableBlockingWait` can be used to control whether a blocking wait of the last frame's GPU work happens when frame-pacing is disabled.

**Bug Fixes**

- Performance improvements are made for GPU bound cases when using Swappy GL API.

## Games Frame Pacing Version 2.0

### Version 2.0.0

March 8, 2023

`androidx.games:games-frame-pacing:2.0.0` is released. [Version 2.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..e1e20061358fd38e7f014d4d02b9e2878c2169a9/games-frame-pacing)

**Important changes since 1.10.1**

- The build system went through major changes leading to only one library generated instead of multiple per SDK/NDK version.
- Vulkan Frame Statistics are added.
- A new API for clearing frame statistics is added.
- The logs are all silent in release mode, they can be enabled in debug mode.

### Version 2.0.0-rc01

February 22, 2023

`androidx.games:games-frame-pacing:2.0.0-rc01` is released. [Version 2.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/27573e27acd71cc7ba80ce592c76611edc3b6328..83d676655ca28ed426bdaf0602bb3046cbf79ce8/games-frame-pacing)

**New Features**

- Logging is now hidden behind a compile flag. By default release build of the library has no logging, and debug release of the library has all the logging turned on.

### Version 2.0.0-beta01

February 8, 2023

`androidx.games:games-frame-pacing:2.0.0-beta01` is released. [Version 2.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/fd1ddaa12b110384031f09fb8fb6b96d80f896c4..27573e27acd71cc7ba80ce592c76611edc3b6328/games-frame-pacing)

**New Features**

- New API introduced to clear frame statistics.

**API Changes**

- Added `SwappyGL_clearStats` and `SwappyGL_clearStats` APIs.

### Version 2.0.0-alpha01

January 11, 2023

`androidx.games:games-frame-pacing:2.0.0-alpha01` is released. [Version 2.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf..fd1ddaa12b110384031f09fb8fb6b96d80f896c4/games-frame-pacing)

**New Features**

- Added vulkan frame statistics

**API Changes**

- Major version increase due to build files refactoring
- Added 3 new APIs : `SwappyVk_enableStats`, `SwappyVk_recordFrameStart`, and `SwappyVk_getStats`

**Bug Fixes**

- Apply threshold only in auto swap mode ([Ic0786](https://android-review.googlesource.com/c/platform/frameworks/opt/gamesdk/+/2281447))

## Games Frame Pacing 1.10

### Version 1.10.2-alpha01

November 9, 2022

`androidx.games:games-frame-pacing:1.10.2-alpha01` is released. [Version 1.10.2-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c1b2d4ff92af5ccfa4d345a21f67f1690fba1eaf/games-frame-pacing)

**New Features**

- No new changes

### Version 1.10.1

June 15, 2022

`androidx.games:games-frame-pacing:1.10.1` is released. [Version 1.10.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/ac44a0dd8d5c0a5919346be5df11d473fdb87151../src/swappy)

**Bug Fixes**

- Fix for swappy not building with ndk \<23 and \>17.
- Exposed API to retrieve the refresh rates supported by the display.

### Version 1.10.0

February 23, 2022

`androidx.games:games-frame-pacing:1.10.0` is released. [Version 1.10.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/4f851ef851998ea2cb65dad519f595377fd73fcf..ac44a0dd8d5c0a5919346be5df11d473fdb87151/src/swappy)

**Important changes since 1.9.0**

- Ignore polluting choreographer filter inputs and smooth more to prevent freezes on emulator
- Add \*_uninjectTracer functions.

### Version 1.10.0-rc01

February 9, 2022

`androidx.games:games-frame-pacing:1.10.0-rc01` is released. [Version 1.10.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/60b0ddc9b45463685713d52558c2fa62c4ca50bb..4f851ef851998ea2cb65dad519f595377fd73fcf/src/swappy)

### Version 1.10.0-beta01

January 26, 2022

`androidx.games:games-frame-pacing:1.10.0-beta01` is released. [Version 1.10.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/e8e9971ec507a219142344409f5176cc4aea8b3f..60b0ddc9b45463685713d52558c2fa62c4ca50bb/src/swappy)

### Version 1.10.0-alpha01

December 15, 2021

`androidx.games:games-frame-pacing:1.10.0-alpha01` is released. [Version 1.10.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/91cc404409d0e732941ce0d13bbaf12739bb14a8..e8e9971ec507a219142344409f5176cc4aea8b3f/src/swappy)

**New Features**

- Addition of `SwappyGL_uninjectTracer` function.

**API Changes**

- Remove callbacks that were previously added using `SwappyGL_injectTracer` by using `SwappyGL_uninjectTracer(const SwappyTracer *t)` API.

## Games Frame Pacing 1.9

### Version 1.9.1

October 13, 2021

`androidx.games:games-frame-pacing:1.9.1` is released. [Version 1.9.1 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8..91cc404409d0e732941ce0d13bbaf12739bb14a8/src/swappy)

**Bug Fixes**

- Fixed [b/199487756](https://issuetracker.google.com/199487756)

### Version 1.9.0

July 12, 2021

`androidx.games:games-frame-pacing:1.9.0` is released. [Version 1.9.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc..c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8/src/swappy)

**Important changes since 1.7.0**

- Updated to match internal versioning scheme.

## Games Frame Pacing 1.7.0

### Version 1.7.0

June 30, 2021

`androidx.games:games-frame-pacing:1.7.0` is released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/11d9f8ed1ee4f04f87dd8ab0ef7c0690e63e1078..66204fc44cbcee003287d7a37f98eefd22bca9dc/src/swappy)

### Version 1.7.0-rc01

June 2, 2021

`androidx.games:games-frame-pacing:1.7.0-rc01` is released. Version 1.7.0-rc01 contains these commits.

### Version 1.7.0-beta02

February 24, 2021

`androidx.games:games-frame-pacing:1.7.0-beta02` is released.

### Version 1.7.0-beta01

December 16, 2020

`androidx.games:games-frame-pacing:1.7.0-beta01` is released.

## Games Performance Tuner 1.4.3

### Version 2.0.0-rc01

July 24, 2024

`androidx.games:games-performance-tuner:2.0.0-rc01` is released. Version 2.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/12ef8dab8ec4a03116abce11081601d883d8170e..17ce5e87964a3fd53662850262c2740b9b70cee8/games-performance-tuner).

### Version 1.4.3

July 12, 2021

`androidx.games:games-performance-tuner:1.4.3` is released. [Version 1.4.3 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/66204fc44cbcee003287d7a37f98eefd22bca9dc..c6508fc0745ecbc0bccc6e55bcc47aefc0ada7a8/src/tuningfork)

**Important changes since 1.1.0**

- Updated to match internal versioning scheme.

## Games Performance Tuner 1.1.0

### Version 1.1.0

June 30, 2021

`androidx.games:games-performance-tuner:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/opt/gamesdk/+log/11d9f8ed1ee4f04f87dd8ab0ef7c0690e63e1078..66204fc44cbcee003287d7a37f98eefd22bca9dc/src/tuningfork)

### Version 1.1.0-rc01

June 2, 2021

`androidx.games:games-performance-tuner:1.1.0-rc01` is released. Version 1.1.0-rc01 contains these commits.

### Version 1.1.0-beta03

April 21, 2021

`androidx.games:games-performance-tuner:1.1.0-beta03` is released.

### Version 1.1.0-beta02

February 24, 2021

`androidx.games:games-performance-tuner:1.1.0-beta02` is released.

### Version 1.1.0-beta01

December 16, 2020

`androidx.games:games-performance-tuner:1.1.0-beta01` is released.

### Version 1.1.0-alpha01

androidx.games:games-performance-tuner:1.1.0-alpha01 is released.

## Version 1.0.0

### Version 1.0.0-alpha02

August 12, 2020

The Android Gaming library was renamed to the Android Games library.  

    androidx.gaming -> androidx.games

### Version 1.0.0-alpha01

June 10, 2020

androidx.games:1.0.0-alpha01 is released.