---
title: https://developer.android.com/jetpack/androidx/releases/arch-core
url: https://developer.android.com/jetpack/androidx/releases/arch-core
source: md.txt
---

# Arch Core

# Arch Core

API Reference  
[androidx.arch.core.executor.testing](https://developer.android.com/reference/kotlin/androidx/arch/core/executor/testing/package-summary)  
[androidx.arch.core.util](https://developer.android.com/reference/kotlin/androidx/arch/core/util/package-summary)  
Helper for other arch dependencies, including JUnit test rules that can be used with LiveData.  

|   Latest Update   |                                  Stable Release                                  | Release Candidate | Beta Release | Alpha Release |
|-------------------|----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| February 22, 2023 | [2.2.0](https://developer.android.com/jetpack/androidx/releases/arch-core#2.2.0) | -                 | -            | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:197448+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=197448&template=878802)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 2.2

### Version 2.2.0

February 22, 2023

`androidx.arch.core:core-common:2.2.0`,`androidx.arch.core:core-runtime:2.2.0`, and`androidx.arch.core:core-testing:2.2.0`are released.[Version 2.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e4d01e766eec76322a514a161797b8189f4b194b..d00300b06c00dbf348f871980400948cdf7b10dc/arch/core)

**Important changes since 2.1.0**

- Added the correct nullability to many APIs that previously did not specify whether they were`@NonNull`or`@Nullable`. This may be source incompatible if your Kotlin code was assuming the wrong nullability.

### Version 2.2.0-rc01

February 8, 2023

`androidx.arch.core:core-common:2.2.0-rc01`,`androidx.arch.core:core-runtime:2.2.0-rc01`, and`androidx.arch.core:core-testing:2.2.0-rc01`are released with no changes.[Version 2.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..e4d01e766eec76322a514a161797b8189f4b194b/arch/core)

### Version 2.2.0-beta01

January 25, 2023

`androidx.arch.core:core-common:2.2.0-beta01`,`androidx.arch.core:core-runtime:2.2.0-beta01`, and`androidx.arch.core:core-testing:2.2.0-beta01`are released with no changes.[Version 2.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/arch/core)

### Version 2.2.0-alpha01

January 11, 2023

`androidx.arch.core:core-common:2.2.0-alpha01`,`androidx.arch.core:core-runtime:2.2.0-alpha01`, and`androidx.arch.core:core-testing:2.2.0-alpha01`are released.[Version 2.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b0aad67b0808159e777de3df1dfd347071e366f..adf1c279a86ab3886e1666c08e2c3efba783367b/arch/core)

**API Changes**

- Added the correct nullability to many APIs that previously did not specify whether they were`@NonNull`or`@Nullable`. This may be source incompatible if your Kotlin code was assuming the wrong nullability. ([I34b6b](https://android-review.googlesource.com/#/q/I34b6b636572f1bce61d38af563b4a989aa108f82),[b/236472329](https://issuetracker.google.com/issues/236472329),[b/236472101](https://issuetracker.google.com/issues/236472101),[b/236472102](https://issuetracker.google.com/issues/236472102),[b/236471987](https://issuetracker.google.com/issues/236471987),[b/236472078](https://issuetracker.google.com/issues/236472078),[b/236472176](https://issuetracker.google.com/issues/236472176),[b/236471905](https://issuetracker.google.com/issues/236471905),[b/236472103](https://issuetracker.google.com/issues/236472103))

## Version 2.1.0

### Version 2.1.0

September 5, 2019

`androidx.arch.core:core-common:2.1.0`,`androidx.arch.core:core-runtime:2.1.0`, and`androidx.arch.core:core-testing:2.1.0`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/031e16ab465321fba520b9977ed2972def14b7de..4b0aad67b0808159e777de3df1dfd347071e366f/arch).

No notable public changes changes since 2.0.1

### Version 2.1.0-rc01

July 2, 2019

`androidx.arch.core:core-common:2.1.0-rc01`,`androidx.arch.core:core-runtime:2.1.0-rc01`, and`androidx.arch.core:core-testing:2.1.0-rc01`are released with no changes from`2.1.0-beta01`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311..031e16ab465321fba520b9977ed2972def14b7de/arch).

### Version 2.1.0-beta01

May 7, 2019

`androidx.arch.core:*:2.1.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/c5af1d83cdaec5dff1d4bdefe93d0a24bd1fec89..fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311/arch).

**API changes**

- Breaking change: the previously deprecated`Cancellable`class has been removed. ([aosp/952616](https://android-review.googlesource.com/952616))

### Version 2.1.0-alpha02

April 25, 2019

`androidx.arch.core:*:2.1.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/479525251389167f9bed63ec4e1485a2ceec0aa7..1d1a928881b4a7a75a85ab5b723cc81c829f1c83/arch).

**API Changes**

- The`Cancellable`interface has been deprecated due to a lack of composable infrastructure and its removal from public API in[androidx.activity 1.0.0-alpha07](https://developer.android.com/jetpack/androidx/releases/activity#1.0.0-alpha07). ([aosp/945461](https://android-review.googlesource.com/945461))

### Version 2.1.0-alpha01

April 3, 2019

`androidx.arch.core:*:2.1.0-alpha01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/845cc95561b0c5370e341e6d7640afeda55718a2..479525251389167f9bed63ec4e1485a2ceec0aa7/arch).

**New features**

- Added a new`Cancellable`interface to`core-common`to represent cancellable operations. See[androidx.activity 1.0.0-alpha05](https://developer.android.com/jetpack/androidx/releases/activity#1.0.0-alpha05). ([aosp/922523](https://android-review.googlesource.com/922523))

## Version 2.0.1

### Version 2.0.1

March 22, 2019

Version 2.0.1 of the`androidx.arch.core`artifact group is released with a single adjustment:

- Maximum number of threads in the ArchExecutor is increased from 2 to 4.