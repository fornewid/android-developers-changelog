---
title: https://developer.android.com/studio/releases/past-releases/as-3-4-0-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-3-4-0-release-notes
source: md.txt
---

<br />

# Android Studio 3.4 (April 2019)

<br />

<br />

Android Studio 3.4 is a major release that includes a variety of new features
and improvements.

<br />

<br />

<br />

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

## IntelliJ IDEA 2018.3.4

<br />

<br />

The core Android Studio IDE has been updated with improvements from IntelliJ
IDEA through the
[2018.3.4 release](https://blog.jetbrains.com/idea/2019/01/intellij-idea-2018-3-4-is-released/).

<br />

<br />

## Android Gradle plugin 3.4.0 updates

<br />

<br />

For information on what's new in Android Gradle plugin 3.4.0, see its
[release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />

<br />

## New Project Structure Dialog

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

### Variables

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

### Modules

<br />

<br />

Configure properties that are applied to all build variants in an existing
module or add new modules to your project from the **Modules** section. For
example, this is where you can configure `defaultConfig` properties or manage
signing configurations.

<br />

<br />

### Dependencies

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

### Build Variants

<br />

<br />

In this section of the PSD, create and configure build variants and product
flavors for each module in your project. You can add manifest placeholders, add
ProGuard files, and assign signing keys, and more.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_build_variants.png)

<br />

### Suggestions

<br />

<br />

See suggested updates for project dependencies and build variables in the
**Suggestions** section, as shown below.

<br />

![](https://developer.android.com/static/studio/images/releases/psd_suggestions.png)

<br />

## New Resource Manager

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

## Checking build IDs when profiling and debugging APKs

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

## R8 enabled by default

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

## Navigation Editor now supports all argument types

<br />

<br />

All argument types supported by the Navigation component are now supported in
the Navigation Editor. For more information on supported types, see
[Pass data between destinations](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data).

<br />

<br />

## Layout Editor improvements {:#layout-editor}

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

## New intention action to quickly import dependencies

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