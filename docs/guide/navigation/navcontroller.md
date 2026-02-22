---
title: https://developer.android.com/guide/navigation/navcontroller
url: https://developer.android.com/guide/navigation/navcontroller
source: md.txt
---

# Create a navigation controller

The navigation controller is one of the[key concepts](https://developer.android.com/guide/navigation#types)in navigation. It holds the navigation graph and exposes methods that allow your app to move between the destinations in the graph.

When using the[Navigation component](https://developer.android.com/reference/androidx/navigation/package-summary), you create a navigation controller using the[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController)class.[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController)is the central navigation API. It tracks which destinations the user has visited, and allows the user to move between destinations. This guide demonstrates how to create a`NavController`in your app.

For information on how to add a navigation graph to your`NavController`, see[Design your navigation graph](https://developer.android.com/guide/navigation/design).`NavController`provides a few different ways to navigate to the destinations in its graph. For more, see[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate).
| **Note:** Each`NavHost`you create has its own corresponding`NavController`. The`NavController`provides access to the`NavHost`'s graph.

## Compose

To create a`NavController`when using Jetpack Compose, call[`rememberNavController()`](https://developer.android.com/reference/kotlin/androidx/navigation/compose/package-summary#rememberNavController(kotlin.Array)):  

    val navController = rememberNavController()

You should create the`NavController`high in your composable hierarchy. It needs to be high enough that all the composables that need to reference it can do so.

Doing so lets you to use the`NavController`as the single source of truth for updating composables outside of your screens. This follows the principles of[state hoisting](https://developer.android.com/jetpack/compose/state#state-hoisting).

## Views

If you are using the Views UI framework, you can retrieve your NavController using one of the following methods depending on the context:

**Kotlin:**

- [`Fragment.findNavController()`](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/package-summary#(androidx.fragment.app.Fragment).findNavController())
- [`View.findNavController()`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#%28android.view.View%29.findNavController%28%29)
- [`Activity.findNavController(viewId: Int)`](https://developer.android.com/reference/kotlin/androidx/navigation/package-summary#(android.app.Activity).findNavController(kotlin.Int))

**Java:**

- [`NavHostFragment.findNavController(Fragment)`](https://developer.android.com/reference/androidx/navigation/fragment/NavHostFragment#findNavController(androidx.fragment.app.Fragment))
- [`Navigation.findNavController(Activity, @IdRes int viewId)`](https://developer.android.com/reference/androidx/navigation/Navigation#findNavController(android.app.Activity,%20int))
- [`Navigation.findNavController(View)`](https://developer.android.com/reference/androidx/navigation/Navigation#findNavController(android.view.View))

Typically, you first get a`NavHostFragment`, and then retrieve the`NavController`from the fragment. The following snippet demonstrates this:  

### Kotlin

    val navHostFragment =
        supportFragmentManager.findFragmentById(R.id.nav_host_fragment) as NavHostFragment
    val navController = navHostFragment.navController

### Java

    NavHostFragment navHostFragment =
        (NavHostFragment) getSupportFragmentManager().findFragmentById(R.id.nav_host_fragment);
    NavController navController = navHostFragment.getNavController();

| **Warning:** You can encounter problems when creating the`NavHostFragment`using`FragmentContainerView`or when manually adding the`NavHostFragment`to your activity using a`FragmentTransaction`. If you do so, you can cause`Navigation.findNavController(Activity, @IdRes int)`to fail if you attempt to retrieve the`NavController`in`onCreate()`. You should retrieve the`NavController`directly from the`NavHostFragment`instead, as in the preceding example.

## Further reading

- **[Design your navigation graph](https://developer.android.com/guide/navigation/design):** A guide detailing how to add a graph to your`NavController`that contains all the destinations in your app.
- **[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate):** A guide detailing how to use the`NavController`to move between destinations in your navigation graph.