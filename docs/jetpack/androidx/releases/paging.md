---
title: https://developer.android.com/jetpack/androidx/releases/paging
url: https://developer.android.com/jetpack/androidx/releases/paging
source: md.txt
---

# Paging

[User Guide](https://developer.android.com/topic/libraries/architecture/paging/v3-overview) [Code Sample](https://github.com/android/architecture-components-samples) [Codelab](https://codelabs.developers.google.com/codelabs/android-paging) API Reference  
[androidx.paging](https://developer.android.com/reference/kotlin/androidx/paging/package-summary)  
The Paging Library makes it easier for you to load data gradually and gracefully within your app's [RecyclerView](https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView).


This table lists all the artifacts in the `androidx.paging` group.

| Artifact | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| paging-\* | [3.4.1](https://developer.android.com/jetpack/androidx/releases/paging#3.4.1) | - | - | - |
| paging-compose | [3.4.1](https://developer.android.com/jetpack/androidx/releases/paging#3.4.1) | - | - | - |

This library was last updated on: February 11, 2026

## Declaring dependencies

To add a dependency on Paging, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
  def paging_version = "3.4.1"

  implementation "androidx.paging:paging-runtime:$paging_version"

  // alternatively - without Android dependencies for tests
  testImplementation "androidx.paging:paging-common:$paging_version"

  // optional - RxJava2 support
  implementation "androidx.paging:paging-rxjava2:$paging_version"

  // optional - RxJava3 support
  implementation "androidx.paging:paging-rxjava3:$paging_version"

  // optional - Guava ListenableFuture support
  implementation "androidx.paging:paging-guava:$paging_version"

  // optional - Jetpack Compose integration
  implementation "androidx.paging:paging-compose:3.4.1"
}
```

### Kotlin

```kotlin
dependencies {
  val paging_version = "3.4.1"

  implementation("androidx.paging:paging-runtime:$paging_version")

  // alternatively - without Android dependencies for tests
  testImplementation("androidx.paging:paging-common:$paging_version")

  // optional - RxJava2 support
  implementation("androidx.paging:paging-rxjava2:$paging_version")

  // optional - RxJava3 support
  implementation("androidx.paging:paging-rxjava3:$paging_version")

  // optional - Guava ListenableFuture support
  implementation("androidx.paging:paging-guava:$paging_version")

  // optional - Jetpack Compose integration
  implementation("androidx.paging:paging-compose:3.4.1")
}
```

For information on using Kotlin extensions, see
[ktx documentation](https://developer.android.com/kotlin/ktx).

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:413106+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=413106&template=1096385)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 3.4

### Version 3.4.1

February 11, 2026

`androidx.paging:paging-*:3.4.1` is released. Version 3.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9bfc2c700440f809fc6b8a9565788c078861187..302478513a01447578462b168226f9de5a26ed10/paging).

**Dependency Update**

- Updated paging-guava's guava dependency from version 31.1 to 32.0.1.

### Version 3.4.0

January 28, 2026

`androidx.paging:paging-*:3.4.0` is released. Version 3.4.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1e6b87e344c28f71f464996b0d753a971aa1b83d..f9bfc2c700440f809fc6b8a9565788c078861187/paging).

**Important changes since 3.3.0:**

- Added more KMP targets to `paging-common`, `paging-testing`, and `paging-compose`. In total they all now support JVM(Android and Desktop), Native (Linux, iOS, watchOS, tvOS, macOS, MinGW), and Web (JavaScript, WasmJS)
- `paging-common`, `paging-testing`, and `paging-compose` has removed support for `macosX64`, `iosX64`, `watchosX64`, and `tvosX64` to align with Jetbrains deprecation of the macosX64 targets.
- Added a new `PagingState` API `closestItemAroundPosition` to retrieve the loaded item that is closest to the target position and matches the input predicate. This can be used to generate item-based refresh keys where the ideal anchorable item is around but not at the exact target position.

### Version 3.4.0-rc01

January 14, 2026

`androidx.paging:paging-*:3.4.0-rc01` is released. Version 3.4.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6796a2af8e90dcd826dae7bd8ab99abe5d95bdda..dc94774a192f9929fafe7305d8d54043526a3448/paging).

**New Features**

- Removed support for the following KMP platforms: `macosX64`, `iosX64`, `watchosX64`, and `tvosX64` to align with [Jetbrains deprecation of the macosX64 targets](https://youtrack.jetbrains.com/issue/KT-78660/meta-Deprecation-of-the-macosX64-target). ([7cb9a4](https://android.googlesource.com/platform/frameworks/support/+/7cb9a4cc835cbdd98b53c1bb7bc3e0f59c6510fd))

### Version 3.4.0-beta01

December 17, 2025

`androidx.paging:paging-*:3.4.0-beta01` is released. Version 3.4.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/68ced4a5279f8eedb21eeb26aeb4cd8fda9dfc55..6796a2af8e90dcd826dae7bd8ab99abe5d95bdda/paging).

**Bug Fixes**

- Fix race between `RecyclerView` and `Refresh` loads leading to `IndexOutOfBoundsException` in `RecyclerView`. Interrupted UI updates due to continuous `Refresh` loads can cause Paging state to desync with `RecyclerView`. This is fixed by resetting Paging to its pre-Refresh state if a Refresh is interrupted (i.e. by a consecutive `Refresh` load). ([I771b0](https://android-review.googlesource.com/#/q/I771b04c781c0f8eae79d0cacf60075add91bafee), [b/409809768](https://issuetracker.google.com/issues/409809768))

### Version 3.4.0-alpha04

September 10, 2025

`androidx.paging:paging-*:3.4.0-alpha04` is released. Version 3.4.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f3f47822df75f2b8849c22ee13319bad7100dd38..68ced4a5279f8eedb21eeb26aeb4cd8fda9dfc55/paging).

**API Changes**

- Added a new `PagingState` API `closestItemAroundPosition` to retrieve the loaded item that is closest to the target position and matches the input predicate. This can be used to generate item-based refresh keys where the ideal anchorable item is around but not at the exact target position. ([I96e5c](https://android-review.googlesource.com/#/q/I96e5cca751dd68de37df5e34b156c4e30201fade), [b/440187139](https://issuetracker.google.com/issues/440187139))

### Version 3.4.0-alpha03

August 27, 2025

`androidx.paging:paging-*:3.4.0-alpha03` is released. Version 3.4.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e208566d25cf8b92cb64dd9364a539da8c64694f..f3f47822df75f2b8849c22ee13319bad7100dd38/paging).

**New Features**

- Paging-common has added desktop as a new Kotlin Multiplatform (KMP) target. In total it now supports JVM(Android and Desktop), Native (Linux, iOS, watchOS, tvOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([Id2483](https://android-review.googlesource.com/#/q/Id2483e340b3b9b6f9ddf756a25b5937ab9c884ec), [b/436884811](https://issuetracker.google.com/issues/436884811))
- Paging-testing has added new Kotlin Multiplatform (KMP) targets. In total it now supports JVM(Android and Desktop), Native (Linux, iOS, watchOS, tvOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([I0c543](https://android-review.googlesource.com/#/q/I0c5431115157a42c01384602e37bfb0d1f024bdb), [b/435014650](https://issuetracker.google.com/issues/435014650))
- Paging-compose has added new Kotlin Multiplatform (KMP) targets. In total it now supports JVM(Android and Desktop), Native (Linux, iOS, watchOS, tvOS, macOS, MinGW), and Web (JavaScript, WasmJS). ([I70d44](https://android-review.googlesource.com/#/q/I70d4488c41da8ccb799858a2530577214d433cd2), [b/436884801](https://issuetracker.google.com/issues/436884801))

**API Changes**

- Moving the default minSdk from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 3.4.0-alpha02

July 30, 2025

`androidx.paging:paging-*:3.4.0-alpha02` is released. Version 3.4.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1b437892629a2cdedb46d9b7232575987b2cc6b5..e208566d25cf8b92cb64dd9364a539da8c64694f/paging).

**API Changes**

- `PagingData.from` now allows setting `placeholdersBefore` and `placeholdersAfter`. Note that scrolling through these placeholders does not trigger loads. ([I06983](https://android-review.googlesource.com/#/q/I06983dd6293efe458d75ef3c469df07396b1fd75))

### Version 3.4.0-alpha01

July 2, 2025

`androidx.paging:paging-*:3.4.0-alpha01` is released. Version 3.4.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1e6b87e344c28f71f464996b0d753a971aa1b83d..1b437892629a2cdedb46d9b7232575987b2cc6b5/paging).

**New Features**

- Paging has added the following KMP targets: watchos, tvos, mingwX64, watchosDeviceArm64, and linuxArm64. ([I237dd](https://android-review.googlesource.com/#/q/I237dd5f9468c75193d460cc8c6c16083c215963e), [Ia62b3](https://android-review.googlesource.com/#/q/Ia62b3464382a7b4a7751a054d711d1be823431ff), [b/368046982](https://issuetracker.google.com/issues/368046982), [Icf15d](https://android-review.googlesource.com/#/q/Icf15d056ce2380ca3c733fb1a93fd502f60b40e4), [b/364652024](https://issuetracker.google.com/issues/364652024), [I139d3](https://android-review.googlesource.com/#/q/I139d36226a3d06d9768bd63302de98b576a12a48), [b/338268719](https://issuetracker.google.com/issues/338268719))

**Bug Fixes**

- Android unit tests pulling in Paging 3.3 or later will no longer throw from `PagingLogger` ([Ia9400](https://android-review.googlesource.com/#/q/Ia9400db995e7f0357cae2647cbd2cef9cf6c3398), [b/331684448](https://issuetracker.google.com/issues/331684448))
- Fixed bug where `RecyclerView` throws `IndexOutOfBoundsException` when user scrolls while updating `RecyclerView` ([Id1f16](https://android-review.googlesource.com/#/q/Id1f16a1e2cc0286458659d0bf63cf59ab3399b93), [b/381024738](https://issuetracker.google.com/issues/381024738))
- Fixed bug where paging was unable to trigger more loads when refreshing while scrolling. ([I60ca5](https://android-review.googlesource.com/#/q/I60ca5c23e01c2ff28d120d10ae9b28eda57fac50), [b/352586078](https://issuetracker.google.com/issues/352586078))
- Fixed crash when scrolling while refreshing Paging items. ([I8c65a](https://android-review.googlesource.com/#/q/I8c65ac87639c0d501ccab1fd44fd3adbc9147a31), [b/347649763](https://issuetracker.google.com/issues/347649763))

## Version 3.3

### Version 3.3.6

February 12, 2025

`androidx.paging:paging-*:3.3.6` is released. Version 3.3.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/37e8321e41e98a0c2588dd346983c0638530bfc5..5675330a0b06fca9d23a5367e27f307ad64c95c4/paging).

**Bug Fixes**

- Refresh and retry signals sent during an initial Refresh will now be stored and automatically re-sent once the Paging presenter is ready.

**External Contribution**

- Thank you [Eva](https://github.com/evant) for submitting the bug fix ([#754](https://github.com/androidx/androidx/pull/754))

### Version 3.3.5

December 11, 2024

`androidx.paging:paging-*:3.3.5` is released. Version 3.3.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ecec376274f1b9abeee169b3ae4f8bb8ad7baf31..da656da1096bccb30c4a2292a9375c175a9b0bdc/paging).

**Bug Fixes**

- Fixed bug where `RecyclerView` throws `IndexOutOfBoundsException` when user scrolls while updating `RecyclerView`. ([Id1f16](https://android-review.googlesource.com/#/q/Id1f16a1e2cc0286458659d0bf63cf59ab3399b93), [b/381024738](https://issuetracker.google.com/issues/381024738))

### Version 3.3.4

November 13, 2024

`androidx.paging:paging-*:3.3.4` is released. Version 3.3.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c46a8d0eefa9cf9c4b07e28ebd88a0d737a0508..ecec376274f1b9abeee169b3ae4f8bb8ad7baf31/paging).

**Bug Fixes**

- Android unit tests pulling in Paging 3.3 or later will no longer throw an error such as `Method isLoggable in android.util.Log not mocked`. ([Ia9400](https://android-review.googlesource.com/#/q/Ia9400db995e7f0357cae2647cbd2cef9cf6c3398), [b/331684448](https://issuetracker.google.com/issues/331684448))

### Version 3.3.2

August 7, 2024

`androidx.paging:paging-*:3.3.2` is released. Version 3.3.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/358f66daa422fdd114efe0c11683c70b47ba1051..1c46a8d0eefa9cf9c4b07e28ebd88a0d737a0508/paging).

**New Features**

- `paging-common` and `paging-testing` has added new Kotlin-Multiplatform targets: `watchos`, `tvos`, and `linuxArm64` ([90c9768](https://android.googlesource.com/platform/frameworks/support/+/90c97683b9811e57c63ddb93d87b6fa21f02bcde)), ([53e0eca](https://android.googlesource.com/platform/frameworks/support/+/53e0eca80fb98486e38db466d6cb2449c7cecd1f))

### Version 3.3.1

July 24, 2024

`androidx.paging:paging-*:3.3.1` is released. Version 3.3.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/656d55d844d23f2561b23f4970d65e4b7f63debc..358f66daa422fdd114efe0c11683c70b47ba1051/paging).

**Bug Fixes**

- Fixed an issue where `AsyncPagingDataDiffer` or APIs built on top of it like the `PagingDataAdapter` used with `RecyclerView` would be unable to trigger more loads when the backing data source refreshed while scrolling. ([I60ca5](https://android-review.googlesource.com/#/q/I60ca5c23e01c2ff28d120d10ae9b28eda57fac50), [b/352586078](https://issuetracker.google.com/issues/352586078))
- Fixed a crash that occurs when items are removed from the backing data source while scrolling a `RecyclerView` using a `PagingDataAdapter` or `AsyncPagingDataDiffer`. ([I8c65a](https://android-review.googlesource.com/#/q/I8c65ac87639c0d501ccab1fd44fd3adbc9147a31), [b/347649763](https://issuetracker.google.com/issues/347649763))

### Version 3.3.0

May 14, 2024

`androidx.paging:paging-*:3.3.0` is released. Version 3.3.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c6ffa207f646ff44d4ca47694e4ef62043d2fdd3..656d55d844d23f2561b23f4970d65e4b7f63debc/paging).

**Important changes since 3.2.0**

- `PagingDataPresenter` is now a public class. Multiplatform presenters can now be built on top of `PagingDataPresenter` rather than requiring internal Paging APIs or `paging-runtime`'s `AsyncPagingDataDiffer`.
- Added new `LoadStates` and `CombinedLoadStates` helper methods in `hasError` and `isIdle` to check if `LoadStates` is in Error or `NotLoading` state, respectively. Also added a new `awaitNotLoading()` Kotlin extension method on `Flow<CombinedLoadStates>` that waits until a load has settled into either `NotLoading` or Error state.
- `PagingData.empty()` now dispatches `NotLoading` states by default unless custom `LoadStates` are passed to its constructor. This departs from existing behavior where it doesn't dispatch `LoadStates` when submitted to a `PagingDataAdapter` or it dispatches Loading states when collected as `LazyPagingItems`. When collected as `LazyPagingItems`, it will now also display an empty list immediately upon initial composition.

**Kotlin Multiplatform Compatibility**

Paging now ships artifacts compatible with Kotlin Multiplatform, thanks in large part to upstreamed work from CashApp's [multiplatform-paging](https://github.com/cashapp/multiplatform-paging) project.

- `paging-common` has moved all Paging 3 APIs to `common` and is now compatible with jvm and iOS in addition to Android.
- `paging-testing` has moved its code to `common` and is now compatible with jvm and iOS in addition to Android.
- `paging-compose` has moved its code to `common` and ships an Android artifact, matching the multiplatform support of `androidx.compose`.
- `paging-runtime`, `paging-guava`, `paging-rxjava2`, and `paging-rxjava3` will remain Android only.

### Version 3.3.0-rc01

May 1, 2024

`androidx.paging:paging-*:3.3.0-rc01` is released with no changes in Paging 3.3.0-beta01. Version 3.3.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/02b55f664eba38e42e362e1af3913be1df552d55..c6ffa207f646ff44d4ca47694e4ef62043d2fdd3/paging).

### Version 3.3.0-beta01

April 3, 2024

`androidx.paging:paging-*:3.3.0-beta01` is released with no notable changes. Version 3.3.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8fbefdc70ea49fce9c8f8cfcf80e1fa2122a7ee4..02b55f664eba38e42e362e1af3913be1df552d55/paging).

### Version 3.3.0-alpha05

March 20, 2024

`androidx.paging:paging-*:3.3.0-alpha05` is released. Version 3.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..8fbefdc70ea49fce9c8f8cfcf80e1fa2122a7ee4/paging).

**API Changes**

- Paging now uses the AndroidX Annotation `@MainThread` annotation for common code. ([I78f0d](https://android-review.googlesource.com/#/q/I78f0d3cf36e3a3a9088e0698c351289cf2dbc1bf), [b/327682438](https://issuetracker.google.com/327682438))

### Version 3.3.0-alpha04

March 6, 2024

`androidx.paging:paging-*:3.3.0-alpha04` is released. Version 3.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ca2a8cf8da3a3502fccc593974f8085653e38261..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/paging).

**Bug Fixes**

- Fixed minor documentation errors related to the addition of Kotlin multiplatform compatibility. ([aosp/2950785](https://android-review.googlesource.com/c/platform/frameworks/support/+/2950785))

### Version 3.3.0-alpha03

February 7, 2024

`androidx.paging:paging-*:3.3.0-alpha03` is released. [Version 3.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fcfb71eda8bee777689ca7b4124283b37e287a..ca2a8cf8da3a3502fccc593974f8085653e38261/paging)

**New Features**

- `PagingDataPresenter` is now a public class. Multiplatform presenters can now be built on top of `PagingDataPresenter` rather than requiring internal Paging APIs or `paging-runtime`'s `AsyncPagingDataDiffer`. ([Id1f74](https://android-review.googlesource.com/#/q/Id1f748af435e6f5d733bc731ef7e8cd12455845a), [b/315214786](https://issuetracker.google.com/issues/315214786))
- Added new `LoadStates` and `CombinedLoadStates` helper methods to check if `LoadStates` is in Error or `NotLoading` state. Also added a new API that awaits on a `LoadStateFlow` until a load has settled into either `NotLoading` or Error state. ([Id6c67](https://android-review.googlesource.com/#/q/Id6c67a6ba3805130d1a08840bad38e179604f786))

**Behavior change**

- `PagingData.empty()` now dispatches `NotLoading` states by default unless custom `LoadStates` are passed to its constructor. This departs from existing behavior where it doesn't dispatch `LoadStates` when submitted to a `PagingDataAdapter` or it dispatches Loading states when collected as `LazyPagingItems`. When collected as `LazyPagingItems`, it will now also display an empty list immediately upon initial composition. ([I4d11d](https://android-review.googlesource.com/#/q/I4d11df131d81fb0234e096581b74440a4b076a76), [b/301833847](https://issuetracker.google.com/issues/301833847))

### Version 3.3.0-alpha02

September 20, 2023

`androidx.paging:paging-*:3.3.0-alpha02` is released. [Version 3.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aca6f23c6857800cf245fbe5b19a94dca0e71c18/paging)

**Kotlin Multiplatform Compatibility**

Paging now ships artifacts compatible with Kotlin Multiplatform, thanks in large part to upstreamed work from CashApp's [multiplatform-paging](https://github.com/cashapp/multiplatform-paging) project. This will allow us to avoid divergence between two repositories and keep them compatible.

- `paging-common` has moved all Paging 3 APIs to `common` and is now compatible with jvm and iOS in addition to Android.
- `paging-testing` has moved its code to `common` and is now compatible with jvm and iOS in addition to Android.
- `paging-compose` has moved its code to `common` and ships an Android artifact, matching the multiplatform support of `androidx.compose`.
- `paging-runtime`, `paging-guava`, `paging-rxjava2`, and `paging-rxjava3` will remain Android only.

**API Changes**

- The public Logger interface that was meant only for internal usage has been deprecated ([I16e95](https://android-review.googlesource.com/#/q/I16e9505d60bbe864528e0be2266668c6140bcc24), [b/288623117](https://issuetracker.google.com/issues/288623117))

**External Contribution**

- Thanks [veyndan](https://github.com/veyndan) from Cash App for helping move Paging to Kotlin Multiplatform ([#560](https://github.com/androidx/androidx/pull/560), [#561](https://github.com/androidx/androidx/pull/561), [#562](https://github.com/androidx/androidx/pull/562), [#573](https://github.com/androidx/androidx/pull/573), [#576](https://github.com/androidx/androidx/pull/576), [#577](https://github.com/androidx/androidx/pull/577), [#578](https://github.com/androidx/androidx/pull/578), [#579](https://github.com/androidx/androidx/pull/579), [#580](https://github.com/androidx/androidx/pull/580), [#581](https://github.com/androidx/androidx/pull/581), [#583](https://github.com/androidx/androidx/pull/583), [#584](https://github.com/androidx/androidx/pull/584), [#586](https://github.com/androidx/androidx/pull/586), [#609](https://github.com/androidx/androidx/pull/609))

### Version 3.3.0-alpha01

September 20, 2023

- This is the first multiplatform release of androidx.paging libraries. This version only has `*-jvm`, and `*-android` artifacts. For macOS, iOS, and linux variants, use `3.3.0-alpha02`.

## Version 3.2

### Version 3.2.1

September 6, 2023

`androidx.paging:paging-*:3.2.1` is released. [Version 3.2.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22c1844d8a4508469b860b1415c1aea9aa46eb78..ebd21c8f3259d88fac4fd6d9769f23a8dc179ab1/paging)

**Bug Fixes**

- Fixed an issue where the `asSnapshot()` API of the Paging Testing artifact would hang when passed a Flow built using `PagingData.from(List)` since `asSnapshot()` would not have any information on when loading has finished (unlike the `PagingData.from(List, LoadStates)` overload). This workaround only works for completable Flows (e.g., a `flowOf(PagingData.from(...))`). For non-completable Flows (e.g., `MutableStateFlow`, use the `PagingData.from` overload that provides `LoadStates`). ([I502c3](https://android-review.googlesource.com/#/q/I502c3653398feaf1a2dba34072cf89eb58126670))
- Paging Compose now internally uses `AndroidUiDispatcher.Main` to ensure that new data is available in the same frame as loading completes. ([Ia55af](https://android-review.googlesource.com/#/q/Ia55af9ad4aeb366d7a280922563d29424619abf9))

### Version 3.2.0

July 26, 2023

`androidx.paging:paging-*:3.2.0` is released. [Version 3.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c2d5f1bbc58c2910a46d02584ecc6ff02f1cc789..22c1844d8a4508469b860b1415c1aea9aa46eb78/paging)

**Important changes since 3.1.0**

- Paging Compose reached API stability and has been merged back into the rest of Paging where its version now matches all the other Paging artfacts. Changes since 3.1.0 include:
  - Support for previewing a list of fake data by creating a `PagingData.from(fakeData)` and wrapping that `PagingData` in a `MutableStateFlow` (e.g. `MutableStateFlow(PagingData.from(listOf(1, 2, 3)))`). Pass this flow into `@Preview` composables as receiver for `collectAsLazyPagingItems()` to preview.
  - Support for all lazy layouts such as `LazyVerticalGrid` and `HorizontalPager` as well as custom lazy components from Wear and TV libraries. This was achieved through new lower level `LazyPagingItems` extension methods `itemKey` and `itemContentType`, which helps you implement the `key` and `contentType` parameters to the standard `items` APIs that already exist for `LazyColumn`, `LazyVerticalGrid` as well as their equivalents in APIs like `HorizontalPager`.
  - `items(lazyPagingItems)` and `itemsIndexed(lazyPagingItems)` which only supports `LazyListScope` were deprecated.
- New `paging-testing` artifact which provides APIs designed around unit testing each layer of your app and its integration with Paging in isolation. For example, it includes
  - `TestPager` class that allows you to validate the behavior of your own custom `PagingSource` implementation independently from the Pager and real UI.
  - `asPagingSourceFactory` APIs to transform either a `Flow<List<Value>>` or a static `List<Value>` into a `PagingSourceFactory` that can be passed to a Pager in tests
  - `asSnapshot` Kotlin extension on `Flow<PagingData<Value>>`, which translates the `Flow<PagingData<Value>>` into a direct `List<Value>`. The `asSnapshot lambda` allows you to mimic the UI of your app via APIs such as `scrollTo` or `appendScrollWhile` so that you can verify the snapshot of data is correct at any point in your set of paged data.
- Added default logs to expose Paging debugging information in two levels: `VERBOSE` and `DEBUG`. The logs can be enabled via the command `adb shell setprop log.tag.Paging [DEBUG|VERBOSE]`. This applies to both Paging with views or Paging with Compose.
- Added constructors for `PagingDataAdapter` and `AsyncPagingDataDiffer` which accept `CoroutineContext` instead of `CoroutineDispatcher`.
- Added a new `PagingSourceFactory` functional interface that provides a more explicit API surface than the previous () -\> `PagingSource` lambdas. This factory can be used to instantiate a Pager.

### Version 3.2.0-rc01

June 21, 2023

`androidx.paging:paging-*:3.2.0-rc01` is released. [Version 3.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/73f902dee011bfe400d8a0330bfd8d4bb632065f..c2d5f1bbc58c2910a46d02584ecc6ff02f1cc789/paging)

**External Contribution**

- Thanks [Veyndan](https://github.com/veyndan) for contributing to moving Paging away from Android/JVM specifics. ([#553](https://github.com/androidx/androidx/pull/553), [#554](https://github.com/androidx/androidx/pull/554), [#555](https://github.com/androidx/androidx/pull/555), [#559](https://github.com/androidx/androidx/pull/559))

### Version 3.2.0-beta01

June 7, 2023

`androidx.paging:paging-*:3.2.0-beta01` is released. [Version 3.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d..73f902dee011bfe400d8a0330bfd8d4bb632065f/paging)

**Paging Compose**

- Paging Compose has officially reached API stability. As such, the version has been updated from `1.0.0-alpha20` to now match the version of all other Paging artifacts.

**API Changes**

- Removed the deprecated `items(LazyPagingItems)` and `itemsIndexed(LazyPagingItems)` APIs from Paging Compose. See the [Paging Compose `1.0.0-alpha20` release notes](https://developer.android.com/jetpack/androidx/releases/paging#1.0.0-alpha20) for an example of their replacement APIs. ([I9626e](https://android-review.googlesource.com/#/q/I9626e55d070a11902952862c7663721f775503e4))

### Version 3.2.0-alpha06

May 24, 2023

`androidx.paging:paging-*:3.2.0-alpha06` is released. [Version 3.2.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/paging)

**New Features**

- Added a new `PagingSourceFactory` functional interface that provides a more explicit API surface than the existing `() -> PagingSource` lambdas. This factory can be used to instantiate a `Pager`. ([I33165](https://android-review.googlesource.com/#/q/I3316590a0d667566edeb40d4e99e005cd6cee3ac), [b/280655188](https://issuetracker.google.com/issues/280655188))
- Added new `paging-testing` API of `List<Value>.asPagingSourceFactory()` to get a `PagingSourceFactory` that only loads from an immutable list of data. The existing extension on `Flow<List<Value>>` should still be used for testing with multiple generations of static data. ([Id34d1](https://android-review.googlesource.com/#/q/Id34d1361119413d0c19a054a2e23dd26241faa6f), [b/280655188](https://issuetracker.google.com/issues/280655188))

**API Changes**

- All public APIs in paging-testing are now annotated with `@VisibleForTesting` to ensure these APIs are used only in tests. ([I7db6e](https://android-review.googlesource.com/#/q/I7db6e8431cb78604653220c2768339c39db88f54))
- The `asSnapshot` API no longer requires passing in a `CoroutineScope`. It now defaults to using the context inherited from its parent scope. ([Id0a78](https://android-review.googlesource.com/#/q/Id0a78cc5dd633901b39cc608d66d6b7255618549), [b/282240990](https://issuetracker.google.com/issues/282240990))
- Reordered `TestPager` constructor parameters to intuitively match the order of real `Pager` constructor parameters ([I6185a](https://android-review.googlesource.com/#/q/I6185ad09fb5e695c02b50f88022d168405de39f2))
- Migrated paging-testing's use of lambda type `() -> PagingSource<Key, Value>` to type `PagingSourceFactory<Key, Value>`. ([I4a950](https://android-review.googlesource.com/#/q/I4a95067989fabf8258a3392007dbf8abd35d8efa), [b/280655188](https://issuetracker.google.com/issues/280655188))

**Behavior Changes**

- Main dispatcher is no longer required to run `asSnapshot` Paging tests. Setting it no longer makes any changes to the test behavior. ([Ie56ea](https://android-review.googlesource.com/#/q/Ie56ead0c5fcec3ef8dce1c77c150d2f8dd0d7d5e))

### Version 3.2.0-alpha05

May 3, 2023

`androidx.paging:paging-*:3.2.0-alpha05` is released. [Version 3.2.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/paging)

**API Changes**

- The Paging Testing API of `asSnapshot` now defaults its `loadOperations` parameter to an empty lambda. This allows calling `asSnapshot` without passing in any load operations to retrieve the data from the initial refresh load. ([Ied354](https://android-review.googlesource.com/#/q/Ied354f58b94c8303eb9914dc5ca784d1313ddc04), [b/277233770](https://issuetracker.google.com/issues/277233770))

**Documentation Improvements**

- Updated the documentation on `asPagingSourceFactory()` to clarify that it is an extension method on a `Flow` which returns a reusable factory for generating `PagingSource` instances. ([I5ff4f](https://android-review.googlesource.com/#/q/I5ff4f23644c737e86deab84fb9bcce7668239c7f), [I705b5](https://android-review.googlesource.com/q/I705b5ab25c0dee98d90fe8d28248e66d67ebcb40))
- Updated the documentation on the `LoadResult.Page`constructor to clarify the need to override `itemsBefore` and `itemsAfter` to support jumping. ([Ied354](https://android-review.googlesource.com/#/q/I367334e2570bfaba2f43adcdf00543559fa3b37f))

**External Contributions**

- Thanks [Veyndan](https://github.com/veyndan) for contributing to moving Paging away from Android/JVM specifics. ([#525](https://github.com/androidx/androidx/pull/525), [#523](https://github.com/androidx/androidx/pull/523), [#520](https://github.com/androidx/androidx/pull/520), [#519](https://github.com/androidx/androidx/pull/519), [#507](https://github.com/androidx/androidx/pull/507), [#506](https://github.com/androidx/androidx/pull/506), [#505](https://github.com/androidx/androidx/pull/505), [#499](https://github.com/androidx/androidx/pull/499), [#497](https://github.com/androidx/androidx/pull/497), [#496](https://github.com/androidx/androidx/pull/496), [#493](https://github.com/androidx/androidx/pull/493))

### Version 3.2.0-alpha04

February 8, 2023

`androidx.paging:paging-*:3.2.0-alpha04` is released. [Version 3.2.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..7d3ac1ab1206c01fae3ebb500b5b942636070155/paging)

**Paging Testing**

- The `paging-testing` artifact now contains a `asPagingSourceFactory` method to create a `pagingSourceFactory` from a `Flow<List<Value>>` to be supplied to a Pager. Each `List<Value>>` emitted from the Flow represents a generation of Paged data. This facilitates paging tests on, for example, `PagingData` transformations by faking a data source for the Pager to collect from. ([I6f230](https://android-review.googlesource.com/#/q/I6f230da9825c187eb0d8ae6645df7f0a67925574), [b/235528239](https://issuetracker.google.com/issues/235528239))
- The `paging-testing` artifact has been expanded with new APIs suitable for verifying the data contained with a `Flow<PagingData<T>>` is correct. This can be used, for example, to assert the output of a `Flow<PagingData<T>>` from your ViewModel layer.

  This is done via the `asSnapshot` Kotlin extension on `Flow<PagingData<Value>>`, which translates the `Flow<PagingData<Value>>` into a direct `List<Value>`. The `asSnapshot` lambda allows you to mimic the UI of your app via APIs such as `scrollTo` or `appendScrollWhile` in a way that is repeatable and consistent so that you can verify the snapshot of data is correct at any point in your set of paged data.

      // Create your ViewModel instance
      val viewModel = ...
      // Get the Flow of PagingData from the ViewModel
      val data< Flow<PagingData<String>> = viewModel.data
      val snapshot: List<String> = data.asSnapshot {
        // Each operation inside the lambda waits for the data to settle before continuing
        scrollTo(index = 50)

        // While you can't view the items within the asSnapshot call,
        // you can continuously scroll in a direction while some condition is true
        // i.e., in this case until you hit a placeholder item
        appendScrollWhile {  item: String -> item != "Header 1" }
      }
      // With the asSnapshot complete, you can now verify that the snapshot
      // has the expected values

  `asSnapshot` is a `suspend` method that is expected to be run within `runTest`. See [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test) for more information. ([I55fd2](https://android-review.googlesource.com/#/q/I55fd2374b68f8e18a292865a92143f9de50bbad0), [I5bd26](https://android-review.googlesource.com/#/q/I5bd26ec7d66f52696a3d4ea6a610b0ccabd95a84), [I7ce34](https://android-review.googlesource.com/#/q/I7ce345200d07fa1eef9f5d1028fd88caab1477b3), [I51f4d](https://android-review.googlesource.com/#/q/I51f4d2bba2a98a829eeac3ed689ecc0ea0fc7a19), [I2249f](https://android-review.googlesource.com/#/q/I2249f7147213881bdef9acd42287d9fca0dfcc09), [Id6223](https://android-review.googlesource.com/#/q/Id6223b81ebf221456147e41c428a7718e9c494e6), [Ic4bab](https://android-review.googlesource.com/#/q/Ic4babf6783f51dbdab690693e176f65820fa3a38), [Ib29b9](https://android-review.googlesource.com/#/q/Ib29b92793c33a759b52d6b4881d3a3f812b26382), [Ic1238](https://android-review.googlesource.com/#/q/Ic1238184b82106a5ac6ec5f517819a489dd13218), [I96def](https://android-review.googlesource.com/#/q/I96def78b99fcc9ee088a0a912ba69866d8667715), [b/235528239](https://issuetracker.google.com/issues/235528239))

**API Changes**

- UI calls to `getItem` and `peek` in `AsyncPagingDataDiffer` and `PagingDataAdapter` are now correctly marked as only callable on the Main thread. ([I699b6](https://android-review.googlesource.com/#/q/I699b6d8875267b186ead2dc3254099b8c2fdd5e9))
- Removed wildcards from generic types used by `TestPager`, making it easier to consume the results of those methods in code written in the Java programming language. ([I56c42](https://android-review.googlesource.com/#/q/I56c429dcda1a579ea1512d3e9a2b235ba33ad200))

### Version 3.2.0-alpha03

October 24, 2022

`androidx.paging:paging-*:3.2.0-alpha03` is released. [Version 3.2.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..548c8ac2570ae6cf15798fea1380491f7d93796b/paging)

**Paging Testing**

This release contains a new artifact: `paging-testing`. This artifact provides APIs designed around unit testing each layer of your app and its integration with Paging in isolation.

For example, this first release includes a `TestPager` class that allows you to validate the behavior of your own custom `PagingSource` implementation independently from the `Pager` and real UI you would normally need to simulate the end-to-end Paging integration.

`TestPager` should be considered a **fake** - a [test double](https://training/testing/fundamentals/test-doubles) that mirrors the real implementation of `Pager` while providing a simplified API surface for testing a `PagingSource`. These APIs are `suspend` APIs and should be run within `runTest` as outlined in the guide for [Testing Kotlin coroutines on Android](https://developer.android.com/kotlin/coroutines/test).

An example of these APIs in use can be found in the [`room-paging` tests](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:room/room-paging/src/androidTest/kotlin/androidx/room/paging/LimitOffsetPagingSourceTest.kt), which were refactored to use `TestPager`.

**API Changes**

- Enables convenient iteration over `LoadResult.Page.data` through `LoadResult.Page.iterator()`. This indirectly allows the usage of the [Kotlin standard library `flatten` method](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/flatten.html) when given a `List<LoadResult.Page>` such as with the `pages` property of `PagingState` that is passed to the `PagingSource.getRefreshKey` method. ([Ie0718](https://android-review.googlesource.com/#/q/Ie0718ec7179434d2ec2466374cb33cf1c4aec92f))

### Version 3.2.0-alpha02

August 10, 2022

`androidx.paging:paging-*:3.2.0-alpha02` is released. [Version 3.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..bea814b246f89ff7244e3c6b0648f0b57e47897c/paging)

**New Features**

- Paging now provides logs via the `AsyncPagingDataDiffer`or `PagingDataAdapter` classes to expose debugging information collected from `PagingData`.
- The logs can be enabled via the `adb shell` command `adb shell setprop log.tag.Paging [DEBUG|VERBOSE].`([b/235527159](https://issuetracker.google.com/issues/235527159))

**Bug Fixes**

- Fixed the missing `PagingDataDiffer` constructor error when using `paging-common:3.2.0-alpha01` with runtime `paging-runtime:3.1.1` or older.([b/235256201](https://issuetracker.google.com/issues/235256201))

### Version 3.2.0-alpha01

June 1, 2022

`androidx.paging:paging-*:3.2.0-alpha01` is released. [Version 3.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/65c8f2c53158200a61e0e1cc012cdbbadaee60ab..7cbb37cc779160b89644d03e042c129d0ce025d2/paging)

**API Changes**

- Added constructors for `PagingDataAdapter` and `AsyncPagingDataDiffer` which accept `CoroutineContext` instead of `CoroutineDispatcher`. ([Idc878](https://android-review.googlesource.com/#/q/Idc8784ff12a2d6e4a617bae51c7053582c5f1986))
- By default, `PagingData.from()` and `PagingData.empty()` will no longer affect `CombinedLoadStates` on the presenter side. A new overload that allows passing `sourceLoadStates` and `remoteLoadStates` in to these constructors has been added to maintain the existing behavior of setting `LoadStates` to be fully terminal (i.e., `NotLoading(endOfPaginationReached = false)`), with the option to include remote states as well if needed. If `LoadStates` are not passed, then the previous `CombinedLoadStates` will be maintained on the presenter side when it receives the static `PagingData`. ([Ic3ce5](https://android-review.googlesource.com/#/q/Ic3ce54f8984e2f1d76b3f3e3412b3e41a837f1db), [b/205344028](https://issuetracker.google.com/issues/205344028))

**Bug Fixes**

- The result of `PagingSource.getRefreshKey()` is now correctly priotized over `initialKey` in cases where it would return null, but a non-null `initialKey` was set. ([Ic9542](https://android-review.googlesource.com/#/q/Ic9542c0062f9a72e5cfa15469bcf0c204a0934bd), [b/230391606](https://issuetracker.google.com/issues/230391606))

**External Contribution**

- Updated :compose:ui:ui-test api (updateApi) due to test-coroutines-lib migration ([I3366d](https://android-review.googlesource.com/#/q/I3366d5111b2fb830d619da5402c12ea4c929391a))

## Version 3.1

### Version 3.1.1

March 9, 2022

`androidx.paging:paging-*:3.1.1` is released. [Version 3.1.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/04b73e954d139340d0ac8b00cdcef55b103ba393..65c8f2c53158200a61e0e1cc012cdbbadaee60ab/paging)

**Bug Fixes**

- Removed intermediate `LoadState.NotLoading` events between generations that were incorrectly inserted by `.cachedIn()`. This change makes it much easier to react on `LoadState` changes by removing redundant `LoadState.NotLoading` events that were produced between retrying failed loads, when refreshing or during invalidation.

### Version 3.1.0

November 17, 2021

`androidx.paging:paging-*:3.1.0` is released. [Version 3.1.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b15a1d282b578971faba0bbe4e631dd2e9b5b854..04b73e954d139340d0ac8b00cdcef55b103ba393/paging)

**Important changes since 3.0.0**

- `Flow<PagingData>.observable` and `Flow<PagingData>.flowable` APIs are no longer experimental
- Behavior changes to `LoadState`:
  - `endOfPaginationReached` is now always `false` for `LoadType.REFRESH` for both `PagingSource` and `RemoteMediator`
  - `LoadStates` from Paging now await valid values from both `PagingSource` and `RemoteMediator` before emitting downstream. New generations of `PagingData` will now always correctly begin with `Loading` for refresh state instead of resetting to `NotLoading` incorrectly in some cases.
  - `.loadStateFlow` and `.addLoadStateListener` on presenter APIs no longer redundantly send an initial `CombinedLoadStates` that always has mediator states set to `null`
- Cancellation on past generations now happens eagerly on invalidation / new generations. It should no longer be required to use `.collectLatest` on `Flow<PagingData>`, although it is still recommended to do so.
- `PagingSource.LoadResult.Invalid` has been added as a new return type from `PagingSource.load`, which causes Paging to discard any pending or future load requests to this `PagingSource` and invalidate it. This return type is designed to handle potentially invalid or stale data that can be returned from the database or network.
- Added `.onPagesPresented` and `.addOnPagesUpdatedListener` presenter APIs which triggered synchronously as pages are presented in UI. Page updates can happen in the following scenarios:
  - Initial load of a new generation of PagingData completes, regardless if the new generation contains any changes to the presented items. i.e., A new generation completing initial load with no updates because the list is exactly the same will still trigger this callback.
  - A page is inserted, even if the inserted page contains no new items.
  - A page is dropped, even if the dropped page was empty.

### Version 3.1.0-rc01

November 3, 2021

`androidx.paging:paging-*:3.1.0-rc01` is released. [Version 3.1.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..b15a1d282b578971faba0bbe4e631dd2e9b5b854/paging)

**Bug Fixes**

- Fixed a race condition + memory leak in .cachedIn() in cases where multiple load events were sent by Paging downstream while there are no observers or between when an observer is switching to a new PagingData. ([Ib682e](https://android-review.googlesource.com/c/platform/frameworks/support/+/1869943))

### Version 3.1.0-beta01

October 13, 2021

`androidx.paging:paging-*:3.1.0-beta01` is released. [Version 3.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/paging)

**Bug Fixes**

- Fixed an issue where many rapid item accesses could cause them to get dropped for consideration in prefetchDistance, causing page loads to stall. This is especially an issue when many items are laid out at once in an order which would prioritize loading against the user scroll direction. These item accesses are now buffered and synchronously prioritized to prevent them from getting dropped. ([aosp/1833273](https://android-review.googlesource.com/c/platform/frameworks/support/+/1833273))

### Version 3.1.0-alpha04

September 29, 2021

`androidx.paging:paging-*:3.1.0-alpha04` is released. [Version 3.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/paging)

**API Changes**

- `Flow<PagingData>.observable` and `Flow<PagingData>.flowable` APIs are no longer experimental. ([Ie0bdd](https://android-review.googlesource.com/#/q/Ie0bdd8c453baa752836a0c53e5ff035fcf8d85c5))

**Bug Fixes**

- For LoadStates, `endOfPaginationReached` is now always `false` for `LoadType.REFRESH`. Previously, it was possible for endOfPaginationReached to be `true` for RemoteMediator `REFRESH`, but not for PagingSource. This behavior is now consolidated to always return `false` as it never makes sense for REFRESH to be terminal, and is now documented as part of the API contract in LoadStates. When deciding if pagination is terminated, you should always do so with respect to either the APPEND or PREPEND directions. ([I047b6](https://android-review.googlesource.com/#/q/I047b601726e8cbdb55eb68bd849cba1136dd0e3e))
- LoadStates from Paging now await valid values from both
  PagingSource and RemoteMediator before emitting downstream between
  generations. This prevents new generations of PagingData from sending
  NotLoading in CombinedLoadStates.source.refresh if it was already
  Loading; new generations of PagingData will now always correctly begin
  with Loading for refresh state instead of first resetting to NotLoading
  incorrectly in some cases.

  Cancellation on past generations now happen eagerly on invalidation /
  new generations. It should no longer be required to use .collectLatest
  on `Flow<PagingData>`, although it is still highly recommended to do so. ([I0b2b5](https://android-review.googlesource.com/#/q/I0b2b5e0120e2e3a677f65d40d3955a9bbbe2e1a9), [b/177351336](https://issuetracker.google.com/issues/177351336), [b/195028524](https://issuetracker.google.com/issues/195028524))
- `.loadStateFlow` and `.addLoadStateListener` on presenter APIs
  no longer redundantly send an initial `CombinedLoadStates` that always
  has mediator states set to `null` and source states set to
  `NotLoading(endOfPaginationReached = false)`. This means that:

  1. mediator states will always be populated if you use RemoteMediator.
  2. Registering a new loadState listener or a new collector on `.loadStateFlow` will no longer immediately emit the current value if it hasn't received a real `CombinedLoadStates` from `PagingData`. This can happen if a collector or listener starts before a `PagingData` has been submitted. ([I1a748](https://android-review.googlesource.com/#/q/I1a7485edd077f1ae08f7d9656cbcdfb6bf9ec99f))

### Version 3.1.0-alpha03

July 21, 2021

`androidx.paging:paging-*:3.1.0-alpha03` is released. [Version 3.1.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/paging)

**API Changes**

- A third LoadResult return type LoadResult.Invalid is added to
  PagingSource. When a PagingSource.load returns
  LoadResult.Invalid, paging will discard the loaded data and
  invalidate the PagingSource. This return type is designed to
  handle potentially invalid or stale data that can be returned
  from the database or network.

  For example, if the underlying database gets written into but
  the PagingSource does not invalidate in time, it may return
  inconsistent results if its implementation depends on the
  immutability of the backing dataset it loads from (e.g., LIMIT
  OFFSET style db implementations). In this scenario, it is
  recommended to check for invalidation after loading and to
  return LoadResult.Invalid, which causes Paging to discard any
  pending or future load requests to this PagingSource and
  invalidate it.

  This return type is also supported by Paging2 API that leverages
  LivePagedList or RxPagedList. When using a PagingSource with
  Paging2's PagedList APIs, the PagedList is immediately detached,
  stopping further attempts to load data on this PagedList and
  triggers invalidation on the PagingSource.

  LoadResult is a sealed class, which means this is a
  source-incompatible change such that use cases directly using
  PagingSource.load results will have to handle LoadResult.Invalid
  at compile time. For example, Kotlin users leveraging
  exhaustive-when to check return type will have to add a check
  for Invalid type. ([Id6bd3](https://android-review.googlesource.com/#/q/Id6bd3f2544f1ba97a95a0d590353438a95fedf2a), [b/191806126](https://issuetracker.google.com/issues/191806126), [b/192013267](https://issuetracker.google.com/issues/192013267))

**Bug Fixes**

- Invalidation callbacks added via PagingSource.registerInvalidatedCallback or DataSource.addInvalidatedCallback now automatically trigger if they were registered on a PagingSource / DataSource that was already invalid. This resolves a race condition which caused Paging to drop invalidation signals and get stuck when provided a Source which was already invalid during initial load. Additionally, invalidate callbacks are now properly removed after being triggered as they are guaranteed to be called at most once. ([I27e69](https://android-review.googlesource.com/#/q/I27e699be2bfa3d6656d10c8c0c1f2ef9638f52fc))
- Submitting the placeholder initial value (InitialPagedList) from a newly instantiated PagedList stream, e.g., LivePagedListBuilder or RxPagedListBuilder will no longer clear previously loaded data.

### Version 3.1.0-alpha02

July 1, 2021

`androidx.paging:paging-*:3.1.0-alpha02` is released. [Version 3.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/paging)

**New Features**

- Added onPagesPresented listener and flow presenter APIs
  which trigger immediately after presented pages are updated in UI.

  Since these updates are synchronous with UI, you may call adapter methods
  such as .snapshot, .getItemCount, to inspect the state after the
  update has been applied. Note that .snapshot() was left to be
  explicitly called because it can be expensive to do on every update.

  Page updates can happen in the following scenarios:
  - Initial load of a new generation of PagingData completes, regardless if the new generation contains any changes to the presented items. i.e., A new generation completing initial load with no updates because the list is exactly the same will still trigger this callback.
  - A page is inserted, even if the inserted page contains no new items
  - A page is dropped, even if the dropped page was empty ([I272c9](https://android-review.googlesource.com/#/q/I272c9a6b5d80f155dffcc05d5cda176d58c18d31), [b/189999634](https://issuetracker.google.com/issues/189999634))

**Bug Fixes**

- Accessing PagedList.dataSource from the initial value produced by LivePagedList or RxPagedList will no longer incorrectly throw an IllegalStateException ([I96707](https://android-review.googlesource.com/#/q/I96707a477f347bd19e7aeccdb52eca39d637297a))

### Version 3.1.0-alpha01

June 2, 2021

`androidx.paging:paging-*:3.1.0-alpha01` is released. [Version 3.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5651d1dbcb19d1b2d3cc50e8c379a8cc9f6ee1ad..86ff5b4bb956431ec884586ce0aea0127e189ec4/paging)

**API Changes**

- Classes provided by `paging-rxjava3` now live under the `androidx.paging.rxjava3` package so that they do not conflict with `paging-rxjava2` ([Ifa7f6](https://android-review.googlesource.com/#/q/Ifa7f693a3207da589926b35428637dd128ffc762))

**Bug Fixes**

- Fixed an issue where Paging would sometimes send no-op differ events to RecyclerView, which could cause certain listeners to trigger early. ([Ic507f](https://android-review.googlesource.com/#/q/Ic507fa793cb22ac9f8880a8f8841f8e6caa197f4), [b/182510751](https://issuetracker.google.com/issues/182510751))

**External Contribution**

- Added deprecated PagedList compat APIs to rxjava3 artifact ([Id1ce2](https://android-review.googlesource.com/#/q/Id1ce2d9a3b1c7e7d1d20bf6e9f4cdc646376b43d), [b/182497591](https://issuetracker.google.com/issues/182497591))

## Paging Compose Version 1.0.0

### Version 1.0.0-alpha20

May 24, 2023

`androidx.paging:paging-compose:1.0.0-alpha20` is released. [Version 1.0.0-alpha20 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6f3ac2bd197d5e61ab2708125b57d6ae4003ad68..c5bf9bc40dd5d9f0b3f34e7273ac0d4e4f05c41d/paging/paging-compose)

**New Features**

- Paging Compose now supports previewing a list of fake data by creating a `PagingData.from(fakeData)` and wrapping that `PagingData` in a `MutableStateFlow` (e.g., `MutableStateFlow(PagingData.from(listOf(1, 2, 3)))`). By using that data as the input into your `@Preview`, calls to `collectAsLazyPagingItems()` will provide previewable `LazyPagingItems`. ([I8a78d](https://android-review.googlesource.com/#/q/I8a78db059776190b833773986825579e96e042d5), [b/194544557](https://issuetracker.google.com/issues/194544557))

**Bug Fixes**

- Cached data from `pager.flow.cachedIn` that has been collected in `LazyPagingItems` will now be immediately available after state restoration without requiring asynchronous collection. This means the cached data will be ready for presentation immediately upon initial composition after state is restored. ([I97a60](https://android-review.googlesource.com/#/q/I97a6078c0563f8017af24448c32e59b86a987465), [b/177245496](https://issuetracker.google.com/issues/177245496))

### Version 1.0.0-alpha19

May 3, 2023

`androidx.paging:paging-compose:1.0.0-alpha19` is released. [Version 1.0.0-alpha19 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7d3ac1ab1206c01fae3ebb500b5b942636070155..6f3ac2bd197d5e61ab2708125b57d6ae4003ad68/paging/paging-compose)

**Supporting all lazy layouts**

Previously, Paging Compose provided custom `items` and `itemsIndexed` extensions on `LazyListScope`, which meant that you could not use Paging Compose with other lazy layouts like `LazyVerticalGrid`, `HorizontalPager`, or other custom lazy components provided by the Wear and TV libraries. Addressing this inflexibility is the primary update for this release.

To support more lazy layouts, we needed to build out APIs at a different layer - rather than providing a custom `items` API for each lazy layout, Paging Compose now provides slightly lower level extension methods on `LazyPagingItems` in `itemKey` and `itemContentType`. These APIs focus on helping you implement the `key` and `contentType` parameters to the standard `items` APIs that already exist for `LazyColumn`, `LazyVerticalGrid` as well as their equivalents in APIs like `HorizontalPager`. ([Ifa13b](https://android-review.googlesource.com/q/Ifa13b3d764203422645cac8bfc3d09278d508874), [Ib04f0](https://android-review.googlesource.com/q/Ib04f099111605af368c5b025d84a085ab4251fb6), [b/259385813](https://issuetracker.google.com/issues/259385813))

This means that supporting a `LazyVerticalGrid` would look like:

    // This part is unchanged
    val lazyPagingItems = pager.collectAsLazyPagingItems()

    LazyVerticalGrid(columns = GridCells.Fixed(2)) {
      // Here we use the standard items API
      items(
        count = lazyPagingItems.itemCount,
        // Here we use the new itemKey extension on LazyPagingItems to
        // handle placeholders automatically, ensuring you only need to provide
        // keys for real items
        key = lazyPagingItems.itemKey { it.uniqueId },
        // Similarly, itemContentType lets you set a custom content type for each item
        contentType = lazyPagingItems.itemContentType { "contentType" }
      ) { index ->
        // As the standard items call provides only the index, we get the item
        // directly from our lazyPagingItems
        val item = lazyPagingItems[index]
        PagingItem(item = item)
      }
    }

For more examples of using these new APIs, please see [our samples](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:paging/paging-compose/samples/src/main/java/androidx/paging/compose/samples/PagingFoundationSample.kt?q=PagingFoundationSample).

While these changes do make the `LazyColumn` and `LazyRow` examples a few lines longer, we felt that consistency across all lazy layouts was an important factor for those using Paging Compose going forward. For that reason, the existing extensions to `LazyListScope` have now been deprecated. ([I0c459](https://android-review.googlesource.com/#/q/I0c45926ecf7fbaa7b68fba7bb1201cdf6f13105d), [I92c8f](https://android-review.googlesource.com/#/q/I92c8ffc330fd98f9fb31fe14db2da7a3f7a3b547), [b/276989796](https://issuetracker.google.com/issues/276989796))
| **Note:** while the deprecated `items` API has a clear equivalent, the quick fix for `itemsIndexed` may still leave your code in a state where it does not compile immediately as generating keys and content types based on indices is no longer possible or recommended as this pattern is susceptible to errors when item indices shift due to prepends (i.e., item 0 actually becomes item 20 due to prepending 20 additional items). It is always recommended to use `items` when using Paging Compose.

**API Changes**

- To ease the migration to the new APIs, the `items` and `itemsIndexed` extension functions on `LazyListScope` now support a `contentType` parameter, mirroring the support in the new APIs. ([Ib1918](https://android-review.googlesource.com/#/q/Ib19181ac9cfd734c940c015a605c03440bbdfda6), [b/255283378](https://issuetracker.google.com/issues/255283378))

**Dependency Updates**

- Paging Compose has updated its dependency from Compose 1.0.5 to Compose 1.2.1. ([Ib1918](https://android-review.googlesource.com/#/q/Ib19181ac9cfd734c940c015a605c03440bbdfda6), [b/255283378](https://issuetracker.google.com/issues/255283378))

### Version 1.0.0-alpha18

February 8, 2023

`androidx.paging:paging-compose:1.0.0-alpha18` is released with no changes. [Version 1.0.0-alpha18 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/548c8ac2570ae6cf15798fea1380491f7d93796b..7d3ac1ab1206c01fae3ebb500b5b942636070155/paging/paging-compose)

### Version 1.0.0-alpha17

October 24, 2022

`androidx.paging:paging-compose:1.0.0-alpha17` is released. [Version 1.0.0-alpha17 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..548c8ac2570ae6cf15798fea1380491f7d93796b/paging/paging-compose)

**New Features**

- Add support for a custom `CoroutineContext` when calling `collectLazyPagingItems`. ([I7a574](https://android-review.googlesource.com/#/q/I7a57418bcbd9ab86ddcbed3313b00aa82bf2398f), [b/243182795](https://issuetracker.google.com/issues/243182795), [b/233783862](https://issuetracker.google.com/issues/233783862))

### Version 1.0.0-alpha16

August 10, 2022

`androidx.paging:paging-compose:1.0.0-alpha16` is released. [Version 1.0.0-alpha16 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..bea814b246f89ff7244e3c6b0648f0b57e47897c/paging/paging-compose)

**New Features**

- Paging now provides logs via the `LazyPagingItems` class to expose debugging information collected from PagingData.
- The logs can be enabled via the `adb shell` command `adb shell setprop log.tag.Paging [DEBUG|VERBOSE]`. (\[b/235527159}(https://issuetracker.google.com/issues/235527159))

**Bug Fixes**

- Fixed the missing `PagingDataDiffer` constructor error when using `paging-compose:1.0.0-alpha15` with `paging-common:3.1.1` or older.([b/235256201](https://issuetracker.google.com/issues/235256201),[b/239868768](https://issuetracker.google.com/issues/239868768))

### Version 1.0.0-alpha15

June 1, 2022

`androidx.paging:paging-compose:1.0.0-alpha15` is released. [Version 1.0.0-alpha15 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..7cbb37cc779160b89644d03e042c129d0ce025d2/paging/paging-compose)

**API Changes**

- Added constructors for `PagingDataAdapter` and `AsyncPagingDataDiffer` which accept `CoroutineContext` instead of `CoroutineDispatcher`. ([Idc878](https://android-review.googlesource.com/#/q/Idc8784ff12a2d6e4a617bae51c7053582c5f1986))

**Bug Fixes**

- `LazyPagingItems` now sets the initial `loadState` to have a `LoadState.Loading` refresh. ([I55043](https://android-review.googlesource.com/#/q/I55043244f92c8029e4667df2e23c5813dcf2f729), [b/224855902](https://issuetracker.google.com/issues/224855902))

### Version 1.0.0-alpha14

October 13, 2021

`androidx.paging:paging-compose:1.0.0-alpha14` is released. [Version 1.0.0-alpha14 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/paging/paging-compose)

### Version 1.0.0-alpha13

September 29, 2021

`androidx.paging:paging-compose:1.0.0-alpha13` is released. [Version 1.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/paging/paging-compose)

**API Changes**

- `LazyPagingItems.snapshot()` function was replaced with`LazyPagingItems.itemSnapshotList` property ([Ie2da8](https://android-review.googlesource.com/#/q/Ie2da86edc45827f8282b524b5bb1bfe8f349a9da))
- Deprecated `LazyPagingItems.getAsState()` was removed ([Ie65e4](https://android-review.googlesource.com/#/q/Ie65e417e6fd3c20553dcc799bcceffdf00dfc98a))

### Version 1.0.0-alpha12

July 21, 2021

`androidx.paging:paging-compose:1.0.0-alpha12` is released. [Version 1.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/19ae3a88ff0824d615355b492cb56049e16991f2..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/paging/paging-compose)

**API Changes**

- `items(lazyPagingItems)` and `itemsIndexed(lazyPagingItems)` used to connect Paging with `LazyColumn/Row` now accept the option key param which allows you to specify a stable key representing the item. You can read more about keys [here.](https://developer.android.com/jetpack/compose/lists#item-keys) ([I7986d](https://android-review.googlesource.com/#/q/I7986d308b9588a43bb11fe7ac4f3b420bbafda70))
- Function `lazyPagingItems.getAsState(index)` is now deprecated. Use `lazyPagingItems[index]` instead. ([I086cb](https://android-review.googlesource.com/#/q/I086cbb113a0c4ddcc333c78fa1346612e4496a5b), [b/187339372](https://issuetracker.google.com/issues/187339372))

### Version 1.0.0-alpha11

June 30, 2021

`androidx.paging:paging-compose:1.0.0-alpha11` is released. [Version 1.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/86ff5b4bb956431ec884586ce0aea0127e189ec4..19ae3a88ff0824d615355b492cb56049e16991f2/paging/paging-compose)

### Version 1.0.0-alpha10

June 2, 2021

`androidx.paging:paging-compose:1.0.0-alpha10` is released. [Version 1.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12..86ff5b4bb956431ec884586ce0aea0127e189ec4/paging/paging-compose)

### Version 1.0.0-alpha09

May 18, 2021

`androidx.paging:paging-compose:1.0.0-alpha09` is released. [Version 1.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4b6cff92e45f1d4467086aa2c6aa0248b4883950..b648147c5fdfc5ecbad57e40e2dc0c69aa23bf12/paging/paging-compose)

**Bug Fixes**

- LazyPagingItems' itemCount and item getter are now observable which allows it to be used with LazyVerticalGrid as well ([Ie2446](https://android-review.googlesource.com/#/q/Ie24468ec51660c144acab71e8e520ac09d00b023), [b/171872064](https://issuetracker.google.com/issues/171872064), [b/168285687](https://issuetracker.google.com/issues/168285687))

**Compose Compatibility**

- `androidx.paging:paging-compose:1.0.0-alpha09` is only compatible with Compose version `1.0.0-beta07` and above.

### Version 1.0.0-alpha08

February 24, 2021

`androidx.paging:paging-compose:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..4b6cff92e45f1d4467086aa2c6aa0248b4883950/paging/paging-compose)

Updated to integrate with Compose 1.0.0-beta01.
| **Note:** Paging Compose 1.0.0-alpha08 is only compatible with Compose 1.0.0-beta01.

### Version 1.0.0-alpha07

February 10, 2021

`androidx.paging:paging-compose:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6950aab50fe6c9f7e9d97cf865161f2d3999eb9e..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/paging/paging-compose)

Updated to integrate with Compose alpha12.

### Version 1.0.0-alpha06

January 28, 2021

`androidx.paging:paging-compose:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..aee18b103203a91ee89df91f0af5df2ecff356d6/paging/paging-compose)

**Bug Fixes**

Updated to depend on Compose 1.0.0-alpha11.

### Version 1.0.0-alpha05

January 13, 2021

`androidx.paging:paging-compose:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/72f02c12e4709ab41ae0fea9a8a668d5267a1df8..6207afb1646d302c5d29c2c67d332b48db87fb27/paging/paging-compose)

Updated to depend on Compose 1.0.0-alpha10.

### Version 1.0.0-alpha04

December 16, 2020

`androidx.paging:paging-compose:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/10b5e9fd366c1c413d5576aed50a305d300938e1..72f02c12e4709ab41ae0fea9a8a668d5267a1df8/paging/paging-compose)

