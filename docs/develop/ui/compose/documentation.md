---
title: Get started with Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/documentation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Get started with Jetpack Compose Stay organized with collections Save and categorize content based on your preferences.




Jetpack Compose is the modern toolkit for building Android UI, simplifying the
development of apps that adapt to any display size.

* [Overview](/develop/ui/compose): See the resources available to Compose developers.
* [Tutorial](/develop/ui/compose/tutorial): Get started with Compose by building a basic UI.
* [Quick Guides](/quick-guides): Try out our fast and focused guides, designed to get you
  to your goal as quickly as possible.

## Foundation

* [Thinking in Compose](/develop/ui/compose/mental-model): How the declarative approach of Compose is
  different from the view-based approach you may have used in the past. Build
  a mental model of working with Compose.
* [Managing state](/develop/ui/compose/state): Setting and using state in your Compose app.
* [Lifecycle of composables](/develop/ui/compose/lifecycle): Lifecycle of a composable, and how Compose
  determines whether it needs to be redrawn.
* [Modifiers](/develop/ui/compose/modifiers): Use modifiers to augment or decorate your composables.
* [Side-effects in Compose](/develop/ui/compose/side-effects): Ways to manage side-effects.
* [Jetpack Compose Phases](/develop/ui/compose/phases): The steps Compose goes through to render your
  app's UI, and how to use that information to write efficient code.
* [Architectural layering](/develop/ui/compose/layering): The architectural layers that make up Jetpack
  Compose and the core principles that informed the design of Compose.
* [Performance](/develop/ui/compose/performance): Avoid the common programming pitfalls that can degrade
  app performance.
* [Semantics in Compose](/develop/ui/compose/semantics): The semantics tree, which organizes your UI in a
  way that can be used by accessibility services and testing frameworks.
* [Locally scoped data with CompositionLocal](/develop/ui/compose/compositionlocal): Use `CompositionLocal` to
  pass data through the composition.

## Adaptive UI

* [Build adaptive apps](/develop/adaptive-apps/guides/build-adaptive-apps): Learn the core principles of creating layouts
  optimized for any display size, including phones, tablets, foldables, and
  more.
* [Apply proven layouts](/develop/adaptive-apps/guides/canonical-layouts): Use canonical layouts like list-detail and
  supporting pane for optimized apps on large screens.
* [Adaptive navigation](/guide/topics/large-screens/navigation-for-responsive-uis): Implement navigation patterns that automatically
  adjust to the available display space.

## Development environment

* [Android Studio with Compose](/develop/ui/compose/setup): How to et up your development environment
  to use Compose.
* [Tooling for Compose](/develop/ui/compose/tooling): Android Studio's new features to support Compose.
* [Kotlin for Compose](/develop/ui/compose/kotlin): Kotlin-specific idioms work with Compose.
* [Compare Compose and view metrics](/develop/ui/compose/migrate/compare-metrics): How migrating to Compose can affect
  your app's APK size and runtime performance.
* [Bill of Materials](/develop/ui/compose/bom): Manage all your Compose dependencies by specifying
  only the BOM's version.

## Design

* [Layouts](/develop/ui/compose/layouts): Compose layout components and how to design your own.
  + [Layout basics](/develop/ui/compose/layouts/basics): The building blocks for a straightforward app UI.
  + [Material Components and layouts](/develop/ui/compose/components): Material components and layouts
    in Compose.
  + [Custom layouts](/develop/ui/compose/layouts/custom): Take control of your app's layout and design a
    custom layout of your own.
  + [Alignment lines](/develop/ui/compose/layouts/alignment-lines): Create custom alignment guides to precisely align
    and position your UI elements.
  + [Intrinsic measurements](/develop/ui/compose/layouts/intrinsic-measurements): How to query for information about child
    elements before measuring them because Compose measure UI elements only
    once per pass.
  + [ConstraintLayout](/develop/ui/compose/layouts/constraintlayout): Use `ConstraintLayout` in your Compose UI.
