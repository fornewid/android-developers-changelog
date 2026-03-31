---
title: Media3 UI modules  |  Android media  |  Android Developers
url: https://developer.android.com/media/media3/ui/overview
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Essentials](https://developer.android.com/get-started)
* [Camera & media dev center](https://developer.android.com/media)
* [Guides](https://developer.android.com/media/guides)

# Media3 UI modules Stay organized with collections Save and categorize content based on your preferences.




An app playing media requires user interface components for displaying media and
controlling playback. The Media3 library includes two UI modules that contain a
number of UI components.

To use the [Views-based UI module](/media/media3/ui/playerview), add the following dependency:

### Kotlin

```
implementation("androidx.media3:media3-ui:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-ui:1.10.0"
```

To depend on the [Jetpack Compose-based UI module](/media/media3/ui/compose/material3), add the following
dependency:

### Kotlin

```
implementation("androidx.media3:media3-ui-compose:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-ui-compose:1.10.0"
```

To depend on the [Jetpack Compose-based UI module with Material3](/media/media3/ui/compose/customization), add the
following dependency:

### Kotlin

```
implementation("androidx.media3:media3-ui-compose-material3:1.10.0")
```

### Groovy

```
implementation "androidx.media3:media3-ui-compose-material3:1.10.0"
```

We highly encourage you to develop your app in a Compose-first fashion or
[migrate from using Views](/develop/ui/compose/migrate).

**Note:** The `media3-ui-compose` and `media3-ui-compose-material3` modules are
not yet at parity with the `media3-ui` module.