---
title: https://developer.android.com/ndk/guides/asan
url: https://developer.android.com/ndk/guides/asan
source: md.txt
---

| **Note:** This document covers running Android applications built with the NDK under [Address Sanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer). For information about using [Address Sanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) on Android platform components, see the [AOSP documentation](https://source.android.com/devices/tech/debug/asan.html).
| **Deprecated:** As of 2023, ASan is unsupported. It is recommended to use [HWASan](https://developer.android.com/ndk/guides/hwasan) instead. HWASan can be used on ARM64 devices running Android 14 (API level 34) or newer; or on Pixel devices running Android 10 (API level 29) by flashing a [special system image](https://developer.android.com/ndk/guides/hwasan#setup). ASan may still be used but might have bugs.
| **Important:** Asan is one of many tools available for memory debugging and mitigation. See [Memory error debugging and mitigation](https://developer.android.com/ndk/guides/memory-debug) for an overview of all the tools.

The Android NDK supports [Address Sanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) (also known as ASan) beginning
with API level 27 (Android O MR 1).

ASan is a fast compiler-based tool for detecting memory bugs in native code.
ASan detects:

- Stack and heap buffer overflow/underflow
- Heap use after free
- Stack use outside scope
- Double free/wild free

ASan's CPU overhead is roughly 2x, code size overhead is between 50% and 2x,
and the memory overhead is large (dependent on your allocation patterns, but on
the order of 2x).

## Sample App

A [sample app](https://github.com/android/ndk-samples/tree/main/sanitizers)
shows how to configure a [build variant](https://developer.android.com/studio/build/build-variants) for asan.

## Build

To build your app's native (JNI) code with [Address Sanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer), do the
following:

### ndk-build

In your Application.mk:

    APP_STL := c++_shared # Or system, or none.
    APP_CFLAGS := -fsanitize=address -fno-omit-frame-pointer
    APP_LDFLAGS := -fsanitize=address

For each module in your Android.mk:

    LOCAL_ARM_MODE := arm

### CMake

In your module's build.gradle:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    // Can also use system or none as ANDROID_STL.
                    arguments "-DANDROID_ARM_MODE=arm", "-DANDROID_STL=c++_shared"
                }
            }
        }
    }

For each target in your CMakeLists.txt:

    target_compile_options(${TARGET} PUBLIC -fsanitize=address -fno-omit-frame-pointer)
    set_target_properties(${TARGET} PROPERTIES LINK_FLAGS -fsanitize=address)

| **Caution:** ASan is currently incompatible with C++ exception handling when using `libc++_static`. Apps using `libc++_shared` or not using exception handling are either unaffected or have workarounds available. See [Issue 988](https://github.com/android-ndk/ndk/issues/988) for more details.

## Run

Beginning with Android O MR1 (API level 27) an application can provide a
[wrap shell script](https://developer.android.com/ndk/guides/wrap-script) that can wrap or replace the application process. This allows
a debuggable application to customize their application startup, which enables
using ASan on production devices.
| **Note:** The following instructions describe how to use ASan with an Android Studio project. For a non-Android Studio project, refer to the [wrap shell script](https://developer.android.com/ndk/guides/wrap-script) documentation.

1. Add `android:debuggable` to the application manifest.
2. Set [`useLegacyPackaging`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/JniLibsPackagingOptions#uselegacypackaging) to `true` in your app's `build.gradle` file. See the [wrap shell script](https://developer.android.com/ndk/guides/wrap-script) guide for more information.
3. Add the ASan runtime library to your app module's `jniLibs`.
4. Add `wrap.sh` files with the following contents to each directory in your
   `src/main/resources/lib` directory.

       #!/system/bin/sh
       HERE="$(cd "$(dirname "$0")" && pwd)"
       export ASAN_OPTIONS=log_to_syslog=false,allow_user_segv_handler=1
       ASAN_LIB=$(ls $HERE/libclang_rt.asan-*-android.so)
       if [ -f "$HERE/libc++_shared.so" ]; then
           # Workaround for https://github.com/android-ndk/ndk/issues/988.
           export LD_PRELOAD="$ASAN_LIB $HERE/libc++_shared.so"
       else
           export LD_PRELOAD="$ASAN_LIB"
       fi
       "$@"

| **Note:** The NDK contains a recommended wrap.sh file for ASan [here](https://android.googlesource.com/platform/ndk/+/refs/heads/master/wrap.sh/asan.sh).

Assuming your project's application module is named `app`, your final directory
structure should include the following:

    <project root>
    └── app
        └── src
            └── main
                ├── jniLibs
                │   ├── arm64-v8a
                │   │   └── libclang_rt.asan-aarch64-android.so
                │   ├── armeabi-v7a
                │   │   └── libclang_rt.asan-arm-android.so
                │   ├── x86
                │   │   └── libclang_rt.asan-i686-android.so
                │   └── x86_64
                │       └── libclang_rt.asan-x86_64-android.so
                └── resources
                    └── lib
                        ├── arm64-v8a
                        │   └── wrap.sh
                        ├── armeabi-v7a
                        │   └── wrap.sh
                        ├── x86
                        │   └── wrap.sh
                        └── x86_64
                            └── wrap.sh

## Stack traces

[Address Sanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) needs to unwind the stack on every `malloc`/`realloc`/`free`
call. There are two options here:

1. A "fast" frame pointer-based unwinder. This is what is used by following the
   instructions in the [building section](https://developer.android.com/ndk/guides/asan#building).

2. A "slow" CFI unwinder. In this mode ASan uses `_Unwind_Backtrace`. It
   requires only `-funwind-tables`, which is normally enabled by default.

   | **Caution:** the "slow" unwinder is **slow** (10x or more, depending on how often you call `malloc`/`free`).

The fast unwinder is the default for malloc/realloc/free. The slow unwinder is
the default for fatal stack traces. The slow unwinder can be enabled for all
stack traces by adding `fast_unwind_on_malloc=0` to the `ASAN_OPTIONS` variable
in your wrap.sh.