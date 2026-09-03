---
title: https://developer.android.com/android-performance-analyzer/frame-profiler/quickstart
url: https://developer.android.com/android-performance-analyzer/frame-profiler/quickstart
source: md.txt
---

If you're already familiar with frame profiling, this guide provides all the
information you need to meet requirements, install the software, and begin
capturing and viewing frame profiles with the Frame Profiler in Android Performance Analyzer. Otherwise, see [Next
steps](https://developer.android.com/android-performance-analyzer/frame-profiler/quickstart#next-steps) for links to more in-depth guidance.

## Requirements

In order to successfully use the Frame Profiler to capture a frame profile, you
must meet requirements for the computer running the software, for the device
running the app under test, and for the app under test itself.

### Computer requirements

The computer that runs the Frame Profiler must meet the following requirements:

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

- A [supported Android device](https://developer.android.com/android-performance-analyzer/compatibility#device-gpu-compat) running Android 12 or higher.
- A USB cable.
- [Android Debug Bridge (`adb`)](https://developer.android.com/tools/adb) debugging must be enabled and the device must be accessible through `adb`. If the **Install via USB** option is present, enable it.

#### Device validation

To ensure a valid frame profile, Android Performance Analyzer runs a validation check the first
time you connect a new device. Don't disturb the device while validation is in
progress. This might cause the device to fail validation. If a device fails
validation but is set up correctly, you can retry validation by clicking the
**Retry** button in the **Device** drop-down or by disconnecting and
reconnecting the device.

After your device passes validation, a green check mark appears next to your
device's name in the **Configure a GFXR Recording** window.

### App requirements

While it's not a strict requirement, we recommend the following in order to help
profiling be as useful and accurate as possible:

- Use the release version of your game or a version that's built with performance options (such as compiler flags or packaging optimizations) enabled.
- Ensure that your app follows the guidance on [engine
  compatibility](https://developer.android.com/android-performance-analyzer/frame-profiler/compatibility#engine-compat) and [API compatibility](https://developer.android.com/android-performance-analyzer/frame-profiler/compatibility#api-compat) from the compatibility guide.

## Basic workflow

Perform the following steps to capture a frame profile and open the results for
analysis:

1. Open Android Performance Analyzer and either select an existing project or click **New
   Project** to create a new project.

   ![](https://developer.android.com/static/android-performance-analyzer/images/welcome-window-canary.png) **Figure 1** : A screenshot of the **Welcome to Android
   Performance Analyzer** startup window.
2. Type a name and a directory location for your new project. Android Performance Analyzer opens
   your empty project automatically.

   ![](https://developer.android.com/static/android-performance-analyzer/images/empty-project-canary.png) **Figure 2**: A screenshot of an empty project.
3. Click the **Record Trace** button on the left side of the title bar to open
   the **New Capture** window.

   ![](https://developer.android.com/static/android-performance-analyzer/images/new-capture-window.png) **Figure 3** : A screenshot of the **New Capture** window.
4. Select **Frame** and click **Configure** to open the **Configure a GFXR
   Recording** window.

   ![](https://developer.android.com/static/android-performance-analyzer/images/gfxr-recording.png) **Figure 4** : A screenshot of the **Configure a GFXR
   Recording** window.
5. [Adjust the options](https://developer.android.com/android-performance-analyzer/frame-profiler/capture#configure-profile) in the **Configure a GFXR Recording** window
   according to your needs and click **OK** . This opens the **Control
   Recording** window and automatically starts the app on your testing device.

   ![](https://developer.android.com/static/android-performance-analyzer/images/frame-control-recording.png) **Figure 5** : A screenshot of the **Control Recording** window.
6. When you reach the frame that you want to profile, click **Start**.
   Android Performance Analyzer retrieves the data for that single frame, then opens the output
   file in the trace view automatically. The data in the frame profile appears
   as the Frame Profiler finishes each task.

   ![](https://developer.android.com/static/android-performance-analyzer/images/frame-profile.png) **Figure 6**: A screenshot of an example frame profile.

## Next steps

For more in-depth guidance on using the Frame Profiler in Android Performance Analyzer, see [Capture a frame
profile](https://developer.android.com/android-performance-analyzer/frame-profiler/capture) and [View a frame profile](https://developer.android.com/android-performance-analyzer/frame-profiler/view).