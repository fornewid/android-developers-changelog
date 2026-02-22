---
title: https://developer.android.com/guide/navigation
url: https://developer.android.com/guide/navigation
source: md.txt
---

Navigation refers to the interactions that let users navigate across, into, and
back out from the different pieces of content within your app.

Android Jetpack's Navigation component includes the [Navigation
library](https://developer.android.com/jetpack/androidx/releases/navigation), [Safe Args Gradle plug-in](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args),
and tooling to help you implement app navigation. The Navigation component
handles diverse navigation use cases, from straightforward button clicks to more
complex patterns, such as app bars and the navigation drawer.
| **Important:** The Navigation component also ensures a consistent and predictable user experience by adhering to an established [set of principles](https://developer.android.com/guide/navigation/navigation-principles).

## Key concepts

The following table provides an overview of the key concepts in
navigation and the main types that you use to implement them.

| Concept | Purpose | Type |
|---|---|---|
| Host | A UI element that contains the current navigation destination. That is, when a user navigates through an app, the app essentially swaps destinations in and out of the navigation host. | - **Compose** : [`NavHost`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#NavHost(androidx.navigation.NavHostController,androidx.navigation.NavGraph,androidx.compose.ui.Modifier,androidx.compose.ui.Alignment,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1)) - **Fragments** : [`NavHostFragment`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment) |
| Graph | A data structure that defines all the navigation destinations within the app and how they connect together. | [`NavGraph`](https://developer.android.com/reference/androidx/navigation/NavGraph) |
| Controller | The central coordinator for managing navigation between destinations. The controller offers methods for navigating between destinations, handling deep links, managing the back stack, and more. | [`NavController`](https://developer.android.com/reference/androidx/navigation/NavController) |
| Destination | A node in the navigation graph. When the user navigates to this node, the host displays its content. | [`NavDestination`](https://developer.android.com/reference/androidx/navigation/NavDestination) Typically created when constructing the navigation graph. |
| Route | Uniquely identifies a destination and any data required by it. You can navigate using routes. Routes take you to destinations. | Any serializable data type. |

| **Important:** Whether you are using Compose, views, or a custom UI framework, these concepts always apply when implementing navigation. However, the specific ways in which you use them can differ.

## Benefits and features

The Navigation component provides a number of other benefits and features,
including the following:

- **Animations and transitions:** Provides standardized resources for animations and transitions.
- **Deep linking:** Implements and handles deep links that take the user directly to a destination.
- **UI patterns:** Supports patterns such as navigation drawers and bottom navigation with minimal additional work.
- **Type safety:** Includes support for passing data between destinations with [type safety](https://developer.android.com/guide/navigation/design/type-safety).
- **ViewModel support:** Enables scoping a `ViewModel` to a navigation graph to share UI-related data between the graph's destinations.
- **Fragment transactions:** Fully supports and handles fragment transactions.
- **Back and up:** Handles back and up actions correctly by default.

| **Note:** If you are using XML for your navigation graphs, use Android Studio's [Navigation Editor](https://developer.android.com/guide/navigation/design/editor) to view and edit your graphs.
| **Note:** Android 13 introduces predictive back navigation, which works with the Navigation component for Android devices. Implement predictive back navigation in your app as soon as possible. Otherwise, users might experience unexpected behavior in a future Android release.

## Set up your environment

To include navigation support in your project, add the following dependencies to
your app's `build.gradle` file:  

### Groovy

```groovy
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  id 'org.jetbrains.kotlin.plugin.serialization' version '2.0.21'
}
  
dependencies {
  def nav_version = "2.9.7"

  // Jetpack Compose Integration
  implementation "androidx.navigation:navigation-compose:$nav_version"

  // Views/Fragments Integration
  implementation "androidx.navigation:navigation-fragment:$nav_version"
  implementation "androidx.navigation:navigation-ui:$nav_version"

  // Feature module support for Fragments
  implementation "androidx.navigation:navigation-dynamic-features-fragment:$nav_version"

  // Testing Navigation
  androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"

  // JSON serialization library, works with the Kotlin serialization plugin.
  implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3"
}
```

### Kotlin

```kotlin
plugins {
  // Kotlin serialization plugin for type safe routes and navigation arguments
  kotlin("plugin.serialization") version "2.0.21"
}

dependencies {
  val nav_version = "2.9.7"

  // Jetpack Compose integration
  implementation("androidx.navigation:navigation-compose:$nav_version")

  // Views/Fragments integration
  implementation("androidx.navigation:navigation-fragment:$nav_version")
  implementation("androidx.navigation:navigation-ui:$nav_version")

  // Feature module support for Fragments
  implementation("androidx.navigation:navigation-dynamic-features-fragment:$nav_version")

  // Testing Navigation
  androidTestImplementation("androidx.navigation:navigation-testing:$nav_version")

  // JSON serialization library, works with the Kotlin serialization plugin
  implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.7.3")
}
```

For information on adding other architecture components to your project, see
[Add components to your project](https://developer.android.com/topic/libraries/architecture/adding-components#navigation).

## Next steps

For more documentation and resources related to the Navigation component, see
the following resources.

### Detailed guides

For more information on how to implement a navigation host and `NavController`,
as well as detail on how they interact with Compose and other UI frameworks, see
the following guides:

- [Create a navigation controller](https://developer.android.com/guide/navigation/navcontroller): Outlines how to create a `NavController`.
- [Create your navigation graph](https://developer.android.com/guide/navigation/design): Details how to create a navigation host and a navigation graph.
- [Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate): Demonstrates how to use a `NavController` to move between the destinations in your graph.

### Codelabs

- [Learn Jetpack Navigation](https://developer.android.com/codelabs/android-navigation)
- [Fragments and the Navigation Component](https://developer.android.com/codelabs/basic-android-kotlin-training-fragments-navigation-component)
- [Build an adaptive app with dynamic navigation](https://developer.android.com/codelabs/basic-android-kotlin-compose-adaptive-navigation-for-large-screens#0)

### Videos

- [Navigating navigation](https://www.youtube.com/watch?v=09qjn706ITA)
- [10 best practices for moving to a single activity](https://www.youtube.com/watch?v=9O1D_Ytk0xg)
- [Single activity: Why, when, and how (Android Dev Summit '18)](https://www.youtube.com/watch?v=2k8x8V77CrU)
- [Android Jetpack: Manage UI navigation with navigation controller (Google
  I/O '18)](https://www.youtube.com/watch?v=8GCXtCjtg40)

### Samples