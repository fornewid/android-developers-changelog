---
title: https://developer.android.com/guide/playcore/asset-delivery/integrate-native
url: https://developer.android.com/guide/playcore/asset-delivery/integrate-native
source: md.txt
---

Use the steps in this guide to access your app's asset packs from your C and C++
code.

Sample [integration code](https://github.com/android/app-bundle-samples/tree/main/PlayAssetDelivery/NativeSample) is available on GitHub.

## Build for Native

Use the following steps to build Play Asset Delivery into your project's Android
App Bundle. You don't need to use Android Studio to perform these steps.
| **Note:** For a guided tutorial, see the [Using Play Asset Delivery in Native games Codelab](https://codelabs.developers.google.com/codelabs/native-gamepad).

1. Update the version of the Android Gradle plugin in your project's
   `build.gradle` file to `4.0.0` or later.

2. In the top-level directory of your project, create a directory for the asset
   pack. This directory name is used as the asset pack name. Asset pack names
   must start with a letter and can only contain letters, numbers, and
   underscores.

3. In the asset pack directory, create a `build.gradle` file and add the
   following code. Make sure to specify the name of the asset pack and only one
   delivery type:

   ```groovy
   // In the asset pack's build.gradle file:
   plugins {
       id 'com.android.asset-pack'
   }

   assetPack {
       packName = "<var translate="no">asset-pack-name</var>" // Directory name for the asset pack
       dynamicDelivery {
           deliveryType = "[ install-time | fast-follow | on-demand ]"
       }
   }
   ```
4. In the project's app `build.gradle` file, add the name of every asset pack
   in your project as shown below:

   ```groovy
   // In the app build.gradle file:
   android {
       ...
       assetPacks = [":<var translate="no">asset-pack-name</var>", ":<var translate="no">asset-pack2-name</var>"]
   }
   ```
5. In the project's `settings.gradle` file, include all asset packs in your
   project as shown below:

   ```groovy
   // In the settings.gradle file:
   include ':app'
   include ':<var translate="no">asset-pack-name</var>'
   include ':<var translate="no">asset-pack2-name</var>'
   ```
6. In the asset pack directory, create the following subdirectory:
   `src/main/assets`.

7. Place assets in the `src/main/assets` directory. You can create
   subdirectories in here as well. The directory structure for your app should
   now look like the following:

   - `build.gradle`
   - `settings.gradle`
   - `app/`
   - <var translate="no">asset-pack-name</var>`/build.gradle`
   - <var translate="no">asset-pack-name</var>`/src/main/assets/`<var translate="no">your-asset-directories</var>
8. [Build the Android App Bundle with Gradle](https://developer.android.com/studio/build/building-cmdline#build_bundle).
   In the generated app bundle, the root-level directory now includes the
   following:

   - <var translate="no">asset-pack-name</var>`/manifest/AndroidManifest.xml`: Configures the asset pack's identifier and delivery mode
   - <var translate="no">asset-pack-name</var>`/assets/`<var translate="no">your-asset-directories</var>: Directory that contains all assets delivered as part of the asset pack

   Gradle generates the manifest for each asset pack and outputs the `assets/`
   directory for you.
9. (Optional) Configure your app bundle to support different [texture
   compression formats](https://developer.android.com/guide/playcore/asset-delivery/texture-compression).

## Integrate with Play Asset Delivery Library

You implement this API according to the delivery type of
the asset pack you wish to access. These steps are shown in the following
flowchart.
| **Note:** You use a different API to access `install-time` asset packs than `fast-follow` and `on-demand` asset packs.

![Asset pack flow diagram for native code](https://developer.android.com/static/images/app-bundle/asset-pack-flow-native.png)


**Figure 1.** Flow diagram for accessing asset packs

<br />

The [Play Core Native SDK](https://developer.android.com/reference/native/play/core) provides the C header
file `play/asset_pack.h` for requesting asset packs, managing downloads, and
accessing the assets.

## Set up your development environment for Play Core Native SDK


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

## Install-time delivery

Asset packs configured as `install-time` are immediately available at app
launch. Use the [NDK AAssetManager API](https://developer.android.com/ndk/reference/group/asset#aassetmanager) to access
assets served in this mode:  

```c
#include <android/asset_manager.h>
#include <android_native_app_glue.h>
...
AAssetManager* assetManager = app->activity->assetManager;
AAsset* asset = AAssetManager_open(assetManager, "<var translate="no">asset-name</var>", AASSET_MODE_BUFFER);
size_t assetLength = AAsset_getLength(asset);
char* buffer = (char*) malloc(assetLength + 1);
AAsset_read(asset, buffer, assetLength);
```

## Fast-follow and on-demand delivery

The following sections show how to initialize the API, how to get information
about asset packs before downloading them, how to call the API to start the
download, and how to access the downloaded packs. These sections apply to
`fast-follow` and `on-demand` asset packs.

### App launch

Always call [`AssetPackManager_init()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_init)
to initialize the asset pack API before calling any other
function. Check for any
[asset pack error codes](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackerrorcode).  

```c
#include "play/asset_pack.h"
...
AssetPackErrorCode AssetPackManager_init(JavaVM* jvm, jobject android_context);
```

Also be sure to call the following functions in the `onPause()` and `onResume()`
of
[`ANativeActivityCallbacks`](https://developer.android.com/ndk/reference/struct/a-native-activity-callbacks):

- [`AssetPackErrorCode AssetPackManager_onPause()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_onpause)
- [`AssetPackErrorCode AssetPackManager_onResume()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_onresume)

### Get download information about asset packs

Apps are required to disclose the size of the download before fetching the asset
pack. Use the [`AssetPackManager_requestInfo()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestinfo) function to start an
asynchronous request for the size of the download and
whether the pack is already downloading. Then use
[`AssetPackManager_getDownloadState()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getdownloadstate) to poll for the download state
(for example, call this function once per frame in your game loop). If a request
fails, check the [asset pack error codes](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackerrorcode).  

```c
AssetPackErrorCode AssetPackManager_requestInfo();      // Call once
AssetPackErrorCode AssetPackManager_getDownloadState(); // Call once per frame in your game loop
```

The `AssetPackManager_getDownloadState()` function returns the opaque type
[`AssetPackDownloadState`](https://developer.android.com/reference/native/play/core/group/assetpack#group__assetpack_1gaa635665bad061c34cbee483ada331afc)
as an output pointer. Use this pointer to call the following functions:  

```c
AssetPackDownloadState* state;
AssetPackErrorCode error_code = AssetPackManager_getDownloadState(asset-pack-name, &state);
AssetPackDownloadStatus status = AssetPackDownloadState_getStatus(state);
uint64_t downloadedBytes = AssetPackDownloadState_getBytesDownloaded(state);
uint64_t totalBytes = AssetPackDownloadState_getTotalBytesToDownload(state));
AssetPackDownloadState_destroy(state);
```

### Install

Use
[`AssetPackManager_requestDownload()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestdownload)
to start downloading an asset pack for the first time or to request for an asset
pack update to complete:  

```c
AssetPackErrorCode AssetPackManager_requestDownload();  // Call once
AssetPackErrorCode AssetPackManager_getDownloadState(); // Call once per frame in your game loop
```

The `AssetPackManager_getDownloadState()` function returns the opaque type
[`AssetPackDownloadState`](https://developer.android.com/reference/native/play/core/group/assetpack#group__assetpack_1gaa635665bad061c34cbee483ada331afc).
For information on how to use this type, see
[Get download information](https://developer.android.com/guide/playcore/asset-delivery/integrate-native#get-download-information).
| **Note:** The Android system notification bar shows download progress for `fast-follow` and `on-demand` asset packs. The user can cancel the download from this bar at any time.

#### Large downloads

If the download is larger than 200MB and the user is not on Wi-Fi, the download
does not start until the user explicitly gives their consent to proceed with the
download using a mobile data connection. Similarly, if the download is large and
the user loses Wi-Fi, the download pauses and explicit consent is required to
proceed using a mobile data connection. A paused pack has state
`WAITING_FOR_WIFI`. To trigger the UI flow to prompt the user for consent, use
the following:

- [`AssetPackManager_showConfirmationDialog()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_showconfirmationdialog)
- [`AssetPackManager_getShowConfirmationDialogStatus()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getshowconfirmationdialogstatus)

#### Required user confirmation

If a pack has the `REQUIRES_USER_CONFIRMATION` status, the download doesn't
proceed until the user accepts the dialog that is shown with
`AssetPackManager_showConfirmationDialog()`. This status can arise if the
app is not recognized by Play. Note that calling
`AssetPackManager_showConfirmationDialog()` in this case causes the app to be
updated. After the update, request the assets again.

### Access asset packs

You can access an asset pack using file system calls after the download request
reaches the `COMPLETED` state. Each asset pack is stored in a separate directory
in the app's internal storage. Use
[`AssetPackManager_getAssetPackLocation()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_getassetpacklocation)
to get an
[`AssetPackLocation`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation)
for the specified asset pack. Use
[`AssetPackLocation_getStorageMethod()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation_getstoragemethod)
on that location to determine the storage method:

- `ASSET_PACK_STORAGE_APK`: The asset pack is installed as an APK. See [Install-time delivery](https://developer.android.com/guide/playcore/asset-delivery/integrate-native#install-time-delivery) to access these assets.
- `ASSET_PACK_STORAGE_FILES`: Use [`AssetPackLocation_getAssetsPath()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpacklocation_getassetspath) to get a file path to the directory containing the assets, or null if the assets have not been downloaded. Do not modify downloaded files in this file path.

```c
AssetPackLocation* location;

AssetPackErrorCode error_code = AssetPackManager_getAssetPackLocation(asset-pack-name, &location);

if (error_code == ASSET_PACK_NO_ERROR) {
    AssetPackStorageMethod storage_method = AssetPackLocation_getStorageMethod(location);
    const char* assets_path = AssetPackLocation_getAssetsPath(location);
    AssetPackLocation_destroy(location);
}
```

Once you locate the assets, use functions like `fopen` or `ifstream` to access
the files.
| **Note:** Do not rely on cached asset pack locations between app launches. The app should check for the existence of asset packs at every launch. Asset packs may become invalid due to app updates or if the user clears the app data.

## Other Play Core API methods

The following are some additional API methods you may want to use in your app.

### Cancel request

Use
[`AssetPackManager_cancelDownload()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_canceldownload)
to cancel an active asset pack request. Note that this request is a best-effort
operation.

### Request removal

Use
[`AssetPackManager_requestRemoval()`](https://developer.android.com/reference/native/play/core/group/assetpack#assetpackmanager_requestremoval)
to schedule the removal of an asset pack.

## Next steps

[Test Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery/test) locally and from
Google Play.