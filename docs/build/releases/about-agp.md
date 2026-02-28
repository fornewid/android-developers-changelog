---
title: https://developer.android.com/build/releases/about-agp
url: https://developer.android.com/build/releases/about-agp
source: md.txt
---

> [!IMPORTANT]
> **Important:** For a detailed log of Android Gradle plugin API deprecations and removals, see the [Android Gradle plugin API updates](https://developer.android.com/studio/releases/gradle-plugin-api-updates).

The Android Studio build system is based on Gradle, and the Android Gradle
plugin adds several features that are specific to build Android apps.

This page explains how to keep your Gradle tools up to date. For release notes
on the Android Gradle plugin, see the [release notes page](https://developer.android.com/build/releases/gradle-plugin).

For a high-level summary of upcoming breaking changes in the Android Gradle
plugin, see the [Android
Gradle plugin roadmap](https://developer.android.com/studio/releases/gradle-plugin-roadmap).

For details about how to configure your Android builds with Gradle,
see the following pages:

- [Configure your build](https://developer.android.com/build)
- [Android Gradle plugin DSL reference](https://developer.android.com/reference/tools/gradle-api)
- [Gradle DSL reference](https://docs.gradle.org/current/dsl/)
- [Gradle performance user guide](https://docs.gradle.org/current/userguide/performance.html)

For more information about the Gradle build system, see the
[Gradle user guide](https://docs.gradle.org/current/userguide/userguide.html).

## Update the Android Gradle plugin


When you update Android Studio, you may receive a prompt to automatically
update the Android Gradle plugin to the latest available version. You
can choose to accept the update or manually specify a version based on
your project's build requirements.


You can specify the plugin version in
either the **File** \> **Project
Structure** \> **Project** menu in Android Studio, or
the top-level `build.gradle.kts` file. The plugin version applies to
all modules built in that Android Studio project. The following example sets
the plugin to version 9.0.0 from the
`build.gradle.kts` file:

### Kotlin

```kotlin
plugins {
    id("com.android.application") version "9.0.0" apply false
    id("com.android.library") version "9.0.0" apply false
    id("org.jetbrains.kotlin.android") version "2.3.10" apply false
}
```

### Groovy

```groovy
plugins {
    id 'com.android.application' version '9.0.0' apply false
    id 'com.android.library' version '9.0.0' apply false
    id 'org.jetbrains.kotlin.android' version '2.3.10' apply false
}
```


**Caution:** You should not use dynamic dependencies in version
numbers, such as
`'com.android.tools.build:gradle:9.0.+'`.
Using this feature can cause unexpected version updates and difficulty
resolving version differences.


If the specified plugin version has not been downloaded, Gradle downloads it
the next time you build your project or click **File** \>
**Sync Project with Gradle Files**
from the Android Studio menu bar.

## Update Gradle


When you update Android Studio, you may receive a prompt to also
update Gradle to the latest available version. You can choose to accept the
update or manually specify a version based on your project's build
requirements.

The following table lists which version of Gradle is required for each
version of the Android Gradle plugin. For the best performance, you should
use the latest possible version of both Gradle and the plugin.

| Plugin version | Minimum required Gradle version |
|---|---|
| 9.0 | 9.1.0 |
| 8.13 | 8.13 |
| 8.12 | 8.13 |
| 8.11 | 8.13 |
| 8.10 | 8.11.1 |
| 8.9 | 8.11.1 |
| 8.8 | 8.10.2 |
| 8.7 | 8.9 |
| 8.6 | 8.7 |
| 8.5 | 8.7 |
| 8.4 | 8.6 |
| 8.3 | 8.4 |
| 8.2 | 8.2 |
| 8.1 | 8.0 |
| 8.0 | 8.0 |

### Older versions

| Plugin version | Required Gradle version |
|---|---|
| 7.4 | 7.5 |
| 7.3 | 7.4 |
| 7.2 | 7.3.3 |
| 7.1 | 7.2 |
| 7.0 | 7.0 |
| 4.2.0+ | 6.7.1 |
| 4.1.0+ | 6.5+ |
| 4.0.0+ | 6.1.1+ |
| 3.6.0 - 3.6.4 | 5.6.4+ |
| 3.5.0 - 3.5.4 | 5.4.1+ |
| 3.4.0 - 3.4.3 | 5.1.1+ |
| 3.3.0 - 3.3.3 | 4.10.1+ |
| 3.2.0 - 3.2.1 | 4.6+ |
| 3.1.0+ | 4.4+ |
| 3.0.0+ | 4.1+ |
| 2.3.0+ | 3.3+ |
| 2.1.3 - 2.2.3 | 2.14.1 - 3.5 |
| 2.0.0 - 2.1.2 | 2.10 - 2.13 |
| 1.5.0 | 2.2.1 - 2.13 |
| 1.2.0 - 1.3.1 | 2.2.1 - 2.9 |
| 1.0.0 - 1.1.3 | 2.2.1 - 2.3 |


You can specify the Gradle version in either the **File** \>
**Project Structure** \> **Project** menu in Android Studio,
or update your Gradle version using the command line.
The preferred way is to use the
[Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html)
command line tool, which updates the `gradlew` scripts. The following
example sets the Gradle version to 9.1.0 using the Gradle Wrapper.
Note, you need to run this command *twice* to upgrade both Gradle and the
Gradle Wrapper itself (for more information, see
[Upgrading the Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html#sec:upgrading_wrapper)).

    gradle wrapper --gradle-version 9.1.0


However this might fail in some cases, for example if you've just updated AGP
and it's no longer compliant with the current Gradle version. In this case,
you need to edit the Gradle distribution reference in the
`gradle/wrapper/gradle-wrapper.properties` file. The following
example sets the Gradle version to 9.1.0 in the
`gradle-wrapper.properties` file.

    ...
    distributionUrl = https\://services.gradle.org/distributions/gradle-9.1.0-bin.zip
    ...


## Android Gradle
plugin and Android Studio compatibility

The Android Studio build system is based on Gradle, and the Android Gradle
plugin (AGP) adds several features that are specific to building Android apps. The
following table lists which version of AGP is required for each version of
Android Studio.

> [!NOTE]
> There is now a time-based compatibility policy for AGP and Android Studio. Each Android Studio version will support AGP versions released within the previous 3 years. AGP versions older than 3 years will no longer be supported in newer Android Studio versions. If your project's AGP version is incompatible, Android Studio will require you to update AGP.

> [!NOTE]
> If your project is not supported by a specific version of Android Studio, you can still open and update your project using an [older version of Android Studio](https://developer.android.com/studio/archive).

| Android Studio version | Required AGP version |
|---|---|
| Panda 1 \| 2025.3.1 | 4.0-9.0 |
| Otter 3 Feature Drop \| 2025.2.3 | 4.0-9.0 |
| Otter 2 Feature Drop \| 2025.2.2 | 4.0-8.13 |
| Otter \| 2025.2.1 | 4.0-8.13 |
| Narwhal 4 Feature Drop \| 2025.1.4 | 4.0-8.13 |
| Narwhal 3 Feature Drop \| 2025.1.3 | 4.0-8.13 |
| Narwhal Feature Drop \| 2025.1.2 | 4.0-8.12 |
| Narwhal \| 2025.1.1 | 3.2-8.11 |
| Meerkat Feature Drop \| 2024.3.2 | 3.2-8.10 |
| Meerkat \| 2024.3.1 | 3.2-8.9 |

### Older versions

| Android Studio version | Required AGP version |
|---|---|
| Ladybug Feature Drop \| 2024.2.2 | 3.2-8.8 |
| Ladybug \| 2024.2.1 | 3.2-8.7 |
| Koala Feature Drop \| 2024.1.2 | 3.2-8.6 |
| Koala \| 2024.1.1 | 3.2-8.5 |
| Jellyfish \| 2023.3.1 | 3.2-8.4 |
| Iguana \| 2023.2.1 | 3.2-8.3 |
| Hedgehog \| 2023.1.1 | 3.2-8.2 |
| Giraffe \| 2022.3.1 | 3.2-8.1 |
| Flamingo \| 2022.2.1 | 3.2-8.0 |
| Electric Eel \| 2022.1.1 | 3.2-7.4 |
| Dolphin \| 2021.3.1 | 3.2-7.3 |
| Chipmunk \| 2021.2.1 | 3.2-7.2 |
| Bumblebee \| 2021.1.1 | 3.2-7.1 |
| Arctic Fox \| 2020.3.1 | 3.1-7.0 |

For information on what's new in the Android Gradle plugin, see the
[Android Gradle plugin release notes](https://developer.android.com/studio/releases/gradle-plugin).

<br />


## Minimum versions of tools for Android API level

There are minimum versions of Android Studio and AGP that support a specific API
level. Using lower versions of Android Studio or AGP than required by your
project's `targetSdk` or `compileSdk` could lead to unexpected issues. We
recommend using the latest preview version of Android Studio and AGP to work on
projects that target preview versions of the Android OS. You can
[install
preview versions of Android Studio alongside a stable version](https://developer.android.com/studio/preview/install-preview#install_alongside_your_stable_version).

The minimum versions of Android Studio and AGP are as follows:

| API level | Minimum Android Studio version | Minimum AGP version |
|---|---|---|
| 36.1 | Narwhal 3 Feature Drop \| 2025.1.3 | 8.13.0 |
| 36.0 | Meerkat \| 2024.3.1 Patch 1 | 8.9.1 |
| 35 | Koala Feature Drop \| 2024.2.1 | 8.6.0 |
| 34 | Hedgehog \| 2023.1.1 | 8.1.1 |
| 33 | Flamingo \| 2022.2.1 | 7.2 |

<br />