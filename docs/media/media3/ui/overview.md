---
title: https://developer.android.com/media/media3/ui/overview
url: https://developer.android.com/media/media3/ui/overview
source: md.txt
---

An app playing media requires user interface components for displaying media and
controlling playback. The Media3 library includes two UI modules that contain a
number of UI components.

To use the [Views-based UI module](https://developer.android.com/media/media3/ui/playerview), add the following dependency:  

### Kotlin

    implementation("androidx.media3:media3-ui:1.9.2")

### Groovy

    implementation "androidx.media3:media3-ui:1.9.2"

To depend on the [Jetpack Compose-based UI module](https://developer.android.com/media/media3/ui/compose/material3), add the following
dependency:  

### Kotlin

    implementation("androidx.media3:media3-ui-compose:1.9.2")

### Groovy

    implementation "androidx.media3:media3-ui-compose:1.9.2"

To depend on the [Jetpack Compose-based UI module with Material3](https://developer.android.com/media/media3/ui/compose/customization), add the
following dependency:  

### Kotlin

    implementation("androidx.media3:media3-ui-compose-material3:1.9.2")

### Groovy

    implementation "androidx.media3:media3-ui-compose-material3:1.9.2"

We highly encourage you to develop your app in a Compose-first fashion or
[migrate from using Views](https://developer.android.com/develop/ui/compose/migrate).

**Note:** The `media3-ui-compose` and `media3-ui-compose-material3` modules are
not yet at parity with the `media3-ui` module.