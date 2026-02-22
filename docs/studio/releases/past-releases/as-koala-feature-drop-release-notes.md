---
title: https://developer.android.com/studio/releases/past-releases/as-koala-feature-drop-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-koala-feature-drop-release-notes
source: md.txt
---

The following are new features in Android Studio Koala Feature Drop.

## Patch releases

The following is a list of patch releases in Android Studio Koala Feature Drop.

### Android Studio Koala Feature Drop \| 2024.1.2 Patch 1 and AGP 8.6.1 (September 2024)

This version contains minor improvements and [bug
fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2024.1.2#android-studio-koala-feature-drop-%7C-2024.1.2-patch-1).

## Android Device Streaming: more devices and improved sign-up

[Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming) now includes the
following devices, in addition to the portfolio of 20+ device models already
available:

- Samsung Galaxy Fold5
- Samsung Galaxy S23 Ultra
- Google Pixel 8a

Additionally, if you're new to Firebase, Android Studio automatically creates
and sets up a no-cost Firebase project for you when you sign in to Koala Feature
Drop to use Device Streaming. So, you can get to streaming the device you need
much faster.
[Learn more about Android Device Streaming quotas](https://firebase.google.com/docs/test-lab/usage-quotas-pricing#device-streaming),
including promotional quota for the Firebase Blaze plan projects available for a
limited time.

![](https://developer.android.com/static/studio/images/device-streaming-kfd.png)

## USB cable speed detection

Android Studio now detects when it's possible to connect your Android device
with a faster USB cable, and suggests an upgrade that maximizes your device
capabilities. Using an appropriate USB cable optimizes app installation time and
minimizes latency when using tools such as the Android Studio debugger.

The whole USB chain leading to a device is verified. If you see a "Connection
speed warning" notification, check the version certification of the cables but
also any hubs, including the monitor's hub, involved in the USB chain.

USB cable speed detection is available with the following:

- Devices running API level 30 (Android 11) or higher.
- Workstations running macOS or Linux. Windows support is coming soon.
- The latest version of the [SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools).

![](https://developer.android.com/static/studio/images/usb-check.png)

The information provided by Android Studio is similar to the information you can
get using one of the following tools, depending on your OS:

- Mac: running `system_profiler SPUSBDataType` from the terminal
- Linux: running `lsusb -vvv` from the terminal

## Updated sign in flow to Google services

It's now easier to sign in to multiple Google services with one authentication
step. Whether you want to use Gemini in Android Studio, Firebase for Android
Device Streaming, Google Play for Android Vitals reports, or all these useful
services, the new sign in flow makes it easier to get up and running. If you're
new to Firebase and want to use Android Device Streaming, Android Studio
automatically creates a project for you, so you can quickly start streaming a
real physical Firebase device. With granular permissions scoping, you will
always be in control of which services have access to your account. To get
started, click the profile avatar and sign in with your developer account.

![](https://developer.android.com/static/studio/images/sign-in-flow.png)

## Device UI setting shortcuts

To help you build and debug your UI, we have introduced Device UI
setting shortcuts in the **Running Devices** tool window in Android Studio.
Use the shortcuts to view the effect of common UI settings such as dark
theme, font size, screen size, app language and TalkBack. You can use the
shortcuts with emulators, mirrored physical devices, and devices streamed
from Firebase Test Lab.

Note that accessibility settings such as **TalkBack** and **Select to Speak**
only show up if they are already installed on the device. If you don't see
those options, download the Android Accessibility Suite app from the
Play Store.

Device UI setting shortcuts are available for devices running API level 33 or
higher.
![Device UI Setting Shortcuts in Running Device Window](https://developer.android.com/static/studio/preview/features/images/device-ui-settings-shortcut.gif) Device UI Setting Shortcuts in Running Device Window

## Faster and improved Profiler with a task-centric approach

We've improved the performance of the Android Studio Profiler such that popular
profiling tasks like capturing a system trace with profileable apps now
start up to 60% faster.

The Profiler's task-centric redesign also makes it easier to start the task
you're interested in, whether it's profiling your app's CPU, memory, or power
usage. For example, you can start a system trace task to profile and improve
your app's startup time right from the UI as soon as you open the Profiler.

![](https://developer.android.com/static/studio/images/task-based-profiler.png)

## Wear OS tiles preview panel

![Group names in the preview panel match the group name given in the
preview annotation](https://developer.android.com/static/studio/images/design/wear-tiles-preview-panel.png) Tiles preview panel in Android Studio.

By including several dependencies on version 1.4 of the Jetpack Tiles library,
you can
[view snapshots of your Wear OS app's tiles](https://developer.android.com/training/wearables/tiles/preview).
This preview panel is particularly useful if your tile's appearance changes in
response to conditions, such as different content depending on the device's
display size, or a sports event reaching halftime.

## Compose Glance widget previews

Android Studio Koala Feature Drop makes it easy to preview your [Jetpack Compose
Glance widgets](https://developer.android.com/jetpack/compose/glance) directly within the IDE. Catch
potential UI issues and fine-tune your widget's appearance early in the
development process. To get started follow these steps:

1. Add the dependencies.
   1. Add the dependencies to your version catalog:  

      ```transact-sql
          [versions]
          androidx-glance-preview = "1.1.0-rc01"

          [libraries]
          androidx-glance-preview = {
            group = "androidx.glance",
            name = "glance-preview",
            version.ref = "androidx-glance-preview" }
          androidx-glance-appwidget-preview = {
            group = "androidx.glance",
            name = "glance-appwidget-preview",
            version.ref = "androidx-glance-preview" }
          
      ```
   2. Add the dependencies to your app-level `build.gradle.kts` file:  

      ```kotlin
          debugImplementation(libs.androidx.glance.preview)
          debugImplementation(libs.androidx.glance.appwidget.preview)
          
      ```
2. Import the dependencies in the file where you have Glance UI:  

   ```kotlin
       import androidx.glance.preview.ExperimentalGlancePreviewApi
       import androidx.glance.preview.Preview
       
   ```
3. Create a preview of your Glance widget:  

   ```kotlin
     @Composable
     fun MyGlanceContent() {
       GlanceTheme {
         Scaffold(
           backgroundColor = GlanceTheme.colors.widgetBackground,
           titleBar = { ... },
         ) {
             ...
         }
       }
     }

     @OptIn(ExperimentalGlancePreviewApi::class)
     @Preview(widthDp = 172, heightDp = 244)
     @Composable
     fun MyGlancePreview() {
       MyGlanceContent()
     }
     
   ```

## Live Edit for Compose enabled by default and new shortcut

[Live Edit](https://developer.android.com/develop/ui/compose/tooling/iterative-development#live-edit) is now
enabled in manual mode by default. It has increased stability and more robust
change detection, including support for import statements.

Note that starting with Android Studio Koala Feature Drop Beta 1, the default
shortcut to push your changes in manual mode has been updated to
<kbd>Command+'</kbd>. You can still customize it on the **Keymap** settings
page.