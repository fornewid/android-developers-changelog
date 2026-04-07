---
title: https://developer.android.com/build/optimize-your-build
url: https://developer.android.com/build/optimize-your-build
source: md.txt
---

Long build times slow down your development process. This page provides some techniques to help
resolve build speed bottlenecks.

The general process of improving your app's build speed is as follows:

1. [Optimize your build configuration](https://developer.android.com/build/optimize-your-build#optimize) by taking a few steps that immediately benefit most Android Studio projects.
2. [Profile your build](https://developer.android.com/studio/build/profile-your-build) to identify and diagnose some of the trickier bottlenecks that may be specific to your project or workstation.


When developing your app, deploy to a device running Android
7.0 (API level 24) or higher whenever possible. Newer versions of the
Android platform implement better mechanics for pushing updates to your app,
such as the [Android
Runtime (ART)](https://source.android.com/devices/tech/dalvik/) and native support for [multiple DEX files](https://developer.android.com/studio/build/multidex).


**Note:** After your first clean build, you may notice that subsequent
builds, both clean and incremental, perform much faster even without using any of
the optimizations described on this page. This is because the Gradle daemon
has a "warm-up" period of increasing performance---similar to other JVM
processes.

## Optimize your build configuration


Follow these tips to improve the build
speed of your Android Studio project.

### Keep your tools up to date


The Android tools receive build optimizations and new features with almost
every update. Some tips on this page assume you're using the latest
version. To take advantage of the latest optimizations, keep the following up
to date:

- [Android Studio and SDK tools](https://developer.android.com/studio/intro/update)
- [The Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin)

### Use KSP instead of kapt


The Kotlin Annotation Processing Tool (kapt) is significantly slower than the Kotlin
Symbol Processor (KSP). If you are writing annotated Kotlin source and using tooling that
processes annotations (such as [Room](https://developer.android.com/training/data-storage/room))
that supports KSP, you'll want to [migrate to KSP](https://developer.android.com/build/migrate-to-ksp).

### Avoid compiling unnecessary resources


Avoid compiling and packaging resources that you aren't testing, such as
additional language localizations and screen-density resources. Instead, only specify one
language resource and screen density for your "dev" flavor, as shown in the following sample:

### Groovy

```groovy
android {
    ...
    productFlavors {
        dev {
            ...
            // The following configuration limits the "dev" flavor to using
            // English stringresources and xxhdpi screen-density resources.
            resourceConfigurations "en", "xxhdpi"
        }
        ...
    }
}
```

### Kotlin

```kotlin
android {
    ...
    productFlavors {
        create("dev") {
            ...
            // The following configuration limits the "dev" flavor to using
            // English stringresources and xxhdpi screen-density resources.
            resourceConfigurations("en", "xxhdpi")
        }
        ...
    }
}
```

### Experiment with putting the Gradle Plugin Portal last


In Android, all plugins are found in the `google()` and
`mavenCentral()` repositories. However, your build might
need third-party plugins that are resolved using the
[`gradlePluginPortal()`](https://plugins.gradle.org/)
service.

Gradle searches repositories in the order that they're declared,
so build performance is improved if the repositories listed first contain
most of the plugins. Therefore, experiment with the `gradlePluginPortal()`
entry by putting it last in the repository block in your `settings.gradle`
file. In most cases, this minimizes the number of redundant plugin searches and
improves your build speed.


For more information about how Gradle navigates multiple repositories, see
[Declaring multiple repositories](https://docs.gradle.org/current/userguide/declaring_repositories.html#sec:declaring_multiple_repositories)
in the Gradle documentation.

### Use static build config values with your debug build


Always use static values for properties that go in the manifest file or resource files for your
debug build type.


Using dynamic version codes, version names, resources, or any
other build logic that changes the manifest file requires a full app build
every time you want to run a change, even if the actual change might
otherwise require only a hot swap. If your build configuration requires such
dynamic properties, then isolate those properties to your release build variants and keep
the values static for your debug builds, as shown in the following sample:

```kotlin
  ...
  // Use a filter to apply onVariants() to a subset of the variants.
  onVariants(selector().withBuildType("release")) { variant ->
      // Because an app module can have multiple outputs when using multi-APK, versionCode
      // is only available on the variant output.
      // Gather the output when we are in single mode and there is no multi-APK.
      val mainOutput = variant.outputs.single { it.outputType == OutputType.SINGLE }

      // Create the version code generating task.
      val versionCodeTask = project.tasks.register("computeVersionCodeFor${variant.name}", VersionCodeTask::class.java) {
          it.outputFile.set(project.layout.buildDirectory.file("versionCode${variant.name}.txt"))
      }

      // Wire the version code from the task output.
      // map will create a lazy Provider that:
      // 1. Runs just before the consumer(s), ensuring that the producer (VersionCodeTask) has run
      //    and therefore the file is created.
      // 2. Contains task dependency information so that the consumer(s) run after the producer.
      mainOutput.versionCode.set(versionCodeTask.flatMap { it.outputFile.map { it.asFile.readText().toInt() } })
  }
  ...

  abstract class VersionCodeTask : DefaultTask() {

    @get:OutputFile
    abstract val outputFile: RegularFileProperty

    @TaskAction
    fun action() {
        outputFile.get().asFile.writeText("1.1.1")
    }
  }
```

See the [setVersionsFromTask recipe](https://github.com/android/gradle-recipes/blob/agp-7.3/BuildSrc/setVersionsFromTask) on GitHub to learn how to set
a dynamic version code in your project.

### Use static dependency versions


When you declare dependencies in your `build.gradle` files, avoid using dynamic version
numbers (those with a plus sign at the end, such as `'com.android.tools.build:gradle:2.+'`).
Using dynamic version numbers can cause unexpected version updates, difficulty resolving version
differences, and slower builds caused by Gradle checking for updates.
Use static version numbers instead.

### Create library modules


Look for code in your app that you can convert into an [Android library module](https://developer.android.com/studio/projects/android-library).
Modularizing your code this way allows the build system to compile only the
modules you modify and cache those outputs for future builds. Modularization also makes
[parallel project execution](https://docs.gradle.org/current/userguide/performance.html#parallel_execution) more effective when you
enable that optimization.

### Create tasks for custom build logic


After you [create a build profile](https://developer.android.com/studio/build/profile-your-build), if the build
profile shows that a relatively long portion of the build time is spent in the \*\*Configuring
Projects\*\* phase, review your `build.gradle` scripts and look for
code to include in a custom Gradle task. By moving some build logic
into a task, you help ensure that the task runs only when required, results can be cached for
subsequent builds, and that build logic becomes eligible to run in parallel if you enable [parallel project execution](https://docs.gradle.org/current/userguide/performance.html#parallel_execution). To learn more about taks for custom build
logic, read the [official Gradle documentation](https://docs.gradle.org/current/userguide/more_about_tasks.html).


**Tip:** If your build includes a large number of custom tasks, you might
want to declutter your `build.gradle` files by [creating custom task classes](https://docs.gradle.org/current/userguide/custom_tasks.html). Add your classes to the
`project-root/buildSrc/src/main/groovy/` directory;
Gradle automatically includes those classes in the classpath for all
`build.gradle` files in your project.

### Convert images to WebP


[WebP](https://developers.google.com/speed/webp/) is an image file
format that provides lossy compression (like JPEG) as well as transparency
(like PNG). WebP can provide better compression than either JPEG or PNG.

Reducing image file sizes without having to perform build-time compression
can speed up your builds, especially if your app uses a lot of image
resources. However, you may notice a small increase in device CPU usage while
decompressing WebP images. Use Android Studio to easily
[convert your images
to WebP](https://developer.android.com/studio/write/convert-webp#convert_images_to_webp).

### Disable PNG crunching


If you don't [convert your PNG
images to WebP](https://developer.android.com/studio/write/convert-webp#convert_images_to_webp), you can still speed up your build by disabling automatic
image compression every time you build your app.

If you're using [Android Gradle plugin 3.0.0](https://developer.android.com/studio/releases/gradle-plugin#3-0-0)
or higher, PNG crunching is disabled by default for the "debug" build type. To disable this
optimization for other build types, add the following to your `build.gradle` file:

### Groovy

```groovy
android {
    buildTypes {
        release {
            // Disables PNG crunching for the "release" build type.
            crunchPngs false
        }
    }
}
```

### Kotlin

```kotlin
android {
    buildTypes {
        getByName("release") {
            // Disables PNG crunching for the "release" build type.
            isCrunchPngs = false
        }
    }
}
```


Because build types or product flavors don't define this property, you need
to manually set this property to `true` when building the release
version of your app.

### Experiment with the JVM parallel garbage collector


Build performance can be improved by configuring the optimal JVM garbage collector used by Gradle.
While JDK 8 is configured to use the parallel garbage collector by default, JDK 9 and higher are
configured to use
[the G1 garbage collector](https://docs.oracle.com/javase/9/gctuning/garbage-first-garbage-collector.htm#JSGCT-GUID-ED3AB6D3-FD9B-4447-9EDF-983ED2F7A573).


To potentially improve build performance, we recommend
[testing your Gradle builds](https://developer.android.com/studio/build/profile-your-build) with the parallel
garbage collector. In `gradle.properties` set the following:

```text
org.gradle.jvmargs=-XX:+UseParallelGC
```


If there are other options already set in this field, add a new option:

```text
org.gradle.jvmargs=-Xmx1536m -XX:+UseParallelGC
```


To measure build speed with different configurations, see
[Profile your build](https://developer.android.com/studio/build/profile-your-build#profiling_different_memorycpu_settings).

| **Note:** Be aware of Gradle [issue #19750](https://github.com/gradle/gradle/issues/19750): setting the `org.gradle.jvmargs` property can lead to "Daemon disappeared" failures. Until the bug is fixed you must explicitly set JVM argument defaults. The key JVM arguments that you must explicitly set are the `-XX:MaxMetaspaceSize=256m` and `-XX:+HeapDumpOnOutOfMemoryError` arguments; for the full list of arguments, see the [`java` command documentation](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/java.html).

### Increase the JVM heap size


If you observe slow builds, and in particular the garbage collection takes more than 15% of the
build time in your
[Build Analyzer](https://developer.android.com/studio/build/build-analyzer)
results, then you should increase the Java Virtual Machine (JVM) heap size.
In the `gradle.properties` file, set the limit to 4, 6, or 8 gigabytes
as shown in the following example:

```text
org.gradle.jvmargs=-Xmx6g
```


Then test for build speed improvement. The easiest way to determine the optimal heap
size is to increase the limit by a small amount and then test for sufficient build
speed improvement.
| **Note:** If you change the default memory limit, you also have to set the `-XX:MaxMetaspaceSize=1g` argument due to [Gradle issue #19750](https://github.com/gradle/gradle/issues/19750).


If you also use the
[JVM parallel garbage collector](https://developer.android.com/studio/build/profile-your-build#experiment-gc),
then the entire line should look like:

```text
org.gradle.jvmargs=-Xmx6g -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8 -XX:+UseParallelGC -XX:MaxMetaspaceSize=1g
```


You can analyze the JVM memory errors by turning the [HeapDumpOnOutOfMemoryError](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/clopts001.html)
flag on. By doing so, the JVM will generate a heap dump, when running out of memory.

### Use non-transitive R classes


Use non-transitive [`R` classes](https://developer.android.com/reference/android/R) to have faster builds
for apps with multiple modules. Doing so helps prevent resource duplication by ensuring that
each module's `R` class only contains references to its own resources without pulling references from
its dependencies. This leads to faster builds and the corresponding benefits of compilation
avoidance. This is the default behavior in Android Gradle plugin 8.0.0 and higher.


Starting with Android Studio Bumblebee, non-transitive `R` classes are on by default for new projects.
For projects created with earlier versions of Android Studio, update them to use non-transitive
`R` classes by going to **Refactor \> Migrate to Non-Transitive R Classes**.

To learn more about app resources and the `R` class, see
[App resources overview](https://developer.android.com/guide/topics/resources/providing-resources).

### Use non-constant R classes


Use non-constant [`R` class](https://developer.android.com/reference/android/R)
fields in apps and tests to improve the incrementality of Java compilation
and allow for more precise resource shrinking. `R` class fields
are always not constant for libraries, as the resources are numbered
when packaging the APK for the app or test that depends on that library.
This is the default behavior in Android Gradle Plugin 8.0.0 and higher.

### Disable the Jetifier flag


Since most projects use AndroidX libraries directly, you can remove the
[Jetifier](https://developer.android.com/studio/command-line/jetifier) flag for better build performance. To remove
the Jetifier flag, set `android.enableJetifier=false` in your
`gradle.properties` file.

The Build Analyzer can perform a check to see whether the flag can
be safely removed to enable your project to have better build performance and migrate away from the
unmaintained Android Support libraries. To learn more about the Build Analyzer, see
[Troubleshoot build performance](https://developer.android.com/studio/build/build-analyzer).

### Use the configuration cache


The
[configuration cache](https://docs.gradle.org/current/userguide/configuration_cache.html)
lets Gradle record information about the build tasks graph and reuse it in subsequent builds, so
Gradle doesn't have to reconfigure the whole build again.

To enable the configuration cache, follow these steps:

1. Check that all project plugins are compatible.<br />

   Use the
   [Build Analyzer](https://developer.android.com/studio/build/build-analyzer#warnings-types) to check whether your
   project is compatible with the configuration cache. The Build Analyzer runs a sequence of test
   builds to determine whether the feature can be turned on for the project. See
   [issue #13490](https://github.com/gradle/gradle/issues/13490) for
   a list of plugins that are supported.
2. Add the following code to the `gradle.properties` file:

   <br />

   ```text
     org.gradle.configuration-cache=true
     # Use this flag carefully, in case some of the plugins are not fully compatible.
     org.gradle.configuration-cache.problems=warn
   ```

   <br />

When the configuration cache is enabled, the first time you run your project the build output
says `Calculating task graph as no configuration cache is available for tasks`. During
subsequent runs, the build output says `Reusing configuration cache`.

To learn more about the configuration cache, see the blog post
[Configuration caching deep dive](https://medium.com/androiddevelopers/configuration-caching-deep-dive-bcb304698070) and
the Gradle documentation about the
[configuration cache](https://docs.gradle.org/current/userguide/configuration_cache.html).

#### Configuration cache issues introduced in Gradle 8.1 and Android Gradle Plugin 8.1


The configuration cache became stable in Gradle 8.1, and introduced file API
tracking. Calls such as `File.exists()`, `File.isDirectory()` and `File.list()` are recorded by
Gradle to track configuration input files.

Android Gradle Plugin (AGP) 8.1 uses these `File` APIs for some files that Gradle should
not consider to be cache inputs. This triggers additional cache invalidation when used with
Gradle 8.1 and higher, slowing build performance.
The following are treated as cache inputs in AGP 8.1:

| Input | Issue Tracker | Fixed in |
| $GRADLE_USER_HOME/android/FakeDependency.jar | [Issue #289232054](https://issuetracker.google.com/289232054) | AGP 8.2 |
| cmake output | [Issue #287676077](https://issuetracker.google.com/287676077) | AGP 8.2 |
| $GRADLE_USER_HOME/.android/analytics.settings | [Issue #278767328](https://issuetracker.google.com/278767328) | AGP 8.3 |
|---|---|---|


If you use these APIs or a plugin that uses these APIs,
you might experience a regression in your build time, because some build logic using these APIs
can trigger additional cache invalidation. Please see
[Improvements in the build configuration input tracking](https://blog.gradle.org/improvements-in-the-build-configuration-input-tracking)
for a discussion of these patterns and how to fix the build logic, or temporarily disable the
file API tracking.