---
title: https://developer.android.com/jetpack/androidx/releases/compose-runtime
url: https://developer.android.com/jetpack/androidx/releases/compose-runtime
source: md.txt
---

# Compose Runtime

[User Guide](https://developer.android.com/jetpack/compose/tutorial) [Code Sample](https://github.com/android/compose-samples) API Reference  
[androidx.compose.runtime](https://developer.android.com/reference/kotlin/androidx/compose/runtime/package-summary)  
[androidx.compose.runtime.rxjava2](https://developer.android.com/reference/kotlin/androidx/compose/runtime/rxjava2/package-summary)  
[androidx.compose.runtime.rxjava3](https://developer.android.com/reference/kotlin/androidx/compose/runtime/rxjava3/package-summary)  
[androidx.compose.runtime.saveable](https://developer.android.com/reference/kotlin/androidx/compose/runtime/saveable/package-summary)  
[androidx.compose.runtime.snapshots](https://developer.android.com/reference/kotlin/androidx/compose/runtime/snapshots/package-summary)  
(*See the API reference docs for all compose packages*) Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.10.3](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.10.3) | - | - | [1.11.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.11.0-alpha05) |

## Structure

Compose is combination of 7 Maven Group Ids within `androidx`. Each Group
contains a targeted subset of functionality, each with its own set of release
notes.

This table explains the groups and links to each set of release notes.

| Group | Description |
|---|---|
| [compose.animation](https://developer.android.com/jetpack/androidx/releases/compose-animation) | Build animations in their Jetpack Compose applications to enrich the user experience. |
| [compose.compiler](https://developer.android.com/jetpack/androidx/releases/compose-compiler) | Transform @Composable functions and enable optimizations with a Kotlin compiler plugin. |
| [compose.foundation](https://developer.android.com/jetpack/androidx/releases/compose-foundation) | Write Jetpack Compose applications with ready to use building blocks and extend foundation to build your own design system pieces. |
| [compose.material](https://developer.android.com/jetpack/androidx/releases/compose-material) | Build Jetpack Compose UIs with ready to use Material Design Components. This is the higher level entry point of Compose, designed to provide components that match those described at www.material.io. |
| [compose.material3](https://developer.android.com/jetpack/androidx/releases/compose-material3) | Build Jetpack Compose UIs with Material Design 3 Components, the next evolution of Material Design. Material 3 includes updated theming and components and Material You personalization features like dynamic color, and is designed to be cohesive with the new Android 12 visual style and system UI. |
| [compose.runtime](https://developer.android.com/jetpack/androidx/releases/compose-runtime) | Fundamental building blocks of Compose's programming model and state management, and core runtime for the Compose Compiler Plugin to target. |
| [compose.ui](https://developer.android.com/jetpack/androidx/releases/compose-ui) | Fundamental components of compose UI needed to interact with the device, including layout, drawing, and input. |

## Declaring dependencies

To add a dependency on Compose, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.compose.runtime:runtime:1.10.3"
    implementation "androidx.compose.runtime:runtime-livedata:1.10.3"
    implementation "androidx.compose.runtime:runtime-rxjava2:1.10.3"
}

android {
    buildFeatures {
        compose true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.compose.runtime:runtime:1.10.3")
    implementation("androidx.compose.runtime:runtime-livedata:1.10.3")
    implementation("androidx.compose.runtime:runtime-rxjava2:1.10.3")
}

android {
    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.15"
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:610764+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=610764&template=1424126)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Runtime Tracing Version 1.7

### Version 1.7.0-rc01

September 18, 2024

`androidx.compose.runtime:runtime-tracing:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/runtime/runtime-tracing).

## Runtime Tracing Version 1.0

### Version 1.0.0-beta01

November 29, 2023

`androidx.compose.runtime:runtime-tracing:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/compose/runtime/runtime-tracing)

### Version 1.0.0-alpha05

November 15, 2023

`androidx.compose.runtime:runtime-tracing:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose/runtime/runtime-tracing)

**Bug Fixes**

- Pinned dependencies to lowest supported stable versions (i.e. compose-runtime and tracing-perfetto) - fixing an issue where compose-runtime-tracing would bring in a newer version of compose-runtime into the app.

### Version 1.0.0-alpha04

August 23, 2023

`androidx.compose.runtime:runtime-tracing:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/runtime/runtime-tracing)

**New Features**

- Compatible with latest versions of Benchmark and Tracing Perfetto, enabling support for Composition Tracing at app startup (cold start) e.g. in AndroidX Benchmark and Android Studio (starting from Hedgehog Beta 2).

**API Changes**

- Renamed `androidx.tracing.perfetto.Trace` to `androidx.tracing.perfetto.PerfettoSdkTrace`. ([I44af8](https://android-review.googlesource.com/#/q/I44af824893288c17c792369058132cca3ac61f1b))
- Making Tracing Perfetto SDK APIs consistent with `android.os.Trace`. ([I73ba0](https://android-review.googlesource.com/#/q/I73ba07ca6cc4bd2b6519553c395fe9075a49fe75), [b/282199917](https://issuetracker.google.com/issues/282199917))
- Prerequisites for tracing at app startup. ([Iad890](https://android-review.googlesource.com/#/q/Iad890a61eab26611469704a7451c6fdc611622e5))
- Merged experimental and public API files ([I0f2e1](https://android-review.googlesource.com/#/q/I0f2e1b547f5c460e72edae3d84f3ae7cfc27cf30), [b/278769092](https://issuetracker.google.com/issues/278769092))

### Version 1.0.0-alpha02

February 8, 2023

`androidx.compose.runtime:runtime-tracing:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..f7337eab774a6ce3b17367d5f31708564b66e677/compose/runtime/runtime-tracing)

**New Features**

- No functional changes. Multiple performance optimisations in downstream dependencies `androidx.tracing:tracing-perfetto*`.

### Version 1.0.0-alpha01

September 7, 2022

`androidx.compose.runtime:runtime-tracing:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/runtime/runtime-tracing)

**New Features**

- `androidx.compose.runtime:runtime-tracing` is a library which - in the presence of tooling supporting it (coming soon) - allows for extended tracing in a Compose app. This initial release is 1.0.0-alpha01.

## Version 1.11

### Version 1.11.0-alpha05

February 11, 2026

`androidx.compose.runtime:runtime-*:1.11.0-alpha05` is released. Version 1.11.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..cdf076c6abd0f3125cb0302756fcb77fe981ab7c/compose/runtime).

**API Changes**

- `ComposeRuntimeFlags.isMovingNestedMovableContentEnabled`, a runtime feature flag, has been removed. ([I3ee62](https://android-review.googlesource.com/#/q/I3ee6207230e3cb6966e7199d34818946b866020d), [b/455588848](https://issuetracker.google.com/issues/455588848))
- Converted `HostDefaultKey` from an `open class` to an `interface`. This allows keys to implement multiple lookup mechanisms (such as `ViewTreeHostDefaultKey`) without being restricted by single-class inheritance, improving extensibility for custom hosting environments. ([I917a2](https://android-review.googlesource.com/#/q/I917a2b6d3e3b9e2bf6c44c0e63815e663940ec8b))
- `HostDefaultProvider` and `LocalHostDefaultProvider` are now `public`, allowing custom hosting environments to define values for platform-specific locals. ([I5bdbe](https://android-review.googlesource.com/#/q/I5bdbea665d23b23e53cdb9c96dfeece51b5f4687))

**Bug Fixes**

- Eliminated the possibility of deadlocking when running two `snapshotFlow`s simultaneously on two threads. ([Ib4339](https://android-review.googlesource.com/#/q/Ib43399d4417111af8385f3865ff2e6606f9acfdd))
- Fixed an issue in the link table that could cause tooling to omit composables in the hierarchy and incorrectly link subcompositions ([I7178e](https://android-review.googlesource.com/#/q/I7178e2d75c6a4a1767980781aa4028d495637a3d))

**External Contribution**

- Fixed Lint false positive when using a unary operator to modify the value in a produceState block ([I1c7c9](https://android-review.googlesource.com/#/q/I1c7c9aaf2aac3371cfb58868cdddfc83d22f3806))

### Version 1.11.0-alpha04

January 28, 2026

`androidx.compose.runtime:runtime-*:1.11.0-alpha04` is released. Version 1.11.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..c26c6f088b95903b7b9cd5e6f2092988f1e64dc3/compose/runtime).

**API Changes**.

- We've rewritten the `SlotTable`, which is the internal data structure used by the Compose Runtime to track your composition hierarchy, determine the changes caused by a recomposition, and store remembered values. This rewrite is focused on improving recomposition performance and does so primarily by using substantially fewer memory copy operations than the gap buffer `SlotTable`. Certain changes to your composition hierarchy, like reordering a long list of items, can recompose over twice as fast compared to the former `SlotTable`. Most other operations are on the order of 10% faster to recompose under the new `SlotTable` implementation. The `SlotTable` implementation used by the runtime affects all Composable methods and requires no recompilation. Using the new `SlotTable` is an app-wide change, including for dependencies.
- This `SlotTable` implementation is currently disabled by default and can be enabled by setting `ComposeRuntimeFlags.isLinkBufferComposerEnabled` to `true`.
- In release builds with minification enabled, this value is assumed to be `false` in the default `proguard-rules.pro` file supplied with the runtime. To enable the new `SlotTable` in production, this assumption needs to be changed to `true` in the application's `proguard-rules.pro` file. See the documentation on `ComposeRuntimeFlags.isLinkBufferComposerEnabled` for more information. ([Ib741d](https://android-review.googlesource.com/#/q/Ib741df400f1035c79df9ce3d34c39dd35fb9445e), [b/268366116](https://issuetracker.google.com/issues/268366116))

**New Features**

- Added `compositionLocalWithHostDefaultOf` which allows defining `CompositionLocals` that fallback to the hosting environment (e.g. Android View tags) for their default values. ([I15b81](https://android-review.googlesource.com/#/q/I15b81bf6a9cb50575ba37d0061bead8b1a09b2a0))

**Bug Fixes**

- Ensured that `Snapshot.sendApplyNotifications` calls cannot return until the necessary apply notifications have been sent. ([I95f20](https://android-review.googlesource.com/#/q/I95f209dbc6c08e1a847b0fc4acde586618a7c1b3), [b/418800424](https://issuetracker.google.com/issues/418800424))
- Prevent source information stack traces downgrading to group keys in cases when source information is not present at runtime. ([If3712](https://android-review.googlesource.com/#/q/If371286516f3e0cffecca02926084ea63d2793e5))
- Introduce `ComposeToolingFlags`. These flags are intended to be permanent (as opposed to `ComposeRuntimeFlags`) and are used for tooling features that have non-trivial impact on performance. ([I87863](https://android-review.googlesource.com/#/q/I878638c78c6989b55a69b92e4e715dbf108f1d03))

**External Contribution**

- New experimental `RecomposerInfo#errorState` API ([I0decc](https://android-review.googlesource.com/#/q/I0deccd5180b3f548b52621ef1610ce731a3a1f2d))
- Change `AnnotationRetention` of the `FunctionKeyMeta` annotation to 'BINARY' ([I53495](https://android-review.googlesource.com/#/q/I53495e8be92aa7ff3da40474ff21342f05820d7a))

### Version 1.11.0-alpha03

January 14, 2026

`androidx.compose.runtime:runtime-*:1.11.0-alpha03` is released. Version 1.11.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/compose/runtime).

**API Changes**

- Introduced the `SnapshotFlowManager` class and added an optional `SnapshotFlowManager` parameter to `snapshotFlow`, giving users the ability to optimize the number of snapshot apply observers that get registered. ([I6289b](https://android-review.googlesource.com/#/q/I6289b0067a22e06e4e501b022711527a5bbba253), [b/446746211](https://issuetracker.google.com/issues/446746211))

**Bug Fixes**

- Added a trace annotation for movable content insertion ([Ibf176](https://android-review.googlesource.com/#/q/Ibf17622db1205eaccbed297e3c904b17fbb8727d))

### Version 1.11.0-alpha02

December 17, 2025

`androidx.compose.runtime:runtime-*:1.11.0-alpha02` is released. Version 1.11.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/compose/runtime).

**API Changes**

- The `isMovableContentUsageTrackingEnabled` flag is removed ([I71e2b](https://android-review.googlesource.com/#/q/I71e2ba969fac15ecdba36b4b2433bac297a0c760), [b/427960130](https://issuetracker.google.com/issues/427960130))

**External Contribution**

- Bug fixed with Live Edit that does not recover from error. ([Ieb34f](https://android-review.googlesource.com/#/q/Ieb34ffb231a0f6dea10752eb4f25d381e1b1c33c))

### Version 1.11.0-alpha01

December 03, 2025

`androidx.compose.runtime:runtime-*:1.11.0-alpha01` is released. Version 1.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b48588febd37d5947dfa0f2827d2b5ca6af2ed90..deb96499dfe95073f5c1215c1287787683cb1e92/compose/runtime).

**API Changes**

- `RetainedValuesStore.getExitedValueOrDefault` is renamed to `consumeExitedValueOrDefault`[c7a0929](https://android.googlesource.com/platform/frameworks/support/+/c7a09293ee22e2c0b7591867879a6fe420b0d0fd)
- Remove experimental concurrent recomposition API.([c8af15d](https://android.googlesource.com/platform/frameworks/support/+/c8af15d82f1d88141a2f6123f73a1ea26ef27dcd))

## Version 1.10

### Version 1.10.3

February 11, 2026

`androidx.compose.runtime:runtime-*:1.10.3` is released. Version 1.10.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b..0d23f956849b578e041ea4245127d4007eae43be/compose/runtime).

### Version 1.10.2

January 28, 2026

`androidx.compose.runtime:runtime-*:1.10.2` is released. Version 1.10.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c09ac6669b664a348ecf964a97968cd81479dcd4..fc5dfcfe7ee3e7025b8da18f02c3d1d3fa96d75b/compose/runtime).

### Version 1.10.1

January 14, 2026

`androidx.compose.runtime:runtime-*:1.10.1` is released. Version 1.10.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9..c09ac6669b664a348ecf964a97968cd81479dcd4/compose/runtime).

### Version 1.10.0

December 03, 2025

`androidx.compose.runtime:runtime-*:1.10.0` is released. Version 1.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26..a1a52f4350c7cb9288486c6fbc7c03af2d6ef9b9/compose/runtime).

### Version 1.10.0-rc01

November 19, 2025

`androidx.compose.runtime:runtime-*:1.10.0-rc01` is released. Version 1.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1c84233fc2372352b838d165d256581ff37ada9..b48588febd37d5947dfa0f2827d2b5ca6af2ed90/compose/runtime).

**Bug Fixes**

- Guard against reentrant modification when recording derived states in `SnapshotStateObserver` ([I7b862](https://android-review.googlesource.com/#/q/I7b86222f143f4a70dfcc0be9c9bde437ab756e64), [b/435655844](https://issuetracker.google.com/issues/435655844), [b/456249373](https://issuetracker.google.com/issues/456249373), [b/402535073](https://issuetracker.google.com/issues/402535073))
- \[Lint\] Minor bug fix to make the detector warn compound assignment properly. ([I08319](https://android-review.googlesource.com/#/q/I08319a3f15e1f9dd2f4edd28a7dea9e7d131c481), [b/456775556](https://issuetracker.google.com/issues/456775556))

### Version 1.10.0-beta02

November 05, 2025

`androidx.compose.runtime:runtime-*:1.10.0-beta02` is released. Version 1.10.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/784e4a2de372f09d49c65fbc1ca64681a25a5f06..d1c84233fc2372352b838d165d256581ff37ada9/compose/runtime).

**API Changes**

- We've made several API-incompatible changes to simplify the installation and management of `RetainedValuesStore`s. Existing calls to `retain` and `RetainedEffect` are unaffected, but any custom `RetainedValuesStore`s will require a migration to be compatible with this release. ([If3c2f](https://android-review.googlesource.com/#/q/If3c2f6af591234cc185e38263fa5671c72ff5813), [b/451921682](https://issuetracker.google.com/issues/451921682), [b/450539803](https://issuetracker.google.com/issues/450539803))

- `RetainedValuesStore` no longer exposes low-level APIs to start/stop retention. Retention state now automatically follows the content. `LocalRetainedValuesStoreProvider` is now offered to install `RetainedValuesStore`. `LocalRetainedValuesStore` should not be provided directly. See the updated documentation and samples for more information on these changes.

- `RetainedValuesStoreProvider` is renamed to `RetainedValuesStoreRegistry`. This class now only exposes APIs to install and manage the `RetainedValuesStore`s in composition.

- `ControlledRetainedValuesStore` is replaced by `ManagedRetainedValuesStore`.

- `RetainedValuesStore` is now an interface.

Previously, installing a custom `RetainedValuesStore` may have looked like this:

      val retainedValuesStore = retainControlledRetainedValuesStore()
      if (active) {
          CompositionLocalProvider(LocalRetainedValuesStore provides retainedValuesStore) {
              content()
          }

          val composer = currentComposer
          DisposableEffect(retainedValuesStore) {
              val cancellationHandle =
                  if (retainedValuesStore.retainExitedValuesRequestsFromSelf > 0) {
                      composer.scheduleFrameEndCallback {
                          retainedValuesStore.stopRetainingExitedValues()
                      }
                  } else {
                      null
                  }

              onDispose {
                  cancellationHandle?.cancel()
                  retainedValuesStore.startRetainingExitedValues()
              }
          }
      }

With these API changes, this installation can be expressed with this code instead:

      val retainedValuesStore = retainManagedRetainedValuesStore()
      if (active) {
          LocalRetainedValuesStoreProvider(retainedValuesStore) {
              content()
          }
      }

**Bug Fixes**

- Transfers invalidations of the scope in movable content before moving that content out of the slot table ([I9d123](https://android-review.googlesource.com/#/q/I9d1230d2fc2ff52f9e041b4d42bb6d3d86fd1d80), [b/451651649](https://issuetracker.google.com/issues/451651649))

### Version 1.10.0-beta01

October 22, 2025

`androidx.compose.runtime:runtime-*:1.10.0-beta01` is released. Version 1.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4350deab5806bf95370a4d012d7eeaa70a10be44..784e4a2de372f09d49c65fbc1ca64681a25a5f06/compose/runtime).

**API Changes**

- `RetainedValuesStore.getExitedValueOrDefault` is renamed to `RetainedValuesStore.getExitedValueOrElse` ([If9653](https://android-review.googlesource.com/#/q/If9653ebe8d634c1cfb6e255cc7f82bb295965cf9), [b/452340613](https://issuetracker.google.com/issues/452340613))
- `isKeepingExitedValues` has been renamed to `isRetainingExitedValues` ([I660bf](https://android-review.googlesource.com/#/q/I660bfbab80322e06092195fbc5e02fec10b19fdb), [b/437095756](https://issuetracker.google.com/issues/437095756))
- `RetainScope` has been renamed to `RetainedValuesStore`. `RetainScopeHolder` has been renamed to `RetainedValuesStoreRegistry`. `RetainScopeHolder.RetainScopeProvider` has been renamed to `RetainedValuesStoreRegistry.ProvideChildRetainedValuesStore`. ([Idf23a](https://android-review.googlesource.com/#/q/Idf23a7b7c1ede2e4f980b97b391364891f6261e4), [b/437095756](https://issuetracker.google.com/issues/437095756))

**Bug Fixes**

- Delayed initialization of `SavedState` in `SaveableStateRegistry` until the first usage. ([Ic0a93](https://android-review.googlesource.com/#/q/Ic0a93f45587427a02351bf7320bddc8cc660d2f5))

### Version 1.10.0-alpha05

October 08, 2025

`androidx.compose.runtime:runtime-*:1.10.0-alpha05` is released. Version 1.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef9c81cf7222a390e0a467d8c8b48d04362fd3d..4350deab5806bf95370a4d012d7eeaa70a10be44/compose/runtime).

**Bug Fixes**

- Fill in the stack trace for `DiagnosticComposeException` in release mode. ([Ib76cb](https://android-review.googlesource.com/#/q/Ib76cba026417427c9bb7eac21b3b3e3a942ae956))
- Fixed an issue in Snapshot state where, when using a merge policy for a type could result in the previous value to be computed incorrectly which would return a future value of the state instead of the previous value. This would occur if more than two mutable snapshots were pending and at least one of the values being applied had a merge policy. ([I527b5](https://android-review.googlesource.com/#/q/I527b56bcfc9f423e5f862f460e78260a9da47844), [b/442791065](https://issuetracker.google.com/issues/442791065))

### Version 1.10.0-alpha04

September 24, 2025

`androidx.compose.runtime:runtime-*:1.10.0-alpha04` is released. Version 1.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cf4bc156e75473f159aa2536c8948d273ac67d97..6ef9c81cf7222a390e0a467d8c8b48d04362fd3d/compose/runtime).

**API Changes**

- Added `RetainScopeHolder` API to manage a collection of `RetainScopes`. This can be used to implement retention for containers and navigation hosts that compose many children with different retention lifespans. ([I10e0f](https://android-review.googlesource.com/#/q/I10e0faa45a33ef4fc34c77428dfb24e4c49233de))
- Added `RetainedContentHost` and `retainControlledRetainScope` APIs, which can be used to create automatically managed `RetainScopes` for disappearing content like collapsing panes ([If81f6](https://android-review.googlesource.com/#/q/If81f63ae07c9080dc05bd3c5c5b99372a34b0766))
- Deprecated inline overload of `Updater#set` as it was boxing the provided value too many times. Added an overload of `Updater#init` which takes a parameter which avoids requiring a capturing lambda. ([Id679e](https://android-review.googlesource.com/#/q/Id679eefb099cbf45c00ba01338af5c1cfa2f8782))
- Introduces `RetainedEffect`, a side-effect API similar to `DisposableEffect` that follows the retention lifecycle instead of the composition lifecycle. This API is intended to be used for effects tied to the retention of another object that doesn't or can't implement `RetainObserver`. ([I1c61f](https://android-review.googlesource.com/#/q/I1c61f7f644a99e2ca57bec4f617e443c2c0ac480), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Corrected documentation of `RetainObserver.onRetained` and added `RetainObserver.onUnused`, which mirrors `RememberObserver.onAbandoned` ([Ia6fc5](https://android-review.googlesource.com/#/q/Ia6fc517b08308e53e8742202c3cc5525d173e077))

**Bug Fixes**

- Fixed dispatching remember after the first group in a function (such as a composable call) and before a group that can be removed (such as an `if` statement) that could dispatch `onForgotten` in incorrect order. ([I453f6](https://android-review.googlesource.com/#/q/I453f64705cc4dd092c14f0027d837b00760b80f7), [b/346821372](https://issuetracker.google.com/issues/346821372))
- Avoid coroutine context traversal when initializing `LaunchedEffect`. ([I8d2c3b](https://android-review.googlesource.com/#/q/I8d2c3b65feffb9cd388e64b3facab5dcd2853e1a))

### Version 1.10.0-alpha03

September 10, 2025

`androidx.compose.runtime:runtime-*:1.10.0-alpha03` is released. Version 1.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..cf4bc156e75473f159aa2536c8948d273ac67d97/compose/runtime).

**API Changes**

- Introduces group key based Compose stack traces that work in minified apps. The proguard mapping for these traces will be generated by Compose compiler Gradle plugin starting from Kotlin 2.3.0. These stack traces are disabled by default, use `ComposeStackTraceMode.GroupKeys` to enable them. ([Ifbcb5](https://android-review.googlesource.com/#/q/Ifbcb5302344d20eca05d9762662bcad893d80a56))
- Add interface: `IdentifiableRecomposeScope` for tooling ([Idd5e0](https://android-review.googlesource.com/#/q/Idd5e0a03388fbc5776b28548b4a3f47206d899b8), [b/434194620](https://issuetracker.google.com/issues/434194620))
- Prevented unnecessary invalidations from occurring in compositions involving `CompositionLocalContext`s ([I3fa21](https://android-review.googlesource.com/#/q/I3fa21d18c0497c18bc077ac4541ef2d9480a85a8), [b/412750209](https://issuetracker.google.com/issues/412750209))

**Bug Fixes**

- Clarified in documentation and in tooling that keys passed to retain are also retained. Avoid passing keys to retain that will lead to a memory leak. ([Ib553b](https://android-review.googlesource.com/#/q/Ib553beecc3f574424d5ce9d7cc66d48021d87558), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Fixed and issue when a paused composition's `resume()` is called on a different thread, the state of the pending notifications could get confused when the main thread tries to recompose the pausable composition for the next frame. ([Ie5f17](https://android-review.googlesource.com/#/q/Ie5f178c03e698aa112b5d531284b0cad7ea7e28c), [b/442649894](https://issuetracker.google.com/issues/442649894))
- Log exceptions captured in composition. ([I47d78](https://android-review.googlesource.com/#/q/I47d789b046af1019114a965dc8b7b8950481094e), [b/432799675](https://issuetracker.google.com/issues/432799675), [b/436878515](https://issuetracker.google.com/issues/436878515), [b/359623674](https://issuetracker.google.com/issues/359623674), [b/400436355](https://issuetracker.google.com/issues/400436355))

### Version 1.10.0-alpha02

August 27, 2025

`androidx.compose.runtime:runtime-*:1.10.0-alpha02` is released. Version 1.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c359e97fece91f3767a7d017e9def23c7caf1f53..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/compose/runtime).

**API Changes**

- Added `@DoNotRetain`, which can be used to annotate types that should not be used with the `retain` API, possibly because they will leak resources. ([Ie5435](https://android-review.googlesource.com/#/q/Ie5435ce4b51204035a9ecfb52945d7bc7356f181))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

**Bug Fixes**

- Fixed movable content to correctly compute the operations to the Applier when the content modifies the root node of a composition. When computing changes for movable content an `up()` call could be left pending and undispatched to the applier causing the applier state to be incorrectly positioned for any subsequent use. ([I7c583](https://android-review.googlesource.com/#/q/I7c5835bab1e6565813567c985f574907cc1d4d56)), ([I47b70](https://android-review.googlesource.com/#/q/I47b70ec2f90273a55aa7d794a58280cf513b66ff))
- Marks `CheckResult` as deprecated because it is not meant to be used. ([I32934](https://android-review.googlesource.com/#/q/I329342171d0e1081acaf7929a82895b9c985c71e))

### Version 1.10.0-alpha01

August 13, 2025

`androidx.compose.runtime:runtime-*:1.10.0-alpha01` is released. Version 1.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c30d03ab9e19dcf35e8b79438f0d91ee74cae557..c359e97fece91f3767a7d017e9def23c7caf1f53/compose/runtime).

**API Changes**

- Introduces the retain API. Like `rememberSaveable`, retain can persist and save remembered values that leave the composition hierarchy. Retained values are not serialized and have a shorter lifespan than saved values, and behave similarly to an androidx `ViewModel`. See the documentation for more details. ([Ia3105](https://android-review.googlesource.com/#/q/Ia31056d0ea23d6358a11d8ad9f472b51f41879d8), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Added an `awaitOrScheduleNextCompositionEnd()` API, which issues a callback when the Recomposer finishes composing the current frame. If the Recomposer isn't currently composing a frame, this API suspends until the next frame's composition finishes and schedules a new frame to be composed. ([Ib873c](https://android-review.googlesource.com/#/q/Ib873cd7d64e63f6337232634faf04ee9e711f7fd))
- Add a non-unit returning composition local provider API ([I22521](https://android-review.googlesource.com/#/q/I22521efe847f230577e3b00311221677060d9d20), [b/271871288](https://issuetracker.google.com/issues/271871288))
- Added a feature flag, `isMovableContentUsageTrackingEnabled`, that allows tracking the usage of movable content to avoid some overhead when initially creating the content. This feature flags is currently disabled by default. ([Ia713d](https://android-review.googlesource.com/#/q/Ia713da2a0882b134a4819f98a73caf97b994b64a))

**Bug Fixes**

- Fixes a crash in movable content when it is moved between subcompositions. ([I3fa1e](https://android-review.googlesource.com/#/q/I3fa1e3aec35022431b7579bf7b41458c5d53e636), [b/436858107](https://issuetracker.google.com/issues/436858107))
- Fixes a bug with part of a composable stack trace missing when inside multiple nested subcompositions. ([I98c6f](https://android-review.googlesource.com/#/q/I98c6ffd441e8ac999a11c9bcfd902411ba37055f))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Fixed a race condition when internal state of a pausable composition was being updated from multiple threads. ([I03895](https://android-review.googlesource.com/#/q/I0389587852f5758890d594c1b5466433c458bfe7))
- Updates composition registration observer to be called before initial composition. ([I4adca](https://android-review.googlesource.com/#/q/I4adcae354abb1c55c66d213812b10830614f8e9c), [b/430600932](https://issuetracker.google.com/issues/430600932))
- Minor bug fix to make `AutoboxingStateValuePropertyDetector` compatible for both K1 and K2. ([Ie81c1](https://android-review.googlesource.com/#/q/Ie81c19fdfb3d88da4b56ae251a3a462dbe927923))

**External Contribution**

- Make the runtime-rxjava2 artifact multiplatform and add the JVM as a supported target. ([I5409e](https://android-review.googlesource.com/#/q/I5409efb25f70afcb01d3532df3087609d835991b))
- Make the runtime-rxjava3 artifact multiplatform and add the JVM as a supported target. ([I97e84](https://android-review.googlesource.com/#/q/I97e841cbb23a687fbeb7b2808200c4899aa34037))

## Version 1.9

### Version 1.9.5

November 19, 2025

`androidx.compose.runtime:runtime-*:1.9.5` is released. Version 1.9.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41..1dc35fe3e1d2d1b9dad444a0458c5e8039ba3d26/compose/runtime).

**Bug Fixes**

- Transfers invalidations of the scope in movable content before moving that content out of the slot table ([I9d123](https://android-review.googlesource.com/#/q/I9d1230d2fc2ff52f9e041b4d42bb6d3d86fd1d80), [b/451651649](https://issuetracker.google.com/issues/451651649))

### Version 1.9.4

October 22, 2025

`androidx.compose.runtime:runtime-*:1.9.4` is released. Version 1.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ea7909f13c54ea29d87d55d27ecf449000f82a8a..b7d3ef4c3ddc955decb747a0aa7b72eb953b1e41/compose/runtime).

### Version 1.9.3

October 08, 2025

`androidx.compose.runtime:runtime-*:1.9.3` is released. Version 1.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6177e34a7667c42030e47ee8ecba82f09e2a5de..ea7909f13c54ea29d87d55d27ecf449000f82a8a/compose/runtime).

### Version 1.9.2

September 24, 2025

`androidx.compose.runtime:runtime-*:1.9.2` is released. Version 1.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/93a1ed2aac05dbfa192392b9d4ab27c40da53d69..b6177e34a7667c42030e47ee8ecba82f09e2a5de/compose/runtime).

### Version 1.9.1

September 10, 2025

`androidx.compose.runtime:runtime-*:1.9.1` is released. Version 1.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/44da9aeaf3fa617c6f81f887691b37fe901109aa..93a1ed2aac05dbfa192392b9d4ab27c40da53d69/compose/runtime).

**Bug Fixes**

- Avoid recomposing compositions that are in the process of composing. ([Iacb01](https://android-review.googlesource.com/#/q/Iacb01dfc10a13ebe30e9594fa430b0e2f56bca49))
- Prevent recompose scopes from being paused twice. ([I060b2](https://android-review.googlesource.com/#/q/I060b2aa9277722351543c8873b52f7dad872a06c), [b/431584881](https://issuetracker.google.com/431584881))

### Version 1.9.0

August 13, 2025

`androidx.compose.runtime:runtime-*:1.9.0` is released. Version 1.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..44da9aeaf3fa617c6f81f887691b37fe901109aa/compose/runtime).

**Important changes since 1.8.0**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your gradle.properties. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.
- A new runtime-annotation library has been created. This contains annotation definitions without a dependency on Compose runtime, so it can be used from non-Compose modules.
  - `@Stable`, `@Immutable`, and `@StableMarker` have been moved to runtime-annotation, to allow annotating non-Compose modules
  - `@FrequentlyChangingValue` and `@RememberInComposition` have been added to runtime-annotation. `@FrequentlyChangingValue` marks declarations that can cause frequent recompositions, and `@RememberInComposition` marks declarations that should be remembered in composition. Corresponding lint checks warn for incorrect usage.

### Version 1.9.0-rc01

July 30, 2025

`androidx.compose.runtime:runtime-*:1.9.0-rc01` is released. Version 1.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5735a11c1798c2f8b419dfdc02347578a6ebf870..c30d03ab9e19dcf35e8b79438f0d91ee74cae557/compose/runtime).

**Bug Fixes**

- Updates composition registration observer to be called before initial composition. ([I4adca](https://android-review.googlesource.com/#/q/I4adcae354abb1c55c66d213812b10830614f8e9c), [b/430600932](https://issuetracker.google.com/issues/430600932))

### Version 1.9.0-beta03

July 16, 2025

`androidx.compose.runtime:runtime-*:1.9.0-beta03` is released. Version 1.9.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d578548e34459870db64b61d8788d83f2cf49f54..5735a11c1798c2f8b419dfdc02347578a6ebf870/compose/runtime).

### Version 1.9.0-beta02

July 2, 2025

`androidx.compose.runtime:runtime-*:1.9.0-beta02` is released. Version 1.9.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3a0aa7a0552da83ba3994838f5db40d0d7a6196f..d578548e34459870db64b61d8788d83f2cf49f54/compose/runtime).

**Bug Fixes**

- Reduced the reference lifetime of values in the slot table between compositions. There are cases where a reference in a slot table could last a frame longer than necessary. ([I49e74](https://android-review.googlesource.com/#/q/I49e7488186782a95cb62358292b2950b5730089b), [b/418516940](https://issuetracker.google.com/issues/418516940))
- Remove Kotlin mangle for Hot reload methods. ([Ic56a3](https://android-review.googlesource.com/#/q/Ic56a3142f763b01a14b29e1cc20937622efd21eb), [b/426871325](https://issuetracker.google.com/issues/426871325))

### Version 1.9.0-beta01

June 18, 2025

`androidx.compose.runtime:runtime-*:1.9.0-beta01` is released. Version 1.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2483fff136f4442bcaab608b3194ffe0b58565ef/compose/runtime).

**API Changes**

- Added a tooling API for parsing source information added by Compose compiler. ([Iceaf9](https://android-review.googlesource.com/#/q/Iceaf954bf1d09a8ada7b908ceb2909c7f4652819), [b/408492167](https://issuetracker.google.com/issues/408492167))
- `SnapshotStateSet` now implements `Parcelable` on Android, it is now supported to be used as part `rememberSaveable { ... }`. ([I755dd](https://android-review.googlesource.com/#/q/I755dd7d20ed39545a1b7805b28b676fcff019fff), [b/378623803](https://issuetracker.google.com/issues/378623803))
- `SnapshotStateList` now implements `Parcelable` on Android, it is now supported to be used as part `rememberSaveable { ... }`. ([Id18be](https://android-review.googlesource.com/#/q/Id18be0bf1ad0bf5c7de580f5289629b838c76876), [b/378623803](https://issuetracker.google.com/issues/378623803))
- `movableContentOf()` is now marked with `@RememberInComposition` annotation, which allows lint to catch incorrect usages ([I2738d](https://android-review.googlesource.com/#/q/I2738d6889fdf3aea8a6017d30c8a8f53c7915e9d))
- Updated experimental composition observers API to allow for more comprehensive observation of recomposition causes ([I32b6a](https://android-review.googlesource.com/#/q/I32b6ac0ac3c4c584e03c755a1651b28882ae4a37))
- Change `setDiagnosticStackTraceEnabled` to experimental to account for future development of this feature. ([I11db3](https://android-review.googlesource.com/#/q/I11db30dfc2e0922aa4da13bc9769ab33f3e94f65))
- `currentCompositeKeyHash` is now deprecated. Use `currentCompositeKeyHashCode` instead. The replacement API encodes the same hash with more bits, which exponentially reduces the chance of two random unrelated groups in the composition hierarchy from having the same hash key. ([I4cb6a](https://android-review.googlesource.com/#/q/I4cb6a801d12447ac52bc92bb899ae84d69c4a6ed), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `@Stable`, `@Immutable`, and `@StableMarker` have been moved to runtime-annotation (in a compatible way). You can now depend on runtime-annotation if you want to use these annotations from libraries that do not depend on compose. ([I23a16](https://android-review.googlesource.com/#/q/I23a16a27aaacc1a17c181d821e4a6fdcef2ea882))
- Renamed the `rememberSaveable` overload that accepts a `KSerializer` to `rememberSerializable`. This change clarifies its intended use with `kotlinx.serialization`. Supporting general `kotlinx.Serializable` classes directly in `rememberSaveable` would require a `reified` type parameter, which would break source compatibility by requiring all call sites to provide reified type information at compile time. ([Idb875](https://android-review.googlesource.com/#/q/Idb875617dfef959fa3200de01524580f19d35dbe), [I38627](https://android-review.googlesource.com/#/q/I38627f58f4aa77af80e68f4a2925a379d9157c23), [b/376028110](https://issuetracker.google.com/issues/376028110))

**Bug Fixes**

- Compositions that was set with pausable content that was cancelled must be disposed of. This is now checked by the composition and will throw if it is reused. ([I2daa5](https://android-review.googlesource.com/#/q/I2daa59af4c943aaab3d2b656341a28735bdb5d83), [b/406792785](https://issuetracker.google.com/issues/406792785))
- Fixed pausable composition to no longer send a spurious `onForgotten` to remember observers when the pausable composition is disposed of. `RememberObservers` in a cancelled pausable composition should only be sent an onAbandoned. ([I26f54](https://android-review.googlesource.com/#/q/I26f5486a9d563a6d17937224adaeb4e8a2d928a0))
- Fixed a movable content issue where invalidations that arrive late stages of the processing movable content are added to the composer but these invalidations are not updated when the content is moved causing the content to be recomposed in the wrong place. ([Icd2fa](https://android-review.googlesource.com/#/q/Icd2fa594f8e701b98b7241bf3279c3a92861099d), [b/409439507](https://issuetracker.google.com/issues/409439507))
- Fixed an issue when movable content was invalidated after it was composed but before it was moved. ([I99eac](https://android-review.googlesource.com/#/q/I99eac55ca58f7addfdee0cbb5088d365e7ff4644), [b/229001114](https://issuetracker.google.com/issues/229001114))
- Calling `remove()` of a list iterator produced by `SnapshotStateList` after calling `previous()` could removed the wrong element from the list and didn't match what the `ArrayList` does for the same sequence of calls. ([I05ab7](https://android-review.googlesource.com/#/q/I05ab7c8d15a88652badb021fc65c4fb103556788), [b/417493222](https://issuetracker.google.com/issues/417493222))
- Fixed an ordering issue with the dispatching of `onForgotton` that could, for example, cause the `onDispose` of disposable effects to execute in the wrong order. ([Ic1c91](https://android-review.googlesource.com/#/q/Ic1c9127c3faf980e373eaa2c162a6cc49d55ff28), [b/417450712](https://issuetracker.google.com/issues/417450712))
- Fix for for reusing state handling in pausable composition ([Ife96e](https://android-review.googlesource.com/#/q/Ife96e7e011daa3644cdda2f112bbe7bbedb49ae4), [b/404058957](https://issuetracker.google.com/issues/404058957))
- Fixed the reusing state when a composition was paused and restarted but some previously paused state needed to be recomposed because some state it read changed while the composition was paused. ([I441d1](https://android-review.googlesource.com/#/q/I441d17b0bcca7b7073347a9b7cea89333cff2c93), [b/416209738](https://issuetracker.google.com/issues/416209738))
- Completed the pausable composition remember dispatch fix for issue [b/404058957](https://issuetracker.google.com/issues/404058957) previous fix was incomplete. ([I1afd4](https://android-review.googlesource.com/#/q/I1afd4981c6dadda8f61b02fe42d146f6f5d3c52e), [b/404058957](https://issuetracker.google.com/issues/404058957))
- `OffsetApplier` now correctly overrides `apply()` which was introduced with pausable composition. Not having this could cause pausable composition to throw an exception when updating virtual nodes. ([Idbf31](https://android-review.googlesource.com/#/q/Idbf314adbd64254dd4a4eb4e3a897930ece407c7), [b/409291131](https://issuetracker.google.com/issues/409291131))
- Fixed a deadlock that may affect Molecule users when a suspended call to `FrameClock.withFrameNanos` is cancelled while a frame is being dispatched. ([I89cab](https://android-review.googlesource.com/#/q/I89cab8e3eab14ed9a85b36e151f11b5f526a01fd), [b/407027032](https://issuetracker.google.com/issues/407027032))
- The Recomposer could go idle with movable content ([Ie5416](https://android-review.googlesource.com/#/q/Ie54168320625f09c9390d542caa625f1f0d1d896), [b/409267170](https://issuetracker.google.com/issues/409267170))
- The order in which `onReuse` and `onDeactivate` could get inverted during pausable composition. They are now guaranteed to occur in order of `onDeactivate`/`onReuse`. ([I996e4](https://android-review.googlesource.com/#/q/I996e45fe97e2edbcceb776cf2fff009fe1b6ad8a), [b/404058957](https://issuetracker.google.com/issues/404058957))
- Fix dispatching of remember observers in pausable composition to avoid dispatching remembered/forgotten in the same apply ([I570b2](https://android-review.googlesource.com/#/q/I570b2436b95c7f8fb88a6f9824dbb9b8bccbc0fa), [b/404645679](https://issuetracker.google.com/issues/404645679), [b/407931790](https://issuetracker.google.com/issues/407931790))
- Switched `LifecycleRegistry` to unsafe mode in Compose Multiplatform to disable `MainThread` checks and fix threading issues. See [CMP-8227](https://youtrack.jetbrains.com/issue/CMP-8227/Support-LocalSavedStateRegistryOwner-locals-in-runtime-saveable) for details. ([Icee87](https://android-review.googlesource.com/#/q/Icee87874a5b186f5947d9fe97dd2ff67061359b3))

**External Contribution**

- Fixed a bug affecting Molecule users where using `RecompositionMode.Immediate` could cause missed recompositions. ([I9f3a9](https://android-review.googlesource.com/#/q/I9f3a9b3d879aef23a73eb4110f2efed6cca81dfa), [b/419527812](https://issuetracker.google.com/issues/419527812))
- Exposed `PausableComposition` `isApplied` and `isCancelled` getters which allow for checking the state of the `PausableComposition`. ([I994aa](https://android-review.googlesource.com/#/q/I994aa9f48fcdb5eeb551bc7db4cba917af408d23))
- Added `AnnotationTarget.FUNCTION` to the `FunctionKeyMeta` annotation. ([I08021](https://android-review.googlesource.com/#/q/I080216a2fde1be6d5f189608645e061a96fb83e6))

### Version 1.9.0-alpha04

June 4, 2025

`androidx.compose.runtime:runtime-*:1.9.0-alpha04` is released. Version 1.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/5fd8d5a2f883c1cdd7f712b200d5a4fedf342136..786176dc2284c87a0e620477608e0aca9adeff15/compose/runtime).

**API Changes**

- `SnapshotStateSet` now implements Parcelable on Android, it is now supported to be used as part `rememberSaveable { ... }`. ([I755dd](https://android-review.googlesource.com/#/q/I755dd7d20ed39545a1b7805b28b676fcff019fff), [b/378623803](https://issuetracker.google.com/issues/378623803))
- `SnapshotStateList` now implements Parcelable on Android, it is now supported to be used as part `rememberSaveable { ... }`. ([Id18be](https://android-review.googlesource.com/#/q/Id18be0bf1ad0bf5c7de580f5289629b838c76876), [b/378623803](https://issuetracker.google.com/issues/378623803))
- `movableContentOf()` is now marked with `@RememberInComposition` annotation, which allows lint to catch incorrect usages ([I2738d](https://android-review.googlesource.com/#/q/I2738d6889fdf3aea8a6017d30c8a8f53c7915e9d))
- Updated experimental composition observers API to allow for more comprehensive observation of recomposition causes ([I32b6a](https://android-review.googlesource.com/#/q/I32b6ac0ac3c4c584e03c755a1651b28882ae4a37))

**Bug Fixes**

- Fixed an ordering issue with the dispatching of `onForgotton` that could, for example, cause the `onDispose` of disposable effects to execute in the wrong order. ([Ic1c91](https://android-review.googlesource.com/#/q/Ic1c9127c3faf980e373eaa2c162a6cc49d55ff28), [b/417450712](https://issuetracker.google.com/issues/417450712))
- Fix for for reusing state handling in pausable composition ([Ife96e](https://android-review.googlesource.com/#/q/Ife96e7e011daa3644cdda2f112bbe7bbedb49ae4), [b/404058957](https://issuetracker.google.com/issues/404058957))
- Minor bug fix to make mutable collection detection compatible for both K1 and K2 ([Ie4878](https://android-review.googlesource.com/#/q/Ie48784d814683fa1a73ab7c41d3225fc84d3b14c))
- Minor bug fix to make annotation lookup on overridden property accessors compatible for both K1 and K2 ([I9900d](https://android-review.googlesource.com/#/q/I9900dbc6263666591db1dfe1c9d2ca21f26319f3))

**External Contribution**

- Fixed a bug affecting Molecule users where using `RecompositionMode.Immediate` could cause missed recompositions. ([I9f3a9](https://android-review.googlesource.com/#/q/I9f3a9b3d879aef23a73eb4110f2efed6cca81dfa), [b/419527812](https://issuetracker.google.com/issues/419527812))
- Exposed `PausableComposition` isApplied and `isCancelled` getters which allow for checking the state of the `PausableComposition`. ([I994aa](https://android-review.googlesource.com/#/q/I994aa9f48fcdb5eeb551bc7db4cba917af408d23))

### Version 1.9.0-alpha03

May 20, 2025

`androidx.compose.runtime:runtime-*:1.9.0-alpha03` is released. Version 1.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..5fd8d5a2f883c1cdd7f712b200d5a4fedf342136/compose/runtime).

**API Changes**

- Change `setDiagnosticStackTraceEnabled` to experimental to account for future development of this feature. ([I11db3](https://android-review.googlesource.com/#/q/I11db30dfc2e0922aa4da13bc9769ab33f3e94f65))

**Bug Fixes**

- Fixed the reusing state when a composition was paused and restarted but some previously paused state needed to be recomposed because some state it read changed while the composition was paused. ([I441d1](https://android-review.googlesource.com/#/q/I441d17b0bcca7b7073347a9b7cea89333cff2c93), [b/416209738](https://issuetracker.google.com/issues/416209738))
- Completed the pausable composition remember dispatch fix for issue b/404058957 previous fix was incomplete. ([I1afd4](https://android-review.googlesource.com/#/q/I1afd4981c6dadda8f61b02fe42d146f6f5d3c52e), [b/404058957](https://issuetracker.google.com/issues/404058957))
- `SaveableStateHolder.SaveableStateProvider` now provides a `LocalSavedStateRegistryOwner` to its content via composition. ([Ia2761](https://android-review.googlesource.com/#/q/Ia276100065156c4fa15d0d813cf5766302f26c82), [b/413108878](https://issuetracker.google.com/issues/413108878))
- `androidx.compose.runtime.saveable` now depends on `androidx.lifecycle.runtime.compose`. ([I53228](https://android-review.googlesource.com/#/q/I53228e5401011b619ac4cab06b2fa9cbadda6d09), [b/413108878](https://issuetracker.google.com/issues/413108878))

### Version 1.9.0-alpha02

May 7, 2025

`androidx.compose.runtime:runtime-*:1.9.0-alpha02` is released. Version 1.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4/compose/runtime).

**API Changes**

- Deprecated `rememberSaveable` with a custom 'key'. It bypasses positional scoping, leading to state bugs and inconsistent behavior (e.g., unintentional state sharing or loss, issues in nested `LazyLayouts`). Please remove the 'key' parameter to use positional scoping for consistent, locally-scoped state. See [the full commit message](https://r.android.com/3610053) for more details. ([I5e6ff](https://android-review.googlesource.com/#/q/I5e6ff7f527aafea4845f21a104500a902951fe10), [b/357685851](https://issuetracker.google.com/issues/357685851))

**Bug Fixes**

- `OffsetApplier` now correctly overrides `apply()` which was introduced with pausable composition. Not having this could cause pausable composition to throw throw an exception when updating virtual nodes. ([Idbf31](https://android-review.googlesource.com/#/q/Idbf314adbd64254dd4a4eb4e3a897930ece407c7), [b/409291131](https://issuetracker.google.com/issues/409291131))
- Fixed a deadlock that may affect Molecule users when a suspended call to `FrameClock.withFrameNanos` is cancelled while a frame is being dispatched. ([I89cab](https://android-review.googlesource.com/#/q/I89cab8e3eab14ed9a85b36e151f11b5f526a01fd), [b/407027032](https://issuetracker.google.com/issues/407027032))
- The Recomposer could go idle with movable content state still pending to be discarded. This normally does not occur as movable content state is discarded in the main loop of the Recomposer. However, this can occur in pausable composition when the movable content is discarded during `resume()`([Ie5416](https://android-review.googlesource.com/#/q/Ie54168320625f09c9390d542caa625f1f0d1d896), [b/409267170](https://issuetracker.google.com/issues/409267170))
- The order in which `onReuse` and `onDeactivate` could get inverted during pausable composition. They are now guaranteed to occur in order of `onDeactivate/onReuse`. ([I996e4](https://android-review.googlesource.com/#/q/I996e45fe97e2edbcceb776cf2fff009fe1b6ad8a), [b/404058957](https://issuetracker.google.com/issues/404058957))

### Version 1.9.0-alpha01

April 23, 2025

`androidx.compose.runtime:runtime-*:1.9.0-alpha01` is released. Version 1.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..008cbd021e3a2b4d1f36ea7f48200c4692bfc169/compose/runtime).

**Behavior Changes**

- Lint checks shipped with Compose now require a minimum AGP version of 8.8.2. If you are unable to upgrade AGP, you can instead upgrade Lint on its own by using `android.experimental.lint.version=8.8.2` (or a newer version) in your `gradle.properties`. To run Compose lint checks inside the IDE, Android Studio Ladybug or newer is required.

**API Changes**

- `currentCompositeKeyHash` is now deprecated. Use `currentCompositeKeyHashCode` instead. The replacement API encodes the same hash with more bits, which exponentially reduces the chance of two random unrelated groups in the composition hierarchy from having the same hash key. ([I4cb6a](https://android-review.googlesource.com/#/q/I4cb6a801d12447ac52bc92bb899ae84d69c4a6ed), [b/177562901](https://issuetracker.google.com/issues/177562901))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `@Stable`, `@Immutable`, and `@StableMarker` have been moved to runtime-annotation (in a compatible way). You can now depend on runtime-annotation if you want to use these annotations from libraries that do not depend on compose. ([I23a16](https://android-review.googlesource.com/#/q/I23a16a27aaacc1a17c181d821e4a6fdcef2ea882))
- Removes `onCreating` and `onDisposing` as they were deprecated and renamed to `onPreCreate` and `onPreDispose`. This change completes the rename. ([I97461](https://android-review.googlesource.com/#/q/I9746116d7374dfc845d2769b19a6fca5b3a2bb3f))
- Expose a composition local that allows to attach a compose stack trace based on a compose node location in composition. ([Ie0bda](https://android-review.googlesource.com/#/q/Ie0bdaffb43a46328057c31e7fc9db51a80789b5e), [b/354163858](https://issuetracker.google.com/issues/354163858))
- Introduce diagnostic Compose stack traces based on source information stored in composition. ([I3db9f](https://android-review.googlesource.com/#/q/I3db9fb976f61c768e2d1cf11d69019e4d0a08330), [b/354163858](https://issuetracker.google.com/issues/354163858))
- Deprecate `runWithTimingDisabled` in favor of `runWithMeasurementDisabled`, which more clearly describes the behavior - all metrics are paused. Additionally, expose the `MicrobenchmarkScope` superclass since redeclaring the `runWithMeasurementDisabled` function to open access isn't possible, since it's inline. ([I9e23b](https://android-review.googlesource.com/#/q/I9e23b0dfcff18f162ca0d2517734f3038870b59c), [b/389149423](https://issuetracker.google.com/issues/389149423), [b/149979716](https://issuetracker.google.com/issues/149979716))
- Adds `@FrequentlyChangingValue`: an annotation that can mark functions, and property getters, to indicate that they should not be called directly inside composition, as this may cause frequent recompositions. For example, to mark scroll position values and animating values. Warnings are provided by a corresponding lint check. ([I83630](https://android-review.googlesource.com/#/q/I836300029e0806b203ea3145426f4c079494482e), [b/234042500](https://issuetracker.google.com/issues/234042500))
- Adds `@RememberInComposition`: an annotation that can mark constructors, functions, and property getters, to indicate that they must not be called directly inside composition, without being remembered. Errors will be raised by a corresponding lint check. This annotation can be used to mark declarations that return stateful / mutable objects, objects whose identity is important to maintain across compositions, or objects that are expensive to instantiate and should be cached across compositions. ([Ie7db0](https://android-review.googlesource.com/#/q/Ie7db088c6d601b39d7f0bbb5f877f961108b6c47))
- Added a new `rememberSaveable` overload that supports `KSerializer` for type-safe state persistence using KotlinX Serialization. The existing `Saver`-based API remains supported. ([Iea4ab](https://android-review.googlesource.com/#/q/Iea4ab073ae8d62fac18069e072cf5a8d11ba31b8), [b/376028110](https://issuetracker.google.com/issues/376028110))

**Bug Fixes**

- Fix dispatching of remember observers in pausable composition to avoid dispatching remembered/forgotten in the same apply ([I570b2](https://android-review.googlesource.com/#/q/I570b2436b95c7f8fb88a6f9824dbb9b8bccbc0fa), [b/404645679](https://issuetracker.google.com/issues/404645679), [b/407931790](https://issuetracker.google.com/issues/407931790))
- Renamed `SnapshotObserver` methods onCreating to `onPreCreate` and `onDisposing` to `onPreDispose` to match API guidelines. The previous methods are deprecated and the new methods default to call the old ones so existing implementations of this interface will continue to work until the methods are removed. These methods will be removed in 1.9.0 alpha in a follow-up CL that will shortly follow this one. They will be removed from 1.8 beta before 1.8 stable. ([I6d753](https://android-review.googlesource.com/#/q/I6d753f73ac673337dcf5d35aa688b9dfc13ef24a))
- Fixed an issue where remembered values could incorrectly be forgotten and re-computed when recomposing an elided group that appears after a movable group ([I62cab](https://android-review.googlesource.com/#/q/I62cab3671fb6bf567e9f2c66996638247a8021f0), [b/383769314](https://issuetracker.google.com/issues/383769314))
- Added support for compose stack traces in `LaunchedEffect` and `rememberCoroutineScope` ([I705c0](https://android-review.googlesource.com/#/q/I705c0898bc527741d87cc9ff838016b87b14fb54), [b/354163858](https://issuetracker.google.com/issues/354163858))
- Compose lint checks now require a minimum AGP version of 8.8.2 from command line, and at least Android Studio Ladybug for IDE support. If you are using an older version of AGP, you can set `android.experimental.lint.version=8.8.2` in gradle.properties to upgrade the Lint version, without affecting AGP. ([I6f2a8](https://android-review.googlesource.com/#/q/I6f2a8816d93bc7d9d2a24658d69baa0900abf4c6))

**External Contribution**

- Added `AnnotationTarget.FUNCTION` to the `FunctionKeyMeta` annotation. ([I08021](https://android-review.googlesource.com/#/q/I080216a2fde1be6d5f189608645e061a96fb83e6))

## Version 1.8

### Version 1.8.3

June 18, 2025

`androidx.compose.runtime:runtime-*:1.8.3` is released. Version 1.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/754896be0859599f16ed264d79a04ee337bac777..13362f65a9c0649415fe57052ea0e3932d2303d1/compose/runtime).

### Version 1.8.2

May 20, 2025

`androidx.compose.runtime:runtime-*:1.8.2` is released. Version 1.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/018e42f9db74b5e4fce8007734de4da6ae087407..754896be0859599f16ed264d79a04ee337bac777/compose/runtime).

### Version 1.8.1

May 7, 2025

`androidx.compose.runtime:runtime-*:1.8.1` is released. Version 1.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9..018e42f9db74b5e4fce8007734de4da6ae087407/compose/runtime).

### Version 1.8.0

April 23, 2025

`androidx.compose.runtime:runtime-*:1.8.0` is released. Version 1.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b6bba717628c4c8c633c9509bfc4e4d9b89f428..d6d9afca3dfa73c1b9ea74daf9d6ad49c56fe0e9/compose/runtime).

### Version 1.8.0-rc03

April 9, 2025

`androidx.compose.runtime:runtime-*:1.8.0-rc03` is released. Version 1.8.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c0907800009c0cb37dd12c5586d620350c1975de..1b6bba717628c4c8c633c9509bfc4e4d9b89f428/compose/runtime).

### Version 1.8.0-rc02

March 26, 2025

`androidx.compose.runtime:runtime-*:1.8.0-rc02` is released. Version 1.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/071f2b22541efa1d5d528479b28aa42960923a4f..c0907800009c0cb37dd12c5586d620350c1975de/compose/runtime).

### Version 1.8.0-rc01

March 12, 2025

`androidx.compose.runtime:runtime-*:1.8.0-rc01` is released. Version 1.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/2d195d8376d369f4bf74652abe60101aa658bbcc..071f2b22541efa1d5d528479b28aa42960923a4f/compose/runtime).

**API Changes**

- Renamed `SnapshotObserver` methods onCreating to `onPreCreate` and `onDisposing` to `onPreDispose` to match API guidelines. The previous methods are deprecated and the new methods default to call the old ones so existing implementations of this interface will continue to work until the methods are removed. These methods will be removed in 1.9.0 alpha in a follow-up CL that will shortly follow this one. They will be removed from 1.8 beta before 1.8 stable. ([I6d753](https://android-review.googlesource.com/#/q/I6d753f73ac673337dcf5d35aa688b9dfc13ef24a))

### Version 1.8.0-beta03

February 26, 2025

`androidx.compose.runtime:runtime-*:1.8.0-beta03` is released. Version 1.8.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/08954f0d500d220e8d6af07b4e6c51090911f779..2d195d8376d369f4bf74652abe60101aa658bbcc/compose/runtime).

### Version 1.8.0-beta02

February 12, 2025

`androidx.compose.runtime:runtime-*:1.8.0-beta02` is released. Version 1.8.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5d82c9c8e72f3dd8c4ee71ff5ac9a1365d24de4..08954f0d500d220e8d6af07b4e6c51090911f779/compose/runtime).

**Bug Fixes**

- Rethrow caught exception in pausable composition .([384486d](https://android-review.googlesource.com/#/q/Ib01c8e75f9c32638fc658bf0ad9df01e103d8e89))

### Version 1.8.0-beta01

January 29, 2025

`androidx.compose.runtime:runtime-*:1.8.0-beta01` is released. Version 1.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c80a82c4ab50276ac6c1a8d9b9175c9fdbb0d1b8..80c9eca8dc00a6ae7188bf5f2beaf129b79de243/compose/runtime).

**API Changes**

- Fixes an issue where raising a throwable during composition that does not extend from Exception may lead to a 'Pending composition has not been applied' error. ([I356be](https://android-review.googlesource.com/#/q/I356be5d99df41138be790275807544b2d717050c), [b/382094412](https://issuetracker.google.com/issues/382094412))

### Version 1.8.0-alpha08

January 15, 2025

`androidx.compose.runtime:runtime-*:1.8.0-alpha08` is released. Version 1.8.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/compose/runtime).

### Version 1.8.0-alpha07

December 11, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha07` is released. Version 1.8.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6f09cf2ae979e48fdb19485f757a033e4a34bb82..46295bc0b75a16f452e8e0090e8de41073d4dbb6/compose/runtime).

**API Changes**

- Added tooling API that helps the layout inspector to correlate subcompositions to the parent composition in cases where a node is not used to bridge the compositions together. ([I4ce3d](https://android-review.googlesource.com/#/q/I4ce3da156737b5f18b5d9a8fffc73542a988b9cc))
- Made the arithmetic and special constants for `SnapshotId` internal instead of public. Arithmetic can be performed on a `SnasphotId`, if necessary, by converting it to a `Int` or `Long` by using `toInt()` or `toLong()` respectively. ([Ic3a57](https://android-review.googlesource.com/#/q/Ic3a57eed3968234376877c743a23dc13a127fbe0))

**External Contribution**

- Optimize storage for `movableContentOf` parameters. ([ed87177](https://android-review.googlesource.com/#/q/I1479f19a4e63bb4beae2921b66d274e5410abd22))

### Version 1.8.0-alpha06

November 13, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha06` is released. Version 1.8.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..6f09cf2ae979e48fdb19485f757a033e4a34bb82/compose/runtime).

**API Changes**

- Changes to the `PausableComposition` API. These breaking changes with respect to previous releases of 1.8.0-alpha (since 1.8.0-alpha02) but, as these are new APIs in 1.8.0, backwards compatibility is not maintained as the APIs are still in alpha. ([I39819](https://android-review.googlesource.com/#/q/I39819fd1a6509973a0008cd4fdec8a892829a301))
- Adds tooling APIs to observe the creation of new compositions within a Recomposer ([Iaeb7e](https://android-review.googlesource.com/#/q/Iaeb7e218aa949ebf1c061b311a3c4383cf5c2728))
- Added `snapshotId`, of type `Long`, to `Snapshot` and deprecated `id`. The ID of a snapshot changed from a `Int` to a `Long` to avoid the snapshot ID from overflowing on systems with very high frame rates and long running animations. The type was made expect/actual to allow this type to be `Int`, or other type, on platforms that don't have a native `Long` type. Platforms that do not have a native `Long`, such as JavaScript, should avoid high frame rates (over 1000 FPS) which would cause an overflow for `Int` approximate every 24 days. ([I38ac3](https://android-review.googlesource.com/#/q/I38ac3d43d3af7f691c957017eaf6895f5ae6ebb9), [b/374821679](https://issuetracker.google.com/issues/374821679))

**Bug Fixes**

- Fixed `providesDefault` for a single `provides`. ([aosp/3318540](https://android-review.googlesource.com/c/platform/frameworks/support/+/3318540) [b/374263387](https://issuetracker.google.com/issues/374263387))
- Optimize `ChangeList`. ([3318538](https://android-review.googlesource.com/c/platform/frameworks/support/+/3318538))

### Version 1.8.0-alpha05

October 30, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha05` is released. Version 1.8.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/compose/runtime).

**Bug Fixes**

- Fix stack overflow adding `Int.MAX_VALUE` to `SnapshotIdSet`. ([b/370536104](https://issuetracker.google.com/issues/370536104), [Ic4179f6](https://android-review.googlesource.com/#/q/Ic4179f629065874e23c597dbbf6575e751c16e34))
- Runtime micro-optimizations ([I50c60](https://android-review.googlesource.com/#/q/I50c60a20e43c5c816ed5f6f23d37c2470fa2ec88))
- Allow R8 to remove debugging runtimeCheck calls ([I8c44](https://android-review.googlesource.com/#/q/I8c441aa22f729e05651486265af9a2c0d9ee75b8))
- Make `compoundKeyOf` iterative instead of recursive ([I5817f](https://android-review.googlesource.com/#/q/I5817f443e766f85b874ccbdd11db16d20313f6df))

**External Contribution**

- Implement stacks with collection lists ([I7d47c](https://android-review.googlesource.com/#/q/I7d47c0a2850a5a166d045ccc6e8392b029ef7956))

### Version 1.8.0-alpha04

October 16, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha04` is released. Version 1.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/compose/runtime).

**Performance Improvements**

- Provide snapshot id for state records in constructor ([85c00f](https://android-review.googlesource.com/#/q/Iefb93e7ec256bac69e41dd37c15b6cfc61b51896))
- Refactor `SnapshotState***` to avoid class verification errors ([6ee4a6](https://android-review.googlesource.com/#/q/I61ad02d55b18bc1f4a636ef28a630df5614777c1))
- Fix R8 rules to prevent throw inlining ([5beb92](https://android-review.googlesource.com/#/q/I3d041cfcd9bd13c94c29a47b3f6d258f15537ba8))
- Micro-optimize Operations ([d73c5c](https://android-review.googlesource.com/#/q/I1b87da4dbad1e5954672f5eb437e9c2798f232a8))
- Optimize `SynchronizedObject` allocations on JVM ([2b043f](https://android-review.googlesource.com/#/q/I68cc15dce5682f4fd6873d6da52a2070dc42ec64))

### Version 1.8.0-alpha03

October 2, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha03` is released. Version 1.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/compose/runtime).

**Performance Improvements**

- Lazily create child context for `rememberCoroutineScope` ([f61464](https://android-review.googlesource.com/#/q/I6be8777ee40a52d1ca0d9f28f6c8ba687a6d5263))
  - `rememberCoroutineScope` is typically used to launch coroutines in response to events that happen post-composition. In some scenarios these events may never occur, leading to added costs of Job creation and cancellation without any benefit.
  - Make the scope returned by `rememberCoroutineScope` create its `coroutineContext` lazily when accessed, avoiding job creation and cancellation entirely if the scope is never used.

### Version 1.8.0-alpha02

September 18, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha02` is released. Version 1.8.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/80f82d37cb9b40250ee9eb15d9cbe9e93849355e..0431b84980e97d6bafdfda7c9038bc4d9529564f/compose/runtime).

**New Features**

- Added `PausableComposition` which allows creating a subcomposition that can be paused during composition and and applied asynchronously to the composition. Compiler support is required for pausing which is currently in development. ([I3394b](https://android-review.googlesource.com/#/q/I3394b7ebd90932ca451c7d55df7f286329de7656))

### Version 1.8.0-alpha01

September 4, 2024

`androidx.compose.runtime:runtime-*:1.8.0-alpha01` is released. Version 1.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..80f82d37cb9b40250ee9eb15d9cbe9e93849355e/compose/runtime).

## Version 1.7

### Version 1.7.8

February 12, 2025

`androidx.compose.runtime:runtime-*:1.7.8` is released. Version 1.7.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/456f991655af86d9ae121f7e93f8699f958fc7ac..215cdfd8cb9c0762dd0347c383250644057c367f/compose/runtime).

### Version 1.7.7

January 29, 2025

`androidx.compose.runtime:runtime-*:1.7.7` is released. No changes from 1.7.6.

`androidx.compose.runtime:runtime-*:1.7.6` is released. Version 1.7.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4cbf03b378a865660d8209d0229c2bb1928c6e33..5e65beadeb2e2c15f34d0fff72861847795cca4f/compose/runtime).

### Version 1.7.5

October 30, 2024

`androidx.compose.runtime:runtime-*:1.7.5` is released. Version 1.7.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6b0ae0e41147a8a917cab35b4a6487af4fce6ead..4cbf03b378a865660d8209d0229c2bb1928c6e33/compose/runtime).

### Version 1.7.4

October 16, 2024

`androidx.compose.runtime:runtime-*:1.7.4` is released. Version 1.7.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/00e91ed140ce2c4677f56fc06692b182b8a07fcf..6b0ae0e41147a8a917cab35b4a6487af4fce6ead/compose/runtime).

### Version 1.7.3

October 2, 2024

`androidx.compose.runtime:runtime-*:1.7.3` is released. Version 1.7.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9..00e91ed140ce2c4677f56fc06692b182b8a07fcf/compose/runtime).

### Version 1.7.2

September 18, 2024

`androidx.compose.runtime:runtime-*:1.7.2` is released. Version 1.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1efd0b233a17f707cd918993df1fa12e0bf9ae83..baa5cf7b949ae30f236d40b11ba88f9b0c8cffb9/compose/runtime).

### Version 1.7.1

September 10, 2024

- No changes to Android artifacts. `-desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts.

### Version 1.7.0

September 4, 2024

`androidx.compose.runtime:runtime-*:1.7.0` is released. Version 1.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d8995e2377dd4baad64b39becb6d480cadd05c86..38ffb9c315c3f894412184bda180c1b58b2a8556/compose/runtime).

**Important changes since 1.6.0**

- Added the ability to provide a composition local that is computed based on the values of other composition locals either by default, using `compositionLocalWithComputedDefault()` or by supplying a lambda to use to compute the value by using `providesComputed` instead of `provides`.
- The value of a composition local can be obtained by using the `currentValue` property of the composition local accessible from within the lambda computing the value. This is used instead of `current` which is only accessible in `@Composable` functions. ([Iadbc0](https://android-review.googlesource.com/#/q/Iadbc05f5ce04aeb1b67b53cff265b9017958947a))
- Newly created state objects are immediately accessible from other snapshots, including the global snapshot, with their initial state. Any subsequent modifications are not visible until the snapshot in which the object was created is applied.
- The initial state of `mutableStateOf()`, as well as their primitive versions, is the value passed in as a parameter to `mutableStateOf()`. The initial state of `mutableStateListOf()` and `mutableStateMapOf()` is empty.
- Added `Snapshot.isInSnapshot` and `Snapshot.PreexistingSnapshotId` that are used to enable a state object to support being immediately accessible from the global snapshot upon its creation.
- Custom state objects can support being immediately accessible by following the pattern of changes made to the built-in snapshot objects. ([I84a17](https://android-review.googlesource.com/#/q/I84a17f3cb84c7335a93b759b9eff908c487e83a8))
- Enable `nonSkippingGroupOptimization` for compose libraries. This causes the generated code for all non-restartable composable functions in androidx to be more efficient. In the future we plan to enable this by default. I([acbc08](https://android-review.googlesource.com/#/q/I486ef31e83f76763ffb3d3ca6ff78f04e7b0e465))
- Invalidate composable lambdas in subcompositions on the same frame. ([98301c](https://android-review.googlesource.com/#/q/I56bfb6fa98f05744587461158f933877aa8f64d4))
- Call `onRelease` callback in the same order as `onForgotten`. ([2cd790](https://android-review.googlesource.com/#/q/I0429d56ae6d02406fbc6f062d1c1ca040030ab09))
- Enable strong skipping mode ([ed1766](https://android-review.googlesource.com/#/q/I5e6a1ebb48f214f82a3f188b0810e0b6f7dba03e))
- Make `currentCompoundHashKey` unique in more cases ([d4a872](https://android-review.googlesource.com/#/q/I65507c0d4f5ac5d92db2619b284b1f3266c04e2f))

### Version 1.7.0-rc01

August 21, 2024

`androidx.compose.runtime:runtime-*:1.7.0-rc01` is released. Version 1.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98bc1cf10201a973793b72d2ff1ae728070e47e4..d8995e2377dd4baad64b39becb6d480cadd05c86/compose/runtime).

### Version 1.7.0-beta07

August 7, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta07` is released. Version 1.7.0-beta07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/16151cbc8a68e976da6f2b0f624c2e9883c55aa3..98bc1cf10201a973793b72d2ff1ae728070e47e4/compose/runtime).

### Version 1.7.0-beta06

July 24, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta06` is released. Version 1.7.0-beta06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8346df8de9f86a546fc9c316113bd4a3cc82ede9..16151cbc8a68e976da6f2b0f624c2e9883c55aa3/compose/runtime).

### Version 1.7.0-beta05

July 10, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta05` is released. Version 1.7.0-beta05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/487d2b07dba29c903cfd87a8dc7f99483084ebb6..8346df8de9f86a546fc9c316113bd4a3cc82ede9/compose/runtime).

### Version 1.7.0-beta04

June 26, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta04` is released. Version 1.7.0-beta04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c29f7383c14ede0af9cb64be9f3eee63714bc73c..487d2b07dba29c903cfd87a8dc7f99483084ebb6/compose/runtime).

### Version 1.7.0-beta03

June 12, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta03` is released. Version 1.7.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1a123f646cfea1599f9efead6da546b0c26063fa..c29f7383c14ede0af9cb64be9f3eee63714bc73c/compose/runtime).

### Version 1.7.0-beta02

May 29, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta02` is released. Version 1.7.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..1a123f646cfea1599f9efead6da546b0c26063fa/compose/runtime).

### Version 1.7.0-beta01

May 14, 2024

`androidx.compose.runtime:runtime-*:1.7.0-beta01` is released. Version 1.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/compose/runtime).

### Version 1.7.0-alpha08

May 1, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha08` is released. Version 1.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..06bfcd36801b67b9fe9b9bcae0d16a55e7d40fd7/compose/runtime).

### Version 1.7.0-alpha07

April 17, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha07` is released. Version 1.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/compose/runtime).

**New Features**

- Added the ability to provide a composition local that is computed based on the values of other composition locals either by default, using `compositionLocalWithComputedDefault()` or by supplying a lambda to use to compute the value by using `providesComputed` instead of `provides`.
- The value of a composition local can be obtained by using the `currentValue` property of the composition local accessible from within the lambda computing the value. This is used instead of `current` which is only accessible in `@Composable` functions. ([Iadbc0](https://android-review.googlesource.com/#/q/Iadbc05f5ce04aeb1b67b53cff265b9017958947a))

**API Changes**

- Newly created state objects are immediately accessible from other snapshots, including the global snapshot, with their initial state. Any subsequent modifications are not visible until the snapshot in which the object was created is applied.
- The initial state of `mutableStateOf()`, as well as their primitive versions, is the value passed in as a parameter to `mutableStateOf()`. The initial state of `mutableStateListOf()` and `mutableStateMapOf()` is empty.
- Added `Snapshot.isInSnapshot` and `Snapshot.PreexistingSnapshotId` that are used to enable a state object to support being immediately accessible from the global snapshot upon its creation.
- Custom state objects can support being immediately accessible by following the pattern of changes made to the built-in snapshot objects. ([I84a17](https://android-review.googlesource.com/#/q/I84a17f3cb84c7335a93b759b9eff908c487e83a8))

**Bug Fixes**

- Fixed merging of `readObserver` in nested snapshots. This caused nested derived states to under-invalidate when used inside a `snapshotFlow`. ([Idf138](https://android-review.googlesource.com/#/q/Idf1380c80ff9d651a930391c833ef3e403765afa))

### Version 1.7.0-alpha06

April 3, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha06` is released. Version 1.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a57d7d17753695012b58c9ce7ad55a8d39157e62..02b55f664eba38e42e362e1af3913be1df552d55/compose/runtime).

**Bug Fixes**

- Fix provide single values handling `providesDefault` ([538f45](https://android-review.googlesource.com/#/q/Ie91e0e0106aedafb03850a9a1bdf560bc0960d55))
- Avoid a deadlock in the Recomposer accessing the frame clock ([07e5c6](https://android-review.googlesource.com/#/q/Iff3f93b195b92adcc58210ae4a7f633bac390bb3))

### Version 1.7.0-alpha05

March 20, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha05` is released. Version 1.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..a57d7d17753695012b58c9ce7ad55a8d39157e62/compose/runtime).

**Bug Fixes**

- Clear late changes on deactivated composition ([5950bc](https://android-review.googlesource.com/#/q/I30694ea01cb64cd675c5542346b43cea67133bc9))

### Version 1.7.0-alpha04

March 6, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha04` is released. Version 1.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e1b82c49c59d8e976ce558aba5586f6c61bc9054..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/compose/runtime).

**Performance Improvements**

- Call `Snapshot.current` once per derived state evaluation ([ee7daf](https://android-review.googlesource.com/#/q/I56b506c51222ff15588e80e3090d3bc8731fcc99))
- Read `currentRecord` once per observation in composition ([b882b2](https://android-review.googlesource.com/#/q/Ie9b7e0b9d296802c38b0a1c91ab2cc9650aa71ea))
- Remove accidental iterator allocation in `snapshotFlow` ([231e56](https://android-review.googlesource.com/#/q/I45c7948014ee647de0532dd5727682d5a4fcc427))
- Enable `nonSkippingGroupOptimization` for compose libraries. This causes the generated code for all non-restartable composable functions in androidx to be more efficient. In the future we plan to enable this by default. I([acbc08](https://android-review.googlesource.com/#/q/I486ef31e83f76763ffb3d3ca6ff78f04e7b0e465))

### Version 1.7.0-alpha03

February 21, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha03` is released. [Version 1.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..e1b82c49c59d8e976ce558aba5586f6c61bc9054/compose/runtime)

**API Changes**

- Introduce a replace groups to improve detecting changes ([0941b5](https://android-review.googlesource.com/#/q/Iad90f02440e8f7c258ff493afa6cad1c6369be7a))

**Performance Improvements**

- Improve memory allocation when detecting changes ([53e7fd](https://android-review.googlesource.com/#/q/Ib4ce21c0506bc85d1ccb4902df0a97e4dfcea3d0))
- Fix a memory leak in the composer ([0e097d](https://android-review.googlesource.com/#/q/I6e69e17eff3332df140495ed6dbcfe561957f703))
- Use `ScopeMap` to pass invalidations when recomposing ([e19a7e](https://android-review.googlesource.com/#/q/I35e2a7829b358c1c5fc24d4b64f934af22fce89f))
- Optimize invalidations map to only keep derived states ([f11c44](https://android-review.googlesource.com/#/q/Iaa123305fa8e04484ef130f3bcbcafe0ac7eff02))
- Replace `IdentityArraySet` usages with `ScatterSet` ([db572e](https://android-review.googlesource.com/#/q/I6309be8c13581d67af664cfd5fa4298650c5ec8e))
- Optimize `removeScope` in `ScopeMap` ([bb0530](https://android-review.googlesource.com/#/q/If6cd7a2d1054ab2a6ab834f7a8ee37e0bcb2ee02))

### Version 1.7.0-alpha02

February 7, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha02` is released. [Version 1.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f..ca2a8cf8da3a3502fccc593974f8085653e38261/compose/runtime)

**Bug Fixes**

- Invalidate composable lambdas in subcompositions on the same frame. ([98301c](https://android-review.googlesource.com/#/q/I56bfb6fa98f05744587461158f933877aa8f64d4))
- Call `onRelease` callback in the same order as `onForgotten`. ([2cd790](https://android-review.googlesource.com/#/q/I0429d56ae6d02406fbc6f062d1c1ca040030ab09))
- Filter changed states that are not observed in `snapshotFlow`. ([796b80](https://android-review.googlesource.com/#/q/I5dee9640ea65854d17678f3672ad5efcd0b34b72))

**Performance Improvements**

- Modify snapshot observer in place when it is already transparent. ([f60f30](https://android-review.googlesource.com/#/q/I164e559b46fbafec67f10e06d851b664fe159503))
- Optimize `SnapshotIdSet.lowest()`. ([7ae149](https://android-review.googlesource.com/#/q/I418ec6b87b76ab85f4ff41b87cb2ba2a03b587b6))
- Use an allocation-free `fold()` in `SnapshotIdSet`. ([532b7d](https://android-review.googlesource.com/#/q/Ia0c807844305f6505867b007a2e9268f2bdf0b0d))
- Remove iterator allocation ([83f96b](https://android-review.googlesource.com/#/q/I7cbac6de6c91c1f272afcf086d977fbeae5cc0e7))

### Version 1.7.0-alpha01

January 24, 2024

`androidx.compose.runtime:runtime-*:1.7.0-alpha01` is released. [Version 1.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2b3fea6e026942389e9db59a4d68f2bb32c94e8f/compose/runtime)

**Performance Optimizations**

- Add the ability to create slots after a child group has been added ([b5960c](https://android-review.googlesource.com/#/q/I570eb93a9e588c5197853b53396102b10a777b0f))
- Optimize recording modifications of snapshot states ([28c3fe](https://android-review.googlesource.com/#/q/Id3f888de859e9ca4aa185879d766567e3bc87162))
- Enable strong skipping mode ([ed1766](https://android-review.googlesource.com/#/q/I5e6a1ebb48f214f82a3f188b0810e0b6f7dba03e))

**Bug Fixes**

- Account for default parameter meta in intrinsic remember ([096665](https://android-review.googlesource.com/#/q/I02d6b381ad96a3b5869c94180c32afe2984f8e89))
- Make `currentCompoundHashKey` unique in more cases ([d4a872](https://android-review.googlesource.com/#/q/I65507c0d4f5ac5d92db2619b284b1f3266c04e2f))
- Realize groups when exiting inline function call ([2a90fc](https://android-review.googlesource.com/#/q/I8a3906eadb951657c350e5ecf5b7597c4611e881))

## Version 1.6

### Version 1.6.8

June 12, 2024

`androidx.compose.runtime:runtime-*:1.6.8` is released. Version 1.6.8 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9a13a0e3b1197d66bfc19b9051576bc705f2c337..9dbbab668fd22cd643de4651197354a828aaa7b9/compose/runtime).

### Version 1.6.7

May 1, 2024

`androidx.compose.runtime:runtime-*:1.6.7` is released. Version 1.6.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a886cfe86852600d131eb7fa1ec8b7d0a8fc1e6b..9a13a0e3b1197d66bfc19b9051576bc705f2c337/compose/runtime).

### Version 1.6.6

April 17, 2024

`androidx.compose.runtime:runtime-*:1.6.6` is released. No changes since the last release.

### Version 1.6.5

April 3, 2024

`androidx.compose.runtime:runtime-*:1.6.5` is released. Version 1.6.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3..917ada96acf0ac343128c3f4af9bd67a4b80b99c/compose/runtime).

### Version 1.6.4

March 20, 2024

`androidx.compose.runtime:runtime-*:1.6.4` is released. Version 1.6.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/22b329dfa8888198eb3024650d236b3afe6c0907..1cbb6ee3e46f538bb2dc7ef6ce8e9c4b3cbc4dc3/compose/runtime).

### Version 1.6.3

March 6, 2024

`androidx.compose.runtime:runtime-*:1.6.3` is released. Version 1.6.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/af119e2e31de85654fb7b2e5a2c7e724231131fd..22b329dfa8888198eb3024650d236b3afe6c0907/compose/runtime).

### Version 1.6.2

February 21, 2024

`androidx.compose.runtime:runtime-*:1.6.2` is released. [Version 1.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f639ccf09a84fa5af4a9016fa239539aeed40b94..af119e2e31de85654fb7b2e5a2c7e724231131fd/compose/runtime)

### Version 1.6.1

February 7, 2024

`androidx.compose.runtime:runtime-*:1.6.1` is released. [Version 1.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf..f639ccf09a84fa5af4a9016fa239539aeed40b94/compose/runtime)

**Bug Fixes**

- Call `onRelease` callback in the same order as `onForgotten`. ([2cd790](https://android-review.googlesource.com/#/q/I0429d56ae6d02406fbc6f062d1c1ca040030ab09))
- Filter changed states that are not observed in `snapshotFlow`. ([796b80](https://android-review.googlesource.com/#/q/I5dee9640ea65854d17678f3672ad5efcd0b34b72))

### Version 1.6.0

January 24, 2024

`androidx.compose.runtime:runtime-*:1.6.0` is released. [Version 1.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/296c44d6ba03d2167bdea85d53e8387d7b1644f9..4c61c4d68d2bf0ccc61e316bc2a03754bb6979cf/compose/runtime)

**Important changes since 1.5.0**

**New Features**

- Re-throw exceptions that are swallowed during recomposition loop ([4dff9a](https://android-review.googlesource.com/#/q/I93d0b31d3d4a4b0298db5d604572761fad143464))

**Performance Optimizations**

- Optimize recording modifications of snapshot states ([28c3fe](https://android-review.googlesource.com/#/q/Id3f888de859e9ca4aa185879d766567e3bc87162))
- Optimize `rememberSaveable` ([f01d79](https://android-review.googlesource.com/#/q/Idb32853a52d502222acdd0c156bf9f8ed30cc352))
- Defer re-reading derived states until changes are recorded ([f38099](https://android-review.googlesource.com/#/q/I561cb932a478d3797a1ff8e2e59147ae505d47c1))
- Improve providing composition local values ([a337ea](https://android-review.googlesource.com/#/q/I5486fae04c873dac4947848e536446a97b6e13f9))

**Bug Fixes**

- Fix slot table memory leak ([73fcfe](https://android-review.googlesource.com/#/q/I21097e85475bc01da5297ca31161d04ecdc7547f))
- Skip recomposition of subcompositions that will be removed. ([Ieeb99](https://android-review.googlesource.com/#/q/Ieeb9919897a9f9b4274ddc77e66608a673cd1112), [b/254645321](https://issuetracker.google.com/issues/254645321))
- Only trigger `RememberObserver` lifecycles when it is stored in remember calculation. ([f6b4dc](https://android-review.googlesource.com/#/q/I9ef6f7f45b623079f0f394c7ba4943554fc29263))
- Restrict `$dirty` capture to inline lambdas. ([acfca0](https://android-review.googlesource.com/#/q/I67f435f73ba8c5e3c96bdd21e94827364a9b5a84))
- Fix moveable content sometimes receiving the wrong composition locals. ([035cd6](https://android-review.googlesource.com/#/q/I99bccb7c7ef6b60ea07512c1c4d25399f9dec58f))

### Version 1.6.0-rc01

January 10, 2024

`androidx.compose.runtime:runtime-*:1.6.0-rc01` is released. [Version 1.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc038a4bc84de9ab20493d6efa8d26f4a70214ae..6dc685be02316455881d22b69d0bb8adbe768c4f/compose/runtime)

### Version 1.6.0-beta03

December 13, 2023

`androidx.compose.runtime:runtime-*:1.6.0-beta03` is released. [Version 1.6.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/15c82aaef0f1fd0307d6c00061859e5b6c4384c6..fc038a4bc84de9ab20493d6efa8d26f4a70214ae/compose/runtime)

### Version 1.6.0-beta02

November 29, 2023

`androidx.compose.runtime:runtime-*:1.6.0-beta02` is released. [Version 1.6.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f80a6f0c1cb96288c04124001fa2c9bd29617d6..15c82aaef0f1fd0307d6c00061859e5b6c4384c6/compose/runtime)

### Version 1.6.0-beta01

November 15, 2023

`androidx.compose.runtime:runtime-*:1.6.0-beta01` is released. [Version 1.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..1f80a6f0c1cb96288c04124001fa2c9bd29617d6/compose)

**API Changes**

- Propagate Certain stability values in annotation. [(274a4c)](https://android-review.googlesource.com/#/q/Ib39a8b8d9a598a252ea7489686f264dab27b802a)

**Bug Fixes**

- Use referential policy for composition local scope state in context. [(83361c)](https://android-review.googlesource.com/#/q/I315f1c664890023342196659c5ff6eba2b70d553)
- Restrict $dirty capture to inline lambdas. [(acfca0)](https://android-review.googlesource.com/#/q/I67f435f73ba8c5e3c96bdd21e94827364a9b5a84)
- Fix moveable content sometimes receiving the wrong composition locals. [(035cd6)](https://android-review.googlesource.com/#/q/I99bccb7c7ef6b60ea07512c1c4d25399f9dec58f)
- Use faster non-allocating hashmaps in `RecomposeScopeImpl`. [(d79494)](https://android-review.googlesource.com/#/q/I7b4b55329003827c0555082a27d7d88d871efecd)
- Use `ObjectIntMap` in `DerivedState`. [(21862e)](https://android-review.googlesource.com/#/q/Ib10a28f4e870ddcc123716c1cfd2d0962c7ee945)
- Use `IntRef` for int `SnapshotThreadLocal` in `DerivedState`. [(04eaf4)](https://android-review.googlesource.com/#/q/I30b27c826147e51017d11e61a166912dfb7cf497)

### Version 1.6.0-alpha08

October 18, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha08` is released. [Version 1.6.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/compose/runtime)

**Bug Fixes**

- Only trigger `RememberObserver` lifecycles when it is stored in remember calculation. ([f6b4dc](https://android-review.googlesource.com/#/q/I9ef6f7f45b623079f0f394c7ba4943554fc29263))
- Improve allocations in invalidations list sorting. ([954d63](https://android-review.googlesource.com/#/q/Icfbd9eeafefc5a1c5467503bb3f0030904fffd69))
- Use new non-allocating maps in `SnapshotStateObserver`. ([4303ce](https://android-review.googlesource.com/#/q/Ie107e8ec8be2550f56ca86943cf292232f90b7eb))
- Clear invalidations when composition is deactivated. ([e001be](https://android-review.googlesource.com/#/q/I533e2012ba44c8918639a069a21e133bed349d51))

### Version 1.6.0-alpha07

October 4, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha07` is released. [Version 1.6.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f7407d4293384a1b91bc142880e3525048b3443/compose/runtime)

**API Changes**

- `SnapshotStateList` is now marked as `RandomAccess` to enable the direct indexing version of list helpers to be used. ([I5210c](https://android-review.googlesource.com/#/q/I5210ca5c0f490619381ecf93ac0b1ccb03071e36), [b/219554654](https://issuetracker.google.com/issues/219554654))

### Version 1.6.0-alpha06

September 20, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha06` is released. [Version 1.6.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..91bb8c1f81dcb031bda00fcd8e55f1e890b56f06/compose/runtime)

### Version 1.6.0-alpha05

September 6, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha05` is released. [Version 1.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/216f103fa4a5c7247f7bafc8bb3014616c265f0c..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/compose/runtime)

### Version 1.6.0-alpha04

August 23, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha04` is released. [Version 1.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..216f103fa4a5c7247f7bafc8bb3014616c265f0c/compose/runtime)

**New Features**

- Re-throw exceptions that are swallowed during recomposition loop ([4dff9a](https://android-review.googlesource.com/#/q/I93d0b31d3d4a4b0298db5d604572761fad143464))

**API Changes**

- Added a method to deactivate `ReusableComposition`, removing observations but keeping nodes in place. The deactivated composition can be activated again by calling `setContent`. ([Ib7f31](https://android-review.googlesource.com/#/q/Ib7f318c47b9e4cad19da5702ddd0ea69fc4fa827))
- Add `ReusableComposition` interface for managing lifecycle and reuse of subcompositions. ([I812d1](https://android-review.googlesource.com/#/q/I812d1fa36791857a04471882d5edabea1400c15e), [b/252846775](https://issuetracker.google.com/issues/252846775))

### Version 1.6.0-alpha03

August 9, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha03` is released. [Version 1.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..5d7dd999525725bd038a00ca4e89e0fef624a6da/compose/runtime)

**Bug Fixes**

- Fix new `CompositionLocalProvider` optimization ([3118e88](https://android-review.googlesource.com/#/q/I883c3ba691e41821944a3020eaa1089130cf11a3))
- Correct how movable content nodes are disassembled. ([5e3d59b](https://android-review.googlesource.com/#/q/I5a12f4174c5ec7cf9809dfae9ac61bfa8f454f4b))

### Version 1.6.0-alpha02

July 26, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha02` is released. [Version 1.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..4aed940027a19667e67d155563fc5fa8b7279313/compose/runtime)

**New Features \& Performance Enhancements**

- Optimize `rememberSaveable` ([f01d79](https://android-review.googlesource.com/#/q/Idb32853a52d502222acdd0c156bf9f8ed30cc352))
- Defer re-reading derived states until changes are recorded ([f38099](https://android-review.googlesource.com/#/q/I561cb932a478d3797a1ff8e2e59147ae505d47c1))
- Improve providing composition local values ([a337ea](https://android-review.googlesource.com/#/q/I5486fae04c873dac4947848e536446a97b6e13f9))
- `SideEffect` is marked as `@ExplicitGroupsComposable` to avoid generating a group. ([I74815](https://android-review.googlesource.com/#/q/I7481512ddcdfa2db575828225e2b81363bdf01ac))
- Avoid comparing composition local maps on reuse ([782071](https://android-review.googlesource.com/#/q/I098d5478ae8dadc9c5f0aa50f74ab99f3274a15d))

**API Changes**

- Added a special case overload for `CompositionLocalProviders` that avoids overhead used to make providing multiple values faster but is overhead when providing a single value. ([I6d640](https://android-review.googlesource.com/#/q/I6d640d97b96c26d9120c396063d84c73d947b852), [b/288169379](https://issuetracker.google.com/issues/288169379))

**Bug Fixes**

- Fix slot table memory leak ([73fcfe](https://android-review.googlesource.com/#/q/I21097e85475bc01da5297ca31161d04ecdc7547f))
- Fix how we restore `rememberSaveable` when `stateSaver` returns null ([90748c](https://android-review.googlesource.com/#/q/Ie51f499a7e2996cf509dbb340131f6b5a40fcf9c))

### Version 1.6.0-alpha01

June 21, 2023

`androidx.compose.runtime:runtime-*:1.6.0-alpha01` is released. [Version 1.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..3b5b931546a48163444a9eddc533489fcddd7494/compose/runtime)

**Bug Fixes**

- Skip recomposition of subcompositions that will be removed. ([Ieeb99](https://android-review.googlesource.com/#/q/Ieeb9919897a9f9b4274ddc77e66608a673cd1112), [b/254645321](https://issuetracker.google.com/issues/254645321))
- Reduced allocations when applying snapshots. ([I65c09](https://android-review.googlesource.com/#/q/I65c09492518269d6605a4731effd164d93be023a))
- Avoid calculating `readableHash` in `DerivedState` if snapshot wasn't modified ([68c565](https://android-review.googlesource.com/#/q/Iadb225542a94e5df2a59021696ad151eefa930c8))

## Version 1.5

### Version 1.5.4

October 18, 2023

`androidx.compose.runtime:runtime-*:1.5.4` is released. [Version 1.5.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4ed495b997a532cc4cbe39abdbaa98b8fc6f3764..b6d5e6e62e40f6938bdbcfef1d6c8a79e25006f8/compose/runtime)

### Version 1.5.3

October 4, 2023

`androidx.compose.runtime:runtime-*:1.5.3` is released. [Version 1.5.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2bc777611812ef8ef7329a332fbaf8348af05ec7..4ed495b997a532cc4cbe39abdbaa98b8fc6f3764/compose/runtime)

### Version 1.5.2

September 27, 2023

`androidx.compose.runtime:runtime-*:1.5.2` is released. [Version 1.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0a2cac855f7723e1e485c20ac68d34dc8bb68d1e..2bc777611812ef8ef7329a332fbaf8348af05ec7/compose/runtime)

### Version 1.5.1

September 6, 2023

`androidx.compose.runtime:runtime-*:1.5.1` is released. [Version 1.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65e3f15108d25a7e1c5c841c0855b21eca194070..824a15c9a34e9d13a5f58f4066029f0a784186b6/compose/runtime)

### Version 1.5.0

August 9, 2023

`androidx.compose.runtime:runtime-*:1.5.0` is released. [Version 1.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e423b92ad8e8707ff4031626131f05e33979eac8..65e3f15108d25a7e1c5c841c0855b21eca194070/compose/runtime)

**API Changes**

- Removed allocations in recomposition, color animations, and `AndroidComposeView`. ([Ib2bfa](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223))
- Added a `@StateFactoryMarker` annotation, to mark functions that create states and must be wrapped in a `remember` call. ([I64550](https://android-review.googlesource.com/#/q/I64550a0cb1647096260f00b75e7d35897878c617))
- Add primitive versions of State and `MutableState` ([fb3d89](https://android-review.googlesource.com/#/q/I48e438d0af15226217b77b2ba9a970c3219580bf))
- Added `Snapshot.isApplyObserverNotificationPending` ([I672a5](https://android-review.googlesource.com/#/q/I672a5c268230bfa1603341dd3327733faca5ca2a))
- Added primitive versions of the `State` API, allowing Int, Long, Float, and Double values to be tracked in `State` objects without incurring penalties for autoboxing. Use the new factory methods `mutableIntState(Int)`, `mutableFloatStateOf(Float)`, etc in order to use these. ([I48e43](https://android-review.googlesource.com/#/q/I48e438d0af15226217b77b2ba9a970c3219580bf))

**Bug Fixes**

- Skip recomposition of subcompositions that will be removed. ([Ieeb99](https://android-review.googlesource.com/#/q/Ieeb9919897a9f9b4274ddc77e66608a673cd1112), [b/254645321](https://issuetracker.google.com/issues/254645321))
- Don't retain snapshot reference in `ComposerImpl` ([0206f7](https://android-review.googlesource.com/q/commit:6f0e3949772ada45e2c376ce67a55380820206f7))
- Don't apply composition twice ([f5791b](https://android-review.googlesource.com/#/q/Ie64c91900541e39b0397e9c4141be92007291353))
- Ensure invalidation for non-initialized derived state values ([aa2a92](https://android-review.googlesource.com/#/q/I73d7888ac05f4adaa2128e01088288b7cf369fbd))
- Call `onEndChanges` during composition dispose. ([62cc8c](https://android-review.googlesource.com/#/q/I03ddce4062cbf7fb97f0447484ac46b0aedeab35))
- Fix moving content into a sub-composition ([4beb41](https://android-review.googlesource.com/#/q/Ic75f8dcaddc8c784f35f1884d662be04f084b455))
- Fix potential deadlocks ([c1a425](https://android-review.googlesource.com/#/q/Ie8b87caecabc88f6a6dd610805d964aed3489b85) and [8edce0](https://android-review.googlesource.com/#/q/I5cd5b2b3388758fef0826af619c680edce07d349))
- The recomposer created for an Android window will now only block calls to `withFrameNanos` instead of all composition when it receives an ON_STOP notification. This means windows associated with stopped activites will continue to recompose for data changes but the animations, or any other caller of `withFrameNanos`, will block. ([Id9e7f](https://android-review.googlesource.com/#/q/Id9e7fe262710544a48c2e4fc5fcbf1d27bfaa1ba), [b/240975572](https://issuetracker.google.com/issues/240975572))
- Execute deactivation callbacks for `LayoutNode` before disposing effects [3784073](https://android.googlesource.com/platform/frameworks/support/+/dfbea3ec8e88bf2a9a77c1bca0b02a8e2b8b0fa4)
- Fix changed flags for restarted lambdas [ea81df9](https://android.googlesource.com/platform/frameworks/support/+/9d9677ac37d963a7472698f23b63bd97e68a03e9)
- Fix live edit regression for Composable with nodes [73fd4d8](https://android.googlesource.com/platform/frameworks/support/+/2fc2bea6dbe7430e8add3d87e611cdeceadb309f)
- ON_STOP should pause the frame clock broadcasts instead of composition [ae276f1](https://android.googlesource.com/platform/frameworks/support/+/66fef38b1d11e0c48b11137e6c3d007909f4a2d1)
- Invalidate `SnapshotStateObserver` scopes for unchanged derived states [84d9b1c](https://android.googlesource.com/platform/frameworks/support/+/c5d22e7f422942f83a8649e0dec0a5546141c52d)
- Fix potential dead-lock when disposing compositions [28761fc](https://android.googlesource.com/platform/frameworks/support/+/59526cdd95681694b310ae874ec2b1ad198edce0)
- Fix moving content into a sub-composition [92d4156](https://android.googlesource.com/platform/frameworks/support/+/803754d2519a47c1aec0b1a0f1b058f1024beb41)
- Fix changed flags for restarted lambdas ([8a03e9](https://android-review.googlesource.com/#/q/I203ec51beb7fc8c09eb536fa435ea2f8203f046c))
- Execute deactivation callbacks for `LayoutNode` before disposing effects ([8b0fa4](https://android-review.googlesource.com/#/q/I5957617e9f15af8d581b5cf304f5312bba310169))
- Fix `endToMarker()` when ending node groups. ([d71d980](https://android-review.googlesource.com/#/q/Ibe7063cf22f4bff6eda5bde05c37c1e665c09167))
- Use current `SlotWriter` group for check on deactivation ([a0b518b](https://android-review.googlesource.com/#/q/Ief210ba5d2e20734277d58ae6b5916db2c92e8db))
- Remove the `fill` in `SlotTable.moveSlotGapTo()` and move it to close ([81f9935](https://android-review.googlesource.com/#/q/Iccc23740ba06a0aa952a5f6f52999de247ce62c5))
- Fix missing invalidations while movable content is moving ([1d7c024](https://android-review.googlesource.com/#/q/Ic487b8f797a2862effc07d2ef020d8461717940e))
- Fix immediate invalidations for moved movable content ([8676618](https://android-review.googlesource.com/#/q/I4d23a4f5745782ae65c1e0186579842d73bdbddb))

**Performance Improvements**

- Avoid calculating `readableHash` in `DerivedState` if snapshot wasn't modified. ([307102](https://android-review.googlesource.com/#/q/Iadb225542a94e5df2a59021696ad151eefa930c8))
- Reduced allocations ([I65c09](https://android-review.googlesource.com/#/q/I65c09492518269d6605a4731effd164d93be023a), [d7ea77](https://android-review.googlesource.com/q/commit:55a39a86b2af2221eee79db32036cb649bd7ea77), [727974](https://android-review.googlesource.com/#/q/Ifc5a47a41da8c75409d987c84f672f6cc8a82682), and [445808](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223) )
- Quick cancellation of compose `CoroutineScopes` ([a55362](https://android-review.googlesource.com/#/q/I2fbb777cbdab880f062584ae86ce69e89e9a9cf0) and [bd382f](https://android-review.googlesource.com/#/q/I8fbb9904408dff4dd694f24d8a5effb7d16ed2c4))
- Overwrite records of state objects with inaccessible state records ([c986960](https://android-review.googlesource.com/#/q/I9e793b3285b5102392cea30f72ed1583e798b810))
- Use composer of the correct scope when realizing groups ([9a5e5b6](https://android-review.googlesource.com/#/q/I0cc3c7be151edb7cbbe4114fffbde8736f7ec428))
- Use `IdentityArraySet` to store snapshot invalidations ([7f60cca](https://android-review.googlesource.com/#/q/I476e3c43cabd165ad8edce928aa3b46c06952779))
- Reduce allocations for snapshot observations ([5bc535f](https://android-review.googlesource.com/#/q/I72da3303b1b7ea0d02324cf85f10023cdc97b564))

### Version 1.5.0-rc01

July 26, 2023

`androidx.compose.runtime:runtime-*:1.5.0-rc01` is released. [Version 1.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/81e6706c269471032b283755131d2aa4e8821a89..e423b92ad8e8707ff4031626131f05e33979eac8/compose)

**Bug Fixes**

- Defer re-reading derived states until changes are recorded ([f38099](https://android-review.googlesource.com/q/commit:14aa10be879adb028eb48b60af6de11bfdf38099))

- An optional inspection to recommend migrating `mutableStateOf()` calls to their corresponding specialized types for primitives is available. Its lint ID is `AutoboxingStateCreation`. Previously, this inspection was enabled by default for all projects. To see this warning in Android Studio's editor and your project's lint outputs, change its severity from informational to warning (or higher) by declaring `warning "AutoboxingStateCreation"` inside your module's build.gradle or build.gradle.kts configuration as shown ([I34f7e](https://android-review.googlesource.com/#/q/I34f7ea540f782ae95630f7f94cab93d842dfdd0f)):

          android {
              lint {
                  warning "AutoboxingStateCreation"
              }
              ...
          }

### Version 1.5.0-beta03

June 28, 2023

`androidx.compose.runtime:runtime-*:1.5.0-beta03` is released. [Version 1.5.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9eb2d144f9209cb9c4205ad1f981eb7ddf29b96e..24dc7b0781cb908b2385ec207ca1b3a72cb90093/compose/runtime)

**Bug Fixes**

- Skip recomposition of subcompositions that will be removed. ([Ieeb99](https://android-review.googlesource.com/#/q/Ieeb9919897a9f9b4274ddc77e66608a673cd1112), [b/254645321](https://issuetracker.google.com/issues/254645321))

### Version 1.5.0-beta02

June 7, 2023

`androidx.compose.runtime:runtime-*:1.5.0-beta02` is released. [Version 1.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d26ca4055c940126ae1663ad0d54aafd23205ea4..df792c9ff86d87f538bab5d7f9dd9f56e2437b15/compose/runtime)

**Performance Improvements**

- Avoid calculating `readableHash` in `DerivedState` if snapshot wasn't modified. ([307102](https://android-review.googlesource.com/#/q/Iadb225542a94e5df2a59021696ad151eefa930c8))

### Version 1.5.0-beta01

May 24, 2023

`androidx.compose.runtime:runtime-*:1.5.0-beta01` is released. [Version 1.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..d26ca4055c940126ae1663ad0d54aafd23205ea4/compose/runtime)

**API Changes**

- Removed allocations in recomposition, color animations, and `AndroidComposeView` ([Ib2bfa](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223))
- Added a `@StateFactoryMarker` annotation, to mark functions that create states and must be wrapped in a `remember` call. ([I64550](https://android-review.googlesource.com/#/q/I64550a0cb1647096260f00b75e7d35897878c617))
- Add primitive versions of State and `MutableState` ([fb3d89](https://android-review.googlesource.com/#/q/I48e438d0af15226217b77b2ba9a970c3219580bf))
- Added `Snapshot.isApplyObserverNotificationPending` ([I672a5](https://android-review.googlesource.com/#/q/I672a5c268230bfa1603341dd3327733faca5ca2a))

**Bug Fixes**

- Reduced allocations ([I65c09](https://android-review.googlesource.com/#/q/I65c09492518269d6605a4731effd164d93be023a), [d7ea77](https://android-review.googlesource.com/q/commit:55a39a86b2af2221eee79db32036cb649bd7ea77), [727974](https://android-review.googlesource.com/#/q/Ifc5a47a41da8c75409d987c84f672f6cc8a82682), and [445808](https://android-review.googlesource.com/#/q/Ib2bfaf0af40bc0970424f86141ae24607a2b1223) )
- Don't retain snapshot reference in `ComposerImpl` ([0206f7](https://android-review.googlesource.com/q/commit:6f0e3949772ada45e2c376ce67a55380820206f7))
- Quick cancellation of compose `CoroutineScopes` ([a55362](https://android-review.googlesource.com/#/q/I2fbb777cbdab880f062584ae86ce69e89e9a9cf0) and [bd382f](https://android-review.googlesource.com/#/q/I8fbb9904408dff4dd694f24d8a5effb7d16ed2c4))
- Don't apply composition twice ([f5791b](https://android-review.googlesource.com/#/q/Ie64c91900541e39b0397e9c4141be92007291353))
- Ensure invalidation for non-initialized derived state values ([aa2a92](https://android-review.googlesource.com/#/q/I73d7888ac05f4adaa2128e01088288b7cf369fbd))
- Call `onEndChanges` during composition dispose. ([62cc8c](https://android-review.googlesource.com/#/q/I03ddce4062cbf7fb97f0447484ac46b0aedeab35))
- Fix moving content into a sub-composition ([4beb41](https://android-review.googlesource.com/#/q/Ic75f8dcaddc8c784f35f1884d662be04f084b455))
- Fix potential deadlocks ([c1a425](https://android-review.googlesource.com/#/q/Ie8b87caecabc88f6a6dd610805d964aed3489b85%5D%20and%20%5B8edce0%5D(https://android-review.googlesource.com/#/q/I5cd5b2b3388758fef0826af619c680edce07d349))
- ON_STOP should pause the frame clock broadcasts instead of composition ([f4a2d1](https://android-review.googlesource.com/#/q/Id9e7fe262710544a48c2e4fc5fcbf1d27bfaa1ba))
- Fix changed flags for restarted lambdas ([8a03e9](https://android-review.googlesource.com/#/q/I203ec51beb7fc8c09eb536fa435ea2f8203f046c))
- Execute deactivation callbacks for `LayoutNode` before disposing effects ([8b0fa4](https://android-review.googlesource.com/#/q/I5957617e9f15af8d581b5cf304f5312bba310169))

**External Contribution**

- Added `Snapshot.isApplyObserverNotificationPending` ([I672a5](https://android-review.googlesource.com/#/q/I672a5c268230bfa1603341dd3327733faca5ca2a))

### Version 1.5.0-alpha04

May 10, 2023

`androidx.compose.runtime:runtime-*:1.5.0-alpha04` is released. [Version 1.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/01bd392d5702480f8bfe61a8f8bbbea64cf362a0..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/compose/runtime)

**API Changes**

- Added primitive versions of the `State` API, allowing Int, Long, Float, and Double values to be tracked in `State` objects without incurring penalties for autoboxing. Use the new factory methods `mutableIntState(Int)`, `mutableFloatStateOf(Float)`, etc in order to use these. ([I48e43](https://android-review.googlesource.com/#/q/I48e438d0af15226217b77b2ba9a970c3219580bf))

**Bug Fixes**

- Call `onEndChanges` during composition dispose. Focus nodes removed during `Composition.dispose` are subscribing to `onEndChanges` to reset focus.([03d4a47](https://android-review.googlesource.com/#/q/I03ddce4062cbf7fb97f0447484ac46b0aedeab35))

- Ensure invalidation for non-initialized derived state values. Each derived state is associated with a list of its dependencies in `SnapshotStateObserver`, used to invalidate scopes associated with derived state whenever dependency changes. The dependency change is registered on snapshot advance, which can happen after derived state read (due to the call to `Snapshot.notifyObjectsInitialized()`).

  Previous derived state observation logic in `SnapshotStateObserver` was cleaning up old dependencies, then reading new value. This resulted in a race condition with invalidation happening in a cleaned up state, where dependency invalidation wasn't registered.

  This change reorders derived state read and dependency cleanup, ensuring that invalidation always happens in a valid state. ([c472be6](https://android-review.googlesource.com/#/q/I73d7888ac05f4adaa2128e01088288b7cf369fbd))

### Version 1.5.0-alpha03

April 19, 2023

`androidx.compose.runtime:runtime-*:1.5.0-alpha03` is released. [Version 1.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..01bd392d5702480f8bfe61a8f8bbbea64cf362a0/compose/runtime)

**API Changes**

- The recomposer created for an Android window will now only block calls to `withFrameNanos` instead of all composition when it receives an ON_STOP notification. This means windows associated with stopped activites will continue to recompose for data changes but the animations, or any other caller of `withFrameNanos`, will block. ([Id9e7f](https://android-review.googlesource.com/#/q/Id9e7fe262710544a48c2e4fc5fcbf1d27bfaa1ba), [b/240975572](https://issuetracker.google.com/issues/240975572))

**Bug Fixes**

- Fix potential deadlock in snapshot list and map [5c1a425](https://android.googlesource.com/platform/frameworks/support/+/5e7f64d97283fb2be1db3f0d5c6dcd1a55c1a425)
- Execute deactivation callbacks for `LayoutNode` before disposing effects [3784073](https://android.googlesource.com/platform/frameworks/support/+/dfbea3ec8e88bf2a9a77c1bca0b02a8e2b8b0fa4)
- Fix changed flags for restarted lambdas [ea81df9](https://android.googlesource.com/platform/frameworks/support/+/9d9677ac37d963a7472698f23b63bd97e68a03e9)
- Fix live edit regression for Composable with nodes [73fd4d8](https://android.googlesource.com/platform/frameworks/support/+/2fc2bea6dbe7430e8add3d87e611cdeceadb309f)
- ON_STOP should pause the frame clock broadcasts instead of composition [ae276f1](https://android.googlesource.com/platform/frameworks/support/+/66fef38b1d11e0c48b11137e6c3d007909f4a2d1)
- Invalidate `SnapshotStateObserver` scopes for unchanged derived states [84d9b1c](https://android.googlesource.com/platform/frameworks/support/+/c5d22e7f422942f83a8649e0dec0a5546141c52d)
- Fix potential dead-lock when disposing compositions [28761fc](https://android.googlesource.com/platform/frameworks/support/+/59526cdd95681694b310ae874ec2b1ad198edce0)
- Fix moving content into a sub-composition [92d4156](https://android.googlesource.com/platform/frameworks/support/+/803754d2519a47c1aec0b1a0f1b058f1024beb41)

### Version 1.5.0-alpha02

April 5, 2023

`androidx.compose.runtime:runtime-*:1.5.0-alpha02` is released. [Version 1.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..a200cb82769634cecdb118ec4f0bfdf0b086e597/compose/runtime)

**New Features**

- Kotlin's `getValue` operator can now be composable ([f174f6e](https://android-review.googlesource.com/#/q/Ib40ff82e608811673f64d80d2accd5121e8a4b7c))

**Bug Fixes, Performance Improvements**

- Overwrite records of state objects with inaccessible state records ([c986960](https://android-review.googlesource.com/#/q/I9e793b3285b5102392cea30f72ed1583e798b810))
- Use composer of the correct scope when realizing groups ([9a5e5b6](https://android-review.googlesource.com/#/q/I0cc3c7be151edb7cbbe4114fffbde8736f7ec428))
- Fix `endToMarker()` when ending node groups. ([d71d980](https://android-review.googlesource.com/#/q/Ibe7063cf22f4bff6eda5bde05c37c1e665c09167))
- Use current `SlotWriter` group for check on deactivation ([a0b518b](https://android-review.googlesource.com/#/q/Ief210ba5d2e20734277d58ae6b5916db2c92e8db))
- Use `IdentityArraySet` to store snapshot invalidations ([7f60cca](https://android-review.googlesource.com/#/q/I476e3c43cabd165ad8edce928aa3b46c06952779))
- Remove the `fill` in `SlotTable.moveSlotGapTo()` and move it to close ([81f9935](https://android-review.googlesource.com/#/q/Iccc23740ba06a0aa952a5f6f52999de247ce62c5))
- Fix missing invalidations while movable content is moving ([1d7c024](https://android-review.googlesource.com/#/q/Ic487b8f797a2862effc07d2ef020d8461717940e))
- Fix immediate invalidations for moved movable content ([8676618](https://android-review.googlesource.com/#/q/I4d23a4f5745782ae65c1e0186579842d73bdbddb))
- Reduce allocations for snapshot observations ([5bc535f](https://android-review.googlesource.com/#/q/I72da3303b1b7ea0d02324cf85f10023cdc97b564))

### Version 1.5.0-alpha01

March 22, 2023

`androidx.compose.runtime:runtime-*:1.5.0-alpha01` is released. [Version 1.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce5f1f96b304c7952d07c5bb472112c4b0ee2312..5e7d256f82fbafb6d059ab7b18fddd87c7531553/compose/runtime)

**New Features**

- Adds `Modifier.Node#coroutineScope` to allow `Modifier.Nodes` to launch coroutines ([I76ef9](https://android-review.googlesource.com/#/q/I76ef9c67fb270c8d6ba4f7ccfd5379fdf7d2db69))
- Allow `Modifier.Nodes` to read `CompositionLocals` by implementing the `CompositionLocalConsumerModifierNode` interface. ([Ib44df](https://android-review.googlesource.com/#/q/Ib44df147ceaad520c9102c416440d20fadadc403))

## Version 1.4

### Version 1.4.3

May 3, 2023

`androidx.compose.runtime:runtime-*:1.4.3` is released with no changes.

### Version 1.4.2

April 19, 2023

`androidx.compose.runtime:runtime-*:1.4.2` is released. [Version 1.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5..0872f930da585f7fbf6e17c74b1dc42045e8b2c6/compose/runtime)

**Bug Fixes**

- Fix potential deadlock in snapshot list and map [2eb6570](https://android.googlesource.com/platform/frameworks/support/+/2eb65706778b66e205a414e96365b9e267f5c3ce)

- Adding content to a `SnapshotStateList` or `SnapshotStateMap` can encounter a deadlock if the modification is concurrent with a direct write to the state record. This was made significantly more likely to be encountered with the changes introduced by [93fcae828b](https://android-review.googlesource.com/#/q/I9e793b3285b5102392cea30f72ed1583e798b810) that uses direct writes to release unused records.

- The locks are now ordered in that a snapshot lock is never attempted to be taken when a map or list lock is held.

### Version 1.4.1

April 5, 2023

`androidx.compose.runtime:runtime-*:1.4.1` is released. [Version 1.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c13b30cf6683e0a43585416f30b55e07bf2b560e..5dcb085369a3574f1b09eaaf2a58ee0ea01c22d5/compose/runtime)

**Bug Fixes**

- Fix `endToMarker()` when ending node groups. [d71d980](https://android-review.googlesource.com/#/q/Ibe7063cf22f4bff6eda5bde05c37c1e665c09167)

### Version 1.4.0

March 22, 2023

`androidx.compose.runtime:runtime-*:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..c5b142d6ab0494c996b2378d5008ac1cd6da75f3/compose/runtime)

**Important changes since 1.3.0**

- Use initialized value from `LiveData` for first composition [3680e25](https://android-review.googlesource.com/c/platform/frameworks/support/+/2433877)
- Add `ComposeNodeLifecycleCallback` to observe lifecycle of compose nodes. [8b6a258](https://android-review.googlesource.com/c/platform/frameworks/support/+/2392879)
- Add `parameterTypes` property to `ComposableMethod` [7b6c7ad](https://android-review.googlesource.com/c/platform/frameworks/support/+/2285054)

**Bug Fixes \& Performance Improvements**

- Clear both scope indexes in `SnapshotStateObserver` [29f4a3e](https://android-review.googlesource.com/c/platform/frameworks/support/+/2450646)
- Add groups needed in the body of unskippable lambdas [7d06752](https://android-review.googlesource.com/c/platform/frameworks/support/+/2418924)
- Improve memory reference characteristics of Snapshot state [93fcae8](https://android-review.googlesource.com/c/platform/frameworks/support/+/2366970)
- Remove boxing in composition local lookups [0875717](https://android-review.googlesource.com/c/platform/frameworks/support/+/2393022)
- Use correct key for non-reusable nodes groups [6388d8d](https://android-review.googlesource.com/c/platform/frameworks/support/+/2375738)
- Protect `SnapshotStateObserver` from recursive and concurrent applies [98cb6ba](https://android-review.googlesource.com/c/platform/frameworks/support/+/2360799)
- Added a check-index-bounds check in the `IdentityArraySet` "get" method [35a77d3](https://android-review.googlesource.com/c/platform/frameworks/support/+/2325197)
- Update compose module to use `ViewTreeLifecycleOwner` extensions [21c2122](https://android-review.googlesource.com/c/platform/frameworks/support/+/2321999)
- Send apply notifications after Recomposer finishes frame. [98f2641](https://android-review.googlesource.com/c/platform/frameworks/support/+/2296013)
- Fix index out of bounds crash when cancelling the Recomposer [8f8656f](https://android-review.googlesource.com/c/platform/frameworks/support/+/2305731)
- Always force recompose if parent providers of Composition have changed [9526fcc](https://android-review.googlesource.com/c/platform/frameworks/support/+/2292300)
- Recomposer tolerance for cancelled Jobs [a55f7ed](https://android-review.googlesource.com/c/platform/frameworks/support/+/2267995)
- Improve handling invalidations for large number of composers [9b7ed67](https://android-review.googlesource.com/c/platform/frameworks/support/+/2258823)
- Fix generating closing groups for non-local returns [b6f590c](https://android-review.googlesource.com/c/platform/frameworks/support/+/2174652)

### Version 1.4.0-rc01

March 8, 2023

`androidx.compose.runtime:runtime-*:1.4.0-rc01` is released. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/87533b4ff06971ed59028936cd9b6da988cd4522..6022301db806601f282c53b8cbb5a981923a1589/compose/runtime)

**Bug Fixes**

- [Clear both scope indexes in `SnapshotStateObserver`](https://android.googlesource.com/platform/frameworks/support/+/29f4a3ef8c36a1af7ea4f1d35e669e1d19fe4b23)

### Version 1.4.0-beta02

February 22, 2023

`androidx.compose.runtime:runtime:1.4.0-beta02` and `androidx.compose.runtime:runtime-saveable:1.4.0-beta02` are released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f7337eab774a6ce3b17367d5f31708564b66e677..87533b4ff06971ed59028936cd9b6da988cd4522/compose/runtime)

### Version 1.4.0-beta01

February 8, 2023

`androidx.compose.runtime:runtime-*:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..f7337eab774a6ce3b17367d5f31708564b66e677/compose/runtime)

**API Changes**

- `ComposeNodeLifecycleCallback` was added which allows to observe lifecycle of Compose nodes ([I3731b](https://android-review.googlesource.com/#/q/I3731b3face6bf8c4a9646dff7c22055a1a999620))
- Added `@TestOnly` to `Composer.disableSourceInformation()` as this function is only safe to call in a test. ([I896c8](https://android-review.googlesource.com/#/q/I896c84a91e1ec01f0107c52def0900196e2cde45))

**Bug Fixes**

- Remove boxing in composition local lookups ([62f66a](https://android-review.googlesource.com/#/q/I178a48a0643f8ed5d498014cf43c9063b146c66c))
- Improve memory reference characteristics of Snapshot state ([dfb451](https://android-review.googlesource.com/#/q/I04ff2e1b8766615590908bafb79fda135744c506))

### Version 1.4.0-alpha05

January 25, 2023

`androidx.compose.runtime:runtime:1.4.0-alpha05` and `androidx.compose.runtime:runtime-saveable:1.4.0-alpha05` are released. [Version 1.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/compose/runtime)

**API Changes**

- More type/nullability of inline/deprecated-hidden functions ([I24f91](https://android-review.googlesource.com/#/q/I24f91d55dabdd4f7ee05b8a679a4e928acc95d6d))

### Version 1.4.0-alpha04

January 11, 2023

`androidx.compose.runtime:runtime-*:1.4.0-alpha04` is released. [Version 1.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/047e199bdcb8a5cd744cc7a2f986631bfb350ec7..adf1c279a86ab3886e1666c08e2c3efba783367b/compose/runtime)

**API Changes**

- `TestMonotonicFrameClock` now uses correct experimental annotation. ([I95c9e](https://android-review.googlesource.com/#/q/I95c9efb389cad81cb9182ff83910f53c7a99c239))

**Bug Fixes**

- Protect `SnapshotStateObserver` from recursive and concurrent applies ([d902fb](https://android-review.googlesource.com/#/q/I5556dd8624dd008bfc49431dc8de02c8e0578e68))

### Version 1.4.0-alpha03

December 7, 2022

`androidx.compose.runtime:runtime-*:1.4.0-alpha03` is released. [Version 1.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a1e318590b217ecfce1b2de17eed2f18b6a680bb..047e199bdcb8a5cd744cc7a2f986631bfb350ec7/compose/runtime)

**API Changes**

- adding a new public method to `ComposableMethod` class analogous to `java.lang.reflect.Method#getParameterTypes()` ([Iab0c3](https://android-review.googlesource.com/#/q/Iab0c3375bb20c9831512f1aa3c63eab8f2a46209))

**Bug Fixes**

- Snapshot apply notifications are now sent after the `Recomposer` finishes applying changes. ([Iad6c0](https://android-review.googlesource.com/#/q/Iad6c0dcd163a5a8f9c5aec426da3d4f701ca509f), [b/222093277](https://issuetracker.google.com/issues/222093277))

### Version 1.4.0-alpha02

November 9, 2022

`androidx.compose.runtime:runtime-*:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..a1e318590b217ecfce1b2de17eed2f18b6a680bb/compose/runtime)

### Version 1.4.0-alpha01

October 24, 2022

`androidx.compose.runtime:runtime-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6ab75d133443eb5c1d92f910f625741041fc591..548c8ac2570ae6cf15798fea1380491f7d93796b/compose/runtime)

**API Changes**

- `SnapshotStateList` and `SnapshotStateMap` now have explicit implementaions of `toList()` and `toMap()`, respectfully. These methods return their current content without peforming a copy as they return the internal immutable data used to store their content. This value can be used, for example, to produce a flow of values using `snapshotFlow` without requiring copying of the data. ([Ica2bd](https://android-review.googlesource.com/#/q/Ica2bd64be73862b8497bf756c5b0537987d691e5))

## Version 1.3

### Version 1.3.3

January 11, 2023

`androidx.compose.runtime:runtime-*:1.3.3` is released. [Version 1.3.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8476d588d4975cb86be01bf4e356c5605ad89d48..59e93356f8f2bfb40b6f56dc086c8b821bbebda6/compose/runtime)

- No changes since 1.3.2

### Version 1.3.2

December 7, 2022

`androidx.compose.runtime:runtime-*:1.3.2` is released. [Version 1.3.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d29f2a87e3c1d5cb6dfde828400d67b6f161be63..8476d588d4975cb86be01bf4e356c5605ad89d48/compose/runtime)

**Bug Fixes**

- Updated to support androidx.compose.ui 1.3.2

### Version 1.3.1

November 9, 2022

`androidx.compose.runtime:runtime-*:1.3.1` is released. [Version 1.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5cb4dae1f526ce2408f450b50ade8708684b2be..d29f2a87e3c1d5cb6dfde828400d67b6f161be63/compose/runtime)

### Version 1.3.0

October 24, 2022

`androidx.compose.runtime:runtime-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255..b5cb4dae1f526ce2408f450b50ade8708684b2be/compose/runtime)

**Important changes since 1.2.0**

**Exception Handling / Live Edit Support**

- In order to better support live edit, APIs were added to enable handling of exceptions during composition
- [Composition error handling for hot reload](https://android.googlesource.com/platform/frameworks/support/+/2819ab44af5776f76d8ac1e29d33e50a0b929a61)
- [Handle live edit errors on save/restore](https://android.googlesource.com/platform/frameworks/support/+/ae943d2f8299b58a3054f70b83d2bdd8d6e6913d)

**Composition Tracing**

- Runtime tracing APIs were added in order to support new composition tracing tooling
- [Generate composable trace event start/end calls](https://android.googlesource.com/platform/frameworks/support/+/24ece7949cc87f232664336a0fb7f26839378aa5)
- [Re-added ComposerKt.traceEventStart(Int, String)](https://android.googlesource.com/platform/frameworks/support/+/96e00fb1786ae4bc4a515d22d13f995ece7ed2b5)

**Composable Reflection APIs**

- A new `ComposableMethod` API was added to allow for more reliable reflection-based invocations of composable APIs.
- [Move invokeComposable to compose runtime](https://android.googlesource.com/platform/frameworks/support/+/5d0660b9e8113873c8887ce74bb989aa1c212191)
- [Rework API to invoke composable method](https://android.googlesource.com/platform/frameworks/support/+/eb253ee20bd005b0b419e2157d96c06a96e92916)

**Runtime Fixes**

- [Fix faulty range test for slot table checking for markers](https://android.googlesource.com/platform/frameworks/support/+/bc7b810e4bcb1702e46b562682b6c96830cab649)
- [Allow movable content to move into and out of SubcomposeLayout](https://android.googlesource.com/platform/frameworks/support/+/07b6f4372eb02255568de41924515ec50d0acd94)
- [Fix moving content to new content of a subcomposition](https://android.googlesource.com/platform/frameworks/support/+/63e59df34fcb10d627a3aea2d22013888ee76993)

**Snapshot System**

- The snapshot system got various improvements around memory management, performance, and correctness.
- [Optimize scope removal in SnapshotStateObserver](https://android.googlesource.com/platform/frameworks/support/+/486f60a81dd4accb2a52106005f002fac4ddddff)
- [Dispose nested snapshots created from transparent snapshots](https://android.googlesource.com/platform/frameworks/support/+/e82b3518094e5451dd4697f31a412c10075b28c5)
- [Fixed race condition when reading state from the global snapshot](https://android.googlesource.com/platform/frameworks/support/+/c5ff609874b5f7c19f7dfadcadcb7651d4ee14cd)
- [Support DerivedState in SnapshotStateObserver](https://android.googlesource.com/platform/frameworks/support/+/0f8c4cc72262771896665eb83887ec4f7ea5a225)
- [Prevent removing derived state from composition when it is read in other scopes](https://android.googlesource.com/platform/frameworks/support/+/4945dfa31180f343697de5810b99ec80a48dc386)
- [Use IdentityArrayMap instead of HashMap inside DerivedState](https://android.googlesource.com/platform/frameworks/support/+/fbe8655d6c56990f4de613176939a52f2bc9fa9a)
- [Update derived state observers to use mutable vector](https://android.googlesource.com/platform/frameworks/support/+/ae918365742eadb840fe89c72ec8b14b9dacf8a1)
- [Update SnapshotStateObserver state cleanup](https://android.googlesource.com/platform/frameworks/support/+/62ef19d62c33659c190b4018d8ffb67d929bcc61)
- [Replace SnapshotStateObserver.invalidated with ArraySet](https://android.googlesource.com/platform/frameworks/support/+/4088aca726bb99f5c007ef61209fddacdb8817ad)
- [Fixed race condition when reading state from the global snapshot](https://android.googlesource.com/platform/frameworks/support/+/c5ff609874b5f7c19f7dfadcadcb7651d4ee14cd)
- [Fix use of stale record in DerivedState hash calculation](https://android.googlesource.com/platform/frameworks/support/+/bfd2a904f9e78db21b23b8c5420260f95fb16129)
- [Fix race condition when advancing the global snapshot](https://android.googlesource.com/platform/frameworks/support/+/2abd2315fd690a61c868684c93018ed79ad949d1)
- [Speed up scope observations cleanup in SnapshotStateObserver](https://android.googlesource.com/platform/frameworks/support/+/05812da909010aa9c73251849aac4b970a5a9209)

### Version 1.3.0-rc01

October 5, 2022

`androidx.compose.runtime:runtime-*:1.3.0-rc01` is released. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bdce26bd7556b92d2d4d2af3de881dd8e2c51459..e6ab75d133443eb5c1d92f910f625741041fc591/compose/runtime)

**Bug Fixes**

- Fixed `ArrayIndexOutOfBoundsException` coming from the slot table ([b/249076084](https://issuetracker.google.com/issues/249076084))

### Version 1.3.0-beta03

September 21, 2022

`androidx.compose.runtime:runtime-*:1.3.0-beta03` is released. [Version 1.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bdce26bd7556b92d2d4d2af3de881dd8e2c51459/compose/runtime)

**Behavior Breaking Change**

- The parameter to `remember` and `rememberCoroutineScope` where changed to be `crossinline`. This will report an error for early returns instead of allowing an early return which will cause a later internal error to be reported.
- This change can potentially lead to new compiler errors to be reported requiring non-local returns to be removed from the lambdas passed to these functions. ([Ibea62](https://android-review.googlesource.com/#/q/Ibea62b31341fb386f47d495ce6bb1708fbfa6c0a))

### Version 1.3.0-beta02

September 7, 2022

`androidx.compose.runtime:runtime-*:1.3.0-beta02` is released. [Version 1.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d9910e143f859716fd850a1f0036147622d6089b..cce7b70f6a5ebf955cf748a73c18b63228b22c74/compose/runtime)

**Bug Fixes**

- Updated API ([I64ca0](https://android-review.googlesource.com/#/q/I64ca0ae49dffb777379fc90d6be8e05a3f89378a))

### Version 1.3.0-beta01

August 24, 2022

`androidx.compose.runtime:runtime-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..d9910e143f859716fd850a1f0036147622d6089b/compose/runtime)

**API Changes**

- A `find` method was added to `CompositionData` to allow developer tools using this API to quickly find a sub-group of composition using its identity. ([I5794f](https://android-review.googlesource.com/#/q/I5794ff3ee6a036d3e425b21d092dba3caaeed4bb))

### Version 1.3.0-alpha03

August 10, 2022

`androidx.compose.runtime:runtime-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a7f0710ad21f556f0dde9bf7bdab6d2135170fd4..bea814b246f89ff7244e3c6b0648f0b57e47897c/compose/runtime)

### Version 1.3.0-alpha02

July 27, 2022

`androidx.compose.runtime:runtime-*:1.3.0-alpha02` is released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/compose/runtime)

**API Changes**

- Re-added `ComposerKt.traceEventStart(Int, String)` for backwards compatibility ([I6e6de](https://android-review.googlesource.com/#/q/I6e6de7e8a7c9eb0fa8eee7a6adf1b4234f76811d))

### Version 1.3.0-alpha01

June 29, 2022

`androidx.compose.runtime:runtime-*:1.3.0-alpha01` is released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..8094b683499b4098092c01028b55a38b49e357f2/compose/runtime)

**API Changes**

- Moving utility functionality to runtime ([I4f729](https://android-review.googlesource.com/#/q/I4f729ac5919a71218d89e8892ab9d96b8c76aa96))

## Version 1.2

### Version 1.2.1

August 10, 2022

`androidx.compose.runtime:runtime-*:1.2.1` is released. [Version 1.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0793130863c72dc4a2d02bc975128f3ef0158b..3c2d5397fb8ef697bb04bfc7e98721e2dc0aa255/compose/runtime)

**Bug Fixes**

- Fixed memory leak: dispose of nested snapshots created from transparent snapshots [b/239603305](https://issuetracker.google.com/239603305)

### Version 1.2.0

July 27, 2022

`androidx.compose.runtime:runtime-*:1.2.0` is released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/564504df2d2c03ea9d48f868e09764418772a8a7..1e0793130863c72dc4a2d02bc975128f3ef0158b/compose/runtime)

**Important changes since `1.1.0`**

- Compose Runtime had a handful of features introduced in 1.2.0, along with many stabilizing bug fixes. The most significant new feature was the [introduction of the `movableContentOf`API](https://android.googlesource.com/platform/frameworks/support/+/f66e3a1be22d3490e8ff10474510bb8abf73c9f9), which can be used to enable complex UX such as shared element transitions. The `movableContentOf` API converts a composable lambda into a lambda that moves it state, and corresponding nodes, to any new location it is called. When the previous call leaves the composition the state is temporarily preserved and if a new call to the lambda enters the composition then the state, and associated Nodes, are moved to the location of the new call. If no new call is added the state is removed permanently and remember observers are notified.

- If a `movableContentOf` lambda is called multiple times in the same composition, new state and nodes are created for each call and, as calls leave the composition and new calls enter, the state is moved from the first leaving calls to the entering calls in the order they are called. All state not claimed by new calls is removed permanently.

- In addition to this and a few other new features, much time was spent stabilizing the runtime and Snapshot state system. Various memory leaks were removed and code paths optimized.

- A summarized list of the changes can be found below:

**New Features in `1.2`**

- [Add experimental snapshot unsafeEnter/Leave](https://android.googlesource.com/platform/frameworks/support/+/2ff1b5569536ab54fcc9442320f24ee2b58cf02e)
- [Add Snapshot.asContextElement experimental API](https://android.googlesource.com/platform/frameworks/support/+/30abde422d8213dea266b1ddff7b4bbc39c74024)
- [Introduce Snapshot.withoutReadObservation](https://android.googlesource.com/platform/frameworks/support/+/53805a49b7369999a2eb0f0230a8bbd99e86bbf8)
- [Allow state to move within a composition](https://android.googlesource.com/platform/frameworks/support/+/f66e3a1be22d3490e8ff10474510bb8abf73c9f9)
- [Tracing of Recompositions in Compose](https://android.googlesource.com/platform/frameworks/support/+/8176d9bb38dc25d1d6c4cc247bb57c3e5e6e4308)

**Performance in `1.2`**

- [Improve composition local performance](https://android.googlesource.com/platform/frameworks/support/+/45982f6e6be5ac74204d6b426a6eb56c5889efbb)
- [Baseline profiles for compose should be derived using benchmarks](https://android.googlesource.com/platform/frameworks/support/+/2dfe4b4afed725fda5bf42f6a790d1d43a443db6)

**Bug Fixes in `1.2`**

- [Remove tracking information from release recompose scopes](https://android.googlesource.com/platform/frameworks/support/+/7ff668d1061ec9e732d65ec3bfa9dc3db50fd87a)
- [Prevent removing derived state from composition when it is read in other scopes](https://android.googlesource.com/platform/frameworks/support/+/30bc6b162ba68a8cab14a781c8c27def5d35cbbc)
- [Use more efficient removeScope() in SnapshotStateObserver](https://android.googlesource.com/platform/frameworks/support/+/a1ba9c954b9cc2e36bf897e4c649f52442a07a0b)
- [Clean up derived state dependencies in composition](https://android.googlesource.com/platform/frameworks/support/+/ad7c95cd58204ef7be4cec4f999d602619c51a8a)
- [Fix currentCompositeKeyHash changing after inner recomposition inside movable content](https://android.googlesource.com/platform/frameworks/support/+/35585b15a00ec9022b1b9488e2a2edf23f205240)
- [Clean up invalidated compositions during disposal](https://android.googlesource.com/platform/frameworks/support/+/896a6ccff51ea6186c047e818999d52482bdcfce)
- [Fix derive state read during recomposition](https://android.googlesource.com/platform/frameworks/support/+/8e7c1e6bb6dcc0ce8133d731b6b779de21194fa1)
- [Fix memory leak when observing derived state objects](https://android.googlesource.com/platform/frameworks/support/+/78dc85f30cb72ba38d36bee4f85509a975f19d06)
- [Fixed movableContent composite hash key to be consistent](https://android.googlesource.com/platform/frameworks/support/+/3b830dfc084154218517a6f4e4d53f1d1203a26b)
- [Fix corner a case where the composer would crash](https://android.googlesource.com/platform/frameworks/support/+/32e4b949a79c50dbd5e935c052112c5cd4f51c54)
- [Ensure forced invalidation of a group forces recomposition](https://android.googlesource.com/platform/frameworks/support/+/4504c4f219ca8491fc2a7896e0ab1f24d0718cba)
- [Fix bug when rememberSaveable with input is restored in the wrong order](https://android.googlesource.com/platform/frameworks/support/+/59b8fa1ec8a2d45dc9df64e05b1c4f2f2d4b58f5)

### Version 1.2.0-rc03

June 29, 2022

`androidx.compose.runtime:runtime-*:1.2.0-rc03` is released. [Version 1.2.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8328bd32e5ca96bc5a53d6369130e856cd2ca80b..e8af23f4f30713a3f6073d57558e7cde0f3056e9/compose/runtime)

**Bug Fixes**

- Derived state observations were previously unconditionally removed from the recompose scope and composition together, which broke other scopes which might be still observing derived state. This change only removes derived state instances if it is no longer observed by other scopes. ([b/236618362](https://issuetracker.google.com/236618362))

### Version 1.2.0-rc02

June 22, 2022

`androidx.compose.runtime:runtime-*:1.2.0-rc02` is released. [Version 1.2.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d8badfd263991345376562fc0f247bc76ca6312..8328bd32e5ca96bc5a53d6369130e856cd2ca80b/compose/runtime)

### Version 1.2.0-rc01

June 15, 2022

`androidx.compose.runtime:runtime-*:1.2.0-rc01` is released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5973fd35e79471563d11a6776b6a1816b1e33409..2d8badfd263991345376562fc0f247bc76ca6312/compose/runtime)

**API Changes**

- Interfaces in compose libraries are now built using jdk8 default interface methods ([I5bcf1](https://android-review.googlesource.com/#/q/I5bcf197603f66ec66177c98c01c3fe4868d60997))

### Version 1.2.0-beta03

June 1, 2022

`androidx.compose.runtime:runtime-*:1.2.0-beta03` is released. [Version 1.2.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc..7cbb37cc779160b89644d03e042c129d0ce025d2/compose/runtime)

### Version 1.2.0-beta02

May 18, 2022

`androidx.compose.runtime:runtime-*:1.2.0-beta02` is released. [Version 1.2.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/eea19c54f6d94f1c234c4305c1329f7f1427867a..6266a22ad9adaed6fa88fe98aa8adaa46eb96ccc/compose/runtime)

### Version 1.2.0-beta01

May 11, 2022

`androidx.compose.runtime:runtime-*:1.2.0-beta01` is released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/41a4e31408842caa2b58db5e4ee6ec708464425f..eea19c54f6d94f1c234c4305c1329f7f1427867a/compose/runtime)

**New Features**

- This is the first beta release of 1.2!

**API Changes**

- Added experimental `Snapshot.unsafeEnter/unsafeLeave` ([I108f3](https://android-review.googlesource.com/#/q/I108f3f633fdeed300c1260d62effd2749e38bbb3))
- Added experimental `Snapshot.asContextElement()` API ([Iff072](https://android-review.googlesource.com/#/q/Iff072daba13e2d202e1895114cf62bb0290d10ea))
- The `@ComposableTarget` annotation and annotations marked by `@ComposableTargetMarker` can now be used at the file scope using the `@file` prefix. Using a target annotation at the file scope will cause the compiler to assume all composable functions in the file are intended to be target the associated applier. For example, using `@file:UiComposable` declares that all `@Composable` functions target the Compose UI applier. A function that needs to target another applier must explicitly supply the target marker annotation for the desired applier. ([I40804](https://android-review.googlesource.com/#/q/I40804e71dcc931b788c101a0be90ae1d6fc7eba1))

### Version 1.2.0-alpha08

April 20, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha08` is released. [Version 1.2.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..41a4e31408842caa2b58db5e4ee6ec708464425f/compose/runtime)

**API Changes**

- Added `TracingInProgress` to the `CompositionTracer` interface. ([Ic6f12](https://android-review.googlesource.com/#/q/Ic6f12d84c8622c7a796d44cf3eb04b0e077efc97))
- Add `recomposeScopeIdentity` to Composer ([I0c873](https://android-review.googlesource.com/#/q/I0c8733fc97baaec4990e85f3fcbf8904ca732eaa))
- Restricted tracing APIs (Composer.setTracer) to `OptIn(InternalComposeTracingApi)`. ([I9187f](https://android-review.googlesource.com/#/q/I9187fb92741e90a78945ebb078686b53d103d19f))
- Added `ResuableContentHost` which allows better control over the lifetime of state created for reusable content. For example, if a sub-composition is temporarily not in use then the content can be deactivated causing all the remembered state in the composition to be forgotten triggering, for example, all disposable effects. ([I2c0f2](https://android-review.googlesource.com/#/q/I2c0f297104d425e2bf673debccfe7a1729761593), [b/220322704](https://issuetracker.google.com/issues/220322704))

### Version 1.2.0-alpha07

April 6, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha07` is released. [Version 1.2.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/compose/runtime)

**API Changes**

- New function `Snapshot.withoutReadObservation { ... }` was added. It allows users to run the passed lambda without subscribing to the changes of the state values read during this block. You could find it useful in use cases when you want to benefit from the snapshot based thread safe write/reads, but want to be able to read the value without causing unnecessary recomposition or remeasure. ([I9f365](https://android-review.googlesource.com/#/q/I9f365d653483310cfda02cfa2c582fdcce8cfe33), [b/214054486](https://issuetracker.google.com/issues/214054486))

### Version 1.2.0-alpha06

March 23, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha06` is released. [Version 1.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/compose/runtime)

### Version 1.2.0-alpha05

March 9, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha05` is released. [Version 1.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/compose/runtime)

**External Contribution**

- Updated to use Kotlinx coroutines 1.6.0 ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

### Version 1.2.0-alpha04

February 23, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha04` is released. [Version 1.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/compose/runtime)

**API Changes**

- Added `ComposableTarget`, `ComposableTargetMarker` and
  `ComposableOpenTarget` that allows compile time reporting of when
  a composable function is called targeting an applier it was not
  designed to use.

  In most cases the annotations can be inferred by the compose
  compiler plugin so using these annotation directly should be
  rare . The cases that cannot be inferred include creating and
  using a custom applier, abstract composable functions (such as
  interface methods), fields or global variables that are
  composable lambdas (local variables and parameters are inferred),
  or when using `ComposeNode` or a related composable functions.

  For custom appliers the composable functions that calls
  `ComposeNode` or `ReusableComposeNode` need to add a
  `CompoableTarget` annotation for the function and any
  composable lambda parameter types. It is recommended, however,
  to create an annotation that is annotated with
  `ComposableTargetMarker` and then the marked annotation be used
  instead of `ComposableTarget` directly. A composable annotation
  marked with `ComposableTargetMarker` is equivalent to a
  `ComposbleTarget` with the fully qualified name of the attribute
  class as the applier parameter. For an example of using
  `ComposableTargetMarker` see `anroidx.compose.ui.UiComposable`. ([I38f11](https://android-review.googlesource.com/#/q/I38f11b789291db89fc0bb92fc14ac5b3fcba0283))

### Version 1.2.0-alpha03

February 9, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha03` is released. [Version 1.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/compose/runtime)

**API Changes**

- Added `movableContentOf` which converts a composable
  lambda into a lambda that moves it state, and corresponding nodes,
  to any new location it is called. When the previous call leaves
  the composition the state is temporarily preserved and if a new call
  to the lambda enters the composition then the state, and associated
  nodes, are moved to the location of the new call. If no new call is
  added the state is removed permanently and remember observers are
  notified.

  If a `movableContentOf` lambda is called multiple times in the same
  composition, new state and nodes are created for each call and, as
  calls leave the composition and new calls enter, the state is moved
  from the first leaving calls to the entering calls in the order they
  are called. All state not claimed by new calls is removed
  permanently. ([Ib4850](https://android-review.googlesource.com/#/q/Ib4850095f241617a191ea7815fc947adaf867456))
- Added a tracing API to composition to enable tools to
  provide more detailed tracing of composable functions. The compiler
  now generates calls to the tracing API which include source
  information. ([Ib0eb5](https://android-review.googlesource.com/#/q/Ib0eb5c1ead489ab8104548f53bf30dcf1ba511ea))

  To remove these calls and the associated source
  information from a release build, add the following Proguard rule:

        -assumenosideeffects public class androidx.compose.runtime.ComposerKt {
            boolean isTraceInProgress();
            void traceEventStart(int,java.lang.String);
            void traceEventEnd();
        }

- Add `InternalComposeScope` which gives tools the ability
  to identify a composable during recompositions. ([I07a3f](https://android-review.googlesource.com/#/q/I07a3f85a74d2a20e02b55c2bfb2ce6f3c63988b2))

### Version 1.2.0-alpha02

January 26, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha02` is released. [Version 1.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f09f3e0f47cacc65a631115deac08ee8cc132ceb..9dceceb54300ed028a7e8fc7a3454f270337ffde/compose/runtime)

### Version 1.2.0-alpha01

January 12, 2022

`androidx.compose.runtime:runtime-*:1.2.0-alpha01` is released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..f09f3e0f47cacc65a631115deac08ee8cc132ceb/compose/runtime)

**API Changes**

- Added `identity` field to `CompositionData` for generating invariant ids in the Layout Inspector. ([Ic116e](https://android-review.googlesource.com/#/q/Ic116e6682233c31ccc4a81f8cf0cc96cac4a83ca))

**Dependency Updates**

- Now depends on Kotlin `1.6.10`.

## Version 1.1

### Version 1.1.1

February 23, 2022

`androidx.compose.runtime:runtime-*:1.1.1` is released. [Version 1.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f9e9589a03c4b53f4401cc0cb8f763526fb885c7..564504df2d2c03ea9d48f868e09764418772a8a7/compose/runtime)

**Bug Fixes**

- Fix `NullPointerException` at `androidx.compose.ui.platform.RenderNodeLayer.updateDisplayList` ([aosp/1947059](https://android-review.googlesource.com/c/platform/frameworks/support/+/1947059), [b/206677462](https://issuetracker.google.com/issues/206677462))
- Fix crash caused by clipboard content while reading from clipboard on Android. ([I06020](https://android-review.googlesource.com/#/q/I0602066750e3fce55deceb709f8c04ee9a71dabf), [b/197769306](https://issuetracker.google.com/issues/197769306))
- Fixed RTL in `LazyVerticalGrid` ([aosp/1931080](https://android-review.googlesource.com/c/platform/frameworks/support/+/1931080), [b/207510535](https://issuetracker.google.com/issues/207510535))

### Version 1.1.0

February 9, 2022

`androidx.compose.runtime:runtime-*:1.1.0` is released. [Version 1.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0310f2e9c177573a16c2d594fffabaada9b446ea..f9e9589a03c4b53f4401cc0cb8f763526fb885c7/compose/runtime)

**Important changes since 1.0.0**

- Stable support for the Android 12 [Overscroll effect](https://android-review.googlesource.com/c/platform/frameworks/support/+/1795727/)
- Improvements to touch target sizing
- Note that, with respect to Compose 1.0, Material components will expand their layout space to meet Material [accessibility guidelines](https://material.io/design/usability/accessibility.html) for [touch target size](https://material.io/design/usability/accessibility.html#layout-and-typography). For instance, Button touch target will expand to a minimum size of `48x48dp`, even if you set the Button's size to be smaller. This aligns Compose Material to the same behavior of Material Design Components, providing consistent behavior if you mix Views and Compose. This change also ensures that when you create your UI using Compose Material components, minimum requirements for touch target accessibility will be met.
- Stable support for [Navigation Rail](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#navigationrail)
- Graduates a number of previously experimental APIs to stable
- [Support](https://developer.android.com/jetpack/androidx/releases/compose-kotlin) for newer versions of Kotlin

### Version 1.1.0-rc03

January 26, 2022

`androidx.compose.runtime:runtime-*:1.1.0-rc03` is released. [Version 1.1.0-rc03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8b1e748d80de10c087ce57eaaa93cd209cccebad..0310f2e9c177573a16c2d594fffabaada9b446ea/compose/runtime)

**Bug Fixes**

- Updated to support Compose Material `1.1.0-rc03`

### Version 1.1.0-rc01

December 15, 2021

`androidx.compose.runtime:runtime-*:1.1.0-rc01` is released. [Version 1.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..8b1e748d80de10c087ce57eaaa93cd209cccebad/compose/runtime)

### Version 1.1.0-beta04

December 1, 2021

`androidx.compose.runtime:runtime-*:1.1.0-beta04` is released. [Version 1.1.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9fee5f6a2093713639af8853adbf898f7b609969..75784ce6dbac6faa5320e5898e9472f02ab8710c/compose/runtime)

**New Features**

- Updated to be compatible with Kotlin `1.6.0`

### Version 1.1.0-beta03

November 17, 2021

`androidx.compose.runtime:runtime-*:1.1.0-beta03` is released. [Version 1.1.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f07d12061370a603549747200c79b60239706330..cc1240d00b28657ee0c1a937f60430eaf1b03b09/compose/runtime)

### Version 1.1.0-beta02

November 3, 2021

`androidx.compose.runtime:runtime-*:1.1.0-beta02` is released. [Version 1.1.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/92af5b17ecee9d3c62f59e98b483e411c390f51b..f07d12061370a603549747200c79b60239706330/compose/runtime)

**API Changes**

- Snapshot code was split up into multiple files, but all still lives in the same JVM class. ([Ic6c98](https://android-review.googlesource.com/#/q/Ic6c98dc9d1e4a85a2ef5acf099bc153b0d5f4146))

### Version 1.1.0-beta01

October 27, 2021

`androidx.compose.runtime:runtime-*:1.1.0-beta01` is released. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..92af5b17ecee9d3c62f59e98b483e411c390f51b/compose/runtime)

### Version 1.1.0-alpha06

October 13, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/da9716386798fc4e39075f54e5bd3317384a63e6..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/compose/runtime)

**API Changes**

- Removed `InternalCompilerApi` from Composer methods that are required to be called cross-module ([I1aa0b](https://android-review.googlesource.com/#/q/I1aa0b78dbfb808d352e3a46de2388797548d34a9))
- `Recomposer.state` has been deprecated and replaced by `Recomposer.currentState` to change its type to a StateFlow ([Ic2ab3](https://android-review.googlesource.com/#/q/Ic2ab34c19176704fe2f6cd081607dfb92d86ea3c), [b/197773820](https://issuetracker.google.com/issues/197773820))

### Version 1.1.0-alpha05

September 29, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..da9716386798fc4e39075f54e5bd3317384a63e6/compose/runtime)

### Version 1.1.0-alpha04

September 15, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bf63d633b292368932b7ea1994e4116f95a94b5c..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/compose/runtime)

### Version 1.1.0-alpha03

September 1, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha03` is released. [Version 1.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc..bf63d633b292368932b7ea1994e4116f95a94b5c/compose/runtime)

**New Features**

- The Compose Compiler now supports older versions of the Compose Runtime (1.0). Prior to this change, the Compose Compiler was only compatible with the Compose Runtime of the same version or later. After this change, the Compose Compiler is compatible with an older version of the Compose Runtime (1.0). ([aosp/1796968](https://android-review.googlesource.com/c/platform/frameworks/support/+/1796968))
- Updated Compose `1.1.0-alpha03` to depend on Kotlin `1.5.30`. ([I74545](https://android-review.googlesource.com/#/q/I74545c317093029a2a46707b9024ad3385854ecb))

### Version 1.1.0-alpha02

August 18, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1e0ab9e58c3c2ebe8152b7507938aef7e9c1acdc/compose/runtime)

### Version 1.1.0-alpha01

August 4, 2021

`androidx.compose.runtime:runtime-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/compose/runtime)

## Version 1.0

### Version 1.0.5

November 3, 2021

`androidx.compose.runtime:runtime-*:1.0.5` is released. [Version 1.0.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74486e447dc2667c6a4cc46b2963f40210ceb348..39088e9f5278a15516318bb8979517d532bfdac3/compose/runtime)

**Bug Fixes**

- Fixed a crash tracking derivedStateOf instances. ([aosp/1792247](https://android-review.googlesource.com/c/platform/frameworks/support/+/1792247))

### Version 1.0.4

October 13, 2021

`androidx.compose.runtime:runtime-*:1.0.4` is released. [Version 1.0.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b73eb10b9c34d4659d950c12ff23cf094d4d8c7..74486e447dc2667c6a4cc46b2963f40210ceb348/compose/runtime)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.31`

### Version 1.0.3

September 29, 2021

`androidx.compose.runtime:runtime-*:1.0.3` is released. [Version 1.0.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c1876203334d14761d2c11e47c8191ef9107989..4b73eb10b9c34d4659d950c12ff23cf094d4d8c7/compose/runtime)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.30`

### Version 1.0.2

September 1, 2021

`androidx.compose.runtime:runtime-*:1.0.2` is released. [Version 1.0.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c076d3eb651533329571facecfb54dc72e1b0fc4..9c1876203334d14761d2c11e47c8191ef9107989/compose/runtime)

Updated to support the Compose `1.0.2` release. Compose `1.0.2` is still compatible with Kotlin `1.5.21`.

### Version 1.0.1

August 4, 2021

`androidx.compose.runtime:runtime-*:1.0.1` is released. [Version 1.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7077236bd50d5bf31068c8ac40302765010a0e56..c076d3eb651533329571facecfb54dc72e1b0fc4/compose/runtime)

**Dependency Updates**

- Updated to depend on Kotlin `1.5.21`.

### Version 1.0.0

July 28, 2021

`androidx.compose.runtime:runtime-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/abcc318573114e39365e63de4bea7736a81491af..7077236bd50d5bf31068c8ac40302765010a0e56/compose/runtime)

**Major features of 1.0.0**

This is the first stable release of Compose. Please see the official [Compose Release blog](https://android-developers.googleblog.com/2021/07/jetpack-compose-announcement.html) for more details!

**Known Issues**

- If you are using Android Studio Bumblebee Canary 4 or AGP `7.1.0-alpha04`/`7.1.0-alpha05`, you may hit the following crash:

        java.lang.AbstractMethodError: abstract method "void androidx.lifecycle.DefaultLifecycleObserver.onCreate(androidx.lifecycle.LifecycleOwner)"

  To fix, temporarily increase your minSdkVersion to 24+ in your `build.gradle` file. This issue will be fixed in the next version of Android Studio Bumblebee and AGP `7.1`. ([b/194289155](https://issuetracker.google.com/issues/194289155))

### Version 1.0.0-rc02

July 14, 2021

`androidx.compose.runtime:runtime-*:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e..abcc318573114e39365e63de4bea7736a81491af/compose/runtime)

- Fixed race conditions in SnapshotStateObserver causing spurratic NullPointerExceptions. ([aosp/1763445](https://android-review.googlesource.com/c/platform/frameworks/support/+/1763445), [aosp/1758105](https://android-review.googlesource.com/c/platform/frameworks/support/+/1758105), [b/192677711](https://issuetracker.google.com/issues/192677711))
- Fixed issues with runtime snapshots causing `java.lang.IllegalStateException: Reading a state that was created after the snapshot was taken or in a snapshot that has not yet been applied` crashes. ([b/193006595](https://issuetracker.google.com/issues/193006595), [b/192570897](https://issuetracker.google.com/issues/192570897))

### Version 1.0.0-rc01

July 1, 2021

`androidx.compose.runtime:runtime-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f434dccf3dc4d4e82d8d965da3746615870537b4..1a3ba62b97c98d85f6c0ac2fb6483fc9ac60872e/compose/runtime)

### Version 1.0.0-beta09

June 16, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta09` is released. [Version 1.0.0-beta09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/compose/runtime)

**Added Profile Rules**

This release adds profile rules to the following compose modules ([I14ed6](https://android-review.googlesource.com/#/q/I14ed64578d535320a40ed8d486f75715641b2762)):

- androidx.compose.animation
- androidx.compose.animation-core
- androidx.compose.foundation
- androidx.compose.foundation-layout
- androidx.compose.material
- androidx.compose.material-ripple
- androidx.compose.runtime
- androidx.compose.ui
- androidx.compose.ui.geometry
- androidx.compose.ui.graphics
- androidx.compose.ui.text
- androidx.compose.ui.text
- androidx.compose.ui.unit
- androidx.compose.ui.util

#### What are profile rules?

- Profile rules for a library are specified in a text file `baseline-prof.txt` located in the `src/main` or equivalent directory. The file specifies a rule per line, where a rule in this case is a pattern for matching to methods or classes in the library. The syntax for these rules is a superset of the human-readable ART profile format that is used when using `adb shell profman --dump-classes-and-methods ...`. These rules take one of two forms to target either methods or classes.

- A method rule will have the following pattern:

      <FLAGS><CLASS_DESCRIPTOR>-><METHOD_SIGNATURE>

- And a class rule will have the following pattern:

      <CLASS_DESCRIPTOR>

- Here `<FLAGS>` is one or more of the characters `H`, `S`, and `P` to indicate whether or not this method should be flagged as "Hot", "Startup", or "Post Startup".

- The `<CLASS_DESCRIPTOR>` is the descriptor for the class that the targeted method belongs to. For example, the class `androidx.compose.runtime.SlotTable` would have a descriptor of `Landroidx/compose/runtime/SlotTable;`.

- The `<METHOD_SIGNATURE>` is the signature of the method, and includes the name, parameter types, and return types of the method. For example, the method `fun isPlaced(): Boolean` on `LayoutNode` has the signature `isPlaced()Z`.

- These patterns can have wildcards (`**`, `*`, and `?`) in order to have a single rule encompass multiple methods or classes.

#### What do the rules do?

- A method that has the flag `H` indicates that this method is a "hot" method, and should be compiled ahead of time.

- A method that has the flag `S` indicates that it is a method which is called at startup, and should be compiled ahead of time to avoid the cost of compilation and interpreting the method at startup time.

- A method that has the flag `P` indicates that it is a method which is called after startup.

- A class that is present in this file indicates that it is used during startup and should be pre-allocated in the heap to avoid the cost of class loading.

#### How does this work?

- Libraries can define these rules which will be packaged in AAR artifacts. When an app is then built which includes these artifacts, these rules are merged together and the merged rules are used to build a compact binary ART profile that is specific to the app. ART can then leverage this profile when the app is installed on devices in order to ahead-of-time compile a specific subset of the application to improve the performance of the application, especially the first run. Note that this will have no effect on debuggable applications.

### Version 1.0.0-beta08

June 2, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta08` is released. [Version 1.0.0-beta08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/compose/runtime)

**API Changes**

- `State<T>` is now `State<out T>` ([I69049](https://android-review.googlesource.com/#/q/I690492799c315e5bf8eaa655cc160f008b6ec299))
- `ControlledComposition` API change to enable recomposing changes in a recompose single pass. ([Iaafd1](https://android-review.googlesource.com/#/q/Iaafd1d5f11e2ee2b499745b9f111f7442563a4ce), [b/184173932](https://issuetracker.google.com/issues/184173932))

### Version 1.0.0-beta07

May 18, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta07` is released. [Version 1.0.0-beta07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/compose/runtime)
| **Note:** Libraries dependent on Compose will need to recompile with version `1.0.0`‑`beta07`. Otherwise, libraries may encounter a `NoSuchMethodError`, such as:  
| `java.lang.NoSuchMethodError: No interface method startReplaceableGroup(ILjava/lang/String;)V in class Landroidx/compose/runtime/Composer; or its super classes`. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))

**API Changes**

- Added new compose compiler APIs that allow the source information generated by the compiler to be removed during source minification. ([Ia34e6](https://android-review.googlesource.com/#/q/Ia34e699fdbeaeb86b74e9da27d79d186e6e71757))
- Introduces `ReusableContent` which will attempt to reuse the
  nodes in its content instead of replacing them when the key
  is changed. When the key is changed the previous values in
  the slot table for the content is ignored except for the
  nodes that were generated and the values used to update the
  nodes.

  Introduces `ReusableComposeNode` that will reuse the node
  emitted instead of replacing it as is done for `ComposeNode`. ([I1dd86](https://android-review.googlesource.com/#/q/I1dd86f88d3e96be8aee0a433746f4f3fbc54c3c6))
- `@ComposeCompilerApi` no longer `@RequiresOptIn` ([Iab690](https://android-review.googlesource.com/#/q/Iab6901114e02706221c6f1f2050d372b366ee060))

**Bug Fixes**

- LazyColumn/Row will now keep up to 2 previously visible items active (not disposed) even when they are scrolled out already. This allows the component to reuse the active subcompositions when we will need to compose a new item which improves the scrolling performance. ([Ie5555](https://android-review.googlesource.com/#/q/Ie5555c9a7031dc9bd31f452a0ed9b28d8a337f5f))

### Version 1.0.0-beta06

May 5, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta06` is released. [Version 1.0.0-beta06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..4c1927601bfcaaaf049d0fc7a4e5801ff5cf9729/compose/runtime)

**API Changes**

- `@ComposeCompilerApi` no longer `@RequiresOptIn` ([Iab690](https://android-review.googlesource.com/#/q/Iab6901114e02706221c6f1f2050d372b366ee060))

### Version 1.0.0-beta05

April 21, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta05` is released. [Version 1.0.0-beta05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/compose/runtime)

**API Changes**

- Removed`@InternalComposeApi` for recording snapshot reads and writes ([Id134d](https://android-review.googlesource.com/#/q/Id134d5546887381ceb59fa420202d8f9c891fd1e))

**Bug Fixes**

- The AndroidManifest files from ui-test-manifest and ui-tooling-data are now compatible with Android 12 ([I6f9de](https://android-review.googlesource.com/#/q/I6f9dec0515ad6eb7fd232eeb124ee0164f4e90cb), [b/184718994](https://issuetracker.google.com/issues/184718994))

### Version 1.0.0-beta04

April 7, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta04` is released. [Version 1.0.0-beta04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..0e6e72e136ada934db74265667417524ba0ba04f/compose/runtime)

**Bug Fixes**

- Prior to this change, local composable functions were skippable based on their parameters. After this change, no local composable functions will skip. This change is done because it is common and expected for local functions to capture parameters from the parent and them skipping is a common source of bugs.

  To summarize, consider the example:

      @Composable fun Counter(count: Int, onCountChange: (Int) -> Unit) {
        @Composable fun ShowCount() { Text("Count: $count") }
        ShowCount()
        Button(onClick={ onCountChange(count + 1) }) {
          Text("Increment")
        }
      }

  Prior to this change, the `ShowCount` composable function would always skip, even after the `count` parameter was updated. This is no longer the case. ([I5648a](https://android-review.googlesource.com/#/q/I5648a5f11c89e71c6b8c748f111c47bcafee9178))
- Fixed the issue when `rememberSaveable()` was restoring the old value when used with input params ([I1b110](https://android-review.googlesource.com/#/q/I1b1108e2d8f141887a46e781d4fe04a0d84cd09c), [b/182403380](https://issuetracker.google.com/issues/182403380))

### Version 1.0.0-beta03

March 24, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta03` is released. [Version 1.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/compose/runtime)

**API Changes**

- `DefaultMonotonicFrameClock` is deprecated. Calling `withFrameNanos` or `Recomposer.runRecomposeAndApplyChanges` with no `MonotonicFrameClock` will now throw `IllegalStateException`. ([I4eb0d](https://android-review.googlesource.com/#/q/I4eb0d7a8ebae7497735d25bc35e9f94c66ce2232))

### Version 1.0.0-beta02

March 10, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/df134e0f94ac70e36764a70dc7fb6a083e0e0fab..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/compose/runtime)

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))
- Fix for broken `rememberSaveable { mutableStateOf(0) }` when used inside a destination of navigation-compose. ([I1312b](https://android-review.googlesource.com/#/q/I1312b5b210dde32250945d164a2f3a1b574cb0a8), [b/180042685](https://issuetracker.google.com/issues/180042685), [b/180701630](https://issuetracker.google.com/issues/180701630))

### Version 1.0.0-beta01

February 24, 2021

`androidx.compose.runtime:runtime-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ed3262e0dfca1d352bdbf8f8e10253a61ef6218..4b6cff92e45f1d4467086aa2c6aa0248b4883950/compose/runtime)

This is the first release of Compose 1.0.0 Beta.

**API Changes**

- Add `Recomposer.runRecomposeConcurrentlyAndApplyChanges` experimental API for recomposing invalidated compositions off the main frame loop. ([I342d0](https://android-review.googlesource.com/#/q/I342d03606de9fe04254e620296ad9b57c42da7b4))
- Any composables marked with @ReadOnlyComposable are now compile-time validated to ensure that they only make calls to other @ReadOnlyComposables ([I58961](https://android-review.googlesource.com/#/q/I58961d2946c80a6a2d9e8e0cca35fd61f41ee703))
- The `defaultFactory` for `compositionLocalOf` and
  `staticCompositionLocalOf` is now required instead of
  optional.

  This changes removes a potential type error for non-nullable
  types where no default factory was provided. Previously this
  would provide a null reference for a non-nullable type.

  For nullable types consider supplying `{ null }` as the default
  factory.

  We do not recommend using locals with non-nullable types unless
  a sensible default can be provided. If no sensible default exists,
  the `defaultFactory` lambda should throw an exception. However
  throwing an exception means that consumers of the local will have
  an implicit dependency on it being provided that is not enforced
  by the type system. ([Ifbd2a](https://android-review.googlesource.com/#/q/Ifbd2a8abd2f1fc4578da4b782b570ed9de088beb))
- Deprecated symbols were removed from the compose runtime ([I3252c](https://android-review.googlesource.com/#/q/I3252c231cab96abb5b73ffb1d37410c0569490f5))

- Deprecated `emptyContent()` is removed. Use `{}` instead. ([Idb33f](https://android-review.googlesource.com/#/q/Idb33f22d9a1002f86b42606dd93478ee37924445), [b/179432510](https://issuetracker.google.com/issues/179432510))

- Providers has been renamed to CompositionLocalProvider

  - The Composition constructor no longer accepts a key parameter, and has been deprecated.
  - currentCompositeKeyHash has been turned into a composable top level property instead of a composable top level function.
  - CompositionData and CompositionGroup have been moved to the androidx.compose.runtime.tooling namespace
  - ComposableLambda has been made an interface instead of a concrete class, and no longer has type parameters.
  - ComposableLambdaN has been made an interface instead of a concrete class, and no longer has type parameters.
  - The snapshotFlow function has been moved to the androidx.compose.runtime namespace
  - the merge method of SnapshotMutationPolicy is no longer experimental
  - The @TestOnly top level clearRoots function has been removed. It is no longer necessary.
  - keySourceInfoOf and resetSourceInfo functions have been removed. They are no longer necessary.
  - Composer.collectKeySourceInformation has been removed. It is no longer necessary.
  - isJoinedKey, joinedKeyLeft, and joinedKeyRight methods have been removed. They are no longer necessary.
  - Various top level APIs have been moved and reorganized into different files. Due to Kotlin's file class semantics, this will break binary compatibility but not source compatibility, so should not be an issue for most users.
  - ([I99b7d](https://android-review.googlesource.com/#/q/I99b7de8ea0fb5d73a0ee4667a65e35d976383831), [b/177245490](https://issuetracker.google.com/issues/177245490))
- SnapshotStateObserver is not Experimental anymore ([Id2e6a](https://android-review.googlesource.com/#/q/Id2e6a2eaac801b2eb9ef3fcacfdadb679ffbffab))

- Deleted some previously deprecated APIs ([Ice5da](https://android-review.googlesource.com/#/q/Ice5dae36591015a9d905b84b26cc02662385d831), [b/178633932](https://issuetracker.google.com/issues/178633932))

- Made the following Material API changes:

  - Added contentPadding parameter to Top/BottomAppBar to allow customizing the default padding.
  - Reordered parameters in BackdropScaffold to follow API guidelines for required parameters being before optional parameters.
  - Moved `icon` parameter in BottomNavigationItem to be after `selected` and `onClick`.
  - Renamed `alwaysShowLabels` parameter in BottomNavigationItem to `alwaysShowLabel`.
  - Renamed `bodyContent` parameters in a few components to just `content`.
  - Reordered parameters in `ButtonDefaults.buttonColors()`. Please note that because the type of the parameters have not changed, this will not cause an error in your code - please ensure you are either using named parameters or update the ordering manually, otherwise your code will not work the same as previously.
  - Added `secondaryVariant` parameter to `darkColors()`. This color is typically the same as `secondary` in dark theme, but adding for consistency and further customization.
  - Removed ElevationDefaults and animateElevation() from the public API surface since they were not commonly used / useful.
  - Renamed `onValueChangeEnd` in `Slider` to `onValueChangeFinished` and made it nullable.
  - Renamed `text` parameter in `Snackbar` to `content` for consistency.
  - Added `contentPadding` parameter to `DropdownMenuItem` to allow customizing the default padding and made `content` be an extension on `RowScope`.
  - Renamed `ModalDrawerLayout` to `ModalDrawer`.
  - Renamed `BottomDrawerLayout` to `BottomDrawer`.
  - ([I1cc66](https://android-review.googlesource.com/#/q/I1cc669dfec6194e13843879823bfdc97f98a7d20))

### Version 1.0.0-alpha12

February 10, 2021

`androidx.compose.runtime:runtime-*:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..9ed3262e0dfca1d352bdbf8f8e10253a61ef6218/compose/runtime)

**API Changes**

- Support for ViewGroups was removed from UiApplier. The Deprecated emitView composables were removed. ([Ifb214](https://android-review.googlesource.com/#/q/Ifb2141153189ac4b0fbd748a23c3de38ed155af7))
- CompositionReference renamed to CompositionContext ([I53fcb](https://android-review.googlesource.com/#/q/I53fcb2d87d57c95c293108bf80e54c7d17064f24))
- ComponentActivity.setContent has moved to androidx.activity.compose.setContent in the androidx.activity:activity-compose module. ([Icf416](https://android-review.googlesource.com/#/q/Icf4168e6078b87ce746569a946b2a90274197c72))
- Snapshot API was updated to be more consistent with API guideline as well as hiding internal implementation classes from the public API. ([Id9e32](https://android-review.googlesource.com/#/q/Id9e32c885473f09cd69354a4c87a2c57c5f86533))
- Renamed Ambients to match the Ambient -\> CompositionLocal rename. Ambients used to be named AmbientFoo, now CompositionLocals are named LocalFoo. ([I2d55d](https://android-review.googlesource.com/#/q/I2d55d1c5c38a08b04e72a569d3079db4feca1bf7))
- Renamed Ambient to CompositionLocal, and ambientOf / staticAmbientOf to compositionLocalOf / staticCompositionLocalOf respectively. This change helps to make the purpose of CompositionLocal more clear: a mechanism for providing / retrieving values local to a composition. CompositionLocal instances should be prefixed with `Local`, such as val LocalFoo = compositionLocalOf { Foo() }. ([Ia55b6](https://android-review.googlesource.com/#/q/Ia55b6cb149a659a2738cd1c60540e81ef835b8cc))
- takeMutableSnapshot and takeSnapshot have moved to be companion methods of Snapshot. ([I91f19](https://android-review.googlesource.com/#/q/I91f197a054cd967e69c47fa99c40e0da7e91b83a))
- `@ComposableContract` has been deprecated in favor of three more specific annotations.

  `@ComposableContract(restartable = false)` has become `@NonRestartableComposable`
  `@ComposableContract(readonly = true)` has become `@ReadOnlyComposable`
  `@ComposableContract(preventCapture = true)` has become `@DisallowComposableCalls`
  `@ComposableContract(tracked = true)` has been removed. ([I60a9d](https://android-review.googlesource.com/#/q/I60a9db0287dc0e03b38e6cf31a7d435026a2ce0f))
- emptyContent() and (@Composable () -\> Unit).orEmpty() utilities have been deprecated as they no longer have any positive performance impact or value ([I0484d](https://android-review.googlesource.com/#/q/I0484d3ef439993d05eea86e53f05997eced590ab))

- `snapshotFlow` and `withMutableSnapshot` are no longer
  experimental ([I6a45f](https://android-review.googlesource.com/#/q/I6a45fac62267a318481e9a3ba8a3acf3162219f6))

- Recomposers can now be closed. Closed recomposers will
  continue recomposition until composition child coroutines complete.
  Recomposer.shutDown renamed to cancel to contrast with close. ([Ib6d76](https://android-review.googlesource.com/#/q/Ib6d766b91381ee45af41a14b7951c48f794f0a90))

- The `compose:runtime-dispatch` artifact is now deprecated.
  MonotonicFrameClock can now be found in compose:runtime and
  AndroidUiDispatcher can be found in compose:ui. ([Ib5c36](https://android-review.googlesource.com/#/q/Ib5c36a427306eceac4b9b16b52a091e864e5b936))

- The API the Compose compiler plugin targets
  has been refactored to use an interface instead of a
  concrete class. The interface also no longer uses
  a type parameter.

  This is an internal change that should not effect source
  code compatibility but is a binary breaking change. ([I3b922](https://android-review.googlesource.com/#/q/I3b9229969aa70138bc57f5e8498602f5b2dba1e6), [b/169406779](https://issuetracker.google.com/issues/169406779))
- SnapshotMutableState was introduced ([Icfd03](https://android-review.googlesource.com/#/q/Icfd03593afd98c2cd1ad94751e590f4eefbc06e5))

- DisposableEffectDisposable was renamed to DisposaleEffectResult ([Ica7c6](https://android-review.googlesource.com/#/q/Ica7c6a63e2bc101837cdd0463d827d3a8193d6e0))

- Removed Recomposer.current(). \[Abstract\]ComposeView now
  default to lazily created, window-scoped Recomposers driven by the
  ViewTreeLifecycleOwner for the window. Recomposition and
  withFrameNanos-based animation ticks are paused while the host Lifecycle
  is stopped. ([I38e11](https://android-review.googlesource.com/#/q/I38e11565b2fc776966b6b6984aceafd8a1e6fed1))

- Recomposer.runningRecomposers now offers a global StateFlow
  of read-only RecomposerInfo for observing ongoing composition state in
  the process. Prefer this API to Recomposer.current(), which is now
  deprecated. ([If8ebe](https://android-review.googlesource.com/#/q/If8ebe3959cfe71682ad372382d3b720035ef1605))

- DisposableEffectDisposable was renamed to DisposaleEffectResult ([I3ea68](https://android-review.googlesource.com/#/q/I3ea68f09bf464edace067212655a85b8d55b679b))

### Version 1.0.0-alpha11

January 28, 2021

`androidx.compose.runtime:runtime-*:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..6950aab50fe6c9f7e9d97cf865161f2d3999eb9e/compose/runtime)

**API Changes**

- onCommit, onDispose, and onActive have been deprecated in favor of SideEffect and DisposableEffect APIs ([If760e](https://android-review.googlesource.com/#/q/If760ec2a190c4121a35006695d953010ac22a43a))
- The emit() API and all overloads have been deprecated and renamed to ComposeNode. The APIs are identical, just a different name in order to follow the naming conventions of Compose ([I4137b](https://android-review.googlesource.com/#/q/I4137beb6f23fb43350bf7badcbe790f59fa85e2c))
- invalidate and compositionReference() are now deprecated in favor of currentRecomposeScope and rememberCompositionReference respectively. ([I583a8](https://android-review.googlesource.com/#/q/I583a8efa6e3d3bc303792b825b948b3722ada103))
- RememberObserver replaces CompositionLifecycleObserver
  and CompositionLifecycleObserver is now deprecated.

  `RememberObserver` is a replacement for
  `CompositionLifecycleObserver` with modified semantics and
  renamed methods. Changing to the new API can be done mechanically
  for objects that are only remembered once which is, and continues to
  be, the recommended practice. However, if a reference was
  remembered more than once in a composition `onRemembered` is called
  for each reference where `onEnter` is only called once. `onEnter`
  was called multiple time if the object was used in subcompositions,
  such as `WithConstraints` and `Scaffold` making the single
  `onEnter` call guarantee unreliable and it was removed for
  `RememberObserver`.

  `RememberObserver` adds `onAbandoned` which is called if the
  `RememberObserver` instance is returned from the callback passed
  to `remember` but was not remembered in the composition state
  and, therefore, will never have `onRemembered` called. This can
  occur if an exception terminates composition before completing or
  the composition is discarded because the state is was producing
  a composition for is no longer current or otherwise is no longer
  needed. If the instance of `RememberObserver` following the single
  reference recommendation above is tracking an external resource
  both `onForgotten` and `onAbandoned` each indicate that the
  resource is no longer needed. If the object is tracking work
  started or resources allocated in `onRemembered`, `onAbandoned`
  can be ignored as it will not be called if `onRemembered` is
  called. ([I02c36](https://android-review.googlesource.com/#/q/I02c364f517507abd6a5c071fb527192ad1d77239))
- Do not mark `collectAsState()` functions as inline ([Ia73e4](https://android-review.googlesource.com/#/q/Ia73e40c20f0bd5eea3b2fa870aae90ba02237cfc))

**Bug Fixes**

- WithConstraints was reworked as BoxWithConstraints and moved to foundation.layout. ([I9420b](https://android-review.googlesource.com/#/q/I9420b9e0fbea7ee048b23a6ef328165bbb11e8a8), [b/173387208](https://issuetracker.google.com/issues/173387208))
- Leverage TestCoroutineDispatcher in testing ([I532b6](https://android-review.googlesource.com/#/q/I532b68e37ea6f72964fdcc267e397d285cffd9ad))

### Version 1.0.0-alpha10

January 13, 2021

`androidx.compose.runtime:runtime-*:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/compose/runtime)

**Breaking Change**

- Restructuring of the internal compiler
  API allows batching changes to the nodes generated
  as a result of composition into the "apply changes"
  phase of composition, after all `@Composable` functions
  have completed.

  This is a behavioral breaking
  change that might affect application code as
  nodes are no longer available from internal and
  experimental APIs until after changes have been
  applied. This can usually be worked around by
  surrounding code with such dependencies in a
  `SideEffect` composable to defer execution of the
  code until after the nodes have been created and
  initialized. ([I018da](https://android-review.googlesource.com/#/q/I018dab05a0486e8db663aea39a7546aa73142c11))

**API Changes**

- Added a way to track if the recomposer has applied changes. ([I1b3e2](https://android-review.googlesource.com/#/q/I1b3e25252119ddf45e1c72af5239cd1a999722ce))
- Expand \[Abstract\]ComposeView APIs to allow recycling
  Compose-based views, disposing their composition to recreate again
  later. Add APIs for installing and discovering window-scoped Recomposers
  and CompositionReferences for creating child compositions.

  Add ViewCompositionStrategy for configuring the composition disposal
  strategy of \[Abstract\]ComposeViews; default behavior is dispose on
  window detach. ([I860ab](https://android-review.googlesource.com/#/q/I860ab99a2950457157a4d904e0c514d5134fdfd7))

**Bug Fixes**

- Recomposer now exposes a Flow of its current state, allowing monitoring its activity and the activity of associated effects. ([Ifb2b9](https://android-review.googlesource.com/#/q/Ifb2b901636db4ec2f3ad068d063f5b8f74be82f4))
- The native keyEvent can now be accessed through keyEvent.nativeKeyEvent ([I87c57](https://android-review.googlesource.com/#/q/I87c57d68b76441fe92d2b91f58385832fc40ec8d), [b/173086397](https://issuetracker.google.com/issues/173086397))

### Version 1.0.0-alpha09

December 16, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/compose/runtime)

**API Changes**

- Removed SlotTable, SlotReader and
  SlotWriter from the public API. These were marked as
  InternalComposeAPI previously. Now they are internal
  to the compose module.

  CompositionData and CompositionGroup were added as a
  replacement for the ui-tooling API to use to extract
  composition information. These are public but are not
  intended for use outside the ui-tooling API as they provide
  the raw information the ui-tooling API interprets ([I31a9c](https://android-review.googlesource.com/#/q/I31a9ca6a7e5bbf162c984394dffd7a25b059315a))
- The Applier class is no longer considered an ([Id85b0](https://android-review.googlesource.com/#/q/Id85b061f677b509bfc62d1fd797531520ac8e09d))

- The `Applier` interface has changed to simplify
  building trees bottom-up instead of top-down.

  The `insert()` method has been renamed to `insertTopDown()`.

  A new method, `insertBottomUp()`, was added.

  An applier either inserts nodes into the tree it is editing
  using `insertTopDown()` or `insertBottomUp()` depending on
  which performs better.

  Some trees, such as `LayoutNode` and `View`, are much more
  efficient to build bottom-up than top-down. Prior to this change,
  a stack of inserts was required to implement bottom-up which
  needed to be copied to every applier which needed bottom-up
  construction for performance. With this change an `Applier`
  overrides `insertBottomUp()` to build a tree bottom-up and
  `insertTopDown()` to build the tree top-down. ([Icbdc2](https://android-review.googlesource.com/#/q/Icbdc2929ab8fc8fce231d633b062fc80be5c10c9))
- Compose supports property getters that can make composable invocations. Support for this is not going away, but the syntax for declaring a property getter as being @Composable is changing.

  The now-deprecated syntax for doing this was by annotating the property itself:

          @Composable val someProperty: Int get() = ...

  The now-correct syntax for doing this is by annotating the getter of the property:

         val someProperty: Int @Composable get() = ...

  Both syntaxes will work for some time, but the former deprecated syntax will eventually become a compile error. ([Id9197](https://android-review.googlesource.com/#/q/Id91977f2583b81d3e4e51bbf120cfaf943be25d5))

**Bug Fixes**

- AndroidOwner made internal ([Ibcad0](https://android-review.googlesource.com/#/q/Ibcad027dbc1794f5d202be52fe0783c73d249a25), [b/170296980](https://issuetracker.google.com/issues/170296980))
- subcomposeInto(LayoutNode) was made internal ([Id724a](https://android-review.googlesource.com/#/q/Id724aebef104f6404884f1a45bee9958583b7229))

### Version 1.0.0-alpha08

December 2, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/358bdaf3c3c4a917883408e9f747da521fdf9e65..10b5e9fd366c1c413d5576aed50a305d300938e1/compose/runtime)
| **Note:** This release is only compatible with Kotlin `1.4.20`, so you will need to update your Kotlin version.

**API Changes**

- Added lint check for composable lambda parameter naming and position, to check for consistency with Compose guidelines. Also migrated some APIs using `children` as the name for their trailing lambda to `content`, according to the lint check and guidance. ([Iec48e](https://android-review.googlesource.com/#/q/Iec48e38a2896785b521814d95c9fb624d2807315))
- Recomposer no longer accepts an EmbeddingContext; required scheduling dependencies are obtained from the effectCoroutineContext. FrameManager is deprecated; platform integrations should initialize their own global snapshot handling. ([I02369](https://android-review.googlesource.com/#/q/I02369db94b92e6ace0a7273d9d74ad44cc8cebe5))
- RestorableStateHolder.withRestorableState function was renamed to RestorableStateProvider ([I66640](https://android-review.googlesource.com/#/q/I66640dac2f299f5d85d270f2aa1c5d6fc8ab7128))

**Bug Fixes**

- Deprecated Ambients named with `Ambient` as their suffix, and replaced them with new properties prefixed with Ambient, following other Ambients and Compose API guidelines. ([I33440](https://android-review.googlesource.com/#/q/I334403cc490ea913b8980d29e2cbe08e98ad7945))
- Remove old ui-test module and its stubs ([I3a7cb](https://android-review.googlesource.com/#/q/I3a7cbbe376d0542955983fb09afd2dc37be7647e))

### Version 1.0.0-alpha07

November 11, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..358bdaf3c3c4a917883408e9f747da521fdf9e65/compose/runtime)

**New Features**

**API Changes**

- The `@UnionType` annotation has been deprecated ([I57cde](https://android-review.googlesource.com/#/q/I57cdec8694f46c502f7f6fc2bfe377a0ea0c075b))
- provideDefault was added as an alternative to provide for providing ambients, and it can be used to specify ambient values that will only be set when there is no ambient value already provided. ([Id6635](https://android-review.googlesource.com/#/q/Id663500276ad2ec3e5a5b1310a81efbf3acc0842), [b/171024925](https://issuetracker.google.com/issues/171024925))
- LaunchedTask was renamed to LaunchedEffect for consistency with the SideEffect and DisposableEffect APIs. LaunchedEffect with no subject params is not permitted in order to encourage best practices. ([Ifd3d4](https://android-review.googlesource.com/#/q/Ifd3d4f3b529b3956915c99096eef3fb3108b2b61))
- Applier now has onBeginChanges/onEndChanges callbacks that are invoked when a Composer begins/is finished applying changes to the tree. These may be used for batching resource management if needed. ([Icf476](https://android-review.googlesource.com/#/q/Icf4765f3fd6102d26177aac6f5f259f9b9c0c0de))
- Recomposer now requires a CoroutineContext at construction ([Ic4610](https://android-review.googlesource.com/#/q/Ic4610c5531ceebafc3c8644a3501a8442d1479d6))
- Changes to the internal SlotTable implementation which should not affect the public API. ([If9828](https://android-review.googlesource.com/#/q/If98280439f4965fd05f21dd0362635314176eaf8))
- Deprecated rxjava2 adapters which does not take the initial value were removed ([Idb72f](https://android-review.googlesource.com/#/q/Idb72f5d9df0562cdfe1c0e77d89f228e9e01e857))

**Bug Fixes**

- foundation.Text has been deprecated and replaced with material.Text. For a basic, unopinionated text API that does not consume values from a theme, see androidx.compose.foundation.BasicText. ([If64cb](https://android-review.googlesource.com/#/q/If64cbdd89497f171edfd1b4de907123f73279e8d))
- BaseTextField has been deprecated. Use BasicTextField instead. ([I896eb](https://android-review.googlesource.com/#/q/I896eb0eb21e73bda5f269e1ffae4357201acb219))
- Several layout related symbols were moved from androidx.compose.ui to androidx.compose.layout.ui. ([I0fa98](https://android-review.googlesource.com/#/q/I0fa982d87929e5ca9e3a32762fe9cf1fa8b8cfef), [b/170475424](https://issuetracker.google.com/issues/170475424))

**External Contribution**

- Added `runtime-rxjava3` module for compose. Similar to `runtime-rxjava2` ([I02cbf](https://android-review.googlesource.com/#/q/I02cbfebc2770cedd58de9d5ecbdcc87c7141a089))

### Version 1.0.0-alpha06

October 28, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd84d35abd1bc13fe53a4632d4b3889f6062ac81..234e23e470a5e7f81291f6acd12d538146dc010b/compose/runtime)

**API Changes**

- Recomposer is now a CompositionReference and a valid composition parent. Explicit Recomposer is now required in fewer places. ([I4036f](https://android-review.googlesource.com/#/q/I4036ff66dff4759bd40127a9af0ca59cbaa37041))
- Added DisposableEffect counterpart API to SideEffect, filling the role of onCommit-with-params but with a required onDispose.
  - Added rememberUpdatedState API to publish data from recomposition to ongoing or long-lived processes such as DisposableEffects or LaunchedTasks.
  - ([Id50b9](https://android-review.googlesource.com/#/q/Id50b9b85d2303166e5abe10aea47d6934d2c8597))
- MutableVector now implements RandomAccess ([I85d73](https://android-review.googlesource.com/#/q/I85d73f55b19cce31ba70770dbd0dc98cb3a6957a), [b/170461551](https://issuetracker.google.com/issues/170461551))
- Added SideEffect composable for applying side effects of composition to objects managed by the composition. SideEffect is intended to replace the onCommit composable. ([Ia77c2](https://android-review.googlesource.com/#/q/Ia77c2060e10aa8011052e18ece011297fc28831c))
- New experimental api RestorableStateHolder. It allows to save the state defined with \[savedInstanceState\] and \[rememberSavedInstanceState\] for the subtree before disposing it to make it possible to compose it back next time with the restored state. ([I66884](https://android-review.googlesource.com/#/q/I66884b1e65f716de7936c4fe9e573efc6539b80f), [b/166586419](https://issuetracker.google.com/issues/166586419))

**Bug Fixes**

- Enable transitions in ComposeTestRule; remove option to enable the blinking cursor from ComposeTestRule. ([If0de3](https://android-review.googlesource.com/#/q/If0de36db743b7f57b161b0fe6324565750436866))

### Version 1.0.0-alpha05

October 14, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64c532a70705a33e1e12d83a42fe6aeaca6823f9..dd84d35abd1bc13fe53a4632d4b3889f6062ac81/compose/runtime)

**API Changes**

- Experimental Modifier.pointerInput suspending input modifier ([Ia77d2](https://android-review.googlesource.com/#/q/Ia77d26185ba835c33bf48015977667df31800dff))
- The scrolling performance of LazyColumn/Row is improved by doing less work in subcomposition on every scroll. The new hasInvalidations() method was added for Composition class. hasPendingChanges() method from Recomposer was renamed to hasInvalidations() ([Ib2f32](https://android-review.googlesource.com/#/q/Ib2f324dd6845fd83321e0d4f3fa6e502c346dbc3), [b/168293643](https://issuetracker.google.com/issues/168293643), [b/167972292](https://issuetracker.google.com/issues/167972292), [b/165028371](https://issuetracker.google.com/issues/165028371))
- Add produceState API for launching coroutines from composition that update a single `State<T>` value over time ([Id4a57](https://android-review.googlesource.com/#/q/Id4a573e37be1f3072066dadd3032511acae8d2ff))
- launchInComposition renamed to LaunchedTask to match Compose API guidelines ([I99a8e](https://android-review.googlesource.com/#/q/I99a8ef39b1e1abd7b9cae898863a35ed71b62e48))
- The order of place() calls in custom Layouts now defines the drawing order for the children ([Ibc9f6](https://android-review.googlesource.com/#/q/Ibc9f6844b7309f45a8f3dadfdcda0a33b39425e6))

### Version 1.0.0-alpha04

October 1, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18a5639262f8504db530176550e338a5d0e2e044..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/compose/runtime)
| **Note:** Compose Version 1.0.0-alpha04 is only compatible with Android Studio 4.2 Canary 13 and later.

**API Changes**

- Added OwnerScope to allow collection of layout and drawing observation scopes once they are no longer valid. ([Ic4cf8](https://android-review.googlesource.com/#/q/Ic4cf8889e486e175e0f2405f1a0dc7a5a085ad99))
- Added derivedStateOf API to create State objects based on a calculation which may read (and derive from) other State objects ([If758b](https://android-review.googlesource.com/#/q/If758b97e85ac4c0c087ff0d62e4aa47da72dcf1d))
- Added TestOnly API for SnapshotStateObserver ([I6e2a9](https://android-review.googlesource.com/#/q/I6e2a9e3dd227254545c29cd5e5b19fede89b7598))

**Bug Fixes**

- foundation.Box was deprecated. Please use foundation.layout.Box instead. ([Ie5950](https://android-review.googlesource.com/#/q/Ie59501cfd404c6bce53afee2d14dd95f1520d02c), [b/167680279](https://issuetracker.google.com/issues/167680279))

### Version 1.0.0-alpha03

September 16, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..18a5639262f8504db530176550e338a5d0e2e044/compose/runtime)

**API Changes**

- `CompositionCoroutineScope` no longer implements `MonotonicFrameClock`. Callers of `withFrameNanos` should import the top-level function explicitly. ([Icb642](https://android-review.googlesource.com/#/q/Icb642e00a670c235f26d11e6549b4222b2b4c2fb), [b/166778123](https://issuetracker.google.com/issues/166778123))

**Bug Fixes**

- Global testing functions such as `onNode` or `waitForIdle` are now deprecated, please migrate to their new counterparts that are defined on ComposeTestRule ([I7f45a](https://android-review.googlesource.com/#/q/I7f45a41128160a0e67ad07e32a1ad49774602a97))
- `launchInComposition` no longer launches coroutines undispatched ([Ief6af](https://android-review.googlesource.com/#/q/Ief6afbbd9cae98ef337808a5cb481f012df602c8), [b/166486000](https://issuetracker.google.com/issues/166486000))

### Version 1.0.0-alpha02

September 2, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/compose/runtime)

**API Changes**

- Add `snapshotFlow` and `withMutableSnapshot` APIs for consuming and producing Snapshot data changes. ([I3e722](https://android-review.googlesource.com/#/q/I3e7226bacc660bdfc9ea4d781a7abfef86f5dfce))
- The calling convention for composable functions has
  changed. This is a binary breaking change. All libraries must be
  recompiled to work with this version of the compose compiler plugin.

  This change does not create a source level breaking change as the
  only APIs that have changed are compiler APIs that have an explicit
  opt in. ([I7afd2](https://android-review.googlesource.com/#/q/I7afd2d7b19652ec92b8d6d1d1e92f0745968aa66), [b/158123185](https://issuetracker.google.com/issues/158123185))
- Removed scheduling methods from EmbeddingContext ([I7b9be](https://android-review.googlesource.com/#/q/I7b9bea6af71d1b610ce68c89938bbbc793193457))

- onPreCommit is deprecated; onCommit now has onPreCommit's
  behavior.

  onCommit and onActive now run in the same choreographer frame that
  the composition changes committed in rather than at the beginning
  of the next choreographer frame. ([I70403](https://android-review.googlesource.com/#/q/I70403eea442a7a003f08e7b1d19e44e0134ea077))

### Version 1.0.0-alpha01

August 26, 2020

`androidx.compose.runtime:runtime-*:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..c93ac38a59f31e5db0eab67687532a4ba61913d5/compose)

## Version 0.1.0-dev

### Version 0.1.0-dev17

August 19, 2020

`androidx.compose.runtime:runtime-*:0.1.0-dev17` is released. [Version 0.1.0-dev17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/compose)

**API Changes**

- Custom emits can now declare that one or more of its setters can be skipped and recomposed independently of the emit. ([Ibbd13](https://android-review.googlesource.com/#/q/Ibbd13068440252724db405b26d1f6be179e80411))
- Removed deprecated FrameManager calls.

  Internal compose APIs have been changed to reduce the amount of
  overhead to track state objects such as `mutableStateof()` ([I80ba6](https://android-review.googlesource.com/#/q/I80ba67ebf59f9399e673b6218edfca4249158f82))
- The `state { ... }` composable is now deprecated in favor of
  explicit calls to `remember { mutableStateOf(...) }` for clarity.
  This reduces the overall API surface and number of concepts for state
  management, and matches the `by mutableStateOf()` pattern for class
  property delegation. ([Ia5727](https://android-review.googlesource.com/#/q/Ia57278556d4f35ecf2cf5e6e30888b0d1f1f8012))

- Flow.collectAsState now determines the default dispatcher from
  the composition itself rather than defaulting to Dispatchers.Main. ([I9c1d9](https://android-review.googlesource.com/#/q/I9c1d9ad9a881492cd74a89e896ddf5b3b8d12777))

- Crash when something which saves the state was used inside the for loop is fixed. Now having the same key in savedInstanceState() is allowed, api of UiSavedStateRegistry is now adjusted to this new requirement ([I4ab76](https://android-review.googlesource.com/#/q/I4ab7630120ffce145d1bf09d52a475d197030150), [b/160042650](https://issuetracker.google.com/issues/160042650), [b/156853976](https://issuetracker.google.com/issues/156853976), [b/159026663](https://issuetracker.google.com/issues/159026663), [b/154920561](https://issuetracker.google.com/issues/154920561))

**Bug Fixes**

- `emitView` was deprecated. Use `AndroidView` instead if possible for emitting Views inside Compose. Note that composing Views and ViewGroups directly will not be supported in the future unless these are leaves in the composition tree, case when this can be achieved using AndroidView. ([I29b1e](https://android-review.googlesource.com/#/q/I29b1e5405077f45e101eacfb26a1ebed85120444), [b/163871221](https://issuetracker.google.com/issues/163871221))

### Version 0.1.0-dev16

August 5, 2020

`androidx.compose.runtime:runtime-*:0.1.0-dev16` is released. [Version 0.1.0-dev16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9c74ed7b07d1c18da576f179d55e568ca12973df..316f882e649c600372170f013a18515f590f490d/compose)

**API Changes**

- The default mutation policy of `mutableStateOf()`,
  `ambientOf()` and `savedInstanceStateOf()` has changed to be
  `structuralEqualityPolicy()` instead of `referentialEqualityPolicy()`.

  The default for deciding if a new value assigned to a
  `mutableStateOf()` instance is considered a change now defaults to
  using `==` instead of using `===`.

  See https://kotlinlang.org/docs/reference/equality.html

  `ambientOf()` and `savedInstanceStateOf()` use `mutableStateOf()`
  in their implementations so they were changed to be consistent with
  `mutableStateOf()`.

  Using structural equality more closely matches developer
  expectations.

  For example,

      val state = mutableStateOf(1f)

  followed by,

      state.value = 1f

  will no longer be consider a change to `state` and uses of
  `state` during composition will no longer need to be recomposed.

  This is a breaking change but, in most cases (such when using
  classes that do not override `equals()`), this will not have a
  noticeable effect on an application.

  Classes that do override `equals()`, such as `data` classes,
  might see a performance degradation as their `equals()` methods
  are now, by default, called when assigned to a `mutableStateOf()`.

  The previous behavior can be restored by adding the policy
  parameter `policy = referentialEqualityPolicy()` to calls to
  `mutableStateOf()`, `ambientOf()` and `savedInstanceStateOf()`. ([Ic21a7](https://android-review.googlesource.com/#/q/Ic21a772051c4f891c655c9bd816ebb360ce19a81))
- `Row` and `Column` are now inline function significantly
  reducing the overhead of using them. ([I75c10](https://android-review.googlesource.com/#/q/I75c10e663b74ffc250a3293df7583fcd86ea891a))

**Bug Fixes**

- setViewContent was deprecated. setContent should be used instead. ([I7e497](https://android-review.googlesource.com/#/q/I7e49740d26f42e9326cb5582a4522d74957b90fe), [b/160335130](https://issuetracker.google.com/issues/160335130))
- Added MonotonicFrameAnimationClock that enables you to use a
  MonotonicFrameClock as an AnimationClockObservable to bridge the gap
  between the new coroutines based clocks and APIs that still use the old
  callback based clocks.

  The MonotonicFrameClock equivalent of ManualAnimationClock is now
  ManualFrameClock. ([I111c7](https://android-review.googlesource.com/#/q/I111c7b7182a1495f95eab1bb808d3acd6af82447), [b/161247083](https://issuetracker.google.com/issues/161247083))
- Modifier.stateDraggable was completely reworked and renamed
  to Modifier.swipeable. A new SwipeableState class was introduced, and
  DrawerState and BottomDrawerState were refactored to inherit from it.
  \[Modal/Bottom\]DrawerLayout no longer take an onStateChange parameter. ([I72332](https://android-review.googlesource.com/#/q/I7233229dfc9c04a4615f4c1cc29e604b97edd1df), [b/148023068](https://issuetracker.google.com/issues/148023068))

- Modifier.plus has been deprecated, use Modifier.then instead. 'Then' has a stronger signal of ordering, while also prohibits to type `Modifier.padding().background() + anotherModifier`, which breaks the chain and harder to read ([Iedd58](https://android-review.googlesource.com/#/q/Iedd587edbed0ba964ef203a66b98be7297147bd7), [b/161529964](https://issuetracker.google.com/issues/161529964))

- SubcomposeLayout is added. It is a low level primitive which allows to compose the children during the measuring if we want to use some values available only later during the measure for the subtree composition. For example WithConstraints is not implemented using SubcomposeLayout. ([I25cc8](https://android-review.googlesource.com/#/q/I25cc8cfe8382db1ef61e93866ba08f4668cbc734))

- Material FilledTextField was renamed to TextField and foundational TextField was renamed to BaseTextField to make simplest desired API easy to discover and use ([Ia6242](https://android-review.googlesource.com/#/q/Ia62420a7a2231c02b6874a9a2867bf786a397ed3), [b/155482676](https://issuetracker.google.com/issues/155482676))

- Modifier.drawBackground has been renamed to Modifier.background ([I13677](https://android-review.googlesource.com/#/q/I1367723fce0e07418ed4ab391fe20c69aa092f53))

### Version 0.1.0-dev15

July 22, 2020

`androidx.compose.runtime:runtime-*:0.1.0-dev15` is released. [Version 0.1.0-dev15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec/compose)

#### Dependencies Update

- To use the `0.1.0-dev15` version of Compose, you will need to update your dependencies according to the new code snippets shown above in [Declaring dependencies](https://developer.android.com/jetpack/androidx/releases/compose-runtime#declaring_dependencies).

**API Changes**

- `@Model` annotation is now deprecated. Use state and mutableStateOf as alternatives. This deprecation decision was reached after much careful discussion.

  #### Justification

  Rationale includes but is not limited to:
  - Reduces API surface area and concepts we need to teach
  - More closely aligns with other comparable toolkits (Swift UI, React, Flutter)
  - Reversible decision. We can always bring `@Model` back later.
  - Removes corner-case usage and difficult to answer questions about configuring `@Model` as things we need to handle
  - `@Model` data classes, equals, hashcode, etc.
  - How do I have some properties "observed" and others not?
  - How do I specify structural vs. referential equality to be used in observation?
  - Reduces "magic" in the system. Would reduce the likelihood of someone assuming system was smarter than it is (ie, it knowing how to diff a list)
  - Makes the granularity of observation more intuitive.
  - Improves refactorability from variable -\> property on class
  - Potentially opens up possibilities to do hand-crafted State-specific optimizations
  - More closely aligns with the rest of the ecosystem and reduces ambiguity towards immutable or us "embracing mutable state"

  #### Migration Notes

  Almost all existing usages of `@Model` are fairly trivially transformed in one of two ways. The example below has a `@Model` class with two properties just for the sake of example, and has it being used in a composable.

      @Model class Position(
       var x: Int,
       var y: Int
      )

      @Composable fun Example() {
       var p = remember { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p.x = it }
         onYChange={ p.y = it }
       )
      }

  #### Alternative 1: Use `State<OriginalClass>` and create copies.

  This approach is made easier with Kotlin's data classes. Essentially, make all previously `var` properties into `val` properties of a data class, and then use `state` instead of `remember`, and assign the state value to cloned copies of the original using the data class `copy(...)` convenience method.

  It's important to note that this approach only works when the only mutations to that class were done in the same scope that the `State` instance is created. If the class is internally mutating itself outside of the scope of usage, and you are relying on the observation of that, then the next approach is the one you will want to use.

      data class Position(
       val x: Int,
       val y: Int
      )

      @Composable fun Example() {
       var p by state { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p = p.copy(x=it) }
         onYChange={ p = p.copy(y=it) }
       )
      }

  #### Alternative 2: Use mutableStateOf and property delegates

  This approach is made easier with Kotlin's property delegates and the `mutableStateOf` API which allows you to create MutableState instances outside of composition. Essentially, replace all `var` properties of the original class with `var` properties with `mutableStateOf` as their property delegate. This has the advantage that the usage of the class will not change at all, only the internal implementation of it. The behavior is not completely identical to the original example though, as each property is now observed/subscribed to individually, so the recompositions you see after this refactor could be more narrow (a good thing).

      class Position(x: Int, y: Int) {
       var x by mutableStateOf(x)
       var y by mutableStateOf(y)
      }

      // source of Example is identical to original
      @Composable fun Example() {
       var p = remember { Position(0, 0) }
       PositionChanger(
         position=p,
         onXChange={ p.x = it }
         onYChange={ p.y = it }
       )
      }

  ([I409e8](https://android-review.googlesource.com/#/q/I409e8c158841eae1dd548b33f1ec80bb609cba31), [b/152050010](https://issuetracker.google.com/issues/152050010), [b/146362815](https://issuetracker.google.com/issues/146362815), [b/146342522](https://issuetracker.google.com/issues/146342522), [b/143413369](https://issuetracker.google.com/issues/143413369), [b/135715219](https://issuetracker.google.com/issues/135715219), [b/143263925](https://issuetracker.google.com/issues/143263925), [b/139653744](https://issuetracker.google.com/issues/139653744))
- Changes the code generation strategy of Compose's compiler. Prior to the change, the compose compiler would transform calls to composable functions. With this change, we now transform the body of a composable function and leave the callsite unaltered (mostly).

  This means that most of the logic communicating with the compose runtime happens at the start of the function body, instead of at the callsite.

  This should be a source-compatible change for all usage of compose. Most users of compose should not have to update any code as a result of this change.

  In order to support this work, the JVM signature of all composable functions has changed. A Composable function accepting a single parameter is transformed into a function accepting 3 parameters, the additional parameters are the Composer, a 'key' integer. a bitmask integer used to propagate metadata through calls.

  Compose now also transforms default arguments to a composable function. It does this without introducing an additional synthetic default overload of the function itself, so this change will result in fewer functions being defined.

  Known intentional behavioral changes resulting from this:
  1. Some calls will skip where they wouldn't have previously
  2. Composable expressions in default argument expressions are now correctly subscribed to and handled

  This work included some optimizations:
  1. The result of comparisons of parameters are propagated through the call graph to other composable functions. This will result in fewer comparisons at runtime, reduces the slot table size, as well as more skipping of composable functions that were previously not skipped
  2. Paremeters which are determined to be "static" at compile time are no longer compared or stored in the runtime. This reduces the number of comparisons and reduces slot table size.
  3. Control flow structure of the body of functions is used to minimize the number of groups that are generated. This reduces slot table size and results in less work for the runtime
  4. Unused dispatch and receiver parameters to functions are not included in determining skippability of the function if they are not used inside of the body of the function.

  Most breaking changes were for APIs that the compiler targets directly, and typical use of compose will not be affected:
  1. Composer::startExpr was removed
  2. Composer::endExpr was removed
  3. Composer::call was deprecated
  4. The non-varargs overloads of `key` have been removed. Use the `vararg` version going forward.
  5. The Pivotal annotation was deprecated. Use `key` as a replacement.
  6. ScopeUpdateScope::updateScope was changed to expect a Function3 instead of Function1
  7. restartableFunction and restartableFunctionN were updated to include additional compile time parameters
  ([I60756](https://android-review.googlesource.com/#/q/I607560574d83b4b6c1e68ff72cc4124c5f8c2602), [b/143464846](https://issuetracker.google.com/issues/143464846))
- Added sortWith and removeRange to MutableVector ([Icccf7](https://android-review.googlesource.com/#/q/Icccf73d3dd073dab0c7e67edf06afe77ec19bc67))

- Added default method implementations for
  CompositionLifecycleObserver ([I24289](https://android-review.googlesource.com/#/q/I2428951907b8256d698fc11291dc7d8c3b756d4c))

- Applier now requires a clear() method for disposing
  compositions ([Ibe697](https://android-review.googlesource.com/#/q/Ibe697b06ea885852731d029ef56da657b5f290dc))

- Added asMutableList() to MutableVector to allow it
  to be passed to public API without having to copy the entire
  list. ([I298df](https://android-review.googlesource.com/#/q/I298df3722ef0fa4bcce7cc0398b931ee934bb233))

- Added rememberCoroutineScope() to obtain a managed
  CoroutineScope in composition for launching jobs in response to events. ([I0e264](https://android-review.googlesource.com/#/q/I0e264f3f74fc520c6e57051000a513a52f2d07ce))

- MutableVector is a new collection that does not
  implement any of the standard Collection interface. This
  collection offers speed above other requirements and is
  intended to only be used in internal implementations. ([I8ebd6](https://android-review.googlesource.com/#/q/I8ebd6bf1407595d45eee2a22c1d1db3f38f4ab0b))

- Temporarily removed `StableMutableList` and `StableMutableMap`
  to avoid an issue in the version of Kotlin compose requires. These
  interfaces will be reintroduced once compose is updated to a version
  of Kotlin that doesn't have the issue.

  `SnapshotStateList` and `SnapshotStateMap` are now public but they will be
  deprecated once `StableMutableList` and `StableMutableMap` are restored. ([Ia7769](https://android-review.googlesource.com/#/q/Ia77691c6a5f523f63bd5d76cd6d7d7dc3f1afce1))
- add top-level withFrameNanos function for animation timing ([Ie34c5](https://android-review.googlesource.com/#/q/Ie34c53e2e105353acc5ad56df0e15e1bc2a2da08))

- @Untracked annotation has been deprecated. Replace with @ComposableContract(tracked=false) ([Id211e](https://android-review.googlesource.com/#/q/Id211e1c7c168c5171bbf3c844792890ee87d4fc2))

- RestartableFunction and associated APIs have been renamed to ComposableLambda, etc. These APIs were targeted only by the compiler so this should not affect source level compatibility normally. The rename was done primarily to communicate what this class is better when it shows up in stack traces ([I7eb25](https://android-review.googlesource.com/#/q/I7eb259b38d832c575810c6d61f2fd7d5fc035009))

- @Composable annotation is no longer valid on classes ([Ia5f02](https://android-review.googlesource.com/#/q/Ia5f02c4e27d7f96ee52206dc29896751dbf98fb2))

- `Ambient<T>` is now @Stable instead of @Immutable ([I0b4bb](https://android-review.googlesource.com/#/q/I0b4bbe1926fd68e04a7b7a66485c7a2e090f8c46))

- Prior to this change, the compose compiler plugin would non-trivially intercept calls to constructors inside of a @Composable function if there was an ([I5205a](https://android-review.googlesource.com/#/q/I5205af707238a70d600c105843cd99e88a5381e0), [b/158123804](https://issuetracker.google.com/issues/158123804))

- The Recompose composable is no longer a useful abstraction. Most recomposition should happen as a result of MutableState assignments. For anything beyond that, it is recommended that you use the `invalidate` function to trigger a recomposition of the current scope. ([Ifc992](https://android-review.googlesource.com/#/q/Ifc9926013c51c1db1e27e702a707bc1050f82fa6))

- Observe is no longer a useful abstraction. If you need to replicate it, its implementation can be replicated by just creating a composable function which executes a composable lambda parameter. For example, `@Composable fun Observe(body: @Composable () -> Unit) = body()` ([I40d37](https://android-review.googlesource.com/#/q/I40d37d6da7268c612231e0b91e1940c6c4fe2ac9))

- @Direct was deprecated in favor of @ComposableContract(restartable=false) ([If4708](https://android-review.googlesource.com/#/q/If47080869682224dff147fd11505c0bc3949fb20))

- Added an adapter for the recently introduced StateFlow which allows as to pre-populate the initial value so the returned State is non-nullable ([I61dd8](https://android-review.googlesource.com/#/q/I61dd845b2329f0e209175ed500a7f27f1520f471), [b/156233789](https://issuetracker.google.com/issues/156233789))

- Added an adapter for Flow. Example of the usage: val value by flow.collectAsState() ([If2198](https://android-review.googlesource.com/#/q/If219801db734613cc4ea411756141d372f889490), [b/153375923](https://issuetracker.google.com/issues/153375923))

- \[Mutable\]State property delegate operators moved to extensions
  to support Kotlin 1.4 property delegate optimizations. Callers must add
  imports to continue using `by state { ... }` or `by mutableStateOf(...)`. ([I5312c](https://android-review.googlesource.com/#/q/I5312cf7bdfa072cadc1be2de5d5f45ec53200f41))

- androidx.compose.ViewComposer has been moved to androidx.ui.node.UiComposer
  androidx.compose.Emittable has been removed. It was redundant with ComponentNode.
  androidx.compose.ViewAdapters has been removed. They are no longer a supported use case.
  Compose.composeInto has been deprecated. Use `setContent` or `setViewContent` instead.
  Compose.disposeComposition has been deprecated. Use the `dispose` method on the `Composition` returned by `setContent` instead.
  androidx.compose.Compose.subcomposeInto has moved to androidx.ui.core.subcomposeInto
  ComponentNode#emitInsertAt has been renamed to ComponentNode#insertAt
  ComponentNode#emitRemoveAt has been renamed to ComponentNode#removeAt
  ComponentNode#emitMode has been renamed to ComponentNode#move ([Idef00](https://android-review.googlesource.com/#/q/Idef00fba3a2e67d7034e31d580d69192e9018b5f))

- Updated the `ComposeFlags.COMPOSER_PARAM` flag to be `true`, which will change the code generation strategy for the compose plugin. At a high level, this causes @Composable functions to be generated with an additional synthetic parameter, which is passed through to subsequent @Composable calls in order for the runtime to properly manage execution. This is a significant binary breaking change, however, should preserve source-level compatibility in all sanctioned usage of compose. ([I7971c](https://android-review.googlesource.com/#/q/I7971ca1b6525440c38643953645fa388131e31f0))

- Breaking changes to the ambients API. See log and `Ambient<T>` documentation for details ([I4c7ee](https://android-review.googlesource.com/#/q/I4c7eea45f2b7bf41f8a8ba75fd667c06010469a9), [b/143769776](https://issuetracker.google.com/issues/143769776))

- Added ui-livedata - new artifact with an adapter for LiveData. Example of the usage: val value by liveData.observeAsState() ([Ie9e8c](https://android-review.googlesource.com/#/q/Ie9e8c37c952358186ab311d0d232c188003631f4), [b/150465596](https://issuetracker.google.com/issues/150465596))

- Rx adapters without explicit initial value are deprecated. Using null is not always the best default, for example when you have a List it is better to start with emptyList() or any other reasonable default ([I00025](https://android-review.googlesource.com/#/q/I00025b20be5441dc64edf3077c2e63800e1abf77), [b/161348384](https://issuetracker.google.com/issues/161348384))

- Added ui-rxjava2 - new artifact with adapters for RxJava2. Example of the usage: val value by observable.subscribeAsState() ([Ifab4b](https://android-review.googlesource.com/#/q/Ifab4b1eebfa0649716ffd3d9fc980a71ef30eb61), [b/153369097](https://issuetracker.google.com/issues/153369097))

- `savedInstanceState()` can now be used with nullable types ([I6847f](https://android-review.googlesource.com/#/q/I6847f1a78afc14061082993583a6fcfc374e3277), [b/153532190](https://issuetracker.google.com/issues/153532190))

- New listSaver() and mapSaver() to make it easier to write custom Saver objects ([I8cf68](https://android-review.googlesource.com/#/q/I8cf68efa3344c92d69a980efd4a737c5cac436fa), [b/152331508](https://issuetracker.google.com/issues/152331508))

- New functions: savedInstanceState() and rememberSavedInstanceState(). They are similar to state() and remember() but have a saved instance state support build in ([If1987](https://android-review.googlesource.com/#/q/If1987a758d18f9fa4ccfeb75011155304ee99cef), [b/152025209](https://issuetracker.google.com/issues/152025209))

**Bug Fixes**

- `runOnIdleCompose` renamed to `runOnIdle` ([I83607](https://android-review.googlesource.com/#/q/I836071f1c3c63d21417a531f336f8a93ca13f9ed))
- Made LayoutNode experimental API ([I4f2e9](https://android-review.googlesource.com/#/q/I4f2e93737020b0993f8ba5671e2a0a87f5de3ce2))
- androidx.ui.foundation.TextFieldValue and androidx.ui.input.EditorValue is deprecated. TextField, FilledTextField and CoreTextField composables that uses that type is also deprecated. Please use androidx.ui.input.TextFieldValue instead ([I4066d](https://android-review.googlesource.com/#/q/I4066d1f4d2e3e3514753aa3495680292dc55f89d), [b/155211005](https://issuetracker.google.com/issues/155211005))
- Removed deprecated DrawBackground API in favor of drawBackground extension APIs on Modifier. Refactored color, brush and paint drawBackground implementations to reduce code paths as well as remove requirement for Modifier to be created as part of composition. ([I0343a](https://android-review.googlesource.com/#/q/I0343a0d32684e77f9bc72c9cf68ce55d92ec575d))
- Updated higher level compose APIs that expose a Canvas to expose CanvasScope instead. This removes the need for consumers to maintain their own Paint objects. For consumers that still require access to a Canvas they can use the drawCanvas extension method which provides a callback to issue drawing commands with the underlying Canvas. ([I80afd](https://android-review.googlesource.com/#/q/I80afdf4c0a648962aa6ef1efc05b1d3b65757094))
- WithConstraints trailing lambda API has been changed. Now instead of two params it has a receiver scope which in addition to constraints and layoutDirection provides minWidth, maxWidth, minHeight and maxHeight properties in Dp ([I91b9a](https://android-review.googlesource.com/#/q/I91b9af740cd2613ddd4fe6d63cd539a46b52fc52), [b/149979702](https://issuetracker.google.com/issues/149979702))
- Added symmetric padding modifier. ([I39840](https://android-review.googlesource.com/#/q/I39840a44ea3ff9cbf17dc1c073b1d142d59b02ec))
- Updated wrapContentWidth and wrapContentHeight to expect vertical or horizontal Alignment rather than any Alignment. The gravity modifier was updated to accept vertical or horizontal Alignment. Row, Column and Stack were updated to support custom continuous Alignments. ([Ib0728](https://android-review.googlesource.com/#/q/Ib07281752fa9806a13e61823e00accb26f99c1f6))
- ui-text module is renamed as ui-text-core ([I57dec](https://android-review.googlesource.com/#/q/I57dec72ca50e7288e37c9272ef6ce8bcc485a83e))
- Improve DrawModifier API:
  - Made the receiver scope for draw() ContentDrawScope
  - Removed all parameters on draw()
  - DrawScope has same interface as former CanvasScope
  - ContentDrawScope has drawContent() method ([Ibaced](https://android-review.googlesource.com/#/q/Ibaced5feb8778510b8fe78e96f4fd3da1a6fda50), [b/152919067](https://issuetracker.google.com/issues/152919067))
- ColoredRect has been deprecated. Use `Box(Modifier.preferredSize(width, height).drawBackground(color))` instead. ([I499fa](https://android-review.googlesource.com/#/q/I499fa26b66b128943500fbdf9ba490d754adf561), [b/152753731](https://issuetracker.google.com/issues/152753731))
- Replaced Modifier plus operator with factory extension functions ([I225e4](https://android-review.googlesource.com/#/q/I225e444f50956d84e15ca4f1378b7f805d54e0ca))
- RowScope and ColumnScope members are now accessible outside Row and Column. ([I3a641](https://android-review.googlesource.com/#/q/I3a6415334c145f6a3f610d7852c4d2478371e6e6))
- Renamed LayoutFlexible to LayoutWeight. Renamed tight parameter to fill. ([If4738](https://android-review.googlesource.com/#/q/If4738c70c381e149ded400d657b5efd888ae5891))
- WithConstraints got LayoutDirection parameter ([I6d6f7](https://android-review.googlesource.com/#/q/I6d6f7d5fd9a4a0428e3ee188a9a3790e1cdaf083))
- Renamed background to DrawBackground and make it to be memorized by default ([Ia0bd3](https://android-review.googlesource.com/#/q/Ia0bd3f7657dc66ae6f492ccfcf88c44ba92bb7e0))
- Replaced ButtonStyle with distinct functions and removed text (string) overload. See updated samples for usage information. ([If63ab](https://android-review.googlesource.com/#/q/If63ab32bd3f12050a2d2f4b8c0cb044bc7144a6b), [b/146478620](https://issuetracker.google.com/issues/146478620), [b/146482131](https://issuetracker.google.com/issues/146482131))
- `runOnIdleCompose` and `runOnUiThread` are now global functions instead of methods on ComposeTestRule. ([Icbe8f](https://android-review.googlesource.com/#/q/Icbe8fd71d52144e855ccb4ce06a4677337be731a))

**External Contribution**

- Remove unneeded API such as Looper and Handler from Compose Runtime porting layer ([I6847d](https://android-review.googlesource.com/#/q/I6847daf0d70608673a8fe8b2bbf7f3b94fb762f1))
- Deprecate `Flow<T>.collectAsState()` with no initial value. Use `StateFlow<T>` or pass an explicit initial value instead. ([I63f98](https://android-review.googlesource.com/#/q/I63f98eabd19d74c87bc951677cef15c678aeae2f), [b/157674865](https://issuetracker.google.com/issues/157674865))