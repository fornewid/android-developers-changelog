---
title: https://developer.android.com/jetpack/androidx/releases/health
url: https://developer.android.com/jetpack/androidx/releases/health
source: md.txt
---

# Health

API Reference  
[androidx.health.services.client](https://developer.android.com/reference/kotlin/androidx/health/services/client/package-summary)  
Create performant health applications in a platform agnostic way.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.0.0](https://developer.android.com/jetpack/androidx/releases/health#1.0.0) | - | [1.1.0-beta01](https://developer.android.com/jetpack/androidx/releases/health#1.1.0-beta01) | - |

## Declaring dependencies

To add a dependency on Health, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.health:health-services-client:1.1.0-beta01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.health:health-services-client:1.1.0-beta01")
}
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:1056301+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=1056301&template=1581114)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Health Connect Client Version 1.0

### Version 1.0.0-alpha04

August 24, 2022

As of 1.0.0-alpha04, `androidx.health:health-connect-client` was migrated to
`androidx.health.connect:connect-client`. For future, releases please use
`androidx.health.connect:connect-client` and the associated release notes on our
[Health Connect](https://developer.android.com/jetpack/androidx/releases/health-connect) page.

To migrate, simply change your dependency import from
`androidx.health:health-connect-client:1.0.0-alpha03` to
`androidx.health.connect:connect-client:1.0.0-alpha04`.

### Version 1.0.0-alpha03

July 27, 2022

`androidx.health:health-connect-client:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/health/health-connect-client)

**New Features**

- Summary of new API changes: a set of units have been added to the read, write, aggregate APIs. Apps can now retrieve or write records with their unit of choice, such as grams or milligrams for `NutritionRecord` nutrients.

**API Changes**

- Fix `List<DataOrigin>` to be `Set<DataOrigin>` across various request response objects. ([I42342](https://android-review.googlesource.com/#/q/I4234240b3986e042df1140bf02171cab25312542))
- Fix unit of basal total calories from Power-\>Energy. ([I0b429](https://android-review.googlesource.com/#/q/I0b429388ac68305a95396f89c754a2206dc3264c))
- Moved series sample classes inside series records ([Ica9bb](https://android-review.googlesource.com/#/q/Ica9bb4656889d300d6d71ff811a283dfd195bf67)):
  - `CyclingPedalingCadence` -\> `CyclingPedalingCadenceRecord.Sample`
  - `HeartRate` -\> `HeartRateRecord.Sample`
  - `StepsCadence` -\> `StepsCadenceRecord.Sample`
- Deprecate `HealthDataRequestPermission` class, in favor of `PermissionController.createRequestPermissionActivityContract`; This promotes better discoverability and unified parameterization. ([I81e7f](https://android-review.googlesource.com/#/q/I81e7f5cf104f6fdd35cc943b0a975027049e69af))
- Added US fluid ounces to Volume. ([I5f03d](https://android-review.googlesource.com/#/q/I5f03d96f1f328232c0672952adcfc56206ff28ea))
- Added Speed unit type ([I1d574](https://android-review.googlesource.com/#/q/I1d574f1585da182bc8ec648adecebc313fdf470a))
- Added Percentage unit type ([I08f23](https://android-review.googlesource.com/#/q/I08f23783bafb653ec4476e3c88fdd93435213538))
- Added Pressure unit type ([Ifb01f](https://android-review.googlesource.com/#/q/Ifb01f75c5455ebecdbd5816005592a7c55a180cd))
- Added Mass unit type ([Ifd81a](https://android-review.googlesource.com/#/q/Ifd81ae024e2eae061b1046c556823d57c2bb80ec))
- Added Volume unit type ([I59ad1](https://android-review.googlesource.com/#/q/I59ad1e9394b76b8405fad4163e9871c47a852499))
- Added Power unit type. Moved Power series sample class inside `PowerRecord` class. ([I5b1e5](https://android-review.googlesource.com/#/q/I5b1e51373afa05aad5d21bac5cf8e48a16ce3805))
- Added Energy unit type ([I983ae](https://android-review.googlesource.com/#/q/I983ae2f3f282aee332697c012a1fcf20b9c91419))
- Added Temperature unit type ([I4cdb5](https://android-review.googlesource.com/#/q/I4cdb50de23e0374bf2bffe455ec61dcf9e7fffdb))
- Rename references of Activity to be specific to Exercise, including ([I3f936](https://android-review.googlesource.com/#/q/I3f93615765a41d3aacac2eafb8d3b2930c8af414)):
  - Renamed `ActivityLap` -\> `ExerciseLapRecord`
  - Renamed `ActivityEvent` -\> `ExerciseEventRecord`
  - Renamed `Repetitions` -\> `ExerciseRepetitionsRecord`
  - Renamed `ActivitySession` -\> `ExerciseSessionRecord`
- Moved package metadata nested under records. ([Ie0835](https://android-review.googlesource.com/#/q/Ie08355e7debbdf391aa689e6cad239b5cdab72e9))
- Used Length unit in all remaining records ([Ib10dd](https://android-review.googlesource.com/#/q/Ib10dd02e742b188bfed63d8f2be99f3c1df02887)):
  - `ActivityLapRecord`
  - `ElevationGainedRecord`
  - `HeightRecord`
  - `HipCircumferenceRecord`
  - `WaistCircumferenceRecord`
- Added Length unit type ([Idae39](https://android-review.googlesource.com/#/q/Idae39b675aa6ee8816f281755bceb048e1a3a6f4))
- Update `CervicalMucus` description terminology ([I25a2b](https://android-review.googlesource.com/#/q/I25a2b19e13184f111666113923638396f56f2cff)):
  - `CervicalMucus.Amount` -\> `CervicalMucusRecord.Texture`
  - `CervicalMucus.Appearance` -\> `CervicalMucusRecord.Sensation`
- Added 'Record' suffix to all record class names ([I1ffc2](https://android-review.googlesource.com/#/q/I1ffc272c9d271bb71a3f7ae3fad3b63c28492939))

**Bug Fixes**

- Fix proguard issues when lib built with release flavor and `minifyEnabled` true. ([I78933](https://android-review.googlesource.com/#/q/I78933cdcf910688d2acd825fccbbb0ada643b959))
- Hides documentation not intended for public usage. ([I7a08f](https://android-review.googlesource.com/#/q/I7a08f4e0ff3bd685e123427cee23787507ee0680))
- Fixes the issue in clients who may have their own protobuf dependencies.(https://android-review.googlesource.com/c/platform/frameworks/support/+/2105430)

### Version 1.0.0-alpha02

June 1, 2022

`androidx.health:health-connect-client:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b18424ac8b7d47a65751381a4f8ad4777f537107..7cbb37cc779160b89644d03e042c129d0ce025d2/health/health-connect-client)

