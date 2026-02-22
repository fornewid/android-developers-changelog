---
title: https://developer.android.com/studio/releases/past-releases/as-4-2-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-4-2-0-release-notes
source: md.txt
---

<br />

# Android Studio 4.2 (April 2021)

Android Studio 4.2 is a major release that includes a variety of new features
and improvements.  
**4.2.2 (June 2021)**

This minor update includes various bug fixes. To see a list of notable
bug fixes, read the related post on the
[Release
Updates blog](https://androidstudio.googleblog.com/2021/06/android-studio-422-available.html).

**4.2.1 (May 2021)**

This minor update bundles Kotlin plugin 1.5.0 and includes various bug
fixes. To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2021/05/android-studio-421-available.html).

<br />

<br />

## Android Gradle plugin 4.2.0

The latest version of the Android Gradle plugin includes many updates. To learn
more, read the [full Android Gradle plugin release notes](https://developer.android.com/studio/releases/gradle-plugin#4-2-0).

### Gradle compatibility and configuration changes

When running in Android Studio, the Gradle build tool uses Studio's bundled JDK.
In previous releases, JDK 8 was bundled with Studio. In 4.2,
however, JDK 11 is now bundled instead. When using the new bundled JDK to run
Gradle, this may result in some incompatibility or impact JVM performance
due to changes to the garbage collector. These issues are described in the
[AGP release notes](https://developer.android.com/studio/releases/gradle-plugin#4.2-bundled-jdk-11).

### Option to optimize Gradle sync time

To improve Gradle Sync performance, Android Studio skips building the task list
during sync. This allows Gradle Sync to complete faster and improves UI
responsiveness for very large projects. This option is on by default in Android
Studio 4.2. To turn it off, go to
**File \> Settings \> Experimental** (**Preferences \> Experimental** on a Mac) and
uncheck **Do not build Gradle task list during Gradle sync**.

<br />

<br />

## Database Inspector

<br />

<br />

### Query editor improvements

The [Database Inspector](https://developer.android.com/r/studio-ui/db-inspector-help) includes some
improvements to help you write and execute your custom SQL statements. When
you open the inspector and open a **New query** tab, you should notice a
larger, resizable editor surface to author and format your queries, as
shown below.

![DB Inspector editor](https://developer.android.com/static/studio/images/releases/db-inspector-query-editor.png)

Additionally, we now provide a history of your previous queries. When you click on the
**Show query history** ![Show query history button](https://developer.android.com/static/studio/images/buttons/db-inspector-query-history.png){: .inline-icon}
button, you should see a list of queries you previously ran against the currently
selected database. Click a query in the list to see a preview of the full
query in the editor and press **Enter** to copy it to the editor. Then,
click **Run** to execute the statement.

![Run command in query editor](https://developer.android.com/static/studio/images/releases/db-inspector-run-command.png)

### Offline mode

In previous versions of Android Studio, disconnecting from an app process while
using the Database Inspector resulted in closing the inspector and its data.
In Android Studio 4.2, we've added the ability to keep
inspecting your app's databases after a process disconnects, making it easier
to debug your app after a crash.

When a disconnect occurs, the Database Inspector downloads your databases and
then makes them available to you in offline mode. When offline, you can open
tables and run queries.

Keep in mind, when you reconnect to a live app process, the Database Inspector
returns to live mode and shows you only the data that is on the device. That is,
data shown in offline mode doesn't persist when you reconnect to an app process.
Because of this, the Database Inspector does not allow editing or running
modification statements while in offline mode.

<br />

<br />

## Upgrade Assistant for AGP

A new Upgrade Assistant for Android
Gradle plugin can help you update the AGP version for your project.

![Android Gradle plugin Upgrade Assistant dialog](https://developer.android.com/static/studio/images/releases/agp-upgrade-assistant-dialog.png)

Built on top of the existing AGP upgrade functionality, this tool guides you
through project-wide updates/refactorings and includes a preview of the
updates to help prevent potential breaking changes before executing the AGP
upgrade.

![Preview of changes to be performed by Upgrade Assistant](https://developer.android.com/static/studio/images/releases/agp-upgrade-assistant-preview.png)

<br />

<br />

## System Trace: Improved metrics for memory and graphics

In the CPU profiler, the [System Trace](https://developer.android.com/studio/profile/cpu-profiler#system-trace)
feature now includes new metrics for analyzing app performance and includes
the following:

- **Events Table.** Lists all
  trace events in the currently selected thread.

- **BufferQueue.** In the Display
  section, this new track shows the buffer count of the app's surface
  [BufferQueue](https://source.android.com/devices/graphics#bufferqueue) (0, 1,
  or 2) to help you understand the state of image buffers as they move
  between the Android graphics components.

  ![System Trace Buffer Queue](https://developer.android.com/static/studio/images/releases/system-trace-buffer-queue.png)
- **CPU Frequency.** In the CPU
  cores section, this new track displays CPU frequency by core, indicating how
  hard each core is working.

  ![System Trace CPU Frequency](https://developer.android.com/static/studio/images/releases/system-trace-cpu-frequency.png)
- **Process Memory (RSS).**
  This new window shows the amount of physical memory
  currently in use by the app.

  ![System Trace Process Memory (RSS)](https://developer.android.com/static/studio/images/releases/system-trace-process-memory.png)

For more details, see [Inspect CPU activity with CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler#system-trace).

<br />

<br />

## New Layout Inspector refresh action

Introduced in Android Studio 4.0, the Layout Inspector was designed for
real-time inspection of your running app's UI stack.
However, you might not always want the Layout Inspector
to immediately reflect what's happening in your app, since you might want to
inspect a snapshot of your app's layout at a specific point in time or
minimize the performance impact of live updates on your app.

To manually load a snapshot of UI data from your app, first disable the
**Live updates** option. You can then click the **Refresh** ![](https://developer.android.com/static/studio/images/buttons/live-layout-refresh-icon.png){:.inline-icon}
button to take a new snapshot of the UI stack for inspection. The Layout
Inspector now remembers your preference to keep **Live updates** enabled or
disabled between sessions.

<br />

<br />

## Support for Safe Args

[Safe Args](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args) is a Gradle
plugin that generates simple object and builder classes
for type-safe navigation and access to any associated arguments. Android
Studio now includes richer support when working with Safe
Args, as described below:

- Autocompletions for Directions, Args, and the various builder classes
- Support for both Java and Kotlin safe args plugins
- Navigation from source to XML

<br />

<br />

## R8 retrace now available in command-line tools

Available in version 4.0 of the command-line tools, R8 retrace
is a standalone tool for obtaining the original stack trace from an obfuscated
stack trace.

You can download this package with the SDK manager, which installs
R8 retrace in android_sdk/cmdline-tools.
Alternatively, you can
[download the standalone command-line tools package](https://developer.android.com/studio#command-tools).

For usage information, see
[R8 retrace](https://developer.android.com/studio/command-line/retrace) in the user guide.

<br />

<br />

## Deploy to multiple devices

To help streamline app testing across devices and API levels, you can now
deploy your app to multiple devices or emulators simultaneously by following
these steps:

1. Choose **Select Multiple Devices** in the target device dropdown menu (in the top-center of the IDE).

   ![Target device dropdown](https://developer.android.com/static/studio/images/releases/instrumentation-dropdown-select-multiple-devices.png)
2. Select the target devices and click **OK** .

   ![Modify device set dialog](https://developer.android.com/static/studio/images/releases/instrumentation-dialog-select-multiple-devices.png)
3. Run your app.

| **Note:** Running and viewing tests across multiple devices is an experimental feature. When running a test configuration across multiple devices, you might be prompted to enable this feature before you can proceed.

<br />

<br />

## New `removable` setting for feature modules

Android Gradle plugin 4.2 uses `bundletool` 1.0.0, which introduces a behavior
change for apps using feature modules: Any feature module specified as
`dist:install-time` that's not explicitly marked as `dist:removable` will
become non-removable by default. This new setting optimizes fusing of
install-time modules with the base module, potentially improving app
performance for some apps.

To keep feature modules removable, set `dist:removable="true"` on any module
you want to uninstall.

For more information on this new setting, see the documentation for the
`dist:removable` tag in the documentation for
[feature module manifest](https://developer.android.com/guide/app-bundle/play-feature-delivery#feature-module-manifest).

<br />

<br />

## Apply Changes

To help you be more productive as you iterate on your app, we've made the
following enhancements to Apply Changes for devices running Android 11 or higher:

<br />

<br />

### Support for additional code changes

For devices running Android 11 or higher, you can now add static
final primitive fields and then deploy those changes to your running app by
clicking either **Apply Code Changes**
![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.svg)
or **Apply Changes and Restart Activity**
![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.svg).

You can now also add resources and then deploy those changes to your running app
on Android 11 devices by clicking **Apply Changes and Restart
Activity**
![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.svg).

<br />

<br />

## Updated New Project and New Module wizards

The **New Project** and **New Module** wizards have been updated to make it
easier to browse, select a template, and input information about the new
project or module.

![](https://developer.android.com/static/studio/images/releases/new-project-wizard.png)

![](https://developer.android.com/static/studio/images/releases/new-module-wizard.png)

The option to **Import .JAR/.AAR Package** from the **New Module** wizard has
also been removed. To import a JAR or AAR into your project,
[use the Project Structure Dialog](https://developer.android.com/studio/projects/android-library#psd-add-library-dependency)
instead.

<br />

<br />

## Kotlin 1.4.31

Android Studio 4.2 bundles Kotlin 1.4.31. Check out
the [Kotlin 1.4.0 changelog](https://github.com/JetBrains/kotlin/releases/tag/v1.4.0)
to review the major changes.

<br />

<br />

## `ANDROID_SDK_HOME` environment variable deprecated

The `ANDROID_SDK_HOME` environment variable is deprecated and has been
replaced with `ANDROID_PREFS_ROOT`. For more information, see
[Emulator Environment Variables](https://developer.android.com/studio/command-line/variables#android-sdk-home).

<br />

<br />

## Known Issues with Android Studio 4.2

This section describes known issues that exist in Android Studio 4.2. For a
complete list, go to the [Known issues](https://developer.android.com/studio/known-issues) page.

<br />

<br />

### Android Studio 4.2.0 generates projects with wrong Kotlin version: "1.5.0-release-764"

If you are using Android Studio 4.2.0 and have upgraded to Kotlin plugin 1.5.0,
then new Kotlin projects created by Studio will fail to build due to the
following Gradle sync error:  

    Could not find org.jetbrains.kotlin:kotlin-gradle-plugin:1.5.0-release-764.

As a workaround, replace `1.5.0-release-764` with `1.5.0`
in the project's `build.gradle` files.

<br />

### Error when using different passwords for key and keystore

Starting with version 4.2, Android Studio now runs on JDK 11. This update
causes an underlying behavior change related to signing keys.

When you navigate to **Build \> Generate Signed Bundle / APK**
and attempt to configure app signing for an app bundle or an APK,
entering different passwords for the key and keystore may result in the
following error:  

    Key was created with errors:
    Warning: Different store and Key passwords not supported for PKCS12 Key stores

To work around this issue, enter the same password for both the key and
keystore.

<br />

<br />

### Android Studio doesn't start after installing version 4.2

Studio tries to import previous
*.vmoptions* and sanitize them to work with the garbage collector used by
JDK 11. If that process fails, the IDE may not start for certain users who
set custom VM options in the *.vmoptions* file.

To work around this issue, we recommend commenting out custom options
in *.vmoptions* (using the `#` character). The *.vmoptions* file can be
found in the following locations:

**Windows**

`C:\Users\YourUserName\AppData\<var>[Local|Roaming]</var>\Google\AndroidStudio4.2\studio64.exe.vmoptions`

**macOS**

`~/Library/Application Support/Google/AndroidStudio4.2/studio.vmoptions`

**Linux**

`~/.config/Google/AndroidStudio4.2/studio64.vmoptions`

If Studio still doesn't start after trying this workaround,
see [Studio doesn't start after upgrade](https://developer.android.com/studio/known-issues#studio-config-directories)
below.

<br />