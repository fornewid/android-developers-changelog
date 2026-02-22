---
title: https://developer.android.com/ndk/guides/concepts
url: https://developer.android.com/ndk/guides/concepts
source: md.txt
---

# Concepts

## Before you begin

This guide assumes that you are already familiar with concepts inherent in native programming and in[Android development](https://developer.android.com/develop).

## Introduction

This section provides a high-level explanation of how the NDK works. The Android NDK is a set of tools allowing you to embed C or C++ ("native code") into your Android apps. The ability to use native code in Android apps can be particularly useful to developers who wish to do one or more of the following:

- Port their apps between platforms.
- Reuse existing libraries, or provide their own libraries for reuse.
- Increase performance in certain cases, particularly computationally intensive ones like games.

## How it works

This section introduces the main components used in building a native application for Android, and goes on to describe the process of building and packaging.

### Main components

You should have an understanding of the following components as you build your app:

- Native shared libraries: The NDK builds these libraries, or`.so`files, from your C/C++ source code.

- Native static libraries: The NDK can also build static libraries, or`.a`files, which you can link into other libraries.

- Java Native Interface (JNI): The JNI is the interface via which the Java and C++ components talk to one another. This guide assumes knowledge of the JNI; for information about it, consult the[Java Native Interface Specification](http://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html).

- Application Binary Interface (ABI): The ABI defines exactly how your app's machine code is expected to interact with the system at runtime. The NDK builds`.so`files against these definitions. Different ABIs correspond to different architectures: The NDK includes ABI support for 32-bit ARM, AArch64, x86, and x86-64. For more information, see[Android ABIs](https://developer.android.com/ndk/guides/abis).

- Manifest: If you are writing an app with no Java component to it, you must declare the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class in the[manifest](https://developer.android.com/guide/topics/manifest/manifest-intro). See[Use the native_activity.h interface](https://developer.android.com/ndk/guides/concepts#na)for more detail on how to do this.

### Flow

The general flow for developing a native app for Android is as follows:

1. Design your app, deciding which parts to implement in Java, and which parts to implement as native code.

   | **Note:** While it is possible to completely avoid Java, you are likely to find the Android Java framework useful for tasks including controlling the display and UI.
2. Create an Android app Project as you would for any other Android project.

3. If you are writing a native-only app, declare the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class in`AndroidManifest.xml`. For more information, see the[Native activities and applications](https://developer.android.com/ndk/guides/concepts#naa).

4. Create an`Android.mk`file describing the native library, including name, flags, linked libraries, and source files to be compiled in the "JNI" directory.

5. Optionally, you can create an`Application.mk`file configuring the target ABIs, toolchain, release/debug mode, and STL. For any of these that you do not specify, the following default values are used, respectively:

   - ABI: all non-deprecated ABIs
   - Mode: Release
   - STL: system
6. Place your native source under the project's`jni`directory.

7. Use ndk-build to compile the native (`.so`,`.a`) libraries.

8. Build the Java component, producing the executable`.dex`file.

9. Package everything into an APK file, containing`.so`,`.dex`, and other files needed for your app to run.

## Native activities and applications

The Android SDK provides a helper class,[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity), that allows you to write a completely native activity.[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)handles the communication between the Android framework and your native code, so you do not have to subclass it or call its methods. All you need to do is declare your application to be native in your`AndroidManifest.xml`file, and begin creating your native application.

An Android application using[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)still runs in its own virtual machine, sandboxed from other applications. You can therefore still access Android framework APIs through the JNI. In certain cases, such as for sensors, input events, and assets, the NDK provides native interfaces that you can use instead of having to call across the JNI. For more information about such support, see[Native APIs](https://developer.android.com/ndk/guides/stable_apis).

Regardless of whether or not you are developing a native activity, we recommend that you create your projects with the traditional Android build tools. Doing so helps ensure building and packaging of Android applications with the correct structure.

The Android NDK provides you with two choices to implement your native activity:

- The[native_activity.h](https://developer.android.com/ndk/reference/native__activity_8h)header defines the native version of the[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity)class. It contains the callback interface and data structures that you need to create your native activity. Because the main thread of your application handles the callbacks, your callback implementations must not be blocking. If they block, you might receive ANR (Application Not Responding) errors because your main thread is unresponsive until the callback returns.
- The`android_native_app_glue.h`file defines a static helper library built on top of the[native_activity.h](https://developer.android.com/ndk/reference/native__activity_8h)interface. It spawns another thread, which handles things such as callbacks or input events in an event loop. Moving these events to a separate thread prevents any callbacks from blocking your main thread.

The`<ndk_root>/sources/android/native_app_glue/android_native_app_glue.c`source is also available, allowing you to modify the implementation.

For more information on how to use this static library, examine the native-activity sample application and its documentation. Further reading is also available in the comments in the`<ndk_root>/sources/android/native_app_glue/android_native_app_glue.h`file.

### Use the native_activity.h interface

To implement a native activity with the[native_activity.h](https://developer.android.com/ndk/reference/native__activity_8h)interface:

1. Create a`jni/`directory in your project's root directory. This directory stores all of your native code.

2. Declare your native activity in the`AndroidManifest.xml`file.

   Because your application has no Java code, set`android:hasCode`to`false`.  

       <application android:label="@string/app_name" android:hasCode="false">

   You must set the`android:name`attribute of the activity tag to[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity).  

       <activity android:name="android.app.NativeActivity"
                 android:label="@string/app_name">

   | **Note:** You can subclass[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity). If you do, use the name of the subclass instead of[NativeActivity](https://developer.android.com/reference/android/app/NativeActivity).

   The`android:value`attribute of the`meta-data`tag specifies the name of the shared library containing the entry point to the application (such as C/C++`main`), omitting the`lib`prefix and`.so`suffix from the library name.  

       <manifest>
         <application>
           <activity>
             <meta-data android:name="android.app.lib_name"
                        android:value="native-activity" />
             <intent-filter>
               <action android:name="android.intent.action.MAIN" />
               <category android:name="android.intent.category.LAUNCHER" />
             </intent-filter>
           </activity>
         </application>
       </manifest>

3. Create a file for your native activity, and implement the function named in the[ANativeActivity_onCreate](https://developer.android.com/ndk/reference/group___native_activity#ga02791d0d490839055169f39fdc905c5e)variable. The app calls this function when the native activity starts. This function, analogous to`main`in C/C++, receives a pointer to an[ANativeActivity](https://developer.android.com/ndk/reference/struct_a_native_activity)structure, which contains function pointers to the various callback implementations that you need to write. Set the applicable callback function pointers in`ANativeActivity->callbacks`to the implementations of your callbacks.

4. Set the`ANativeActivity->instance`field to the address of any instance of specific data that you want to use.

5. Implement anything else that you want your activity to do upon starting.

6. Implement the rest of the callbacks that you set in`ANativeActivity->callbacks`. For more information on when the callbacks are called, see[Managing the Activity Lifecycle](https://developer.android.com/training/basics/activity-lifecycle).

7. Develop the rest of your application.

8. Create an`Android.mk file`in the`jni/`directory of your project to describe your native module to the build system. For more information, see[Android.mk](https://developer.android.com/ndk/guides/android_mk).

9. Once you have an[Android.mk](https://developer.android.com/ndk/guides/android_mk)file, compile your native code using the`ndk-build`command.

       cd <path>/<to>/<project>
       $NDK/ndk-build

10. Build and install your Android project as usual. If your native code is in the`jni/`directory, the build script automatically packages the`.so`file(s) built from it into the APK.

## Additional sample code

To download NDK samples, see[NDK Samples](https://github.com/android/ndk-samples).