**API Changes**

- Deprecated `hasMetric` and `getMetric` in `AggregationResult`, added contains and get operators ([I7cc7c](https://android-review.googlesource.com/#/q/I7cc7c118e6fab03b7eaa9e551072ca3a59e5027c))
- Adds `OvulationTest.Result.HIGH` and `OvulationTest.Result.INCONCLUSIVE`. ([I9f9c4](https://android-review.googlesource.com/#/q/I9f9c41787ae40aa245821e4c48b339296df4a781))

**Bug Fixes**

- Reduce SDK requirements to 26. ([I6d201](https://android-review.googlesource.com/#/q/I6d20121096fdaa0a5e72436c4e1888678dc61eae))

### Version 1.0.0-alpha01

May 11, 2022

`androidx.health:health-connect-client:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b18424ac8b7d47a65751381a4f8ad4777f537107/health/health-connect-client)

**New Features**

- API for reading fitness and health records shared by other apps.
- API for writing fitness and health records to share with other apps.
- API to retrieve aggregated metrics for accessible records.
- API to retrieve incremental changes (insert, update or delete) of records by other apps.
- API to prompt users for health permissions.
- API to check for permissions or revoke granted health permissions.

## Health Services Client Version 1.1

### Version 1.1.0-beta01

February 11, 2026

`androidx.health:health-services-client:1.1.0-beta01`, `androidx.health:health-services-client-external-protobuf:1.1.0-beta01`, and `androidx.health:health-services-client-proto:1.1.0-beta01` are released. Version 1.1.0-beta01 contains [no changes](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..2e98d140740558dc55710bde96311d2e0e8d5cfd/health/health-services-client) since the prior alpha release.

### Version 1.1.0-alpha05

December 11, 2024

`androidx.health:health-services-client:1.1.0-alpha05`, `androidx.health:health-services-client-external-protobuf:1.1.0-alpha05`, and `androidx.health:health-services-client-proto:1.1.0-alpha05` are released. Version 1.1.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..46295bc0b75a16f452e8e0090e8de41073d4dbb6/health).

**New Features**

- Now includes proguard rules to avoid necessary classes from being stripped out. ([65d0c3f](https://android-review.googlesource.com/#/q/I415de3ff36ad212bc3b1e0d6eb6a74eccb5259fd))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Iaf73a](https://android-review.googlesource.com/#/q/Iaf73a787b8b07034e55d1ec8e3495728849dc127), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.1.0-alpha04

October 16, 2024

`androidx.health:health-services-client:1.1.0-alpha04`, `androidx.health:health-services-client-external-protobuf:1.1.0-alpha04`, and `androidx.health:health-services-client-proto:1.1.0-alpha04` are released. Version 1.1.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7/health).

**Security Fixes**

- As of [this change](https://android-review.googlesource.com/q/topic:%22protobuf-4.28.2%22), androidx compiles against protobuf 4.28.2 in order to address [CVE-2024-7254](https://nvd.nist.gov/vuln/detail/CVE-2024-7254). Upgrade your dependency on `androidx.health:health-services-client` to the latest 1.1.0-alpha04 to address the vulnerability risk.

### Version 1.1.0-alpha02

December 13, 2023

`androidx.health:health-services-client:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..9174577f8a57ba4ae4958cc31787ea4db3b2b44a/health/health-services-client)

**API Changes**

- Use a single source of truth for supported `ExerciseEvent`s. ([I03308](https://android-review.googlesource.com/#/q/I03308abac06b2870a4e176842e2ea4528f7c2743))

**Bug Fixes**

- Minor bug fixes and documentation improvements.

### Version 1.1.0-alpha01

August 9, 2023

`androidx.health:health-services-client:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf2530aff824f92789d2b6d9964024b0256287d1..5d7dd999525725bd038a00ca4e89e0fef624a6da/health/health-services-client)

**New Features**

- `ExerciseEvent` APIs have been added alongside the first concrete event: `GolfShotEvent`. The `ExerciseEvent` primitives enable developers to query support for and request to be notified when the watch detects something has occurred. `GolfShotEvent` as an example enables developers to be notified when the user takes a golf shot in addition to receiving the swing type recognized.

**API Changes**

- Enable WHS SDK clients to use `GolfShotEvent` functionalities. ([I76b03](https://android-review.googlesource.com/#/q/I76b0315811181e53eff189f0beaf76de06febf9d))

**Bug Fixes**

- Instead of aggressively throwing exceptions on seeing unknown exercise event capabilities, filter it out from the list. ([I06afc](https://android-review.googlesource.com/#/q/I06afc9ee967ea39453118ff9695d645a707c2659))

## Health Services Client Version 1.0

### Version 1.0.0

May 7, 2025

`androidx.health:health-services-client:1.0.0` is released. Version 1.0.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c6e90dd69e820ce8e2891808c319258854224a87..406d818337299d527568b8dcc6bbce396a84c769/health/health-services-client).

**Major features of 1.0.0**

- This is the promotion of 1.0.0-rc02 to be the stable release of Health Services Client. There are no changes from 1.0.0-rc02.

### Version 1.1.0-alpha03

May 14, 2024

`androidx.health:health-services-client:1.1.0-alpha03` is released. Version 1.1.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9174577f8a57ba4ae4958cc31787ea4db3b2b44a..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/health/health-services-client).

**New Features**

- Introduced `DebouncedGoal` APIs that allows tracking a goal for sample data type or stats sample data type during exercise with debouncing features(`initialDelay` and `durationAtThreshold`). ([I09be9](https://android-review.googlesource.com/#/q/I09be92bf1842d32012fc665a55d4b994a9614310))
- Added the following advanced running metrics sample and statistical `DataTypes`. ([I0b8b5](https://android-review.googlesource.com/#/q/I0b8b570d14c6b79113c51a12ead57da94f531f7e)):
  - `Ground Contact Time`
  - `Vertical Oscillation`
  - `Vertical Ratio`
  - `Stride Length`

**API Changes**

- Added `ELEVATION_GAIN_DAILY` `DataType`. ([I059d1](https://android-review.googlesource.com/#/q/I059d143ee24a0629454f79cdd80e3c6fe545d71b))
- Added `SWIM_LAP_COUNT_TOTAL` `DataType` as the aggregated `DataType` for `SWIM_LAP_COUNT`. ([I0beeb](https://android-review.googlesource.com/#/q/I0beebdee76d0cbe82f4378d45b310d3473d2f397))

**Bug Fixes**

- Fixed various issues to improve IPC reliability.

### Version 1.0.0-rc02

April 3, 2024

`androidx.health:health-services-client:1.0.0-rc02` is released. Version 1.0.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bf2530aff824f92789d2b6d9964024b0256287d1..c6e90dd69e820ce8e2891808c319258854224a87/health/health-services-client). This is a bug fix only release and does not contain API changes.

**Bug Fixes**

- Fixed various issues to improve IPC reliability
- Fixed an issue where calling `startExercise` at the same time as `prepareExercise` could lead to a `ConcurrentModificationException` ([4e37773](https://android.googlesource.com/platform/frameworks/support/+/4e377730de43743cf73c8c090bf61b5a24084976))
- Improved documentation

### Version 1.0.0-rc01

July 26, 2023

`androidx.health:health-services-client:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..bf2530aff824f92789d2b6d9964024b0256287d1/health/health-services-client)

**New Features**

- Health Services has moved to 1.0.0-rc01 after stabilizing in beta.

**API Changes**

- Merged public and experimental API files for h- thru m-paths. ([Ic4630](https://android-review.googlesource.com/#/q/Ic46302e01e1352d8b4d37cb2468ef61474e79df3), [b/278769092](https://issuetracker.google.com/issues/278769092))
- N/A, API file changes are just reordering methods. ([I5fa95](https://android-review.googlesource.com/#/q/I5fa95ca42073461bed8e5020c91b4c0894b70753))

### Version 1.0.0-beta03

April 5, 2023

`androidx.health:health-services-client:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..a200cb82769634cecdb118ec4f0bfdf0b086e597/health/health-services-client)

**New Features**

`BatchingMode` can now be configured to deliver batched exercise data at the configured interval instead of the default during an active exercise, either at exercise start via `ExerciseConfig` or during with an override method. Support for this will be enabled by an upcoming Health Services release in the Google Play Store and can be checked via exercise capabilities. *Note: batching modes take effect while the device is in a non-interactive power state, and will cause increased power consumption.*

**API Changes**

- Throwing `HealthServicesException` when suspend function `overrideBatchingModesForActiveExercise` fails ([Ifd387](https://android-review.googlesource.com/#/q/Ifd3872c1c354a06952630e11614c5a8e3bf918e3))
- Introduced suspend functions for async `overrideBatchingModesForActiveExercise` API making them more kotlin friendly ([I7dd15](https://android-review.googlesource.com/#/q/I7dd15d8a09ff48e43b680d6b7c51e436a2c5f63c))
- `BatchingMode` overrides optional in `ExerciseConfig` ([Id22e9](https://android-review.googlesource.com/#/q/Id22e9c25a70666ba0329189e6c328e075d5d26cd))

**Bug Fixes**

- `DataType` and `ExerciseUpdate` small fixes ([5e185f](https://android-review.googlesource.com/#/q/a88dc75ff88fdda9d5306287add55842f25e185f))

### Version 1.0.0-beta02

January 11, 2023

`androidx.health:health-services-client:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..adf1c279a86ab3886e1666c08e2c3efba783367b/health/health-services-client)

**New Features**

- Added `suspend` extension functions for the existing asynchronous `ListenableFuture` APIs in `ExerciseClient`, `PassiveMonitoringClient` and `MeasureClient` for better Kotlin support. ([Iadea4](https://android-review.googlesource.com/#/q/Iadea42d6c5a4a7ba510e6400f374c13574c2abfd))
- Added `ExerciseTypeConfig` API which enables updates during an ongoing exercise. Added `GolfExerciseTypeConfig` to support updating `ExerciseTypeConfig` during golf exercises. ([I4c539](https://android-review.googlesource.com/#/q/I4c539e1abde8e51e65dcc82e3495f202b10282ea))

**API Changes**

- Throw `HealthServicesException` on suspend functions ([I5e509](https://android-review.googlesource.com/#/q/I5e509122f25af84a81713eeb2f26e2e62c18978c))
- Add another constructor for backward compatibility ([Iddeda](https://android-review.googlesource.com/#/q/Iddeda8a23e653cf104d8dfacabc5ef8c5e8f83a8))
- Throw `RuntimeException` on suspend functions ([I53bca](https://android-review.googlesource.com/#/q/I53bca3e3ea21f16fd8fcd8e0e913edc700266902))
- Remove default implementation of throwing Exception ([Id947f](https://android-review.googlesource.com/#/q/Id947f2552f3c6e4e9abd981f09f6922db3f4fa7d))
- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

**Bug Fixes**

- Add to kdoc for clarity ([Ide285](https://android-review.googlesource.com/#/q/Ide2859c52cac07e6c4184ade52b578bdd5a08b73))
- Allow passive monitoring tracking for goals only if the same data types are also tracked ([Ibed8d](https://android-review.googlesource.com/#/q/Ibed8da24bafb1786c47e72c069e9cec6ac9ee564))

### Version 1.0.0-beta01

October 24, 2022

`androidx.health:health-services-client:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..548c8ac2570ae6cf15798fea1380491f7d93796b/health/health-services-client)

**New Features**

- Added the ability to listen for health events through `PassiveMonitoringClient` with the first event being: `HealthEvent.FALL_DETECTED`.

- New ExerciseTypes:

  - `ALPINE_SKIING`
  - `BACKPACKING`
  - `CROSS_COUNTRY_SKIING`
  - `HORSE_RIDING`
  - `INLINE_SKATING`
  - `MOUNTAIN_BIKING`
  - `ORIENTEERING`
  - `ROLLER_SKATING`
  - `YACHTING`
- New DataTypes:

  - `ELEVATION_LOSS`
  - `GOLF_SHOT_COUNT`

**API Changes**

- [Updated how data is modeled](https://android-review.googlesource.com/#/q/I287a816075bf721c9cec2471a5032366f70eee4f): the data model and how `DataType`s, `DataPoint`s, and their underlying values are represented have been overhauled. The top level impact is that APIs are now much more explicit and type safe.
- Location `DataPoint`s are no longer represented as a `DoubleArray`, but instead as a strongly-typed `LocationData` object.
- Moved to a new set of passive listener APIs:
  - The broadcast was replaced by the `PassiveListenerService`.
  - The existing listeners were replaced with a single listener: `PassiveListenerCallback`.
- Added `<queries>` tag to Health Services manifest so that applications no longer need to specify this in their own manifest (provided manifest merger is turned on in their build system.)
- Moved away from many `ExerciseState`s to represent the exercise is ending / ended and added new exercise states `ENDING` and `ENDED`. These are now combined with `ExerciseEndReason` to represent the full gamut of previous states.
- Renamed `PassiveListenerConfig` `setPassiveGoals` to `setDailyGoals` to better reflect we only support daily passive goals.
- `PassiveGoal`s now always `REPEATED`, passive `TriggerFrequency` removed.
- Annotated all `Long` and `Double` parameters with `@FloatRange`.
- Added `swimmingPoolLengthMeters` property to `ExerciseConfig` which may be optionally specified to improve distance calculations for pool swims.
- Deprecated `ExerciseUpdate.activeDuration`. Use `ExerciseUpdate.activeDurationCheckpoint` instead.
- Renamed the API `flushExerciseAsync()` to `flushAsync()` in `ExerciseClient`.
- `Measure.registerCallback` renamed to `Measure.registerMeasureCallback`.
- General naming changes:
  - Distance properties now have `meters` suffix.
  - Callback method names are now past tense.
  - Most abbreviations have been removed (`HrAccuracy` is now `HeartRateAccuracy`.)
  - Properties following the pattern `enableFoo` are now named `isFooEnabled`.
- Migrated away from Enums.
- Times represented by `Double` are now represented by `Duration`.
- Functions returning a `ListenableFuture<Void?>` now return a `ListenableFuture<Void>`.
- Functions that accept a callback now always have the callback appear as the last parameter.
- Classes with builders now always also have public constructors.
- Registration functions no longer return a `ListenableFuture` and instead pass registration status to the provided callback.
- KDocs have now been improved.
- Public classes no longer extend `ProtoParcelable`.

**Bug Fixes**

- General improvements to IPC reliability ([I3b1e2](https://android-review.googlesource.com/#/q/I3b1e2a66a652a0882d06d4353cbf015a6a637004))

### Version 1.0.0-alpha03

November 3, 2021

`androidx.health:health-services-client:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..f07d12061370a603549747200c79b60239706330/health/health-services-client)

**New Features**

- The SDK will automatically re-register measure, exercise listener, and passive monitoring callback registration requests in the event that the IPC connection is broken with the Health Services APK.

**API Changes**

- minSdkVersion of the SDK library bumped to API level 30 since the Health Services Client is currently only supported on Wear3.

### Version 1.0.0-alpha02

September 29, 2021

`androidx.health:health-services-client:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b26835518d143ca5c7cc6f70c596aba6e527456..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/health/health-services-client)

**API Changes**

- `ExerciseClient` now supports preparing an exercise. This allows clients to warm-up the sensors and wait for things like a GPS Fix before starting exercise.
- Introduces CumulativeDataPoints and StatisticalDataPoints AggregateDataPoint classes to better model aggregate metrics tracked during an active exercise. CumulativeDataPoints hold cumulative values of aggregated interval data types (such as total distance during the exercise) while StatisticalDataPoints model aggregates of sampled data points (such as min, max, and average HeartRateBpm). This replaces the previous `AGGREGATE_*` DataTypes and can be accessed in the ExerciseUpdate via `getLatestAggregateMetrics()`. `AGGREGATE_*` DataTypes are no longer supported.
- `PassiveMonitoring` Events have been renamed to `PassiveGoals` which supports setting of goals and receiving notifications when those goals are met for data types like Daily metrics (i.e. DAILY_STEPS).
- Improved modeling of Heart Rate and Location accuracy and availability via the introduction of the new HrAccuracy, LocationAccuracy, and LocationAvailability classes.
- Improved naming of `ExerciseConfig` and new `PassiveMonitoringConfig` fields and introduction of `ExerciseConfig.shouldEnableGps` to request GPS-backed data

**Bug Fixes**

- Migrates to proto-backed IPC transport for better backwards compatibility support

### Version 1.0.0-alpha01

May 18, 2021

`androidx.health:health-services-client:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b26835518d143ca5c7cc6f70c596aba6e527456/health/health-services-client)

**Features of initial release**

The Health Services library provides a uniform set of APIs for developers to integrate with device-specific sensor implementations. It will work out of the box with Wear OS 3 emulators and upcoming devices, with additional platforms supported in the future. Three top level API surfaces are included in this initial release: The `ExerciseClient`, `PassiveMonitoringClient`, and `MeasureClient`.

**ExerciseClient**

The `ExerciseClient` is made for applications tracking active workouts, with up to 82 different `ExerciseType`s from walking and running to dancing and water polo. While tracking these exercises, there's a selection of 50 different `DataType`s available depending on the exercise type and hardware available on the device. To get started, just specify the relevant information in your `ExerciseConfig`, call `exerciseClient.startExercise` and listen for progress on the update listener.

**PassiveMonitoringClient**

The `PassiveMonitoringClient` is a great choice if your application tracks the user's activity throughout the day. You can register a `PendingIntent` with a set of `DataType`s and be woken up to handle batched changes. Alternatively, you can specify an `Event` such as reaching a certain number of steps.

**MeasureClient**

Sometimes the user needs to measure e.g. their heart rate in the moment, not during an exercise and not throughout the day. In those moments the `MeasureClient` is the perfect choice.You just register your callback with supported `DataType`s to receive a stream of data, unregistering your callback when it's no longer needed.