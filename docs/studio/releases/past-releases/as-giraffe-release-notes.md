---
title: https://developer.android.com/studio/releases/past-releases/as-giraffe-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-giraffe-release-notes
source: md.txt
---

# Android Studio Giraffe | 2022.3.1 (July 2023)

The following are new features in Android Studio Giraffe.

## Use Live Edit to update composables in real time

Live Edit lets you update composables in emulators and physical devices in real time. Edit composables and see the UI changes on the running device without re-deploying your app. This capability minimizes context switches between writing and building your app, letting you focus on writing code longer without interruption. To try Live Edit, use AGP 8.1 or higher and Compose 1.3.0 or higher.

To learn more, see the[Live Edit documentation](https://developer.android.com/studio/run#live-edit).

## New UI preview

Android Studio Giraffe introduces support for the[new UI theme](https://www.jetbrains.com/help/idea/new-ui.html)from IntelliJ. To opt in to this option, go to**Android Studio \> Settings \> Appearance \& Behavior**.

![](https://developer.android.com/static/studio/images/new-ui-theme.png)

The redesigned theme aims to reduce visual complexity, provide easier access to essential features, and disclose complex features as needed --- resulting in a modern, cleaner look and feel. The key changes are:

- Simplified main toolbar with new**VCS** ,**Project** , and**Run**widgets
- Tool windows have a new layout
- New Light and Dark color themes with improved contrast and consistent color palettes
- New icon set for improved legibility

For a full list of changes, see the[IntelliJ new UI documentation](https://www.jetbrains.com/help/idea/new-ui.html).

If you'd like to provide feedback on the new UI in Android Studio,[file a bug](https://issuetracker.google.com/issues/new?component=192708&template=1777729).

## New API support for Compose Animation Preview

[Compose Animation Preview](https://developer.android.com/develop/ui/compose/tooling/animation-preview)now also supports[`animate*AsState`](https://developer.android.com/jetpack/compose/animation#animate-as-state),[`CrossFade`](https://developer.android.com/jetpack/compose/animation#crossfade),[`rememberInfiniteTransition`](https://developer.android.com/jetpack/compose/animation#rememberinfinitetransition), and[`AnimatedContent`](https://developer.android.com/jetpack/compose/animation#animatedcontent)(in addition to[`updateTransition`](https://developer.android.com/jetpack/compose/animation#updateTransition)and[`AnimatedVisibility`](https://developer.android.com/jetpack/compose/animation#animatedvisibility)). To use these additional APIs with Compose Animation Preview, upgrade to Android Studio Giraffe Canary 3 and Compose 1.4.0-alpha04 or higher.
![](https://developer.android.com/static/studio/images/compose-animation-preview-picker.gif)

## Support for Grammatical Inflection API

Android Studio Giraffe Canary 7 introduces support for the[Grammatical Inflection API](https://developer.android.com/about/versions/14/features#grammatical-inflection)(available as of Android 14 Developer Preview 1).

This new feature lets you personalize the UI for your users by adding translations inflected based on your user's grammatical gender when required. You can add grammatically masculine, feminine, or neutral translations. When no grammatically inflected translation is provided for a string, Android displays the default translation for the language.

## View and manage processes in the Device Explorer

Android Studio Giraffe includes an updated Device Explorer, known as the Device File Explorer in previous versions of Android Studio. In the Device Explorer, files and related actions are located in the**Files** tab. In the new**Processes** tab, view a list of debuggable processes for the connected device. From there you can also select a process and perform a kill![](https://developer.android.com/static/studio/images/device-explorer-kill.png), force-stop![](https://developer.android.com/static/studio/images/device-explorer-force-stop.png), or attach the debugger to a given process![](https://developer.android.com/static/studio/images/device-explorer-attach-debugger.png).
| **Note:** The options to kill, force-stop, or attach the debugger to a process have moved from Logcat to the Device Explorer.
![](https://developer.android.com/static/studio/images/device-explorer.png)

## New Android SDK Upgrade Assistant

Starting with Android Studio Giraffe, see the steps required to upgrade the[`targetSdkVersion`](https://developer.android.com/guide/topics/manifest/uses-sdk-element#target), or the API level that your app targets, directly in the Studio IDE. The Android SDK Upgrade Assistant pulls documentation directly into its tool window, so you don't have to jump back and forth between your browser and the IDE.

The Android SDK Upgrade Assistant helps you save time and effort when updating the`targetSdkVersion`:

- For each migration step, it highlights the major breaking changes and how to address them.
- It filters the full list of changes to only show steps relevant to your app.

| **Important:** Starting August 31, 2023, all apps must target Android 12 (API level 33) or higher to be submitted to Google Play for review and remain discoverable for all Google Play users. Configuring your app to target a recent API level ensures that users benefit from security and performance improvements while your app can still run on lower Android versions (down to the specified`minSdkVersion`). To learn more, see the[Google Play target API level requirement](https://developer.android.com/google/play/requirements/target-sdk).

To open the Android SDK Upgrade Assistant, go to**Tools \> Android SDK Upgrade Assistant** . In the**Assistant** panel, select the API level that you want to upgrade to for guidance. For the best experience, you should upgrade`targetSdkVersion`values one level at a time.

To help us create the best experience for you,[submit feedback and bugs](https://issuetracker.google.com/issues/new?component=1267157&template=1750462).

![](https://developer.android.com/static/studio/images/sdk-upgrade-assistant.png)

## Enhanced diagnostic tools and bug reporting

Android Studio Giraffe Canary 8 introduces new diagnostic tools that make it easier to report bugs with relevant log files attached. To use the new diagnostic report generator, follow these steps:

1. To launch the tool, click**Help \> Collect Logs and Diagnostic Data**. A dialog appears that lets you choose which files to include.
2. Check or un-check specific files to include in your diagnostic report. Click a specific file in the menu to see a preview of it.
3. When you're ready to export the diagnostic report, agree to the terms and click**Create**.
4. Select the location where you want to save the diagnostic report zip file and click**Save**.

As part of this enhancement, the bug reporting template (**Help \> Submit feedback**) has also been updated to emphasize the importance of attaching log files. If you file a bug, be sure to attach logs because they help us isolate the issue and are an essential first step to our debugging process.

## Make selected modules toolbar button

Starting with Android Studio Giraffe Canary 10, build only the current module you're working on by selecting the**Make Selected Modules** ![](https://developer.android.com/static/studio/images/buttons/toolbar-make-module.png)build option in the toolbar. This new option lets you check that the code you just wrote compiles without building more than needed. Alternatively, build your entire project by clicking the arrow next to the build button and selecting**Make Project**.

## Download info during sync

The**Sync**tool window now includes a summary of time spent downloading dependencies and a detailed view of downloads per repository. This view updates live as sync takes place. You can use this information to determine whether unexpected dependency downloads are negatively impacting your sync performance. Since Gradle resolves dependencies by searching through each repository in the declared order, it's important to list the repository that hosts most dependencies at the top of the repository configuration list. Additionally, if you see a high number of failed requests for a specific repository, it could indicate that the repository should be removed or moved lower in your repository configuration.
| **Note:** Download information is only available if your project uses Gradle version 7.3 or higher.

![Download info during sync.](https://developer.android.com/static/studio/images/download-info-sync.png)

This download info is also available during builds in the**Build** tool window and[Build Analyzer](https://developer.android.com/studio/build/build-analyzer#download-impact).