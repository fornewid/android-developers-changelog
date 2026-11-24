---
title: https://developer.android.com/agents/skills/navigation/navigation-3/skill
url: https://developer.android.com/agents/skills/navigation/navigation-3/skill
source: md.txt
---

*** ** * ** ***

## Migration guide

- *[Navigation 2 to Navigation 3 migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide.md.txt)*: Step-by-step guide to migrate an Android application from Navigation 2 to Navigation 3, covering dependency updates, route changes, state management, and UI component replacements.

### Requirements

- *[Guide: Migrate to type-safe navigation in Compose](https://developer.android.com/guide/navigation/type-safe-destinations.md.txt)* : Step-by-step guide to migrating an Android application from string-based navigation to **Type-Safe Navigation** in Jetpack Compose using Jetpack Navigation 2.

## Developer documentation

- *[Navigation 3](https://developer.android.com/guide/navigation/navigation-3.md.txt)*. Search documentation for more information on basics, saving and managing navigation state, modularizing navigation code, creating custom layouts using Scenes, animating between destinations, or applying logic or wrappers to destinations.

## Recipes

Code examples showcasing common patterns.

### Basic API usage

- *[Basic](https://developer.android.com/guide/navigation/navigation-3/recipes/basic.md.txt)*: Shows most basic API usage.
- *[Saveable back stack](https://developer.android.com/guide/navigation/navigation-3/recipes/basicsaveable.md.txt)*: Shows basic API usage with a persistent back stack.
- *[Entry provider DSL](https://developer.android.com/guide/navigation/navigation-3/recipes/basicdsl.md.txt)*: Shows basic API usage using the entryProvider DSL.
- *[Basic Parcelable](https://developer.android.com/guide/navigation/navigation-3/recipes/basicparcelable.md.txt)*: Shows how to use Parcelable with Navigation 3 arguments.

### Common UI

- *[Common UI](https://developer.android.com/guide/navigation/navigation-3/recipes/common-ui.md.txt)*: Demonstrates how to implement a common navigation UI pattern with a bottom navigation bar and multiple back stacks, where each tab in the navigation bar has its own navigation history.

### Deep links

- *[Static URI](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-staticuri.md.txt)*: Shows how to handle simple static URI deep links.
- *[URI with Arguments](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-uriarguments.md.txt)*: Shows how to parse path and query arguments from a deep link.
- *[Synthetic BackStack](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-syntheticbackstack.md.txt)*: Shows how to handle deep links with a synthetic back stack.
- *[Custom Matcher](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-custommatcher.md.txt)*: Shows how to implement custom deep link matching logic.
- *[Custom Serializer](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-serializer.md.txt)*: Shows how to use a custom DeepLinkSerializer with Kotlinx Serialization to parse non-primitive deep link arguments.
- *[Composite Filter](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-compositefilter.md.txt)*: Shows how to combine multiple DeepLinkMatcher.Filter instances using infix operator functions.
- *[DeepLinkKey](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-deeplinkkey.md.txt)*: Shows how to associate deep link URI pattern templates with navigation keys using a DeepLinkKey interface.

### Scenes

#### Use built-in Scenes

- *[Dialog](https://developer.android.com/guide/navigation/navigation-3/recipes/dialog.md.txt)*: Shows how to create a Dialog.

#### Create custom Scenes

- *[BottomSheet](https://developer.android.com/guide/navigation/navigation-3/recipes/bottomsheet.md.txt)*: Shows how to create a BottomSheet destination.
- *[List-Detail Scene](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-listdetail.md.txt)*: Demonstrates how to implement adaptive list-detail layouts using the Navigation 3 Scenes API.
- *[Two pane Scene](https://developer.android.com/guide/navigation/navigation-3/recipes/scenes-twopane.md.txt)*: Demonstrates how to implement adaptive two-pane layouts using the Navigation 3 Scenes API.

#### Scene decorators

- *[Responsive Navigation Scene Decorator](https://developer.android.com/guide/navigation/navigation-3/recipes/navscenedecorator.md.txt)*: Shows how to use NavigationSceneDecorator to implement responsive navigation UI.
- *[Dialog Scene Decorator](https://developer.android.com/guide/navigation/navigation-3/recipes/dialogscenedecorator.md.txt)*: Shows how to use DialogSceneDecorator in Jetpack Compose.

### Material Adaptive

- *[Material List-Detail](https://developer.android.com/guide/navigation/navigation-3/recipes/material-listdetail.md.txt)*: Demonstrates how to implement an adaptive list-detail layout using Material 3 Adaptive.
- *[Material Supporting Pane](https://developer.android.com/guide/navigation/navigation-3/recipes/material-supportingpane.md.txt)*: Demonstrates how to implement an adaptive supporting pane layout using Material 3 Adaptive.

### Animations

- *[Animations](https://developer.android.com/guide/navigation/navigation-3/recipes/animations.md.txt)*: Shows how to override the default animations for all destinations and a single destination.
- *[Conditional Transitions](https://developer.android.com/guide/navigation/navigation-3/recipes/conditional-transitions.md.txt)*: Shows how to implement conditional transition animations.

### Common back stack behavior

- *[Multiple back stacks](https://developer.android.com/guide/navigation/navigation-3/recipes/multiple-backstacks.md.txt)*: Shows how to create multiple top level routes, each with its own back stack. Top level routes are displayed in a navigation bar allowing users to switch between them. State is retained for each top level route, and the navigation state persists config changes and process death.
- *[Retain](https://developer.android.com/guide/navigation/navigation-3/recipes/retain.md.txt)*: Shows how to retain values for items on the back stack and implement a custom NavEntryDecorator.

### Conditional navigation

- *[Conditional navigation](https://developer.android.com/guide/navigation/navigation-3/recipes/conditional.md.txt)*: Switch to a different navigation flow when a condition is met. For example, for authentication or first-time user onboarding.

### Lifecycle

- *[Lifecycle Owner](https://developer.android.com/guide/navigation/navigation-3/recipes/lifecycle-owner.md.txt)*: Shows how to use and observe Lifecycle in Navigation 3.

### Architecture

- *[Modularized navigation code (Hilt)](https://developer.android.com/guide/navigation/navigation-3/recipes/modular-hilt.md.txt)*: Demonstrates how to decouple navigation code into separate modules using Hilt or Dagger for DI.
- *[Modularized navigation code (Koin)](https://developer.android.com/guide/navigation/navigation-3/recipes/modular-koin.md.txt)*: Demonstrates how to decouple navigation code into separate modules using Koin for DI.
- *[Dynamic Feature Module](https://developer.android.com/guide/navigation/navigation-3/recipes/dynamicfeature.md.txt)*: Demonstrates how to implement navigation to dynamic feature modules using Play Feature Delivery.

### Working with ViewModel

#### Passing navigation arguments

- *[Basic ViewModel](https://developer.android.com/guide/navigation/navigation-3/recipes/passingarguments.md.txt)* : Navigation arguments are passed to a `ViewModel` constructed using `viewModel()`

#### Sharing ViewModels

- *[Shared ViewModel](https://developer.android.com/guide/navigation/navigation-3/recipes/sharedviewmodel.md.txt)* : Shows how to share a `ViewModel` between different screens using a custom `NavEntryDecorator`.

### Returning results

- *[Returning Results as Events](https://developer.android.com/guide/navigation/navigation-3/recipes/results-event.md.txt)* : Returning results as events to content in another `NavEntry`
- *[Returning Results as State](https://developer.android.com/guide/navigation/navigation-3/recipes/results-state.md.txt)* : Returning results as state stored in a `CompositionLocal`
- *[Returning Results as Serializable State](https://developer.android.com/guide/navigation/navigation-3/recipes/results-serializable.md.txt)*: Returning results as serializable state that survives configuration changes and process death.

### Interoperability

- *[Fragment and View Interop](https://developer.android.com/guide/navigation/navigation-3/recipes/interop.md.txt)* : Shows how to use `AndroidFragment` and `AndroidView` within a Navigation 3 application.