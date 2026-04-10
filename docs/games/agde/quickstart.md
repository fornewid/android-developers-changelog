---
title: https://developer.android.com/games/agde/quickstart
url: https://developer.android.com/games/agde/quickstart
source: md.txt
---

Set up the Android Game Development Extension on a Windows computer and run a sample Visual
Studio C++ project on an Android device or emulator.

## Prerequisites

Follow the steps in this section to prepare your Windows computer for
installation of the extension:

1. Download and install one of the supported versions of Visual Studio:

   - [Visual Studio 2017 Version 15.4.0 (October 9th, 2017) or higher](https://docs.microsoft.com/en-us/visualstudio/install/update-visual-studio?view=vs-2017).
   - [Visual Studio 2019 Version 16.0.0 or higher](https://docs.microsoft.com/en-us/visualstudio/install/update-visual-studio?view=vs-2019).
   - [Visual Studio 2022 Version 17.0.0 or higher](https://docs.microsoft.com/en-us/visualstudio/install/update-visual-studio?view=vs-2022).
2. [Download and install .NET Core SDK 2.2](https://dotnet.microsoft.com/download/thank-you/dotnet-sdk-2.2.107-windows-x64-installer).

3. [Android Studio 3.5 or higher](https://developer.android.com/studio) is optional, but can be used
   instead of the Android Game Development Extension to install the
   [Android SDK and NDK](https://developer.android.com/games/agde/quickstart#install-sdk-ndk).

4. Download and install [JDK 17](https://jdk.java.net/archive/) for AGDE
   23.1.82 or newer, or [JDK 11](https://jdk.java.net/archive/) for up to AGDE
   22.2.71, and set your `JAVA_HOME` environment variable.

## Install the extension

Follow the steps in this section to download and install the
Android Game Development Extension:

1. Close all instances of Visual Studio.

2. Download the latest extension installer and samples from the
   [Downloads](https://developer.android.com/games/agde#downloads) page.

3. From your download location, double-click the installer. The installer takes
   several minutes to complete.

4. If you have more than one version of Visual Studio installed, select the
   versions that you would like the extension to be installed for.

5. Click **Finish** to complete the installation.

## Install the Android SDK and NDK

You can install the Android SDK and the Android
[Native Development Kit (NDK)](https://developer.android.com/studio/projects/install-ndk#specific-version)
with Android Studio or the Android Game Development Extension. To install the SDK and NDK from
the extension, use the **SDK Manager**, which is located in the
extension toolbar of Visual Studio.

When installing the NDK, make sure to use the **NDK (Side by side)** checkbox so
that the extension can locate it. You must install an NDK version
that is supported by the extension
(see [NDK revision history](https://developer.android.com/ndk/downloads/revision_history)).

To install the SDK to a different location than the default, set the
`ANDROID_SDK_ROOT` environment variable on your computer:

1. Ensure that Visual Studio is closed.
2. In Windows Search, search for `Environment Variables`.
3. Select **Edit the system environment variables**.
4. Click **Environment Variables**.
5. Under **User Variables** , click **New**.
6. In the **Variable Name** box, type `ANDROID_SDK_ROOT`.
7. In the **Variable Value** box, enter the path to the Android SDK.
8. Reboot your computer.

The location of the SDK cannot be modified using the SDK Manager window as this
environment variable is the only source-of-truth for the SDK location.

## Run the sample

Follow the steps in this section to run a provided sample on an
emulator and then on a physical Android device.

### Configure the platform

1. Unzip the samples zip file into a directory of your choice. The following
   samples are included:

   - endless-tunnel
   - HelloJNI
   - Teapot
2. Start Visual Studio if it is not already running.

3. Open the samples directory. Select **File \> Open \> Project/Solution** and
   navigate to the `.sln` file.

4. Select an Android platform:

   1. Select **Build \> Configuration Manager**.
   2. Under **Active solution platform** , select **Android-x86_64**.

   Android platforms are already configured in the samples (see [add
   more Android platforms](https://developer.android.com/games/agde/quickstart#add-platform) for adding platforms).

   > [!NOTE]
   > **Note:** Typical emulator images use x86 or x86_64 ABIs.

5. Make sure the sample project has the Android SDK and NDK properties
   configured:

   ![](https://developer.android.com/static/images/agde/android-platform-properties.png) **Figure
   1.** Android platform properties
   - In the **Solution Explorer** , right-click the project and select
     **Properties**.

   - Select the **General** properties tab and find the **Platform**
     properties for Android.

   > [!NOTE]
   > **Note:** Make sure you select an NDK that is installed.

6. Select the **Android Packaging** properties tab.

   ![](https://developer.android.com/static/images/agde/android-packaging-properties.png) **Figure
   2.** Android packaging properties

   You can change the output APK name and directory from this tab. Note that
   some of the Android configuration properties are defined in the property
   pages and are passed to Gradle. For example, the APK name property
   `MSBUILD_ANDROID_OUTPUT_APK_NAME` passes this name to the app `build.gradle`
   file.

### Set up the emulator

1. Start AVD Manager from the extension toolbar in Visual Studio.
   Configure a virtual device and then
   [run it in the Android emulator](https://developer.android.com/studio/run/emulator).

   1. In the Android Virtual Device Manager, click **Create Virtual Device**.
   2. Choose a device definition (for example, Pixel 2).
   3. Select a system image. You should select an x86_64 ABI because this architecture performs faster in the emulator.
   4. Verify the configuration and click **Finish**.
2. Start the virtual device by clicking the **Run**
   ![Run icon](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) button in the Android
   Virtual Device Manager.

3. In Visual Studio, the virtual device should appear next to the
   **Start Debugging** toolbar button. Click **Start Debugging** to launch the
   sample app on the device. It may take a few moments for the debugger
   to attach to the app. If you are running the Teapot sample, you can rotate
   the teapot by dragging your mouse cursor across it.

   ![Teapot sample running on an emulator](https://developer.android.com/static/images/agde/teapot-sample.png)  

   **Figure
   3**. Teapot sample running on an Android emulator

### Set up the device

1. To run the sample on a physical Android device, you may need to create a
   new Android platform in the project. This platform must match the architecture
   of the device. To create a new platform, do the following in Visual Studio:

   1. Select **Build \> Configuration Manager**.
   2. Under **Active solution platform** , select **\<New\>**.
   3. Type one of the following for the new platform:

      - **Android-armeabi-v7a**
      - **Android-arm64-v8a**
      - **Android-x86**
      - **Android-x86_64**
   4. In the **Copy settings from** box, select another existing Android
      platform (or **None** if you do not have any Android platforms yet).
      Make sure you enabled **Create new project platforms**.

2. Connect an Android device to your computer using a USB cable. The device
   type should be shown next to the **Start Debugging** toolbar button.

   ![Run button in Visual Studio](https://developer.android.com/static/images/agde/run-sample-target.png)  

   **Figure
   4** . Connected Android device shown next to the **Start Debugging** toolbar button

   If the device is not shown, check the following:
   - The platform selection matches the ABI of your device.
   - [Developer options and USB debugging](https://developer.android.com/studio/debug/dev-options) are enabled on the device.
   - The USB cable is connected from the device to the computer.
   - The USB cable supports a data connection (and not just power).
3. Click the **Start Debugging** toolbar button to launch the sample app on the
   device. It may take a few moments for the debugger to attach to the app.
   Once it is attached, you can interact with the app on your device.

## FAQ

The following are some frequently asked questions about the Android Game Development Extension.

### Where are the logs for the plugin located?

You can open the log file for the plugin using the **Open Logs** icon in the
**Android Game Development Extension** toolbar.

### What environment variables does the plugin use?

The plugin uses the following environment variables:

- `ANDROID_SDK_ROOT`
- `ANDROID_SDK_HOME`
- `TEMP`
- `GOOGLE_ANDROID_LOG_DIR`

## What's next

To use your own project with the extension, you must configure it according to
the [project configuration](https://developer.android.com/games/agde/adapt-existing-project) guide.