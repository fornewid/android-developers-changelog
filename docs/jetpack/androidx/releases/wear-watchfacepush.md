---
title: wear watchfacepush  |  Jetpack  |  Android Developers
url: https://developer.android.com/jetpack/androidx/releases/wear-watchfacepush
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Get started](https://developer.android.com/get-started/overview)
* [Jetpack](https://developer.android.com/jetpack)
* [Libraries](https://developer.android.com/jetpack/androidx/explorer)

Stay organized with collections

Save and categorize content based on your preferences.




# Wear Watch Face Push

API Reference  
[androidx.wear.watchfacepush](/reference/kotlin/androidx/wear/watchfacepush/package-summary)

Watch Face Push allows a Wear OS app to install a watch face on a watch programmatically.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
| --- | --- | --- | --- | --- |
| March 25, 2026 | - | [1.0.0-rc02](/jetpack/androidx/releases/wear-watchfacepush#1.0.0-rc02) | - | - |

## Declaring dependencies

To add a dependency on Wear Watch Face Push, you must add the Google Maven
repository to your project.
Read [Google's Maven repository](/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```
repositories {
    google() // For the watchfacepush library itself
}
dependencies {
    implementation "androidx.wear.watchfacepush:watchfacepush:1.0.0-rc02"
}
```

### Kotlin

```
repositories {
    google() // For the watchfacepush library itself
}

dependencies {
    implementation("androidx.wear.watchfacepush:watchfacepush:1.0.0-rc02")
}
```

Additionally, if the app needs to generate tokens for a watch face at runtime, add the following
dependency:

### Groovy

```
repositories {
    google() // For the validator-push library itself
    maven {
        url "https://jitpack.io" // For dependencies of the validator-push library
        content {
            includeGroup "com.github.xgouchet"
        }
    }
}

dependencies {
    implementation "com.google.android.wearable.watchface.validator:validator-push:1.0.0-alpha10"
}
```

### Kotlin

```
repositories {
    google() // For the validator-push library itself
    maven {
        url = uri("https://jitpack.io") // For dependencies of the validator-push library
        content {
            includeGroup("com.github.xgouchet")
        }
    }
}

dependencies {
    implementation("com.google.android.wearable.watchface.validator:validator-push:1.0.0-alpha10")
}
```

For more information about dependencies, see [Add build dependencies](/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1235337%20status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1235337&template=1726812)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-rc02

March 25, 2026

`androidx.wear.watchfacepush:watchfacepush:1.0.0-rc02` is released. Version 1.0.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/17bd646a50810d4ad3ef4974404f4d7047eff303..c27c590bb2fe7d4c6c309ef19ade06d146b103da/wear/watchfacepush/watchfacepush).

* Updates the Guava dependency version to resolve security vulnerability CVE-2023-2976.

### Version 1.0.0-rc01

March 11, 2026

`androidx.wear.watchfacepush:watchfacepush:1.0.0-rc01` is released with no changes from the previous beta. Version 1.0.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..17bd646a50810d4ad3ef4974404f4d7047eff303/wear/watchfacepush/watchfacepush).

### Version 1.0.0-beta01

December 03, 2025

`androidx.wear.watchfacepush:watchfacepush:1.0.0-beta01` is released. Version 1.0.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb..deb96499dfe95073f5c1215c1287787683cb1e92/wear/watchfacepush/watchfacepush).

**API Changes**

* Lower watchfacepush `minSdk` to 33. Introduce an `isSupported` method to check if the functionality is supported on the device, which returns false for sdk<36 (Wear OS 6 / Android 16). This allows clients to set their `minSdk` lower and conditionally use watchfacepush where supported. ([I0e8c0](https://android-review.googlesource.com/#/q/I0e8c05370ec52a758427f71238e150a3a849834c), [b/438149344](https://issuetracker.google.com/issues/438149344))

### Version 1.0.0-alpha01

June 18, 2025

`androidx.wear.watchfacepush:watchfacepush:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8af6ab7417811bf386c52a59ab5d0b94d194eeb/wear/watchfacepush/watchfacepush).

**API Changes**

* Added the Watch Face Push API which allows a Wear OS app to install a watch face on a watch programmatically.
* The API was previously published as `:wear:watchface:watchface-push`