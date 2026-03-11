---
title: https://developer.android.com/guide/navigation/navigation-3/skill
url: https://developer.android.com/guide/navigation/navigation-3/skill
source: md.txt
---

## Migration guide

- *[Navigation 2 to Navigation 3 migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide)*: Step-by-step guide to migrate an Android application from Navigation 2 to Navigation 3, covering dependency updates, route changes, state management, and UI component replacements.

### Requirements

- *[Guide: Migrate to type-safe navigation in Compose](https://developer.android.com/guide/navigation/type-safe-destinations)* : Step-by-step guide to migrating an Android application from string-based navigation to **Type-Safe Navigation** in Jetpack Compose using Jetpack Navigation 2.

## Developer documentation

- \*[Navigation 3](https://developer.android.com/guide/navigation/navigation-3). Search documentation for more information on basics, saving and managing navigation state, modularizing navigation code, creating custom layouts using Scenes, animating between destinations, or applying logic or wrappers to destinations.

## Recipes

Code examples showcasing common patterns.

### Basic API usage

- *[Basic](https://developer.android.com/guide/navigation/navigation-3/recipes/basic)*: Shows most basic API usage.
- *[Saveable back stack](https://developer.android.com/guide/navigation/navigation-3/recipes/basicsaveable)*: Shows basic API usage with a persistent back stack.
- *[Entry provider DSL](https://developer.android.com/guide/navigation/navigation-3/recipes/basicdsl)*: Shows basic API usage using the entryProvider DSL.

### Common UI

- *[Common UI](https://developer.android.com/guide/navigation/navigation-3/recipes/common-ui)*: Demonstrates how to implement a common navigation UI pattern with a bottom navigation bar and multiple back stacks, where each tab in the navigation bar has its own navigation history.

### Deep links

- *[Basic](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-basic)*: Shows how to parse a deep link URL from an Android Intent into a navigation key.
- *[Advanced](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-advanced)*: Shows how to handle deep links with a synthetic back stack and correct "Up" navigation behavior.

### Scenes

#### Use built-in Scenes

- *[Dialog](https://developer.android.com/guide/navigation/navigation-3/recipes/dialog)*: Shows how to create a Dialog.

#### Create custom Scenes

- *[BottomSheet](https://developer.android.com/guide/navigation/navigation-3/recipes/bottomsheet)*: Shows how to create a BottomSheet destination.
- *[List-Detail Scene](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-listdetail)*: Demonstrates how to implement adaptive list-detail layouts using the Navigation 3 Scenes API.
- *[Two pane Scene](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-twopane)*: Demonstrates how to implement adaptive two-pane layouts using the Navigation 3 Scenes API.

### Material Adaptive

- *[Material List-Detail](https://developer.android.com/guide/navigation/navigation-3/recipes/material-listdetail)*: Demonstrates how to implement an adaptive list-detail layout using Material 3 Adaptive.
- *[Material Supporting Pane](https://developer.android.com/guide/navigation/navigation-3/recipes/material-supportingpane)*: Demonstrates how to implement an adaptive supporting pane layout using Material 3 Adaptive.

### Animations

- *[Animations](https://developer.android.com/guide/navigation/navigation-3/recipes/animations)*: Shows how to override the default animations for all destinations and a single destination.

### Common back stack behavior

- *[Multiple back stacks](https://developer.android.com/guide/navigation/navigation-3/recipes/multiple-backstacks)*: Shows how to create multiple top level routes, each with its own back stack. Top level routes are displayed in a navigation bar allowing users to switch between them. State is retained for each top level route, and the navigation state persists config changes and process death.

### Conditional navigation

- *[Conditional navigation](https://developer.android.com/guide/navigation/navigation-3/recipes/conditional)*: Switch to a different navigation flow when a condition is met. For example, for authentication or first-time user onboarding.

### Architecture

- *[Modularized navigation code (Hilt)](https://developer.android.com/guide/navigation/navigation-3/recipes/modular-hilt)*: Demonstrates how to decouple navigation code into separate modules using Hilt or Dagger for DI.
- *[Modularized navigation code (Koin)](https://developer.android.com/guide/navigation/navigation-3/recipes/modular-koin)*: Demonstrates how to decouple navigation code into separate modules using Koin for DI.

### Working with ViewModel

#### Passing navigation arguments

- *[Basic ViewModel](https://developer.android.com/guide/navigation/navigation-3/recipes/passingarguments)* : Navigation arguments are passed to a `ViewModel` constructed using `viewModel()`

### Returning results

- *[Returning Results as Events](https://developer.android.com/guide/navigation/navigation-3/recipes/results-event)* : Returning results as events to content in another `NavEntry`
- *[Returning Results as State](https://developer.android.com/guide/navigation/navigation-3/recipes/results-state)* : Returning results as state stored in a `CompositionLocal`