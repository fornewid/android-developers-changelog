---
title: https://developer.android.com/jetpack/androidx/releases/metrics
url: https://developer.android.com/jetpack/androidx/releases/metrics
source: md.txt
---

# Metrics

# Metrics

API Reference  
[androidx.metrics.performance](https://developer.android.com/reference/kotlin/androidx/metrics/performance/package-summary)  
Track and report various runtime metrics for your application  

|  Latest Update  |                                 Stable Release                                 | Release Candidate | Beta Release | Alpha Release |
|-----------------|--------------------------------------------------------------------------------|-------------------|--------------|---------------|
| October 8, 2025 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/metrics#1.0.0) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on Metrics, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    implementation "androidx.metrics:metrics-performance:1.0.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.metrics:metrics-performance:1.0.0")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:1109743+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1109743&template=1621342)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 1.0.0

### Version 1.0.0

October 08, 2025

`androidx.metrics:metrics-performance:1.0.0`is released. Version 1.0.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/599dbe3f97c08376b43e35a077420c0983df515d..45d9ff85a8fad0fe921ab094f57d33dade94babd/metrics/metrics-performance).

**Major features of 1.0.0:**

- The JankStats API allows you to measure frame performance of your app, and add context (what's happening, and where frames are being produced) into performance metrics. For more information, see the documentation.

### Version 1.0.0-rc01

September 24, 2025

`androidx.metrics:metrics-performance:1.0.0-rc01`is released. Version 1.0.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b02262f9c0b8d35ab8586b077922409e5f6612a9..599dbe3f97c08376b43e35a077420c0983df515d/metrics/metrics-performance).

### Version 1.0.0-beta04

September 10, 2025

`androidx.metrics:metrics-performance:1.0.0-beta04`is released. Version 1.0.0-beta04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..b02262f9c0b8d35ab8586b077922409e5f6612a9/metrics/metrics-performance).

**External Contribution**

