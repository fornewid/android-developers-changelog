---
title: https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes
source: md.txt
---

<br />

# Android Studio 3.5 (August 2019)

<br />

<br />

Android Studio 3.5 is a major release and a result of Project Marble.
Beginning with the release of
[Android Studio 3.3](https://android-developers.googleblog.com/2019/01/android-studio-33.html), the Project Marble initiative has spanned multiple releases that focus on
improving three main areas of the IDE:
[system health](https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes#3-5-system-health),
[feature polish](https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes#3-5-feature-polish), and fixing bugs.

<br />

<br />

For information about these and other Project Marble updates, read the
[Android Developers blog post](https://android-developers.googleblog.com/2019/08/android-studio-35-project-marble-goes.html) or the sections below.

<br />

<br />

We also want to thank all of our
[community contributors](https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes#3-5-community-contributors) who have
helped with this release.

<br />

<br />

<br />

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

## Project Marble: System health

<br />

<br />

This section describes the changes in Android Studio 3.5 that are focused on
improving system health.

<br />

<br />

### Recommended memory settings

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

### Memory usage report

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

### Windows: Antivirus file I/O optimization

<br />

<br />

Android Studio now automatically checks whether certain project directories are
excluded from real-time antivirus scanning. When adjustments can be made to
improve build performance, Android Studio notifies you and provides instructions
on how to optimize your antivirus configuration. To learn more, see
[Minimize the impact of antivirus software on build speed](https://developer.android.com/studio/intro/studio-config#antivirus-impact).

<br />

<br />

## Project Marble: Feature polish

<br />

<br />

This section describes the changes in Android Studio 3.5 that are focused on
improving existing features.

<br />

<br />

### Apply Changes

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

### App deployment flow

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

### Improved Gradle sync and cache detection

<br />

<br />

The IDE now better detects when Gradle periodically clears your build cache when
reducing its hard disk consumption. In previous versions, this state caused the
IDE to report missing dependencies and Gradle sync to fail. Now, the IDE simply
downloads dependencies as needed to ensure that Gradle sync completes
successfully.

<br />

<br />

### Improved build error output

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

### Project Upgrades

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

### Layout Editor

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

### Data Binding

In addition to adding [incremental annotation processing support](https://developer.android.com/studio/releases/past-releases/as-3-5-0-release-notes#incremental_ap)
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

### Improved support for C/C++ projects

<br />

<br />

Android Studio 3.5 includes several changes that improve support for C/C++
projects.

<br />

<br />

#### Build Variants panel improvements for single variant sync

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

#### Side-by-side versions of the NDK

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

## ChromeOS Support

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

## Conditional delivery for feature modules

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

## IntelliJ IDEA 2019.1

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

## Android Gradle plugin 3.5.0 updates

<br />

<br />

For information on what's new in Android Gradle plugin 3.5.0, such as improved
support for incremental annotation processing and cacheable unit tests, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

## Community contributors

Thank you to all of our community contributors who have helped us discover bugs
and other ways to improve Android Studio 3.5. In particular, we'd like to thank
the following people who reported P0 and P1 bugs:

<br />

<br />

|---|---|---|
| - [Aaron He](https://github.com/aaronhe42) - [Andreas Dybdahl](https://github.com/anddybdahl) - [Andrei Vădan](https://github.com/Vampirelu) - [Andrew Hughes](https://github.com/ashughes) - [Andrey Mischenko](https://github.com/gildor) - Andrii Seredenko - [Benoît 'BoD' Lubek](https://github.com/BoD) - [Berkeli Alashov](https://github.com/alashow) - [Bram Stolk](https://github.com/stolk) - [Charles Anderson](https://github.com/gtcompscientist) - Curtis Kroetsch - [David Burström](https://stackoverflow.com/users/643007/david-burstr%c3%b6m) - [DeweyReed](https://github.com/DeweyReed) - Dmitriy Dolovov - [Emin Kokalari](https://stackoverflow.com/users/3636806/eak-team) - [Evan Tatarka](https://github.com/evant) - [Evgeny Brazgin](https://github.com/xapienz) | - [George Kropotkin](https://github.com/gmk57) - [Ido Feins](https://github.com/ifeins) - Jakub Banaszewski - [Jean-Michel Fayard](https://github.com/jmfayard) - [John Rodriguez](https://github.com/jrodbx) - [Kamil Dudek](https://github.com/dudududi) - [Kenji Abe](https://github.com/STAR-ZERO) - [Liran Barsisa](https://stackoverflow.com/users/878126/android-developer) - [Louis CAD](https://github.com/LouisCAD) - Luke Fielke - [Lóránt Pintér](https://github.com/lptr) - Marcin Dawid - Mario O - [Mauricio Vignale](https://github.com/mvignale1987) - [Michael Bailey](https://stackoverflow.com/users/1686989/yogurtearl) - Miguel Angel Rossi Sanahuja - [Niklas Baudy](https://github.com/vanniktech) | - [Noah Andrews](https://github.com/NoahAndrews) - [Oleksandr Zakrevskyi](https://github.com/sanchopanchos) - Peter Vegh - [Rishabh harit](https://github.com/rishabh876) - [Roar Grønmo](https://github.com/RoarGronmo) - [Said Tahsin Dane](https://github.com/tasomaniac/) - [Shayan Sabahi](https://stackoverflow.com/users/6600637/shynline) - [Slawomir Czerwinski](https://github.com/sczerwinski) - Stephen Yu - [Steven Schoen](https://github.com/dsteve595) - [Tolriq](https://github.com/tolriq) - [Tony Robalik](https://github.com/autonomousapps) - [Uli Bubenheimer](https://github.com/bubenheimer/) - Vixb Xue - [Yi Cheng](https://github.com/wisechengyi) |

<br />