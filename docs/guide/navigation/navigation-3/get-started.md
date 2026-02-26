---
title: https://developer.android.com/guide/navigation/navigation-3/get-started
url: https://developer.android.com/guide/navigation/navigation-3/get-started
source: md.txt
---

To get started with Navigation 3, add the library to your project along with any
supporting libraries. Use the following table to decide which libraries to add:

## Artifacts

| **Name** | **What it does** | **Artifact** |
|---|---|---|
| Navigation 3 runtime library | Core Navigation 3 API. Includes `NavEntry`, `EntryProvider` and the associated DSL. | [androidx.navigation3:navigation3-runtime](https://developer.android.com/jetpack/androidx/releases/navigation3) |
| Navigation 3 UI library | Provides classes to display content, including `NavDisplay` and `Scene`. | [androidx.navigation3:navigation3-ui](https://developer.android.com/jetpack/androidx/releases/navigation3) |
| ViewModel Lifecycle for Navigation 3 | Allows ViewModels to be scoped to entries in the back stack. | [androidx.lifecycle:lifecycle-viewmodel-navigation3](https://developer.android.com/jetpack/androidx/releases/lifecycle#lifecycle.lifecycle-viewmodel-navigation3) |
| Material 3 adaptive layouts for Navigation 3 | Provides adaptive layouts (SceneStrategies, Scenes and metadata definitions) for use with NavDisplay. | [androidx.compose.material3.adaptive:adaptive-navigation3](https://developer.android.com/jetpack/androidx/releases/compose-material3-adaptive) |
| [KotlinX Serialization](https://kotlinlang.org/docs/serialization.html) | Allows navigation keys to be serialized. | Plugin: org.jetbrains.kotlin.plugin.serialization Library: org.jetbrains.kotlinx:kotlinx-serialization-core |

## Project setup

To add the Navigation 3 library to your existing project, add the following to
your `libs.versions.toml`:

    [versions]
    nav3Core = "1.0.1"
    lifecycleViewmodelNav3 = "2.11.0-alpha01"
    kotlinSerialization = "2.2.21"
    kotlinxSerializationCore = "1.9.0"
    material3AdaptiveNav3 = "1.3.0-alpha09"

    [libraries]
    # Core Navigation 3 libraries
    androidx-navigation3-runtime = { module = "androidx.navigation3:navigation3-runtime", version.ref = "nav3Core" }
    androidx-navigation3-ui = { module = "androidx.navigation3:navigation3-ui", version.ref = "nav3Core" }

    # Optional add-on libraries
    androidx-lifecycle-viewmodel-navigation3 = { module = "androidx.lifecycle:lifecycle-viewmodel-navigation3", version.ref = "lifecycleViewmodelNav3" }
    kotlinx-serialization-core = { module = "org.jetbrains.kotlinx:kotlinx-serialization-core", version.ref = "kotlinxSerializationCore" }
    androidx-material3-adaptive-navigation3 = { group = "androidx.compose.material3.adaptive", name = "adaptive-navigation3", version.ref = "material3AdaptiveNav3" }

    [plugins]
    # Optional plugins
    jetbrains-kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlinSerialization"}

Also, update your compile SDK to 36 or later:

    [versions]
    compileSdk = "36"

Add the following to your **app** build file `app/build.gradle.kts`:

    plugins {
        ...
        // Optional, provides the @Serialize annotation for autogeneration of Serializers.
        alias(libs.plugins.jetbrains.kotlin.serialization)
    }

    dependencies {
        ...
        implementation(libs.androidx.navigation3.ui)
        implementation(libs.androidx.navigation3.runtime)
        implementation(libs.androidx.lifecycle.viewmodel.navigation3)
        implementation(libs.androidx.material3.adaptive.navigation3)
        implementation(libs.kotlinx.serialization.core)
    }