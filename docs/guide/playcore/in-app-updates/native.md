---
title: https://developer.android.com/guide/playcore/in-app-updates/native
url: https://developer.android.com/guide/playcore/in-app-updates/native
source: md.txt
---

This guide describes how to support [in-app updates](https://developer.android.com/guide/playcore/in-app-updates) in your app using native
code (C or C++). There are separate guides for cases where your implementation
uses [the Kotlin programming language or the Java programming language](https://developer.android.com/guide/playcore/in-app-updates/kotlin-java), and
cases where your implementation uses [Unity](https://developer.android.com/guide/playcore/in-app-updates/unity) or [Unreal Engine](https://developer.android.com/guide/playcore/in-app-updates/unreal-engine).
| **Note:** The Native API for in-app updates requires your app to [use Play Core
| library](https://developer.android.com/guide/playcore#native) version 1.10.0 or higher.

## Native SDK overview

The Play Core Native SDK is part of the [Play Core SDK](https://developer.android.com/reference/com/google/android/play/core/release-notes) family. The Native
SDK includes a C header file, `app_update.h`, that wraps [`AppUpdateManager`](https://developer.android.com/reference/com/google/android/play/core/appupdate/AppUpdateManager)
from the Java Play In-App Update Library. This header file allows your app to
call the API for in-app updates directly from your native code.

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
I have read and agree with the above terms and conditions  
Download Play Core Native SDK [Download Play Core Native SDK](https://dl.google.com/games/play/core/play-core-native-sdk-1.16.0.zip)

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
   | play-core-native-sdk-1.16.0.zip | 54.8 MiB | 008b8fedc6179a6dc6ccc21af75591afc7036f78f3d5559d844f1b923934fef0 |

4. Update your app's `build.gradle` file as shown below:

   ### Groovy

   ```groovy
       // App build.gradle

       plugins {
         id 'com.android.application'
       }

       // Define a path to the extracted Play Core SDK files.
       // If using a relative path, wrap it with file() since CMake requires absolute paths.
       def playcoreDir = file('<var translate="no">../path/to/playcore-native-sdk</var>')

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
                   proguardFile '$playcoreDir/proguard/<var translate="no">per-feature-proguard-files</var>'
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
   val playcoreDir = file("<var translate="no">../path/to/playcore-native-sdk</var>")

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
               proguardFile("$playcoreDir/proguard/<var translate="no">per-feature-proguard-files</var>")
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

    #include "play/app_update.h"

## Initialize the in-app update API

Whenever you use the in-app update API, initialize it first by calling the
[`AppUpdateManager_init()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_init) function, as shown in the following example built
with [`android_native_app_glue.h`](https://developer.android.com/ndk/guides/concepts#naa):  

    void android_main(android_app* app) {
      app->onInputEvent = HandleInputEvent;

      AppUpdateErrorCode error_code =
        AppUpdateManager_init(app->activity->vm, app->activity->clazz);
      if (error_code == APP_UPDATE_NO_ERROR) {
        // You can use the API.
      }
    }

## Check for update availability

Before you request an update, check if there is an update available for your
app. [`AppUpdateManager_requestInfo()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requestinfo) starts an asynchronous request that
gathers the required information to launch the in-app update flow later. The
function returns `APP_UPDATE_NO_ERROR` if the request starts successfully.  

    AppUpdateErrorCode error_code = AppUpdateManager_requestInfo()

    if (error_code == APP_UPDATE_NO_ERROR) {
        // The request has successfully started, check the result using
        // AppUpdateManager_getInfo.
    }

You can track the ongoing process and result of the request using
[`AppUpdateManager_getInfo()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_getinfo). In addition to the error code, this function
returns an [`AppUpdateInfo`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo) opaque struct, which you can use to retrieve
information about the update request. For example, you might want to call this
function in every game loop until it returns a non-null result for `info`:  

    AppUpdateInfo* info;
    GameUpdate() {

       // Keep calling this in every game loop until info != nullptr
       AppUpdateErrorCode error_code = AppUpdateManager_getInfo(&info);

       if (error_code == APP_UPDATE_NO_ERROR && info != nullptr) {
           // Successfully started, check the result in the following functions
       }
    ...
    }

### Check update staleness

In addition to checking whether an update is available, you might also want to
check how much time has passed since the user was last notified of an update
through the Play Store. This can help you decide whether you should initiate a
flexible update or an immediate update. For example, you might wait a few days
before notifying the user with a flexible update, and a few days after that
before requiring an immediate update.

Use [`AppUpdateInfo_getClientVersionStalenessDays()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_getclientversionstalenessdays) to check the number of
days since the update became available through the Play Store:  

    int32_t staleness_days = AppUpdateInfo_getClientVersionStalenessDays(info);

### Check update priority

The Google Play Developer API lets you set the priority of each update. This
allows your app to decide how strongly to recommend an update to the user. For
example, consider the following strategy for setting update priority:

- Minor UI improvements: **Low-priority** update; request neither a flexible update nor an immediate update. Update only when the user isn't interacting with your app.
- Performance improvements: **Medium-priority** update; request a flexible update.
- Critical security update: **High-priority** update; request an immediate update.

To determine priority, Google Play uses an integer value between 0 and 5, with 0
being the default and 5 being the highest priority. To set the priority for an
update, use the `inAppUpdatePriority` field under [`Edits.tracks.releases`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks#release)
in the Google Play Developer API. All newly-added versions in the release are
considered to be the same priority as the release. Priority can only be set when
rolling out a new release and cannot be changed later.

Set the priority using the Google Play Developer API, as described in the [Play
Developer API documentation](https://developers.google.com/android-publisher/tracks#apk_workflow_example). Specify in-app update priority in the
[`Edit.tracks`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks) resource passed in the [`Edit.tracks: update`](https://developers.google.com/android-publisher/api-ref/rest/v3/edits.tracks/update) method.
The following example demonstrates releasing an app with version code 88 and
`inAppUpdatePriority` 5:  

```json
{
  "releases": [{
      "versionCodes": ["88"],
      "inAppUpdatePriority": 5,
      "status": "completed"
  }]
}
```

In your app's code, you can check the priority level for a given update using
[`AppUpdateInfo_getPriority()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_getpriority):  

    int32_t priority = AppUpdateInfo_getPriority(info);

## Start an update

After you confirm that an update is available, you can request an update using
[`AppUpdateManager_requestStartUpdate()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requeststartupdate). Before you request an update, get
an up-to-date `AppUpdateInfo` object and create an [`AppUpdateOptions`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions)
object to configure the update flow. An `AppUpdateOptions` object defines
options for an in-app update flow, including whether the update should be
flexible or immediate.

The following example creates an `AppUpdateOptions` object for a flexible update
flow:  

    // Creates an AppUpdateOptions configuring a flexible in-app update flow.
    AppUpdateOptions* options;
    AppUpdateErrorCode error_code = AppUpdateOptions_createOptions(APP_UPDATE_TYPE_FLEXIBLE, &options);

The following example creates an `AppUpdateOptions` object for an immediate
update flow:  

    // Creates an AppUpdateOptions configuring an immediate in-app update flow.
    AppUpdateOptions* options;
    AppUpdateErrorCode error_code = AppUpdateOptions_createOptions(APP_UPDATE_TYPE_IMMEDIATE, &options);

The `AppUpdateOptions` object also contains an `AllowAssetPackDeletion` field
that defines whether the update is allowed to clear [asset packs](https://developer.android.com/guide/app-bundle/asset-delivery) in case of
limited device storage. This field is set to `false` by default, but you can use
the [`AppUpdateOptions_setAssetPackDeletionAllowed()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions_setassetpackdeletionallowed) method to set it to
`true` instead:  

    bool allow = true;
    AppUpdateErrorCode error_code = AppUpdateOptions_setAssetPackDeletionAllowed(options, allow);

| **Caution:** Use the `AllowAssetPackDeletion` API option with care to avoid accidentally deleting assets. Before setting this option to `true`, you should check whether the update is allowed with this option set to `false`.

After you have an up-to-date `AppUpdateInfo` object and a properly-configured
`AppUpdateOptions` object, call `AppUpdateManager_requestStartUpdate()` to
asynchronously request an update flow, passing in an Android Activity `jobject`
for the final parameter.  

    AppUpdateErrorCode request_error_code =
    AppUpdateManager_requestStartUpdate(info, options, app->activity->clazz);

To free up resources, release instances of `AppUpdateInfo` and
`AppUpdateOptions` that you no longer need by calling
[`AppUpdateInfo_destroy()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateinfo_destroy) and [`AppUpdateOptions_destroy()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateoptions_destroy),
respectively.  

    AppUpdateInfo_destroy(info);
    AppUpdateOptions_destroy(options);

For an immediate update flow, Google Play displays a user confirmation page.
When the user accepts the request, Google Play automatically downloads and
installs the update in the foreground, then restarts the app to the updated
version if installation is successful.

For a flexible update flow, you can keep requesting up-to-date `AppUpdateInfo`
objects to keep track of the current update status while the user continues to
interact with the app. After the download finishes successfully, you must
trigger the completion of the update by calling
[`AppUpdateManager_requestCompleteUpdate()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_requestcompleteupdate), as shown in the following
example:  

    AppUpdateStatus status = AppUpdateInfo_getStatus(info);
    if (status == APP_UPDATE_DOWNLOADED) {
        AppUpdateErrorCode error_code = AppUpdateManager_requestCompleteUpdate();
        if (error_code != APP_UPDATE_NO_ERROR)
        {
          // There was an error while completing the update flow.
        }
    }

Free up resources by calling the [`AppUpdateManager_destroy()`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdatemanager_destroy) function
after your app has finished using the API.

## Error handling

This section describes solutions for common errors indicated by specific
[`AppUpdateErrorCode`](https://developer.android.com/reference/native/play/core/group/appupdate#appupdateerrorcode) values:

- An error code of `-110, APP_UPDATE_INITIALIZATION_NEEDED` indicates that the API has not been initialized successfully. Call `AppUpdateManager_init()` to initialize the API.
- An error code of `-4, APP_UPDATE_INVALID_REQUEST` indicates that some parameters of the update flow request are malformed. Check to make sure that the `AppUpdateInfo` and `AppUpdateOptions` objects are not null and are correctly formatted.
- An error code of `-5, APP_UPDATE_UNAVAILABLE` indicates that there is no applicable update available. Make sure that the target version has the same [package name](https://developer.android.com/studio/build/configure-app-module#change_the_package_name), [application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id), and [signing key](https://developer.android.com/studio/publish/app-signing). If there is an update available, clear the app's cache and call `AppUpdateManager_requestAppUpdateInfo()` again to refresh `AppUpdateInfo`.
- An error code of `-6, APP_UPDATE_NOT_ALLOWED` indicates that the update type indicated by the `AppUpdateOption` object is not allowed. Check whether the `AppUpdateInfo` object indicates that the update type is allowed before starting the update flow.

## Next steps

[Test your app's in-app updates](https://developer.android.com/guide/playcore/in-app-updates/test) to verify that your integration is working
correctly.