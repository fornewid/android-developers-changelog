---
title: https://developer.android.com/build/releases/agp-3-3-0-release-notes
url: https://developer.android.com/build/releases/agp-3-3-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 3.3.0 (January 2019)

This version of the Android plugin requires the following:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 4.10.1 | 4.10.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). When using Gradle 5.0 and higher, the default Gradle daemon memory heap size decreases from 1 GB to 512 MB. This might result in a build performance regression. To override this default setting, specify the Gradle daemon heap size in your project's gradle.properties file. |
| SDK Build Tools | 28.0.3 | 28.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**3.3.3 (July 2020)**


This minor update supports compatibility with new default settings and
features for
[package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).


See the [4.0.1 release notes](https://developer.android.com/build/releases/agp-3-3-0-release-notes#4.0.1) for details.

**3.3.2 (March 2019)**


This minor update supports Android Studio 3.3.2 and includes various bug
fixes and performance improvements.
To see a list of noteable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2019/03/android-studio-332-available.html).

**3.3.1 (February 2019)**

This minor update supports Android Studio 3.3.1 and includes various bug
fixes and performance improvements.

<br />

<br />

## New features

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

## Behavior changes

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

## Bug Fixes

- Android Gradle plugin 3.3.0 fixes the following issues:

  - The build process calling `android.support.v8.renderscript.RenderScript` instead of the AndroidX version, despite Jetifier being enabled
  - Clashes due to `androidx-rs.jar` including statically bundled `annotation.AnyRes`
  - When using RenderScript, you no longer have to manually set the Build Tools version in your `build.gradle` files

<br />