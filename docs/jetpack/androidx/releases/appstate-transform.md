---
title: https://developer.android.com/jetpack/androidx/releases/appstate-transform
url: https://developer.android.com/jetpack/androidx/releases/appstate-transform
source: md.txt
---

> Documentation index: https://developer.android.com/jetpack/androidx/llms.txt

# Appstate Transform

--

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| November 18, 2026 | - | - | - | [1.0.0-alpha03](https://developer.android.com/jetpack/androidx/releases/appstate-transform.md.txt#1.0.0-alpha03) |

## Declaring dependencies

To add a dependency on appstate transform, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Groovy

```groovy
dependencies {
    implementation "androidx.appstate.transform:transform:1.0.0-alpha03"
    implementation "androidx.appstate.transform:transform-testing:1.0.0-alpha03"
    implementation "androidx.appstate.transform:transform-testing-wasm:1.0.0-alpha03"
    implementation "androidx.appstate.transform:transform-wasm:1.0.0-alpha03"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.appstate.transform:transform:1.0.0-alpha03")
    implementation("androidx.appstate.transform:transform-testing:1.0.0-alpha03")
    implementation("androidx.appstate.transform:transform-testing-wasm:1.0.0-alpha03")
    implementation("androidx.appstate.transform:transform-wasm:1.0.0-alpha03")
}
```

For more information about dependencies, see [Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component&template)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 1.0

### Version 1.0.0-alpha03

November 18, 2026

`androidx.appstate.transform:transform-*:1.0.0-alpha03` is released. Version 1.0.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a021adf44194ae86e596ae25ca43d5e4e18f6926..3e55c1ad889c6c0087b0bf6720b1a970b6e8ea3b/appstate/transform).

**API Changes**

- `AppState Transform` has added support for `SavedStateContainer` that enables the use of `rememberSaveable` inside of the `@Composable` lambda. The ensures that all of the state inside the transform is not saved across configuration changes and process death. ([Ia66ea](https://android-review.googlesource.com/#/q/Ia66eaca2bb23885fd8f7968275a54b9df8e76990))
- `AppState Transform` now provides a `RunnableTransformScope` that provides a public `run` function to kick off the scope while the default `TransformScope` interface can continue to be used for `launchTransform` with the assumption that the scope is already running. ([Ia1f0d](https://android-review.googlesource.com/#/q/Ia1f0d4eff859ffa37b25d4fccf60d5f89b8214b9))

### Version 1.0.0-alpha02

November 04, 2026

`androidx.appstate.transform:transform-*:1.0.0-alpha02` is released. Version 1.0.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f9cd04314f915c133a8f6e109ed8fbbf2a82bf65..a021adf44194ae86e596ae25ca43d5e4e18f6926/appstate/transform).

### Version 1.0.0-alpha01

October 28, 2026

`androidx.appstate.transform:transform-*:1.0.0-alpha01` is released. Version 1.0.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56ca943f55b3d53ce513a0fa356fe8fe4c43fe9f/appstate/transform).

**New Features**

[`AppState Transform`](https://developer.android.com/reference/kotlin/androidx/appstate/transform/package-summary.md.txt) is a new library built on the Compose runtime that allows for running a composition outside of your UI. The `androidx.appstate.transform:transform` artifact provides the library APIs and it also comes with a `androidx.appstate.transform:transform-testing` artifact for testing. Developers can use Transform to manage their composition anywhere within their app.

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