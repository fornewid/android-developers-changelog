---
title: https://developer.android.com/studio/intro/update
url: https://developer.android.com/studio/intro/update
source: md.txt
---

# Update the IDE and SDK tools

Once you install Android Studio, you can keep the Android Studio IDE and Android SDK tools up to date with automatic updates and the Android SDK Manager.

## Update your IDE using JetBrains Toolbox

If you installed Android Studio using[JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/), then Toolbox is responsible for handling updates to Android Studio. Toolbox lets you install canary, RC, and stable versions of Android Studio in parallel. It also lets you roll back to earlier versions of each, if required. When an update is available it displays in Toolbox, as shown in figure 1.
![Jetbrains Toolbox showing updcates available](https://developer.android.com/static/studio/images/jetbrains-toolbox_2x.png)

**Figure 1.**Jetbrains Toolbox showing available updates.

## Update your IDE and change channels

If you installed Android Studio manually, Android Studio notifies you with a small bubble dialog when an update is available for the IDE. To manually check for updates, click**File** \>**Settings** \>**Appearance \& Behavior** \>**System Settings** \>**Updates** (on macOS,**Android Studio** \>**Check for Updates**). See figure 2.

Updates for Android Studio are available from the following release channels:

- **Canary channel:** these bleeding-edge releases are updated roughly weekly and are available for download on the[Preview release](https://developer.android.com/studio/preview)page.

  In addition to receiving canary versions of Android Studio, you also receive preview versions of other SDK tools, including the Android Emulator.

  Although these builds are subject to more bugs, they do get tested and are available so you can try new features and provide feedback.

  <br />

  **Note:**This channel is not recommended for production development.
- **RC channel:** these are release candidates based on stable canary builds and are available for download on the[Preview release](https://developer.android.com/studio/preview)page. They are released to get feedback before being integrated into the stable channel.
- **Stable channel:** the official, stable release of[Android Studio](https://developer.android.com/studio).

If you'd like to try one of the preview channels (canary or RC) while still using the stable build for your production projects, you can[install them side by side](https://developer.android.com/studio/preview/install-preview).
![](https://developer.android.com/static/studio/images/preferences-updates_2x.png)

**Figure 2.**The Android Studio Updates preferences.

### Delete unused Android Studio directories

![](https://developer.android.com/static/studio/images/intro/delete-unused-directories-dialog-2x.png)

When you run a major version of Android Studio for the first time, it looks for directories containing caches, settings, indices, and logs for versions of Android Studio for which a corresponding installation can't be found. The**Delete Unused Android Studio Directories**dialog then displays locations, sizes, and last-modified times of these unused directories and provides an option to delete them.

## Update your tools with the SDK Manager

The Android SDK Manager helps you download the SDK tools, platforms, and other components you need to develop your apps. Once downloaded, you can find each package in the directory indicated as the**Android SDK Location**, as shown in figure 3.

To open the SDK Manager from Android Studio, click**Tools \> SDK Manager** or click**SDK Manager** ![](https://developer.android.com/static/studio/images/buttons/toolbar-sdk-manager.png)in the toolbar. If you're not using Android Studio, you can download tools using the[`sdkmanager`](https://developer.android.com/studio/command-line/sdkmanager)command-line tool.

When an update is available for a package you already have, a dash![](https://developer.android.com/static/studio/images/sdk-manager-icon-update_2-0_2x.png)appears in the checkbox next to the package.

- To update an item or install a new one, select the checkbox.
- To uninstall a package, click to clear the checkbox.

Pending updates are indicated in the left column with a download icon![](https://developer.android.com/static/images/tools/studio-sdk-dwnld-icon.png). Pending removals are indicated with a red X:![](https://developer.android.com/static/images/tools/studio-sdk-removal-icon.png).

To update the selected packages, click**Apply** or**OK**and agree to any license agreements.
| **Note:** To install SDK packages from another release channel without changing your IDE's release channel, see the[`sdkmanager`documentation](https://developer.android.com/tools/sdkmanager#usage).
![](https://developer.android.com/static/studio/images/sdk-manager-tools_2x.png)

**Figure 3.**The Android SDK Manager.

### Required packages

You can find the following tools in the**SDK Tools**tab:

**Android SDK Build Tools**
:   Includes tools to build Android apps. For more information, see the[SDK Build Tools release notes](https://developer.android.com/studio/releases/build-tools).

**Android SDK Platform Tools**
:   Includes various tools required by the Android platform, including the[`adb`](https://developer.android.com/studio/command-line/adb)tool.

**Android SDK Command-Line Tools**
:   Includes essential tools such as ProGuard. For more information, see the[SDK Tools release notes](https://developer.android.com/studio/releases/sdk-tools).

**Android SDK Platform**

:   In the**SDK Platforms**tab, you must install at least one version of the Android platform so you can compile your app. Use the latest platform version as your build target to provide the best user experience on the latest devices. To download a version, select the checkbox next to the version name.

    You can still run your app on older versions; however, you must build against the latest version to use new features when running on devices with the latest version of Android.

**Google USB Driver**
:   Required for Windows. Includes tools to help you perform[`adb`](https://developer.android.com/studio/command-line/adb)debugging with Google devices. To install, visit[Get the Google USB Driver](https://developer.android.com/studio/run/win-usb).