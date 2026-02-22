---
title: https://developer.android.com/studio/releases/archives
url: https://developer.android.com/studio/releases/archives
source: md.txt
---

The following are release notes of Android Studio 3.6 and lower, and Android
Gradle plugin 3.6.0 and lower.

## Older releases of Android Studio

### 3.6 (February 2020)

Android Studio 3.6 is a major release that includes a variety of new features
and improvements.

We'd also like to thank all of our [community contributors](https://developer.android.com/studio/releases/archives#3-6-community-contributors) who have helped with this release.  
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

#### Design tools

<br />

<br />

This version of Android Studio includes updates to several design tools,
including the Layout Editor and Resource Manager.

<br />

<br />

##### Split view and zoom in design editors

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

##### Color Picker Resource Tab

<br />

<br />

To help you quickly update color resource values in your app when you're using
the color picker in your XML or the design tools, the IDE now populates
color resource values for you.

<br />

![Color picker with populated color values](https://developer.android.com/static/studio/images/releases/color-picker-resource-tab.png)

<br />

##### Resource Manager

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

#### Updates to the Android Gradle plugin

<br />

<br />

The latest version of the Android Gradle plugin includes many updates,
including optimizations for build speed, support for the Maven publishing
plugin, and support for View Binding. To learn more, read the
[full release notes](https://developer.android.com/studio/releases/gradle-plugin#3-6-0).

<br />

<br />

##### View binding

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

#### Apply Changes

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

#### Refactor menu option to enable Instant Apps support

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

#### Deobfuscate class and method bytecode in APK Analyzer

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

#### Native tooling

<br />

<br />

The following updates support native (C/C++) development in Android Studio.

<br />

<br />

##### Kotlin support

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

##### Other JNI improvements

<br />

<br />

The code editor in Android Studio now supports a more seamless JNI development
workflow, including improved type hints, auto-completion, inspections, and
code refactoring.

<br />

<br />

##### APK reloading for native libraries {:#3.6-reload-apk}

<br />

<br />

You no longer need to create a new project when the APK in your project is
updated outside the IDE. Android Studio detects changes in the APK and gives you
the option to re-import it.

<br />

![](https://developer.android.com/static/studio/images/debug/import-updated-apk.png)

<br />

#### Attach Kotlin-only APK sources

<br />

<br />

It is now possible to attach Kotlin-only external APK sources when you profile
and debug pre-built APKs. To learn more, see
[Attach Kotlin/Java sources](https://developer.android.com/studio/debug/apk-debugger#attach_java).

<br />

<br />

#### Leak detection in Memory Profiler

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

##### Attach Kotlin-only APK sources

<br />

<br />

It is now possible to attach Kotlin-only external APK sources when you profile
and debug pre-built APKs. To learn more, see
[Attach Kotlin/Java sources](https://developer.android.com/studio/debug/apk-debugger#attach_java).

<br />

<br />

##### Leak detection in Memory Profiler

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

#### Emulators

<br />

<br />

Android Studio 3.6 helps you take advantage of several updates included in
Android Emulator 29.2.7 and higher, as described below.

<br />

<br />

##### Improved Location Support

<br />

<br />

Android Emulator 29.2.7 and higher provides additional support for emulating
GPS coordinates and route information. When you open the Emulators
[Extended controls](https://developer.android.com/studio/run/advanced-emulator-usage#extended),
options in the Location tab are now organized under two tabs:
**Single points** and **Routes**.

<br />

<br />

###### Single points

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

###### Routes

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

##### Multi-display support

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

##### New virtual devices and project templates for Android Automotive OS

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

#### Resumable SDK downloads

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

#### Win32 deprecated

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

#### New option for optimizing Gradle sync time

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

#### New location to toggle Gradle's offline mode

<br />

<br />

To enable or disable Gradle's offline mode, first select
**View \> Tool Windows \> Gradle** from the menu bar. Then, near the top of
the **Gradle** window, click **Toggle Offline Mode**
![Gradle offline button in the Gradle panel.](https://developer.android.com/static/studio/images/buttons/gradle-offline.png).

<br />

<br />

#### IntelliJ IDEA 2019.2

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

#### Community contributors

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

### 3.5 (August 2019)

Android Studio 3.5 is a major release and a result of Project Marble.
Beginning with the release of
[Android Studio 3.3](https://android-developers.googleblog.com/2019/01/android-studio-33.html), the Project Marble initiative has spanned multiple releases that focus on
improving three main areas of the IDE:
[system health](https://developer.android.com/studio/releases/archives#3-5-system-health),
[feature polish](https://developer.android.com/studio/releases/archives#3-5-feature-polish), and fixing bugs.

For information about these and other Project Marble updates, read the
[Android Developers blog post](https://android-developers.googleblog.com/2019/08/android-studio-35-project-marble-goes.html) or the sections below.

We also want to thank all of our
[community contributors](https://developer.android.com/studio/releases/archives#3-5-community-contributors) who have
helped with this release.  

<br />

**3.5.3 (December 2019)**


This minor update includes various bug fixes and performance improvements.

**3.5.2 (November 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/11/android-studio-352-available.html).

**3.5.1 (October 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/10/android-studio-351-available.html).

<br />

<br />

#### Project Marble: System health

<br />

<br />

This section describes the changes in Android Studio 3.5 that are focused on
improving system health.

<br />

<br />

##### Recommended memory settings

<br />

<br />

Android Studio now notifies you if it detects that you could improve performance
by increasing the maximum amount of RAM that your OS should allocate for Android
Studio processes, such as the core IDE, Gradle daemon, and Kotlin daemon. You
can either accept the recommended settings by clicking the action link in the
notification, or you can adjust these settings manually by selecting
**File \> Settings** (or
**Android Studio \> Preferences** on macOS), and then finding the
**Memory Settings** section under
**Appearance \& Behavior \> System Settings** . To learn more,
see [Maximum heap size](https://developer.android.com/studio/intro/studio-config#adjusting_heap_size).

<br />

![A notification about recommended memory settings.](https://developer.android.com/static/studio/images/memory-settings-notification.png)

A notification about recommended memory settings.

<br />

<br />

##### Memory usage report

<br />

<br />

Memory problems in Android Studio are sometimes difficult to reproduce and
report. To help solve this problem, Android Studio lets you generate a memory
usage report by clicking **Help \> Analyze Memory Usage** from the menu bar. When
you do so, the IDE locally sanitizes the data for personal information before
asking whether you want to send it to the Android Studio team to help identify
the source of the memory issues. To learn more, see [Run a memory usage
report](https://developer.android.com/studio/report-bugs#run-memory-usage-report).

<br />

![A memory usage report.](https://developer.android.com/static/studio/images/memory-usage-report.png)

A memory usage report.

<br />

<br />

##### Windows: Antivirus file I/O optimization

<br />

<br />

Android Studio now automatically checks whether certain project directories are
excluded from real-time antivirus scanning. When adjustments can be made to
improve build performance, Android Studio notifies you and provides instructions
on how to optimize your antivirus configuration. To learn more, see
[Minimize the impact of antivirus software on build speed](https://developer.android.com/studio/intro/studio-config#antivirus-impact).

<br />

<br />

#### Project Marble: Feature polish

<br />

<br />

This section describes the changes in Android Studio 3.5 that are focused on
improving existing features.

<br />

<br />

##### Apply Changes

<br />

<br />

Apply Changes lets you push code and resource changes to your running app
without restarting your app---and, in some cases, without restarting the current
activity. Apply Changes implements a completely new approach for preserving your
app's state. Unlike Instant Run, which rewrote the bytecode of your APK, Apply
Changes redefines classes on the fly by leveraging the runtime instrumentation
supported in Android 8.0 (API level 26) or higher.

To learn more, see [Apply Changes](https://developer.android.com/studio/run#apply-changes).

<br />

![The toolbar buttons for Apply Changes.](https://developer.android.com/static/studio/images/releases/apply-changes-buttons-3.5.png)

The toolbar buttons for Apply Changes.

<br />

<br />

##### App deployment flow

<br />

<br />

The IDE has a new drop-down menu that lets you quickly select which device you'd
like to deploy your app to. This menu also includes a new option that lets you
run your app on multiple devices at once.

<br />

![Target device drop-down menu.](https://developer.android.com/static/studio/images/run/deploy-run-app.png)

Target device drop-down menu.

<br />

<br />

##### Improved Gradle sync and cache detection

<br />

<br />

The IDE now better detects when Gradle periodically clears your build cache when
reducing its hard disk consumption. In previous versions, this state caused the
IDE to report missing dependencies and Gradle sync to fail. Now, the IDE simply
downloads dependencies as needed to ensure that Gradle sync completes
successfully.

<br />

<br />

##### Improved build error output

<br />

<br />

The **Build** ![Build window icon](https://developer.android.com/static/studio/images/buttons/window-build-2x.png)
window now provides better error reporting, such as a link to the file and line
of the reported error, for the following build processes:

<br />

<br />

- AAPT compilation and linking
- R8 and ProGuard
- Dexing
- Resource merging
- XML file parsing
- Javac, Kotlinc, and CMake compilation

<br />

<br />

##### Project Upgrades

<br />

<br />

Improved update experience to provide more information and actions to help you
update the IDE and the Android Gradle plugin. For example, more sync and build
errors include actions to help you mitigate errors when updating.

<br />

<br />

It's important to keep in mind, you can update the IDE independently of other
components, such as the Android Gradle plugin. So, you can safely update the IDE
as soon as a newer version is available, and update other components later.

<br />

<br />

##### Layout Editor

<br />

<br />

Android Studio 3.5 includes several improvements to layout visualization,
management, and interaction.

<br />

<br />

When working with `ConstraintLayout`, a new **Constraints**
section in the **Attributes** panel lists the constraints relationships of
the selected UI component. You can select a constraint either from the design
surface or from the constraints list to highlight the constraint in both areas.

<br />

![Constraint relationships for a selected UI element.](https://developer.android.com/static/studio/images/releases/constraint-relationships-3.5.png)

Constraint relationships for a selected UI element.

<br />

<br />

Similarly, you can now delete a constraint by selecting it and pressing the
`Delete` key. You can also delete a constraint by holding the
`Control` key (`Command` on macOS) and clicking on the
constraint anchor. Note that when you hold the `Control` or
`Command` key and hover over an anchor, any associated constraints
turn red to indicate that you can click to delete them.

<br />

<br />

When a view is selected, you can create a constraint by clicking on any of the
**+** icons in the **Constraint Widget** section of
the **Attributes** panel, as
shown in the following image. When you create a new constraint, the Layout
Editor now selects and highlights the constraint, providing immediate visual
feedback for what you've just added.

<br />

![An animation showing how to use the constraint widget to create
constraints.](https://developer.android.com/static/studio/images/releases/constraint-widget-3.5.gif)

Using the constraint widget to create constraints .

<br />

<br />

When creating a constraint, the Layout Editor now shows only the eligible anchor
points to which you can constrain. Previously, the Layout Editor highlighted all
anchor points on all views, regardless of whether you could constrain to them.
In addition, a blue overlay now highlights the target of the constraint. This
highlighting is particularly useful when attempting to constrain to a component
that overlaps with another.

<br />

![An animation showing how to create a constraint for an overlapping
component in Android Studio 3.4.](https://developer.android.com/static/studio/images/releases/constraint-target-overlay-3.4.gif)

Creating a constraint for an overlapping component in
Android Studio 3.4.

<br />

![An animation showing how to create a constraint for an overlapping
component in Android Studio 3.5.](https://developer.android.com/static/studio/images/releases/constraint-target-overlay-3.5.gif)

Creating a constraint for an overlapping component in
Android Studio 3.5.

<br />

<br />

In addition to the above updates, Android Studio 3.5 also contains the
following Layout Editor improvements:

<br />

<br />

- The **Constraint Widget** and default margin drop-down now allow you to use dimension resources for margins.
- In the Layout Editor toolbar, the list of devices that determine the size of the design surface has been updated. In addition, snapping behavior while resizing has been improved, and the resizing handles on the design surface are now always visible. When resizing, new overlays appear that show common device sizes.
- The Layout Editor has a new color scheme that improves consistency and reduces contrast between components, text, and constraints.
- Blueprint mode now includes text support for some components where text wasn't being shown.

For more information about these changes, see
[Android Studio Project Marble: Layout Editor](https://medium.com/androiddevelopers/android-studio-project-marble-layout-editor-608b6704957a).

<br />

<br />

##### Data Binding

In addition to adding [incremental annotation processing support](https://developer.android.com/studio/releases/archives#incremental_ap)
for Data Binding, the IDE improves smart editor features and performance
when creating data binding expressions in XML.

<br />

![An animation showing code editor performance on Android Studio
3.4.](https://developer.android.com/static/studio/images/releases/xml-editing-latency-3.4.gif)

Code editor performance on Android Studio 3.4.
![An animation showing code editor performance on Android Studio
3.5.](https://developer.android.com/static/studio/images/releases/xml-editing-latency-3.5.gif)

Improved code editing performance on Android Studio
3.5.

<br />

<br />

##### Improved support for C/C++ projects

<br />

<br />

Android Studio 3.5 includes several changes that improve support for C/C++
projects.

<br />

<br />

###### Build Variants panel improvements for single variant sync

<br />

<br />

You can now specify both the active build variant and active ABI in the
**Build Variants** panel. This feature simplifies build configuration per module
and can also improve Gradle sync performance.

<br />

<br />

To learn more, see [Change the build variant](https://developer.android.com/studio/run#changing-variant).

<br />

![Build Variants panel showing single variant selection by ABI.](https://developer.android.com/static/studio/images/releases/single-variant-ABI.png)

The Build Variants panel with single variant selection by
ABI.

<br />

<br />

###### Side-by-side versions of the NDK

<br />

<br />

You can now use multiple versions of the NDK side-by-side. This feature gives
you more flexibility when configuring your projects---for example, if you have
projects that use different versions of the NDK on the same machine.

<br />

<br />

If your project uses Android Gradle plugin 3.5.0 or higher, you can also specify
the version of the NDK that each module in your project should use. You can use
this feature to create reproducible builds and to mitigate incompatibilities
between NDK versions and the Android Gradle plugin.

<br />

<br />

To learn more, see[Install and configure the NDK, CMake, and LLDB](https://developer.android.com/studio/projects/install-ndk).

<br />

<br />

#### ChromeOS Support

<br />

<br />

Android Studio now officially supports ChromeOS devices, such as the HP
Chromebook x360 14, Acer Chromebook 13/Spin 13, and others that you can read
about in the [system requirements](https://developer.android.com/studio#Requirements). To get
started, [download Android Studio](https://developer.android.com/studio) on your compatible
ChromeOS device and follow the
[installation instructions](https://developer.android.com/studio/install#chrome-os).

Note: Android Studio on ChromeOS currently supports deploying your app only to
a connected hardware device. To learn more, read
[Run apps on a hardware
device](https://developer.android.com/studio/run/device).

<br />

<br />

#### Conditional delivery for feature modules

<br />

<br />

Conditional delivery allows you to set certain device configuration requirements
for feature modules to be downloaded automatically during app install.
For example, you can configure a feature module that includes
functionality for augmented reality (AR) to be available at app install for only
devices that support AR.

<br />

<br />

This delivery mechanism currently supports controlling the download of a module
at app install-time based on the following device configurations:

<br />

<br />

- Device hardware and software features, including OpenGL ES version
- User country
- API level

<br />

<br />

If a device does not meet all the requirements you specify, the module is not
downloaded at app install-time. However, your app may later request to
[download the module on demand](https://developer.android.com/guide/app-bundle/playcore) using the Play Core
Library. To learn more, read
[Configure conditional delivery](https://developer.android.com/studio/projects/dynamic-delivery/conditional-delivery).

<br />

<br />

#### IntelliJ IDEA 2019.1

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the [2019.1 release](https://blog.jetbrains.com/idea/2019/03/intellij-idea-2019-1-is-released-theme-customization-java-12-switch-expressions-debug-inside-docker-containers-and-more/), such as theme customization.

<br />

<br />

The last IntelliJ version that was included with Android Studio was 2018.3.4.
For more information about the improvements from other IntelliJ versions
that are included cumulatively with this release of Android Studio, see the
following bug-fix updates:

<br />

<br />

- [IntelliJ IDEA 2018.3.6](https://blog.jetbrains.com/idea/2019/03/intellij-idea-2018-3-6-is-released/){: .external-link}
- [IntelliJ IDEA 2018.3.5](https://blog.jetbrains.com/idea/2019/02/intellij-idea-2018-3-5-is-out/){: .external-link}

<br />

<br />

#### Android Gradle plugin 3.5.0 updates

<br />

<br />

For information on what's new in Android Gradle plugin 3.5.0, such as improved
support for incremental annotation processing and cacheable unit tests, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

#### Community contributors

Thank you to all of our community contributors who have helped us discover bugs
and other ways to improve Android Studio 3.5. In particular, we'd like to thank
the following people who reported P0 and P1 bugs:

<br />

<br />

|---|---|---|
| - [Aaron He](https://github.com/aaronhe42) - [Andreas Dybdahl](https://github.com/anddybdahl) - [Andrei Vădan](https://github.com/Vampirelu) - [Andrew Hughes](https://github.com/ashughes) - [Andrey Mischenko](https://github.com/gildor) - Andrii Seredenko - [Benoît 'BoD' Lubek](https://github.com/BoD) - [Berkeli Alashov](https://github.com/alashow) - [Bram Stolk](https://github.com/stolk) - [Charles Anderson](https://github.com/gtcompscientist) - Curtis Kroetsch - [David Burström](https://stackoverflow.com/users/643007/david-burstr%c3%b6m) - [DeweyReed](https://github.com/DeweyReed) - Dmitriy Dolovov - [Emin Kokalari](https://stackoverflow.com/users/3636806/eak-team) - [Evan Tatarka](https://github.com/evant) - [Evgeny Brazgin](https://github.com/xapienz) | - [George Kropotkin](https://github.com/gmk57) - [Ido Feins](https://github.com/ifeins) - Jakub Banaszewski - [Jean-Michel Fayard](https://github.com/jmfayard) - [John Rodriguez](https://github.com/jrodbx) - [Kamil Dudek](https://github.com/dudududi) - [Kenji Abe](https://github.com/STAR-ZERO) - [Liran Barsisa](https://stackoverflow.com/users/878126/android-developer) - [Louis CAD](https://github.com/LouisCAD) - Luke Fielke - [Lóránt Pintér](https://github.com/lptr) - Marcin Dawid - Mario O - [Mauricio Vignale](https://github.com/mvignale1987) - [Michael Bailey](https://stackoverflow.com/users/1686989/yogurtearl) - Miguel Angel Rossi Sanahuja - [Niklas Baudy](https://github.com/vanniktech) | - [Noah Andrews](https://github.com/NoahAndrews) - [Oleksandr Zakrevskyi](https://github.com/sanchopanchos) - Peter Vegh - [Rishabh harit](https://github.com/rishabh876) - [Roar Grønmo](https://github.com/RoarGronmo) - [Said Tahsin Dane](https://github.com/tasomaniac/) - [Shayan Sabahi](https://stackoverflow.com/users/6600637/shynline) - [Slawomir Czerwinski](https://github.com/sczerwinski) - Stephen Yu - [Steven Schoen](https://github.com/dsteve595) - [Tolriq](https://github.com/tolriq) - [Tony Robalik](https://github.com/autonomousapps) - [Uli Bubenheimer](https://github.com/bubenheimer/) - Vixb Xue - [Yi Cheng](https://github.com/wisechengyi) |

<br />

### 3.4 (April 2019)

Android Studio 3.4 is a major release that includes a variety of new features
and improvements.  

<br />

**3.4.2 (July 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/07/android-studio-342-available.html).

**3.4.1 (May 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/05/android-studio-341-available.html).

**3.4.0 known issues**

- Profiling is disabled when deploying your app to a device
  running Android Q Beta.

- When using the Data Binding Library, `LiveDataListener.onChanged()` might fail with a NPE. A fix for this issue will be included in Android Studio 3.4.1 and is already available in the latest [Preview version](https://developer.android.com/studio/preview) of Android Studio 3.5. (See [issue #122066788](https://issuetracker.google.com/122066788))

<br />

<br />

#### IntelliJ IDEA 2018.3.4

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the
[2018.3.4 release](https://blog.jetbrains.com/idea/2019/01/intellij-idea-2018-3-4-is-released/).

<br />

<br />

#### Android Gradle plugin 3.4.0 updates

<br />

<br />

For information on what's new in Android Gradle plugin 3.4.0, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

#### New Project Structure Dialog

<br />

<br />

The new Project Structure Dialog (PSD) makes it easier to update
dependencies and configure different aspects of your project, such as modules,
build variants, signing configurations, and build variables.

<br />

<br />

You can open the PSD by selecting **File \> Project Structure** from the menu
bar. You can also open the PSD by pressing `Ctrl+Shift+Alt+S` on Windows and
Linux, or `Command+;` (semicolon) on macOS. You can find descriptions of some of
the new and updated sections of the PSD below.

<br />

<br />

##### Variables

<br />

<br />

The new variables section of the PSD allows you to create and manage build
variables, such as those to keep version numbers for dependencies consistent
across your project.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_variables.png)

<br />

- Quickly view and edit build variables that already exist in your project's Gradle build scripts.
- Add new build variables at a project- or module-level directly from the PSD.

<br />

<br />

**Note:** If your existing build configuration files assign
values through complex Groovy scripts, you may not be able to edit those values
through the PSD. Additionally, you can not edit build files written in Kotlin
using the PSD.

<br />

<br />

##### Modules

<br />

<br />

Configure properties that are applied to all build variants in an existing
module or add new modules to your project from the **Modules** section. For
example, this is where you can configure `defaultConfig` properties or manage
signing configurations.

<br />

<br />

##### Dependencies

<br />

<br />

Inspect and visualize each dependency in the dependency graph of
your project, as resolved by Gradle during project sync, by following these
steps:

<br />

<br />

1. In the left pane of the PSD, select **Dependencies**.
2. In the **Modules** pane, select a module for which you'd like to inspect the resolved dependencies.
3. On the right side of the PSD, open the **Resolved Dependencies** pane, which is shown below.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_resolved_dependencies.png)

<br />

You can also quickly search for and add dependencies to your project by first
selecting a module from the **Dependencies** section of the PSD, clicking
the (+) button in the **Declared Dependencies** section, and selecting the type
of dependency you want to add.

<br />

<br />

Depending on the type of dependency you select, you should see a dialog,
similar to the one below, that helps you add the dependency to the module.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_add_dependency.png)

<br />

##### Build Variants

<br />

<br />

In this section of the PSD, create and configure build variants and product
flavors for each module in your project. You can add manifest placeholders, add
ProGuard files, and assign signing keys, and more.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_build_variants.png)

<br />

##### Suggestions

<br />

<br />

See suggested updates for project dependencies and build variables in the
**Suggestions** section, as shown below.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_suggestions.png)

<br />

#### New Resource Manager

<br />

<br />

Resource Manager is a new tool window for importing, creating, managing, and
using resources in your app. You can open the tool window by selecting
**View \> Tool Windows \> Resource Manager** from the menu bar. The Resource
Manager allows you to do the following:

<br />

![](https://developer.android.com/static/studio/images/releases/resource_manager.png)

<br />

- **Visualize resources:** You can preview drawables, colors, and layouts to quickly find the resources you need.
- **Bulk import:** You can import multiple drawable assets at once by either dragging and dropping them into the **Resource Manager** tool window or by using the **Import drawables** wizard. To access the wizard, select the (+) button at the top-left corner of the tool window, and then select **Import Drawables** from the drop down menu.
- **Convert SVGs into `VectorDrawable` objects:** You can use the **Import Drawables** wizard to convert your SVG images into `VectorDrawable` objects.
- **Drag and drop assets:** From the **Resource Manager** tool window, you can drag and drop drawables onto both the design and XML views of the Layout Editor.
- **View alternative versions:** You can now view alternative versions of your resources by double-clicking a resource within the **Tool** window. This view shows the different versions you have created and the qualifiers that were included.
- **Tile and list views:** You can change the view within the tool window to visualize your resources in different arrangements.

<br />

<br />

To learn more, read the guide about how to
[Manage app resources](https://developer.android.com/studio/write/resource-manager).

<br />

<br />

#### Checking build IDs when profiling and debugging APKs

<br />

<br />

When you provide debugging symbol files for the `.so` shared libraries inside
your APK, Android Studio verifies that the
[build ID](https://linux.die.net/man/1/ld) of the provided symbol files match
the build ID of the `.so` libraries inside the APK.

<br />

<br />

If you build the native libraries in your APK with a build ID, Android Studio
checks whether the build ID in your symbol files matches the build ID in your
native libraries and rejects the symbol files if there is a mismatch. If
you did not build with a build ID, then providing incorrect symbol files may
cause problems with debugging.

<br />

<br />

#### R8 enabled by default

<br />

<br />

R8 integrates desugaring, shrinking, obfuscating,
optimizing, and dexing all in one step---resulting in
[noticeable build performance improvements](https://www.google.com/url?q=https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html&sa=D&ust=1551922493258000&usg=AFQjCNH0N1wuMX645n7giw0wjikzjm3WCA).
R8 was introduced in Android Gradle plugin 3.3.0 and
is now enabled by default for both app and Android library projects using
plugin 3.4.0 and higher.

<br />

<br />

The image below provides a high-level overview of the compile process
before R8 was introduced.

<br />

![Before R8, ProGuard was a different compile step from dexing and
desugaring.](https://developer.android.com/static/studio/images/build/r8/compile_with_d8_proguard.png)

<br />

Now, with R8, desugaring, shrinking, obfuscating, optimizing, and dexing (D8)
are all completed in one step, as illustrated below.

<br />

![With R8, desugaring, shrinking, obfuscating, optimizing, and dexing
are all performed in a single compile step.](https://developer.android.com/static/studio/images/build/r8/compile_with_r8.png)

<br />

Keep in mind, R8 is designed to work with your existing ProGuard rules, so
you'll likely not need to take any actions to benefit from R8. However,
because it's a different technology to ProGuard that's designed specifically
for Android projects, shrinking and optimization may result in removing code
that ProGuard may have not. So, in this unlikely situation, you might need to
add additional rules to keep that code in your build output.

<br />

<br />

If you experience issues using R8, read the
[R8 compatibility FAQ](https://r8.googlesource.com/r8/+/refs/heads/master/compatibility-faq.md)
to check if there's a solution to your issue. If a solution isn't documented,
please [report a bug](https://issuetracker.google.com/issues/new?component=326788&template=1025938).
You can disable R8 by adding one of the following lines to your project's
`gradle.properties` file:

<br />

<br />

        # Disables R8 for Android Library modules only.
        android.enableR8.libraries = false
        # Disables R8 for all modules.
        android.enableR8 = false
        
      
<br />

<br />

**Note:** For a given build type, if you set
`useProguard` to `false` in your app
module's `build.gradle` file, the Android Gradle plugin uses R8 to shrink your
app's code for that build type, regardless of whether you disable R8 in your
project's `gradle.properties` file.

<br />

<br />

#### Navigation Editor now supports all argument types

<br />

<br />

All argument types supported by the Navigation component are now supported in
the Navigation Editor. For more information on supported types, see
[Pass data between destinations](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data).

<br />

<br />

#### Layout Editor improvements {:#layout-editor}

The **Attributes** pane in the Layout Editor has been streamlined into a single
page with sections you can expand to reveal attributes you can configure. The
**Attributes** pane also includes the following updates:

<br />

<br />

- A new **Declared Attributes** section lists the attributes the layout file specifies and allows you to quickly add new ones.
- The **Attributes** pane now also features indicators next to each attribute that are solid when the attribute's value is a resource reference and empty otherwise.
- Attributes with errors or warnings are now highlighted. Red highlights indicate errors (for example, when you use invalid layout values) and orange highlights indicate warnings (for example, when you use hard-coded values).

<br />

<br />

#### New intention action to quickly import dependencies

<br />

<br />

If you start using certain Jetpack and Firebase classes in your code, a new
intention action suggests adding the required Gradle library dependency to your
project, if you haven't already done so. For example, if you reference the
`WorkManager` class without first importing the required
`android.arch.work:work-runtime` dependency, an intention action lets you do so
easily in a single click, as shown below.

<br />

![](https://developer.android.com/static/studio/images/releases/import_intention.png)

<br />

In particular, because Jetpack repackaged the support library into discrete
packages that are easier to manage and update, this intention action helps you
quickly add only the dependencies you need for the Jetpack components you want
to use.

<br />

### 3.3 (January 2019)

Android Studio 3.3 is a major release that includes a variety of new features
and improvements.  

<br />

**3.3.2 (March 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/03/android-studio-332-available.html).

**3.3.1 (February 2019)**


This minor update includes various bug fixes and performance improvements.

<br />

<br />

#### IntelliJ IDEA 2018.2.2

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the [2018.2.2 release](http://blog.jetbrains.com/idea/2018/08/intellij-idea-2018-2-2-is-released).

<br />

<br />

#### Android Gradle plugin updates

<br />

<br />

For information on what's new in the Android Gradle plugin, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

#### Navigation Editor

<br />

<br />

The Navigation Editor lets you quickly visualize and build navigation into your
app by using the
[Navigation Architecture Component](https://developer.android.com/topic/libraries/architecture/navigation).

<br />

![](https://developer.android.com/static/studio/images/releases/navigation-editor_2x.png)

<br />

For more information, see
[Implement navigation with the Navigation Architecture Component](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing).

<br />

<br />

#### Delete unused Android Studio directories

<br />

<br />

When you run a major version of Android Studio for the first time, it looks for
directories containing caches, settings, indices, and logs for versions of
Android Studio for which a corresponding installation can't be found. The
**Delete Unused Android Studio Directories** dialog then displays locations,
sizes, and last-modified times of these unused directories and provides an
option to delete them.

<br />

<br />

The directories Android Studio considers for deletion are listed below:

<br />

<br />

- Linux: `~/.AndroidStudio[Preview]`*X.Y*
- Mac: `~/Library/{Preferences, Caches, Logs, Application Support}/AndroidStudio[Preview]`*X.Y*
- Windows: `%USER%.AndroidStudio[Preview]`*X.Y*

<br />

![](https://developer.android.com/static/studio/images/releases/delete-unused-directories-dialog-2x.png)

<br />

#### Lint improvements

<br />

<br />

Lint, when invoked from Gradle, is significantly faster---larger projects can
expect lint to run up to four times faster.

<br />

<br />

#### Create New Project wizard

<br />

<br />

The **Create New Project** wizard has a new look and contains updates that help
streamline the creation of new Android Studio projects.

<br />

![](https://developer.android.com/static/studio/images/projects/new-project-wizard-choose_2x.png)

<br />

For more information, see [Create a project](https://developer.android.com/studio/projects/create-project).

<br />

<br />

#### Profiler updates

<br />

<br />

Android Studio 3.3 includes updates to several of the individual profilers.

<br />

<br />

##### Improved performance

<br />

<br />

Based on user feedback, rendering performance while using the profilers has been
greatly improved. Please continue to
[provide feedback](https://issuetracker.google.com/issues/new?component=192722),
especially if you continue to see performance issues.

<br />

##### Profiler memory allocation tracking options

<br />

<br />

To improve app performance while profiling, the
[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler) now samples memory
allocations periodically by default. If desired, you can change this behavior by
using the **Allocation Tracking** dropdown when testing on devices running
Android 8.0 (API level 26) or higher.

<br />

![](https://developer.android.com/static/studio/images/releases/profiler-memory-allocation-modes.png)

<br />

Using the **Allocation Tracking** dropdown, you can choose from the following
modes:

<br />

<br />

- **Full:** captures all object memory allocations. Note that if you have an app
  that allocates a lot of objects, you might see significant performance issues
  while profiling.

- **Sampled:** captures a periodic sample of object memory allocations. This is
  the default behavior and has less impact on app performance while profiling.
  You might encounter some performance issues with apps that allocate a lot of
  objects within a short time period.

- **Off:** turns memory allocation off. If not already selected, this mode is
  enabled automatically while taking a CPU recording and then returned to the
  previous setting when the recording is finished. You can change this behavior
  in the CPU recording configuration dialog.

  The tracking affects both Java objects and JNI references.

<br />

<br />

##### Inspect frame rendering data

<br />

<br />

In the [CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler), you can now inspect how
long it takes your Java app to render each frame on the main UI thread and
RenderThread. This data might be useful when investigating bottlenecks that
cause UI jank and low framerates. For example, each frame that takes longer than
the 16ms required to maintain a smooth framerate is displayed in red.

<br />

<br />

To see frame rendering data, [record a trace](https://developer.android.com/studio/profile/cpu-profiler#method_traces)
using a configuration that allows you to **Trace System Calls** . After recording
the trace, look for info about each frame along the timeline for the recording
under the section called **FRAMES**, as shown below.

<br />

![](https://developer.android.com/static/studio/images/releases/frame-rendering_2x.png)

<br />

To learn more about investigating and fixing framerate issues, read
[Slow rendering](https://developer.android.com/topic/performance/vitals/render).

<br />

<br />

##### Fragments in the event timeline

<br />

<br />

The event timeline now shows when fragments are attached and detached.
Additionally, when you hover over a fragment, a tooltip shows you the fragment
status.

<br />

![](https://developer.android.com/static/studio/images/releases/fragments-activity-bar_2x.png)

<br />

##### View formatted text for connection payloads in the Network profiler

<br />

<br />

Previously, the Network profiler displayed only raw text from connection
payloads. Android Studio 3.3 now formats certain text types by default,
including JSON, XML, and HTML. In the **Response** and **Request** tabs, click
the **View Parsed** link to display formatted text, and click the
**View Source** link to display raw text.

<br />

![](https://developer.android.com/static/studio/images/releases/network-profiler-text_2x.png)

<br />

For more information, see
[Inspect network traffic with Network Profiler](https://developer.android.com/studio/profile/network-profiler).

<br />

<br />

#### Automatic downloading of SDK components

<br />

<br />

When your project needs an SDK component from the SDK platforms, NDK, or CMake,
Gradle now attempts to automatically download the required packages as long as
you've previously accepted any related license agreements using the SDK Manager.

<br />

<br />

For more information, see
[Auto-download missing packages with Gradle](https://developer.android.com/studio/intro/update#download-with-gradle).

<br />

<br />

#### Support for Clang-Tidy

<br />

<br />

Android Studio now includes support for static code analysis using
[Clang-Tidy](http://clang.llvm.org/extra/clang-tidy/) for projects that include
native code. To enable support for Clang-Tidy,
[update your NDK](https://developer.android.com/ndk/guides#download-ndk) to r18 or higher.

<br />

<br />

You can then enable or re-enable the inspections by opening the **Settings** or
**Preferences** dialog and navigating to
**Editor \> Inspections \> C/C++ \> General \> Clang-Tidy** . When selecting this
inspection in the **Settings** or **Preferences** dialog, you can also see the
list of Clang-Tidy checks that are enabled and disabled under the
**Option** section of the right-most panel. To enable
[additional checks](https://clang.llvm.org/extra/clang-tidy/checks/list.html),
add them to the list and click **Apply**.

<br />

<br />

To configure Clang-Tidy with [additional options](http://clang.llvm.org/extra/clang-tidy/#using-clang-tidy),
click **Configure Clang-Tidy Checks Options** and add them in the dialog that
opens.

<br />

<br />

#### Removal of options for C++ customization

<br />

<br />

The following options have been removed from the **Customize C++ Support**
dialog:

<br />

<br />

- **Exceptions Support (-fexceptions)**
- **Runtime Type Information Support (-ftti)**

<br />

<br />

The respective behaviors are enabled for all projects created through Android Studio.

<br />

<br />

#### CMake version 3.10.2

<br />

<br />

CMake version 3.10.2 is now included with SDK Manager. Note that Gradle still
uses version 3.6.0 by default.

<br />

<br />

To specify a CMake version for Gradle to use, add the following to your module's
`build.gradle` file:

<br />

<br />

        android {
            ...
            externalNativeBuild {
                cmake {
                    ...
                    version "3.10.2"
                }
            }
        }
        
      
<br />

<br />

For more information on configuring CMake in `build.gradle`, see
[Manually configure Gradle](https://developer.android.com/studio/projects/gradle-external-native-builds#configure-gradle).

<br />

<br />

#### New "+" syntax to specify minimum CMake versions

<br />

<br />

When specifying a version of CMake in your main module's `build.gradle` file,
you can now append a "+" to match the behavior of CMake's
[`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html)
command.

<br />

<br />

**Caution:** Using "+" syntax with other
[build dependencies](https://developer.android.com/studio/build/dependencies)
is discouraged, as dynamic dependencies can cause unexpected version updates and
difficulty resolving version differences.

<br />

<br />

#### Android App Bundles now support Instant Apps

<br />

<br />

Android Studio now lets you build [Android App Bundles](https://developer.android.com/guide/app-bundle) with
full support for [Google Play Instant](https://developer.android.com/topic/google-play-instant/overview). In
other words, you can now build and deploy both installed app and instant
experiences from a single Android Studio project and include them in a single
Android App Bundle.

<br />

<br />

If you're creating a new Android Studio project using the **Create New Project**
dialog, make sure you check the box next to
**Configure your project \> This project will support instant apps**. Android
Studio then creates a new app project as it normally would, but includes the
following properties in your manifest to add Instant app support to your app's
base module:

<br />

<br />

        <manifest ... xmlns:dist="http://schemas.android.com/apk/distribution">
            <dist:module dist:instant="true" />
            ...
        </manifest>
        
      
<br />

<br />

You can then
[create an instant-enabled feature](https://developer.android.com/studio/projects/dynamic-delivery#create_instant_enabled)
module by selecting **File \> New \> New Module** from the menu bar and then
selecting **Instant Dynamic Feature Module** from the **Create New Module**
dialog. Keep in mind, creating this module also instant-enables your app's base
module.

<br />

<br />

To deploy your app to a local device as an instant experience,
[edit your run configuration](https://developer.android.com/studio/run/rundebugconfig#editing) and check the
box next to **General \> Deploy as instant app**.

<br />

<br />

#### Single-variant project sync

<br />

<br />

[Syncing your project](https://developer.android.com/studio/build#sync-files) with your build configuration
is an important step in letting Android Studio understand how your project is
structured. However, this process can be time-consuming for large projects. If
your project uses multiple build variants, you can now optimize project syncs by
limiting them to only the variant you have currently selected.

<br />

<br />

You need to use Android Studio 3.3 or higher with Android Gradle plugin 3.3.0
or higher to enable this optimization. When you meet these requirements, the
IDE prompts you to enable this optimization when you sync your project. The
optimization is also enabled by default on new projects.

<br />

<br />

To enable this optimization manually, click
**File \> Settings \> Experimental \> Gradle**
(**Android Studio \> Preferences \> Experimental \> Gradle** on a Mac) and select
the **Only sync the active variant** checkbox.

<br />

<br />

**Note:** This optimization currently supports projects that include only the Java
programming language. If, for example, the IDE detects Kotlin or C++ code in
your project, it does not automatically enable this optimization, and you should
not enable it manually.

<br />

<br />

For more information, see
[Enable single-variant project sync](https://developer.android.com/studio/build/optimize-your-build#single_variant_sync).

<br />

<br />

#### Provide quick feedback

<br />

<br />

If you've opted into sharing usage statistics to help improve Android Studio,
you'll see these two new icons in the status bar at the bottom of the IDE
window:
![](https://developer.android.com/static/studio/images/releases/user-sentiment-positive.png) ![](https://developer.android.com/static/studio/images/releases/user-sentiment-negative.png)

<br />

<br />

Simply click the icon that best represents your current experience with the IDE.
When you do so, the IDE sends usage statistics that allow the Android Studio
team to better understand your sentiment. In some cases, such as when you
indicate a negative experience with the IDE, you'll have an opportunity to
provide additional feedback.

<br />

<br />

If you haven't already done so, you can enable sharing usage statistics by
opening the **Settings** dialog **Preferences** on a Mac), navigating to
**Appearance \& Behavior \> System Settings \> Data Sharing** and checking
**Send usage statistics to Google**.

<br />

### 3.2 (September 2018)

Android Studio 3.2 is a major release that includes a variety of new features
and improvements.  
**3.2.1 (October 2018)**

This update to Android Studio 3.2 includes the following changes and fixes:

- The bundled Kotlin version is now 1.2.71.
- The default build tools version is now 28.0.3.
- In the Navigation library, argument types have been renamed from `type` to `argType`.
- The following bugs have been fixed:
  - When using the Data Binding library, variable names with underscores were causing compilation errors.
  - CMake was causing IntelliSense and other CLion features to fail.
  - Adding a `SliceProvider` was causing compilation errors in projects that did not use `androidx.*` libraries.
  - Some Kotlin unit tests were not being run.
  - An issue with data binding was causing a `PsiInvalidElementAccessException`.
  - `<merge>` elements were sometimes causing the Layout Editor to crash.

**3.2.0 known issues**

**Note:** These issues have been resolved in Android Studio
3.2.1

- We strongly recommend against using Kotlin version 1.2.70.

  Kotlin version 1.2.61 fixes a bug that can cause Android Studio to hang,
  but **Kotlin 1.2.70 does not include this fix**.

  Kotlin versions 1.2.71 and later, however, do include this fix.
- Although you typically don't need to specify the build tools version,
  when using Android Gradle plugin 3.2.0 with
  `renderscriptSupportModeEnabled` set to `true`, you
  need to include the following in each module's `build.gradle`
  file:

  `android.buildToolsVersion "28.0.3"`

<br />

#### What's New Assistant

A new assistant informs you about the latest changes in Android Studio.

The assistant opens when you start Android Studio after a fresh installation or
update if it detects that there is new information to show. You can also open
the assistant by choosing **Help \> What's new in Android Studio**.

<br />

<br />

#### Android Jetpack

Android Jetpack helps to accelerate Android development with components, tools,
and guidance that eliminate repetitive tasks and enable you to more quickly and
easily build high-quality, testable apps. Android Studio includes the following
updates to support Jetpack. For more information, see the
[Jetpack documentation](https://developer.android.com/jetpack).

##### Navigation Editor

The new Navigation Editor integrates with the navigation components of Android
Jetpack to provide a graphical view for creating the navigation structure of
your app. The Navigation Editor simplifies the design and implementation of
navigation between in-app destinations.

In Android Studio 3.2, the Navigation Editor is an experimental feature. To
enable the Navigation Editor, click **File \> Settings**
(**Android Studio \> Preferences** on Mac), select the **Experimental** category
in the left pane, check the box next to **Enable Navigation Editor**, and
restart Android Studio.

To learn more, read the
[Navigation Editor documentation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing).

##### AndroidX migration

As part of Jetpack, we are migrating the Android Support Libraries to a new
Android extension library using the `androidx` namespace. For more
information, see the
[AndroidX overview](https://developer.android.com/topic/libraries/support-library/androidx-overview).

Android Studio 3.2 helps you through this process with a new migration feature.

To migrate an existing project to AndroidX, choose **Refactor \> Migrate to
AndroidX**. If you have any Maven dependencies that have not migrated to the
AndroidX namespace, the Android Studio build system also automatically converts
those project dependencies.

The Android Gradle plugin provides the following global flags that you can set
in your `gradle.properties` file:

- `android.useAndroidX`: When set to `true`, this flag indicates that you want to start using AndroidX from now on. If the flag is absent, Android Studio behaves as if the flag were set to `false`.
- `android.enableJetifier`: When set to `true`, this flag indicates that you want to have tool support (from the Android Gradle plugin) to automatically convert existing third-party libraries as if they were written for AndroidX. If the flag is absent, Android Studio behaves as if the flag were set to `false`.

Both flags are set to `true` when you use the
**Migrate to AndroidX** command.

If you want to start using AndroidX libraries immediately and don't need to
convert existing third-party libraries, you can set the
`android.useAndroidX` flag to `true` and the
`android.enableJetifier` flag to `false`.

<br />

<br />

#### Android App Bundle

*Android App Bundle* is a new upload format that includes all of your app's
compiled code and resources, but defers APK generation and signing to the Google
Play Store.

Google Play's new app serving model then uses your
app bundle to generate and serve optimized APKs for each user's device
configuration, so each user downloads only the code and resources they need to
run your app. You no longer need to build, sign, and manage multiple APKs, and
users get smaller, more optimized downloads.

Additionally, you can add feature modules to your app project and
include them in your app bundle. Your users can then
download and install your app's features on demand.

To build a bundle, choose **Build \> Build Bundle(s) / APK(s) \> Build Bundle(s)**.

For more information, including instructions for building and analyzing an
Android App Bundle, see
[Android App Bundle](https://developer.android.com/platform/technology/app-bundle).

<br />

<br />

#### Sample data in Layout Editor

Many Android layouts have runtime data that can make it difficult to visualize
the look and feel of a layout during the design stage of app development. You
can now easily see a preview of your view in the Layout Editor filled with
sample data. When you add a view, a button
![](https://developer.android.com/static/studio/images/buttons/layout-editor-wrench.png)
appears below the view in the Design window. Click this button to set the
design-time view attributes. You can choose
from a variety of sample data templates and specify the number of sample items
with which to populate the view.

To try using sample data, add a
[`RecyclerView`](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView)
to a new layout, click the design-time attributes button
![](https://developer.android.com/static/studio/images/buttons/layout-editor-wrench.png)
below the view, and choose a selection from the carousel of sample data
templates.

<br />

<br />

#### Slices

*Slices* provide a new way to embed portions of your app's functionality in
other user interface surfaces on Android. For example, Slices make it possible
to show app functionality and content in Google Search suggestions.

Android Studio 3.2 has a built-in template to help you to extend your app with
the new Slice Provider APIs, as well as new lint checks to ensure that you're
following best practices when constructing the Slices.

To get started right-click a project folder and choose
**New \> Other \> Slice Provider**.

To learn more, including how to test your Slice interactions, read the [Slices
getting started guide](https://developer.android.com/guide/slices/getting-started).

<br />

<br />

#### Kotlin 1.2.61

Android Studio 3.2 bundles Kotlin 1.2.61, and the new Android SDK integrates
better with Kotlin. For more information, see the
[Android Developers blog](https://android-developers.googleblog.com/2018/08/android-pie-sdk-is-now-more-kotlin.html).

<br />

<br />

#### IntelliJ IDEA 2018.1.6

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the
[2018.1.6 release](https://blog.jetbrains.com/idea/2018/07/intellij-idea-2018-1-6-is-released/).

<br />

<br />

#### Android profilers

Try the following new [Android Profiler](https://developer.android.com/studio/profile/android-profiler)
features in Android Studio 3.2.

##### Sessions

You can now save Profiler data as
[sessions](https://developer.android.com/studio/profile/android-profiler#sessions) to revisit and
inspect later. The profiler keeps your session data until you restart the IDE.

When you [record a method trace](https://developer.android.com/studio/profile/cpu-profiler#method_traces) or
[capture a heap dump](https://developer.android.com/studio/profile/memory-profiler#capture-heap-dump), the IDE adds that data (along with your app's network
activity) as a separate entry to the current session, and you can easily switch
back and forth between recordings to compare data.

##### System Trace

In the [CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler), select the
new **System Trace** configuration to inspect your device's system CPU and
thread activity. This trace configuration is built on
[`systrace`](https://developer.android.com/studio/command-line/systrace)
and is useful for investigating system-level issues, such as UI jank.

While using this trace configuration, you can visually mark important code
routines in the profiler timeline by instrumenting your C/C++ code with the
[native tracing API](https://developer.android.com/ndk/guides/tracing) or your Java code with the
[`Trace`](https://developer.android.com/reference/android/os/Trace) class.

##### Inspect JNI references in the Memory Profiler

If you deploy your app to a device running Android 8.0 (API level 26) or higher,
you can now inspect memory allocations for your app's JNI code using the
[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler).

While your app is running, select a portion of the timeline that you want to
inspect and select **JNI heap** from the drop-down menu above the class list, as
shown below. You can then inspect objects in the heap as you normally would and
double-click objects in the **Allocation Call Stack** tab to see where the JNI
references are allocated and released in your code.
![](https://developer.android.com/static/studio/images/releases/memory-profiler-jni-heap_2x.png)

##### Import, export, and inspect memory heap dump files

You can now import, export, and inspect `.hprof` memory heap dump files created
with the [Memory Profiler](https://developer.android.com/studio/profile/memory-profiler).

Import your `.hprof` file by clicking **Start new profiler session**
![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) in the
profiler's **Sessions** pane and then selecting **Load from file**. You can then
inspect its data in the Memory Profiler as you would any other heap dump.

To save heap dump data to review later, use the **Export Heap Dump** button at
the right of the **Heap Dump** entry in the **Sessions** pane. In the
**Export As** dialog that appears, save the file with the `.hprof` filename
extension.

##### Record CPU activity during app startup

You can now record CPU activity during your app's startup, as follows:

1. Select **Run \> Edit Configurations** from the main menu.
2. Under the **Profiling** tab of your desired run configuration, check the box next to **Start recording a method trace on startup**.
3. Select a CPU recording configuration to use from the dropdown menu.
4. Deploy your app to a device running Android 8.0 (API level 26) or higher by selecting **Run \> Profile**.

##### Export CPU traces

After you record CPU activity with the CPU Profiler, you can export the data as
a `.trace` file to share with others or inspect later.

To export a trace after you've recorded CPU activity, do the following:

1. Right-click on the recording you want to export from the CPU timeline.
2. Select **Export trace** from the dropdown menu.
3. Navigate to where you want to save the file and click **Save**.

##### Import and inspect CPU trace files

You can now import and inspect `.trace` files created with the
[Debug API](https://developer.android.com/reference/android/os/Debug) or
[CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler#method_traces). (Currently, you
can't import System Trace recordings.)

Import your trace file by clicking **Start new profiler session**
![](https://developer.android.com/static/studio/images/buttons/ic_plus.png) in the
profiler's **Sessions** pane and then selecting
**Load from file**. You can then
inspect its data in the CPU Profiler similar to how you normally would, with the
following exceptions:

- CPU activity is not represented along the CPU timeline.
- The thread activity timeline indicates only where trace data is available for each thread and not actual thread states (such as running, waiting, or sleeping).

##### Record CPU activity using the Debug API

You can now start and stop recording CPU activity in the CPU Profiler by
instrumenting your app with the [Debug API](https://developer.android.com/reference/android/os/Debug). After
you deploy your app to a device, the profiler automatically starts recording CPU
activity when your app calls
[`startMethodTracing(String tracePath)`](https://developer.android.com/reference/android/os/Debug#startMethodTracing(java.lang.String)),
and the profiler stops recording when your app calls
[`stopMethodTracing()`](https://developer.android.com/reference/android/os/Debug#stopMethodTracing()). While
recording CPU activity that's triggered using this API, the CPU Profiler shows
**Debug API** as the selected CPU recording configuration.

##### Energy Profiler

The [Energy Profiler](https://developer.android.com/studio/profile/energy-profiler) displays a visualization of the
estimated energy usage of your app, as well as system events that affect energy
usage, such as wakelocks, alarms, and jobs.

The Energy Profiler appears as a new row at the bottom of the **Profiler**
window when you run your app on a connected device or Android Emulator running
Android 8.0 (API 26) or higher.

Click the **Energy** row to maximize the Energy Profiler view. Place your mouse
pointer over a bar in the timeline to see a breakdown of energy use by CPU,
network, and location (GPS) resources, as well as relevant system events.

System events that affect energy usage are indicated in the **System** timeline
below the **Energy** timeline. Details of system events within the specified
time range are shown in the event pane when you select a time range in the
**Energy** timeline.

To see the call stack and other details for a system event, such as a wakelock,
select it in the event pane. To go to the code responsible for a system event,
double-click the entry in the call stack.

<br />

<br />

#### Lint checking

Android Studio 3.2 includes many new and improved features for
[lint checking](https://developer.android.com/studio/write/lint).

The new lint checks help you to find and identify common code problems, ranging
from warnings about potential usability issues to high-priority errors regarding
potential security vulnerabilities.

##### Lint checks for Java/Kotlin interoperability

To make sure that your Java code interoperates well with your Kotlin code, new
lint checks enforce the best practices described in the
[Kotlin Interop Guide](https://android.github.io/kotlin-guides/interop.html).
Examples of these checks include looking for the presence of Nullability
annotations, use of Kotlin hard keywords, and placing lambda parameters last.

To enable these checks, click **File \> Settings** (**Android Studio \> Preferences**
on Mac) to open the **Settings** dialog, navigate to the
**Editor \> Inspections \> Android \> Lint \> Interoperability \> Kotlin Interoperability**
section, and select the rules that you want to enable.
![](https://developer.android.com/static/studio/images/releases/java-kotlin-interop.png)

To enable these checks for command-line builds, add the following to your
`build.gradle` file:  

            android {
                lintOptions {
                    check 'Interoperability'
                }
            }
            
          
##### Lint checks for Slices

New lint checks for Slices help to ensure that you are constructing Slices
correctly. For example, lint checks warn you if you have not assigned a primary
action to a Slice.

##### New Gradle target

Use the new `lintFix` Gradle task to apply all of the *safe*
fixes suggested by the lint check directly to the source code. An example of a
lint check that suggests a safe fix to apply is `SyntheticAccessor`.

##### Metadata updates

Various metadata, such as the service cast check, have been updated for lint
checks to work with Android 9 (API level 28).

##### Warning if running lint on a new variant

Lint now records which variant and version a baseline is recorded with, and lint
warns you if you run it on a different variant than the one with which the
baseline was created.

##### Improvements to existing lint checks

Android Studio 3.2 includes many improvements to existing lint checks. For
example, the resource cycle checks now apply to additional resource types, and
the translation detector can find missing translations on the fly, in the
editor.

##### Issue IDs more discoverable

Issue IDs are now shown in more places now, including in the **Inspection
Results** window. This makes it easier for you to find the information that you
need to enable or disable specific checks through `lintOptions` in
`build.gradle`.

For more information, see
[Configure lint options with Gradle](https://developer.android.com/studio/write/lint#gradle).

<br />

<br />

#### Data Binding V2

Data Binding V2 is now enabled by default and is compatible with V1. This means
that, if you have library dependencies that you compiled with V1, you can use
them with projects using Data Binding V2. However, note that projects using V1
cannot consume dependencies that were compiled with V2.

<br />

<br />

#### D8 desugaring

In Android Studio 3.1, we integrated the desugaring step into the D8 tool as an
experimental feature, reducing overall build time. In Android Studio 3.2,
desugaring with D8 is turned on by default.

<br />

<br />

#### New code shrinker

R8 is a new tool for code shrinking and obfuscation that replaces ProGuard. You
can start using the preview version of R8 by including the following in your
project's `gradle.properties` file:  

          android.enableR8 = true
        
<br />

<br />

#### Changed default ABIs for multi-APKs

When [building multiple APKs](https://developer.android.com/studio/build/configure-apk-splits) that
each target a different ABI, the plugin no longer generates APKs for the
following ABIs by default: `mips`, `mips64`, and `armeabi`.

If you want to build APKs that target these ABIs, you must use
[NDK r16b or lower](https://developer.android.com/ndk/downloads/revision_history) and specify the ABIs
in your `build.gradle` file, as shown below:  

```groovy
    splits {
        abi {
            include 'armeabi', 'mips', 'mips64'
            ...
        }
    }
    
```  

```kotlin
    splits {
        abi {
            include("armeabi", "mips", "mips64")
            ...
        }
    }
    
```

**Note:** This behavior change is also included in Android Studio 3.1 RC1 and
higher.

<br />

<br />

#### Improved editor features for CMake build files

If you use CMake to
[add C and C++ code to your project](https://developer.android.com/studio/projects/add-native-code),
Android Studio now includes improved editor features to help you to edit your
CMake build scripts, such as the following:

- **Syntax highlighting and code completion:** The IDE now highlights and suggests code completion for common CMake commands. Additionally, you can navigate to a file by clicking it while pressing the Control key (Command on Mac).
- **Code reformatting:** You can now use IntelliJ's code reformat option to apply code styles to your CMake build scripts.
- **Safe refactoring:** The IDE's built-in refactoring tools now also check if you are renaming or deleting files that you reference in your CMake build scripts.

<br />

<br />

#### Navigate external header files

When using the **Project** window in previous versions of Android Studio, you
could navigate and inspect only the header files that belong to libraries you
build from a local project. With this release, you can now also view and inspect
header files included with external C/C++ library dependencies that you import
into your app project.

If you already
[include C/C++ code and libraries in your project](https://developer.android.com/studio/projects/add-native-code),
open the **Project** window on the left side of the IDE by selecting
**View \> Tool Windows \> Project** from the main menu and select **Android** from
the drop-down menu. In the **cpp** directory, all headers that are within the
scope of your app project are organized under the **include** node for each of
your local C/C++ library dependencies, as shown below.
![](https://developer.android.com/static/studio/images/releases/project-include-nodes.png)

<br />

<br />

#### Native multidex enabled by default

Previous versions of Android Studio enabled native multidex when deploying the
debug version of an app to a device running Android API level 21 or higher. Now,
whether you're deploying to a device or building an APK for release, the Android
plugin for Gradle enables native multidex for all modules that set
`minSdkVersion=21` or higher.

<br />

<br />

#### AAPT2 moved to Google's Maven repository

Beginning with Android Studio 3.2, the source for
[AAPT2 (Android Asset Packaging Tool 2)](https://developer.android.com/studio/command-line/aapt2)
is Google's Maven repository.

To use AAPT2, make sure that you have a `google()` dependency in your
`build.gradle` file, as shown here:  

```groovy
    buildscript {
        repositories {
            google() // here
            jcenter()
        }
        dependencies {
            classpath 'com.android.tools.build:gradle:3.2.0'
        }
    }
    allprojects {
        repositories {
            google() // and here
            jcenter()
        }
    }
    
```  

```kotlin
    buildscript {
        repositories {
            google() // here
            jcenter()
        }
        dependencies {
            classpath("com.android.tools.build:gradle:3.2.0")
        }
    }
    allprojects {
        repositories {
            google() // and here
            jcenter()
        }
    }
    
```

The new version of AAPT2 fixes many issues, including improved handling of
non-ASCII characters on Windows.

<br />

<br />

#### Removal of configuration on demand

The **Configure on demand** preference has been removed from Android Studio.

Android Studio no longer passes the `--configure-on-demand`
argument to Gradle.

<br />

<br />

#### ADB Connection Assistant

The new [ADB Connection Assistant](https://developer.android.com/studio/run/device#assistant)
provides step-by-step instructions to help you set up and use a device over the
*Android Debug Bridge (ADB)* connection.

To start the assistant, choose **Tools \> Connection Assistant**.

The ADB Connection Assistant provides instructions, in-context controls, and
a list of connected devices in a series of pages in the **Assistant** panel.

<br />

#### Emulator improvements

You can now save and load snapshots of an AVD (Android virtual device) at
any time in the Android Emulator, making it fast and easy to return an
emulated device to a known state for testing. When you edit an AVD using the AVD
Manager, you can specify which AVD snapshot to load when the AVD starts.

Controls for saving, loading, and managing AVD snapshots are now in the
**Snapshots** tab in the emulator's **Extended controls** window.

For details, see [Snapshots](https://developer.android.com/studio/run/advanced-emulator-usage#snapshots).

For additional information on what's new and changed in the Emulator, see the
[Emulator release notes](https://developer.android.com/studio/releases/emulator).

<br />

### 3.1 (March 2018)

Android Studio 3.1.0 is a major release that includes a variety of new
features and improvements.  
**3.1.4 (August 2018)**

This update to Android Studio 3.1 includes the following changes and fixes:

- The bundled Kotlin is now version 1.2.50.
- New projects are created with `kotlin-stdlib-jdk* artifacts`, rather than with `kotlin-stdlib-jre*` artifacts, which are deprecated.
- R8 parsing of ProGuard rules has been improved.
- The following bugs have been fixed:
  - Attempting to run the Kotlin Main class failed with an error: `"Error: Could not find or load main class..."`
  - R8 entered an infinite loop while performing certain optimizations.
  - Using the **Rerun failed tests** command in the **Run** window sometimes incorrectly returned the message "No tests were found".
  - D8 did not correctly handle `invoke-virtual` instances, causing a crash with a `VerifyError`: `invoke-super/virtual can't be used on private method`
  - The Data Binding compiler was depending on an old version of `com.android.tools:annotations`. The compiler now uses tools annotations from the base project when available.
  - Android Studio crashed during fragment transitions when using profilers.
  - The debugger crashed when debugging a layout with a text box.
  - D8 failed to read some ZIP files with special characters.

**3.1.3 (June 2018)**

This update to Android Studio 3.1 includes fixes for the following bugs:

- Memory leaks caused Android Studio to become slow and unresponsive after you had been using the Layout Editor. This update includes fixes for most of these issues. We intend to release another update soon to address additional memory leaks.
- Some applications built with D8 crashed on some Verizon Ellipsis tablets.
- Installation of applications built with D8 failed with an `INSTALL_FAILED_DEXOPT` error on devices running Android 5.0 or 5.1 (API level 21 or 22).
- Some applications that used the OkHttp library and were built with D8 crashed on devices running Android 4.4 (API level 19).
- Android Studio sometimes failed to start, with a `ProcessCanceledException` during class initialization for `com.intellij.psi.jsp.JspElementType`.

**3.1.2 (April 2018)**

This update to Android Studio 3.1 includes fixes for the following bugs:

- In some cases, Android Studio hung indefinitely during exit.
- Builds configured with [source sets](https://developer.android.com/studio/build/build-variants#sourcesets)
  failed with the following message when Instant Run was enabled:

  `"The SourceSet `<var translate="no">name</var>` is not recognized by the
  Android Gradle Plugin."`
- When Instant Run was enabled, builds of new Kotlin projects failed when triggered by the **Run** command.
- During editing of the `build.gradle` file, there was sometimes a noticeable delay between typing a character and the character appearing on the screen.
- Build failures occurred during dexing in some projects with large
  numbers of modules or external dependencies, with the following error
  message:

  `"RejectedExecutionException: Thread limit exceeded replacing
  blocked worker"`
- The computation of the D8 main DEX list was not taking into account some reflective invocations.

This update also includes changes that make running lint checks from Gradle
much faster in some scenarios.

**3.1.1 (April 2018)**

This update to Android Studio 3.1 includes fixes for the following bugs:

- In some cases, when a project created in Android Studio 3.0 was opened
  for the first time in Android Studio 3.1, the Gradle-aware Make task
  was removed from the **Before launch** area in **Run/Debug
  Configurations** . The result was that projects did not build when the
  **Run** or **Debug** button was clicked, which in turn caused
  failures such as deployment of incorrect APKs and crashes when using
  Instant Run.

  To solve this problem, Android Studio 3.1.1 adds the Gradle-aware Make
  task to the run configuration for projects that are missing this entry.
  This modification occurs after the first Gradle sync when the project is
  loaded.
- The debugger crashed when debugging a layout with a text box if advanced profiling was enabled.
- Android Studio froze after you clicked **Build Variants**.
- AAR (Android archive) files were extracted twice, once during the Gradle sync process and once during the Gradle build process.
- Elements were missing from some vector drawables imported from SVG files.
- The warning regarding the deprecation of the `compile` dependency configuration has been updated with better guidance regarding the `implementation` and `api` configurations. For details of migrating away from using the `compile` configuration, see the [documentation for the new dependency configurations](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration#new_configurations).

<br />

#### Coding/IDE

##### IntelliJ 2017.3.3

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the 2017.3.3 release. Improvements include better control flow
analysis for collections and strings, improved nullability inference, new quick
fixes, and much more.

For details, see the JetBrains release notes for IntelliJ IDEA versions
[2017.2](https://www.jetbrains.com/idea/whatsnew/#v2017-2) and
[2017.3](https://www.jetbrains.com/idea/whatsnew/#v2017-3), as
well as the JetBrains release notes for
[bug-fix updates](https://blog.jetbrains.com/idea/2018/01/intellij-idea-2017-3-3-is-released/).

##### SQL editing improvements with
Room

When you use the
[Room database library](https://developer.android.com/topic/libraries/architecture/room),
you can take advantage of several improvements to SQL editing:

- Code completion within a [`Query`](https://developer.android.com/reference/androidx/room/Query) understands SQL tables (entities), columns, query parameters, aliases, joins, subqueries, and WITH clauses.
- SQL syntax highlighting now works.
- You can right-click a table name in SQL and rename it, which also rewrites the corresponding Java or Kotlin code (including, for example, the return type of the query). Renaming works in the other direction, too, so renaming a Java class or field rewrites the corresponding SQL code.
- SQL usages are shown when using **Find usages** (right-click and choose **Find usages** from the context menu).
- To navigate to an SQL entity's declaration in Java or Kotlin code, you can hold Control (Command on Mac) while clicking the entity.

For information on using SQL with Room, see
[Save data in a local
database using Room](https://developer.android.com/training/data-storage/room).

##### Updates to data
binding

This update includes several improvements for
[data binding](https://developer.android.com/topic/libraries/data-binding):

- You can now use a
  [`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData)
  object as an observable field in data binding expressions. The
  [`ViewDataBinding`](https://developer.android.com/reference/androidx/databinding/ViewDataBinding)
  class now includes a new `setLifecycle()` method that you use
  to observe
  [`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData)
  objects.

- The
  [`ObservableField`](https://developer.android.com/reference/androidx/databinding/ObservableField)
  class can now accept other
  [`Observable`](https://developer.android.com/reference/androidx/databinding/Observable)
  objects in its constructor.

- You can preview a new incremental compiler for your data binding
  classes. For details of this new compiler and instructions for enabling
  it, see
  [Data Binding Compiler V2](https://developer.android.com/topic/libraries/data-binding#enable_v2).

  Benefits of the new compiler include the following:
  - `ViewBinding` classes are generated by the Android Plugin for Gradle before the Java compiler.
  - Libraries keep their generated binding classes when the app is compiled, rather than being regenerated each time. This can greatly improve performance for multi-module projects.

<br />

<br />

#### Compiler and Gradle

##### D8 is the default DEX
compiler

The D8 compiler is now used by default for generating DEX bytecode.

This new DEX compiler brings with it several benefits, including the
following:

- Faster dexing
- Lower memory usage
- Improved code generation (better register allocation, smarter string tables)
- Better debugging experience when stepping through code

You don't need to make any changes to your code or your development
workflow to get these benefits, unless you had previously manually
disabled the D8 compiler.

If you set `android.enableD8` to `false` in your
`gradle.properties`, either delete that flag or set it to
`true`:  

            android.enableD8=true
          
For details, see
[New DEX compiler](https://developer.android.com/studio/releases/gradle-plugin#D8).

##### Incremental
desugaring

For projects that use
[Java 8 language features](https://developer.android.com/studio/write/java8-support),
incremental desugaring is enabled by default, which can improve build
times.

Desugaring converts
[syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar)
into a form that the compiler can process more efficiently.

You can disable incremental desugaring by specifying the following in
your project's `gradle.properties` file:  

            android.enableIncrementalDesugaring=false
          
##### Simplified output window

The **Gradle Console** has been replaced with the **Build**
window, which has **Sync** and **Build** tabs.

For details about how to use the new, simplified **Build** window,
see[Monitor the build
process](https://developer.android.com/studio/run#gradle-console).

##### Batch updates and indexing
concurrency

The Gradle sync and IDE indexing processes are now much more efficient,
reducing time wasted on many redundant indexing operations.

<br />

<br />

#### C++ and LLDB

We have made many quality and performance improvements in the coding, syncing,
building, and debugging phases of C++ development. Improvements include the
following:

- If you work with large C++ projects, you should notice a significant improvement
  in the reduction of time spent building symbols. Sync time is also greatly
  reduced for large projects.

- Performance when building and syncing with CMake has been improved through
  more aggressive reuse of cached results.

- The addition of formatters ("pretty printers") for more C++ data structures
  makes LLDB output easier to read.

- [LLDB](https://developer.android.com/studio/debug) now works with only Android 4.1 (API level 16)
  and higher.

**Note:** Native debugging with Android Studio 3.0 or
greater does not work on 32-bit Windows. If you are using 32-bit Windows and
need to debug native code, use Android Studio 2.3.

<br />

<br />

#### Kotlin

##### Kotlin upgraded to version 1.2.30

Android Studio 3.1 includes
[Kotlin
version 1.2.30](https://blog.jetbrains.com/kotlin/2018/03/kotlin-1-2-30-is-out/).

##### Kotlin code now analyzed with
command-line lint check

[Running lint from the
command line](https://developer.android.com/studio/write/lint#commandline) now analyzes your Kotlin classes.

For each project that you would like to run lint on,
[Google's Maven
repository](https://developer.android.com/studio/build/dependencies#google-maven) must be included in the top-level `build.gradle`
file. The Maven repository is already included for projects created in
Android Studio 3.0 and higher.

<br />

<br />

#### Performance tools

##### Sample native C++ processes with CPU Profiler

The [CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler) now
includes a default configuration to record sampled traces of your app's
native threads. You can use this configuration by deploying your app to a
device running Android 8.0 (API level 26) or higher and then selecting
**Sampled (Native)** from the CPU Profiler's recording
configurations dropdown menu. After that,
[record and
inspect a trace](https://developer.android.com/studio/profile/cpu-profiler#method_traces) as you normally would.

You can change default settings, such as the sampling interval, by
[creating a
recording configuration](https://developer.android.com/studio/profile/cpu-profiler#configurations).

To switch back to tracing your Java threads, select either a
**Sampled (Java)** or **Instrumented (Java)**
configuration.

##### Filter CPU traces, memory
allocation results, and heap dumps

The [CPU Profiler](https://developer.android.com/studio/profile/cpu-profiler) and
[Memory Profiler](https://developer.android.com/studio/profile/memory-profiler) include
a search feature that allows you to filter results from recording a method
trace, memory allocations, or heap dump.
![](https://developer.android.com/static/studio/images/releases/cpu-profiler-method-filter_1x.png)

To search, click **Filter**
![](https://developer.android.com/static/studio/images/buttons/profiler_filter.png) in the top-right corner of the pane, type
your query, and press Enter.


**Tip:** You can also open the search field by pressing Control + F
(Command + F on Mac).

In the CPU Profiler's **Flame Chart** tab, call stacks that include
methods related to your search query are highlighted and moved to the left
side of the chart.

For more information on filtering by method, class, or package name, see
[Record and inspect method traces](https://developer.android.com/studio/profile/cpu-profiler#method_traces).

##### Request tab in the Network Profiler

The [Network Profiler](https://developer.android.com/studio/profile/network-profiler)
now includes a **Request** tab that provides details about network
requests during the selected timeline. In previous versions, the Network
Profiler only provided information about network responses.

##### Thread View in the Network Profiler

After selecting a portion of the timeline in the
[Network Profiler](https://developer.android.com/studio/profile/network-profiler), you can select one of
the following tabs to see more detail about the network activity during that
timeframe:

- **Connection View**: Provides the same information as previous versions of Android Studio---it lists files that were sent or received during the selected portion of the timeline across all of your app's CPU threads. For each request, you can inspect the size, type, status, and transmission duration.
- **Thread View**: Displays network activity of each of your app's CPU threads. This view allows you to inspect which of your app's threads are responsible for each network request.

![](https://developer.android.com/static/studio/images/profile/network_profiler_thread_view-2X.png)

<br />

<br />

#### Layout Inspector

The [Layout Inspector](https://developer.android.com/studio/debug/layout-inspector) gained new
features, including some functionality previously provided by the deprecated
Hierarchy Viewer and Pixel Perfect tools:

- Zoom buttons and keyboard shortcuts for navigating and inspecting layouts
- Reference grid overlay
- Ability to load a reference image and use it as an overlay (useful for comparing your layout with a UI mockup)
- **Render subtree preview** to isolate a view in a complex layout

![](https://developer.android.com/static/studio/images/releases/layout-editor-add-constraint-left-below_2x.png)

<br />

<br />

#### Layout Editor

The **Palette** in the
[Layout Editor](https://developer.android.com/studio/write/layout-editor#convert-view)
has received many improvements:

- Reorganization of categories for views and layouts.
- New **Common** category for views and layouts, which you can add to with a **Favorite** command.
- Improved [search for views
  and layouts](https://developer.android.com/studio/write/layout-editor#views-palette).
- New commands for [opening
  documentation](https://developer.android.com/studio/write/layout-editor#palette-documentation) for a specific view or layout element.

You can use the new [**Convert view**](https://developer.android.com/studio/write/layout-editor#convert-view)
command in the **Component tree** or design editor to convert a view or layout
to another type of view or layout.

You can now easily create constraints to items near the selected view using the
new Create a connection ![](https://developer.android.com/static/studio/images/buttons/attributes-plus-icon_2x.png)
buttons in the view inspector at the top of the **Attributes** window.

<br />

<br />

#### Run and Instant Run

The behavior of the **Use same selection for future
launches** option in the **Select deployment target**
dialog has been made more consistent. If the **Use same
selection** option is enabled, then the **Select deployment
target** dialog opens only the first time that you use the
**Run** command until the selected device is no longer
connected.

When targeting a device running Android 8.0 (API level 26) or higher,
[Instant Run](https://developer.android.com/studio/run#instant-run) can deploy
changes to resources without causing an application restart. This is
possible because the resources are contained in a split APK.

<br />

<br />

#### Emulator

For details of what's new and changed in the emulator since Android
Studio 3.0, see the Android Emulator release notes from
[version 27.0.2](https://developer.android.com/studio/releases/emulator#27-0-2)
through [version 27.1.12](https://developer.android.com/studio/releases/emulator#27-1-12).

Major improvements include the following:

- Quick Boot snapshots for saving of emulator state and faster start, with the ability to use the **Save now** command to save a custom start state.
- Windowless emulator screen.
- System images for Android 8.0 (API level 26), Android 8.1 (API level 27), and Android P Developer Preview.

<br />

<br />

#### User interface and user experience
improvements

##### More tooltips, keyboard shortcuts,
and helpful messages

We have added tooltips and helpful message overlays in many places
throughout Android Studio.

To see keyboard shortcuts for many commands, just hold the mouse
pointer over a button until the tooltip appears.

##### Tools \> Android menu removed

The **Tools \> Android** menu has been removed. Commands
that were previously under this menu have been moved.

- Many commands moved to directly under the **Tools** menu.
- The **Sync project with gradle files** command moved to the **File** menu.
- The **Device Monitor** command has been removed, as described below.

<br />

<br />

#### Device Monitor available
from the command line

In Android Studio 3.1, the Device Monitor serves less of a role than it
previously did. In many cases, the functionality available through the
Device Monitor is now provided by new and improved tools.

See the
[Device Monitor documentation](https://developer.android.com/studio/profile/monitor) for
instructions for invoking the Device Monitor from the command line and for
details of the tools available through the Device Monitor.

<br />

### 3.0 (October 2017)

Android Studio 3.0.0 is a major release that includes a variety of new
features and improvements.  


**macOS users:** If you are updating an older version of Android Studio,
you may encounter an update error dialog that says "Some conflicts were
found in the installation area". Simply ignore this error and click
**Cancel** to resume the installation.  

**3.0.1 (November 2017)**


This is a minor update to Android Studio 3.0 that includes general bug
fixes and performance improvements.

#### Android Plugin for Gradle 3.0.0

The new [Android plugin for Gradle](https://developer.android.com/studio/releases/gradle-plugin)
includes a variety of improvements and new features, but it primarily improves
build performance for projects that have a large number of modules. When using
the new plugin with these large projects, you should experience the following:

- Faster build configuration times due to new delayed dependency resolution.
- [Variant-aware dependency resolution](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration#variant_aware) for only the projects and variants you are building.
- Faster incremental build times when applying simple changes to code or resources.

Note: These improvements required significant changes that break some of the
plugin's behaviors, DSL, and APIs. [Upgrading to version 3.0.0](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration) might require
changes to your build files and Gradle plugins.

This version also includes the following:

- Support for Android 8.0.
- Support for building separate APKs based on language resources.
- Support for [Java 8 libraries and Java 8 language features](https://developer.android.com/studio/write/java8-support) (without the Jack compiler).
- Support for Android Test Support Library 1.0 (Android Test Utility and [Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator)).
- Improved ndk-build and cmake build speeds.
- Improved Gradle sync speed.
- AAPT2 is now enabled by default.
- Using `ndkCompile` is now more restricted. You should instead migrate to using either CMake or ndk-build to compile native code that you want to package into your APK. To learn more, read [Migrate from ndkcompile](https://developer.android.com/studio/projects/add-native-code#ndkCompile).

For more information about what's changed, see the [Android Plugin for Gradle
release notes](https://developer.android.com/studio/releases/gradle-plugin#3-0-0).

If you're ready to upgrade to the new plugin, see
[Migrate to Android Plugin for Gradle 3.0.0](https://developer.android.com/studio/build/gradle-plugin-3-0-0-migration).

#### Kotlin support

As [announced at Google I/O 2017](https://android-developers.googleblog.com/2017/05/android-announces-support-for-kotlin.html),
the Kotlin programming language is now officially supported on Android.
So with this release, Android Studio includes Kotlin language
support for Android development.

You can incorporate Kotlin into your project by converting a Java file to Kotlin
(click **Code \> Convert Java File to Kotlin File**) or by creating a new Kotlin-
enabled project using the New Project wizard.

To get started,
read how to [add Kotlin to your project](https://developer.android.com/studio/projects/add-kotlin).
![](https://developer.android.com/static/studio/images/releases/kotlin-convert_2x.png)

#### Java 8 language features support

You can now use certain Java 8 language features and
consume libraries built with Java 8. **Jack is no longer required** , and you
should first [disable Jack](https://developer.android.com/studio/write/java8-support#disable_jack)
to use the improved Java 8 support built into the default toolchain.

To update your project to support the new Java 8 language toolchain,
update the **Source Compatibility** and **Target Compatibility** to 1.8
in the **Project Structure** dialog (click **File \> Project Structure** ).
To learn more, read how to
[use Java 8 language features](https://developer.android.com/studio/write/java8-support).
![](https://developer.android.com/static/studio/images/projects/project-java-compatibility_2x.png)

#### Android Profiler

The new Android Profiler **replaces the Android Monitor tool** and provides a
new suite of tools to measure your app's CPU, memory, and network usage in
realtime. You can perform sample-based method tracing to time your code
execution, capture heap dumps, view memory allocations, and inspect the details
of network-transmitted files.

To open, click **View \> Tool Windows \> Android Profiler**
(or click **Android Profiler** in the toolbar).

The event timeline at the top of the window shows touch events, key
presses, and activity changes so you have more context to understand other
performance events in the timeline.

Note: The [Logcat](https://developer.android.com/studio/debug/am-logcat) view also moved to a
separate window (it was previously inside Android Monitor, which was removed).
![](https://developer.android.com/static/studio/images/profile/android-profiler-overview_2x.png)

From the Android Profiler's overview timeline, click on the **CPU** , **MEMORY** ,
or **NETWORK** timelines to access the corresponding profiler tools.

##### CPU Profiler

The CPU Profiler helps you analyze the CPU thread usage of your app by
triggering a sample or instrumented CPU trace. Then, you can
troubleshoot CPU performance issues using a variety of data views and filters.

For more information, see the [CPU Profiler guide](https://developer.android.com/studio/profile/cpu-profiler).
![](https://developer.android.com/static/studio/images/releases/cpu-profiler_2x.png)

##### Memory Profiler

The Memory Profiler helps you identify memory leaks and memory churn that can
lead to stutter, freezes, and even app crashes. It shows a realtime graph of
your app's memory use, lets you capture a heap dump, force garbage collections,
and track memory allocations.

For more information, see the [Memory Profiler guide](https://developer.android.com/studio/profile/memory-profiler).
![](https://developer.android.com/static/studio/images/releases/memory-profiler_2x.png)

##### Network Profiler

The Network Profiler allows you to monitor the network activity of your app,
inspect the payload of each of your network requests, and link back to the
code that generated the network request.

For more information, see the [Network Profiler guide](https://developer.android.com/studio/profile/network-profiler).
![](https://developer.android.com/static/studio/images/releases/network-profiler_2x.png)

#### APK profiling and debugging

Android Studio now allows you to **profile and debug any
APK** without having to build it from an Android Studio project---as long as the
APK is built to [enable debugging](https://developer.android.com/studio/debug#enable-debug) and
you have access to the debug symbols and source files.

To get started, click **Profile or debug APK** from the
Android Studio Welcome screen. Or, if you already have a project open, click
**File \> Profile or debug APK** from the menu bar. This displays the
unpacked APK files, but it does not decompile the code.
So, to properly add breakpoints and view stack traces,
you need to attach Java source files and native debug symbols.

For more information, see
[Profile and Debug Pre-built APKs](https://developer.android.com/studio/debug/apk-debugger).
![](https://developer.android.com/static/studio/images/debug/apk-debugging_2x.png)

#### Device File Explorer

The new Device File Explorer allows you to inspect your connected device's
filesystem, and transfer files between the device and your computer.
This replaces the filesystem tool available in DDMS.

To open, click **View \> Tool Windows \> Device File Explorer**.

For more information, see the
[Device File Explorer guide](https://developer.android.com/studio/debug/device-file-explorer).
![](https://developer.android.com/static/studio/images/debug/device-file-explorer_2x.png)

#### Instant Apps support

New support for Android Instant Apps allows you to create Instant Apps in your
project using **two new module types** : Instant App modules and Feature modules
(these require that you [install the Instant Apps Development SDK](https://developer.android.com/topic/instant-apps/getting-started/setup#setup-sdk)).
![](https://developer.android.com/static/studio/images/projects/instant-apps-module_2x.png)

Android Studio also includes a **new modularize refactoring action** to help you
add support for Instant Apps in an existing project. For example, if you want to
refactor your project to place some classes in an Instant App feature module,
select the classes in the **Project** window and click **Refactor \>
Modularize** . In the dialog that appears, select the module where the classes
should go and click **OK**.

And when you're ready to test your Instant App, you can **build and run your
Instant App module** on a connected device by specifying the Instant App's URL
within the [run configuration launch
options](https://developer.android.com/studio/run/rundebugconfig#general-tab): Select **Run \>
Edit Configurations** , select your Instant App module, and then set the URL
under **Launch Options**.

For more information, see
[Android Instant Apps](https://developer.android.com/topic/instant-apps).

#### Android Things modules

New Android Things templates in the New Project and New Module wizards to help
you start developing for Android-powered IOT devices.

For more information, see how to [create an Android Things project](https://developer.android.com/things/training/first-device/create-studio-project).

#### Adaptive Icons wizard

Image Asset Studio now supports [vector drawables](https://developer.android.com/guide/topics/graphics/vector-drawable-resources) and
allows you to create **adaptive launcher icons for
Android 8.0** while simultaneously creating traditional icons ("Legacy" icons)
for older devices.

To start, right-click on the **res** folder in your
project, and then click **New \> Image Asset** . In the **Asset Studio** window,
select **Launcher Icons (Adaptive and Legacy)** as the icon type.

Note: You must set `compileSdkVersion` to 26 or higher to use adaptive launcher
icons.

For more information, read about
[Adaptive Icons](https://developer.android.com/guide/practices/ui_guidelines/icon_design_adaptive).
![](https://developer.android.com/static/studio/images/write/image-asset-studio_2x.png)

#### Support for font resources

To support the new font resources in Android 8.0, Android Studio includes a
**font resources selector** to help bundle fonts into your app or configure
your project to download the fonts on the device (when available). The layout
editor can also **preview the fonts** in your layout.

To try downloadable fonts, ensure that your device or emulator is running
Google Play Services v11.2.63 or higher. For more information, read about
[Downloadable Fonts](https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts).
![](https://developer.android.com/static/studio/images/write/font-download_2x.png)

#### Firebase App Indexing Assistant

The Firebase Assistant has been updated with a new tutorial to test [App
Indexing](https://firebase.google.com/docs/app-indexing/).
To open the Assistant, select **Tools \> Firebase** .
Then select **App Indexing \> Test App Indexing**.

The tutorial includes new
buttons to test your public and personal content indexing:

- In step 2, click **Preview search results** to verify that your URLs are showing up in Google Search results.
- In step 3, click **Check for errors** to verify that the indexable objects in your app have been added to the personal content index.

#### Android App Links Assistant

The [App Links Assistant](https://developer.android.com/studio/write/app-link-indexing)
has been updated with the following new capabilities:

- **Add URL tests** for each URL mapping to be sure your intent filters
  handle real-world URLs.

  <br />

  You can also define these URL tests by hand using the `<tools:validation>`
  tag described below.
- **Create a Digital Asset Links file** with the appropriate object entry to
  support [Google Smart Lock](https://developers.google.com/identity/smartlock-passwords/android/),
  and add the corresponding `asset_statements` `<meta-data>` tag to your
  manifest file.

![](https://developer.android.com/static/studio/images/write/applinks-smartlock-callout_2x.png)

#### URL intent-filter validator

Android Studio now supports a special tag in the manifest file that allows you
to **test your intent filter URLs** . These are the same tags that the [App Links
Assistant can create for you](https://developer.android.com/studio/releases/archives#app-links-assistant).

To declare a test URL
for an intent filter, add a `<tools:validation>` element alongside the
corresponding `<intent-filter>` element. For example:  

          <activity ...>
              <intent-filter>
                  ...
              </intent-filter>
              <tools:validation testUrl="https://www.example.com/recipe/1138" />
          </activity>
        
        
Be sure to also include `xmlns:tools="http://schemas.android.com/tools"` in
the `<manifest>` tag.

If any one of the test URLs does not pass the intent filter definition, a
lint error appears. Such an error still allows you to build debug variants,
but it will break your release builds.
![](https://developer.android.com/static/studio/images/write/intent-url-validation_2x.png)

#### Layout Editor

The [Layout Editor](https://developer.android.com/studio/write/layout-editor) has been updated
with a number of enhancements, including the following:

- New toolbar layout and icons.
- Updated layout in the component tree.
- Improved drag-and-drop view insertions.
- New error panel below the editor, showing all issues with suggestions to fix (if available).
- Various UI enhancements for building with `ConstraintLayout`, including the following:
  - New support to [create barriers](https://developer.android.com/training/constraint-layout#constrain-to-a-barrier).
  - New support to create groups: In the toolbar, select **Guidelines \>
    Add Group** (requires [ConstraintLayout 1.1.0 beta 2](https://androidstudio.googleblog.com/2017/10/constraintlayout-110-beta-2.html) or higher)
  - New UI to create chains: Select multiple views, and then right-click and select **Chain**.

![](https://developer.android.com/static/studio/images/write/layout-editor-errors_2x.png)

#### Layout Inspector

The [Layout Inspector](https://developer.android.com/studio/debug/layout-inspector) includes
enhancements to make it easier to debug issues with your app layouts, including
grouping properties into common categories and new search functionality in both
the **View Tree** and the **Properties** panes.
![](https://developer.android.com/static/studio/images/debug/layout-inspector_2x.png)

#### APK Analyzer

You can now use the APK Analyzer from the command line with the
[`apkanalyzer`](https://developer.android.com/studio/command-line/apkanalyzer) tool.

The APK Analyzer has also been updated with the following improvements:

- For APKs built with ProGuard, you can load ProGuard mapping files that add capabilities to the DEX viewer, including:
  - Bolded nodes to indicate that the nodes should not be removed when shrinking code.
  - A button to show nodes that were removed during the shrinking process.
  - A button that restores the original names of nodes in the tree view that were obfuscated by ProGuard.
- The DEX Viewer now shows the estimated size impact of each package, class and method.
- New filtering options at the top to show and hide fields and methods.
- In the tree view, nodes that are references not defined in the DEX file appear in italics.

For more information, see [Analyze Your Build with APK Analyzer](https://developer.android.com/studio/debug/apk-analyzer).

#### Preview for D8 DEX compiler

Android Studio 3.0 includes an optional new DEX compiler called D8. It will
eventually replace the DX compiler, but you can opt-in to use the new D8
compiler now.

DEX compilation directly impacts your app's build time, `.dex` file
size, and runtime performance. And when comparing the new D8 compiler with the
current DX compiler, D8 compiles faster and outputs smaller `.dex` files, while
having the same or better app runtime performance.

To try it, set the following in your project's `gradle.properties` file:  

    android.enableD8=true
        
For more information, see the [blog post about the D8 compiler](https://android-developers.googleblog.com/2017/08/next-generation-dex-compiler-now-in.html).

#### Google's Maven repository

Android Studio now uses Google's Maven Repository by default instead of
depending on the Android SDK Manager to get updates for Android Support Library,
Google Play Services, Firebase, and other dependencies. This makes it easier to
keep your libraries up to date, especially when using
a continuous integration (CI) system.

All new projects now include the Google Maven repository by default. To update
your existing project, add `google()` in the `repositories` block of the
top-level `build.gradle` file:  

          allprojects {
              repositories {
                  google()
              }
          }
        
        
Learn more about [Google's Maven repository here](https://developer.android.com/studio/build/dependencies#google-maven).

#### Other changes

- Native debugging with Android Studio no longer supports 32-bit Windows. We've chosen to focus on other platforms because very few developers are using this platform. If you are using 32-bit Windows and you plan to debug native code, you should keep using [Android Studio 2.3](https://developer.android.com/studio/archive#android-studio-2-3-3).
- Upgraded the base IDE to [IntelliJ 2017.1.2](https://confluence.jetbrains.com/display/IDEADEV/IntelliJ+IDEA+2017.1.2+Release+Notes), which adds a number of new features from [2016.3](https://www.jetbrains.com/idea/whatsnew/#v2016-3) and [2017.1](https://blog.jetbrains.com/idea/2017/02/intellij-idea-2017-1-public-preview-java-9-debugger-vcs-search-editor-and-many-more/), such as Java 8 language refactoring, parameter hints, semantic highlighting, draggable breakpoints, instant results in search, and much more.
- Added many new lint checks.
- Also see the latest [Android Emulator updates](https://developer.android.com/studio/releases/emulator).  

### 2.3 (March 2017)

Android Studio 2.3.0 is primarily a bug fix and stability release, but it
also includes a number of new features.  

**2.3.3 (June 2017)**


This is a minor update to add support for Android O (API level 26).  

**2.3.2 (April 2017)**


This is a minor update to Android Studio 2.3 for the following changes:

- AVD Manager updates to support Google Play in system images.
- Bug fixes for NDK builds when using R14+ of the NDK.


Also see corresponding updates for [Android Emulator 26.0.3](https://developer.android.com/studio/releases/emulator).  

**2.3.1 (April 2017)**


This is a minor update to Android Studio 2.3 that fixes an issue where some
physical Android devices did not work properly with [Instant Run](https://developer.android.com/studio/run#instant-run) (see [Issue
#235879](https://code.google.com/p/android/issues/detail?id=235879)).  

    <h3 class="hide-from-toc">
      New
    </h3>

    <div class="video-wrapper-left">
      <iframe class="devsite-embedded-youtube-video" data-video-id="VFyKclKBGf0"
              data-autohide="1" data-showinfo="0" frameborder="0" allowfullscreen>
      </iframe>
    </div>

    <ul>
      <li>Android Studio can now convert PNG, BMP, JPG, and static GIF files to
      WebP format. WebP is an image file format from Google that provides lossy
      compression (like JPEG) as well as transparency (like PNG) but can provide
      better compression than either JPEG or PNG. For more information, see
        <a href="/studio/write/convert-webp.html">Convert images to WebP in Android
        Studio</a>.
      </li>

      <li>The new <a href="/studio/write/app-link-indexing.html">App Links
      Assistant</a> simplifies the process of adding Android App Links to your app
      into a step-by-step wizard. Android App Links are HTTP URLs that bring users
      directly to specific content in your Android app.
      </li>

      <li>The Layout Editor now includes support for two new ConstraintLayout
      features:
        <ul>
          <li>Define a view size based on an aspect ratio.
          </li>
          <li>Create packed, spread, and weighted linear groups with constraint
          chains.
          </li>
        </ul>
        For more information, see <a href=
        "/training/constraint-layout/index.html">Build a Responsive UI with
        ConstraintLayout</a>.
      </li>

      <li>The Layout Editor also now lets you create a list of <a href=
      "/studio/write/layout-editor.html#edit-properties">favorite attributes</a> so
      you don't have to click <b>View all attributes</b> to access the attributes
      you use most.
      </li>

      <li>When adding a material icon using the Vector Import Dialog (<b>File &gt;
      New &gt; Vector Asset</b>), you can now filter the list of available icons by
      category or by icon name. For more information, see <a href=
      "/studio/write/vector-asset-studio.html#materialicon">Adding a material
      icon</a>.
      </li>

      <li>
        <a href="/studio/write/annotations.html#accessibility">New and updated
        annotations</a>. The new <code>@RestrictTo</code> annotation for methods,
        classes, and packages lets you restrict an API. The updated
        <code>@VisibleForTesting</code> annotation now has an optional
        <code>otherwise</code> argument that lets you designate what the visibility
        of a method should be if not for the need to make it visible for testing.
        Lint uses the <code>otherwise</code> option to enforce the intended
        visibility of the method.
      </li>

      <li>New <a href="/studio/write/lint.html#snapshot">lint baseline support</a>
      allows you to use a snapshot of your project's current set of warnings as a
      baseline for future inspection runs so only new issues are reported. The
      baseline snapshot lets you start using lint to fail the build for new issues
      without having to go back and address all existing issues first.
      </li>

      <li>New lint checks, including the following:
        <ul>
          <li>Obsolete <code>SDK_INT</code> Checks: Android Studio removes obsolete
          code that checks for SDK versions.
          </li>
          <li>Object Animator Validation: Lint analyzes your code to make sure that
          your <code>ObjectAnimator</code> calls reference valid methods with the
          right signatures and checks that those methods are annotated with <code>
            @Keep</code> to prevent ProGuard from renaming or removing them during
            release builds.
          </li>
          <li>Unnecessary Item Decorator Copy: Older versions of the
          <code>RecyclerView</code> library did not include a divider decorator
          class, but one was provided as a sample in the support demos. Recent
          versions of the library have a divider decorator class. Lint looks for
          the old sample and suggests replacing it with the new one.
          </li>
          <li>WifiManager Leak: Prior to Android 7.0 (API level 24), initializing
          the <code>WifiManager</code> with <code><a href="/reference/android/content/Context.html#getSystemService(java.lang.Class&lt;T&gt;)">Context.getSystemService()</a></code>
          can cause a memory leak if the context is not the application context.
          Lint looks for these initializations, and if it <em>cannot</em> determine
          that the context is the application context, it suggests you use <code><a href="/reference/android/content/Context.html#getApplicationContext()">Context.getApplicationContext()</a></code> to get the proper context for the
          initialization.
          </li>
          <li>Improved Resource Prefix: The existing <code>resourcePrefix</code>
          lint check had many limitations. You can now configure your project with
          a prefix, such as <code>android { resourcePrefix '<var>my_lib</var>'
          }</code>, and lint makes sure that all of your resources are using this
          prefix. You can use variations of the name for styles and themes. For
          example for the <var>my_lib</var> prefix, you can have themes named
          <code>MyLibTheme</code>, <code>myLibAttr</code>,
          <code>my_lib_layout</code>, and so on.
          </li>
          <li>Switch to WebP: This check identifies images in your project that can
          be converted to WebP format based on your project's
          <code>minSdkVersion</code> setting. An associated quickfix can
          automatically convert the images, or you can <a href=
          "/studio/write/convert-webp.html">convert images to WebP</a> manually.
          </li>
          <li>Unsafe WebP: If your project already includes WebP images, this check
          analyzes your project to ensure that your <code>minSdkVersion</code>
          setting is high enough to support the included images. For more
          information about WebP support in Android and Android Studio, see
          <a class="external" href=
          "https://developers.google.com/speed/webp/faq#which_web_browsers_natively_support_webp">
            Which browsers natively support WebP?</a> and <a href=
            "/studio/write/convert-webp.html">Create WebP Images Using Android
            Studio</a>.
          </li>
        </ul>
      </li>
    </ul>

    <h3 class="hide-from-toc">
      Changes
    </h3>

    <ul>
      <li>A separate button to push changes with Instant Run: After deploying your
      app, you now click <b>Apply Changes</b> <img src=
      "/studio/images/buttons/toolbar-apply-changes.svg" alt="" class=
      "inline-icon"> to quickly push incremental changes to your running app using
      Instant Run. The <b>Run</b> <img src="/studio/images/buttons/toolbar-run.png"
        alt="" class="inline-icon"> and <b>Debug</b> <img src=
        "/studio/images/buttons/toolbar-debug.png" alt="" class="inline-icon">
        buttons are always available to you when you want to reliably push your
        changes and force an app restart.
        <ul>
          <li>Instant Run is supported only when deploying your app to a target
          device running Android 5.0 (API level 21) or higher.
          </li>
          <li>Instant Run is no longer disabled for projects that <a href=
          "/studio/projects/add-native-code.html">link to external native
          projects</a> using CMake or ndk-build. However, you can only use Instant
          Run to push incremental changes to your Java code, not your native code.
          </li>
          <li>Cold swaps (which you can force for a running app by clicking
          <strong>Run</strong> <img src="/studio/images/buttons/toolbar-run.png"
          alt="" class="inline-icon">) are now more reliable. Forcing a cold swap
          also fixes the issue where changes to notification and widget UIs were
          not updated on the target device.
          </li>
          <li>Includes optimizations that make app startup much faster. These
          optimizations may affect profiling, so you should temporarily <a href=
          "/studio/run/index.html#disable-ir">disable Instant Run</a> whenever
          profiling your app.
          </li>
        </ul>
      </li>

      <li>
        <p>
          The <b>AVD Manager</b> <img src=
          "/studio/images/buttons/toolbar-avd-manager.png" alt="" class=
          "inline-icon"> and <b>SDK Manager</b> <img src=
          "/studio/images/buttons/toolbar-sdk-manager.png" alt="" class=
          "inline-icon"> buttons are now included in the lean Navigation Bar as
          well as the full Toolbar. To use the lean Navigation Bar, click
          <b>View</b> to open the View menu, then ensure that <b>Navigation Bar</b>
          is selected and <b>Toolbar</b> is <em>not</em> selected.
        </p>
        <img src="/studio/images/releases/navigationbar_sdkavd_2x.png" width="757">
      </li>

      <li>The "Hybrid" debugger has been renamed to "Dual" debugger.
      </li>

      <li>In the <a href="/studio/run/rundebugconfig.html">Run/Debug
      Configurations</a> dialog, under Defaults in the left pane, the following run
      configuration names have changed with no behavior changes:
        <ul>
          <li>The JUnit name has changed to Android JUnit. If you have a project
          that uses JUnit run configurations, those configurations are transformed
          to Android JUnit run configurations the first time you open the project
          with Android Studio. A dialog appears to inform you of the name change.
          </li>
          <li>The Android Tests name has changed to Android Instrumented Tests.
          </li>
        </ul>
      </li>

      <li>The <a href="/studio/debug/am-gpu-debugger.html">GPU Debugger</a> has
      been removed from Android Studio as of version 2.3. An open-source,
      standalone version of the tool is now available on <a href=
      "https://github.com/google/gapid" class="external-link">GitHub</a>.
      </li>

      <li>The Run/Debug option is no longer available when you right-click a <code>
        *.gradle build</code> script.
      </li>

      <li>All templates now use <code>ConstraintLayout</code> as the default
      layout.
      </li>

      <li>The Widgets palette in the Layout Editor has been redesigned.
      </li>
    </ul>

    <p>
      This release also includes a number of bug fixes. <a href=
      "https://code.google.com/p/android/issues/list?can=1&amp;q=target%3D2.3+status%3DReleased&amp;colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&amp;cells=tiles">
      See all bug fixes in 2.3.0.</a>
    </p>

    <p class="note">
      <b>Known issue:</b> Some device manufacturers block apps from automatically
      launching after being installed on the device. When deploying your app to a
      physical device using Android Studio 2.3, this restriction breaks the
      intended behavior of Instant Run and causes the following error output:
      <code>Error: Not found; no service started</code>. To avoid this issue,
      either <a href="/studio/run/emulator.html">use the emulator</a> or enable
      automatic launching for your app in your device's settings. The procedure
      for doing this is different for each device, so check the instructions
      provided by the manufacturer. To learn more about this issue, see
      <a href="https://code.google.com/p/android/issues/detail?id=235879">Issue
        #235879</a>.
    </p>


<br />

<br />

### 2.2 (September 2016)

<br />

<br />


**2.2.3 (December 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes a bug fixes
      focused around gradle, the core IDE, and lint.
    </p>

    <p>
      Highlighted build changes:
    </p>

    <ul>
      <li>ProGuard version rollback. Due to a <a href=
      "https://sourceforge.net/p/proguard/bugs/625/">correctness issue</a>
      discovered in ProGuard 5.3.1, we have rolled back to ProGuard 5.2.1. We
      have worked with the ProGuard team on getting a fix quickly, and we expect
      to roll forward to ProGuard 5.3.2 in Android Studio 2.3 Canary 3.
      </li>
      <li>Bug fix for <code>aaptOptions</code> <code>IgnoreAssetsPattern</code>
      not working properly (<a href="http://b.android.com/224167">issue
      224167</a>)
      </li>
      <li>Bug fix for Gradle autodownload for Constraint Layout library
        (<a href="https://code.google.com/p/android/issues/detail?id=212128">issue
        212128</a>)
      </li>
      <li>Bug fix for a JDK8/Kotlin compiler + dx issue (<a href=
      "http://b.android.com/227729">issue 227729</a>)
      </li>
    </ul>

    <p>
      <a href=
      "https://code.google.com/p/android/issues/list?can=1&amp;q=target%3D2.2.3+status%3AReleased+&amp;colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&amp;cells=tiles">
      See all bug fixes in 2.2.3</a>.
    </p>

<br />

<br />

<br />


**2.2.2 (October 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes a number of small
      changes and bug fixes, including:
    </p>

    <ul>
      <li>When reporting Instant Run issues through the IDE, the report now also
      includes logcat output for <code>InstantRun</code> events. To help us
      improve Instant Run, please <a href=
      "/studio/run/index.html#submit-feedback">enable extra logging and report
      any issues</a>.
      </li>
      <li>A number of small bug fixes for Gradle.
      </li>
      <li>A fix for problems with generating multiple APKs.
      </li>
    </ul>

<br />

<br />

<br />


**2.2.1 (October 2016)**

<br />

    <p>
      This is a minor update to Android Studio 2.2. It includes several bug fixes
      and a new feature to enable extra logging to help us troubleshoot Instant
      Run issues---to help us improve Instant Run, please <a href=
      "/studio/run/index.html#submit-feedback">enable extra logging and report
      any issues</a>.
    </p>

<br />

<br />

<br />

### New

<br />

<br />

<br />

<br />

- All new **[Layout
Editor](https://developer.android.com/studio/write/layout-editor)** with tools custom-built to support [ConstraintLayout](https://developer.android.com/training/constraint-layout).  

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/layout-inspector">Layout
    Inspector</a></strong> lets you examine snapshots of your layout hierarchy
    while your app is running on the emulator or a device.
    </li>

    <li>New <strong><a href="/studio/write/firebase.html">Assistant</a></strong>
    window to help you integrate Firebase services into your app.
    </li>

    <li>New <strong><a href="/studio/debug/apk-analyzer.html">APK
    Analyzer</a></strong> tool so you can inspect the contents of your packaged
    app.
    </li>

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/test-recorder">Espresso Test
    Recorder</a></strong> tool (currently in beta) to help you create UI tests by
    recording your own interactions.
    </li>

    <li>New <strong><a href=
    "http://tools.android.com/tech-docs/build-cache">build cache</a></strong>
    (currently experimental) to speed up build performance.
    </li>

    <li>New <strong>C/C++ build integration with CMake and ndk-build</strong>.
    Compile and build new or existing native code into libraries packaged into
    your APK, and debug using lldb. For new projects, Android Studio uses CMake
    by default, but also supports ndk-build for existing projects. To learn how
    to include native code in your Android application, read <a href=
    "/studio/projects/add-native-code.html">Add C and C++ Code to Your
    Project</a>. To learn how to debug native code with lldb, see <a href=
    "/studio/debug/index.html#debug-native">Debug Native Code</a>.
    </li>

    <li>New <strong><a href="/studio/intro/index.html#sample-code">Samples
    Browser</a></strong> so you can easily look up Google Android sample code
    from within Android Studio to jump start app development.
    </li>

    <li>New <strong>Merged Manifest Viewer</strong> to help you diagnose how your
    manifest file merges with your app dependencies across project build
    variants.
    </li>

    <li>The <strong>Run</strong> window now contains log messages for the current
    running app. Note that you can configure the <a href=
    "/studio/debug/am-logcat.html">logcat Monitor</a> display, but not the
    <strong>Run</strong> window.
    </li>

    <li>New <strong><a href="/studio/run/emulator.html">Android
    Emulator</a></strong> features:
      <ul>
        <li>Added new <strong>Virtual</strong> <strong>Sensors</strong> and
        <strong>Cellular</strong> &gt; <strong>Signal Strength</strong> controls.
        </li>
        <li>Added an <strong>LTE</strong> option to the <strong>Cellular</strong>
        &gt; <strong>Network type</strong> control.
        </li>
        <li>Added simulated vertical swipes for scrolling through vertical menus
        with a mouse wheel.
        </li>
      </ul>
    </li>

    <li>New <strong><a href="/studio/run/rundebugconfig.html">Run/Debug
    Configuration</a></strong> features:
      <ul>
        <li>The <strong>Debugger</strong> tab of the Android App and Android
        Tests templates now contain several new options for debugging with LLDB.
        </li>
        <li>The <strong>Profiling</strong> tab of the Android App and Android
        Tests templates now contain a <strong>Capture GPU Commands</strong>
        option for enabling GPU tracing. You can display GPU traces in the GPU
        Debugger (a beta feature).
        </li>
        <li>The Android Tests template now has a <strong>Firebase Test Lab Device
        Matrix</strong> option for the <strong>Deployment Target</strong>.
        </li>
        <li>The Native Application template has been deprecated. If you use this
        template in a project, Android Studio automatically converts it to the
        Android App template.
        </li>
        <li>The Android Application template has been renamed to Android App.
        </li>
      </ul>
    </li>

    <li>Improved installation, configuration, performance, and UI features in the
    <strong><a href="/studio/debug/am-gpu-debugger.html">GPU
    Debugger</a></strong> (currently in beta).
    </li>

    <li>Android Studio now comes bundled with <strong>OpenJDK 8</strong>.
    Existing projects still use the JDK specified in <strong>File &gt; Project
    Structure &gt; SDK Location</strong>. You can switch to use the new bundled
    JDK by clicking <strong>File &gt; Project Structure &gt; SDK
    Location</strong> and checking the <strong>Use embedded JDK</strong>
    checkbox.
    </li>

    <li>Added new <strong>help menus and buttons</strong> in the UI so you can
    more easily find the online documentation.
    </li>

<br />

<br />

### Changes

<br />

<br />

- Updated the IDE codebase from IntelliJ 15 to **IntelliJ
  2016.1**
- Instant Run now requires the platform SDK corresponding to the target device API level to be installed.
- Instant Run will automatically disabled if user is running the app under a work profile or as a secondary user.
- Fixed many reliability issues for **[Instant Run](https://developer.android.com/studio/run#instant-run)** where changes were not getting deployed or the app would crash:
  - Some app assets were not deployed to your running app. ( [Bug: #213454](http://b.android.com/213454))
  - App crashes when user transitions between Instant Run and non Instant Run sessions where a Serializable class does not have serialVersionUID defined. ([Bug: #209006](http://b.android.com/209006))
  - Style changes aren't reflected with Instant Run. ([Bug: #210851](http://b.android.com/210851))
  - Instant Run session is unreliable and causes FileNotFoundException. ([Bug: #213083](http://b.android.com/213083))
  - Changes to drawables not reflected until full rebuild is performed for KitKat. ([Bug: #21530](http://b.android.com/215360))
  - Resource changes aren't reflected with Instant Run when custom sourceSets contain nested paths. ([Bug: #219145](http://b.android.com/219145))
  - Hot and warm swap don't work if changed class contains annotation with enum value. ([Bug: #209047](http://b.android.com/209047))
  - Changes to annotation data not reflected with Instant Run. ([Bug: #210089](http://b.android.com/210089))
  - Instant Run doesn't pick up code changes if you make changes outside the IDE. ([Bug: #213205](http://b.android.com/213205))
  - Instant Run session is unreliable due to mismatch security token. ([Bug: #211989](http://b.android.com/211989)
  - Cold swap fails for devices that doesn't properly support run-as. ([Bug: #210875](http://b.android.com/210875))
  - App crash after instant run restart. ([Bug: #219744](http://b.android.com/219744))
- ClassNotFoundException observed when switching from Instant Run to Instant Debug. ([Bug: #215805](http://b.android.com/215805))  

    <li>Improved performance for <strong>Gradle sync</strong> within the IDE,
    especially for large projects.
    </li>

    <li>Improved build times for both full and incremental builds with new app
    packaging code.
    </li>

    <li>Improved <strong>Jack compiler performance and features</strong>,
    including support for annotation processors and dexing in process. To learn
    more, read the <a href=
    "/studio/releases/gradle-plugin.html#revisions">Android plugin for Gradle
    2.2.0 release notes</a>.
    </li>

    <li>Removed the <strong>Scale</strong> AVD property from the AVD Manager.
    </li>

    <li>The Android Emulator <strong>-port</strong> and <strong>-ports</strong>
    command-line options now report which ports and serial number the emulator
    instance is using, and warn if there are any issues with the values you
    provided.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/create-java-class.html">Create New Class dialog</a></strong>
    and the corresponding file templates. <strong>Note:</strong> If you've
    previously customized the <strong>AnnotationType</strong>,
    <strong>Class</strong>, <strong>Enum</strong>, <strong>Interface</strong>, or
    <strong>Singleton</strong> file templates, you need to modify your templates
    to comply with the new templates or you won't be able to use the new fields
    in the <strong>Create New Class</strong> dialog.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/vector-asset-studio.html">Vector Asset Studio</a></strong>
    user interface and added support for Adobe Photoshop Document (PSD) files.
    </li>

    <li>Improved the <strong><a href=
    "/studio/write/image-asset-studio.html">Image Asset Studio</a></strong> user
    interface.
    </li>

    <li>Improved the <strong>Theme Editor</strong>'s Resource Picker.
    </li>

    <li>Fixed memory leaks and reduced overall memory usage in Android Studio.
    </li>

    <li>Added a <strong>Background</strong> button in the <strong><a href=
    "/studio/intro/update.html#sdk-manager">SDK Manager</a></strong> so you can
    get back to work and install your packages in the background.
    </li>

    <li>Improved <strong><a href="/studio/intro/accessibility.html">Accessibility
    features</a></strong>, including support for screen readers and keyboard
    navigation.
    </li>

    <li>Enhanced <strong>Code Analysis</strong> includes code quality checks for
    Java 8 language usage and more cross-file analysis.
    </li>

    <li>Several toolbar icons have changed.
    </li>

<br />

### 2.1 (April 2016)

The primary changes in this update provide support for development with the
Android N Preview.  
**2.1.3 (August 2016)**


This update adds compatibility with Gradle 2.14.1, which includes performance
improvements, new features, and an important [security fix](https://docs.gradle.org/2.14/release-notes#local-privilege-escalation-when-using-the-daemon). For more details, see the [Gradle
release notes](https://docs.gradle.org/2.14.1/release-notes).


By default, new projects in Android Studio 2.1.3 use Gradle 2.14.1. For
existing projects, the IDE prompts you to upgrade to Gradle 2.14.1 and
[Android plugin
for Gradle 2.1.3](https://developer.android.com/studio/releases/gradle-plugin#revisions), which is required when using Gradle 2.14.1 and
higher.

<br />

**2.1.2 (June 2016)**


This update includes a number of small changes and bug fixes:

- [Instant Run](https://developer.android.com/studio/run#instant-run) updates and bug fixes.
- Improvements to LLDB performance and crash notifications.
- Fixed a regression in the Android Studio 2.1.1 security update that caused `git rebase` to fail.

<br />

<br />

**2.1.1 (May 2016)**

Security release update.

<br />

<br />

The Android N platform adds support for [Java 8 language features](https://developer.android.com/studio/write/java8-support), which
require a new experimental compiler called Jack. The latest version of Jack is
currently supported only in Android Studio 2.1. So if you want to use Java 8
language features, you need to use Android Studio 2.1 to build your app.

<br />

<br />

**Note:** [Instant Run](https://developer.android.com/tools/building/building-studio#instant-run)
is disabled when you enable the Jack compiler because they currently are not
compatible.

<br />

<br />

Although Android Studio 2.1 is now stable, the Jack compiler is still
experimental and you must enable it with the `jackOptions`
property in your `build.gradle` file.

<br />

<br />

Other than the changes to support the N Preview, Android Studio 2.1
includes minor bug fixes and the following enhancements:

- The Java-aware C++ debugger is now enabled by default when you're using an N device or emulator and select **Native** debugger mode (in the **Debugger** tab for your run/debug configuration).

For other build enhancements, including incremental Java compilation
and dexing-in-process,update your [Android plugin for
Gradle](https://developer.android.com/tools/revisions/gradle-plugin) to version 2.1.0.

<br />

### 2.0 (April 2016)


**Note:** If you are developing for the N Developer Preview, you
should use Android Studio 2.1 Preview. Android Studio 2.0 does not support
all the features required to target the N Preview.


**Instant Run**:

- Android Studio now deploys clean builds faster than ever before. Additionally, pushing incremental code changes to the emulator or a physical device is now almost instantaneous. Review your updates without redeploying a new debug build or, in many cases, without restarting the app.
- Instant Run supports pushing the following changes to a running app:
  - Changes to the implementation of an existing instance method or static method
  - Changes to an existing app resource
  - Changes to structural code, such as a method signature or a static field (requires a target device running API level 21 or higher).
- Read the documentation to learn more [about Instant
  Run](https://developer.android.com/tools/building/building-studio#instant-run).


  **Note:** Instant Run is supported only when you deploy the
  debug build variant, use [Android plugin for
  Gradle version 2.0.0](https://developer.android.com/tools/revisions/gradle-plugin#revisions) or higher, and configure your app's module-level
  `build.gradle` file for `minSdkVersion 15` or higher.
  For the best performance, configure your app for `minSdkVersion
  21` or higher.

**New additions to Lint:**

- Inspection of `switch` statements using [@IntDef](https://developer.android.com/reference/androidx/annotation/IntDef) annotated integers to make sure all constants are handled. To quickly add any missing statements, use the intention action drop-down menu and select **Add Missing @IntDef
  Constants**.
- Flags for incorrect attempts to use string interpolation to insert version numbers in the `build.gradle` file.
- Flags for anonymous classes that extend the [Fragment](https://developer.android.com/reference/android/app/Fragment) class.
- Flags for native code in unsafe locations, such as the `res/` and `asset/` folders. This flag encourages storing native code in the `libs/` folder, which is then securely packaged into the application's `data/app-lib/` folder at install time. [AOSP: #169950](https://android-review.googlesource.com/#/c/169950/)
- Flags for unsafe calls to [Runtime.load()](https://developer.android.com/reference/java/lang/Runtime#load(java.lang.String)) and [System.load()](https://developer.android.com/reference/java/lang/System#load(java.lang.String)) calls. [AOSP: #179980](https://android-review.googlesource.com/#/c/179980/)
- Find and remove any unused resources by selecting **Refactor \> Remove
  Unused Resources** from the menu bar. Unused resource detection now supports resources only referenced by unused resources, references in raw files such as `.html` image references, and `tools:keep` and `tools:discard` attributes used by the Gradle resource shrinker, while considering inactive source sets (such as resources used in other build flavors) and properly handling static field imports.
- Checks that implicit API references are supported on all platforms targeted by `minSdkVersion`.
- Flags improper usage of [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView) and [Parcelable](https://developer.android.com/reference/android/os/Parcelable).
- [@IntDef](https://developer.android.com/reference/androidx/annotation/IntDef), [@IntRange](https://developer.android.com/reference/androidx/annotation/IntRange), and [@Size](https://developer.android.com/reference/androidx/annotation/Size) inspections are now also checked for `int` arrays and varargs.

**Additional Improvements**:

- Optimized for Android Emulator 2.0, which is faster than ever before, supports a wider range of virtual devices, and features a drastically improved UI. To learn more about the new emulator, read the [SDK Tools release notes](https://developer.android.com/studio/releases/sdk-tools#notes).
- Improvements to the [Android Virtual Device
  Manager](https://developer.android.com/tools/devices/managing-avds):
  - System images are now categorized under the following tabs: *Recommended* , *x86* , and *Other*.
  - Under advanced settings, you can enable multi-core support and specify the number of cores the emulator can use.
  - Under advanced settings, you can determine how graphics are rendered on the emulator by selecting one of the following options:
    - **Hardware:** use you computer's graphics card for faster rendering.
    - **Software:** use software-based rendering.
    - **Auto:** let the emulator decide the best option. This is the default setting.
- Improved AAPT packaging times by specifying deploy target before the app is built. This allows Android Studio to efficiently package only the resources required by the specified device.
- Added Cloud Test Lab integration to provide on-demand app testing with the convenience and scalability of a cloud service. Learn more about how you can [use Cloud
  Test Lab with Android Studio](https://developer.android.com/training/testing/start#run-ctl).
- Added a preview of the new [GPU Debugger](https://tools.android.com/tech-docs/gpu-profiler). For graphics intensive applications, you can now visually step through your OpenGL ES code to optimize your app or game.
- Added Google App Indexing Test. Add support for URLs, app indexing, and search functionality to your apps to help drive more traffic to your app, discover which app content is used most, and attract new users. Test and validate URLs in your app all within Android Studio. See [Supporting URLs and App
  Indexing in Android Studio](https://developer.android.com/tools/help/app-link-indexing).
- Upgrades from the latest IntelliJ 15 release, including improved code analysis and performance. See [What's New in IntelliJ](https://www.jetbrains.com/idea/whatsnew) for a complete description of the new features and enhancements.
- XML editor auto-complete now adds quotations marks when completing attributes. To check if this option is enabled, open the **Setting** or **Preferences** dialogue, navigate to **Editor \> General \> Smart
  Keys** , and check the box next to **Add quotes for attribute value on
  attribute completion** . [Issue: 195113](https://b.android.com/195113)
- The XML editor now supports code completion for [data binding](https://developer.android.com/topic/libraries/data-binding#layout_details) expressions.  

### Android Studio v1.5.1 (December 2015)

Fixes and enhancements:

- Fixed a rendering failure issue in the Layout Editor. [Issue: 194612](http://b.android.com/194612)
- Added the ability to vary `description` manifest attributes by configuration. [Issue: 194705](http://b.android.com/194705)
- Improved the contrast of the Android Studio Darcula appearance theme in Vector Asset Studio. [Issue: 191819](http://b.android.com/191819)
- Added *Help* button support to Vector Asset Studio.
- Added support for the `%` operator for data binding. [Issue: 194045](http://b.android.com/194045)
- Fixed a case where launching an app for debugging resulted in the debugger connecting to the wrong device. [Issue: 195167](http://b.android.com/195167)
- Fixed a null pointer exception that could occur when attempting to run an app in certain scenarios.  

### Android Studio v1.5.0 (November 2015)

Fixes and enhancements:

- Added new Memory Monitor analysis abilities to Android Monitor. When you view an HPROF file captured from this monitor, the display is now more helpful so you can more quickly locate problems, such as memory leaks. To use this monitor, click **Android Monitor** at the bottom of the main window. In Android Monitor, click the **Memory** tab. While the monitor is running, click the **Dump Java Heap** icon, and then click **Captures** in the main window and double-click the file to view it. Click *Capture Analysis* on the right. (The Android Device Monitor can't be running at the same time as Android Monitor.)
- Added new deep link and app link support. The Code Editor can automatically create an intent filter for deep linking in the `AndroidManifest.xml` file. It can also generate code to help you integrate with the [App Indexing API](http://developers.google.com/app-indexing/android/publish) in an activity in a Java file. A deep link testing feature helps you verify that a specified deep link can launch an app. In the **General** tab of the *Run/Debug Configurations* dialog, you can specify deep link launch options. You can also test App Indexing API calls in an activity by using the Android Monitor **logcat** display. The Android `lint` tool now has warnings for certain issues involving deep links and the App Indexing API.
- Added the ability to use short names when code-completing custom views in the Code Editor.
- Added support for more [VectorDrawable](https://developer.android.com/reference/android/graphics/drawable/VectorDrawable) elements to [Vector Asset Studio](https://developer.android.com/tools/help/vector-asset-studio) for backward-compatibility. Vector Asset Studio can use these elements to convert vector drawables into PNG raster images to use with Android 4.4 (API level 20) and lower.
- Added new `lint` checks for Android TV and Android Auto to give you immediate, actionable feedback in Android Studio, along with several quick fixes. For example, for Android TV, it can report and provide a quick fix for permissions, unsupported hardware, `uses-feature` element, and missing banner issues. For Android Auto, it can validate the correct usage in the descriptor file referred from your `AndroidManifest.xml` file, report if there isn't an intent filter for the `MediaBrowserService` class, and identify certain voice actions issues.
- Added new `lint` checks for insecure broadcast receivers, `SSLCertificateSocketFactory` and `HostnameVerifier` class uses, and `File.setReadable()` and `File.setWritable()` calls. It also detects invalid manifest resource lookups, especially for resources that vary by configuration.
- Fixed a number of stability issues.  

### Android Studio v1.4.1 (October 2015)

Fixes and enhancements:

- Fixed a Gradle model caching issue that could lead to excessive Gradle syncing when the IDE was restarted.
- Fixed a native debugging deadlock issue.
- Fixed an issue blocking users of the Subversion 1.9 version control system.
- Fixed a *Device Chooser* dialog problem where after connecting a device that was unauthorized you could no longer select the emulator. [Issue: 189658](http://b.android.com/189658)
- Fixed incorrect translation error reporting for locales that have a region qualifier and a translation in the region (but not in the base locale). [Issue: 188577](http://b.android.com/188577)
- Fixed a deadlock issue in the Theme Editor related to its interaction with the Layout Editor. [Issue: 188070](http://b.android.com/188070)
- Fixed a Theme Editor reload and edit conflict causing attributes to not properly update. [Issue: 187726](http://b.android.com/187726)
- Improved Theme Editor performance.
- Fixed an issue where the `android:required` attribute was ignored in the manifest. [Issue: 187665](http://b.android.com/187665)  

### Android Studio v1.4.0 (September 2015)

Fixes and enhancements:

- Added the [Vector Asset Studio](https://developer.android.com/tools/help/vector-asset-studio) tool for importing vector graphics, such as material icons and SVG files. To use this tool, in the Android view of the Project window, right-click the **res** folder and select **New** \> **Vector Asset**.
- Added new Android Monitor functions, GPU and Network. To use these monitors, click **Android Monitor** at the bottom of the main window. The Android Device Monitor can't be running at the same time as Android Monitor.
- Added an early preview of the new Theme Editor. To use this feature, select **Tools** \> **Android** \> **Theme Editor**.
- Updated the Android templates for the Design Support Library. Templates now include support for the Material Design specification, as well as the `appcompat` Support Library for backwards compatibility.  

### Android Studio v1.3.2 (August 2015)

Fixes and enhancements:

- Added support for Android 6.0 (API level 23), including new icons and AVD Manager support for creating devices with new screen densities.
- Fixed an exception that was occurring during update checks. [Issue: 183068](http://b.android.com/183068)
- Fixed problem where unresolved view coordinates could cause the layout editor to crash. [Issue: 178690](http://b.android.com/178690)
- Fixed issue with invalid resource type warnings. [Issue: 182433](http://b.android.com/182433)
- Fixed lint check that was incorrectly flagging resources as private. [Issue: 183120](http://b.android.com/183120)  

### Android Studio v1.3.1 (August 2015)

Fixes and enhancements:

- Fixed support for creating an Android Wear Android Virtual Device (AVD) on Windows.
- Updated the *Project Wizard* to use the entered project name.
- Added support to allow the Android SDK to be stored in a read-only directory.
- Updated Android plugin for Gradle version to 1.3.0.
- Fixed issues with launching a debug session from the Android Debug Bridge (adb) Unix shell.
- Fixed the Java package renaming message to show the correct package name.  

### Android Studio v1.3.0 (July 2015)

Fixes and enhancements:

- Added options to enable [developer services](https://developer.android.com/tools/studio/studio-features#dev-services), such as [Google AdMob](https://developers.google.com/admob/) and [Analytics](https://developer.android.com/distribute/analyze/start), in your app from within Android Studio.
- Added additional [annotations](https://developer.android.com/tools/debugging/annotations), such as `@RequiresPermission`, `@CheckResults`, and `@MainThread`.
- Added the capability to generate Java heap dumps and analyze thread allocations from the [Memory Monitor](https://developer.android.com/tools/studio#mem-cpu). You can also convert Android-specific HPROF binary format files to standard HPROF format from within Android Studio.
- Integrated the [SDK Manager](https://developer.android.com/tools/help/sdk-manager) into Android Studio to simplify package and tools access and provide update notifications.

  **Note:** The standalone SDK Manager is still available from
  the command line, but is recommended for use only with standalone SDK
  installations.
- Added the `finger` command in the emulator console to simulate [fingerprint](https://developer.android.com/tools/studio/studio-features#finger-print) authentication.
- Added a `<public>` resource declaration to designate library resources as [public and private](https://developer.android.com/tools/studio/studio-features#private-res) resources.

  **Note:** Requires
  [Android plugin for Gradle](https://developer.android.com/tools/building/plugin-for-gradle)
  version 1.3 or higher.
- Added [data binding](https://developer.android.com/tools/data-binding/guide) support to create declarative layouts that bind your application logic to layout elements.
- Added support for a separate [test APK module](https://developer.android.com/tools/studio/studio-features#test-module) to build test APKs in Android Studio.
- Updated the [AVD Manager](https://developer.android.com/tools/devices/managing-avds) with HAXM optimizations and improved notifications.
- Added 64-bit ARM and MIPS emulator support for [QEMU](http://wiki.qemu.org/Main_Page) 2.1.
- Simplified the resolution of Lint warnings by adding quick fixes, such as the automatic generation of [Parcelable](https://developer.android.com/reference/android/os/Parcelable) implementation.
- Added live template support for quick insertion of code snippets.  

### Android Studio v1.2.2(June 2015)

Fixes and enhancements:

- Fixed build issues that were blocking builds from completing.  

### Android Studio v1.2.1 (May 2015)

Fixes and enhancements:

- Fixed minor performance and feature issues.  

### Android Studio v1.2.0 (April 2015)


Fixes and enhancements:

- Updated the Android runtime window to include the [Memory Monitor](https://developer.android.com/tools/studio#mem-cpu) tool and added a tab for CPU performance monitoring.
- Added a *Captures* tab in the left margin to display the captured memory and CPU performance data files, such as CPU method tracking and memory heap snapshots.
- Expanded [annotation](https://developer.android.com/tools/debugging/annotations) support with additional metadata annotations and inferred nullability.
- Enhanced the Translations Editor with additional support for Best Current Practice (BCP) 47, which uses 3-letter language and region codes.
- Integrated IntelliJ 14 and 14.1 features for improved code analysis and performance:
-
  - Enhanced debugging to show inline values for variables and referring objects, as well as perform inline evaluation of lambda and operator expressions.
  - Added code style detection for tab and indent sizes.
  - Added scratch files for code experiments and prototyping without project files.
  - Added the simultaneous insertion of opening and closing tags in HTML and XML files.
  - Added a built-in Java class decompiler so you can look at what's inside a library for which the source code is not available.


  See [What's New in IntelliJ](https://www.jetbrains.com/idea/whatsnew)
  for a complete description of the new features and enhancements.
- Added additional [Project Views](https://developer.android.com/tools/studio#project-view) for *Scratches* , *Project Files* , *Problems* , *Production* , and *Tests* to enhance project management and access.
- Enhanced the **File \> Settings** menu and dialogs for improved settings access and management.
- Added support for high-density displays for Windows and Linux.
- Added support for 280 dpi resources in the `res/drawable-280dpi/` folder.  

### Android Studio v1.1.0 (February 2015)

Various fixes and enhancements:

- Added support for the [Android Wear](https://developer.android.com/design/wear) watch template.
- Modified new project and module creation to include [`res/mipmap`](https://developer.android.com/tools/projects#mipmap) folders for density-specific launcher icons. These `res/mipmap` folders replace the [`res/drawable`](https://developer.android.com/guide/topics/resources/drawable-resource) folders for launcher icons.
- Updated launcher icons to have a [Material Design](https://developer.android.com/design/material) look and added an `xxxhdpi` launcher icon.
- Added and enhanced Lint checks for region and language combinations, launcher icons, resource names, and other common code problems.
- Added support for Best Current Practice (BCP) language tag 47.  

### Android Studio v1.0.1 (December 2014)

Various fixes and enhancements:

- Fixed AVD Manager and **device.xml** file lock issue.
- Fixed the emulator log on Windows systems.
- Fixed issue with creating AVDs with Android Studio and Android SDK installed on different drives on Windows systems.
- Sets the default update channel for new downloads to **Stable** . If you installed the 1.0.0 version of Android Studio and would like stable, production-ready version updates, use **File \> Settings \> Updates** to change to the **Stable** update channel.  

### Android Studio v1.0 (December 2014)

Initial release of Android Studio.  

### Android Studio v0.8.14 (October 2014)

See
[tools.android.com](http://tools.android.com/recent/androidstudio0814inbetachannel)
for a full list of changes.  

### Android Studio v0.8.6 (August 2014)

See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.8.0 (June 2014)

Added support for Android Wear projects.

See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.5.2 (May 2014)

- See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.4.6 (March 2014)

- See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.4.2 (Jan 2014)

- See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.3.2 (Oct 2013)

- See [tools.android.com](http://tools.android.com/recent) for a full list of changes.  

### Android Studio v0.2.x (July 2013)

- Merged in the latest IntelliJ codebase changes. Includes fixes for issues reported by Studio users such as tweaks to Linux font sizes and font rendering.
- Android Gradle plug-in updated to 0.5.0. **Caution:** This new version is not backwards compatible.
  When opening a project that uses an older version of the plug-in, Studio will show an error
  stating **Gradle \<project_name\> project refresh failed.**

  The updated Gradle plug-in includes the following changes:
  - Fixed IDE model to contain the output file even if it's customized through the DSL. Also fixed the DSL to get/set the output file on the variant object so that it's not necessary to use `variant.packageApplication or variant.zipAlign`
  - Fixed dependency resolution so that we resolved the combination of (default config, build types, flavor(s)) together instead of separately.
  - Fixed dependency for tests of library project to properly include all the dependencies of the library itself.
  - Fixed case where two dependencies have the same leaf name.
  - Fixed issue where Proguard rules file cannot be applied on flavors.

  All Gradle plugin release notes are available are here: <http://tools.android.com/tech-docs/new-build-system>.
- Gradle errors from aapt no longer point to merged output files in the build/ folder, they point back to the real source locations.
- Parallel Builds. It's now possible to use Gradle's parallel builds. Please be aware that parallel builds are in "incubation" (see [Gradle's
  documentation](http://www.gradle.org/docs/current/userguide/gradle_command_line.html).) This feature is off by default. To enable it, go to **Preferences** \> **Compiler** and check the box *Compile
  independent modules in parallel*.
- Further work on the new resource repository used for layout rendering, resource folding in the editor, and more:
  - Basic support for .aar library dependencies (e.g. using a library without a local copy of the sources). Still not working for resource XML validation and navigation in source editors.
  - Cycle detection in resource references.
  - Quick Documentation (F1), which can show all translations of the string under the caret, will now also show all resource overlays from the various Gradle flavors and build types, as well as libraries. They are listed in reverse resource overlay order, with strikethrough on the versions of the string that are masked.
  - Fixes to handle updating the merged resources when the set of module dependencies change.
  - XML rendering fixes to properly handle character entity declarations and XML and unicode escapes.
- Save screenshot support for the layout preview and layout editor windows.
- Template bug fixes.
- Lint bug fixes.
- Various fixes for crash reports. Thank you, and keep filing crash reports!  

### Android Studio v0.1.x (May 2013)

- Various bug fixes, including a fix for a common Windows installation issue.

## Older releases of Android Gradle Plugin

### 3.6.0 (February 2020)

This version of the Android plugin requires the following:

- [Gradle 5.6.4](https://docs.gradle.org/5.6.4/release-notes.html).
  To learn more, read the section about [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).

- [SDK Build Tools 28.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**3.6.4 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/studio/releases/archives#4.0.1) for details.

#### New features

This version of the Android Gradle plugin includes the following new
features.

##### View Binding

View binding provides compile-time safety when referencing views in
your code. You can now replace `findViewById()` with the
auto-generated binding class reference. To start using View binding,
include the following in each module's `build.gradle` file:  

```groovy
      android {
          viewBinding.enabled = true
      }
      
```  

```kotlin
      android {
          viewBinding.enabled = true
      }
      
```

To learn more, read the [View
Binding documentation](https://developer.android.com/topic/libraries/view-binding).

##### Support for the Maven Publish plugin

The Android Gradle plugin includes support for the
[Maven
Publish Gradle plugin](https://docs.gradle.org/current/userguide/publishing_maven.html), which allows you to publish build artifacts to
an Apache Maven repository. The Android Gradle plugin creates a
[*component*](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_component)
for each build variant artifact in your app or library module that you can
use to customize a
[*publication*](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:publications)
to a Maven repository.

To learn more, go to the page about how to
[use the Maven Publish
plugin](https://developer.android.com/studio/build/maven-publish-plugin).

##### New default packaging tool

When building the debug version of your app, the plugin uses a new
packaging tool, called *zipflinger* , to build your APK. This new
tool should provide build speed improvements. If the new packaging tool
doesn't work as you expect,
please [report a bug](https://developer.android.com/studio/report-bugs). You can revert to
using the old packaging tool by including the following in your
`gradle.properties` file:  

            android.useNewApkCreator=false
          
##### Native build attribution

You can now determine the length of time it takes Clang to build and
link each C/C++ file in your project. Gradle can output a Chrome trace
that contains timestamps for these compiler events so you can better
understand the time required to build your project. To output this build
attribution file, do the following:

1. Add the flag `-Pandroid.enableProfileJson=true` when
   running a Gradle build. For example:

   `gradlew assembleDebug -Pandroid.enableProfileJson=true`
2. Open the Chrome browser and type `chrome://tracing` in
   the search bar.

3. Click the **Load** button and navigate to
   `<var>project-root</var>/build/android-profile`
   to find the file. The file is named
   `profile-<var>timestamp</var>.json.gz`.

You can see the native build attribution data near the top of the
viewer:

![Native build attribution trace in Chrome](https://developer.android.com/static/studio/images/releases/native-build-attribution.png)

#### Behavior changes

When using this version of the plugin, you might encounter the following
changes in behavior.

##### Native libraries packaged uncompressed by
default

When you build your app, the plugin now sets
`extractNativeLibs` to `"false"` by
default. That is, your native libraries are page aligned and packaged
uncompressed. While this results in a larger upload size, your users
benefit from the following:

- Smaller app install size because the platform can access the native libraries directly from the installed APK, without creating a copy of the libraries.
- Smaller download size because Play Store compression is typically better when you include uncompressed native libraries in your APK or Android App Bundle.

If you want the Android Gradle plugin to instead package compressed
native libraries, include the following in your app's manifest:  

            <application
              android:extractNativeLibs="true"
              ... >
            </application>
            
          
**Note:** The `extractNativeLibs` manifest
attribute has been replaced by the `useLegacyPackaging` DSL
option. For more information, see the release note
[Use the DSL to package compressed
native libraries](https://developer.android.com/studio/releases/archives#compress-native-libs-dsl).

##### Default NDK version

If you download multiple versions of the NDK, the Android Gradle plugin
now selects a default version to use in compiling your source code files.
Previously, the plugin selected the latest downloaded version of the NDK.
Use the `android.ndkVersion` property in the module's
`build.gradle` file to override the plugin-selected default.

##### Simplified R class generation

The Android Gradle plugin simplifies the compile classpath by
generating only one R class for each library module in your project and
sharing those R classes with other module dependencies. This optimization
should result in faster builds, but it requires that you keep the
following in mind:

- Because the compiler shares R classes with upstream module dependencies, it's important that each module in your project uses a unique package name.
- The visibility of a library's R class to other project dependencies is determined by the configuration used to include the library as a dependency. For example, if Library A includes Library B as an 'api' dependency, Library A and other libraries that depend on Library A have access to Library B's R class. However, other libraries might not have access to Library B's R class. If Library A uses the `implementation` dependency configuration. To learn more, read about [dependency
  configurations](https://developer.android.com/studio/build/dependencies#dependency_configurations).

##### Remove resources missing from default
configuration

For Library modules, if you include a resource for a language that you
do not include in the default set of resources---for example, if you include
`hello_world` as a string resource in
`/values-es/strings.xml` but you don't define that resource in
`/values/strings.xml`---the Android Gradle plugin no longer
includes that resource when compiling your project. This behavior change
should result in fewer `Resource Not Found` runtime exceptions
and improved build speed.

##### D8 now respects CLASS retention policy
for annotations

When compiling your app, D8 now respects when annotations apply a CLASS
retention policy, and those annotations are no longer available at
runtime. This behavior also exists when setting the app's target SDK to
API level 23, which previously allowed access to these annotations during
runtime when compiling your app using older versions of the Android Gradle
plugin and D8.

##### Other behavior changes

- `aaptOptions.noCompress` is no longer case sensitive on all platforms (for both APK and bundles) and respects paths that use uppercase characters.
- Data binding is now incremental by default. To learn more, see
  [issue #110061530](https://issuetracker.google.com/110061530).

- All unit tests, including Roboelectric unit tests, are now fully
  cacheable. To learn more, see
  [issue #115873047](https://issuetracker.google.com/115873047).

#### Bug fixes

This version of the Android Gradle plugin includes the following bug
fixes:

- Robolectric unit tests are now supported in library modules that use data binding. To learn more, see [issue #126775542](https://issuetracker.google.com/126775542).
- You can now run `connectedAndroidTest` tasks across multiple modules while Gradle's [parallel
  execution mode](https://guides.gradle.org/performance/#parallel_execution) is enabled.

#### Known issues

This section describes known issues that exist in Android Gradle plugin
3.6.0.

##### Slow performance of Android Lint task

Android Lint can take much longer to complete on some projects due to a
regression in its parsing infrastructure, resulting in slower computation
of inferred types for lambdas in certain code constructs.

The issue is reported as
[a bug in IDEA](https://youtrack.jetbrains.com/issue/IDEA-229655)
and will be fixed in Android Gradle Plugin 4.0.

##### Missing Manifest class {:#agp-missing-manifest}

If your app defines custom permissions in its manifest, the Android
Gradle plugin typically generates a `Manifest.java` class that
includes your custom permissions as string constants. The plugin packages
this class with your app, so you can more easily reference those
permissions at runtime.

Generating the manifest class is broken in Android Gradle plugin 3.6.0.
If you build your app with this version of the plugin, and it references
the manifest class, you might see a `ClassNotFoundException`
exception. To resolve this issue, do one of the following:

- Reference your custom permissions by their fully-qualified name.
  For example,
  `"com.example.myapp.permission.DEADLY_ACTIVITY"`.

- Define your own constants, as shown below:

                  public final class CustomPermissions {
                    public static final class permission {
                      public static final String DEADLY_ACTIVITY="com.example.myapp.permission.DEADLY_ACTIVITY";
                    }
                  }
                  
                
### 3.5.0 (August 2019)

Android Gradle plugin 3.5.0, along with
[Android Studio 3.5](https://developer.android.com/studio/releases#3-5-0), is a major release
and a result of Project Marble, which is a focus on improving three main
areas of the Android developer tools: system health, feature polish, and
fixing bugs. Notably,
[improving project
build speed](https://medium.com/androiddevelopers/improving-build-speed-in-android-studio-3e1425274837) was a main focus for this update.

For information about these and other Project Marble updates, read the
[Android
Developers blog post](https://android-developers.googleblog.com/2019/05/android-studio-35-beta.html) or the sections below.

This version of the Android plugin requires the following:

- [Gradle
  5.4.1](https://docs.gradle.org/5.4.1/release-notes.html).
  To learn more, read the section about
  [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).

- [SDK Build Tools
  28.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**3.5.4 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/studio/releases/archives#4.0.1) for details.

**3.5.3 (December 2019)**


This minor update supports Android Studio 3.5.3 and includes various bug
fixes and performance improvements.

**3.5.2 (November 2019)**


This minor update supports Android Studio 3.5.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/11/android-studio-352-available.html).

**3.5.1 (October 2019)**


This minor update supports Android Studio 3.5.1 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/10/android-studio-351-available.html).

<br />

#### Incremental annotation processing

The [Data Binding](https://developer.android.com/reference/android/databinding/package-summary)
annotation processor supports
[incremental annotation processing](https://docs.gradle.org/current/userguide/java_plugin.html#sec:incremental_annotation_processing)
if you set `android.databinding.incremental=true` in your
`gradle.properties` file. This optimization results in improved
incremental build performance. For a full list of optimized annotation
processors, refer to the table of [incremental annotation
processors](https://docs.gradle.org/current/userguide/java_plugin.html#state_of_support_in_popular_annotation_processors).

Additionally, KAPT 1.3.30 and higher also support incremental annotation
processors, which you can enable by including `kapt.incremental.apt=true` in
your `gradle.properties` file.

<br />

<br />

#### Cacheable unit tests

When you enable unit tests to use Android resources, assets, and
manifests by setting
[`includeAndroidResources`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.TestOptions.UnitTestOptions.html#com.android.build.gradle.internal.dsl.TestOptions.UnitTestOptions:includeAndroidResources)
to `true`, the Android Gradle plugin generates a test config file
containing absolute paths, which breaks cache relocatability. You can instruct
the plugin to instead generate the test config using relative paths, which
allows the `AndroidUnitTest` task to be fully cacheable, by
including the following in your `gradle.properties` file:  

          android.testConfig.useRelativePath = true
        
<br />

<br />

#### Known issues

- When using Kotlin Gradle plugin 1.3.31 or earlier, you might see the
  following warning when building or syncing your project:

                WARNING: API 'variant.getPackageLibrary()' is obsolete and has been replaced
                        with 'variant.getPackageLibraryProvider()'.
                
              
  To resolve
  [this issue](https://youtrack.jetbrains.com/issue/KT-30784),
  upgrade the plugin to version 1.3.40 or higher.

<br />

### 3.4.0 (April 2019)

This version of the Android plugin requires the following:

- [Gradle
  5.1.1](https://docs.gradle.org/5.1.1/release-notes.html) or higher. To learn more, read the section about
  [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).

  Note: When using Gradle 5.0 and higher, the
  [default Gradle daemon memory heap size](https://docs.gradle.org/current/userguide/upgrading_version_4.html#rel5.0:default_memory_settings)
  decreases from 1 GB to 512 MB. This might result in a build performance
  regression. To override this default setting,
  [specify the Gradle daemon heap size](https://docs.gradle.org/current/userguide/build_environment.html#sec:configuring_jvm_memory)
  in your project's `gradle.properties` file.
- [SDK Build Tools
  28.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**3.4.3 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/studio/releases/archives#4.0.1) for details.

**3.4.2 (July 2019)**


This minor update supports Android Studio 3.4.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/07/android-studio-342-available.html).

**3.4.1 (May 2019)**


This minor update supports Android Studio 3.4.1 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/05/android-studio-341-available.html).

<br />

#### New features

- **New lint check dependency configurations:** The
  behavior of `lintChecks` has changed and a new dependency
  configuration, `lintPublish`, has been introduced to give
  you more control over which lint checks are packaged in your Android
  libraries.

  - `lintChecks`: This is an existing configuration that you should use for lint checks you want to only run when building your project locally. If you were previously using the `lintChecks` dependency configuration to include lint checks in the published AAR, you need to migrate those dependencies to instead use the new `lintPublish` configuration described below.
  - `lintPublish`: Use this new configuration in library projects for lint checks you want to include in the published AAR, as shown below. This means that projects that consume your library also apply those lint checks.

  The following code sample uses both dependency configurations in a
  local Android library project.  

  ```groovy
  dependencies {
    // Executes lint checks from the ':lint' project at build time.
    lintChecks project(':lint')
    // Packages lint checks from the ':lintpublish' in the published AAR.
    lintPublish project(':lintpublish')
  }
          
  ```  

  ```kotlin
  dependencies {
    // Executes lint checks from the ':lint' project at build time.
    lintChecks(project(":lint"))
    // Packages lint checks from the ':lintpublish' in the published AAR.
    lintPublish(project(":lintpublish"))
      }
          
  ```
  - In general, packaging and signing tasks should see an overall build
    speed improvement. If you notice a performance regression related to
    these tasks, please [report a bug](https://developer.android.com/studio/report-bugs).

<br />

<br />

#### Behavior changes

- **Android Instant Apps Feature plugin deprecation
  warning:** If you're still using the
  `com.android.feature` plugin to build your instant app,
  Android Gradle plugin 3.4.0 will give throw you a deprecation warning.
  To make sure you can still build you instant app on future versions of
  the plugin, migrate your instant app to using
  [the dynamic feature plugin](https://developer.android.com/studio/projects/dynamic-delivery),
  which also allows you to publish both your installed and instant app
  experiences from a single Android App Bundle.

- **R8 enabled by default:** R8 integrates desugaring,
  shrinking, obfuscating, optimizing, and dexing all in one step---resulting
  in
  [noticeable build performance
  improvements](https://www.google.com/url?q=https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html&sa=D&ust=1551922493258000&usg=AFQjCNH0N1wuMX645n7giw0wjikzjm3WCA). R8 was introduced in Android Gradle plugin 3.3.0 and
  is now enabled by default for both app and Android library projects
  using plugin 3.4.0 and higher.

The image below provides a high-level overview of the compile process
before R8 was introduced.
![Before R8, ProGuard was a different compile step from dexing and
desugaring.](https://developer.android.com/static/studio/images/build/r8/compile_with_d8_proguard.png)

Now, with R8, desugaring, shrinking, obfuscating, optimizing, and dexing (D8)
are all completed in one step, as illustrated below.
![With R8, desugaring, shrinking, obfuscating, optimizing, and
dexing are all performed in a single compile step.](https://developer.android.com/static/studio/images/build/r8/compile_with_r8.png)

Keep in mind, R8 is designed to work with your existing ProGuard rules, so
you'll likely not need to take any actions to benefit from R8. However,
because it's a different technology to ProGuard that's designed specifically
for Android projects, shrinking and optimization may result in removing code
that ProGuard may have not. So, in this unlikely situation, you might need
to add additional rules to keep that code in your build output.

If you experience issues using R8, read the
[R8 compatibility FAQ](https://r8.googlesource.com/r8/+/refs/heads/master/compatibility-faq.md)
to check if there's a solution to your issue. If a solution isn't documented,
please [report a bug](https://issuetracker.google.com/issues/new?component=326788&template=1025938).
You can disable R8 by adding one of the following lines to your project's
`gradle.properties` file:  

          # Disables R8 for Android Library modules only.
          android.enableR8.libraries = false
          # Disables R8 for all modules.
          android.enableR8 = false
          
        
**Note:** For a given build type, if you set
`useProguard` to `false` in your app
module's `build.gradle` file, the Android Gradle plugin uses R8
to shrink your app's code for that build type, regardless of whether you
disable R8 in your project's `gradle.properties` file.

- **`ndkCompile` is deprecated:** You now get a build error if you try to use `ndkBuild` to compile your native libraries. You should instead use either CMake or ndk-build to [Add C and C++ code to your
  project](https://developer.android.com/studio/projects/add-native-code).

<br />

<br />

#### Known issues

- The correct usage of unique package names are currently not enforced
  but will become more strict on later versions of the plugin. On Android
  Gradle plugin version 3.4.0, you can opt-in to check whether your
  project declares acceptable package names by adding the line below to
  your `gradle.properties` file.

                android.uniquePackageNames = true
                
              
  To learn more about setting a package name through the Android Gradle
  plugin, see
  [Set the application ID](https://developer.android.com/studio/build/configure-app-module#set_the_application_id).

<br />

### 3.3.0 (January 2019)

This version of the Android plugin requires the following:

- [Gradle
  4.10.1](https://docs.gradle.org/4.10.1/release-notes.html) or higher. To learn more, read the section about
  [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).

  Note: When using Gradle 5.0 and higher, the
  [default
  Gradle daemon memory heap size](https://docs.gradle.org/current/userguide/upgrading_version_4.html#rel5.0:default_memory_settings) decreases from 1 GB to 512 MB. This
  might result in a build performance regression. To override this default
  setting,
  [specify
  the Gradle daemon heap size](https://docs.gradle.org/current/userguide/build_environment.html#sec:configuring_jvm_memory) in your project's
  `gradle.properties` file.
- [SDK Build Tools 28.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**3.3.3 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/studio/releases/archives#4.0.1) for details.

**3.3.2 (March 2019)**


This minor update supports Android Studio 3.3.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/03/android-studio-332-available.html).

**3.3.1 (February 2019)**

This minor update supports Android Studio 3.3.1 and includes various bug
fixes and performance improvements.

<br />

#### New features

- **Improved classpath synchronization:** When resolving
  dependencies on your runtime and compile time classpaths, the Android
  Gradle plugin attempts to fix certain downstream version conflicts for
  dependencies that appear across multiple classpaths.

  For example, if the runtime classpath includes Library A version 2.0 and the
  compile classpath includes Library A version 1.0, the plugin automatically
  updates the dependency on the compile classpath to Library A version 2.0 to
  avoid errors.

  However, if the runtime classpath includes Library A version 1.0 and the
  compile includes Library A version 2.0, the plugin does not downgrade the
  dependency on the compile classpath to Library A version 1.0, and you will get
  an error. To learn more, see
  [Fix conflicts
  between classpaths](https://developer.android.com/studio/build/dependencies#classpath_conflicts).
- **Improved incremental Java compilation when using annotation
  processors:**
  This update decreases build time by improving support for incremental Java
  compilation when using annotation processors.

  Note: This feature is compatible with Gradle 4.10.1 and higher, except Gradle
  5.1 due to [Gradle
  issue 8194](https://github.com/gradle/gradle/issues/8194).
  - **For projects using Kapt (most Kotlin-only projects and
    Kotlin-Java hybrid projects):** Incremental Java compilation
    is enabled, even when you use data binding or the retro-lambda
    plugin. Annotation processing by the Kapt task is not yet incremental.

  - **For projects not using Kapt (Java-only projects):** If
    the annotation processors you use all support
    [incremental annotation processing](https://docs.gradle.org/4.10.1/userguide/java_plugin.html#sec:incremental_annotation_processing),
    incremental Java compilation is enabled by default. To monitor incremental
    annotation processor adoption, watch
    [Gradle issue 5277](https://github.com/gradle/gradle/issues/5277).

    If, however, one or more annotation processors do not support incremental
    builds, incremental Java compilation is not enabled. Instead, you can
    include the following flag in your `gradle.properties` file:  

        android.enableSeparateAnnotationProcessing=true
                    
    When you include this flag, the Android Gradle plugin executes the
    annotation processors in a separate task and allows the Java compilation
    task to run incrementally.
- **Better debug info when using obsolete API:** When the
  plugin detects that
  you're using an API that's no longer supported, it can now provide
  more-detailed information to help you determine where that API is being used.
  To see the additional info, you need to include the following in your
  project's `gradle.properties` file:

                android.debug.obsoleteApi=true
              
  You can also enable the flag by passing
  `-Pandroid.debug.obsoleteApi=true`
  from the command line.
- You can run instrumentation tests on feature modules from the command
  line.

<br />

<br />

#### Behavior changes

- **Lazy task configuration:** The plugin now uses
  [Gradle's new task creation API](https://docs.gradle.org/current/userguide/task_configuration_avoidance.html)
  to avoid initializing and configuring tasks that are not required to complete
  the current build (or tasks not on the execution task graph). For example, if
  you have multiple build variants, such as "release" and "debug" build
  variants, and you're building the "debug" version of your app, the plugin
  avoids initializing and configuring tasks for the "release" version of your
  app.

  Calling certain older methods in the Variants API, such as
  `variant.getJavaCompile()`, might still force task configuration. To make sure
  that your build is optimized for lazy task configuration, invoke new methods
  that instead return a
  [TaskProvider](https://docs.gradle.org/current/javadoc/org/gradle/api/tasks/TaskProvider.html)
  object, such as `variant.getJavaCompileProvider()`.

  If you execute custom build tasks, learn how to
  [adapt to Gradle's new task-creation API](https://docs.gradle.org/current/userguide/task_configuration_avoidance.html#sec:old_vs_new_configuration_api_overview).
- For a given build type, when setting `useProguard false`, the plugin now
  uses R8 instead of ProGuard to shrink and obfuscate your app's code and
  resources. To learn more about R8, read
  [this blog post](https://android-developers.googleblog.com/2018/11/r8-new-code-shrinker-from-google-is.html)
  from the Android Developer's Blog.

- **Faster R class generation for library projects:** Previously, the Android
  Gradle plugin would generate an `R.java` file for each of your project's
  dependencies and then compile those R classes alongside your app's other
  classes. The plugin now generates a JAR containing your app's compiled R class
  directly, without first building intermediate `R.java` classes. This
  optimization may significantly improve build performance for projects that
  include many library subprojects and dependencies, and improve the indexing
  speed in Android Studio.

- When building an [Android App Bundle](https://developer.android.com/guide/app-bundle), APKs generated from
  that app bundle that target Android 6.0 (API level 23) or higher now include
  uncompressed versions of your native libraries by default. This optimization
  avoids the need for the device to make a copy of the library and thus reduces
  the on-disk size of your app. If you'd rather disable this optimization, add
  the following to your `gradle.properties` file:

      android.bundle.enableUncompressedNativeLibs = false
              
- The plugin enforces minimum versions of some third-party plugins.

- **Single-variant project sync** :
  [Syncing your project](https://developer.android.com/studio/build#sync-files)
  with your build configuration is an important step in letting Android Studio
  understand how your project is structured. However, this process can be
  time-consuming for large projects. If your project uses multiple build
  variants, you can now optimize project syncs by limiting them to only the
  variant you have currently selected.

  You need to use Android Studio 3.3 or higher with Android Gradle Plugin 3.3.0
  or higher to enable this optimization. When you meet these requirements, the
  IDE prompts you to enable this optimization when you sync your project. The
  optimization is also enabled by default on new projects.

  To enable this optimization manually, click **File \> Settings \> Experimental**
  **\> Gradle** (**Android Studio \> Preferences \> Experimental \> Gradle** on a
  Mac) and select the **Only sync the active variant** checkbox.

  **Note**: This optimization fully supports projects that
  include Java and C++ languages, and has some support for Kotlin. When enabling
  the optimization for projects with Kotlin content, Gradle sync falls back to
  using full variants internally.
- **Automatic downloading of missing SDK packages** : This functionality has
  been expanded to support NDK. To learn more, read
  [Auto-download missing
  packages with Gradle](https://developer.android.com/studio/intro/update#download-with-gradle).

<br />

<br />

#### Bug Fixes

- Android Gradle plugin 3.3.0 fixes the following issues:

  - The build process calling `android.support.v8.renderscript.RenderScript` instead of the AndroidX version, despite Jetifier being enabled
  - Clashes due to `androidx-rs.jar` including statically bundled `annotation.AnyRes`
  - When using RenderScript, you no longer have to manually set the Build Tools version in your `build.gradle` files

<br />

### 3.2.0 (September 2018)

This version of the Android plugin requires the following:

- [Gradle 4.6](https://docs.gradle.org/4.6/release-notes.html) or higher. To learn more, read the section about [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).
- [SDK Build Tools
  28.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**3.2.1 (October 2018)**

With this update, you no longer need to specify a version for the SDK Build
Tools. The Android Gradle plugin now uses version 28.0.3 by default.

<br />

#### New features

- **Support for building Android App Bundles:** The app bundle is a new upload
  format that includes all your app's compiled code and resources while
  deferring APK generation and signing to the Google Play Store. You no longer
  have to build, sign, and manage multiple APKs, and users get smaller downloads
  that are optimized for their device. To learn more, read
  [About Android App Bundles](https://developer.android.com/guide/app-bundle).

- **Support for improved incremental build speeds when using annotation processors:**
  The [`AnnotationProcessorOptions`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.AnnotationProcessorOptions.html)
  DSL now extends [`CommandLineArgumentProvider`](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html),
  which enables either you or the annotation processor author to annotate
  arguments for the processor using
  [incremental build property type annotations](https://docs.gradle.org/current/userguide/more_about_tasks.html#sec:up_to_date_checks).
  Using these annotations improves the correctness and performance of
  incremental and cached clean builds. To learn more, read
  [Pass arguments to annotation processors](https://developer.android.com/studio/build/dependencies#processor-arguments).

- **Migration tool for AndroidX:** When using Android Gradle plugin 3.2.0 with
  Android 3.2 and higher, you can migrate your project's local and Maven
  dependencies to use the new AndroidX libraries by selecting **Refactor \>
  Migrate to AndroidX** from the menu bar. Using this migration tool also sets
  the following flags to `true` in your `gradle.properties` file:

  - **`android.useAndroidX`:** When set to `true`, the Android plugin uses the
    appropriate AndroidX library instead of a Support Library. When this flag
    is not specified, the plugin sets it to `false` by default.

  - **`android.enableJetifier`:** When set to `true`, the Android plugin
    automatically migrates existing third-party libraries to use AndroidX by
    rewriting their binaries. When this flag is not specified, the plugin sets
    it to `false` by default. You can set this flag to `true` only while
    `android.useAndroidX` is also set to `true`, otherwise you get a build error.

    To learn more, read the [AndroidX overview](https://developer.android.com/topic/libraries/support-library/androidx-overview).
- **New code shrinker, R8:** R8 is a new tool for code shrinking and obfuscation
  that replaces ProGuard. You can start using the preview version of R8 by
  including the following in your project's `gradle.properties` file:

  ```groovy
          android.enableR8 = true
          
  ```  

  ```kotlin
          android.enableR8 = true
          
  ```

<br />

<br />

#### Behavior changes

- Desugaring with D8 is now enabled by default.

- AAPT2 is now on Google's Maven repo. To use AAPT2, make sure that you
  have the `google()` dependency in your `build.gradle`
  file, as shown below:

  ```groovy
            buildscript {
                  repositories {
                      google() // here
                      jcenter()
                  }
                  dependencies {
                      classpath 'com.android.tools.build:gradle:3.2.0'
                  }
              }
              allprojects {
                  repositories {
                      google() // and here
                      jcenter()
              }
            
  ```  

  ```kotlin
            buildscript {
                  repositories {
                      google() // here
                      jcenter()
                  }
                  dependencies {
                      classpath 'com.android.tools.build:gradle:3.2.0'
                  }
              }
              allprojects {
                  repositories {
                      google() // and here
                      jcenter()
              }
            
  ```
- Native multidex is now enabled by default. Previous versions of Android
  Studio enabled native multidex when deploying the debug version of an app to a
  device running Android API level 21 or higher. Now, whether you're deploying
  to a device or building an APK for release, the Android Gradle plugin
  enables native multidex for all modules that set
  `minSdkVersion=21` or higher.

- The plugin now enforces a minimum version of the protobuf plugin (0.8.6),
  Kotlin plugin (1.2.50), and Crashlytics plugin (1.25.4).

- The feature module plugin,`com.android.feature`, now
  enforces the use of only letters, digits, and underscores when specifying
  a module name. For example, if your feature module name includes dashes,
  you get a build error. This behavior matches that of the dynamic feature
  plugin.

<br />

<br />

#### Bug fixes

- JavaCompile is now cacheable in projects with data binding. ([Issue #69243050](https://issuetracker.google.com/69243050))
- Better compile avoidance for library modules with data binding. ([Issue #77539932](https://issuetracker.google.com/77539932))
- You can now re-enable [configure-on-demand](https://docs.gradle.org/current/userguide/multi_project_builds.html#sec:configuration_on_demand) if you've disable it in earlier versions due to some unpredictable build errors. ([Issue #77910727](https://issuetracker.google.com/77910727))

<br />

### 3.1.0 (March 2018)

This version of the Android plugin requires the following:

- [Gradle
  4.4](https://docs.gradle.org/current/release-notes.html) or higher.

  To learn more, read the section about
  [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).
- [Build Tools
  27.0.3](https://developer.android.com/studio/releases/build-tools#notes) or higher.

  Keep in mind, you no longer need to specify a version for the build
  tools using the `android.buildToolsVersion` property---the
  plugin uses the minimum required version by default.

#### New DEX compiler, D8

By default, Android Studio now uses a new DEX compiler called D8. DEX
compilation is the process of transforming `.class` bytecode into
`.dex` bytecode for the Android Runtime (or Dalvik, for older
versions of Android). Compared to the previous compiler, called DX, D8
compiles faster and outputs smaller DEX files, all while having the same or
better app runtime performance.

D8 shouldn't change your day-to-day app development workflow. However, if
you experience any issues related to the new compiler, please
[report a bug](https://developer.android.com/studio/report-bugs). You can temporarily
disable D8 and use DX by including the following in your project's
`gradle.properties` file:  

          android.enableD8=false
        
For projects that
[use Java 8 language features](https://developer.android.com/studio/write/java8-support),
incremental desugaring is enabled by default. You can disable it by
specifying the following in your project's `gradle.properties` file:  

          android.enableIncrementalDesugaring=false.
        

**Preview users:** If you're already using a preview version of D8, note
that it now compiles against libraries included in the
[SDK build tools](https://developer.android.com/studio/releases/build-tools)---not the JDK.
So, if you are accessing APIs that exist in the JDK but not in the SDK build
tools libraries, you get a compile error.

#### Behavior changes

- When building multiple APKs that each target a different ABI, the
  no longer generates APKs for the following ABIs by default:
  `mips`, `mips64`, and `armeabi`.

  If you want to build APKs that target these ABIs, you must use
  [NDK r16b or lower](https://developer.android.com/ndk/downloads/revision_history) and
  specify the ABIs in your `build.gradle` file, as shown below:  

  ```groovy
            splits {
                abi {
                    include 'armeabi', 'mips', 'mips64'
                    ...
                }
            }
          
  ```  

  ```kotlin
            splits {
                abi {
                    include("armeabi", "mips", "mips64")
                    ...
                }
            }
          
  ```
- The Android plugin's [build
  cache](https://developer.android.com/studio/build/build-cache) now evicts cache entries that are older than 30 days.

- Passing `"auto"` to
  [`resConfig`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:resConfig(java.lang.String))
  no longer automatically picks string resources to package into your APK.
  If you continue to use `"auto"`, the plugin packages all string
  resources your app and its dependencies provide. So, you should instead
  specify each locale that you want the plugin to package into your APK.

- Because local modules can't depend on your app's test APK, adding
  dependencies to your instrumented tests using the
  `androidTestApi` configuration, instead of
  `androidTestImplementation`, causes Gradle to issue the
  following warning:

  ```groovy
          WARNING: Configuration 'androidTestApi' is obsolete
          and has been replaced with 'androidTestImplementation'
          
  ```  

  ```kotlin
          WARNING: Configuration 'androidTestApi' is obsolete
          and has been replaced with 'androidTestImplementation'
          
  ```

#### Fixes

- Fixes an issue where Android Studio doesn't properly recognize dependencies in composite builds.
- Fixes an issue where you get a project sync error when loading the Android plugin multiple times in a single build--for example, when multiple subprojects each include the Android plugin in their buildscript classpath.  

### 3.0.0 (October 2017)

Android Gradle plugin 3.0.0 includes a variety of changes that aim to
address performance issues of large projects.

For example, on a
[sample skeleton
project](https://github.com/jmslau/perf-android-large.git) with \~130 modules and a large number of external dependencies
(but no code or resources), you can experience performance improvements
similar to the following:  

| Android plugin version + Gradle version | Android plugin 2.2.0 + Gradle 2.14.1 | Android plugin 2.3.0 + Gradle 3.3 | Android plugin 3.0.0 + Gradle 4.1 |
| Configuration (e.g. running `./gradlew --help`) | \~2 mins | \~9 s | \~2.5 s |
| 1-line Java change (implementation change) | \~2 mins 15 s | \~29 s | \~6.4 s |
|---|---|---|---|

Some of these changes break existing builds. So, you should consider the\\
effort of migrating your project before using the new plugin.

If you don't experience the performance improvements described above,
please [file a bug](https://issuetracker.google.com/issues/new?component=192708&template=840533)
and include a trace of your build using the
[Gradle Profiler](https://github.com/gradle/gradle-profiler).

This version of the Android plugin requires the following:

- [Gradle 4.1](https://docs.gradle.org/current/release-notes.html) or higher. To learn more, read the section about [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).
- [Build Tools 26.0.2](https://developer.android.com/studio/releases/build-tools#notes) or higher. With this update, you no longer need to specify a version for the build tools---the plugin uses the minimum required version by default. So, you can now remove the `android.buildToolsVersion` property.


**3.0.1 (November 2017)**

This is a minor update to support Android Studio 3.0.1, and includes general
bug fixes and performance improvements.

#### Optimizations

- Better parallelism for multi-module projects through a fine grained task graph.
- When making changes to dependency, Gradle performs faster builds by not re-compiling modules that do not have access to that dependency's API. You should restrict which dependencies leak their APIs to other modules by [using
  Gradle's new dependency configurations](https://developer.android.com/studio/build/dependencies#dependency_configurations): `implementation`, `api`, `compileOnly`, and `runtimeOnly`.
- Faster incremental build speed due to per-class dexing. Each class is now compiled into separate DEX files, and only the classes that are modified are re-dexed. You should also expect improved build speeds for apps that set `minSdkVersion` to 20 or lower, and use [legacy multi-dex](https://developer.android.com/studio/build/multidex#mdex-pre-l).
- Improved build speeds by optimizing certain tasks to use chached outputs. To benefit from this optimization, you need to first [enable the Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html#sec:build_cache_enable).
- Improved incremental resource processing using AAPT2, which is now enabled by default. If you are experiencing issues while using AAPT2, please [report a bug](https://developer.android.com/studio/report-bugs). You can also disable AAPT2 by setting `android.enableAapt2=false` in your `gradle.properties` file and restarting the Gradle daemon by running `./gradlew --stop` from the command line.

#### New features

- [Variant-aware dependency
  management](https://developer.android.com/studio/build/build-variants#variant_aware). When building a certain variant of a module, the plugin now automatically matches variants of local library module dependencies to the variant of the module you are building.
- Includes a new Feature module plugin to support [Android Instant Apps](https://developer.android.com/topic/instant-apps) and the Android Instant Apps SDK (which you can download [using the SDK manager](https://developer.android.com/studio/intro/update#sdk-manager)). To learn more about creating Feature modules with the new plugin, read [Structure of an
  instant app with multiple features](https://developer.android.com/topic/instant-apps/getting-started/structure#structure_of_an_instant_app_with_multiple_features).
- Built-in support for using certain Java 8 language features and Java 8 libraries. **Jack is now deprecated and no longer required** , and you should first disable Jack to use the improved Java 8 support built into the default toolchain. For more information, read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support).
- Added support for running tests with
  [Android
  Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), which allows you to run each of your app's tests within
  its own invocation of Instrumentation. Because each test runs in its own
  Instrumentation instance, any shared state between tests doesn't accumulate
  on your device's CPU or memory. And, even if one test crashes, it takes down
  only its own instance of Instrumentation, so your other tests still run.

  - Added `testOptions.execution` to determine whether to use on-device test orchestration. If you want to [use
    Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), you need to specify `ANDROID_TEST_ORCHESTRATOR`, as shown below. By default, this property is set to `HOST`, which disables on-device orchestration and is the standard method of running tests.

  ### Groovy

  ```groovy
          android {
            testOptions {
              execution 'ANDROID_TEST_ORCHESTRATOR'
            }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
            testOptions {
              execution = "ANDROID_TEST_ORCHESTRATOR"
            }
          }
          
  ```
- New `androidTestUtil` dependency configuration allows you to
  install another test helper APK before running your instrumentation tests,
  such as Android Test Orchestrator:

  ### Groovy

  ```groovy
          dependencies {
            androidTestUtil 'com.android.support.test:orchestrator:1.0.0'
            ...
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
            androidTestUtil("com.android.support.test:orchestrator:1.0.0")
            ...
          }
          
  ```
- Added `testOptions.unitTests.includeAndroidResources` to
  support unit tests that require Android resources, such as
  [Roboelectric](http://robolectric.org/). When you set this
  property to `true`, the plugin performs resource, asset, and
  manifest merging before running your unit tests. Your tests can then
  inspect `com/android/tools/test_config.properties` on the
  classpath for the following keys:

  - `android_merged_assets`: the absolute path to the
    merged assets directory.

    **Note:** For library modules, the merged assets
    do not contain the assets of dependencies (see
    [issue
    #65550419](https://issuetracker.google.com/65550419)).
  - `android_merged_manifest`: the absolute path to the
    merged manifest file.

  - `android_merged_resources`: the absolute path to the
    merged resources directory, which contains all the resources from
    the module and all its dependencies.

  - `android_custom_package`: the package name of the
    final R class. If you dynamically modify the application ID, this
    package name may not match the `package` attribute in the
    app's manifest.

- Support for [fonts
  as resources](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml) (which is a new feature introduced in [Android 8.0 (API level 26)](https://developer.android.com/about/versions/oreo)).
- Support for language-specific APKs with [Android
  Instant Apps SDK 1.1](https://developer.android.com/topic/instant-apps/release-notes#android_instant_apps_development_sdk_v110) and higher.
- You can now change the output directory for your external native build
  project, as shown below:

  ### Groovy

  ```groovy
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory "./outputs/cmake"
                  }
              }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory = "./outputs/cmake"
                  }
              }
          }
          
  ```
- You can now [use CMake 3.7 or
  higher](https://developer.android.com/studio/projects/install-ndk#vanilla_cmake) when building native projects from Android Studio.
- New `lintChecks` dependency configuration allows you to
  build a JAR that defines custom lint rules, and package it into your AAR
  and APK projects.

  Your custom lint rules must belong to a separate project that outputs
  a single JAR and includes only
  [`compileOnly`](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)
  dependencies. Other app and library modules can then depend on your lint
  project using the `lintChecks` configuration:  

  ### Groovy

  ```groovy
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks project(':lint-checks')
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks(project(":lint-checks"))
          }
          
  ```

#### Behavior changes

- Android plugin 3.0.0 removes certain APIs, and your build will break if you use them. For example, you can no longer use the Variants API to access `outputFile()` objects or use `processManifest.manifestOutputFile()` to get the manifest file for each variant. To learn more, read [API changes](https://developer.android.com/studio/known-issues#variant_api).
- You no longer need to specify a version for the build tools (so, you can now remove the `android.buildToolsVersion` property). By default, the plugin automatically uses the minimum required build tools version for the version of Android plugin you're using.
- You now enable/disable PNG crunching in the `buildTypes` block, as shown below. PNG crunching is enabled by default for all builds except debug builds because it increases build times for projects that include many PNG files. So, to improve build times for other build types, you should either disable PNG crunching or [convert
  your images to WebP](https://developer.android.com/studio/write/convert-webp#convert_images_to_webp).  

  ### Groovy

  ```groovy
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              crunchPngs false
            }
          }
        }
        
  ```

  ### Kotlin

  ```kotlin
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              isCrunchPngs = false
            }
          }
        }
        
  ```
- The Android plugin now automatically builds executable targets that you configure in your external CMake projects.
- You must now [add annotation
  processors](https://developer.android.com/studio/build/dependencies#annotation_processor) to the processor classpath using the `annotationProcessor` dependency configuration.
- Using the deprecated `ndkCompile` is now more restricted. You should instead migrate to using either CMake or ndk-build to compile native code that you want to package into your APK. To learn more, read [Migrate from
ndkcompile](https://developer.android.com/studio/projects/add-native-code#ndkCompile).  

### 3.0.0 (October 2017)

Android Gradle plugin 3.0.0 includes a variety of changes that aim to
address performance issues of large projects.

For example, on a
[sample skeleton
project](https://github.com/jmslau/perf-android-large.git) with \~130 modules and a large number of external dependencies
(but no code or resources), you can experience performance improvements
similar to the following:  

| Android plugin version + Gradle version | Android plugin 2.2.0 + Gradle 2.14.1 | Android plugin 2.3.0 + Gradle 3.3 | Android plugin 3.0.0 + Gradle 4.1 |
| Configuration (e.g. running `./gradlew --help`) | \~2 mins | \~9 s | \~2.5 s |
| 1-line Java change (implementation change) | \~2 mins 15 s | \~29 s | \~6.4 s |
|---|---|---|---|

Some of these changes break existing builds. So, you should consider the\\
effort of migrating your project before using the new plugin.

If you don't experience the performance improvements described above,
please [file a bug](https://issuetracker.google.com/issues/new?component=192708&template=840533)
and include a trace of your build using the
[Gradle Profiler](https://github.com/gradle/gradle-profiler).

This version of the Android plugin requires the following:

- [Gradle 4.1](https://docs.gradle.org/current/release-notes.html) or higher. To learn more, read the section about [updating Gradle](https://developer.android.com/studio/releases/archives#updating-gradle).
- [Build Tools 26.0.2](https://developer.android.com/studio/releases/build-tools#notes) or higher. With this update, you no longer need to specify a version for the build tools---the plugin uses the minimum required version by default. So, you can now remove the `android.buildToolsVersion` property.


**3.0.1 (November 2017)**

This is a minor update to support Android Studio 3.0.1, and includes general
bug fixes and performance improvements.

#### Optimizations

- Better parallelism for multi-module projects through a fine grained task graph.
- When making changes to dependency, Gradle performs faster builds by not re-compiling modules that do not have access to that dependency's API. You should restrict which dependencies leak their APIs to other modules by [using
  Gradle's new dependency configurations](https://developer.android.com/studio/build/dependencies#dependency_configurations): `implementation`, `api`, `compileOnly`, and `runtimeOnly`.
- Faster incremental build speed due to per-class dexing. Each class is now compiled into separate DEX files, and only the classes that are modified are re-dexed. You should also expect improved build speeds for apps that set `minSdkVersion` to 20 or lower, and use [legacy multi-dex](https://developer.android.com/studio/build/multidex#mdex-pre-l).
- Improved build speeds by optimizing certain tasks to use chached outputs. To benefit from this optimization, you need to first [enable the Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html#sec:build_cache_enable).
- Improved incremental resource processing using AAPT2, which is now enabled by default. If you are experiencing issues while using AAPT2, please [report a bug](https://developer.android.com/studio/report-bugs). You can also disable AAPT2 by setting `android.enableAapt2=false` in your `gradle.properties` file and restarting the Gradle daemon by running `./gradlew --stop` from the command line.

#### New features

- [Variant-aware dependency
  management](https://developer.android.com/studio/build/build-variants#variant_aware). When building a certain variant of a module, the plugin now automatically matches variants of local library module dependencies to the variant of the module you are building.
- Includes a new Feature module plugin to support [Android Instant Apps](https://developer.android.com/topic/instant-apps) and the Android Instant Apps SDK (which you can download [using the SDK manager](https://developer.android.com/studio/intro/update#sdk-manager)). To learn more about creating Feature modules with the new plugin, read [Structure of an
  instant app with multiple features](https://developer.android.com/topic/instant-apps/getting-started/structure#structure_of_an_instant_app_with_multiple_features).
- Built-in support for using certain Java 8 language features and Java 8 libraries. **Jack is now deprecated and no longer required** , and you should first disable Jack to use the improved Java 8 support built into the default toolchain. For more information, read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support).
- Added support for running tests with
  [Android
  Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), which allows you to run each of your app's tests within
  its own invocation of Instrumentation. Because each test runs in its own
  Instrumentation instance, any shared state between tests doesn't accumulate
  on your device's CPU or memory. And, even if one test crashes, it takes down
  only its own instance of Instrumentation, so your other tests still run.

  - Added `testOptions.execution` to determine whether to use on-device test orchestration. If you want to [use
    Android Test Orchestrator](https://developer.android.com/training/testing/junit-runner#using-android-test-orchestrator), you need to specify `ANDROID_TEST_ORCHESTRATOR`, as shown below. By default, this property is set to `HOST`, which disables on-device orchestration and is the standard method of running tests.

  ### Groovy

  ```groovy
          android {
            testOptions {
              execution 'ANDROID_TEST_ORCHESTRATOR'
            }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
            testOptions {
              execution = "ANDROID_TEST_ORCHESTRATOR"
            }
          }
          
  ```
- New `androidTestUtil` dependency configuration allows you to
  install another test helper APK before running your instrumentation tests,
  such as Android Test Orchestrator:

  ### Groovy

  ```groovy
          dependencies {
            androidTestUtil 'com.android.support.test:orchestrator:1.0.0'
            ...
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
            androidTestUtil("com.android.support.test:orchestrator:1.0.0")
            ...
          }
          
  ```
- Added `testOptions.unitTests.includeAndroidResources` to
  support unit tests that require Android resources, such as
  [Roboelectric](http://robolectric.org/). When you set this
  property to `true`, the plugin performs resource, asset, and
  manifest merging before running your unit tests. Your tests can then
  inspect `com/android/tools/test_config.properties` on the
  classpath for the following keys:

  - `android_merged_assets`: the absolute path to the
    merged assets directory.

    **Note:** For library modules, the merged assets
    do not contain the assets of dependencies (see
    [issue
    #65550419](https://issuetracker.google.com/65550419)).
  - `android_merged_manifest`: the absolute path to the
    merged manifest file.

  - `android_merged_resources`: the absolute path to the
    merged resources directory, which contains all the resources from
    the module and all its dependencies.

  - `android_custom_package`: the package name of the
    final R class. If you dynamically modify the application ID, this
    package name may not match the `package` attribute in the
    app's manifest.

- Support for [fonts
  as resources](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml) (which is a new feature introduced in [Android 8.0 (API level 26)](https://developer.android.com/about/versions/oreo)).
- Support for language-specific APKs with [Android
  Instant Apps SDK 1.1](https://developer.android.com/topic/instant-apps/release-notes#android_instant_apps_development_sdk_v110) and higher.
- You can now change the output directory for your external native build
  project, as shown below:

  ### Groovy

  ```groovy
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory "./outputs/cmake"
                  }
              }
          }
          
  ```

  ### Kotlin

  ```kotlin
          android {
              ...
              externalNativeBuild {
                  // For ndk-build, instead use the ndkBuild block.
                  cmake {
                      ...
                      // Specifies a relative path for outputs from external native
                      // builds. You can specify any path that's not a subdirectory
                      // of your project's temporary build/ directory.
                      buildStagingDirectory = "./outputs/cmake"
                  }
              }
          }
          
  ```
- You can now [use CMake 3.7 or
  higher](https://developer.android.com/studio/projects/install-ndk#vanilla_cmake) when building native projects from Android Studio.
- New `lintChecks` dependency configuration allows you to
  build a JAR that defines custom lint rules, and package it into your AAR
  and APK projects.

  Your custom lint rules must belong to a separate project that outputs
  a single JAR and includes only
  [`compileOnly`](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)
  dependencies. Other app and library modules can then depend on your lint
  project using the `lintChecks` configuration:  

  ### Groovy

  ```groovy
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks project(':lint-checks')
          }
          
  ```

  ### Kotlin

  ```kotlin
          dependencies {
              // This tells the Gradle plugin to build ':lint-checks' into a lint.jar file
              // and package it with your module. If the module is an Android library,
              // other projects that depend on it automatically use the lint checks.
              // If the module is an app, lint includes these rules when analyzing the app.
              lintChecks(project(":lint-checks"))
          }
          
  ```

#### Behavior changes

- Android plugin 3.0.0 removes certain APIs, and your build will break if you use them. For example, you can no longer use the Variants API to access `outputFile()` objects or use `processManifest.manifestOutputFile()` to get the manifest file for each variant. To learn more, read [API changes](https://developer.android.com/studio/known-issues#variant_api).
- You no longer need to specify a version for the build tools (so, you can now remove the `android.buildToolsVersion` property). By default, the plugin automatically uses the minimum required build tools version for the version of Android plugin you're using.
- You now enable/disable PNG crunching in the `buildTypes` block, as shown below. PNG crunching is enabled by default for all builds except debug builds because it increases build times for projects that include many PNG files. So, to improve build times for other build types, you should either disable PNG crunching or [convert
  your images to WebP](https://developer.android.com/studio/write/convert-webp#convert_images_to_webp).  

  ### Groovy

  ```groovy
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              crunchPngs false
            }
          }
        }
        
  ```

  ### Kotlin

  ```kotlin
        android {
          buildTypes {
            release {
              // Disables PNG crunching for the release build type.
              isCrunchPngs = false
            }
          }
        }
        
  ```
- The Android plugin now automatically builds executable targets that you configure in your external CMake projects.
- You must now [add annotation
  processors](https://developer.android.com/studio/build/dependencies#annotation_processor) to the processor classpath using the `annotationProcessor` dependency configuration.
- Using the deprecated `ndkCompile` is now more restricted. You should instead migrate to using either CMake or ndk-build to compile native code that you want to package into your APK. To learn more, read [Migrate from
ndkcompile](https://developer.android.com/studio/projects/add-native-code#ndkCompile).  

### 2.3.0 (February 2017)

**2.3.3 (June 2017)**

This is a minor update that adds compatibility with
[Android Studio 2.3.3](https://developer.android.com/studio/releases#Revisions).

**2.3.2 (May 2017)**

This is a minor update that adds compatibility with
[Android Studio
2.3.2](https://developer.android.com/studio/releases#Revisions).

**2.3.1 (April 2017)**

This is a minor update to Android plugin 2.3.0 that fixes an issue
where some physical Android devices did not work properly with
[Instant Run](https://developer.android.com/studio/run#instant-run) (see
[Issue #235879](https://code.google.com/p/android/issues/detail?id=235879)).

Dependencies:
:
    - Gradle 3.3 or higher.
    - [Build Tools 25.0.0](https://developer.android.com/tools/revisions/build-tools) or higher.

New:
:
    - Uses Gradle 3.3, which includes performance improvements and new features. For more details, see the [Gradle release notes](https://docs.gradle.org/3.3/release-notes).
    - **Build cache** : stores certain outputs that the Android plugin generates when building your project (such as unpackaged AARs and pre-dexed remote dependencies). Your clean builds are much faster while using the cache because the build system can simply reuse those cached files during subsequent builds, instead of recreating them. Projects using Android plugin 2.3.0 and higher use the build cache by default. To learn more, read [Improve Build Speed with
      Build Cache](https://developer.android.com/studio/build/build-cache).
      - Includes a `cleanBuildCache` task that [clears
        the build cache](https://developer.android.com/studio/build/build-cache#clear_the_build_cache).
      - If you are using the experimental version of build cache (included in earlier versions of the plugin), you should [update your plugin](https://developer.android.com/studio/releases/archives#updating-plugin) to the latest version.

Changes:
:
    - Supports changes to Instant Run included in [Android Studio 2.3](https://developer.android.com/studio/releases).
    - Configuration times for very large projects should be significantly faster.
    - Fixed issues with auto-downloading for the [constraint layout
      library](https://developer.android.com/training/constraint-layout).
    - Plugin now uses [ProGuard version 5.3.2](https://www.guardsquare.com/en/proguard/manual/versions).
    - Includes many fixes for [reported bugs](https://code.google.com/p/android/issues/list?can=1&q=Component%3DTools++Subcomponent%3DTools-gradle,Tools-build,Tools-instantrun,Tools-cpp-build+Target%3D2.3+status:FutureRelease,Released+&sort=priority+-status&colspec=ID+Status+Priority+Owner+Summary+Stars+Reporter+Opened&cells=tiles). Please continue to [file bug reports](https://developer.android.com/studio/report-bugs) when you encounter issues.

### 2.2.0 (September 2016)

Dependencies:
:
    - Gradle 2.14.1 or higher.
    - [Build Tools 23.0.2](https://developer.android.com/tools/revisions/build-tools) or higher.

New:
:
    - Uses Gradle 2.14.1, which includes performance improvements and new features, and fixes a security vulnerability that allows local privilege escalation when using the Gradle daemon. For more details, see the [Gradle release notes](https://docs.gradle.org/2.14.1/release-notes).
    - Using the [`externalNativeBuild {}`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ExternalNativeBuild.html) DSL, Gradle now lets you link to your native sources and compile native libraries using CMake or ndk-build. After building your native libraries, Gradle packages them into your APK. To learn more about using CMake and ndk-build with Gradle, read [Add C and C++ Code to Your
      Project](https://developer.android.com/studio/projects/add-native-code).
    - When you [run a
      build from the command line](https://developer.android.com/studio/build/building-cmdline), Gradle now attempts to auto-download any missing SDK components or updates that your project depends on. To learn more, read [Auto-download
      missing packages with Gradle](https://developer.android.com/studio/intro/update#download-with-gradle).
    - A new experimental caching feature lets Gradle speed up build times by pre-dexing, storing, and reusing the pre-dexed versions of your libraries. To learn more about using this experimental feature, read the [Build
      Cache](https://developer.android.com/studio/build/build-cache) guide.
    - Improves build performance by adopting a new default packaging pipeline which handles zipping, signing, and [zipaligning](https://developer.android.com/studio/command-line/zipalign) in one task. You can revert to using the older packaging tools by adding `android.useOldPackaging=true` to your `gradle.properties` file. While using the new packaging tool, the `zipalignDebug` task is not available. However, you can create one yourself by calling the `createZipAlignTask(String taskName, File inputFile, File
      outputFile)` method.
    - APK signing now uses [APK Signature Scheme
      v2](https://developer.android.com/about/versions/nougat/android-7.0#apk_signature_v2) in addition to traditional JAR signing. All Android platforms accept the resulting APKs. Any modification to these APKs after signing invalidates their v2 signatures and prevents installation on a device. To disable this feature, add the following to your module-level `build.gradle` file:  

      ### Groovy

      ```groovy
      android {
        ...
        signingConfigs {
          config {
            ...
            v2SigningEnabled false
          }
        }
      }
            
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        signingConfigs {
          create("config") {
            ...
            v2SigningEnabled = false
          }
        }
      }
            
      ```
    - For multidex builds, you can now use ProGuard rules to determine which classes Gradle should compile into your app's *main* DEX file. Because the Android system loads the main DEX file first when starting your app, you can prioritize certain classes at startup by compiling them into the main DEX file. After you create a ProGuard configuration file specifically for your main DEX file, pass the configuration file's path to Gradle using [buildTypes.multiDexKeepProguard](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:multiDexKeepProguard). Using this DSL is different from using [`buildTypes.proguardFiles`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:proguardFiles(java.lang.Object[])), which provides general ProGuard rules for your app and does not specify classes for the main DEX file.
    - Adds support for the `android:extractNativeLibs` flag, which can reduce the size of your app when you install it on a device. When you set this flag to `false` in the [`<application>`](https://developer.android.com/guide/topics/manifest/application-element) element of your app manifest, Gradle packages uncompressed and aligned versions of your native libraries with your APK. This prevents [`PackageManager`](https://developer.android.com/reference/android/content/pm/PackageManager) from copying out your native libraries from the APK to the device's file system during installation and has the added benefit of making delta updates of your app smaller.
    - You can now specify [`versionNameSuffix`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:versionNameSuffix) and [`applicationIdSuffix`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.ProductFlavor.html#com.android.build.gradle.internal.dsl.ProductFlavor:applicationIdSuffix) for product flavors. ([Issue 59614](http://b.android.com/59614))


Changes:
:
    - `getDefaultProguardFile` now returns the default ProGuard files that Android plugin for Gradle provides and no longer uses the ones in the Android SDK.
    - Improved Jack compiler performance and features:
      - Jack now supports Jacoco test coverage when setting [testCoverageEnabled](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.BuildType.html#com.android.build.gradle.internal.dsl.BuildType:testCoverageEnabled) to `true`.
      - Improved support for annotation processors. Annotation processors on your classpath, such as any `compile` dependencies, are automatically applied to your build. You can also specify an annotation processor in your build and pass arguments by using the [`javaCompileOptions.annotationProcessorOptions {}`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.AnnotationProcessorOptions.html) DSL in your module-level `build.gradle` file:  

        ### Groovy

        ```groovy
        android {
          ...
          defaultConfig {
            ...
            javaCompileOptions {
              annotationProcessorOptions {
                className 'com.example.MyProcessor'
                // Arguments are optional.
                arguments = [ foo : 'bar' ]
              }
            }
          }
        }
            
        ```

        ### Kotlin

        ```kotlin
        android {
          ...
          defaultConfig {
            ...
            javaCompileOptions {
              annotationProcessorOptions {
                className = "com.example.MyProcessor"
                // Arguments are optional.
                arguments(mapOf(foo to "bar"))
              }
            }
          }
        }
            
        ```


        If you want to apply an annotation processor at compile
        time but not include it in your APK, use the
        `annotationProcessor` dependency scope:  

        ### Groovy

        ```groovy
        dependencies {
            compile 'com.google.dagger:dagger:2.0'
            annotationProcessor 'com.google.dagger:dagger-compiler:2.0'
           // or use buildVariantAnnotationProcessor to target a specific build variant
        }
            
        ```

        ### Kotlin

        ```kotlin
        dependencies {
            implementation("com.google.dagger:dagger:2.0")
            annotationProcessor("com.google.dagger:dagger-compiler:2.0")
           // or use buildVariantAnnotationProcessor to target a specific build variant
        }
            
        ```
      - For a list of parameters you can set, run the following from the command line:  

      ```
      java -jar /build-tools/jack.jar --help-properties
      ```
      - By default, if the Gradle daemon's heap size is at least 1.5 GB, Jack now runs in the same process as Gradle. To adjust the daemon heap size, add the following to your `gradle.properties` file:  

        ```
        # This sets the daemon heap size to 1.5GB.
        org.gradle.jvmargs=-Xmx1536M
        ```

### 2.1.0 (April 2016)


**2.1.3 (August 2016)**

This update requires Gradle 2.14.1 and higher. Gradle 2.14.1 includes
performance improvements, new features, and an important [security fix](https://docs.gradle.org/2.14/release-notes#local-privilege-escalation-when-using-the-daemon). For more details, see the
[Gradle release notes](https://docs.gradle.org/2.14.1/release-notes).

Dependencies:
:
    - Gradle 2.10 or higher.
    - [Build Tools 23.0.2](https://developer.android.com/tools/revisions/build-tools) or higher.

New:
:
    - Added support for the N Developer Preview, JDK 8, and [Java 8 language features](https://developer.android.com/preview/j8-jack) using the Jack toolchain. To find out more, read the [N Preview guide](https://developer.android.com/about/versions/nougat).


      **Note:** [Instant
      Run](https://developer.android.com/tools/building/building-studio#instant-run) does not currently work with Jack and will be disabled while
      using the new toolchain. You only need to use Jack if you are developing
      for the N Preview and want to use the supported Java 8 language features.
    - Added default support for incremental Java compilation to reduce compilation time during development. It does this by only recompiling portions of the source that have changed or need to be recompiled. To disable this feature, add the following code to your module-level `build.gradle` file:  

      ### Groovy

      ```groovy
      android {
        ...
        compileOptions {
          incremental false
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        compileOptions {
          incremental = false
        }
      }
      ```
    -
      Added support for dexing-in-process which performs dexing within the build
      process rather than in a separate, external VM processes. This not only makes
      incremental builds faster, but also speeds up full builds. The feature is
      enabled by default for projects that have set the Gradle daemon's maximum heap
      size to at least 2048 MB. You can do this by including the following in your
      project's `gradle.properties` file:

      \`\`\`none org.gradle.jvmargs = -Xmx2048m \`\`\`


      If you have defined a value for [`javaMaxHeapSize`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.DexOptions.html#com.android.build.gradle.internal.dsl.DexOptions:javaMaxHeapSize) in your module-level `build.gradle`
      file, you need to set `org.gradle.jvmargs` to the value of
      `javaMaxHeapSize` + 1024 MB. For example, if you have set
      `javaMaxHeapSize` to "2048m", you need to add the following to your
      project's `gradle.properties` file:
      \`\`\`none org.gradle.jvmargs = -Xmx3072m \`\`\`


      To disable dexing-in-process, add the following code to your module-level `build.gradle` file:  

      ### Groovy

      ```groovy
      android {
        ...
        dexOptions {
            dexInProcess false
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        dexOptions {
            dexInProcess = false
        }
      }
      ```


<br />

### 2.0.0 (April 2016)

Dependencies:
:
    - Gradle 2.10 or higher.
    - [Build Tools 21.1.1](https://developer.android.com/tools/revisions/build-tools) or higher.

New:
:
    - Enables [Instant Run](https://developer.android.com/tools/building/building-studio#instant-run) by supporting bytecode injection, and pushing code and resource updates to a running app on the emulator or a physical device.
    - Added support for incremental builds, even when the app isn't running. Full build times are improved by pushing incremental changes through the [Android Debug Bridge](https://developer.android.com/tools/help/adb) to the connected device.
    - Added [`maxProcessCount`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.DexOptions.html#com.android.build.gradle.internal.dsl.DexOptions:maxProcessCount) to control how many worker dex processes can be spawned concurrently. The following code, in the module-level `build.gradle` file, sets the maximum number of concurrent processes to 4:  

      ### Groovy

      ```groovy
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        dexOptions {
          maxProcessCount = 4 // this is the default value
        }
      }
      ```  

            </li>

            <li>Added an experimental code shrinker to support pre-dexing and reduce re-dexing
            of dependencies, which are not supported with Proguard. This improves the build
            speed of your debug build variant. Because the experimental shrinker does not
            support optimization and obfuscation, you should enable Proguard for your
            release builds. To enable the experimental shrinker for your debug builds, add
            the following to your module-level <code>build.gradle</code> file:

      ### Groovy

      ```groovy
      android {
        ...
        buildTypes {
          debug {
            minifyEnabled true
            useProguard false
          }
          release {
            minifyEnabled true
            useProguard true // this is a default setting
          }
        }
      }
      ```

      ### Kotlin

      ```kotlin
      android {
        ...
        buildTypes {
          getByName("debug") {
            minifyEnabled = true
            useProguard = false
          }
          getByName("release") {
            minifyEnabled = true
            useProguard = true // this is a default setting
          }
        }
      }
      ```  

            </li>

            <li>Added logging support and improved performance for the resource shrinker.
            The resource shrinker now logs all of its operations into a <code>resources.txt</code>
            file located in the same folder as the Proguard log files.
            </li>
          </ul>

      <br />

Changed behavior:
:
    - When `minSdkVersion` is set to 18 or higher, APK signing uses SHA256.  

          <li>DSA and ECDSA keys can now sign APK packages.

            <p class="note">
              <strong>Note:</strong> The <a href=
              "/training/articles/keystore.html">Android keystore</a> provider no
              longer supports <a href=
              "/about/versions/marshmallow/android-6.0-changes.html#behavior-keystore">
              DSA keys on Android 6.0</a> (API level 23) and higher.
            </p>

          </li>
        </ul>

Fixed issues:
:
    - Fixed an issue that caused duplicate AAR dependencies in both the test and main build configurations.

<br />

### Android plugin for Gradle, revision 1.5.0 (November 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Integrated the Data Binding plugin into the Android plugin for Gradle. To enable it, add the following code to each per-project `build.gradle` file that uses the plugin:  

    ```groovy
    android {
        dataBinding {
            enabled = true
        }
    }
            
    ```  

    ```kotlin
    android {
        dataBinding {
            enabled = true
        }
    }
            
    ```
    - Added a new [Transform API](https://google.github.io/android-gradle-dsl/javadoc/1.5/) to allow third-party plugins to manipulate compiled `.class` files before they're converted to `.dex` files. The Transform API simplifies injecting custom class manipulations while offering more flexibility regarding what you can manipulate. To insert a transform into a build, create a new class implementing one of the `Transform` interfaces, and register it with `android.registerTransform(theTransform)` or `android.registerTransform(theTransform, dependencies)`. There's no need to wire tasks together. Note the following about the Transform API:
      - A transform can apply to one or more of the following: the current project, subprojects, and external libraries.
      - A transform must be registered globally, which applies them to all variants.
      - Internal code processing, through the Java Code Coverage Library (JaCoCo), ProGuard, and MultiDex, now uses the Transform API. However, the Java Android Compiler Kit (Jack) doesn't use this API: only the `javac/dx` code path does.
      - Gradle executes the transforms in this order: JaCoCo, third-party plugins, ProGuard. The execution order for third-party plugins matches the order in which the transforms are added by the third party plugins; third-party plugin developers can't control the execution order of the transforms through an API.
    - Deprecated the `dex` getter from the `ApplicationVariant` class. You can't access the `Dex` task through the variant API anymore because it's now accomplished through a transform. There's currently no replacement for controlling the dex process.
    - Fixed incremental support for assets.
    - Improved MultiDex support by making it available for test projects, and tests now automatically have the `com.android.support:multidex-instrumentation` dependency.
    - Added the ability to properly fail a Gradle build and report the underlying error cause when the Gradle build invokes asynchronous tasks and there's a failure in the worker process.
    - Added support for configuring a specific Application Binary Interface (ABI) in variants that contain multiple ABIs.
    - Added support for a comma-separated list of device serial numbers for the `ANDROID_SERIAL` environment variable when installing or running tests.
    - Fixed an installation failure on devices running Android 5.0 (API level 20) and higher when the APK name contains a space.
    - Fixed various issues related to the Android Asset Packaging Tool (AAPT) error output.
    - Added JaCoCo incremental instrumentation support for faster incremental builds. The Android plugin for Gradle now invokes the JaCoCo instrumenter directly. To force a newer version of the JaCoCo instrumenter, you need to add it as a build script dependency.
    - Fixed JaCoCo support so it ignores files that aren't classes.
    - Added vector drawable support for generating PNGs at build time for backward-compatibility. Android plugin for Gradle generates PNGs for every vector drawable found in a resource directory that doesn't specify an API version or specifies an `android:minSdkVersion` attribute of 20 or lower in the `<uses-sdk>` element in the app manifest. You can set PNG densities by using the `generatedDensities` property in the `defaultConfig` or `productFlavor` sections of a `build.gradle` file.
    - Added sharing of the mockable `android.jar`, which the plugin generates only once and uses for unit testing. Multiple modules, such as `app` and `lib`, now share it. Delete `$rootDir/build` to regenerate it.
    - Changed the processing of Java resources to occur before the obfuscation tasks instead of during the packaging of the APK. This change allows the obfuscation tasks to have a chance to adapt the Java resources following packages obfuscation.
    - Fixed an issue with using Java Native Interface (JNI) code in the experimental library plugin.
    - Added the ability to set the platform version separately from the `android:compileSdkVersion` attribute in the experimental library plugin.

### Android plugin for Gradle, revision 1.3.1 (August 2015)

**Dependencies:**

- Gradle 2.2.1 or higher.
- Build Tools 21.1.1 or higher.

**General Notes:**

- Fixed the [ZipAlign](https://developer.android.com/tools/help/zipalign) task to properly consume the output of the previous task when using a customized filename.
- Fixed [Renderscript](https://developer.android.com/guide/topics/renderscript/compute) packaging with the [NDK](https://developer.android.com/tools/sdk/ndk).
- Maintained support for the `createDebugCoverageReport` build task.
- Fixed support for customized use of the `archiveBaseName` property in the `build.gradle` build file.
- Fixed the `Invalid ResourceType` [lint](https://developer.android.com/tools/help/lint) warning caused by parameter method annotation lookup when running [lint](https://developer.android.com/tools/help/lint) outside of Android Studio.  

### Android plugin for Gradle, revision 1.3.0 (July 2015)

**Dependencies:**

- Gradle 2.2.1 or higher.
- Build Tools 21.1.1 or higher.

**General Notes:**

- Added support for the `com.android.build.threadPoolSize`
  property to control the `Android` task thread pool size from
  the `gradle.properties` file or the command line. The
  following example sets this property to 4.

              
              -Pcom.android.build.threadPoolSize=4
              
            
- Set the default build behavior to exclude `LICENSE` and `LICENSE.txt` files from APKs. To include these files in an APK, remove these files from the `packagingOptions.excludes` property in the `build.gradle` file. For example:  

  ```groovy
  android {
        packagingOptions.excludes = []
      }
        
  ```  

  ```kotlin
  android {
        packagingOptions.excludes.clear()
      }
      
  ```
- Added the `sourceSets` task to inspect the set of all available source sets.
- Enhanced unit test support to recognize multi-flavor and [build variant](https://developer.android.com/tools/building/configuring-gradle#workBuildVariants) source folders. For example, to test an app with multi-flavors `flavor1` and `flavorA` with the `Debug` build type, the test source sets are:
  - test
  - testFlavor1
  - testFlavorA
  - testFlavor1FlavorA
  - testFlavor1FlavorADebug

  Android tests already recognized multi-flavor source folders.
- Improved unit test support to:
  - Run `javac` on main and test sources, even if the `useJack` property is set to `true` in your build file.
  - Correctly recognize dependencies for each build type.
- Added support for specifying instrumentation test-runner arguments from the command line. For example:  

  ```
  ./gradlew connectedCheck \
     -Pandroid.testInstrumentationRunnerArguments.size=medium \
     -Pandroid.testInstrumentationRunnerArguments.class=TestA,TestB
          
  ```
- Added support for arbitrary additional Android Asset Packaging Tool (AAPT) parameters
  in the `build.gradle` file. For example:

  ```groovy
  android {
      aaptOptions {
        additionalParameters "--custom_option", "value"
      }
  }
        
  ```  

  ```kotlin
  android {
      aaptOptions {
        additionalParameters += listOf("--custom_option", "value")
      }
  }
        
  ```
- Added support for a [test APK module](https://developer.android.com/tools/studio/studio-features#test-module) as a separate test module, using the `targetProjectPath` and `targetVariant` properties to set the APK path and target variant.

  **Note:** A test APK module does not support product
  flavors and can only target a single variant. Also, Jacoco is not supported yet.
- Added resource name validation before merging resources.
- When building an AAR (Android ARchive) package for library modules, do not provide an automatic `@{applicationId}` placeholder in the [manifest merger](https://developer.android.com/tools/building/manifest-merge) settings. Instead, use a different placeholder, such as `@{libApplicationId}` and provide a value for it if you want to include application Ids in the archive library.  

### Android plugin for Gradle, revision 1.2.0 (April 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Enhanced support for running unit tests with Gradle.
      - Added support to include Java-style resources in the classpath when running unit tests directly from Gradle.
      - Added unit test dependency support for Android Archive (AAR) artifacts.
      - Added support for the `unitTestVariants` property so unit test variants can be manipulated using the `build.gradle` file.
      - Added the `unitTest.all` code block under `testOptions` to configure customized tasks for unit test. The following sample code shows how to add unit test configuration settings using this new option:  

        ```groovy
        android {
          testOptions {
            unitTest.all {
              jvmArgs '-XX:MaxPermSize=256m' // Or any other gradle option.
            }
          }
        }
        ```  

        ```kotlin
        android {
          testOptions {
            unitTest.all {
              jvmArgs += listOf("-XX:MaxPermSize=256m") // Or any other gradle option.
            }
          }
        }
                    
        ```
      - Fixed the handling of enums and public instance fields in the packaging of the `mockable-android.jar` file.
      - Fixed library project task dependencies so test classes recompile after changes.
    - Added the `testProguardFile` property to apply [ProGuard](https://developer.android.com/tools/help/proguard) files when minifying a test APK.
    - Added the `timeOut` property to the `adbOptions` code block for setting the maximum recording time for [Android Debug Bridge](https://developer.android.com/tools/help/adb) screen recording.
    - Added support for 280 dpi resources.
    - Improved performance during project evaluation.

### Android plugin for Gradle, revision 1.1.3 (March 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Fixed issue with duplicated dependencies on a test app that triggered a ProGuard failure.
    - Fixed Comparator implementation which did not comply with the JDK Comparator contract and generated a JDK 7 error.

### Android plugin for Gradle, revision 1.1.2 (February 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Normalized path when creating a mockable JAR for unit testing.
    - Fixed the `archivesBaseName` setting in the `build.gradle` file.
    - Fixed the unresolved placeholder failure in manifest merger when building a library test application.

### Android plugin for Gradle, revision 1.1.1 (February 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Modified build variants so only variants that package a [Wear](https://developer.android.com/training/wearables/apps) app trigger Wear-specific build tasks.
    - Changed dependency related issues to fail at build time rather than at debug time. This behavior allows you to run diagnostic tasks (such as 'dependencies') to help resolve the conflict.
    - Fixed the `android.getBootClasspath()` method to return a value.

### Android plugin for Gradle, revision 1.1.0 (February 2015)

Dependencies:
:
    - Gradle 2.2.1 or higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Added new unit test support
      - Enabled [unit
        tests](https://developer.android.com/training/activity-testing/activity-unit-testing) to run on the local JVM against a special version of the `android.jar` file that is compatible with popular mocking frameworks, for example Mockito.
      - Added new test tasks `testDebug`, `testRelease`, and `testMyFlavorDebug` when using product flavors.
      - Added new source folders recognized as unit tests: `src/test/java/`, `src/testDebug/java/`, `src/testMyFlavor/java/`.
      - Added new configurations in the `build.gradle` file for declaring test-only dependencies, for example, `testCompile 'junit:junit:4.11'`, `testMyFlavorCompile 'some:library:1.0'`.

        **Note:** Test-only dependencies
        are not currently compatible with Jack (Java Android Compiler
        Kit).
      - Added the `android.testOptions.unitTests.returnDefaultValues` option to control the behaviour of the mockable android.jar.
    - Replaced `Test` in test task names with `AndroidTest`. For example, the `assembleDebugTest` task is now `assembleDebugAndroidTest` task. Unit test tasks still have `UnitTest` in the task name, for example `assembleDebugUnitTest`.
    - Modified [ProGuard](https://developer.android.com/tools/help/proguard) configuration files to no longer apply to the test APK. If minification is enabled, ProGuard processes the test APK and applies only the mapping file that is generated when minifying the main APK.
    - Updated dependency management
      - Fixed issues using `provided` and `package` scopes.

        **Note:** These scopes are
        incompatible with AAR (Android ARchive) packages and will
        cause a build with AAR packages to fail.
      - Modified dependency resolution to compare the dependencies of an app under test and the test app. If an artifact with the same version is found for both apps, it's not included with the test app and is packaged only with the app under test. If an artifact with a different version is found for both apps, the build fails.
    - Added support for `anyDpi` [resource
      qualifier](https://developer.android.com/guide/topics/resources/providing-resources) in resource merger.
    - Improved evaluation and IDE sync speeds for projects with a large number of Android [modules](https://developer.android.com/studio/projects).

### Android plugin for Gradle, revision 1.0.1 (January 2015)

Dependencies:
:
    - Gradle 2.2.1 up to 2.3.x.

      **Note:** This version of the Android
      plugin for Gradle is not compatible with Gradle 2.4 and
      higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Fixed issue with Gradle build failure when accessing the `extractReleaseAnnotations` module. ([Issue 81638](http://b.android.com/81638)).
    - Fixed issue with `Disable` passing the `--no-optimize` setting to the Dalvik Executable (dex) bytecode. ([Issue
      82662](http://b.android.com/82662)).
    - Fixed manifest merger issues when importing libraries with a `targetSdkVersion` less than 16.
    - Fixed density ordering issue when using Android Studio with JDK 8.

### Android plugin for Gradle, revision 1.0.0 (December 2014)

Dependencies:
:
    - Gradle 2.2.1 up to 2.3.x.


      **Note:** This version of the Android plugin for
      Gradle is not compatible with Gradle 2.4 and higher.
    - Build Tools 21.1.1 or higher.

General Notes:
:
    - Initial plugin release.