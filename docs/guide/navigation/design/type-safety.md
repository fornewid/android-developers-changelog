---
title: https://developer.android.com/guide/navigation/design/type-safety
url: https://developer.android.com/guide/navigation/design/type-safety
source: md.txt
---

# Type safety in Kotlin DSL and Navigation Compose

You can use built-in type safe APIs to provide compile-time type safety for your navigation graph. These APIs are available when your app uses the[Navigation Compose](https://developer.android.com/jetpack/compose/navigation)or[Navigation Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl). They are available as of`Navigation
2.8.0`.

These APIs are equivalent to what[Safe Args](https://developer.android.com/guide/navigation/navigation-pass-data#Safe-args)provides to navigation graphs built using XML.

## Define routes

To use type-safe routes in Compose, you first need to define serializable classes or objects that represent your routes.

To define serializable objects use`@Serializable`annotation provided by the[Kotlin Serialization plugin](https://kotlinlang.org/docs/serialization.html). This plugin can be added to your project by[adding these dependencies](https://developer.android.com/guide/navigation#set-up).

Use the following rules to decide what type to use for your route:

- **Object**: Use an object for routes without arguments.
- **Class**: Use a class or data class for routes with arguments.
- **`KClass<T>`** : Use if you don't need to pass arguments, such as a class without parameters, or a class where all parameters have default values
  1. For example:`Profile::class`

In all cases the object or class must be serializable.

For example:  

    // Define a home route that doesn't take any arguments
    @Serializable
    object Home

    // Define a profile route that takes an ID
    @Serializable
    data class Profile(val id: String)

### Build your graph

Next, you need to define your navigation graph. Use the[`composable()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.collections.Map,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))function to define composables as destinations in your navigation graph.  

    NavHost(navController, startDestination = Home) {
         composable<Home> {
             HomeScreen(onNavigateToProfile = { id ->
                 navController.navigate(Profile(id))
             })
         }
         composable<Profile> { backStackEntry ->
             val profile: Profile = backStackEntry.toRoute()
             ProfileScreen(profile.id)
         }
    }

Observe the following in this example:

- `composable()`takes a type parameter. That is,`composable<Profile>`.
- Defining the destination type is a more robust approach than passing a[`route`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.String,kotlin.collections.List,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))[string](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.String,kotlin.collections.List,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))as in`composable("profile")`.
- The route class defines the type of each navigation argument, as in`val id:
  String`, so there's no need for[`NavArgument`](https://developer.android.com/reference/kotlin/androidx/navigation/NavArgument).
- For the profile route, the`toRoute()`extension method recreates the`Profile`object from the[`NavBackStackEntry`](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry)and its arguments.

For more information on how to design your graph in general, see the[Design your Navigation graph](https://developer.android.com/guide/navigation/design)page.

### Navigate to type safe route

Finally, you can navigate to your composable using the[`navigate()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.collections.Map,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))function by passing in the instance of the route:  

    navController.navigate(Profile(id = 123))

This navigates the user to the`composable<Profile>`destination in the navigation graph. Any navigation arguments, such as`id`, can be obtained by reconstructing`Profile`using`NavBackStackEntry.toRoute`and reading its properties.
| **Important:** Because the parameters of the data class are typed, when you pass an instance of that class to`navigate()`, the arguments are necessarily type safe.

### Additional resources

- [Design your navigation graph](https://developer.android.com/guide/navigation/design)
- [Use your navigation graph](https://developer.android.com/guide/navigation/use-graph)