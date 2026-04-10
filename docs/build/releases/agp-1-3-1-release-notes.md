---
title: https://developer.android.com/build/releases/agp-1-3-1-release-notes
url: https://developer.android.com/build/releases/agp-1-3-1-release-notes
source: md.txt
---

<br />

# Android plugin for Gradle, revision 1.3.1 (August 2015)

**Dependencies:**

|   | Minimum version | Default version | Notes |
|---:|:---:|:---:|:---:|
| Gradle | 2.2.1 | 2.2.1 | To learn more, see [updating Gradle](https://developer.android.com/build/releases/gradle-plugin?buildsystem=ndk-build#updating-gradle). |
| SDK Build Tools | 21.1.1 | 21.1.1 | [Install](https://developer.android.com/studio/intro/update#sdk-manager) or [configure](https://developer.android.com/tools/releases/build-tools) SDK Build Tools. |

**General Notes:**

- Fixed the [ZipAlign](https://developer.android.com/tools/help/zipalign) task to properly consume the output of the previous task when using a customized filename.
- Fixed [Renderscript](https://developer.android.com/guide/topics/renderscript/compute) packaging with the [NDK](https://developer.android.com/tools/sdk/ndk).
- Maintained support for the `createDebugCoverageReport` build task.
- Fixed support for customized use of the `archiveBaseName` property in the `build.gradle` build file.
- Fixed the `Invalid ResourceType` [lint](https://developer.android.com/tools/help/lint) warning caused by parameter method annotation lookup when running [lint](https://developer.android.com/tools/help/lint) outside of Android Studio.

<br />