**Bug Fixes**

- Updated the convenience properties, `CombinedLoadStates.refresh`, `CombinedLoadStates.prepend`, `CombinedLoadStates.append` to only transition from `Loading` to `NotLoading` after both mediator and source load states are `NotLoading` to ensure the remote update has been applied. ([I65619](https://android-review.googlesource.com/#/q/I656192632c4ce073ac8e54a3f1c597bbbae77002))

### Version 1.0.0-alpha03

December 2, 2020

`androidx.paging:paging-compose:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..10b5e9fd366c1c413d5576aed50a305d300938e1/paging/paging-compose)

- Updated to match Compose 1.0.0-alpha08.

### Version 1.0.0-alpha02

November 11, 2020

`androidx.paging:paging-compose:1.0.0-alpha02` is released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/paging/compose)

**API Changes**

- Added `.peek()`, `.snapshot()`, `.retry()` and `.refresh()` methods to `LazyPagingItem`s which expose the same functionality available in `AsyncPagingDataDiffer` / `PagingDataAdapter` ([Iddfe8](https://android-review.googlesource.com/#/q/Iddfe8a8dc9339bf4aff86f562b94eabdf8f92056), [b/172041660](https://issuetracker.google.com/issues/172041660))

### Version 1.0.0-alpha01

October 28, 2020

`androidx.paging:paging-compose:1.0.0-alpha01` is released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b/paging/compose)

**New Features**

The `paging-compose` artifact provides integration between [The Paging Library](https://developer.android.com/paging) and [Jetpack Compose](https://developer.android.com/jetpack/compose). A simple usage example:

      @Composable
      @OptIn(ExperimentalLazyDsl::class)
      fun ItemsDemo(flow: Flow<PagingData<String>>) {
          val lazyPagingItems = flow.collectAsLazyPagingItems()
          LazyColumn {
              items(lazyPagingItems) {
                  Text("Item is $it")
              }
          }
      }

## Version 3.0.1

### Version 3.0.1

July 21, 2021

`androidx.paging:paging-*:3.0.1` is released. [Version 3.0.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5651d1dbcb19d1b2d3cc50e8c379a8cc9f6ee1ad..650bc3241df3e2336ba181a08d14611087c73083/paging)

**Bug Fixes**

- Accessing `PagedList.dataSource` from the initial value produced by `LivePagedList` or `RxPagedList` will no longer incorrectly throw an IllegalStateException ([I96707](https://android-review.googlesource.com/#/q/I96707a477f347bd19e7aeccdb52eca39d637297a))

## Version 3.0.0

### Version 3.0.0

May 5, 2021

`androidx.paging:paging-*:3.0.0` is released. [Version 3.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ce0bda2d989654e33f843b4c7cb263afaca28b14..5651d1dbcb19d1b2d3cc50e8c379a8cc9f6ee1ad/paging)

**Major features of 3.0.0**

The majority of the existing API from Paging 2.x.x has been deprecated in favor of the new Paging 3 APIs to bring the following improvements:

- First-class support for Kotlin coroutines and Flow
- Support for cancellation
- Built-in load state and error signals
- Retry + refresh functionality
- All three DataSource subclasses have been combined into a unified PagingSource class
- Custom page transformations including a built-in one for adding separators
- Loading state headers and footers

### Version 3.0.0-rc01

April 21, 2021

`androidx.paging:paging-*:3.0.0-rc01` is released. [Version 3.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c42896eb6591b09e3952030fb7ea8d9b8c42713..ce0bda2d989654e33f843b4c7cb263afaca28b14/paging)

**Bug Fixes**

- Fixed an issue where Paging would sometimes send no-op differ events to RecyclerView, which could cause certain listeners to trigger early. ([Ic507f](https://android-review.googlesource.com/#/q/Ic507fa793cb22ac9f8880a8f8841f8e6caa197f4), [b/182510751](https://issuetracker.google.com/issues/182510751))

### Version 3.0.0-beta03

March 24, 2021

`androidx.paging:paging-*:3.0.0-beta03` is released. [Version 3.0.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..5c42896eb6591b09e3952030fb7ea8d9b8c42713/paging)

**Bug Fixes**

- We've revamped how placeholders are handled when list is reloaded to prevent unexpected jumps in RecyclerView. See [NullPaddedDiffing.md](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:paging/runtime/src/main/java/androidx/paging/NullPaddedDiffing.md) for details. ([If1490](https://android-review.googlesource.com/#/q/If1490f5bc833a61793d27eeaae9b37b26153df87), [b/170027529](https://issuetracker.google.com/issues/170027529), [b/177338149](https://issuetracker.google.com/issues/177338149))
- The various PagedList builders (old compatibility path) no longer incorrectly synchronously call `DataSource.Factory.create()` on Main thread when `.build()` is called. ([b/182798948](https://issuetracker.google.com/182798948))

### Version 3.0.0-beta02

March 10, 2021

`androidx.paging:paging-*:3.0.0-beta02` is released. [Version 3.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/602cf9bff5e74e4355760aa47d3fc73a2e6d779b..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/paging)

**API Changes**

- Rx3 extensions now correctly propagate `@ExperimentalCoroutinesApi` Opt-In requirement. Previously they were marked on the `@get` method, which is ignored by the Kotlin Compiler due to: https://youtrack.jetbrains.com/issue/KT-45227 ([I5733c](https://android-review.googlesource.com/#/q/I5733cdcebf531126d4aa6bef66daefe53a8d7177))

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))
- Fixed a bug causing `PagingState` to always be `null` when remote refresh is called.
- Fixed a bug where empty pages returned by PagingSource could prevent Paging from fetching again to fulfill `prefetchDistance` causing Paging to get "stuck".

| **Note:** Users using PagingSource provided by Room should upgrade to 2.3.0-beta03, which fixes a critical threading bug that could cause Paging to crash due to creating PagingSource on the main thread.

### Version 3.0.0-beta01

February 10, 2021

`androidx.paging:paging-*:3.0.0-beta01` is released. [Version 3.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..602cf9bff5e74e4355760aa47d3fc73a2e6d779b/paging)

**API Changes**

- Rx2 and Rx3 wrappers now expose the experimental annotation it depends on. If you are using the Rx compat wrappers in paging-rxjava2 or paging-rxjava3, you will now need to annotate usages with `@OptIn(ExperimentalCoroutinesApi::class)` ([Ib1f9d](https://android-review.googlesource.com/#/q/Ib1f9d578ee9eb4c1bdf6c8bbabc99c978398c584))

**Bug Fixes**

- Fixed `IndexOutOfBoundsException: Inconsistency detected` sometimes thrown when using v2 `DataSource` APIs through compatibility paths
- `isInvalid` call during initialization of `DataSource` when used via compatibility paths are now correctly launched on fetchDispatcher instead of on the main thread. This fixes an `IllegalStateException` due to Db access on the main thread when using Room's `PagingSource` implementation.

### Version 3.0.0-alpha13

January 27, 2021

`androidx.paging:paging-*:3.0.0-alpha13` is released. [Version 3.0.0-alpha13 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6207afb1646d302c5d29c2c67d332b48db87fb27..aee18b103203a91ee89df91f0af5df2ecff356d6/paging)

**API Changes**

- `PagingSource.getRefreshKey` is no longer optional to implement, it is now an abstract function without a default implementation. Migrating users can either continue returning the default implementation, which simply returns `null`, but `getRefreshKey()` should have a real implementation returning a key based on user's current scroll position that allows Paging to continue loading centered around the viewport via `PagingState.anchorPosition` if possible. ([I4339a](https://android-review.googlesource.com/#/q/I4339a1a2962b6883451511439012d084ada84651))
- `InvalidatingPagingSourceFactory` is now a final class ([Ia3b0a](https://android-review.googlesource.com/#/q/Ia3b0a3540f14606f120708c542071fa72030afed))
- Allow configuration of terminal separator (header / footer) behavior with an additional optional SeparatorType parameter. The two options are:
  - `FULLY_COMPLETE` - existing behavior; wait for both PagingSource and RemoteMediator to mark endOfPaginationReached before adding terminal separators. If RemoteMediator is not used, remote loadState is ignored. This is primarily useful if you only want to show section separators when the section is fully loaded, including fetching from remote source e.g., network.
  - `SOURCE_COMPLETE` - only wait for PagingSource to mark endOfPaginationReached even if RemoteMediator is used. This allows headers and footers to be presented synchronously with the initial load, which prevents users from needing to scroll to see terminal separators. ([Ibe993](https://android-review.googlesource.com/#/q/Ibe9938d069e66d0deae806dc44684f3a05e651a0), [b/174700218](https://issuetracker.google.com/issues/174700218))

**Bug Fixes**

- Fixed a rare memory leak which happens when a PagingSource is invalidated before PageFetcher can even begin to start loading from it. ([I9606b](https://android-review.googlesource.com/#/q/I9606bc3c393a40d732bf633b721b13b23c46db02), [b/174625633](https://issuetracker.google.com/issues/174625633))

### Version 3.0.0-alpha12

January 13, 2021

`androidx.paging:paging-*:3.0.0-alpha12` is released. [Version 3.0.0-alpha12 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd3c8e9c2424b78e44f55db599251891fd1cadb4..6207afb1646d302c5d29c2c67d332b48db87fb27/paging)

**API Changes**

- InvalidatingPagingSourceFactory is no longer an abstract class as it never had any abstract methods. ([I4a8c4](https://android-review.googlesource.com/#/q/I4a8c48ecf20b539a058f90e8675554a671b4a653))
- Added an overload of .cachedIn() that accepts ViewModel instead of Lifecycle or CoroutineScope for Java users. ([I97d81](https://android-review.googlesource.com/#/q/I97d815a9a2750eaae3445ea9cb222c14f5125a0b), [b/175332619](https://issuetracker.google.com/issues/175332619))
- Allow Java callers to use PagingData transform operations in an async way, by accepting an Executor into transform operator arguments. All of the -Sync transform operators have the -Sync suffix removed now, and Kotlin Coroutine users will need to disambiguate by calling the extension function which accepts a suspending block instead. All PagingData transformation operators have been moved to extensions under the static PagingDataTransforms class. Java users will need to call them via static helpers e.g., `PagingDataTransforms.map(pagingData, transform)` For Kotlin users, the syntax is the same but you'll need to import the function. ([If6885](https://android-review.googlesource.com/#/q/If688562d07d96e943b1abfa3690042132db1c4d0), [b/172895919](https://issuetracker.google.com/issues/172895919))

**Bug Fixes**

- Fixed a bug where `RemoteMediator.load()` would not be called during `adapter.refresh()` if the end of pagination had already been reached.

### Version 3.0.0-alpha11

December 16, 2020

`androidx.paging:paging-*:3.0.0-alpha11` is released. [Version 3.0.0-alpha11 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63..dd3c8e9c2424b78e44f55db599251891fd1cadb4/paging)

**New Features**

- Saved state support added for the following basic use cases (full support, especially in the layered source case is still a work in progress):
  - flow is cached and application is not killed (e.g. flow is cached in a view model and activity is recreated in process)
  - paging source is counted, placeholders are enabled and the layout is not staggered.

**API Changes**

- `PagingSource.getRefreshKey()` is now stable API ([I22f6f](https://android-review.googlesource.com/#/q/I22f6fb44ec84b33f4ed14fc7d4a3783795832c52), [b/173530980](https://issuetracker.google.com/issues/173530980))
- `PagingSource.invalidate` is no longer an open function. If you need to get notified when invalidation happens, consider calling the registerInvalidatedCallback method instead of overriding invalidate. ([I628d9](https://android-review.googlesource.com/#/q/I628d9893a4ac55409aa24e49de1e2d2c35beda4f), [b/173029013](https://issuetracker.google.com/issues/173029013), [b/137971356](https://issuetracker.google.com/issues/137971356))
- Pager now has a single experimental constructor alongside its regular constructors, rather than leaking experimental APIs into non-experimental public API via the opt-in annotation. ([I9dc61](https://android-review.googlesource.com/#/q/I9dc614204842258a72be000c6e37846fb85470c1), [b/174531520](https://issuetracker.google.com/issues/174531520))
- Updated the convenience properties, `CombinedLoadStates.refresh`, `CombinedLoadStates.prepend`, `CombinedLoadStates.append` to only transition from `Loading` to `NotLoading` after both mediator and source load states are `NotLoading` to ensure the remote update has been applied. ([I65619](https://android-review.googlesource.com/#/q/I656192632c4ce073ac8e54a3f1c597bbbae77002))
- LoadParams.pageSize has been removed (it was already
  deprecated).
  The recommendation is to use `LoadParams.loadSize` in your PagingSource.

  `LoadParams.loadSize` is always equal to the `PagingConfig.pageSize`
  except for the initial load call where it is equal to the
  `PagingConfig.initialLoadSize`.

  If you are testing your Paging2 DataSource without using a Pager or
  PagedList, `pageSize` may not match the `PagingConfig.pageSize` if
  you are also setting `initialLoadSize`. If it is important for your
  tests, try using a Pager/PagedList instead which will internally set
  the correct PageSize for your DataSource load methods. ([I98ac7](https://android-review.googlesource.com/#/q/I98ac735090f65919282c4afbd005bbd27b9af0f3), [b/149157296](https://issuetracker.google.com/issues/149157296))

**Bug Fixes**

- Fixed a crash due to IllegalStateException when using separators with PagingConfig.maxSize set. ([I0ed33](https://android-review.googlesource.com/#/q/I0ed33e86d3a09e1fb5f157c841331238d7ff83b4), [b/174787528](https://issuetracker.google.com/issues/174787528))
- Fixed a bug where load state for PREPEND / APPEND would not update to `NotLoading(endOfPaginationReached = true)` immediately after initial load if RemoteMediator was set ([I8cf5a](https://android-review.googlesource.com/#/q/I8cf5aec7d1b8499758d4445e3c2ede65a2447df5))
- Fixed a bug where presenter-side APIs such as .snapshot(), .peek(), etc., would return the previous (out-of-date) list within ListUpdateCallback updates.
- Fixed a bug where Separators operators would not add headers or footers when used with RemoteMediator
- Fixed a bug where LoadState updates to NotLoading for RemoteMediator would get stuck in the Loading state
- Fixed a bug where the Paging2.0 compatibility API, `.asPagingSourceFactory()`, could cause the backing `DataSource` to be initialized on the incorrect CoroutineDispatcher. This resolves a crash and possible ANR cases, especially when using Room's current implementation of PagingSource, which uses this compatibility path.

### Version 3.0.0-alpha10

December 2, 2020

`androidx.paging:paging-*:3.0.0-alpha10` is released. [Version 3.0.0-alpha10 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/paging)

**API Changes**

- The deprecated `dataRefreshFlow` and `dataRefreshListener` APIs have been removed
  as they are redundant with loadStateFlow / Listener updates. For
  those migrating, the loadStateFlow equivalent is:

      loadStateFlow.distinctUntilChangedBy { it.refresh }
          .filter { it.refresh is NotLoading }

  ([Ib5570](https://android-review.googlesource.com/#/q/Ib55709c3f560711200a9eac5a4931d57c76053af), [b/173530908](https://issuetracker.google.com/issues/173530908))

**Bug Fixes**

- endOfPaginationReached for RemoteMediator `REFRESH` now correctly propagate to LoadState updates and prevents remote `APPEND` and `PREPEND` from triggering. ([I94a3f](https://android-review.googlesource.com/#/q/I94a3f787182eee6c5875b11e8c861d5e6e6e9e22), [b/155290248](https://issuetracker.google.com/issues/155290248))
- Presenting an empty list either due to empty initial page or heavy filtering will no longer prevent Paging from kicking off `PREPEND` or `APPEND` loads. ([I3e702](https://android-review.googlesource.com/#/q/I3e702b6daf002f6dd3010c9b6f8867caf95135e0), [b/168169730](https://issuetracker.google.com/issues/168169730))
- Fixed an issue where `getRefreshKey` does not get called on subsequent generations of PagingSource when invalidations occur rapidly. ([I45460](https://android-review.googlesource.com/#/q/I4546070c31ed73fd285754707b8b480cba206b93), [b/170027530](https://issuetracker.google.com/issues/170027530))

**External Contribution**

- A new abstract class InvalidatingPagingSourceFactory has been added with an `.invalidate()` API that forwards invalidate to all of the PagingSources it emits. Thanks to [@claraf3](https://github.com/claraf3)! ([Ie71fc](https://android-review.googlesource.com/#/q/Ie71fc1cc974dbc72f42572234ea9053e31b44039), [b/160716447](https://issuetracker.google.com/issues/160716447))

**Known Issues**

- Headers and footers from the .insertSeparators() transform may not appear immediately when using RemoteMediator [b/172254056](https://issuetracker.google.com/172254056)
- Using RemoteMediator can cause remote `LoadState` to get stuck if invalidation and `PagingSource.load(LoadParams.Refresh(...))` completes before `RemoteMediator.load()` returns [b/173717820](https://issuetracker.google.com/173717820)

### Version 3.0.0-alpha09

November 11, 2020

`androidx.paging:paging-*:3.0.0-alpha09` is released. [Version 3.0.0-alpha09 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/234e23e470a5e7f81291f6acd12d538146dc010b..2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/paging)

**API Changes**

- Fully deprecate dataRefreshFlow / Listener methods with a replaceWith clause. ([I6e2dd](https://android-review.googlesource.com/#/q/I6e2dd23b100bc1186dc652e5076b2d15b191c436))

**Bug Fixes**

- Fix for `IllegalArgumentException` being throw when using separators with RemoteMediator and an invalidate is triggered while a remote load that would return endOfPagination is still running ([I3a260](https://android-review.googlesource.com/#/q/I3a260ff98f07f5be615192e31ce1dc533c8b75b8))

### Version 3.0.0-alpha08

October 28, 2020

`androidx.paging:paging-*:3.0.0-alpha08` is released. [Version 3.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8d1cacd5e482a2b20351525ac2b630ce49911228..234e23e470a5e7f81291f6acd12d538146dc010b/paging)

**API Changes**

- The Kotlin / Java variants of `DataSource.InvalidatedCallback` have been combined by enabling SAM-conversions in Kotlin via functional interface (available in Kotlin 1.4). This also fixes a bug where the kotlin variant of invalidate callbacks were not called after transformed by `.map` or `.mapByPage`. ([I1f244](https://android-review.googlesource.com/#/q/I1f244498bd9f78bfed2744d9e6c9d5c1c1448971), [b/165313046](https://issuetracker.google.com/issues/165313046))

**Bug Fixes**

- Paging's interaction with ViewPager has been improved considerably. Specifically, Paging will no longer cancel a `RemoteMediator#load` call due to a page invalidation. It will also no longer make an append/prepend load request, *if REFRESH is required* , until REFRESH request completes successfully. ([I6390b](https://android-review.googlesource.com/#/q/I6390be0c0c1073005456f928a2a8afa81c16d3ef), [b/162252536](https://issuetracker.google.com/issues/162252536))
- API lint check for MissingGetterMatchingBuilder is enabled for androidx ([I4bbea](https://android-review.googlesource.com/#/q/I4bbeacf9869d8338a3d7086acb40bc56ec68c3f9), [b/138602561](https://issuetracker.google.com/issues/138602561))
- Fixed a bug where `.withLoadState*` `ConcatAdapter` helpers would crash due to notifying RecyclerView from background thread ([I18bb5](https://android-review.googlesource.com/#/q/I18bb54c857dfc5098cd36b5c22dce386c4776d3d), [b/170988309](https://issuetracker.google.com/issues/170988309))
- Fixed a bug where loading a very small non-empty page would sometimes prevent prefetch from triggering loads correctly.[Iffda3](https://android-review.googlesource.com/q/Iffda3a0eb7abe162045893367b4781daf75adb01) [b/169259468](https://issuetracker.google.com/169259468)

### Version 3.0.0-alpha07

October 1, 2020

`androidx.paging:paging-*:3.0.0-alpha07` is released. [Version 3.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..f5a2c7477391539d8bc9f65a8f0db1e8a7bf2cf5/paging)

**API Changes**

- Async PagingData Guava-based operators now accept an Executor as a param, to control execution context. ([Id4372](https://android-review.googlesource.com/#/q/Id4372a9d30afd3f702782bba46f4da37a1b8e30d))

**Bug Fixes**

- Fixed IndexOutOfBounds exception thrown in RemoteMediator due to a race condition. ([I00b7f](https://android-review.googlesource.com/#/q/I00b7f9b00b2a36395ba8fe5c77931fec3ce20d7a), [b/165821814](https://issuetracker.google.com/issues/165821814))
- Fixed a race condition in DataSource -\> PagingSource conversion that could cause the resulting PagingSource to ignore invalidation signals from DataSource.
- Fixed an issue in page fetchin logic that would sometimes cause it to fail to pick up new generations of PagingSource until PagingDataAdapter.refresh() was invoked
- Fixed an issue that would cause scroll-position to sometimes be lost when using a DataSource converted into a PagingSource (such as the one produced by Room), in conjunction with RemoteMediator

**External Contribution**

- Thanks to @simonschiller for adding RxJava2, RxJava3, and Guava-based async transformation operators for PagingData!

### Version 3.0.0-alpha06

September 2, 2020

`androidx.paging:paging-*:3.0.0-alpha06` is released. [Version 3.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/96eb302ee1740ba656c90c9fb27df3723a1a89c1..31022a2dda22705843be1199c786552a6f9f875d/paging)

**API Changes**

- `UnsupportedOperationException` with clearer messaging around lack of support for stable ids is now thrown whenever `PagingDataAdapter.setHasStableIds` is called. ([Ib3890](https://android-review.googlesource.com/#/q/Ib38903e00e30e719a8c0104d076afb1cead6c8e1), [b/158801427](https://issuetracker.google.com/issues/158801427))

**Bug Fixes**

- insertSeparators no longer filters out empty pages allowing prefetch distance to be respected by the presenter even in cases where many empty pages are inserted. ([I9cff6](https://android-review.googlesource.com/#/q/I9cff68ad1cc33076254681a3260be3f8ae32b598), [b/162538908](https://issuetracker.google.com/issues/162538908))

### Version 3.0.0-alpha05

August 19, 2020

`androidx.paging:paging-*:3.0.0-alpha05` is released. [Version 3.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d..96eb302ee1740ba656c90c9fb27df3723a1a89c1/paging)

**Bug Fixes**

- Paging now correctly prefetches pages even when the presented data is heavily filtered
- Returning `LoadResult.Error` to a retried load no longer causes Item accesses to incorrectly re-trigger retry

**External Contribution**

- Thanks to Clara F for helping clean up some tests! ([549612](https://android-review.googlesource.com/c/platform/frameworks/support/+/1394447))

### Version 3.0.0-alpha04

August 5, 2020

`androidx.paging:paging-*:3.0.0-alpha04` is released. [Version 3.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/316f882e649c600372170f013a18515f590f490d/paging)

**API Changes**

- Added `peek()` API to `AsyncPagingDataDiffer` and `PagingDataAdapter` to allow presented data access without trigger page loads. ([I38898](https://android-review.googlesource.com/#/q/I388982364c55ffd87a2f515dffdada817eceaec0), [b/159104197](https://issuetracker.google.com/issues/159104197))
- Added a `snapshot()` API to `PagingDataAdapter` and `AsyncPagingDataDiffer` to allow retrieving the presented items without triggering page fetch. ([I566b6](https://android-review.googlesource.com/#/q/I566b6044da1d9fb26278bb3cada28913684f941b), [b/159104197](https://issuetracker.google.com/issues/159104197))
- Added a `PagingData.from(List<T>)` constructor to allow presenting static lists, which can be combined with the overall PagingData flow to show static lists in certain states, e.g., before initial REFRESH finishes or simply for testing transformations. ([Id134d](https://android-review.googlesource.com/#/q/Id134d9cdb3197a2069f74227f052793ed40971cf))
- Deprecate dataRefresh Flow / Listener APIs as they were intended to expose the presented items state on REFRESH, but with improvements to loadState Flow / Listener callback timing, and itemCount property, it is redundant ([Ia19f3](https://android-review.googlesource.com/#/q/Ia19f3a4249e4f5586894d6702e998a2d9fb22eb0))
- Added RxJava3 compatibility wrappers for `PagingSource` and `RemoteMediator` ([I49ef3](https://android-review.googlesource.com/#/q/I49ef38fde9b84f92dd272ed0b1cd1719fbbf1761), [b/161480176](https://issuetracker.google.com/issues/161480176))

**Bug Fixes**

- `PositionalDataSource` converted into `PagingSource` via `toPagingSourceFactory` helper, including `PagingSource` generated by Room now correctly mark themselves to support jumping. ([I3e84c](https://android-review.googlesource.com/#/q/I3e84c2d0cb941b58862f3804f346151b8d720a37), [b/162161201](https://issuetracker.google.com/issues/162161201))
- Fixed a bug where using the synchronous variant of submitData would sometimes lead to a race causing a `ClosedSendChannelException` ([I4d702](https://android-review.googlesource.com/#/q/I4d70208a6def82099644ec88b087426a1ae0cffd), [b/160192222](https://issuetracker.google.com/issues/160192222))

**External Contribution**

- Thanks to Zac Sweers for adding RxJava3 compatibility wrappers on behalf of Slack! ([I49ef3](https://android-review.googlesource.com/#/q/I49ef38fde9b84f92dd272ed0b1cd1719fbbf1761), [b/161480176](https://issuetracker.google.com/issues/161480176))

### Version 3.0.0-alpha03

July 22, 2020

`androidx.paging:paging-*:3.0.0-alpha03` is released. [Version 3.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b6054a1a7396b962ac2c6d80d21053cf9d2f02db..9f60cc700129e30cee9df020005c317fb39d32ec/paging)

**API Changes**

- The constructor for PagingState is now public, which should make testing implementations of getRefreshKey() easier ([I8bf15](https://android-review.googlesource.com/#/q/I8bf1577c8aad40d90a27f6fec12682ab84d2b49e))
- Hid DataSource kotlin map function variants from Java, to resolve ambiguity between original and kotlin variants. ([If7b23](https://android-review.googlesource.com/#/q/If7b239bfd58391e11b46a4fcd2ea99ffd729f84d), [b/161150011](https://issuetracker.google.com/issues/161150011))
- Redundant APIs intended as conveniences for Kotlin users have been marked @JvmSynthetic ([I56ae5](https://android-review.googlesource.com/#/q/I56ae584e362d046df5361f49005b39c31177f7ac))
- Added overloads for LoadResult.Page's constructor which defaults itemsBefore and itemsAfter to COUNT_UNDEFINED ([I47849](https://android-review.googlesource.com/#/q/I4784906e23efd2f552326f56c145fb4b8754c099))
- Made existing PagingData operators accept suspending methods and introduced new mapSync, flatMapSync, and filterSync non-suspending operators for Java users. The existing transformation methods have been moved to extension functions so Kotlin users will now need to import them. ([I34239](https://android-review.googlesource.com/#/q/I342390a7b1eb98ac87072998744a9e46c99a1000), [b/159983232](https://issuetracker.google.com/issues/159983232))

**Bug Fixes**

- Room (and PositionalDataSource) PagingSources will now display a leading separator as part of the first page, so the user doesn't need to scroll to reveal it. ([I6f747](https://android-review.googlesource.com/#/q/I6f747ebc0b823b146c39b925ce1d659913a50421), [b/160257628](https://issuetracker.google.com/issues/160257628))
- Item accesses on placeholders now correctly trigger PagingSource loads until a page is returned that fulfills the requested index after being transformed by PagingData.filter() ([I95625](https://android-review.googlesource.com/#/q/I95625d22c1775be75f231ec25824b50ef404150d), [b/158763195](https://issuetracker.google.com/issues/158763195))
- Fix for a bug where sometimes scrolling after PagingSource returns an error could prevent PagingDataAdapter.retry() from retrying. ([I1084f](https://android-review.googlesource.com/#/q/I1084fdc5d66254bbbcaa87e154ccab1dbffd54db), [b/160194384](https://issuetracker.google.com/issues/160194384))
- Fixes an issue where item accesses after dropping a page might not load pages although the item access was within prefetchDistance ([Ie95ae](https://android-review.googlesource.com/#/q/Ie95ae57c4f73c35ea0ebd77fe5d7fa7dbf4923e6), [b/160038730](https://issuetracker.google.com/issues/160038730))
- Setting PagingConfig.maxSize no longer enables placeholders after a drop event ([I2be29](https://android-review.googlesource.com/#/q/I2be299e5ce094c8c7460295ff5218758a65dfd1f), [b/159667766](https://issuetracker.google.com/issues/159667766))

### Version 3.0.0-alpha02

June 24, 2020

`androidx.paging:paging-*:3.0.0-alpha02` is released. [Version 3.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91b99a1bab5d164df694a93d77b6694a65257e7e..b6054a1a7396b962ac2c6d80d21053cf9d2f02db/paging)

**API Changes**

- Added overloads for `PagingConfig`'s constructor with common default values ([I39c50](https://android-review.googlesource.com/#/q/I39c508a7403e0372b66d2f511843538e26e7cde7), [b/158576040](https://issuetracker.google.com/issues/158576040))
- Added overloads for constructors of `PagingDataAdapter` and `AsyncPagingDataDiffer` with common default values ([Ie91f5](https://android-review.googlesource.com/#/q/Ie91f55060e17102435525ef4e90f8d943df3c90b))
- The adapter APIs, `dataRefreshFlow` and `dataRefreshListener` now pass a Boolean to signal whether a `PagingData` is empty ([I6e37e](https://android-review.googlesource.com/#/q/I6e37e844cf9f947aeefaaa99d22b2672e04f207d), [b/159054196](https://issuetracker.google.com/issues/159054196))
- Added RxJava and Guava APIs for RemoteMediator - [RxRemoteMediator](https://developer.android.com/reference/kotlin/androidx/paging/RxRemoteMediator) and [ListenableFutureRemoteMediator](https://developer.android.com/reference/kotlin/androidx/paging/ListenableFutureRemoteMediator)
- Added helpers to PagingState for common item access such as `isEmpty()` and `firstItemOrNull()` ([I3b5b6](https://android-review.googlesource.com/#/q/I3b5b687f5188e1408806c567417921fb8101bfdb), [b/158892717](https://issuetracker.google.com/issues/158892717))

**Bug Fixes**

- Pager now checks for PagingSource reuse in factory, to prevent accidental reuse of invalid PagingSources, which gave an unclear error ([I99809](https://android-review.googlesource.com/q/I99809eba7ca878fb841d2f250387d6b989ef701e), [b/158486430](https://issuetracker.google.com/issues/158486430))
- Failures from RemoteMediator REFRESH no longer prevent PagingSource from loading ([I38b1b](https://android-review.googlesource.com/#/q/I38b1b1784af935cfbd8b937d9f4ab372f59619ed), [b/158892717](https://issuetracker.google.com/issues/158892717))
- The non-suspending version of `submitData` no longer causes a crash due to concurrent collection on multiple `PagingData` when called after the suspending version of `submitData`. ([I26358](https://android-review.googlesource.com/#/q/I263580a7cb300229eadaa431fa699f25d7ac4ee1), [b/158048877](https://issuetracker.google.com/issues/158048877))
- Fixed "cannot collect twice from pager" exception that could occur after config change ([I58bcc](https://android-review.googlesource.com/#/q/I58bcc4b2bde88b1c78ed1a96cf227e068127b47e), [b/158784811](https://issuetracker.google.com/issues/158784811))

### Version 3.0.0-alpha01

June 10, 2020

`androidx.paging:paging-*:3.0.0-alpha01` is released. [Version 3.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/91b99a1bab5d164df694a93d77b6694a65257e7e/paging)

The Paging Library has updated to 3.0, to enable several major new features.

**New Features of 3.0**

- First-class support for Kotlin coroutines and Flow.
- Support for async loading with [coroutines suspend functions, RxJava Single or Guava ListenableFuture primitives](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#data-source).
- [Built-in load state and error signals](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#display-loading-state) for responsive UI design, including retry and refresh functionality.
- Improvements to the repository layer
  - [Simplified data source interface](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#data-source)
  - Simplified network + database pagination
  - Cancellation support
- Improvements to the presentation layer
  - [Custom page transformations](https://developer.android.com/topic/libraries/architecture/paging/v3-transform)
  - [List separators](https://developer.android.com/topic/libraries/architecture/paging/v3-transform#handle-separators-ui)
  - [Loading state headers and footers](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#load-state-adapter)

**Known Issues**

- Paging 3 javadocs are not yet available. In the interim, please use the guides linked above or the Kotlin docs. ([b/158614050](https://issuetracker.google.com/issues/158614050))

## Version 2.1.2

### Version 2.1.2

March 18, 2020

`androidx.paging:paging:2.1.2` is released. [Version 2.1.2 contains these commits *against 2.1.0*](https://android.googlesource.com/platform/frameworks/support/+log/ccb8e324ee105f23ea5d97e683a853330f236203..f4786c969d8bdf214a797bc7ef09f05037fdea58/paging).

**Bug Fixes**

- Fix for `IndexOutOfBoundsException` in rare cases when converting a position during invalidation.

**Release issue**

- Paging version `2.1.1` was released incorrectly from a misconfigured branch, exposing partially-implemented APIs and functionality upcoming in a future release.

- Paging `2.1.2` contains the load-centering fix originally released in 2.1.1, but this time correctly cherry-picked atop the 2.1.0 release. It is strongly recommended to upgrade to this release, if you are currently on 2.1.1.

## Version 2.1.1

| **Caution:** This version (`2.1.1`) contains unintentionally added methods, which can cause a build or runtime failure. Please update to the latest version (`2.1.2`), in which this issue has been fixed.

### Version 2.1.1

December 18, 2019

`androidx.paging:paging-*:2.1.1` is released. [Version 2.1.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/237c8946756af4b0fe9d0fa3965593e247d53698..5cad5782a1610dc724e2715c93c349e95828981e/paging).

**Bug fixes**

- Contiguous initial loads from PositionalDataSources are now centered around last access when placeholders disabled

## Version 2.1.0

### Version 2.1.0

January 25, 2019

Paging `2.1.0` is released with no changes from `2.1.0-rc01`.

### Version 2.1.0-rc01

December 6, 2018

Paging `2.1.0-rc01` is released with no changes from `2.1.0-beta01`.

### Version 2.1.0-beta01

November 1, 2018

Paging `2.1.0-beta01` is released with no changes from `2.1.0-alpha01`.

### Version 2.1.0-alpha01

October 12, 2018

Paging `2.1.0-alpha01` has two major additions - page dropping, and KTX extension libraries for every artifact - as well as several other API changes and bugfixes.

**API Changes**

- Added `PagedList.Config.Builder.setMaxSize()` for limiting the number of loaded items in memory.
- Added `androidx.paging.Config()` as a Kotlin alternative for `PagedList.Config.Builder`
- Added `androidx.paging.PagedList()` as a Kotlin alternative for `PagedList.Builder`
- Added `DataSourceFactory.toLiveData()` as a Kotlin alternative for `LivePagedListBuilder`
- Added `DataSourceFactory.toObservable()` and `toFlowable()` as Kotlin alternatives for `RxPagedListBuilder`
- Added `AsyncPagedListDiffer.addPagedListListener()` for listening to when PagedList is swapped. [b/111698609](https://issuetracker.google.com/111698609)
- Added `PagedListAdapter.onCurrentListChanged()` variant that passes old and new list, deprecated previous variant.
- Added `PagedListAdapter/AsyncPagedListDiffer.submitList()` variants which take an additional callback that triggers if/when the pagedlist is displayed, after diffing. This allows you to synchronize a PagedList swap with other UI updates. [b/73781068](https://issuetracker.google.com/73781068)
- `PagedList.getLoadedCount()` added to let you know how many items are in memory. Note that the return value is always equal to `.size()` if placeholders are disabled.

**Bug Fixes**

- Fixed a race condition when diffing if lists are reused [b/111591017](https://issuetracker.google.com/111591017)
- `PagedList.loadAround()` now throws `IndexOutOfBoundsException` when index is invalid. Previously it could crash with an unclear other exception.
- Fixed a case where an extremely small initial load size together with unchanged data would result in no further loading [b/113122599](https://issuetracker.google.com/113122599)

| **Note:** page dropping is currently off by default - enable it with the new `PagedList.Config.Builder.setMaxSize()` API. To correctly support page dropping in a custom `ItemKeyedDataSource`, you must implement `loadBefore`.
| **Note:** Page dropping is not currently supported in `PageKeyedDataSource`, due to having no way to re-load the `loadInitial` result incrementally.

## Version 2.0.0

### Version 2.0.0

October 1, 2018

Paging `2.0.0` is released with a single bugfix.

**Bug Fixes**

- Fixed a crash that could occur with very fast scrolling using `PositionalDataSource` and placeholders [b/114635383](https://issuetracker.google.com/114635383).

### Version 2.0.0-beta01

July 2, 2018

**Bug Fixes**

- Fixed content disappearing in some prepend cases (placeholders disabled, PositionalDataSource) [b/80149146](https://issuetracker.google.com/issues/80149146)
- (Already released in `1.0.1`) Fixed crashes where `PagedListAdapter` and `AsyncPagedListDiffer` would fail to signal move events. [b/110711937](https://issuetracker.google.com/issues/110711937)

## Pre-AndroidX Dependencies

For the pre-AndroidX versions of Paging that follow, include these dependencies:

    dependencies {
        def paging_version = "1.0.0"

        implementation "android.arch.paging:runtime:$paging_version"

        // alternatively - without Android dependencies for testing
        testImplementation "android.arch.paging:common:$paging_version"

        // optional - RxJava support
        implementation "android.arch.paging:rxjava2:$paging_version"
    }

## Version 1.0.1

### Version 1.0.1

June 26, 2018

Paging `1.0.1` is released with a single bugfix in `runtime`. We highly recommend using `1.0.1` for stability. Paging RxJava2 `1.0.1` is also released, and is identical to `1.0.0-rc1`.

**Bug Fixes**

- Fixed crashes where `PagedListAdapter` and `AsyncPagedListDiffer` would fail to signal move events. [b/110711937](https://issuetracker.google.com/issues/110711937)

## RxJava2 Version 1.0.0

### RxJava2 Version 1.0.0-rc1

May 16, 2018

Paging RxJava2 `1.0.0-rc1` is moving to release candidate with no changes from the initial
alpha.

## Version 1.0.0

### Version 1.0.0-rc1

April 19, 2018
Paging Release Candidate

We **do not have** any more known issues or new features scheduled for the
Paging `1.0.0` release. Please upgrade your projects to use `1.0.0-rc1` and
help us battle test it so that we can ship a rock solid `1.0.0`.

There are no changes in this release, it is the same as `1.0.0-beta1`.

### Version 1.0.0-beta1

April 5, 2018

Paging will be in beta for a short time before progressing to release candidate.
We are not planning further API changes for `Paging 1.0`, and the bar for any API changes is very high.

Alpha RxJava2 support for Paging is released as a separate optional module (`android.arch.paging:rxjava2:1.0.0-alpha1`)
and will temporarily be versioned separately until it stabilizes.

This new library provides an RxJava2 alternative to `LivePagedListBuilder`, capable of constructing
`Observable`s and `Flowable`s, taking `Scheduler`s instead of `Executor`s:

### Kotlin

```kotlin
val pagedItems = RxPagedListBuilder(myDataSource, /* page size */ 50)
        .setFetchScheduler(myNetworkScheduler)
        .buildObservable()
```

### Java

```java
Observable<PagedList<Item>> pagedItems =
        RxPagedListBuilder(myDataSource, /* page size */ 50)
                .setFetchScheduler(myNetworkScheduler)
                .buildObservable();
```

**New Features**

- `RxPagedListBuilder` is added via the new `android.arch.paging:rxjava2` artifact.

**API Changes**

- API changes to clarify the role of executors in builders:

  - Renamed `setBackgroundThreadExecutor()` to `setFetchExecutor()` (in `PagedList.Builder` and `LivePagedListBuilder`)

  - Renamed `setMainThreadExecutor()` to `setNotifyExecutor()` (in `PagedList.Builder`).

- Fixed `PagedList.mCallbacks` member to be private.

**Bug Fixes**

- `LivePagedListBuilder` triggers initial `PagedList` load on the specified executor,
  instead of the Arch Components IO thread pool.

- Fixed invalidate behavior in internal `DataSource` wrappers (used to implement `DataSource.map`,
  as well as placeholder-disabled `PositionalDataSource` loading) [b/77237534](https://issuetracker.google.com/issues/77237534)

### Version 1.0.0-alpha7

March 21, 2018

Paging `1.0.0-alpha7` is released alongside Lifecycles `1.1.1`. As Paging alpha7 depends on the move of the `Function` class mentioned above, you will need to update your `lifecycle:runtime` dependency to `android.arch.lifecycle:runtime:1.1.1`.

Paging `alpha7` is planned to be the final release before Paging hits beta.

**API Changes**

- `DataSource.LoadParams` objects now have a public constructor and `DataSource.LoadCallback` objects are now abstract. This enables wrapping a `DataSource` or directly testing a `DataSource` with a mock callback. [b/72600421](https://issuetracker.google.com/issues/72600421)
- Mappers for DataSource and DataSource.Factory
  - `map(Function<IN,OUT>)` allows you to transform, wrap, or decorate results loaded by a `DataSource`.
  - `mapByPage(<List<IN>,List<OUT>>)` enables the same for batch processing (e.g. if items loaded from SQL need to additionally query a separate database, that can be done as a batch.)
- `PagedList#getDataSource()` is added as a convenience method [b/72611341](https://issuetracker.google.com/issues/72611341)
- All deprecated classes have been removed from the API, including the remains of `recyclerview.extensions` package, and the `LivePagedListProvider`.
- `DataSource.Factory` is changed from an interface to an abstract class to enable map functionality.

**Bug Fixes**

- Changed Builders to be final. [b/70848565](https://issuetracker.google.com/issues/70848565)
- Room `DataSource` implementation is now fixed to handle multi-table queries - this fix is contained within Room 1.1.0-beta1, see above.
- Fixed a bug where `BoundaryCallback.onItemAtEndLoaded` would not be invoked for `PositionalDataSource` if placeholders are enabled and the total size is an exact multiple of the page size.

### Version 1.0.0-alpha5

January 22, 2018

**Bug Fixes**

- Fix page loading when placeholders are disabled [b/70573345](https://issuetracker.google.com/issues/70573345)
- Additional logging for tracking down IllegalArgumentException bug [b/70360195](https://issuetracker.google.com/issues/70360195) (and speculative Room-side fix)
- Javadoc sample code fixes [b/70411933](https://issuetracker.google.com/issues/70411933), [b/71467637](https://issuetracker.google.com/issues/71467637)