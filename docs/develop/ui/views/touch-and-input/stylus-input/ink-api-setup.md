---
title: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-setup
url: https://developer.android.com/develop/ui/views/touch-and-input/stylus-input/ink-api-setup
source: md.txt
---

To integrate the Ink API, add the following dependencies to your app from the Google Maven repository:  

### Kotlin

    dependencies {
        val ink_version = "1.0.0"

        implementation "androidx.ink:ink-authoring:$ink_version"
        implementation "androidx.ink:ink-brush:$ink_version"
        implementation "androidx.ink:ink-geometry:$ink_version"
        implementation "androidx.ink:ink-nativeloader:$ink_version"
        implementation "androidx.ink:ink-rendering:$ink_version"
        implementation "androidx.ink:ink-strokes:$ink_version"
        implementation "androidx.ink:ink-storage:$ink_version"
    }

### Groovy

    dependencies {
        def ink_version = "1.0.0"

        implementation("androidx.ink:ink-authoring:$ink_version")
        implementation("androidx.ink:ink-brush:$ink_version")
        implementation("androidx.ink:ink-geometry:$ink_version")
        implementation("androidx.ink:ink-nativeloader:$ink_version")
        implementation("androidx.ink:ink-rendering:$ink_version")
        implementation("androidx.ink:ink-strokes:$ink_version")
        implementation("androidx.ink:ink-storage:$ink_version")
    }