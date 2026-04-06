---
title: https://developer.android.com/jetpack/androidx/releases/textclassifier
url: https://developer.android.com/jetpack/androidx/releases/textclassifier
source: md.txt
---

# Textclassifier

# Textclassifier

API Reference  
[androidx.textclassifier](https://developer.android.com/reference/kotlin/androidx/textclassifier/package-summary)  
Identifies conversations, links, selections, and other similar constructs in text.  

| Latest Update  | Stable Release | Release Candidate | Beta Release |                                             Alpha Release                                             |
|----------------|----------------|-------------------|--------------|-------------------------------------------------------------------------------------------------------|
| March 23, 2022 | -              | -                 | -            | [1.0.0-alpha04](https://developer.android.com/jetpack/androidx/releases/textclassifier#1.0.0-alpha04) |

## Declaring dependencies

To add a dependency on TextClassifier, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.textclassifier:textclassifier:1.0.0-alpha04"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.textclassifier:textclassifier:1.0.0-alpha04")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:878772+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=878772&template=1441952)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0.0

### Version 1.0.0-alpha04

March 23, 2022

`androidx.textclassifier:textclassifier:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a3d894e8fe0217f1312fb163a89ad51bf15794e..5ef5671233460b844828e14a816255dbf7904868/textclassifier/textclassifier)

**API Changes**

- Deprecate all the APIs in the textclassifier module ([Idc180](https://android-review.googlesource.com/#/q/Idc18063196531c0e926162fefeadf2dc5f559da1),[b/210509084](https://issuetracker.google.com/issues/210509084))

**Bug Fixes**

- API lint check for`MissingGetterMatchingBuilder`is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9),[b/138602561](https://issuetracker.google.com/issues/138602561))
- `AppCompatRatingBar`PNG drawables have been replaced with vector sources. This may cause slight changes in the visual appearance of individual stars. ([I6b99d](https://android-review.googlesource.com/#/q/I6b99d3fde8d3cd275d0fc279324066bcd7f3ecd6))

### TextClassifier Version 1.0.0-alpha03

January 22, 2020

`androidx.textclassifier:textclassifier:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ddceab357394ac5ab55c825844f111afe9401261..0a3d894e8fe0217f1312fb163a89ad51bf15794e/textclassifier).

**New features**

**API changes**

- `setIncludeDefaultEntityTypes`has been renamed to`includeTypesFromTextClassifier`
- `setIncludedEntityTypes`has been renamed to`setIncludedTypes`
- `setExcludedEntityTypes`has been renamed to`setExcludedTypes`

**Bug fixes**

### Version 1.0.0-alpha02

February 7, 2019

`androidx.textclassifier 1.0.0-alpha02`is released.

**API changes**

- `TextLinks.TextLink.getEntityType`replaces`TextLinks.TextLink.getEntity`
- `TextLinks.TextLink.getEntityTypeCount`replaces`TextLinks.TextLink.getEntityCount`
- `TextSelection.getEntityType`replaces`TextSelection.getEntity`
- `TextSelection.getEntityTypeCount`replaces \`TextSelection.getEntityCount

**Bug fixes**

- Fix a memory leak issue in AndroidX TextClassificationManager. ([aosp/887354](https://android-review.googlesource.com/887354))
- Floating Toolbar: Handle TextView position changes. ([aosp/877713](https://android-review.googlesource.com/877713))

### Version 1.0.0-alpha01

December 3, 2018

This is the first refactoring of`TextClassifier`to`androidx`. This release backports (`android.view.textclassifier.TextClassifier`)\[/reference/android/view/textclassifier/TextClassifier\] features, particularly Smart Linkify, back to API 14.