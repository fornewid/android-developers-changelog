---
title: https://developer.android.com/jetpack/androidx/releases/annotation
url: https://developer.android.com/jetpack/androidx/releases/annotation
source: md.txt
---

# Annotation

API Reference  
[androidx.annotation](https://developer.android.com/reference/androidx/annotation/package-summary)  
Expose metadata that helps tools and other developers understand your app's code.


This table lists all the artifacts in the `androidx.annotation` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| annotation | [1.9.1](https://developer.android.com/jetpack/androidx/releases/annotation#1.9.1) | - | - | - |
| annotation-experimental | [1.5.1](https://developer.android.com/jetpack/androidx/releases/annotation#annotation-experimental-1.5.1) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/annotation#annotation-experimental-1.6.0-rc01) | - | - |

This library was last updated on: February 11, 2026

## Declaring dependencies

To add a dependency on Annotation, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.annotation:annotation:1.9.1"
    // To use the Java-compatible @androidx.annotation.OptIn API annotation
    implementation "androidx.annotation:annotation-experimental:1.5.1"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.annotation:annotation:1.9.1")
    // To use the Java-compatible @androidx.annotation.OptIn API annotation
    implementation("androidx.annotation:annotation-experimental:1.5.1")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:459778+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=459778&template=1422649)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.9

### Version 1.9.1

October 30, 2024

`androidx.annotation:annotation-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2e6556166965445a8a129114765a3903c063735c..87b88ad088cc9b18d4ab75611fc8b74e8b01c24a/annotation).

**Bug Fixes**

- Added JS target platform. ([I2310b](https://android-review.googlesource.com/#/q/I2310bf3a1f89064d0d36cea65b4ba91898f49d17))
- Kotlin version update to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))

### Version 1.9.0

October 16, 2024

`androidx.annotation:annotation-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67abb2fb5b5281c063f189eeb9863086f8a206c8..2e6556166965445a8a129114765a3903c063735c/annotation/annotation).

**Important changes since 1.8.0**

- Added support for the following Kotlin Multiplatform targets: `watchosDeviceArm64`, `mingwX64`, `linuxArm64`.

### Version 1.9.0-rc01

October 2, 2024

`androidx.annotation:annotation-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..67abb2fb5b5281c063f189eeb9863086f8a206c8/annotation) since the previous beta.

### Version 1.9.0-beta01

September 18, 2024

`androidx.annotation:annotation-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f1a4862ceeaaa0161261ad24ea72a5430d3090d0..0431b84980e97d6bafdfda7c9038bc4d9529564f/annotation/annotation).

**API Changes**

