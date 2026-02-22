---
title: https://developer.android.com/ndk/guides/hwasan
url: https://developer.android.com/ndk/guides/hwasan
source: md.txt
---

| **Note:** This document covers running Android applications built with the NDK under [HWAddress Sanitizer](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html). For information about using [HWAddress Sanitizer](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html) on Android platform components, see the [AOSP documentation](https://source.android.com/devices/tech/debug/hwasan.html).

The Android NDK supports [HWAddress Sanitizer](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html), also known as HWASan, beginning
with NDK r21 and Android 10 (API level 29). HWASan is only available on 64-bit
Arm devices.
| **Important:** HWAsan is one of many tools available for memory debugging and mitigation. See [Memory error debugging and mitigation](https://developer.android.com/ndk/guides/memory-debug) for an overview of all the tools.

HWASan is a memory error detection tool similar to ASan. Compared to classic
ASan, HWASan has:

- Similar CPU overhead (\~2x)
- Similar code size overhead (40 -- 50%)
- Much smaller RAM overhead (10% -- 35%)

HWASan detects the same set of bugs as ASan:

- Stack and heap buffer overflow or underflow
- Heap use after free
- Stack use outside scope
- Double free or wild free

Additionally, HWASan also detects:

- Stack use after return

## Sample App

A [sample app](https://github.com/android/ndk-samples/tree/main/sanitizers)
shows how to configure a [build variant](https://developer.android.com/studio/build/build-variants) for
hwasan.

## Build

| **Important:** Make sure you are using an up-to-date NDK to build your code.

To build your app's native (JNI) code with [HWAddress Sanitizer](https://clang.llvm.org/docs/HardwareAssistedAddressSanitizerDesign.html), do the
following:

### ndk-build

In your `Application.mk` file:

    APP_STL := c++_shared # Or system, or none, but not c++_static.
    APP_CFLAGS := -fsanitize=hwaddress -fno-omit-frame-pointer
    APP_LDFLAGS := -fsanitize=hwaddress

### CMake (Gradle Groovy)

In your module's `build.gradle` file:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    # Can also use system or none as ANDROID_STL, but not c++_static.
                    arguments "-DANDROID_STL=c++_shared"
                }
            }
        }
    }

For each target in your CMakeLists.txt:

    target_compile_options(${TARGET} PUBLIC -fsanitize=hwaddress -fno-omit-frame-pointer)
    target_link_options(${TARGET} PUBLIC -fsanitize=hwaddress)

With NDK 27 or newer, you can also use the following in your `build.gradle`
and don't have to change CMakeLists.txt:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    arguments "-DANDROID_SANITIZE=hwaddress"
                }
            }
        }
    }

This will not work when using `ANDROID_USE_LEGACY_TOOLCHAIN_FILE=false`.

### CMake (Gradle Kotlin)

In your module's `build.gradle` file:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    # Can also use system or none as ANDROID_STL, but not c++_static.
                    arguments += "-DANDROID_STL=c++_shared"
                }
            }
        }
    }

For each target in your CMakeLists.txt:

    target_compile_options(${TARGET} PUBLIC -fsanitize=hwaddress -fno-omit-frame-pointer)
    target_link_options(${TARGET} PUBLIC -fsanitize=hwaddress)

With NDK 27 or newer, you can also use the following in your `build.gradle`
and don't have to change CMakeLists.txt:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    arguments += "-DANDROID_SANITIZE=hwaddress"
                }
            }
        }
    }

This will not work when using `ANDROID_USE_LEGACY_TOOLCHAIN_FILE=false`.
| **Note:** A shared library STL is required because implementations of the operators `new` and `delete` in the STL are usually built without frame pointers. HWASan brings its own implementation, but it can't be used if the STL is linked statically into the application.

### Android 14 or newer: add wrap.sh

