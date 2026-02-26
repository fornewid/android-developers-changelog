---
title: https://developer.android.com/jetpack/androidx/releases/lifecycle
url: https://developer.android.com/jetpack/androidx/releases/lifecycle
source: md.txt
---

# Lifecycle

[User Guide](https://developer.android.com/topic/libraries/architecture/lifecycle) [Code Sample](https://github.com/android/architecture-components-samples) [Codelab](https://codelabs.developers.google.com/codelabs/android-lifecycles/index.html?index#0) API Reference  
[androidx.lifecycle](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary)  
Lifecycle-aware components perform actions in response to a change in the lifecycle status of another component, such as activities and fragments. These components help you produce better-organized, and often lighter-weight code, that is easier to maintain.


This table lists all the artifacts in the `androidx.lifecycle` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| lifecycle-\* | [2.10.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.10.0) | - | - | [2.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0-alpha01) |
| lifecycle-viewmodel-navigation3 | [2.10.0](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.10.0) | - | - | [2.11.0-alpha01](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.11.0-alpha01) |

This library was last updated on: February 25, 2026

## Declaring dependencies

To add a dependency on Lifecycle, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

> [!NOTE]
> The APIs in `lifecycle-extensions` have been deprecated. Instead, add dependencies for the specific Lifecycle artifacts you need.

### Kotlin

### Groovy

```groovy
    dependencies {
        def lifecycle_version = "2.10.0"
        def arch_version = "2.2.0"

        // ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
        // ViewModel utilities for Compose
        implementation "androidx.lifecycle:lifecycle-viewmodel-compose:$lifecycle_version"
        // LiveData
        implementation "androidx.lifecycle:lifecycle-livedata-ktx:$lifecycle_version"
        // Lifecycles only (without ViewModel or LiveData)
        implementation "androidx.lifecycle:lifecycle-runtime-ktx:$lifecycle_version"
        // Lifecycle utilities for Compose
        implementation "androidx.lifecycle:lifecycle-runtime-compose:$lifecycle_version"

        // Saved state module for ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version"

        // ViewModel integration with Navigation3
        implementation "androidx.lifecycle:lifecycle-viewmodel-navigation3:2.11.0-alpha01"

        // Annotation processor
        kapt "androidx.lifecycle:lifecycle-compiler:$lifecycle_version"
        // alternately - if using Java8, use the following instead of lifecycle-compiler
        implementation "androidx.lifecycle:lifecycle-common-java8:$lifecycle_version"

        // optional - helpers for implementing LifecycleOwner in a Service
        implementation "androidx.lifecycle:lifecycle-service:$lifecycle_version"

        // optional - ProcessLifecycleOwner provides a lifecycle for the whole application process
        implementation "androidx.lifecycle:lifecycle-process:$lifecycle_version"

        // optional - ReactiveStreams support for LiveData
        implementation "androidx.lifecycle:lifecycle-reactivestreams-ktx:$lifecycle_version"

        // optional - Test helpers for LiveData
        testImplementation "androidx.arch.core:core-testing:$arch_version"

        // optional - Test helpers for Lifecycle runtime
        testImplementation "androidx.lifecycle:lifecycle-runtime-testing:$lifecycle_version"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        val lifecycle_version = "2.10.0"
        val arch_version = "2.2.0"

        // ViewModel
        implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version")
        // ViewModel utilities for Compose
        implementation("androidx.lifecycle:lifecycle-viewmodel-compose:$lifecycle_version")
        // LiveData
        implementation("androidx.lifecycle:lifecycle-livedata-ktx:$lifecycle_version")
        // Lifecycles only (without ViewModel or LiveData)
        implementation("androidx.lifecycle:lifecycle-runtime-ktx:$lifecycle_version")
        // Lifecycle utilities for Compose
        implementation("androidx.lifecycle:lifecycle-runtime-compose:$lifecycle_version")

        // Saved state module for ViewModel
        implementation("androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version")

        // ViewModel integration with Navigation3
        implementation("androidx.lifecycle:lifecycle-viewmodel-navigation3:2.11.0-alpha01")

        // Annotation processor
        kapt("androidx.lifecycle:lifecycle-compiler:$lifecycle_version")
        // alternately - if using Java8, use the following instead of lifecycle-compiler
        implementation("androidx.lifecycle:lifecycle-common-java8:$lifecycle_version")

        // optional - helpers for implementing LifecycleOwner in a Service
        implementation("androidx.lifecycle:lifecycle-service:$lifecycle_version")

        // optional - ProcessLifecycleOwner provides a lifecycle for the whole application process
        implementation("androidx.lifecycle:lifecycle-process:$lifecycle_version")

        // optional - ReactiveStreams support for LiveData
        implementation("androidx.lifecycle:lifecycle-reactivestreams-ktx:$lifecycle_version")

        // optional - Test helpers for LiveData
        testImplementation("androidx.arch.core:core-testing:$arch_version")

        // optional - Test helpers for Lifecycle runtime
        testImplementation ("androidx.lifecycle:lifecycle-runtime-testing:$lifecycle_version")
    }
    
```

### Java

### Groovy

```groovy
    dependencies {
        def lifecycle_version = "2.10.0"
        def arch_version = "2.2.0"

        // ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version"
        // LiveData
        implementation "androidx.lifecycle:lifecycle-livedata:$lifecycle_version"
        // Lifecycles only (without ViewModel or LiveData)
        implementation "androidx.lifecycle:lifecycle-runtime:$lifecycle_version"

        // Saved state module for ViewModel
        implementation "androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version"

        // Annotation processor
        annotationProcessor "androidx.lifecycle:lifecycle-compiler:$lifecycle_version"
        // alternately - if using Java8, use the following instead of lifecycle-compiler
        implementation "androidx.lifecycle:lifecycle-common-java8:$lifecycle_version"

        // optional - helpers for implementing LifecycleOwner in a Service
        implementation "androidx.lifecycle:lifecycle-service:$lifecycle_version"

        // optional - ProcessLifecycleOwner provides a lifecycle for the whole application process
        implementation "androidx.lifecycle:lifecycle-process:$lifecycle_version"

        // optional - ReactiveStreams support for LiveData
        implementation "androidx.lifecycle:lifecycle-reactivestreams:$lifecycle_version"

        // optional - Test helpers for LiveData
        testImplementation "androidx.arch.core:core-testing:$arch_version"

        // optional - Test helpers for Lifecycle runtime
        testImplementation "androidx.lifecycle:lifecycle-runtime-testing:$lifecycle_version"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        val lifecycle_version = "2.10.0"
        val arch_version = "2.2.0"

        // ViewModel
        implementation("androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version")
        // LiveData
        implementation("androidx.lifecycle:lifecycle-livedata:$lifecycle_version")
        // Lifecycles only (without ViewModel or LiveData)
        implementation("androidx.lifecycle:lifecycle-runtime:$lifecycle_version")

        // Saved state module for ViewModel
        implementation("androidx.lifecycle:lifecycle-viewmodel-savedstate:$lifecycle_version")

        // Annotation processor
        annotationProcessor("androidx.lifecycle:lifecycle-compiler:$lifecycle_version")
        // alternately - if using Java8, use the following instead of lifecycle-compiler
        implementation("androidx.lifecycle:lifecycle-common-java8:$lifecycle_version")

        // optional - helpers for implementing LifecycleOwner in a Service
        implementation("androidx.lifecycle:lifecycle-service:$lifecycle_version")

        // optional - ProcessLifecycleOwner provides a lifecycle for the whole application process
        implementation("androidx.lifecycle:lifecycle-process:$lifecycle_version")

        // optional - ReactiveStreams support for LiveData
        implementation("androidx.lifecycle:lifecycle-reactivestreams:$lifecycle_version")

        // optional - Test helpers for LiveData
        testImplementation("androidx.arch.core:core-testing:$arch_version")

        // optional - Test helpers for Lifecycle runtime
        testImplementation("androidx.lifecycle:lifecycle-runtime-testing:$lifecycle_version")
    }
    
```

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:413132+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=413132&template=1096619)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 2.11

### Version 2.11.0-alpha01

February 25, 2026

`androidx.lifecycle:lifecycle-*:2.11.0-alpha01` is released. Version 2.11.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ee621bea3237b1eab3c48eef4cf7ef7c7943b4bb..c640b9aa8e30b5db9ee258561ad1fc4bc947e69d/lifecycle).

**New Features**

