---
title: https://developer.android.com/games/agde/adapt-existing-project
url: https://developer.android.com/games/agde/adapt-existing-project
source: md.txt
---

Configure a project to use the Android Game Development Extension.

The Android Game Development Extension invokes MSBuild to build C/C++ source code into shared
libraries (`.so`) and static libraries (`.a`). As part of the build process, a
custom MSBuild task invokes Gradle to compile Java and Kotlin source code,
package assets, and generate an APK file for deployment. When you configure your
project, you must ensure that MSBuild has the information it needs to build for
the Android platform.

## Build C/C++ with MSBuild

A typical Android project is built with Gradle, where the native code inside the
project is built by a Gradle pass that runs either [CMake](https://developer.android.com/ndk/guides/cmake) or
[ndk-build](https://developer.android.com/ndk/guides/ndk-build). With the Android Game Development Extension for Visual
Studio, the build process is inverted. Now MSBuild is the starting point of the
build process. All C/C++ source code is built first by MSBuild for the new
Android platforms installed on your system as part of the extension (for
example, "Android-x86_64"). MSBuild then invokes Gradle to package the shared
library files that contain your C/C++ logic into an APK.

You should first replicate your project's existing build logic in CMake or
ndk-build in MSBuild. Set the target platforms to the following:

- Android-x86
- Android-x86_64
- Android-armeabi-v7a
- Android-arm64-v8a

These platforms are all provided by the Android Game Development Extension.

### Set your compile and link options

AGDE uses the NDK you select to determine the default compile and link options
when building the C/C++ part of your app.

If you need to customize these compile or link options, you can set them using
Project Properties. You can find the most common options in the C/C++
(for compilation), Librarian (for static library archiving) and Linker (for
dynamic library linking) groups. If you need to pass any other custom
options, you can add them to the Command Line section. For example,
if you are using an NDK older than r28, you might want to set the linker flag
to make your app [support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes#compile-16-kb-alignment).

### Add an Android Platform

While the teapot sample project includes Android platforms, you must manually
add an Android platform to an existing project. To add a new platform, do the
following in Visual Studio:

1. Select **Build \> Configuration Manager**.
2. Under **Active solution platform** , select **\<New\>**.
3. Type one of the following for the new platform:

   - **Android-armeabi-v7a**
   - **Android-arm64-v8a**
   - **Android-x86**
   - **Android-x86_64**
4. In the **Copy settings from** box, select another existing Android
   platform, or **\<Empty\>** if you do not have any Android platforms yet.
   Make sure you enabled **Create new project platforms**.

### Add an Android APK item

Select **Add \> New Item \> Visual C++ \> Android \> Android APK** and click
**Add**. Configure the Android application on the following dialog.

- **Application Name**: The human-readable name of your Android application.
- **Application ID** : The [unique identifier](https://developer.android.com/studio/build/configure-app-module#set_the_application_id) for your Android application.
- **Solution Explorer Location** : Location of the virtual folder that contains the added Android packaging support files. By default, these files are also located in the project in a folder with the same name. You can customize the location by selecting the **Put support files in a custom location** checkbox and specifying a custom location. The virtual folder will still be under the current project in the Solution Explorer.

## Make MSBuild invoke Gradle to build an APK

MSBuild cannot invoke Gradle unless it knows the location of the Gradle project.
Set this location using the **Gradle Build Directory** property, as
shown in figure 1.

![](https://developer.android.com/static/images/agde/property-build-directory.png)  

**Figure 1** . **Gradle Build Directory** property

In addition, set the **Application Module** , **Application Variant** , and **APK
Name** properties (as shown in the previous image) in order for MSBuild to know
what to build.

- **Application Module** : The name of the Gradle subproject. This is the main project set in the `settings.gradle` file. It is usually called `app` for projects directly created using Android Studio.
- **Application Variant** : The Android variant to build. This value should be set according to the MSBuild configurations. For example, a debug build should have a value set to the debug variant. If your project's MSBuild configuration name matches the Gradle variant names, then just use the default value of `$(Configuration)`.
- **APK Name** : The name of the generated APK file used for debugging and profiling on your development computer. This name is passed to Gradle and your Gradle build script should respect this (see the property `MSBUILD_ANDROID_OUTPUT_APK_NAME` in the following section).

### Modify your Gradle build scripts

During the build, MSBuild passes the following information as project properties
to the Gradle script. Change your project's existing build scripts (typically
named `build.gradle`) to read these properties.

- `MSBUILD_MIN_SDK_VERSION`: The minimum SDK version for building the APK, as a
  string. Set this value in the **Minimum Android SDK Version** box on the
  project property page shown in figure 2.

  ![](https://developer.android.com/static/images/agde/property-min-sdk-version.png)  

  **Figure 2** . **Minimum Android SDK Version** property

  The Gradle build script should set `minSdkVersion` or `minSdk` to this
  string value, with a `toInteger()` type conversion when necessary.

  ### Groovy

  ```groovy
  android {
    // ...

    defaultConfig {
        applicationId "com.yourcompany.yourapp"
        minSdkVersion MSBUILD_MIN_SDK_VERSION
        // Or: minSdk MSBUILD_MIN_SDK_VERSION.toInteger()
        // ...
    }

    // ...
  }
  ```

  ### Kotlin

  ```kotlin
  android {
    // ...

    defaultConfig {
        applicationId = "com.yourcompany.yourapp"
        minSdkVersion(MSBUILD_MIN_SDK_VERSION)
        // Or: minSdk = MSBUILD_MIN_SDK_VERSION.toInteger()
        // ...
    }

    // ...
  }
  ```
- `MSBUILD_ANDROID_OUTPUT_APK_NAME`: The expected name of the APK that Gradle
  builds. The Android Game Development Extension will look for an APK matching this name and
  then deploy it to connected devices (for debugging and profiling). Set this
  value in the **APK Name** box on the project property page shown in figure 3.

  ![](https://developer.android.com/static/images/agde/property-apk-name.png)  

  **Figure 3** . **APK Name** property

  The Gradle build script must respect this property. For example, the
  following example sets the output APK name for all variants to the name
  chosen by MSBuild.

  ### Groovy

  ```groovy
  android {
    // ...

    applicationVariants.all { variant ->
        variant.outputs.all {
            outputFileName = MSBUILD_ANDROID_OUTPUT_APK_NAME
        }
    }

    // ...
  }
  ```

  ### Kotlin

  ```kotlin
  android {
    // ...

    applicationVariants.all { variant ->
        variant.outputs.all {
            outputFileName = MSBUILD_ANDROID_OUTPUT_APK_NAME
        }
    }

    // ...
  }
  ```
- `MSBUILD_JNI_LIBS_SRC_DIR`: The directory containing the shared libraries
  (`.so` files) built by MSBuild. Set this value in the **Output Directory**
  box on the project property page shown below. By default, this value is the
  output directory property for the Visual Studio project, as shown in figure 4.

  ![](https://developer.android.com/static/images/agde/property-output-directory.png)  

  **Figure 4** . **Output Directory** property

  Gradle should package the shared library files in this folder inside the APK
  in order for the Android application to load them at runtime.

  ### Groovy

  ```groovy
  android {
    // ...

    sourceSets {
        main {
            jniLibs.srcDirs += [MSBUILD_JNI_LIBS_SRC_DIR]
        }
    }

    // ...
  }
  ```

  ### Kotlin

  ```kotlin
  android {
    // ...

    sourceSets.getByName("main") {
        jniLibs.srcDir(MSBUILD_JNI_LIBS_SRC_DIR)
    }

    // ...
  }
  ```

  In addition, since any C/C++ code is now built by MSBuild, remove the
  `externalNativeBuild` sections in your Gradle build scripts. These sections
  were used to invoke CMake or ndk-build to compile your C/C++ code, but are
  no longer needed.
- `MSBUILD_NDK_VERSION`: The version of the NDK to use to build your
  project. Set this value in the **Android NDK Version** box on the
  project property page shown in figure 5.

  ![](https://developer.android.com/static/images/agde/property-ndk-version.png)  

  **Figure 5** . **Android NDK Version** property

  The Gradle build script should set `ndkVersion` to this value, as shown:

  ### Groovy

  ```groovy
  android {
    // ...

    ndkVersion MSBUILD_NDK_VERSION

    // ...
  }
  ```

  ### Kotlin

  ```kotlin
  android {
    // ...

    ndkVersion = MSBUILD_NDK_VERSION

    // ...
  }
  ```

  For more information, see the Android Studio topic
  [Install and configure the NDK and CMake](https://developer.android.com/studio/projects/install-ndk).