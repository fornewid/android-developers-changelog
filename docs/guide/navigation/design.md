---
title: https://developer.android.com/guide/navigation/design
url: https://developer.android.com/guide/navigation/design
source: md.txt
---

# Design your navigation graph

The[Navigation component](https://developer.android.com/guide/navigation)uses a*navigation graph*to manage your app's navigation. The navigation graph is a data structure that contains each destination within your app and the connections between them.
| **Note:** The navigation graph is distinct from the[back stack](https://developer.android.com/guide/navigation/backstack), which is a stack within the`NavController`that holds destinations the user has recently visited.

## Destination types

There are three general types of destinations: hosted, dialog, and activity. The following table outlines these three destination types and their purposes.

|   Type   |                                                                              Description                                                                              |                                                                                                                                                                                                 Use cases                                                                                                                                                                                                 |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hosted   | Fills the entire navigation host. That is, the size of a hosted destination is the same as the size of the navigation host and previous destinations are not visible. | Main and detail screens.                                                                                                                                                                                                                                                                                                                                                                                  |
| Dialog   | Presents overlay UI components. This UI is not tied to the location of the navigation host or its size. Previous destinations are visible underneath the destination. | Alerts, selections, forms.                                                                                                                                                                                                                                                                                                                                                                                |
| Activity | Represents unique screens or features within the app.                                                                                                                 | Serve as an exit point to the navigation graph that starts a new Android activity that is managed separately from the Navigation component. In modern Android development, an app consists of a single activity. Activity destinations are therefore best used when interacting with third party activities or as part of[the migration process](https://developer.android.com/guide/navigation/migrate). |

This document contains examples of hosted destinations, which are the most common and fundamental destinations. See the following guides for information on the other destinations:

- [Dialog destinations](https://developer.android.com/guide/navigation/design/dialog-destinations)
- [Activity destinations](https://developer.android.com/guide/navigation/design/activity-destinations)

### Frameworks

Although the same general workflow applies in every case, how exactly you create a navigation host and graph depends on the UI framework you use.

- **Compose:** Use the`NavHost`composable. Add a`NavGraph`to it using the[Kotlin DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl). You can create the graph in two ways:
  - **As part of the NavHost:** Construct the navigation graph directly as part of adding the`NavHost`.
  - **Programmatically:** Use the[`NavController.createGraph()`](https://developer.android.com/reference/androidx/navigation/NavController#(androidx.navigation.NavController).createGraph(kotlin.String,kotlin.String,kotlin.Function1))method to create a`NavGraph`and pass it to the`NavHost`directly.
- **Fragments:** When using fragments with the views UI framework, use a`NavHostFragment`as the host. There are several ways to create a navigation graph:
  - **Programmatically:** Use the Kotlin DSL to create a`NavGraph`and directly apply it on the`NavHostFragment`.
    - The`createGraph()`function used with the Kotlin DSL for both fragments and Compose is the same.
  - **XML:**Write your navigation host and graph directly in XML.
  - **Android Studio editor:**Use the GUI editor in Android Studio to create and adjust your graph as an XML resource file.

| **Note:** How you interact with the graph through the`NavController`is similar between frameworks. See the[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate)guide for more details.

## Compose

In Compose, use a serializable object or class to define a*route*. A route describes how to get to a destination, and contains all the information that the destination requires.

Use the`@Serializable`annotation to automatically create the necessary serialization and deserialization methods for your route types. This annotation is provided by the[Kotlin Serialization plugin](https://kotlinlang.org/docs/serialization.html).[Follow these instructions to add this plugin](https://developer.android.com/guide/navigation#set-up).

Once you have defined your routes, use the`NavHost`composable to create your navigation graph. Consider the following example:  

    @Serializable
    object Profile
    @Serializable
    object FriendsList

    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = Profile) {
        composable<Profile> { ProfileScreen( /* ... */ ) }
        composable<FriendsList> { FriendsListScreen( /* ... */ ) }
        // Add more destinations similarly.
    }

1. A serializable object represents each of the two routes,`Profile`and`FriendsList`.
2. The call to the`NavHost`composable passes a`NavController`and a route for the start destination.
3. The lambda passed to the`NavHost`ultimately calls[`NavController.createGraph()`](https://developer.android.com/reference/androidx/navigation/NavController#(androidx.navigation.NavController).createGraph(kotlin.String,kotlin.String,kotlin.Function1))and returns a`NavGraph`.
4. Each route is supplied as a type argument to[`NavGraphBuilder.composable<T>()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.collections.Map,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))which adds the destination to the resulting`NavGraph`.
5. The lambda passed to`composable`is what the`NavHost`displays for that destination.

| **Caution:** Instead of passing a type to`composable()`, you can pass a`route`string or an integer`id`. However, this makes it much more difficult to manage passing additional arguments to the destination.

### Understand the lambda

To better understand the lambda that creates the`NavGraph`, consider that to build the same graph as in the preceding snippet, you could create the`NavGraph`separately using[`NavController.createGraph()`](https://developer.android.com/reference/androidx/navigation/NavController#(androidx.navigation.NavController).createGraph(kotlin.String,kotlin.String,kotlin.Function1))and pass it to the`NavHost`directly:  

    val navGraph by remember(navController) {
      navController.createGraph(startDestination = Profile)) {
        composable<Profile> { ProfileScreen( /* ... */ ) }
        composable<FriendsList> { FriendsListScreen( /* ... */ ) }
      }
    }
    NavHost(navController, navGraph)

| **Important:** A[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController)is associated with a single`NavHost`composable. The`NavHost`provides the`NavController`access to its navigation graph. When you use the`NavController`to navigate to a destination, you cause the`NavController`to interact with its associated`NavHost`.

### Pass arguments

If you need to pass data to a destination, define the route with a class that has parameters. For example, the`Profile`route is a data class with a`name`parameter.  

    @Serializable
    data class Profile(val name: String)

Whenever you need to pass arguments to that destination, you create an instance of your route class, passing the arguments to the class constructor.
| **Note:** Use a`data class`for a route with arguments, and an`object`or`data
| object`for a route with no arguments.

For optional arguments, create nullable fields with a default value.  

    @Serializable
    data class Profile(val nickname: String? = null)

### Obtain route instance

You can obtain the route instance with`NavBackStackEntry.toRoute()`or`SavedStateHandle.toRoute()`. When you create a destination using`composable()`, the`NavBackStackEntry`is available as a parameter.  

    @Serializable
    data class Profile(val name: String)

    val navController = rememberNavController()

    NavHost(navController = navController, startDestination = Profile(name="John Smith")) {
        composable<Profile> { backStackEntry ->
            val profile: Profile = backStackEntry.toRoute()
            ProfileScreen(name = profile.name) }
    }

Note the following in this snippet:

- The`Profile`route specifies the starting destination in the navigation graph, with`"John Smith"`as the argument for`name`.
- The destination itself is the`composable<Profile>{}`block.
- The`ProfileScreen`composable takes the value of`profile.name`for its own`name`argument.
- As such, the value`"John Smith"`passes through to`ProfileScreen`.

### Minimal example

A complete example of a`NavController`and`NavHost`working together:  

    @Serializable
    data class Profile(val name: String)

    @Serializable
    object FriendsList

    // Define the ProfileScreen composable.
    @Composable
    fun ProfileScreen(
        profile: Profile
        onNavigateToFriendsList: () -> Unit,
      ) {
      Text("Profile for ${profile.name}")
      Button(onClick = { onNavigateToFriendsList() }) {
        Text("Go to Friends List")
      }
    }

    // Define the FriendsListScreen composable.
    @Composable
    fun FriendsListScreen(onNavigateToProfile: () -> Unit) {
      Text("Friends List")
      Button(onClick = { onNavigateToProfile() }) {
        Text("Go to Profile")
      }
    }

    // Define the MyApp composable, including the `NavController` and `NavHost`.
    @Composable
    fun MyApp() {
      val navController = rememberNavController()
      NavHost(navController, startDestination = Profile(name = "John Smith")) {
        composable<Profile> { backStackEntry ->
            val profile: Profile = backStackEntry.toRoute()
            ProfileScreen(
                profile = profile,
                onNavigateToFriendsList = {
                    navController.navigate(route = FriendsList)
                }
            )
        }
        composable<FriendsList> {
          FriendsListScreen(
            onNavigateToProfile = {
              navController.navigate(
                route = Profile(name = "Aisha Devi")
              )
            }
          )
        }
      }
    }

As the snippet demonstrates, instead of passing the`NavController`to your composables, expose an event to the`NavHost`. That is, your composables should have a parameter of type`() -> Unit`for which the`NavHost`passes a lambda that calls`NavController.navigate()`.
| **Note:** By using the parameters of the route class you can pass data to the given destination with full type safety. For example, in the previous code`Profile.name`ensures that`name`is always a`String`.

## Fragments

As outlined in the preceding sections, when using fragments you have the option to create a navigation graph programmatically using the Kotlin DSL, XML, or the Android Studio editor.

The following sections detail these different approaches.
| **Note:** The Navigation component is designed for apps that have one main activity with multiple fragment destinations. The main activity is associated with a navigation graph and contains a`NavHostFragment`that is responsible for swapping destinations as needed. In an app with multiple activity destinations, each activity has its own navigation graph.

### Programmatically

The Kotlin DSL provides a programmatic way of creating a navigation graph with fragments. In many ways this is neater and more modern than using an XML resource file.

Consider the following example, which implements a two-screen navigation graph.

First it is necessary to create the`NavHostFragment`, which must*not* include an`app:navGraph`element:  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <androidx.fragment.app.FragmentContainerView
            android:id="@+id/nav_host_fragment"
            android:name="androidx.navigation.fragment.NavHostFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent" />
    </FrameLayout>

Next, pass the`id`of the`NavHostFragment`to[`NavController.findNavController`](https://developer.android.com/reference/androidx/navigation/Navigation#findNavController(android.view.View))(). This associates the NavController with the`NavHostFragment`.

Subsequently, the call to[`NavController.createGraph()`](https://developer.android.com/reference/androidx/navigation/NavController#(androidx.navigation.NavController).createGraph(kotlin.String,kotlin.String,kotlin.Function1))links the graph to the`NavController`and consequently also to the`NavHostFragment`:  

    @Serializable
    data class Profile(val name: String)

    @Serializable
    object FriendsList

    // Retrieve the NavController.
    val navController = findNavController(R.id.nav_host_fragment)

    // Add the graph to the NavController with `createGraph()`.
    navController.graph = navController.createGraph(
        startDestination = Profile(name = "John Smith")
    ) {
        // Associate each destination with one of the route constants.
        fragment<ProfileFragment, Profile> {
            label = "Profile"
        }

        fragment<FriendsListFragment, FriendsList>() {
            label = "Friends List"
        }

        // Add other fragment destinations similarly.
    }

Using the DSL in this way is very similar to the workflow outlined in the preceding section on[Compose](https://developer.android.com/guide/navigation/design#compose). For example, both there and here, the`NavController.createGraph()`function generates the`NavGraph`. Likewise, while`NavGraphBuilder.composable()`adds composable destinations to the graph, here[`NavGraphBuilder.fragment()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).fragment(kotlin.Int))adds a fragment destination.

For more information on how to use the Kotlin DSL, see[Build a graph with the NavGraphBuilder DSL](https://developer.android.com/guide/navigation/navigation-kotlin-dsl).

### XML

You can directly write the XML yourself. The following example mirrors and is equivalent to the two-screen example from the preceding section.

First, create a`NavHostFragment`. This serves as the navigation host which contains the actual navigation graph.

A minimal implementation of a`NavHostFragment`:  

    <FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">

        <androidx.fragment.app.FragmentContainerView
            android:id="@+id/nav_host_fragment"
            android:name="androidx.navigation.fragment.NavHostFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:navGraph="@navigation/nav_graph" />

    </FrameLayout>

The`NavHostFragment`contains the attribute`app:navGraph`. Use this attribute to connect your navigation graph to the navigation host. The following is an example of how you might implement the graph:  

    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        android:id="@+id/nav_graph"
        app:startDestination="@id/profile">

        <fragment
            android:id="@+id/profile"
            android:name="com.example.ProfileFragment"
            android:label="Profile">

            <!-- Action to navigate from Profile to Friends List. -->
            <action
                android:id="@+id/action_profile_to_friendslist"
                app:destination="@id/friendslist" />
        </fragment>

        <fragment
            android:id="@+id/friendslist"
            android:name="com.example.FriendsListFragment"
            android:label="Friends List" />

        <!-- Add other fragment destinations similarly. -->
    </navigation>

You use actions to define the connections between different destinations. In this example, the`profile`fragment contains an action that navigates to`friendslist`. For more information, see[Use Navigation actions and fragments](https://developer.android.com/guide/navigation/design/actions).
| **Note:** The DSL example does not define actions because they don't apply in that context. When using the DSL,[use`NavController.navigate()`directly](https://developer.android.com/guide/navigation/design/kotlin-dsl#host).

### Editor

You can manage your app's navigation graph using the Navigation Editor in Android Studio. This is essentially a GUI you can use to create and edit your`NavigationFragment`XML, as seen in the preceding section.

For more information, see[Navigation editor](https://developer.android.com/guide/navigation/design/editor).

## Nested graphs

You can also use nested graphs. This involves using a graph as a navigation destination. For more information, see[Nested graphs](https://developer.android.com/guide/navigation/design/nested-graphs).

## Further Reading

For more core navigation concepts, see the following guides:

- **[Overview](https://developer.android.com/guide/navigation):**Make sure to read the general overview of the Navigation component.
- **[Activity destinations](https://developer.android.com/guide/navigation/design/activity-destinations):**Examples of how to implement destinations that take the user to activities.
- **[Dialog destinations](https://developer.android.com/guide/navigation/design/dialog-destinations):**Examples of how to create destinations that take the user to a dialog.
- **[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate):**A detailed guide that covers how to navigate from one destination to another.
- **[Nested graphs](https://developer.android.com/guide/navigation/design/nested-graphs):**An in-depth guide on how to nest one navigation graph within another.