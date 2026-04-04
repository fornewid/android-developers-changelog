---
title: https://developer.android.com/jetpack/androidx/releases/jetifier
url: https://developer.android.com/jetpack/androidx/releases/jetifier
source: md.txt
---

# Jetifier

# Jetifier

A standalone tool that migrates a library's dependencies on the deprecated support library to equivalent AndroidX dependencies.  

|   Latest Update   | Stable Release | Release Candidate |                                         Beta Release                                          | Alpha Release |
|-------------------|----------------|-------------------|-----------------------------------------------------------------------------------------------|---------------|
| September 2, 2020 | -              | -                 | [1.0.0-beta10](https://developer.android.com/jetpack/androidx/releases/jetifier#1.0.0-beta10) | -             |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460323+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460323&template=1287245)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0.0

### Version 1.0.0-beta10

September 2, 2020

`androidx.jetifier:jetifier-core:1.0.0-beta10`and`androidx.jetifier:jetifier-processor:1.0.0-beta10`are released.[Version 1.0.0-beta10 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82..31022a2dda22705843be1199c786552a6f9f875d/jetifier/jetifier).

**New features**

- Introduced timestamp policy (for deterministic builds)
  - new parameter "--timestampsPolicy" in jetifier standalone to use it.
- Upgraded jetifier to asm 8

**Bug Fixes**

- Fixed input method string mappings

### Version 1.0.0-beta09

February 19, 2020

`androidx.jetifier:jetifier-core:1.0.0-beta09`and`androidx.jetifier:jetifier-processor:1.0.0-beta09`are released.[Version 1.0.0-beta09 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b062e6d3d53790823deac02cc553aa21461a4079..6f7b9ed69dc63e3c2c2b02ee1155b6009a9d5f82/jetifier).

**New features**

- Added support for processing`@link`references in XML

**Bug Fixes**

- Rewrite libraries that contain a mix of androidx and android.support references as these were skipped before. ([b/148462462](https://issuetracker.google.com/issues/148462462))

### Version 1.0.0-beta08

November 20, 2019

`androidx.jetifier:jetifier-core:1.0.0-beta08`and`androidx.jetifier:jetifier-processor:1.0.0-beta08`are released.[Version 1.0.0-beta08 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/d9761c71f9eacfa0abb8f0bc3e2305c8b229d75a..b062e6d3d53790823deac02cc553aa21461a4079/jetifier/jetifier).

**Bug fixes**

- Fixed a ProGuard parsing error ([b/134100420](http://issuetracker.google.com/134100420))
- Fixed a signature error that occurred on unmodified archives ([b/142580430](http://issuetracker.google.com/142580430))
- Removed an unnecessary warning that displayed when modifying single files ([b/143609228](http://issuetracker.google.com/143609228))

### Version 1.0.0-beta07

September 18, 2019

`com.android.tools.build.jetifier:jetifier-core:1.0.0-beta07`and`com.android.tools.build.jetifier:jetifier-processor:1.0.0-beta07`are released.[Version 1.0.0-beta07 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/af05c08e2a2f721b3f7411affca883f6a3336513..d9761c71f9eacfa0abb8f0bc3e2305c8b229d75a/jetifier).

**Bug fixes**

- Fixed the mappings of the`androidx.navigation`library

### Version 1.0.0-beta06

August 15, 2019

`androidx.jetifier:jetifier-core:1.0.0-beta06`and`androidx.jetifier:jetifier-processor:1.0.0-beta06`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/c7ff6518ef8c45a3ce775f9a3dde4fbc77854e7a..af05c08e2a2f721b3f7411affca883f6a3336513/jetifier).

**Bug fixes**

- Fixed a thread safety issue with`Class.getResourceAsStream()`. ([b/137929327](https://issuetracker.google.com/issues/137929327),[b/120277395](https://issuetracker.google.com/issues/120277395))

- Fixed`NullPointerException`when processing files locally with Jetifier standalone ([b/136576786](https://issuetracker.google.com/issues/136576786))

### Version 1.0.0-beta05

June 18, 2019

`com.android.tools.build.jetifier:jetifier-core:1.0.0-beta05`and`com.android.tools.build.jetifier:jetifier-processor:1.0.0-beta05`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/0010058fd49253b84e622b2a74ec348e23f5af7f..c7ff6518ef8c45a3ce775f9a3dde4fbc77854e7a/jetifier).

**New features**

- Adds mappings for Navigation and WorkManager.
- Jetifier can now skip libraries containing AndroidX references ([b/119135578](https://issuetracker.google.com/119135578))

**Bug fixes**

- Close stream when loading config in jetifier ([b/120277395](https://issuetracker.google.com/120277395)
- Fix for incorrectly migrated Bundle key strings

### Version 1.0.0-beta04

February 25, 2019

`com.android.tools.build.jetifier 1.0.0-beta04`is released.

**Bug fixes**

- Updated version of`ConstraintLayout`to`1.1.3`
- Fixed mapping of`android.support.v4.os.ResultReceiver`([b/123651524](https://issuetracker.google.com/123651524))

### Version 1.0.0-beta03

February 7, 2019

`com.android.tools.build.jetifier 1.0.0-beta03`is released.

**New features**

- Jetifier now throws an exception if it finds a signature inside a jetified JAR. This can be disabled by using`-stripSignatures`which will remove all signature files. This does not apply to libraries that do not have any dependencies on old support library as jetifier skips these ([aosp/894356](https://android-review.googlesource.com/894356/))

**Bug fixes**

- Fixed jetification of android.support.customtabs so jetifier no longer migrates the constants ([aosp/875343](https://android-review.googlesource.com/875343/))
- Fixed that jetifier always marked non-modified archives as modified if they contained a POM file ([aosp/876353](https://android-review.googlesource.com/876353/))