---
title: https://developer.android.com/ndk/guides/other_build_systems
url: https://developer.android.com/ndk/guides/other_build_systems
source: md.txt
---

# Use the NDK with other build systems

| **Note:** The content described on this page requires at least NDK r19. If you're using an older NDK, consider upgrading. If you're unable to upgrade, use`<NDK>/build/tools/make_standalone_toolchain.py`.

The NDK contains official support for[ndk-build](https://developer.android.com/ndk/guides/ndk-build)and[CMake](https://developer.android.com/ndk/guides/cmake). Most users should refer to one of those guides for building application code. The purpose of this document is to describe how to build existing code that uses other build systems. This is often the case with third-party dependencies that are not Android-specific, such as OpenSSL and libbzip2.

Build system maintainers looking to add native NDK support to their build systems should instead read the[Build System Maintainers Guide](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md).

## Overview

The Clang compiler in the NDK is useable with only minimal configuration required to define your target environment.

To ensure that you build for the correct architecture, pass the appropriate target with`-target`when invoking Clang. For example, to compile for 64-bit ARM Android with a`minSdkVersion`of 21, do the following:  

    $ $NDK/toolchains/llvm/prebuilt/$HOST_TAG/bin/clang++ \
        --target=aarch64-linux-android21 foo.cpp

Alternatively, there are target-prefixed entry-points for Clang. These may be either symlinks or scripts that forward to clang, depending on the NDK release and host OS. Invoking Clang directly with`--target`will be more reliable, as that is the most tested workflow, and there are occasionally argument forwarding bugs in the scripts. On Windows, the extra`CreateProcess`needed to forward from the script to the real compiler could potentially have a noticeable negative impact on build speed.  

    $ $NDK/toolchains/llvm/prebuilt/$HOST_TAG/bin/aarch64-linux-android21-clang++ \
        foo.cpp

In both cases, replace`$NDK`with the path to the NDK and`$HOST_TAG`to match the NDK you downloaded according to the following table:

| NDK OS Variant |     Host Tag     |
|----------------|------------------|
| macOS          | `darwin-x86_64`  |
| Linux          | `linux-x86_64`   |
| 64-bit Windows | `windows-x86_64` |

| **Note:** Despite the x86_64 tag in the Darwin name, those are fat binaries that include M1 support. The paths were not updated to reflect that support because doing so would have broken existing builds that encode those paths.

The format of the prefix or target argument here is the target triple with a suffix denoting the`minSdkVersion`. This suffix is only used with clang/clang++; the binutils tools (such as`ar`and`strip`) do not require a suffix because they are unaffected by`minSdkVersion`. Android's supported target triples are as follows:

|     ABI     |           Triple           |
|-------------|----------------------------|
| armeabi-v7a | `armv7a-linux-androideabi` |
| arm64-v8a   | `aarch64-linux-android`    |
| x86         | `i686-linux-android`       |
| x86-64      | `x86_64-linux-android`     |

| **Note:** For 32-bit ARM, the compiler is prefixed with`armv7a-linux-androideabi`, but the binutils tools are prefixed with`arm-linux-androideabi`. For other architectures, the prefixes are the same for all tools.

Many projects' build scripts will expect GCC-style cross compilers where each compiler targets only one OS/architecture combination and so may not handle`-target`cleanly. In these cases, you can typically include the`-target`argument as part of the compiler definition (e.g.`CC="clang -target
aarch64-linux-android21`). In rare cases where the build system you're using is not able to use that form, use the triple-prefixed Clang binaries.

## Autoconf

| **Caution:** Autoconf projects are generally not buildable on Windows. Windows users can build these projects using the Linux NDK in a Linux VM. The[Windows Subsystem for Linux](https://developer.android.com/ndk/guides/specifically%20WSL2)may also work, but is not officially supported. WSL1 is known not to work.

Autoconf projects allow you to specify the toolchain to use with environment variables. For example, the following shows how to build`libpng`for Android x86-64 with a`minSdkVersion`of API level 21, on Linux.  

    # Check out the source.
    git clone https://github.com/glennrp/libpng -b v1.6.37
    cd libpng
    # Only choose one of these, depending on your build machine...
    export TOOLCHAIN=$NDK/toolchains/llvm/prebuilt/darwin-x86_64
    export TOOLCHAIN=$NDK/toolchains/llvm/prebuilt/linux-x86_64
    # Only choose one of these, depending on your device...
    export TARGET=aarch64-linux-android
    export TARGET=armv7a-linux-androideabi
    export TARGET=i686-linux-android
    export TARGET=x86_64-linux-android
    # Set this to your minSdkVersion.
    export API=21
    # Configure and build.
    export AR=$TOOLCHAIN/bin/llvm-ar
    export CC="$TOOLCHAIN/bin/clang --target=$TARGET$API"
    export AS=$CC
    export CXX="$TOOLCHAIN/bin/clang++ --target=$TARGET$API"
    export LD=$TOOLCHAIN/bin/ld
    export RANLIB=$TOOLCHAIN/bin/llvm-ranlib
    export STRIP=$TOOLCHAIN/bin/llvm-strip
    ./configure --host $TARGET
    make

The tools selected in this sample are correct for NDK r22 and newer. Older NDKs may require different tools.

## Non-autoconf make projects

| **Caution:** Not all make projects support cross compiling, and not all do so in the same way. It is very likely that the project will not build without modifications. In those cases, refer to the[Build System Maintainers Guide](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md)for instructions on porting the build to Android.

Some makefile projects allow cross compilation by overriding the same variables that you would with an autoconf project. As an example, the following shows how to build`libbzip2`for Android x86-64 with a`minSdkVersion`of 21.  

    # Check out the source.
    git clone https://gitlab.com/bzip/bzip2.git
    cd bzip2

    # Only choose one of these, depending on your build machine...
    export TOOLCHAIN=$NDK/toolchains/llvm/prebuilt/darwin-x86_64
    export TOOLCHAIN=$NDK/toolchains/llvm/prebuilt/linux-x86_64

    # Only choose one of these, depending on your device...
    export TARGET=aarch64-linux-android
    export TARGET=armv7a-linux-androideabi
    export TARGET=i686-linux-android
    export TARGET=x86_64-linux-android

    # Set this to your minSdkVersion.
    export API=21

    # Build.
    make \
        CC="$TOOLCHAIN/bin/clang --target=$TARGET$API" \
        AR=$TOOLCHAIN/bin/llvm-ar \
        RANLIB=$TOOLCHAIN/bin/llvm-ranlib \
        bzip2

The tools selected in this sample are correct for NDK r22 and newer. Older NDKs may require different tools.