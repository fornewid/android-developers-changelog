---
title: https://developer.android.com/build/releases/agp-4-0-0-release-notes
url: https://developer.android.com/build/releases/agp-4-0-0-release-notes
source: md.txt
---

<br />

# Android Gradle Plugin 4.0.0 (April 2020)

This version of the Android plugin requires the following:

- [Gradle 6.1.1](https://docs.gradle.org/6.1.1/release-notes.html).
  To learn more, read the section about [updating Gradle](https://developer.android.com/build/releases/agp-4-0-0-release-notes#updating-gradle).

- [SDK Build Tools 29.0.2](https://developer.android.com/studio/releases/build-tools#notes) or higher.

**4.0.1 (July 2020)**


This minor update supports compatibility with new default settings and
features for [package
visibility in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).

In previous versions of Android, it was possible to view a list of all
apps installed on a device. Starting with Android 11 (API level 30), by
default apps have access to only a filtered list of installed packages.
To see a broader list of apps on the system, you now need to
[add a
`<queries>` element](https://developer.android.com/training/basics/intents/package-visibility#package-name) in your app or library's
Android manifest.

Android Gradle plugin 4.1+ is already compatible with the new
`<queries>` declaration; however, older versions are not
compatible. If you add the `<queries>` element or if you
start relying on a library or SDK that supports targeting Android 11, you
may encounter manifest merging errors when building your app.


To address this issue, we're releasing a set of patches for AGP 3.3 and
higher. If you're using an older version of AGP,
[upgrade](https://developer.android.com/studio/releases/gradle-plugin?buildsystem=ndk-build#updating-plugin)
to one of the following versions:

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 6.1.1 | 6.1.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 29.0.2 | 29.0.2 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |


For more information on this new feature, see
[Package visibility
in Android 11](https://developer.android.com/about/versions/11/privacy/package-visibility).

<br />

<br />

## New features

This version of the Android Gradle plugin includes the following new features.

### Support for Android Studio Build Analyzer

The **Build Analyzer** window helps you understand and diagnose issues with your
build process, such as disabled optimizations and improperly configured tasks.
This feature is available when you use Android Studio 4.0 and higher with
Android Gradle plugin `4.0.0` and higher. You can open the **Build Analyzer**
window from Android Studio as follows:

1. If you haven't already done so, build your app by selecting **Build \> Make
   Project** from the menu bar.
2. Select **View \> Tool Windows \> Build** from the menu bar.
3. In the **Build** window, open the **Build Analyzer** window in one of the following ways:
   - After Android Studio finishes building your project, click the **Build
     Analyzer** tab.
   - After Android Studio finishes building your project, click the link on the right side of the **Build Output** window.

![](https://developer.android.com/static/studio/images/build/build-analyzer/plugins-breakdown.png)

The **Build Analyzer** window organizes possible build issues in a tree on the
left. You can inspect and click on each issue to investigate its details in the
panel on the right. When Android Studio analyzes your build, it computes the set
of tasks that determined the build's duration and provides a visualization to
help you understand the impact of each of these tasks. You can also get details
on warnings by expanding the **Warnings** node.

To learn more, read [identify build speed regressions](https://developer.android.com/studio/build/build-analyzer).

### Java 8 library desugaring in D8 and R8

The Android Gradle plugin now includes support for using a number of Java 8
language APIs without requiring a minimum API level for your app.

Through a process called *desugaring* , the DEX compiler, D8, in Android Studio
3.0 and higher already provided substantial support for Java 8 language features
(such as lambda expressions, default interface methods, try with resources, and
more). In Android Studio 4.0, the desugaring engine has been extended to be able
to desugar Java language APIs. This means that you can now include standard
language APIs that were available only in recent Android releases (such as
`java.util.streams`) in apps that support older versions of Android.

The following set of APIs is supported in this release:

- Sequential streams (`java.util.stream`)
- A subset of `java.time`
- `java.util.function`
- Recent additions to `java.util.{Map,Collection,Comparator}`
- Optionals (`java.util.Optional`, `java.util.OptionalInt` and `java.util.OptionalDouble`) and some other new classes useful with the above APIs
- Some additions to `java.util.concurrent.atomic` (new methods on `AtomicInteger`, `AtomicLong` and `AtomicReference`)
- `ConcurrentHashMap` (with bug fixes for Android 5.0)

To support these language APIs, D8 compiles a separate library DEX file that
contains an implementation of the missing APIs and includes it in your app. The
desugaring process rewrites your app's code to instead use this library at
runtime.

To enable support for these language APIs, include the following in your
**app module** 's `build.gradle` file:

    android {
      defaultConfig {
        // Required when setting minSdkVersion to 20 or lower
        multiDexEnabled true
      }

    <br />





    compileOptions {
        // Flag to enable support for the new language APIs
        coreLibraryDesugaringEnabled true
        // Sets Java compatibility to Java 8
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
      }
    }


    `dependencies {
      coreLibraryDesugaring 'com.android.tools:desugar_jdk_libs:1.0.4'
    }`

    android {
      defaultConfig {
        // Required when setting minSdkVersion to 20 or lower
        multiDexEnabled = true
      }

    <br />





    compileOptions {
        // Flag to enable support for the new language APIs
        isCoreLibraryDesugaringEnabled = true
        // Sets Java compatibility to Java 8
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
      }
    }


    `dependencies {
      coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:1.0.4")
    }`

Note that you may also need to include the above code snippet in a
**library module** 's `build.gradle` file if

- The library module's instrumented tests use these language APIs (either
  directly or through the library module or its dependencies). This is so that
  the missing APIs are provided for your instrumented test APK.

- You want to run lint on the library module in isolation. This is to help
  lint recognize valid usages of the language APIs and avoid reporting false
  warnings.

### New options to enable or disable build features

Android Gradle plugin 4.0.0 introduces a new way to control which build features
you want to enable and disable, such as View Binding and Data Binding. When new features are added, they will be disabled, by default. You can
then use the `buildFeatures` block to enable only the features you want, and it
helps you optimize the build performance for your project. You can set the
options for each module in the module-level `build.gradle` file, as follows:

    android {
      // The default value for each feature is shown below. You can change the value to
      // override the default behavior.
      buildFeatures {
        // Determines whether to generate a BuildConfig class.
        buildConfig = true
        // Determines whether to support View Binding.
        // Note that the viewBinding.enabled property is now deprecated.
        viewBinding = false
        // Determines whether to support Data Binding.
        // Note that the dataBinding.enabled property is now deprecated.
        dataBinding = false
        // Determines whether to generate binder classes for your AIDL files.
        aidl = true
        // Determines whether to support RenderScript.
        renderScript = true
        // Determines whether to support injecting custom variables into the module's R class.
        resValues = true
        // Determines whether to support shader AOT compilation.
        shaders = true
      }
    }

    android {
      // The default value for each feature is shown below. You can change the value to
      // override the default behavior.
      buildFeatures {
        // Determines whether to generate a BuildConfig class.
        buildConfig = true
        // Determines whether to support View Binding.
        // Note that the viewBinding.enabled property is now deprecated.
        viewBinding = false
        // Determines whether to support Data Binding.
        // Note that the dataBinding.enabled property is now deprecated.
        dataBinding = false
        // Determines whether to generate binder classes for your AIDL files.
        aidl = true
        // Determines whether to support RenderScript.
        renderScript = true
        // Determines whether to support injecting custom variables into the module's R class.
        resValues = true
        // Determines whether to support shader AOT compilation.
        shaders = true
      }
    }

You can also specify the default setting for these features across all modules
in a project by including one or more of the following in your project's
`gradle.properties` file, as shown below. Keep in mind, you can still use the
`buildFeatures` block in the module-level `build.gradle` file to override these
project-wide default settings.

    android.defaults.buildfeatures.buildconfig=true
    android.defaults.buildfeatures.aidl=true
    android.defaults.buildfeatures.renderscript=true
    android.defaults.buildfeatures.resvalues=true
    android.defaults.buildfeatures.shaders=true

### Feature-on-feature dependencies

In previous versions of the Android Gradle plugin, all feature modules
could depend only on the app's base module. When using Android Gradle plugin
4.0.0, you can now include a feature module that depends on another feature
module. That is, a `:video` feature can depend on the
`:camera` feature, which depends on the base module, as shown
in the figure below.
![Feature on feature dependencies](https://developer.android.com/static/images/app-bundle/feature-on-feature.png)

Feature module `:video` depends on feature
`:camera`, which depends on the base `:app` module.

This means that when your app requests to download a feature module, the
app also downloads other feature modules it depends on. After you
[create
feature modules](https://developer.android.com/studio/projects/dynamic-delivery/on-demand-delivery)
for your app, you can declare a feature-on-feature dependency in the module's
`build.gradle` file. For example, the `:video` module declares a dependency on
`:camera` as follows:

    // In the build.gradle file of the ':video' module.
    dependencies {
      // All feature modules must declare a dependency
      // on the base module.
      implementation project(':app')
      // Declares that this module also depends on the 'camera'
      // feature module.
      implementation project(':camera')
      ...
    }

    // In the build.gradle file of the ':video' module.
    dependencies {
        // All feature modules must declare a dependency
        // on the base module.
        implementation(project(":app"))
        // Declares that this module also depends on the 'camera'
        // feature module.
        implementation(project(":camera"))
        ...
    }

Additionally, you should enable the feature-on-feature dependency feature in
Android Studio (to support the feature when editing the Run configuration, for
example) by clicking **Help \> Edit Custom VM Options** from the menu bar and
including the following:

    -Drundebug.feature.on.feature=true

### Dependencies metadata

When building your app using Android Gradle plugin 4.0.0 and higher, the plugin
includes metadata that describes the dependencies that are compiled into your
app. When uploading your app, the Play Console inspects this metadata to provide
you with the following benefits:

- Get alerts for known issues with SDKs and dependencies your app uses
- Receive actionable feedback to resolve those issues

The data is compressed, encrypted by a Google Play signing key, and stored in
the signing block of your release app. However, you can inspect the metadata
yourself in the local intermediate build files in the following directory:
`<project>/<module>/build/outputs/sdk-dependencies/release/sdkDependency.txt`.

If you'd rather not share this information, you can opt-out by including the
following in your module's `build.gradle` file:

    android {
      dependenciesInfo {
          // Disables dependency metadata when building APKs.
          includeInApk = false
          // Disables dependency metadata when building Android App Bundles.
          includeInBundle = false
      }
    }

    android {
      dependenciesInfo {
          // Disables dependency metadata when building APKs.
          includeInApk = false
          // Disables dependency metadata when building Android App Bundles.
          includeInBundle = false
      }
    }

### Import native libraries from AAR dependencies

You can now import C/C++ libraries
from your app's AAR dependencies. When you follow the configuration steps
described below, Gradle automatically makes these native libraries available to
use with your external native build system, such as CMake. Note that Gradle only
makes these libraries available to your build; you must still configure your
build scripts to use them.

Libraries are exported using the [Prefab](https://google.github.io/prefab/)package format.

Each dependency can expose at most one Prefab package, which comprises one or
more modules. A Prefab module is a single library, which could be either a
shared, static, or header-only library.

Typically, the package name matches the Maven artifact name and the module name
matches the library name, but this is not always true. Because you need to know
the package and module name of the libraries, you might need to consult the
dependency's documentation to determine what those names are.

#### Configure your external native build system

To see the steps you need to follow, follow the steps below for the external native build system
you plan to use.

Each of your app's AAR dependencies that includes native code exposes an
`Android.mk` file that you need to import into your ndk-build project. You import
this file using the [`import--module`](https://developer.android.com/ndk/guides/android_mk#import-module) command, which searches the paths you
specify using the `import--add--path` property in your ndk-build project. For
example, if your application defines `libapp.so` and it uses curl, you
should include the following in your Android.mk file:

1. For CMake:

       add_library(app SHARED app.cpp)

       <br />




       `# Add these two lines.
       find_package(curl REQUIRED CONFIG)
       target_link_libraries(app curl::curl)`

2. For `ndk-build`:

       include $(CLEAR_VARS)
       LOCAL_MODULE := libapp
       LOCAL_SRC_FILES := app.cpp
       # Link libcurl from the curl AAR.
       LOCAL_SHARED_LIBRARIES := curl
       include $(BUILD_SHARED_LIBRARY)

       <br />





       # If you don't expect that your project will be built using versions of the NDK
       # older than r21, you can omit this block.
       ifneq ($(call ndk-major-at-least,21),true)
           $(call import-add-path,$(NDK_GRADLE_INJECTED_IMPORT_PATH))
       endif


       `# Import all modules that are included in the curl AAR.
       $(call import-module,prefab/curl)`

Native dependencies included in an AAR are exposed to your CMake project via the
[CMAKE_FIND_ROOT_PATH](https://cmake.org/cmake/help/latest/variable/CMAKE_FIND_ROOT_PATH.html){: .external} variable. This value will be set automatically by Gradle when
CMake is invoked, so if your build system modifies this variable, be sure to append
rather than assign to it.

Each dependency exposes a [config-file package](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#config-file-packages){: .external} to your CMake build, which you
import with the [`find_package`](https://cmake.org/cmake/help/latest/command/find_package.html){: .external} command. This command searches for config-file
packages that match the given package name and version and exposes the targets it
defines to be used in your build. For example, if your application defines
`libapp.so` and it uses curl, you should include the following in your
`CMakeLists.txt` file:


    add_library(app SHARED app.cpp)

    <br />




    `# Add these two lines.
    find_package(curl REQUIRED CONFIG)
    target_link_libraries(app curl::curl)`

You can now specify `#include "curl/curl.h"` in `app.cpp`. When you build your project, your external native build system automatically links `libapp.so`
against `libcurl.so` and packages `libcurl.so` in the APK or app bundle. For
additional information, refer to the [curl prefab sample](https://github.com/android/ndk-samples/tree/main/prefab/curl-ssl){:.external}.

<br />

<br />

## Behavior changes

When using this version of the plugin, you might encounter the following changes
in behavior.

### v1/v2 signing configuration updates

The behavior for app signing configurations in the `signingConfig` block has
changed to the following:

#### v1 signing

- If `v1SigningEnabled` is explicitly enabled, AGP performs v1 app signing.
- If `v1SigningEnabled` is explicitly disabled by the user, v1 app signing is not performed.
- If the user has not explicitly enabled v1 signing, it can be automatically disabled based on `minSdk` and `targetSdk`.

#### v2 signing

- If `v2SigningEnabled` is explicitly enabled, AGP performs v2 app signing.
- If `v2SigningEnabled` is explicitly disabled by the user, v2 app signing is not performed.
- If the user has not explicitly enabled v2 signing, it can be automatically disabled based on `targetSdk`.

These changes allow AGP to optimize builds by disabling the signing mechanism
based on whether the user has explicitly enabled these flags. Prior to this
release, it was possible for `v1Signing` to be disabled even when explicitly
enabled, which could be confusing.

### `feature` and `instantapp` Android Gradle plugins removed

Android Gradle plugin 3.6.0 deprecated the Feature plugin
(`com.android.feature`) and the Instant App plugin
(`com.android.instantapp`) in
favor of using the Dynamic Feature plugin
(`com.android.dynamic-feature`) to build and package your
instant apps using [Android App Bundles](https://developer.android.com/guide/app-bundle).

In Android Gradle plugin 4.0.0 and higher, these deprecated plugins are
fully removed. So, to use the latest Android Gradle plugin, you need to [migrate
your instant app to support Android App
Bundles](https://developer.android.com/topic/google-play-instant/feature-module-migration).
By migrating your instant apps, you can leverage the benefits of app
bundles and [simplify your app's modular
design](https://android-developers.googleblog.com/2019/04/google-play-instant-feature-plugin.html).

Note: To open projects that use the removed plugins in
Android Studio 4.0 and higher, the project must use Android Gradle plugin
3.6.0 or lower.

### Separate annotation processing feature removed

The ability to separate annotation processing into a dedicated task has been
removed. This option was used to maintain
incremental Java compilation when non-incremental annotation processors are
used in Java-only projects; it was enabled by setting
`android.enableSeparateAnnotationProcessing` to `true` in the
`gradle.properties` file, which no longer works.

Instead, you should migrate to [using incremental annotation
processors](https://developer.android.com/studio/build/optimize-your-build#annotation_processors) to improve
build performance.

### includeCompileClasspath is deprecated

The Android Gradle plugin no longer checks for or includes annotation processors
you declare on the compile classpath, and the
`annotationProcessorOptions.includeCompileClasspath` DSL property no longer has
any effect. If you include annotation processors on the compile classpath, you
might get the following error:

    Error: Annotation processors must be explicitly declared now.

To resolve this issue, you must include annotation processors in your
`build.gradle` files using the `annotationProcessor` dependency configuration.
To learn more, read [Add annotation
processors](https://developer.android.com/studio/build/dependencies#annotation_processor).

## Automatic packaging of prebuilt dependencies
used by CMake

Prior versions of the Android Gradle Plugin required that you explicitly
package any prebuilt libraries used by your CMake external native build by
using `jniLibs`. You may have libraries in the
`src/main/jniLibs` directory of your module, or possibly in some
other directory configured in your `build.gradle` file:

    sourceSets {
      main {
        // The libs directory contains prebuilt libraries that are used by the
        // app's library defined in CMakeLists.txt via an IMPORTED target.
        jniLibs.srcDirs = ['libs']
      }
    }

    sourceSets {
      main {
        // The libs directory contains prebuilt libraries that are used by the
        // app's library defined in CMakeLists.txt via an IMPORTED target.
        jniLibs.setSrcDirs(listOf("libs"))
      }
    }

With Android Gradle Plugin 4.0, the above configuration is no longer necessary
and will result in a build failure:

    * What went wrong:
    Execution failed for task ':app:mergeDebugNativeLibs'.
      > A failure occurred while executing com.android.build.gradle.internal.tasks.Workers$ActionFacade
        > More than one file was found with OS independent path 'lib/x86/libprebuilt.so'

External native build now automatically packages those
libraries, so explicitly packaging the library with `jniLibs` results in a
duplicate. To avoid the build error, move the prebuilt library to a location
outside `jniLibs` or remove the `jniLibs` configuration from your `build.gradle`
file.

## Known issues

This section describes known issues that exist in Android Gradle plugin 4.0.0.

### Race condition in Gradle worker mechanism

Changes in Android Gradle plugin 4.0 can trigger a race condition in Gradle
when running with `---no--daemon` and versions of Gradle 6.3 or lower, causing
builds to hang after the build is finished.

This issue will be fixed in Gradle 6.4.

<br />