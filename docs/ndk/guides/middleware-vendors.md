---
title: https://developer.android.com/ndk/guides/middleware-vendors
url: https://developer.android.com/ndk/guides/middleware-vendors
source: md.txt
---

Distributing middleware built with the NDK raises some additional issues that
app developers do not need to worry about. Prebuilt libraries impose some of
their implementation choices on their users.

## Choosing API levels and NDK versions

Your users cannot use a [minSdkVersion](https://developer.android.com/ndk/guides/sdk-versions#minsdkversion) lower than yours. If your users' apps
need to run on API 21, you cannot build for API 24. It is okay to build your
library for a *lower* API level than your users. You can build for API
16 and remain compatible with your API 21 users.

NDK versions are largely compatible with each other, but occasionally there are
changes that break compatibility. If you know that all of your users are using
the same version of the NDK, it's best to use the same version that they do.
Otherwise, use the newest version.

## Using the STL

If you're writing C++ and using the STL, your choice between `libc++_shared` and
`libc++_static` affects your users if you distribute a shared library. If you
distribute a shared library, you must either use `libc++_shared` or ensure that
libc++'s symbols are not exposed by your library. The best way to do this is to
explicitly declare your ABI surface with a [version script](https://developer.android.com/ndk/guides/this%20also%20helps%0Akeep%20your%20implementation%20details%20private).

Another, less robust option is to use `-Wl,--exclude-libs,libc++_static.a
-Wl,--exclude-libs,libc++abi.a` when linking. This is less robust because it
will only hide the symbols in the libraries that are explicitly named, and no
diagnostics are reported for libraries that are not used (a typo in the library
name is not an error, and the burden is on the user to keep the library list up
to date). This approach also does not hide your own implementation details.

## Distributing native libraries in AARs

| **Note:** This section describes how to distribute C/C++ *APIs* to users. If your native libraries are implementation details of your *Java* API, see the [Java
| middleware with JNI libraries](https://developer.android.com/ndk/guides/middleware-vendors#java_middleware_with_jni_libraries) section.

The Android Gradle plugin can import [native dependencies](https://developer.android.com/studio/build/dependencies#using-native-dependencies) distributed in
[AARs](https://developer.android.com/studio/projects/android-library). If your users are using the Android Gradle plugin, this will be the
easiest way for them to consume your library.

Native libraries can be packaged into an AAR [by
AGP](https://developer.android.com/studio/releases/gradle-plugin#4.1-prefab-publish). This will be the
easiest option if your library is already built by [externalNativeBuild](https://developer.android.com/reference/tools/gradle-api/current/com/android/build/api/dsl/ExternalNativeBuild).

Non-AGP builds can use [ndkports](https://android.googlesource.com/platform/tools/ndkports/), or perform manual packaging by following the
[Prefab](https://google.github.io/prefab/) documentation to create the `prefab/` subdirectory of their AAR.

## Java middleware with JNI libraries

Java libraries that include JNI libraries (in other words, AARs that contain
`jniLibs`) need to be careful that the JNI libraries they include will not
collide with other libraries in the user's app. For example, if the AAR includes
`libc++_shared.so`, but a different version of `libc++_shared.so` than the app
uses, only one will be installed to the APK and that may lead to unreliable
behavior.
| **Warning:** [Bug 141758241](https://issuetracker.google.com/141758241): Older versions of the Android Gradle plugin do not currently diagnose this error condition. One of the identically named libraries will be arbitrarily chosen for packaging in the APK.

The most reliable solution is for Java libraries to include no more than **one**
JNI library (this is good advice for apps too). All dependencies including the
STL should be statically linked into the implementation library, and a version
script should be used to enforce the ABI surface. For example, a Java library
`com.example.foo` that includes the JNI library `libfooimpl.so` should use the
following version script:

    LIBFOOIMPL {
    global:
        JNI_OnLoad;
    local:
        *;
    };

This example uses `registerNatives` via `JNI_OnLoad` as described in [JNI Tips](https://developer.android.com/training/articles/perf-jni#native-libraries)
to ensure that the minimal ABI surface is exposed and library load time is
minimized.