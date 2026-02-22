---
title: https://developer.android.com/jetpack/androidx/releases/collection
url: https://developer.android.com/jetpack/androidx/releases/collection
source: md.txt
---

# Collection

API Reference  
[androidx.collection](https://developer.android.com/reference/kotlin/androidx/collection/package-summary)  
Reduce the memory impact of existing and new collections that are small.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| February 11, 2026 | [1.5.0](https://developer.android.com/jetpack/androidx/releases/collection#1.5.0) | [1.6.0-rc01](https://developer.android.com/jetpack/androidx/releases/collection#1.6.0-rc01) | - | - |

## Declaring dependencies

To add a dependency on Collection, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    def collection_version = "1.5.0"
    implementation "androidx.collection:collection:$collection_version"
}
```

### Kotlin

```kotlin
dependencies {
    val collection_version = "1.5.0"
    implementation("androidx.collection:collection:$collection_version")
}
```

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:460756+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460756&template=1422573)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.6

### Version 1.6.0-rc01

February 11, 2026

`androidx.collection:collection-*:1.6.0-rc01` is released. Version 1.6.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56689f09bddc07bd2faa0f271c8eb917a4ebc4c7..a82c1e5e5dc308856c6f54ce28bd29ba21c81bf4/collection).

### Version 1.6.0-beta01

January 14, 2026

`androidx.collection:collection-*:1.6.0-beta01` is released. Version 1.6.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cd8ce2bdb21194a81a76325a8e65dad5d7e28681..56689f09bddc07bd2faa0f271c8eb917a4ebc4c7/collection).

**API Changes**

- Added `.toScatterSet()` and `.toScatterMap()` extensions. These provide a read-only alternative to the mutable conversion functions and return allocation-free singletons when the source collection is empty. ([I1769a](https://android-review.googlesource.com/#/q/I1769a123ac8dc55978808b1c3220605148fe69da), [b/459867876](https://issuetracker.google.com/issues/459867876))
- Replace the `MutableScatterMap(source)` and `MutableScatterSet(source)` pseudo-constructors with standard `.toMutableScatterMap()` and `.toMutableScatterSet()` extension functions. This aligns with Kotlin conventions for collection conversions. ([Ic9ca6](https://android-review.googlesource.com/#/q/Ic9ca625b616fa52e2294f8ac59dc8882e883018e), [b/459867876](https://issuetracker.google.com/issues/459867876))
- Add `MutableScatterMap(Map)` and `MutableScatterSet(Set)` factory functions. Use these functions to easily create a scatter collection pre-filled with the contents of an existing collection. ([I51d70](https://android-review.googlesource.com/#/q/I51d70d426606f4deeb2124ee5c51723915d4d3a0))

**Bug Fixes**

- This library now uses [JSpecify nullness annotations](https://jspecify.dev/), which are type-use. Kotlin developers should use the following compiler argument to enforce correct usage: `-Xjspecify-annotations=strict` (this is the default starting with version 2.1.0 of the Kotlin compiler) ([I05181](https://android-review.googlesource.com/#/q/I05181b94cb05ed6d35268673106faf6e6f18b219), [b/326456246](https://issuetracker.google.com/issues/326456246))

### Version 1.6.0-alpha01

August 27, 2025

`androidx.collection:collection-*:1.6.0-alpha01` is released. Version 1.6.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/fb376ee6d05727045f41e320bd36923eb385c5f8..cd8ce2bdb21194a81a76325a8e65dad5d7e28681/collection).

**API Changes**

- Projects released with Kotlin 2.0 require KGP 2.0.0 or newer to be consumed ([Idb6b5](https://android-review.googlesource.com/#/q/Idb6b5d6ae1625ab870ffe74f9790ffabc82a63b4))

**Bug Fixes**

- Previously `SparseArrayCompat` was returning `null` for valueAt and `keyAt` when passed an index that was within the allocated range, but outside the inserted range `0..size -1`. As documented, this behavior was never expected and outside the valid input range and this change fixes this behavior to instead throw `IndexOutOfBounds` when passed an invalid index. ([I68453](https://android-review.googlesource.com/#/q/I684530a49eec7ef915ad227b954a28f0d0913734))

**External Contribution**

Thanks Jake Wharton for the following contributions:

- Align `joinToString` behavior with platform collections by adding a separator before and the postfix after the truncation indicator when limiting included elements. ([I1b7e8](https://android-review.googlesource.com/#/q/I1b7e858a5b777b450dea7d77d8886427305dcce5))
- `ScatterSet.hashCode` no longer defends against recursion (i.e., the set being added to itself). This brings its behavior in line with `ScatterMap`, `HashSet`, and the primitive scatter-based sets (e.g., `LongSet`). Note that the `equals` method was already susceptible to recursion and `toString` defends against it---both behaviors which align with the other collections. ([I9c84a](https://android-review.googlesource.com/#/q/I9c84afff4c6844addd7b301000efbccc76176df0))
- `ScatterSet.retainAll` function is now inline to avoid creating a lambda instance. ([Ifa4b7](https://android-review.googlesource.com/#/q/Ifa4b73c85270bfdb7df99806d51aa2101f59a84a))
- `ScatterSet.hashCode` no longer uses its capacity in the hash calculation ensuring equal contents but different capacities still produce the same value. ([Ic863b](https://android-review.googlesource.com/#/q/Ic863be0ca47d572f075d2597b46e3131168b3111))
- `IllegalStateException` is now thrown if you call `remove()` before `next()` on an iterator of the `keys`, `values`, or `entries` collections of `ScatterMap.asMap()` or `ScatterSet.asSet()`. This brings its behavior into alignment with the regular map and set behavior. ([I71694](https://android-review.googlesource.com/#/q/I71694ce62de699e461336aa4e71b6059bbc91990))

## Version 1.5

### Version 1.5.0

March 12, 2025

`androidx.collection:collection-*:1.5.0` is released. Version 1.5.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6ef080d6bffda7b2687544a36d90f2919551581b..fb376ee6d05727045f41e320bd36923eb385c5f8/collection).

### Version 1.5.0-rc01

February 26, 2025

`androidx.collection:collection-*:1.5.0-rc01` is released. Version 1.5.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f383921582ae43bfe6fb2f11d71b8ace3f9ceb65..6ef080d6bffda7b2687544a36d90f2919551581b/collection).

### Version 1.5.0-beta03

January 29, 2025

`androidx.collection:collection-*:1.5.0-beta03` is released. Version 1.5.0-beta03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ad66672b42ec1e9359219e82b7f8189d03df40f5..f383921582ae43bfe6fb2f11d71b8ace3f9ceb65/collection).

### Version 1.5.0-beta02

January 15, 2025

`androidx.collection:collection-*:1.5.0-beta02` is released. Version 1.5.0-beta02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..ad66672b42ec1e9359219e82b7f8189d03df40f5/collection).

### Version 1.5.0-beta01

December 11, 2024

`androidx.collection:collection-*:1.5.0-beta01` is released. Version 1.5.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0aac1878823c58d5a7b1eee060cc79d1b38b4996..46295bc0b75a16f452e8e0090e8de41073d4dbb6/collection).

**API Changes**

- Adds support for `watchosDeviceArm64` KMP target and target kotlin 1.9 ([Icf15d](https://android-review.googlesource.com/#/q/Icf15d056ce2380ca3c733fb1a93fd502f60b40e4), [b/364652024](https://issuetracker.google.com/issues/364652024))

### Version 1.5.0-alpha06

November 13, 2024

`androidx.collection:collection-*:1.5.0-alpha06` is released. Version 1.5.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..0aac1878823c58d5a7b1eee060cc79d1b38b4996/collection).

**Bug Fixes**

- Fixed a crash that could occur in `SieveCache` and `OrderedScatterSet` when adding numerous items causing repeated key collisions. ([Iaaf3d](https://android-review.googlesource.com/#/q/Iaaf3d36d6adb491daf564d5625810446b6f5d321), [b/375607736](https://issuetracker.google.com/issues/375607736))
- Add wasm target to collection library. ([I66fe3](https://android-review.googlesource.com/#/q/I66fe3ee5593de47220bedcb59de18e9ec79b1105), [b/352722444](https://issuetracker.google.com/issues/352722444))

### Version 1.5.0-alpha05

October 30, 2024

`androidx.collection:collection-*:1.5.0-alpha05` is released. Version 1.5.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/collection).

### Version 1.5.0-alpha04

October 16, 2024

`androidx.collection:collection-*:1.5.0-alpha04` is released. Version 1.5.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/collection).

### Version 1.5.0-alpha03

October 2, 2024

`androidx.collection:collection-*:1.5.0-alpha03` is released. Version 1.5.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/collection).

**API Changes**

- Kotlin version update to 1.9 ([I1a14c](https://android-review.googlesource.com/#/q/I1a14ce236e70bdc55f94afd42ead44587018c097))

**External Contribution**

- Forward `contains` to `containsKey`. Thanks Jake Wharton! ([I9362b](https://android-review.googlesource.com/#/q/I9362b30782b97561d810b09e9746df96fac3625c))
- Add container builders for scalar-specialized collections. Thanks Jake Wharton! ([I13179](https://android-review.googlesource.com/#/q/I13179cbd2665dfbd1a1a1c97091df0e14954bb14))

### Version 1.5.0-alpha02

September 18, 2024

`androidx.collection:collection-*:1.5.0-alpha02` is released. Version 1.5.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0ef76d4ae53ed9530ce05734219a352a918baf83..0431b84980e97d6bafdfda7c9038bc4d9529564f/collection).

**API Changes**

- Adds support for `watchosDeviceArm64` platform target. ([I1cc04](https://android-review.googlesource.com/#/q/I1cc049dcca344226878d2f5a096e4ebb2e8bb5ac), [b/364652024](https://issuetracker.google.com/issues/364652024))

### Version 1.5.0-alpha01

September 4, 2024

`androidx.collection:collection-*:1.5.0-alpha01` is released. Version 1.5.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e3e748755ae0a4bd350b5e1f1f06ea40170528c0..f1a4862ceeaaa0161261ad24ea72a5430d3090d0/collection).

**API Changes**

- `OrderedScatterSet` is a new ordered, allocation-free collection ([Ic4178](https://android-review.googlesource.com/#/q/Ic417847247396583835d88abfb05b0af25224435))
- `SieveCache` is a new allocation-free replacement for `LruCache` that offers better hit ratio characteristics. ([I50a17](https://android-review.googlesource.com/#/q/I50a1740f9f58789c4b8ee0810f9bd92d9c1a9af4))
- Exposed the `packedValue` internal representation for `IntIntPair` and `FloatFloatPair`. ([Ifeb75](https://android-review.googlesource.com/#/q/Ifeb75cb8ea63d2b5c23d78640fd76bf81ec4f090), [b/331853566](https://issuetracker.google.com/issues/331853566))
- Adding access to the content array in list collections. ([I899d5](https://android-review.googlesource.com/#/q/I899d56ce4bc69e1a0be296995627ff9a8f3204cb), [b/333903173](https://issuetracker.google.com/issues/333903173))
- Add `DoubleList`, a List-like data structure optimized for Double values. ([Ia10d1](https://android-review.googlesource.com/#/q/Ia10d192b1c24132272e7b005c10fea2446c9f933), [b/315127635](https://issuetracker.google.com/issues/315127635))

**Bug Fixes**

- Collections library is moving to target Kotlin 1.9 ([I0782f](https://android-review.googlesource.com/#/q/I0782f09d014afa816a7844b97969deb5ecee8f85))
- Optimize many of the collections to be more efficient. ([Ic0566](https://android-review.googlesource.com/#/q/Ic0566fa291904feec9cd8e0fa2fd45ff13e61c32))

## Version 1.4

### Version 1.4.5

October 30, 2024

`androidx.collection:collection-*:1.4.5` is released. Version 1.4.5 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6d60ba37c125c305d09c6bc89b062a31fd913628..ebf5fdb40f911ff89a4355f3612288c152bb5fab/collection).

### Version 1.4.4

September 18, 2024

`androidx.collection:collection-*:1.4.4` is released. Version 1.4.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e3e748755ae0a4bd350b5e1f1f06ea40170528c0..6d60ba37c125c305d09c6bc89b062a31fd913628/collection).

**Bug Fixes**

- Workaround `ArrayIndexOutOfBounds` when sorting an empty collection. ([I65245](https://android-review.googlesource.com/#/q/I652455f6dae4eb470ebbd53723611d0401e5a158))

### Version 1.4.3

August 7, 2024

`androidx.collection:collection-*:1.4.3` is released. Version 1.4.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/62eff04974cadb45eee848ddb67ecd76c5fda38e..e3e748755ae0a4bd350b5e1f1f06ea40170528c0/collection).

**Bug Fixes**

- Fixed a corruption that could happen in `ScatterMap`, `ScatterSet`, and their primitive variants. ([I38a4a](https://android-review.googlesource.com/#/q/I38a4afee75595958594310a0ad14cca486997163), [b/352560465](https://issuetracker.google.com/issues/352560465))
- Performance optimizations. In particular:
  - Replace calls to `check()` and `required()` with variants that don't inline exception throws. This reduces the final binary size and more importantly relieves i-cache pressure a little bit.
  - Improved `removeDeletedMarkers()` in the "scatter" family of collections. The new version clears deleted markers 8 markers at a time and skips more expensive writes in the process. ([Ic0566](https://android-review.googlesource.com/#/q/Ic0566fa291904feec9cd8e0fa2fd45ff13e61c32))

### Version 1.4.2

July 24, 2024

`androidx.collection:collection-*:1.4.2` is released. Version 1.4.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/dba39e49c503b546475a23652716b80581e1c7b5..62eff04974cadb45eee848ddb67ecd76c5fda38e/collection).

**New Features**

- Includes additional Kotlin Multiplatform targets: `watchos`, `tvos`, `linuxArm64`. ([b/352543988](https://issuetracker.google.com/352543988))

### Version 1.4.1

July 10, 2024

`androidx.collection:collection-*:1.4.1` is released. Version 1.4.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6bb3d4c5410cf394070cca4ff347d46454194480..dba39e49c503b546475a23652716b80581e1c7b5/collection).

**Bug Fixes**

- Remove deleted tombstones from Map/Set when resizing. ([7a996c5](https://android-review.googlesource.com/#/q/Ic72352b3209e463de8de2278896a4b1bf10bd832), [b/345960092](https://issuetracker.google.com/issues/345960092))

### Version 1.4.0

January 24, 2024

`androidx.collection:collection-*:1.4.0` is released. [Version 1.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f75b95a5cd6354e397704b84c8d536e4f56831da..6bb3d4c5410cf394070cca4ff347d46454194480/collection)

**Important changes since 1.3.0**

New high-efficiency collections for storing primitives without boxing have been added:

- `MutableScatterMap` \& `ScatterMap` - Classes with `MutableMap` \& Map-like API
- `MutableScatterSet` \& `ScatterSet` - Classes with `MutableSet` \& Set-like API
- `MutableObjectList` \& `ObjectList` - Classes with `MutableList` \& List-like API

For example, a map with an integer key and a reference type value is an `IntObjectMap<T>`. A map with a long key and a float value is a `LongFloatMap`. There is no version with the name `ObjectObjectMap` because that is covered by `ScatterMap/MutableScatterMap`.

### Version 1.4.0-rc01

January 10, 2024

`androidx.collection:collection-*:1.4.0-rc01` is released with no changes. [Version 1.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b5166f9a1e9c047162d1215884c3e2cd41a4a74a..f75b95a5cd6354e397704b84c8d536e4f56831da/collection)

### Version 1.4.0-beta02

November 29, 2023

`androidx.collection:collection-*:1.4.0-beta02` is released. [Version 1.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/312eb9f1ddece3a18317f18515a877e0e745cb2c..b5166f9a1e9c047162d1215884c3e2cd41a4a74a/collection)

**New Features**

- Improved performance of `FloatFloatPair`. ([If5537](https://android-review.googlesource.com/#/q/If5537d58ae9248b558bfc1c63e4fdec4f343253c))

**Bug Fixes**

- `ScatterMap.asMap()` iterator now return new instances ([I28932](https://android-review.googlesource.com/#/q/I2893260c67fcbd3388c74043786c0329570ca5db), [b/310365754](https://issuetracker.google.com/issues/310365754))

### Version 1.4.0-beta01

November 15, 2023

`androidx.collection:collection-*:1.4.0-beta01` is released. [Version 1.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d01dc8c0d7a84bfca831a38146dccc49111668f2..312eb9f1ddece3a18317f18515a877e0e745cb2c/collection)

**Bug Fixes**

- Fix for `ListIterator` incorrectly setting values in `ObjectList` that could result in a crash due to `IndexOutOfBoundsException`. ([I3bd8a](https://android-review.googlesource.com/#/q/I3bd8a616a27c6537db32e6bcec22a69f093c8f37), [b/307049391](https://issuetracker.google.com/issues/307049391))

### Version 1.4.0-alpha02

October 18, 2023

`androidx.collection:collection-*:1.4.0-alpha02` is released. [Version 1.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b4a3474b543fec681c14700d322e9d2ed8f2cce6..d01dc8c0d7a84bfca831a38146dccc49111668f2/collection)

**API Changes**

- Added overload for `put` that returns the previous value when it is replaced to all primitive collections, such as `FloatFloatMap`.
- Convert `removeIf` methods on primitive collections, such as `MutableFloatFloatMap` to inline. This ensures that the lambda for `removeIf` is not allocated.

### Version 1.4.0-alpha01

October 4, 2023

`androidx.collection:collection-*:1.4.0-alpha01` is released. [Version 1.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b4a3474b543fec681c14700d322e9d2ed8f2cce6/collection)

**New Features**

New high-efficiency collections have been added that have low allocation overhead and high performance:

- `MutableScatterMap` \& `ScatterMap` - Classes with `MutableMap` \& Map-like API
- `MutableScatterSet` \& `ScatterSet` - Classes with `MutableSet` \& Set-like API
- `MutableObjectList` \& `ObjectList` - Classes with `MutableList` \& List-like API

New high-efficiency collections for storing primitives without boxing have been added:

- `Mutable[Int|Float|Long]List` - Classes with `MutableList<Int|Float|Long>`-like API. The read-only `[Int|Float|Long]List` also exists. For example, integers can be held in an `IntList`.
- `Mutable[Int|Float|Long]Set` - Classes with `MutableSet<Int|Float|Long>`-like API. The read-only `[Int|Float|Long]Set` also exists. For example, integers can be held in an IntSet.
- `Mutable[Int|Float|Long|Object][Int|Float|Long|Object]Map` - Classes with `Mutable<Int|Float|Long,T, Int|Float|Long|T>`-like API. The read-only `[Int|Float|Long|Object][Int|Float|Long|Object]Map` also exists. For example, a map with an integer key and a reference type value is an `IntObjectMap<T>`. A map with a long key and a float value is a `LongFloatMap`. There is no version with the name `ObjectObjectMap` because that is covered by `ScatterMap/MutableScatterMap`.

## Version 1.3.0

### Version 1.3.0

October 4, 2023

`androidx.collection:collection-*:1.3.0` is released. [Version 1.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/24829a8f5716a43f47e658c52d6b73778b337ed8..98434a2f2cbb050b244b18159ae23627c89c5bca/collection)

**Important changes since 1.2.0**

- You can now use Collections in Kotlin Multiplatform projects. Note that non-Android targets of Collections are still experimental, but we decided to merge versions to make it easier for developers to try them.
- All of the source has been migrated to Kotlin. As part of this change, many APIs are now properly typed for nullity and a few package private members have become `internal`. A list of exact changes are available in the minor release notes for 1.3.x below.
- Along with the Kotlin migration, `collection-ktx` has been merged with the main collection artifact. You can safely drop any dependencies on `collection:collection-ktx` in favor of `collection:collection` as `collection-ktx` is now empty.

### Version 1.3.0-rc01

September 6, 2023

`androidx.collection:collection-*:1.3.0-rc01` is released with no changes. [Version 1.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..24829a8f5716a43f47e658c52d6b73778b337ed8/collection)

### Version 1.3.0-beta01

August 9, 2023

`androidx.collection:collection-*:1.3.0-beta01` is released. [Version 1.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22b70bebd89f109ec8a21cb84c21f37240124cfd..5d7dd999525725bd038a00ca4e89e0fef624a6da/collection)

### Version 1.3.0-alpha04

March 24, 2023

`androidx.collection:collection-*:1.3.0-alpha04` is released.

**Bug Fixes**

- Removed dependency constraints from Maven artifacts to workaround a build problem in Kotlin Native Targets ([b/274786186](https://issuetracker.google.com/issues/274786186), [KT-57531](https://youtrack.jetbrains.com/issue/KT-57531)).

### Version 1.3.0-alpha03

March 22, 2023

`androidx.collection:collection-*:1.3.0-alpha03` is released. [Version 1.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/d2c1a0a27fe7c836c532f8eeae4c514c6f7ea2b4..8ded11092287e280a40fc35b7eede22664ac5641/collection)

**New Features**

- You can now use Collections in [KMM](https://kotlinlang.org/docs/multiplatform-mobile-getting-started.html) projects. Note that non-Android targets of Collections are still experimental but we decided to merge versions to make it easier for developers to try them.

**API Changes**

- `ArraySet` now implements `MutableCollections` instead of `AbstractMutableCollection` to allow for a more memory efficient implementation of `toArray` ([I1ac32](https://android-review.googlesource.com/#/q/I1ac32b09334619a2252805814dda21fba9ad3883))

**Bug Fixes**

- `ArraySet.toArray` is now only available on JVM as it was always only included for compatibility with Java. Kotlin users should generally use the stdlib's `.toTypedArray` helpers instead, which provides the exact same functionality with added type safety. ([I2c59b](https://android-review.googlesource.com/#/q/I2c59be76341e284936d6da16a3feb582d1f66c51))

### Version 1.3.0-alpha02

July 27, 2022

`androidx.collection:collection:1.3.0-alpha02` and `androidx.collection:collection-ktx:1.3.0-alpha02` are released. [Version 1.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/8094b683499b4098092c01028b55a38b49e357f2..a7f0710ad21f556f0dde9bf7bdab6d2135170fd4/collection)

**API Changes**

- `SparseArrayCompat` is now available to non-jvm platforms from the common artifact ([Ic9bd0](https://android-review.googlesource.com/#/q/Ic9bd08bed81ddc1d902fc9947d6b3f8e5bb4c45f), [b/219589118](https://issuetracker.google.com/issues/219589118), [b/228347315](https://issuetracker.google.com/issues/228347315))
- `CircularIntArray` is now available to non-jvm platforms from the common artifact ([I3d8ef](https://android-review.googlesource.com/#/q/I3d8ef18a8086fa706e45d6c53913c2a37268bd26), [b/228344943](https://issuetracker.google.com/issues/228344943))
- `LongSparseArray` is now available to non-jvm platforms from the common artifact ([I73149](https://android-review.googlesource.com/#/q/I73149c74661a556e1d8693ebd25f52fe64dca626), [b/228347315](https://issuetracker.google.com/issues/228347315))

### Version 1.3.0-alpha01

June 29, 2022

`androidx.collection:collection:1.3.0-alpha01` and `androidx.collection:collection-ktx:1.3.0-alpha01` are released. [Version 1.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/271a55ffaa9a85ba4f84c140c435906d088e79a0..8094b683499b4098092c01028b55a38b49e357f2/collection/collection)

**New Features**

- `collection-ktx` extensions have been migrated into the main collections artifact, `androidx.collection:collection`. This change makes the pre-existing -ktx extensions accessible to Kotlin users without requiring the -ktx dependency, while still maintaining compatibility for existing users. Maintaining these extensions in a separate -ktx artifact is no longer beneficial since the main artifact has moved to Kotlin. ([I6eef2](https://android-review.googlesource.com/#/q/I6eef28fa8fcb929df5979a29a869ca8aa0828215))

**API Changes**

- `ArraySet` now extends `AbstractMutableCollection` and no longer directly implements the Collection interface. ([If6da0](https://android-review.googlesource.com/#/q/If6da08d5a1a41257b0b79728796509e06efe9f35), [b/230860589](https://issuetracker.google.com/issues/230860589))
- Converted `ArraySet` to Kotlin. Due to stricter typing, some Kotlin calls may no longer compile. ([Id68c1](https://android-review.googlesource.com/#/q/Id68c130a8451c916c1e85b8a59c76ba267297cc4), [b/230860589](https://issuetracker.google.com/issues/230860589))
  - The following calls have the argument type `T`, not `T?`:
    - `ArraySet<T>.contains(null)`
    - `ArraySet<T>.add(null)`
    - `ArraySet<T>.remove(null)`
  - The following calls have the return type `T?`, not `T!`:
    - `ArraySet<T?>.valueAt(n)`
    - `ArraySet<T?>.removeAt(n)`
    - `ArraySet<T?>().iterator().next()`
  - The following calls are no longer possible from Kotlin:
    - `set.toArray()` - use `set.toTypedArray()`
    - `set.toArray(array)` - use `set.forEachIndexed(array::set)`
- Combine overloaded constructor for `SparseArrayCompat` as an optional argument for Kotlin users. ([If8407](https://android-review.googlesource.com/#/q/If8407a9111227e7e7fb960f4065af07b5fbc1d99), [b/227474719](https://issuetracker.google.com/issues/227474719))
- Remove operator syntax for `SparseArrayCompat.get(key, defaultValue).` Note this still allows operator syntax for `.get(key)`, but better aligns the API surface of `SparseArrayCompat` with the other classes in this library. ([I9a38d](https://android-review.googlesource.com/#/q/I9a38dbed9008f1280e14bf8f12df304de1293447))
- Migrate `LongSparseArray` extensions into the main artifact, androidx.collection:collection. This change makes the pre-existing -ktx extensions accessible to Kotlin users without requiring the -ktx dependency, while still maintaining compatibility for existing users. Maintaining these extensions in a separate -ktx artifact is no longer beneficial since the main artifact has moved to Kotlin. ([I8659a](https://android-review.googlesource.com/#/q/I8659ae3f23dd6c568b3a15f84cf1592ce7446774))
- Convert `LongSparseArray` to Kotlin. This change adds explicit nullity to its types, which is a binary compatible change, but may cause source incompatibilities. In particular: \* `.isEmpty` is no longer accessible as a property, it must be accessed as a function call in Kotlin - `.isEmpty()` ([Idfd0f](https://android-review.googlesource.com/#/q/Idfd0f4592fa5a708ba90b41f88d0600690aa2896))
- Convert `SimpleArrayMap` to Kotlin. This change introduces a few incompatible changes, as a result of Java-Kotlin interop and the ability to correctly define nullity of types in the source.
  - The package private APIs, `.mSize`, `.mArray`, `.mHashes`, `.indexOf()`, `.indexOfNull()`, and `.indexOfValue()`, were made private - this is technically a binary incompatible change, but reflects the intended visibility of these fields and is the closest we can achieve in Kotlin since it does not include a way to specify package-private visibility.
  - The nullity of some types are now properly defined, the affected methods are: `.getOrDefault`, `.keyAt`, `.valueAt`, `.setValueAt`, `.put`, `.putIfAbsent`, `.removeAt`, `.replace`.
  - For Kotlin users, `.isEmpty()` is now only available as a function instead of also through property access. ([I271b7](https://android-review.googlesource.com/#/q/I271b70587e94ef166be71c5b60d8c6361b4b1849), [b/182813986](https://issuetracker.google.com/issues/182813986))
- Convert `CircularArray` to Kotlin. Notable changes:

  - Corrects the nullity of its generics to be non-null, which was previously impossible to declare, but was enforced in all of its public APIs.
  - Due to Kotlin's Java interop, it was previously possible to access certain methods as both properties or functions. However, to reduce duplication while maintaining binary compatibility, it was necessary to remove these, which is a source-incompatible change. The affectedn calls are: `.isEmpty`, `.getLast()` and `.getFirst()`. ([Ifffac](https://android-review.googlesource.com/#/q/Ifffac44a13ca2bc4eb652728ef2c412dd0425f7e))
- Convert `CircularIntArray` to Kotlin. Due to Kotlin's Java interop, it was previously possible to access certain methods as both properties or functions. However, to reduce duplication while maintaining binary compatibility, it was necessary to remove these, which is a source-incompatible change. The affected calls are: `.isEmpty`, `.getLast()` and `.getFirst()`. ([Ie36ce](https://android-review.googlesource.com/#/q/Ie36ce80725187227e054177d5bbe07f76ed5462a))

- Convert `LruCache` to Kotlin ([Ia2f19](https://android-review.googlesource.com/#/q/Ia2f190fa5e262dbb30204ab2a74ae8b91587e2d9))

- Convert `SparseArrayCompat` to Kotlin. ([If6fe8](https://android-review.googlesource.com/#/q/If6fe8079f570d8e1a356c0d4a586d3c66d871d82))

  A small behavior change is added to `SparseArrayCompat.valueAt()`, which
  no longer incorrectly returns `null` for un-initialized calls out of
  bounds of `size()` but within the provided initial capacity.

  This change also introduces the correct nullity for some types which was
  previously missing.
  - `.get(): E?` -\> `.get(): E`
  - `.replace(Int, Int?): Int?` -\> `.replace(Int, Int): Int?`
  - `.replace(Int, Int?, Int?): Boolean` -\> `.replace(Int, Int, Int): Boolean`
  - `.put(Int, Int?)` -\> `.put(Int, Int)`
  - `.putIfAbsent(Int, Int?): Int?` -\> `.putIfAbsent(Int, Int): Int?`
  - `.setValueAt(index: Int, value: Int?)` -\> `.setValueAt(index: Int, value: Int)`
  - `.indexOfValue(value: Int?): Int` -\> `.indexOfValue(value: Int): Int`
  - `.containsValue(value: Int?): Boolean` -\> `.containsValue(value: Int): Boolean`
  - `.append(key: Int, value: Int?)` -\> `.append(key: Int, value: Int)`

## Version 1.2.0

### Version 1.2.0

December 1, 2021

`androidx.collection:collection:1.2.0` and `androidx.collection:collection-ktx:1.2.0` are released. [Version 1.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2bc1daaee7473641ca10a727847a1a884c17d1ae..271a55ffaa9a85ba4f84c140c435906d088e79a0/collection)

**Important changes since 1.1.0**

- Add an array constructor to `ArraySet`. ([Id7f19](https://android-review.googlesource.com/#/q/Id7f199478f1cb7a69ac056a69e4c87d24faa80a8))
- Make `entrySet()` API-compliant by implementing `entrySet().toArray()`, `remove()`, `removeAll()`, and `retainAll()`, and removing implementation of `entrySet().addAll()` ([I5d505](https://android-review.googlesource.com/#/q/I5d5059350c611de1e4cd7d83e8d3dad17a5ba00f))

### Version 1.2.0-rc01

November 17, 2021

`androidx.collection:collection:1.2.0-rc01` and `androidx.collection:collection-ktx:1.2.0-rc01` are released. [Version 1.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..2bc1daaee7473641ca10a727847a1a884c17d1ae/collection)

**API Changes**

- No changes from previous beta.

### Version 1.2.0-beta01

October 13, 2021

`androidx.collection:collection:1.2.0-beta01` and `androidx.collection:collection-ktx:1.2.0-beta01` are released. [Version 1.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd3c8e9c2424b78e44f55db599251891fd1cadb4..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/collection)

**Bug Fixes**

- Make `entrySet()` API-compliant by implementing `entrySet().toArray()`, `remove()`, `removeAll()`, and `retainAll()`, and removing implementation of `entrySet().addAll()` ([I5d505](https://android-review.googlesource.com/#/q/I5d5059350c611de1e4cd7d83e8d3dad17a5ba00f))

### Version 1.2.0-alpha01

December 16, 2020

`androidx.collection:collection:1.2.0-alpha01` and `androidx.collection:collection-ktx:1.2.0-alpha01` are released. [Version 1.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/895a032750ecd6ee03b76c4304023a1464df528f..dd3c8e9c2424b78e44f55db599251891fd1cadb4/collection)

**API Changes**

- Add an array constructor to `ArraySet`. ([Id7f19](https://android-review.googlesource.com/#/q/Id7f199478f1cb7a69ac056a69e4c87d24faa80a8))

## Version 1.1.0

### Version 1.1.0

June 5, 2019

`androidx.collection:collection:1.1.0` and `androidx.collection:collection-ktx:1.1.0` are released. The commits included 1.1.0 can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/cd5f909e9f35c63dbc7252a0d790de4a62c22b7e..2ee5d826c17d6b538469d85d92745ea43f1ec19e/collection).

**Below is a summary of changes from 1.0.0 to 1.1.0:**

**New features**

- Use more efficient implementation for `contains` and `isNotEmpty` functions in 'collection-ktx' artifact. ([aosp/866529](https://android-review.googlesource.com/c/platform/frameworks/support/+/866529))

**API changes**

- Add `putIfAbsent` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772608](https://android-review.googlesource.com/c/platform/frameworks/support/+/772608))
- Add `getOrDefault` to `SimpleArrayMap` ([aosp/772607](https://android-review.googlesource.com/c/platform/frameworks/support/+/772607))
- Add two-argument `remove` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat`. Deprecate corresponding KTX extensions for this functionality. ([aosp/772482](https://android-review.googlesource.com/c/platform/frameworks/support/+/772482))
- Add two-argument `replace` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772483](https://android-review.googlesource.com/c/platform/frameworks/support/+/772483))
- Add three-argument `replace` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772484](https://android-review.googlesource.com/c/platform/frameworks/support/+/772484))
- Deprecate redundant `delete` methods. The `remove` method offers the same API and functionality and matches the API used by non-specialized Maps. ([aosp/866053](https://r.android.com/866053))

**Bug fixes**

- Change `SimpleArrayMap` to synchronize its internal global cache of arrays on `SimpleArrayMap.class` instead of `ArrayMap.class`. This ensures that if you are only using `SimpleArrayMap`, `ArrayMap` can be removed by code shrinking tools. ([aosp/934557](https://android-review.googlesource.com/c/platform/frameworks/support/+/934557))

### Version 1.1.0-rc01

May 7, 2019

`androidx.collection:collection:1.1.0-rc01` and `androidx.collection:collection-ktx:1.1.0-rc01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/a81cba4406e40dfca7ba3c37e629537c4840de95..2ee5d826c17d6b538469d85d92745ea43f1ec19e/collection).

**New features**

- Use more efficient implementation for `contains` and `isNotEmpty` functions in 'collection-ktx' artifact. ([aosp/866529](https://android-review.googlesource.com/c/platform/frameworks/support/+/866529))

### Version 1.1.0-beta01

April 3, 2019

`androidx.collection:collection:1.1.0-beta01` and `androidx.collection:collection-ktx:1.1.0-beta01` are released. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/79285e90f077844e4b3b1a72a4a051389e3c190a..a81cba4406e40dfca7ba3c37e629537c4840de95/collection).

**API changes**

- The method mentioned in [the alpha03 release notes](https://developer.android.com/jetpack/androidx/releases/collection#1.0.0-alpha03) as having its `@RestrictTo` value changed has been removed. It was unused by any AndroidX library (now or historically) and it did not offer any functionality that was missing from the public API.

**Bug fixes**

- Change `SimpleArrayMap` to synchronize its internal global cache of arrays on `SimpleArrayMap.class` instead of `ArrayMap.class`. This ensures that if you are only using `SimpleArrayMap`, `ArrayMap` can be removed by code shrinking tools. ([aosp/934557](https://android-review.googlesource.com/c/platform/frameworks/support/+/934557))

### Version 1.1.0-alpha03

March 13, 2019

`androidx.collection:collection:1.0.0-alpha03` and
`androidx.collection:collection-ktx:1.0.0-alpha03` are released.
The full list of commits included in this version can be found
[here](https://android.googlesource.com/platform/frameworks/support/+log/9684a6ace257773f30f568e5559cb91b68113060..79285e90f077844e4b3b1a72a4a051389e3c190a/collection).

**API changes**

- A method on `ArraySet` previously marked `@RestrictTo(LIBRARY_GROUP)` was changed to `@RestrictTo(LIBRARY_GROUP_PREFIX)`. This is to support historical use by other AndroidX libraries which are now in different Maven group IDs. This method will either be made public or removed in 1.1.0-alpha04 because other AndroidX libraries should not get special APIs that other developers do not.

### Version 1.1.0-alpha02

January 30, 2019

`androidx.collection:collection 1.1.0-alpha02` and
`androidx.collection:collection-ktx 1.1.0-alpha02` are released.

**API changes**

- Deprecate redundant `delete` methods. The `remove` methods offers the same API and functionality and matches the API used by non-specialized Maps. ([aosp/866053](https://r.android.com/866053))

### Version 1.1.0-alpha01

December 3, 2018

**API changes**

- Add `putIfAbsent` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772608](https://android-review.googlesource.com/c/platform/frameworks/support/+/772608))
- Add `getOrDefault` to `SimpleArrayMap` ([aosp/772607](https://android-review.googlesource.com/c/platform/frameworks/support/+/772607))
- Add two-argument `remove` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat`. Deprecate corresponding KTX extensions for this functionality. ([aosp/772482](https://android-review.googlesource.com/c/platform/frameworks/support/+/772482))
- Add two-argument `replace` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772483](https://android-review.googlesource.com/c/platform/frameworks/support/+/772483))
- Add three-argument `replace` to `LongSparseArray`, `SimpleArrayMap`, and `SparseArrayCompat` ([aosp/772484](https://android-review.googlesource.com/c/platform/frameworks/support/+/772484))