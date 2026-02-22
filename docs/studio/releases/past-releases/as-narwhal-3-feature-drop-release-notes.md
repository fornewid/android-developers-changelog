---
title: https://developer.android.com/studio/releases/past-releases/as-narwhal-3-feature-drop-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-narwhal-3-feature-drop-release-notes
source: md.txt
---

# Android Studio Narwhal 3 Feature Drop | 2025.1.3 (September 2025)

The following are new features in Android Studio Narwhal 3 Feature Drop.

## Resizable Compose previews

Compose Preview now supports dynamic resizing to give you instant visual feedback on how your UI adapts to different screen sizes.

To use the feature, enter**Focus**mode in Compose Preview by changing the view option on the toolbar:
![Compose Preview Focus mode](https://developer.android.com/static/studio/preview/features/images/focus-mode.png)Compose Preview Focus mode

You can now resize the preview window by dragging its edges:
Your browser doesn't support the video tag.Resizing the preview window by dragging its edges.

Or, you can use the resize toolbar, which is shown after the preview has been resized:
Your browser doesn't support the video tag.Resizing the preview window using the resize toolbar.

If you want to save the new size as a new`Preview`annotation, use the right-click menu:
![Compose Resizeable Preview save new size](https://developer.android.com/static/studio/preview/features/images/save-new-size.png)Compose Resizeable Preview save new size

The dynamic resize feature helps you create UIs that look great on any screen size.

## Android view setting to display build files under corresponding modules

There is a new setting to display build files under their corresponding module in the Android view. This view can be helpful when you work on projects with many modules. To enable the view open the**Options** ![](https://developer.android.com/static/studio/images/android-view-options.png)menu available next to the Android view. Then select**Appearance \> Display Build Files In Module**.
![Android View: Build Files In Module](https://developer.android.com/static/studio/preview/features/images/build-files-in-module.png)Option to view build files under corresponding modules in Android View.

## Play Policy Insights in Android Studio

Android Studio now includes richer insights and guidance on Google Play policies that may impact your app. This information helps you build safer apps from the start, preventing issues that could disrupt your launch process and cost more time and resources to fix later on.

Starting with Android Studio Narwhal 3 Feature Drop, you can see Play Policy Insights as lint checks. These lint checks will present the following information:

- An overview of the policy.
- Dos and don'ts to avoid common pitfalls.
- Links to Play policy pages where you can find the full formal policy and more helpful information and resources.

This feature is intended to provide helpful pre-review guidance so you can have smoother app submission experiences. It does not cover every policy, nor does it provide final app review decisions. Always review the full policy in the[Policy Center](https://play.google/developer-content-policy/)for guidance. We are also actively evolving and improving this integration. If you have any feedback, please[report it](https://developer.android.com/studio/report-bugs).

To see if there are any Play Policy Insights for your project, go to**Code \> Inspect for Play Policy Insights...**Insights will be listed in the 'Problems' tool window and they will also appear as Lint warnings in the corresponding files.
![Play Policy Insights in Android Studio](https://developer.android.com/static/studio/preview/features/images/play-policy-insights.png)Play Policy Insights in Android Studio Narwhal 3 Feature Drop.

## Test and develop with app backup and restore

Ensuring[Android Backup and Restore](https://developer.android.com/identity/data/testingbackup)works properly for your app is a critical aspect of ensuring users stay engaged with your app after switching to a new device or restoring from the cloud. However, testing whether data backup and restore is working for your app can be difficult.

Android Studio Narwhal 3 Feature Drop provides ways for you to generate a backup for your app and restore it to another device. This can be useful for testing whether your app behaves as expected when restoring app data from device to device or from a cloud backup, or if you want a faster way to set up a test device with data you need to develop and debug your app.

### Generate a backup

To generate a backup file, do the following:

1. Deploy a debug version of your app to a connected device
2. Use one of the following actions to generate a backup:
   - From the**Running Device** window, click the**Backup App Data**action from the toolbar
   - Select**Run \> Backup App Data**from the main menu bar
   - From the**Device Explorer \> Processes** tab, right-click on the app process and select**Backup App Data**
3. In the dialog that appears, do the following:
   - Confirm the application ID for the app you want to generate a backup for
     - Select whether you want to generate a**Device to Device** ,**Cloud** , or**Cloud (Unencrypted)**backup
   - Confirm the name and location of the backup you want to save. By default, the backup is saved to the root directory of the current Android Studio project.![](https://developer.android.com/static/studio/images/run/backuprestore-generate_backup.png)Generate a backup for your app.
4. Click**Ok**when Android Studio asks if it can stop the app. To generate the backup, Android Studio must stop the app process.

You can view the backups that you generate in the**Project \> Android** tool window under the**Backup Files**node.

### Backup types

You can generate different types of backup for your app. When generating a backup, select the backup type that relates to the scenario you want to test:

- **Device-to-device:**Generates a backup of your app, similar to one created during device-to-device transfer. In device-to-device transfers the app's backup data is sent directly to another device, for example over USB or Wi-Fi.
- **Cloud:**Generates a backup of your app, similar to one saved to the user's Google Account storage. When a user sets up a new device, they can choose to restore from a Cloud backup.
- **Cloud (unencrypted):**Generates a backup of your app, similar to one saved to the user's Google Account storage on a device which does not have client side encryption enabled.

**Note** : When using the feature to test**Cloud** ,**Cloud (Unencrypted)** or**Device to Device backups** , the generated backup is not sent to Cloud or to another device, unlike actual backup flow. It generates the backup of your app as if it was going to be saved to Cloud or to be sent to another device. The backups generated for any Backup type can be under**Backup Files** in**Project \> Android**tool window.

### Restore app data

To restore app data, do the following:

1. Deploy your app to the connected device. The app should have the same application ID as the backup file you want to restore onto the device.
2. Navigate to and click one of the following actions:
   - From the**Running Device** window, click the**Restore App Data** action from the toolbar, and either select a backup file from the recent history or click**Browse**.
   - Navigate to**Run \> Restore App Data**from the main menu bar.
   - From the**Device Explorer \> Processes** tab, right-click on the app process and select**Restore App Data**.
   - From the**Project \> Android** tool window, right-click on a backup under the**Backup Files** node and select**Restore App Data**.
3. If applicable, either select a backup from the recent history or click**Browse**to select a backup file to restore from local storage.

Alternatively, you can include a backup file as part of a run configuration, so that deploying your app also restores the app data from a backup file. To do this, do the following:

1. Navigate to**Run \> Edit Configurations**from the main menu bar.
2. Select an app run configuration and navigate to**Restore options** .![](https://developer.android.com/static/studio/images/run/backuprestore-runconfig.png)Restore options in a run configuration.
3. To restore an app from a backup, check the box next to**Restore app state**.
4. Either select a backup file from recent history or browse and select the backup file from local storage.
5. If you only want to restore app data on a fresh app installation, check the box next to**Only restore on fresh apk installation**. This option can be helpful if you are deploying to a new test device and want to restore data to aid in debugging and app development.
6. Click**OK**to save the run configuration.
7. Deploy your app using the run configuration to test restoring your app data to a connected device.

## Proguard inspections

Android Studio now includes inspections to prevent poorly crafted Proguard rules, or rules that prevent R8 optimizations. Overly broad keep rules such as`-keep class **.*`and consumer Proguard rule configurations such as`dontshrink`and`-dontoptimize`trigger a warning now in the Studio IDE. To craft a good keep rule that allows for code shrinking, scope the rule to a specific package and be explicit about what you want to keep.

## AGENTS.md files for project-level context

You can now include`AGENTS.md`files in your project. These are Markdown files that provide project-specific instructions, coding style rules, and other guidance to Gemini as context.

Gemini automatically discovers and applies instructions from any file named`AGENTS.md`in your project. If an`AGENTS.md`file is not present, Gemini instead looks for a`GEMINI.md`file as a fallback.

## New setting to disable Automatic Sync

Android Studio now offers a setting to switch from the default Automatic Sync mode (e.g. Sync runs automatically when a project is opened) to a new Manual Sync mode with reminders. The default behavior is still Automatic Sync. To switch to Manual Sync go to**File** (**Android Studio** on macOS)**\> Settings \> Build, Execution, Deployment \> Build Tools** and set**Project Sync mode** to**Manual Sync with reminders**as the Project Sync mode.
| **Note:** You might not see the setting if you open**Settings**immediately after starting Android Studio and before opening a project. The setting appears once you open a project.

## Image attachment in Gemini

You can now attach image files and provide additional information along with your prompt. For example: you can attach UI mock-ups or screenshots to tell Gemini context about your app's layout. Consequently, Gemini can generate Compose code based on a provided image, or explain the composables and data flow of a UI screenshot. To learn more, see[Attach an image to your query](https://developer.android.com/studio/gemini/attach-image).
![Gemini dialog with Image Attachments](https://developer.android.com/static/studio/gemini/images/image-attachments.png)Image attachment \& preview generation using Gemini in Android Studio

## @File context in Gemini

You can now attach your project files as context in chat interactions with Gemini in Android Studio. This lets you quickly reference files in your prompts for Gemini. In the Gemini chat input, type`@`to bring up a file completion menu and select files to attach. You can also click the**Context** drop-down to see which files were automatically attached by Gemini. This gives you more control over the context sent to Gemini. To learn more, see[Attach a file to your query](https://developer.android.com/studio/gemini/attach-file).
![@File context in Gemini](https://developer.android.com/static/studio/gemini/images/file-context.png)@File context in Gemini