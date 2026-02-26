---
title: https://developer.android.com/jetpack/androidx/releases/datastore
url: https://developer.android.com/jetpack/androidx/releases/datastore
source: md.txt
---

# DataStore

[User Guide](https://developer.android.com/datastore) [Codelab](https://codelabs.developers.google.com/codelabs/android-preferences-datastore) API Reference  
[androidx.datastore](https://developer.android.com/reference/kotlin/androidx/datastore/package-summary)   
Store data asynchronously, consistently, and transactionally, overcoming some of the drawbacks of SharedPreferences

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 25, 2026 | [1.2.0](https://developer.android.com/jetpack/androidx/releases/datastore#1.2.0) | - | - | [1.3.0-alpha06](https://developer.android.com/jetpack/androidx/releases/datastore#1.3.0-alpha06) |

## Declare dependencies

To add a dependency on DataStore, you must add the Google Maven repository to
your project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

DataStore provides [different options for serialization](https://developer.android.com/topic/libraries/architecture/datastore#implementations)
, choose one or the other. You can also add Android-free dependencies to either
implementation.

Add the dependencies for the implementation you need in the `build.gradle` file
for your app or module:

### Preferences DataStore

Add the following lines to the dependencies part of your gradle file:

### Groovy

```groovy
    dependencies {
        // Preferences DataStore (SharedPreferences like APIs)
        implementation "androidx.datastore:datastore-preferences:1.2.0"

        // Alternatively - without an Android dependency.
        implementation "androidx.datastore:datastore-preferences-core:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // Preferences DataStore (SharedPreferences like APIs)
        implementation("androidx.datastore:datastore-preferences:1.2.0")

        // Alternatively - without an Android dependency.
        implementation("androidx.datastore:datastore-preferences-core:1.2.0")
    }
    
```

To add optional RxJava support, add the following dependencies:

### Groovy

```groovy
    dependencies {
        // optional - RxJava2 support
        implementation "androidx.datastore:datastore-preferences-rxjava2:1.2.0"

        // optional - RxJava3 support
        implementation "androidx.datastore:datastore-preferences-rxjava3:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // optional - RxJava2 support
        implementation("androidx.datastore:datastore-preferences-rxjava2:1.2.0")

        // optional - RxJava3 support
        implementation("androidx.datastore:datastore-preferences-rxjava3:1.2.0")
    }
    
```

### DataStore

Add the following lines to the dependencies part of your gradle file:

### Groovy

```groovy
    dependencies {
        // Typed DataStore for custom data objects (for example, using Proto or JSON).
        implementation "androidx.datastore:datastore:1.2.0"

        // Alternatively - without an Android dependency.
        implementation "androidx.datastore:datastore-core:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // Typed DataStore for custom data objects (for example, using Proto or JSON).
        implementation("androidx.datastore:datastore:1.2.0")

        // Alternatively - without an Android dependency.
        implementation("androidx.datastore:datastore-core:1.2.0")
    }
    
```

Add the following optional dependencies for RxJava support:

### Groovy

```groovy
    dependencies {
        // optional - RxJava2 support
        implementation "androidx.datastore:datastore-rxjava2:1.2.0"

        // optional - RxJava3 support
        implementation "androidx.datastore:datastore-rxjava3:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // optional - RxJava2 support
        implementation("androidx.datastore:datastore-rxjava2:1.2.0")

        // optional - RxJava3 support
        implementation("androidx.datastore:datastore-rxjava3:1.2.0")
    }
    
```

To serialize content, add dependencies for either Protocol Buffers or JSON serialization.

#### JSON serialization

To use JSON serialization, add the following to your Gradle file:

### Groovy

```groovy
    plugins {
        id("org.jetbrains.kotlin.plugin.serialization") version "2.2.20"
    }

    dependencies {
        implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.9.0"
    }
    
```

### Kotlin

```kotlin
    plugins {
        id("org.jetbrains.kotlin.plugin.serialization") version "2.2.20"
    }

    dependencies {
        implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.9.0")
    }
    
```

#### Protobuf serialization

To use Protobuf serialization, add the following to your Gradle file:

### Groovy

```groovy
    plugins {
        id("com.google.protobuf") version "0.9.5"
    }
    dependencies {
        implementation "com.google.protobuf:protobuf-kotlin-lite:4.32.1"

    }

    protobuf {
        protoc {
            artifact = "com.google.protobuf:protoc:4.32.1"
        }
        generateProtoTasks {
            all().forEach { task ->
                task.builtins {
                    create("java") {
                        option("lite")
                    }
                    create("kotlin")
                }
            }
        }
    }
    
```

### Kotlin

```kotlin
    plugins {
        id("com.google.protobuf") version "0.9.5"
    }
    dependencies {
        implementation("com.google.protobuf:protobuf-kotlin-lite:4.32.1")
    }

    protobuf {
        protoc {
            artifact = "com.google.protobuf:protoc:4.32.1"
        }
        generateProtoTasks {
            all().forEach { task ->
                task.builtins {
                    create("java") {
                        option("lite")
                    }
                    create("kotlin")
                }
            }
        }
    }
    
```

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:907884+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=907884&template=1466542)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.3

### Version 1.3.0-alpha06

February 25, 2026

`androidx.datastore:datastore-*:1.3.0-alpha06` is released. Version 1.3.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c26c6f088b95903b7b9cd5e6f2092988f1e64dc3..c640b9aa8e30b5db9ee258561ad1fc4bc947e69d/datastore).

**New Features**

- `DataStore` now supports `androidx.tracing` on the Android target platform. You can create a `DataStore` with tracing by providing a `androidx.tracing.Tracer` instance to the `DataStoreFactory.createWithTracing()` function. ([I71bc2](https://android-review.googlesource.com/#/q/I71bc206a0b272b5a21d6695d62de0d2c916a5067), [b/427722902](https://issuetracker.google.com/issues/427722902))

### Version 1.3.0-alpha05

January 28, 2026

`androidx.datastore:datastore-*:1.3.0-alpha05` is released. Version 1.3.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad..b0ea337f3538c22dae2295d6a9265ab0c753e301/datastore).

**New Features**

- Baseline profiles added to datastore. ([3916245](https://android.googlesource.com/platform/frameworks/support/+/654945eb08b1ecc8c71165b7b7f0c194b16c86c4),[b/469127532](https://issuetracker.google.com/469127532)).
- Implement WASM/JS support in DataStore via `localStorage`. This creates a distinct advantage over the existing `sessionStorage` implementation by enabling cross-tab event notifications and synchronization. ([I67246](https://android-review.googlesource.com/#/q/I6724679fbb62d92acd1d7e8891e52f1dbfb2efed), [b/441511612](https://issuetracker.google.com/issues/441511612))

### Version 1.3.0-alpha04

January 14, 2026

`androidx.datastore:datastore-*:1.3.0-alpha04` is released. Version 1.3.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ec985eed3cba8444e5aaa52a748333397a1298f3..adeb519268e4eeff7d0a5a9d024dbe26d88bb6ad/datastore).

**API Changes**

- Added a utility copy function that can be used to update data for Preferences `DataStore`. ([I70a18](https://android-review.googlesource.com/#/q/I70a18b9795130a03f651703091e097d06318ff44), [b/467120382](https://issuetracker.google.com/issues/467120382))

**Bug Fixes**

- Resolved an issue where binary data could be malformed during storage by replacing UTF-8 string handling with Base64 encoding for Web. ([Ie3178](https://android-review.googlesource.com/#/q/Ie317819a0819ebf695547f5314505ddab3c22cb1), [b/473790107](https://issuetracker.google.com/473790107))

### Version 1.3.0-alpha03

December 17, 2025

`androidx.datastore:datastore-*:1.3.0-alpha03` is released. Version 1.3.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/deb96499dfe95073f5c1215c1287787683cb1e92..ec985eed3cba8444e5aaa52a748333397a1298f3/datastore).

**Bug Fixes**

- Fixed Issue with failing renaming of temp datastore file. ([I94f89](https://android-review.googlesource.com/#/q/I94f89debfd53d8c1d33e97a9725ed9884a1a2da2), [b/203087070](https://issuetracker.google.com/203087070))
- Fixed issue to prevent dropped updates during concurrent read/write. A race condition could occur between a new collector on `DataStore.data` and a concurrent `updateData` call, causing the collector to miss the new value. ([I6a427](https://android-review.googlesource.com/#/q/I6a427a4a359130eb8481f5a65852147a88d34bf4), [b/431787506](https://issuetracker.google.com/431787506))

### Version 1.3.0-alpha02

December 03, 2025

`androidx.datastore:datastore-*:1.3.0-alpha02` is released. Version 1.3.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fa8c4d8394173ca27d836045c97432e9b7462ecf..deb96499dfe95073f5c1215c1287787683cb1e92/datastore).

**Bug Fixes**

- Add js() target to `androidx.datastore`. ([I1f62b](https://android-review.googlesource.com/#/q/I1f62b86933b8a422f73500ed0e3ee8c5f944611b), [b/441511612](https://issuetracker.google.com/issues/441511612))
- Enforce FIFO ordering in `GuavaDataStore` updates. ([I6fd00](https://android-review.googlesource.com/#/q/I6fd003f9e3479a64c84c9acdf7ee21c2625fe82d),[b/451491257](https://issuetracker.google.com/issues/451491257))

### Version 1.3.0-alpha01

November 19, 2025

`androidx.datastore:datastore-*:1.3.0-alpha01` is released. Version 1.3.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/9c556fd714d249b153cbe3ddce61e9eb43f77ffc..fa8c4d8394173ca27d836045c97432e9b7462ecf/datastore).

**New Features**

- Added KMP Web support in `DataStore` by using the `sessionStorage` API. This feature allows `DataStore` to persist data temporarily within a single browser tab. ([I60fad](https://android.googlesource.com/platform/frameworks/support/+/3130f94ffea871b556a231bed86f331c1fd82643), [b/316376114](https://issuetracker.google.com/316376114))

## Version 1.2

### Version 1.2.0

November 19, 2025

`androidx.datastore:datastore-*:1.2.0` is released. Version 1.2.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/420da5f291449f11801e378c6789a328a06ec6cb..9c556fd714d249b153cbe3ddce61e9eb43f77ffc/datastore).

### Major changes since 1.1.0 release

**Java/Guava Support:**

- Added the new `datastore-guava` module to expose APIs friendly to Java and Guava `ListenableFuture` users via **`GuavaDataStore`**.
- Added **multiprocess support** within `GuavaDataStore`.
- Added an overload for `GuavaDataStore.from` that accepts a Java `Executor` (instead of a `CoroutineContext`) and uses `androidx.core.util.Function`.

**Direct Boot Support:**

- **DataStore usage during Direct Boot mode is now supported.** New APIs like **`createInDeviceProtectedStorage()`** in `DataStoreFactory` and **`deviceProtectedDataStore()`** in `DataStoreDelegate` allows creating the DataStore within the Device Protected storage.

**Storage and API Changes:**

- Added **`PreferencesFileSerializer`** that implements `androidx.datastore.core.Serializer` for use with `FileStorage`.
- Defined the default constructor for **`ReplaceFileCorruptionHandler`** for common code usage.

**Bug Fixes:**

- Fixed `java.lang.UnsatisfiedLinkError` when using `DataStore` in an app optimized with R8 but not using the standard ProGuard file.
- Fixed an issue where `GuavaDataStore` operations could incorrectly run on the calling thread (e.g., the main thread) instead of the specified IO dispatcher.
- Resolved a `FileNotFoundException` issue in `OkioStorage` at startup by adding a second attempt to read data in case of a race condition.

### Version 1.2.0-rc01

November 05, 2025

`androidx.datastore:datastore-*:1.2.0-rc01` is released. Version 1.2.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/86834fc8081b293eb0510226f68608d1688b9b99..ba855a7539de0ec6b32d3c2c3d3d90346f2bf854/datastore).

### Version 1.2.0-beta01

October 22, 2025

`androidx.datastore:datastore-*:1.2.0-beta01` is released. Version 1.2.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6c541571b9fb5471f965fc52612cb280713e5e4..86834fc8081b293eb0510226f68608d1688b9b99/datastore).

**API Changes**

- Make `CorruptionHandler` public. ([I9ac35](https://android-review.googlesource.com/#/q/I9ac35e246746353251965c34b8de3bb2a5ea09aa), [b/452406457](https://issuetracker.google.com/issues/452406457))
- Use `androidx.core.util.Function` in `GuavaDataStore`. ([I71eae](https://android-review.googlesource.com/#/q/I71eae3f48a2efe3cfaf8f2be93ec442296f6e4f1), [b/448563999](https://issuetracker.google.com/issues/448563999))
- Add an overload for `GuavaDataStore.from` that takes in an Executor instead of a `CoroutineContext`. ([I989fa](https://android-review.googlesource.com/#/q/I989fa6ac8ed8179c96371dd5ecfd3441f7729cc2), [b/448563183](https://issuetracker.google.com/issues/448563183))

**Bug Fixes**

- Fix `java.lang.UnsatisfiedLinkError` when using `DataStore` in an app which is optimized with R8, but which is not using `getDefaultProguardFile('android-proguard-optimize.txt')`. ([I27d0d](https://android-review.googlesource.com/#/q/I27d0dfeffe7956af04f8b49f8893d3edd38ac440), [b/434696293](https://issuetracker.google.com/issues/434696293))
- Fix issue where `GuavaDataStore` operations could incorrectly run on the calling thread (e.g., the main thread) instead of the specified IO dispatcher. ([Ic91ea](https://android-review.googlesource.com/#/q/Ic91eab1f61907b2c3d97bca18b43ce7c9d7658a3),[b/441801112](https://issuetracker.google.com/issues/441801112))

### Version 1.2.0-alpha02

May 7, 2025

`androidx.datastore:datastore-*:1.2.0-alpha02` is released. Version 1.2.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/78132378b67c86698d1ade3dc368c9f15d738a71..b6c541571b9fb5471f965fc52612cb280713e5e4/datastore).

**API Changes**

- Added multiprocess support in `GuavaDataStore`. ([e0d608a](https://android-review.googlesource.com/#/q/I3bf445555e5b30a3441d094456df7fe1c1bd603a)).
- Added a helper method to create a `GuavaDataStore` from a `DataStore`. ([9af26f4](https://android-review.googlesource.com/#/q/I4c8ac091e425d75bd3915e396861b3ad438ac661))
- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed. ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))
- Replace the existing `datastore` overload with a delegate method to initialize a DataStore to be used during direct boot. ([If71b9](https://android-review.googlesource.com/#/q/If71b98f6c88f4d1b213246cda67fe7c612f0e6e3))

### Version 1.2.0-alpha01

March 26, 2025

`androidx.datastore:datastore-*:1.2.0-alpha01` is released. Version 1.2.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6dd3f37a049d4541eb239be0f5cfe7fd4ed86bcb..78132378b67c86698d1ade3dc368c9f15d738a71/datastore).

**New Features**

- Added `datastore-guava` module to expose APIs friendly to Java and Guava `ListenableFuture` users via `GuavaDataStore`. ([Iadd5e0](https://android.googlesource.com/platform/frameworks/support/+/81dab615341b8a98792ad39eb65fc0fa4e34f957))
- `DataStore` usage during `DirectBoot` mode is now supported. To create a datastore to be used during direct boot mode it must be created within the Device Protected storage. This can be achieved by the following new `DataStore` APIs: `createInDeviceProtectedStorage()` in `DataStoreFactory` and `deviceProtectedDataStore()` in `DataStoreDelegate`. ([Ib90e56](https://android.googlesource.com/platform/frameworks/support/+/c68855c64e6a12a4b47d3082417b810f685a72c3))

**API Changes**

- Added `PreferencesFileSerializer` that implements `androidx.datastore.core.Serializer` interface for use with `FileStorage`. ([I4c71f3](https://android.googlesource.com/platform/frameworks/support/+/804dd3b895f87f886331a9b359137e99205f83ff))

**Bug Fixes**

- Resolved `FileNotFoundException` issue in `OkioStorage` at startup by adding a second attempt to read data in the case of a race condition. ([I43b3fb](https://android.googlesource.com/platform/frameworks/support/+/3e2cc72ab89a0c011f99627a61eba045d7378cb5), [b/337870543](https://issuetracker.google.com/issues/337870543))
- Defined the default constructor for `ReplaceFileCorruptionHandler` for common code usage. ([I795b05](https://android.googlesource.com/platform/frameworks/support/+/0f39d9164b42a309a9a9fdb89d8ec0f9ef4c9eb8), [b/358138957](https://issuetracker.google.com/issues/358138957))

## Version 1.1

### Version 1.1.7

May 20, 2025

`androidx.datastore:datastore-*:1.1.7` is released. Version 1.1.7 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/bc52f5ea6b0d7be1de1988026fc1f39325e2918b..420da5f291449f11801e378c6789a328a06ec6cb/datastore).

**Bug Fixes**

- Fixed missing Proguard rules issue in the Android artifact of `datastore-preferences-core`. ([3f3f6e](https://android-review.googlesource.com/#/q/3f3f6ecadb0f3beb755a27fb5859e238e81b7ea3), [b/413078297](https://issuetracker.google.com/issues/413078297))

### Version 1.1.6

May 7, 2025

`androidx.datastore:datastore-*:1.1.6` is released. Version 1.1.6 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/c866dad2ea6af9f78a490565a4cb399e0f140e4f..bc52f5ea6b0d7be1de1988026fc1f39325e2918b/datastore).

**Bug Fixes**

- Resolved an issue where Gradle metadata was broken in version `1.1.5`. This issue was caused by a bug in the new AGP KMP plugin DSL preventing metadata for all target platforms from being automatically included. The bug leads to some DataStore Android methods no longer visible in clients' builds. The fix involves using the older `android` DSL in `build.gradle` instead of `androidLibrary`. ([7801abf](https://android-review.googlesource.com/#/q/Id2587cd1459996399e879cdc905c692cf47bc4fd))

### Version 1.1.5

April 23, 2025

`androidx.datastore:datastore-*:1.1.5` is released. Version 1.1.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e36072d009624b67a11ffe8299467f21274d89a7..c45cbc1d347f5de69476fa21653b7031f10764e0/datastore).

**Bug Fixes**

- To mitigate `CorruptionException` issues in `PreferencesDataStore`, the default Storage has been changed from `OkioStorage`to `FileStorage`. This change was implemented by introducing a `PreferencesFileSerializer`. [b/346197747](https://issuetracker.google.com/issues/346197747)

### Version 1.1.4

March 26, 2025

`androidx.datastore:datastore-*:1.1.4` is released. Version 1.1.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ae63f655454c1548483e3f34d8f47d98ae21119b..e36072d009624b67a11ffe8299467f21274d89a7/datastore).

**Bug Fixes**

- Replace the default storage from `OkioStorage` to `FileStorage` to improve reliability by reducing `CorruptionException`. ([I71181](https://android.googlesource.com/platform/frameworks/support/+/47dd41dcf5aca9580dbd49144e2e347edb102e82), [b/346197747](https://issuetracker.google.com/issues/346197747))

### Version 1.1.3

February 26, 2025

`androidx.datastore:datastore-*:1.1.3` is released. Version 1.1.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/415f1db2f60935ab85e76f2e97fd213e4e5fcdd3..ae63f655454c1548483e3f34d8f47d98ae21119b/datastore).

**Bug Fixes**

- Resolved a `FileNotFoundException` issue in `OkioStorage` encountered at app startup. If the initial file read attempt is unsuccessful, a second attempt will be made in case a race condition has occurred due to the file being created by a different process during the initial read. ([I43b3f](https://android-review.googlesource.com/3496412), [b/337870543](https://issuetracker.google.com/issues/337870543))

### Version 1.1.2

January 15, 2025

`androidx.datastore:datastore-*:1.1.2` is released. Version 1.1.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/4e91af5f5597ac6275559f2ce4bc2f5cc852bddb..4f8f225b55d7d2d8d2a4469fb382881d1fe13064/datastore).

**Bug Fixes**

- Improve warm read latency (`DataStore.data.first()`) by 8x. ([22b8a40](https://android.googlesource.com/platform/frameworks/support/+/22b8a401e8867d1689f9fc0d2a696636fb2e6c74))
- `ReplaceFileCorruptionHandler` can be created from KMP common code. ([7632e839](https://android.googlesource.com/platform/frameworks/support/+/7632e839c505e4082378bfdd08979b25cb7a5035))

### Version 1.1.1

May 1, 2024

`androidx.datastore:datastore-*:1.1.1` is released. Version 1.1.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8cb4f17bcd16bd758f3d93838da28bb9294a0fbf..4e91af5f5597ac6275559f2ce4bc2f5cc852bddb/datastore).

**Bug Fixes**

- Mitigated Linux false alarm on "Resource deadlock would occur" error in a corner case multiple `DataStore` instances attempt to write from different processes by backing off the file lock.

### Version 1.1.0

April 17, 2024

`androidx.datastore:datastore-*:1.1.0` is released. Version 1.1.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/76cd793f15d1a1646b4ba892b9659379cdf1ee79..8cb4f17bcd16bd758f3d93838da28bb9294a0fbf/datastore).

**Major changes since 1.0.0 release**

Please review the release notes from alpha and beta versions of 1.1.0 for more info. Some of the major updates in 1.1.0 are:

- DataStore now supports multiple processes accessing the same file, with support for observability across processes.
- The new Storage interface allows you to customize how to store or serialize your data models.
- You can now use DataStore in Kotlin Multiplatform projects.

### Version 1.1.0-rc01

April 3, 2024

`androidx.datastore:datastore-*:1.1.0-rc01` is released. Version 1.1.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/638a8d3a474af45f6ad5fdc3d6d1836ea42d1778..76cd793f15d1a1646b4ba892b9659379cdf1ee79/datastore).

**Bug Fixes**

- Fixed the performance degradation where `updateData` calls didn't optimize on disk writes if the new data is the same as the old data ([d64cfb5](https://android.googlesource.com/platform/frameworks/support/+/d64cfb51b4243e341af8953f952681c20894206b))
- Fixed a race condition where `MultiProcess` `DataStore` might miss invalidations during initialization. (([b/326141553](https://issuetracker.google.com/issues/326141553)),([094c2dd](https://android.googlesource.com/platform/frameworks/support/+/094c2dd1ca5f267289b34187882b76b6fbde19af)))

### Version 1.1.0-beta02

March 6, 2024

`androidx.datastore:datastore-*:1.1.0-beta02` is released. Version 1.1.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/7a45f0bc9e0a73744b3780a6f92e1b570de58bba..638a8d3a474af45f6ad5fdc3d6d1836ea42d1778/datastore).

**Bug Fixes**

- Performance improvement on `DataStore` only collects update notifications when it is observed. ([b/267792241](https://issuetracker.google.com/267792241))
  - Note that this change might trigger `UncompletedCoroutinesError` in your tests if you are using the Coroutines testing library. Make sure you pass the [`TestScope.backgroundScope`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-test/kotlinx.coroutines.test/-test-scope/background-scope.html) when initializing `DataStore` in your tests to avoid this issue.
- Fixed the issue of nested `updateData` calls on the same instance would deadlock. ([b/241760537](https://issuetracker.google.com/issues/241760537))
- Made `DataStore` no longer throw `IOExceptions` if it fails to delete `SharedPreferences` during migration. ([b/195553816](https://issuetracker.google.com/issues/195553816))
- Fixed the issue where file rename fails during `updateData` in non-Android JVM environments. ([b/203087070](https://issuetracker.google.com/issues/203087070))
- Fixed the issue where `CorruptionException` is not handled after `DataStore` initialization. ([b/289582516](https://issuetracker.google.com/289582516))

### Version 1.1.0-beta01

January 10, 2024

`androidx.datastore:datastore-*:1.1.0-beta01` is released with no changes since `1.1.0-alpha07`. [Version 1.1.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..7a45f0bc9e0a73744b3780a6f92e1b570de58bba/datastore)

### Version 1.1.0-alpha07

November 29, 2023

`androidx.datastore:datastore-*:1.1.0-alpha07` is released. [Version 1.1.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e3ffd7948030a769c857b8c629e0079c54b730ad..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/datastore)

**API Changes**

- `MultiProcessDataStoreFactory` methods are no longer experimental.The `@ExperimentalMultiProcessDataStore` annotation has been removed entirely. ([Ieee54](https://android-review.googlesource.com/#/q/Ieee5497537562d4c3ac820b5dff626e983d0e518), [I8e607](https://android-review.googlesource.com/#/q/I8e607f110ab184396237972dd479cea82ebeb412))

**Bug Fixes**

- Rollout the removal of `@ExperimentalMultiProcessDataStore` annotations to 1.1.0-alpha07. ([I8e607](https://android-review.googlesource.com/#/q/I8e607f110ab184396237972dd479cea82ebeb412))

### Version 1.1.0-alpha06

November 1, 2023

`androidx.datastore:datastore-*:1.1.0-alpha06` is released. [Version 1.1.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9ce75ea1baa2af10dda8f787f69c40c6654bcac1..e3ffd7948030a769c857b8c629e0079c54b730ad/datastore)

**API Changes**

- `createSingleProcessCoordinator` factory method now receives a file path (`String`, `java.io.File` and `okio.Path`) to be consistent with `createMultiProcessCoordinator`. ([I211c8](https://android-review.googlesource.com/#/q/I211c8a55215607234554eff7127ef9bdf270984a), [b/305755935](https://issuetracker.google.com/issues/305755935))

### Version 1.1.0-alpha05

September 6, 2023

`androidx.datastore:datastore-*:1.1.0-alpha05` is released. [Version 1.1.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/a200cb82769634cecdb118ec4f0bfdf0b086e597..9ce75ea1baa2af10dda8f787f69c40c6654bcac1/datastore)

**API Changes**

- Datastore `FileStorage` is publicly available now, so clients can provide custom params. ([Icb985](https://android-review.googlesource.com/#/q/Icb98587682dd309b6a80eb352c76126cbd3b3740))
- Changed `OkioStorage` constructor to accept an `InterProcessCoordinator` so that it can be used on Android with `MultiProcessCoordinator`. ([Iecea3](https://android-review.googlesource.com/#/q/Iecea30cb3ce9677d5a9e9011fa3100d9672e2d1f))

**Bug Fixes**

- Fix `MultiProcessCoordinator` unable to monitor multiple files in the same directory.
- Fix unable to detect duplicate files if file paths are not normalized.
- Fix wrong values returned from `RxDataStore#isDisposed`.
- Fix missing proguard configuration for `datstore-preferences-core` artifact.

### Version 1.1.0-alpha04

April 5, 2023

`androidx.datastore:datastore-*:1.1.0-alpha04` is released. [Version 1.1.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22b70bebd89f109ec8a21cb84c21f37240124cfd..a200cb82769634cecdb118ec4f0bfdf0b086e597/datastore)

**Bug Fixes**

- Improve internal implementation to avoid a race condition where `DataStore`'s data flow might emit an older value after an update.

### Version 1.1.0-alpha03

March 24, 2023

`androidx.datastore:datastore-*:1.1.0-alpha03` is released.

**Bug Fixes**

- Removed dependency constraints from Maven artifacts to workaround a build problem in Kotlin Native Targets ([b/274786186](https://issuetracker.google.com/issues/274786186), [KT-57531](https://youtrack.jetbrains.com/issue/KT-57531)).

### Version 1.1.0-alpha02

March 22, 2023

`androidx.datastore:datastore-*:1.1.0-alpha02` is released. [Version 1.1.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cebbd6df05e83f6381aa710c63b17e764b5d7cf0..5e7d256f82fbafb6d059ab7b18fddd87c7531553/datastore)

**Note**

Note that this version includes an important internal refactor that merges the implementations for single process and multi process DataStore implementations. Please keep an eye on possible unintended behavior changes (e.g. timing of update notifications). You can use the issue tracker component to report such changes.

**New Features**

- You can now use `DataStore` in [KMM](https://kotlinlang.org/docs/multiplatform-mobile-getting-started.html) projects. Note that non-Android targets of DataStore are still experimental but we decided to merge versions to make it easier for developers to try them.
- Multi process features are moved from `androidx.datastore.multiprocess` to `androidx.datastore.core`.
- Add a new factory method in `androidx.datastore.core.MultiProcessDataStoreFactory` to create DataStore instances with `Storage` objects for file operations.
- Add a new interface `InterProcessCoordinator` that helps multiple DataStore instances communicate across processes. Note that, Multi-Process implementation of `InterProcessCoordinator` is only available on Android.

**API Changes**

- Add `InterProcessCoordinator` to `StorageConnection` in datastore-core interface ([I555bb](https://android-review.googlesource.com/#/q/I555bb258ac460b29b7a5d638957d861cf13e4d21))
- Change APIs in datastore-core `MultiProcessDataStoreFactory` to use Storage. ([Iac02f](https://android-review.googlesource.com/#/q/Iac02f50e9334d4fb384238f9447208598441b8ab))
- Move public APIs in datastore-multiprocess to datastore-core ([I76d7c](https://android-review.googlesource.com/#/q/I76d7cc8b230fc408511fe8799de9a0236c1bde43))
- Exposed `PreferencesSerializer` from datastore-preferences-core ([I4b788](https://android-review.googlesource.com/#/q/I4b78858d19f5000c6cc9bb293b1a055bf25293a2))
- Adding `@JvmDefaultWithCompatibility` annotation ([I8f206](https://android-review.googlesource.com/#/q/I8f2067bb0754a5e9dc70c934403366ca8d319c36))

### Version 1.1.0-alpha01

November 9, 2022

`androidx.datastore:datastore-*:1.1.0-alpha01` is released. [Version 1.1.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d2c1a0a27fe7c836c532f8eeae4c514c6f7ea2b4..a1e318590b217ecfce1b2de17eed2f18b6a680bb/datastore)

**New Features**

- Support multi-process use cases where data consistency is guaranteed among `DataStore` instances across processes. Add `MultiProcessDataStoreFactory#create` to create such `DataStore` instances.
- New Storage interface which allows the underlying storage mechanism for `Datastore` to be switched out. Implementations for java.io and okio are provided. `DataStore` factories have new methods which accept this Storage object.

**API Changes**

- Change APIs in datastore-core `MultiProcessDataStoreFactory` to use Storage. ([Iac02f](https://android-review.googlesource.com/#/q/Iac02f50e9334d4fb384238f9447208598441b8ab))
- Move public APIs in datastore-multiprocess to datastore-core ([I76d7c](https://android-review.googlesource.com/#/q/I76d7cc8b230fc408511fe8799de9a0236c1bde43))
- Exposed `PreferencesSerializer` from datastore-preferences-core ([I4b788](https://android-review.googlesource.com/#/q/I4b78858d19f5000c6cc9bb293b1a055bf25293a2))

## Version 1.0.0

### Version 1.0.0

August 4, 2021

`androidx.datastore:datastore-*:1.0.0` is released. [Version 1.0.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/34b1eceb499a984d35a72b8eacbaacb4a5d781e9..1999f75936498263f82e18b8c21a2b7cc76a5eb2/datastore)

**Major features of 1.0.0**

Jetpack DataStore is a data storage solution that allows you to store key-value pairs or typed objects with protocol buffers. DataStore uses Kotlin coroutines and Flow to store data asynchronously, consistently, and transactionally.

### Version 1.0.0-rc02

July 21, 2021

`androidx.datastore:datastore-*:1.0.0-rc02` is released. [Version 1.0.0-rc02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d820781c3ac6a7414042bafed5ca02affaca48a2..34b1eceb499a984d35a72b8eacbaacb4a5d781e9/datastore)

**Bug Fixes**

- Clarify that `SharedPreferencesMigration` does not run if there are no keys. ([Icfa32](https://android-review.googlesource.com/#/q/Icfa327c72834bab2a53be8f3696f48c19781c93f), [b/192824325](https://issuetracker.google.com/issues/192824325))
- Fix bug where `SharedPreferencesMigration` constructed with `MIGRATE_ALL_KEYS` would throw an exception if the key requested does not yet exist. ([Ie318a](https://android-review.googlesource.com/#/q/Ie318a9eb3772f5ef6dd231c18837842b887587e0), [b/192824325](https://issuetracker.google.com/issues/192824325))

### Version 1.0.0-rc01

June 30, 2021

`androidx.datastore:datastore-*:1.0.0-rc01` is released. [Version 1.0.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..d820781c3ac6a7414042bafed5ca02affaca48a2/datastore)

**Bug Fixes**

- Fixes bug where .java file was inadvertently added into final jar ([I65d96](https://android-review.googlesource.com/#/q/I65d96f778bd70d47d0ca6f6516efc8f39619a8f6), [b/188985637](https://issuetracker.google.com/issues/188985637))

### Version 1.0.0-beta02

June 16, 2021

`androidx.datastore:datastore-*:1.0.0-beta02` is released. [Version 1.0.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e..ccf79f53033e665475116a4e78ff124df2a52c4b/datastore)

**Bug Fixes**

- Fix `ClassVerificationFailure` ([b/187450483](https://issuetracker.google.com/issues/187450483))

### Version 1.0.0-beta01

April 21, 2021

`androidx.datastore:datastore-*:1.0.0-beta01` is released. [Version 1.0.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/52fbd7ed5b07ca4431fa828325a1f8da45b02e51..b04f2c39ebb45a0480dc0dc04d7fb7406646eb5e/datastore)

**API Changes**

- Remove JVM overloads for kotlin only methods ([I2adc7](https://android-review.googlesource.com/#/q/I2adc7f3420595e0308e087bcac353fec6f5cda30))

**Bug Fixes**

- Fixed a bug where datastore delegates could result in leaking contexts ([Ie96fc](https://android-review.googlesource.com/#/q/Ie96fc0933d653d1292d44f7ba7005a0319585881), [b/184415662](https://issuetracker.google.com/issues/184415662))

### Version 1.0.0-alpha08

March 10, 2021

`androidx.datastore:datastore-*:1.0.0-alpha08` is released. [Version 1.0.0-alpha08 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5c90131a69042a6a3e13952e1da9e7ffc571c31d..52fbd7ed5b07ca4431fa828325a1f8da45b02e51/datastore)

**API Changes**

- You can now add a migration that depends on context to your `dataStore` and `preferencesDataStore` property delegate. ([I4ef69](https://android-review.googlesource.com/#/q/I4ef69b0eed544cde4f05cdee9e885d36af0f4abb), [b/173726702](https://issuetracker.google.com/issues/173726702))
- Adds helper functions to get the name of the file if you are no longer using datastore delegate or context.createDataStore ([I60f9a](https://android-review.googlesource.com/#/q/I60f9a28df922ca7a730152cc4f83c2117e48d06a))
- Serializer writeTo and readFrom are now suspending. If you have implemented a Serializer, you will need to update your functions to be suspend functions. ([I1e58e](https://android-review.googlesource.com/#/q/I1e58eaa9a6c0653e5da461deecc35113a6e1d1ed))
- Added property delegates for RxDataStore users. ([Ied768](https://android-review.googlesource.com/#/q/Ied7680e698bc98b385b4bb4f33b6481963e7589a), [b/173726702](https://issuetracker.google.com/issues/173726702))

**Bug Fixes**

- Enforce restrictions on public usage of experimental APIs ([I6aa29](https://android-review.googlesource.com/#/q/I6aa29518ed4d6a3821d921d2ae1a300e31183dcc), [b/174531520](https://issuetracker.google.com/issues/174531520))

### Version 1.0.0-alpha07

February 24, 2021

`androidx.datastore:datastore-*:1.0.0-alpha07` is released. [Version 1.0.0-alpha07 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4d3f15273386f887bf6407b11dfa23460ee0164..5c90131a69042a6a3e13952e1da9e7ffc571c31d/datastore)

**API Changes**

- The `Context.createDataStore` extension function has been removed and replaced with globalDataStore property delegate. Call globalDataStore once at the top level in your kotlin file. For example:

      val Context.myDataStore by dataStore(...)

  Put this at the top level of your kotlin file so there is only one instance of it. ([I57215](https://android-review.googlesource.com/#/q/I5721591268086f2111719fcc48c4144c20b4e129), [b/173726702](https://issuetracker.google.com/issues/173726702))
- The RxDataStore functions are now on an RxDataStore class instead of extension functions on DataStore. ([Idccdb](https://android-review.googlesource.com/#/q/Idccdb6086e0fef2a76f0cf7c4577f56dab317107), [b/177691248](https://issuetracker.google.com/issues/177691248))

- If you want to migrate EncryptedSharedPreferences (or direct boot SharedPreferences) to DataStore you can now do that with the new SharedPreferencesMigration constructor that allows you to inject the SharedPreferences. ([I8e04e](https://android-review.googlesource.com/#/q/I8e04e9f3c62d41ba6bfeffe3e5978be4790b3661), [b/177278510](https://issuetracker.google.com/issues/177278510))

**Bug Fixes**

- DataStore will now throw an exception if there are multiple active DataStores for the same file. If you were not managing your DataStore as a Singleton or were not ensuring that no two instances of DataStore are simultaneously active for a file then you may now see exceptions when reading or writing to DataStore. These can be fixed by managing your DataStore as a Singleton. ([Ib43f4](https://android-review.googlesource.com/#/q/Ib43f4495f7741a3d480e0f6256e7bfee512c0d56), [b/177691248](https://issuetracker.google.com/issues/177691248))
- Fix cancellation behavior when caller scope is cancelled. ([I2c7b3](https://android-review.googlesource.com/#/q/I2c7b335c01cc2b59bea4474d676c4343ec90e596))

### Version 1.0.0-alpha06

January 13, 2021

`androidx.datastore:datastore-*:1.0.0-alpha06` is released. [Version 1.0.0-alpha06 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d4d3f15273386f887bf6407b11dfa23460ee0164/datastore)

**New Features**

- Added RxJava wrappers for DataStore. The `datastore-rxjava2/3` artifacts contain the wrappers for the core DataStore APIs (`RxDataStore`, `RxDataStoreBuilder`, and `RxDataMigration`). The `datastore-preferences-rxjava2/3` artifacts contain a builder to construct a Preferences DataStore.

**API Changes**

- Hide the CorruptionHandler interface. There was no reason for it to be public because the DataStore factory only accepts a ReplaceFileCorruptionHandler. ([I0b3b3](https://android-review.googlesource.com/#/q/I0b3b3c3aa47c6c7848bc1496371ad331ac571253), [b/176032264](https://issuetracker.google.com/issues/176032264))
- The `preferencesKey<T>(name: String): Key<T>` method has been removed and replaced with methods specific to each supported type, for example `preferencesKey<Int>("int")` is now `intPreferencesKey("int")` ([Ibcfac](https://android-review.googlesource.com/#/q/Ibcfac9cca7c8a3dbf2eaae17bdb8c22a8ce5a9f7), [b/170311106](https://issuetracker.google.com/issues/170311106))

**Bug Fixes**

- Fixes documentation on DataStoreFactory which left out the fact that the datastore file is created in the "datastore/" subdirectory. ([Ica222](https://android-review.googlesource.com/#/q/Ica222bbedb34f0bfc7169cce222f90c55bb6923c))

### Version 1.0.0-alpha05

December 2, 2020

`androidx.datastore:datastore-*:1.0.0-alpha05` is released. [Version 1.0.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/64e990c9cb237828482b8517567ab6d1ef4f177a..38a668d3ef95f40ad28d6e735a2c3eb95ae4cf63/datastore)

**Bug Fixes**

- Add better documentation and exceptions around concurrent writes from datastores. ([Ia98a2](https://android-review.googlesource.com/#/q/Ia98a2c42d9a43bab2af0672f52b8786fe854cdfd), [b/173522155](https://issuetracker.google.com/issues/173522155), [b/173726702](https://issuetracker.google.com/issues/173726702))
- We now allow (but don't require) the OutputStream passed to `Serializer.writeTo()` to be closed. ([I5c9bf](https://android-review.googlesource.com/#/q/I5c9bffd60bd12179a496e4589b010e31d00d8a5a), [b/173037611](https://issuetracker.google.com/issues/173037611))

### Version 1.0.0-alpha04

November 17, 2020

`androidx.datastore:datastore-*:1.0.0-alpha04` is released. [Version 1.0.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b..64e990c9cb237828482b8517567ab6d1ef4f177a/datastore)

**Bug Fixes**

- Fixed a packaging issue that causes the following crash in Preference Datastore `1.0.0-alpha03`: `java.lang.NoClassDefFoundError: Failed resolution of: Landroidx/datastore/preferences`
  - The crash was originally reported here: [b/173036843](https://issuetracker.google.com/issues/173036843)
  - ([I4712d](https://android-review.googlesource.com/#/q/I4712daf1343574f79ead8393079a84570a49b4bf), [b/173036843](https://issuetracker.google.com/issues/173036843))

### Version 1.0.0-alpha03

November 11, 2020

`androidx.datastore:datastore-*:1.0.0-alpha03` is released. [Version 1.0.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2d49f9fa892a0d067580a871f3aa0cd6764f4c3b/datastore)

> [!CAUTION]
> **Caution:** Please use version `1.0.0-alpha04` instead. A critical issue was found in `1.0.0-alpha03` that causes Preference Datastore to crash with `java.lang.NoClassDefFoundError`. ([b/173036843](https://issuetracker.google.com/issues/173036843))

**New Features**

- Preferences now supports double values (which is useful if you need more precision than floats) ([I5be8f](https://android-review.googlesource.com/#/q/I5be8f30e938e0ff6f2e699b51452c4eb8ffda031), [b/169471808](https://issuetracker.google.com/issues/169471808))

**API Changes**

- Created a pure kotlin dependency for datastore to allow for faster compilation. `androidx.datastore:datastore-core` contains the core kotlin only APIs and `androidx.datastore:datastore` contains the APIs that depend on android (including the `SharedPreferencesMigration` and the `Context.createDataStore` constructor.)([I42d75](https://android-review.googlesource.com/#/q/I42d75d0f66dc0cac19bd0f452a84b58806a65a46), [b/168512698](https://issuetracker.google.com/issues/168512698))
- Splitting out targets for preferences data store for faster kotlin compilation ([Ia3c19](https://android-review.googlesource.com/#/q/Ia3c19ddedcb622b751efc189ca20ce0ef684393a))
- Serializers now require a new property for the default value that will be used if there is no data on disk. This makes it easier to implement custom serializers so users do not have to special case empty input streams (empty input streams don't parse with json).

  - Also there is now a check to confirm that the output stream provided to writeTo() is not closed, and if it is closed it throws exceptions ([I16e29](https://android-review.googlesource.com/#/q/I16e2984b16cb387d8df55bad7a82a8120e94597a))
- Making the constructor for SharedPreferencesView internal. It was originally public to allow for testing. Tests should instead construct a SharedPreferencesMigration and test against that. ([I93891](https://android-review.googlesource.com/#/q/I938912884b2f088e70262fecc9c81a80795e1579))

**Bug Fixes**

- The `produceFile` parameter on `DataStoreFactory` and `PreferenceDataStoreFactory` is now the last parameter in the list so it lets you use the kotlin trailing lambda syntax. ([Ibe7f1](https://android-review.googlesource.com/#/q/Ibe7f1ef0d244dd22ad1513a66e79f228fd088469), [b/169425442](https://issuetracker.google.com/issues/169425442))
- Following the new explicit API requirements for kotlin ([I5ae1e](https://android-review.googlesource.com/#/q/I5ae1edbb2184cc9793a91f22457fe0c2864d61b5))

**Known Issues**

- Preference Datastore crashes with `java.lang.NoClassDefFoundError`. ([b/173036843](https://issuetracker.google.com/issues/173036843))

### Version 1.0.0-alpha02

October 14, 2020

`androidx.datastore:datastore-core:1.0.0-alpha02` and `androidx.datastore:datastore-preferences:1.0.0-alpha02` are released. [Version 1.0.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d..f413b8be76bfa0a4d109a3afb583188c580a2aa6/datastore)

**Bug Fixes**

- Added a safeguard against mutation in datastore-core. Mutation breaks datastore usage for people using datastore with non-proto/non-preferences types ([I6aa84](https://android-review.googlesource.com/#/q/I6aa84a2f158b5e368d8e0188ab41b6845c48151f))
- Added a `toString` method to Preferences.kt to make current state easy to debug ([I96006](https://android-review.googlesource.com/#/q/I96006139505f4026fe2e1ff2c04c3f3bc4218c44))
- Added an exception to safeguard against misuse of `DataStore.Preferences` ([I1134d](https://android-review.googlesource.com/#/q/I1134da8fecd588bfc4867368f57c40351ad7a109))
- Fixed a bug that would cause the app to crash on start up ([I69237](https://android-review.googlesource.com/#/q/I69237e3036c4863c3aa011cd88f363441ae5999f), [b/168580258](https://issuetracker.google.com/issues/168580258))

### Version 1.0.0-alpha01

September 2, 2020

`androidx.datastore:datastore-core:1.0.0-alpha01` and `androidx.datastore:datastore-preferences:1.0.0-alpha01` are released. [Version 1.0.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31022a2dda22705843be1199c786552a6f9f875d/datastore)

**New Features**

Jetpack DataStore is a new and improved data storage solution aimed at replacing SharedPreferences. Built on Kotlin coroutines and Flow, DataStore provides two different implementations:

- Proto DataStore, that lets you store typed objects (backed by [protocol buffers](https://developers.google.com/protocol-buffers))
- Preferences DataStore, that stores key-value pairs

Data is stored asynchronously, consistently, and transactionally, overcoming most of the drawbacks of SharedPreferences.