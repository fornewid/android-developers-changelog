---
title: https://developer.android.com/jetpack/androidx/releases/versionedparcelable
url: https://developer.android.com/jetpack/androidx/releases/versionedparcelable
source: md.txt
---

# Versionedparcelable

# Versionedparcelable

API Reference  
[androidx.versionedparcelable](https://developer.android.com/reference/kotlin/androidx/versionedparcelable/package-summary)  
Provides a stable and compact binary serialization format that can be passed across processes or persisted safely.  

|  Latest Update   |                                       Stable Release                                       | Release Candidate | Beta Release | Alpha Release |
|------------------|--------------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| January 29, 2025 | [1.2.1](https://developer.android.com/jetpack/androidx/releases/versionedparcelable#1.2.1) | -                 | -            | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460991+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460991&template=1422652)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2

### Version 1.2.1

January 29, 2025

`androidx.versionedparcelable:versionedparcelable:1.2.1`is released. Version 1.2.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fad42d44b65dfac68191ccd49e22d418b82c625..bed62b26ea4f47707c9610421bfed533c6830c58/versionedparcelable/versionedparcelable).

**Bug Fixes**

- Updated`VersionedParcelable`to avoid class init during the initial stages of unparceling, which prevents externally-controlled inputs from executing unexpected code in static initialization blocks for non-`VersionedParcelable`classes already present in the application classpath. ([Icceed](https://android-review.googlesource.com/#/q/Icceed9dfc7c78434d78336f2f606fc0530133d7c))
- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ibc328](https://android-review.googlesource.com/#/q/Ibc3284a4b99a39636c4ec08e448ffbe434473e77),[b/326456246](https://issuetracker.google.com/issues/326456246))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See[this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd)for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8),[b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 1.2.0

January 10, 2024

`androidx.versionedparcelable:versionedparcelable:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d24bc8cd7ea22574c46ea04d0ca524299c35be53..5fad42d44b65dfac68191ccd49e22d418b82c625/versionedparcelable/versionedparcelable)

**Important changes since 1.1.0**

- Added support for depending on`VersionedParcelable`from a project using Stable AIDL.

### Version 1.2.0-rc01

December 13, 2023

`androidx.versionedparcelable:versionedparcelable:1.2.0-rc01`is released. There are no changes since the previous beta release.

### Version 1.2.0-beta01

November 29, 2023

`androidx.versionedparcelable:versionedparcelable:1.2.0-beta01`is released with no changes since 1.2.0-alpha01.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/versionedparcelable/versionedparcelable)

### Version 1.2.0-alpha01

November 15, 2023

`androidx.versionedparcelable:versionedparcelable:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fd278801e06c07a5d230fd7edbb97e16c322949..312eb9f1ddece3a18317f18515a877e0e745cb2c/versionedparcelable/versionedparcelable)

**New Features**

- Export stable AIDL definitions to dependent projects ([I473cb](https://android-review.googlesource.com/#/q/I473cbc23b15505b8493a00766248fcd1d8a10a96),[b/277084531](https://issuetracker.google.com/issues/277084531))

**API Changes**

- Added nullability annotations ([Ic16ed](https://android-review.googlesource.com/#/q/Ic16ed43e46dfd51803d40e6332b0cf34467aaf7c))

## Version 1.1.1

### Version 1.1.1

April 15, 2020

`androidx.versionedparcelable:versionedparcelable:1.1.1`is released.[Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e9fe1bb5aab6c2f410f8992bfe340768e0c74abd..9fd278801e06c07a5d230fd7edbb97e16c322949/versionedparcelable)

**Bug Fixes**

- Updated ProGuard rules to keep all classes that implement`VersionedParcelable`, including non-public classes ([I480bf8](https://android-review.googlesource.com/q/I480bf84ca20b79f83ea4d6c74af45ea55a3b8e9a))

## Version 1.1.0

### Version 1.1.0

August 7, 2019

`androidx.versionedparcelable:versionedparcelable:1.1.0`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/33004feca088677f6f8135824d6e09169afd3491..e9fe1bb5aab6c2f410f8992bfe340768e0c74abd/versionedparcelable).

**Below is a summary of changes from`1.0.0`to`1.1.0`:**

**New features**

- New convenience methods`ParcelUtils.getVersionedParcelableList()`and`ParcelUtils.putVersionedParcelableList()`

**API changes**

- `ParcelUtils.getVersionedParcelable()`now returns null if the key is not found in the bundle
- `ParcelUtils.putVersionedParcelable()`now accepts null VersionedParcelable objects

### Version 1.1.0-rc01

June 5, 2019

`androidx.versionedparcelable:versionedparcelable:1.1.0-rc01`is released with no changes from 1.1.0-beta01. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311..33004feca088677f6f8135824d6e09169afd3491/versionedparcelable).

### Version 1.1.0-beta01

May 7, 2019

`androidx.versionedparcelable:versionedparcelable:1.1.0-alpha01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/0b2c8b5a3ea18e80b32b57c49dba74c2812946ee..fbdc0c35696b2e1ee3216e3e8c397aeb1abe4311/versionedparcelable).

**API changes**

- `Parcelutils.getVersionedParcelable`and Parcelutils.putVersionedParcelable\` now support null ([aosp/940072](https://android-review.googlesource.com/c/940072/))
- `RemoteActionCompat`is now a VersionedParcelable\` ([aosp/928534](https://android-review.googlesource.com/c/928534/))

### Version 1.1.0-alpha02

March 13, 2019

`androidx.versionedparcelable:versionedparcelable:1.1.0-alpha02`is released. The full list of commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/f1c97d6550c139c61400f5efd88932a6020587..HEAD/versionedparcelable).

**Bug fixes**

- Updated to the latest annotation version for new annotations.

### Version 1.1.0-alpha01

November 5, 2018

**New features**

- Added support for CharSequence in all classes except VersionedParcelStream.
- Added support for SuperClass, Set, and Map.

**Bug fixes**

- Fixed a bug with checking IDs in inherited classes.