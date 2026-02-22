---
title: https://developer.android.com/topic/libraries/architecture/adding-components
url: https://developer.android.com/topic/libraries/architecture/adding-components
source: md.txt
---

[Issue Tracker](https://issuetracker.google.com/issues/new?component=197448&template=878802)

Report issues so we can fix bugs.

Before getting started, read the
[Guide to app architecture](https://developer.android.com/topic/architecture) for useful principles that
apply to all Android apps and for guidance on
using architecture components together.

Architecture components are available from Google's Maven repository. To use
them, add the repository to your project.

Open the `settings.gradle` file and add the `google()` repository:

### Groovy

```groovy
dependencyResolutionManagement {
   ...
    repositories {
        google()
        jcenter()
    }
}
```

### Kotlin

```kotlin
dependencyResolutionManagement {
    ...
    repositories {
        google()
        jcenter()
    }
}
```
| **Warning:** The JCenter repository is read-only, as of March 31, 2021. For more information, see [JCenter service update](https://developer.android.com/studio/build/jcenter-migration).

## Declare dependencies

Open the `build.gradle` file for your app or module and add the artifacts
that you need as dependencies. You can add dependencies for all architecture
components or choose a subset.

See the instructions for declaring dependencies for each architecture component in the release notes:

- [Futures (found in androidx.concurrent)](https://developer.android.com/jetpack/androidx/releases/concurrent)
- [Lifecycle (including ViewModel)](https://developer.android.com/jetpack/androidx/releases/lifecycle)
- [Navigation (including SafeArgs)](https://developer.android.com/jetpack/androidx/releases/navigation)
- [Paging](https://developer.android.com/jetpack/androidx/releases/paging)
- [Room](https://developer.android.com/jetpack/androidx/releases/room)
- [WorkManager](https://developer.android.com/jetpack/androidx/releases/work)

See [AndroidX releases](https://developer.android.com/jetpack/androidx/versions) for the most up-to-date
version numbers for each component.

For more information about the AndroidX refactor and how it affects these class
packages and module IDs, see [Migrate to AndroidX](https://developer.android.com/jetpack/androidx/migrate).

## Kotlin

Kotlin extension modules are supported for several AndroidX dependencies. These
modules have the suffix `-ktx` appended to their names. For example:

### Groovy

```groovy
implementation "androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version"
```

### Kotlin

```kotlin
implementation("androidx.lifecycle:lifecycle-viewmodel:$lifecycle_version")
```

becomes

### Groovy

```groovy
implementation "androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version"
```

### Kotlin

```kotlin
implementation("androidx.lifecycle:lifecycle-viewmodel-ktx:$lifecycle_version")
```

More information, including docs for Kotlin extensions, can be found in the
[KTX documentation](https://developer.android.com/kotlin/ktx).

**Note:** For Kotlin based apps, make sure you use
`kapt` instead of `annotationProcessor`. You should also
add the `kotlin-kapt` plugin.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [App Architecture: UI Layer - Get Started - Android Developers](https://developer.android.com/topic/libraries/data-binding/start)
- [Work with observable data objects](https://developer.android.com/topic/libraries/data-binding/observability)
- [Migrate from Kotlin synthetics to Jetpack view binding](https://developer.android.com/topic/libraries/view-binding/migration)