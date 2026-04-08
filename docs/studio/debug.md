---
title: https://developer.android.com/studio/debug
url: https://developer.android.com/studio/debug
source: md.txt
---

Android Studio provides a debugger that lets you do the following and more:

- Select a device to debug your app on.
- Set breakpoints in your Java, Kotlin, and C/C++ code.
- Examine variables and evaluate expressions at runtime.

This page includes instructions for basic debugger operations. For more documentation, also
see the [IntelliJ IDEA debugging docs](https://www.jetbrains.com/help/idea/2025.3/debugging.html).

## Enable debugging

Before you can begin debugging, do the following:

Enable debugging on your device.
:   If you're using the emulator, debugging is enabled by default. But for a connected device, you
    need to [enable debugging in the device developer
    options](https://developer.android.com/studio/debug/dev-options).

Run a debuggable build variant.

:   Use a [build variant](https://developer.android.com/studio/build/build-variants) that
    includes [`debuggable true`](https://developer.android.com/studio/build/build-variants#build-types)
    (`isDebuggable = true` in Kotlin scripts) in the build configuration.

    Usually, you can select the default "debug" variant that's included in every Android Studio
    project, even though it's not visible in the `build.gradle` file. However, if you
    define new build types that should be debuggable, you must add `debuggable true`
    to the build type: