---
title: https://developer.android.com/jetpack/androidx/releases/draganddrop
url: https://developer.android.com/jetpack/androidx/releases/draganddrop
source: md.txt
---

# DragAndDrop

API Reference  
[androidx.draganddrop](https://developer.android.com/reference/kotlin/androidx/draganddrop/package-summary)  
Accept drag-and-drop data from another app or within an app, and show a consistent drop target affordance.  

| Latest Update |                                   Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| May 11, 2022  | [1.0.0](https://developer.android.com/jetpack/androidx/releases/draganddrop#1.0.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on DragAndDrop, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.draganddrop:draganddrop:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.draganddrop:draganddrop:1.0.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1139019+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1139019&template=1644483)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0

### Version 1.0.0

May 11, 2022

`androidx.draganddrop:draganddrop:1.0.0`is released.[Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/792d15289c94ffb5121f8e0ea664cc758926ff49..50f2d1d62c4cb89366df3bf9f811754b8cdda677/draganddrop/draganddrop)

**Major features of 1.0.0**

`DropHelper`, the first member of the`draganddrop`library, is a utility class that simplifies implementation of drag and drop capabilities. Use`DropHelper`to specify drop targets, customize drop target highlighting, and define how dropped data is handled.

- `DropHelper`leverages Jetpack's[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener)to provide target-specific processing of drag and drop[`ClipData`](https://developer.android.com/reference/android/content/ClipData).`DropHelper`enhances the user experience by configuring drop targets to display a highlight as users drag content over the targets. The`DropHelper.Options`nested class enables you to customize the appearance of the default highlight.
- `DropHelper`attaches an[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener)to drop targets and configures drop targets to listen for drag and drop events. Do not attach an[`OnDragListener`](https://developer.android.com/jetpack/androidx/releases/m/reference/android/view/View.OnDragListener)or additional`OnReceiveContentListener`to drop targets when using`DropHelper`.
- `DropHelper.Options`gives you the ability to list all[`EditText`](https://developer.android.com/reference/android/widget/EditText)elements contained in the view hierarchy of complex drop targets. If any are present, they must be specified in this way.`DropHelper`prevents the`EditText`elements from stealing focus from the drop target when users drag data over the target. If the drag and drop`ClipData`includes text and URI data,`DropHelper`selects one of the`EditText`elements in the drop target to handle the text data when the`ClipData`is dropped.

For more information, see the[Drag and drop](https://developer.android.com/guide/topics/ui/drag-drop#drophelper)developer's guide.

### Version 1.0.0-rc01

April 20, 2022

`androidx.draganddrop:draganddrop:1.0.0-rc01`is released.[Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..792d15289c94ffb5121f8e0ea664cc758926ff49/draganddrop/draganddrop)

- No changes since the last beta release.

### Version 1.0.0-beta01

March 23, 2022

`androidx.draganddrop:draganddrop:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..5ef5671233460b844828e14a816255dbf7904868/draganddrop/draganddrop)

- No changes since last alpha release.

### Version 1.0.0-alpha04

February 23, 2022

`androidx.draganddrop:draganddrop:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/draganddrop/draganddrop)

**API Changes**

- DragEvents with a non-null localState will not trigger highlighting by default. There is a configuration option to change this behavior. ([I55792](https://android-review.googlesource.com/#/q/I55792b436b346ed9e5fa092c88b4e878087d1395))

### Version 1.0.0-alpha03

January 26, 2022

`androidx.draganddrop:draganddrop:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f..9dceceb54300ed028a7e8fc7a3454f270337ffde/draganddrop/draganddrop)

**New Features**

- On devices running Android S or later,`DropHelper`now delegates to the system implementation of`OnReceiveContentListener`, automatically providing support for input methods other than drag and drop.

### Version 1.0.0-alpha02

December 15, 2021

`androidx.draganddrop:draganddrop:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/301586664b5aad60548f21866cad502d524dbf9f/draganddrop/draganddrop)

**Features in initial release**

`DropHelper`, the first member of the`draganddrop`library, is a utility class that simplifies implementation of drag and drop capabilities. Use`DropHelper`to specify drop targets, customize drop target highlighting, and define how dropped data is handled.

`DropHelper`leverages Jetpack's[`OnReceiveContentListener`](https://developer.android.com/reference/androidx/core/view/OnReceiveContentListener)to provide target-specific processing of drag and drop[`ClipData`](https://developer.android.com/reference/android/content/ClipData).`DropHelper`enhances the user experience by configuring drop targets to display a highlight as users drag content over the targets. The`DropHelper.Options`nested class enables you to customize the color and corner radius of the default highlight.

`DropHelper.Options`also gives you the ability to list all[`EditText`](https://developer.android.com/reference/android/widget/EditText)elements contained in the view hierarchy of complex drop targets.`DropHelper`prevents the`EditText`elements from stealing focus from the drop target when users drag data over the target. If the drag and drop`ClipData`includes text and URI data,`DropHelper`selects one of the`EditText`elements in the drop target to handle the text data when the`ClipData`is dropped.

For more information, see the[Drag and drop](https://developer.android.com/guide/topics/ui/drag-drop)developer's guide.