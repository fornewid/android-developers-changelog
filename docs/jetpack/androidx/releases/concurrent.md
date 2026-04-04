---
title: https://developer.android.com/jetpack/androidx/releases/concurrent
url: https://developer.android.com/jetpack/androidx/releases/concurrent
source: md.txt
---

# Concurrent

# Concurrent

API Reference  
[androidx.concurrent](https://developer.android.com/reference/kotlin/androidx/concurrent/futures/package-summary)  
Move tasks off the main thread with coroutines and take advantage of ListenableFuture.  

| Latest Update |                                  Stable Release                                   | Release Candidate | Beta Release | Alpha Release |
|---------------|-----------------------------------------------------------------------------------|-------------------|--------------|---------------|
| July 16, 2025 | [1.3.0](https://developer.android.com/jetpack/androidx/releases/concurrent#1.3.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Futures, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.concurrent:concurrent-futures:1.3.0"

    // Kotlin
    implementation "androidx.concurrent:concurrent-futures-ktx:1.3.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.concurrent:concurrent-futures:1.3.0")

    // Kotlin
    implementation("androidx.concurrent:concurrent-futures-ktx:1.3.0")
}
```

For more information about dependencies, see[Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:790637+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=790637&template=1378722)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.3

### Version 1.3.0

July 16, 2025

`androidx.concurrent:concurrent-futures:1.3.0`and`androidx.concurrent:concurrent-futures-ktx:1.3.0`are released. Version 1.3.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/149916a17e3b8d9820c19e689be2dc0c64d4b40c..6d6c8782f1e2f710a8f305225f8cf20699dbafb2/concurrent).

### Version 1.3.0-rc01

July 2, 2025

`androidx.concurrent:concurrent-futures:1.3.0-rc01`and`androidx.concurrent:concurrent-futures-ktx:1.3.0-rc01`are released. Version 1.3.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/d9489d3b515bfdf6acfda6613e0ce61413328c42..149916a17e3b8d9820c19e689be2dc0c64d4b40c/concurrent).

### Version 1.3.0-beta01

May 20, 2025

`androidx.concurrent:concurrent-futures:1.3.0-beta01`and`androidx.concurrent:concurrent-futures-ktx:1.3.0-beta01`are released. Version 1.3.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..d9489d3b515bfdf6acfda6613e0ce61413328c42/concurrent).

### Version 1.3.0-alpha01

December 11, 2024

`androidx.concurrent:concurrent-futures:1.3.0-alpha01`and`androidx.concurrent:concurrent-futures-ktx:1.3.0-alpha01`are released. Version 1.3.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3f60b391b39a0d5c6bbb3bb9f83f227a0c8a72b..46295bc0b75a16f452e8e0090e8de41073d4dbb6/concurrent).

**Bug Fixes**

- This library now uses[JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage:`-Xjspecify-annotations=strict`(this is the default starting with version 2.1.0 of the Kotlin compiler). ([I0faf4](https://android-review.googlesource.com/#/q/I0faf40c26ac0d0e45f1e549ef2c4d04df653d2f3),[b/326456246](https://issuetracker.google.com/issues/326456246))

## Version 1.2

### Version 1.2.0

June 12, 2024

`androidx.concurrent:concurrent-futures:1.2.0`and`androidx.concurrent:concurrent-futures-ktx:1.2.0`are released. Version 1.2.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/981a26f286d763f3ebe90ef825c12873ae8fd171..f3f60b391b39a0d5c6bbb3bb9f83f227a0c8a72b/concurrent).

**Important changes since 1.1.0**

- Added[`SuspendToFutureAdapter`](https://developer.android.com/reference/kotlin/androidx/concurrent/futures/SuspendToFutureAdapter)for translating a call to a suspending API into a`ListenableFuture`.

### Version 1.2.0-rc01

May 29, 2024

`androidx.concurrent:concurrent-futures:1.2.0-rc01`and`androidx.concurrent:concurrent-futures-ktx:1.2.0-rc01`are released. Version 1.2.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..981a26f286d763f3ebe90ef825c12873ae8fd171/concurrent).

### Version 1.2.0-beta01

May 14, 2024

`androidx.concurrent:concurrent-futures:1.2.0-beta01`and`androidx.concurrent:concurrent-futures-ktx:1.2.0-beta01`are released. Version 1.2.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/concurrent).

### Version 1.2.0-alpha03

March 20, 2024

`androidx.concurrent:concurrent-futures:1.2.0-alpha03`and`androidx.concurrent:concurrent-futures-ktx:1.2.0-alpha03`are released. Version 1.2.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..a57d7d17753695012b58c9ce7ad55a8d39157e62/concurrent).

**Bug Fixes**

- Fixed a bug in error handling when a`SuspendToFutureAdapter`task throws an exception. ([b/327629504](https://issuetracker.google.com/issues/327629504))

### Version 1.2.0-alpha02

August 9, 2023

`androidx.concurrent:concurrent-futures:1.2.0-alpha02`and`androidx.concurrent:concurrent-futures-ktx:1.2.0-alpha02`are released.[Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..5d7dd999525725bd038a00ca4e89e0fef624a6da/concurrent)

**API Changes**

- Added`SuspendToFutureAdapter`for writing suspend-`ListenableFuture`bridges ([Ia8a66](https://android-review.googlesource.com/#/q/Ia8a66143012dd3e5ceb2ba22a4a0d33ad7eb8fcc))

### Version 1.2.0-alpha01

February 22, 2023

`androidx.concurrent:concurrent-futures:1.2.0-alpha01`and`androidx.concurrent:concurrent-futures-ktx:1.2.0-alpha01`are released.[Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a14b33c6c6a435ff5409f18396180e9b61b1425a..87533b4ff06971ed59028936cd9b6da988cd4522/concurrent)

**API Changes**

- `ResolvableFuture`now has proper nullability annotations on its methods. ([I2339f](https://android-review.googlesource.com/#/q/I2339f5da0e113d629d0684409a5193ae31c29820),[b/236474470](https://issuetracker.google.com/issues/236474470))

## Version 1.1.0

### Version 1.1.0

August 19, 2020

`androidx.concurrent:concurrent-futures:1.1.0`and`androidx.concurrent:concurrent-futures-ktx:1.1.0`are released with no changes since`1.1.0-rc01`.[Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b1f7aa3fc45314f510e1e742b96939468c1f7679..a14b33c6c6a435ff5409f18396180e9b61b1425a/concurrent)

**Major changes since 1.0.0**

- `1.1.0`introduces Kotlin extensions to help convert between ListenableFuture and Kotlin Coroutines, now available with`androidx.concurrent:concurrent-futures-ktx:1.1.0`. This artifact is meant to be used with`com.google.guava:listenablefuture`as opposed to the full Guava library, which is a lightweight substitute for Guava that only contains ListenableFuture. For users of the full Guava library, you should use the official ListenableFuture extensions from`kotlinx.coroutines.kotlinx-coroutines-guava`instead.

### Version 1.1.0-rc01

July 22, 2020

`androidx.concurrent:concurrent-futures:1.1.0-rc01`and`androidx.concurrent:concurrent-futures-ktx:1.1.0-rc01`are released with no changes since`1.1.0-beta01`.[Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..b1f7aa3fc45314f510e1e742b96939468c1f7679/concurrent)

### Version 1.1.0-beta01

June 24, 2020

`androidx.concurrent:concurrent-futures:1.1.0-beta01`and`androidx.concurrent:concurrent-futures-ktx:1.1.0-beta01`are released with no changes since`1.1.0-alpha01`.[Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/740cde70237dd276f8ad66dfe9528b1cdb5d54bb..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/concurrent)

### Version 1.1.0-alpha01

December 18, 2019

`androidx.concurrent:concurrent-futures:1.1.0-alpha01`and`androidx.concurrent:concurrent-futures-ktx:1.1.0-alpha01`are released.[Version 1.1.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/631e6dd8dd3e57789af36d56a8d720da1c37cbd5..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/concurrent). This is first release of`androidx.concurrent:concurrent-futures-ktx`.

**New features**

- Kotlin extensions to help convert between ListenableFuture and Kotlin Coroutines are now available in`concurrent-futures-ktx`. This artifact is meant to be used with`com.google.guava:listenablefuture`as opposed to the full Guava library, which is a lightweight substitute for Guava that only contains`ListenableFuture`. For users of the full Guava library, you should use the official ListenableFuture extensions from`kotlinx.coroutines.kotlinx-coroutines-guava`instead.

**API changes**

- Adds a suspending`ListenableFuture.await()`extension which converts a ListenableFuture to a Kotlin Coroutine

## Version 1.0.0

### Version 1.0.0

October 9, 2019

`androidx.concurrent:concurrent-futures:1.0.0`is released.[Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/631e6dd8dd3e57789af36d56a8d720da1c37cbd5..42110456c2e1d47872fd667326ec179e2bca32b3/concurrent/futures).

**Important features of 1.0.0**

`androidx.concurrent:concurrent-futures:1.0.0`provides`CallbackToFutureAdapter`class, a minimalistic utility that allows to wrap callback based code and return instances of`ListenableFuture`. It is useful for libraries that would like to expose asynchronous operations in their java APIs in a more elegant way than custom callbacks, but don't do enough multithreading heavy-lifting to take a dependency on full guava or rx java due to library size concerns.

### Version 1.0.0-rc01

August 7, 2019

`androidx.concurrent:concurrent-futures:1.0.0-rc01`is released with no changes from`1.0.0-beta01`. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/26b84a56581b60b44efe49f4ee63c95fa8dc8787..631e6dd8dd3e57789af36d56a8d720da1c37cbd5/concurrent/futures).

## Concurrent-ListenableFuture Version 1.0.0-beta01

May 30th, 2019

`androidx.concurrent:concurrent-listenablefuture:1.0.0-beta01`and`androidx.concurrent:concurrent-listenablefuture-callback:1.0.0-beta01`are released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/26b84a56581b60b44efe49f4ee63c95fa8dc8787..75e93a025020288fd9cd22580aabbcd7b11b4fd9/concurrent).

These libraries provide a standalone equivalent to Guava's[ListenableFuture](https://guava.dev/releases/23.1-android/api/docs/com/google/common/util/concurrent/ListenableFuture.html)interface and an adapter for converting callbacks.

The previously-released`androidx.concurrent:concurrent-futures`artifact, which provided a similar adapter and included the`com.google.guava:listenablefuture`artifact, may be problematic for developers using toolchains -- such as Android Gradle Plugin 3.4.0 -- with strict dependency resolution matching. Developers who do not rely on the full Guava library are advised to switch to`androidx.concurrent:concurrent-listenablefuture-callback`.

### Version 1.0.0-beta01

May 7, 2019

`androidx.concurrent:concurrent-futures:1.0.0-beta01`is released. The commits included in this version can be found[here](https://android.googlesource.com/platform/frameworks/support/+log/033f65978071d72164b3707a61d342844c9f2811..26b84a56581b60b44efe49f4ee63c95fa8dc8787/concurrent/futures).

**API changes**

- `ResolvableFuture`and`AbstractResolvableFuture`were hidden from public api in favor`CallbackToFutureAdapter`that provides safer API.

### Version 1.0.0-alpha03

December 17, 2018

`androidx.concurrent:concurrent-futures 1.0.0-alpha03`is released.

**New features**

- `CallbackToFutureAdapter`was introduced. It's a new, safer API to wrap a callback driven API into`ListenableFuture`. Prefer it over using`ResolvableFuture`.