---
title: Add C and C++ code to your project  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/projects/add-native-code
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Add C and C++ code to your project Stay organized with collections Save and categorize content based on your preferences.




Add C and C++ code to your Android project by placing the code into a
`cpp` directory in your project module. When you build your project, this
code is compiled into a native library that Gradle can package with your app.
Your Java or Kotlin code can then call functions in your native library
through the Java Native Interface (JNI). To learn more about using the JNI
framework, read [JNI tips for
Android](/training/articles/perf-jni).

Android Studio supports CMake, which is useful for cross-platform projects.
Android Studio also supports [`ndk-build`](/ndk/guides/ndk-build), which
can be faster than CMake but only supports Android. Using both CMake and
`ndk-build` in the same module is not currently supported.

To import an existing `ndk-build` library into your Android Studio
project, learn how to
[link Gradle to your native library project](/studio/projects/gradle-external-native-builds).

This page shows you how to [set up Android Studio](#download-ndk) with the
necessary build tools, [create a new project](#new-project) with C/C++
support, and [add new C/C++ files](#create-sources) to your project.

If instead you want to add native code to an existing project,
follow these steps:

1. [Create new native source files](#create-sources) and add the
   files to your Android Studio project.
   * Skip this step if you already have native code or want to
     import a prebuilt native library.
2. [Configure CMake](/studio/projects/configure-cmake) to
   build your native source code into a library. This build script is required
   if you are importing and linking against prebuilt or platform
   libraries.
   * If you have an existing native library that already has a
     `CMakeLists.txt` build script or uses `ndk-build` and includes
     an [`Android.mk`](/ndk/guides/android_mk)
     build script, skip this step.
3. [Configure
   Gradle](/studio/projects/gradle-external-native-builds) by providing a path to your CMake or `ndk-build`
   script file. Gradle uses the build script to import source code into your
   Android Studio project and package your native library into the app.

Once you configure your project, access your native functions from
Java or Kotlin code using the [JNI framework](http://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html). To build and run your app,
click **Run** ![run then run app from the menu bar](/static/studio/images/buttons/toolbar-run.png).

**Note:** If your existing project uses the deprecated
`ndkCompile` tool, migrate to using either CMake or
`ndk-build`.

## Download the NDK and build tools

To compile and debug native code for your app, you need the following
components:

* [The Android Native Development Kit
  (NDK)](/ndk): a toolset that lets you use C and C++ code with
  Android. NDK provides platform libraries that let you manage native
  activities and access physical device components, such as sensors and touch
  input.
* [CMake](https://cmake.org/): an
  external build tool that works alongside Gradle to build your native
  library. You don't need this component if you only plan to use
  `ndk-build`.
* [LLDB](http://lldb.llvm.org/): the
  debugger in Android Studio that [debugs native code](/studio/debug).

For information on installing these components, see [Install and configure the NDK and CMake](/studio/projects/install-ndk).

## Create a new project with C/C++ support

To create a new project with support for native code, the process is similar to
[creating any other Android
Studio project](/studio/projects/create-project), but with an additional step:

1. In the **Choose your project** section of the wizard,
   select the **Native C++** project type.
2. Click **Next**.
3. Complete all other fields in the next section of the wizard.
4. Click **Next**.
5. In the **Customize C++ Support** section of the wizard, you can customize
   your project with the **C++ Standard** field.
   * Use the drop-down list to
     select which standardization of C++ you want to use. Selecting **Toolchain
     Default** uses the default CMake setting.
6. Click **Finish**.

After Android Studio finishes creating your new project, open the
**Project** pane from the left side of the IDE and select the
**Android** view from the menu. As shown in figure 1, Android
Studio adds the **cpp** group:

![](/static/studio/images/projects/cpp-project-view_2-2_2x.png)

**Figure 1.** Android view groups for your native sources
and external build scripts.

**Note:** This view does not reflect the actual file hierarchy
on disk, but groups similar files to simplify navigating your project.

The **cpp** group is where you can find all the native
source files, headers, build scripts for CMake or `ndk-build`, and prebuilt
libraries that are a part of your project. For new projects, Android Studio
creates a sample C++ source file, `native-lib.cpp`, and places it
in the `src/main/cpp/` directory of your app module. This sample
code provides a simple C++ function, `stringFromJNI()`, that
returns the string `"Hello from C++"`. Learn how to add additional
source files to your project in the section about how to
[create new native source files](#create-sources).

Similar to how `build.gradle` files instruct Gradle how to build
your app, CMake and `ndk-build` require a build script to know how to build
your native library. For new projects, Android Studio creates a CMake build
script,`CMakeLists.txt`, and places it in your module’s root directory.
To learn more about the contents of this build script, read
[Configure CMake](/studio/projects/configure-cmake).

### Build and run the sample app

When you click **Run** ![run then run app from the menu bar](/static/studio/images/buttons/toolbar-run.png), Android Studio
builds and launches an app that displays the text "Hello from C++" on your
Android device or emulator. The following overview describes the events that
occur to build and run the sample app:

1. Gradle calls on your external build script,
   `CMakeLists.txt`.
2. CMake follows commands in the build script to compile a C++ source
   file, `native-lib.cpp`, into a shared object library and names
   it `libnative-lib.so`. Gradle then packages it into the app.
3. During runtime, the app's `MainActivity` loads the native
   library using [`System.loadLibrary()`](/reference/java/lang/System#loadLibrary(java.lang.String)). The library’s native function,
   `stringFromJNI()`, is now available to the app.
4. `MainActivity.onCreate()` calls `stringFromJNI()`,
   which returns `"Hello from C++"` and uses it to update the [`TextView`](/reference/android/widget/TextView).

To verify that Gradle packages the native library in the app, use the
[APK Analyzer](/studio/debug/apk-analyzer):

1. Select **Build > Build Bundles(s) / APK(s) > Build APK(s)**.
2. Select **Build > Analyze APK**.
3. Select the APK or AAB from the `app/build/outputs/` directory
   and click **OK**.
4. As shown in figure 2, you can see `libnative-lib.so` in the
   APK Analyzer window under `lib/<ABI>/`.
   ![](/static/studio/images/projects/cpplib-apk-analyzer_2-2_2x.png)

   **Figure 2.** Locate a native library using the APK
   Analyzer.

**Tip:** If you want to experiment with other Android apps that
use native code, click **File > New > Import Sample** and
select a sample project from the **Ndk** list.

## Create new C/C++ source files

To add new C/C++ source files to an existing project, proceed as follows:

1. If you don't already have a `cpp/` directory in the main source
   set of your app, create one as follows:

1. Open the **Project** pane in the left side of the IDE and
   select the **Project** view from the menu.
2. Navigate to **your-module > src**.
3. Right-click on the **main** directory and select **New >
   Directory**.
4. Enter `cpp` as the directory name and click **OK**.

- Right-click the `cpp/` directory and select **New >
  C/C++ Source File**.

- Enter a name for your source file, such as `native-lib`.

- From the **Type** menu, select the file extension
  for your source file, such as `.cpp`.
  * Click **Edit File Types**
    ![](/static/studio/images/buttons/dialog-wrench.png) to add other file types to the menu, such as
    `.cxx` or `.hxx`. In the **New File Extensions**
    dialog box that pops up, select another file extension from the
    **Source Extension** and **Header Extension** menus and
    click **OK**.

- To create a header file, select the **Create an
  associated header** checkbox.

- Click **OK**.

After you add new C/C++ files to you project, you still need to
[configure CMake](/studio/projects/configure-cmake) to include the files in
your native library.

## Additional resources

To learn more about supporting C/C++ code in your app, try the following
resource.

### Codelabs

* [Create Hello-CMake with Android Studio](https://codelabs.developers.google.com/codelabs/android-studio-cmake/)
  This codelab shows you how to use the Android Studio CMake template to start
  Android NDK project development.