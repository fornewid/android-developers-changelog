---
title: https://developer.android.com/build/releases/gradle-plugin-roadmap
url: https://developer.android.com/build/releases/gradle-plugin-roadmap
source: md.txt
---

The Android Gradle Plugin (AGP) is the supported build system for Android
applications and includes support for compiling many different types of sources
and linking them together into an application that you can run on a physical
Android device or an emulator.

The following section describes the planned evolution of the AGP's DSL and API.
As new APIs are introduced in stable releases, old APIs will be marked as
deprecated. Those deprecated APIs will then become unavailable in the next
stable release. Below you will find information about upcoming changes in each
major AGP release.

For a more detailed log of AGP API deprecations or removals, see the [AGP API
updates](https://developer.android.com/studio/releases/gradle-plugin-api-updates).
| **Note:** The timeframes mentioned below are estimates and are subject to change.

## AGP 9.0 (January 2026)

**New Variant APIs are stable, old APIs are deprecated**

- The [Variant APIs](https://medium.com/androiddevelopers/new-apis-in-the-android-gradle-plugin-f5325742e614) that were incubating in 4.1 and 4.2 are stable.
- All of these interfaces are located in the [`gradle-api`](https://maven.google.com/web/index.html#com.android.tools.build:gradle-api) artifact.
- The previous interfaces and classes used in the old Variant API are now deprecated, and require [explicit opt-in](https://developer.android.com/build/releases/agp-9-0-0-release-notes#android-gradle-plugin-new-dsl) to use.

**New DSL interfaces are stable, old ones are deprecated**

- The [DSL interfaces](https://medium.com/androiddevelopers/new-apis-in-the-android-gradle-plugin-f5325742e614) that were incubating in 4.1, 4.2 and 7.0 are now stable.
- All of these interfaces are located in the `gradle-api` artifact.
- The previous interfaces and classes used in the DSL are now deprecated, and require [explicit opt-in](https://developer.android.com/build/releases/agp-9-0-0-release-notes#android-gradle-plugin-new-dsl) to use.

**Private internal AGP classes still accessible**

Private internal classes from AGP, located in other artifacts, are still
accessible during compilation of build files and plugins, but it is **not**
recommended to use them as they may change in breaking ways at any time.

## AGP 10.0 (late 2026)

**Old APIs are removed**

- All previous interfaces and classes used in the DSL and the old Variant API are **deleted**.
- The `gradle-api` artifact is the only artifact you need to access DSL and variant API interfaces and classes, and should be used when developing plugins.

**(Tentative) Access to private internal AGP classes is removed**

Dependency on the
[`gradle`](https://maven.google.com/web/index.html#com.android.tools.build:gradle)
artifact now hides all internal classes and gives compilation access only to the
interfaces and classes available in the `gradle-api` artifact. This impacts
plugin compilation.

It isn't possible to manually add a dependency to get access to the internal
classes.
| **Important:** We would like your feedback on the removal of internal AGP classes. Please let us know about your use case, including specific examples of what you need access to, by submitting your feedback on this [tracking issue](https://issuetracker.google.com/219002669).