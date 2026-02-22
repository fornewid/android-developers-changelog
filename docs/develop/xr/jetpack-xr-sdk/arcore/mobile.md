---
title: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/mobile
url: https://developer.android.com/develop/xr/jetpack-xr-sdk/arcore/mobile
source: md.txt
---

ARCore for Jetpack XR can run on [supported mobile devices](https://developers.google.com/ar/devices)
as well as Android XR devices. The
[ARCore for Jetpack XR library](https://developer.android.com/jetpack/androidx/releases/xr-arcore) can use the
[Google Play Services for AR](https://developers.google.com/ar/develop/java/enable-arcore) runtime on those devices.
This lets you write apps for AR experiences that use a shared codebase to
interact with the ARCore for Jetpack XR perception APIs.

> [!WARNING]
> **Experimental:** Running ARCore for Jetpack XR apps on mobile devices is currently in developer preview. Some features may be missing or may not work as expected. [Report any bugs](https://developer.android.com/develop/xr/support) you encounter.

## Feature compatibility

The following features provided by ARCore for Jetpack XR are not supported on
the mobile runtime:

- Locally-persistent anchors
- Face tracking
- Eye tracking

## Access the underlying mobile runtime

Your app might need to access features from the underlying mobile runtime that
are not exposed in ARCore for Jetpack XR, for example, to access [Lighting
Estimation](https://developers.google.com/ar/develop/lighting-estimation) values or to use [Recording and
Playback](https://developers.google.com/ar/develop/recording-and-playback).

### Add dependencies

Your app needs to explicitly depend on the following libraries as an
[`implementation` dependency](https://developer.android.com/build/dependencies#dependency_configurations) to access these classes
directly.

Use the following dependency specification in your `build.gradle` file:

### Groovy

```groovy
dependencies {
    implementation "androidx.xr.arcore:arcore-play-services:1.0.0-alpha10"
    implementation "com.google.ar:core:1.51.0"
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.xr.arcore:arcore-play-services:1.0.0-alpha10")
    implementation("com.google.ar:core:1.51.0")
}
```

### Access the `ArCoreRuntime`

Your app can obtain a [`Session`](https://developers.google.com/ar/reference/java/com/google/ar/core/Session) and
[`Frame`](https://developers.google.com/ar/reference/java/com/google/ar/core/Frame) from the underlying runtime and use those objects
directly:


```kotlin
val arCoreRuntime = session.runtimes.firstNotNullOfOrNull { it as? ArCoreRuntime } ?: return
val originalSession = arCoreRuntime.lifecycleManager.session()
val originalFrame = arCoreRuntime.perceptionManager.lastFrame()
```

<br />

> [!NOTE]
> **Note:** Your app must opt in to `UnsupportedArCoreCompatApi` to access the underlying `Session` or `Frame`. Symbols annotated by `UnsupportedArCoreCompatApi` are exposed for compatibility reasons, and will be removed in a future release.