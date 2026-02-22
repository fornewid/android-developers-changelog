---
title: https://developer.android.com/studio/platform/debug
url: https://developer.android.com/studio/platform/debug
source: md.txt
---

# Debug platform code

Android Studio for Platform (ASfP) provides a powerful debugger that lets you:

- Select a device to debug on.
- Set breakpoints in your Java, Kotlin, and C/C++ code.
- Examine variables and evaluate expressions at runtime.

Before you use the debugger, you must flash your build to a device or emulator.

## App process (Java/Kotlin) debugging

To debug a Java or Kotlin application process:

1. Set breakpoints in your Java or Kotlin code within ASfP.

2. Select**Run \> Attach Debugger to Android Process**from the menu.

3. In the**Choose Process** dialog, make sure the**Debug type** is set to**Java Only**.

4. Select your device from the list.

5. Choose the specific application process you want to debug.

6. Click**OK**.

7. Interact with the application on your device to hit the breakpoints.

## System process (C/C++) debugging

To debug a system process written in C or C++:

1. Verify that you have only one device or emulator running.

2. Open a terminal and run`adb root`from your AOSP checkout root:`bash
   adb root`

<!-- -->

1. Set breakpoints in your C/C++ code within ASfP.

2. Select**Run \> Attach Debugger to Android Process**from the menu.

3. In the**Choose Process** dialog, change the**Debug type** to**Native Only** or**Dual (Java + Native)**.

4. Check the**Show all processes**box to see system processes.

5. Select your device from the list.

6. Choose the specific system process you want to debug (such as`surfaceflinger`or`system_server`).

7. Click**OK**.

8. The debugger attaches to the process. Interact with the device to hit your breakpoints.