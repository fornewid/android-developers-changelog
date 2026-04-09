---
title: https://developer.android.com/build/native-dependencies
url: https://developer.android.com/build/native-dependencies
source: md.txt
---

AAR libraries can contain native dependencies that the Android Gradle Plugin can
consume. AGP is also capable of producing AARs that expose native libraries to
their consumers.

## Using native dependencies

Starting with Android Gradle plugin 4.0, C/C++ dependencies can be imported from
AARs linked in your `build.gradle` file. Gradle will automatically make these
available to the native build system, but your build system must be configured
to make use of the imported libraries and headers. Since C/C++ dependencies are
distributed as AARs, the following links about generic AARs may be helpful:

- [Creating an Android Library](https://developer.android.com/studio/projects/android-library) for generic AAR documentation and how to integrate it into your project, especially when you want to use the AAR as a local C/C++ dependency.
- [Add build dependencies](https://developer.android.com/studio/build/dependencies) for information on adding dependencies to your `build.gradle` file, especially for the remote dependencies.

This document focuses on how to configure your native build system and assumes you've already
added a C/C++ dependency AAR into your project's Gradle build environment.

## Native dependencies in AARs

AAR dependencies of your Gradle modules can expose native libraries for use by
your application. Inside the AAR, the `prefab` directory contains a [Prefab](https://google.github.io/prefab/)
package, which includes the headers and libraries of the native dependency.

Each dependency can expose at most one Prefab package, which comprises one or
more modules. A Prefab module is a single library, which could be either a
shared, static, or header only library.

The package and module names need to be known to make use of the libraries. By
convention the package name will match the Maven artifact name and the module
name will match the C/C++ library name, but this is not required. Consult the
dependency's documentation to determine what names it uses.

## Build system configuration

<button value="4.0">Android Gradle Plugin 4.0</button> <button value="4.1" default="">Android Gradle Plugin 4.1+</button>

The `prefab` feature must be enabled for your Android Gradle module.

To do so, add the following to the `android` block of your module's
`build.gradle` file:

### Kotlin

```kotlin
buildFeatures {
  prefab = true
}
```

### Groovy

```groovy
buildFeatures {
  prefab true
}
```

Optionally, configure [a version](https://github.com/google/prefab/releases)
in your project's `gradle.properties` file:

    android.prefabVersion=2.0.0

Typically the default version selected AGP will fit your needs. You should only
need to select a different version if there is a bug you need to work around or
a new feature you want.

<button value="cmake" default="">CMake</button> <button value="ndk-build">ndk-build</button>

Dependencies imported from an AAR are exposed to CMake via
[CMAKE_FIND_ROOT_PATH](https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH.html). This value will be set automatically by Gradle when
CMake is invoked, so if your build modifies this variable be sure to append
rather than assign to it.

Each dependency exposes a [config-file package](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#config-file-packages) to your build. These are
imported with the [find_package](https://cmake.org/cmake/help/latest/command/find_package.html) command. This command searches for config-file
packages matching the given package name and version and exposes the targets it
defines to be used in your build. For example, if your application defines
`libapp.so` and it uses cURL, your `CMakeLists.txt` should include the following:

    add_library(app SHARED app.cpp)

    # Add these two lines.
    find_package(curl REQUIRED CONFIG)
    target_link_libraries(app curl::curl)

`app.cpp` is now able to `#include "curl/curl.h"`, `libapp.so` will be
automatically linked against `libcurl.so` when building, and `libcurl.so` will
be included with the app.

## Publishing native libraries in AARs

The ability to create native AARs was first added in AGP 4.1.

To export your native libraries, add the following to the `android` block of
your library project's `build.gradle.kts` file:

### Kotlin

```kotlin
buildFeatures {
    prefabPublishing = true
}

prefab {
    create("mylibrary") {
      headers = "src/main/cpp/mylibrary/include"
    }

    create("myotherlibrary") {
        headers = "src/main/cpp/myotherlibrary/include"
    }
}
```

### Groovy

```groovy
buildFeatures {
    prefabPublishing true
}

prefab {
    mylibrary {
      headers "src/main/cpp/mylibrary/include"
    }

    myotherlibrary {
        headers "src/main/cpp/myotherlibrary/include"
    }
}
```

In this example, the `mylibrary` and `myotherlibrary` libraries from either your
ndk-build or CMake external native build will be packaged in the AAR produced by
your build, and each will export the headers from the specified directory to
their dependents.