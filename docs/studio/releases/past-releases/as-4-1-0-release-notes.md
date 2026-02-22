---
title: https://developer.android.com/studio/releases/past-releases/as-4-1-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-4-1-0-release-notes
source: md.txt
---

# Android Studio 4.1 (August 2020)

<br />

Android Studio 4.1 is a major release that includes a variety of new features
and improvements.

<br />

<br />

**4.1.3 (March 2021)**


This minor update includes various bug fixes.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2021/03/android-studio-413-available.html).

**4.1.2 (January 2021)**

<br />

    <p>
      This minor update includes various bug fixes.
      To see a list of notable bug fixes, read the related post on the
      <a href="https://androidstudio.googleblog.com/2021/01/android-studio-412-available.html">
        Release Updates blog</a>.
    </p>
    <p><b>4.1.1 (November 2020)</b></p>

    <p>
      This minor update includes various bug fixes.
      To see a list of notable bug fixes, read the related post on the
      <a href="https://androidstudio.googleblog.com/2020/11/android-studio-411-available.html">
        Release Updates blog</a>.
    </p>

<br />

<br />

<br />

## New Database Inspector

<br />

<br />

Inspect, query, and modify your databases in your running app using the new
**Database Inspector** . To get started, deploy your app to a device running
API Level 26 or higher, and select **View \>
Tool Windows \> Database Inspector**
from the menu bar.

