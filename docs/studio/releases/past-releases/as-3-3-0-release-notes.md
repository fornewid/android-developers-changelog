---
title: https://developer.android.com/studio/releases/past-releases/as-3-3-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-3-3-0-release-notes
source: md.txt
---

<br />

# Android Studio 3.3 (January 2019)

<br />

<br />

Android Studio 3.3 is a major release that includes a variety of new features
and improvements.

<br />

<br />

<br />

<br />

**3.3.2 (March 2019)**


This minor update includes various bug fixes and performance improvements.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/03/android-studio-332-available.html).

**3.3.1 (February 2019)**


This minor update includes various bug fixes and performance improvements.

<br />

<br />

## IntelliJ IDEA 2018.2.2

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the [2018.2.2 release](http://blog.jetbrains.com/idea/2018/08/intellij-idea-2018-2-2-is-released).

<br />

<br />

## Android Gradle plugin updates

<br />

<br />

For information on what's new in the Android Gradle plugin, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

## Navigation Editor

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

## Delete unused Android Studio directories

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

## Lint improvements

<br />

<br />

Lint, when invoked from Gradle, is significantly faster---larger projects can
expect lint to run up to four times faster.

<br />

<br />

## Create New Project wizard

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

## Profiler updates

<br />

<br />

Android Studio 3.3 includes updates to several of the individual profilers.

<br />

<br />

### Improved performance

<br />

<br />

Based on user feedback, rendering performance while using the profilers has been
greatly improved. Please continue to
[provide feedback](https://issuetracker.google.com/issues/new?component=192722),
especially if you continue to see performance issues.

<br />

### Profiler memory allocation tracking options

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

### Inspect frame rendering data

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

### Fragments in the event timeline

<br />

<br />

The event timeline now shows when fragments are attached and detached.
Additionally, when you hover over a fragment, a tooltip shows you the fragment
status.

<br />

![](https://developer.android.com/static/studio/images/releases/fragments-activity-bar_2x.png)

<br />

### View formatted text for connection payloads in the Network profiler

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

## Automatic downloading of SDK components

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

## Support for Clang-Tidy

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

## Removal of options for C++ customization

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

## CMake version 3.10.2

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

## New "+" syntax to specify minimum CMake versions

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

## Android App Bundles now support Instant Apps

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

## Single-variant project sync

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

## Provide quick feedback

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