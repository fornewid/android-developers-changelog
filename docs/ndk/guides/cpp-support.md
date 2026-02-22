---
title: https://developer.android.com/ndk/guides/cpp-support
url: https://developer.android.com/ndk/guides/cpp-support
source: md.txt
---

# C++ library support

The NDK supports multiple C++ runtime libraries. This document provides information about these libraries, the tradeoffs involved, and how to use them.

## C++ runtime libraries

**Table 1.**NDK C++ Runtimes and Features.

|                                 Name                                  |                Features                |
|-----------------------------------------------------------------------|----------------------------------------|
| [libc++](https://developer.android.com/ndk/guides/cpp-support#libc)   | Modern C++ support.                    |
| [system](https://developer.android.com/ndk/guides/cpp-support#system) | `new`and`delete`. (Deprecated in r18.) |
| [none](https://developer.android.com/ndk/guides/cpp-support#none)     | No headers, limited C++.               |

libc++ is available as both a static and shared library.
| **Warning:** Using static runtimes can cause unexpected behavior. See the[static runtimes section](https://developer.android.com/ndk/guides/cpp-support#static_runtimes)for more information.

### libc++

[LLVM's libc++](https://libcxx.llvm.org)is the C++ standard library that has been used by the Android OS since Lollipop, and as of NDK r18 is the only STL available in the NDK.
| **Note:** For full details of the expected level of C++*library* support for any given version, see the[C++14 Status](https://libcxx.llvm.org/Status/Cxx14.html),[C++17 Status](https://libcxx.llvm.org/Status/Cxx17.html), and[C++20 Status](https://libcxx.llvm.org/Status/Cxx20.html)pages. (C++20 was previously known as C++2a.) The level of C++*language* support in the compiler is orthogonal; see[C++ Support in Clang](https://clang.llvm.org/cxx_status.html)instead.

CMake defaults to whatever version of C++ clang defaults to (currently C++14), so you'll need to set the standard`CMAKE_CXX_STANDARD`to the appropriate value in your`CMakeLists.txt`file to use C++17 or later features. See the CMake[documentation for`CMAKE_CXX_STANDARD`](https://cmake.org/cmake/help/latest/variable/CMAKE_CXX_STANDARD.html)for more details.

ndk-build also leaves the decision to clang by default, so ndk-build users should use`APP_CPPFLAGS`to add`-std=c++17`or whatever they want instead.

The shared library for libc++ is`libc++_shared.so`, and the static library is`libc++_static.a`. In typical cases the build system will handle using and packaging these libraries as needed for the user. For atypical cases or when implementing your own build system, see the[Build System Maintainers Guide](https://android.googlesource.com/platform/ndk/+/master/docs/BuildSystemMaintainers.md)or the guide for[using other build systems](https://developer.android.com/ndk/guides/other_build_systems).
| **Note:** libc++ is not a system library. If you use`libc++_shared.so`, it must be included in your app. If you're building your application with Gradle this is handled automatically.

The LLVM Project is under the Apache License v2.0 with LLVM Exceptions. For more information, see the[license file](https://github.com/llvm/llvm-project/blob/main/libcxx/LICENSE.TXT).

### system

The system runtime refers to`/system/lib/libstdc++.so`. This library should not be confused with GNU's full-featured libstdc++. On Android, libstdc++ is just`new`and`delete`. Use libc++ for a full-featured C++ standard library.
| **Note:** The system STL will be removed in a future NDK release. See[Issue 744](https://github.com/android-ndk/ndk/issues/744).

The system C++ runtime provides support for the basic C++ Runtime ABI. Essentially, this library provides`new`and`delete`. In contrast to the other options available in the NDK, there is no support for exception handling or RTTI.

There is no standard library support aside from the C++ wrappers for the C library headers such as`<cstdio>`. If you want an STL, you should use one of the other options presented on this page.

### none

There is also the option to have no STL. There are no linking or licensing requirements in that case. No C++ standard headers are available.

### Selecting a C++ Runtime

#### CMake

The default for CMake is`c++_static`.

You can specify`c++_shared`,`c++_static`,`none`, or`system`using the`ANDROID_STL`variable in your module-level`build.gradle`file. To learn more, see the documentation for[ANDROID_STL](https://developer.android.com/ndk/guides/cmake#android_stl)in CMake.

#### ndk-build

The default for ndk-build is`none`.

You can specify`c++_shared`,`c++_static`,`none`, or`system`using the`APP_STL`variable in your[Application.mk](https://developer.android.com/ndk/guides/application_mk)file. For example:  

    APP_STL := c++_shared

ndk-build only allows you to select one runtime for your app, and can only do in[Application.mk](https://developer.android.com/ndk/guides/application_mk).

#### Use clang directly

If you're using clang directly in your own build system, clang++ will use`c++_shared`by default. To use the static variant, add`-static-libstdc++`to your linker flags. Note that although the option uses the name "libstdc++" for historical reasons, this is correct for libc++ as well.

## Important considerations

### Static runtimes

If all of your application's native code is contained in a single shared library, we recommend using the static runtime. This allows the linker to inline and prune as much unused code as possible, leading to the most optimized and smallest application possible. It also avoids PackageManager and dynamic linker bugs in old versions of Android that make handling multiple shared libraries difficult and error-prone.

That said, in C++, it is not safe to define more than one copy of the same function or object in a single program. This is one aspect of the[One Definition Rule](http://en.cppreference.com/w/cpp/language/definition)present in the C++ standard.

When using a static runtime (and static libraries in general), it is easy to accidentally break this rule. For example, the following application breaks this rule:  

    # Application.mk
    APP_STL := c++_static

    # Android.mk

    include $(CLEAR_VARS)
    LOCAL_MODULE := foo
    LOCAL_SRC_FILES := foo.cpp
    include $(BUILD_SHARED_LIBRARY)

    include $(CLEAR_VARS)
    LOCAL_MODULE := bar
    LOCAL_SRC_FILES := bar.cpp
    LOCAL_SHARED_LIBRARIES := foo
    include $(BUILD_SHARED_LIBRARY)

In this situation, the STL, including and global data and static constructors, will be present in both libraries. The runtime behavior of this application is undefined, and in practice crashes are very common. Other possible issues include:

- Memory allocated in one library, and freed in the other, causing memory leakage or heap corruption.
- Exceptions raised in`libfoo.so`going uncaught in`libbar.so`, causing your app to crash.
- Buffering of`std::cout`not working properly.

Beyond the behavioral issues involved, linking the static runtime into multiple libraries will duplicate the code in each shared library, increasing the size of your application.

In general, you can only use a static variant of the C++ runtime if you have one and only one shared library in your application.
| **Note:** This rule applies to both your code and your third party dependencies.

### Shared runtimes

| **Caution:** JNI libraries distributed with Java AARs**must not** use the shared runtime to avoid conflicting with other libraries and the app. The warnings below still apply. See the documentation for[Middleware Vendors](https://android.googlesource.com/platform/ndk/+/refs/heads/master/docs/user/middleware_vendors.md)for more information.

If your application includes multiple shared libraries, you should use`libc++_shared.so`.

On Android, the libc++ used by the NDK is not the same as the one that's part of the OS. This gives NDK users access to the latest libc++ features and bug fixes even when targeting old versions of Android. The trade-off is that if you use`libc++_shared.so`, you must include it in your app. If you're building your application with Gradle this is handled automatically.

Old versions of Android had bugs in PackageManager and the dynamic linker that caused installation, update, and loading of native libraries to be unreliable. In particular, if your app targets a version of Android earlier than Android 4.3 (Android API level 18), and you use`libc++_shared.so`, you must load the shared library before any other library that depends on it.

The[ReLinker](https://github.com/KeepSafe/ReLinker)project offers workarounds for all known native library loading problems, and is usually a better choice than writing your own workarounds.

### One STL per app

Historically the NDK supported GNU libstdc++ and STLport in addition to libc++. If your application depends on prebuilt libraries that were built against an NDK different than the one used to build your application, you will need to ensure that it does so in a compatible manner.

An application should not use more than one C++ runtime. The various STLs are**not** compatible with one another. As an example, the layout of`std::string`in libc++ is not the same as it is in gnustl. Code written against one STL will not be able to use objects written against another. This is just one example; the incompatibilities are numerous.
| **Note:** The exception to this rule is that "no STL" does not count as an STL. You can safely use C only libraries (or even the[none](https://developer.android.com/ndk/guides/cpp-support#none)or[system](https://developer.android.com/ndk/guides/cpp-support#system)runtimes, since they're not actually STLs) in the same application as an STL. This rule only applies to[libc++](https://developer.android.com/ndk/guides/cpp-support#libc), gnustl, and stlport.
| **Warning:** The linker can catch some of these issues at build time, but many of these issues will only manifest as a crash or odd behavior at run time.

This rule extends beyond your code. All of your dependencies must use the same STL that you have selected. If you depend on a closed source third-party dependency that uses the STL and does not provide a library per STL, you do not have a choice in STL. You must use the same STL as your dependency.

It is possible that you will depend on two mutually incompatible libraries. In this situation the only solutions are to drop one of the dependencies or ask the maintainer to provide a library built against the other STL.
| **Note:** While we attempt to maintain ABI compatibility across NDK releases, this is not always possible. For the best compatibility, you should use not only the same STL as your dependencies but also the same version of the NDK whenever possible.

## C++ Exceptions

C++ exceptions are supported by libc++, but they are disabled by default in ndk-build. This is because historically C++ exceptions were not available in the NDK. CMake and standalone toolchains have C++ exceptions enabled by default.

To enable exceptions across your whole application in ndk-build, add the following line to your[Application.mk](https://developer.android.com/ndk/guides/application_mk)file:  

    APP_CPPFLAGS := -fexceptions

To enable exceptions for a single ndk-build module, add the following line to the given module in its[Android.mk](https://developer.android.com/ndk/guides/android_mk):  

    LOCAL_CPP_FEATURES := exceptions

Alternatively, you can use:  

    LOCAL_CPPFLAGS := -fexceptions

## RTTI

As with exceptions, RTTI is supported by libc++, but is disabled by default in ndk-build. CMake and standalone toolchains have RTTI enabled by default.

To enable RTTI across your whole application in ndk-build, add the following line to your[Application.mk](https://developer.android.com/ndk/guides/application_mk)file:  

    APP_CPPFLAGS := -frtti

To enable RTTI for a single ndk-build module, add the following line to the given module in its[Android.mk](https://developer.android.com/ndk/guides/android_mk):  

    LOCAL_CPP_FEATURES := rtti

Alternatively, you can use:  

    LOCAL_CPPFLAGS := -frtti