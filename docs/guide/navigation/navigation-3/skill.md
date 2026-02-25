---
title: Jetpack Navigation 3 Skill  |  App architecture  |  Android Developers
url: https://developer.android.com/guide/navigation/navigation-3/skill
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [App architecture](https://developer.android.com/topic/architecture/intro)

# Jetpack Navigation 3 Skill Stay organized with collections Save and categorize content based on your preferences.




## Migration guide

* *[Navigation 2 to Navigation 3 migration guide](/guide/navigation/navigation-3/migration-guide)*: Step-by-step guide to
  migrate an Android application from Navigation 2 to Navigation 3, covering
  dependency updates, route changes, state management, and UI component
  replacements.

### Requirements

* *[Guide: Migrate to type-safe navigation in Compose](https://developer.android.com/guide/navigation/type-safe-destinations)*: Step-by-step
  guide to migrating an Android application from string-based navigation to
  **Type-Safe Navigation** in Jetpack Compose using Jetpack Navigation 2.

## Developer documentation

* \*[Navigation 3](/guide/navigation/navigation-3). Search documentation for more information on basics,
  saving and managing navigation state, modularizing navigation code, creating
  custom layouts using Scenes, animating between destinations, or applying
  logic or wrappers to destinations.

## Recipes

These are the recipes and what they demonstrate.

### Basic API usage

* *[Basic](/guide/navigation/navigation-3/recipes/basic)*: Shows most basic API usage.
* *[Saveable back stack](/guide/navigation/navigation-3/recipes/basicsaveable)*: Shows basic API usage with a persistent back
  stack.
* *[Entry provider DSL](/guide/navigation/navigation-3/recipes/basicdsl)*: Shows basic API usage using the entryProvider
  DSL.

### Deep links

* *[Basic](/guide/navigation/navigation-3/recipes/deeplinks-basic)*: Shows how to parse a deep link URL from an Android Intent
  into a navigation key.
* *[Advanced](/guide/navigation/navigation-3/recipes/deeplinks-advanced)*: Shows how to handle deep links with a synthetic back
  stack and correct "Up" navigation behavior.

### Scenes

#### Use built-in Scenes

* *[Dialog](/guide/navigation/navigation-3/recipes/dialog)*: Shows how to create a Dialog.

#### Create custom Scenes

* *[BottomSheet](/guide/navigation/navigation-3/recipes/bottomsheet)*: Shows how to create a BottomSheet destination.
* *[List-Detail Scene](/guide/navigation/navigation-3/recipes/scenes#list-detail-scene)*: Shows how to create a custom, list-detail
  layout using a `Scene` and `SceneStrategy`.
* *[Two pane Scene](/guide/navigation/navigation-3/recipes/scenes#two-pane-scene)*: Shows how to create a custom, 2-pane layout.

### Animations

* *[Animations](/guide/navigation/navigation-3/recipes/animations)*: Shows how to override the default animations for all
  destinations and a single destination.

### Common back stack behavior

* *[Multiple back stacks](/guide/navigation/navigation-3/recipes/multiple-backstacks)*: Shows how to create multiple top level
  routes, each with its own back stack. Top level routes are displayed in a
  navigation bar allowing users to switch between them. State is retained for
  each top level route, and the navigation state persists config changes and
  process death.

### Conditional navigation

* *[Conditional navigation](/guide/navigation/navigation-3/recipes/conditional)*: Switch to a different navigation flow when
  a condition is met. For example, for authentication or first-time user
  onboarding.

### Architecture

* *[Hilt - Modularized navigation code](/guide/navigation/navigation-3/recipes/modular)*: Demonstrates how to decouple
  navigation code into separate modules (uses Dagger/Hilt for DI).

### Working with ViewModel

#### Passing navigation arguments

* *[Basic ViewModel](/guide/navigation/navigation-3/recipes/passingarguments)*: Navigation arguments are passed to a `ViewModel`
  constructed using `viewModel()`

### Returning results

* *[Returning Results as Events](/guide/navigation/navigation-3/recipes/results-event)*: Returning results as events to
  content in another `NavEntry`
* *[Returning Results as State](/guide/navigation/navigation-3/recipes/results-state)*: Returning results as state stored in a
  `CompositionLocal`