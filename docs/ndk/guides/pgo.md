---
title: https://developer.android.com/ndk/guides/pgo
url: https://developer.android.com/ndk/guides/pgo
source: md.txt
---

# Profile-guided Optimization

[Profile-guided optimization (PGO)](https://clang.llvm.org/docs/UsersManual.html#profile-guided-optimization)is a well known compiler optimization technique. In PGO, runtime profiles from a program's executions are used by the compiler to make optimal choices about inlining and code layout. This leads to improved performance and reduced code size.

PGO can be deployed to your application or library with the following steps: 1. Identify a representative workload. 2. Collect profiles. 3. Use the profiles in a Release build.

## Step 1: Identify a Representative Workload

First, identify a representative benchmark or workload for your application. This is a critical step as the profiles collected from the workload identify the hot and cold regions in the code. When using the profiles, the compiler will perform aggressive optimizations and inlining in the hot regions. The compiler may also choose to reduce the code size of cold regions while trading off performance.

Identifying a good workload is also beneficial to keep track of performance in general.

## Step 2: Collect Profiles

Profile collection involves three steps: - building native code with instrumentation, - running the instrumented app on the device and generating profiles, and - merging/post-processing the profiles on the host.

### Create Instrumented Build

The profiles are collected by running the workload from step 1 on an instrumented build of the application. To generate an instrumented build, add`-fprofile-generate`to the compiler and linker flags. This flag should be controlled by a separate build variable since the flag is not needed during a default build.

### Generate Profiles

Next, run the instrumented app on the device and generate profiles. Profiles are collected in memory when the instrumented binary is run and get written to a file at exit. However, functions registered with`atexit`are not called in an Android app --- the app just gets killed.

The application/workload has to do extra work to set a path for the profile file and then explicitly trigger a profile write.

- To set the profile file path, call`__llvm_profile_set_filename(PROFILE_DIR "/default-%m.profraw`.`%m`is useful when there are multiple shared libraries.`%m`expands to a unique module signature for that library, resulting in a separate profile per library. See[here](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html#running-the-instrumented-program)for other useful pattern specifiers.`PROFILE_DIR`is a directory that is writable from the app. See the[demo](https://developer.android.com/ndk/guides/pgo#putting_it_all_together)for detecting this directory at runtime.
- To explicitly trigger a profile write, call the`__llvm_profile_write_file`function.

    extern "C" {
    extern int __llvm_profile_set_filename(const char*);
    extern int __llvm_profile_write_file(void);
    }

    #define PROFILE_DIR "<location-writable-from-app>"
    void workload() {
      // ...
      // run workload
      // ...

      // set path and write profiles after workload execution
      __llvm_profile_set_filename(PROFILE_DIR "/default-%m.profraw");
      __llvm_profile_write_file();
      return;
    }

NB: Generating the profile file is simpler if the workload is a standalone binary --- just set the`LLVM_PROFILE_FILE`environment variable to`%t/default-%m.profraw`before running the binary.

### Post-process Profiles

The profile files are in the .profraw format. They must first be fetched from the device using`adb pull`. After fetch, use the`llvm-profdata`utility in the NDK to convert from`.profraw`to`.profdata`, which can then be passed to the compiler.  

    $NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/llvm-profdata \
        merge --output=pgo_profile.profdata \
        <list-of-profraw-files>

Use the`llvm-profdata`and`clang`from the same NDK release to avoid version mismatch of the profile file formats.

## Step 3 Use the Profiles to Build Application

Use the profile from the previous step during a release build of your application by passing`-fprofile-use=<>.profdata`to the compiler and linker. The profiles can be used even as the code evolves --- the Clang compiler can tolerate slight mismatch between the source and the profiles.

NB: In general, for most libraries, the profiles are common across architectures. For e.g., profiles generated from arm64 build of the library can be used for all architectures. The caveat being that if there are architecture-specific code paths in the library (arm vs x86 or 32-bit vs 64-bit), separate profiles should be used for each such configuration.

## Putting it all together

<https://github.com/DanAlbert/ndk-samples/tree/pgo/pgo>shows an end-to-end demo for using PGO from an app. It provides additional details that were skimmed over in this doc.

- The[CMake build rules](https://github.com/DanAlbert/ndk-samples/blob/pgo/pgo/app/src/main/cpp/CMakeLists.txt)show how to setup a CMake variable that builds native code with instrumentation. When the build variable is not set, native code is optimized using previously generated PGO profiles.
- In an instrumented build,[pgodemo.cpp](https://github.com/DanAlbert/ndk-samples/blob/pgo/pgo/app/src/main/cpp/pgodemo.cpp)writes the profiles are workload execution.
- A writable location for the profiles is obtained at runtime in[MainActivity.kt](https://github.com/DanAlbert/ndk-samples/blob/pgo/pgo/app/src/main/java/com/example/pgodemo/MainActivity.kt)using`applicationContext.cacheDir.toString()`.
- To pull profiles from the device without requiring`adb root`, use the`adb`recipe[here](https://github.com/DanAlbert/ndk-samples/blob/pgo/pgo/app/src/main/cpp/CMakeLists.txt#L11).