---
title: https://developer.android.com/develop/ui/compose/glance/setup
url: https://developer.android.com/develop/ui/compose/glance/setup
source: md.txt
---

This page describes how to set up your development environment to use Glance.
You can get the latest available version from
[the release page](https://developer.android.com/jetpack/androidx/releases/glance).

Add the specific Glance dependency in your app's module based on the type of
"glanceable" you want to build.

    dependencies {
       // For AppWidgets support
       implementation "androidx.glance:glance-appwidget:1.1.1"

       // For interop APIs with Material 3
       implementation "androidx.glance:glance-material3:1.1.1"

       // For interop APIs with Material 2
       implementation "androidx.glance:glance-material:1.1.1"
    }

## Activate Compose compiler

Set the following options to ensure that the Compose compiler is available for
Glance:


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