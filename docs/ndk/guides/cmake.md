---
title: https://developer.android.com/ndk/guides/cmake
url: https://developer.android.com/ndk/guides/cmake
source: md.txt
---

The Android NDK supports using [CMake](https://cmake.org/) to
compile C and C++ code for your application. This page discusses how to use
CMake with the NDK via the Android Gradle Plugin's `ExternalNativeBuild` or when
invoking CMake directly.
| **Note:** If you are using Android Studio, go to [Add C and C++ code to your
| project](https://developer.android.com/studio/projects/add-native-code) to learn the basics of adding native sources to your project, creating a CMake build script, adding your CMake project as a Gradle dependency, and using newer versions of CMake than those included in the SDK.

## The CMake toolchain file

The NDK supports CMake via a [toolchain file](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html). Toolchain files are CMake files
that customize the behavior of the toolchain for cross-compiling. The toolchain
file used for the NDK is located in the NDK at
`<NDK>/build/cmake/android.toolchain.cmake`.
| **Note:** If the Android SDK is installed, then the NDK is installed in the SDK directory in `ndk/version/` or `ndk-bundle/`.

Build parameters such as ABI, `minSdkVersion`, etc. are given on the command
line when invoking `cmake`. For a list of supported arguments, see the
[Toolchain arguments](https://developer.android.com/ndk/guides/cmake#variables) section.
| **Caution:** CMake has its [own built-in NDK support](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html#cross-compiling-for-android) which has behavior differences compared to the NDK's CMake toolchain file. Android does not support or test the built-in workflow. We recommend using our toolchain file. `externalNativeBuild` (the NDK workflow that's a part of the Android Gradle Plugin) users will get this automatically. If you're not using `externalNativeBuild`, see below for instructions on using our toolchain file directly.

### The "new" toolchain file

| **Warning:** We do not recommend using `-DANDROID_USE_LEGACY_TOOLCHAIN_FILE=OFF`. The legacy toolchain is the default, and despite the name, is what we recommend.

Earlier NDKs experimented with a new implementation of the toolchain file that
would reduce behavior differences between using the NDK's toolchain file and
using the built-in CMake support. This ended up requiring a significant amount
of work (which has not been completed), but did not actually improve behavior,
so we're no longer pursuing this.

The "new" toolchain file has behavior regressions compared to the "legacy"
toolchain file. **The default behavior is the recommended workflow.** If you're
using `-DANDROID_USE_LEGACY_TOOLCHAIN_FILE=OFF`, we recommend removing that flag
from your build. The new toolchain file never reached parity with the legacy
toolchain file, so there are likely behavior regressions.

Though we recommend against using the new toolchain file, there are currently no
plans to remove it from the NDK. Doing so would break builds that rely on the
behavior differences between the new and legacy toolchain files, and
unfortunately renaming the option to make it clear that "legacy" is actually
recommended would also break users of that option. If you're happily using the
new toolchain file you do not need to migrate, but know that any bugs filed
against new toolchain file behavior will probably not be fixed, and instead
you'll need to migrate.

## Usage

### Gradle

Use of the CMake toolchain file is automatic when using
`externalNativeBuild`. See Android Studio's [Add C and C++ code to your
project](https://developer.android.com/studio/projects/add-native-code) guide for more information.

### Command Line

When building with CMake outside of Gradle, the toolchain file itself and
its arguments must be passed to CMake. For example:

    $ cmake \
        -DCMAKE_TOOLCHAIN_FILE=$NDK/build/cmake/android.toolchain.cmake \
        -DANDROID_ABI=$ABI \
        -DANDROID_PLATFORM=android-$MINSDKVERSION \
        $OTHER_ARGS

## Toolchain arguments

The following arguments can be passed to the CMake toolchain file. If building
with Gradle, add arguments to
`android.defaultConfig.externalNativeBuild.cmake.arguments` as described in the
[ExternalNativeBuild docs](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/ExternalNativeBuildOptions). If building from the command line, pass arguments to
CMake with `-D`. For example, to force armeabi-v7a to not build with Neon
support, pass `-DANDROID_ARM_NEON=FALSE`.
| **Note:** Any required arguments are passed automatically by Gradle and need only be passed explicitly if building from the command line.

### `ANDROID_ABI`

| **Note:** This is a required argument.

The target ABI. For information on supported ABIs, see [Android ABIs](https://developer.android.com/ndk/guides/abis).

### Gradle

Gradle provides this argument automatically. Do not explicitly set this
argument in your `build.gradle` file. To control what ABIs Gradle targets,
use `abiFilters` as described in [Android ABIs](https://developer.android.com/ndk/guides/abis).

### Command Line

CMake builds for a single target per build. To target more than one Android
ABI, you must build once per ABI. It is recommended to use different build
directories for each ABI to avoid collisions between builds.

| Value | Notes |
|---|---|
| `armeabi-v7a` |   |
| `armeabi-v7a with NEON` | Same as `armeabi-v7a`. |
| `arm64-v8a` |   |
| `x86` |   |
| `x86_64` |   |

### `ANDROID_ARM_MODE`

Specifies whether to generate arm or thumb instructions for armeabi-v7a. Has no
effect for other ABIs. For more information, see the [Android ABIs](https://developer.android.com/ndk/guides/abis)
documentation.

| Value | Notes |
|---|---|
| arm |   |
| thumb | Default behavior. |

### `ANDROID_NATIVE_API_LEVEL`

Alias for [ANDROID_PLATFORM](https://developer.android.com/ndk/guides/cmake#android_platform).

### `ANDROID_PLATFORM`

Specifies the minimum API level supported by the application or library. This
value corresponds to the application's `minSdkVersion`.

### Gradle

When using the Android Gradle Plugin, this value is automatically set to
match the application's `minSdkVersion` and should not be set manually.

### Command Line

When invoking CMake directly, this value defaults to the lowest API level
supported by the NDK in use. For example, with NDK r20 this value defaults
to API level 16.
| **Warning:** NDK libraries cannot be run on devices with an API level below the `ANDROID_PLATFORM` value with which the code was built.

Multiple formats are accepted for this parameter:

- `android-$API_LEVEL`
- `$API_LEVEL`
- `android-$API_LETTER`

The `$API_LETTER` format allows you to specify `android-N` without the need to
determine the number associated with that release. Note that some releases
received an API increase without a letter increase. These APIs can be specified
by appending the `-MR1` suffix. For example, API level 25 is `android-N-MR1`.

### `ANDROID_STL`

Specifies which STL to use for this application. For more information, see [C++
library support](https://developer.android.com/ndk/guides/cpp-support). By default, `c++_static` will be used.
| **Caution:** The default behavior is not appropriate for all applications. Be sure to read the [C++ library support](https://developer.android.com/ndk/guides/cpp-support) guide and in particular the section about [static runtimes](https://developer.android.com/ndk/guides/cpp-support#static_runtimes) before choosing an STL.

| Value | Notes |
|---|---|
| c++_shared | The shared library variant of [libc++](https://developer.android.com/ndk/guides/cpp-support#libc). |
| c++_static | The static library variant of [libc++](https://developer.android.com/ndk/guides/cpp-support#libc). |
| none | No C++ standard library support. |
| system | The [system STL](https://developer.android.com/ndk/guides/cpp-support#system) |

## Manage compiler flags

If you need to pass specific flags to the compiler or linker for your build,
refer to the CMake documentation for [set_target_compile_options](https://cmake.org/cmake/help/latest/command/target_compile_options.html) and the
related family of options. The "see also" section at the bottom of that page has
some helpful clues.
| **Caution:** When using the global compiler flag variables in CMake, such as `CMAKE_CXX_FLAGS`, you need to be aware that CMake has per build-type (`CMAKE_BUILD_TYPE`) variants of those variables and use the appropriate one. The build-type-specific form of the variable (e.g. `CMAKE_CXX_FLAGS_RELEASE`) typically overrides similar flags that appear in the generic form. A common mistake is to add optimization flags (e.g. `-O3`) to `CMAKE_CXX_FLAGS`. This will have no effect, because the default optimization flags in `CMAKE_CXX_FLAGS_RELEASE` will override the flag in `CMAKE_CXX_FLAGS`.

In general, the best practice is to apply compiler flags as the narrowest
available scope. Flags that you want to apply to all of your targets (such as
`-Werror`) are inconvenient to repeat per-module, but still should rarely be
applied globally (`CMAKE_CXX_FLAGS`), as those may have undesired effects on
third-party dependencies in your project. For such cases, the flags can be
applied at directory-scope (`add_compile_options`).

For a narrow subset of compiler flags, they can also be set in your build.gradle
file using `cppFlags` or similar properties. **You should not do this.** Flags
passed to CMake from Gradle will have surprising precedence behaviors, in some
cases overriding flags passed implicitly by the implementation which are
required for building Android code. Always prefer handling CMake behavior
directly in CMake. If you need to control compiler flags per AGP `buildType`,
see [Work with AGP build types in CMake](https://developer.android.com/ndk/guides/cmake#agp-build-types).

## Work with AGP build types in CMake

If you need to tailor CMake behavior to a custom Gradle `buildType`, use that
build type to pass an additional CMake flag (not a compiler flag) that your
CMake build scripts can read. For example, if you have "free" and "premium"
build variants that are controlled by your build.gradle.kts and you need to pass
that data to CMake:

    android {
        buildTypes {
            free {
                externalNativeBuild {
                    cmake {
                        arguments.add("-DPRODUCT_VARIANT_PREMIUM=OFF")
                    }
                }
            }
            premium {
                externalNativeBuild {
                    cmake {
                        arguments.add("-DPRODUCT_VARIANT_PREMIUM=ON")
                    }
                }
            }
        }
    }

Then, in your CMakeLists.txt:

    if (DPRODUCT_VARIANT_PREMIUM)
      # Do stuff for the premium build.
    else()
      # Do stuff for the free build.
    endif()

The name of the variable is up to you, but make sure you avoid anything with an
`ANDROID_`, `APP_`, or `CMAKE_` prefix to avoid collision or confusion with
existing flags.

See the [Sanitizers NDK sample](https://github.com/android/ndk-samples/tree/main/sanitizers) for an example.

## Understand the CMake build command

When debugging CMake build issues, it's helpful to know the specific build
arguments that Gradle uses when cross-compiling for Android.

The Android Gradle Plugin saves the build arguments it uses for executing a
CMake build for each ABI and [build type](https://developer.android.com/studio/build/build-variants)
pair to the `build_command.txt`. These files are found in the following
directory:

    <project-root>/<module-root>/.cxx/cmake/<build-type>/<ABI>/

The following snippet shows an example of the CMake arguments to build a
debuggable release of the [`hello-jni`](https://github.com/android/ndk-samples/tree/main/hello-jni) sample targeting the `armeabi-v7a`
architecture.

                        Executable : ${HOME}/Android/Sdk/cmake/3.10.2.4988404/bin/cmake
    arguments :
    -H${HOME}/Dev/github-projects/googlesamples/ndk-samples/hello-jni/app/src/main/cpp
    -DCMAKE_FIND_ROOT_PATH=${HOME}/Dev/github-projects/googlesamples/ndk-samples/hello-jni/app/.cxx/cmake/universalDebug/prefab/armeabi-v7a/prefab
    -DCMAKE_BUILD_TYPE=Debug
    -DCMAKE_TOOLCHAIN_FILE=${HOME}/Android/Sdk/ndk/22.1.7171670/build/cmake/android.toolchain.cmake
    -DANDROID_ABI=armeabi-v7a
    -DANDROID_NDK=${HOME}/Android/Sdk/ndk/22.1.7171670
    -DANDROID_PLATFORM=android-23
    -DCMAKE_ANDROID_ARCH_ABI=armeabi-v7a
    -DCMAKE_ANDROID_NDK=${HOME}/Android/Sdk/ndk/22.1.7171670
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    -DCMAKE_LIBRARY_OUTPUT_DIRECTORY=${HOME}/Dev/github-projects/googlesamples/ndk-samples/hello-jni/app/build/intermediates/cmake/universalDebug/obj/armeabi-v7a
    -DCMAKE_RUNTIME_OUTPUT_DIRECTORY=${HOME}/Dev/github-projects/googlesamples/ndk-samples/hello-jni/app/build/intermediates/cmake/universalDebug/obj/armeabi-v7a
    -DCMAKE_MAKE_PROGRAM=${HOME}/Android/Sdk/cmake/3.10.2.4988404/bin/ninja
    -DCMAKE_SYSTEM_NAME=Android
    -DCMAKE_SYSTEM_VERSION=23
    -B${HOME}/Dev/github-projects/googlesamples/ndk-samples/hello-jni/app/.cxx/cmake/universalDebug/armeabi-v7a
    -GNinja
    jvmArgs :


                        Build command args: []
                        Version: 1

## Use prebuilt libraries

If the prebuilt library you need to import is distributed as an AAR, follow
[Studio's dependency docs](https://developer.android.com/studio/build/dependencies#native-dependencies-with-agp)
to import and use those. If you are not using AGP you can follow
https://google.github.io/prefab/example-workflow.html, but it is likely much
easier to migrate to AGP.

For libraries that are not distributed as an AAR, instructions on using prebuilt
libraries with CMake, see the `add_library` documentation regarding `IMPORTED`
targets in the [CMake manual](https://cmake.org/cmake/help/latest/command/add_library.html).

## Building third-party code

There are a handful of ways to build third-party code as part of your CMake
project, and which option works best will depend on your situation. The best
option will often be to not do this at all. Instead, [build an AAR](https://developer.android.com/studio/build/dependencies?buildsystem=cmake&agpversion=4.1#publish-native-libs-in-aars) for the
library and consume that in your application. You do not necessarily need to
*publish* that AAR. It can be internal to your Gradle project.

If that's not an option:

- Vendor (i.e. copy) the third-party source into your repository and use [add_subdirectory](https://cmake.org/cmake/help/latest/command/add_subdirectory.html) to build it. This only works if the other library is also built with CMake.
- Define an [ExternalProject](https://cmake.org/cmake/help/latest/module/ExternalProject.html).
- Build the library separately from your project and follow [Use prebuilt libraries](https://developer.android.com/ndk/guides/cmake#using_prebuilt_libraries) to import it as a prebuilt.

## YASM support in CMake

The NDK provides CMake support for building assembly code written in
[YASM](http://yasm.tortall.net/) to run on x86 and x86-64
architectures. YASM is an open-source assembler for x86 and x86-64
architectures, based on the NASM assembler.

To build assembly code with CMake, make the following changes in your project's
`CMakeLists.txt`:

1. Call [`enable_language`](https://cmake.org/cmake/help/latest/command/enable_language.html) with the value set to `ASM_NASM`.
2. Depending on whether you are building a shared library or an executable binary, call [`add_library`](https://cmake.org/cmake/help/latest/command/add_library.html) or [`add_executable`](https://cmake.org/cmake/help/latest/command/add_executable.html). In the arguments, pass in a list of source files consisting of the `.asm` files for the assembly program in YASM and the `.c` files for the associated C libraries or functions.

The following snippet shows how you might configure your `CMakeLists.txt` to
build a YASM program as a shared library.

    cmake_minimum_required(VERSION 3.6.0)

    enable_language(ASM_NASM)

    add_library(test-yasm SHARED jni/test-yasm.c jni/print_hello.asm)

For an example of how to build a YASM program as an executable, see the [yasm
test](https://android.googlesource.com/platform/ndk/+/master/tests/device/yasm/) in the NDK git repository.

## Report problems

If you run into any issues with the NDK or its CMake toolchain file, report them
via the [android-ndk/ndk](https://github.com/android/ndk/issues) issue tracker on GitHub. For Gradle or
Android Gradle Plugin issues, [report a Studio bug](https://developer.android.com/studio/report-bugs) instead.