---
title: Update the IDE and SDK tools  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/intro/update
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [IDE guides](https://developer.android.com/studio/intro)

# Update the IDE and SDK tools Stay organized with collections Save and categorize content based on your preferences.





Once you install Android Studio, you can keep the Android Studio IDE
and Android SDK tools up to date with automatic updates
and the Android SDK Manager.

## Update your IDE using JetBrains Toolbox

If you installed Android Studio using
[JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/), then
Toolbox is responsible for handling updates to Android Studio. Toolbox lets you install canary,
RC, and stable versions of Android Studio in parallel. It also lets you roll back to earlier
versions of each, if required. When an update is available it displays in Toolbox, as
shown in figure 1.

![Jetbrains Toolbox showing updcates available](/static/studio/images/jetbrains-toolbox_2x.png)

**Figure 1.** Jetbrains Toolbox showing available updates.

## Update your IDE and change channels

If you installed Android Studio manually, Android Studio notifies you with a small bubble
dialog when an update is available for the IDE. To manually check for updates,
click **File** >**Settings** >**Appearance & Behavior** >
**System Settings** > **Updates**
(on macOS, **Android Studio** > **Check for Updates**). See figure 2.

Updates for Android Studio are available from the following
release channels:

* **Canary channel:** these bleeding-edge
  releases are updated roughly weekly and are available for download on the
  [Preview release](/studio/preview) page.

  In addition to receiving canary versions of Android Studio, you also receive preview
  versions of other SDK tools, including the Android Emulator.

  Although these builds are subject to more
  bugs, they do get tested and are available so you can try new
  features and provide feedback.

  **Note:** This channel is not recommended for
  production development.
* **RC channel:** these are release candidates based on stable canary builds
  and are available for download on the [Preview release](/studio/preview) page.
  They are released to get feedback before being integrated into the stable channel.
* **Stable channel:** the official, stable release of
  [Android Studio](/studio).

If you'd like to try one of the preview channels (canary or RC)
while still using the stable build for your production projects, you
can [install them side by side](/studio/preview/install-preview).

![](/static/studio/images/preferences-updates_2x.png)

**Figure 2.** The Android Studio Updates
preferences.

### Delete unused Android Studio directories

![](/static/studio/images/intro/delete-unused-directories-dialog-2x.png)

When you run a major version of Android Studio for the first time, it looks for directories
containing caches, settings, indices, and logs for versions of Android Studio for which a
corresponding installation can't be found. The **Delete Unused Android Studio
Directories** dialog then displays locations, sizes, and last-modified times of these unused
directories and provides an option to delete them.

## Update your tools with the SDK Manager

The Android SDK Manager helps you download the SDK tools, platforms, and
other components you need to develop your apps. Once downloaded, you can find
each package in the directory indicated as the **Android SDK Location**,
as shown in figure 3.

To open the SDK Manager from Android Studio, click **Tools >
SDK Manager** or click **SDK Manager**
![](/static/studio/images/buttons/toolbar-sdk-manager.png)
in the toolbar. If you're not using Android Studio, you can download tools
using the [`sdkmanager`](/studio/command-line/sdkmanager) command-line tool.

When an update is available for a package you already have, a dash
![](/static/studio/images/sdk-manager-icon-update_2-0_2x.png) appears in the checkbox next to the package.

* To update an item or install a new one, select the checkbox.
* To uninstall a package, click to clear the checkbox.

Pending updates are indicated in the left column with a download icon
![](/static/images/tools/studio-sdk-dwnld-icon.png). Pending removals are
indicated with a red X: ![](/static/images/tools/studio-sdk-removal-icon.png).

To update the selected packages,
click **Apply** or **OK** and agree to any
license agreements.

**Note:** To install SDK packages from another release channel without changing your IDE's
release channel, see the
[`sdkmanager` documentation](/tools/sdkmanager#usage).
![](/static/studio/images/sdk-manager-tools_2x.png)

**Figure 3.** The Android SDK Manager.

### Required packages

You can find the following tools in the **SDK Tools** tab:

**Android SDK Build Tools**
:   Includes tools to build Android apps.
    For more information, see the
    [SDK Build Tools release notes](/studio/releases/build-tools).

**Android SDK Platform Tools**
:   Includes various tools required by the
    Android platform, including the [`adb`](/studio/command-line/adb) tool.

**Android SDK Command-Line Tools**
:   Includes essential tools such as ProGuard. For more information, see
    the [SDK Tools release notes](/studio/releases/sdk-tools).

    **Android SDK Platform**
    :   In the **SDK Platforms** tab, you must install at least one version of the Android
        platform so you can compile your app. Use the latest platform version as your build target to
        provide the best user experience on the latest devices. To download a version, select the checkbox next
        to the version name.

        You can still run your app on older versions; however, you must build against the latest
        version to use new features when running on devices with the latest version of
        Android.

    **Google USB Driver**
    :   Required for Windows. Includes tools to help you perform
        [`adb`](/studio/command-line/adb) debugging with Google devices. To install, visit
        [Get the Google USB Driver](/studio/run/win-usb).

### Recommended packages

The following tools are recommended for development:

**Android Emulator**
:   A QEMU-based device-emulation tool that you can use to debug
    and test your applications in an actual Android runtime environment. For more details, see
    the [Emulator release notes](/studio/releases/emulator).

**Note:** Most API libraries that were previously provided by the
**Support Repository** packages (such as the Android Support Library, Constraint Layout,
Google Play services, and Firebase) are now available from Google's Maven repository.
Projects created with Android Studio 3.0 and higher automatically include this repository in the
build configuration. If you're using an older project, you must manually [add Google's Maven repository](/studio/build/dependencies#google-maven) to your
`build.gradle` or `build.gradle.kts` file.

**Intel** or **ARM System Images**
:   The system image is required to run the [Android Emulator](/tools/devices/emulator). Each platform version
    contains the supported system images. You can also download system images later
    when creating Android Virtual Devices (AVDs) in the [AVD Manager](/studio/run/managing-avds). Select either Intel
    or ARM based on your development computer's processor.

Google Play services
:   Includes a set of libraries, Javadocs, and samples to help build your app. If you want to use
    APIs from [Google Play services](https://developers.google.com/android/), you must use either the Google APIs system
    image or the Google play system image.

The preceding list is not comprehensive, and you can add other sites to download additional packages
from third parties, as described in the following section.

In some cases, an SDK package might require a specific minimum revision of
another tool. If so, the SDK Manager notifies you with a warning and adds
the dependencies to your list of downloads.

### Edit or add SDK tool sites

Under the **SDK Update Sites** tab, you can add and manage other sites that host their own tools,
and then download the packages from those sites. Android Studio checks for Android tools and
third-party tool updates from the SDK sites you add.

For example, a mobile carrier or device manufacturer might offer additional
API libraries that are supported by their own Android-powered devices. To
develop using their libraries, you can install their Android SDK package
by adding their SDK tools URL to the **SDK Manager** in the
**SDK Update Sites** tab.

If a carrier or device manufacturer has hosted an SDK add-on repository file
on their website, follow these steps to add the site to the Android SDK
Manager:

1. Click the **SDK Update Sites** tab.
2. Click **Add**
   ![](/static/studio/images/buttons/ic_plus.png) at the
   top of the window.
3. Enter the name and URL of the third-party site, then
   click **OK**.
4. Make sure the checkbox is selected in the **Enabled**
   column.
5. Click **Apply** or **OK**.

Any SDK packages available from the site now appear
in the **SDK Platforms** or **SDK Tools** tabs,
as appropriate.

### Auto-download missing packages with Gradle

When you run a build [from the
command line](/studio/build/building-cmdline) or Android Studio, Gradle can automatically download
missing SDK packages that a project depends on, as long as the corresponding SDK license
agreements have already been accepted in the **SDK Manager**.

When you accept the license agreements using the SDK Manager, Android Studio
creates a licenses directory inside the SDK home directory. This licenses directory
is necessary for Gradle to auto-download missing packages.

If you have accepted the license agreements on one workstation but want to
build your projects on a different one, you can export your licenses by
copying over the accepted licenses directory.

To copy the licenses to another
machine, follow these steps:

1. On a machine with Android Studio installed, click **Tools >
   SDK Manager**. At the top of the window, note the **Android
   SDK Location**.
2. Navigate to that directory and locate the `licenses/` directory
   inside it.

   If you don't see a `licenses/` directory, return to
   Android Studio, update your SDK tools, and accept the license
   agreements. When you return to the Android SDK home directory, you should
   see the directory.
3. Copy the entire `licenses/` directory and paste it into the
   Android SDK home directory on the machine where you want to build your
   projects.

Gradle can now automatically download missing packages your
project depends on.

Note that this feature is automatically disabled for builds you run from
Android Studio, as the SDK manager handles downloading missing packages for
the IDE. To manually disable this feature, set
`android.builder.sdkDownload=false` in the
`gradle.properties` file for your project.

## Update your tools with the command line

On systems that don't have a graphical UI, such as CI servers, you can't use
the SDK Manager in Android Studio. Instead, use the
[`sdkmanager`](/studio/command-line/sdkmanager) command-line tool
to [install](/studio/command-line/sdkmanager#install)
and [update](/studio/command-line/sdkmanager#update-all) SDK tools and platforms.

After installing SDK tools and platforms using `sdkmanager`, you might need to accept
any missing licenses. This can also be done using `sdkmanager`:

```
$ sdkmanager --licenses
```

This command scans all of the installed SDK tools and platforms and displays any licenses that have
not been accepted. You are prompted to accept each license.