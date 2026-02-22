---
title: https://developer.android.com/jetpack/androidx/releases/work
url: https://developer.android.com/jetpack/androidx/releases/work
source: md.txt
---

# WorkManager

[User Guide](https://developer.android.com/topic/libraries/architecture/workmanager) [Code Sample](https://github.com/android/architecture-components-samples/tree/main/WorkManagerSample) [Codelab](https://codelabs.developers.google.com/codelabs/android-workmanager/#0)  
API Reference  
[androidx.work](https://developer.android.com/reference/kotlin/androidx/work/package-summary)  
[androidx.work.testing](https://developer.android.com/reference/kotlin/androidx/work/testing/package-summary)  
The WorkManager API makes it easy to schedule deferrable, asynchronous tasks that must be run reliably. These APIs let you create a task and hand it off to WorkManager to run when the work constraints are met.  
| **Note:** WorkManager requires `compileSdk` version 33 or higher.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| January 28, 2026 | [2.11.1](https://developer.android.com/jetpack/androidx/releases/work#2.11.1) | - | - | - |

## Declaring dependencies

To add a dependency on WorkManager, you must add the [Google Maven repository](https://developer.android.com/studio/build/dependencies#google-maven) to your
project:

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:  

### Groovy

```groovy
dependencies {
    def work_version = "2.11.1"

    // (Java only)
    implementation "androidx.work:work-runtime:$work_version"

    // Kotlin + coroutines
    implementation "androidx.work:work-runtime-ktx:$work_version"

    // optional - RxJava2 support
    implementation "androidx.work:work-rxjava2:$work_version"

    // optional - GCMNetworkManager support
    implementation "androidx.work:work-gcm:$work_version"

    // optional - Test helpers
    androidTestImplementation "androidx.work:work-testing:$work_version"

    // optional - Multiprocess support
    implementation "androidx.work:work-multiprocess:$work_version"
}
```

### Kotlin

```kotlin
dependencies {
    val work_version = "2.11.1"

    // (Java only)
    implementation("androidx.work:work-runtime:$work_version")

    // Kotlin + coroutines
    implementation("androidx.work:work-runtime-ktx:$work_version")

    // optional - RxJava2 support
    implementation("androidx.work:work-rxjava2:$work_version")

    // optional - GCMNetworkManager support
    implementation("androidx.work:work-gcm:$work_version")

    // optional - Test helpers
    androidTestImplementation("androidx.work:work-testing:$work_version")

    // optional - Multiprocess support
    implementation("androidx.work:work-multiprocess:$work_version")
}
```

For information on using Kotlin extensions, see the [ktx documentation](https://developer.android.com/kotlin/ktx).

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:409906+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=409906&template=1094197)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 2.11

### Version 2.11.1

January 28, 2026

`androidx.work:work-*:2.11.1` is released. Version 2.11.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d99a439061701df265e4fb9fcab131bac078be6b..5a3057b3fba2ecd31580689419aff5f082f9efdc/work).

**Bug Fixes**

- Fix network state constraint from passing while connectivity is blocked on Android 15 and above. ([I5abb7](https://android-review.googlesource.com/#/q/I5abb7f65b095a0feefa8e2645baa742f48049cae), [b/465016918](https://issuetracker.google.com/issues/465016918))
- Fixed network constraint tracking not considering blocked state for its initial value. ([I8a0a2](https://android-review.googlesource.com/#/q/I8a0a2c029957335892d12a2df33a23ae0b77ab3e), [b/452081708](https://issuetracker.google.com/issues/452081708))
- Fixed an issue with network request constraint passing while connectivity is blocked on Android 15 and above. ([I60f24](https://android-review.googlesource.com/#/q/I60f241226361660db8513575fd4f8095b340069e), [b/452081708](https://issuetracker.google.com/issues/452081708))

### Version 2.11.0

October 22, 2025

`androidx.work:work-*:2.11.0` is released. Version 2.11.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f91a1f9067864cf67439d16cefe16d1a7edeac07..d99a439061701df265e4fb9fcab131bac078be6b/work).

**Important changes since 2.10.0:**

- The `minSdk` has been updated from API 21 to API 23.
- The API `setRemoteSessionTimeoutMillis` in `WorkManager`'s Configuration builder has been added to enable configuring the amount of time a `RemoteWorkManager` session is alive from its last usage.

### Version 2.11.0-rc01

October 08, 2025

`androidx.work:work-*:2.11.0-rc01` is released. Version 2.11.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a..f0a129e54680c04c425b93e84ca7f2a32a0a25dd/work).

### Version 2.11.0-beta01

September 24, 2025

`androidx.work:work-*:2.11.0-beta01` is released. Version 2.11.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..3ee4b76dd7f79cd4ce3fbe7aa76816fec0b8186a/work).

**API Changes**

- Add `stopRunningWorkWithReason` to `WorkManager` `TestDriver`. ([Ie53b2](https://android-review.googlesource.com/#/q/Ie53b2b9cacbbc0a8273826e0eeaf33ffcb1358e2), [b/439955564](https://issuetracker.google.com/issues/439955564))

**Bug Fixes**

- Fix foreground service stopping when there are pending commands ([Iae822](https://android-review.googlesource.com/#/q/Iae822d63398e81ea0f1810c4d3cb4e0dafd4e13f), [b/432069314](https://issuetracker.google.com/issues/432069314))
- Fix remote coroutine worker failing to unbind remote service ([I842f2](https://android-review.googlesource.com/#/q/I842f29aa5c8b26fbe467758f335ae0380ffc839f), [b/247113322](https://issuetracker.google.com/issues/247113322))

### Version 2.11.0-alpha01

August 27, 2025

`androidx.work:work-*:2.11.0-alpha01` is released. Version 2.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f1db959e4b5791abbb290ef4b40786c998b481ea..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/work).

**API Changes**

- The minSdk has been updated from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- The API `setRemoteSessionTimeoutMillis` in WorkManager's Configuration builder has been added to enable configuring the amount of time a RemoteWorkManager session is alive from its last usage. ([Ib23c8](https://android-review.googlesource.com/#/q/Ib23c8c189ea4e5a72e0add5fc6fa0eaf0ee274d4))
- Add an experimental API in `WorkRequest.Builder` to apply backoff when work is interrupted by the system. ([Ie2dc7](https://android-review.googlesource.com/#/q/Ie2dc722282f520427d1758cd3d108e0147ed4646), [b/335513480](https://issuetracker.google.com/issues/335513480))
- Add test API to pass in a different worker class to `TestListenableWorkerBuilder` than the one being built to support custom `WorkerFactory` implementations ([If6bff](https://android-review.googlesource.com/#/q/If6bffd90f15ecacbbec8734a9649b1dc2dc4fd21), [b/389154854](https://issuetracker.google.com/issues/389154854))

**Bug Fixes**

- Cache network capabilities in `SharedNetworkCallback` to prevent unnecessary IPCs ([Ie4027](https://android-review.googlesource.com/#/q/Ie40279799b98b888bc15fbc51a9ca48d4c6b0bde), [b/427115602](https://issuetracker.google.com/issues/427115602))
- Fix an issue with network constraint evaluation where work items after the first would not get the current network capabilities and would instead hit `ConstraintsNotMet` after a timeout ([Ib6a66](https://android-review.googlesource.com/#/q/Ib6a66aab60bc960481cb6eca4c9e9a83fa0cee20), [b/427115602](https://issuetracker.google.com/issues/427115602))

## Version 2.10

### Version 2.10.5

September 24, 2025

`androidx.work:work-*:2.10.5` is released. Version 2.10.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/09848ba38e78a66330c95fe6461d8094f6f195d1..f91a1f9067864cf67439d16cefe16d1a7edeac07/work).

**Bug Fixes**

- Fix foreground service stopping when there are pending commands ([Iae822](https://android-review.googlesource.com/#/q/Iae822d63398e81ea0f1810c4d3cb4e0dafd4e13f), [b/432069314](https://issuetracker.google.com/issues/432069314))

### Version 2.10.4

September 10, 2025

`androidx.work:work-*:2.10.4` is released. Version 2.10.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f1db959e4b5791abbb290ef4b40786c998b481ea..09848ba38e78a66330c95fe6461d8094f6f195d1/work).

**Bug Fixes**

- Fix an issue with `RemoteCoroutineWorker` failing to unbind remote service ([I842f2](https://android-review.googlesource.com/#/q/I842f29aa5c8b26fbe467758f335ae0380ffc839f), [b/247113322](https://issuetracker.google.com/issues/247113322))

### Version 2.10.3

July 30, 2025

`androidx.work:work-*:2.10.3` is released. Version 2.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e122c77cac1f7b853bd53087936209cf528c4843..f1db959e4b5791abbb290ef4b40786c998b481ea/work).

**Bug Fixes**

- Fix an issue where workers with identical network constraints as a previous worker would report their constraints not being met. ([b/427115602](https://issuetracker.google.com/427115602)).

### Version 2.10.2

June 18, 2025

`androidx.work:work-*:2.10.2` is released. Version 2.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b4aab61a00d34fcd7c591ac1600b53ffba42c2bf..e122c77cac1f7b853bd53087936209cf528c4843/work).

**Bug Fixes**

- Fix an issue when persisting workers with network requests and default capabilities that would lead to removed capabilities being re-added causing workers with network constraints to misbehave. ([b/409716532](https://issuetracker.google.com/409716532))
- Fix a bug that would cause workers with network constraints to not execute promptly due to constraints not met even though the network and capabilities were available. ([b/423403088](https://issuetracker.google.com/423403088))

### Version 2.10.1

April 23, 2025

`androidx.work:work-*:2.10.1` is released. Version 2.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/380219beddae76ab6e6c9d16b8acbf25489d988d..b4aab61a00d34fcd7c591ac1600b53ffba42c2bf/work).

**Bug Fixes**

- Reduce the possibility of `TooManyRequestsException` being thrown from `WorkManager`'s registration of a `NetworkCallback` used for constraint tracking. ([b/231499040](https://issuetracker.google.com/231499040), [b309d5](https://android-review.googlesource.com/#/q/b309d5876cf79ae71643b79a220c7811ada71f50)).

### Version 2.10.0

October 30, 2024

`androidx.work:work-*:2.10.0` is released. Version 2.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/61fffa80db30c92b3f06eb44b8f108dcdb33410e..380219beddae76ab6e6c9d16b8acbf25489d988d/work).

Significant changes since version 2.9.1

- Added trace tags to Jobs from `WorkManager` which makes 'adb shell dumpsys jobscheduler' a lot simpler to understand since it will contain the name of the Worker being executed. Trace sections are also added around key areas of `WorkManager`.
- `Configuration.workerCoroutineContext` was added to for control of dispatcher where `CoroutineWorker` is executed.
- Developers can specify `NetworkRequest` as a constraint for a worker via the `Constraints.setRequiredNetworkRequest` method. This enables more granular control over which network this worker should run.
- `WorkManager` 2.10.0 is now compiled with SDK 35 and contain various changes for SDK 35 compatibility.

### Version 2.10.0-rc01

October 24, 2024

`androidx.work:work-*:2.10.0-rc01` is released. Version 2.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..61fffa80db30c92b3f06eb44b8f108dcdb33410e/work).

### Version 2.10.0-beta01

October 2, 2024

`androidx.work:work-*:2.10.0-beta01` is released. Version 2.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/work).

### Version 2.10.0-alpha04

September 18, 2024

`androidx.work:work-*:2.10.0-alpha04` is released. Version 2.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..0431b84980e97d6bafdfda7c9038bc4d9529564f/work).

**API Changes**

- Add the stop reason `STOP_REASON_FOREGROUND_SERVICE_TIMEOUT` for when a foreground worker is stopped due to execution timeout based on the foreground service type. ([Ibd0af](https://android-review.googlesource.com/#/q/Ibd0afaa7c32fa41562d8386abea524cbd1bbe679))

### Version 2.10.0-alpha03

September 4, 2024

`androidx.work:work-*:2.10.0-alpha03` is released. Version 2.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4584e40d8375770d35077900321f49bce0bd10c7..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/work).

**New Features**

- Added trace tags to Jobs from `WorkManager` which makes 'adb shell dumpsys jobscheduler' a lot simpler to understand since it will contain the name of the Worker being executed. Trace sections are also added around key areas of `WorkManager`.

**API Changes**

- WorkManager 2.10.0 is now compiled with SDK 35.
- Fix foreground workers of type 'short service' and 'data sync' timing out and causing an ANR when `WorkManager` didn't call `stopSelf()`. This fix only applies to devices with API 34 and 35 where foreground service types were introduced. ([ca06b2](https://android-review.googlesource.com/#/q/Ibd046586fe2851467948fdd6f70f98be4dca06b2), [b/364508145](https://issuetracker.google.com/issues/364508145))
- New `WorkerParameters` APIs that make it possible to switch the remote process that the `Worker` binds to when using a `WorkerFactory`. ([Ibdc8a](https://android-review.googlesource.com/#/q/Ibdc8abb7966e8d3af41d0d93354d699a0426f303), [Ie8a90](https://android-review.googlesource.com/#/q/Ie8a908627ca30ccc711ebbdaf8df4f8fa24e662f), [I7373f](https://android-review.googlesource.com/#/q/I7373f2fa1db38f5649cb6091bb69d58999b2ddba))

**Bug Fixes**

- Fix a crash caused by `WorkManager` attempting to restart a long-running worker (i.e. a foreground worker) when the foreground type of the work had Android 14 prerequisite permissions that were revoked. ([b/333957914](https://issuetracker.google.com/issues/333957914))
- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([Ia60e0](https://android-review.googlesource.com/#/q/Ia60e0ab9f0fd613883a772c8aa34e27cc986cae8), [b/345472586](https://issuetracker.google.com/issues/345472586))

### Version 2.10.0-alpha02

April 17, 2024

`androidx.work:work-*:2.10.0-alpha02` is released. Version 2.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..4584e40d8375770d35077900321f49bce0bd10c7/work).

**API Changes**

- Added the ability to emit trace spans via a configurable `@RestrictTo` `Tracer` in `WorkManager`. ([I17d7f](https://android-review.googlesource.com/#/q/I17d7f0ec2b1947d09d568ca1f69ea6fee64c713c), [b/260214125](https://issuetracker.google.com/issues/260214125))
- `Configuration.workerCoroutineContext` was added to for control of dispatcher where `CoroutineWorker` is executed. It helps to completely avoid usage of `Dispatchers.Default` in `WorkManager`. ([Icd1b7](https://android-review.googlesource.com/#/q/Icd1b7755fc90ea71ac2e8509c0f21d3e60ca8d53))
- Add custom exception handlers for Workers ([Ib1b74](https://android-review.googlesource.com/#/q/Ib1b740f0503757bcc2baa90482a4e7b8d6002ffb), [b/261190695](https://issuetracker.google.com/issues/261190695))
- `OneTimeWorkRequest.Builder` and `PeriodicWorkRequest.Builder` can now be constructed with `KClass` instead of `Class`: `val request = OneTimeWorkRequest.Builder(Worker::class).setConstraints(...).build()` ([Ib55f6](https://android-review.googlesource.com/#/q/Ib55f6bb22dd629b4b3bfd94fb2480a6cfe222dc6))
- `WorkManager` class was migrated to Kotlin. Now methods that return `LiveData`, `ListenableFuture` or `Flow` provides correct nullability information. It could require changes in clients' source code, if nullability assumptions in that code were incorrect. ([If6757](https://android-review.googlesource.com/#/q/If6757e6713968ebe46b37ad1605d0db430c23e38))

### Version 2.10.0-alpha01

January 24, 2024

`androidx.work:work-*:2.10.0-alpha01` is released. [Version 2.10.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8dd90c8d04c2e85019a84ac8f4b01df8932f1899..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/work)

**New Features**

- Developers can specify `NetworkRequest` as a constraint for a worker via the `Constraints.setRequiredNetworkRequest` method. This enables more granular control over which network this worker should run.

**API Changes**

- Adding an ability to specify `NetworkRequest` as the constraint. ([Id98a1](https://android-review.googlesource.com/#/q/Id98a186c963c6472ead2392eccf37ae0e88048eb), [b/280634452](https://issuetracker.google.com/issues/280634452))

## Version 2.9

### Version 2.9.1

August 7, 2024

`androidx.work:work-*:2.9.1` is released. Version 2.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8dd90c8d04c2e85019a84ac8f4b01df8932f1899..a49fcf4e9a5dfa41c06e805d706d21d68e5cc6fb/work).

**Bug Fixes**

- Fix a crash caused by `WorkManager` attempting to restart a long-running worker (i.e. a foreground worker) when the foreground type of the work had [Android 14 prerequisite permissions](https://developer.android.com/about/versions/14/changes/fgs-types-required#system-runtime-checks) that were revoked. ([b/333957914](https://issuetracker.google.com/333957914))

### Version 2.9.0

November 29, 2023

`androidx.work:work-*:2.9.0` is released. [Version 2.9.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b5fbfa0dbb62c3a185a0be13fb1a63f50b2c034..8dd90c8d04c2e85019a84ac8f4b01df8932f1899/work)

**Important changes since 2.8.0**

- Observability via `Flow`-s. Instead of `LiveData`, Worker's progress now can be observed via Flow's via `WorkManager.getWorkInfosFlow` and similar methods.
- Now `WorkManager` provides a hint on why a worker was previously stopped. It can be queried from a worker itself via `getStopReason()` method or from `WorkInfo` via `getStopReason()`.
- Precise scheduling of periodic workers via `setNextScheduleTimeOverride`. This allows dynamic calculation of the next Periodic work schedule, which can be used to implement advanced features like adaptive refresh times, custom retry behavior, or making a newsfeed worker run before the user wakes up every morning without drift. `ExistingPeriodicWorkPolicy.UPDATE` should be used with these techniques to avoid canceling a currently-running worker while scheduling the next one.
- WorkManager's testing with threading matching production. `ExecutorsMode.PRESERVE_EXECUTORS` can be used in `initializeTestWorkManager` to preserve executors set in `Configuration` and to use the real main thread.
- Coroutines APIs such as `CoroutineWorker` have been moved from additional artifact work-runtime-ktx to the main artifact work-runtime. work-runtime-ktx is now empty.

**API Changes**

- `stopReason` was added to `WorkInfo`. It makes `stopReason` available after the worker has run. It could be helpful in the reporting `stopReason` in a usable way, because once a worker has been stopped, an app itself could be killed very quickly. ([I21386](https://android-review.googlesource.com/#/q/I213869adf99dd675b705f6d7f7a080c7bed88220))
- Allow `Clock` to be set via config and used to drive execution sequencing of Worker tests. ([Ic586e](https://android-review.googlesource.com/#/q/Ic586efd1c81ac21ece399f4d74f0d2d8bdb1e5ea))
- `getStopReason()` method was added to `ListenableWorker` that gives a hint why the worker was stopped. ([I07060](https://android-review.googlesource.com/#/q/I070605b2337c30c496c02bef142167f65c23cf5e))
- Added `WorkManagerTestInitHelper#closeWorkDatabase()` to avoid Closeguard's warning about leaked resources. ([Ia8d49](https://android-review.googlesource.com/#/q/Ia8d49b6054df11ab5a67c8960c6317b515aa14b6))
- `WorkInfo`'s constructor is public now, which can be useful in testing. ([Ia00b6](https://android-review.googlesource.com/#/q/Ia00b6beffca0b0b2dff5cdae67020bbd4b068579), [b/209145335](https://issuetracker.google.com/issues/209145335))
- `work-runtime-ktx` is now empty, `CoroutineWorker` and other Kotlin specific utilities are now available in the main work-runtime artifact. ([I71a9a](https://android-review.googlesource.com/#/q/I71a9a873fb3a68b1150ff6a0f9e62774393a17e8))
- Added `setNextScheduleTimeOverride` method, which allows accurate setting of periodic work schedules ([I3b4da](https://android-review.googlesource.com/#/q/I3b4da91bab9ffc6da3e305ef7ae814b59f7090fb))
- Added `getNextScheduleTimeMillis` to get scheduled run time info is added to `WorkInfo`. ([I797e4](https://android-review.googlesource.com/#/q/I797e4a88d7d96eb14ea4c689f7b64be038d4fbd8))
- Initial delay and periodicity info are added to `WorkInfo`. ([I52f2f](https://android-review.googlesource.com/#/q/I52f2f2f18f30dae132b6db4a11cc4c426e461ba6))
- Added method observe workers via Flows via methods `getWorkInfosByTagFlow`, `getWorkInfoByIdFlow`, `getWorkInfosForUniqueWorkFlow`, `getWorkInfosFlow` ([If122a](https://android-review.googlesource.com/#/q/If122a4bcc280e30c3721abec7bea6c7f1bbb4bd0))
- Added missing `@RequiresApi(...)` annotations to `Constraints`' constructors and properties. They are now aligned with corresponding annotations on setters in `Constraints.Builder` that existed from early versions of `WorkManager`. ([I6d7d2](https://android-review.googlesource.com/#/q/I6d7d23237c06a9cc197b30b054e213e96672a6dc))
- `WorkManager` now has a separate limit for content uri workers to give them guaranteed slots in `JobScheduler` to prevent missing content updates under the high load. The limit can be configured via `Configuration.Builder.setContentUriTriggerWorkersLimit`. ([Ic128f](https://android-review.googlesource.com/#/q/Ic128f0bd0095e17c01a6ed6ed30d5ac00cb9772c))
- Constraints are added to `WorkInfo`. ([I162c0](https://android-review.googlesource.com/#/q/I162c0d683dc5066f4f842f4431d25a9750633524))

### Version 2.9.0-rc01

October 18, 2023

`androidx.work:work-*:2.9.0-rc01` is released. [Version 2.9.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..2b5fbfa0dbb62c3a185a0be13fb1a63f50b2c034/work)

- No changes since the last beta release

### Version 2.9.0-beta01

September 6, 2023

`androidx.work:work-*:2.9.0-beta01` is released. [Version 2.9.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/work)

**API Changes**

- Added constants for stop reasons returned by [`WorkInfo.stopReason`](https://developer.android.com/reference/kotlin/androidx/work/WorkInfo#stopReason()) and [`ListenableWorker.stopReason`](https://developer.android.com/reference/kotlin/androidx/work/ListenableWorker#getStopReason()) ([I0cc00](https://android-review.googlesource.com/#/q/I0cc002a1db83766bb7af4632cd682eb57cbabdd6))

### Version 2.9.0-alpha02

July 26, 2023

`androidx.work:work-*:2.9.0-alpha02` is released. [Version 2.9.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..4aed940027a19667e67d155563fc5fa8b7279313/work)

**New Features**

- Now `WorkManager` provides a hint on why a worker was previously stopped. It can be queried from a worker itself via `getStopReason()` method or from `WorkInfo` via `getStopReason()`.

**API Changes**

- `stopReason` was added to `WorkInfo`. It makes available `stopReason` after the worker ran. It could be helpful in the reporting `stopReason` in usable way, because once a worker has been stopped, an app itself could be very quickly killed. ([I21386](https://android-review.googlesource.com/#/q/I213869adf99dd675b705f6d7f7a080c7bed88220))
- Allow Clock to be set via config and used to drive execution sequencing of Worker tests. ([Ic586e](https://android-review.googlesource.com/#/q/Ic586efd1c81ac21ece399f4d74f0d2d8bdb1e5ea))
- `getStopReason()` method was added to `ListenableWorker` that gives a hint why the worker was stopped. ([I07060](https://android-review.googlesource.com/#/q/I070605b2337c30c496c02bef142167f65c23cf5e))
- Added `WorkManagerTestInitHelper#closeWorkDatabase()` to avoid Closeguard's warning about leaked resources. ([Ia8d49](https://android-review.googlesource.com/#/q/Ia8d49b6054df11ab5a67c8960c6317b515aa14b6))

**Bug Fixes**

- Added ability to bypass `overrideNextScheduleTime` using `TestDriver` and fixed issues with testability. ([Ic2905](https://android-review.googlesource.com/#/q/Ic29056d338f5aeb6c1825f487d8f206908465141))

### Version 2.9.0-alpha01

June 7, 2023

`androidx.work:work-*:2.9.0-alpha01` is released. [Version 2.9.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/95d318f1c5a8a858d7224a452f3a9fc802d2caa1..73f902dee011bfe400d8a0330bfd8d4bb632065f/work)

**New Features**

- Observability via `Flow`-s. Instead of `LiveData`, Worker's progress now can be observed via Flow's via `WorkManager.getWorkInfosFlow` and similar methods.
- Precise scheduling of periodic workers via `setNextScheduleTimeOverride`. This allows dynamic calculation of the next Periodic work schedule, which can be used to implement advanced features like adaptive refresh times, custom retry behavior, or making a newsfeed worker run before the user wakes up every morning without drift. `ExistingPeriodicWorkPolicy.UPDATE` should be used with these techniques to avoid cancelling a currently-running worker while scheduling the next one.
- `WorkManager`'s testing with threading matching production. `ExecutorsMode.PRESERVE_EXECUTORS` can be used to preserve executors set in `Configuration` and to use the real main thread.
- Coroutines APIs such as `CoroutineWorker` have been moved from additional artifact `work-runtime-ktx` to the main artifact `work-runtime`. `work-runtime-ktx` is now empty.

**API Changes**

- `WorkInfo`'s constructor is public now, that can be useful in testing. ([Ia00b6](https://android-review.googlesource.com/#/q/Ia00b6beffca0b0b2dff5cdae67020bbd4b068579), [b/209145335](https://issuetracker.google.com/issues/209145335))
- `work-runtime-ktx` is now empty, `CoroutineWorker` and other kotlin specific utilities are now available in the main `work-runtime` artifact. ([I71a9a](https://android-review.googlesource.com/#/q/I71a9a873fb3a68b1150ff6a0f9e62774393a17e8))
- Added `setNextScheduleTimeOverride` method, which allows accurate setting of periodic work schedules ([I3b4da](https://android-review.googlesource.com/#/q/I3b4da91bab9ffc6da3e305ef7ae814b59f7090fb))
- Renamed `getEarliestRunTimeMillis` to `getNextScheduleTimeMillis`. ([I2bd7a](https://android-review.googlesource.com/#/q/I2bd7acdd5ee14021fa288aeafe97e48e175073c4))
- Next scheduled run time info is added to `WorkInfo`. ([I797e4](https://android-review.googlesource.com/#/q/I797e4a88d7d96eb14ea4c689f7b64be038d4fbd8))
- Initial delay and periodicity info are added to `WorkInfo`. ([I52f2f](https://android-review.googlesource.com/#/q/I52f2f2f18f30dae132b6db4a11cc4c426e461ba6))
- Added method observe workers via Flows via methods `getWorkInfosByTagFlow`, `getWorkInfoByIdFlow`, `getWorkInfosForUniqueWorkFlow`, `getWorkInfosFlow` ([If122a](https://android-review.googlesource.com/#/q/If122a4bcc280e30c3721abec7bea6c7f1bbb4bd0))
- Added missing `@RequiresApi(...)` annotations to Constraints' constructors and properties. They are now aligned with corresponding annotations on setters in `Constraints.Builder` that existed from early versions of `WorkManager`. ([I6d7d2](https://android-review.googlesource.com/#/q/I6d7d23237c06a9cc197b30b054e213e96672a6dc))
- `WorkManager` now has a separate limit for content uri workers to give them guaranteed slots in `JobScheduler` to prevent missing content updates under the high load. Limit can be configured via `Configuration.Builder.setContentUriTriggerWorkersLimit`. ([Ic128f](https://android-review.googlesource.com/#/q/Ic128f0bd0095e17c01a6ed6ed30d5ac00cb9772c))
- Constraints are added to `WorkInfo`. ([I162c0](https://android-review.googlesource.com/#/q/I162c0d683dc5066f4f842f4431d25a9750633524))

## Version 2.8

### Version 2.8.1

March 22, 2023

`androidx.work:work-*:2.8.1` is released. [Version 2.8.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d697ceaa517db5c8286395e186c5c8d8f85238fd..95d318f1c5a8a858d7224a452f3a9fc802d2caa1/work)

**Bug Fixes**

- Fixed ANR in `RescheduleReceiver` that previously didn't correctly handle two simultaneous broadcasts. ([b/236906724](https://issuetracker.google.com/issues/236906724))

### Version 2.8.0

February 8, 2023

`androidx.work:work-*:2.8.0` is released. [Version 2.8.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6809fb97f68a2d1a861e81cd6d32800039dcb09..d697ceaa517db5c8286395e186c5c8d8f85238fd/work)

**Important changes since 2.7.0**

**New Features**

- An ability to update `WorkRequests` in a non-intrusive way was added, preserving original enqueue time, chaining etc. See [detailed blogpost](https://developer.android.com/guide/background/persistent/how-to/update-work) about this feature, as well as javadocs for [`WorkManager.updateWork`](https://developer.android.com/reference/androidx/work/WorkManager#updateWork(androidx.work.WorkRequest)) and [`ExistingPeriodicWorkPolicy.UPDATE`](https://developer.android.com/reference/androidx/work/ExistingPeriodicWorkPolicy#UPDATE) for more details.

**API Changes**

- `WorkManager.updateWork` was added to update work preserving its original enqueue time and chaining.([I9a248](https://android-review.googlesource.com/c/platform/frameworks/support/+/2051581), [b/219446409](https://issuetracker.google.com/issues/219446409))
- `ExistingPeriodicWorkPolicy.UPDATE` was added. This policy allows updating a periodic work by the name. It is similar to the existing `REPLACE`, but it is less intrusive: it doesn't cancel a worker if it is currently running and it preserves enqueue time - initial delay and period are calculated from original enqueue time, rather than update time. `REPLACE` was deprecated to decrease a confusion between the very similarly named `REPLACE` and `UPDATE`. If you still want to keep the previous semantics of `REPLACE`, the newly added `CANCEL_AND_REENQUEUE`, which is identical to `REPLACE`, can be used. ([I985ed](https://android-review.googlesource.com/#/q/I985edc2cf7ac7c316932185f3fd0a3ca6660f2dc), [b/219446409](https://issuetracker.google.com/issues/219446409))
- Added the ability to intercept scheduling exceptions providing `Consumer<Throwable>` via [setSchedulingExceptionHandler](https://developer.android.com/reference/androidx/work/Configuration.Builder#setSchedulingExceptionHandler(androidx.core.util.Consumer%3Cjava.lang.Throwable%3E)))
- Added the ability to provide `Consumer<Throwable>` via [setInitializationExceptionHandler](https://developer.android.com/reference/androidx/work/Configuration.Builder#setInitializationExceptionHandler(androidx.core.util.Consumer%3Cjava.lang.Throwable%3E)) to determine if there were issues when trying to initialize WorkManager.
- Inline helpers for `OneTimeWorkRequest` \& `PeriodicWorkRequest` were moved from `androidx.work:work-runtime-ktx` to `androidx.work:work-runtime` ([I0010f](https://android-review.googlesource.com/#/q/I0010f0bc806318ad840550458d872c12ee60eae7), [b/209145335](https://issuetracker.google.com/issues/209145335))
- Helper methods `WorkQuery.fromIds`, `WorkQuery.fromStates`, `WorkQuery.fromUniqueWorkNames`, `WorkQuery.fromTags` were added to create `WorkQuery` directly. ([b/199919736](https://issuetracker.google.com/issues/199919736)) ([If48f2](https://android-review.googlesource.com/#/q/If48f2ae0a5523792a9abe21279084f895abe7c53), [b/199919736](https://issuetracker.google.com/issues/199919736))
- Added `getForegroundInfo` to `Worker`. ([Ic1ead](https://android-review.googlesource.com/#/q/Ic1ead06bc9cc4cf61e90526dc47dff4c1365ea4c))
- `RxWorker` both for RxJava 2 and RxJava 3 now has `setForeground` returning `Completable` that can be used instead of `setForegroundInfoAsync` that returns `ListenableFuture`
- `RxWorker` both for RxJava 2 and RxJava 3 has `getForegroundInfo` returning `Single` that can be used instead of `getForegroundInfoAsync` that returns `ListenableFuture`. ([b/203851459](https://issuetracker.google.com/issues/203851459))
- Constraints can now be directly constructed rather than using `Constraints.Builder`, which is convenient for Kotlin users. ([Idc390](https://android-review.googlesource.com/#/q/Idc3900488dcaae5ca6c52b706723a752425875d9), [b/137568653](https://issuetracker.google.com/issues/137568653))
- Added the ability to check if `WorkManager` has been initialized. Also, added a new `getConfiguration()` API for library developers to get the configuration that `WorkManager` was initialized with. ([I6eff3](https://android-review.googlesource.com/#/q/Idc3900488dcaae5ca6c52b706723a752425875d9), [b/212300336](https://issuetracker.google.com/issues/137568653))

**Bug Fixes**

- Fixed an issue with the greedy scheduler that would prevent workers from running immediately when under load. ([I9686b](https://android-review.googlesource.com/#/q/I9686ba0810e4444b41ae7d638a6b8db3943da8cb), [b/248111307](https://issuetracker.google.com/issues/248111307))
- Added `@RequiresPermission` to APIs that require granting the `POST_NOTIFICATIONS` permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631), [b/238790278](https://issuetracker.google.com/issues/238790278))
- Propagate cancellations in the `CoroutineScope` to the `ListenableFuture` when using `suspendCancellableCoroutine`.

### Version 2.8.0-rc01

December 7, 2022

`androidx.work:work-*:2.8.0-rc01` is released. [Version 2.8.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..b6809fb97f68a2d1a861e81cd6d32800039dcb09/work)

**New Features**

- No new features on this release. This is mainly a version bump

### Version 2.8.0-beta02

November 9, 2022

`androidx.work:work-*:2.8.0-beta02` is released. [Version 2.8.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6d0e3ed0829f3e41c89e6dfa985e16f8e7437aab..a1e318590b217ecfce1b2de17eed2f18b6a680bb/work)

**Bug Fixes**

- Fixed `equals` method in `WorkInfo`, that previously didn't take into account new generation information. ([4977cc](https://android-review.googlesource.com/c/platform/frameworks/support/+/2259481))

### Version 2.8.0-beta01

October 5, 2022

`androidx.work:work-*:2.8.0-beta01` is released. [Version 2.8.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/work)

**Bug Fixes**

- Fixed an issue with the greedy scheduler that would prevent workers from running immediately when under load. ([I9686b](https://android-review.googlesource.com/#/q/I9686ba0810e4444b41ae7d638a6b8db3943da8cb), [b/248111307](https://issuetracker.google.com/issues/248111307))

### Version 2.8.0-alpha04

September 7, 2022

`androidx.work:work-*:2.8.0-alpha04` is released. [Version 2.8.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..cce7b70f6a5ebf955cf748a73c18b63228b22c74/work)

**API Changes**

- `WorkerInfo.getGeneration()` and `WorkerParameters.getGeneration()` were added that return the generation of a worker. A worker has multiple generations, if it was updated via `WorkManager.updateWork` or `WorkManager.enqueueUniquePeriodicWork` using `ExistingPeriodicWorkPolicy.UPDATE`. Note that If the worker is currently running, it is possible for this method to return a newer generation from that of the currently running worker if an update has happened during an execution of the worker. ([I665c5](https://android-review.googlesource.com/#/q/I665c5d480700dd682d1268ee88be124783fca70f), [b/219446409](https://issuetracker.google.com/issues/219446409)) ([I128a9](https://android-review.googlesource.com/#/q/I128a9838067f3a1722a9460f52ef58fb0f98136c), [b/219446409](https://issuetracker.google.com/issues/219446409))
- Added `InitializationExceptionHandler`, an Exception Handler that can be used to determine if there were issues when trying to initialize `WorkManager`. ([I061de](https://android-review.googlesource.com/#/q/I061de05e60048dc7a816c1392f2b5ae60a31f14c))

### Version 2.8.0-alpha03

August 10, 2022

`androidx.work:work-*:2.8.0-alpha03` is released. [Version 2.8.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..bea814b246f89ff7244e3c6b0648f0b57e47897c/work)

**New Features**

- An ability to update `WorkRequests` in a non-intrusive way was added, preserving original enqueue time, chaining etc. See `WorkManager.updateWork` and `ExistingPeriodicWorkPolicy.UPDATE` for more details.

**API Changes**

- `WorkManager.updateWork` was added to update work preserving its original enqueue time and chaining.([I9a248](https://android-review.googlesource.com/#/q/I9a2489e50d217cf70377d348b183ceb2d777506d), [b/219446409](https://issuetracker.google.com/issues/219446409))
- `ExistingPeriodicWorkPolicy.UPDATE` was added. This policy allows to update a periodic work by the name. It is similar to the existing `REPLACE`, but it is less intrusive: it doesn't cancel a worker if it is currently running and it preserves enqueue time - initial delay and period are calculated from original enqueue time, rather than update time. `REPLACE` was deprecated to decrease a confusion between very similarly named `REPLACE`and `UPDATE`. If you still want to keep the previous semantics of `REPLACE`, the newly added `CANCEL_AND_REENQUEUE`, which is identical to `REPLACE`, can be used. ([I985ed](https://android-review.googlesource.com/#/q/I985edc2cf7ac7c316932185f3fd0a3ca6660f2dc), [b/219446409](https://issuetracker.google.com/issues/219446409))
- Add the ability to intercept scheduling exceptions by defining a `SchedulingExceptionHandler`. ([I033eb](https://android-review.googlesource.com/#/q/I033eb7d6c3496a23825a63e1f55ecc35d05602f5))
- Inline helpers for `OneTimeWorkRequest` \& `PeriodicWorkRequest` were moved from `androidx.work:work-runtime-ktx` to `androidx.work:work-runtime` ([I0010f](https://android-review.googlesource.com/#/q/I0010f0bc806318ad840550458d872c12ee60eae7), [b/209145335](https://issuetracker.google.com/issues/209145335))

**Bug Fixes**

- Added `@RequiresPermission` to APIs that require granting the POST_NOTIFICATIONS permission on SDK 33 and above. ([Ie542e](https://android-review.googlesource.com/#/q/Ie542eb66c9af6e3c3a7c59bb291c7c5879458631), [b/238790278](https://issuetracker.google.com/issues/238790278))

### Version 2.8.0-alpha02

April 6, 2022

`androidx.work:work-*:2.8.0-alpha02` is released. [Version 2.8.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/work)

**API Changes**

- Constraints can now be directly constructed rather than using Builder, which is convenient for Kotlin users. ([Idc390](https://android-review.googlesource.com/#/q/Idc3900488dcaae5ca6c52b706723a752425875d9), [b/137568653](https://issuetracker.google.com/issues/137568653))
- Added the ability to check if `WorkManager` has been initialized. Also, added a new `getConfiguration()` API for library developers to get the configuration that `WorkManager` was initialized with. ([I6eff3](https://android-review.googlesource.com/#/q/I6eff387fcf99eac94ef4cc210cc75e8f3edd6a7b), [b/212300336](https://issuetracker.google.com/issues/212300336))

### Version 2.8.0-alpha01

January 12, 2022

`androidx.work:work-*:2.8.0-alpha01` is released. [Version 2.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a8b339074687010fb5c861b5af9d169113f0c04b..f09f3e0f47cacc65a631115deac08ee8cc132ceb/work)

**API Changes**

- Helper methods `WorkQuery.fromStates`, `WorkQuery.fromUniqueWorkNames`, `WorkQuery.fromTags` were added to create WorkQuery directly. ([If48f2](https://android-review.googlesource.com/#/q/If48f2ae0a5523792a9abe21279084f895abe7c53), [b/199919736](https://issuetracker.google.com/issues/199919736))
- Adds experimental BuildCompat methods for future SDKs ([Iafd82](https://android-review.googlesource.com/#/q/Iafd82e20e0c6d54878d352baddb18e86095504a7), [b/207528937](https://issuetracker.google.com/issues/207528937))
- Add `getForegroundInfo` to `Worker`. ([Ic1ead](https://android-review.googlesource.com/#/q/Ic1ead06bc9cc4cf61e90526dc47dff4c1365ea4c))
- Helper methods `WorkQuery.fromIds` to create WorkQuery directly from ids were added. ([Ie5bdf](https://android-review.googlesource.com/#/q/Ie5bdf99ac193c9aa9179dcf629a46227fe876242), [b/199919736](https://issuetracker.google.com/issues/199919736))
- RxWorker now has `setForeground` returning `Completable` that can be used instead of `setForegroundInfoAsync` that returns `ListenableFuture`. ([I85156](https://android-review.googlesource.com/#/q/I851567cc042d4f3f6de9023f4eb6d0f2a25e8b8e))
- RxWorker for RxJava 2 now has `getForegroundInfo` returning `Single` that can be used instead of `getForegroundInfoAsync` that returns `ListenableFuture`. ([I21c91](https://android-review.googlesource.com/#/q/I21c91cd5db57e85bf1aaa7e1596e2287ab44675c), [b/203851459](https://issuetracker.google.com/issues/203851459))
- RxWorker for RxJava 3 now has `getForegroundInfo` returning `Single` that can be used instead of `getForegroundInfoAsync` that returns `ListenableFuture`. ([I1ca8a](https://android-review.googlesource.com/#/q/I1ca8aee15cd28ea1afe363fa235ff6a13be8f95c))
- RxWorker now has `setForeground` returning `Completable` that can be used instead of `setForegroundInfoAsync` that returns `ListenableFuture`. ([I992a3](https://android-review.googlesource.com/#/q/I992a32849600b8c3bb37fa362e9775bc46a6462b), [b/203851459](https://issuetracker.google.com/issues/203851459))

**Bug Fixes**

- Propagate cancellations in the `CoroutineScope` to the `ListenableFuture` when using `suspendCancellableCoroutine`. ([I77e63](https://android-review.googlesource.com/#/q/I77e6348e89ba345f1ae1024b7102334b3608ca6d))

## Version 2.7

| **Note:** WorkManager Version `2.7.0` is required for apps targeting Android 12 (S).

### Version 2.7.1

November 17, 2021

`androidx.work:work-*:2.7.1` is released. [Version 2.7.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/43e01da60178b0f86ff63c730b8adae2d22ecb62..a8b339074687010fb5c861b5af9d169113f0c04b/work)

**Bug Fixes**

- Cancellations in the `CoroutineScope`are propagated to the `ListenableFuture` when using `suspendCancellableCoroutine`. ([I77e63](https://android-review.googlesource.com/#/q/I77e6348e89ba345f1ae1024b7102334b3608ca6d))
- An exception is thrown immediately when delayed work requests are marked as expedited. [bef1762](https://android.googlesource.com/platform/frameworks/support/+/bef1762d4bdcc336c078e8502639579c31a89e15)

### Version 2.7.0

October 13, 2021

`androidx.work:work-*:2.7.0` is released. [Version 2.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ec09ba07aae1c2baaf6b84a2b30bd85cddbc9902..43e01da60178b0f86ff63c730b8adae2d22ecb62/work)

**Important changes since 2.6.0**

- WorkManager introduces a new `WorkRequest.Builder.setExpedited(...)` API to help with Foreground Service restrictions in Android 12.

- When using [`setExpedited(...)`](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setExpedited(boolean)), WorkManager delegates to expedited jobs in JobScheduler starting Android 12, while providing backwards compatibility on prior versions of Android by delegating to a Foreground Service.

### Version 2.7.0-rc01

September 29, 2021

`androidx.work:work-*:2.7.0-rc01` is released. [Version 2.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74cf577caf9b6557a015ebd82996fc5fa907a219..ec09ba07aae1c2baaf6b84a2b30bd85cddbc9902/work)

This version is identical to `androidx.work:work-*:2.7.0-beta01`.

### Version 2.7.0-beta01

September 1, 2021

`androidx.work:work-*:2.7.0-beta01` is released. [Version 2.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ed683bd5038dd4cdcc7440896b7949d6917b0c8a..74cf577caf9b6557a015ebd82996fc5fa907a219/work)

**New Features**

- Reduce multi-process SQLite contention when initializing WorkManager.

**API Changes**

- Remove `@ExperimentalExpeditedWork` APIs given the underlying platform APIs for Android 12 (S) are stable. ([aosp/1792806](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792806))

**Bug Fixes**

- Provide a better error message for expedited workers that do not implement `getForegroundInfoAsync()`. ([aosp/1809376](https://android-review.googlesource.com/c/platform/frameworks/support/+/1809376))

### Version 2.7.0-alpha05

July 21, 2021

`androidx.work:work-*:2.7.0-alpha05` is released. [Version 2.7.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9718dac3db72190dec105d92592bea08527f196a..ed683bd5038dd4cdcc7440896b7949d6917b0c8a/work)

This release also contains bug fixes from the [WorkManager `2.6.0-beta02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-beta02) release.

### Version 2.7.0-alpha04

June 2, 2021

`androidx.work:work-*:2.7.0-alpha04` is released.

This release also contains the changes from the [2.6.0-beta01](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-beta01) release.

**API Changes**

- `ListenableWorker.setForegroundAsync()` is no longer deprecated.
- We recommend using `WorkRequest.Builder.setExpedited(...)` API when possible. To better support situations when the [app is not subject to foreground service restrictions](https://developer.android.com/about/versions/12/foreground-services#cases-fgs-background-starts-allowed), developers can use the `ListenableWorker.setForegroundAsync()` API.
- If `ListenableWorker.setForegroundAsync()` is called, when the app is subject to foreground service restrictions, this will throw the [ForegroundServiceStartNotAllowedException](https://developer.android.com/reference/android/app/ForegroundServiceStartNotAllowedException).

**Bug Fixes**

- When expedited jobs are rescheduled, they are no longer expedited. They become *regular* jobs.

### Version 2.7.0-alpha03

April 21, 2021
| **Note:** WorkManager Version 2.7.0-alpha03 is **only compatible** with the Android 12 Developer Preview 3 SDK.

`androidx.work:work-*:2.7.0-alpha03` is released. [Version 2.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/23e58206a34ee2ac5a0e6ac8bf8d6e4f1e070efb..d31c94c58e59b87051a5ba2f8ba791cbdb421748/work)

**New Features**

- From [WorkManager `2.6.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02): Adds support for Workers that can run in any process. ([Iaf200](https://android-review.googlesource.com/#/q/Iaf2009914abca579d6d3e5786011a79d6b99f8fa))

- From [WorkManager `2.6.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02): Added a `RemoteCoroutineWorker` which is an implementation of `RemoteListenableWorker` that can bind to a remote process. ([I30578](https://android-review.googlesource.com/#/q/I30578ea87b8bbff82f8d5b70c6cf97a105b387f9))

**API Changes**

- From [WorkManager `2.6.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02):Added support for `TEMPORARILY_UNMETERED` network constraint. ([I08d5e](https://android-review.googlesource.com/#/q/I08d5efa05691df9c9e6445073db8fd184da1ebb8))
- From [WorkManager `2.6.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02):Multi-process worker support for `setProgressAsync()`. ([Ib6d08](https://android-review.googlesource.com/#/q/Ib6d0893300662e9b226d50c656360d59a29cba60))
- From [WorkManager `2.6.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02):Make `WorkManagerInitializer` public so other `androidx.startup.Initializer`s can use these as dependencies. ([I5ab11](https://android-review.googlesource.com/#/q/I5ab117d1f69b6efc40227be4712e5e0865410a03))

### Version 2.7.0-alpha02

March 10, 2021

`androidx.work:work-*:2.7.0-alpha02` is released. [Version 2.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51b9293137916801ce8564a523a6ae77398694c1..23e58206a34ee2ac5a0e6ac8bf8d6e4f1e070efb/work)
| **Note:** WorkManager Version 2.7.0-alpha02 is **only compatible** with the Android 12 Developer Preview 1 SDK.

**Bug Fixes**

- Make `PendingIntent` mutability explicit, to fix a crash when targeting Android 12. ([b/180884673](https://issuetracker.google.com/issues/180884673))

### Version 2.7.0-alpha01

February 18, 2021

`androidx.work:work-*:2.7.0-alpha01` is released. [Version 2.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b32e1d4efc3b6976da585fb8783f913e92108428..51b9293137916801ce8564a523a6ae77398694c1/work)
| **Note:** WorkManager Version 2.7.0-alpha01 is **only compatible** with the Android 12 Developer Preview 1 SDK.

**New Features**

- WorkManager introduces a new`WorkRequest.Builder.setExpedited(...)` API to take into account the [foreground Service restrictions](https://developer.android.com/about/versions/12/behavior-changes-12#foreground-service-launch-restrictions) in Android 12.

  Applications can no longer launch a foreground service when they are in the background. Therefore, to better support long running work which was previously bound to the lifecycle of a foreground service, applications can mark `WorkRequest`s as [*expedited*](https://developer.android.com/reference/android/app/job/JobInfo.Builder#setExpedited(boolean)).

  This API is a replacement for the `setForegroundAsync(...)` / `setForeground(...)` APIs which are now **deprecated**.

  When using `setExpedited(...)`, WorkManager delegates to expedited jobs in `JobScheduler` starting Android 12, while providing backwards compatibility on prior versions of Android by delegating to foreground services,

**API Changes**

- Add support for expedited `WorkRequest`s.

## Version 2.6.0

### Version 2.6.0

September 1, 2021

`androidx.work:work-*:2.6.0` is released. [Version 2.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fb4befebd5dfb03c14a0593799f68f1567993e6b..554afbcb0b3fba9fd022029713d72b2f376411b6/work)
| **Note:** WorkManager Version `2.6.0` is not compatible for apps targeting Android 12 (S). You should be using version `2.7.0` instead.

**Important changes since 2.5.0**

- WorkManager now uses `androidx.startup` to initialize WorkManager.
  If you used `tools:node="remove"` the `ContentProvider` being used to initialize WorkManager in the past, then you need to do the following instead.

      <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities=\"${applicationId}.androidx-startup"
          android:exported="false"
          tools:node=\"merge">
          <!-- If you are using androidx.startup to initialize other components -->
          <meta-data
              android:name="androidx.work.WorkManagerInitializer"
              android:value="androidx.startup"
              tools:node="remove" />
       </provider>

      <!-- If you want to disable android.startup completely. -->
       <provider
                  android:name="androidx.startup.InitializationProvider"
                  android:authorities="${applicationId}.androidx-startup"
                  tools:node="remove" />

- Added support for Workers that can run in any process. ([Iaf200](https://android-review.googlesource.com/#/q/Iaf2009914abca579d6d3e5786011a79d6b99f8fa))

- Added a `RemoteCoroutineWorker` which is an implementation of RemoteListenableWorker that can bind to a remote process. ([I30578](https://android-review.googlesource.com/#/q/I30578ea87b8bbff82f8d5b70c6cf97a105b387f9))

### Version 2.6.0-rc01

August 4, 2021

`androidx.work:work-*:2.6.0-rc01` is released. [Version 2.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..fb4befebd5dfb03c14a0593799f68f1567993e6b/work)

This version is identical to `androidx.work:work-*:2.6.0-beta02`.

### Version 2.6.0-beta02

July 21, 2021

`androidx.work:work-*:2.6.0-beta02` is released. [Version 2.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/work)

**Bug Fixes**

- `RemoteWorkManager` now correctly unbinds from `RemoteWorkManagerService` which allows `RemoteWorkManagerService` to clean up correctly. [aosp/1730694](https://android-review.googlesource.com/c/platform/frameworks/support/+/1730694)
- `RemoteListenableWorker` now correctly unbinds from `RemoteWorkerService` which allows `RemoteWorkerService` to clean up correctly. [aosp/1743817](https://android-review.googlesource.com/c/platform/frameworks/support/+/1743817)
- `ForceStopRunnable` now only runs in the primary app process. This is an optimization, and avoids resource contention for apps that use multiple processes. [aosp/1749180](https://android-review.googlesource.com/c/platform/frameworks/support/+/1749180), [aosp/1761729](https://android-review.googlesource.com/c/platform/frameworks/support/+/1761729)

### Version 2.6.0-beta01

June 2, 2021

`androidx.work:work-*:2.6.0-beta01` is released. [Version 2.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ddfc1583c09aaa878d34437fbfee1b995b60d3a..86ff5b4bb956431ec884586ce0aea0127e189ec4/work)

This release contains some minor documentation improvements. The release is largely identical to [2.6.0-alpha02](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha02).

### Version 2.6.0-alpha02

April 21, 2021

`androidx.work:work-*:2.6.0-alpha02` is released. [Version 2.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..4ddfc1583c09aaa878d34437fbfee1b995b60d3a/work)

**New Features**

- Adds support for Workers that can run in any process. ([Iaf200](https://android-review.googlesource.com/#/q/Iaf2009914abca579d6d3e5786011a79d6b99f8fa))

- Added a `RemoteCoroutineWorker` which is an implementation of `RemoteListenableWorker` that can bind to a remote process. ([I30578](https://android-review.googlesource.com/#/q/I30578ea87b8bbff82f8d5b70c6cf97a105b387f9))

**API Changes**

- Added support for `TEMPORARILY_UNMETERED` network constraint. ([I08d5e](https://android-review.googlesource.com/#/q/I08d5efa05691df9c9e6445073db8fd184da1ebb8))
- Multi-process worker support for `setProgressAsync()`. ([Ib6d08](https://android-review.googlesource.com/#/q/Ib6d0893300662e9b226d50c656360d59a29cba60))
- Make `WorkManagerInitializer` public so other `androidx.startup.Initializer`s can use these as dependencies. ([I5ab11](https://android-review.googlesource.com/#/q/I5ab117d1f69b6efc40227be4712e5e0865410a03))

### Version 2.6.0-alpha01

March 24, 2021

`androidx.work:work-*:2.6.0-alpha01` is released. [Version 2.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b32e1d4efc3b6976da585fb8783f913e92108428..5c42896eb6591b09e3952030fb7ea8d9b8c42713/work)

**New Features**

- `WorkManager` now uses `androidx.startup` to initialize WorkManager.
  Previously, this was being done by `androidx.work.impl.WorkManagerInitializer`. ([aosp/1608813](https://android-review.googlesource.com/c/platform/frameworks/support/+/1608813))

  If you used `tools:node="remove"` the `ContentProvider` being used to initialize
  process lifecycle in the past, then you need to do the following instead.  

       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities=\"${applicationId}.androidx-startup"
          android:exported="false"
          tools:node=\"merge">
          <!-- If you are using androidx.startup to initialize other components -->
          <meta-data
              android:name="androidx.work.impl.WorkManagerInitializer"
              android:value="androidx.startup"
              tools:node="remove" />
       </provider>

  (or)  

       <!-- If you want to disable android.startup completely. -->
       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities="${applicationId}.androidx-startup"
          tools:node="remove">
       </provider>

**API Changes**

- Add a `Result.getOutputData()` API which returns the ListenableWorker's `outputData`. ([Ie51e3](https://android-review.googlesource.com/#/q/Ie51e31db49b6952172dd502d2178164c951a2db1))

**Bug Fixes**

- Add a workaround for an OEM bug which causes a `SecurityException` to be thrown when using `AlarmManager` APIs. ([aosp/1587518](https://android-review.googlesource.com/c/platform/frameworks/support/+/1587518))

## Version 2.5.0

| **Note:** WorkManager Version 2.5.0 is **not compatible** with apps targeting Android 12 (S)

### Version 2.5.0

January 27, 2021

`androidx.work:work-*:2.5.0` is released. [Version 2.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8e8a196e1c2eb6d6e6194b621267473c31bea375..b32e1d4efc3b6976da585fb8783f913e92108428/work)

**Major changes since 2.4.0**

- A new `:work:work-multiprocess` artifact for apps that use multiple processes. This introduces performance gains by unifying work request scheduling to a single process.
  - To use `work-multiprocess`, define a dependency on: `implementation "androidx.work:work-multiprocess:2.5.0"`
  - Designate a primary process using [Configuration.Builder.setDefaultProcessName(String)](https://developer.android.com/reference/androidx/work/Configuration.Builder#setDefaultProcessName(java.lang.String)).
  - When using `work-multiprocess` you also want to use [RemoteWorkManager](https://developer.android.com/reference/androidx/work/multiprocess/RemoteWorkManager) to manage your `WorkRequest`s. [RemoteWorkManager](https://developer.android.com/reference/androidx/work/multiprocess/RemoteWorkManager) always reaches out to the designated process. The in-process scheduler also runs in the designated process.
- Sometimes, `ActivityManager` cannot instantiate the `JobService` instance, to start a job. This causes the underlying job to get silently dropped because of a platform bug. `WorkManager` now ensures that there are backing jobs for every single `WorkRequest` when an `Application` is being initialized by reconciling jobs. This greatly improves job execution reliability. ([b/172475041](https://issuetracker.google.com/issues/172475041), [aosp/1489577](https://android-review.googlesource.com/c/platform/frameworks/support/+/1489577))
- `WorkManager` limits database growth by reducing the buffer duration that `WorkRequest`s are tracked after a `WorkRequest` is complete. The duration was `7` days previously. It has been reduced to `1` day + the [keepResultsForAtLeast](https://developer.android.com/reference/androidx/work/WorkRequest.Builder#keepResultsForAtLeast(java.time.Duration)) duration. ([aosp/1419708](https://android-review.googlesource.com/c/platform/frameworks/support/+/1419708))
- The `TestListenableWorkerBuilder` now supports the reified class extending `ListenableWorker` to make testing easier. ([aosp/1443299](https://android-review.googlesource.com/c/platform/frameworks/support/+/1443299), [b/169787349](https://issuetracker.google.com/issues/169787349))
- [WorkManager inspector](https://developer.android.com/studio/preview/features#workmanager-inspector) is now available when using Android Studio Arctic Fox.

### Version 2.5.0-rc01

January 13, 2021

`androidx.work:work-*:2.5.0-rc01` is released. [Version 2.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19cec447c629db6ab3e716338e55682beb599529..8e8a196e1c2eb6d6e6194b621267473c31bea375/work)

**Bug Fixes**

- Fixed a bug where `getWorkInfosLiveData` was not correctly getting invalidated after entities were updated when using the `WorkQuery` based API. ([aosp/1540566](https://android-review.googlesource.com/c/platform/frameworks/support/+/1540566), [b/173769028](https://issuetracker.google.com/issues/173769028))
- Fixed a bug where database transactions were not being marked as successful in some rare cases. This causes issues on some Motorola devices. ([aosp/1535368](https://android-review.googlesource.com/c/platform/frameworks/support/+/1535368), [b/175944460](https://issuetracker.google.com/issues/175944460))
- Fixed a bug to ignore `NoSuchElementException`s when trying to unbind from a dead process. ([aosp/1530589](https://android-review.googlesource.com/c/platform/frameworks/support/+/1530589))
- Improve `ConstraintTrackingWorker` to only stop a `ListenableWorker` if it's not already been stopped. ([aosp/1496844](https://android-review.googlesource.com/c/platform/frameworks/support/+/1496844), [b/172946965](https://issuetracker.google.com/issues/172946965))
- Update androidx.work libraries to target Java 8 ([Ibd2f2](https://android-review.googlesource.com/#/q/Ibd2f2076704eccf61ee4e7062b73ae24977adeb6))

### Version 2.5.0-beta02

December 2, 2020

`androidx.work:work-*:2.5.0-beta02` is released. [Version 2.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/67682f4d35e4f57d0fe3727c451a9537f64b0632..06e510c5098678de176fbda9c499fe09b096e257/work)

**Bug Fixes**

- Fixed a bug in `androidx.work:work-multiprocess` where WorkManager inadvertently blocked the calling thread when trying to bind to the designated process. ([aosp/1475538](https://android-review.googlesource.com/c/platform/frameworks/support/+/1475538))
- Fixed a bug where `PeriodicWorkRequest`s were not being reconciled correctly. ([b/172475041](https://issuetracker.google.com/issues/172475041), [aosp/1489577](https://android-review.googlesource.com/c/platform/frameworks/support/+/1489577))
- Added a workaround for a platform bug when stopping the foreground service when using the `setForeground*` APIs. ([b/170924044](https://issuetracker.google.com/issues/170924044), [aosp/1489901](https://android-review.googlesource.com/c/platform/frameworks/support/+/1489901))

### Version 2.5.0-beta01

October 28, 2020

`androidx.work:work-*:2.5.0-beta01` is released. [Version 2.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..67682f4d35e4f57d0fe3727c451a9537f64b0632/work)

**New Features**

- `WorkManager` automatically throttles the number of `WorkRequest`s that can be picked up by the in-process scheduler. The requests are still executed in FIFO order. ([aosp/1455228](https://android-review.googlesource.com/c/platform/frameworks/support/+/1455228))
- `WorkManager` attempts to recover when the application's datastore is in a bad state. ([aosp/1463103](https://android-review.googlesource.com/c/platform/frameworks/support/+/1463103))

**Bug Fixes**

- When `ListenableWorker`s are interrupted, mark them `ENQUEUED` immediately so they can be subsequently rescheduled. ([aosp/1455618](https://android-review.googlesource.com/c/platform/frameworks/support/+/1455618), [b/170273988](https://issuetracker.google.com/issues/170273988))

### Version 2.5.0-alpha03

October 14, 2020

`androidx.work:work-*:2.5.0-alpha03` is released. [Version 2.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f413b8be76bfa0a4d109a3afb583188c580a2aa6/work)

**API Changes**

- `TestListenableWorkerBuilder` and `TestWorkerBuilder` do not use raw types. ([I883ad](https://android-review.googlesource.com/#/q/I883ad37181cc32733c6f617009d4ab5903760452), [b/169787349](https://issuetracker.google.com/issues/169787349))

**Bug Fixes**

- Use `ApplicationInfo` to determine the name of the default app process. ([b/168716641](https://issuetracker.google.com/issues/168716641), [aosp/1429950](https://android-review.googlesource.com/1429950))
- Fix the visibility rules for `RemoteWorkManager` and `RemoteWorkContinuation`. These APIs are no-longer marked as `@Restricted`. ([aosp/1432091](https://android-review.googlesource.com/c/platform/frameworks/support/+/1432091))
- Fix proguard rules for `:work:work-multiprocess`. ([aosp/1432091](https://android-review.googlesource.com/c/platform/frameworks/support/+/1432091))
- Improve notification lifecycles for long running work bound to a foreground service. ([b/168502234](https://issuetracker.google.com/issues/168502234), [aosp/1431331](https://android-review.googlesource.com/c/platform/frameworks/support/+/1431331))

### Version 2.5.0-alpha02

September 16, 2020

`androidx.work:work-*:2.5.0-alpha02` is released. [Version 2.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..18a5639262f8504db530176550e338a5d0e2e044/work)

**New Features**

- Add an API to WorkQuery to be able to use `id`s to query `WorkInfo`s. ([aosp/1412372](https://android-review.googlesource.com/c/platform/frameworks/support/+/1412372), [b/157335295](https://issuetracker.google.com/issues/157335295))
- WorkManager better supports apps that use multiple processes with a new artifact (`androidx.work:work-multiprocess:*`). This new artifact helps solve a few problems that large apps encounter including:
  - WorkManager typically needs to be initialized in every app process. This is not great because there is increased SQLite contention which in turn causes other problems. WorkManager now has new APIs which can be used to designate a *primary* app process using `Configuration#setDefaultProcessName(processName)`. The `processName` is a fully qualified process name which looks like `packageName:processName` (e.g. `com.example:remote`).
  - A set of new APIs: `RemoteWorkManager` and `RemoteWorkContinuation` to `enqueue`, `cancel` and `query` work requests. These APIs do *not* include `LiveData` variants to avoid SQLite contention across multiple-processes. All calls to `enqueue`, `cancel` and `query` are forwarded to a `primary` app process using AIDL and return a fluent `ListenableFuture`. ([aosp/1392657](https://android-review.googlesource.com/c/platform/frameworks/support/+/1392657), [aosp/1411210](https://android-review.googlesource.com/c/platform/frameworks/support/+/1411210), [aosp/1412215](https://android-review.googlesource.com/c/platform/frameworks/support/+/1412215), [aosp/1417713](https://android-review.googlesource.com/c/platform/frameworks/support/+/1417713))

**API Changes**

- WorkManager now prunes completed `WorkRequest`s that have no incomplete dependencies more aggressively. The buffer duration changed from `7` days to `1` day. ([aosp/1419708](https://android-review.googlesource.com/c/platform/frameworks/support/+/1419708))

**Bug Fixes**

- WorkManager now reconciles jobs proactively so `WorkRequest`s and `JobScheduler` jobs are in sync when `WorkManager` is initialized. ([aosp/1412794](https://android-review.googlesource.com/c/platform/frameworks/support/+/1412794), [b/166292069](https://issuetracker.google.com/issues/166292069))

### Version 2.5.0-alpha01

August 19, 2020

`androidx.work:work-*:2.5.0-alpha01` is released. [Version 2.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1fe9950a2c96b1046e15091cd832dbecd8a2d9cf..96eb302ee1740ba656c90c9fb27df3723a1a89c1/work)

**New Features**

- Changes to internal APIs that allow us to provide better tooling with `WorkManager` going forward. Stay tuned for additional updates.

**Bug Fixes**

- Handle `SecurityException`s when tracking network state on some devices. ([aosp/1396969](https://android-review.googlesource.com/c/platform/frameworks/support/+/1396969))

**External Contribution**

- Fix documentation for `ArrayCreatingInputMerger` by [Zac Sweers](https://twitter.com/ZacSweers) ([github/43](https://github.com/androidx/androidx/pull/43)).

## Version 2.4.0

### Version 2.4.0

July 22, 2020

`androidx.work:work-*:2.4.0` is released. [Version 2.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/098521464a5be8f6d5fb14a9772d859a8e6d3638..1fe9950a2c96b1046e15091cd832dbecd8a2d9cf/work)

**Major changes since 2.3.0**

- `WorkManager`s in-process scheduler is now more capable. Previously, the in-process `Scheduler` would only consider executing work that was not delayed and whose constraints were met. Now, the in-process scheduler tracks `WorkRequest`s which might be executed in the future, including PeriodicWorkRequests. The in-process `Scheduler` also does not observe scheduling limits (but is still restricted to the size of the `Executor` being used by WorkManager). This means that the application can now execute a lot more WorkRequests when the app is in the foreground. To manage execution of delayed work in the foreground, `WorkManager` also introduces a new configurable [`RunnableScheduler`](https://developer.android.com/reference/kotlin/androidx/work/RunnableScheduler). ([aosp/1185778](https://android-review.googlesource.com/c/platform/frameworks/support/+/1185778))
- WorkManager now supports RxJava 3. To use RxJava 3, you should include the following dependency: `implementation "androidx.work:work-rxjava3:2.4.0"`. ([aosp/1277904](https://android-review.googlesource.com/c/platform/frameworks/support/+/1277904))
- Added the ability to query for `WorkInfo`s by using a `WorkQuery`. This is useful when developers want to query `WorkInfo`s by a combination of multiple attributes. For more information look at `WorkQuery.Builder.fromStates(...)`, `WorkQuery.Builder. fromTags(...)` or `WorkQuery.Builder.fromUniqueWorkNames(...)`. ([aosp/1253230](https://android-review.googlesource.com/c/platform/frameworks/support/+/1253230), [b/143847546](https://issuetracker.google.com/issues/143847546))
- Add the ability to request diagnostic information from `WorkManager` using:

      adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p "<your_app_package_name>"

  This provides a lot of useful information including:
  - WorkRequests that were completed in the last 24 hours.
  - WorkRequests that are currently RUNNING.
  - Scheduled WorkRequests. ([aosp/1235501](https://android-review.googlesource.com/c/platform/frameworks/support/+/1235501))
- Add `ExistingWorkPolicy.APPEND_OR_REPLACE` which is similar to `APPEND`, but replaces a chain that has cancelled or failed prerequisites. ([b/134613984](https://issuetracker.google.com/issues/134613984), [aosp/1199640](https://android-review.googlesource.com/c/platform/frameworks/support/+/1199640))

- Provide the ability to add a custom `RunnableScheduler` to track WorkRequests that need to be executed in the future. This is used by the in-process Scheduler. ([aosp/1203944](https://android-review.googlesource.com/c/platform/frameworks/support/+/1203944))

- Add support for dynamically adding factories to delegate to, when using a `DelegatingWorkerFactory`.
  ([b/156289105](https://issuetracker.google.com/issues/156289105),
  [aosp/1309745](https://android-review.googlesource.com/c/platform/frameworks/support/+/1309745))

- Align tracking for `BATTERY_NOT_LOW` constraints more closely with the platform. ([aosp/1312583](https://android-review.googlesource.com/c/platform/frameworks/support/+/1312583))

- The in-process scheduler now uses better APIs to determine the name of the process. This is useful to better support apps that use multiple-processes. ([aosp/1324732](https://android-review.googlesource.com/c/platform/frameworks/support/+/1324732))

- New Lint rules which enforce:

  - Use of the right `foregroundServiceType` when using `setForegroundAsync()` APIs. ([b/147873061](https://issuetracker.google.com/issues/147873061), [aosp/1215915](https://android-review.googlesource.com/c/platform/frameworks/support/+/1215915))
  - Specifying JobScheduler ids that WorkManager should use when using JobService APIs directly. [aosp/1223567](https://android-review.googlesource.com/c/platform/frameworks/support/+/1223567)
  - Added a new lint rule that ensures that `ListenableWorker`implementations are now `public` when using the default `WorkerFactory`. ([aosp/1291262](https://android-review.googlesource.com/c/platform/frameworks/support/+/1291262))
- Calls to `setForegroundAsync()` that do not complete before completion of a `ListenableWorker` will now be signalled via an `IllegalStateException` on the returned `ListenableFuture`. ([aosp/1262743](https://android-review.googlesource.com/c/platform/frameworks/support/+/1262743))

- Fix a bug where the `ForegroundService` is not stopped after a foreground `Worker` is interrupted. ([b/155579898](https://issuetracker.google.com/issues/155579898), [aosp/1302153](https://android-review.googlesource.com/c/platform/frameworks/support/+/1302153))

- Fix a bug where `WorkManager` attempts to execute multiple instances of a `Worker` bound to a Foreground Service ([b/156310133](https://issuetracker.google.com/issues/156310133),
  [aosp/1309853](https://android-review.googlesource.com/c/platform/frameworks/support/+/1309853))

### Version 2.4.0-rc01

June 24, 2020

`androidx.work:work-*:2.4.0-rc01` is released. [Version 2.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..098521464a5be8f6d5fb14a9772d859a8e6d3638/work)

**Bug Fixes**

- The in-process scheduler now uses better APIs to determine the name of the process. This is useful to better support apps that use multiple-processes. ([aosp/1324732](https://android-review.googlesource.com/c/platform/frameworks/support/+/1324732))

### Version 2.4.0-beta01

May 20, 2020

`androidx.work:work-gcm:2.4.0-beta01`, `androidx.work:work-runtime:2.4.0-beta01`, `androidx.work:work-runtime-ktx:2.4.0-beta01`, `androidx.work:work-rxjava2:2.4.0-beta01`, and `androidx.work:work-testing:2.4.0-beta01` are released. [Version 2.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..ccc6e95c574b66563952c33fbe26888b93a0e0cb/work)

**Bug Fixes**

- Fix a bug where the `ForegroundService` is not stopped after a foreground `Worker` is interrupted. ([b/155579898](https://issuetracker.google.com/issues/155579898), [aosp/1302153](https://android-review.googlesource.com/c/platform/frameworks/support/+/1302153))
- Fix a bug where `WorkManager` attempts to execute multiple instances of a `Worker` bound to a Foreground Service ([b/156310133](https://issuetracker.google.com/issues/156310133), [aosp/1309853](https://android-review.googlesource.com/c/platform/frameworks/support/+/1309853))
- Add support for dynamically adding factories to delegate to, when using a `DelegatingWorkerFactory`. ([b/156289105](https://issuetracker.google.com/issues/156289105), [aosp/1309745](https://android-review.googlesource.com/c/platform/frameworks/support/+/1309745))
- Align tracking for `BATTERY_NOT_LOW` constraints more closely with the platform. ([aosp/1312583](https://android-review.googlesource.com/c/platform/frameworks/support/+/1312583))

### Version 2.4.0-alpha03

April 29, 2020

`androidx.work:work-*:2.4.0-alpha03` is released. [Version 2.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6c98d66b901be2eecdf89477ccd70d2490ca6fc2..b752a10305d7cd58a7f50ad094ed54af4d765f27/work)

**New Features**

- WorkManager now supports RxJava 3. To use RxJava 3, you should include the following dependency: `implementation "androidx.work:work-rxjava3:2.4.0-alpha03"`. ([aosp/1277904](https://android-review.googlesource.com/c/platform/frameworks/support/+/1277904))
- Added a new lint rule that ensures that `ListenableWorker`implementations are now `public` when using the default `WorkerFactory`. ([aosp/1291262](https://android-review.googlesource.com/c/platform/frameworks/support/+/1291262))

**API Changes**

- Calling `setProgressAsync()` after a `ListenableWorker` has finished execution will now signal an `Exception` via the `ListenableFuture`. ([aosp/1285494](https://android-review.googlesource.com/c/platform/frameworks/support/+/1285494))
- `WorkQuery.Builder` is now marked `final`. ([aosp/1275037](https://android-review.googlesource.com/c/platform/frameworks/support/+/1275037))
- `WorkQuery.Builder` factory methods `withStates`, `withTags` and `withUniqueWorkNames` have been renamed to `fromStates`, `fromTags` and `fromUniqueWorkNames` respectively. ([aosp/1280287](https://android-review.googlesource.com/c/platform/frameworks/support/+/1280287))

**Bug Fixes**

- Ignore `SecurityException`s when tracking network state of a device. ([b/153246136](https://issuetracker.google.com/issues/153246136), [aosp/1280813](https://android-review.googlesource.com/c/platform/frameworks/support/+/1280813))

### Version 2.4.0-alpha02

April 1, 2020

`androidx.work:work-*:2.4.0-alpha02` is released. [Version 2.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2fd74387bd35dc4acb471992654788fab3244b35..6c98d66b901be2eecdf89477ccd70d2490ca6fc2/work)

**New Features**

- Added a new Lint rule that warns when `WorkRequest`s requires both `Constraints.setRequiresCharging(...)` and `Constraints.setRequiresDeviceIdle(...)`. Some devices are never charging and idle at the same time. So such requests would run less frequently than expected. ([aosp/1253840](https://android-review.googlesource.com/c/platform/frameworks/support/+/1253840))

**API Changes**

- Added the ability to query for `WorkInfo`s by using a `WorkQuery`. This is useful when developers want to query `WorkInfo`s by a combination of multiple attributes. For more information look at `WorkQuery.Builder withStates(...)`, `WorkQuery.Builder withTags(...)` or `WorkQuery.Builder withUniqueWorkNames(...)`. ([aosp/1253230](https://android-review.googlesource.com/c/platform/frameworks/support/+/1253230), [b/143847546](https://issuetracker.google.com/issues/143847546))

- Calls to `setForegroundAsync()` that do not complete before completion of a `ListenableWorker` will now be signalled via an `IllegalStateException` on the returned `ListenableFuture`. ([aosp/1262743](https://android-review.googlesource.com/c/platform/frameworks/support/+/1262743))

**Bug Fixes**

- Fixed the lint rule that checks for invalid interval durations for `PeriodicWorkRequest`s. ([aosp/1254846](https://android-review.googlesource.com/c/platform/frameworks/support/+/1254846), [b/152606442](https://issuetracker.google.com/issues/152606442))

### Version 2.4.0-alpha01

March 4, 2020

`androidx.work:work-*:2.4.0-alpha01` is released. [Version 2.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d7ffb1e3214adc08092397ca92881b05fb69521a..2fd74387bd35dc4acb471992654788fab3244b35/work)

**New Features**

- `WorkManager`s in-process scheduler is now more capable. Previously, the in-process Scheduler would only consider executing work that was *not* delayed and whose constraints were met. Now, the in-process scheduler tracks `WorkRequest`s which might be executed in the future, including `PeriodicWorkRequest`s. The in-process Scheduler also does **not** observe [scheduling limits](https://developer.android.com/reference/androidx/work/Configuration.Builder#setMaxSchedulerLimit(int)) (but is still restricted to the size of the `Executor` being used by WorkManager). This means that the application can now execute a lot more `WorkRequest`s when the app is in the foreground. ([aosp/1185778](https://android-review.googlesource.com/c/platform/frameworks/support/+/1185778))

- Added the ability to request diagnostic information from WorkManager using `adb shell am broadcast -a "androidx.work.diagnostics.REQUEST_DIAGNOSTICS" -p "<your_app_package_name>"`. This provides a lot of useful information including:

  - WorkRequests that were completed in the last 24 hours.
  - WorkRequests that are currently RUNNING.
  - Scheduled WorkRequests. ([aosp/1235501](https://android-review.googlesource.com/c/platform/frameworks/support/+/1235501))
- New Lint rules which enforce:

  - Use of the right `foregroundServiceType` when using `setForegroundAsync()` APIs. ([b/147873061](https://issuetracker.google.com/issues/147873061), [aosp/1215915](https://android-review.googlesource.com/c/platform/frameworks/support/+/1215915))
  - Specifying `JobScheduler` ids that `WorkManager` should use when using `JobService` APIs directly. ([aosp/1223567](https://android-review.googlesource.com/c/platform/frameworks/support/+/1223567))

**API Changes**

- Add `ExistingWorkPolicy.APPEND_OR_REPLACE` which is similar to `APPEND`, but **replaces** a chain that has cancelled or failed prerequisites.
  ([b/134613984](https://issuetracker.google.com/issues/134613984),
  [aosp/1199640](https://android-review.googlesource.com/c/platform/frameworks/support/+/1199640))

- Provide the ability to add a custom `RunnableScheduler` to track `WorkRequest`s that need to be executed in the future. This is used by the in-process Scheduler. ([aosp/1203944](https://android-review.googlesource.com/c/platform/frameworks/support/+/1203944))

**Bug Fixes**

- Deprecated `setProgress()` in `RxWorker` because it previously returned a `Single<Void>` which is an impossible type. Added a new API `setCompletableProgress()` which returns a `Completable` instead; and added new Lint rules which help migrate to the new APIs. ([b/150080946](https://issuetracker.google.com/issues/150080946), [aosp/1242665](https://android-review.googlesource.com/c/platform/frameworks/support/+/1242665))

## Version 2.3.4

### Version 2.3.4

March 18, 2020

`androidx.work:work-*:2.3.4` is released. [Version 2.3.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3735155f52238ca168c5608ed332179382b76899..a6360a30a94ce26f8b4d9322eccd3038b669adee/work)

**Bug Fixes**

- Fixed a bug which would cause multiple instances of a long running `Worker`s to run, after exceeding the 10 minute execution window. ([aosp/1247484](https://android-review.googlesource.com/c/platform/frameworks/support/+/1247484), [b/150553353](https://issuetracker.google.com/issues/150553353))
- Fix for WorkManager's lint `IssueRegistry`. Thank you [@ZacSweers](https://twitter.com/ZacSweers) from Slack, for the contribution. ([aosp/1217923](https://android-review.googlesource.com/c/platform/frameworks/support/+/1217923))

## Version 2.3.3

### Version 2.3.3

March 4, 2020

`androidx.work:work-*:2.3.3` is released. [Version 2.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3735155f52238ca168c5608ed332179382b76899..107a42c26aa39c3f96f6de0cc46021ef39b76cc6/work)

**Bug Fixes**

- Fixed a bug where if a `Worker` was interrupted, it would not get rescheduled correctly. ([b/150325687](https://issuetracker.google.com/issues/150325687), [aosp/1246571](https://android-review.googlesource.com/c/platform/frameworks/support/+/1246571))

## Version 2.3.2

### Version 2.3.2

February 19, 2020

`androidx.work:work-*:2.3.2` are released. [Version 2.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d7ffb1e3214adc08092397ca92881b05fb69521a..3735155f52238ca168c5608ed332179382b76899/work)

**Bug Fixes**

- Fixes an issue where WorkManager exceeds the 100 job limit in JobScheduler in rare cases. ([aosp/1226859](https://android-review.googlesource.com/c/platform/frameworks/support/+/1226859), [b/149092520](https://issuetracker.google.com/issues/149092520))
- Fix for a race condition in ConstraintControllers. ([aosp/1220100](https://android-review.googlesource.com/c/platform/frameworks/support/+/1220100))
- Improved the management foreground Service lifecycle for long running Workers. ([aosp/1226295](https://android-review.googlesource.com/c/platform/frameworks/support/+/1226295))
- Improved the management of cancellation of Notifications for long running Workers upon Worker cancellation. ([aosp/1228346](https://android-review.googlesource.com/c/platform/frameworks/support/+/1228346))

## Version 2.3.1

### Version 2.3.1

February 5, 2020

`androidx.work:work-*:2.3.1` is released. [Version 2.3.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/cdec0090b957bd9020ff2462c3006cbb1381ddc6..d7ffb1e3214adc08092397ca92881b05fb69521a/work).

**Bug fixes**

- Better manage the lifecycle of `Notification`s for long running `Worker`s that run when a foreground `Service` is active. ([aosp/1218539](https://android-review.googlesource.com/c/platform/frameworks/support/+/1218539), [b/147249312](https://issuetracker.google.com/issues/147249312))
- `WorkManager` now depends on `androidx.sqlite:sqlite-framework:2.1.0` stable. ([aosp/1217729](https://android-review.googlesource.com/c/platform/frameworks/support/+/1217729))
- Added lint rules to ensure that a `foregroundServiceType` is specified in the `AndroidManifest.xml` when using `foregroundServiceType`s in `ForegroundInfo`. ([aosp/1214207](https://android-review.googlesource.com/c/platform/frameworks/support/+/1214207), [b/147873061](https://issuetracker.google.com/issues/147873061))

## Version 2.3.0

### Version 2.3.0

January 22, 2020

`androidx.work:work-*:2.3.0` is released with no changes since `2.3.0-rc01`. [Version 2.3.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/491f8d1faf067d76cfaf0c8e82561386861e55e1..cdec0090b957bd9020ff2462c3006cbb1381ddc6/work).

**Important changes since 2.2.0**

- Support for long running or important work via `ListenableWorker#setForegroundAsync()`.
- Support for Worker Progress via `ListenableWorker#setProgressAsync()`.
- WorkManager now packages additional lint rules as part of the library which helps catch bugs early.

### Version 2.3.0-rc01

January 8, 2020

`androidx.work:work-*:2.3.0-rc01` is released. [Version 2.3.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/740cde70237dd276f8ad66dfe9528b1cdb5d54bb..491f8d1faf067d76cfaf0c8e82561386861e55e1/work).

This release is identical to [`2.3.0-beta02`](https://developer.android.com/jetpack/androidx/releases/work#2.3.0-beta02)

**Bug fixes**

- The `work-testing` artifact now defines an `api` dependency on `work-runtime-ktx`. ([aosp/1194410](https://android-review.googlesource.com/c/platform/frameworks/support/+/1194410))

### Version 2.3.0-beta02

December 18, 2019

`androidx.work:work-*:2.3.0-beta02` is released. [Version 2.3.0-beta02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0042c0019bb455afc79ddfec9bf2993d018f70ce..740cde70237dd276f8ad66dfe9528b1cdb5d54bb/work).

**New features**

- Added a better error message for non-recoverable SQLite exceptions. ([aosp/1185777](https://android-review.googlesource.com/c/1185777))
- Added a lint rule which ensures that the content provider `androidx.work.impl.WorkManagerInitializer` is removed from the `AndroidManifest.xml` when using on demand initialization. ([aosp/1167007](https://android-review.googlesource.com/c/1167007))
- Added a lint warning when `enqueue()` is used for a `PeriodicWorkRequest` instead of `enqueueUniquePeriodicWork()`. ([aosp/1166032](https://android-review.googlesource.com/c/1166032))

**API changes**

- `ForegroundInfo` now requires you to specify the `notificationId` to be used when using `ListenableWorker.setForegroundAsync()`. **This is a breaking change.** This allows you to run multiple long running `Worker`s in parallel. `WorkManager` also better manages lifetimes of the provided `Notification`s. ([b/145473554](https://issuetracker.google.com/issues/145473554), [aosp/1181208](https://android-review.googlesource.com/c/1181208), [asop/1181216](https://android-review.googlesource.com/c/1181216), [asop/1183577](https://android-review.googlesource.com/c/1183577))

**Bug fixes**

- Fixed a bug in the AlarmManager implementation where alarms were not being cleaned up correctly. ([aosp/1156444](https://android-review.googlesource.com/c/1156444))
- Fixed a bug where an empty list of `WorkRequest`s would cause an incorrect `WorkContinuation` chain to be built. ([b/142835274](https://issuetracker.google.com/issues/142835274), [aosp/1157051](https://android-review.googlesource.com/c/1157051))

**Dependency changes**

- WorkManager now uses Room 2.2.2.

### Version 2.3.0-beta01

November 20, 2019

`androidx.work:work-*:2.3.0-beta01` is released. [Version 2.3.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/bc0450b5cd9c18270bfc4ce5068140e0b76d52c9..0042c0019bb455afc79ddfec9bf2993d018f70ce/work).

**New features**

- Added a new lint rule which prevents developer errors due to incorrect implementation of `androidx.work.Configuration.Provider` when using on-demand initialization. [aosp/1164559](https://android-review.googlesource.com/c/platform/frameworks/support/+/1164559)

### Version 2.3.0-alpha03

October 23, 2019

`androidx.work:work-*:2.3.0-alpha03` is released. [Version 2.3.0-alpha03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/3ceb16dfb202e267249a5a5f14e9159ff0f95d9e..bc0450b5cd9c18270bfc4ce5068140e0b76d52c9/work).

**New features**

- Added `WorkManager.createCancelPendingIntent()` API which makes it easy to cancel `WorkRequest`s without having to register another component in the `AndroidManifest.xml`. This API makes it especially easy to cancel `WorkRequest`s from `Notification`s. We expect this to be paired with the new foreground APIs in 2.3.0.
- WorkManager now depends on `androidx.room:*:2.2.0` stable.

**API changes**

- Renamed `ForegroundInfo.getNotificationType()` to `ForegroundInfo.getForegroundServiceType()` to be more consistent with the underlying platform APIs. ([b/142729893](https://issuetracker.google.com/issues/142729893), [aosp/1143316](https://android-review.googlesource.com/c/platform/frameworks/support/+/1143316))

**Bug fixes**

- Fixed a bug which is caused by an unnecessary call to `setTransactionSuccessful()` outside of a transaction. This happens for rare migrations. ([b/142580433](https://issuetracker.google.com/issues/142580433), [aosp/1141737](https://android-review.googlesource.com/c/platform/frameworks/support/+/1141737))

### Version 2.3.0-alpha02

October 9, 2019

`androidx.work:work-*:2.3.0-alpha02` is released. [Version 2.3.0-alpha02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/2114e28ad291adc12d4ea9bd4038a211daec16b8..3ceb16dfb202e267249a5a5f14e9159ff0f95d9e/work).

**New features**

- WorkManager now supports running long running or important work that should be kept alive by the OS. For more information look at `ListenableWorker#setForegroundAsync()` (or `CoroutineWorker#setForeground()` for Kotlin). ([aosp/1133636](https://android-review.googlesource.com/c/platform/frameworks/support/+/1133636))

**API changes**

- The `containsKey` API in `Data` is renamed to `hasKeyWithValueOfType`. The corresponding extension method in the `ktx` library has also been renamed. ([b/141916545](https://issuetracker.google.com/issues/141916545))

**Bug fixes**

- WorkManager schedules work fairly when the number of `WorkRequest`s enqueued approach [scheduling limits](https://developer.android.com/reference/androidx/work/Configuration.Builder#setMaxSchedulerLimit(int)). ([aosp/1105766](https://android-review.googlesource.com/c/platform/frameworks/support/+/1105766))
- WorkManager calls `ListenableWorker#onStopped()` only if the work is not already completed. ([b/140055777](https://issuetracker.google.com/issues/140055777))
- WorkManager now removes progress information when a worker gets interrupted or reaches its terminal state. ([aosp/1114572](https://android-review.googlesource.com/c/platform/frameworks/support/+/1114572))
- `Data` now has a much more useful `toString()`representation. ([b/140945323](https://issuetracker.google.com/issues/140945323))
- `Data` now has a better `equals()` method. It also supports `deepEquals` for `Array` types. ([b/140922528](https://issuetracker.google.com/issues/140922528))
- WorkManager now stores its internal database and preference files in a no backup directory. ([b/114808216](https://issuetracker.google.com/issues/114808216))

### Version 2.3.0-alpha01

August 22, 2019

`androidx.work:work-*:2.3.September 5, 20190-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/57828f2feae3e65ae15c1cd8acd4f56af451ce5e..2114e28ad291adc12d4ea9bd4038a211daec16b8/work).

**New features**

- `ListenableWorker`s can now set progress via the `setProgressAsync()` API. Also added a corresponding `suspend`-ing `setProgress` API in `CoroutineWorker` and a `setProgress` in `RxWorker` which returns a `Single<Void>`. With these new APIs Workers can convey progress information via `WorkInfo` which has a corresponding `getProgress` API. ([b/79481554](https://issuetracker.google.com/issues/79481554))
- `Data` has a `containsKey()` API which can be used to validate that input data to `Worker`s has keys with the expected type. ([b/117136838](https://issuetracker.google.com/issues/117136838))
- `Data` can now be serialized using `Data.toByteArray()` and `Data.fromByteArray()`. Note that there are no versioning guarantees with `Data` so you should *not* persist it or use it for IPC between applications. They are only safe to be used between multiple processes of the *same* application.
- Added the ability to specify an `InputMergerFactory` via `Configuration.setInputMergerFactory`. ([b/133273159](https://issuetracker.google.com/issues/133273159))

**API changes**

- WorkManager will throw an instance of `IllegalStateException` if a `WorkerFactory` returns an instance of `ListenableWorker` which has been previously invoked. ([b/139554406](https://issuetracker.google.com/issues/139554406))
- Documentation updates around `ListenableFuture` cancellation and the `onStopped()` callback in `ListenableWorker`. ([b/138413671](https://issuetracker.google.com/issues/138413671))

**Bug fixes**

- The in-process Scheduler now ignores `WorkRequest`s with the `idle` constraint. These requests are now only picked up by `JobScheduler` when the device is actually `idle`. ([aosp/1089779](https://android-review.googlesource.com/c/platform/frameworks/support/+/1089779))
- `TestScheduler` now correctly uses the specified `Executor` for its internal task executor in tests. ([aosp/1090749](https://android-review.googlesource.com/c/platform/frameworks/support/+/1090749))

## Version 2.2.0

### Version 2.2.0

August 15, 2019

`androidx.work:work-*:2.2.0` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/cb0c2f6acf089f2ad79726ab04dc2a56335999e4..ce4459ef9ceb05f7ffedfe072ed16f0aca352d07/work).

This release is identical to `androidx.work:work-*:2.2.0-rc01`.

**Important Changes in 2.2.0 from 2.1.0**

`androidx.work:work-gcm:2.2.0` is a new Maven artifact which supports the use of GCMNetworkManager as a scheduler when Google Play Services is available for API levels \<= 22. This is an optional dependency that helps with more reliable and performant background processing on older API versions. If your app uses Google Play Services, add this dependency to your gradle file to automatically get GCMNetworkManager support. If Play Services is not available, WorkManager will continue to fall back to AlarmManager on older devices.

### Version 2.2.0-rc01

July 30, 2019

`androidx.work:work-*:2.2.0-rc01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/57828f2feae3e65ae15c1cd8acd4f56af451ce5e..cb0c2f6acf089f2ad79726ab04dc2a56335999e4/work).

**Bug fixes**

- Fixed a bug in the AlarmManager implementation that causes the Service to shutdown prematurely and resulting in a `RejectedExecutionException` in rare cases. ([aosp/1092374](https://android-review.googlesource.com/1092374)) ([b/138238197](https://issuetracker.google.com/138238197)).
- Added a workaround for a `NullPointerException` when using `JobScheduler` APIs on some devices. ([aosp/1091020](https://android-review.googlesource.com/1091020)) ([b/138364061](https://issuetracker.google.com/138364061)), ([b/138441699](https://issuetracker.google.com/138441699))

### Version 2.2.0-beta02

July 19, 2019

`androidx.work:work-*:2.2.0-beta02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/32988b2236646245cde4cd158dedbf8c6b2fd0c2..57828f2feae3e65ae15c1cd8acd4f56af451ce5e/work).

**Bug fixes**

- Removed unintentional jacoco dependency that was introduced in `2.2.0-beta01`.

### Version 2.2.0-beta01

July 17, 2019

`androidx.work:work-*:2.2.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/41741982b76f2249a5fc71f2b2fa86aed5e6b6df..32988b2236646245cde4cd158dedbf8c6b2fd0c2/work).
| **Caution:** This version contains an unintentional dependency on `org.jacoco:org.jacoco.agent:0.8.3`, which can cause a build failure. Please update to the latest version, in which this dependency has been removed.

**New features**

- `androidx.work:work-gcm:2.2.0-beta01` is a new Maven artifact which supports the use of GCMNetworkManager as a scheduler when Google Play Services is available for API levels \<= 22. This is an *optional* dependency that helps with more reliable and performant background processing on older API versions. If your app uses Google Play Services, add this dependency to your gradle file to automatically get GCMNetworkManager support. If Play Services is not available, WorkManager will continue to fall back to AlarmManager on older devices.

**Bug fixes**

- Fix for `IllegalArgumentException` when tracking network state on Nvidia Shield K1 tablets. ([aosp/1010188](https://android-review.googlesource.com/1010188))

## Version 2.1.0

### Version 2.1.0

July 11, 2019

`androidx.work:work-*:2.1.0` is released. This release is identical to `androidx.work:work-*:2.1.0-rc01`.

**Important changes since 2.0.1**

- `work-runtime-ktx` now requires Java 8. If you run into any issues, you can add the following to your `build.gradle`: `kotlinOptions {
  jvmTarget = "1.8"
  }`
- Added on-demand initialization for WorkManager, which will create WorkManager only when referenced. [b/127497100](https://issuetracker.google.com/127497100) To set up your project for on-demand initialization:
  1. [Disable the automatic initializer](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration#remove-default).
  2. Implement `Configuration.Provider` on your custom `Application` object.
  3. Change all references of `WorkManager.getInstance()` to `WorkManager.getInstance(Context)`. As part of this change, we have deprecated `WorkManager.getInstance()`. It is always safer to call the new `WorkManager.getInstance(Context)` replacement, even if you're not doing on-demand initialization.
- `PeriodicWorkRequest`s now support initial delays. You can use the `setInitialDelay` method on `PeriodicWorkRequest.Builder` to set an initial delay. [b/111404867](https://issuetracker.google.com/111404867)
- Added the ability to delegate to one or more registered `WorkerFactory`s using `DelegatingWorkerFactory`. [b/131435993](https://issuetracker.google.com/131435993)
- Added the ability to customize the `Executor` used by WorkManager for all its internal book-keeping via `Configuration.Builder.setTaskExecutor`.
- Added the ability to create unit testable `Worker` and `ListenableWorker` classes by using `TestWorkerBuilder` and `TestListenableWorkerBuilder` in the `work-testing` artifact.
  - Note that `work-testing` now pulls in Kotlin as a dependency and includes several Kotlin extensions by default.
- Added run attempt count to `WorkInfo`. [b/127290461](https://issuetracker.google.com/127290461)
- `Data` types can now store and retrieve bytes and byte arrays. This does NOT change the maximum size of `Data` objects.
- WorkManager now depends on `Room 2.1.0`, which should fix some database issues.

### Version 2.1.0-rc01

June 27, 2019

`androidx.work:work-*:2.1.0-rc01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/0dfc7dae1875b1c0463d279bf6fd557447b99caf..5f859f4f6909b055eac53ac7fe918a9f65e489c5/work).

**Bug fixes**

- Fixed a bug which would cause an application to crash when executing jobs with `JobScheduler` while a backup was in progress [b/135858602](https://issuetracker.google.com/135858602).

### Version 2.1.0-beta02

June 20, 2019

`androidx.work:work-*:2.1.0-beta02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/3aa279901a440d8a3a16c07c7e49361991097939..eae198ee097b359f70989d2c5c0f5ff6f6b72ead/work).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**Bug fixes**

- `TestListenableWorkerBuilder` now uses the correct `WorkerFactory` when creating instances of `ListenableWorker`. [b/135275844](https://issuetracker.google.com/135275844)
- Fixed a bug which caused drifts in the execution windows for `WorkRequest`s due to process death. [b/135272196](https://issuetracker.google.com/135272196)

### Version 2.1.0-beta01

June 13, 2019

`androidx.work:work-*:2.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/5243b462794554b6dcc3f51793c5ef22531bb6ec..3aa279901a440d8a3a16c07c7e49361991097939/work).
| **Note:** This version is dependent on the Java 8 programming language. Please read [Use Java 8 language features](https://developer.android.com/studio/write/java8-support) to learn how to use it in your project.

**Bug fixes**

- WorkManager now depends on `Room 2.1.0`, which should fix some database issues.
- Removed some startup disk I/O on the main thread.
- Fixed a potential deadlock in constraint tracking. [b/134361006](https://issuetracker.google.com/134361006)
- Preemptively cancelled invalid jobs attributed to WorkManager. [b/134058261](https://issuetracker.google.com/134058261)
- Added some defensive calls to JobScheduler APIs for misbehaving devices.

### Version 2.1.0-alpha03

June 5, 2019

`androidx.work:*:2.1.0-alpha03` is released.

**Bug fixes**

- Improved documentation for `PeriodicWorkRequest`s.
- `WorkManagerTestInitHelper` now uses the correct background executor for tests.
- Fixes for SQLite issues when dealing with large transactions on some devices. ([b/130182503](https://issuetracker.google.com/130182503))
- WorkManager's dependencies are now more granular. ([b/133169148](https://issuetracker.google.com/133169148)).
- Workaround OEM specific bugs in the implementation of `JobScheduler` when scheduling jobs using WorkManager.
- Improvements in the AlarmManager based scheduler around service lifetimes that previously caused rare crashes. ([b/133313734](https://issuetracker.google.com/133313734))

### Version 2.1.0-alpha02

May 16, 2019

WorkManager 2.1.0-alpha02 is released. This version contains several new APIs.

**API Changes**

- `PeriodicWorkRequest`s now support initial delays. You can use the
  `setInitialDelay` method on `PeriodicWorkRequest.Builder` to set an initial
  delay. [b/111404867](https://issuetracker.google.com/111404867)

- Added the ability to delegate to one or more registered `WorkerFactory`s using
  `DelegatingWorkerFactory`. [b/131435993](https://issuetracker.google.com/131435993)

- Added the ability to customize the `Executor` used by WorkManager for
  all its internal book-keeping via `Configuration.Builder.setTaskExecutor`.

- Improved documentation around `WorkRequest.keepResultsForAtLeast` ([b/130638001](https://issuetracker.google.com/130638001)),
  on-demand initialization, and `PeriodicWorkRequest.Builder` ([b/131711394](https://issuetracker.google.com/131711394)).

### Version 2.1.0-alpha01

April 24, 2019

WorkManager 2.1.0-alpha01 is released. This version contains several new APIs.
Please note that starting with this version, there will be new features that
won't get backported to the 1.x release. We recommend switching to 2.x.

**API Changes**

- Added on-demand initialization for WorkManager, which will create WorkManager only when referenced. [b/127497100](https://issuetracker.google.com/127497100) To set up your project for on-demand initialization:
  1. [Disable the automatic initializer](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration#removing_the_default_initializer).
  2. Implement `Configuration.Provider` on your custom `Application` object.
  3. Change all references of `WorkManager.getInstance()` to `WorkManager.getInstance(Context)`. As part of this change, we have deprecated `WorkManager.getInstance()`. It is always safer to call the new `WorkManager.getInstance(Context)` replacement, even if you're not doing on-demand initialization.
- Added the ability to create unit testable `Worker` and `ListenableWorker` classes by using `TestWorkerBuilder` and `TestListenableWorkerBuilder` in the `work-testing` artifact.
  - Note that `work-testing` now pulls in Kotlin as a dependency, but also includes several Kotlin extensions by default.
- Added run attempt count to `WorkInfo`. [b/127290461](https://issuetracker.google.com/127290461)
- `Data` types can now store and retrieve bytes and byte arrays. This does NOT change the maximum size of `Data` objects.
- Deprecated `CoroutineWorker.coroutineContext`. This field was incorrectly typed as a `CoroutineDispatcher`; you should no longer need it as you can go to the desired coroutineContext yourself in the body of the suspending function.
- `RxWorker.createWork()` and `RxWorker.getBackgroundScheduler()` are now annotated with `@NonNull` return types.

## Version 2.0.1

### Version 2.0.1

April 9, 2019

WorkManager 2.0.1 is released. This release is identical to
[2.0.1-rc01](https://developer.android.com/jetpack/androidx/releases/work#2.0.1-rc01).

### Version 2.0.1-rc01

April 3, 2019

WorkManager 2.0.1-rc01 is released. This version contains some bug fixes. For
legacy 1.x users, some of these changes also appear in
[1.0.1-rc01](https://developer.android.com/jetpack/androidx/releases/work#1.0.1-rc01).

**Bug Fixes**

- Robolectric tests now operate properly with WorkManager. [b/122553577](https://issuetracker.google.com/122553577)
- Fixed an edge case crash with constraints tracking not being cleaned up on pre-JobScheduler APIs. [b/129226383](https://issuetracker.google.com/129226383)
- Fixed a `StackOverflowError` dealing with long chains of work. [b/129091233](https://issuetracker.google.com/129091233)
- Updated documentation for `PeriodicWorkRequest`s to indicate that flex time is not supported on API 23.
- Fixed some broken links in the Kotlin documentation.

## Version 2.0.0

### Version 2.0.0

March 20, 2019

WorkManager 2.0.0 is released. This version is identical to 2.0.0-rc01 and is
the AndroidX version of 1.0.0 stable with AndroidX dependencies. We recommend
targeting this version instead of the legacy 1.x versions. All active
development will target 2.x and 1.x will only receive critical bug fixes for a
limited time.

### Version 2.0.0-rc01

March 7, 2019

WorkManager 2.0.0-rc01 is released. This version is identical to 1.0.0 stable
but has AndroidX dependencies. Once this reaches 2.0.0 stable, you should
include this version and the legacy 1.x versions will only receive some critical
bug fixes. All active development will target 2.x.

## Pre-AndroidX Dependencies

For information on using Kotlin extensions, see the [KTX documentation](https://developer.android.com/kotlin/ktx).  
Reference docs: [Java](https://developer.android.com/reference/androidx/work/package-summary)  

### Groovy

```groovy
dependencies {
    def work_version = "1.0.1"

    // (Java only)
    implementation "android.arch.work:work-runtime:$work_version"

    // Kotlin + coroutines
    implementation "android.arch.work:work-runtime-ktx:$work_version"

    // optional - RxJava2 support
    implementation "android.arch.work:work-rxjava2:$work_version"
    // optional - Test helpers
    androidTestImplementation "android.arch.work:work-testing:$work_version"
}
```

### Kotlin

```kotlin
dependencies {
    val work_version = "1.0.1"

    // (Java only)
    implementation("android.arch.work:work-runtime:$work_version")

    // Kotlin + coroutines
    implementation("android.arch.work:work-runtime-ktx:$work_version")

    // optional - RxJava2 support
    implementation("android.arch.work:work-rxjava2:$work_version")

    // optional - Test helpers
    androidTestImplementation("android.arch.work:work-testing:$work_version")
}
```
| **Note:** WorkManager classes are already in the androidx.work package, but currently depend on non-AndroidX dependencies including the Support Library 27.1 and associated Arch component versions. A version of WorkManager with AndroidX dependencies will be released in the future.

## Version 1.0.1

### Version 1.0.1

April 9, 2019

WorkManager 1.0.1 is released. This release is identical to
[1.0.1-rc01](https://developer.android.com/jetpack/androidx/releases/work#1.0.1-rc01).

Please note that we *strongly* encourage users to update to WorkManager 2.x, as
there will be very few updates to the 1.x branch moving forward. New APIs will
also not be released for the 1.x library.

### Version 1.0.1-rc01

April 2, 2019

WorkManager 1.0.1-rc01 is released. This version contains some bug fixes.

**Bug Fixes**

- Robolectric tests now operate properly with WorkManager. [b/122553577](https://issuetracker.google.com/122553577)
- Fixed an edge case crash with constraints tracking not being cleaned up on pre-JobScheduler APIs. [b/129226383](https://issuetracker.google.com/129226383)
- Fixed a `StackOverflowError` dealing with long chains of work. [b/129091233](https://issuetracker.google.com/129091233)

## Version 1.0.0

### Version 1.0.0

March 05, 2019

This is WorkManager's 1.0.0 stable release. This version of WorkManager is
identical to 1.0.0-rc02.

### Version 1.0.0-rc02

February 21, 2019

This is the second release candidate for WorkManager's 1.0.0 stable release.
This release contains two bug fixes.

**Bug Fixes**

- `Worker`s are now correctly scheduled after an application crash.
  [b/124546316](https://issuetracker.google.com/124546316)

- `Worker`s that throw an unchecked `Exception` are now correctly marked as
  `FAILED` and no longer crash the app process.

### Version 1.0.0-rc01

February 14, 2019

This is a release candidate for WorkManager's 1.0.0 stable release.
This release contains one bug fix.

**Bug Fixes**

- The AlarmManager based implementation now correctly respects `flex` windows for PeriodicWorkRequests. [b/124274584](https://issuetracker.google.com/124274584)

### Version 1.0.0-beta05

February 6, 2019

This release contains some bug fixes.

**Bug Fixes**

- Fixed a case where `JobScheduler.getPendingJob(...)` was used on API 23. [b/123893059](https://issuetracker.google.com/123893059)
- Fixed a `NullPointerException` on devices running Android 5.1 (API level 22) or lower. [b/123835104](https://issuetracker.google.com/123835104)

### Version 1.0.0-beta04

February 4, 2019

This release contains some bug fixes.

**Bug Fixes**

- Improved scheduling of PeriodicWork for the AlarmManager based implementation.
- Fixed a case where WorkManager failed to correctly track constraints when using the AlarmManager based implementation. [b/123379508](https://issuetracker.google.com/123379508)
- Fixed a case when WorkManager failed to retry work on process death when using the AlarmManager based implementation. [b/123329850](https://issuetracker.google.com/123329850)
- Fixed a case which would cause WorkManager to leak Wakelocks when using the AlarmManager based implementation.

### Version 1.0.0-beta03

January 25, 2019

This release contains some bug fixes.

**Bug Fixes**

- We introduced a regression `1.0.0-beta02` that was causing work to not execute properly in some situations. [b/123211993](https://issuetracker.google.com/123211993)
- Fixed a case where work wasn't properly honoring backoff timing. [b/122881597](https://issuetracker.google.com/122881597)
- Fixed a `ConcurrentModificationException` on devices running Android 5.1 (API or) or lower. This is a continuation of the fix in `1.0.0-beta02`. [b/121345393](https://issuetracker.google.com/121345393)
- Added `exported=false` for some components in our manifest that were missing this annotation.
- Included information about how WorkManager interacts with the OS in the package-level documentation.

### Version 1.0.0-beta02

January 15, 2019

This release contains some bug fixes.

**Bug Fixes**

- Fixed an edge case where periodic work could run more than once per interval on devices running Android 6.0 (API level 23). [b/121998363](https://issuetracker.google.com/121998363)
- Fixed a `ConcurrentModificationException` on devices running Android 5.1 (API level 22) or lower. [b/121345393](https://issuetracker.google.com/121345393)
- Fixed erroneous execution of work when Constraints aren't met on devices running Android 5.1 (API level 22) or lower. [b/122578012](https://issuetracker.google.com/122578012)
- Optimized work completion handling to be faster in some edge cases. [b/122358129](https://issuetracker.google.com/122358129)
- Added a change to address potential race conditions among multiple instances of `LiveData` that WorkManager uses.
- Moved to use `Room` dependency `1.1.1` instead of `1.1.1-rc01`; these versions are identical. [b/122578011](https://issuetracker.google.com/122578011)

### Version 1.0.0-beta01

December 19, 2018

This release contains no API changes; moving forward, WorkManager is expected to stay API stable until the next version unless there is a critical problem. This release contains some bug fixes.

**Bug Fixes**

- Previously-cancelled children of successfully completed parent work will no longer run. [b/120811767](https://issuetracker.google.com/120811767)
- Properly initialized logging classes (primarily surfaced during tests).

### Version 1.0.0-alpha13

December 12, 2018

This release contains a minor API change that will be helpful for some Kotlin users.

**API Changes**

- `androidx.work.Result` has been moved to be an inner class of `ListenableWorker`. This prevents refactoring conflicts with Kotlin's top-level `Result` class. *This is a breaking API change.* [b/120564418](https://issuetracker.google.com/120564418)

**Breaking API Changes**

- `androidx.work.Result` has been moved to be an inner class of `ListenableWorker`.

### Version 1.0.0-alpha12

December 5, 2018

This release contains some breaking API changes; please see the *Breaking API Changes* section below. This version is likely to be released as our first beta. `alpha12` also contains extensive documentation updates.

**API Changes**

- A new artifact, `work-rxjava2`, introduces `RxWorker`. This is a `ListenableWorker` that expects a `Single<Payload>`.
- Support for Firebase JobDispatcher has been removed because of its impending deprecation. This means that the `work-firebase` artifact will no longer be updated as we head into beta. We will be looking into adding an alternative in the future.
- Combined `Payload` into `Result`. `Result` is now a "sealed class" with three concrete implementations, which you can obtain via `Result.success()` (or `Result.success(Data)`), `Result.failure()` (or `Result.failure(Data)`), and `Result.retry()`. Your `ListenableFuture`s now result `Result` instead of `Payload`. `Worker`s don't have getter and setter methods for output `Data`. *This is a breaking change.*
- Added `Constraints.Builder.setTriggerContentMaxDelay(long, TimeUnit)` and `Constraints.Builder.setTriggerContentUpdateDelay(long, TimeUnit)` and variants to better support slow triggering content URIs. [b/119919774](https://issuetracker.google.com/119919774)
- Added `WorkRequest.Builder.setBackoffCriteria(BackoffPolicy, Duration)` variant. This method requires API 26.
- Added `Operation.await()` and `ListenableFuture.await()` Kotlin extension methods.
- Renamed `Operation.getException()` to `Operation.getThrowable()`. *This is a breaking change.*
- The `ContentUriTriggers` class and methods referencing it are no longer available for public usage. *This is a breaking change.*
- Removed the rest of the varargs methods in `WorkManager`, `WorkContinuation`, and `OneTimeWorkRequest` to streamline the API. To fix any build problems, you can wrap your existing varargs with `Arrays.asList(...)`. We still include single-argument versions of each method. *This is a breaking change.*
- Removed `WorkContinuation.combine(OneTimeWorkRequest, *)` variants. They were presenting a confusing API; the existing `combine` methods are more understandable. *This is a breaking change.*

**Bug Fixes**

- Pre-Marshmallow implementations are now more reliable in recovering from process death of an already-executing task.
- `LiveData` that is observed via `observeForever` is tracked via WorkManager. This is a backport of a Room library fix. [b/74477406](https://issuetracker.google.com/74477406)
- `Data.Builder.build()` now throws an exception if the serialized object exceeds its maximum size. This previously would only happen on a background thread where you couldn't properly handle it.
- Further distinguished stopped vs. cancelled work; `getWorkInfoById()` will return a `WorkInfo` with the `CANCELLED` `State` during `ListenableWorker.onStopped()`.
- Treat `null` `Result`s as failures in `ListenableWorker`. [b/120362353](https://issuetracker.google.com/120362353)
- Speculative fix for Shield Tablets running API 24 that sometimes threw an `IllegalArgumentException`. [b/119484416](https://issuetracker.google.com/119484416)

**Breaking API Changes**

- Support for Firebase JobDispatcher has been removed because of its impending deprecation. This means that the `work-firebase` artifact will no longer be updated as we head into beta. We will be looking into adding an alternative in the future.
- Combined `Payload` into `Result`. `Result` is now a "sealed class" with three concrete implementations, which you can obtain via `Result.success()` (or `Result.success(Data)`), `Result.failure()` (or `Result.failure(Data)`), and `Result.retry()`. Your `ListenableFuture`s now result `Result` instead of `Payload`. `Worker`s don't have getter and setter methods for output `Data`.
- Added `Operation.await()` and `ListenableFuture.await()` Kotlin extension methods.
- Renamed `Operation.getException()` to `Operation.getThrowable()`.
- The `ContentUriTriggers` class and methods referencing it are no longer available for public usage.
- Removed the rest of the varargs methods in `WorkManager`, `WorkContinuation`, and `OneTimeWorkRequest` to streamline the API. To fix any build problems, you can wrap your existing varargs with `Arrays.asList(...)`. We still include single-argument versions of each method.
- Removed `WorkContinuation.combine(OneTimeWorkRequest, *)` variants. They were presenting a confusing API; the existing `combine` methods are more understandable.

### Version 1.0.0-alpha11

November 8, 2018

This release contains many changes that will become stable API at `beta`.
There are breaking API changes in this release; please see the *Breaking API Changes* section below.

**API Changes**

- `work-runtime-ktx` introduces a new `CoroutineWorker`.
- `WorkStatus` has been renamed to `WorkInfo`. All corresponding `getStatus` method variants have been renamed to the corresponding `getWorkInfo` variants. *This is a breaking change.*
- `ListenableWorker.onStopped()` no longer accepts has a boolean argument representing if the `WorkRequest` was cancelled. `WorkManager` no longer makes this distinction. *This is a breaking change.*
- `androidx.work.test` package has been renamed to `androidx.work.testing` package. *This is a breaking change.*
- Setters on `Constraints` are no longer a part of the public API. *This is a breaking change.*
- `WorkerParameters.getTriggeredContentUris()` and `WorkerParameters.getTriggeredContentAuthorities()` previously returned arrays. Now these methods return Collections. *This is a breaking change.*
- `ListenableWorker.onStartWork()` is renamed to `ListenableWorker.startWork()`. *This is a breaking change.*
- The constructor for `WorkStatus` is no longer a part of the public API. *This is a breaking change.*
- `Configuration.getMaxJobSchedulerID()` and `Configuration.getMinJobSchedulerID()` are renamed to `Configuration.getMinJobSchedulerId()` and `Configuration.getMaxJobSchedulerId()` respectively. *This is a breaking change.*
- Added a lot of `@NonNull` annotations to the public API to improve ergonomics of the API.
- Add `WorkManager.enqueueUniqueWork()` API to enqueue unique `OneTimeWorkRequest`s without having to create a `WorkContinuation`.
- All variants of `enqueue` and `cancel` methods on `WorkManager` now return a new `Operation` type. *This is a breaking change.*
- All variants of `enqueue` no longer accept varargs for `WorkRequest`s. *This is a breaking change.* Use Collections instead. You can use `Arrays.asList()` to modify existing code. We did this to reduce the API surface and method count.
- Attempting to `initialize` `WorkManager` more than once per process will now result in an `IllegalStateException`. *This is a breaking change.*

**Bug Fixes**

- `WorkRequest.Builder`s in the `work-runtime-ktx` artifact now use `ListenableWorker`s. Fixes [b/117666259](https://issuetracker.google.com/issues/117666259)
- Ensure the next run time for `PeriodicWork` is in the future. Fixes [b/118204399](https://issuetracker.google.com/issues/118204399)
- Remove potential disk I/O when using WorkManager on app startup. Fixes [b/117796731](https://issuetracker.google.com/issues/117796731)
- Fix a race condition in `WorkConstraintsTracker`. Fixes [android-workmanager/issues/56](https://github.com/googlecodelabs/android-workmanager/issues/56)

**Breaking API Changes**

- `WorkStatus` has been renamed to `WorkInfo`. All corresponding `getStatus` method variants have been renamed to the corresponding `getWorkInfo` variants.
- `ListenableWorker.onStopped()` no longer accepts has a boolean argument representing if the `WorkRequest` was cancelled. `WorkManager` no longer makes this distinction.
- `androidx.work.test` package has been renamed to `androidx.work.testing` package.
- Setters on `Constraints` are no longer a part of the public API.
- `WorkerParameters.getTriggeredContentUris()` and `WorkerParameters.getTriggeredContentAuthorities()` previously returned arrays. Now these methods return Collections.
- `ListenableWorker.onStartWork()` is renamed to `ListenableWorker.startWork()`.
- The constructor for `WorkStatus` is no longer a part of the public API.
- `Configuration.getMaxJobSchedulerID()` and `Configuration.getMinJobSchedulerID()` are renamed to `Configuration.getMinJobSchedulerId()` and `Configuration.getMaxJobSchedulerId()` respectively.
- All variants of`enqueue` and `cancel` methods on `WorkManager` now return a new `Operation` type.
- All variants of `enqueue` no longer accept varargs for `WorkRequest`s.
- Attempting to `initialize` `WorkManager` more than once per process will now result in an `IllegalStateException`.

### Version 1.0.0-alpha10

October 11, 2018

This release supports developer-controlled asynchronous work. There are breaking API changes in this release; please see the *Breaking API Changes* section below.

We anticipate that WorkManager is entering the final phases of its alpha period. We expect to be API stable in beta, so please take some time to file your feedback on our issue tracker.

**API Changes**

- Removed all previously `deprecated` methods and classes, notably the default `Worker` constructor. *This is a breaking API change.*
- Renamed `NonBlockingWorker` to `ListenableWorker`, which is now an unhidden public class and ready for usage.
  - `ListenableWorker` provides access to one abstract method, `ListenableFuture<Payload> onStartWork()` which is called on the main thread. It is up to you to start and process work asynchronously. When finished, you should update the `ListenableFuture` appropriately. Reference implementations of `ListenableFuture`s are provided in the `Futures` package in `alpha02` (see below the `WorkManager` section).
  - `Worker` extends `ListenableWorker` and still operates as before, with an abstract `Result doWork()` method.
  - Shuffled some methods and members from `Worker` to `ListenableWorker`.
  - We shall soon provide reference implementations for `ListenableWorker`s that use Kotlin coroutines (once the stable versions are released) and RxJava2.
- The interface `WorkerFactory` and the concrete implementation `DefaultWorkerFactory` have been merged into an abstract class called `WorkerFactory`. The implementation ensures that the default reflection-based behavior is called as a last-ditch effort for any user-created `WorkerFactory` instances. *This is a breaking change.*
- Removed `WorkManager.synchronous()` and `WorkContinuation.synchronous()` and all related methods. Added `ListenableFuture<Void>` as the return type of many methods in the API. *This is a breaking API change.*
  - You can now synchronously get and observe by using `ListenableFuture`s. For example, `WorkManager.enqueue()` used to return `void`; it now returns a `ListenableFuture<Void>`. You can call `ListenableFuture.addListener(Runnable, Executor)` or `ListenableFuture.get()` to run code once the operation is complete.
  - Note that these `ListenableFuture`s do not tell you if the operation succeeded or failed; only that they finished. You will still need to chain WorkManager methods to find out this information.
  - We ignore `cancel()` calls on these objects, as they are confusing and hard to reason about (are you cancelling the operation or the resulting work?). This is within the `Future`s contract.
  - To maintain parity with the synchronous `getStatus*` methods, we have provided `ListenableFuture` variants, and renamed the existing ones that returned `LiveData` to explicitly have "LiveData" as part of the name (for example, `getStatusesByIdLiveData(UUID)`). *This is a breaking API change.*

**Bug Fixes**

- Fixed the known issue from alpha09 regarding duplicate `androidx-annotations.pro` files. You may remove the workaround from the previous release notes by deleting `exclude 'META-INF/proguard/androidx-annotations.pro'` from your gradle file.
- Added proguard configurations to keep new `Worker` constructor. [b/116296569](https://issuetracker.google.com/116296569)
- Fix potential `NullPointerException` in a race condition where work was `REPLACE`d. [b/116253486](https://issuetracker.google.com/116253486) and [b/116677275](https://issuetracker.google.com/116677275)
- `WorkContinuation.combine()` now accepts one or more `WorkContinuation`s instead of two or more. [b/117266752](https://issuetracker.google.com/117266752)

**Breaking API Changes**

- Removed all previously `deprecated` methods and classes, notably the default `Worker` constructor.
- The interface `WorkerFactory` and the concrete implementation `DefaultWorkerFactory` have been merged into an abstract class called `WorkerFactory`.
- Removed `WorkManager.synchronous()` and `WorkContinuation.synchronous()`.
- `WorkManager.getStatus*()` methods now return `ListenableFuture`s. `WorkManager.getStatus*LiveData()` return `LiveData`s.

### Version 1.0.0-alpha09

September 19, 2018

**Known Issue**

If you run into the following issue: "More than one file was found with OS independent path 'META-INF/proguard/androidx-annotations.pro'", please put the following in your gradle file as a temporary workaround while we fix the issue in alpha10:  

### Groovy

```groovy
android {
    packagingOptions {
        exclude 'META-INF/proguard/androidx-annotations.pro'
    }
}
```

### Kotlin

```kotlin
android {
    packagingOptions {
        exclude("META-INF/proguard/androidx-annotations.pro")
    }
}
```

**Bug Fixes**

- Added another fix that was needed for the "100 jobs" error. [b/115560696](https://issuetracker.google.com/115560696)
- Added some fixes for foreign key constraint errors due to race conditions. [b/114705286](https://issuetracker.google.com/114705286)
- Delegated `ConstraintTrackingWorker.onStopped(boolean)` calls to the underlying `Worker`. [b/114125093](https://issuetracker.google.com/114125093)
- Enforce correct minimum backoff delay for Firebase JobDispatcher. [b/113304626](https://issuetracker.google.com/113304626)
- Improved threading guarantees internal to the library.
- Correct potential issue with deduping of `LiveData` internally.

**API Changes**

- You can now create your own `Worker` instances at runtime by specifying a `WorkerFactory` as part of the `WorkManager.Configuration`. The fallback factory is `DefaultWorkerFactory`, which matches behavior of previous versions of WorkManager.
  - The default constructors for `Worker` and `NonBlockingWorker` are now marked as deprecated. Please use the new constructor (`Worker(Context, WorkerParameters)`) and call `super(Context, WorkerParameters)`; future versions of WorkManager will remove the default constructor.
- We have started using the new `ListenableFuture` artifact internally (free of Guava dependencies). We will introduce ListenableFutures to the API in upcoming releases. This change will support the eventual unhiding of `NonBlockingWorker`.
- Add ability to trigger timed work in `TestDriver` via `TestDriver.setInitialDelayMet(UUID)` and `TestDriver.setPeriodDelayMet(UUID)`. [b/113360060](https://issuetracker.google.com/113360060)

**Breaking Changes**

- The default `Worker` and `NonBlockingWorker` constructors are deprecated. Please migrate to the new constructor ASAP. Future versions will remove the default constructor.

### Version 1.0.0-alpha08

August 27, 2018

**Bug Fixes**

- Explicitly labelled WorkManager components as direct boot unaware so they don't fire up during direct boot. In the future, we will provide a version of WorkManager that is direct boot-aware. [b/112665532](https://issuetracker.google.com/112665532)
- Fixed an issue where retried work was not running. [b/112604021](https://issuetracker.google.com/112604021)
- Fixed periodic work not executing repeatedly (related to the above issue). [b/112859683](https://issuetracker.google.com/112859683)
- Honored backoff policies when the app process is already running.
- Corrected exception messages in `Data` to indicate the limit is 10KB.
- Lowered maximum value of `Configuration.setMaxSchedulerLimit(int)` to 50 to account for some latency in `JobScheduler` processing completion. [b/112817355](https://issuetracker.google.com/112817355)

### Version 1.0.0-alpha07

August 16, 2018

**Bug Fixes**

- Fixed a potential SQL query with negative limits that could return an unbounded number of results.
- Work that has finished execution now correctly cancels all pending copies of that work in other Schedulers. This led to exceeding the `JobScheduler` jobs limit. [b/111569265](https://issuetracker.google.com/111569265)
- Fixed a `ConcurrentModificationException` in `ConstraintTracker`. [b/112272753](https://issuetracker.google.com/112272753)
- Changed return type annotations of `Data.getBooleanArray(String)` and `Data.getIntArray(String)` to `@Nullable` instead of `@NonNull`. [b/112275229](https://issuetracker.google.com/112275229)

**API Changes**

- `Worker` now extends a new class, `NonBlockingWorker`. This does not affect any current usage. In the future, `NonBlockingWorker` will become a fully supported entity for custom threading solutions.
- Changed return type annotations of `Data.getBooleanArray(String)` and `Data.getIntArray(String)` to `@Nullable` instead of `@NonNull`. [b/112275229](https://issuetracker.google.com/112275229)
- Kotlin extensions: deprecated `Map.toWorkData()` and added a top-level `workDataOf(vararg Pair<String, Any?>)` to be more consistent with existing APIs.

### Version 1.0.0-alpha06

August 1, 2018

**Bug Fixes**

- Prevent a database lock when scheduling work. [b/111801342](https://issuetracker.google.com/issues/111801342)
- Fix a bug which causes `PeriodicWork` to not run on schedule when in Doze mode. [b/111469837](https://issuetracker.google.com/issues/111469837)
- Fix a race condition when tracking constraints which causes `WorkManager` to crash. [googlecodelabs/android-workmanager/issues/56](https://github.com/googlecodelabs/android-workmanager/issues/56)
- Create unique `WorkRequest`s when using `WorkRequest.Builder#build()`. [b/111408337](https://issuetracker.google.com/issues/111408337)
- Enable the use of `RescheduleReceiver` only when there are `WorkRequest`s that need it. [b/111765853](https://issuetracker.google.com/issues/111765853)

### Version 1.0.0-alpha05

July 24, 2018

**API Changes**

- `WorkManager.getInstance()` is now annotated with `@NonNull` instead of `@Nullable`. Instead, if the singleton isn't properly initialized in cases of manual initialization, the method will throw an `IllegalStateException`. **This is a
  breaking API change.**
- Added a new API, `Configuration.Builder.setMinimumLoggingLevel(int)`, which can control WorkManager verbosity. By default, WorkManager logs `Log.INFO` and above.
- Changed signature of `Data.getString()` so it no longer takes a default value (it is implicitly `null`). **This is a breaking API change.**
- Marked some methods needed only for internal usage as `@hide`. This includes the `Constraints` constructor, `Data.toByteArray()`, and `Data.fromByteArray(byte[])`. **This is a breaking API change.**

**Bug Fixes**

- WorkManager no longer executes work during known cases of auto-backup. This could have resulted in a crash. [b/110564377](https://issuetracker.google.com/issues/110564377)
- Fixed double-scheduling of `PeriodicWorkRequest`s when using `JobScheduler`. [b/110798652](https://issuetracker.google.com/issues/110798652)
- Fixed an issue with `PeriodicWorkRequest`s not executing correctly after device doze. [b/111469837](https://issuetracker.google.com/issues/111469837)
- Fixed an issue with initial delays when using Firebase JobDispatcher. [b/111141023](https://issuetracker.google.com/issues/111141023)
- Fixed some potential race conditions and timing issues.
- Correctly freed up `BroadcastReceiver`s that were no longer needed.
- Optimized rescheduling performance when apps restart after being force closed.
- Allowed `TestScheduler.setAllConstraintsMet(UUID)` to be called before or after enqueuing the given `WorkRequest`. [b/111238024](https://issuetracker.google.com/issues/111238024)

**Breaking Changes**

- `WorkManager.getInstance()` is now annotated with `@NonNull` instead of `@Nullable`.
- Changed signature of `Data.getString()` so it no longer takes a default value (it is implicitly `null`).
- Marked some methods needed only for internal usage as `@hide`. This includes the `Constraints` constructor, `Data.toByteArray()`, and `Data.fromByteArray(byte[])`.

### Version 1.0.0-alpha04

June 26, 2018

**Bug Fixes**

- `PeriodicWorkRequest`s are now correctly rescheduled when using the `AlarmManager` based implementation.
- Fixed a potential ANR when rescheduling all workers after a force stop or a reboot. [b/110507716](https://issuetracker.google.com/issues/110507716)
- Added nullability annotations to various WorkManager APIs. [b/110344065](https://issuetracker.google.com/issues/110344065)
- Log uncaught exceptions that occur during Worker execution. [b/109900862](https://issuetracker.google.com/issues/109900862)
- Allowed destructive database migrations in case you decide to roll back to an older version of WorkManager. [b/74633270](https://issuetracker.google.com/issues/74633270)
- Fixed a migration crash if creating duplicate implicit tags. This is a very rare issue that occurred only if you used the same implicit tag format yourself.

### Version 1.0.0-alpha03

June 19, 2018

**Bug Fixes**

- Fixed a race condition in the `AlarmManager` based implementation. [b/80346526](https://issuetracker.google.com/issues/80346526).

- Fixed duplicate jobs when using `JobScheduler` after a device reboot.

- Jobs with Content URI triggers now persist across reboots. [b/80234744](https://issuetracker.google.com/issues/80234744)

- Documentation updates. [b/109827628](https://issuetracker.google.com/issues/109827628), [b/109758949](https://issuetracker.google.com/issues/109758949), [b/80230748](https://issuetracker.google.com/issues/80230748)

- Fixed a crash when re-enqueuing a `WorkRequest`. [b/109572353](https://issuetracker.google.com/issues/109572353).

- Fixed Kotlin compiler warnings when using the `work-runtime-ktx` dependency.

- WorkManager now uses `Room` version `1.1.1-rc1`.

**API Changes**

- Added `getStatusesSync()`, the synchronous version of `WorkContinuation.getStatuses()`.
- `Worker` has the ability to distinguish between user-initiated cancellation and temporary os-requested stopping. `Worker.isStopped()` returns `true` if any kind of stop has been requested. `Worker.isCancelled()` returns `true` when the work has been explicitly cancelled. [b/79632247](https://issuetracker.google.com/issues/79632247)
- Add support for [JobParameters#getNetwork()](https://developer.android.com/reference/android/app/job/JobParameters.html#getNetwork()) on API 28. This is exposed via `Worker.getNetwork()`.
- Added `Configuration.Builder.setMaxSchedulerLimit(int maxSchedulerLimit)` so you can enforce how many jobs can be sent to `JobScheduler` or `AlarmManager`. This helps prevent `WorkManager` from taking all your available `JobScheduler` slots.
- Added `Configuration.setJobSchedulerJobIdRange(int minJobSchedulerId, int maxJobSchedulerId)` which helps define a range of `JobScheduler` job ids safe for `WorkManager` to use. [b/79996760](https://issuetracker.google.com/issues/79996760)
- `Worker.getRunAttemptCount()` returns the current run count for a given `Worker`. [b/79716516](https://issuetracker.google.com/issues/79716516)
- `WorkManager.enqueueUniquePeriodicWork(String uniqueWorkName, ExistingPeriodicWorkPolicy existingPeriodicWorkPolicy, PeriodicWorkRequest periodicWork)` allows you to enqueue a unique `PeriodicWorkRequest`s. [b/79600647](https://issuetracker.google.com/issues/79600647)
- `WorkManager.cancelAllWork()` cancels all `Worker`s. Libraries that depend on `WorkManager` can query when this method was called last by using `WorkManager.getLastCancelAllTimeMillis()` for additional cleanup of internal state.
- Added `WorkManager.pruneWork()` to remove completed jobs from the internal database. [b/79950952](https://issuetracker.google.com/issues/79950952), [b/109710758](https://issuetracker.google.com/issues/109710758)

**Behavior Changes**

- Added an implicit tag for all `WorkRequest`s, which is the fully qualified class name for the `Worker`. This allows the ability to remove `WorkRequest`s without `tag`s or when the `id` is not available. [b/109572351](https://issuetracker.google.com/issues/109572351)

**Breaking Changes**

- Renamed `Worker.WorkerResult` to `Worker.Result`.
- `Worker.onStopped` now has an **additional** `isCancelled` parameter which is set to`true` when the `Worker` has explicitly been cancelled.

### Version 1.0.0-alpha02

May 24, 2018

**Bug Fixes**

- Fixed a `NullPointerException` on `State.isFinished()`. [b/79550068](https://issuetracker.google.com/issues/79550068)
- Fixed an issue which caused `Worker`s to be rescheduled on `Application.onCreate()`. [b/79660657](https://issuetracker.google.com/issues/79660657)
- Fixed an issue where you could schedule more work than is allowed by the OS. [b/79497378](https://issuetracker.google.com/issues/79497378)
- Moved cleanup of wake locks associated with `Worker`s to the background thread.
- The `AlarmManager` implementation now correctly cleans up when all pending work is complete.
- Fixed cleanup SQL queries which affected non-English locales. [b/80065360](https://issuetracker.google.com/issues/80065360)
- Added support for `float`s in `Data`. [b/79443878](https://issuetracker.google.com/issues/79443878)
- `Data.Builder.putAll()` now returns an instance of the `Builder`. [b/79699162](https://issuetracker.google.com/issues/79699162)
- More javadoc and fixes in documentation. [b/79691663](https://issuetracker.google.com/issues/79691663)

**API Changes**

- `Worker`s can react to being stopped. `Worker.isStopped()` can be used to check if a `Worker` has been stopped. `Worker.onStopped()` can be used to perform lightweight cleanup operations.
- `Worker.getTags()` API returns a `Set` of tags associated with the `Worker`.
- Added `javax.time.Duration` overloads for APIs which take a combination of duration and `TimeUnit`s. This is guarded by `@RequiresApi(26)`.
- `WorkManager` extensions have moved from the `androidx.work.ktx` package to the `androidx.work` package. The old extensions are deprecated and will be removed in a future version.
- `Configuration.withExecutor()` is deprecated. Use `Configuration.setExecutor()` instead.

### Version 1.0.0-alpha01

May 8, 2018

[WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) simplifies scheduling and execution of
guaranteed, constraint-aware background work. This initial release is `1.0.0-alpha01`.