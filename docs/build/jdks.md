---
title: Java versions in Android builds  |  Android Studio  |  Android Developers
url: https://developer.android.com/build/jdks
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gradle build guides](https://developer.android.com/build/gradle-build-overview)

# Java versions in Android builds Stay organized with collections Save and categorize content based on your preferences.



Whether your source code is written in Java, Kotlin, or both,
there are several places you must choose a JDK or Java language
version for your build.

![Overview of JDK relationships in a Gradle build](/static/images/build/jdks.svg)


**Figure 1.** JDK relationships in a build

## Glossary

*Java Development Kit (JDK)*
:   The [Java Development Kit (JDK)](https://www.oracle.com/java)
    contains:

    * Tools, such as a compiler, profiler, and archive creator.
      These are used behind the scenes during your build to
      create your application.
    * Libraries containing APIs that you can call from your
      Kotlin or Java source code. Note that not all functions are
      available on Android.
    * The Java Virtual Machine (JVM), an interpreter that executes
      Java applications. You use the JVM to run the Android Studio IDE
      and the Gradle build tool. The JVM is not used on Android
      devices or emulators.

*JetBrains Runtime (JBR)*
:   The [JetBrains Runtime (JBR)](https://github.com/JetBrains/JetBrainsRuntime) is an enhanced JDK, distributed with Android Studio.
    It includes several optimizations for use in Studio and related JetBrains
    products, but can also be used to run other Java applications.

## How do I choose a JDK to run Android Studio?

We recommend that you use the JBR to run Android Studio. It's deployed
with and used to test Android Studio, and includes enhancements for optimal
Android Studio usage. To ensure this, don't set the `STUDIO_JDK`
environment variable.

The startup scripts for Android Studio look for a JVM in the following
order:

1. `STUDIO_JDK` environment variable
2. `studio.jdk` directory (in the Android Studio distribution)
3. `jbr` directory (JetBrains Runtime), in the Android Studio
   distribution. Recommended.
4. `JDK_HOME` environment variable
5. `JAVA_HOME` environment variable
6. `java` executable in the `PATH` environment variable

## How do I choose which JDK runs my Gradle builds?

If you run Gradle using the buttons in Android Studio, the JDK set in the
Android Studio settings is used to run Gradle. If you run Gradle in a terminal,
either inside or outside Android Studio, the `JAVA_HOME` environment variable
(if set) determines which JDK runs the Gradle scripts. If `JAVA_HOME`
is not set, it uses the `java` command on your `PATH` environment
variable.

For the most consistent results, make sure you set your `JAVA_HOME`
environment variable, and
[Gradle JDK configuration in Android Studio](#jdk-config-in-studio) to that same
JDK.

**Note:** If you run a Gradle command in the Android Studio Terminal by
right-clicking and selecting **Run highlighted command** using the IDE then it
uses the JDK in the Android Studio settings, not JAVA\_HOME.

When running your build, Gradle creates a process called a *daemon* to
perform the actual build. This process can be reused,
as long as the builds are using the same JDK and Gradle version. Reusing
a daemon reduces the time to start a new JVM and initialize the build system.

If you start builds with different JDKs or Gradle versions, additional
daemons are created, consuming more CPU and memory.

**Tip:** When working with multiple projects simultaneously, if possible,
specify the same Gradle version in their
[`gradle-wrapper.properties` file](/build#wrapper-file)
to reduce the number of Gradle daemons created.

### Gradle JDK configuration in Android Studio

**Note:** Android Studio Panda 1 and higher uses [Gradle Daemon JVM
criteria](https://docs.gradle.org/current/userguide/gradle_daemon.html#sec:configuring_daemon_jvm) by default for new projects. For existing
projects that use a compatible Gradle version, Android Studio shows a
notification offering an option to automatically migrate your project's defined
Gradle JDK configuration to Daemon JVM criteria while maintaining the same
specifications.

To modify the existing project's Gradle JDK configuration, open the Gradle
settings from **File** (or **Android Studio** on macOS) **> Settings >
Build, Execution, Deployment > Build Tools > Gradle**. The **Gradle JDK**
drop-down contains the following options to select from:

* Macros such as `JAVA_HOME` and `GRADLE_LOCAL_JAVA_HOME`
* JDK table entries in `vendor-version` format like `jbr-17` which are stored
  in the [Android configuration files](/studio/intro/studio-config#file_location)
* Downloading a JDK
* Adding a specific JDK
* Locally detected JDKs from the operating system's default JDK installation
  directory

The selected option is stored in the `gradleJvm` option in the
project's `.idea/gradle.xml` file, and its JDK path resolution is used to run
Gradle when started through Android Studio.

![](/static/images/tools/as-gradle-jdk.png)


**Figure 2.** Gradle JDK settings in Android Studio.

The macros enable dynamic project JDK path selection:

* `JAVA_HOME`: uses the environment variable with the same name
* `GRADLE_LOCAL_JAVA_HOME`: uses the `java.home` property in
  the `.gradle/config.properties` file which defaults to the JetBrains Runtime.

The selected JDK is used to run your Gradle build and resolve JDK API
references when editing your build scripts and source code. Note that the
specified `compileSdk` will further restrict which Java symbols will be
available when editing and building your source code.

**Note:** In most cases, we recommend using `GRADLE_LOCAL_JAVA_HOME`, which
is the default for newly created projects. This lets you define
a project-specific JDK without opening the project first.

Make sure to choose a JDK version that is higher than or equal to the JDK
versions used by plugins that you use in your Gradle build. To determine the
minimum required JDK version for the Android Gradle Plugin (AGP), see the
compatibility table in the [release notes](/build/releases/gradle-plugin).

For example, the Android Gradle Plugin version 8.x requires JDK 17.
If you try to run a Gradle build that uses it with an earlier version of
the JDK, it reports a message like:

```
An exception occurred applying plugin request [id: 'com.android.application']
> Failed to apply plugin 'com.android.internal.application'.
   > Android Gradle plugin requires Java 17 to run. You are currently using Java 11.
      Your current JDK is located in /usr/local/buildtools/java/jdk
      You can try some of the following options:
       - changing the IDE settings.
       - changing the JAVA_HOME environment variable.
       - changing `org.gradle.java.home` in `gradle.properties`.
```

## Which Java APIs can I use in my Java or Kotlin source code?

An Android application can use some of the APIs defined in a JDK, but not all
of them. The Android SDK defines implementations of many Java library functions
as part of its available APIs. The `compileSdk` property specifies which
Android SDK version to use when compiling your Kotlin or Java source code.

### Kotlin

```
android {
    ...
    compileSdk = 36
}
```