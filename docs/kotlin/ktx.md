---
title: https://developer.android.com/kotlin/ktx
url: https://developer.android.com/kotlin/ktx
source: md.txt
---

> Documentation index: https://developer.android.com/kotlin/ktx/llms.txt

Android KTX was a set of Kotlin extension modules for Android Jetpack
libraries. Each module had a `-ktx` suffix, for example,
`androidx.core:core-ktx` or `androidx.fragment:fragment-ktx`. These modules
added extension functions, coroutine support, and other Kotlin features to the
base libraries.

The AndroidX libraries are Kotlin-first, and the KTX extensions are moving into
the base module of each library. For most libraries, the `-ktx` artifacts are
empty starting in the versions in
[Libraries with a stable release](https://developer.android.com/kotlin/ktx.md.txt#stable), and you don't need them.

## Remove KTX dependencies

To remove a KTX dependency for a library in
[Libraries with a stable release](https://developer.android.com/kotlin/ktx.md.txt#stable), follow these steps:

1. Find the library in the [Libraries with a stable release](https://developer.android.com/kotlin/ktx.md.txt#stable) table.
2. Make sure that your project uses the base artifact at the version in the table, or at a later version.
3. Replace the `-ktx` artifact with the base artifact listed in the table. For example, replace `androidx.fragment:fragment-ktx` with `androidx.fragment:fragment`, and replace `androidx.room:room-ktx` with `androidx.room:room-runtime`.

You don't need to change your code or imports. The extensions keep the same
package names.

## Libraries with a stable release

For these libraries, the base artifact includes the extensions in a stable
release. You can remove the `-ktx` dependency.

| KTX artifact | Base artifact | Empty starting in version |
|---|---|---|
| `androidx.activity:activity-ktx` | `androidx.activity:activity` | 1.9.0 |
| `androidx.collection:collection-ktx` | `androidx.collection:collection` | 1.3.0 |
| `androidx.core:core-ktx` | `androidx.core:core` | 1.19.0 |
| `androidx.fragment:fragment-ktx` | `androidx.fragment:fragment` | 1.9.0 |
| `androidx.lifecycle:lifecycle-livedata-ktx` | `androidx.lifecycle:lifecycle-livedata` | 2.7.0 |
| `androidx.lifecycle:lifecycle-livedata-core-ktx` | `androidx.lifecycle:lifecycle-livedata-core` | 2.8.0 |
| `androidx.lifecycle:lifecycle-reactivestreams-ktx` | `androidx.lifecycle:lifecycle-reactivestreams` | 2.6.0 |
| `androidx.lifecycle:lifecycle-runtime-ktx` | `androidx.lifecycle:lifecycle-runtime` | 2.8.0 |
| `androidx.lifecycle:lifecycle-viewmodel-ktx` | `androidx.lifecycle:lifecycle-viewmodel` | 2.8.0 |
| `androidx.navigation:navigation-common-ktx` | `androidx.navigation:navigation-common` | 2.4.0 |
| `androidx.navigation:navigation-fragment-ktx` | `androidx.navigation:navigation-fragment` | 2.4.0 |
| `androidx.navigation:navigation-runtime-ktx` | `androidx.navigation:navigation-runtime` | 2.4.0 |
| `androidx.navigation:navigation-ui-ktx` | `androidx.navigation:navigation-ui` | 2.4.0 |
| `androidx.paging:paging-common-ktx` | `androidx.paging:paging-common` | 3.0.0 |
| `androidx.paging:paging-runtime-ktx` | `androidx.paging:paging-runtime` | 3.0.0 |
| `androidx.paging:paging-rxjava2-ktx` | `androidx.paging:paging-rxjava2` | 3.0.0 |
| `androidx.palette:palette-ktx` | `androidx.palette:palette` | 1.1.0 |
| `androidx.room:room-ktx` | `androidx.room:room-runtime` | 2.7.0 |
| `androidx.savedstate:savedstate-ktx` | `androidx.savedstate:savedstate` | 1.3.0 |
| `androidx.sqlite:sqlite-ktx` | `androidx.sqlite:sqlite` | 2.7.0 |
| `androidx.tracing:tracing-ktx` | `androidx.tracing:tracing` | 1.3.0 |
| `androidx.work:work-runtime-ktx` | `androidx.work:work-runtime` | 2.9.0 |

## Libraries without a stable release

For these libraries, the base artifact doesn't include the KTX extensions in a
stable release. Keep the `-ktx` dependency until a stable release includes
them.

| KTX artifact | Base artifact |
|---|---|
| `androidx.concurrent:concurrent-futures-ktx` | `androidx.concurrent:concurrent-futures` |
| `androidx.dynamicanimation:dynamicanimation-ktx` | `androidx.dynamicanimation:dynamicanimation` |
| `androidx.preference:preference-ktx` | `androidx.preference:preference` |
| `androidx.transition:transition-ktx` | `androidx.transition:transition` |
| `androidx.wear.watchface:watchface-complications-data-source-ktx` | `androidx.wear.watchface:watchface-complications-data-source` |

## Libraries that don't move to a base module

The `androidx.appsearch:appsearch-ktx` artifact is empty in all versions. You
can remove it.

All public APIs in the `androidx.security:security-crypto` library are
deprecated, together with its KTX module. The KTX extensions don't move to the
base module. Remove the library from your project.