- Adds support for `watchosDeviceArm64` platform target ([I1cc04](https://android-review.googlesource.com/#/q/I1cc049dcca344226878d2f5a096e4ebb2e8bb5ac), [b/364652024](https://issuetracker.google.com/issues/364652024))

### Version 1.9.0-alpha03

September 4, 2024

`androidx.annotation:annotation-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/c71a0ac68935256ff7027557d5396130c71eb54d..f1a4862ceeaaa0161261ad24ea72a5430d3090d0/annotation/annotation) since the previous alpha.

### Version 1.9.0-alpha02

August 21, 2024

`androidx.annotation:annotation-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5a50de555336ab8cf837fd0ddd32febb2cc85f74..c71a0ac68935256ff7027557d5396130c71eb54d/annotation).

**New Features**

- Adding support for `mingwX64` platform ([I461ca](https://android-review.googlesource.com/#/q/I461cad1935cd2c29aa7eb05f5e6971215292f11c), [b/349894318](https://issuetracker.google.com/issues/349894318))
- Add support for `linuxArm64` kotlin multiplatform target. ([I139d3](https://android-review.googlesource.com/#/q/I139d36226a3d06d9768bd63302de98b576a12a48), [b/338268719](https://issuetracker.google.com/issues/338268719))

### Version 1.9.0-alpha01

June 26, 2024

`androidx.annotation:annotation-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4e5e9e3ddec39fb6f9f34c89b1b4f9b58a1ab627..948119be341fa4affc055418e695d8c4c7e5e2e4/annotation/annotation).

**External Contribution**

- Adds support for `linuxArm64` multiplatform target (thanks to Jake Wharton!)

## Version 1.8

### Version 1.8.2

August 7, 2024

`androidx.annotation:annotation-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c31837541924de174f7b1b14106bc9bc29a0080..5a50de555336ab8cf837fd0ddd32febb2cc85f74/annotation).

**Bug Fixes**

- Adding support for `mingwX64` platform ([I461ca](https://android-review.googlesource.com/#/q/I461cad1935cd2c29aa7eb05f5e6971215292f11c), [b/349894318](https://issuetracker.google.com/issues/349894318))

### Version 1.8.1

July 24, 2024

`androidx.annotation:annotation-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c31837541924de174f7b1b14106bc9bc29a0080/annotation/annotation).

**Bug Fixes**

- Includes additional Kotlin Multiplatform targets: `watchos`, `tvos`.

### Version 1.8.0

May 14, 2024

`androidx.annotation:annotation-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2f0179ef63aef86044266c1445541db90a410052..4e5e9e3ddec39fb6f9f34c89b1b4f9b58a1ab627/annotation/annotation).

**Important changes since 1.7.0**

- Added [`@ReplaceWith`](https://developer.android.com/reference/kotlin/androidx/annotation/ReplaceWith) annotation to express replacements for deprecated APIs
- The `@MainThread` annotation has been moved to the common source set.

### Version 1.8.0-rc01

May 1, 2024

`androidx.annotation:annotation-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..2f0179ef63aef86044266c1445541db90a410052/annotation/annotation) since the prior beta release.

### Version 1.8.0-beta02

April 17, 2024

`androidx.annotation:annotation-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains no changes since the prior release.

### Version 1.8.0-beta01

April 3, 2024

`androidx.annotation:annotation-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8fbefdc70ea49fce9c8f8cfcf80e1fa2122a7ee4..02b55f664eba38e42e362e1af3913be1df552d55/annotation/annotation).

**New Features**

- [`ReplaceWith`](https://developer.android.com/reference/kotlin/androidx/annotation/ReplaceWith) annotation is now API-stable, but the associated lint check with auto-fix has not shipped yet

### Version 1.8.0-alpha02

March 20, 2024

`androidx.annotation:annotation-*:1.8.0-alpha02` is released with no notable changes. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..8fbefdc70ea49fce9c8f8cfcf80e1fa2122a7ee4/annotation/annotation).

### Version 1.8.0-alpha01

February 21, 2024

`androidx.annotation:annotation-*:1.8.0-alpha01` is released. [Version 1.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bff33338af8303e6c2540b14ec3d7960f7f7a15d..e1b82c49c59d8e976ce558aba5586f6c61bc9054/annotation/annotation)

**API Changes**

- Added `@ReplaceWith` annotation to express replacements for deprecated APIs. ([I38db3](https://android-review.googlesource.com/#/q/I38db39789f657e70e962cae2e3360023db50ecb5), [b/322373864](https://issuetracker.google.com/issues/322373864))

**External Contributions**

- Thanks Ivan Matkov for moving the `@MainThread` annotation to the common source set. ([6f228c](https://android-review.googlesource.com/#/q/6f228cd685f996a6d6ad7f757ea6b71b5b248f5d))

## Version 1.7

### Version 1.7.1

December 13, 2023

`androidx.annotation:annotation-*:1.7.1` is released. [Version 1.7.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/100ed06ac4f1452198cbd831d614aa479ff8d470..97bb154d62daa2e34d35c8ccb6f5c02b14fd2323)

**Bug Fixes**

- Use `compile` scope when inserting default platform dependency. ([I4958f](https://android-review.googlesource.com/q/I4958f8350d788611ab874b3e136c57b1acaaf9f1))

### Version 1.7.0

September 6, 2023

`androidx.annotation:annotation-*:1.7.0` is released. [Version 1.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7f02b332becdac55393a5abbd5f2a95fcfed836..7c3e5b10f8d8c65b55fd233b7e32ec0fe19ca78a/annotation/annotation)

**Important changes since 1.6.0**

- Includes Kotlin Multiplatform artifacts targeting iOS, Linux, and MacOS platforms.
- You can now use Annotations in [KMM](https://kotlinlang.org/docs/multiplatform-mobile-getting-started.html) projects. Note that non-Android targets of Annotations are still experimental but we decided to merge versions to make it easier for developers to try them. Specifically, some annotations might move between common and platform specific code during the alpha development as we finalize the boundaries.

### Version 1.7.0-rc01

August 23, 2023

`androidx.annotation:annotation-*:1.7.0-rc01` is released. [Version 1.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..f7f02b332becdac55393a5abbd5f2a95fcfed836/annotation/annotation)

This release does not contain any changes from the prior beta.

### Version 1.7.0-beta01

August 9, 2023

`androidx.annotation:annotation-*:1.7.0-beta01` is released. [Version 1.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1467250e415aa65b25534031c5f4b9b2118d7625..5d7dd999525725bd038a00ca4e89e0fef624a6da/annotation/annotation)

**New Features**

- Stabilized APIs for release

### Version 1.7.0-alpha03

July 26, 2023

`androidx.annotation:annotation-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22b70bebd89f109ec8a21cb84c21f37240124cfd..1467250e415aa65b25534031c5f4b9b2118d7625/annotation/annotation)

**Bug Fixes**

- Maven POM publication now includes default JVM-targeted multiplatform artifact as dependency

### Version 1.7.0-alpha02

March 24, 2023

`androidx.annotation:annotation-*:1.7.0-alpha02` is released.

**Bug Fixes**

- Removed dependency constraints from Maven artifacts to workaround a build problem in Kotlin Native Targets ([b/274786186](https://issuetracker.google.com/issues/274786186), [KT-57531](https://youtrack.jetbrains.com/issue/KT-57531)).

### Version 1.7.0-alpha01

March 22, 2023

`androidx.annotation:annotation-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7c0dba3c01588fa781e827cfd1547c38609205c2..8ded11092287e280a40fc35b7eede22664ac5641/annotation/annotation)

**New Features**

- Includes Kotlin Multiplatform artifacts targeting iOS, Linux, and MacOS platforms.
- You can now use Annotations in [KMM](https://kotlinlang.org/docs/multiplatform-mobile-getting-started.html) projects. Note that non-Android targets of Annotations are still experimental but we decided to merge versions to make it easier for developers to try them. Specifically, some annotations might move between common and platform specific code during the alpha development as we finalize the boundaries.

## Version 1.6

### Version 1.6.0

February 22, 2023

`androidx.annotation:annotation:1.6.0` and `androidx.annotation:annotation-jvm:1.6.0` are released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f4599a281a0f80775ef6beb97660957cd309b52a..78ea23e83d70119f89575914144a10e246789b1d/annotation/annotation)

**Important changes since 1.5.0**

- Adds a `@RequiresExtension` annotation to express that an API requires a particular version of a particular extension SDK ([I5e4fe](https://android-review.googlesource.com/#/q/I5e4fe555335f70bc21f8c8a4ecabdcd74d25bf25))
- Converted annotation library to build using the Kotlin Multiplatform toolchain ([I3be8d](https://android-review.googlesource.com/#/q/I3be8df187a8f60ad28c0ee8865ab748cafda4c9a))

### Version 1.6.0-rc01

February 8, 2023

`androidx.annotation:annotation:1.6.0-rc01` and `androidx.annotation:annotation-jvm:1.6.0-rc01` are released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7b6c2215d383930f0516bcd90c7d704fec6abd5b..f4599a281a0f80775ef6beb97660957cd309b52a/annotation)

- Annotation has been stabilized for release candidate 1.6.0-rc01.

### Version 1.6.0-beta01

January 25, 2023

`androidx.annotation:annotation:1.6.0-beta01` and `androidx.annotation:annotation-jvm:1.6.0-beta01` are released with no changes from `1.6.0-alpha01`.

### Version 1.6.0-alpha01

January 11, 2023

`androidx.annotation:annotation-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a0de5bf507b3e680c32348d907eef6f4dbcfe65/annotation)

### Version 1.6.0-dev01

February 8, 2023

`androidx.annotation:annotation-*:1.6.0-dev01` is released. [Version 1.6.0-dev01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7c0dba3c01588fa781e827cfd1547c38609205c2/annotation/annotation)

- Annotation has enabled Kotlin multi-platform for developer preview 1.6.0-dev01.

**New Features**

- Adds a `@RequiresExtension` annotation to express that an API requires a particular version of a particular extension SDK. ([I5e4fe](https://android-review.googlesource.com/#/q/I5e4fe555335f70bc21f8c8a4ecabdcd74d25bf25))
- Converted annotation library to build using the Kotlin Multiplatform toolchain ([I3be8d](https://android-review.googlesource.com/#/q/I3be8df187a8f60ad28c0ee8865ab748cafda4c9a))

## Version 1.5.0

### Version 1.5.0

September 21, 2022

`androidx.annotation:annotation:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ff9030bbacf23c63ddcaebc04246af0251eb74b2..8d30752c5370497e2cf7560560fd383fed1b2de8/annotation/annotation)

**Important changes since 1.4.0**

- Annotation library has been fully migrated to Kotlin sources, resulting in support for Kotlin-specific target use sites and other Kotlin-compatible annotation features.

### Version 1.5.0-rc01

September 7, 2022

`androidx.annotation:annotation:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/580b321a1e2ab247096eee6b2c7f65b12ee042c4..ff9030bbacf23c63ddcaebc04246af0251eb74b2/annotation/annotation)

- No changes from previous 1.5.0 beta release.

### Version 1.5.0-beta01

August 24, 2022

`androidx.annotation:annotation:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..580b321a1e2ab247096eee6b2c7f65b12ee042c4/annotation/annotation)

- No changes from previous release. API surface has been frozen for beta.

### Version 1.5.0-alpha02

August 10, 2022

`androidx.annotation:annotation:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/annotation/annotation)

- No changes since the previous alpha release.

### Version 1.5.0-alpha01

July 27, 2022

`androidx.annotation:annotation:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d0a827d2d2415ef04c0c9538af087321d1fc58d8..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/annotation/annotation)

**New Features**

- Annotation library has been fully migrated to Kotlin sources, resulting in support for Kotlin-specific target use sites and other Kotlin-compatible annotation features.

## Version 1.4.0

### Version 1.4.0

June 15, 2022

`androidx.annotation:annotation:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c8fdb47aa3e1bb0f108b7e8dabb71ea66d06f2f9..d0a827d2d2415ef04c0c9538af087321d1fc58d8/annotation/annotation)

**Important changes since 1.3.0**

- `@RestrictTo` has been migrated to Kotlin sources and now supports `@file` usage site. As a result, the Annotation library now depends on the Kotlin standard library.
- `@ReturnThis` (b/140249763): Ensures that overriding methods of this method must return the same instance (intended for builders etc)
- `@OpenForTesting` (b/141539024): Kotlin classes and methods marked "open" can be annotated with this annotation, and lint will make sure that this class is only subclassed (and methods only overridden) from unit tests
- `@DeprecatedSinceApi` (b/37116481): Indicates that the annotated method (or class or field) is part of a backport library for a platform API, which is no longer needed as of the given API level.
- `@EmptySuper`: Indicates that this method is defined to be empty, so when overriding you do not need to call it (and in fact you shouldn't; for example, it can contain backwards compatibility checking.)

### Version 1.4.0-rc01

June 1, 2022

`androidx.annotation:annotation:1.4.0-rc01` is released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/59f5332a9fc2dc4bae1733a97b9518103d068d19..c8fdb47aa3e1bb0f108b7e8dabb71ea66d06f2f9/annotation/annotation)

- API surface and functionality have been finalized for release.

### Version 1.4.0-beta01

May 18, 2022

`androidx.annotation:annotation:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..59f5332a9fc2dc4bae1733a97b9518103d068d19/annotation/annotation)

- No changes since the last alpha. API surface has been locked down for Beta release.

### Version 1.4.0-alpha02

February 9, 2022

`androidx.annotation:annotation:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..db2ecbef194afcddfaede22e1d884a8959a9277c/annotation/annotation)

**New Features**

- Added `@ReturnThis`, `@OpenForTesting`, `@EmptySuper` and `@DeprecatedSinceApi` annotations. ([21946a2](https://android-review.googlesource.com/#/q/I33e85ff4bed137b61b4f264d1993633dcd1a7015))

- `@ReturnThis` ([b/140249763](https://issuetracker.google.com/issues/140249763)): Ensures that overriding methods of this method must return the same instance (intended for builders etc)

- `@OpenForTesting` ([b/141539024](https://issuetracker.google.com/issues/141539024)): Kotlin classes and methods marked "open" can be annotated with this annotation, and lint will make sure that this class is only subclassed (and methods only overridden) from unit tests

- `@DeprecatedSinceApi` ([b/37116481](https://issuetracker.google.com/issues/37116481)): Indicates that the annotated method (or class or field) is part of a backport library for a platform API, which is no longer needed as of the given API level.

- `@EmptySuper`: Indicates that this method is defined to be empty, so when overriding you do not need to call it (and in fact you shouldn't; for example, it can contain backwards compatibility checking.)

### Version 1.4.0-alpha01

December 15, 2021

`androidx.annotation:annotation:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cbe56bb68421125805e82cc6ecb60a7701518e07..301586664b5aad60548f21866cad502d524dbf9f/annotation/annotation)

**API Changes**

- Migrated `RestrictTo` annotation to Kotlin sources ([Ia6336](https://android-review.googlesource.com/#/q/Ia6336418ab834ab1666ce2d56f108706b6ac1498))

## Version 1.3.0

### Version 1.3.0

November 3, 2021

`androidx.annotation:annotation:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c38bf8cba2f6d60f9cceb03adcb56ff57f793b27..cbe56bb68421125805e82cc6ecb60a7701518e07/annotation/annotation)

**Important changes since 1.2.0**

- `@Discouraged` annotation for marking APIs that cannot be reasonably deprecated but have significant negative performance impact and should not be called in normal production code
- `@Context` annotation to mark generic Contexts so that developers can migrate to new APIs more easily
- `@GravityInt` annotation for marking elements containing gravity values packed into integers
- Deprecated `@InspectableProperty` in favor of `@Attribute` for `androidx.resourceinspection`

### Version 1.3.0-rc01

October 27, 2021

`androidx.annotation:annotation:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..c38bf8cba2f6d60f9cceb03adcb56ff57f793b27/annotation/annotation)

### Version 1.3.0-beta01

September 29, 2021

`androidx.annotation:annotation:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/annotation/annotation)

**API Changes**

- Require explanation in 'message' for @Discouraged. ([I3390f](https://android-review.googlesource.com/#/q/I3390f4682fb583fcc38feaa00577a45dbb0d14e6))
- Adding @Discouraged annotation for marking elements that are discouraged. ([Ib2549](https://android-review.googlesource.com/#/q/Ib2549fc20843a13384fa74befc2f733e61549253))
- Make the RestrictTo annotation visible from Studio docs popup ([Ie8e1a](https://android-review.googlesource.com/#/q/Ie8e1a8ce27aca13319b0f02726050b11c8415f77), [b/183134648](https://issuetracker.google.com/issues/183134648))

**Bug Fixes**

- Add Context annotation to mark generic Contexts, so developers can migrate to new APIs more easily. ([Ie581a](https://android-review.googlesource.com/#/q/Ie581abf2bd48eb2120cced5f4592d4344591cf28))

### Version 1.3.0-alpha01

March 24, 2021

`androidx.annotation:annotation:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1eb7d82174683e4f49dfc1ad1a6a085767a40410..5c42896eb6591b09e3952030fb7ea8d9b8c42713/annotation/annotation)

**API Changes**

- Deprecated `@InspectableProperty` in favor of `@Attribute` in `androidx.resourceinspection`. ([Ic0eff](https://android-review.googlesource.com/#/q/Ic0eff8463bacf8efb21c2dfe90e136849b8ef26f))
- Added `@GravityInt` annotation for marking elements containing gravity values packed into integers. ([Ifcaa4](https://android-review.googlesource.com/#/q/Ifcaa4ad1df11c767b1060bcfcf2debeb9b1a666f), [b/180620048](https://issuetracker.google.com/issues/180620048))

## Annotation-Experimental Version 1.6

### Version 1.6.0-rc01

February 11, 2026

`androidx.annotation:annotation-experimental:1.6.0-rc01` is released. Version 1.6.0-rc01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..9bc7aecc488a90940bced04fce3ff47f80f09cf7/annotation/annotation-experimental) since the prior beta release.

### Version 1.6.0-alpha01

October 22, 2025

`androidx.annotation:annotation-experimental:1.6.0-alpha01` is released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af0b67cea9da3f8e8139ee5856040fb5bb47bd72..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/annotation/annotation-experimental).

**API Changes**

- The `OptIn` annotation now supports the `ElementType.PARAMETER` target.

## Annotation-Experimental Version 1.5

### Version 1.5.1

July 16, 2025

`androidx.annotation:annotation-experimental:1.5.1` is released. Version 1.5.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dccd20efaf4df6424d5d73527bb84f396b69ff2d..af0b67cea9da3f8e8139ee5856040fb5bb47bd72/annotation/annotation-experimental).

### Version 1.5.0

May 7, 2025

`androidx.annotation:annotation-experimental:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d0c1307893e9154be53313000d28149a45174387..dccd20efaf4df6424d5d73527bb84f396b69ff2d/annotation/annotation-experimental).

**Important changes since 1.4.0**

- Added `message` to `RequiresOptIn` to match the Kotlin stdlib annotation with default empty string value. ([I1f50e](https://android-review.googlesource.com/#/q/I1f50e2259d75e1d14f5320d21c91cb8fbc2e1609))
- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.5.0-rc01

April 23, 2025

`androidx.annotation:annotation-experimental:1.5.0-rc01` is released. Version 1.5.0-rc01 contains no changes since the previous beta release, see [commits](https://android.googlesource.com/platform/frameworks/support/+log/4c37298a97c16270c139eb812ddadaba03e23a52..d0c1307893e9154be53313000d28149a45174387/annotation/annotation-experimental).

### Version 1.5.0-beta01

April 9, 2025

`androidx.annotation:annotation-experimental:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c71a0ac68935256ff7027557d5396130c71eb54d..4c37298a97c16270c139eb812ddadaba03e23a52/annotation/annotation-experimental).

**Important changes**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.5.0-alpha01

August 21, 2024

`androidx.annotation:annotation-experimental:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cb993e8594b035615bb12e0cb8294769eb7c10d1..c71a0ac68935256ff7027557d5396130c71eb54d/annotation/annotation-experimental).

**API Changes**

- Add `message` to `RequiresOptIn` to match the Kotlin stdlib annotation with default empty string value. ([I1f50e](https://android-review.googlesource.com/#/q/I1f50e2259d75e1d14f5320d21c91cb8fbc2e1609))

## Annotation-Experimental Version 1.4

### Version 1.4.1

April 3, 2024

`androidx.annotation:annotation-experimental:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d25969e764bee00b0d8bb519bdd1487ef71e94de..cb993e8594b035615bb12e0cb8294769eb7c10d1/annotation/annotation-experimental).

**Bug Fixes**

- Fix usage of `isKotlin` to avoid accidentally triggering `RequiresOptIn` check in Kotlin files. ([I2d8c1f](https://android-review.googlesource.com/q/I2d8c1f5b4425bd042cff6552e6a8c45c9905c2b3))

### Version 1.4.0

January 24, 2024

`androidx.annotation:annotation-experimental:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b23f311a4abd047c9b02d5585e80ac7884c1967f..d25969e764bee00b0d8bb519bdd1487ef71e94de/annotation/annotation-experimental)

**Important changes since 1.3.0**

- Add support for Kotlin multi-platform
- Fix compatibility with Kotlin 2.0
- Show warnings for Java usages of experimentally-annotated Kotlin properties ([I8bd43](https://android-review.googlesource.com/#/q/I8bd43b972619c8622a7d57e923951079712b9ace))
- Fix placement of autofix annotation on Kotlin methods ([Id7a41](https://android-review.googlesource.com/#/q/Id7a41679a7262c63c1e4c2f59fd8394283963785))

### Version 1.4.0-rc01

January 10, 2024

`androidx.annotation:annotation-experimental:1.4.0-rc01` is released. Version 1.4.0-rc01 contains no changes since the previous release.

### Version 1.4.0-beta01

December 13, 2023

`androidx.annotation:annotation-experimental:1.4.0-beta01` is released. There are no changes since the previous release.

### Version 1.4.0-alpha01

November 29, 2023

`androidx.annotation:annotation-experimental:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7c0dba3c01588fa781e827cfd1547c38609205c2..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/annotation/annotation-experimental)

**Bug Fixes**

- Temporarily remove class-level autofix suggestions to work around [b/301598518](http://b/301598518). ([Id98b2](https://android-review.googlesource.com/#/q/Id98b2281c79ebd842e8585f9fc04d2286e5001de))
- Show warnings for Java usages of experimentally-annotated Kotlin properties ([I8bd43](https://android-review.googlesource.com/#/q/I8bd43b972619c8622a7d57e923951079712b9ace))
- Fix placement of autofix annotation on Kotlin methods ([Id7a41](https://android-review.googlesource.com/#/q/Id7a41679a7262c63c1e4c2f59fd8394283963785))

### Version 1.4.0-dev01

February 8, 2023

`androidx.annotation:annotation-experimental:1.4.0-dev01` is released. [Version 1.4.0-dev01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f8300b4e1477f08c1afcc8f8934161775573b395..7c0dba3c01588fa781e827cfd1547c38609205c2/annotation/annotation-experimental)

- Annotation-experimental has enabled Kotlin multi-platform for developer preview 1.4.0-dev01.

## Annotation-Experimental Version 1.3.1

### Version 1.3.1

June 21, 2023

`androidx.annotation:annotation-experimental:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f8300b4e1477f08c1afcc8f8934161775573b395..c4344de87983c44f9ae3fdfb235801f65ac42830/annotation/annotation-experimental)

**Bug Fixes**

- Place annotation at the beginning of the modifier list when applying lint auto-fix. ([b/251172715](https://issuetracker.google.com/issue?id=251172715))
- Use lint check to discourage use of `androidx.annotation.RequiresOptIn` in Kotlin sources ([b/241097743](https://issuetracker.google.com/issue?id=241097743))

## Annotation-Experimental Version 1.3.0

### Version 1.3.0

September 7, 2022

`androidx.annotation:annotation-experimental:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdc62408ca3c1344b0c9d9162154ec059263f6b7..f8300b4e1477f08c1afcc8f8934161775573b395/annotation/annotation-experimental)

**Important changes since 1.2.0**

- Add support for package-level use of `@androidx.annotation.OptIn` ([I24d58](https://android-review.googlesource.com/#/q/I24d58185bc3e1d74d34b308b2cd314c099c63354))
- Moved Kotlin stdlib dependency to API-type, rather than compile-only. This means all clients of the Annotation-Experimental library will include the Kotlin standard library in their transitive dependencies.

### Version 1.3.0-rc01

August 24, 2022

`androidx.annotation:annotation-experimental:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..bdc62408ca3c1344b0c9d9162154ec059263f6b7/annotation/annotation-experimental)

- No changes from the previous release. Implementation has been frozen for RC.

### Version 1.3.0-beta01

August 10, 2022

`androidx.annotation:annotation-experimental:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/annotation/annotation-experimental)

- No changes from alpha. This library has been stabilized for beta release.

### Version 1.3.0-alpha01

July 27, 2022

`androidx.annotation:annotation-experimental:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5fcdb6c1747f45ab947850fb8b97b77e78dca09c..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/annotation/annotation-experimental)

**API Changes**

- Add support for package-level use of `@androidx.annotation.OptIn` ([I24d58](https://android-review.googlesource.com/#/q/I24d58185bc3e1d74d34b308b2cd314c099c63354))

## Annotation-Experimental Version 1.2.0

### Version 1.2.0

December 15, 2021

`androidx.annotation:annotation-experimental:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3fb4e62996bb3b5696c6c0eec850a915e6c2d23f..5fcdb6c1747f45ab947850fb8b97b77e78dca09c/annotation/annotation-experimental)

**Important changes since 1.1.0**

This library is now targeting Java 8 language level.

### Version 1.2.0-rc01

December 1, 2021

`androidx.annotation:annotation-experimental:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..3fb4e62996bb3b5696c6c0eec850a915e6c2d23f/annotation/annotation-experimental)

No changes from beta.

### Version 1.2.0-beta01

November 17, 2021

`androidx.annotation:annotation-experimental:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..cc1240d00b28657ee0c1a937f60430eaf1b03b09/annotation/annotation-experimental)

**API Changes**

APIs have been finalized for beta.

### Annotation-Experimental Version 1.2.0-alpha01

June 30, 2021

`androidx.annotation:annotation-experimental:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b3c87f0d84c9d910b5458fe784e71d195d431509..19ae3a88ff0824d615355b492cb56049e16991f2/annotation/annotation-experimental)

**New Features**

- Library is now targeting Java 8 language level

## Version 1.2.0

### Version 1.2.0

March 24, 2021

`androidx.annotation:annotation:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1eb7d82174683e4f49dfc1ad1a6a085767a40410..733fe826e7dadc17467ed3aabe6b724c1d14d704/annotation/annotation)

**Major changes since 1.1.0**

- Added `@ChecksSdkIntAtLeast` annotation, which can be used to identify methods or fields used to gate access on SDK level and satisfy the `NewApi` lint check.
- Added `@DoNotInline` annotation, which is paired with a Proguard rule to prevent members from being inlined during optimization.
- A variety of annotations are now annotated with `@Documented` to ensure they show up in documentation for annotated members.

### Version 1.2.0-rc01

February 24, 2021

`androidx.annotation:annotation:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..1eb7d82174683e4f49dfc1ad1a6a085767a40410/annotation/annotation)

### Version 1.2.0-beta01

January 13, 2021

`androidx.annotation:annotation:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/56da5579c165464d278289e593d73d48571b9510..6207afb1646d302c5d29c2c67d332b48db87fb27/annotation/annotation)

**API Changes**

- New `@DoNotInline` annotation which instructs code optimizers (e.g. Proguard, R8) to not inline the annotated method. ([I3dfe8](https://android-review.googlesource.com/#/q/I3dfe8732c062e500b19d1cf2e3812389c7fc3cca), [b/141326133](https://issuetracker.google.com/issues/141326133))

### Version 1.2.0-alpha01

May 14, 2020

`androidx.annotation:annotation:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2f634eec2143acd6a4ea19a375a6e3877cdcc2ed..56da5579c165464d278289e593d73d48571b9510/annotation/annotation)

**New Features**

- Added `@ChecksSdkIntAtLeast` annotation. This let's androidx and users annotate methods and fields that represent an `SDK_INT` check. ([I89a54](https://android-review.googlesource.com/#/q/I89a5407693458796a6f67446ad107a82dbe47329), [b/120255046](https://issuetracker.google.com/issues/120255046))

## Annotation-Experimental Version 1.1.0

### Version 1.1.0

April 7, 2021

`androidx.annotation:annotation-experimental:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/733fe826e7dadc17467ed3aabe6b724c1d14d704..b3c87f0d84c9d910b5458fe784e71d195d431509/annotation/annotation-experimental)

**Major changes since 1.0.0**

- Jetpack's experimental annotations have been rewritten in Kotlin to provide support for multiple marker classes and improved handling of deprecation.
- `RequiresOptIn` and `OptIn` annotations have been added for parity with Kotlin, and the `Experimental` and `UsesExperimental` annotations have been deprecated.

### Version 1.1.0-rc02

March 24, 2021

`androidx.annotation:annotation-experimental:1.1.0-rc02` is released. [Version 1.1.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1eb7d82174683e4f49dfc1ad1a6a085767a40410..733fe826e7dadc17467ed3aabe6b724c1d14d704/annotation/annotation-experimental)

**Bug Fixes**

- Added Proguard rules to ensure that code optimization does not warn about missing Kotlin meta-annotations.

### Version 1.1.0-rc01

March 10, 2021

`androidx.annotation:annotation-experimental:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..1eb7d82174683e4f49dfc1ad1a6a085767a40410/annotation/annotation-experimental)

No changes since prior beta release.

### Version 1.1.0-beta01

January 27, 2021

`androidx.annotation:annotation-experimental:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..aee18b103203a91ee89df91f0af5df2ecff356d6/annotation/annotation-experimental)

**API Changes**

- The androidx variant of the Experimental annotation has been deprecated to provide parity with Kotlin. It has been replaced by an androidx variant of the RequiresOptIn annotation, and the Java-facing linter has been updated to support both the new Kotlin annotation and the new androidx variant. ([I52495](https://android-review.googlesource.com/#/q/I52495721777cf9d2243a825fc491e59c031d2e96), [b/151331381](https://issuetracker.google.com/issues/151331381))

### Version 1.1.0-alpha01

July 22, 2020

`androidx.annotation:annotation-experimental:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc95e7591c5f430294f92000124c313841aca40e..9f60cc700129e30cee9df020005c317fb39d32ec/annotation/annotation-experimental)

**New Features**

- Experimental annotation library is now written in Kotlin, but does not require the Kotlin standard library to be included as a dependency. It includes a Proguard file that allows unnecessary Kotlin metadata to be stripped from projects that only use the Java programming language.
- `@UseExperimental` now supports multiple marker classes ([aosp/1185577](https://android-review.googlesource.com/1185577), [b/145137892](https://issuetracker.google.com/145137892))

## Annotation-Experimental Version 1.0.0

### Annotation-Experimental Version 1.0.0

November 7, 2019

`androidx.annotation:annotation-experimental:1.0.0` and `androidx.annotation:annotation-experimental-lint:1.0.0` is released with no changes since `1.0.0-rc01`. [Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0bc38a30ea2471d0866c80859ed7fa94e664f461..cc95e7591c5f430294f92000124c313841aca40e/annotation).

**Major features of 1.0.0**

- Lint-based enforcement of Kotlin `@Experimental` semantics in Java source code
- Java annotations that provide equivalent behavior to Kotlin's `@Experimental` and `@UseExperimental` annotations without the need for a dependency on Kotlin

### Annotation-Experimental Version 1.0.0-rc01

October 23, 2019

`androidx.annotation:annotation-experimental:1.0.0-rc01` and `androidx.annotation:annotation-experimental-lint:1.0.0-rc01` are released. [Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/400408ab67b8b2dc8df47dacc7456fccc303bdd0..0bc38a30ea2471d0866c80859ed7fa94e664f461/annotation).

**Known issues**

When using Studio 3.5 stable, warnings from the `@Experimental` usage lint detector are not displayed in the IDE for invalid Java usages of Kotlin `@Experimental` annotation. See [b/140640322](https://issuetracker.google.com/issues/140640322).

### Annotation-Experimental Version 1.0.0-beta01

October 9, 2019

`androidx.annotation:annotation-experimental:1.0.0-beta01` and `androidx.annotation:annotation-experimental-lint:1.0.0-beta01` are released with no changes since version `1.0.0-alpha01`. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd1aae0250ae03f6383bf4fd28a60036778bb509..400408ab67b8b2dc8df47dacc7456fccc303bdd0/annotation).

### Annotation-Experimental Version 1.0.0-alpha01

September 18, 2019

`androidx.annotation:annotation-experimental:1.0.0-alpha01` and `androidx.annotation:annotation-experimental-lint:1.0.0-alpha01` are released. These are the [commits included in annotation-experimental `1.0.0-alpha01`](https://android.googlesource.com/platform/frameworks/support/+log/571d7a890c8b1e90e9f4db8f783380a928da3624..cd1aae0250ae03f6383bf4fd28a60036778bb509/annotation/annotation-experimental) and these are the [commits included in annotation-experimental-lint `1.0.0-alpha01`](https://android.googlesource.com/platform/frameworks/support/+log/571d7a890c8b1e90e9f4db8f783380a928da3624..55024edf8c790a12afe31ed7729acf895b895034/annotation/annotation-experimental-lint)
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**New features**

- The Jetpack Experimental annotation library provides a Java-compatible implementation of Kotlin's [experimental API markers](https://kotlinlang.org/docs/reference/experimental.html). The `-lint` artifact provides a Lint-based implementation of experimental usage restrictions and enforces restrictions on Java usages of Kotlin's native experimental API markers.

- When using the `annotation-experimental` artifact as a dependency, the Lint rules provided by the `annotation-experimental-lint` artifact will be enforced automatically.

## Version 1.1.0

### Version 1.1.0

June 5, 2019

`androidx.annotation:annotation:1.1.0` is released with no changes from 1.1.0-rc01.

### Version 1.1.0-rc01

May 7, 2019

`androidx.annotation:annotation:1.1.0-rc01` is released with no changes from `1.1.0-beta01`. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/d0c85eb6e595cfd4383ef345e97e1b8d6acd0a44..baca2b5c73982f26b5630b87ff7dbf25622bbafc/activity).

### Version 1.1.0-beta01

April 3rd, 2019

`androidx.annotation:annotation:1.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/091eca9ac5e20c1346e4c1fdace7b63721f9ce43..2f634eec2143acd6a4ea19a375a6e3877cdcc2ed/annotations).
| **Note:** this version of Annotation is incompatible with Activity 1.0.0-alpha04 and 1.0.0-alpha05 as well as Fragment 1.1.0-alpha04 and 1.1.0-alpha05. Please upgrade to Activity 1.0.0-alpha06 and Fragment 1.1.0-alpha06, respectively.

**New features**

- New `@InspectableProperty`annotation to support the new view inspection APIs added in Android 10. This annotation can be applied to getters on views or other UI elements. Code generation tools may use it to create companion objects that map property names and attribute IDs to property values without the overhead of reflection.

**API changes**

- Breaking change: `@ContentView` has been changed to a constructor annotation and the `@LayoutRes` value has been removed. Classes wishing to support `@ContentView` annotations should add this annotation to a constructor that takes a `@LayoutRes int` parameter. This fixes an issue when using this annotation in library modules. ([b/128352521](https://issuetracker.google.com/issues/128352521))

### Version 1.1.0-alpha02

March 13, 2019

`androidx.annotation:annotation:1.1.0-alpha02` is released. The full list of commits included
in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/941836d33391459696e51b18c08a08f0441eb216..091eca9ac5e20c1346e4c1fdace7b63721f9ce43/annotations).

**New features**

- New API restriction scope: `RestrictTo.Scope.LIBRARY_GROUP_PREFIX`. It restricts usage to code within packages whose groups share the same library group prefix up to the last `.` (period). For example, because libraries `foo.bar:lib1` and `foo.baz:lib2` share the prefix `foo`, they can use each other's APIs that are restricted to this scope. Similarly, for `com.foo.bar:lib1` and `com.foo.baz:lib2` share the `com.foo.` prefix and can share APIs restricted to that scope. Library `com.bar.qux:lib3` however will not be able to use the restricted API because it only shares the prefix `com.` and not all the way until the last `.` (period).

### Version 1.1.0-alpha01

January 30, 2019

`androidx.annotation:annotation 1.1.0-alpha01` is released.

**New features**

- Added a `@ContentView` annotation that allows you to indicate which layout XML file should be inflated. This is supported in `ComponentActivity` in its `1.0.0-alpha04` and `Fragment` in its `1.1.0-alpha04` release as an alternative to using `setContentView()` or overriding `onCreateView()`, respectively. ([aosp/837619](https://android-review.googlesource.com/837619))

## Version 1.0.2

### Version 1.0.2

February 25, 2019

`androidx.annotation:annotation 1.0.2` is released.

**Bug fixes**

- Correct the R8/ProGuard rules which are embedded in the jar. These were incorrectly referencing the old `android.support.annotation` types instead of `androidx.annotation`. Note: This would have only had an impact on your builds if you were not using `getDefaultProguardFile` as those default rules also included correct rules for both packages. ([aosp/891685](https://android-review.googlesource.com/891685/))
- Add a R8/ProGuard rule which explicitly keeps the @Keep annotation itself. This ensures that ProGuard does not remove the annotation from types prior to actually honoring its semantics. Note: This would have only had an impact on your builds if you were not using `getDefaultProguardFile` as those default rules also included correct rules for both packages. ([aosp/903818](https://android-review.googlesource.com/903818/))