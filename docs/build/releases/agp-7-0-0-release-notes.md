---
title: https://developer.android.com/build/releases/agp-7-0-0-release-notes
url: https://developer.android.com/build/releases/agp-7-0-0-release-notes
source: md.txt
---

# Android Gradle Plugin 7.0.0 (July 2021)

Android Gradle plugin 7.0.0 is a major release that includes a variety of new
features and improvements.
**7.0.1 (August 2021)**


This minor update includes various bug fixes.
To see a list of notable bug fixes, read the related post on the
[Release Updates blog](https://androidstudio.googleblog.com/2021/08/android-studio-arctic-fox-202031-patch.html).

## Compatibility

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 7.0.2 | 7.0.2 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.2 | 30.0.2 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 21.4.7075529 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

## JDK 11 required to run AGP 7.0

When using Android Gradle plugin 7.0 to build your app, JDK 11 is now
required to run Gradle. Android Studio Arctic Fox bundles JDK 11 and
configures Gradle to use it by default, which means that most Android Studio
users do not need to make any configuration changes to their projects.

If you need to manually [set the
JDK version](https://developer.android.com/studio/intro/studio-config#jdk) used by AGP inside of Android Studio, you need to use JDK 11
or higher.

When using AGP independent of Android Studio, upgrade the JDK version by
setting the [JAVA_HOME environment variable](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_environment_variables)
or the `-Dorg.gradle.java.home` [command-line option](https://docs.gradle.org/current/userguide/command_line_interface.html#environment_options)
to your installation directory of JDK 11.

Note that the SDK Manager and AVD Manager in the deprecated SDK Tools package
don't work with JDK 11. To continue to use the SDK Manager and AVD Manager
with AGP 7.0 and higher, you need to switch to the new versions of the tools in
the current
[Android SDK Command-Line Tools
package](https://developer.android.com/studio/command-line#tools-sdk).

## Variant API stable

The new Variant API is now stable. See the new interfaces in the
[com.android.build.api.variant](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/variant/Variant)
package, and examples in the
[gradle-recipes](https://github.com/android/gradle-recipes/tree/agp-7.0) GitHub project. As part of the new
Variant API, we have made available a number of intermediate files, called
artifacts, through the
[Artifacts](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/artifact/Artifacts)
interface. These artifacts, like the merged manifest, can be safely obtained
and customized by using third-party plugins and code.

We will continue extending the Variant API by adding new functionalities
and augmenting the number of intermediate artifacts we make available for
customization.

## Behavior changes for Lint

This section describes multiple Lint behavior changes in Android Gradle
plugin 7.0.0.

### Improved lint for library dependencies

Running lint with `checkDependencies = true` is now faster
than before. For Android projects consisting of an app with library
dependencies, it is recommended to set `checkDependencies` to
`true` as shown below, and to run lint via
`./gradlew :app:lint`, which will analyze all dependency
modules in parallel and produce a single report including issues from the
app and all of its dependencies.

### Groovy

    // build.gradle
    android {
      ...
      lintOptions {
        checkDependencies true
      }
    }

### Kotlin

    // build.gradle.kts
    android {
      ...
      lint {
        isCheckDependencies = true
      }
    }

### Lint tasks can now be UP-TO-DATE

If a module's sources and resources have not changed, the lint analysis
task for the module does not need to run again. When this happens, the
execution of the task appears as "UP-TO-DATE" in the Gradle
output. With this change, when running lint on an application module with `checkDependencies = true`, only modules that have changed will
need to run their analysis. As a result, Lint can run even faster.

The Lint report task also does not need to run if its inputs have not
changed. A related **known issue** is that there is no lint
text output printed to stdout when the lint task is UP-TO-DATE
([issue #191897708](https://issuetracker.google.com/191897708)).

### Running lint on dynamic-feature modules

AGP no longer supports running lint from dynamic-feature modules.
Running lint from the corresponding application module will run lint on
its dynamic-feature modules and include all issues in the app's lint
report. A related **known issue** is that when running lint
with `checkDependencies = true` from an app module,
dynamic-feature library dependencies aren't checked unless they're also app
dependencies ([issue
#191977888](https://issuetracker.google.com/191977888)).

### Running lint on default variant only

Running `./gradlew :app:lint` now runs lint for only the
default variant. In previous versions of AGP, it would run lint for all
variants.

## Missing class warnings in R8 shrinker

[R8](https://developer.android.com/studio/build/shrink-code) more precisely and
consistently handles missing classes and the `-dontwarn` option.
Therefore, you should start to evaluate the missing class warnings emitted
by R8.

When R8 encounters a class reference that is not defined in your app or
one of its dependencies, it will emit a warning that appears in your build
output. For example:

    R8: Missing class: java.lang.instrument.ClassFileTransformer

This warning means that the class definition
`java.lang.instrument.ClassFileTransformer` could not be found
when analyzing your app's code. While this usually means there is an error,
it's possible that you may want to ignore this warning. Two common reasons
to ignore the warning are:

1. Libraries that are targeting the JVM and the missing class are of JVM
   library type (as in the example above).

2. One of your dependencies uses a compile-time only API.

You can ignore a missing class warning by adding a `-dontwarn`
rule to your `proguard-rules.pro` file. For example:

    -dontwarn java.lang.instrument.ClassFileTransformer

For convenience, AGP will generate a file that contains all potentially
missing rules, writing them to a file path such as the following:
`app/build/outputs/mapping/release/missing_rules.txt`. Add the
rules to your `proguard-rules.pro` file to ignore warnings.

In AGP 7.0, missing class messages will appear as warnings, and you can
turn them into errors by setting
`android.r8.failOnMissingClasses = true` in
`gradle.properties`. In AGP 8.0, these warnings will become
errors that break your build. It is possible to keep the AGP 7.0 behavior by
adding the option `-ignorewarnings` to your
`proguard-rules.pro` file, but that is not recommended.

## Android Gradle plugin build cache removed

The AGP build cache was removed in AGP 4.1. Previously introduced in AGP
2.3 to complement the Gradle build cache, the AGP build cache was superseded
entirely by the Gradle build cache in AGP 4.1. This change does not impact
build time.

In AGP 7.0, the `android.enableBuildCache` property,
`android.buildCacheDir` property, and the
`cleanBuildCache` task have been removed.

## Use Java 11 source code in your project

You can now compile up to Java 11 source code in your app's project, enabling
you to use newer language features like private interface methods, the diamond
operator for anonymous classes, and local variable syntax for lambda parameters.

To enable this feature, set `compileOptions` to the desired
Java version and set `compileSdkVersion` to 30 or above:

    // build.gradle
    android {
      compileSdkVersion 30
      compileOptions {
        sourceCompatibility JavaVersion.VERSION_11
        targetCompatibility JavaVersion.VERSION_11
      }
      // For Kotlin projects
      kotlinOptions {
        jvmTarget = "11"
      }
    }

    // build.gradle.kts
    android {
      compileSdkVersion(30)
      compileOptions {
        sourceCompatibility(JavaVersion.VERSION_11)
        targetCompatibility(JavaVersion.VERSION_11)
      }
      kotlinOptions {
        jvmTarget = "11"
      }
    }

## Dependency configurations removed

In AGP 7.0, the following configurations (or dependency scopes) have been
removed:

- `compile`  
  Depending on use case, this has been replaced by [`api`](https://developer.android.com/studio/build/dependencies#api) or [`implementation`](https://developer.android.com/studio/build/dependencies#implementation).  
  Also applies to *\*Compile* variants, for example: `debugCompile`.
- `provided`  
  This has been replaced by [`compileOnly`](https://developer.android.com/studio/build/dependencies#compileOnly).  
  Also applies to *\*Provided* variants, for example: `releaseProvided`.
- `apk`  
  This has been replaced by [`runtimeOnly`](https://developer.android.com/studio/build/dependencies#runtimeOnly).
- `publish`  
  This has been replaced by [`runtimeOnly`](https://developer.android.com/studio/build/dependencies#runtimeOnly).

In most cases, the [AGP
Upgrade Assistant](https://developer.android.com/studio/releases#agp-upgrade-assistant) will automatically migrate your project to the new
configurations.

## Classpath change when compiling against Android
Gradle plugin

If you are compiling against the Android Gradle plugin, your compile
classpath may change. Because AGP now uses `api/implementation`
configurations internally, some artifacts may be removed from your compile
classpath. If you depend on an AGP dependency at compile-time, be sure to
add it as an explicit dependency.

## Addition of native libraries in a Java resources
folder is not supported

Previously, you could add a native library in a Java resources folder, and
register the folder using `android.sourceSets.main.resources.srcDirs
`so that the native library would be extracted and added to the final
APK. Starting with AGP 7.0, this is not supported and native libraries in a
Java resources folder are ignored. Instead, use the DSL method intended for
native libraries, `android.sourceSets.main.jniLibs.srcDirs`. For
more information, see
[how to configure
source sets](https://developer.android.com/studio/build/build-variants#configure-sourcesets).

## Known issues

This section describes known issues that exist in Android Gradle plugin
7.0.0.

### Incompatibility with 1.4.x Kotlin Multiplatform plugin

Android Gradle Plugin 7.0.0 is compatible with
[Kotlin
Multiplatform plugin](https://developer.android.com/build/releases/(https:/plugins.jetbrains.com/plugin/14936-kotlin-multiplatform-mobile/versions/dev)%7B:.external%7D) 1.5.0 and higher. Projects that use the Kotlin
Multiplatform support need to update to Kotlin 1.5.0 to use Android Gradle
Plugin 7.0.0. As a workaround, you can downgrade the Android Gradle plugin
to 4.2.x, although this is not recommended.

For more information, see
[KT-43944](https://youtrack.jetbrains.com/issue/KT-43944).

### Missing lint output

There is no lint text output printed to stdout when the lint task is
up-to-date
([issue #191897708](https://issuetracker.google.com/191897708)).
For more context, see
[Behavior changes for lint](https://developer.android.com/build/releases/agp-7-0-0-release-notes#lint-behavior-changes). This issue
will be fixed in Android Gradle plugin 7.1.

### Not all dynamic-feature library dependencies are lint checked

When running lint with `checkDependencies = true` from an
app module, dynamic-feature library dependencies aren't checked unless
they're also app dependencies
([issue #191977888](https://issuetracker.google.com/191977888)).
As a workaround, the lint task can be run on those libraries. For more context,
see [Behavior changes for lint](https://developer.android.com/build/releases/agp-7-0-0-release-notes#lint-behavior-changes).