---
title: Glance setup  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/setup
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Glance setup Stay organized with collections Save and categorize content based on your preferences.




This page describes how to set up your development environment to use Glance.
You can get the latest available version from
[the release page](/jetpack/androidx/releases/glance).

Add the specific Glance dependency in your app's module based on the type of
"glanceable" you want to build.

```
dependencies {
   // For AppWidgets support
   implementation "androidx.glance:glance-appwidget:1.1.1"

   // For interop APIs with Material 3
   implementation "androidx.glance:glance-material3:1.1.1"

   // For interop APIs with Material 2
   implementation "androidx.glance:glance-material:1.1.1"
}
```

## Activate Compose compiler

Set the following options to ensure that the Compose compiler is available for
Glance:

```
android {
   buildFeatures {
      compose true
   }

   composeOptions {
      kotlinCompilerExtensionVersion = "1.5.15"
   }

   kotlinOptions {
      jvmTarget = "1.8"
   }
}
```

[Previous

arrow\_back

Overview](/develop/ui/compose/glance)

[Next

Create an app widget with Glance

arrow\_forward](/develop/ui/compose/glance/create-app-widget)