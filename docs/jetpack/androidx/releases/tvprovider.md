---
title: https://developer.android.com/jetpack/androidx/releases/tvprovider
url: https://developer.android.com/jetpack/androidx/releases/tvprovider
source: md.txt
---

# TV Provider

# TV Provider

[Code Sample](https://github.com/android/tv-samples)  
API Reference  
[androidx.tvprovider.media.tv](https://developer.android.com/reference/kotlin/androidx/tvprovider/media/tv/package-summary)  
Provide Android TV channels.  

| Latest Update |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| May 7, 2025   | [1.1.0](https://developer.android.com/jetpack/androidx/releases/tvprovider#1.1.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on TVProvider, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.tvprovider:tvprovider:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.tvprovider:tvprovider:1.1.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:878254+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=878254&template=1442004)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.1.0

### Version 1.1.0

May 7, 2025

`androidx.tvprovider:tvprovider:1.1.0`is released. Version 1.1.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/1f50b1ce3e6505df3f1906c60bbf6b1f9d845af0..cc54e3d74495af6183b9e0067e4dbb4806941c17/).

### Version 1.1.0-beta01

April 9, 2025

`androidx.tvprovider:tvprovider:1.1.0-beta01`is released. Version 1.1.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..1f50b1ce3e6505df3f1906c60bbf6b1f9d845af0/tvprovider/tvprovider).

**API Changes**

- Fixed a crash in`PreviewChannelHelper.getAllChannels()`. ([I5041f](https://android-review.googlesource.com/#/q/I5041f69e658dec535930c478f674cf5a29dd57bf))

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I4fcdf](https://android-review.googlesource.com/#/q/I4fcdf3ed392d15751627922d586eac18f821d0d2),[b/326456246](https://issuetracker.google.com/issues/326456246))

**External Contribution**

- Removed`RestrictTo(LIBRARY)`annotation from`TvContractCompact.PreviewProgramColumns`interface for public access of aspect ratio. ([Id610a](https://android-review.googlesource.com/#/q/Id610a80aa6017ea88586fdb78ef2254e27ad4bb9),[b/138150076](https://issuetracker.google.com/issues/138150076))
- Removed`RestrictTo(LIBRARY)`annotation from`PreviewProgram.PROJECTION`and`WatchNextProgram.PROJECTION`for making them public ([I04256](https://android-review.googlesource.com/#/q/I042568f082661ca0c10cb0f757a6715f499b52cc),[b/138150076](https://issuetracker.google.com/issues/138150076))

### Version 1.1.0-alpha01

August 19, 2020

`androidx.tvprovider:tvprovider:1.1.0-alpha01`is released.[Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1/tv-provider/tv-provider)

**Bug Fixes**

- PreviewChannelHelper was made backward compatible with older Android API versions (\<26) by doing a no-op now. ([aosp/1310579](https://android-review.googlesource.com/c/platform/frameworks/support/+/1310579),[b/136123939](https://issuetracker.google.com/issues/136123939))
- PreviewChannel now handles the nullability in the`setDescription`method. ([aosp/1310577](https://android-review.googlesource.com/c/platform/frameworks/support/+/1310577),[b/119800858](https://issuetracker.google.com/issues/119800858))