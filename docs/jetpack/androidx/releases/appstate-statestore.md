---
title: https://developer.android.com/jetpack/androidx/releases/appstate-statestore
url: https://developer.android.com/jetpack/androidx/releases/appstate-statestore
source: md.txt
---

# Appstate Statestore

--

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 28, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/appstate-statestore#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on appstate statestore, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.appstate.statestore:statestore:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-android:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-datastore:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-datastore-android:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-desktop:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-iosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-iossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-js:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-linuxarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-linuxx64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-macosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-mingwx64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-tvosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-tvossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-wasm-js:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-watchosarm32:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-watchosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-watchosdevicearm64:1.0.0-alpha01"
    implementation "androidx.appstate.statestore:statestore-watchossimulatorarm64:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.appstate.statestore:statestore:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-android:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-datastore:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-datastore-android:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-desktop:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-iosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-iossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-js:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-linuxarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-linuxx64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-macosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-mingwx64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-tvosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-tvossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-wasm-js:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-watchosarm32:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-watchosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-watchosdevicearm64:1.0.0-alpha01")
    implementation("androidx.appstate.statestore:statestore-watchossimulatorarm64:1.0.0-alpha01")
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

### Version 1.0.0-alpha01

October 28, 2026

`androidx.appstate.statestore:statestore-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56ca943f55b3d53ce513a0fa356fe8fe4c43fe9f/appstate/statestore).

**New Features**

[`AppState StateStore`](https://developer.android.com/reference/kotlin/androidx/appstate/statestore/package-summary) is a new library built on the Compose runtime that acts as a wrapper to provide custom integrations. The `androidx.appstate.statestore` artifact provides the library APIs and it also comes with a `androidx.appstate.statestore:statestore-datastore` artifact for state persistence. Developers can use `StateStore` to hoist their snapshot state into their application layer and the datastore integration to persist that state.

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