- Fixes`IndexOutOfBoundsException`in`JankStats`([I113e5](https://android-review.googlesource.com/#/q/I113e5fa7f7ba2ad27d7830c0ba6fe7386e0e4802),[b/253576508](https://issuetracker.google.com/issues/253576508))

### Version 1.0.0-beta03

August 27, 2025

`androidx.metrics:metrics-performance:1.0.0-beta03`is released. Version 1.0.0-beta03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/metrics/metrics-performance).

**Bug Fixes**

- Fix`IllegalArgumentException`("attempt to remove`OnFrameMetricsAvailableListener`that was never added"). No attempt is made to record frame timing when a window isn't hardware accelerated, as this isn't supported by`Window.OnFrameMetricsAvailableListener`. ([I8fef2](https://android-review.googlesource.com/#/q/I8fef2d16449a9a50a2092200d28e45baae537e22),[b/436880904](https://issuetracker.google.com/issues/436880904))

### Version 1.0.0-beta02

March 12, 2025

`androidx.metrics:metrics-performance:1.0.0-beta02`is released. Version 1.0.0-beta02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..7a145e052ae61e272e91ffe285e9451b8ab71870/metrics/metrics-performance).

**Bug Fixes**

- Fix crashes`DelegatingFrameMetricsListener cannot be cast...`([Id891c](https://android-review.googlesource.com/#/q/Id891c0cfdd7f45ef9e3b068644a113f39c8fc383),[b/311218678](https://issuetracker.google.com/issues/311218678)).

### Version 1.0.0-beta01

January 10, 2024

The API and functionality of this library has been stable for some time. This release simply pushes the library to beta.

`androidx.metrics:metrics-performance:1.0.0-beta01`is released.[Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/metrics/metrics-performance)

### Version 1.0.0-alpha04

April 5, 2023

This release updates JankStats to the latest fixes, which include more accurate and comprehensive timing information.

`androidx.metrics:metrics-performance:1.0.0-alpha04`is released.[Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..a200cb82769634cecdb118ec4f0bfdf0b086e597/metrics/metrics-performance)

**API Changes**

- `cpuDuration`now more accurate, also new`totalDuration`on API31 ([I59ce8](https://android-review.googlesource.com/#/q/I59ce8c67f06a168f96893375c8aeca5516a55d81),[b/243694893](https://issuetracker.google.com/issues/243694893))

### Version 1.0.0-alpha03

July 27, 2022

`androidx.metrics:metrics-performance:1.0.0-alpha03`is released.[Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/metrics/metrics-performance)

- This release contains minor API refinements as the library gets closer to beta. One of the API changes removes the Executor from the`createAndTrack()`factory method for creating a`JankStats`object. This has implications for the`OnFrameListener`callback, as that listener is now called on the thread which delivers the per-frame data to`JankStats`(the Main/UI thread on versions earlier than API 24, and the`FrameMetrics`thread on API 24+). Moreover, the`FrameData`object passed to the listener is now reused every frame, so data from that object must be copied and cached elsewhere during the callback, as that object should be considered obsolete as soon as the listener returns.

- There were also various bug fixes, including some concurrency issues.

- Finally, the fix to reuse`FrameData`(mentioned above) means that there are now zero allocations per frame due to frame metrics delivery. There weren't many allocations before, but the new approach means that you can use`JankStats`without incurring any per-frame GC overhead in your app.

**API Changes**

- Updated method and parameter names in`PerformanceMetricsState`to make the results of those calls clearer. ([I56da5](https://android-review.googlesource.com/#/q/I56da57b13818bf4077a64ab144222ce255f4539a),[b/233421985](https://issuetracker.google.com/issues/233421985))
- Added benchmark tests to track allocations, eliminated some internal allocations related to state management and reporting. Note that`FrameData`passed to listeners is now considered volatile; that structure will be reused for the next frame and the data is only reliable until the listener returns.
- Removed Executor from constructor for`JankStats`; listeners are now called on whatever thread the internal data was received upon. ([I12743](https://android-review.googlesource.com/#/q/I1274320bf29c171b82578868e657a3b01f7805c7))

**Bug Fixes**

- Fixed crash due to double-removal of`OnFrameMetricsAvailableListener`([I44094](https://android-review.googlesource.com/#/q/I4409483d6e2f7287a0a93f521f68a4be9e22d969),[b/239457413](https://issuetracker.google.com/issues/239457413))
- Return to original logic of posting`OnPreDrawListener`messages at front of queue, for more consistent and predictable frame timing. ([I05a43](https://android-review.googlesource.com/#/q/I05a434fe9453ea1be28d398e3eb284dd9b0cb64a),[b/233358407](https://issuetracker.google.com/issues/233358407))
- Fixed`ConcurrentModificationException`bug where the list of listener delegates was being modified while it was also being iterated through to send per-frame data. ([Ib7693](https://android-review.googlesource.com/#/q/Ib769386f18e51dc6b58c935b42c5b8566c644abc),[b/236612357](https://issuetracker.google.com/issues/236612357))

### Version 1.0.0-alpha02

June 29, 2022

`androidx.metrics:metrics-performance:1.0.0-alpha02`is released.[Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..8094b683499b4098092c01028b55a38b49e357f2/metrics/metrics-performance)

**API Changes**

- Renamed`MetricsStateHolder`to just Holder (within`PerformanceMetricsState`): ([I5a4d9](https://android-review.googlesource.com/#/q/I5a4d9095520399a146e6fd78eb50c86a7051738b),[b/226565716](https://issuetracker.google.com/issues/226565716),[b/213499234](https://issuetracker.google.com/issues/213499234))

**Bug Fixes**

- Fixed timing issue where states could be replaced with new values before the frames had been processed where the old state would have been correct ([aosp/2061892](https://android-review.googlesource.com/c/platform/frameworks/support/+/2061892/),[b/213499234](https://issuetracker.google.com/issues/213499234))
- Fixed concurrent modification exception in adding/removing listeners ([aosp/2092714](https://android-review.googlesource.com/c/platform/frameworks/support/+/2092714/),[b/213499234](https://issuetracker.google.com/issues/230388846))
- Made startTime calculations more accurate ([aosp/2027704](https://android-review.googlesource.com/c/platform/frameworks/support/+/2027704/),[b/213245198](https://issuetracker.google.com/issues/213245198))
- Fixed bug in`FrameData.equals()`implementation ([aosp/2025866](https://android-review.googlesource.com/c/platform/frameworks/support/+/2025866/),[b/218296544](https://issuetracker.google.com/issues/218296544))

### Version 1.0.0-alpha01

February 9, 2022

`androidx.metrics:metrics-performance:1.0.0-alpha01`is released.[Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c/metrics/metrics-performance)

**New Features**

- The`JankStats`library provides functionality to instrument and receive callbacks in your application at runtime which can help find real world performance problems.
- `JankStats`combines an API that makes it easy to inject information about UI state with capabilities for tracking and reporting per-frame performance to allow developers to understand not whether an application has performance issues, but when and why.