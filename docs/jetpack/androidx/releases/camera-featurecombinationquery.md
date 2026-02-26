---
title: https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery
url: https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery
source: md.txt
---

# Camera Feature Combination Query

API Reference  
[androidx.camera.featurecombinationquery](https://developer.android.com/reference/kotlin/androidx/camera/featurecombinationquery/package-summary)  
Query camera capabilities.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.5.3](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery#1.5.3) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/camera-featurecombinationquery#1.6.0-rc01) | - | - |

## Declaring dependencies

To add a dependency on camera feature combination query library, you must add
the Google Maven repository to your project. Read
[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) for more
information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    // Use to pull in the base feature combination query library
    implementation "androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-rc01"

    // Optional [recommended]: Use to enable play services as a query provider
    implementation "androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-rc01"
}
```

### Kotlin

```kotlin
dependencies {
    // Use to pull in the base feature combination query library
    implementation("androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-rc01")

    // Optional [recommended]: Use to enable play services as a query provider
    implementation("androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-rc01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:618491+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=618491&template=1257717)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.6

### Version 1.6.0-rc01

February 25, 2026

`androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-rc01` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-rc01` are released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/82004373076cf552e53b43166e1b4ddfbcfec21e..0dc6fa695e63a0bbc17f07b7368ba2567fb47d01/camera/featurecombinationquery).

### Version 1.6.0-beta02

February 11, 2026

`androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-beta02` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-beta02` are released. Version 1.6.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/48e95c38588deabd109b960f6d6ba5f47461c192..82004373076cf552e53b43166e1b4ddfbcfec21e/camera/featurecombinationquery).

### Version 1.6.0-beta01

January 28, 2026

`androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-beta01` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-beta01` are released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/84753047f87d847904220ad53b1c78d1a98189c4..5fc4e0225a10d812728a4bece5a2f6e82737df85/camera/featurecombinationquery).

### Version 1.6.0-alpha02

December 17, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-alpha02` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-alpha02` are released. Version 1.6.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dacd36e7413e15947cdd89e21c189fead769bfab..84753047f87d847904220ad53b1c78d1a98189c4/camera/featurecombinationquery).

### Version 1.6.0-alpha01

October 22, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.6.0-alpha01` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.6.0-alpha01` are released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..dacd36e7413e15947cdd89e21c189fead769bfab/camera/featurecombinationquery).

## Version 1.5

### Version 1.5.3

January 28, 2026

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.3` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.3` are released. Version 1.5.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0975f1cec9e7c5b1192d3ceb925b3178cd234957..2afad3835627a7fdd11578788696f14b7aff6017/camera/featurecombinationquery).

### Version 1.5.2

December 4, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.2` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.2` are released. Version 1.5.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e7bb7786b42348603fed2825d18815e6dfa9bd4b..0975f1cec9e7c5b1192d3ceb925b3178cd234957/camera/featurecombinationquery).

### Version 1.5.1

October 08, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.1` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.1` are released. Version 1.5.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bf14d325dfcbc73bf18b092f0435beaaf465e126..e7bb7786b42348603fed2825d18815e6dfa9bd4b/camera/featurecombinationquery).

### Version 1.5.0

September 10, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.0` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.0` are released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3496263efa2133a8c8cd25f4ae6509b9d28a788f..bf14d325dfcbc73bf18b092f0435beaaf465e126/camera/featurecombinationquery).

### Version 1.5.0-rc01

August 13, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.0-rc01` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.0-rc01` are released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f22a8ba695b5a3d975f57d279262d9d39444d990..3496263efa2133a8c8cd25f4ae6509b9d28a788f/camera/featurecombinationquery).

### Version 1.5.0-beta02

July 16, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.0-beta02` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.0-beta02` are released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7442ed2cb3111f2187694f18723b4fbd1c9efa69..f22a8ba695b5a3d975f57d279262d9d39444d990/camera/featurecombinationquery).

**New Features**

- Play Service implementation will automatically pull in the Play Services Implementation when used.

**Bug Fixes**

- Clarified restrictions when using deferred surfaces with the play store implementation.
- Moved some initialization to the Factory constructor to give clients better control over when they want the Binder calls to happen. Updated the docs to reflect the same.

### Version 1.5.0-beta01

June 4, 2025

`androidx.camera.featurecombinationquery:featurecombinationquery:1.5.0-beta01` and `androidx.camera.featurecombinationquery:featurecombinationquery-play-services:1.5.0-beta01` are released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7442ed2cb3111f2187694f18723b4fbd1c9efa69/camera/featurecombinationquery).

**New Features**

- With the update to 1.5.0-beta01, the `FeatureCombinationQuery` artifacts have been moved to their own library group. This change is necessary to improve the modularity and maintainability of the CameraX library.

**API Changes**

- `SessionConfigurationCompat` and `SessionParametersCompat` have been renamed to `SessionConfigurationLegacy` and `SessionParametersLegacy` respectively to better reflect their function in supporting older APIs only.
- Similarly, the method name/signature of `CameraDeviceSetupCompat.#isSessionConfigurationSupported(SessionConfigurationCompat)` has been changed to `CameraDeviceSetupCompat.#isSessionConfigurationSupportedLegacy(SessionConfigurationLegacy)`