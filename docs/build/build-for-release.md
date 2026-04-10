---
title: https://developer.android.com/build/build-for-release
url: https://developer.android.com/build/build-for-release
source: md.txt
---

> [!NOTE]
> **Note:** Android Studio Meerkat updated the labels and ordering of some Build actions. [Learn more](https://developer.android.com/studio/releases#build-actions-update)


The **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) button builds and deploys your app to a device. However,
to build your app to share or upload to Google Play, you'll need to use one of
the options in the **Build** menu to compile parts or all of your project.
Before you select any of the build options listed in table 1, make sure you
first [select the build variant](https://developer.android.com/studio/run#changing-variant) you
want to use.

**Table 1.** Build options in the **Build** menu.

| Menu Item | Description |
|---|---|
| **Assemble Selected Modules** | Compiles all source files in the selected module that have been modified since the last build, and all modules the selected module depends on recursively. The compilation includes dependent source files and any associated build tasks. You can select the module to build by selecting either the module name or one of its files in the **Project** window. |
| **Assemble Project** | Assembles all modules. |
| **Assemble Project with Tests** | Assembles all modules, including test ones. |
| **Clean Project** | Deletes all intermediate/cached build files. |
| **Clean and Assemble Project with Tests** | Runs **Clean Project** for the selected build variant and then assembles all modules, including test ones. |
| **Generate Bundle(s) / APK(s) \> Generate APK(s)** | Builds an APK of all modules in the current project for their selected variant. When the build completes, a confirmation notification appears, providing a link to the APK file and a link to analyze it in the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer). If the build variant you've selected is a debug build type, then the APK is signed with a debug key and it's ready to install. If you've selected a release variant, then, by default, the APK is unsigned and you must manually [sign the APK](https://developer.android.com/studio/publish/app-signing). Alternatively, you can select **Build \> Generate Signed Bundle / APK** from the menu bar. Android Studio saves the APKs you build in `project-name/module-name/build/outputs/apk/`. |
| **Generate Bundle(s) / APK(s) \> Generate Bundle(s)** | Builds an [Android App Bundle](https://developer.android.com/guide/app-bundle) of all modules in the current project for their selected variant. When the build completes, a confirmation notification appears, providing a link to the app bundle and a link to analyze it in the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer). If the build variant you've selected is a debug build type, then the app bundle is signed with a debug key, and you can [use `bundletool`](https://developer.android.com/studio/command-line/bundletool) to deploy your app from the app bundle to a connected device. If you've selected a release variant, then the app bundle is unsigned by default and you must manually sign it using [`jarsigner`](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jarsigner.html). Alternatively, you can select **Build \> Generate Signed Bundle / APK** from the menu bar. Android Studio saves the APKs you build in `project-name/module-name/build/outputs/bundle/`. |
| **Generate Signed App Bundle or APK** | Brings up a dialog with a wizard to set up a new signing configuration, and build either a signed app bundle or APK. You need to sign your app with a release key before you can upload it to the Play Console. For more information about app signing, see [Sign your app](https://developer.android.com/studio/publish/app-signing). |

**Note:** The **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) button builds an APK with `https://developer.android.com/guide/topics/manifest/application-element#testOnly`,
which means the APK can only be installed via `https://developer.android.com/studio/command-line/adb` (which Android Studio uses). If you want
a debuggable APK that people can install without adb, select your debug variant and click
**Build Bundle(s) / APK(s) \> Build APK(s)**.

For details about the tasks that Gradle executes for each command, open the **Build** window as
described in the next section. For more information about Gradle and the build process, see
[Configure Your Build](https://developer.android.com/studio/build).