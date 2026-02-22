---
title: https://developer.android.com/studio/run
url: https://developer.android.com/studio/run
source: md.txt
---

| **Note:** Android Studio Meerkat updated the labels and ordering of some Build actions. [Learn more](https://developer.android.com/studio/releases#build-actions-update)

To see how your app looks and behaves on a device, you need to build and run it.
Android Studio sets up new projects so that you can deploy your app to a virtual
or a physical device with just a few clicks.

This overview focuses on how to use Android Studio to build and run your app for
testing and debugging. For information on how to use Android Studio to build
your app so that it can be released to users, see [Build your app for release to
users](https://developer.android.com/studio/run/build-for-release). For more detailed information about
managing and customizing your build with or without Android Studio, see
[Configure your build](https://developer.android.com/studio/build).

## Basic build and run

To build and run your app, follow these steps:

1. In the toolbar, select your app from the run configurations menu.
2. In the target device menu, select the device that you want to run your app
   on.

   ![Target device menu.](https://developer.android.com/static/studio/images/run/deploy-run-app-new-ui.png)

   If you don't have any devices configured, you need to either [create an
   Android Virtual Device](https://developer.android.com/studio/run/managing-avds#createavd) to use the
   [Android Emulator](https://developer.android.com/studio/run/emulator) or [connect a physical
   device](https://developer.android.com/studio/run/device#connect).
3. Click **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).

Android Studio warns you if you attempt to launch your project to a device that
has an error or a warning associated with it. Iconography and stylistic changes
differentiate between *errors* (device selections that result in a broken
configuration) and *warnings* (device selections that might result in unexpected
behavior but are still runnable).
| **Note:** Android Studio includes deployment optimizations for incremental changes on Android 11 or later. If you manually clear app data in between incremental changes, some changes may be discarded without warning. This may result in your app running outdated code. If you need to clear app data in between deployments, check the option to "Always install with package manager" in the Run/Debug configuration. That will bypass these deployment optimizations and ensure the latest version of the app code is deployed every time the app is run.

## Monitor the build process


To view details about the build process, select **View \> Tool
Windows \> Build** or click **Build**
![](https://developer.android.com/static/studio/images/buttons/toolbar-build.png) in the tool window bar. The **Build** tool window
displays the
tasks that Gradle executes to build your app, as shown in figure 1.
![](https://developer.android.com/static/studio/images/run/window-build.png) **Figure 1.** The **Build** tool window in Android Studio.

1. **Sync tab:** Displays tasks that Gradle executes to sync with your project files. Similar to the **Build Output** tab, if you encounter a sync error, select elements in the tree to get more information about the error. Also displays a summary of [download impact](https://developer.android.com/build/build-analyzer#download-impact) to determine whether dependency downloads are negatively affecting your build.
2. **Build Output tab:** Displays the tasks that Gradle executes as a tree, where each node represents either a build phase or a group of task dependencies. If you receive build-time or compile-time errors, inspect the tree and select an element to read the error output, as shown in figure 2. ![](https://developer.android.com/static/studio/images/run/build-output-window-error.png) **Figure 2.** Inspect the **Build Output** tab for error messages.
3. **Build Analyzer tab:** Provides build performance analysis information about your build. See [Troubleshoot build performance with
   Build Analyzer](https://developer.android.com/studio/build/build-analyzer) for more information.
4. **Restart:** Performs the last build action again. If you last ran **Build \> Make Selected Module** , it'll build the current module. If you last ran **Build \> Make Project**, it'll generate intermediate build files for all modules in your project.
5. **Filters:** Filters out warnings, tasks, or both that completed successfully. This can make it easier to find issues in the output.


If your build variants use product flavors, Gradle also invokes tasks to
build those product flavors. To view the list of all available build tasks,
click **View \> Tool Windows \> Gradle** or click **Gradle**
![](https://developer.android.com/static/studio/images/buttons/toolbar-gradle.png) in the tool window bar.


If an error occurs during the build process, Gradle may recommend
command-line options to help you resolve the issue, such as
`--stacktrace` or `--debug`. To use command-line options
with your build process:

1. Open the **Settings** or **Preferences** dialog:
   - On Windows or Linux, select **File** \> **Settings** from the menu bar.
   - On macOS, select **Android Studio** \> **Preferences** from the menu bar.
2. Navigate to **Build, Execution, Deployment** \> **Compiler**.
3. In the text field next to **Command-line Options**, enter your command-line options.
4. Click **OK** to save and exit.


Gradle applies these command-line options the next time you try building
your app.

## Build and run using the AI agent

The AI agent in Android Studio has access to tools that let it build and deploy
your app, and then verify the app's state on your behalf.
When you use [Agent Mode](https://developer.android.com/studio/gemini/agent-mode), the agent can perform
tasks such as:

- **Deploy your app** to a connected physical device or emulator.
- **Inspect the screen** and take screenshots to verify UI changes.
- **Check Logcat** for runtime errors or specific log messages.
- **Interact with your app** using `adb shell` commands to navigate or enter data.

Using the AI agent to build and run your app is useful for multi-stage
tasks where the agent needs to iteratively make changes and verify that they
work as expected.
![Device interaction tools in Android Studio.](https://developer.android.com/static/studio/preview/features/images/device-interaction-tools.gif) **Figure 3:** The AI agent can help you test and verify changes on a device.

## Advanced build and run features

The default way to build and run your app in Android Studio should be sufficient
to test a simple app. However, you can use these build and run features for more
advanced use cases:

- To deploy your app in debug mode, click **Debug**
  ![](https://developer.android.com/static/studio/images/buttons/toolbar-debug.png).
  Running your app in debug mode lets you set breakpoints in your code, examine
  variables and evaluate expressions at run-time, and run debugging tools. To
  learn more, see [Debug your app](https://developer.android.com/studio/debug).

- If you have a larger, more complex app, use Apply Changes instead of
  clicking **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png). This saves time, because you avoid restarting
  your app every time you want to deploy a change. For more information about
  Apply Changes, see the [Deploy incrementally with Apply
  Changes](https://developer.android.com/studio/run#apply-changes) section.

- If you're using Jetpack Compose, Live Edit is an experimental feature that
  lets you update composables in real time without re-clicking
  **Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png).
  This lets you focus on writing UI code with minimal interruption. For more
  information, see the [Live Edit (experimental)](https://developer.android.com/studio/run#live-edit) section.

- If you have an app with multiple build variants or versions, you can choose
  which build variant to deploy by using the **Build Variants** tool window.
  For more information about running a specific build variant, see the [Change
  the build variant](https://developer.android.com/studio/run#changing-variant) section.

- To fine-tune app installation, launch, and test options, you can change the
  run/debug configuration. For more information about creating custom
  run/debug configurations, see the [Create run/debug
  configurations](https://developer.android.com/studio/run#run-configuration) section.

- We recommend that you use Android Studio for your development needs, but you
  can also deploy your app to a virtual or physical device from the command
  line. For more information, see [Build your app from the command
  line](https://developer.android.com/studio/build/building-cmdline).

### Deploy incrementally with Apply Changes

In Android Studio 3.5 and higher, Apply Changes lets you push code and resource
changes to your running app without restarting your app---and, in some
cases, without restarting the current activity. This flexibility helps you
control how much of your app is restarted when you want to deploy and test
small, incremental changes while preserving your device's current state.

Apply Changes uses [capabilities in the Android JVMTI
implementation](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html#bci)
that are supported on devices running Android 8.0 (API level 26) or higher. To
learn more about how Apply Changes works, see [Android Studio Project Marble:
Apply
Changes](https://medium.com/androiddevelopers/android-studio-project-marble-apply-changes-e3048662e8cd).

#### Requirements

Apply Changes actions are only available when you meet the following conditions:

- You build the APK of your app using a debug build variant.
- You deploy your app to a target device or emulator that runs Android 8.0 (API level 26) or higher.

#### Use Apply Changes

Use the following options when you want to deploy your changes to a compatible
device:

**Apply Changes and Restart Activity** ![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.png): Attempts
to apply both your resource and code changes by restarting your activity but
without restarting your app. Generally, you can use this option when you've
modified code in the body of a method or modified an existing resource.

You can also perform this action by pressing
<kbd>Control</kbd>+<kbd>Alt</kbd>+<kbd>F10</kbd>
(<kbd>Control</kbd>+<kbd>Command</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd> on macOS).

**Apply Code Changes** ![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.png) : Attempts to apply only
your code changes without restarting anything. Generally, you can use this
option when you've modified code in the body of a method but you haven't
modified any resources. If you've modified both code and resources, use
**Apply Changes and Restart Activity** instead.

You can also perform this action by pressing <kbd>Control</kbd>+<kbd>F10</kbd>
(<kbd>Control</kbd>+<kbd>Command</kbd>+<kbd>R</kbd> on macOS).

**Run** ![](https://developer.android.com/static/studio/images/buttons/toolbar-run.png): Deploys all changes and restarts the app. Use this
option when the changes you've made can't be applied using either of the Apply
Changes options. To learn more about the types of changes that require an app
restart, see the [Limitations of Apply Changes](https://developer.android.com/studio/run#apply-changes-limitations)
section.

#### Enable run fallback for Apply Changes

When you click either **Apply Changes and Restart Activity** or
**Apply Code Changes** , Android Studio builds a new APK and determines whether
the changes can be applied. If the changes can't be applied and would cause
Apply Changes to fail, Android Studio prompts you to **Run** ![Run icon](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) your app again instead.

If you don't want to be prompted every time this occurs, you can configure
Android Studio to automatically rerun your app when changes can't be applied. To
enable this behavior, follow these steps:

1. Open the **Settings** or **Preferences** dialog:

   - On Windows or Linux, select **File \> Settings** from the menu.
   - On macOS, select **Android Studio \> Preferences** from the menu.
2. Navigate to **Build, Execution, Deployment \> Deployment**.

3. Select the checkboxes to enable automatic run fallback for either or both of
   the Apply Changes actions.

4. Click **OK**.

| **Note:** Some types of changes don't cause Apply Changes to fail but still require you to restart your app manually before you can see those changes. For example, if you make changes to an activity's [`onCreate()`](https://developer.android.com/reference/android/app/Activity#onCreate(android.os.Bundle)) method, those changes only take effect after the activity is relaunched, so you must restart your app to see those changes.

#### Platform-dependent changes

Some features of Apply Changes depend on specific versions of the Android
platform. To apply these kinds of changes, your app must be deployed to a device
running that version of Android (or higher). For example, adding a method
requires Android 11 or higher.

#### Limitations of Apply Changes

Apply Changes is designed to speed up the app deployment process. However, there
are some limitations on when it can be used.

##### Code changes that require app restart

Some code and resource changes can't be applied until the app is restarted,
including the following:

- Adding or removing a field
- Removing a method
- Changing method signatures
- Changing modifiers of methods or classes
- Changing class inheritance
- Changing values in enums
- Adding or removing a resource
- Changing the app manifest
- Changing native libraries (SO files)

##### Libraries and plugins

Some libraries and plugins automatically make changes to your app's manifest
files or to resources that are referenced in the manifest. These automatic
updates can interfere with Apply Changes in the following ways:

- If a library or plugin makes changes to your app's manifest, you can't use Apply Changes. You must restart your app to see your changes.
- If a library or plugin makes changes to your app's resource files, you can't use **Apply Code Changes** ![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.png). You must use **Apply
  Changes and Restart Activity** ![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.png) (or restart your app) to see your changes.

To avoid these limitations, disable all automatic updates for your debug build
variants.

For example, [Firebase
Crashlytics](https://firebase.google.com/products/crashlytics) updates app
resources with a unique build ID during every build, which prevents you from
using **Apply Code Changes** ![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.png)
and requires you to restart your app's activity to see your changes. Disable
this behavior to use **Apply Code Changes** alongside Crashlytics with your
debug builds.

##### Code that directly references content in an installed APK

If your code directly references content from your app's APK that's installed on
the device, that code can cause crashes or misbehave after clicking **Apply Code
Changes** ![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.png). This behavior occurs
because when you click **Apply Code Changes** the underlying APK on the device
is replaced during installation. In these cases, you can click **Apply Changes
and Restart Activity** ![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.png)
or **Run** ![Run icon](https://developer.android.com/static/studio/images/buttons/toolbar-run.png) instead.

If you encounter any other issues while using Apply Changes, [file a
bug](https://issuetracker.google.com/issues/new?component=192708).

### Live Edit

Live Edit is an experimental feature in the Android Studio that lets you update
composables in emulators and physical devices in real time. This functionality
minimizes context switches between writing and building your app, letting you
focus on writing code longer without interruption.

[Learn more about Live
Edit](https://developer.android.com/jetpack/compose/tooling/iterative-development#live-edit)

### Change the build variant

By default, Android Studio builds the debug version of your app, which is
intended for use only during development, when you click **Run** ![UI
button](https://developer.android.com/static/studio/images/buttons/toolbar-run-darkmode.png).

To change the build variant Android Studio uses, do one of the following:

- Select **Build** \> **Select Build Variant** in the menu.
- Select **View** \> **Tool Windows** \> **Build Variants** in the menu.
- Click the **Build Variants** tab on the tool window bar.

For projects without native/C++ code, the **Build Variants** panel has two
columns: **Module** and **Active Build Variant** . The **Active Build Variant**
value for the module determines which build variant the IDE deploys to your
connected device and is visible in the editor.

![](https://developer.android.com/static/studio/images/run/build-variants.png)

**Figure 9.** The **Build
Variants** panel has two columns for projects that don't have native/C++
code.

<br />

To switch between variants, click the **Active Build Variant** cell for a module
and choose the desired variant from the list.

For projects with native/C++ code, the **Build Variants** panel has three
columns:

- **Module**
- **Active Build Variant**
- **Active ABI**

The **Active Build Variant** value for the module determines the build variant
that the IDE deploys to your device and is visible in the editor. For native
modules, the **Active ABI** value determines the [ABI](https://developer.android.com/ndk/guides/abis) that
the editor uses, but doesn't impact what is deployed.

![](https://developer.android.com/static/studio/images/run/build-variants-ndk.png)

**Figure 10.** The **Build
Variants** panel adds the **Active ABI** column for
projects with native/C++ code.

<br />

To change the build variant or ABI, click the cell for the
**Active Build Variant** or **Active ABI** column and choose the desired variant
or ABI from the list. After you change the selection, the IDE syncs your project
automatically. Changing either column for an app or library module applies the
change to all dependent rows.

By default, new projects are set up with two build variants: a debug variant and
release variant. You need to build the release variant to [prepare your app for
public release](https://developer.android.com/studio/publish/preparing). To define other variations of your
app with different features or device requirements, you can [define additional
build variants](https://developer.android.com/studio/build/build-variants).

#### Conflicts in Android Studio Build Variants dialog

In the Android Studio **Build Variants** dialog, you might see error messages
indicating conflicts between build variants, such as the following:

![Build Variant window displaying variant conflict errors](https://developer.android.com/static/studio/images/run/build-variant-conflict.png)

This error doesn't indicate a build issue with Gradle. It indicates that the
Android Studio IDE can't resolve symbols between the variants of the selected
modules.

For example, if you have a module `M1` that depends on variant `v1` of module
`M2`, but `M2` has variant `v2` selected in the IDE, you have unresolved symbols
in the IDE. Suppose `M1` depends on a class that is only available in `v1`; when
`v2` is selected, that class is not known by the IDE. Therefore it fails to
resolve the class name and shows errors in the `M1` module's code.

These error messages appear because the IDE can't load code for multiple
variants simultaneously. In terms of your app's build, however, the variant
selected in this dialog has no effect, because Gradle builds your app with the
source code specified in your Gradle build recipes, not based on what's
currently loaded in the IDE.

### Change the run/debug configuration

When you run your app for the first time, Android Studio uses a default run
configuration. The run configuration specifies whether to deploy your app from
an APK or an [Android App Bundle](https://developer.android.com/guide/app-bundle) as well as the module to
run, package to deploy, activity to start, target device, emulator settings,
Logcat options, and more.

The default run/debug configuration builds an APK, launches the default project
activity, and uses the **Select Deployment Target** dialog for target device
selection. If the default settings don't suit your project or module, you can
customize the run/debug configuration or create a new one at the project,
default, and module levels.

To edit a run/debug configuration, select **Run \> Edit Configurations** . For
more information, see [Create and edit run/debug
configurations](https://developer.android.com/studio/run/rundebugconfig).