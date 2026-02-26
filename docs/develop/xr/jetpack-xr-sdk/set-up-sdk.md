---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk
source: md.txt
---

<br />


Applicable XR devices This guidance helps you build experiences for these types of XR devices. [Learn about XR device types →](https://developer.android.com/develop/xr/devices) ![](https://developer.android.com/static/images/develop/xr/xr-headsets-icon.svg) XR Headsets [](https://developer.android.com/develop/xr/devices#xr-headsets) ![](https://developer.android.com/static/images/develop/xr/xr-glasses-icon.svg) Wired XR Glasses [](https://developer.android.com/develop/xr/devices#xr-glasses) ![](https://developer.android.com/static/images/develop/xr/ai-glasses-icon.svg) AI Glasses [](https://developer.android.com/develop/xr/devices#ai-glasses) [Learn about XR device types →](https://developer.android.com/develop/xr/devices)

<br />

Before you can start building, you need to set up the Jetpack XR SDK. Follow
the steps in each section to set up your development environment with the SDK.

## Check Android SDK compatibility

The Jetpack XR SDK requires your app to use an Android [`minSdk`](https://developer.android.com/build#min-sdk) of 24 and a
[`compileSdk`](https://developer.android.com/build#compile-sdk) of 34 or higher.

## Add library dependencies

The dependencies that your app requires depend on the types of experiences and
XR devices that you are building for. See the following sections for more
information about adding the dependencies for your app.

### Add library dependencies for immersive experiences (XR headsets and XR glasses)

First, see the following reference guides to understand necessary dependencies
and compatibility issues for each of the required libraries:

- [XR Runtime](https://developer.android.com/jetpack/androidx/releases/xr-runtime)
- [Jetpack SceneCore](https://developer.android.com/jetpack/androidx/releases/xr-scenecore)
- [Jetpack Compose for XR](https://developer.android.com/jetpack/androidx/releases/xr-compose)
- [Material Design for XR](https://developer.android.com/jetpack/androidx/releases/xr-compose-material3)
- [ARCore for Jetpack XR](https://developer.android.com/jetpack/androidx/releases/xr-arcore)

Then, add the necessary dependencies to your app's `build.gradle.kts` file:


### Groovy

```groovy
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha11"
    implementation "androidx.xr.scenecore:scenecore:1.0.0-alpha12"
    implementation "androidx.xr.compose:compose:1.0.0-alpha11"
    implementation "androidx.xr.compose.material3:material3:1.0.0-alpha15"
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha11"

    // For compatibility with guava, use these dependencies:
    implementation "androidx.xr.arcore:arcore-guava:1.0.0-alpha11"
    implementation "androidx.xr.runtime:runtime-guava:1.0.0-alpha11"
    implementation "androidx.xr.scenecore:scenecore-guava:1.0.0-alpha12"

    // For compatibility with rxjava3, use these dependencies:
    implementation "androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha11"
    implementation "androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha11"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha11")
    implementation("androidx.xr.scenecore:scenecore:1.0.0-alpha12")
    implementation("androidx.xr.compose:compose:1.0.0-alpha11")
    implementation("androidx.xr.compose.material3:material3:1.0.0-alpha15")
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha11")

    // For compatibility with guava, use these dependencies:
    implementation("androidx.xr.arcore:arcore-guava:1.0.0-alpha11")
    implementation("androidx.xr.runtime:runtime-guava:1.0.0-alpha11")
    implementation("androidx.xr.scenecore:scenecore-guava:1.0.0-alpha12")

    // For compatibility with rxjava3, use these dependencies:
    implementation("androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha11")
    implementation("androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha11")
}
```

#### Enable code minification (optional)

If you want to enable code minification and obfuscation using ProGuard for your
builds, you must also add a dependency on the Android Extensions for XR library.
This is required for projects using Jetpack XR `alpha05` or newer.

Add the following `compileOnly` dependency to your module's `build.gradle.kts`
file:

### Groovy

```groovy
dependencies {
    // ... other dependencies
    compileOnly "com.android.extensions.xr:extensions-xr:1.1.0"
}
```

### Kotlin

```kotlin
dependencies {
    // ... other dependencies
    compileOnly("com.android.extensions.xr:extensions-xr:1.1.0")
}
```

> [!CAUTION]
> **Caution:** You must use `compileOnly` for this dependency. Using `implementation` or `api` will cause your app to break at runtime.

### Add library dependencies for augmented experiences (AI glasses)

First, see the following reference guides to understand necessary dependencies
and compatibility issues for each of the required libraries:

- [XR Runtime](https://developer.android.com/jetpack/androidx/releases/xr-runtime)
- [ARCore for Jetpack XR](https://developer.android.com/jetpack/androidx/releases/xr-arcore)
- [Jetpack Compose Glimmer](https://developer.android.com/jetpack/androidx/releases/xr-glimmer)
- [Jetpack Projected](https://developer.android.com/jetpack/androidx/releases/xr-projected)

Then, add the necessary dependencies to your app's `build.gradle.kts` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha11"
    implementation "androidx.xr.glimmer:glimmer:1.0.0-alpha07"
    implementation "androidx.xr.projected:projected:1.0.0-alpha05"
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha11"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha11")
    implementation("androidx.xr.glimmer:glimmer:1.0.0-alpha07")
    implementation("androidx.xr.projected:projected:1.0.0-alpha05")
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha11")
}
```