---
title: https://developer.android.com/jetpack/androidx/releases/appstate-transform
url: https://developer.android.com/jetpack/androidx/releases/appstate-transform
source: md.txt
---

# Appstate Transform

--

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| October 28, 2026 | - | - | - | [1.0.0-alpha01](https://developer.android.com/jetpack/androidx/releases/appstate-transform#1.0.0-alpha01) |

## Declaring dependencies

To add a dependency on appstate transform, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.appstate.transform:transform:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-android:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-desktop:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-iosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-iossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-js:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-linuxarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-linuxx64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-macosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-mingwx64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-android:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-desktop:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-iosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-iossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-js:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-linuxarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-linuxx64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-macosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-mingwx64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-tvosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-tvossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-wasm-js:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-watchosarm32:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-watchosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-watchosdevicearm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-testing-watchossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-tvosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-tvossimulatorarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-wasm-js:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-watchosarm32:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-watchosarm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-watchosdevicearm64:1.0.0-alpha01"
    implementation "androidx.appstate.transform:transform-watchossimulatorarm64:1.0.0-alpha01"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.appstate.transform:transform:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-android:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-desktop:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-iosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-iossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-js:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-linuxarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-linuxx64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-macosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-mingwx64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-android:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-desktop:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-iosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-iossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-js:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-linuxarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-linuxx64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-macosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-mingwx64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-tvosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-tvossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-wasm-js:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-watchosarm32:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-watchosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-watchosdevicearm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-testing-watchossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-tvosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-tvossimulatorarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-wasm-js:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-watchosarm32:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-watchosarm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-watchosdevicearm64:1.0.0-alpha01")
    implementation("androidx.appstate.transform:transform-watchossimulatorarm64:1.0.0-alpha01")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:2302904+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=2302904&template=2430547)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha01

October 28, 2026

`androidx.appstate.transform:transform-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56ca943f55b3d53ce513a0fa356fe8fe4c43fe9f/appstate/transform).

**New Features**

[`AppState Transform`](https://developer.android.com/reference/kotlin/androidx/appstate/transform/package-summary) is a new library built on the Compose runtime that allows for running a composition outside of your UI. The `androidx.appstate.transform:transform` artifact provides the library APIs and it also comes with a `androidx.appstate.transform:transform-testing` artifact for testing. Developers can use Transform to manage their composition anywhere within their app.

    // With helper function
    var sourceState by mutableStateOf(0)

    val state = transform(initialValue = 0, scope = myCoroutineScope) {
        // any time this state changes, this lambda will update
        sourceState
    }

    // With TransformScope directly
    val transformScope = TransformScope()

    var sourceState by mutableStateOf(0)
    val state = transformScope.launchTransform(initialValue = 0) {
        // any time this state changes, this lambda will update
        sourceState
    }

    myCoroutineScope.launch {
        try {
            transformScope.run()
        } finally {
            state.dispose()
        }
    }

    // In test with the new transformTest API
    @Test
    fun testStateUpdate() = transformTest {
        var sourceState by mutableStateOf(0)
        val state = transform(
            initialValue = 0, scope = backgroundScope, dispatcher = testDispatcher
        ) {
            sourceState
        }

        assertThat(state.value).isEqualTo(0)

        sourceState = 1
        advance()

        assertThat(state.value).isEqualTo(1)
    }