![](https://developer.android.com/static/studio/images/inspect/database-inspector.gif)

To learn more, see [Debug your database with the Database Inspector](https://developer.android.com/studio/inspect/database).

<br />

<br />

## Run the Android Emulator directly in Android Studio

<br />

<br />

You can now run the Android Emulator directly in Android Studio. Use this
feature to conserve screen real estate, to navigate quickly between the emulator
and the editor window using hotkeys, and to organize your IDE and emulator
workflow in a single application window.

<br />

![The emulator launching in a tool window in Android Studio.](https://developer.android.com/static/studio/images/releases/emulator-tool-window.gif)

<br />

To learn more, see the
[Android Emulator documentation](https://developer.android.com/studio/run/advanced-emulator-usage#standalone-window).

<br />

<br />

## Use TensorFlow Lite models

<br />

<br />

ML Model Binding makes it easy for you to directly import `.tflite` model
files and use them in your projects. Android Studio generates easy-to-use
classes so you can run your model with less code and better type safety.

<br />

<br />

### Supported models

<br />

<br />

The current implementation of ML Model Binding supports image
classification and style transfer models, provided they are enhanced with
metadata. Over time, support will be expanded to other problem domains, like
object detection, image segmentation, and text classification.

<br />

<br />

A wide range of pre-trained models with metadata are provided on
[TensorFlow Hub](https://tfhub.dev/android-studio/collections/ml-model-binding/1).
You can also add metadata to a TensorFlow Lite model yourself, as is outlined in
[Adding metadata to TensorFlow Lite model](https://www.tensorflow.org/lite/convert/metadata).

<br />

<br />

### Import a model file

<br />

<br />

To import a supported model file, follow these steps:

1. Open the TensorFlow Lite model import dialog in the File menu at **File \> New \> Other \> TensorFlow Lite Model**.
2. Select the `.tflite` model file that you previously downloaded or created.
3. Click **Finish**.

This imports the model file into your project and places it in the `ml/`
folder; if the directory doesn't exist, Android Studio creates it for you.

<br />

![Import a TensorFlow Lite model](https://developer.android.com/static/studio/images/write/import-tf-lite-model.png)

<br />

### View model metadata and usage

<br />

<br />

To see the details for an imported model and get instructions on how to use it
in your app, double-click the model file in your project to open the
model viewer page, which shows the following:

- **Model:** High-level description of the model
- **Tensors:** Description of input and output tensors
- **Sample code:** Example of how to interface with the model in your app

Here is an example using [mobilenet_v1_0.25_160_quantized.tflite](https://tfhub.dev/tensorflow/lite-model/mobilenet_v1_0.25_160_quantized/1/metadata/1):

<br />

<br />

As the example demonstrates, Android Studio creates a class called
`MobilenetV1025160Quantized` for interacting with the model.

If the model does not have [metadata](https://www.tensorflow.org/lite/convert/metadata),
this screen will only provide minimal information.

<br />

<br />

### Known issues and workarounds

<br />

<br />

- Support for TensorFlow Lite models for problem domains other than image classification and style transfer is currently limited. Although import should work fine, some model inputs and/or outputs are represented by [TensorBuffers](https://github.com/tensorflow/tflite-support/blob/master/tensorflow_lite_support/java/src/java/org/tensorflow/lite/support/tensorbuffer/TensorBuffer.java) rather than friendly types. For models without any metadata, all model inputs and outputs will be TensorBuffers.
- Models with Input and Output data types different from `DataType.UINT8` or `DataType.FLOAT32` are not supported.

This feature is still under development, so please [provide feedback or
report bugs](https://issuetracker.google.com/issues/new?component=192708&template=840533).

<br />

<br />

## Native Memory Profiler

<br />

<br />

The Android Studio Memory Profiler now includes a Native Memory Profiler for
apps deployed to physical devices running Android 10 or later. With the Native
Memory Profiler, you can record memory allocations and deallocations
from native code and inspect cumulative statistics about native objects.

![A recording in the Native Memory Profiler](https://developer.android.com/static/studio/images/profile/native_memory_profiler.png)

To learn more about the Native Memory Profiler, see
[Inspect your app's memory usage with Memory Profiler](https://developer.android.com/studio/profile/memory-profiler#native-memory-profiler).

<br />

<br />

### Known issues and workarounds

<br />

<br />

The Native Memory Profiler in Android Studio 4.1 does not work for Android 11
devices. Support for profiling Android 11 devices is currently available in
the [4.2 preview release"](https://developer.android.com/studio/preview).

<br />

<br />

As of the initial 4.1 release, app startup profiling has been disabled. This
option will be enabled in an upcoming release.

<br />

<br />

As a workaround, you can use the
[Perfetto standalone command-line profiler](https://perfetto.dev/docs/quickstart/heap-profiling)
to capture startup profiles.

<br />

<br />

## System Trace UI: Easier selection, new analysis tab, and more frame rendering data

<br />

<br />

The System Trace UI in the Android Studio profiler includes the following
improvements:

<br />

<br />

- **Box selection:** In the **Threads** section, you can now drag your mouse to
  perform a box selection of a rectangular area, which you can zoom into by
  clicking the **Zoom to Selection** ![Profilers zoom to selection button](https://developer.android.com/static/studio/images/buttons/profiler-system-trace-zoom-to-selection.png)
  button on the top right (or use the **M** keyboard shortcut). When you drag
  and drop similar threads next to each other, you can select across multiple
  threads to inspect all of them at once. For example, you may want to
  perform analysis on multiple worker threads.

  ![](https://developer.android.com/static/studio/images/releases/profiler-system-trace-box-selection.gif)
- **Summary tab:** The new **Summary** tab in the **Analysis** panel displays:

  - Aggregate statistics for all occurrences of a specific event, such as an
    occurrence count and min/max duration.

  - Trace event statistics for the selected occurrence.

  - Data about thread state distribution.

  - Longest-running occurrences of the selected trace event.

  ![](https://developer.android.com/static/studio/images/releases/profiler-system-trace-statistics-panel.png)

  To navigate to another occurrence, select another row from the table.
- **Display data:** In the **Display** section, new timelines for
  [SurfaceFlinger](https://source.android.com/devices/graphics/surfaceflinger-windowmanager)
  and [VSYNC](https://source.android.com/devices/graphics/implement-vsync)
  help you investigate rendering issues in your app's UI.

  ![](https://developer.android.com/static/studio/images/releases/profiler-system-trace-summary-panel.png)

For basic usage instructions on how to record a system trace, see the
[Record traces](https://developer.android.com/studio/profile/cpu-profiler#method_traces) section of
[Inspect CPU activity with CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler).

<br />

<br />

| **Windows users:** If labels are missing in the thread
| activity timeline when you profile your app, see the
| [known issues](https://developer.android.com/studio/known-issues#system-trace-labels)
| for a workaround. This issue is fixed in the 4.2 release.

<br />

<br />

## Standalone profilers now available

<br />

<br />

With the new standalone profilers, it's now possible to profile your app without
running the full Android Studio IDE.

<br />

<br />

For instructions on using the standalone profilers, see [Run standalone profilers](https://developer.android.com/studio/profile/android-profiler#standalone-profilers).

<br />

<br />

## Dagger navigation support

<br />

![IDE gutter actions for navigating to Dagger consumers and providers](https://developer.android.com/static/studio/images/releases/dagger-navigation-support.gif)

<br />

Android Studio makes it easier to navigate between your Dagger-related code
by providing new gutter actions and extending support in the **Find Usages**
window.

<br />

<br />

- **New gutter actions:** For projects that use Dagger, the IDE provides gutter
  actions that help you navigate between your Dagger-annotated code. For example,
  clicking on the ![](https://developer.android.com/static/studio/images/buttons/navigate-to-dagger-provider.png)
  gutter action next to a method that consumes a given type navigates you to
  the provider of that type. Conversely, clicking on the ![](https://developer.android.com/static/studio/images/buttons/navigate-to-dagger-code.png)
  gutter action navigates you to where a type is used as a dependency.

- **Find Usages node:** When you invoke **Find Usages** on a provider of a given
  type, the **Find** window now includes a **Dependency consumer(s** node that
  lists consumers of that type. Conversely, invoking this action on a consumer
  of a Dagger-injected dependency, the **Find** window shows you the provider of
  that dependency.

<br />

<br />

## Material Design Components: Updated themes and styles in new project templates

<br />

![Animation: Creating a project in Android Studio with new material design properties.](https://developer.android.com/static/studio/images/releases/material-design-components-template-update.gif)

<br />

Android Studio templates in the **Create New Project** dialog now use
[Material Design Components (MDC)](https://github.com/material-components/material-components-android) and conform to updated
guidance for themes and styles by default. Updates include:

<br />

<br />

- **MDC** : Projects depend on `com.google.android.material:material`
  in `build.gradle`. Base app themes use `Theme.MaterialComponents.*`
  parents and override updated MDC color and "on" attributes.

- **Color resources** : Color resources in `colors.xml` use
  literal names (for example, `purple_500` instead of
  `colorPrimary`).

- **Theme resources** : Theme resources are in `themes.xml`
  (instead of `styles.xml`) and use `Theme.<var>`<var> names.

- **Dark theme** : Base application themes use `DayNight`
  parents and are split between `res/values` and `res/values-night`.

- **Theme attributes** : Color resources are referenced as theme
  attributes (for example, `?attr/colorPrimary`) in layouts and
  styles to avoid hard-coded colors.

<br />

<br />

## IntelliJ IDEA 2020.1

<br />

<br />

The core Android Studio IDE has been updated with improvements from
IntelliJ IDEA through the 2020.1 release, including a new **Commit** window
that enables version control operations and a new Zen mode that can be toggled
by selecting **View \> Appearance \> Enter Distraction Free Mode**.

<br />

<br />

To learn more about the improvements in version 2020.1, see
[IDEA 2020.1](https://blog.jetbrains.com/idea/2020/04/intellij-idea-2020-1-released/).

<br />

<br />

## IDE configuration directory changes

<br />

<br />

The locations of user configuration directories have been changed to the
following:

<br />

<br />

### Windows

Syntax: `%APPDATA%\Google&lt;product><version>`

Example: `C:\Users\YourUserName\AppData\Roaming\Google\AndroidStudio4.1`

<br />

<br />

### macOS

Syntax: `~/Library/Application Support/Google/<product><version>`

Example: `~/Library/Application Support/Google/AndroidStudio4.1`

<br />

<br />

### Linux

Syntax: `~/.config/Google/<product><version>`

Example: `~/.config/Google/AndroidStudio4.1`

<br />

<br />

These new directory locations are consistent with
[recent updates to IntelliJ IDEA](https://www.jetbrains.com/help/idea/tuning-the-ide.html?_ga=2.165019455.1890831646.1588892783-2122726634.1572645395#default-dirs),
the IDE on which Android Studio is based.

<br />

<br />

If Studio doesn't restart after an upgrade, you may need to delete the
configuration directory from a previous Studio version. See the
[known issues](https://developer.android.com/studio/known-issues#studio-config-directories) page
for more information.

<br />

<br />

## Kotlin 1.3.72

<br />

<br />

Android Studio 4.1 bundles Kotlin 1.3.72, which includes a number of fixes
to improve Kotlin highlighting, inspections, and code completion. Check out
the [1.3.72 Kotlin changelog](https://github.com/JetBrains/kotlin/blob/1.3.70/ChangeLog.md#1372) for details.

<br />

<br />

## Custom view preview

<br />

<br />

When creating a custom view (for example, by extending the
[`View`](https://developer.android.com/reference/android/view/View) or
[`Button`](https://developer.android.com/reference/android/widget/Button) class),
Android Studio now shows you a preview of your custom view. Use the dropdown
menu in the toolbar to switch between multiple custom views, or click the
buttons to wrap vertically or horizontally to the content.

<br />

![Preview custom views in the IDE.](https://developer.android.com/static/studio/images/design/custom-view-preview.png)

<br />

**Note:** If you don't see your changes in the preview,
select **Build \> Make Project** from the menu bar.

<br />

<br />

## Symbolication for native crash reports

<br />

<br />

When a crash or ANR occurs in native code, the system produces a stack trace,
which is a snapshot of the sequence of nested functions called in your program
up to the moment it crashed. These snapshots can help you to identify and fix
any problems in the source, but they must first be symbolicated to translate the
machine addresses back into human-readable function names.

<br />

<br />

If your app or game is developed using native code, like C++, you can now upload
debug symbols files to the Play Console for each version of your app. The Play
Console uses these debug symbols files to symbolicate your app's stack traces,
making it easier to analyze crashes and ANRs. To learn how to upload debug
symbols files, see [Native crash
support](https://developer.android.com/studio/build/shrink-code#native-crash-support).

<br />

<br />

## Apply Changes

<br />

<br />

To help you be more productive as you iterate on your app, we've made the
following enhancements to Apply Changes for devices running
Android 11 Developer Preview 3 or higher:

<br />

<br />

### Faster deploy speeds

<br />

<br />

We've invested heavily in optimizing your iteration speed by developing a method
to deploy and persist changes on a device without installing the application.
After an initial deploy, subsequent deploys to Android 11 devices
using either **Apply Code Changes**
![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.svg) or **Apply Changes and Restart Activity**
![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.svg) are now significantly faster.

<br />

<br />

To learn more about the difference between these two actions, see
[Apply Changes](https://developer.android.com/studio/run#apply-changes).

<br />

<br />

### Support for additional code changes

<br />

<br />

For devices running Android 11 Developer Preview 3 or higher, you
can now add methods and then deploy those changes to your running app by
clicking either **Apply Code Changes**
![Apply Code Changes icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-code-changes.svg) or **Apply Changes and Restart Activity**
![Apply Changes and Restart Activity icon](https://developer.android.com/static/studio/images/buttons/toolbar-apply-changes.svg).

<br />