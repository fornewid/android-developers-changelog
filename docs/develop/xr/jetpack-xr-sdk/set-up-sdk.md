---
title: Set up the Jetpack XR SDK  |  Android XR for Jetpack XR SDK  |  Android Developers
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/set-up-sdk
source: html-scrape
---

The Android XR SDK has  [reached Developer Preview 3](https://android-developers.googleblog.com/2025/12/build-for-ai-glasses-with-android-xr.html), and we want your feedback! Try things out, and visit our [support page](/develop/xr/support) to reach out.

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Devices](https://developer.android.com/develop/devices)
* [Android XR](https://developer.android.com/develop/xr)
* [Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk)
* [Guides](https://developer.android.com/develop/xr/get-started)

# Set up the Jetpack XR SDK Stay organized with collections Save and categorize content based on your preferences.



Applicable XR devices

This guidance helps you build experiences for these types of XR devices.

[Learn about XR device types →](/develop/xr/devices)

![](/static/images/develop/xr/xr-headsets-icon.svg)


XR Headsets

![](/static/images/develop/xr/xr-glasses-icon.svg)


Wired XR Glasses

![](/static/images/develop/xr/ai-glasses-icon.svg)


AI Glasses

[Learn about XR device types →](/develop/xr/devices)

Before you can start building, you need to set up the Jetpack XR SDK. Follow
the steps in each section to set up your development environment with the SDK.

## Check Android SDK compatibility

The Jetpack XR SDK requires your app to use an Android [`minSdk`](/build#min-sdk) of 24 and a
[`compileSdk`](/build#compile-sdk) of 34 or higher.

## Add library dependencies

The dependencies that your app requires depend on the types of experiences and
XR devices that you are building for. See the following sections for more
information about adding the dependencies for your app.

### Add library dependencies for immersive experiences (XR headsets and XR glasses)

First, see the following reference guides to understand necessary dependencies
and compatibility issues for each of the required libraries:

* [XR Runtime](/jetpack/androidx/releases/xr-runtime)
* [Jetpack SceneCore](/jetpack/androidx/releases/xr-scenecore)
* [Jetpack Compose for XR](/jetpack/androidx/releases/xr-compose)
* [Material Design for XR](/jetpack/androidx/releases/xr-compose-material3)
* [ARCore for Jetpack XR](/jetpack/androidx/releases/xr-arcore)

Then, add the necessary dependencies to your app's `build.gradle.kts` file:

### Groovy

```
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha12"
    implementation "androidx.xr.scenecore:scenecore:1.0.0-alpha13"
    implementation "androidx.xr.compose:compose:1.0.0-alpha12"
    implementation "androidx.xr.compose.material3:material3:1.0.0-alpha16"
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha12"

    // For compatibility with guava, use these dependencies:
    implementation "androidx.xr.arcore:arcore-guava:1.0.0-alpha12"
    implementation "androidx.xr.runtime:runtime-guava:1.0.0-alpha12"
    implementation "androidx.xr.scenecore:scenecore-guava:1.0.0-alpha13"

    // For compatibility with rxjava3, use these dependencies:
    implementation "androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha12"
    implementation "androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha12"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha12")
    implementation("androidx.xr.scenecore:scenecore:1.0.0-alpha13")
    implementation("androidx.xr.compose:compose:1.0.0-alpha12")
    implementation("androidx.xr.compose.material3:material3:1.0.0-alpha16")
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha12")

    // For compatibility with guava, use these dependencies:
    implementation("androidx.xr.arcore:arcore-guava:1.0.0-alpha12")
    implementation("androidx.xr.runtime:runtime-guava:1.0.0-alpha12")
    implementation("androidx.xr.scenecore:scenecore-guava:1.0.0-alpha13")

    // For compatibility with rxjava3, use these dependencies:
    implementation("androidx.xr.arcore:arcore-rxjava3:1.0.0-alpha12")
    implementation("androidx.xr.runtime:runtime-rxjava3:1.0.0-alpha12")
}
```

#### Enable code minification (optional)

If you want to enable code minification and obfuscation using ProGuard for your
builds, you must also add a dependency on the Android Extensions for XR library.
This is required for projects using Jetpack XR `alpha05` or newer.

Add the following `compileOnly` dependency to your module's `build.gradle.kts`
file:

### Groovy

```
dependencies {
    // ... other dependencies
    compileOnly "com.android.extensions.xr:extensions-xr:1.1.0"
}
```

### Kotlin

```
dependencies {
    // ... other dependencies
    compileOnly("com.android.extensions.xr:extensions-xr:1.1.0")
}
```

**Caution:** You must use `compileOnly` for this dependency. Using
`implementation` or `api` will cause your app to break at runtime.

### Add library dependencies for augmented experiences (AI glasses)

First, see the following reference guides to understand necessary dependencies
and compatibility issues for each of the required libraries:

* [XR Runtime](/jetpack/androidx/releases/xr-runtime)
* [ARCore for Jetpack XR](/jetpack/androidx/releases/xr-arcore)
* [Jetpack Compose Glimmer](/jetpack/androidx/releases/xr-glimmer)
* [Jetpack Projected](/jetpack/androidx/releases/xr-projected)

Then, add the necessary dependencies to your app's `build.gradle.kts` file:

### Groovy

```
dependencies {
    implementation "androidx.xr.runtime:runtime:1.0.0-alpha12"
    implementation "androidx.xr.glimmer:glimmer:1.0.0-alpha08"
    implementation "androidx.xr.projected:projected:1.0.0-alpha05"
    implementation "androidx.xr.arcore:arcore:1.0.0-alpha11"
}
```

### Kotlin

```
dependencies {
    implementation("androidx.xr.runtime:runtime:1.0.0-alpha12")
    implementation("androidx.xr.glimmer:glimmer:1.0.0-alpha08")
    implementation("androidx.xr.projected:projected:1.0.0-alpha05")
    implementation("androidx.xr.arcore:arcore:1.0.0-alpha11")
}
```

**Note:** While developing for AI glasses, use these stated library versions even if
newer versions of these Jetpack libraries have already been released.

[Previous

arrow\_back

Create an Android XR project](/develop/xr/jetpack-xr-sdk/create-project)