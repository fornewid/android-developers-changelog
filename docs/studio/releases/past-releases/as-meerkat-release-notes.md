---
title: https://developer.android.com/studio/releases/past-releases/as-meerkat-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-meerkat-release-notes
source: md.txt
---

# Android Studio Meerkat | 2024.3.1 (March 2025)

The following are new features in Android Studio Meerkat.

## Compose Preview enhancements

Android Studio Meerkat includes some optimizations of Compose Preview to improve your workflow:

1. **Enhanced zoom**: Enjoy smoother and more responsive zooming in your Compose Previews.
2. **Previews collapsible groups**: Organize your preview surface more effectively! Collapse groups of composables under their titles, reducing clutter and making it easier to focus on specific components.
3. **View modes**: To streamline your preview experience, Grid mode is the default view, Gallery mode is accessed by right-clicking preview, and List view has been removed. This provides a clearer and more organized way to view your composables.

These enhancements make it easier than ever to build and iterate on your Compose UIs.
![Collapsible groups in Compose Previews](https://developer.android.com/static/studio/images/design/preview-grouping.gif)Collapsible groups in Compose Previews.

## KMP Shared Module integration with Android applications

Android Studio now includes a new module template for adding shared logic to your app using Kotlin Multi-Platform (KMP). To try out this feature, follow these steps to create a KMP Shared Module in a newly created Android app:

1. Make sure you're using the latest version of Android Studio Meerkat and that your app uses the latest version of Android Gradle Plugin.
2. Open Android Studio and create a new Android project with the*Empty Activity*template.
3. Switch from the**Android view** to the**Project view**to access the project structure.
4. Click the**New** button in the**Project view** and select*Kotlin Multiplatform Module* from the options. Choose*Shared Module*as the type and keep the default settings.
5. Open the`build.gradle.kts`file in the Android app directory and add a dependency on the shared module.
6. In the shared module, edit the`Platform.android.kt`file and add the following line of code:

       actual fun platform() = "Android from Shared KMP Module"

7. Open the`MainActivity.kt`file in the Android app directory and modify it to call the`platform()`function from the shared module.

8. Build the project and run the Android application. You should see the message, "Hello Android from Shared KMP Module!" displayed on the screen.

These shared modules contain shared business logic that can be used by both Android and iOS platforms.

## Updated UX for adding virtual and remote devices to Device Manager

Android Studio improves the UX when creating a local virtual device or adding a device from[Android Device Streaming](https://developer.android.com/studio/run/android-device-streaming).

To get started, click the**+** button from the Device Manager, and select either**Create Virtual Device** or**Select Remote Devices**.

When creating a new virtual device, new filters and recommendations make it easier to create a device configuration that fits your needs and performs the best on your workstation.
![](https://developer.android.com/static/studio/preview/features/images/configure-avd.png)Identify and select the optimal system image for your virtual device using the UI.

Similarly, when selecting remote devices from Android Device Streaming, new filters make it easier to find and select the devices you need. You now only need to click the Firebase button at the top of the Device Manager window to select the Firebase project you want to use for Android Device Streaming.

## New Gemini in Android Studio features

Android Studio Meerkat introduces new features that use Gemini to help you be more productive. To use these features, enable sharing code context with Gemini in your current project.

Use the following links to learn more about these features:

- [Analyze crash reports](https://developer.android.com/studio/preview/gemini/deploy#crash-reports)
- [Generate unit test scenarios](https://developer.android.com/studio/preview/gemini/deploy#unit-test-gen)

## Updated Build menu and actions

We made the following changes to the build actions and the Build menu to help make it easy to build exactly what you want as you work on projects in Android Studio:

- **Added a new`Build 'run-configuration-name' Run Configuration`action:** This action builds the currently selected run configuration. For example, if you have the`:app`run configuration selected, the action will build and assemble`app`. If you have recently run a test on a device the action will build those tests.
- **Made`Build 'run-configuration-name' Run Configuration`the default Build action:** To better match developer's intent, both the toolbar button and the shortcut<kbd>Control/Command+F9</kbd>now execute the new`Build
  run-configuration-name Run Configuration`action.
- **Reordered build actions:** We placed the new`Build run-configuration-name`action at the top of the Build menu, next the Compile actions, and next the "Assemble ..." actions (previous "Make ..." actions). We also renamed the "Rebuild Project" action to "Clean and Assemble Project with Tests" to more clearly reflect what the action does.
- **Used verbs that match what the build actions actually do:** In addition to "Build" and "Compile" actions, we renamed`Make Project`to`Assemble Project`. We also introduced a new`Assemble Project with Tests`action to assemble test components as well.

## Google Play SDK Insights: Deprecated SDK warnings

SDK authors can now indicate when an[SDK has been deprecated](https://support.google.com/googleplay/android-developer/answer/15321477)and mention alternative SDKs to use instead. If any of the SDKs used by your app have been deprecated by their authors, you'll see corresponding warnings in Android Studio along with information about other SDKs that can be used instead.