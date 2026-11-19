---
title: https://developer.android.com/jetpack/androidx/releases/appstate-statestore
url: https://developer.android.com/jetpack/androidx/releases/appstate-statestore
source: md.txt
---

> Documentation index: https://developer.android.com/jetpack/androidx/llms.txt

# Appstate Statestore

--

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| November 18, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/appstate-statestore.md.txt#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on appstate statestore, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.appstate.statestore:statestore:1.0.0-alpha03"
    implementation "androidx.appstate.statestore:statestore-datastore:1.0.0-alpha03"
    implementation "androidx.appstate.statestore:statestore-datastore-wasm:1.0.0-alpha03"
    implementation "androidx.appstate.statestore:statestore-wasm:1.0.0-alpha03"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.appstate.statestore:statestore:1.0.0-alpha03")
    implementation("androidx.appstate.statestore:statestore-datastore:1.0.0-alpha03")
    implementation("androidx.appstate.statestore:statestore-datastore-wasm:1.0.0-alpha03")
    implementation("androidx.appstate.statestore:statestore-wasm:1.0.0-alpha03")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2302751+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2302751&template=2430521)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha03

November 18, 2026

`androidx.appstate.statestore:statestore-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a021adf44194ae86e596ae25ca43d5e4e18f6926..6dce8f813f5a350c8a2bfe33665c2e1ff5eb55cb/appstate/statestore).

**API Changes**

- The `statestore-datastore` artifact is had added support for the following platforms: `desktop`, `linux`, `mac`, `ios`, `tvos`, `watchos`, `js`, and `wasmJs`. In order to enable this, instead of using reflection, `PersistToDataStore` is now generic in the persisted value type and requires the key to provide the name it is stored under and its `KSerializer`. ([I4cd8e](https://android-review.googlesource.com/#/q/I4cd8ec26c36964cd7bff5dd1ea01de7a0ef17553), [I03124](https://android-review.googlesource.com/#/q/I031246463c4e84a096eb93139fd98dfb003e9be7), [b/579492485](https://issuetracker.google.com/issues/579492485))

### Version 1.0.0-alpha02

November 04, 2026

`androidx.appstate.statestore:statestore-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9cd04314f915c133a8f6e109ed8fbbf2a82bf65..a021adf44194ae86e596ae25ca43d5e4e18f6926/appstate/statestore).

### Version 1.0.0-alpha01

October 28, 2026

`androidx.appstate.statestore:statestore-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56ca943f55b3d53ce513a0fa356fe8fe4c43fe9f/appstate/statestore).

**New Features**

[`AppState StateStore`](https://developer.android.com/reference/kotlin/androidx/appstate/statestore/package-summary.md.txt) is a new library built on the Compose runtime that acts as a wrapper to provide custom integrations. The `androidx.appstate.statestore` artifact provides the library APIs and it also comes with a `androidx.appstate.statestore:statestore-datastore` artifact for state persistence. Developers can use `StateStore` to hoist their snapshot state into their application layer and the datastore integration to persist that state.

    class MyApplication : Application() {
        val stateStore = StateStore()
        private val scope = CoroutineScope(SupervisorJob() + Dispatchers.Default)

        override fun onCreate() {
            super.onCreate()

            scope.launch {
                // Start the listener in a child coroutine so it doesn't block the outer scope
                launch {
                    try {
                        stateStore
                            .syncToDataStore(dataStoreFile("settings").absolutePath, this)
                    } catch (e: Exception) {
                        e.printStackTrace()
                    }
                }
            }
        }
    }