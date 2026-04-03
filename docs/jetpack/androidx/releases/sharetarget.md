---
title: https://developer.android.com/jetpack/androidx/releases/sharetarget
url: https://developer.android.com/jetpack/androidx/releases/sharetarget
source: md.txt
---

# ShareTarget

# ShareTarget

Provide backwards compatibility for using shortcuts as direct share targets.  

|  Latest Update  |                                   Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|-----------------|------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| October 5, 2022 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/sharetarget#1.2.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on ShareTarget, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.sharetarget:sharetarget:1.2.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.sharetarget:sharetarget:1.2.0")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:586834+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=586834&template=1235956)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.2.0

### Version 1.2.0

October 5, 2022

`androidx.sharetarget:sharetarget:1.2.0`is released.[Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bc585b9923497037acb7833d35b95e64864c747e..2112784de630cc17e4dec46809641b554b9b76e4/sharetarget/sharetarget)

**Major changes since 1.1.0**

- Fix required explicit value for`android:exported`attribute for Android 12 ([aosp/1742473](https://android-review.googlesource.com/c/platform/frameworks/support/+/1742473))

### Version 1.2.0-rc02

July 27, 2022

`androidx.sharetarget:sharetarget:1.2.0-rc02`is released with no changes since version 1.2.0-alpha01 .[Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c0bc017f4cd3bac36d7063eaf61ca6a820309c..bc585b9923497037acb7833d35b95e64864c747e/sharetarget/sharetarget)

### Version 1.2.0-rc01

November 3, 2021

`androidx.sharetarget:sharetarget:1.2.0-rc01`is released with no changes.[Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4428a02d484bb23d7e516c6f55579cf9130f086f..64c0bc017f4cd3bac36d7063eaf61ca6a820309c/sharetarget/sharetarget)

### Version 1.2.0-beta01

September 1, 2021

`androidx.sharetarget:sharetarget:1.2.0-beta01`is released.[Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/11d2376b4247b10f75e08c7fcfd67dbf1994a6c1..4428a02d484bb23d7e516c6f55579cf9130f086f/sharetarget/sharetarget)

### Version 1.2.0-alpha01

August 4, 2021

`androidx.sharetarget:sharetarget:1.2.0-alpha01`is released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/414b76580d5a2e88020d6631354817a0f34fec00..11d2376b4247b10f75e08c7fcfd67dbf1994a6c1/sharetarget/sharetarget)

**Bug Fixes**

- Share target service explicit value for android:exported attribute fix for Android 12. ([aosp/1742473](https://android-review.googlesource.com/c/platform/frameworks/support/+/1742473))

## Version 1.1.0

### Version 1.1.0

January 13, 2021

`androidx.sharetarget:sharetarget:1.1.0`is released.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/823ddd0c338c13d048476ba2265c0f991ad0d414..414b76580d5a2e88020d6631354817a0f34fec00/sharetarget/sharetarget)

**Major changes since 1.0.0**

- 1.1.0 uses ShortcutInfoCompat#Rank to set the score of ChooserTargets in compatibility mode. ([aosp/1115363](https://android-review.googlesource.com/c/platform/frameworks/support/+/1115363))
- Fixed a resource leak. ([aosp/1259160](https://android-review.googlesource.com/c/platform/frameworks/support/+/1259160))
- Errorprone warnings are now enforced. ([aosp/1199825](https://android-review.googlesource.com/c/platform/frameworks/support/+/1199825))

### Version 1.1.0-rc01

December 2, 2020

`androidx.sharetarget:sharetarget:1.1.0-rc01`is released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8e2ebc8f1d5979718171d380f3fc1c885c245001..823ddd0c338c13d048476ba2265c0f991ad0d414/sharetarget/sharetarget)

### Version 1.1.0-beta01

October 14, 2020

`androidx.sharetarget:sharetarget:1.1.0-beta01`is released.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/636ec5ea1f23fb6181693b3a9f052311c5bc781c..8e2ebc8f1d5979718171d380f3fc1c885c245001/sharetarget/sharetarget)

**Bug fixes**

- Fixed a resource leak. ([aosp/1259160](https://android-review.googlesource.com/c/platform/frameworks/support/+/1259160))

## Version 1.0.0

| **Note:** newer versions androidx libraries now correctly reflect`implementation`dependencies versus`api`dependencies. If your project relies on an implicit dependency exposed through an`implementation`dependency in version`1.0.0`, it will be necessary to explicitly depend on that dependency in your`build.gradle`.

### Version 1.0.0

May 14, 2020

`androidx.sharetarget:sharetarget:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74353beef24977dfe1748b2f1bc94f6472d725a0..636ec5ea1f23fb6181693b3a9f052311c5bc781c/sharetarget)

**Major features of 1.0.0**

ShareTarget module provides backward compatibility for providing share targets which are shown in the platform's ShareSheet. This module does not have any public APIs, and apps do not need to directly interact with this module. Instead,`ShortcutManagerCompat`internally uses this as a utility library when needed. For more information on how to use the ShareTarget module, please refer to the[Providing Direct Share targets guide](https://developer.android.com/training/sharing/receive#providing-direct-share-targets).

### Version 1.0.0-rc01

December 4, 2019

`androidx.sharetarget:sharetarget:1.0.0-rc01`is released with no changes since`1.0.0-beta02`.[Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/3c455c01a83d0598e2e6a014d8f1b490d0a39170..74353beef24977dfe1748b2f1bc94f6472d725a0/sharetarget).

### Version 1.0.0-beta02

November 7, 2019

`androidx.sharetarget:sharetarget:1.0.0-beta02`is released.[Version 1.0.0-beta02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd1aae0250ae03f6383bf4fd28a60036778bb509..3c455c01a83d0598e2e6a014d8f1b490d0a39170/sharetarget).

**Bug fixes**

- When converting ShortcutInfos to ChooserTargets for backwards compatibility, sort shortcuts based on the given rank.

### Version 1.0.0-beta01

September 5, 2019

`androidx.sharetarget:sharetarget:1.0.0-beta01`is released with no changes since`1.0.0-alpha02`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/c2ea01c74a9e4ecfeca7426cf443dcd1ad067c25..cd1aae0250ae03f6383bf4fd28a60036778bb509/sharetarget).

### Version 1.0.0-alpha02

June 5, 2019

`androidx.sharetarget:sharetarget:1.0.0-alpha02`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/79285e90f077844e4b3b1a72a4a051389e3c190a..c2ea01c74a9e4ecfeca7426cf443dcd1ad067c25/sharetarget).

**Bug fixes**

- Read the shortcuts resource name from manifest instead of hardcoded name ([b/130500127](https://issuetracker.google.com/issues/130500127))

### Version 1.0.0-alpha01

March 13, 2019

`androidx.sharetarget:sharetarget:1.0.0-alpha01`is released.

This module provides backwards compatibility for publishing direct share targets on pre-Q Android versions. None of the APIs in this module are meant to be used directly by the app, but when imported as a dependency, will add extra background functionality to`ShortcutManagerCompat`in the`androidx.core`module.

The full list of commits included in this initial release can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/79285e90f077844e4b3b1a72a4a051389e3c190a/sharetarget).

Please file bugs and feature requests under the[ShareTarger Issue Tracker](https://issuetracker.google.com/issues/new?component=586834&template=1235956).

**New features**

- This is the first release of this module.