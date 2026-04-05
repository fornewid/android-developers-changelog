---
title: https://developer.android.com/jetpack/androidx/releases/startup
url: https://developer.android.com/jetpack/androidx/releases/startup
source: md.txt
---

# Startup

# Startup

[User Guide](https://developer.android.com/topic/libraries/app-startup)  
API Reference  
[androidx.startup](https://developer.android.com/reference/kotlin/androidx/startup/package-summary)  
Implement a straightforward, performant way to initialize components at app startup.  

|   Latest Update    |                                 Stable Release                                 | Release Candidate | Beta Release | Alpha Release |
|--------------------|--------------------------------------------------------------------------------|-------------------|--------------|---------------|
| September 18, 2024 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/startup#1.2.0) | -                 | -            | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:823348+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=823348&template=1400167)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.0

September 18, 2024

`androidx.startup:startup-runtime:1.2.0`is released. Version 1.2.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/627188fdf1cf1902c1713b50c00265575de938ef..2bbbb9ffed2413b31a95f0fa838532db5b541e2e/startup/startup-runtime).

**Important changes since 1.1.0**

- Fixes metadata lookup when the`InitializationProvider`is defined for secondary processes. ([Id9ff1](https://android.googlesource.com/platform/frameworks/support/+/6cab291c428e631adcd3154ef384b6307f17748c))
- Fixed a bug in`AppInitializer.isEagerlyInitialized()`. ([I99e9a](https://android-review.googlesource.com/c/platform/frameworks/support/+/1855769))

### Version 1.2.0-rc01

September 4, 2024

`androidx.startup:startup-runtime:1.2.0-rc01`is released with no changes from the last beta release. Version 1.2.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b2638e1bfd54531dae1f04b33829101af8bf350..627188fdf1cf1902c1713b50c00265575de938ef/startup/startup-runtime).

### Version 1.2.0-beta01

August 21, 2024

`androidx.startup:startup-runtime:1.2.0-beta01`is released. Version 1.2.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..6b2638e1bfd54531dae1f04b33829101af8bf350/startup/startup-runtime).

**New Features**

- Added explicit`ProfileInstaller`dependency to support baseline profile installation fallback when profiles not installed by play.

### Version 1.2.0-alpha02

January 11, 2023

`androidx.startup:startup-runtime:1.2.0-alpha02`is released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..adf1c279a86ab3886e1666c08e2c3efba783367b/startup/startup-runtime)

**Bug Fixes**

- Fixes metadata lookup when the`InitializationProvider`is defined for secondary processes. ([aosp/2012215](https://android.googlesource.com/platform/frameworks/support/+/6cab291c428e631adcd3154ef384b6307f17748c))

### Version 1.2.0-alpha01

February 9, 2022

`androidx.startup:startup-runtime:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c/startup/startup-runtime)

**Bug Fixes**

- Fixed a bug in`AppInitializer.isEagerlyInitialized()`.[aosp/1855769](https://android-review.googlesource.com/c/platform/frameworks/support/+/1855769)

## Version 1.1.1

### Version 1.1.1

February 9, 2022

`androidx.startup:startup-runtime:1.1.1`is released.[Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aea86511661df6f9895d38bab5053a80d15f24c4..8337e0c05174a73ea6db825b680f461c33144bf4/startup/startup-runtime)

**Bug Fixes**

- Fixed a bug in`AppInitializer.isEagerlyInitialized()`.[aosp/1855769](https://android-review.googlesource.com/c/platform/frameworks/support/+/1855769)

## Version 1.1.0

### Version 1.1.0

August 4, 2021

`androidx.startup:startup-runtime:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/436aaeb1688cb1a3dd5f07e7cde763abd5f2761f..aea86511661df6f9895d38bab5053a80d15f24c4/startup/startup-runtime)

This release is identical to`androidx.startup:startup-runtime:1.1.0-rc01`.

**Important changes since 1.0.0**

- Multiple`InitializationProvider``<provider>`elements can now be added to the application's AndroidManifest.xml for libraries or applications that require automatic initialization in multiple processes.[Ia0712](https://android-review.googlesource.com/#/q/Ia07123fcae20f7bdfc9b9f38830d84134fb8d3d4),[b/183136596](https://issuetracker.google.com/issues/183136596)

- Better proguard rules, multi-dex rules to ensure`Initializer`s end up in the primary dex file.[aosp/1743740](https://android-review.googlesource.com/c/platform/frameworks/support/+/1743740)

- Add baseline profile rules to optimize the use of`androidx.startup`.[aosp/17639340](https://android-review.googlesource.com/c/platform/frameworks/support/+/1763934)

### Version 1.1.0-rc01

July 21, 2021

`androidx.startup:startup-runtime:1.1.0-rc01`is released.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/66681ad83c328d0dd821b943bb3d375f02c1db61..436aaeb1688cb1a3dd5f07e7cde763abd5f2761f/startup/startup-runtime)

**Bug Fixes**

- Better proguard rules, multi-dex rules to ensure`Initializer`s end up in the primary dex file. ([aosp/1743740](https://android-review.googlesource.com/c/platform/frameworks/support/+/1743740))
- Add baseline profile rules to optimize the use of`androidx.startup`. ([aosp/1763934](https://android-review.googlesource.com/c/platform/frameworks/support/+/1763934)0

### Version 1.1.0-beta01

May 18, 2021

`androidx.startup:startup-runtime:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24330de8135d689b34a31a701181b20549e8db25..66681ad83c328d0dd821b943bb3d375f02c1db61/startup/startup-runtime)

**New Features**

- Multiple`InitializationProvider``<provider>`elements can now be added to the application's AndroidManifest.xml for libraries or applications that require automatic initialization in multiple processes. ([Ia0712](https://android-review.googlesource.com/#/q/Ia07123fcae20f7bdfc9b9f38830d84134fb8d3d4),[b/183136596](https://issuetracker.google.com/issues/183136596))

**Bug Fixes**

- Minor improvements to proguard rules. ([aosp/1691484](https://android-review.googlesource.com/c/platform/frameworks/support/+/1691484))

### Version 1.1.0-alpha01

April 7, 2021

`androidx.startup:startup-runtime:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/54a9e747adbe6d44bfddd086953bf731e0fd6ac5..24330de8135d689b34a31a701181b20549e8db25/startup/startup-runtime)

**API Changes**

- Multiple`InitializationProvider``<provider>`elements can now be added to the application's`AndroidManifest.xml`for libraries or applications that require automatic initialization in multiple processes. ([Ia0712](https://android-review.googlesource.com/#/q/Ia07123fcae20f7bdfc9b9f38830d84134fb8d3d4),[b/183136596](https://issuetracker.google.com/issues/183136596))

## Version 1.0.0

### Version 1.0.0

October 28, 2020

`androidx.startup:startup-runtime:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a0ef1fe5f8ea83ac8a25b3837b2acb0f364f637e..54a9e747adbe6d44bfddd086953bf731e0fd6ac5/startup/startup-runtime)

**Major features of 1.0.0**

- Provides a straightforward, performant way to define`Initializer`s to run at application startup without having to define a`ContentProvider`.
- Provides a consistent API for lazy initialization.
- `Initializer`s can define dependencies on other`Initializer`s which helps define the order of initialization explicitly.

### Version 1.0.0-rc01

October 14, 2020

`androidx.startup:startup-runtime:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..a0ef1fe5f8ea83ac8a25b3837b2acb0f364f637e/startup/startup-runtime)

This release is identical to`1.0.0-beta01`.

### Version 1.0.0-beta01

September 16, 2020

`androidx.startup:startup-runtime:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..18a5639262f8504db530176550e338a5d0e2e044/startup/startup-runtime)

This version is identical to[`1.0.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/startup#1.0.0-alpha03).`androidx.startup`is now API stable.

### Version 1.0.0-alpha03

August 19, 2020

`androidx.startup:startup-runtime:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/startup/startup-runtime)

**New Features**

- Added a new`isEagerlyInitialized()`API which provides a way for the`Initializer`to determine if it has been eagerly initialized. ([aosp/1372879](https://android-review.googlesource.com/c/platform/frameworks/support/+/1372879),[b/159952713](https://issuetracker.google.com/issues/159952713))

### Version 1.0.0-alpha02

July 22, 2020

`androidx.startup:startup-runtime:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..9f60cc700129e30cee9df020005c317fb39d32ec/startup/startup-runtime)

**Bug Fixes**

- Publish consumer proguard rules for startup-runtime. ([aosp/1347583](https://android-review.googlesource.com/c/platform/frameworks/support/+/1347583),[b/159595260](https://issuetracker.google.com/issues/159595260))
- Improve static checks in`AppInitializer`. ([aosp/1331900](https://android-review.googlesource.com/c/platform/frameworks/support/+/1331900))

### Version 1.0.0-alpha01

June 10, 2020

`androidx.startup:startup-runtime:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e/startup/startup-runtime)

**New Features**

The App Startup library provides a straightforward, performant way to initialize components at application startup. Both library developers and app developers can use App Startup to streamline startup sequences and explicitly set the order of initialization. This initial release is`1.0.0-alpha01`.