* [Design Systems](/develop/ui/compose/designsystems): Implement a design system and give your app a
  consistent look and feel.
  + [Material Design 3](/develop/ui/compose/designsystems/material3): Implement Material You with the Compose
    implementation of [Material Design 3](https://m3.material.io/).
  + [Migrating from Material 2 to Material 3](/develop/ui/compose/designsystems/material2-material3): Migrate your app from
    Material Design 2 to Material Design 3 in Compose.
  + [Material Design 2](/develop/ui/compose/designsystems/material): Customize the Compose implementation of
    [Material Design 2](https://material.io/) to fit your product's brand.
  + [Custom design systems](/develop/ui/compose/designsystems/custom): Implement a custom design system in Compose
    and adapt existing Material Design composables for the new design
    system.
  + [Anatomy of a theme](/develop/ui/compose/designsystems/anatomy): Lower-level constructs and APIs used by
    `MaterialTheme` and custom design systems.
* [Lists and grids](/develop/ui/compose/lists): Compose options for managing and displaying lists and
  grids of data.
* [Text](/develop/ui/compose/text): Main options in Compose for displaying and editing text.
* [Graphics](/develop/ui/compose/graphics): Compose features for building and working with custom
  graphics.
* [Animation](/develop/ui/compose/animation/introduction): Compose options for animating your UI elements.
* [Gestures](/develop/ui/compose/touch-input/pointer-input): Build a Compose UI that detects and interacts with user
  gestures.
* [Handling user interactions](/develop/ui/compose/touch-input/user-interactions/handling-interactions): How Compose abstracts low-level input into
  higher-level interactions so you can customize how your components respond
  to user actions.

## Adopting Compose

* [Migrate view-based apps](/develop/ui/compose/migrate): Migrate your view-based app to Compose.
  + [Migration strategy](/develop/ui/compose/migrate/strategy): How to safely and incrementally introduce
    Compose into your codebase.
  + [Interoperability APIs](/develop/ui/compose/migrate/interoperability-apis): Compose APIs to help you combine Compose
    with a view-based UI.
  + [Other considerations](/develop/ui/compose/migrate/other-considerations): Theming, architecture, testing, and other
    considerations while migrating your view-based app to Compose.
* [Compose and other libraries](/develop/ui/compose/libraries): How to use view-based libraries in your
  Compose content.
* [Compose architecture](/develop/ui/compose/architecture): Implement the unidirectional flow pattern in
  Compose, implement events and state holders, and work with `ViewModel` in
  Compose.
* [Navigation](/develop/ui/compose/navigation): Use `NavController` to integrate the [Navigation
  component](/guide/navigation) with your Compose UI.
* [Resources](/develop/ui/compose/resources): Work with your app's resources in your Compose code.
* [Accessibility](/develop/ui/compose/accessibility): Accommodate users with accessibility requirements.
* [Testing](/develop/ui/compose/testing): Test your Compose code.
  + [Testing cheat sheet](/develop/ui/compose/testing-cheatsheet): A quick reference of useful Compose testing
    APIs.

## Additional resources

* [Get setup](/develop/ui/compose/setup)
* [Curated learning pathway](/courses/pathways/compose)
* [Compose API guidelines](https://android.googlesource.com/platform/frameworks/support/+/androidx-main/compose/docs/compose-api-guidelines.md)
* [API reference](/reference/kotlin/androidx/compose)
* [Codelabs](https://goo.gle/compose-codelabs)
* [Sample apps](https://github.com/android/compose-samples)
* [Videos](https://www.youtube.com/user/androiddevelopers/search?query=%23jetpackcompose)

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Locally scoped data with CompositionLocal](/develop/ui/compose/compositionlocal)
* [Other considerations](/develop/ui/compose/migrate/other-considerations)
* [Anatomy of a theme in Compose](/develop/ui/compose/designsystems/anatomy)