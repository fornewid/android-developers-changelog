---
title: Android Studio Panda 1 (February 2026)  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-panda-1-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

# Android Studio Panda 1 (February 2026) Stay organized with collections Save and categorize content based on your preferences.




The following are new features in Android Studio Panda 1.

## Simplified JDK management with Gradle Daemon JVM Criteria

To simplify JDK management for Gradle builds, Android Studio now uses
[Gradle Daemon JVM criteria](https://docs.gradle.org/current/userguide/gradle_daemon.html#sec:configuring_daemon_jvm)
by default for new projects. This feature lets Gradle [auto-detect](https://docs.gradle.org/current/userguide/toolchains.html#sec:auto_detection)
compatible JDK for your project installed in your machine to execute Gradle
builds or [auto-provision](https://docs.gradle.org/current/userguide/toolchains.html#sec:provisioning)
the required JDK by downloading it if it cannot be found locally. This feature was
stabilized in [Gradle 9.2.0](https://docs.gradle.org/9.2.0/release-notes.html).

This simplifies project setup and improves JDK management in several ways:

* **Fewer setup errors**: You no longer need to have a specific JDK
  installed to import and build a project, which reduces setup-related
  errors given invalid JDK selection.
* **Consistent builds**: JDK selection for Gradle builds is not only
  consistent across different machines but also between the IDE and command-line,
  which prevents spawning multiple Gradle Daemons that adversely affect
  performance.

For existing projects that use a compatible Gradle version, Android Studio
shows a notification offering an option to automatically migrate your project's
defined [Gradle JDK configuration](/build/jdks#jdk-config-in-studio) to
Daemon JVM criteria, while maintaining the same specifications.

![](/static/studio/preview/features/images/gradle-build-execution-flow.png)


New flow for Gradle build executions

**Note:** The project Daemon JVM criteria represents a replacement for the
old Gradle JDK configuration and can be modified from
**File** (**Android Studio** on macOS)
**> Settings > Build, Execution, Deployment > Build Tools > Gradle**.