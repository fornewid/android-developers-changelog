---
title: https://developer.android.com/topic/libraries/architecture/appstate
url: https://developer.android.com/topic/libraries/architecture/appstate
source: md.txt
---

# AppState
Part of [Android Jetpack](https://developer.android.com/jetpack).

> [!WARNING]
> **Experimental:** AppState is in alpha. Its APIs are subject to change. File bugs and feedback using the [Transform issue tracker](https://issuetracker.google.com/issues/new?component=2302904&template=2430547) or [StateStore issue tracker](https://issuetracker.google.com/issues/new?component=2302751&template=2430521).

Jetpack AppState is a group of libraries that helps you extend Jetpack Compose
[`State`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/State) beyond the UI layer so you can transform and share
reactive state across any layer of your app. AppState consists of two main
libraries:

- **[Transform](https://developer.android.com/topic/libraries/architecture/appstate/transform)** : A library built on the Compose runtime that runs a `@Composable` block without a UI to combine and transform state sources into Compose `State`.
- **[StateStore](https://developer.android.com/topic/libraries/architecture/appstate/statestore)** : A type-safe container that stores and exposes shared app state as Compose `State`. It's most commonly used to share state across multiple [application components](https://developer.android.com/guide/components/fundamentals#Components).

To learn how Compose `State` works outside UI composables and how Transform
and StateStore fit alongside existing Compose APIs such as `mutableStateOf` and
`SavedStateHandle.saveable` across your architecture, see [Use Compose State
outside the UI](https://developer.android.com/topic/libraries/architecture/appstate/state-beyond-ui).

## Artifacts

To get started with AppState, add the artifacts your project needs along with
any supporting libraries:

| Name | What it does | Artifact |
|---|---|---|
| Transform | Produces and observes Compose `State` outside the UI (`transform` and `listener`). | `androidx.appstate.transform:transform` |
| Transform Testing | Testing utilities for Transform (`transformTest` and `TransformTestScope`). | `androidx.appstate.transform:transform-testing` |
| StateStore | Core type-safe state container and `StateStoreKey` definitions. | `androidx.appstate.statestore:statestore` |
| StateStore DataStore integration | Persists and restores `StateStore` keys to disk using Jetpack [DataStore](https://developer.android.com/topic/libraries/architecture/datastore). | `androidx.appstate.statestore:statestore-datastore` |
| [Compose Compiler](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler) plugin | Compiles `@Composable` functions and blocks in modules that use `transform` or `listener`. | `org.jetbrains.kotlin.plugin.compose` |
| [KotlinX Serialization](https://kotlinlang.org/docs/serialization.html) plugin | Generates serializers for `@Serializable` `StateStoreKey` and custom state types when using `statestore-datastore`. | `org.jetbrains.kotlin.plugin.serialization` |
| KotlinX Serialization library | Runtime serialization library for `@Serializable` `StateStoreKey` and custom state types when using `statestore-datastore`. | `org.jetbrains.kotlinx:kotlinx-serialization-core` |

## Project setup

To add the AppState libraries to your project, declare the versions, libraries,
and Gradle plugins in your `libs.versions.toml` file:

    [versions]
    appstate = "1.0.0-alpha01"
    kotlin = "2.4.10"
    kotlinxSerializationCore = "1.11.0"

    [libraries]
    # Transform library for producing and observing Compose State
    androidx-appstate-transform = { module = "androidx.appstate.transform:transform", version.ref = "appstate" }
    # Testing utilities for Transform
    androidx-appstate-transform-testing = { module = "androidx.appstate.transform:transform-testing", version.ref = "appstate" }
    # Core StateStore library
    androidx-appstate-statestore = { module = "androidx.appstate.statestore:statestore", version.ref = "appstate" }
    # DataStore integration for StateStore (and required serialization runtime)
    androidx-appstate-statestore-datastore = { module = "androidx.appstate.statestore:statestore-datastore", version.ref = "appstate" }
    kotlinx-serialization-core = { module = "org.jetbrains.kotlinx:kotlinx-serialization-core", version.ref = "kotlinxSerializationCore" }

    [plugins]
    compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
    # Required only when using statestore-datastore
    jetbrains-kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }

Next, configure your module's `build.gradle.kts` file:

    plugins {
        ...
        alias(libs.plugins.compose.compiler)
        // Required only when using statestore-datastore
        alias(libs.plugins.jetbrains.kotlin.serialization)
    }

    android {
        ...
        buildFeatures {
            compose = true
        }
    }

    dependencies {
        ...
        implementation(libs.androidx.appstate.transform)
        implementation(libs.androidx.appstate.statestore)

        // Optional: DataStore integration for StateStore
        implementation(libs.androidx.appstate.statestore.datastore)
        implementation(libs.kotlinx.serialization.core)

        ...
        testImplementation(libs.androidx.appstate.transform.testing)
    }

> [!NOTE]
> **Note:** Any module that calls `@Composable` APIs---including non-UI modules that use `transform` or `listener`---must enable Compose build features (`buildFeatures { compose = true }`) and apply the [Compose Compiler Gradle
> plugin](https://developer.android.com/develop/ui/compose/setup-compose-dependencies-and-compiler). Modules that only read or write `State<T>` and `MutableState<T>` (such as with `mutableStateOf` or `StateStore`) without calling `@Composable` functions don't need to enable Compose build features. The [KotlinX Serialization](https://kotlinlang.org/docs/serialization.html) plugin and `kotlinx-serialization-core` library are only required when persisting `StateStore` keys with `statestore-datastore`.

## Code samples

The [AppState recipes repository](https://github.com/android/appstate-recipes) contains working
examples demonstrating how to use Transform and StateStore across common
Android architecture patterns and form factors.

## Provide feedback

Share your feedback, report bugs, or request features using the
[Transform issue tracker](https://issuetracker.google.com/issues/new?component=2302904&template=2430547) or
[StateStore issue tracker](https://issuetracker.google.com/issues/new?component=2302751&template=2430521).