- Support all Kotlin Multiplatform (KMP) targets in ViewModel-Compose. Decouple owner resolution from `LocalView` to allow platform hosts to provide a default `ViewModelStoreOwner` while maintaining `LocalView` as a safe fallback on Android. ([I09fab](https://android-review.googlesource.com/#/q/I09fab05e9ab9f8fb3a6fdbdf4247e5201710fe34), [b/434940570](https://issuetracker.google.com/issues/434940570), [Ic8526](https://android-review.googlesource.com/#/q/Ic8526f7e8ab9ffe58997333808a93bec7f9f2380), [b/478146897](https://issuetracker.google.com/issues/478146897))

**API Changes**

- Add a `toString` implementation to `ViewModelStore` that lists all stored keys to help streamline debugging. ([I0a6f4](https://android-review.googlesource.com/#/q/I0a6f48651211c317fca47e1491837bde2e0f4e34))
- Add a default implementation for `HasDefaultViewModelProviderFactory.defaultViewModelProviderFactory`, meaning you no longer need to override this property explicitly when implementing the interface. ([Ia7095](https://android-review.googlesource.com/#/q/Ia709580f9344ae5e77eabcc840a384c4bd516e1c))
- Annotate `ViewModel.onCleared` with `@EmptySuper` to explicitly indicate that overriding methods do not need to call `super.onCleared()`. ([I8c226](https://android-review.googlesource.com/#/q/I8c226596b028fd4bf39b9f440d047fdc82ff2eee))

## Version 2.10

### Version 2.10.0

November 19, 2025

`androidx.lifecycle:lifecycle-*:2.10.0` is released. Version 2.10.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/de92a2e4117ed83ceccc5bf636358c1df27d4bd6..ee621bea3237b1eab3c48eef4cf7ef7c7943b4bb/lifecycle).

**Important changes since 2.9.0:**

- Add a `rememberLifecycleOwner` composable to enable creating scoped lifecycles directly within the UI. This is useful for components that need to manage their own lifecycles independently such as a `HorizontalPager` that wants to only make the current page `RESUMED` or libraries like [Navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3#1.0.0):

      @Composable
      fun MyComposable() {
          // This LifecycleOwner is automatically moved to DESTROYED when
          // it leaves composition and its maxLifecycle is the maximum of either
          // the maxLifecycle you set or the Lifecycle.State of the parentLifecycleOwner
          val lifecycleOwner = rememberLifecycleOwner(
              maxLifecycle = RESUMED,
              parentLifecycleOwner = LocalLifecycleOwner.current,
          )
          CompositionLocalProvider(LocalLifecycleOwner provides lifecycleOwner) {
              val childLifecycleOwner = LocalLifecycleOwner.current
          }
      }

- The `lifecycle-viewmodel-navigation3` artifact provides a prebuilt integration for [Navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3#1.0.0), allowing you to enable scoping `ViewModel` instances to individual screens ('entries') by using the `rememberViewModelStoreNavEntryDecorator()` API:

      @Composable
      fun MyComposable() {
          NavDisplay(
              backStack = backStack,
              entryDecorators =
                  listOf(
                      rememberSaveableStateHolderNavEntryDecorator(),
                      // Add this line to automatically scope ViewModels to each entry
                      rememberViewModelStoreNavEntryDecorator(),
                  ),
              entryProvider = entryProvider {
                  // Add your entries here
              }
          }
      }

- Add a builder factory function for `CreationExtras`, providing a more convenient and idiomatic Kotlin API.

      override val defaultViewModelCreationExtras: CreationExtras
          // Use the CreationExtras builder to add in a custom value to the default
          // CreationExtras in your Activity or Fragment
          get() = super.defaultViewModelCreationExtras + CreationExtras {
              this[CustomKey] = "customValue"
         }

- Add native support for nullable types in `SavedStateHandle.saved`, simplifying saving and restoring nullable properties.

- Mark `SavedStateHandle` constructors as `@VisibleForTesting`.

- The minSdk has changed from API 21 to API 23.

### Version 2.10.0-rc01

November 05, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-rc01` is released. Version 2.10.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05..75dae7c6076e30667f6ec99ab8f3790ac42a9cc3/lifecycle).

### Version 2.10.0-beta01

October 22, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-beta01` is released. Version 2.10.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7b8a27d59a3cd5d0aa8259755193aadbd5c119da..46bcdef6281ae0f03c3a2bb2812edfc2c0e66d05/lifecycle).

**API Changes**

- `ViewModelStoreNavEntryDecoratorDefault` has been renamed to `ViewModelStoreNavEntryDecoratorDefaults`, with an 's'. ([I6d27b](https://android-review.googlesource.com/#/q/I6d27b3da1c0be758dfbd45d249bf2fdc2157f4e5), [b/444447434](https://issuetracker.google.com/issues/444447434))

**Bug Fixes**

- `rememberLifecycleOwner` no longer crashes if the owner receives an `Lifecycle.Event.ON_DESTROY` event before moving to `Lifeycle.State.CREATED`. ([I6f98e](https://android-review.googlesource.com/#/q/I6f98e927151c0febf1f8ea673ba19664615904b8), [b/444594991](https://issuetracker.google.com/issues/444594991))

### Version 2.10.0-alpha05

October 08, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-alpha05` is released. Version 2.10.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd..7b8a27d59a3cd5d0aa8259755193aadbd5c119da/lifecycle).

**API Changes**

- The `removeViewModelStoreOnPopCallback()` is now part of a `ViewModelStoreNavEntryDecoratorDefault` object which is where other platforms and implementations can call the default. ([Ia1f23](https://android-review.googlesource.com/#/q/Ia1f23d608671717ec56dbc54dc4e555b4d65a913), [b/444447434](https://issuetracker.google.com/issues/444447434))
- Refactored `ViewModelStoreNavEntryDecorator` from a function to a class to better reflect its functionality as a factory for `NavEntryDecorator`, and renamed the decorator's `shouldRemoveViewModelStore` parameter to `removeViewModelStoreOnPop` to clarify that this callback is invoked only when an entry is popped from the `backStack`. ([Iefdc5](https://android-review.googlesource.com/#/q/Iefdc582a213cfd177fd26862239980afd8f2de93), [b/444447434](https://issuetracker.google.com/issues/444447434))

### Version 2.10.0-alpha04

September 24, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-alpha04` is released. Version 2.10.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..eda15c8d8b0e8a4cdb256c81b44499364dbf0fcd/lifecycle).

**API Changes**

- Refactor the `LifecycleOwner` composable to `rememberLifecycleOwner`. The function now returns the `LifecycleOwner` directly. To provide this owner to a sub-composition, use `CompositionLocalProvider`. ([Ic57f0](https://android-review.googlesource.com/#/q/Ic57f031a67ea1687951a47c6a7f64996e5e86921), [b/444446629](https://issuetracker.google.com/issues/444446629))
- Add KMP stubs to lifecycle-viewmodel-navigation3 to enable JetBrains to provide forks that fill these targets and thus support CMP. ([I44a4c](https://android-review.googlesource.com/#/q/I44a4cc278ee27b59492384aebfa79bdd03f94b76))

### Version 2.10.0-alpha03

August 27, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-alpha03` is released. Version 2.10.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/d1a3af87c572a19851d3436392c73f54a2d9e9a8..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/lifecycle).

**API Changes**

- Update Compose to 1.9.0. ([I2b9de](https://android-review.googlesource.com/#/q/I2b9de4c8a0f1efb5e6e7e328a52152b89d79aa90))

### Version 2.10.0-alpha02

August 13, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-alpha02` is released. Version 2.10.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/90f45005ac103f49af0dfc59047d2aab9752b957..c359e97fece91f3767a7d017e9def23c7caf1f53/lifecycle).

**New Features**

- The `LifecycleOwner` composable can now create a **standalone root lifecycle** . By (explicitly) setting `parent = null`, the new lifecycle operates independently of any host (like an `Activity`, `Fragment` or `NavBackStackEntry`). It starts as soon as the composable enters the composition and is automatically destroyed when it leaves. ([I8dfbe](https://android-review.googlesource.com/#/q/I8dfbe99ecb67853e9303b01646257adeecf05f36), [b/433659048](https://issuetracker.google.com/issues/433659048))

      @Composable
      fun IndependentComponent() {
          // Create a standalone lifecycle, not tied to the parent Activity/Fragment.
          LifecycleOwner(parent = null) {
              val rootLifecycle = LocalLifecycleOwner.current.lifecycle
          }
      }

**API Changes**

- In the `LifecycleOwner` composable, the `parentLifecycleOwner` parameter has been renamed to `parent`. ([I080bc](https://android-review.googlesource.com/#/q/I080bce9d1696c57704b70359b7e1abab9a75296b))

**Bug Fixes**

- `LifecycleOwner` composable now correctly moves its lifecycle to `DESTROYED` upon disposal. This prevents potential leaks for external code that holds a reference to the lifecycle. ([I9e5b7](https://android-review.googlesource.com/#/q/I9e5b7149e64ad44bd8778c0355a0bce045971767), [b/433659048](https://issuetracker.google.com/issues/433659048))
- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

**External Contribution**

- Remove unnecessary internal backing fields from `LifecycleOwner`. Thanks Jake Wharton for the contribution. ([Ideddb](https://android-review.googlesource.com/#/q/Ideddb802e4aa519a14c9f1b2f080818347916385))

### Version 2.10.0-alpha01

July 30, 2025

`androidx.lifecycle:lifecycle-*:2.10.0-alpha01` is released. Version 2.10.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a4f6bbd05dfc763e954251490e19be98bcf05360..90f45005ac103f49af0dfc59047d2aab9752b957/lifecycle).

**New Features**

- Add a `LifecycleOwner` composable to enable creating scoped lifecycles directly within the UI. This is useful for components that need to manage their own lifecycles independently. For an example of how Navigation3 integrates this new composable, see [aosp/3708610](https://r.android.com/3708610). ([76cbf7](https://android-review.googlesource.com/#/q/I70c9c6206ac3f3e1447e4e722e8e5f9861cb880e))

      @Composable
      fun MyComposable() {
          LifecycleOwner(
              maxLifecycle = RESUMED,
              parentLifecycleOwner = LocalLifecycleOwner.current,
          ) {
              val childLifecycleOwner = LocalLifecycleOwner.current
          }
      }

**API Changes**

- Add a builder factory function for `CreationExtras`, providing a more convenient and idiomatic Kotlin API. ([Iab2bd](https://android-review.googlesource.com/#/q/Iab2bd8bfb3cac673f88aa78e25de27044984271d))
- Add native support for nullable types in `SavedStateHandle.saved`, simplifying saving and restoring nullable properties. ([I54d69](https://android-review.googlesource.com/#/q/I54d690589fd099b565edc31df73bbdb7ed16f738), [b/421325690](https://issuetracker.google.com/issues/421325690))
- Mark `SavedStateHandle` constructors as `@VisibleForTesting`. ([Iff0e0](https://android-review.googlesource.com/#/q/Iff0e06b2805ff423e496b56369814f6acfeec50b), [b/408002794](https://issuetracker.google.com/issues/408002794))

## Version 2.9

### Version 2.9.4

September 17, 2025

`androidx.lifecycle:lifecycle-*:2.9.4` is released. Version 2.9.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8760ebe0c4b4174e0a3933fe6162e46ca06f8d80..de92a2e4117ed83ceccc5bf636358c1df27d4bd6/lifecycle).

**Bug Fixes**

- Fixed an error with the Compose Compiler plugin not being applied that caused Lifecycle KMP artifacts to be broken. ([Ie95bc](https://android-review.googlesource.com/#/q/Ie95bc1567a9d2afee9b276057c8a5cb8ed1a4f29), [b/443096483](https://issuetracker.google.com/443096483), [b/443965665](https://issuetracker.google.com/443965665))

### Version 2.9.3

August 27, 2025

`androidx.lifecycle:lifecycle-*:2.9.3` is released. Version 2.9.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a4f6bbd05dfc763e954251490e19be98bcf05360..8760ebe0c4b4174e0a3933fe6162e46ca06f8d80/lifecycle).

**New Features**

- Add new Kotlin Multiplatform (KMP) targets to Lifecycle `*-compose` artifacts. Lifecycle now supports the following platforms in total: JVM (Android and Desktop), Native (Linux, iOS, watchOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([I0a0e4](https://android-review.googlesource.com/#/q/I0a0e4b4c58cbd347336682ddc1acbca252591640))

**Bug Fixes**

- Update `androidx.annotation` to 1.9.1 ([Ic9e4f](https://android-review.googlesource.com/#/q/Ic9e4f34d55e1532167435c843590b2293a6ed1d9), [b/397701294](https://issuetracker.google.com/issues/397701294))

### Version 2.9.2

July 16, 2025

`androidx.lifecycle:lifecycle-*:2.9.2` is released. Version 2.9.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a4f6bbd05dfc763e954251490e19be98bcf05360/lifecycle).

**Bug Fixes**

- Added new Kotlin Multiplatform (KMP) targets to Lifecycle artifacts. Lifecycle now supports the following platforms in total: JVM (Android and Desktop), Native (Linux, iOS, watchOS, macOS, MinGW), and Web (JavaScript, WasmJS). Note that no new KMP targets have been added to the `*-compose` artifacts, as this depends on the stable release of Compose 1.9. ([I01cb8](https://android-review.googlesource.com/#/q/I01cb822e5266e06095517501458657cf9972c67e)).

**Dependency updates**

- Lifecycle now depends on [Annotation `1.9.1`](https://developer.android.com/jetpack/androidx/releases/annotation#1.9.1) to enable support for the new KMP targets ([Ic9e4f](https://android-review.googlesource.com/#/q/Ic9e4f34d55e1532167435c843590b2293a6ed1d9), [b/397701294](https://issuetracker.google.com/issues/397701294)).

### Version 2.9.1

June 4, 2025

`androidx.lifecycle:lifecycle-*:2.9.1` is released. Version 2.9.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ac0ac96d77785db18140c9bad8f1de95f2418806..ae1648c05b723380a53f708fa745357395a7bf0e/lifecycle).

**Bug Fixes**

- Fix `SavedStateHandle.remove(key)` not clearing `SavedStateHandle.getMutableStateFlow(key)` states. ([d5f939](https://android-review.googlesource.com/q/commit:d5f9390a213fb05892f0db98bfd826be98f081a7), [b/418746333](https://issuetracker.google.com/418746333))

### Version 2.9.0

May 7, 2025

`androidx.lifecycle:lifecycle-*:2.9.0` is released. Version 2.9.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/79d624a3b7368c83b4706639bab22beed44ba338..ac0ac96d77785db18140c9bad8f1de95f2418806/lifecycle).

**Important changes since 2.8.0**

- A new `androidx.lifecycle:lifecycle-viewmodel-testing` KMP artifact is available that provides a [`ViewModelScenario`](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/testing/ViewModelScenario) class for testing `ViewModels` in isolation, with support for `onCleared` and `SavedStateHandle` as well as testing process death and recreation via `recreate()`.
- Add `getMutableStateFlow` to `SavedStateHandle` to return a `MutableStateFlow`. This new function is key-exclusive and cannot be used with `getLiveData`. An exception will be thrown if you try to use both to access the same state.
- `CreationExtras` now includes map-like operator overloads to enable idiomatic manipulation of content in Kotlin. It allows the use of `in`, `+=`, and `+` with `CreationExtras`.

**KotlinX Serialization Support**

- With the support of KotlinX Serialization added in [SavedState `1.3.0`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.3.0), we have introduced `saved`, a lazy property delegate, to make it easy to store `@Serializable` classes in a `SavedStateHandle` and have those classes automatically be restored across process death and recreation. Please note the `saved` delegate is lazy and will not call the `init` lambda or save anything into the `SavedStateHandle` until it is accessed.

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      class MyViewModel(handle: SavedStateHandle) : ViewModel() {
          var person by handle.saved { Person("John", "Doe") }

          fun onPersonChanged(person: Person) {
              this.person = person
          }
      }

**Kotlin Multiplatform**

- The `lifecycle-testing` module is now KMP compatible including APIs like `TestLifecycleOwner`.
- The `lifecycle-viewmodel-savedstate` module is now KMP compatible including APIs like `SavedStateHandle`.
- The `androidx.compose.ui.platform.LocalLifecycleOwner` is now available in the common source set.
- `NewInstanceFactory` is now available on JVM Desktop and Android targets.

**Behavior Changes**

- The `Lifecycle.DESTROYED` state is terminal, and any attempt to move a `Lifecycle` from it to any other state will now result in an `IllegalStateException`.
- `SavedStateHandle` no longer includes any `SavedStateProvider.saveState()` where the returned `Bundle` is empty.

### Version 2.9.0-rc01

April 23, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-rc01` is released. Version 2.9.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/64e37c2d3d42028c9ab14070feedcab6b5a9e982..79d624a3b7368c83b4706639bab22beed44ba338/lifecycle).

**Lint API Compatibility Warning**

- JetBrains changed `KaCallableMemberCall` from [a class to an interface](https://cs.android.com/android-studio/kotlin/+/110e9e27b760bdf6902642926998f94f4afea800), which breaks binary compatibility. This can cause crashes if your project's AGP version differs from the version used to compile lint checks. This update was made in [aosp/3577172](https://r.android.com/3577172) but was missing from the release notes --- we're clarifying it here. **Recommended fix:** Update to the latest stable AGP. If you can't fully update, use `android.experimental.lint.version` to align lint checks with your AGP version --- see [Compose Runtime behavior changes](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.9.0-alpha01) for details.

### Version 2.9.0-beta01

April 9, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-beta01` is released. Version 2.9.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..64e37c2d3d42028c9ab14070feedcab6b5a9e982/lifecycle).

**API Changes**

- `Lifecycle ViewModel Compose` now uses the same Kotlin Multiplatform setup as [Compose Runtime 1.7.1](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.7.1) and higher - the `-desktop` artifacts are now removed and `-jvmStubs` and `-linuxx64Stubs` artifacts have been added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts. ([I5cb14](https://android-review.googlesource.com/#/q/I5cb14cb1dc5bc462961763252b2b3726f85145cb), [b/406592090](https://issuetracker.google.com/issues/406592090))

**Dependency Updates**

- This library now targets Kotlin 2.0 language level and requires KGP 2.0.0 or newer. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- `Lifecycle ViewModel Compose` now depends on Compose 1.7.8. ([I5cb14](https://android-review.googlesource.com/#/q/I5cb14cb1dc5bc462961763252b2b3726f85145cb), [b/406592090](https://issuetracker.google.com/issues/406592090))

### Version 2.9.0-alpha13

March 26, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-alpha13` is released with no notable public changes. Version 2.9.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a145e052ae61e272e91ffe285e9451b8ab71870..78132378b67c86698d1ade3dc368c9f15d738a71/lifecycle).

### Version 2.9.0-alpha12

March 12, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-alpha12` is released. Version 2.9.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e8ad418db17c5154100358a9672dc9c3ddbaf12f..7a145e052ae61e272e91ffe285e9451b8ab71870/lifecycle).

**API Changes**

- Add `@MainThread` annotation to `ViewModelProvider.get` in all supported KMP platforms. ([I7e8dd](https://android-review.googlesource.com/#/q/I7e8ddcd37a714fe511719aea74650f48acb85847), [b/397736115](https://issuetracker.google.com/issues/397736115))
- Rename `SavedState*Delegates` to `SavedState*Delegate`. ([I8589b](https://android-review.googlesource.com/#/q/I8589b62294646cb4529869228ea0185dac6087e6), [b/399629301](https://issuetracker.google.com/issues/399629301))

### Version 2.9.0-alpha11

February 26, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-alpha11` is released. Version 2.9.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/679b78391f81554a53123f7dfb1150b72c183307..e8ad418db17c5154100358a9672dc9c3ddbaf12f/lifecycle).

**API Changes**

- Add `SavedStateConfig` parameter to `saved()` delegates ([I39b3a](https://android-review.googlesource.com/#/q/I39b3a73d139c1d4c2a5fd01151679252dab67ad0))

### Version 2.9.0-alpha10

February 12, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-alpha10` is released. Version 2.9.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/3671eefdf920941dd90f135e8dd0caf9fd4cb14c..679b78391f81554a53123f7dfb1150b72c183307/lifecycle).

**API Changes**

- Move `MutableStateSerializer` to `savedstate-compose` from `lifecycle-viewmodel-compose`. ([I4f690](https://android-review.googlesource.com/#/q/I4f690e41dc5619d185784409170943abeb0f0550), [b/378895074](https://issuetracker.google.com/issues/378895074))

**External Contribution**

- Adds a new Lint issue for calling `Lifecycle::currentState` in composition, instead suggesting using `currentStateAsalue().value` to ensure that changes in the Lifecycle state correctly cause recomposition. Thanks Steven Schoen! ([Iad484](https://android-review.googlesource.com/#/q/Iad484fad72149f67f263fc3e0d4799e939e93f95))

### Version 2.9.0-alpha09

January 29, 2025

`androidx.lifecycle:lifecycle-*:2.9.0-alpha09` is released. Version 2.9.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..3671eefdf920941dd90f135e8dd0caf9fd4cb14c/lifecycle).

**New Features**

- Add `MutableStateSerializer` for serializing `androidx.compose.runtime.MutableState`. ([Idfc48](https://android-review.googlesource.com/#/q/Idfc489d9313461bddd0046052d0f6a41644e7712), [b/378895074](https://issuetracker.google.com/issues/378895074))

**API Changes**

- Replace overloaded `SavedStateHandle.saved()` delegate functions with default parameters ([Icd1c1](https://android-review.googlesource.com/#/q/Icd1c1e64c3df58fc7505bef99494ef168a0268bb))
- `AbstractSavedStateViewModelFactory` is deprecated as it creates a `SavedStateHandle` for every `ViewModel`, causing unnecessary overhead. Use `ViewModelProvider.Factory` with `CreationExtras.createSavedStateHandle` instead for more efficient `ViewModel` creation. ([Ia920b](https://android-review.googlesource.com/#/q/Ia920b66ccabde85a105cf4e6f80aa980270098ee), [b/388590327](https://issuetracker.google.com/issues/388590327))

### Version 2.9.0-alpha08

December 11, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha08` is released. Version 2.9.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0dc1e27ead8f6b0c810ea4c8fc9c650507866085..46295bc0b75a16f452e8e0090e8de41073d4dbb6/lifecycle).

**New Features**

- Add `ViewModelScenario.recreate` to simulate a System Process Death recreating the `ViewModel` under test and all associated components. ([Id6a69](https://android-review.googlesource.com/#/q/Id6a696888ce900c573e47c6c93e4ac9df1881e6b), [b/381063087](https://issuetracker.google.com/issues/381063087))
- `LifecycleOwner` and `ViewModelStoreOwner` instances retrieved via their respective `findViewTree` APIs can now be resolved through disjoint parents of a view, such as a `ViewOverlay`. See the release notes of core or the documentation in `ViewTree.setViewTreeDisjointParent` for more information on disjoint view parents. ([I800f4](https://android-review.googlesource.com/#/q/I800f4616721ada959cbc8123a919dbbf199110c4))

**API Changes**

- Make the namings and package organization more consistent with `SavedStateRegistryOwnerDelegate` ([I8c135](https://android-review.googlesource.com/#/q/I8c1353eedd7299f885ce45b7d85deb4a24c557e4), [b/376026744](https://issuetracker.google.com/issues/376026744))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler). ([Ie4340](https://android-review.googlesource.com/#/q/Ie43402aa3b0aca97c4671b421b083365f13b4eb4), [b/326456246](https://issuetracker.google.com/issues/326456246))
- Document `ViewModel.onCleared` clearing sequence. ([I586c7](https://android-review.googlesource.com/#/q/I586c7a6e962a2ff6227a6cd2707e0fcd73b66575), [b/363984116](https://issuetracker.google.com/issues/363984116))

### Version 2.9.0-alpha07

November 13, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha07` is released. Version 2.9.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..0aac1878823c58d5a7b1eee060cc79d1b38b4996/lifecycle).

**Kotlin Multiplatform Compatibility**

- Lifecycle `ViewModel SavedState` is now KMP compatible. This allows you to use `SavedStateHandle` in common code. ([Ib6394](https://android-review.googlesource.com/#/q/Ib63947f53600724de5ebf6c0e64c17c305592b2f), [b/334076622](https://issuetracker.google.com/issues/334076622))

**KotlinX Serialization Support**

- With the support of KotlinX Serialization added in [SavedState `1.3.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.3.0-alpha05), we have introduced `saved`, a lazy property delegate, to make it easy to store `@Serializable` classes in a `SavedStateHandle` and have those classes automatically be restored across process death and recreation. Please note the `saved` delegate is lazy and will not call the `init` lambda or save anything into the `SavedStateHandle` until it is accessed. ([I47a88](https://android-review.googlesource.com/#/q/I47a88d7bc335db7e22a9e6c05da38c2a8e012331), [b/376026744](https://issuetracker.google.com/issues/376026744))

      @Serializable
      data class Person(val firstName: String, val lastName: String)

      class MyViewModel(handle: SavedStateHandle) : ViewModel() {
          var person by handle.saved { Person("John", "Doe") }

          fun onPersonChanged(person: Person) {
              this.person = person
          }
      }

**API Changes**

- Add `getMutableStateFlow` to `SavedStateHandle` to return a `MutableStateFlow`. This new function is key-exclusive and cannot be used with `getLiveData`. An exception will be thrown if you try to use both to access the same state. ([I04a4f](https://android-review.googlesource.com/#/q/I04a4f0b470530a8993b467858abc45ecd2b42527), [b/375408415](https://issuetracker.google.com/issues/375408415))

### Version 2.9.0-alpha06

October 30, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha06` is released. Version 2.9.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/lifecycle).

**Behavior Changes**

- The `Lifecycle.DESTROYED` state is terminal, and any attempt to move a `Lifecycle` from it to any other state will now result in an `IllegalStateException`. ([I116c4](https://android-review.googlesource.com/#/q/I116c40ccb6a7a4807072ecf85ed4cf5ceca07568), [b/370577987](https://issuetracker.google.com/issues/370577987))
- `SavedStateHandle` no longer includes any `SavedStateProvider.saveState()` where the returned `Bundle` is empty. ([I910b5](https://android-review.googlesource.com/#/q/I910b58ff45d036c700a2f3ad93ea9db1d7284e52), [b/370577987](https://issuetracker.google.com/issues/370577987))

**Bug Fixes**

- `Lifecycle.eventFlow` now correctly complete when `Lifecycle` is `DESTROYED` ([I293b2](https://android-review.googlesource.com/#/q/I293b274b166de819115e249b624117f0492ed67b), [b/374043130](https://issuetracker.google.com/issues/374043130))

### Version 2.9.0-alpha05

October 16, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha05` is released with no notable changes. Version 2.9.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/lifecycle).

### Version 2.9.0-alpha04

October 2, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha04` is released. Version 2.9.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/lifecycle).

**Kotlin Multiplatform**

- The `lifecycle-viewmodel-savedstate` module is now configured to be KMP compatible in preparation for APIs like `SavedStateHandle` being made available in the common source set in a future release. ([I503ed](https://android-review.googlesource.com/#/q/I503edb3551108b6c4877c17767a787dda4aaaf4c), [I48764](https://android-review.googlesource.com/#/q/I48764a7a611bc102a08a6caf941d609e7576a350), [b/334076622](https://issuetracker.google.com/issues/334076622))

### Version 2.9.0-alpha03

September 18, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha03` is released. Version 2.9.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/71a0e55934198cacb4c897d9b20e26e2b7275988..0431b84980e97d6bafdfda7c9038bc4d9529564f/lifecycle).

**Bug Fixes**

- From [Lifecycle `2.8.6`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.8.6): The `NullSafeMutableLiveData` Lint error has improved support for smart casts, avoiding false positives. ([85fed6](https://android.googlesource.com/platform/frameworks/support/+/85fed6d07668f2e903172592580d8076cb6da80a), [b/181042665](https://issuetracker.google.com/181042665))

**Dependency Updates**

- From [Lifecycle `2.8.6`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.8.6): Lifecycle Runtime Compose now depends on [Compose Runtime `1.7.1`](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.7.1)
- Lifecycle Runtime now depends on [ProfileInstaller `1.4.0`](https://developer.android.com/jetpack/androidx/releases/jetpack/androidx/releases/profileinstaller#1.4.0)

### Version 2.9.0-alpha02

September 4, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha02` is released. Version 2.9.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c8cb8f02adb648763c096b032f887895619c2d2e..71a0e55934198cacb4c897d9b20e26e2b7275988/lifecycle).

**Bug Fixes**

- From [Lifecycle `2.8.5`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.8.5): Update the `androidx.lifecycle.ReportFragment` ProGuard rules to allow obfuscation . ([ff898e1](https://android.googlesource.com/platform/frameworks/support/+/ff898e1b01a9d3df1a205d8a374537a801e76289))

**External Contribution**

- Move `androidx.compose.ui.platform.LocalLifecycleOwner` to common source set (KMP). Thanks Ivan Matkov from JetBrains for the contribution. ([8cd5d03](https://android.googlesource.com/platform/frameworks/support/+/8cd5d03e92db33899c521bd7172a29f2c2db5114))
- From [Lifecycle `2.8.5`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.8.5): SavedStateHandle.saveable\` extension delegate now supports nullable values. Thanks Roman Kalukiewicz for the contribution. ([0d78ea6](https://android.googlesource.com/platform/frameworks/support/+/0d78ea6ac30db5624315952b4bd62ff232991f40))

### Version 2.9.0-alpha01

August 7, 2024

`androidx.lifecycle:lifecycle-*:2.9.0-alpha01` is released. Version 2.9.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c8cb8f02adb648763c096b032f887895619c2d2e/lifecycle).

**Kotlin Multiplatform**

- `lifecycle-testing` is now KMP compatible. ([Iea41e](https://android-review.googlesource.com/#/q/Iea41e975e31e22b3cf7a994c14e62454b9588b46))
- Add support for `linuxArm64` kotlin multiplatform target ([I139d3](https://android-review.googlesource.com/#/q/I139d36226a3d06d9768bd63302de98b576a12a48), [b/338268719](https://issuetracker.google.com/issues/338268719))

**New Features**

- A new `androidx.lifecycle:lifecycle-viewmodel-testing` KMP artifact is available that provides a [`ViewModelScenario`](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/testing/ViewModelScenario) class for testing ViewModels in isolation, with support for `onCleared` (all platforms) and `SavedStateHandle` (Android only). ([337f68d](https://android.googlesource.com/platform/frameworks/support/+/337f68d7ae82f8eaceba983736bfa10ad1f1a0b9), [c9b3409](https://android.googlesource.com/platform/frameworks/support/+/c9b3409fcde227edba6b2ee6f9baa89c6b43081c), [9799a95c](https://android.googlesource.com/platform/frameworks/support/+/9799a95c1fc5e6d976d693f5a3fcb74ebe1beb4b), [b/264602919](https://issuetracker.google.com/264602919))
- Creating a `ViewModel` with `ViewModelProvider` is now thread safe; `@MainThread` annotations have been removed. ([Ifd978](https://android-review.googlesource.com/#/q/Ifd97842e103a029e1aeeeb5cd57dcb86b8770cf4), [b/237006831](https://issuetracker.google.com/issues/237006831))

**API Changes**

- Add the `CreationExtras.Key()` factory function to simplify the creation of anonymous `CreationExtras.Key` objects. ([I970ee](https://android-review.googlesource.com/#/q/I970ee39e7baf5c0e942a63eb7e175ba1f0de08e5))
- `CreationExtras` now includes map-like operator overloads to enable idiomatic manipulation of content in Kotlin. It allows the use of `in`, `+=`, and `+` with `CreationExtras`. ([Ib4353](https://android-review.googlesource.com/#/q/Ib43532fafb837bf35424d50836e2382d9b4825db))
- `CreationExtras` now implements `equals`, `hashCode`, and `toString` methods. ([Ib4353](https://android-review.googlesource.com/#/q/Ib43532fafb837bf35424d50836e2382d9b4825db))
- `NewInstanceFactory` is now available on JVM Desktop and Android targets. ([d3d0892](https://android.googlesource.com/platform/frameworks/support/+/d3d08924092add88321694bd37611ca911c7613b))
- Inline extension property to expose underlying Application safely in Kotlin language version 2.0 ([I39df2](https://android-review.googlesource.com/#/q/I39df26afb69744f6178d69e11c1d3b2b014a5886))

**Bug Fixes**

- Removed manual outlining of access to new platform APIs since this happens automatically via API modeling when using R8 with AGP 7.3 or later (e.g. R8 version 3.3) and for all builds when using AGP 8.1 or later (e.g. D8 version 8.1). Clients who are not using AGP are advised to update to D8 version 8.1 or later. See [this article](https://medium.com/androiddevelopers/mitigating-soft-verification-issues-in-r8-and-d8-7e9e06827dfd) for more details. ([If6b4c](https://android-review.googlesource.com/#/q/If6b4ccfca0a943b45971a422b58949b13a10bada), [b/345472586](https://issuetracker.google.com/issues/345472586))

## Version 2.8

### Version 2.8.7

October 30, 2024

`androidx.lifecycle:lifecycle-*:2.8.7` is released. Version 2.8.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/68c770fd5ee88b093114c4361b9cc2cd3c436bb7..b635f95bbd59699533b4954f192710b833fb81a5/lifecycle).

**API Changes**

- [`androidx.compose.ui.platform.LocalLifecycleOwner`](http://androidx.compose.ui.platform.LocalLifecycleOwner) is now available in the common source set (KMP). ([6a3f5b3](https://android.googlesource.com/platform/frameworks/support/+/6a3f5b39ca1d24cbdd75950f9d9cdbb5d2aa126d))
- `lifecycle-runtime-compose`: `desktop` artifacts were removed and `-jvmStubs` and `-linuxx64Stubs` artifacts were added. None of these targets are meant to be used, they are placeholders to help Jetbrains Compose efforts. ([6a3f5b3](https://android.googlesource.com/platform/frameworks/support/+/6a3f5b39ca1d24cbdd75950f9d9cdbb5d2aa126d))

### Version 2.8.6

September 18, 2024

`androidx.lifecycle:lifecycle-*:2.8.6` is released. Version 2.8.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1923636d71735aa7f25cd267a3ef7adc2e6af530..68c770fd5ee88b093114c4361b9cc2cd3c436bb7/lifecycle).

**Bug Fixes**

- The `NullSafeMutableLiveData` Lint error has improved support for smart casts, avoiding false positives. ([85fed6](https://android.googlesource.com/platform/frameworks/support/+/85fed6d07668f2e903172592580d8076cb6da80a), [b/181042665](https://issuetracker.google.com/181042665))

**Dependency Updates**

- Lifecycle Runtime Compose now depends on [Compose Runtime `1.7.1`](https://developer.android.com/jetpack/androidx/releases/compose-runtime#1.7.1)

### Version 2.8.5

September 4, 2024

`androidx.lifecycle:lifecycle-*:2.8.5` is released. Version 2.8.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e878847bccb7129bf31369a274059013b3a3c240..1923636d71735aa7f25cd267a3ef7adc2e6af530/lifecycle).

**Bug Fixes**

- Update the `androidx.lifecycle.ReportFragment` ProGuard rules to allow obfuscation . ([ff898e1](https://android.googlesource.com/platform/frameworks/support/+/ff898e1b01a9d3df1a205d8a374537a801e76289))

**External Contribution**

- `SavedStateHandle.saveable` extension delegate now supports nullable values. Thanks Roman Kalukiewicz for the contribution. ([0d78ea6](https://android.googlesource.com/platform/frameworks/support/+/0d78ea6ac30db5624315952b4bd62ff232991f40))

### Version 2.8.4

July 24, 2024

`androidx.lifecycle:lifecycle-*:2.8.4` is released. Version 2.8.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/92cc6e5d71efd12345ce7ba558cbc2a29926e9ac..e878847bccb7129bf31369a274059013b3a3c240/lifecycle).

**Bug Fixes**

- `LiveData.asFlow()` now correctly handles cases where the returned Flow is immediately completed after receiving a value already set on the `LiveData` (for example, when using `take(1)`). ([I9c566](https://android-review.googlesource.com/#/q/I9c56697c40907f9cee43f89f7ee1aa01adb470b1))
- `Lifecycle*Effect` completion is now idempotent (i.e., if the `onStopOrDispose` was called because of the Lifecycle being stopped, it won't be called a second time upon disposal unless the Lifecycle goes back up to `STARTED` again). ([I5f607](https://android-review.googlesource.com/#/q/I5f607934fb725f98c018b567e6e2f0052c7e8a69), [b/352364595](https://issuetracker.google.com/issues/352364595))

### Version 2.8.3

July 1, 2024

`androidx.lifecycle:lifecycle-*:2.8.3` is released. Version 2.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/86a54e23482b320e083f9a337814c7fe4f78e9a3..92cc6e5d71efd12345ce7ba558cbc2a29926e9ac/lifecycle).

**Bug Fixes**

- Fixed an issue with Lifecycle 2.8's backward compatibility with Compose 1.6.0 and lower when using code shrinking. ([aosp/3133056](https://android-review.googlesource.com/3133056), [b/346808608](https://issuetracker.google.com/346808608))

### Version 2.8.2

June 12, 2024

`androidx.lifecycle:lifecycle-*:2.8.2` is released. Version 2.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b390c8d82bf426c9fb727016dc2423891ecd1735..86a54e23482b320e083f9a337814c7fe4f78e9a3/lifecycle).

**Bug Fixes**

- Fixed `CompositionLocal LocalLifecycleOwner not present` errors when using Lifecycle 2.8.X with Compose 1.6.X or earlier - you can now use Lifecycle 2.8.2 with any version of Compose without any workarounds required. ([aosp/3105647](https://android-review.googlesource.com/3105647), [b/336842920](https://issuetracker.google.com/336842920))
- `ViewModelProvider` will no longer crash when mixing previous versions of `compileOnly` Lifecycle dependencies with versions 2.8+, fixing issues with libraries such as LeakCanary. ([I80383](https://android-review.googlesource.com/#/q/I803839b1c34bc8c70d6ebeb9ba90c426b340416c), [b/341792251](https://issuetracker.google.com/issues/341792251))

### Version 2.8.1

May 29, 2024

`androidx.lifecycle:lifecycle-*:2.8.1` is released. Version 2.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7ad6b8bbf8fa3d5a3c97feca6c52a1a2bf98a622..b390c8d82bf426c9fb727016dc2423891ecd1735/lifecycle).

**Bug Fixes**

- `lifecycle-viewmodel-compose` now only has a common dependency on `compose-runtime`, removing its common dependency on `compose-ui`. The Android artifact retains its `compose-ui` for compatibility. ([aosp/3079334](https://android-review.googlesource.com/3079334), [b/339562627](https://issuetracker.google.com/339562627))
- `ViewModel`'s `saveable` integration using property delegates now uses the class name as part of the auto-generated key, avoiding conflicts if multiple classes use the same `SavedStateHandle`. ([aosp/3063463](https://android-review.googlesource.com/3063463))

### Version 2.8.0

May 14, 2024

`androidx.lifecycle:lifecycle-*:2.8.0` is released. Version 2.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c8b86ee34b2e32889913843be8f20bd7b718132d..7ad6b8bbf8fa3d5a3c97feca6c52a1a2bf98a622/lifecycle).

**Important changes since 2.7.0**

- `LocalLifecycleOwner` has been moved from Compose UI to `lifecycle-runtime-compose` so that its Compose-based helper APIs can be used outside of Compose UI.
- The `lifecycle-runtime-compose` artifact now contains the `dropUnlessResumed` and `dropUnlessStarted` APIs which allow you to drop click or other events that occur even after the `LifecycleOwner` has dropped below the given `Lifecycle.State`. For example, this can be used with Navigation Compose to avoid handling click events after a transition to another screen has already begun: `onClick: () -> Unit = dropUnlessResumed { navController.navigate(NEW_SCREEN) }`
- `ViewModel.viewModelScope` is now an overridable constructor parameter, allowing you to inject your own dispatcher and `SupervisorJob()` or to override the default by using the `backgroundScope` available within `runTest`. ([I2817c](https://android-review.googlesource.com/#/q/I2817ca223e31fb3e66b1b87b470b2eb26c2fac55), [b/264598574](https://issuetracker.google.com/issues/264598574))

      class MyViewModel(
        // Make Dispatchers.Main the default, rather than Dispatchers.Main.immediate
        viewModelScope: CoroutineScope = Dispatchers.Main + SupervisorJob()
      ) : ViewModel(viewModelScope) {
        // Use viewModelScope as before, without any code changes
      }

      // Allows overriding the viewModelScope in a test
      fun Test() = runTest {
        val viewModel = MyViewModel(backgroundScope)
      }

- `ViewModel` has been rewritten in Kotlin and now uses `AutoClosable` instead of `Closeable`. It now supports adding `AutoCloseable` objects with a `key` that allows retrieving them via `getCloseable()`.

- Calling `LifecycleStartEffect` and `LifecycleResumeEffect` without a key is now an error, following the same convention as the `DisposableEffect` API that these APIs mirror.

- Deprecated `LiveDataReactiveStreams.toPublisher(lifecycleOwner, liveData)` in favor of `LiveData.toPublisher(lifecycleOwner)`.

- The `lifecycle-livedata-core-ktx` kotlin extensions have now been moved to the `lifecycle-livedata-core` module.

- The `NullSafeMutableLiveData` has been refactored to avoid many false positives.

**Lifecycle Kotlin Multiplatform Compatibility**

The core Lifecycle APIs in `Lifecycle`, `LifecycleOwner`, `LifecycleObserver`, `Lifecycle.State`, `Lifecycle.Event`, and `LifecycleRegistry` are now shipped in artifacts compatible with Kotlin Multiplatform.

Artifacts impacted:

- `lifecycle-common` moves most APIs to `common` and supports jvm and iOS in addition to Android.
- `lifecycle-runtime` moves most APIs to `common` and supports jvm and iOS in addition to Android.
- `lifecycle-runtime-ktx` is now empty, with all APIs being moved into `lifecycle-runtime`.
- `lifecycle-runtime-compose` moves all APIs to `common` and ships an Android artifact, matching the multiplatform support of `androidx.compose`.

**ViewModel Kotlin Multiplatform Compatibility**

The `lifecycle-viewmodel` artifact and APIs like `ViewModel`, `ViewModelStore`, `ViewModelStoreOwner`, and `ViewModelProvider` are now shipped in artifacts compatible with Kotlin Multiplatform.

To accommodate this change, methods such as those on `ViewModelProvider` that took a `java.lang.Class<T>` now have an equivalent method that takes a `kotlin.reflect.KClass<T>`.

Binary compatibility on Android has been maintained, but there are a few notable changes when comparing the Android API surface to the common API surface:

- Constructing a `ViewModelProvider` instance is now done through the `ViewModelProvider.create()` methods rather than directly calling its constructor.
- `ViewModelProvider.NewInstanceFactory` and `ViewModelProvider.AndroidViewModelFactory` are only available on Android.
  - Custom Factories are recommended to extend from `ViewModelProvider.Factory` and use the `create` method that takes a `CreationExtras` or use the `viewModelFactory` Kotlin DSL.
- Using `ViewModelProvider` without a custom factory on non-JVM platforms will result in an `UnsupportedOperationException`. On JVM platforms, compatibility is preserved by using the no-args ViewModel constructor if a custom factory is not provided.
- `viewModelScope` will fallback to an `EmptyCoroutineContext` in platforms where `Dispatchers.Main` is not available (e.g., Linux).

Artifacts impacted:

- `lifecycle-viewmodel` moves most APIs to `common` and supports jvm and iOS in addition to Android.
- `lifecycle-viewmodel-ktx` is now empty, with all APIs being moved into `lifecycle-viewmodel`.
- `lifecycle-viewmodel-compose` moves all APIs to `common` and ships an Android artifact, matching the multiplatform support of `androidx.compose`.

**Behavior Changes**

- `InitializerViewModelFactory` (including `viewModelFactory` builder function) will now throw an `IllegalArgumentException` if a `initializer` with the same `clazz: KClass<VM : ViewModel>` has already been added. ([Ic3a36](https://android-review.googlesource.com/#/q/Ic3a36b87c170bd886e60fc264a352096be003c02))

**Known Issues**

- `lifecycle-*:2.8.0` requires a minimum Compose version of [1.7.0-alpha05](https://developer.android.com/jetpack/androidx/releases/compose-ui#1.7.0-alpha05) ([b/336842920](https://issuetracker.google.com/issues/336842920)).

### Version 2.8.0-rc01

May 1, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-rc01` is released. Version 2.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/67004410fdbff19f90caa4cc43965ab21dca1943..c8b86ee34b2e32889913843be8f20bd7b718132d/lifecycle).

**Bug Fixes**

- Fixed an issue where the Baseline Profile for `lifecycle-common` classes was not properly packaged. These are now packaged in the `lifecycle-runtime` AAR. ([aosp/3038274](https://android-review.googlesource.com/c/platform/frameworks/support/+/3038274), [b/322382422](https://issuetracker.google.com/issues/322382422))
- Fixed an unintentional ordering change in how `AutoCloseable` instances attached to a ViewModel are cleared - the previous order of `addCloseable(String, AutoCloseable)`, then `addClosable(AutoCloseable)`, then `onCleared()` has been restored. ([aosp/3041632](https://android-review.googlesource.com/c/platform/frameworks/support/+/3041632))
- Improve the default creation behavior for `viewModelScope` for native and JVM Desktop environments. ([aosp/3039221](https://android-review.googlesource.com/c/platform/frameworks/support/+/3039221))

**External Contribution**

- Thanks Victor Kropp for improving the checking for the main thread on JVM Desktop. ([aosp/3037116](https://android-review.googlesource.com/c/platform/frameworks/support/+/3037116))

### Version 2.8.0-beta01

April 17, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-beta01` is released. Version 2.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..67004410fdbff19f90caa4cc43965ab21dca1943/lifecycle).

**New Features**

- The `lifecycle-runtime-compose` artifact is now compatible with Kotlin Multiplatform, moving its code to `common` and ships an Android artifact, matching the multiplatform support for `androidx.compose`. ([If7a71](https://android-review.googlesource.com/#/q/If7a714e598e360a1960f8b3a673b33538f595ff4), [I4f4a0](https://android-review.googlesource.com/#/q/I4f4a03613120f3222bd44ae1feab1a085ddb38da), [b/331769623](https://issuetracker.google.com/issues/331769623))

### Version 2.8.0-alpha04

April 3, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-alpha04` is released. Version 2.8.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8fbefdc70ea49fce9c8f8cfcf80e1fa2122a7ee4..02b55f664eba38e42e362e1af3913be1df552d55/lifecycle).

**New Features**

- The `lifecycle-viewmodel-compose` artifact is now compatible with Kotlin Multiplatform, moving its code to `common` and ships an Android artifact, matching the multiplatform support of `androidx.compose`. The accommodate this change, the Composable `viewModel` method now accepts a `KClass` in addition to a `java.lang.Class`. ([b/330323282](https://issuetracker.google.com/issues/330323282))

**Bug Fixes**

- The `NullSafeMutableLiveData` has been refactored to avoid many false positives. ([I2d8c1](https://android-review.googlesource.com/#/q/I2d8c1f5b4425bd042cff6552e6a8c45c9905c2b3), [Iafb18](https://android.googlesource.com/platform/frameworks/support/+/c3b86c80eef9b60fc7e67945f40bf10bde486d04#:%7E:text=Iafb18e625b06ca51602c0636733465da7b6e014e), [I03463](https://android-review.googlesource.com/#/q/I034637a87a8bb873b32dc2fec1263161d578e809), [I7ecef](https://android-review.googlesource.com/#/q/I7ecef93d26a1345a0e47f3298d6952b249384700))

**Dependency update**

- The `lifecycle-viewmodel-compose` artifact now depends on Compose 1.6.0.
- Lifecycle now depends on [Profile Installer 1.3.1](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.1).

### Version 2.8.0-alpha03

March 20, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-alpha03` is released. Version 2.8.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a0ec9dc0763af4507de3604aed283a57843bb85f..a57d7d17753695012b58c9ce7ad55a8d39157e62/lifecycle).

**New Features**

- `ViewModel.viewModelScope` is now an overridable constructor parameter, allowing you to inject your own dispatcher and `SupervisorJob()` or to override the default by using the `backgroundScope` available within `runTest`. ([I2817c](https://android-review.googlesource.com/#/q/I2817ca223e31fb3e66b1b87b470b2eb26c2fac55), [b/264598574](https://issuetracker.google.com/issues/264598574))

      class MyViewModel(
        // Make Dispatchers.Main the default, rather than Dispatchers.Main.immediate
        viewModelScope: CoroutineScope = Dispatchers.Main + SupervisorJob()
      ) : ViewModel(viewModelScope) {
        // Use viewModelScope as before, without any code changes
      }

      // Allows overriding the viewModelScope in a test
      fun Test() = runTest {
        val viewModel = MyViewModel(backgroundScope)
      }

**Kotlin Multiplatform Compatibility**

The `lifecycle-viewmodel` artifact and APIs like `ViewModel`, `ViewModelStore`, `ViewModelStoreOwner`, and `ViewModelProvider` are now shipped in artifacts compatible with Kotlin Multiplatform. ([b/214568825](https://issuetracker.google.com/issues/214568825))

To accommodate this change, methods such as those on `ViewModelProvider` that took a `java.lang.Class<T>` now have an equivalent method that takes a `kotlin.reflect.KClass<T>`.

Binary compatibility on Android has been maintained, but there are a few notable changes when comparing the Android API surface to the common API surface:

- Constructing a `ViewModelProvider` instance is now done through the `ViewModelProvider.create()` methods rather than directly calling its constructor.
- `ViewModelProvider.NewInstanceFactory` and `ViewModelProvider.AndroidViewModelFactory` are only available on Android.
  - Custom Factories are recommended to extend from `ViewModelProvider.Factory` and use the `create` method that takes a `CreationExtras` or use the `viewModelFactory` Kotlin DSL.
- Using `ViewModelProvider` without a custom factory on non-JVM platforms will result in an `UnsupportedOperationException`. On JVM platforms, compatibility is preserved by using the no-args ViewModel constructor if a custom factory is not provided.
- `viewModelScope` will fallback to an `EmptyCoroutineContext` in platforms where `Dispatchers.Main` is not available (e.g., Linux).

**Behavior Changes**

- `InitializerViewModelFactory` (including `viewModelFactory` builder function) will now throw an `IllegalArgumentException` if a `initializer` with the same `clazz: KClass<VM : ViewModel>` has already been added. ([Ic3a36](https://android-review.googlesource.com/#/q/Ic3a36b87c170bd886e60fc264a352096be003c02))

**Bug Fixes**

- `ViewModel.getCloseable` now handles duplicated keys: if the `key` already has an `AutoCloseable` resource associated with it, the old resource will be replaced and closed immediately. ([Ibeb67](https://android-review.googlesource.com/#/q/Ibeb675fc50766f954d980e582374224cfa910548))
- Accessing the `viewModelScope` of a `ViewModel` is now thread safe. ([If4766](https://android-review.googlesource.com/#/q/If4766608206f1354b03463b2771b7a369a0b537f), [b/322407038](https://issuetracker.google.com/issues/322407038))

**External Contribution**

- `LocalLifecycleOwner` moved from Compose UI to lifecycle-runtime-compose so that its Compose-based helper APIs can be used outside of Compose UI. Thanks Jake Wharton for the contribution. ([I6c41b](https://android-review.googlesource.com/#/q/I6c41b92eb6aaab67e7d733dfe3fe0b429b46becf), [b/328263448](https://issuetracker.google.com/issues/328263448))

### Version 2.8.0-alpha02

February 21, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-alpha02` is released. [Version 2.8.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/51191bc12f96f233fc08995e1b4e8ff8b88bc7ce..e1b82c49c59d8e976ce558aba5586f6c61bc9054/lifecycle)

**New Features**

- The `dropUnlessResumed` and `dropUnlessStarted` APIs have been added which allow you to drop click or other events that occur even after the `LifecycleOwner` has dropped below the given `Lifecycle.State`. For example, this can be used with Navigation Compose to avoid handling click events after a transition to another screen has already begun: `onClick: () -> Unit = dropUnlessResumed { navController.navigate(NEW_SCREEN) }` ([Icba83](https://android-review.googlesource.com/#/q/Icba837aeb90426b00bc5888e663f775284191fe2), [b/317230685](https://issuetracker.google.com/issues/317230685))

**Kotlin Conversions**

- `ViewModel` is now written in Kotlin ([I16f26](https://android-review.googlesource.com/#/q/I16f26813d862c76154739888bb631c214fa1c810), [b/214568825](https://issuetracker.google.com/issues/214568825))
- The `lifecycle-viewmodel-ktx` kotlin extensions have now been moved to the base lifecycle module. ([Id787b](https://android-review.googlesource.com/#/q/Id787b6db6817e69e4ec50748a07ccdbef074e99d), [b/274800183](https://issuetracker.google.com/issues/274800183))
- The `lifecycle-runtime-ktx` kotlin extensions have now been moved to the base lifecycle module. ([Ic3686](https://android-review.googlesource.com/#/q/Ic368640a7e66dd0b748601d61b7aa23d99e5a1d6), [b/274800183](https://issuetracker.google.com/issues/274800183))
- The `lifecycle-livedata-core-ktx` kotlin extensions have now been moved to the base lifecycle module. ([I54a3d](https://android-review.googlesource.com/#/q/I54a3d4346b4a9c5861f5f3bdb0079dbb27f29668), [b/274800183](https://issuetracker.google.com/issues/274800183))

**Kotlin Multiplatform Compatibility**

- The core Lifecycle APIs in `Lifecycle`, `LifecycleOwner`, `LifecycleObserver`, `Lifecycle.State`, `Lifecycle.Event`, and `LifecycleRegistry` are now shipped in artifacts compatible with Kotlin Multiplatform. ([b/317249252](https://issuetracker.google.com/317249252))

**API Changes**

- Calling `LifecycleStartEffect` and `LifecycleResumeEffect` without a key is now an error, following the same convention as the `DisposableEffect` API that these APIs mirror. ([Ib0e0c](https://android-review.googlesource.com/#/q/Ib0e0c3248ce23eb4be10f29d193e152646c1653c), [b/323518079](https://issuetracker.google.com/issues/323518079))
- `ViewModel` now uses `AutoCloseable` instead of `Closeable`. That is a backward compatible change. ([I27f8e](https://android-review.googlesource.com/#/q/I27f8e7c85e59aae7c268d66d98f70d717d6f3c83), [b/214568825](https://issuetracker.google.com/issues/214568825))
- Deprecated `LiveDataReactiveStreams.toPublisher(lifecycleOwner, liveData)` in favor of `LiveData.toPublisher(lifecycleOwner)`. ([Iabe29](https://android-review.googlesource.com/#/q/Iabe2986767b85f5b55cdfe6c9a44e3809860a3c6), [b/262623005](https://issuetracker.google.com/issues/262623005))

**External Contribution**

- Thanks Ivan Matkov from Jetbrains for helping move Lifecycle to Kotlin Multiplatform. ([aosp/2926690](https://android-review.googlesource.com/c/platform/frameworks/support/+/2926690), [I0c5ac](https://android-review.googlesource.com/#/q/I0c5acfde52bd6c4a3cf7f38193c235915b45d549), [If445d](https://android-review.googlesource.com/#/q/If445d68e7e85929839ad10347b31b9f11d61c00d))

### Version 2.8.0-alpha01

January 24, 2024

`androidx.lifecycle:lifecycle-*:2.8.0-alpha01` is released. [Version 2.8.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/09469f458ee5c8201480dab80e18c923c531db9e..51191bc12f96f233fc08995e1b4e8ff8b88bc7ce/lifecycle)

**New Features**

- `ViewModel` now supports adding `Closeable` objects with a `key` that allows retrieving them via `getCloseable()`. ([I3cf63](https://android-review.googlesource.com/#/q/I3cf63385f043090daa9dd45cbe74464b36ca47a9))

## Version 2.7

### Version 2.7.0

January 10, 2024

`androidx.lifecycle:lifecycle-*:2.7.0` is released. [Version 2.7.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/58bcc943758bd4e82932a5190d9e5cf6aaedd3e4..09469f458ee5c8201480dab80e18c923c531db9e/lifecycle)

**Important changes since 2.6.0**

- `TestLifecycleOwner` now includes a suspending function `setCurrentState()` which ensures that the state change and all `LifecycleObserver` callbacks are completed before returning. Notably, unlike setting the `currentState` property directly, this does not use `runBlocking`, making it safe to use within a coroutine such as one provided by `runTest`.
- The `LiveData` extensions of `map` and `switchMap` now mirror the behavior of `distinctUntilChanged` - if the `LiveData` has a `value` set, the `map`/`switchMap` function will be *immediately* called to populate the `value` of the returned `LiveData`. This ensures that the initial value will be set as part of the first composition (when used with `observeAsState()`), but does not change the observation behavior - updates values from the source `LiveData` will still only apply once you start observing the `LiveData`.
- This release fixes an issue where `SavedStateHandle` would not properly restore custom `Parcelable` classes after process death and recreation. Due to type information that is lost by the Android framework, arrays of custom Parcelables require additional work (manually creating a typed array of the right type) and the documentation on `get`, `getLiveData`, and `getStateFlow` now specifically calls this limitation out.
- The proguard keep rules associated with `LifecycleObserver` have been removed. This means that proguarded code that wishes to use APIs via reflection (such as using the long since deprecated `@OnLifecycleEvent` annotation) will need to provide their own keep rules for their specific use case.

**Lifecycle Event Observability**

- As an alternative to using a `LifecycleEventObserver`, you can now observe a `Flow` of `Lifecycle.Event` via the `Lifecycle.asFlow()` extension method.
- Jetpack Compose users can now use `LifecycleEventEffect` to run Compose side effects based on `Lifecycle.Event`.

    @Composable
    fun HomeScreen(viewModel: HomeViewModel = viewModel()) {
      LifecycleEventEffect(Lifecycle.Event.ON_RESUME) {
        viewModel.refreshData()
      }
      // ...
    }

- Jetpack Compose users can use `LifecycleStartEffect` and `LifecycleResumeEffect` to handle *pairs* of events - started to stopped and resumed to paused, respectively. This API mirrors the one found in `DisposableEffect` and is suitable for cases where the change being made when the state is going up needs to be reversed when going back down.

    fun HomeScreen(viewModel: HomeViewModel = viewModel()) {
      LifecycleStartEffect(viewModel) {
        val timeTracking = viewModel.startTrackingTimeOnScreen()
        onStopOrDispose {
          timeTracking.stopTrackingTimeOnScreen()
        }
      }
      // ...
    }

See [Run code on lifecycle events](https://developer.android.com/topic/libraries/architecture/compose#run-code) for more information.

**Lifecycle State Observability**

- The current `Lifecycle.State` can now be observed via the `Lifecycle.currentStateFlow` property, which returns a `StateFlow` where the `value` is the current `Lifecycle.State`.
- Jetpack Compose users can use the `Lifecycle.currentStateAsState()` extension to directly expose `Lifecycle.State` as Compose `State`. This is equivalent (and a shorter alternative) to `lifecycle.currentStateFlow.collectAsState()`.

See [Collect lifecycle state with flows](https://developer.android.com/topic/libraries/architecture/compose#collect-lifecycle) for more information.

### Version 2.7.0-rc02

December 13, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-rc02` is released. [Version 2.7.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/13d5e2efb6ca3077b4bd3f6040c5a15b504397d3..58bcc943758bd4e82932a5190d9e5cf6aaedd3e4/lifecycle)

**Bug Fixes**

- Fixed an issue where `SavedStateHandle` would not properly restore custom `Parcelable` classes after process death and recreation. Due to type information that is lost by the Android framework, arrays of custom Parcelables require additional work (manually creating a typed array of the right type) and the documentation on `get`, `getLiveData`, and `getStateFlow` now specifically calls this limitation out. ([I0b55a](https://android-review.googlesource.com/#/q/I0b55ab44b636a5d0e5b33cdc21821310e2d18b9d))

### Version 2.7.0-rc01

November 15, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-rc01` is released. [Version 2.7.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3ffd7948030a769c857b8c629e0079c54b730ad..13d5e2efb6ca3077b4bd3f6040c5a15b504397d3/lifecycle)

**Bug Fixes**

- `LifecycleStartEffect` and `LifecycleResumeEffect` now correctly dispose and recreate the effect block if the `LifecycleOwner` is changed. ([Ia25c6](https://android-review.googlesource.com/#/q/Ia25c6adab84ef2215493c32deecae3d4e61ccad0))

### Version 2.7.0-beta01

November 1, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-beta01` is released with no changes. [Version 2.7.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/465c5c5b7a0d79793bddb26a695f67aba8ea2f7e..e3ffd7948030a769c857b8c629e0079c54b730ad/lifecycle)

- A beta version bump, no major changes to this release version.

### Version 2.7.0-alpha03

October 18, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-alpha03` is released. [Version 2.7.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..465c5c5b7a0d79793bddb26a695f67aba8ea2f7e/lifecycle)

**New Features**

- `lifecycle-runtime-testing` now contains a new Lint check to avoid setting the `Lifecycle.State` of the `TestLifecycleOwner` by using the `currentState` field when inside of a coroutine. The Lint check now suggests the suspending `setCurrentState` which allows setting the `Lifecycle.State` without blocking. ([Icf728](https://android-review.googlesource.com/#/q/Icf728aa93a9aeca7c3cd89311289aae970d1f651), [b/297880630](https://issuetracker.google.com/issues/297880630))

**Bug Fixes**

- Fixed an issue with `LiveData.switchMap` where returning the same `LiveData` instance both on the initial call and a subsequent call would prevent the `LiveData` instance from being added as a source. ([Ibedcba7](https://android-review.googlesource.com/#/q/Ibedcba7934ae43bba58eb1cb43388e125adf4bc6))

### Version 2.7.0-alpha02

September 6, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-alpha02` is released. [Version 2.7.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4aed940027a19667e67d155563fc5fa8b7279313..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/lifecycle)

**New Features**

- `TestLifecycleOwner` now includes the suspending function `setCurrentState()` to give users the option of using `TestLifecycleOwner` from within a coroutine such as one provided by `runTest`. ([I329de](https://android-review.googlesource.com/#/q/I329de3d76bcd7fa5e04077916ff551f9f2f3f864), [b/259344129](https://issuetracker.google.com/issues/259344129))

**API Changes**

- All files from the `lifecycle-livedata-ktx` modules have been moved into the main `lifecycle-livedata` module. ([I10c6f](https://android-review.googlesource.com/#/q/I10c6f70c82a64e80eec704f548911f42bdd0b56a), [b/274800183](https://issuetracker.google.com/issues/274800183))

**Behavior Changes**

- The `LiveData.map()` and `LiveData.switchMap()` extensions now sets the `value` of the returned `LiveData` if the previous `LiveData` has had a value set on it, ensuring that using the resulting LiveData in Jetpack Compose has the right state on the initial composition. ([I91d2b](https://android-review.googlesource.com/#/q/I91d2b286b609976a43b740c45c99975317274b63), [b/269479952](https://issuetracker.google.com/issues/269479952))
- `ViewModel`'s `addCloseable()` now immediately closes the `Closeable` if the `ViewModel` has already received a call to `onCleared()`. ([I4712e](https://android-review.googlesource.com/#/q/I4712ee3600acbf04506af46e6ac479a617cebd86), [b/280294730](https://issuetracker.google.com/issues/280294730))

**Bug Fixes**

- From [Lifecycle `2.6.2`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.6.2): Fixed an issue where `SavedStateHandle` would not correctly be restored after process death if the state was restored, `save()` was called without actually saving the state in the parent `SavedStateRegistry`, and then the state was restored again. This fixes the interaction between `rememberSaveable` and Navigation Compose's `NavHost`. ([aosp/2729289](https://android-review.googlesource.com/c/platform/frameworks/support/+/2729289))

### Version 2.7.0-alpha01

July 26, 2023

`androidx.lifecycle:lifecycle-*:2.7.0-alpha01` is released. [Version 2.7.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5b3397913c8a67b0cffa4d23cb4666aa3cb6c6d7..4aed940027a19667e67d155563fc5fa8b7279313/lifecycle)

**API Changes**

- `Lifecycle.State` is now Compose-observable via `Lifecycle.currentStateFlow`, which returns a `StateFlow` where the `value` is the current `Lifecycle.State`. ([Ib212d](https://android-review.googlesource.com/#/q/Ib212d9b84307e0397306e521ceaae41e2c76d532), [b/209684871](https://issuetracker.google.com/issues/209684871))
- `Lifecycle.Event`s can now able to be observed as a `Flow` with `Lifecycle.asFlow().` ([If2c0f](https://android-review.googlesource.com/#/q/If2c0f10760caca7109d43c235ea76437ef2af5dc), [b/176311030](https://issuetracker.google.com/issues/176311030))
- `LifecycleResumeEffect` API has been added to run Compose `SideEffect`s based on both `Lifecycle.Event.ON_RESUME` and `Lifecycle.Event.ON_PAUSE` event callbacks. ([I60386](https://android-review.googlesource.com/#/q/I603860f21eb6a433c909d7ae6f8120f6d23179aa), [b/235529345](https://issuetracker.google.com/issues/235529345))
- `LifecycleStartEffect` API has been added to run Compose `SideEffect`s based on `Lifecycle.Event.ON_START` and `Lifecycle.Event.ON_STOP` event callbacks. ([I5a8d1](https://android-review.googlesource.com/#/q/I5a8d1e6f152b7083e086146ba97044c4b454db84), [b/235529345](https://issuetracker.google.com/issues/235529345))
- `LifecycleEventEffect` API has been added to run Compose `SideEffect`s based on `Lifecycle.Event`. ([Ic9794](https://android-review.googlesource.com/#/q/Ic9794d7e59b1a66cc7f31cbaebed9b3d3dee5dd3), [b/235529345](https://issuetracker.google.com/issues/235529345))
- `Lifecycle.collectAsState()` extension has been added to directly expose `Lifecycle.State` as Compose `State`. This is equivalent (and a shorter alternative) to `lifecycle.currentStateFlow.collectAsState()`. ([I11015](https://android-review.googlesource.com/#/q/I1101507a270980554046f7505b356c9c923ad48e), [b/235529345](https://issuetracker.google.com/issues/235529345))

**Bug Fixes**

- The `LiveData.distinctUntilChanged()` extension now sets the `value` of the returned `LiveData` if the previous `LiveData` has had a value set on it. This does not change the observation behavior - updated values from the source `LiveData` will still only apply once you start observing the `LiveData` returned from `distinctUntilChanged()`. ([Ib482f](https://android-review.googlesource.com/#/q/Ib482f0cc74fad451e0ff37088a11fcf2682f0f8a))
- The proguard keep rules associated with `LifecycleObserver` have been removed. This means that proguarded code that wishes to use APIs via reflection will need to provide their own keep rules for their specific use case. ([Ia12fd](https://android-review.googlesource.com/#/q/Ia12fdc429a23d43d5b6a4a5c103f866141480bf5))

## Version 2.6

### Version 2.6.2

September 6, 2023

`androidx.lifecycle:lifecycle-*:2.6.2` is released. [Version 2.6.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5b3397913c8a67b0cffa4d23cb4666aa3cb6c6d7..7be61b15f970440682c946bd769cc7e3737acd86/lifecycle)

**Bug Fixes**

- Fixed an issue where `SavedStateHandle` would not correctly be restored after process death if the state was restored, `save()` was called without actually saving the state in the parent `SavedStateRegistry`, and then the state was restored again. This fixes the interaction between `rememberSaveable` and Navigation Compose's `NavHost`. ([aosp/2729289](https://android-review.googlesource.com/c/platform/frameworks/support/+/2729289))

### Version 2.6.1

March 22, 2023

`androidx.lifecycle:lifecycle-*:2.6.1` is released. [Version 2.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/63b60b83b0674a40e13c559d081c757ecbb09d79..f9d30b70c2b1e8a51f63e050ff3fa8527d65e1fd/lifecycle)

**Dependency Updates**

- `lifecycle-viewmodel-savedstate` now depends on [SavedState `1.2.1`](https://developer.android.com/jetpack/androidx/releases/savedstate#1.2.1). ([cd7251](https://android.googlesource.com/platform/frameworks/support/+/cd7251e68b99b9275bdcb722fb2bc0fa39b09901))
- Lifecycle now depends on [ProfileInstaller `1.3.0`](https://developer.android.com/jetpack/androidx/releases/profileinstaller#1.3.0). ([f9d30b](https://android.googlesource.com/platform/frameworks/support/+/f9d30b70c2b1e8a51f63e050ff3fa8527d65e1fd))

### Version 2.6.0

March 8, 2023

`androidx.lifecycle:lifecycle-*:2.6.0` is released. [Version 2.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e6a3d07b22cc0b7b17462b8b52feb2989a8d0e40..63b60b83b0674a40e13c559d081c757ecbb09d79/lifecycle)

**Important changes since 2.5.0**

- `LiveData` now includes a new `isInitialized` property that indicates whether an explicit value has ever been set on the `LiveData`, allowing you to distinguish between `liveData.value` returning `null` because no value has ever been set or an explicit `null` value.
- `MediatorLiveData` now includes a constructor to set an initial value.
- Added a new extension on `StateFlow` and `Flow` of [`collectAsStateWithLifecycle()`](https://medium.com/androiddevelopers/consuming-flows-safely-in-jetpack-compose-cde014d0d5a3) that collect from flows and represents its latest value as Compose State in a lifecycle-aware manner.
- `Lifecycle.launchWhenX` methods and `Lifecycle.whenX` methods have been deprecated as the use of a pausing dispatcher can lead to wasted resources in some cases. It is recommended to use `Lifecycle.repeatOnLifecycle`. For more information about one-time suspending work, please see [this explanation](https://issuetracker.google.com/270049505#comment2) on why this is inherently unsafe.
- **Kotlin Conversion** - A large number of Lifecycle classes have been converted to Kotlin. All converted classes still retain their binary compatibility with previous versions. The following classes have **source incompatible** changes for classes written in Kotlin: `ViewTreeLifecycleOwner`, `LiveDataReactiveStreams`, `HasDefaultViewModelProviderFactory`, `ViewTreeViewModelStoreOwner`, `Transformations`, `ViewModelStoreOwner`, `LifecycleOwner`

The table below provides the source conversions for the new version of lifecycle.

| Lifecycle 2.5 | Lifecycle 2.5 (KTX) | Lifecycle 2.6 |
|---|---|---|
| `Transformations.switchMap(liveData) {...}` | `liveData.switchMap {...}` | `liveData.switchMap {...}` |
| `Transformations.map(liveData) {...}` | `liveData.map {...}` | `liveData.map {...}` |
| `Transformations.distinctUntilChanged(liveData) {...}` | `liveData.distinctUntilChanged{...}` | `liveData.distinctUntilChanged{...}` |
| `LiveDataReactiveStreams.fromPublisher(publisher)` | `publisher.toLiveData()` | `publisher.toLiveData()` |
| `LiveDataReactiveStreams.toPublisher(lifecycleOwner, liveData)` | `liveData.toPublisher(lifecycleOwner)` | `liveData.toPublisher(lifecycleOwner)` |
| `override fun getDefaultViewModelProviderFactory(): ViewModelProvider.Factory = factory` | `override fun getDefaultViewModelProviderFactory(): ViewModelProvider.Factory = factory` | `override val defaultViewModelProviderFactory = factory` |
| `override fun getDefaultViewModelCreationExtras(): CreationExtras = extras` | `override fun getDefaultViewModelCreationExtras(): CreationExtras = extras` | `override val defaultViewModelProviderCreationExtras = extras` |
| `ViewTreeLifecycleOwner.set(view, owner)` | `ViewTreeLifecycleOwner.set(view, owner)` | `view.setViewTreeLifecycleOwner(owner)` |
| `ViewTreeLifecycleOwner.get(view)` | `view.findViewTreeLifecycleOwner()` | `view.findViewTreeLifecycleOwner()` |
| `override fun getViewModelStore(): ViewModelStore = store` | `override fun getViewModelStore(): ViewModelStore = store` | `override val viewModelStore: ViewModelStore = store` |
| `override fun getLifecycle(): Lifecycle = registry` | `override fun getLifecycle(): Lifecycle = registry` | `override val lifecycle: Lifecycle get() = registry` |

- The nullability of the `onChanged` method of a `Observer` created in Kotlin now matches the nullability of the generic type. If you want `Observer.onChanged()` to accept a nullable type, you must instantiate the `Observer` with a nullable type.
- These classes were also converted to Kotlin, but remain source compatible: `DefaultLifecycleObserver`, `LifecycleEventObserver`, `Lifecycle`, `LifecycleRegistry`, `LifecycleObserver`, `ViewModelStore`, `AndroidViewModel`, `AbstractSavedStateViewModelFactory`, `LifecycleService`, `ServiceLifecycleDispatcher`, and `ProcessLifecycleOwner`

### Version 2.6.0-rc01

February 22, 2023

`androidx.lifecycle:lifecycle-*:2.6.0-rc01` is released. [Version 2.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..a0e71d292812d53868b56f94481f420a70843460/lifecycle)

**Bug Fixes**

- The `LiveData.distinctUntilChanged()` extension now sets the `value` of the returned `LiveData` if the previous `LiveData` has had a value set on it. This does not change the observation behavior - updated values from the source `LiveData` will still only apply once you start observing the `LiveData` returned from `distinctUntilChanged()`. ([Ib482f](https://android-review.googlesource.com/#/q/Ib482f0cc74fad451e0ff37088a11fcf2682f0f8a))

### Version 2.6.0-beta01

February 8, 2023

`androidx.lifecycle:lifecycle-*:2.6.0-beta01` is released. [Version 2.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b..7d3ac1ab1206c01fae3ebb500b5b942636070155/lifecycle)

**Kotlin Conversions**

- `LifecycleOwner` is now written in Kotlin. This is a **source incompatible change** for classes written in Kotlin - they must now override the `lifecycle` property rather than implementing the previous `getLifecycle()` function. ([I75b4b](https://android-review.googlesource.com/#/q/I75b4b3ffc999f3f00c6ca57e027dff5e18f54146), [b/240298691](https://issuetracker.google.com/issues/240298691))
- `ViewModelStoreOwner` is now in Kotlin. This is a **source incompatible change** for classes written in Kotlin - they must now override the `viewModelStore` property rather than implementing the previous `getViewModelStore()` function. ([I86409](https://android-review.googlesource.com/#/q/I864099e6aa61bc9cbc041181dafd6a7bce7d93b1), [b/240298691](https://issuetracker.google.com/issues/240298691))
- The Kotlin extension on `LifecycleOwner` that provides the `lifecycleScope` field has been moved to the `lifecycle-common` artifact from `lifecycle-runtime-ktx`. ([I41d78](https://android-review.googlesource.com/#/q/I41d786b9db40eae569b1eb9cedd559bb87178fdc), [b/240298691](https://issuetracker.google.com/issues/240298691))
- The Kotlin extension on `Lifecycle` that provides the `coroutineScope` field has been moved to the `lifecycle-common` artifact from `lifecycle-runtime-ktx`. ([Iabb91](https://android-review.googlesource.com/#/q/Iabb911950a0646052eed89f5ce2751b156268aae), [b/240298691](https://issuetracker.google.com/issues/240298691))

### Version 2.6.0-alpha05

January 25, 2023

`androidx.lifecycle:lifecycle-*:2.6.0-alpha05` is released. [Version 2.6.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/adf1c279a86ab3886e1666c08e2c3efba783367b..e5dad1e7d1c225f89f7c2d5a39a7a0de8d637d7b/lifecycle)

**Kotlin Conversions**

- `Transformations` is now written in Kotlin. This is a **source incompatible change** for those classes written in Kotlin that were directly using syntax such as `Transformations.map` - Kotlin code **must** now use the Kotlin extension method syntax that was previously only available when using `lifecycle-livedata-ktx`. When using the Java programming language, the versions of these methods that take an `androidx.arch.core.util.Function` method are deprecated and replaced with the versions that take a Kotlin `Function1`. This change maintains binary compatibility. ([I8e14f](https://android-review.googlesource.com/#/q/I8e14f0c95d1b509620dfe6b94318e314f84d9f4b))
- `ViewTreeViewModelStoreOwner` is now written in Kotlin. This is a **source incompatible change** for those classes written in Kotlin - you must now directly import and use the Kotlin extension methods on `View` of `androidx.lifecycle.setViewTreeViewModelStoreOwner` and `androidx.lifecycle.findViewTreeViewModelStoreOwner` to set and find a previously set owner. This is binary compatible and remains source compatible for implementations written in the Java programming language. ([Ia06d8](https://android-review.googlesource.com/#/q/Ia06d830b263c0f7f1193c5b3ead1587533ca1b0c), [Ib22d8](https://android-review.googlesource.com/#/q/Ib22d8b129e70972429920bf7dd63632d80e68730), [b/240298691](https://issuetracker.google.com/issues/240298691))
- The `HasDefaultViewModelProviderFactory` interface is now written in Kotlin. This is a **source incompatible change** for classes written in Kotlin - they must now override the `defaultViewModelProviderFactory` and `defaultViewModelCreationExtras` properties rather than implementing the previous corresponding functions. ([Iaed9c](https://android-review.googlesource.com/#/q/Iaed9c26539611f73794de6a1349e7b31a415ee9d), [b/240298691](https://issuetracker.google.com/issues/240298691))
- `Observer` is now written in Kotlin. Its `onChanged()` method now uses the name `value` for its parameter. ([Iffef2](https://android-review.googlesource.com/#/q/Iffef21b829fdb1ce2685747c27b4ff4841c01613), [I4995e](https://android-review.googlesource.com/#/q/I4995e88bac1a5dba16a8359f9361886aff013bb0), [b/240298691](https://issuetracker.google.com/issues/240298691))
- `AndroidViewModel`, `AbstractSavedStateViewModelFactory`, `LifecycleService`, `ServiceLifecycleDispatcher`, and `ProcessLifecycleOwner` are now written in Kotlin ([I2e771](https://android-review.googlesource.com/#/q/I2e771b51b5f7a3250d862b659a48c6f6b709b025), [Ibae40](https://android-review.googlesource.com/#/q/Ibae407718237391b600decdf0700a90c5e23e5b5), [I160d7](https://android-review.googlesource.com/#/q/I160d7e0be9d70207038f35a19cb05e5fcf8d25b2), [I08884](https://android-review.googlesource.com/#/q/I088840f6961cdc5c6b8857cbd6f3bee0a7faa4e8), [I1cda7](https://android-review.googlesource.com/#/q/I1cda7f18602f9d4831027d0199220285557d85ec), [b/240298691](https://issuetracker.google.com/issues/240298691))

### Version 2.6.0-alpha04

January 11, 2023

`androidx.lifecycle:lifecycle-*:2.6.0-alpha04` is released. [Version 2.6.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bef0ef1a976b416db5ece6c6da5d388f1cb8cd7b..adf1c279a86ab3886e1666c08e2c3efba783367b/lifecycle)

**New Features**

- `LiveData` now includes a new `isInitialized` property that indicates whether an explicit value has ever been set on the `LiveData`, allowing you to distinguish between `liveData.value` returning `null` because no value has ever been set or an explicit `null` value. ([Ibd018](https://android-review.googlesource.com/#/q/Ibd01803e2ee34a7cd4854438e5562fea473afad0))

**API Changes**

- The `collectAsStateWithLifecycle()` APIs of `lifecycle-runtime-compose` are no longer in experimental status. ([I09d42](https://android-review.googlesource.com/#/q/I09d42621a1247ad59b37b478e883a61350bf247c), [b/258835424](https://issuetracker.google.com/issues/258835424))
- `Lifecycle.launchWhenX` methods and `Lifecycle.whenX` methods have been deprecated as the use of a pausing dispatcher can lead to wasted resources in some cases. It is recommended to use `Lifecycle.repeatOnLifecycle`. ([Iafc54](https://android-review.googlesource.com/#/q/Iafc54d5078bcb576ba7a326615ce1df6592ef5f1), [b/248302832](https://issuetracker.google.com/issues/248302832))

**Kotlin Conversions**

- `ViewTreeLifecycleOwner` is now written in Kotlin. This is a **source incompatible change** for those classes written in Kotlin - you must now directly import and use the Kotlin extension methods on `View` of `androidx.lifecycle.setViewTreeLifecycleOwner` and `androidx.lifecycle.findViewTreeLifecycleOwner` to set and find a previously set owner. This replaces the previous Kotlin extension in `lifecycle-runtime-ktx`. This is binary compatible and remains source compatible for implementations written in the Java programming language. ([I8a77a](https://android-review.googlesource.com/#/q/I8a77a0b14345639a2bc7c96004017afb54a7f3e0), [I5234e](https://android-review.googlesource.com/#/q/I5234e702d384ac8bdbb9b2f45ae98e146cca21cb), [b/240298691](https://issuetracker.google.com/issues/240298691))
- `LiveDataReactiveStreams` is now written in Kotlin. The Kotlin extensions previously in `lifecycle-reactivestreams-ktx` have been moved into the `lifecycle-reactivestreams` module and have become the primary surface for code written in Kotlin. This is a **source incompatible change** for code written in Kotlin if you were not already using the Kotlin extension method APIs. ([I2b1b9](https://android-review.googlesource.com/#/q/I2b1b9e5dadf2e108e7539ef398e4d252b0ca9043), [I95d22](https://android-review.googlesource.com/#/q/I95d22efa7df46ff8444f207ec015bfc9935a4457), [b/240298691](https://issuetracker.google.com/issues/240298691))
- `DefaultLifecycleObserver`, `LifecycleEventObserver`, `Lifecycle`, `LifecycleRegistry`, `LifecycleObserver`, and `ViewModelStore` are now written in Kotlin ([Iadffd](https://android-review.googlesource.com/#/q/Iadffd272fae9862cd5f3a02c46dc3cb36d18517e), ([I60034](https://android-review.googlesource.com/#/q/I60034ada57f8a23c65f7bdbecdf2792f59b77733), [I8c52c](https://android-review.googlesource.com/#/q/I8c52cdaf8b5546f6505ff93668b84170022ca0a5), [I9593d](https://android-review.googlesource.com/#/q/I9593df2393b1399302ade4acc011128fce3277b2), [I01fe1](https://android-review.googlesource.com/#/q/I01fe1cf525fc1f427f18b8c10e45602f3ea04c6f), [I59a23](https://android-review.googlesource.com/#/q/I59a23a57833e4034474fb6890d4681d8ffb274ae), [b/240298691](https://issuetracker.google.com/issues/240298691))

**Bug Fixes**

- `SavedStateHandle` no longer crashes with a `ClassCastException` when calling `get()` with the incorrect class type. ([I6ae7c](https://android-review.googlesource.com/#/q/I6ae7c23cd7e2ac1ec35bfc6b38aef973be1040a0))

### Version 2.6.0-alpha03

October 24, 2022

`androidx.lifecycle:lifecycle-*:2.6.0-alpha03` is released. [Version 2.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cce7b70f6a5ebf955cf748a73c18b63228b22c74..bef0ef1a976b416db5ece6c6da5d388f1cb8cd7b/lifecycle)

**Bug Fixes**

- Fixed an issue with constraints between different Lifecycle modules not working as intended. ([I18d0d](https://android-review.googlesource.com/#/q/I18d0dcbbc1fb2261108ccc700a439d932693870d), [b/249686765](https://issuetracker.google.com/issues/249686765))
- Errors thrown by `LifecycleRegistry.moveToState()` now include a more helpful error messaging that informs developers of the component causing the error. ([Idf4b2](https://android-review.googlesource.com/#/q/Idf4b23476f809e6c6ff2361d9e864653c90fea2a), [b/244910446](https://issuetracker.google.com/issues/244910446))

### Version 2.6.0-alpha02

September 7, 2022

`androidx.lifecycle:lifecycle-*:2.6.0-alpha02` is released. [Version 2.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..cce7b70f6a5ebf955cf748a73c18b63228b22c74/lifecycle)

**API Changes**

- `MediatorLiveData` now includes a constructor to set an initial value. ([Ib6cc5](https://android-review.googlesource.com/#/q/Ib6cc5fa9e5005642b63d563aa0f3b31162ae0063), [b/151244085](https://issuetracker.google.com/issues/151244085))

**Bug Fixes**

- `Lifecycle` artifacts now include [constraints](https://docs.gradle.org/current/userguide/dependency_constraints.html#sec:adding-constraints-transitive-deps) that ensure that all inter-dependent Lifecycle artifacts use the same version, automatically upgrading other dependencies when one is upgraded. [b/242871265](https://issuetracker.google.com/242871265)
- `FlowLiveData.asFlow()` now creates a `callbackFlow` rather than using its own `Channel` implementation to ensure thread-safety and context preservation. ([I4a8b2](https://android-review.googlesource.com/#/q/I4a8b270a92ac3779cbb3d56dae585bf6876396d2), [b/200596935](https://issuetracker.google.com/issues/200596935))
- `FlowLiveData`'s `asLiveData` function will now preserve the initial value of a `StateFlow` when creating the new `LiveData` object. ([I3f530](https://android-review.googlesource.com/#/q/I3f53068b1a071e2f334f2cbab2819e7f7a4c60b2), [b/157380488](https://issuetracker.google.com/issues/157380488))
- From [Lifecycle `2.5.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.1): Custom implementations of `AndroidViewModelFactory` now correctly calls the `create(modelClass)` function when using the stateful constructor with `Lifecycle` 2.4+ ([I5b315](https://android-review.googlesource.com/#/q/I5b315ae80d1498b92e412d9316a90e7fa0e9fb3a), [b/238011621](https://issuetracker.google.com/issues/238011621))

### Version 2.6.0-alpha01

June 29, 2022

`androidx.lifecycle:lifecycle-*:2.6.0-alpha01` is released. [Version 2.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/414e5d56fe642e82b7a9926e3219cbd756e8c9af..8094b683499b4098092c01028b55a38b49e357f2/lifecycle)

**New Features**

- Added a new extension on `StateFlow` and `Flow` of `collectAsStateWithLifecycle` that collect from flows and represents its latest value as Compose State in a lifecycle-aware manner. The flow is collected and the new emission is set to the State's value when the lifecycle is at least in a certain `Lifecycle.State`. When the lifecycle falls below that `Lifecycle.State`, the flow collection stops and the State's value is not updated. ([I1856e](https://android-review.googlesource.com/#/q/I1856e689232fedf11c133907a63bc08b690d2ce9), [b/230557927](https://issuetracker.google.com/issues/230557927))

## Version 2.5

### Version 2.5.1

July 27, 2022

`androidx.lifecycle:lifecycle-*:2.5.1` is released. [Version 2.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/74552ec00140b723c6c5b0253200a99d41cb3019..39f210d4cd36435557d1ec47d9d2dfe06a64ee44/lifecycle)

**Bug Fixes**

- Custom implementations of `AndroidViewModelFactory` now correctly call the `create(modelClass)` function when using the stateful `AndroidViewModelFactory` constructor with `Lifecycle` 2.4+. ([I5b315](https://android-review.googlesource.com/#/q/I5b315ae80d1498b92e412d9316a90e7fa0e9fb3a), [b/238011621](https://issuetracker.google.com/issues/238011621))

### Version 2.5.0

June 29, 2022

`androidx.lifecycle:lifecycle-*:2.5.0` is released. [Version 2.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/414e5d56fe642e82b7a9926e3219cbd756e8c9af..74552ec00140b723c6c5b0253200a99d41cb3019/lifecycle)

**Important changes since 2.4.0**

- `SavedStateHandle` now offers a `getStateFlow()` API that returns a [Kotlin `StateFlow`](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow#stateflow) for monitoring value changes as an alternative to using `LiveData`.

- **ViewModel CreationExtras** - when writing a custom `ViewModelProvider.Factory`, it is no longer required to extend `AndroidViewModelFactory` or `AbstractSavedStateViewModelFactory` to gain access to an `Application` or `SavedStateHandle`, respectively. Instead, these fields are provided to **every** `ViewModelProvider.Factory` subclass as `CreationExtras` via the new overload of `create`: `create(Class<T>, CreationExtras)`. These extras are provided automatically by your Activity or Fragment when using [Activity `1.5.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.0) and [Fragment `1.5.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0), respectively.

      class CustomFactory : ViewModelProvider.Factory {
          override fun <T : ViewModel> create(modelClass: Class<T>, extras: CreationExtras): T {
              return when (modelClass) {
                  HomeViewModel::class -> {
                      // Get the Application object from extras
                      val application = checkNotNull(extras[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY])
                      // Pass it directly to HomeViewModel
                      HomeViewModel(application)
                  }
                  DetailViewModel::class -> {
                      // Create a SavedStateHandle for this ViewModel from extras
                      val savedStateHandle = extras.createSavedStateHandle()
                      DetailViewModel(savedStateHandle)
                  }
                  else -> throw IllegalArgumentException("Unknown class $modelClass")
              } as T
          }
      }

- `lifecycle-viewmodel` now provides a `viewModelFactory` Kotlin DSL that allows you define your `ViewModelProvider.Factory` in terms of one or more lambda initializers, one for each particular `ViewModel` class your custom factory supports, using `CreationExtras` as the primary data source.

      val customFactory = viewModelFactory {
          // The return type of the lambda automatically sets what class this lambda handles
          initializer {
              // Get the Application object from extras provided to the lambda
              val application = checkNotNull(get(ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY))
              HomeViewModel(application)
          }
          initializer {
              val savedStateHandle = createSavedStateHandle()
              DetailViewModel(savedStateHandle)
          }
      }

- `lifecycle-viewmodel-compose` now offers a `viewModel()` API that takes a lambda factory for creating a `ViewModel` instance without requiring the creation of a custom `ViewModelProvider.Factory`.

      // Within a @Composable, you can now skip writing a custom Factory
      // and instead write a lambda to do the initialization of your ViewModel
      val detailViewModel = viewModel {
        // This lambda is only called the first time the ViewModel is created
        // and all CreationExtras are available inside the lambda
        val savedStateHandle = createSavedStateHandle()
        DetailViewModel(savedStateHandle)
      }

- **SavedStateHandle Compose Saver Integration** - the `lifecycle-viewmodel-compose` artifact now contains new experimental APIs in `SavedStateHandle.saveable` that allow `rememberSaveable` like behavior backed by the `SavedStateHandle` of a \`ViewModel.

      class ListScreenViewModel(handle: SavedStateHandle): ViewModel() {
          // This value survives both configuration changes and process death and recreation
          val editMode by handle.saveable { mutableStateOf(false) }
      }

- Added an `addCloseable()` API and a new constructor overload that allow you to add one or more `Closeable` objects to the `ViewModel` that will be closed when the `ViewModel` is cleared without requiring any manual work in `onCleared()`.

  For instance, to create a coroutine scope that you can inject into a ViewModel, but control via testing, you can create a `CoroutineScope` that implements `Closeable`:

      class CloseableCoroutineScope(
          context: CoroutineContext = SupervisorJob() + Dispatchers.Main.immediate
      ) : Closeable, CoroutineScope {
          override val coroutineContext: CoroutineContext = context
          override fun close() {
              coroutineContext.cancel()
         }
      }

  Which can then be used in your `ViewModel` constructor while maintaining the same lifetime as `viewModelScope`:

      class TestScopeViewModel(
          val customScope: CloseableCoroutineScope = CloseableCoroutineScope()
      ) : ViewModel(customScope) {
          // You can now use customScope in the same way as viewModelScope
      }

**Behavior changes**

- Attempting to move the `Lifecycle.State` from `INITIALIZED` to `DESTROYED` will now always throw an `IllegalStateException` regardless of whether the `Lifecycle` has an attached observer.
- `LifecycleRegistry` will now clear their observers when they reach the `DESTROYED` state.

### Version 2.5.0-rc02

June 15, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-rc02` is released. [Version 2.5.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/916417e4f9a7ec087578a0a8ddc43be1eef606d8..487a289e6247cbd34f8b4d61cd4d06d77dd97fd3/lifecycle)

**Bug Fixes**

- `ViewModelProvider` will no longer crash when mixing previous versions of compileOnly Lifecycle dependencies with versions 2.5+. ([I81a66](https://android-review.googlesource.com/#/q/I81a66ddfc4bc1fb9a98fa8fa526176a8506e1ed8), [b/230454566](https://issuetracker.google.com/issues/230454566))

### Version 2.5.0-rc01

May 11, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-rc01` is released. [Version 2.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c0a89ec374961b3015097ab307ebb8196dbe3888..b8f6a135f523873303760f64f096edf69d71b40b/lifecycle)

**Bug Fixes**

- `MediatorLiveData.addSource()` now throws a `NullPointerException` when passed a `null` source instead of propagating the `null` source to observers.([Ibd0fb](https://android-review.googlesource.com/#/q/Ibd0fbe4d6efef0c4b6bab85eb27b4ed1b872382d), [b/123085232](https://issuetracker.google.com/123085232))

### Version 2.5.0-beta01

April 20, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-beta01` is released. [Version 2.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..c0a89ec374961b3015097ab307ebb8196dbe3888/lifecycle)

**API Changes**

- Added `SavedStateHandle.saveable` property delegates to use property names as keys for persisting state into the `SavedStateHandle` ([I8bb86](https://android-review.googlesource.com/#/q/I8bb86c6c636e62f89b61d8406ea1ecb8435783f6), [b/225014345](https://issuetracker.google.com/issues/225014345))

**Bug Fixes**

- Fixed an issue where nesting one `NavHost` within another `NavHost` in a non-primary bottom navigation tab would lead to an `IllegalStateException` when using multiple back stacks. ([I11bd5](https://android-review.googlesource.com/#/q/I11bd5173f035ae1da7922b4142fcedc0f3b54ff6), [b/228865698](https://issuetracker.google.com/228865698))

### Version 2.5.0-alpha06

April 6, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha06` is released. [Version 2.5.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5ef5671233460b844828e14a816255dbf7904868..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/lifecycle)

**New Features**

- Add experimental `MutableState` overload to `SavedStateHandle.saveable` for parity with `rememberSaveable` ([I38cfe](https://android-review.googlesource.com/#/q/I38cfecc6ba176e003385b4117196828ab1ba993f), [b/224565154](https://issuetracker.google.com/issues/224565154))

**API Changes**

- `CreationExtras` is now abstract instead of sealed. ([Ib8a7a](https://android-review.googlesource.com/#/q/Ib8a7a2205e87995d4a8fd2e17a8a1507493b21a3))

**Bug Fixes**

- Fixed an `IllegalStateException: Already attached to lifecycleOwner` error caused by `SavedStateHandleController`. ([I7ea47](https://android-review.googlesource.com/#/q/I7ea470c1af0385b8bc9d8ca653c84cc8d224e6cf), [b/215406268](https://issuetracker.google.com/215406268))

### Version 2.5.0-alpha05

March 23, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha05` is released. [Version 2.5.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/33cb12e8aba043a05b40470a5ef3be1b35114fd5..5ef5671233460b844828e14a816255dbf7904868/lifecycle)

**New Features**

- The `lifecycle-viewmodel-compose` module now provides `SavedStateHandleSaver`, an experimental API that ensures values in a `SavedStateHandle` are integrated correctly with the same saved instance state that `rememberSaveable` uses. ([Ia88b7](https://android-review.googlesource.com/#/q/Ia88b79c56a5f82263ddaf436777dfc1c4ab73704), [b/195689777](https://issuetracker.google.com/issues/195689777))

**API Changes**

- Fixed a compatibility issue with Lifecycle 2.3 and newer Lifecycle versions in Java. ([I52c8a](https://android-review.googlesource.com/#/q/I52c8a0f83234fea55eea55d0b2e9718bcebd21fd), [b/219545060](https://issuetracker.google.com/issues/219545060))

**Bug Fixes**

- `SavedStateViewFactory` now supports using `CreationExtras` even when it was initialized with a `SavedStateRegistryOwner`. If extras are provided, the initialized arguments are ignored. ([I6c43b](https://android-review.googlesource.com/#/q/I6c43bfd75888cb4b8bdd610cd07d4962aaba37ea), [b/224844583](https://issuetracker.google.com/issues/224844583))

### Version 2.5.0-alpha04

March 9, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha04` is released. [Version 2.5.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..33cb12e8aba043a05b40470a5ef3be1b35114fd5/lifecycle)

**API Changes**

- `SavedStateHandle` now offers a `getStateFlow()` API that returns a [Kotlin `StateFlow`](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow#stateflow) for monitoring value changes as an alternative to using `LiveData`. ([Iad3ab](https://android-review.googlesource.com/#/q/Iad3ab4826281fdd87077b23356e444d17bc19cf6), [b/178037961](https://issuetracker.google.com/issues/178037961))

### Version 2.5.0-alpha03

February 23, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha03` is released. [Version 2.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db2ecbef194afcddfaede22e1d884a8959a9277c..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/lifecycle)

**New Features**

- Added an `addCloseable()` API and a new constructor overload that allow you to add one or more `Closeable` objects to the `ViewModel` that will be closed when the `ViewModel` is cleared without requiring any manual work in `onCleared()`. ([I55ea0](https://android-review.googlesource.com/#/q/I55ea006f3ddcfbf358c488b30d65a21f4fc85998))
- `lifecycle-viewmodel` now provides an `InitializerViewModelFactory` that allows you to add lambda for handling particular `ViewModel` classes, using `CreationExtras` as the primary data source. ([If58fc](https://android-review.googlesource.com/#/q/If58fc49053a6b551643e411c648da564680bff32), [b/216687549](https://issuetracker.google.com/issues/216687549))
- `lifecycle-viewmodel-compose` now offers a `viewModel()` API that takes a lambda factory for creating a `ViewModel` instance without requiring the creation of a custom `ViewModelProvider.Factory`. ([I97fbb](https://android-review.googlesource.com/#/q/I97fbb96b6426eed4805feffe249220a783ec8999), [b/216688927](https://issuetracker.google.com/issues/216688927))

**API Changes**

- You can now create a `ViewModel` with `CreationExtras` via `lifecycle-viewmodel-compose`. ([I08887](https://android-review.googlesource.com/#/q/I08887cf8df03ade08dceeb84bccbe3fd9748186e), [b/216688927](https://issuetracker.google.com/issues/216688927))

**Behavior changes**

- Attempting to move the `Lifecycle.State` from `INITIALIZED` to `DESTROYED` will now always throw an `IllegalStateException` regardless of whether the `Lifecycle` has an attached observer. ([I7c390](https://android-review.googlesource.com/#/q/I7c3903602cc4b9be234a0bed6e6392e710ce3206), [b/177924329](https://issuetracker.google.com/issues/177924329))
- `LifecycleRegistry` will now clear their observers when they reach the `DESTROYED` state. ([I4f8dd](https://android-review.googlesource.com/#/q/I4f8ddff68b9daebbd89aaa6d9abe7d462081d45e), [b/142925860](https://issuetracker.google.com/issues/142925860))

### Version 2.5.0-alpha02

February 9, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha02` is released. [Version 2.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9dceceb54300ed028a7e8fc7a3454f270337ffde..db2ecbef194afcddfaede22e1d884a8959a9277c/lifecycle)

**API Changes**

- `SavedStateHandle` and `SavedStateViewModelFactory` have been converted to Kotlin. This has improved the nullability of the generics in both classes. ([Ib6ce2](https://android-review.googlesource.com/#/q/Ib6ce2007340487f0f4a7d80112ccb94db9c0e3d8), [b/216168263](https://issuetracker.google.com/issues/216168263), [I9647a](https://android-review.googlesource.com/#/q/I9647ab9888955fbdc3b90f9ab86f8204df038a7b), [b/177667711](https://issuetracker.google.com/issues/177667711))
- The `LiveData` `switchMap` function parameter can now have a nullable output. ([I40396](https://android-review.googlesource.com/#/q/I40396c3279a9506a52a4ab1f81e98af2120ff4e0), [b/132923666](https://issuetracker.google.com/issues/132923666))
- The `LiveData` -ktx extensions are now annotated with `@CheckResult` to enforce that the result is used when calling these functions. ([Ia0f05](https://android-review.googlesource.com/#/q/Ia0f05f444838c04ea56cccc066a7270337b65000), [b/207325134](https://issuetracker.google.com/issues/207325134))

**Behavior changes**

- `SavedStateHandle` now properly stores the defaultValue when no value for the specified key exists. ([I1c6ce](https://android-review.googlesource.com/#/q/I1c6ce7584520393eaf58884f92e0b6d90ff7de12), [b/178510877](https://issuetracker.google.com/issues/178510877))

**Bug Fixes**

- From [Lifecycle `2.4.1`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.4.1): Updated `lifecycle-process` to depend on [Startup 1.1.1](https://developer.android.com/jetpack/androidx/releases/startup#1.1.1) to ensure that fixes that prevent `ProcessLifecycleInitializer` from throwing a `StartupException` are available by default. ([Ib01df](https://android-review.googlesource.com/#/q/Ib01dfbba1d63aa03e43e09ee8886cc76e1050e1b), [b/216490724](https://issuetracker.google.com/issues/216490724))
- There is now an improved error message when custom `AndroidViewModel` classes have parameters in the wrong order and attempt to create a `ViewModel`. ([I340f7](https://android-review.googlesource.com/#/q/I340f7696bbf90e331e0b727e9195210cf1dadd0a), [b/177667711](https://issuetracker.google.com/issues/177667711))
- You can now create a view model via `CreationExtras` using the `AndroidViewModelFactory` without setting an application. ([I6ebef](https://android-review.googlesource.com/#/q/I6ebefdf40940a08576a92ee4fb2dcc2b561d781d), [b/217271656](https://issuetracker.google.com/issues/217271656))

### Version 2.5.0-alpha01

January 26, 2022

`androidx.lifecycle:lifecycle-*:2.5.0-alpha01` is released. [Version 2.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03e82488323f4f6d9999228d07c0336a54f4798e..9dceceb54300ed028a7e8fc7a3454f270337ffde/lifecycle)

**ViewModel CreationExtras**

With this release, we are laying the groundwork for restructuring how a `ViewModel` is constructed. Instead of a rigid set of subclasses of `ViewModelProvider.Factory` that each add additional functionality (allowing an `Application` constructor parameter via `AndroidViewModelFactory`, allowing a `SavedStateHandle` constructor parameter via `SavedStateViewModelFactory` and `AbstractSavedStateViewModelFactory`, etc.), we are moving to a world of stateless factories that rely on a new concept, `CreationExtras`. ([Ia7343](https://android-review.googlesource.com/#/q/Ia73439cb2282609a9a1eaebf8ba79b9cc93feb7c), [b/188691010](https://issuetracker.google.com/issues/188691010), [b/188541057](https://issuetracker.google.com/issues/188541057))

With this change, `ViewModelProvider` no longer makes direct calls into the previous `create(Class<T>)` method of `ViewModelProvider.Factory`. Instead, it calls into a new overload of `create`: `create(Class<T>, CreationExtras)`. This means that any direct implementation of the `ViewModelProvider.Factory` instance now has access to each of these new `CreationExtras`:

- `ViewModelProvider.NewInstanceFactory.VIEW_MODEL_KEY`: this `String` provides access to the custom key you passed to `ViewModelProvider.get()`.
- `ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY` provides access to the `Application` class.
- `SavedStateHandleSupport.SAVED_STATE_REGISTRY_OWNER_KEY` provides access to the `SavedStateRegistryOwner` that is being used to construct this ViewModel.
- `SavedStateHandleSupport.VIEW_MODEL_STORE_OWNER_KEY` provides access to the `ViewModelStoreOwner` that is being used to construct this ViewModel.
- `SavedStateHandleSupport.DEFAULT_ARGS_KEY` provides access to the `Bundle` of arguments that should be used to construct a `SavedStateHandle`.

These extras are provided by default when using [Activity `1.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/activity#1.5.0-alpha01), [Fragment `1.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/fragment#1.5.0-alpha01), and [Navigation `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.5.0-alpha01). If you use an earlier version of those libraries, your `CreationExtras` will be empty - all of the existing subclasses of `ViewModelProvider.Factory` have been rewritten to support both the legacy creation path used by earlier versions of those libraries and the `CreationExtras` path which will be used going forward.

These `CreationExtras` allow you to construct a `ViewModelProvider.Factory` that passes just the information you need to each `ViewModel` without relying on a strict hierarchy of Factory subclasses:

    class CustomFactory : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>, extras: CreationExtras): T {
            return when (modelClass) {
                HomeViewModel::class -> {
                    // Get the Application object from extras
                    val application = checkNotNull(extras[ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY])
                    // Pass it directly to HomeViewModel
                    HomeViewModel(application)
                }
                DetailViewModel::class -> {
                    // Create a SavedStateHandle for this ViewModel from extras
                    val savedStateHandle = extras.createSavedStateHandle()
                    DetailViewModel(savedStateHandle)
                }
                else -> throw IllegalArgumentException("Unknown class $modelClass")
            } as T
        }
    }

We use the `createSavedStateHandle()` Kotlin extension function on `CreationExtras` from `SavedStateHandleSupport` to construct a `SavedStateHandle` only for the one ViewModel that needs it. ([Ia6654](https://android-review.googlesource.com/#/q/Ia6654a36eff3c71dc45dbf35e447d1efe24b5b4b), [b/188541057](https://issuetracker.google.com/issues/188541057))

Custom `CreationExtras` can be provided by overriding `getDefaultViewModelCreationExtras()` in your `ComponentActivity` or `Fragment`, thus making them available to your custom `ViewModelProvider.Factory` as a built in form of assisted injection. These extras will automatically be made available to your custom Factory when used directly with `ViewModelProvider` or when using the `by viewModels()` and `by activityViewModels()` Kotlin property extensions. ([I79f2b](https://android-review.googlesource.com/#/q/I79f2bbd8ae78103d3ef764fd527674cdfb592936), [b/207012584](https://issuetracker.google.com/issues/207012584), [b/207012585](https://issuetracker.google.com/issues/207012585), [b/207012490](https://issuetracker.google.com/issues/207012490))

**Bug Fixes**

- Fixed an issue where the default value provided to a `SavedStateHandle` would reappear after process death and recreation, even if it was specifically removed from the `SavedStateHandle`. As a consequence of this, `SavedStateHandle` will no longer merge default values and restored values together, instead only using the restored values as the source of truth. ([I53a4b](https://android-review.googlesource.com/#/q/I53a4bbffc6990f8dea902584daf47e780ae9abdb))

## Version 2.4

### Version 2.4.1

February 9, 2022

`androidx.lifecycle:lifecycle-*:2.4.1` is released. [Version 2.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/03e82488323f4f6d9999228d07c0336a54f4798e..4908527c90073e330885a24394601f337e93abd9/lifecycle)

**Bug Fixes**

- Backported from [Lifecycle `2.5.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.5.0-alpha01): Fixed an issue where the default value provided to a `SavedStateHandle` would re-appear after process death and recreation, even if it was specifically removed from the `SavedStateHandle`. As a consequence of this, `SavedStateHandle` will no longer merge default values and restored values together, instead only using the restored values as the source of truth. ([I53a4b](https://android-review.googlesource.com/#/q/I53a4bbffc6990f8dea902584daf47e780ae9abdb))
- `lifecycle-process` now depends on [Androidx Startup 1.1.1](https://developer.android.com/jetpack/androidx/releases/startup#1.1.1) which fixed a regression in where using `ProcessLifecycleInitializer` would cause an `StartupException`. ([b/216490724](https://issuetracker.google.com/216490724))

### Version 2.4.0

October 27, 2021

`androidx.lifecycle:lifecycle-*:2.4.0` is released. [Version 2.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/433fef42bf9ce2a319e54a8fc3f7ba350249d2d2..03e82488323f4f6d9999228d07c0336a54f4798e/lifecycle)

**Important changes since 2.3.0**

- `@OnLifecycleEvent` was deprecated. `LifecycleEventObserver` or `DefaultLifecycleObserver` should be used instead.
- `androidx.lifecycle:lifecycle-viewmodel-compose` library was added. It provides `viewModel()` composable and `LocalViewModelStoreOwner`.
  - *Source-breaking change* : `ViewModelProvider` has been rewritten in Kotlin. `ViewModelProvider.Factory.create` method no longer allows nullable generic.
- New coroutines API were added to `androidx.lifecycle:lifecycle-runtime-ktx`:
- `Lifecycle.repeatOnLifecycle`, API that executes a block of code in a coroutine when the Lifecycle is at least in a certain state. The block will cancel and re-launch as the lifecycle moves in and out of the target state;
- `Flow.flowWithLifecycle`, API that emits values from the upstream Flow when the lifecycle is at least in a certain state.
- `DefaultLifecycleObserver` was moved from `lifecycle.lifecycle-common-java8` to `lifecycle.lifecycle-common`. `lifecycle.lifecycle-common-java8`doesn't provide anymore any additional functionality on top of `lifecycle.lifecycle-common`, so dependency on it can be replaced by `lifecycle.lifecycle-common`.
- Non coroutines API from `lifecycle-viewmodel-ktx` have been moved to the `lifecycle-viewmodel` module.
- `lifecycle-process` now uses `androidx.startup` to initialize the `ProcessLifecycleOwner`.

  Previously, this was being done by `androidx.lifecycle.ProcessLifecycleOwnerInitializer`.

  If you used `tools:node="remove"` the `ContentProvider` being used to initialize
  process lifecycle in the past, then you need to do the following instead.

       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities=\"${applicationId}.androidx-startup"
          android:exported="false"
          tools:node=\"merge">
          <!-- If you are using androidx.startup to initialize other components -->
          <meta-data
              android:name="androidx.lifecycle.ProcessLifecycleInitializer"
              android:value="androidx.startup"
              tools:node="remove" />
       </provider>

  (or)

       <!-- If you want to disable androidx.startup completely. -->
       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities="${applicationId}.androidx-startup"
          tools:node="remove">
       </provider>

### Version 2.4.0-rc01

September 29, 2021

`androidx.lifecycle:lifecycle-*:2.4.0-rc01` is released with no changes from Lifecycle 2.4.0-beta01. [Version 2.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1a3dcfb231517d6104969f17063fcc6c97ba6eeb..433fef42bf9ce2a319e54a8fc3f7ba350249d2d2/lifecycle)

### Version 2.4.0-beta01

September 15, 2021

`androidx.lifecycle:lifecycle-*:2.4.0-beta01` is released. [Version 2.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d725303accfa9be6d5c3d61c7603ed1b9a780cbd..1a3dcfb231517d6104969f17063fcc6c97ba6eeb/lifecycle)

**API Changes**

- `@OnLifecycleEvent` was deprecated. `LifecycleEventObserver` or `DefaultLifecycleObserver` should be used instead. ([I5a8fa](https://android-review.googlesource.com/#/q/I5a8fa69584fe45c4dfa44c37d08023c0b2235dbb))
- DefaultLifecycleObserver was moved from `androidx.lifecycle.lifecycle-common-java8` to `androidx.lifecycle.lifecycle-common`. `androidx.lifecycle.lifecycle-common-java8` doesn't provide anymore any additional functionality on top of `androidx.lifecycle.lifecycle-common`, so dependency on it can be replaced by `androidx.lifecycle.lifecycle-common`. ([I021aa](https://android-review.googlesource.com/#/q/I021aab3f3b3493e97775757b5aa307c494690b40))
- Non coroutines API from `lifecycle-viewmodel-ktx` have been moved to the `lifecycle-viewmodel` module. ([I6d5b2](https://android-review.googlesource.com/#/q/I6d5b2c3702472d7c6a50b44fc00f7b6e516edba7))

**External Contribution**

- Thanks [dmitrilc](https://github.com/dmitrilc) for fixing a type in the `ViewModel` documentation! ([#221](https://github.com/androidx/androidx/pull/221))

### Version 2.4.0-alpha03

August 4, 2021

`androidx.lifecycle:lifecycle-*:2.4.0-alpha03` is released. [Version 2.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..d725303accfa9be6d5c3d61c7603ed1b9a780cbd/lifecycle)

**API Changes**

- **Source-breaking change** : ViewModelProvider has been rewritten in Kotlin. `ViewModelProvider.Factory.create` method no longer allows nullable generic. ([I9b9f6](https://android-review.googlesource.com/#/q/I9b9f6617dc9377bc99a954eb096194b1240c98fe))

**Behavior Changes**

- The `Lifecycle.repeatOnLifecycle`: `block` is now always invoked serially when repeating execution. ([Ibab33](https://android-review.googlesource.com/#/q/Ibab3391210cbd14fdfe950899f9cb226bd9512fb))

**External Contribution**

- Thanks [chao2zhang](https://github.com/chao2zhang) for fixing the code snippets in the `repeatOnLifecycle` documentation. [#205](https://github.com/androidx/androidx/pull/205).

### Version 2.4.0-alpha02

June 16, 2021

`androidx.lifecycle:lifecycle-*:2.4.0-alpha02` is released. [Version 2.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..ccf79f53033e665475116a4e78ff124df2a52c4b/lifecycle)

**New Features**

- Added a new `RepeatOnLifecycleWrongUsage` lint check to `lifecycle-runtime-ktx` that detects when `repeateOnLifecycle` is incorrectly used in `onStart()` or `onResume()`. ([706078](https://android-review.googlesource.com/#/q/706078c215107f5cde51b66233dd0158bca729dc), [b/187887400](https://issuetracker.google.com/187887400))

**API Changes**

- The `LifecycleOwner.addRepeatingJob` API is removed in favor of `Lifecycle.repeatOnLifecycle` that respects structured concurrency and is easier to reason about. ([I4a3a8](https://android-review.googlesource.com/#/q/I4a3a878686a1b2153dc97778f7942bb3624d6915))
- Make `ProcessLifecycleInitializer` public so other `androidx.startup.Initializer`s can use these as dependencies. ([I94c31](https://android-review.googlesource.com/#/q/I94c31cbdff9aa4b1adaa459a10a6ab5f54b953b1))

**Bug Fixes**

- Fixed an issue with the `NullSafeMutableLiveData` lint check when the field has modifiers. ([#147](https://github.com/androidx/androidx/pull/147), [b/183696616](https://issuetracker.google.com/183696616))
- Fixed another issue with the `NullSafeMutableLiveData` lint check when using generics. ([#161](https://github.com/androidx/androidx/pull/161), [b/184830263](https://issuetracker.google.com/184830263))

**External Contribution**

- Thanks [maxsav](https://github.com/maxsav) for improving the `NullSafeMutableLiveData` lint check. ([#147](https://github.com/androidx/androidx/pull/147), [b/183696616](https://issuetracker.google.com/183696616))
- Thanks [kozaxinan](https://github.com/kozaxinan) for improving the `NullSafeMutableLiveData` lint check. ([#161](https://github.com/androidx/androidx/pull/161), [b/184830263](https://issuetracker.google.com/184830263))

### Version 2.4.0-alpha01

March 24, 2021

`androidx.lifecycle:lifecycle-*:2.4.0-alpha01` is released. [Version 2.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ab69093e69997058cb4a9e61203401169b6ee2a8..5c42896eb6591b09e3952030fb7ea8d9b8c42713/lifecycle)

**Behavior Changes**

- `lifecycle-process` now uses `androidx.startup` to initialize the `ProcessLifecycleOwner`.

  Previously, this was being done by `androidx.lifecycle.ProcessLifecycleOwnerInitializer`.

  If you used `tools:node="remove"` the `ContentProvider` being used to initialize
  process lifecycle in the past, then you need to do the following instead.

       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities=\"${applicationId}.androidx-startup"
          android:exported="false"
          tools:node=\"merge">
          <!-- If you are using androidx.startup to initialize other components -->
          <meta-data
              android:name="androidx.lifecycle.ProcessLifecycleInitializer"
              android:value="androidx.startup"
              tools:node="remove" />
       </provider>

  (or)

       <!-- If you want to disable androidx.startup completely. -->
       <provider
          android:name="androidx.startup.InitializationProvider"
          android:authorities="${applicationId}.androidx-startup"
          tools:node="remove">
       </provider>

**API Changes**

- Added a `Flow.flowWithLifecycle` API that emits values from the upstream Flow when the lifecycle is at least in a certain state using the `Lifecycle.repeatOnLifecycle` API. This is an alternative to the also new `LifecycleOwner.addRepeatinJob` API. ([I0f4cd](https://android-review.googlesource.com/#/q/I0f4cdfd2579b2dae2990f30ec67dc4fd97c46bfc))

**Bug Fixes**

- From [Lifecycle 2.3.1](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.1): The `NonNullableMutableLiveData` lint rule can now properly differentiate between field variables with different nullability. ([b/169249668](https://issuetracker.google.com/issues/169249668))

## Lifecycle Viewmodel Compose Version 1.0.0

### Version 1.0.0-alpha07

June 16, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/836237c11d7a415f28bb71acab597579be1d5227..f434dccf3dc4d4e82d8d965da3746615870537b4/lifecycle/lifecycle-viewmodel-compose)

**Breaking API Changes**

- `viewModel()` now takes an optional `ViewModelStoreOwner`, making it easier to work with owners other than the `LocalViewModelStoreOwner`. For example, you can now use `viewModel(navBackStackEntry)` to retrieve a ViewModel associated with a particular navigation graph. ([I2628d](https://android-review.googlesource.com/#/q/I2628d27791bfeb8a0d2f45b0fa8e9e72cb00c34b), [b/188693123](https://issuetracker.google.com/issues/188693123))

> [!NOTE]
> **Note:** this is a binary breaking change - you must upgrade to [Hilt-Navigation-Compose `1.0.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/hilt#hilt-navigation-compose-1.0.0-alpha03) and [Navigation Compose `2.4.0-alpha03`](https://developer.android.com/jetpack/androidx/releases/navigation#2.4.0-alpha03). This may be a source breaking change if you were not specifying `key =` when using `viewModel(key, factory)`. You should use named arguments: `viewModel(key = key, factory = factory)`.

### Version 1.0.0-alpha06

June 2, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/lifecycle/lifecycle-viewmodel-compose)

Updated to be compatible with Compose version `1.0.0-beta08`.

### Version 1.0.0-alpha05

May 18, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e6e72e136ada934db74265667417524ba0ba04f..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/lifecycle/lifecycle-viewmodel-compose)

**New Features**

- Updated to be compatible with Compose version `1.0.0-beta07`.

**Bug Fixes**

- The AndroidManifest files from ui-test-manifest and ui-tooling-data are now compatible with Android 12 ([I6f9de](https://android-review.googlesource.com/#/q/I6f9dec0515ad6eb7fd232eeb124ee0164f4e90cb), [b/184718994](https://issuetracker.google.com/issues/184718994))

### Version 1.0.0-alpha04

April 7, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..0e6e72e136ada934db74265667417524ba0ba04f/lifecycle/lifecycle-viewmodel-compose)

**Dependency Changes**

- This version allows `androidx.hilt:hilt-navigation-compose` and `androidx.navigation:navigation-compose` to sync dependencies on `androidx.compose.compiler:compiler:1.0.0-beta04` and `androidx.compose.runtime:runtime:1.0.0-beta04`. For 1.0.0, it is required that the compiler and runtime match.

### Version 1.0.0-alpha03

March 10, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b6cff92e45f1d4467086aa2c6aa0248b4883950..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/lifecycle/lifecycle-viewmodel-compose)

**API Changes**

- `LocalViewModelStoreOwner.current` now returns a nullable `ViewModelStoreOwner` to better determine whether a `ViewModelStoreOwner` is available in the current composition. APIs that require a `ViewModelStoreOwner`, such as `viewModel()` and `NavHost`, still throw an exception if a `ViewModelStoreOwner` is not set. ([Idf39a](https://android-review.googlesource.com/#/q/Idf39af28f00e0c0522a897a1202385d21da828be))

### Lifecycle-Viewmodel-Compose Version 1.0.0-alpha02

February 24, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..4b6cff92e45f1d4467086aa2c6aa0248b4883950/lifecycle/lifecycle-viewmodel-compose)

**API Changes**

- `LocalViewModelStoreOwner` now has a `provides` functions that can be used with `CompositionLocalProvider`, replacing the `asProvidableCompositionLocal()` API. ([I45d24](https://android-review.googlesource.com/#/q/I45d244bea668db72a536c1f9bbdb7b24073aba0c))

> [!NOTE]
> **Note:** Lifecycle ViewModel Compose 1.0.0-alpha02 is only compatible with Compose 1.0.0-beta01.

### Lifecycle-Viewmodel-Compose Version 1.0.0-alpha01

February 10, 2021

`androidx.lifecycle:lifecycle-viewmodel-compose:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b/lifecycle/lifecycle-viewmodel-compose)

**New Features**

- The `viewModel()` composable and `LocalViewModelStoreOwner` were moved from `androidx.compose.ui.viewinterop` to this artifact in the `androidx.lifecycle.viewmodel.compose` package. ([I7a374](https://android-review.googlesource.com/#/q/I7a374b76168a6387e585337c131a988bddcb912b))

> [!NOTE]
> **Note:** Lifecycle ViewModel Compose 1.0.0-alpha01 is only compatible with Compose 1.0.0-alpha12.

## Version 2.3.1

### Lifecycle Version 2.3.1

March 24, 2021

`androidx.lifecycle:lifecycle-*:2.3.1` is released. [Version 2.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ab69093e69997058cb4a9e61203401169b6ee2a8..0b84d3ed85bf44f60f4fdda15ef20767cfe06876/lifecycle)

**Bug Fixes**

- The `NonNullableMutableLiveData` lint rule can now properly differentiate between field variables with different nullability. ([b/169249668](https://issuetracker.google.com/issues/169249668))

## Version 2.3.0

### Version 2.3.0

February 10, 2021

`androidx.lifecycle:lifecycle-*:2.3.0` is released. [Version 2.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7dcfa61622c99f7a9814edc198612f91485213c7..ab69093e69997058cb4a9e61203401169b6ee2a8/lifecycle)

**Major changes since 2.2.0**

- **`SavedStateHandle` support for non-parcelable classes** : `SavedStateHandle` now supports lazy serialization by allowing you to call `setSavedStateProvider()` for a given key, providing a `SavedStateProvider` that will get a callback to `saveState()` when the `SavedStateHandle` is asked to save its state. See [Saving non-parcelable classes](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate#non-parcelable).
- **Lifecycle Behavior Enforcement** :
  - LifecycleRegistry now enforces `DESTROYED` as a terminal state.
  - `LifecycleRegistry` now verifies that its methods are called on main thread. It was always a requirement for lifecycles of activities, fragments etc. An addition of observers from non-main threads resulted in hard to catch crashes in runtime. For `LifecycleRegistry` objects that owned by your own components, you can explicitly opt out from checks by using `LifecycleRegistry.createUnsafe(...)`, but then you have to ensure that a proper synchronization is in place when this `LifecycleRegistry` is accessed from different threads.
- **Lifecycle State and Event Helpers** : Added static helper methods of `downFrom(State)`, `downTo(State)`, `upFrom(State)`, `upTo(State)` to `Lifecycle.Event` for generating the `Event` given a `State` and transition direction. Added the `getTargetState()` method that provides the `State` that the Lifecycle will transition to directly following the `Event`.
- **`withStateAtLeast`** : Added `Lifecycle.withStateAtLeast` APIs that await a lifecycle state and run a non-suspending block of code synchronously at the point of state change, then resume with the result. These APIs differ from the existing `when*` methods as they do not permit running suspending code and do not employ a custom dispatcher. ([aosp/1326081](https://android-review.googlesource.com/1326081))
- **`ViewTree` APIs** : A new `ViewTreeLifecycleOwner.get(View)` and `ViewTreeViewModelStoreOwner.get(View)` API allows you to retrieve the containing `LifecycleOwner` and `ViewModelStoreOwner`, respectively, given a `View` instance. You must upgrade to [Activity `1.2.0`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0) and [Fragment `1.3.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0), and [AppCompat 1.3.0-alpha01](https://developer.android.com/jetpack/androidx/releases/appcompat:1.3.0-alpha01) or higher to populate this correctly. The `findViewTreeLifecycleOwner` and `findViewTreeViewModelStoreOwner` Kotlin extensions are available in `lifecycle-runtime-ktx` and `lifecycle-viewmodel-ktx`, respectively.
- **`LiveData.observe()` Kotlin extension deprecation** : The `LiveData.observe()` Kotlin extension necessary to use lambda syntax is now deprecated as it is not necessary when using Kotlin 1.4.

### Version 2.3.0-rc01

December 16, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-rc01` is released. [Version 2.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5..7dcfa61622c99f7a9814edc198612f91485213c7/lifecycle)

**Bug Fixes**

- The `keys()` method of `SavedStateHandle` is now consistent before and after the state is saved - it now includes keys previously used with `setSavedStateProvider()` in addition to the keys used with `set()` and `getLiveData()`. ([aosp/1517919](https://android-review.googlesource.com/c/platform/frameworks/support/+/1517919), [b/174713653](https://issuetracker.google.com/174713653))

**External Contribution**

- The APIs to [suspend Lifecycle-aware coroutines](https://developer.android.com/topic/libraries/architecture/coroutines#suspend) now better handle calls to `yield()`. Thanks Nicklas Ansman Giertz! ([aosp/1430830](https://android-review.googlesource.com/c/platform/frameworks/support/+/1430830), [b/168777346](https://issuetracker.google.com/168777346))

### Version 2.3.0-beta01

October 1, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-beta01` is released. [Version 2.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/lifecycle)

**API Changes**

- The `LiveData.observe()` Kotlin extension necessary to use lambda syntax is now deprecated as it is not necessary when using Kotlin 1.4. ([I40d3f](https://android-review.googlesource.com/#/q/I40d3f40cbaebda0df2292d60704d9c19c9d835b9))

**Bug Fixes**

- Upgrade androidx to use Kotlin 1.4 ([Id6471](https://android-review.googlesource.com/#/q/Id647100407925c16d734c8c43392b4e2d108d0e3), [b/165307851](https://issuetracker.google.com/issues/165307851), [b/165300826](https://issuetracker.google.com/issues/165300826))

**Documentation Changes**

- The `liveData` builder and `asLiveData()` docs have been updated to include details about changing the given timeout values. ([aosp/1122324](https://android-review.googlesource.com/c/platform/frameworks/support/+/1122324))

### Version 2.3.0-alpha07

August 19, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha07` is released. [Version 2.3.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..96eb302ee1740ba656c90c9fb27df3723a1a89c1/lifecycle)

**Bug Fixes**

- Fixed a crash issue in the `NullSafeMutableLiveData` Lint check. ([aosp/1395367](https://android-review.googlesource.com/1395367))

### Version 2.3.0-alpha06

July 22, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha06` is released. [Version 2.3.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/lifecycle)

**New Features**

- Added static helper methods of `downFrom(State)`, `downTo(State)`, `upFrom(State)`, `upTo(State)` to `Lifecycle.Event` for generating the `Event` given a `State` and transition direction. Added the `getTargetState()` method that provides the `State` that the Lifecycle will transition to directly following the `Event`. ([I00887](https://android-review.googlesource.com/#/q/I008870696ecc61e039c35a1dcf4e2dfd3a8fcb24))
- Added `Lifecycle.withStateAtLeast` APIs that await a lifecycle state and run a non-suspending block of code synchronously at the point of state change, then resume with the result. These APIs differ from the existing `when*` methods as they do not permit running suspending code and do not employ a custom dispatcher. ([aosp/1326081](https://android-review.googlesource.com/1326081))

**Behavior Changes**

- LifecycleRegistry now enforces `DESTROYED` as a terminal state. ([I00887](https://android-review.googlesource.com/#/q/I008870696ecc61e039c35a1dcf4e2dfd3a8fcb24))
- `LifecycleRegistry` now verifies that its methods are called on main thread. It was always a requirement for lifecycles of activities, fragments etc. An addition of observers from non-main threads resulted in hard to catch crashes in runtime. For `LifecycleRegistry` objects that owned by your own components, you can explicitly opt out from checks by using `LifecycleRegistry.createUnsafe(...)`, but then you have to ensure that a proper synchronization is in place when this `LifecycleRegistry` is accessed from different threads ([Ie7280](https://android-review.googlesource.com/#/q/Ie72809b34d4e66c20b9694548359a1209d438f3d), [b/137392809](https://issuetracker.google.com/issues/137392809))

**Bug Fixes**

- Fixed a crash in `NullSafeMutableLiveData`. ([b/159987480](https://issuetracker.google.com/159987480))
- Fixed an `ObsoleteLintCustomCheck` for Lint checks bundled with `lifecycle-livedata-core-ktx` (and specifically `NullSafeMutableLiveData`). ([b/158699265](https://issuetracker.google.com/158699265))

### Version 2.3.0-alpha05

June 24, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha05` is released. [Version 2.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea4dafe72ba1ec91a105da3128954d5ed7f1cd0..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/lifecycle)

**Bug Fixes**

- `LiveData` now better handles reentrant cases, avoiding duplicate calls to `onActive()` or `onInactive()`. ([b/157840298](https://issuetracker.google.com/issues/157840298))
- Fixed an issue where Lint checks would not run when using Android Studio 4.1 Canary 6 or higher. ([aosp/1331903](https://android-review.googlesource.com/1331903))

### Version 2.3.0-alpha04

June 10, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha04` is released. [Version 2.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccc6e95c574b66563952c33fbe26888b93a0e0cb..bea4dafe72ba1ec91a105da3128954d5ed7f1cd0/lifecycle)

**Bug Fixes**

- Fixed a crash in the `NonNullableMutableLiveData` Lint check. ([b/157294666](https://issuetracker.google.com/issues/157294666))
- The `NonNullableMutableLiveData` Lint check now covers significantly more cases where a `null` value was set on a `MutableLiveData` with a non-null type parameter. ([b/156002218](https://issuetracker.google.com/issues/156002218))

### Version 2.3.0-alpha03

May 20, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha03` are released. [Version 2.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b752a10305d7cd58a7f50ad094ed54af4d765f27..ccc6e95c574b66563952c33fbe26888b93a0e0cb/lifecycle)

**New Features**

- `SavedStateHandle` now supports lazy serialization by allowing you to call `setSavedStateProvider()` for a given key, providing a `SavedStateProvider` that will get a callback to `saveState()` when the `SavedStateHandle` is asked to save its state. ([b/155106862](https://issuetracker.google.com/issues/155106862))
- A new `ViewTreeViewModelStoreOwner.get(View)` API allows you to retrieve the containing `ViewModelStoreOwner` given a `View` instance. You must upgrade to [Activity `1.2.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha05), [Fragment `1.3.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha05), and [AppCompat `1.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/appcompat#1.3.0-alpha01) to populate this correctly. A `findViewModelStoreOwner()` Kotlin extension has been added to `lifecycle-viewmodel-ktx`. ([aosp/1295522](https://android-review.googlesource.com/1295522))

**Bug Fixes**

- Fixed an issue that caused the `MutableLiveData` Lint checks released in [Lifecycle `2.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha01) from being published alongside the `lifecycle-livedata-core-ktx` artifact. ([b/155323109](https://issuetracker.google.com/issues/155323109))

### Version 2.3.0-alpha02

April 29, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha02` is released. [Version 2.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/666ae665acfcfa2a20eccc18e4494808169742f4..b752a10305d7cd58a7f50ad094ed54af4d765f27/lifecycle)

**API Changes**

- `SavedStateViewModelFactory` now allows you to pass a null `Application` to its constructor to better support cases where one is not readily available and support for `AndroidViewModel` is not needed. ([aosp/1285740](https://android-review.googlesource.com/1285740))

**Bug Fixes**

- Improved cold start performance by avoiding class verification failure on API 28 and lower devices. ([aosp/1282118](https://android-review.googlesource.com/1282118))

### Version 2.3.0-alpha01

March 4, 2020

`androidx.lifecycle:lifecycle-*:2.3.0-alpha01` is released. [Version 2.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fc7c16e8d04b669a38ca27b96646e13d3ae5e733..666ae665acfcfa2a20eccc18e4494808169742f4/lifecycle)

**New Features**

- A new `ViewTreeLifecycleOwner.get(View)` API allows you to retrieve the containing `LifecycleOwner` given a `View` instance. You must upgrade to [Activity `1.2.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/activity#1.2.0-alpha01) and [Fragment `1.3.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/fragment#1.3.0-alpha01) to populate this correctly. A `findViewTreeLifecycleOwner` Kotlin extension is available in `lifecycle-runtime-ktx`. ([aosp/1182361](https://android-review.googlesource.com/1182361), [aosp/1182956](https://android-review.googlesource.com/1182956))
- Added a new Lint check that warns you when setting a `null` value on a `MutableLiveData` that has been defined in Kotlin as non-null. This is available when using the `livedata-core-ktx` or `livedata-ktx` artifacts. ([aosp/1154723](https://android-review.googlesource.com/1154723), [aosp/1159092](https://android-review.googlesource.com/1159092))
- A new `lifecycle-runtime-testing` artifact is available that provides a `TestLifecycleOwner` that implements `LifecycleOwner` and provides a thread safe mutable `Lifecycle`. ([aosp/1242438](https://android-review.googlesource.com/1242438))

**Bug fixes**

- The `lifecycle-runtime` artifact now has a unique package name. ([aosp/1187196](https://android-review.googlesource.com/1187196))

> [!NOTE]
> **Note:** as per the [Lifecycle `2.2.0` release notes](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.2.0), the `lifecycle-extensions` artifact is no longer published.

## Version 2.2.0

### ViewModel-Savedstate Version 2.2.0

February 5, 2020

`androidx.lifecycle:lifecycle-viewmodel-savedstate:2.2.0` is released. [Version 2.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/fee1737a1d380aa1435ae5fca6336ee350bad4e0..fc7c16e8d04b669a38ca27b96646e13d3ae5e733/lifecycle/lifecycle-viewmodel-savedstate).

Lifecycle ViewModel SavedState now shares the same version as other Lifecycle artifacts. The behavior of `2.2.0` is identical to the behavior of `1.0.0`.

### Version 2.2.0

January 22, 2020

`androidx.lifecycle:lifecycle-*:2.2.0` is released. [Version 2.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/8e4cae9ad8deb81db632012ff7b4980108511947..6d46ea5e549b1ec0d0e48ff6b6e63eb6d34c242c/lifecycle).

**Important changes since 2.1.0**

- **Lifecycle Coroutine Integration** : The new `lifecycle-runtime-ktx` artifact adds integration between Lifecycle and Kotlin coroutines. The `lifecycle-livedata-ktx` has also been expanded to take advantage of coroutines. See [Use Kotlin coroutines with Architecture Components](https://developer.android.com/topic/libraries/architecture/coroutines) for more details.
- **`ViewModelProviders.of()` deprecation** : `ViewModelProviders.of()` has been deprecated. You can pass a `Fragment` or `FragmentActivity` to the new `ViewModelProvider(ViewModelStoreOwner)` constructor to achieve the same functionality when using [Fragment `1.2.0`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0).
- **`lifecycle-extensions` Artifact Deprecation** : With the above deprecation of `ViewModelProviders.of()`, this release marks the deprecation of the last API in `lifecycle-extensions` and this artifact should now be considered deprecated in its entirety. We strongly recommend depending on the specific Lifecycle artifacts you need (such as `lifecycle-service` if you're using `LifecycleService` and `lifecycle-process` if you're using `ProcessLifecycleOwner`) rather than `lifecycle-extensions` as there will not be a future `2.3.0` release of `lifecycle-extensions`.
- **Gradle Incremental Annotation Processor** : Lifecycle's annotation processor is incremental by default. If your app is written in the Java 8 programming language you can use `DefautLifecycleObserver` instead; and if it's written in the Java 7 programming language you can use `LifecycleEventObserver`.

### Version 2.2.0-rc03

December 4, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-rc03` is released. [Version 2.2.0-rc03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/45b11795d6737dd540ccedaec026dc34397f1ba6..8e4cae9ad8deb81db632012ff7b4980108511947/lifecycle).

**Bug fixes**

- Fixed a failure occurring when a mocked `ViewModel` was stored in `ViewModelStore` and queried later with default factory.
- Fix a usage of `Dispatchers.Main.immediate` in `launchWhenCreated` and similar methods to be called synchronously during corresponding lifecycle event. ([aosp/1156203](https://android-review.googlesource.com/c/1156203))

**External contributions**

- Thanks to Anders Järleberg for contributing the fix! ([aosp/1156203](https://android-review.googlesource.com/c/1156203))
- Thanks to Vsevolod Tolstopyatov from Jetbrains for reviewing an implementation of inlined execution.

**Dependency changes**

- Lifecycle Extensions now depends on Fragment `1.2.0-rc03`.

### Version 2.2.0-rc02

November 7, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-rc02` is released. [Version 2.2.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/b7bd1f02d0ebc5d54b228055b60fc52a478c69a3..45b11795d6737dd540ccedaec026dc34397f1ba6/lifecycle).

**Bug fixes**

- Fixed a bug in the proguard setup of the library that affected devices running API 28+ if the target API is below 29. ([b/142778206](https://issuetracker.google.com/issues/142778206))

### Version 2.2.0-rc01

October 23, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-rc01` is released. [Version 2.2.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0b805f6f9716b03d7e7753590d78f3f2115e1e76..b7bd1f02d0ebc5d54b228055b60fc52a478c69a3/lifecycle).

**Bug fixes**

- Fixed an issue where `launchWhenCreated` and related methods would run one frame later than the associated lifecycle method due to its use of `Dispatchers.Main` instead of `Dispatchers.Main.immediate`. ([aosp/1145596](https://android-review.googlesource.com/1145596))

**External contributions**

- Thanks to Nicklas Ansman for contributing the fix! ([aosp/1145596](https://android-review.googlesource.com/1145596))

### Version 2.2.0-beta01

October 9, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-beta01` is released. [Version 2.2.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/af12e75e6b4110f48e44ca121466943909de8f06..0b805f6f9716b03d7e7753590d78f3f2115e1e76/lifecycle).

**Bug fixes**

- Fixed a regression introduced in [Lifecycle 2.2.0-alpha05](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.2.0-alpha05) in the ordering of `ProcessLifecycleOwner` and the activity's `LifecycleOwner` moving to started and resumed on Android 10 devices. ([aosp/1128132](https://android-review.googlesource.com/1128132))
- Fixed a regression introduced in [Lifecycle `2.2.0-alpha05`](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.2.0-alpha05) which would cause a `NullPointerException` when using version `2.0.0` or `2.1.0` of `lifecycle-process`. ([b/141536990](https://issuetracker.google.com/issues/141536990))

### Version 2.2.0-alpha05

September 18, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-alpha05` is released. [Version 2.2.0-alpha05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/44b591fe64e859b4b4e34b2590a5257c255c638c..af12e75e6b4110f48e44ca121466943909de8f06/lifecycle).

**Bug fixes**

- Fixed a race condition in coroutine livedata builder. [b/140249349](http://issuetracker.google.com/140249349)

### Version 2.2.0-alpha04

September 5, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-alpha04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/23fecdb1097a69a528ab6109f661b4e46123aecc..44b591fe64e859b4b4e34b2590a5257c255c638c/lifecycle).

**New features**

- `lifecycleScope`, `whenCreated`, `whenStarted`, `whenResumed`, `viewModelScope`, and the underlying implementation of `liveData` now use `Dispatchers.Main.immediate` instead of `Dispatchers.Main`. ([b/139740492](https://issuetracker.google.com/issues/139740492))

**External contributions**

- Thanks to Nicklas Ansman for contributing the move to `Dispatchers.Main.immediate`! ([aosp/1106073](https://android-review.googlesource.com/1106073))

### Version 2.2.0-alpha03

August 7, 2019

`androidx.lifecycle:lifecycle-*:2.2.0-alpha03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/8acc8b2884fbd5add837e33d631ea687070b1aaa..23fecdb1097a69a528ab6109f661b4e46123aecc/lifecycle).

**New features**

- Implementations of `ViewModelStoreOwner` can now optionally implement `HasDefaultViewModelProviderFactory` to provide a default `ViewModelProvider.Factory`. This has been done for [Activity `1.1.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.1.0-alpha02), [Fragment `1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-alpha02), and [Navigation `2.2.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.0-alpha01). ([aosp/1092370](https://android-review.googlesource.com/1092370), [b/135716331](https://issuetracker.google.com/issues/135716331))

**API changes**

- `ViewModelProviders.of()` has been deprecated. You can pass a `Fragment` or `FragmentActivity` to the new `ViewModelProvider(ViewModelStoreOwner)` constructor to achieve the same functionality. ([aosp/1009889](https://android-review.googlesource.com/1009889))

### Version 2.2.0-alpha02

July 2, 2019

`androidx.lifecycle:*:2.2.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7a4525ac3c56adff5e0de713ca54eae89518e28c..8acc8b2884fbd5add837e33d631ea687070b1aaa/lifecycle).

**API changes**

- Replaced `LiveDataScope.initialValue` with `LiveDataScope.latestValue` which will track the current emitted value of the `liveData` block.
- Added a new overload to the `liveData` builder that receives `timeout` parameter as type `Duration`

### Version 2.2.0-alpha01

May 7, 2019

`androidx.lifecycle:*:2.2.0-alpha01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7e9a5afb451c3bff1c20e2ce0121c3677810cd5b..be101c5ab63016840c743ab315e9a77ea4e3164a/lifecycle).

**New features**

- This release adds new features that adds support for Kotlin coroutines for Lifecycle and LiveData. Detailed documentation on them can be found [here](https://developer.android.com/topic/libraries/architecture/coroutines).

## ViewModel-SavedState Version 1.0.0

### Version 1.0.0

January 22, 2020

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0` is released. [Version 1.0.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/149aa50d7509b6df4e5b1d1c1430468b816cf9a0..fee1737a1d380aa1435ae5fca6336ee350bad4e0/lifecycle/lifecycle-viewmodel-savedstate).

**Important features in 1.0.0**

- New **SavedStateHandle** class was added. It enables your `ViewModel` classes to access and to contribute to the saved state. This object can be received in constructor of `ViewModel` class and factories provided by default by Fragments and AppCompatActivity will inject `SavedStateHandle` automatically.
- **AbstractSavedStateViewModelFactory** was added. It allows you to create custom factories for your `ViewModel` and provide them access to `SavedStateHandle`.

### ViewModel-Savedstate Version 1.0.0-rc03

December 4, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-rc03` is released. [Version 1.0.0-rc03 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/45b11795d6737dd540ccedaec026dc34397f1ba6..149aa50d7509b6df4e5b1d1c1430468b816cf9a0/lifecycle/lifecycle-viewmodel-savedstate).

**Dependency changes**

- Lifecycle ViewModel SavedState now depends on Lifecycle `2.2.0-rc03`.

### Viewmodel-Savedstate Version 1.0.0-rc02

November 7, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/c378b9a2eae63d2701c82b0144af36e33d15c26a..45b11795d6737dd540ccedaec026dc34397f1ba6/lifecycle/lifecycle-viewmodel-savedstate).

**Dependency changes**

- Now depends on lifecycle `2.2.0-rc02`.

### ViewModel-SavedState Version 1.0.0-rc01

October 23, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-rc01` is released with no changes from `1.0.0-beta01`. [Version 1.0.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/f14ad350142290622d1645e1d0e280cbe8ca4c2f..c378b9a2eae63d2701c82b0144af36e33d15c26a/lifecycle/lifecycle-viewmodel-savedstate).

### ViewModel-Savedstate Version 1.0.0-beta01

October 9, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/391dc4bc729d2973a6e6e57916d3008c58026e56..f14ad350142290622d1645e1d0e280cbe8ca4c2f/lifecycle/lifecycle-viewmodel-savedstate).

**Bug fixes**

- Fixed an issue where accessing a SavedState ViewModel for the first time in `Activity.onActivityResult()` would result in an `IllegalStateException`. ([b/139093676](https://issuetracker.google.com/issues/139093676))
- Fixed an `IllegalStateException` when using `AbstractSavedStateViewModelFactory`. ([b/141225984](https://issuetracker.google.com/issues/141225984))

### ViewModel-SavedState Version 1.0.0-alpha05

September 18, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/44b591fe64e859b4b4e34b2590a5257c255c638c..391dc4bc729d2973a6e6e57916d3008c58026e56/lifecycle/lifecycle-viewmodel-savedstate).

**API changes**

- `SavedStateViewModelFactory` no longer extends `AbstractSavedStateViewModelFactory` and `SavedStateHandle` is created only for ViewModels that requested have it ([aosp/1113593](https://android-review.googlesource.com/1113593))

### ViewModel-SavedState Version 1.0.0-alpha03

August 7, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-alpha03` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/2e1f4a8ef6eb4252735ed377398bc56f310406c0..23fecdb1097a69a528ab6109f661b4e46123aecc/lifecycle/lifecycle-viewmodel-savedstate).

**Breaking Changes**

- `lifecycle-viewmodel-savedstate` no longer depends on `fragment` and the related `SavedStateViewModelFactory(Fragment)` and `SavedStateViewModelFactory(FragmentActivity)` constructors have been removed. Instead, `SavedStateViewModelFactory` is now the default factory for [Activity `1.1.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/activity#1.1.0-alpha02), [Fragment `1.2.0-alpha02`](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0-alpha02), and [Navigation `2.2.0-alpha01`](https://developer.android.com/jetpack/androidx/releases/navigation#2.2.0-alpha01). ([b/135716331](https://issuetracker.google.com/issues/135716331))

### ViewModel-SavedState Version 1.0.0-alpha02

July 2, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/eced0496fd103512ad396c143917ceafa4d34591..2e1f4a8ef6eb4252735ed377398bc56f310406c0/lifecycle/viewmodel-savedstate).

**New features**

- Added `SavedStateHandle.getLiveData()` overload which accepts a default value.

**API Changes**

- `SavedStateVMFactory` is renamed to `SavedStateViewModelFactory`.
- `AbstractSavedStateVMFactory` is renamed to `AbstractSavedStateViewModelFactory`.

### ViewModel-Savedstate Version 1.0.0-alpha01

March 13, 2019

`androidx.lifecycle:lifecycle-viewmodel-savedstate:1.0.0-alpha01` is released. The full commit log for this initial release can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/eced0496fd103512ad396c143917ceafa4d34591/lifecycle/viewmodel-savedstate).

**New features**

- Now `ViewModels` can contribute to savedstate. To do that you use newly introduced viewmodel's factory `SavedStateVMFactory` and your ViewModel should have a constructor that receives `SavedStateHandle`object as a parameter.

## Version 2.1.0

**Important changes since 2.0.0**

- Added `LifecycleEventObserver` for the cases when a stream of lifecycle events is needed. It is a public API instead of a hidden `GenericLifecycleObserver` class.
- Added ktx extensions for `LiveData.observe` methods and `Transformations.*` methods.
- Added `Transformations.distinctUntilChanged`, which creates a new LiveData object that does not emit a value until the source `LiveData` value has been changed.
- Added coroutine support in ViewModels by adding the extension property `ViewModel.viewModelScope`.

### Version 2.1.0

September 5, 2019

`androidx.lifecycle:lifecycle-*:2.1.0` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7265375be17be52ccd946a32866dab91dd56e434..d4a070778a79bcc80e9cfd8b53140ff81a525983/lifecycle).

### Version 2.1.0-rc01

July 2, 2019

`androidx.lifecycle:*:2.1.0-rc01` is released with no changes from `androidx.lifecycle:*:2.1.0-beta01`. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/be101c5ab63016840c743ab315e9a77ea4e3164a..7265375be17be52ccd946a32866dab91dd56e434/lifecycle).

### Version 2.1.0-beta01

May 7, 2019

`androidx.lifecycle:*:2.1.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/7e9a5afb451c3bff1c20e2ce0121c3677810cd5b..be101c5ab63016840c743ab315e9a77ea4e3164a/lifecycle).

**New features**

- Lifecycles are graduated to beta: api introduced in previous alphas such as `liveData` extension functions for transformations and observations, `ViewModel` initialisation with property delegation and others are stabilised and not going to change.

### Version 2.1.0-alpha04

April 3, 2019

`androidx.lifecycle:*:2.1.0-alpha04` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/69fcbbce9f910d6cb9b2693dacd7c40040ffa495..7e9a5afb451c3bff1c20e2ce0121c3677810cd5b/lifecycle).

> [!NOTE]
> **Note:** lifecycle-viewmodel-ktx is incompatible with Activity 1.0.0-alpha01 through 1.0.0-alpha05 and Fragment 1.1.0-alpha01 through 1.1.0-alpha05. Please upgrade to Activity 1.0.0-alpha06 and Fragment 1.1.0-alpha06, respectively.

**API changes**

- Breaking change: the underlying API behind `by viewModels()` and `by activityViewModels()` has been changed to support a `ViewModelStore` directly, rather than only a `ViewModelStoreOwner`. ([aosp/932932](https://android-review.googlesource.com/932932/))

### Version 2.1.0-alpha03

March 13, 2019

`androidx.lifecycle:*:2.1.0-alpha03` is released. The full list of commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/6d57eb14bdfbd1cb71db0f3c8ca1883df6ece85d..69fcbbce9f910d6cb9b2693dacd7c40040ffa495/lifecycle).

**API changes**

- `ViewModelProvider.KeyedFactory` was removed. Second interface in addition to `ViewModelProvider.Factory` didn't compose well with new features as property delegation in Kotlin `by viewmodels {}`. ([aosp/914133](https://android-review.googlesource.com/c/platform/frameworks/support/+/914133))

### Version 2.1.0-alpha02

January 30, 2019

`androidx.lifecycle 2.1.0-alpha02` is released.

**API changes**

- `LifecycleRegistry` now contains a `setCurrentState()` method that replaces the now deprecated `setState()` method. ([aosp/880715](https://android-review.googlesource.com/880715))

**Bug fixes**

- Fixed an issue where mock `ViewModel` instances would crash when the containing `ViewModelStore` was cleared. [b/122273087](https://issuetracker.google.com/122273087)

### Version 2.1.0-alpha01

December 17, 2018

`androidx.lifecycle 2.1.0-alpha01` is released.

**New features**

- Added `LifecycleEventObserver` for the cases when a stream of lifecycle events is needed. It is a public api instead of a hidden `GenericLifecycleObserver` class.
- Added ktx extensions for `LiveData.observe` methods and `Transformations.*` methods.
- Method `Transformations.distinctUntilChanged` was added. It creates a new `LiveData` object that does not emit a value until the source LiveData value has been changed.
- Coroutine support in ViewModels: extension property `ViewModel.viewModelScope` was added.
- Added `ViewModelProvider.KeyedFactory`, a factory for ViewModels that receives `key` and `Class` in `create` method.

## Version 2.0.0

### Version 2.0.0

September 21, 2018

Lifecycle `2.0.0` is released with one bugfix from `2.0.0-rc01` in ViewModel.

**Bug Fixes**

- Fixed a ViewModel proguard rule that incorrectly removed constructors [b/112230489](https://issuetracker.google.com/112230489)

### Version 2.0.0-beta01

July 2, 2018

**Bug Fixes**

- Fixed LifecycleObserver proguard rule to keep only implementations, not subinterfaces [b/71389427](https://issuetracker.google.com/issues/71389427)
- Fixed ViewModel proguard rules to allow obfuscation and shrinking

## Pre-AndroidX Versions

For the pre-AndroidX versions of Lifecycle that follow, include these dependencies:

    dependencies {
        def lifecycle_version = "1.1.1"

        // ViewModel and LiveData
        implementation "android.arch.lifecycle:extensions:$lifecycle_version"
        // alternatively - just ViewModel
        implementation "android.arch.lifecycle:viewmodel:$lifecycle_version" // For Kotlin use viewmodel-ktx
        // alternatively - just LiveData
        implementation "android.arch.lifecycle:livedata:$lifecycle_version"
        // alternatively - Lifecycles only (no ViewModel or LiveData).
        //     Support library depends on this lightweight import
        implementation "android.arch.lifecycle:runtime:$lifecycle_version"

        annotationProcessor "android.arch.lifecycle:compiler:$lifecycle_version" // For Kotlin use kapt instead of annotationProcessor
        // alternately - if using Java8, use the following instead of compiler
        implementation "android.arch.lifecycle:common-java8:$lifecycle_version"

        // optional - ReactiveStreams support for LiveData
        implementation "android.arch.lifecycle:reactivestreams:$lifecycle_version"

        // optional - Test helpers for LiveData
        testImplementation "android.arch.core:core-testing:$lifecycle_version"
    }

### Version 1.1.1

March 21, 2018

Only one small change: `android.arch.core.util.Function` is moved from `arch:runtime` to `arch:common`. This allows it to be used without the runtime dependency, e.g. in `paging:common` below.

`lifecycle:common` is a dependency of `lifecycle:runtime`, so this change doesn't affect `lifecycle:runtime` directly, only modules that depend directly on `lifecycle:common`, as Paging does.

### Version 1.1.0

January 22, 2018

**Packaging Changes**

New, much smaller dependencies are now available:

- `android.arch.lifecycle:livedata:1.1.0`
- `android.arch.lifecycle:viewmodel:1.1.0`

> [!NOTE]
> **Note:** Lifecycle Extensions `1.0.0` (`android.arch.lifecycle:extensions:1.0.0`) is **not** compatible with `livedata:1.1.0` or `viewmodel:1.1.0`. Please update to `extensions:1.1.0`, which includes a transitive dependency on `livedata:1.1.0` and `viewmodel 1.1.0`.

> [!NOTE]
> **Note:** `android.arch.lifecycle:reactivestreams:1.1.0` now only depends on `android.arch.lifecycle:livedata:1.1.0`, not all of `android.arch.lifecycle:extensions:1.1.0`.

**API Changes**

- The deprecated `LifecycleActivity` and `LifecycleFragment` have now been **removed** - please use `FragmentActivity`, `AppCompatActivity` or support `Fragment`.
- `@NonNull` annotations have been added to `ViewModelProviders` and `ViewModelStores`
- `ViewModelProviders` constructor has been deprecated - please use its static methods directly
- `ViewModelProviders.DefaultFactory` has been deprecated - please use `ViewModelProvider.AndroidViewModelFactory`
- The static `ViewModelProvider.AndroidViewModelFactory.getInstance(Application)` method has been added to retrieve a static `Factory` suitable for creating `ViewModel` and `AndroidViewModel` instances.