---
title: https://developer.android.com/guide/playcore/in-app-review/native
url: https://developer.android.com/guide/playcore/in-app-review/native
source: md.txt
---

This guide describes how to integrate in-app reviews in your app using native (C
or C++) code. There are separate integration guides if you are using [Kotlin or
Java](https://developer.android.com/guide/playcore/in-app-review/kotlin-java), [Unity](https://developer.android.com/guide/playcore/in-app-review/unity) or [Unreal Engine](https://developer.android.com/guide/playcore/in-app-review/unreal-engine).

## Native SDK overview

The Play Core Native SDK is part of [Google Play Core libraries](https://developer.android.com/guide/playcore) family. The
Play Core Native SDK includes a C header file, `review.h`, that wraps
[`ReviewManager`](https://developer.android.com/reference/com/google/android/play/core/review/ReviewManager) from the Java Play In-App Review libraries. This header
file allows your app to call the API directly from your native code. For an
overview of the public functions that are available, see the [Play Review native
module documentation](https://developer.android.com/reference/native/play/core/group/review).

[`ReviewManager_requestReviewFlow`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_requestreviewflow) starts a request that gathers the
information that is required to launch the in-app review flow later. You can
track the result of the request using [`ReviewManager_getReviewStatus`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_getreviewstatus). For
more information about all the statuses that `ReviewManager_getReviewStatus` can
return, see [`ReviewErrorCode`](https://developer.android.com/reference/native/play/core/group/review#reviewerrorcode).

Both the request and launch functions return `REVIEW_NO_ERROR` if the function
succeeds.

## Set up your development environment


## Download Play Core Native SDK

Before downloading, you must agree to the following terms and conditions.

## Terms and Conditions

Last modified: September 24, 2020

1. By using the Play Core Software Development Kit, you agree to these terms in addition to the [Google APIs Terms of Service](https://developers.google.com/terms) ("API ToS"). If these terms are ever in conflict, these terms will take precedence over the API ToS. Please read these terms and the API ToS carefully.
2. For purposes of these terms, "APIs" means Google's APIs, other developer services, and associated software, including any Redistributable Code.
3. "Redistributable Code" means Google-provided object code or header files that call the APIs.
4. Subject to these terms and the terms of the API ToS, you may copy and distribute Redistributable Code solely for inclusion as part of your API Client. Google and its licensors own all right, title and interest, including any and all intellectual property and other proprietary rights, in and to Redistributable Code. You will not modify, translate, or create derivative works of Redistributable Code.
5. Google may make changes to these terms at any time with notice and the opportunity to decline further use of the Play Core Software Development Kit. Google will post notice of modifications to the terms at <https://developer.android.com/guide/playcore/license>. Changes will not be retroactive.
I have read and agree with the above terms and conditions <button class="button button-disabled"> Download Play Core Native SDK </button> [Download Play Core Native SDK](https://dl.google.com/games/play/core/play-core-native-sdk-1.16.0.zip)

*play-core-native-sdk-1.16.0.zip*

1. Do either of the following:

   - Install [Android Studio](https://developer.android.com/studio) version 4.0 or higher. Use the SDK Manager UI to install Android SDK Platform version 10.0 (API level 29).
   - Install the [Android SDK command-line tools](https://developer.android.com/studio#command-tools) and use [`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager) to install Android SDK Platform version 10.0 (API level 29).
2. Prepare Android Studio for native development by using the
   [SDK Manager](https://developer.android.com/studio/intro/update#sdk-manager) to install the latest
   CMake and Android Native Development Kit (NDK). For more information on
   creating or importing native projects, see
   [Getting Started with the NDK](https://developer.android.com/ndk/guides).

3. Download the zip file and extract it alongside your project.

   | Download Link | Size | SHA-256 Checksum |
   |---|---|---|
   | <button class="devsite-dialog-button button-white button-regular gc-analytics-event" data-category="Play Core Native SDK" data-action="download" data-label="play_core_native_sdk_zip" data-modal-dialog-id="play_core_native_sdk_zip">play-core-native-sdk-1.16.0.zip</button> | 54.8 MiB | 008b8fedc6179a6dc6ccc21af75591afc7036f78f3d5559d844f1b923934fef0 |

4. Update your app's `build.gradle` file as shown below:

   ### Groovy

   ```groovy
       // App build.gradle

       plugins {
         id 'com.android.application'
       }

       // Define a path to the extracted Play Core SDK files.
       // If using a relative path, wrap it with file() since CMake requires absolute paths.
       def playcoreDir = file('../path/to/playcore-native-sdk')

       android {
           defaultConfig {
               ...
               externalNativeBuild {
                   cmake {
                       // Define the PLAYCORE_LOCATION directive.
                       arguments "-DANDROID_STL=c++_static",
                                 "-DPLAYCORE_LOCATION=$playcoreDir"
                   }
               }
               ndk {
                   // Skip deprecated ABIs. Only required when using NDK 16 or earlier.
                   abiFilters 'armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'
               }
           }
           buildTypes {
               release {
                   // Include Play Core Library proguard config files to strip unused code while retaining the Java symbols needed for JNI.
                   proguardFile '$playcoreDir/proguard/common.pgcfg'
                   proguardFile '$playcoreDir/proguard/gms_task.pgcfg'
                   proguardFile '$playcoreDir/proguard/per-feature-proguard-files'
                   ...
               }
               debug {
                   ...
               }
           }
           externalNativeBuild {
               cmake {
                   path 'src/main/CMakeLists.txt'
               }
           }
       }

       dependencies {
           // Import these feature-specific AARs for each Google Play Core library.
           implementation 'com.google.android.play:app-update:2.1.0'
           implementation 'com.google.android.play:asset-delivery:2.3.0'
           implementation 'com.google.android.play:integrity:1.6.0'
           implementation 'com.google.android.play:review:2.0.2'

           // Import these common dependencies.
           implementation 'com.google.android.gms:play-services-tasks:18.0.2'
           implementation files("$playcoreDir/playcore-native-metadata.jar")
           ...
       }
       
   ```

   ### Kotlin

   ```kotlin
   // App build.gradle

   plugins {
       id("com.android.application")
   }

   // Define a path to the extracted Play Core SDK files.
   // If using a relative path, wrap it with file() since CMake requires absolute paths.
   val playcoreDir = file("../path/to/playcore-native-sdk")

   android {
       defaultConfig {
           ...
           externalNativeBuild {
               cmake {
                   // Define the PLAYCORE_LOCATION directive.
                   arguments += listOf("-DANDROID_STL=c++_static", "-DPLAYCORE_LOCATION=$playcoreDir")
               }
           }
           ndk {
               // Skip deprecated ABIs. Only required when using NDK 16 or earlier.
               abiFilters.clear()
               abiFilters += listOf("armeabi-v7a", "arm64-v8a", "x86", "x86_64")
           }
       }
       buildTypes {
           release {
               // Include Play Core Library proguard config files to strip unused code while retaining the Java symbols needed for JNI.
               proguardFile("$playcoreDir/proguard/common.pgcfg")
               proguardFile("$playcoreDir/proguard/gms_task.pgcfg")
               proguardFile("$playcoreDir/proguard/per-feature-proguard-files")
               ...
           }
           debug {
               ...
           }
       }
       externalNativeBuild {
           cmake {
               path = "src/main/CMakeLists.txt"
           }
       }
   }

   dependencies {
       // Import these feature-specific AARs for each Google Play Core library.
       implementation("com.google.android.play:app-update:2.1.0")
       implementation("com.google.android.play:asset-delivery:2.3.0")
       implementation("com.google.android.play:integrity:1.6.0")
       implementation("com.google.android.play:review:2.0.2")

       // Import these common dependencies.
       implementation("com.google.android.gms:play-services-tasks:18.0.2")
       implementation(files("$playcoreDir/playcore-native-metadata.jar"))
       ...
   }
   ```
5. Update your app's `CMakeLists.txt` files as shown below:

   ```
   cmake_minimum_required(VERSION 3.6)

   ...

   # Add a static library called “playcore” built with the c++_static STL.
   include(${PLAYCORE_LOCATION}/playcore.cmake)
   add_playcore_static_library()

   // In this example “main” is your native code library, i.e. libmain.so.
   add_library(main SHARED
           ...)

   target_include_directories(main PRIVATE
           ${PLAYCORE_LOCATION}/include
           ...)

   target_link_libraries(main
           android
           playcore
           ...)
   ```

## Data Collection

The Play Core Native SDK may collect version related data to allow Google to
improve the product, including:

- App's package name
- App's package version
- Play Core Native SDK's version

This data will be collected when you upload [your app package](https://developer.android.com/studio/publish/upload-bundle)
to the Play Console. To opt-out of this data collection process, remove the
`$playcoreDir/playcore-native-metadata.jar` import in the build.gradle file.

Note, this data collection related to your use of the Play Core Native SDK and
Google's use of the collected data is separate and independent of Google's
collection of library dependencies declared in Gradle when you upload your app
package to the Play Console.

After you integrate the Play Core Native SDK into your project, include the
following line in files that contain API calls:

## Include review.h

After integrating the Play Core Native SDK into your project, include the
following line in files that will contain API calls:

    #include "play/review.h"

## Initialize the Review API

Whenever you want to use the API, you must initialize it first by calling the
[`ReviewManager_init`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_init) function, as shown in the following example built
with [`android_native_app_glue.h`](https://developer.android.com/ndk/guides/concepts#naa):

    void android_main(android_app* app) {
      app->onInputEvent = HandleInputEvent;

      ReviewErrorCode error_code = ReviewManager_init(app->activity->vm, app->activity->clazz);
      if (error_code == REVIEW_NO_ERROR) {
        // You can use the API.
      }
    }

## Request the in-app review flow

Follow the guidance about [when to request in-app reviews](https://developer.android.com/guide/playcore/in-app-review#when-to-request) to determine good
points in your app's user flow to prompt the user for a review (for example,
after a user dismisses the summary screen at the end of a level in a game). When
your app gets close one of these points, call
[`ReviewManager_requestReviewFlow`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_requestreviewflow) to asynchronously request the information
that your app needs to launch an in-app review flow. Monitor the progress of the
`ReviewManager_requestReviewFlow` operation by calling
[`ReviewManager_getReviewStatus`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_getreviewstatus), for example once every frame. This might
take up to a couple of seconds, so you should start this process before your app
reaches the point when you want to show the in-app review flow.

    ReviewErrorCode error_code = ReviewManager_requestReviewFlow();
    if (error_code == REVIEW_NO_ERROR) {
        // The request has successfully started, check the status using
        // ReviewManager_getReviewStatus.
    } else {
        // Error such as REVIEW_PLAY_STORE_NOT_FOUND indicating that the in-app
        // review isn't currently possible.
    }

## Handle statuses and launch the in-app review flow

Whenever a request has started or the in-app review flow is launched, you can
check the status using [`ReviewManager_getReviewStatus`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_getreviewstatus). This lets you
define the logic depending on the API status. One way to approach this is to
keep the status as a global variable and check whether the status is
`REVIEW_REQUEST_FLOW_COMPLETED` when the user performs a certain action (for
example, tapping a "Next Level" button in a game), as shown in the following
example:

    ReviewStatus status;
    ReviewErrorCode error_code = ReviewManager_getReviewStatus(&status);
    if (error_code != REVIEW_NO_ERROR) {
        // There was an error with the most recent operation.
        return;
    }

    switch (status) {
        case REVIEW_REQUEST_FLOW_PENDING:
            // Request is ongoing. The flow can't be launched yet.
            break;
        case REVIEW_REQUEST_FLOW_COMPLETED:
            // Request completed. The flow can be launched now.
            break;
        case REVIEW_LAUNCH_FLOW_PENDING:
            // The review flow is ongoing, meaning the dialog might be displayed.
            break;
        case REVIEW_LAUNCH_FLOW_COMPLETED:
            // The review flow has finished. Continue with your app flow (for
            // example, move to the next screen).
            break;
        default:
            // Unknown status.
            break;
    }

When the status is `REVIEW_REQUEST_FLOW_COMPLETED` and your app is ready, launch
the in-app review flow:

```c
// This call uses https://developer.android.com/ndk/guides/concepts#naa.
ReviewErrorCode error_code = ReviewManager_launchReviewFlow(app->activity->clazz);
if (error_code != REVIEW_NO_ERROR) {
    // There was an error while launching the flow.
    return;
}
```

After launching the in-app review flow, keep checking the status for completion
and continue with your app flow. A common way to handle this, would be by
following the [Game Loop](https://developer.android.com/games/develop/gameloops) pattern.

## Free resources

Don't forget to free resources by calling the [`ReviewManager_destroy`](https://developer.android.com/reference/native/play/core/group/review#reviewmanager_destroy)
function once your app has finished using the API (for example, after the in-app
review flow is completed).

    void ReviewManager_destroy();

## Next steps

[Test your app's in-app review flow](https://developer.android.com/guide/playcore/in-app-review/test) to verify that your integration is
working correctly.