---
title: https://developer.android.com/training/wearables/compose/migrate-to-navigation3
url: https://developer.android.com/training/wearables/compose/migrate-to-navigation3
source: md.txt
---

Navigation 3 represents a fundamental shift in how Jetpack Compose handles navigation state and offers significant architectural advantages over Navigation 2.

Understand the architectural changes and steps required to migrate a Wear Compose app from Navigation 2 to Navigation 3.

> [!NOTE]
> **Note:** This guide is intended to be read in conjunction with [the main Navigation
> 3 migration guide](https://developer.android.com/guide/navigation/navigation-3/migration-guide). It focuses on the migration steps specific to Wear OS apps, such as transitioning to the [`SwipeDismissableSceneStrategy`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation3/SwipeDismissableSceneStrategy).

## Key advantages of Navigation 3

- **Direct Back Stack Control** : The [`NavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavBackStack) is fundamentally just a mutable list of [`NavKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavKey) objects, representing the history of screens the user has visited. You control it exactly like you would any Kotlin [`MutableList`](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/-mutable-list/) (`add`, `removeLast`, `clear`). You directly manipulate the list to perform navigation actions, such as adding a key to go forward or removing a key to go back.
- **Compose-First Design**: The back stack is modeled as standard observable state. Modifying your navigation history behaves exactly like updating any other Compose state, automatically triggering recomposition to display the current screen.
- **Type-Safe by Default**: String-based routes are eliminated entirely. Navigation utilizes serializable data objects and data classes.
- **Decoupled Presentations (Scene Strategies)** : The UI transition layer ([`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay) and [`SwipeDismissableSceneStrategy`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation3/SwipeDismissableSceneStrategy)) is entirely separated from the state tracking ([`NavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavBackStack)), enabling simpler integration of built-in Wear OS navigation transitions.

## Migration steps

### 1. Update dependencies

Remove the old `androidx.wear.compose:compose-navigation` dependency and
introduce the new split Navigation 3 dependencies, along with Kotlin
serialization support.

**Remove:**

    implementation("androidx.wear.compose:compose-navigation:...")

**Add:**

    implementation("androidx.navigation3:navigation3-runtime:...") // State logic
    implementation("androidx.navigation3:navigation3-ui:...")      // Display logic
    implementation("androidx.wear.compose:compose-navigation3:...") // Wear gestures
    implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:...") // Requires compiler plugin

### 2. Update destinations to implement `NavKey`

In Navigation 2, you might have used strings or generic objects for routing. In
Navigation 3, you **must** implement the [`NavKey`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavKey) marker interface and
annotate every screen object with `@Serializable`.

*Why is this required?* To guarantee that the back stack can be saved and
restored across process death, the underlying `navigation3-runtime` relies on
[`kotlinx-serialization`](https://kotlinlang.org/api/kotlinx.serialization/) to serialize the state.

**Before (Navigation 2 - Generic Type-Safe Routes):**

```kotlin
sealed class Nav2Screen {
    data object Landing : Nav2Screen()
    data object List : Nav2Screen()
}
```

**After (Navigation 3 - NavKey + Serializable):**

```kotlin
@Serializable
sealed interface MigrationScreen : NavKey {
    @Serializable
    data object Landing : MigrationScreen

    @Serializable
    data object List : MigrationScreen
}
```

### 3. Replace the Routing Logic ([`NavController`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) to `NavBackStack`)

Replace your [`NavController`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController) with a [`NavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/NavBackStack) initialized via
[`rememberNavBackStack`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#rememberNavBackStack). You also need to instantiate the
[`SwipeDismissableSceneStrategy`](https://developer.android.com/reference/kotlin/androidx/wear/compose/navigation3/SwipeDismissableSceneStrategy) specifically for Wear OS.

**Before (Navigation 2):**

```kotlin
val navController = rememberSwipeDismissableNavController()
```

**After (Navigation 3):**

```kotlin
val backStack = rememberNavBackStack(MigrationScreen.Landing as NavKey)
val strategy = rememberSwipeDismissableSceneStrategy<NavKey>()
```

### 4. Replace `NavHost` with `NavDisplay` and the `entryProvider` DSL

The `NavHost` container and its internal `composable("route") { ... }` builder
DSL are replaced by [`NavDisplay`](https://developer.android.com/reference/kotlin/androidx/navigation3/ui/NavDisplay) and the [`entryProvider`](https://developer.android.com/reference/kotlin/androidx/navigation3/runtime/package-summary#entryProvider) `{
entry<Key> { ... } }` DSL.

**Before (Navigation 2):**

```kotlin
SwipeDismissableNavHost(navController = navController, startDestination = "menu") {
    composable("menu") {
        GreetingScreen(
            onShowList = { navController.navigate("list") }
        )
    }
    composable("list") {
        ListScreen()
    }
}
```

**After (Navigation 3):**

```kotlin
NavDisplay(
    backStack = backStack,
    sceneStrategies = listOf(strategy),
    entryProvider = entryProvider {
        entry<MigrationScreen.Landing> {
            GreetingScreen(
                onShowList = { backStack.add(MigrationScreen.List) }
            )
        }
        entry<MigrationScreen.List> {
            ListScreen()
        }
    }
)
```