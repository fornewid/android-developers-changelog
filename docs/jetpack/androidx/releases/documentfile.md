---
title: https://developer.android.com/jetpack/androidx/releases/documentfile
url: https://developer.android.com/jetpack/androidx/releases/documentfile
source: md.txt
---

# Documentfile

# Documentfile

[User Guide](https://developer.android.com/guide/topics/providers/document-provider)[Code Sample](https://github.com/android/storage-samples/tree/main/ActionOpenDocumentTree)  
API Reference  
[androidx.documentfile.provider](https://developer.android.com/reference/kotlin/androidx/documentfile/provider/package-summary)  
View a file document.  

| Latest Update |                                   Stable Release                                    | Release Candidate | Beta Release | Alpha Release |
|---------------|-------------------------------------------------------------------------------------|-------------------|--------------|---------------|
| May 7, 2025   | [1.1.0](https://developer.android.com/jetpack/androidx/releases/documentfile#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on DocumentFile, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.documentfile:documentfile:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.documentfile:documentfile:1.1.0")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460422+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460422&template=1422753)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

May 7, 2025

`androidx.documentfile:documentfile:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1fa883225f3ca6238e47b26124515acd0531da82..27495ca3d1fe4a1166bea16413ecf8cff5d85855/documentfile/documentfile).

### Version 1.1.0-rc01

April 23, 2025

`androidx.documentfile:documentfile:1.1.0-rc01`is released. Version 1.1.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fa21b171320cb3de44a0848d06967a15c6402770..1fa883225f3ca6238e47b26124515acd0531da82/).

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

### Version 1.1.0-beta01

April 9, 2025

`androidx.documentfile:documentfile:1.1.0-beta01`is released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..fa21b171320cb3de44a0848d06967a15c6402770/documentfile/documentfile).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler).[b/326456246](https://issuetracker.google.com/issues/326456246)
- Fix documentation issues in documentfile[b/337250687](https://issuetracker.google.com/issues/337250687)

### Version 1.1.0-alpha01

August 18, 2021

`androidx.documentfile:documentfile:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/documentfile/documentfile)

**Bug Fixes**

- Fix ClassVerificationFailures for`DocumentFile`. ([b/188452767](https://issuetracker.google.com/issues/188452767))

## Version 1.0.1

### Version 1.0.1

February 25, 2019

`androidx.documentfile:documentfile 1.0.1`is released.

**Bug fixes**

- Fixed bug where deep tree URIs were truncated by`Document.fromUri`([b/37081745](https://issuetracker.google.com/37081745))