| **Important:** This is incompatible with using `android:useAppZygote` in AndroidManifest. Remove `android:useAppZygote` for testing with HWASan, or follow [Setup Instructions](https://developer.android.com/ndk/guides/hwasan#setup) if you need to keep it.

If you are running Android 14 or newer, you can use a
[wrap.sh script](https://developer.android.com/ndk/guides/wrap-script) to run your **debuggable** app on any
Android-powered device. You can skip this step if you chose to follow the steps
in the [Setup Instructions](https://developer.android.com/ndk/guides/hwasan#setup).

Follow the instructions to
[package a wrap.sh script](https://developer.android.com/ndk/guides/wrap-script#packaging_wrapsh) to add the
following wrap.sh script for `arm64-v8a`.

    #!/system/bin/sh
    LD_HWASAN=1 exec "$@"

## Run

If you're running on an Android version older than 14, or didn't add a wrap.sh
script, follow the [Setup Instructions](https://developer.android.com/ndk/guides/hwasan#setup) before running your app.

Run the app as usual. When a memory error is detected, an app crashes with
SIGABRT and prints a detailed message to logcat. A copy of the message can
be found in a file under `/data/tombstones` and looks like this:

    ERROR: HWAddressSanitizer: tag-mismatch on address 0x0042a0826510 at pc 0x007b24d90a0c
    WRITE of size 1 at 0x0042a0826510 tags: 32/3d (ptr/mem) in thread T0
        #0 0x7b24d90a08  (/data/app/com.example.hellohwasan-eRpO2UhYylZaW0P_E0z7vA==/lib/arm64/libnative-lib.so+0x2a08)
        #1 0x7b8f1e4ccc  (/apex/com.android.art/lib64/libart.so+0x198ccc)
        #2 0x7b8f1db364  (/apex/com.android.art/lib64/libart.so+0x18f364)
        #3 0x7b8f2ad8d4  (/apex/com.android.art/lib64/libart.so+0x2618d4)

    0x0042a0826510 is located 0 bytes to the right of 16-byte region [0x0042a0826500,0x0042a0826510)
    allocated here:
        #0 0x7b92a322bc  (/apex/com.android.runtime/lib64/bionic/libclang_rt.hwasan-aarch64-android.so+0x212bc)
        #1 0x7b24d909e0  (/data/app/com.example.hellohwasan-eRpO2UhYylZaW0P_E0z7vA==/lib/arm64/libnative-lib.so+0x29e0)
        #2 0x7b8f1e4ccc  (/apex/com.android.art/lib64/libart.so+0x198ccc)

The message may be followed by additional debugging information, including the
list of live threads in the application, tags of nearby memory allocations and
CPU register values.

See [Understanding HWASan reports](https://source.android.com/docs/security/memory-safety/hwasan-reports) for more information on HWASan error
messages.

## Building command-line executables

| **Important:** Make sure you are using the newest NDK. This will fail for NDK before r26b.

You can build and run executables instrumented with HWASan on Android 14 and
newer. You can use the same configuration as described in [Build](https://developer.android.com/ndk/guides/hwasan#build) for
ndk-build or CMake for your executables. Push the executables to a device
running Android 14 or newer and run it as normal using the shell.

If you are using libc++, make sure you are using the shared STL and push it to
the device and set `LD_LIBRARY_PATH` to the directory containing it when
running your binary.

If you aren't using Gradle, see the NDK documentation to learn how to build from
the command line with [CMake](https://developer.android.com/ndk/guides/cmake#usage) and
[ndk-build](https://developer.android.com/ndk/guides/ndk-build#ifc).

## Android 13 or earlier: Setup

If your device runs Android 14 or newer, you can skip this step and follow the
[instructions for using wrap.sh](https://developer.android.com/ndk/guides/hwasan#wrapsh) in the [Build](https://developer.android.com/ndk/guides/hwasan#build) section.
You can also choose to follow this section and skip the instructions for using
wrap.sh.

Before Android 14, HWASan applications need a HWASan build of Android to run.
You can flash prebuilt HWASan images to supported Pixel devices. The builds are
available on [ci.android.com](https://ci.android.com/builds/branches/git_aosp-main-with-phones-throttled/grid), where you can click the square for the
exact build you want to get a **Flash Build** link. This requires that you know
the [codename for your phone](https://source.android.com/setup/build/running).

![Flash a device build](https://developer.android.com/static/ndk/guides/images/select-build-ci.png)

It may be easier to instead go straight to [flash.android.com](https://flash.android.com) because there the
flow *starts* with detecting your device and only shows you builds you can use.
The following images illustrate the setup flow in this tool.

Enable developer mode on your device and connect it to your computer using
a USB cable. Click **Add new device** , select your device from the dialog, and
click **Connect**.

![Detect a device to flash](https://developer.android.com/static/ndk/guides/images/flash-tool-step1.png)
![Select the device to connect to](https://developer.android.com/static/ndk/guides/images/flash-tool-step2.png)

After your device is connected, click it to configure the build.
In the **Select a build ID** box, select the `aosp-master-with-phones-throttled`
branch to automatically choose the correct image for the device you have
connected.

![Select the device to flash](https://developer.android.com/static/ndk/guides/images/flash-tool-step3.png)
![Confirm flash options and flash the device](https://developer.android.com/static/ndk/guides/images/flash-tool-step4.png)

Click **Install** to flash your device.

There's more detail about the necessary set up in the
[Android Flash Tool documentation](https://source.android.com/setup/contribute/flash). Alternatively, you can check the
[AOSP documentation](https://source.android.com/devices/tech/debug/hwasan.html) for instructions for building a HWASan image from source.