---
title: https://developer.android.com/studio/releases/past-releases/as-3-6-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-3-6-0-release-notes
source: md.txt
---

<br />

# Android Studio 3.6 (February 2020)

Android Studio 3.6 is a major release that includes a variety of new features
and improvements.

<br />

<br />

We'd also like to thank all of our [community contributors](https://developer.android.com/studio/releases/past-releases/as-3-6-0-release-notes#3-6-community-contributors) who have helped with this release.

<br />

<br />

**3.6.3 (April 2020)**


This minor update includes various bug fixes.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2020/04/android-studio-363-available.html).

**3.6.2 (March 2020)**


This minor update includes various bug fixes.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2020/03/android-studio-362-available.html).

**3.6.1 (February 2020)**


This minor update includes various bug fixes.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2020/02/android-studio-361-available.html).

<br />

<br />

## Design tools

<br />

<br />

This version of Android Studio includes updates to several design tools,
including the Layout Editor and Resource Manager.

<br />

<br />

### Split view and zoom in design editors

<br />

![split view shows both the design and text views at the same time](https://developer.android.com/static/studio/images/releases/split-view.png)

<br />

The following updates to the visual design editors are included in this
release:

<br />

<br />

- Design editors, such as the Layout Editor and Navigation Editor, now
  provide a **Split** view that enables you to see both the **Design**
  and **Code** views of your UI at the same time. In the top-right corner
  of the editor window, there are now three buttons
  ![view icons](https://developer.android.com/static/studio/images/buttons/view-icons.png)
  for toggling between viewing options:

  - To enable split view, click the **Split** icon ![split view icon](https://developer.android.com/static/studio/images/buttons/split-view-icon.png).
  - To enable XML source view, click the **Source** icon ![source view icon](https://developer.android.com/static/studio/images/buttons/source-view-icon.png).
  - To enable design view, click the **Design** icon ![design view icon](https://developer.android.com/static/studio/images/buttons/design-view-icon.png).
- The controls for zooming and panning within design editors have moved
  to a floating panel in the bottom-right corner of the editor window.

<br />

<br />

To learn more, see [Build a UI with Layout Editor](https://developer.android.com/studio/write/layout-editor).

<br />

<br />

### Color Picker Resource Tab

<br />

<br />

To help you quickly update color resource values in your app when you're using
the color picker in your XML or the design tools, the IDE now populates
color resource values for you.

<br />

![Color picker with populated color values](https://developer.android.com/static/studio/images/releases/color-picker-resource-tab.png)

<br />

### Resource Manager

<br />

<br />

The Resource Manager contains the following updates:

<br />

<br />

- The Resource Manager now supports most resource types.
- When searching for a resource, the Resource Manager now displays results from all project modules. Previously, searches returned results only from the selected module.
- The filter button lets you view resources from local dependent modules, external libraries, and the Android framework. You can also use the filter to show theme attributes.
- You can now rename resources during the import process by clicking within the textbox above the resource.

<br />

<br />

To learn more, see
[Manage your app's UI resources with Resource Manager](https://developer.android.com/studio/write/resource-manager).

<br />

<br />

## Updates to the Android Gradle plugin

<br />

<br />

The latest version of the Android Gradle plugin includes many updates,
including optimizations for build speed, support for the Maven publishing
plugin, and support for View Binding. To learn more, read the
[full release notes](https://developer.android.com/studio/releases/gradle-plugin#3-6-0).

<br />

<br />

### View binding

<br />

<br />

[View binding](https://developer.android.com/topic/libraries/view-binding) allows you to more
easily write code that interacts with views by generating a binding class for each XML
layout file. These classes contain direct references to all views that have an
ID in the corresponding layout.

<br />

<br />

Because it replaces `findViewById()`, view binding eliminates
the risk of null pointer exceptions resulting from an invalid view ID.

<br />

<br />

To enable view binding, you need to use Android Gradle plugin
3.6.0 or higher and include the following in each module's
`build.gradle` file:

<br />

<br />

### Groovy

```groovy
  android {
      buildFeatures.viewBinding = true
  }
  
```

### Kotlin

```kotlin
  android {
      buildFeatures.viewBinding = true
  }
  
```

<br />

<br />

## Apply Changes

<br />

<br />

You can now add a class and then deploy that code change to your running app by
clicking either **Apply Code Changes**
or **Apply Changes and Restart Activity** .

<br />

<br />

To learn more about the difference between these two actions, see
[Apply Changes](https://developer.android.com/studio/run#apply-changes).

<br />

<br />

## Refactor menu option to enable Instant Apps support

<br />

<br />

You can now instant-enable your base module at any time after creating your app
project as follows:

<br />

<br />

1. Open the **Project** panel by selecting **View \> Tool Windows \> Project** from the menu bar.
2. Right-click on your base module, typically named 'app', and select **Refactor \> Enable Instant Apps Support**.
3. In the dialog that appears, select your base module from the dropdown menu.
4. Click **OK**.

<br />

<br />

**Note:** The option to instant-enable your base app module
from the **Create New Project** wizard has been removed.

<br />

<br />

To learn more, read
[Overview of Google Play Instant](https://developer.android.com/topic/google-play-instant/overview).

<br />

<br />

## Deobfuscate class and method bytecode in APK Analyzer

<br />

<br />

When using the [APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer) to
inspect DEX files, you can deobfuscate class and method bytecode as follows:

<br />

<br />

1. Select **Build \> Analyze APK** from the menu bar.
2. In the dialog that appears, navigate to the APK you want to inspect and select it.
3. Click **Open**.
4. In the APK Analyzer, select the DEX file you want to inspect.
5. In the DEX file viewer, [load the ProGuard mappings
   file](https://developer.android.com/studio/debug/apk-analyzer#load_proguard_mappings) for the APK you're analyzing.
6. Right-click on the class or method you want to inspect and select **Show bytecode**.

<br />

<br />

## Native tooling

<br />

<br />

The following updates support native (C/C++) development in Android Studio.

<br />

<br />

### Kotlin support

<br />

<br />

The following NDK features in Android Studio, previously supported in Java, are
now also supported in Kotlin:

<br />

<br />

- Navigate from a JNI declaration to the corresponding implementation function
  in C/C++. View this mapping by hovering over the C or C++ item marker near
  the line number in the managed source code file.

- Automatically create a stub implementation function for a JNI declaration.
  Define the JNI declaration first and then type "jni" or the method name in
  the C/C++ file to activate.

  ![](https://developer.android.com/static/studio/preview/features/images/jni-autocomplete.gif)
- Unused native implementation functions are highlighted as a warning in the
  source code. JNI declarations with missing implementations are also
  highlighted as an error.

- When you rename (refactor) a native implementation function, all
  corresponding JNI declarations are updated. Rename a JNI declaration to
  update the native implementation function.

- Signature checking for implicitly-bound JNI implementations.

<br />

<br />

### Other JNI improvements

<br />

<br />

The code editor in Android Studio now supports a more seamless JNI development
workflow, including improved type hints, auto-completion, inspections, and
code refactoring.

<br />

<br />

### APK reloading for native libraries {:#3.6-reload-apk}

<br />

<br />

You no longer need to create a new project when the APK in your project is
updated outside the IDE. Android Studio detects changes in the APK and gives you
the option to re-import it.

<br />

![](https://developer.android.com/static/studio/images/debug/import-updated-apk.png)

<br />

## Attach Kotlin-only APK sources

<br />

<br />

It is now possible to attach Kotlin-only external APK sources when you profile
and debug pre-built APKs. To learn more, see
[Attach Kotlin/Java sources](https://developer.android.com/studio/debug/apk-debugger#attach_java).

<br />

<br />

## Leak detection in Memory Profiler

<br />

<br />

When analyzing a heap dump in the Memory Profiler, you can now filter profiling
data that Android Studio thinks might indicate memory leaks for `Activity` and
`Fragment` instances in your app.

<br />

<br />

The types of data that the filter shows include the following:

<br />

<br />

- `Activity` instances that have been destroyed but are still being referenced.
- `Fragment` instances that do not have a valid `FragmentManager` but are still being referenced.

<br />

<br />

### Attach Kotlin-only APK sources

<br />

<br />

It is now possible to attach Kotlin-only external APK sources when you profile
and debug pre-built APKs. To learn more, see
[Attach Kotlin/Java sources](https://developer.android.com/studio/debug/apk-debugger#attach_java).

<br />

<br />

### Leak detection in Memory Profiler

<br />

<br />

When analyzing a heap dump in the Memory Profiler, you can now filter profiling
data that Android Studio thinks might indicate memory leaks for `Activity` and
`Fragment` instances in your app.

<br />

<br />

The types of data that the filter shows include the following:

<br />

<br />

- `Activity` instances that have been destroyed but are still being referenced.
- `Fragment` instances that do not have a valid `FragmentManager` but are still being referenced.

<br />

<br />

In certain situations, such as the following, the filter might yield false
positives:

<br />

<br />

- A `Fragment` is created but has not yet been used.
- A `Fragment` is being cached but not as part of a `FragmentTransaction`.

<br />

<br />

To use this feature, first
[capture a heap dump](https://developer.android.com/studio/profile/memory-profiler#capture-heap-dump)
or [import a heap dump file](https://developer.android.com/studio/profile/memory-profiler#import-hprof)
into Android Studio. To display the fragments and activities that may
be leaking memory, select the **Activity/Fragment Leaks** checkbox in the heap
dump pane of the Memory Profiler.

<br />

![Profiler: Memory Leak Detection](https://developer.android.com/static/studio/images/profile/profiler-memory-leak-detection.png)

Filtering a heap dump for memory leaks.

<br />

<br />

## Emulators

<br />

<br />

Android Studio 3.6 helps you take advantage of several updates included in
Android Emulator 29.2.7 and higher, as described below.

<br />

<br />

### Improved Location Support

<br />

<br />

Android Emulator 29.2.7 and higher provides additional support for emulating
GPS coordinates and route information. When you open the Emulators
[Extended controls](https://developer.android.com/studio/run/advanced-emulator-usage#extended),
options in the Location tab are now organized under two tabs:
**Single points** and **Routes**.

<br />

<br />

#### Single points

<br />

<br />

In the **Single points** tab, you can use the Google Maps webview to search for
points of interest, just as you would when using Google Maps on a phone or
browser. When you search for or click on a location in the map, you can save
the location by selecting Save point near the bottom of the map. All of your
saved locations are listed on the right side of the **Extended controls**
window.

<br />

<br />

To set the Emulators location to the location you have selected on the map,
click the **Set location** button near the bottom right of the
**Extended controls** window.

<br />

![Single Points tab in Emulator Extended Controls.](https://developer.android.com/static/studio/images/run/emulator-single-points.png).

<br />

#### Routes

<br />

<br />

Similar to the **Single points** tab, the **Routes** tab provides a Google
Maps webview that you can use to create a route between two or more locations.
To create and save a route, do the following:

<br />

<br />

1. In the map view, use the text field to search for the first destination in your route.
2. Select the location from the search results.
3. Select the **Navigate** button.
4. Select the starting point of your route from the map.
5. (Optional) Click **Add destination** to add additional stops to your route.
6. Save your route by clicking **Save route** in the map view.
7. Specify a name for the route and click **Save**.

<br />

<br />

To simulate the Emulator following the route you saved, select the route from
the list of **Saved routes** and click **Play route** near the bottom right of
the **Extended controls** window. To stop the simulation, click **Stop route**.

<br />

![Routes tab in Emulator Extended Controls.](https://developer.android.com/static/studio/images/run/emulator-routes.png).

<br />

To continuously simulate the Emulator following the specified route, enable the
switch next to **Repeat playback** . To change how quickly the Emulator follows
the specified route, select an option from the **Playback speed** dropdown.

<br />

<br />

### Multi-display support

<br />

<br />

The Android Emulator now allows you to deploy your app to multiple displays,
which support customizable dimensions and can help you test apps that support
[multi-window](https://developer.android.com/guide/topics/ui/foldables#multi-window) and [multi-display](https://developer.android.com/guide/topics/ui/foldables#multi-display). While a virtual device is running,
you can add up to two additional displays as follows:

<br />

<br />

1. Open the
   [**Extended controls**](https://developer.android.com/studio/run/advanced-emulator-usage#extended)
   and navigate to the **Displays** tab.

2. Add another display by clicking **Add secondary display**.

3. From the dropdown menu under **Secondary displays**, do one of the following:

4. Select one of the preset aspect ratios

5. Select **custom** and set the **height** , **width** , and **dpi** for your
   custom display.

6. (Optional) Click **Add secondary display** to add a third display.

7. Click **Apply changes** to add the specified display(s) to the running
   virtual device.

<br />

![Add multiple displays Emulator Extended Controls Display tab.](https://developer.android.com/static/studio/images/run/emulator-multi-display.png)

<br />

### New virtual devices and project templates for Android Automotive OS

<br />

<br />

When you create a new project using Android Studio, you can now select from
three templates from the **Automotive** tab in the **Create New Project**
wizard: **No Activity** , **Media service** , and **Messaging service** . For
existing projects, you can add support for Android Automotive devices by
selecting **File \> New \> New Module** from the menu bar, and selecting
**Automotive Module** . The **Create New Module** wizard then guides you
through creating a new module using one of the Android Automotive project
templates.

<br />

![Selecting an Android Automotive project template.](https://developer.android.com/static/studio/images/run/auto-select-project-template.png).

<br />

Additionally, you can now
[create an Android Virtual Device (AVD)](https://developer.android.com/studio/run/managing-avds#createavd)
for Android Automotive OS devices by selecting one of the following options
in the **Automotive** tab in the **Virtual Device Configuration** wizard.

<br />

<br />

1. **Polestar 2**: Create an AVD that emulates the Polestar 2 head unit.
2. **Automotive (1024p landscape)**: Create an AVD for generic 1024 x 768 px Android Automotive head units.

<br />

![Selecting an Android Automotive virtual device.](https://developer.android.com/static/studio/images/run/auto-select-hardware.png).

<br />

## Resumable SDK downloads

<br />

<br />

When downloading SDK components and tools using the SDK Manager, Android Studio
now allows you to resume downloads that were interrupted (for example, due to a
network issue) instead of restarting the download from the beginning. This
enhancement is especially helpful for large downloads, such as the Android
Emulator or system images, when internet connectivity is unreliable.

<br />

<br />

In addition, if you have an SDK download task running in the background, you can
now pause or resume the download using the controls in the status bar.

<br />

![A background download task in the status bar with new controls that
let you pause or resume the download.](https://developer.android.com/static/studio/preview/features/images/background-download-controls.png)

A background download task in the status bar with new
controls that let you pause or resume the download.

<br />

<br />

## Win32 deprecated

<br />

<br />

The Windows 32-bit version of Android Studio will no longer receive updates
after December 2019, and it will no longer receive support after December 2020.
You can continue to use Android Studio. However, to receive additional updates,
upgrade your workstation to a 64-bit version of Windows.

<br />

<br />

To learn more, read the [Windows 32-bit depreciation blog](https://android-developers.googleblog.com/2019/06/moving-android-studio-and-android.html)

<br />

<br />

## New option for optimizing Gradle sync time

<br />

<br />

In previous releases, Android Studio retrieved the list of all Gradle tasks
during Gradle Sync. For large projects, retrieving the task list could cause
slow sync times.

<br />

<br />

To improve Gradle Sync performance, go to **File \> Settings \> Experimental**
and select Do not build Gradle task list during Gradle sync.

<br />

<br />

When you enable this option, Android Studio skips building the task list during
sync, which allows Gradle Sync to complete faster and improves UI
responsiveness. Keep in mind, when the IDE skips building the task list, the
task lists in the Gradle panel are empty, and task name auto-completion in
build files does not work.

<br />

<br />

## New location to toggle Gradle's offline mode

<br />

<br />

To enable or disable Gradle's offline mode, first select
**View \> Tool Windows \> Gradle** from the menu bar. Then, near the top of
the **Gradle** window, click **Toggle Offline Mode**
![Gradle offline button in the Gradle panel.](https://developer.android.com/static/studio/images/buttons/gradle-offline.png).

<br />

<br />

## IntelliJ IDEA 2019.2

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the [2019.2 release](https://blog.jetbrains.com/idea/2019/07/intellij-idea-2019-2-java-13-preview-features-profiling-tools-services-tool-window-and-more/).

<br />

<br />

To learn more about the improvements from other IntelliJ versions that are
included cumulatively with version 2019.2, see the following pages:

<br />

<br />

- [IntelliJ IDEA 2019.1.3](https://blog.jetbrains.com/idea/2019/05/intellij-idea-2019-1-3-is-here/)
- [IntelliJ IDEA 2019.1.2](https://blog.jetbrains.com/idea/2019/05/intellij-idea-2019-1-2-is-here/)
- [IntelliJ IDEA 2019.1.1](https://blog.jetbrains.com/idea/2019/04/intellij-idea-2019-1-1-is-here/)

<br />

<br />

## Community contributors

<br />

<br />

Thank you to all of our community contributors who have helped us discover bugs
and other ways to improve Android Studio 3.6. In particular, we'd like to thank
the following people who reported bugs:

<br />

<br />

|---|---|---|
| - [Albert Lo](https://stackoverflow.com/users/923920/phileo99) - [Alexey Rott](https://github.com/desmondfox) - Andrea Leganza - [Benedikt Kolb](https://github.com/Bennik2000) - César Puerta - [Curtis Kroetsch](https://github.com/cckroets) - [Damian Wieczorek](https://github.com/damianw/) - [Dan Lew](https://github.com/dlew) - [David Burström](https://stackoverflow.com/users/643007/david-burstr%c3%b6m) - Deepanshu - Egor Andreevici - Eli Graber - [Emin Kokalari](https://stackoverflow.com/users/3636806/eak-team) - [Evan Tatarka](https://www.github.com/evant) - Frantisek Nagy - [Greg Moens](https://stackoverflow.com/users/10630172/greg-moens) - [Hannes Achleitner](https://stackoverflow.com/users/1079990/hannes-ach) - [Hans Petter Eide](https://github.com/hanspeide) - [Henning Bunk](https://github.com/henningBunk) - [Hugo Visser](https://twitter.com/botteaap) - [Igor Escodro](https://github.com/igorescodro) | - [Iñaki Villar](https://github.com/cdsap/) - [Javentira Lienata](https://github.com/hugosvent) - [Joe Rogers](https://github.com/joerogers) - [Kristoffer Danielsson](https://stackoverflow.com/users/419761/l33t) - [Liran Barsisa](https://github.com/AndroidDeveloperLB) - [Louis CAD](https://github.com/LouisCAD) - [Lóránt Pintér](https://github.com/lptr) - [Łukasz Wasylkowski](https://github.com/lwasyl) - Luke Fielke - Malvin Sutanto - [Masatoshi Kubode](https://github.com/kubode) - Mathew Winters - [Michael Bailey](https://stackoverflow.com/users/1686989/yogurtearl) - Michał Górny - [Mihai Neacsu](https://stackoverflow.com/users/2607246/mike-n) - [Mike Scamell](https://github.com/mikescamell) - [Monte Creasor](https://github.com/MonteCreasor) - [Nelson Osacky](https://github.com/runningcode/) - [Nelson Osacky](https://osacky.com/) - [Nick Firmani](https://github.com/nickfirmani) - [Nicklas Ansman Giertz](https://github.com/ansman) | - [Niclas Kron](https://github.com/sphrak/) - Nicolás Lichtmaier - [Niek Haarman](https://github.com/nhaarman) - Niels van Hove - [Niklas Baudy](https://github.com/vanniktech) - [Renato Goncalves](https://github.com/renatoarg) - [Roar Grønmo](https://github.com/RoarGronmo) - [Ruslan Baratov](https://github.com/ruslo) - [Sinan Kozak](https://github.com/kozaxinan) - [Slawomir Czerwinski](https://github.com/sczerwinski) - [Stefan Wolf](https://github.com/wolfs) - [Stephen D'Amico](https://github.com/sddamico) - Tao Wang - [Tomas Chladek](https://github.com/ThomasCZ) - [Tomáš Procházka](https://stackoverflow.com/users/504179/atom) - [Tony Robalik](https://github.com/autonomousapps) - [Torbjørn Sørli](https://stackoverflow.com/users/503668/thorbear) - Warren He - [Yenchi Lin](https://github.com/xcatg) - [Zac Sweers](https://github.com/ZacSweers) |

<br />