---
title: https://developer.android.com/google/play/integrity/native-setup
url: https://developer.android.com/google/play/integrity/native-setup
source: md.txt
---

This guide shows you how to set up your native Android project to use the Play
Integrity API from C or C++. Before you can make calls to the API, you must
first integrate the Play Core Native SDK by configuring your development
environment and updating your `build.gradle` and `CMakeLists.txt` files as shown
in the following section. For more details see our [Native API Reference](https://developer.android.com/reference/native/play/core/group/integrity).


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