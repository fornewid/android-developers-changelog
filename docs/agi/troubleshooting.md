---
title: https://developer.android.com/agi/troubleshooting
url: https://developer.android.com/agi/troubleshooting
source: md.txt
---

# Troubleshooting AGI

This topic describes how to fix common issues when using Android GPU Inspector (AGI) .

## Resetting AGI settings

AGI stores its settings in the`~/.agic`file. Removing this file deletes all AGI settings, including the list of recently opened traces and device validation results.

## AGI fails on some devices

Please make sure that your setup meets all the[requirements](https://developer.android.com/agi/getting-started#requirements).

The following can also help:

- Stop any program that may interact with the device over ADB, such as Android Studio.

- Enable the`Stay awake`option (under Developer options on Android) to prevent issues that arise when the device screen turns off due to sleep mode.

## System profiler doesn't report GPU activity for OpenGL ES games

Currently, only GPU counters are supported when you trace an OpenGL ES application. GPU activity information for OpenGL ES applications is under active development.

## Frame profiler fails on some Vulkan games

The first thing to verify is that your game uses Vulkan correctly. Use the[Vulkan validation layer](https://developer.android.com/ndk/guides/graphics/validation-layer)and make sure that your game raises no errors or warnings.

If there is any Vulkan validation error, then AGI frame profiler is not expected to work.

## Game failure when creating a frame profiler trace

If the game runs successfully without AGI but fails to run when creating a frame profile trace, the game might be forking a different process during its startup sequence. In that case, you need to specify the name of the process to trace in the "Process name" field in trace options.

To identify this issue, you can check the logcat output while you create a trace and verify whether a different process is starting:  

    # Clear the logcat output
    adb logcat -c

    ## Use AGI to attempt to create a frame profile trace

    Look at the logcat output to identify the processes that are running AGI. 

    adb logcat | grep "this process name"
    I GAPID   : gapii [gapii/cc/spy.cpp:109] this process name: com.example.mygame
    I GAPID   : gapii [gapii/cc/spy.cpp:109] this process name: com.example.mygame:GameProcess

Most games have only one process, the example above shows what to expect for a game that has more than one process.

The game starts in a main process named`com.example.mygame`, and then forks a new process named`com.example.mygame:GameProcess`. If the actual game rendering happens in the second process, then you must tell AGI that this is the process you want to trace. You can do so by entering the name of the process in the`Process name`field of the trace option dialog.

## Game failure after using AGI

If a trace does not terminate properly, AGI may leave some Android settings in a state that may interrupt subsequent runs of the app. These settings are:

- Vulkan layers related settings:

  - `enable_gpu_debug_layers`

  - `gpu_debug_app`

  - `gpu_debug_layers`

  - `gpu_debug_layer_app`

- ANGLE related settings:

  - `angle_debug_package`

  - `angle_gl_driver_selection_values`

  - `angle_gl_driver_selection_pkgs`

If your app has any issues after using AGI, you can try clearing these settings with the following adb commands:  

    # Vulkan layers
    adb shell settings delete global enable_gpu_debug_layers
    adb shell settings delete global gpu_debug_app
    adb shell settings delete global gpu_debug_layers
    adb shell settings delete global gpu_debug_layer_app
    # ANGLE
    adb shell settings delete global angle_debug_package
    adb shell settings delete global angle_gl_driver_selection_values
    adb shell settings delete global angle_gl_driver_selection_pkgs

## Your game looks different when launching it via AGI while creating a frame profile trace

To create a frame profile trace, AGI intercepts the graphics API calls made by the game, which may affect the game renderings.

AGI captures Vulkan calls. For OpenGL ES games, AGI relies on[ANGLE](https://chromium.googlesource.com/angle/angle)to translate OpenGL ES to Vulkan. If your game looks different (e.g. some colors are not the ones you expect) when you launch it via AGI, it is probably a bug in AGI or ANGLE. You can help us get a better understanding of the root cause of the issue by trying the following.

### Vulkan games: trace with all Vulkan extensions supported

The**Include Unknown Extensions** tracing option controls whether AGI should include Vulkan extensions it does not support. (Browse[a list of supported extensions](https://developer.android.com/agi/vulkan-extensions).)

If your app uses an extension that isn't supported by AGI, you might encounter undesirable behavior, including subtle errors or crashes, when replaying the trace.

Try enabling this option, then launch another frame profiler trace. If the game displays as expected with the option is enabled, the game may rely on a Vulkan extension that is not supported by AGI.

### OpenGL ES games: run with ANGLE only

You can run your OpenGL ES game with ANGLE but without AGI to see if the wrong rendering comes from an issue in ANGLE.

If you already tried to create a frame profile trace of your OpenGL ES game, then AGI already installed ANGLE on your device. The ANGLE package used by AGI is named`org.chromium.angle.agi`.

To force your game to run on ANGLE, use the following commands:  

    # Make sure that the AGI capture layer will be ignored
    adb shell settings delete global enable_gpu_debug_layers
    # Force the package com.example.mygame to use ANGLE
    adb shell settings put global angle_debug_package org.chromium.angle.agi
    adb shell settings put global angle_gl_driver_selection_values angle
    adb shell settings put global angle_gl_driver_selection_pkgs com.example.mygame

If the game looks different with these settings, then it is probably a bug in ANGLE, and not AGI. If the game looks correct with these settings, but looks different while creating an AGI trace, then it is probably a bug in AGI.

You can report AGI bugs by creating a[GitHub issue](https://github.com/google/agi/issues/new?template=standard-bug-report-for-gapid.md).