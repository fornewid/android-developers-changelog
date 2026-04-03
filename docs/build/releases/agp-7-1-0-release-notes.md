---
title: https://developer.android.com/build/releases/agp-7-1-0-release-notes
url: https://developer.android.com/build/releases/agp-7-1-0-release-notes
source: md.txt
---

# Android Gradle Plugin 7.1.0 (January 2022)

Android Gradle plugin 7.1.0 is a major release that includes a variety of
new features and improvements.
**7.1.3 (April 2022)**


This minor update includes the following bug fixes:

- Duplicate class issues reported by R8


To see a complete list of bug fixes included in this release, see the
[Android Studio Bumblebee Patch 3 blog post](https://androidstudio.googleblog.com/2022/04/android-studio-bumblebee-202111-patch-3.html).

**7.1.2 (February 2022)**


This minor update includes the following bug fixes:

- Android Gradle Plugin 7.1.0-rc01 fails to perform ASM bytecode transformation during unit tests
- Gradle sync fails with "Unable to load class 'com.android.build.api.extension.AndroidComponentsExtension'."
- Some new DSL blocks can't be used from Groovy DSL in Android Gradle Plugin 7.0.0
- AGP 7.1 new publishing API: created javadoc jar does not get signed
- ClassesDataSourceCache should use latest Asm version
- Android Studio BumbleBee does not always deploy latest changes


To see a complete list of bug fixes included in this release, see the
[Android Studio Bumblebee Patch 2 blog post](https://androidstudio.googleblog.com/2022/02/android-studio-bumblebee-202111-patch-2.html).

**7.1.1 (February 2022)**


This minor update corresponds to the release of Android Studio Bumblebee
Patch 1.


To see a list of bug fixes included in this release, see the
[Android Studio Bumblebee Patch 1 blog post](https://androidstudio.googleblog.com/2022/02/android-studio-bumblebee-202111-patch-1.html).

## Compatibility


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 7.2 | 7.2 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 21.4.7075529 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

## Lint analysis task is now cacheable

The `AndroidLintAnalysisTask` is now compatible with the
[Gradle
build cache](https://docs.gradle.org/current/userguide/build_cache.html). If you enable the build cache by setting
`org.gradle.caching=true` in your `gradle.properties`
file, the lint analysis task will get its output from the build cache when
possible.

The lint analysis task is often the biggest bottleneck when running lint
with the Android Gradle plugin, so enabling the build cache improves build
speed when running lint in many situations. You should see a noticeable
performance improvement, for example, if you have a multi-module project and
clean your build directory before running lint on your CI server.

## C/C++ modules may now reference other C/C++ modules in
the same project

A Gradle Android module with C/C++ code may now be set up to reference
header files and library code in another Gradle module. The
[Prefab](https://google.github.io/prefab/) protocol is used to
communicate the headers and libraries between Gradle modules.

### Requirements

- The *consuming* module must be `CMake` and not
  `ndk-build`. Support for ndk-build will require a future
  NDK update. The *publishing* module may be `CMake` or
  `ndk-build`.

- The *consuming* module must enable `prefab` in
  the `build.gradle` file.

    android {
      buildFeatures {
        prefab true
      }
    }

- The *publishing* module must enable `prefabPublishing` in the `build.gradle` file.

    android {
      buildFeatures {
        prefabPublishing true
      }
    }

- The *consuming* module must reference the *publishing* module by adding a line in the `build.gradle` file `dependencies` block. For example:

    dependencies {
      implementation project(':mylibrary')
    }

- The *publishing* module must expose a package using a `prefab` section. For example:

    android {
      prefab {
        mylibrary {
          libraryName "libmylibrary"
          headers "src/main/cpp/include"
        }
      }
    }

- The consuming module's `CMakeLists.txt` file may use `find_package()` to locate the package published by the producing module. For example:

    find_package(mylibrary REQUIRED CONFIG)
    target_link_libraries(
      myapplication
      mylibrary::mylibrary)

- There must be [one
  STL for the entire application](https://developer.android.com/ndk/guides/cpp-support#one_stl_per_app). So, for example, both consuming and publishing modules can use C++ shared STL.

       android {
          defaultConfig {
            externalNativeBuild {
              cmake {
                arguments '-DANDROID_STL=c++_shared'
              }
            }
          }
        }

For further explanation of how to configure native AAR consumers and
producers with AGP, see
[Native
dependencies with AGP](https://developer.android.com/studio/build/dependencies?&agpversion=4.1&buildsystem=ndk-build#native-dependencies-with-agp).

## Repository settings in `settings.gradle` file

When a new project is created in Android Studio Bumblebee, the top-level
`build.gradle` file contains the `plugins` block,
followed by code to clean your build directory:

    plugins {
        id 'com.android.application' version '7.1.0-beta02' apply false
        id 'com.android.library' version '7.1.0-beta02' apply false
        id 'org.jetbrains.kotlin.android' version '1.5.30' apply false
    }
    task clean(type: Delete) {
      delete rootProject.buildDir
    }

The repository settings that were previously in the top-level
`build.gradle` file are now in the `settings.gradle`
file:

    pluginManagement {
      repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
      }
    }
    dependencyResolutionManagement {
      repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
      repositories {
        google()
        mavenCentral()
      }
    }
    rootProject.name = 'GradleManagedDeviceTestingNew'
    include ':app'

The module-level `build.gradle` file has not changed. So, use the top-level
`build.gradle` file and the `settings.gradle` file to define build
configurations that apply to all modules in your project, or the repositories
and dependencies that apply to Gradle itself; use the module-level
`build.gradle` file to define build configurations that are specific to a given
module within your project.

## Improved resource shrinker

Android Studio Bumblebee includes an improved resource shrinker that helps
reduce your app size.

### Support for apps with dynamic features

The default implementation of the Android resource shrinker has been
updated in Android Gradle Plugin 7.1.0-alpha09. The new implementation
supports shrinking apps with dynamic features.

### Experimental further app size reductions

The new resource shrinker implementation can reduce the size of your
shrunk app even more by modifying the resource table to remove unused
value resources and references to unused file resources. The new resource
shinker can delete unused file resources completely, reducing the size of
your app more. This behavior is not enabled by default yet, but you can
opt in to try it by adding the experimental option
`android.experimental.enableNewResourceShrinker.preciseShrinking=true`
to your project's `gradle.properties` file.

Please report any issues you find with the new resource shrinker or the
experimental flag. To help diagnose issues, or as a temporary workaround,
you can switch back to the previous implementation by adding
`android.enableNewResourceShrinker=false` to your project's
`gradle.properties`.
The new shrinker replaces unused file-based resources with slightly different
minimal files than the previous resource shrinker, but this is not expected
to have any runtime impact.

The old implementation is scheduled to be removed in Android Gradle
plugin 8.0.0.

## Build variant publishing

Android Gradle plugin 7.1.0 and higher allows you to configure which build
variants to publish to an Apache Maven repository. AGP creates a component
with a single or multiple build variants based on the new publishing DSL, which
you can use to customize a publication to a Maven repository. Compared to
previous versions, this also avoids unnecessary work, as no components will be
created by default. To learn more, see the [publishing code sample](https://android.googlesource.com/platform/tools/base/+/refs/heads/mirror-goog-studio-main/build-system/gradle-api/src/main/java/com/android/build/api/dsl/Publishing.kt).

## Publish Javadoc JAR

AGP 7.1.0 and higher allows you to generate Javadoc from Java and Kotlin
sources and publish Javadoc JAR files in addition to AARs for library
projects. The Javadoc is added to the POM and
[Gradle Module Metadata](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html){:.external}
files. Enable this feature by adding `withJavadocJar()` in the
`singleVariant` or `multipleVariants` publishing block.
To learn more, see the
[publishing options code sample](https://android.googlesource.com/platform/tools/base/+/refs/heads/mirror-goog-studio-main/build-system/gradle-api/src/main/java/com/android/build/api/dsl/PublishingOptions.kt#50).

## Publish sources JAR

AGP 7.1.0 and higher allows you to publish Java and Kotlin source JAR
files in addition to AARs for library projects. The sources are added to the
POM and
[Gradle Module Metadata](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html){:.external} files. You can enable this
feature by adding `withSourcesJar()` in the
`singleVariant` or `multipleVariants` publishing
block. To learn more, see the
[publishing options code sample](https://android.googlesource.com/platform/tools/base/+/refs/heads/mirror-goog-studio-main/build-system/gradle-api/src/main/java/com/android/build/api/dsl/PublishingOptions.kt#45).

## Lint block semantic change

All lint methods that override the given severity level of an
issue---`enable`, `disable`/`ignore`,
`informational`, `warning`, `error`,
`fatal`---now respect the order of configuration. For example,
setting an issue as fatal in
[`finalizeDsl()`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/extension/AndroidComponentsExtension#finalizedsl)
now overrides disabling it in the main DSL. For more information, see the
[`lint{}`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/Lint)
block reference docs and
[Android build
flow and extension points](https://developer.android.com/studio/build/extend-agp#build-flow-extension-points).

## Navigation Safe Args compatibility

AGP APIs that the
[Navigation
Safe Args Gradle plugin](https://developer.android.com/guide/navigation/navigation-getting-started#ensure_type-safety_by_using_safe_args) depend on have been removed. AGP 7.1 does not
work with Navigation Safe Args versions 2.4.0-rc1 or 2.4.0, but will work
with versions 2.5.0-alpha01 and 2.4.1. In the meantime, as a workaround,
you can use AGP 7.1 with a snapshot build of Navigation Safe Args,
Navigation 2.5.0-SNAPSHOT. To use the snapshot build, follow the
[snapshot instructions](https://androidx.dev/)
with build id #8054565.

In addition, Navigation Safe Args versions 2.4.1 and 2.5.0 will no longer
work with AGP 4.2; to use those versions of Safe Args, you must use AGP 7.0
and higher.

## Disable automatic component creation

Starting AGP 8.0, automatic component creation will be disabled by default.
Currently, AGP 7.1 automatically creates a component for each build variant,
which has the same name as the build variant, and an an `all`
component that contains all the build variants. This automatic component
creation will be disabled. To transition to the new behavior, you should
manually disable automatic component creation by setting
`android.disableAutomaticComponentCreation `to` true.`
For more information, see
[Use the Maven Publish plugin](https://developer.android.com/studio/build/maven-publish-plugin).

## Firebase Performance Monitoring compatibility

AGP 7.1 is incompatible with the Firebase Performance Monitoring Gradle
plugin version 1.4.0 and lower. The AGP Upgrade Assistant will not automatically
update the plugin to version 1.4.1, so if you are using `firebase-perf` and wish
to upgrade AGP to 7.1, you need to do this particular upgrade manually.

## Known issues

This section describes known issues that exist in Android Gradle plugin
7.1.0.

### Problems with unit testing an app project that uses the Hilt plugin

The unit test classpath contains the non-instrumented app classes, which
means Hilt does not instrument the app classes to handle dependency injection
when running unit tests.

This issue will be fixed with 7.1.1 release,
see [issue #213534628](https://issuetracker.google.com/213534628).