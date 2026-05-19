---
title: https://developer.android.com/android-performance-analyzer/quickstart
url: https://developer.android.com/android-performance-analyzer/quickstart
source: md.txt
---

If you're already familiar with system profiling, this guide provides all the
information you need to meet requirements, install the software, and begin
running and viewing traces with the System Profiler in Android Performance Analyzer. Otherwise, see [next
steps](https://developer.android.com/android-performance-analyzer/quickstart#next-steps) for links to more in-depth guidance.

## Requirements

In order to successfully use the System Profiler to record a system trace, there
are requirements that must be met by the computer running the software, the
device running the app under test, and the app under test itself.

### Computer requirements

The computer that runs the System Profiler must meet the following
requirements:

- It must have one of the following operating systems installed:
  - **Windows.** 64-bit Windows 10 or higher.
  - **macOS.** macOS 12 or higher.
    - Must have an ARM-based chip. Macs with Intel chips are unsupported.
  - **Linux.**
    - 64-bit machines must install the [required libraries for 64-bit
      machines](https://developer.android.com/studio/install#64bit-libs).
- It must have the Android SDK installed, including the [Platform-Tools](https://developer.android.com/tools/releases/platform-tools) package.
  - The [`ANDROID_HOME`](https://developer.android.com/tools/variables#android_home) environment variable must be set.

### Testing device requirements

The device running the app under test must meet the following requirements:

- A supported Android device running [Android 12 or higher](https://developer.android.com/about/versions).
- A USB cable.
- [Android Debug Bridge (`adb`)](https://developer.android.com/tools/adb) debugging must be enabled and the device must be accessible through `adb`. If the **Install via USB** option is present, enable it.

> [!NOTE]
> **Note:** The listed requirements are the minimum to use the System Profiler with a given testing device. Different devices and GPUs expose different data, which might result in some trace data being unavailable.

#### Device validation

To ensure a valid system trace, the System Profiler runs a validation check the
first time you connect a new device. Don't disturb the device while validation
is in progress. This might cause the device to fail validation. If a device
fails validation but is set up correctly, you can retry validation by clicking
the **Retry** button in the **Device** drop-down or by disconnecting and
reconnecting the device.

After your device passes validation, a green check mark appears next to your
device's name in the **Configure a Recording** window.

### App requirements

While it's not a strict requirement, we recommend the following in order to help
profiling be as useful and accurate as possible:

- Use the release version of your app or game, or a version that's built with performance options (such as compiler flags or packaging optimizations) enabled.
- If you are profiling an app or game that uses [Vulkan](https://developer.android.com/games/develop/vulkan/overview) for graphics, set the [debuggable attribute](https://developer.android.com/guide/topics/manifest/application-element#debug) in the Android manifest to *true*. This allows Vulkan-specific data to be included in system traces.
- For Java and Kotlin applications, set the [debuggable attribute](https://developer.android.com/guide/topics/manifest/application-element#debug) to *false* to allow the Android Runtime to run at maximum optimized efficiency. This helps your system traces mirror real-world performance. It doesn't make as much of a difference for pure C/C++ apps or native game loops, but managed-code apps need it in order to yield accurate profiling data.

## Basic workflow

Perform the following steps to capture profiling data and open the resulting
trace file for analysis:

1. Open Android Performance Analyzer and either select an existing project or click **New
   Project** to create a new project.

   ![](https://developer.android.com/static/android-performance-analyzer/images/welcome-window.png) **Figure 1** : A screenshot of the **Welcome to Android
   Performance Analyzer** startup window.
2. Type a name and a directory location for your new project. Android Performance Analyzer opens
   your empty project automatically.

   ![](https://developer.android.com/static/android-performance-analyzer/images/empty-project.png) **Figure 2**: A screenshot of an empty project.
3. Click the **Record Trace** button on the left side of the title bar to open
   the **Configure a Recording** window.

   ![](https://developer.android.com/static/android-performance-analyzer/images/configure-recording.png) **Figure 3** : A screenshot of the **Configure a
   Recording** window.
4. The **Configure a Recording** window initially opens with the default trace
   configuration. [Adjust the options](https://developer.android.com/android-performance-analyzer/run#config) according to your needs and
   click **OK** . This opens the **Control Recording** window and automatically
   starts the app on your testing device.

   ![](https://developer.android.com/static/android-performance-analyzer/images/control-recording.png) **Figure 4** : A screenshot of the **Control Recording** window.
5. Run your test. The trace runs until you click **Stop** or until the preset
   duration runs out (if you set one). Android Performance Analyzer retrieves the trace data,
   then opens the results in the trace view automatically.

   ![](https://developer.android.com/static/android-performance-analyzer/images/trace-view.png) **Figure 5**: A screenshot of an example trace view.
6. Use the trace view to interact with and analyze the collected data.

## Next steps

For more in-depth guidance on using the the System Profiler in Android Performance Analyzer, see [Record a system
trace](https://developer.android.com/android-performance-analyzer/run) and [View a system trace](https://developer.android.com/android-performance-analyzer/view).