---
title: https://developer.android.com/ndk/guides/cpu-arm-neon
url: https://developer.android.com/ndk/guides/cpu-arm-neon
source: md.txt
---

The NDK supports ARM Advanced SIMD, commonly known as Neon, an optional
instruction set extension for ARMv7 and ARMv8. Neon provides scalar/vector
instructions and registers (shared with the FPU) comparable to MMX/SSE/3DNow!
in the x86 world.

All ARMv8-based ("arm64") Android devices support Neon. Almost all ARMv7-based
("32-bit") Android devices support Neon, including all devices that shipped with
API level 21 or later. The NDK enables Neon by default for both Arm ABIs.

If you target very old devices, you can filter out incompatible devices on the
Google Play Console. You can also use the console for your app to see how many
devices this would affect.

Alternatively, for maximum compatibility, 32-bit code can perform runtime
detection to confirm that Neon code can be run on the target device. An app can
perform this check using any of the options mentioned in
[CPU features](https://developer.android.com/ndk/guides/cpu-features).

You should not write explicit Neon intrinsics in your C/C++ code. Clang's
[portable vector types](https://clang.llvm.org/docs/LanguageExtensions.html#vectors-and-extended-vectors) will automatically use Neon instructions. Clang's Neon
intrinsics are actually just a non-portable wrapper around the portable types,
so writing Neon intrinsics will not make your code any faster than using the
portable types, just less portable.

## Build

| **Note:** For NDK r21 and newer Neon is enabled by default for all API levels. If you need to disable Neon to support non-Neon devices (which are rare), invert the settings described below. Alternatively, the Play Store console can be used to [exclude CPUs](https://support.google.com/googleplay/android-developer/answer/7353455) that do not support Neon to prevent your application from being installed on those devices.

## Disable Neon globally

### ndk-build

ndk-build does not support disabling Neon globally. To disable Neon an entire
ndk-build application, apply the per-module steps to every module in your
application.

### CMake

Pass `-DANDROID_ARM_NEON=ON` when invoking CMake. If building with Android
Studio/Gradle, set the following option in your build.gradle:

    android {
        defaultConfig {
            externalNativeBuild {
                cmake {
                    arguments "-DANDROID_ARM_NEON=OFF"
                }
            }
        }
    }

## Disable Neon per module

### ndk-build

To build all the source files in an ndk-build module without Neon, add the
following to the module definition in your Android.mk:

    LOCAL_ARM_NEON := false

### CMake

To build all the source files in a CMake target without Neon, add the
following to your CMakeLists.txt:

    if(ANDROID_ABI STREQUAL armeabi-v7a)
        set_target_properties(${TARGET} PROPERTIES COMPILE_FLAGS -mfpu=vfpv3-d16)
    endif()

Where `${TARGET}` is replaced with the name of your library.

## Cross-platform support for x86


NDK supports cross-platform compilation of your existing ARM SIMD (Neon)
instrinsic functions into x86 SSE code, through the use of the third-party
[NEON_2_SSE.h](https://github.com/intel/ARM_NEON_2_x86_SSE).
For more information on this topic, see
[From ARM NEON to Intel SSE-the automatic porting solution, tips and tricks](http://software.intel.com/en-us/blogs/2012/12/12/from-arm-neon-to-intel-mmxsse-automatic-porting-solution-tips-and-tricks).

## Sample code

The [vectorization sample](https://github.com/android/ndk-samples/tree/main/vectorization) demonstrates how to use a variety of vectorization
tools to implement a matrix multiply, and compares their performance.