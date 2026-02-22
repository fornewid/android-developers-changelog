---
title: https://developer.android.com/jetpack/androidx/releases/slice
url: https://developer.android.com/jetpack/androidx/releases/slice
source: md.txt
---

# Slice

# Slice

[User Guide](https://developer.android.com/guide/slices)[Code Sample](https://github.com/android/user-interface-samples)  
API Reference  
[androidx.slice](https://developer.android.com/reference/kotlin/androidx/slice/package-summary)  
[androidx.slice.builders](https://developer.android.com/reference/kotlin/androidx/slice/builders/package-summary)  
[androidx.slice.core](https://developer.android.com/reference/kotlin/androidx/slice/core/package-summary)  
[androidx.slice.widget](https://developer.android.com/reference/kotlin/androidx/slice/widget/package-summary)  
Display templated UI elements outside your app.  

|  Latest Update   | Stable Release | Release Candidate | Beta Release |                                        Alpha Release                                         |
|------------------|----------------|-------------------|--------------|----------------------------------------------------------------------------------------------|
| January 13, 2021 | -              | -                 | -            | [1.1.0-alpha02](https://developer.android.com/jetpack/androidx/releases/slice#1.1.0-alpha02) |

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460783+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460783&template=1422470)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0-alpha02

January 13, 2021

`androidx.slice:slice-builders:1.1.0-alpha02`,`androidx.slice:slice-core:1.1.0-alpha02`, and`androidx.slice:slice-view:1.1.0-alpha02`are released.[Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/557d5e4baea877324ddd0d6b9f2b969f080a8b7b..6207afb1646d302c5d29c2c67d332b48db87fb27/slices)

**API Changes**

- Support pickers in slice actions in row view ([I4d965](https://android-review.googlesource.com/#/q/I4d96578848f48d3144d479d8d1d272dc6b0b5876))
- SliceAction support for GridRow ([Ie289b](https://android-review.googlesource.com/#/q/Ie289bc3ae250ee3eca27e0e659181e71f59db9a6))
- Added Time picker text, which creates a time picker or date picker dialog when tapped. ([I07deb](https://android-review.googlesource.com/#/q/I07debf8131466cf9e0488a981497d29001257d23))
- Fixed an issue for Treehug error ([I416cc](https://android-review.googlesource.com/#/q/I416ccc8be568a76bc2bf3c9c9a7a590c5f65c77e))
- Added`ListBuilder.StarRatingBuilder`, which is a row that supports star rating inputs for slices. ([I25aec](https://android-review.googlesource.com/#/q/I25aecc9907f0fea3842f0b29083da1b0d956ff5f))
- Replaced`ListBuilder#setHostExtra`with`ListBuilder#setHostExtras`to accept a bundle ([I43ec7](https://android-review.googlesource.com/#/q/I43ec7ce94b46468c64a542d1b14f2e908e4751bb),[b/](https://issuetracker.google.com/issues/))
- Added new API`ListBuilder#setHostExtra`and`SliceMetadata#getHostExtras`to save and extract additional information for the host from slice. ([Ib0768](https://android-review.googlesource.com/#/q/Ib07683a36ee66e722af0bc873837fdc373c5905f),[b/](https://issuetracker.google.com/issues/))
- Added new API for RowBuilder to indicate end of a section and show bottom line divider. ([I23ddd](https://android-review.googlesource.com/#/q/I23ddd4d4377ec6273b49414d3323afb275f33e05),[b/](https://issuetracker.google.com/issues/))
- Add nullabilities annotation in slice builders for better kotlin interop. ([If00f1](https://android-review.googlesource.com/#/q/If00f14006017c097853a766c89f03f7530f1841d),[b/166489398](https://issuetracker.google.com/issues/166489398))
- Added`CellBuilder.addOverlayText`, which overlays text on the image in the cell. ([I09d97](https://android-review.googlesource.com/#/q/I09d9731c3c2dfef57383161cb4f757dfe99e1d06))
- Added imageCornerRadius attribute for applying rounded corners to`SliceHints.LARGE_IMAGE`images/icons. ([I3e8f8](https://android-review.googlesource.com/#/q/I3e8f85bd415a4fa9a35da55733ee75c36bfd8b08))
- Make`configureViewPolicy`protected instead of private so it can be called from subclasses. ([I6772b](https://android-review.googlesource.com/#/q/I6772b328f34d4b38e2be7d3b2c6b563467860cd0))
- Support raw images in gridrow view being sized for portrait and landscape images. ([I925fb](https://android-review.googlesource.com/#/q/I925fb349bb8382d7618652517cc2ad98ace3abd9))
- Added a new API`SliceView#getNumberOfHiddenItems`to obtain the number of slice items that didn't fit into the view. ([I09651](https://android-review.googlesource.com/#/q/I09651e769b15087364f50a32c3d1ee00bfeee25e))
- Added`SliceView#setRowStyleFactory`to allow slice hosts to customize the style of each row based on slice metadata. ([Ia8f2e](https://android-review.googlesource.com/#/q/Ia8f2ed86af99d58b7d89616899d0bf1f90de70c4))

**Bug Fixes**

- Fix Picker Slice action on Gridrow as only item ([I3d899](https://android-review.googlesource.com/#/q/I3d8993aa9fdedfd6a2418cc69c09619459710d2e))

**External Contribution**

- API lint check for the StaticFinalBuilder is enabled for androidx ([I2b11b](https://android-review.googlesource.com/#/q/I2b11be1bb370e178e3e0d1d1083d43af38eece23),[b/138602561](https://issuetracker.google.com/issues/138602561))

### Slice-Builders-Ktx Version 1.0.0-alpha08

January 13, 2021

`androidx.slice:slice-builders-ktx:1.0.0-alpha08`is released.[Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/557d5e4baea877324ddd0d6b9f2b969f080a8b7b..6207afb1646d302c5d29c2c67d332b48db87fb27/slices/builders/ktx)

Updated to depend on slice-builders 1.1.0-alpha02.

### Version 1.1.0-alpha01

May 7, 2019

`androidx.slice:slice-builders:1.1.0-alpha01`,`androidx.slice:slice-builders-ktx:1.0.0-alpha07`,`androidx.slice:slice-core:1.1.0-alpha01`, and`androidx.slice:slice-view:1.1.0-alpha01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/50a39caa72955aae0c75225fd9805ab537cbf049..557d5e4baea877324ddd0d6b9f2b969f080a8b7b/slices).

**New features**

- `onCreatePermissionRequest`can be overridden in`SliceProvider`to customize the permission grant behavior

**Bug fixes**

- Fixed OnSliceActionListener was not getting called when a row item with only one action was clicked
- Fixed SliceView has not respecting MeasureSpec.EXACTLY layout params
- Fixed duplicate onClick during onLongClick on SliceView