---
title: https://developer.android.com/build/releases/agp-7-4-0-release-notes
url: https://developer.android.com/build/releases/agp-7-4-0-release-notes
source: md.txt
---

Android Gradle Plugin 7.4.0 is a major release that includes a variety of new
features and improvements.

### Compatibility


|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 7.5 | 7.5 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 30.0.3 | 30.0.3 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |
| NDK | N/A | 23.1.7779620 | [Install](https://developer.android.com/studio/projects/install-ndk#specific-version) or [configure](https://developer.android.com/studio/projects/install-ndk#apply-specific-version) a different version of the NDK. |
| JDK | 11 | 11 | To learn more, see [setting the JDK version](https://developer.android.com/studio/intro/studio-config#jdk). |

<br />

### AGP Upgrade Assistant post-upgrade report and rollback functionality

The AGP Upgrade Assistant now includes a post-upgrade report. This report
describes the steps that were completed and if the upgrade was successful or
unsuccessful. It also includes an action to revert changes that were made by
the upgrade assistant, if there are issues building or testing the project
after the upgrade.

### Project import runs in parallel

The Studio IDE now imports projects in parallel when you use Gradle 7.4.2 or
higher and Android Gradle plugin 7.2.0 or higher. Specifically, when Android
Studio triggers a Gradle sync, the information that describes projects included
in your build is created in parallel. This usually speeds up the syncing
process, especially for larger projects. Benchmarks show that the time it takes
to build Gradle models for a very large project (with 3,500 Gradle subprojects)
is reduced by 50%, from 10 minutes to 5 minutes.

### Android Gradle plugin targets JVM 11 bytecode

Starting with Android Gradle plugin 7.4.0-alpha04, AGP ships wth JVM 11
bytecode. This means that if you compile against AGP, or write custom Lint
checks, you need to start targeting JVM 11 bytecode. One of the ways to do this
is to include the following in your module-level `build.gradle` file:

    sourceCompatibility = "11"
    targetCompatibility = "11"

### Patch releases

<br />

The following is a list of the patch releases for Android Gradle Plugin
7.4.

<br />

<br />

#### Android Gradle Plugin 7.4.1 (February 2023)

<br />

<br />

This minor update includes the following bug fixes:

<br />

<br />

| Fixed issues ||
|---|---|
| [Issue #242831042](https://issuetracker.google.com/issues/242831042) Migrate from `destination` property to `outputLocation` property to address deprecation warning and prepare for Gradle 9.0 |
| [Issue #261329823](https://issuetracker.google.com/issues/261329823) AGP 7.4.0-rc01 breaks Variant API with "Querying the mapped value of `map(provider(java.util.Set))` before task '...' has completed is not supported" |

<br />