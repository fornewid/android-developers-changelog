---
title: https://developer.android.com/studio/projects/install-ndk
url: https://developer.android.com/studio/projects/install-ndk
source: md.txt
---

To compile and debug native code for your app, you need the following components:

- The Android Native Development Kit (NDK): a set of tools that allows you to use C and C++ code with Android.
- CMake: an external build tool that works alongside Gradle to build your native library. You do not need this component if you only plan to use ndk-build.
- LLDB: the debugger Android Studio uses to debug native code. By default, LLDB will be installed alongside Android Studio.

This page describes how to install these components automatically, or by using
Android Studio or the `sdkmanager` tool to download and install them manually.

## Install NDK and CMake automatically

Android Gradle Plugin 4.2.0+ can automatically install the required NDK and CMake
the first time you build your project if their licenses have been accepted in advance.
If you've already read and agree to the license terms, then you can pre-accept
the licenses in scripts with the following command:  

       yes | ${sdk}/cmdline-tools/latest/bin/sdkmanager --licenses

## Install the NDK and CMake

When you install the NDK, Android Studio selects the latest available NDK. For
most projects, installing this default version of the NDK is sufficient.
If your project needs one or more specific versions of the NDK, though, you can
[download and configure specific versions](https://developer.android.com/studio/projects/install-ndk#specific-version). Doing so helps
you ensure reproducible builds across projects that each depend on a specific
version of the NDK. Android Studio installs all versions of the NDK in the
<var translate="no">android-sdk</var>`/ndk/` directory.

To install CMake and the default NDK in Android Studio, do the following:

1. With a project open, click **Tools \> SDK Manager**.

2. Click the **SDK Tools** tab.

3. Select the **NDK (Side by side)** and **CMake** checkboxes.

   ![Image of SDK Manager](https://developer.android.com/static/studio/images/projects/install-NDK.png)
   **Figure 1.** The **SDK Tools** window showing the **NDK (Side by side)**
   option
   | **Note:** If you have an NDK installed in the `ndk-bundle` folder, it appears in the list with the label **NDK** . If you are using Android Gradle plugin 3.5.0 or later, you can select this checkbox or clear it. Clearing the checkbox uninstalls the NDK, freeing up disk space, and causes the checkbox to disappear from the list. If you uninstall the legacy NDK, remove the `ndk.dir` value, which is now deprecated, from your projects' `local.properties` files.
4. Click **OK**.

   A dialog box tells you how much space the NDK package consumes on disk.
5. Click **OK**.

6. When the installation is complete, click **Finish**.

7. Your project automatically syncs the build file and performs a build.
   Resolve any errors that occur.

### Configure a specific version of CMake

The SDK Manager includes the 3.6.0 forked version of
CMake and version 3.10.2. Projects that don't set a
specific CMake version are built with CMake 3.10.2. To
set the CMake version, add the following to your module's `build.gradle` file:  

### Groovy

```groovy
android {
    ...
    externalNativeBuild {
        cmake {
            ...
            version "<var translate="no">cmake-version</var>"
        }
    }
}
```

### Kotlin

```kotlin
android {
    ...
    externalNativeBuild {
        cmake {
            ...
            version = "<var translate="no">cmake-version</var>"
        }
    }
}
```

If you want to use a CMake version that is not included by the
SDK Manager, follow these steps:

1. Download and install [CMake](https://cmake.org/download/) from the official CMake website.
2. Specify the CMake version you want Gradle to use in your module's `build.gradle` file.
3. Either add the path to the CMake installation to your `PATH` environment
   variable or include it in your project's `local.properties` file, as
   shown. If Gradle is unable to find the version of CMake you specified in
   your `build.gradle` file, you get a build error.

       # If you set this property, Gradle no longer uses PATH to find CMake.
       cmake.dir = "<var translate="no">path-to-cmake</var>"</pre>

4. If you don't already have the Ninja build system installed on your
   workstation, go to the [official Ninja website](https://ninja-build.org/),
   and download and install the latest version of Ninja available for your OS.
   Make sure to also add the path to the Ninja installation to your
   `PATH` environment variable.

## Install a specific version of the NDK

To install a specific version of the NDK, do the following:

1. With a project open, click **Tools \> SDK Manager**.

2. Click the **SDK Tools** tab.

3. Select the **Show Package Details** checkbox.

4. Select the **NDK (Side by side)** checkbox and the checkboxes below it that
   correspond to the NDK versions you want to install. Android Studio installs
   all versions of the NDK in the <var translate="no">android-sdk</var>`/ndk/`
   directory.

   | **Note:** Preview releases (for example, canary and beta) of the NDK do not show up in this list unless you [change the update channel](https://developer.android.com/studio/preview/install-preview#change_your_update_channel) for Android Studio. You can [install an Android Studio preview](https://developer.android.com/studio/preview/install-preview) side-by-side with the stable version.

   ![Image of SDK Tools window](https://developer.android.com/static/studio/images/projects/install-NDK-sxs.png)
   **Figure 2.** The **SDK Tools** window showing the **NDK (Side by side)**
   options
   | **Note:** If you have an NDK installed in the `ndk-bundle` folder, it appears in the list with the label **NDK** . If you are using Gradle version 3.5 or later, you can select this checkbox or clear it. Clearing it uninstalls the NDK installed, freeing up disk space, and cause the checkbox to disappear from the list. If you uninstall the legacy NDK, remove the `ndk.dir` value, which is now deprecated, from your projects' `local.properties` files.
5. Click **OK**.

   A dialog box tells you how much space the NDK package(s) consumes.
6. Click **OK**.

7. When the installation is complete, click **Finish**.

8. Your project automatically syncs the build file and performs a build.
   Resolve any errors that occur.

9. [Configure each module](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) with the version of the NDK
   you want it to use. When using Android Studio 3.6 or higher, if you do not
   specify the version, the Android Gradle plugin chooses a version that it is
   known to be compatible with.

## Configure specific versions of the NDK in your project

You may need to configure the version of the NDK in your project if one of the
following is true:

- Your project is inherited and you need to use specific versions of the NDK and the Android Gradle plugin (AGP). For more information, see [Configure the NDK for the Android Gradle plugin](https://developer.android.com/studio/projects/configure-agp-ndk).
- You have multiple versions of the NDK installed and you want to use a specific
  one. In this case, specify the version using the `android.ndkVersion`
  property in the module's `build.gradle` file, as shown in the following code
  sample.

  ### Groovy

  ```groovy
  android {
      ndkVersion "<var translate="no">major</var>.<var translate="no">minor</var>.<var translate="no">build</var>" // e.g.,  ndkVersion "21.3.6528147"
  }
  ```

  ### Kotlin

  ```kotlin
  android {
      ndkVersion = "<var translate="no">major</var>.<var translate="no">minor</var>.<var translate="no">build</var>" // e.g.,  ndkVersion "21.3.6528147"
  }
  ```

### Default NDK version per AGP version

Before release, each AGP version is thoroughly tested with the latest stable NDK
release at that time. This NDK version is used to build your projects if you
don't specify an NDK version in the `build.gradle` file. The default NDK version
for different versions of AGP are documented in the
[AGP release notes](https://developer.android.com/build/releases/gradle-plugin#compatibility) and
[AGP past release notes](https://developer.android.com/build/releases/past-releases).