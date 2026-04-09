---
title: Set up development environment for Navigation Event  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-event/setup
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Set up development environment for Navigation Event Stay organized with collections Save and categorize content based on your preferences.



To set up your development environment for `NavigationEvent`, follow these
steps.

## Declare dependencies

1. Add the `navigationevent` artifact to your project. This is the core library
   containing the shared `NavigationEventDispatcher` and `NavigationEventHandler`
   classes.

   For Jetpack Compose integration, you also need to add the corresponding
   Compose artifact:

   ```
   [versions]
   navigationevent = "1.0.0"

   [libraries]
   # NavigationEvent libraries
   androidx-navigationevent = { module = "androidx.navigationevent:navigationevent", version.ref = "navigationevent" }
   androidx-navigationevent-compose = { module = "androidx.navigationevent:navigationevent-compose", version.ref = "navigationevent" }
   ```
2. Update your compile SDK to 36 or above:

   ```
   [versions]
   compileSdk = "36"
   ```
3. Add the following to your app build file, `app/build.gradle.kts`:

   ```
   dependencies {
     ...
     implementation(libs.androidx.navigationevent)
     implementation(libs.androidx.navigationevent.compose)
   }
   ```

[Previous

arrow\_back

Overview](/guide/navigation/navigation-event)

[Next

Handle back gestures and animations

arrow\_forward](/guide/navigation/navigation-event/handle-back)