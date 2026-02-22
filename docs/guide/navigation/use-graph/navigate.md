---
title: https://developer.android.com/guide/navigation/use-graph/navigate
url: https://developer.android.com/guide/navigation/use-graph/navigate
source: md.txt
---

# Navigate to a destination

The Navigation component provides a straightforward and generic way of navigating to a destination. This interface supports a range of contexts and UI frameworks. For example, you can use the Navigation component with Compose, views, fragments, activities, and even custom UI frameworks.

This guide describes how you can use the Navigation component to navigate to a destination in various contexts.

## Use a NavController

The key type you use to move between destinations is the[`NavController`](https://developer.android.com/reference/androidx/navigation/NavController). See[Create a navigation controller](https://developer.android.com/guide/navigation/navcontroller)for more information on the class itself and how to create an instance of it. This guide details how to use it.

## Navigate

Regardless of which UI framework you use, there is a single function you can use to navigate to a destination:[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(android.net.Uri)).

There are many overloads available for`navigate()`. The overload you should choose corresponds to your exact context. For example, you should use one overload when navigating to a composable and another when navigating to a view.

The following sections outline some of the key`navigate()`overloads you can use.

## Navigate to a composable

To navigate to a composable, you should use[`NavController.navigate<T>`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(kotlin.Any,androidx.navigation.NavOptions,androidx.navigation.Navigator.Extras)). With this overload,`navigate()`takes a single`route`argument for which you pass a type. It serves as the key to a destination.  

    @Serializable
    object FriendsList

    navController.navigate(route = FriendsList)

To navigate to a composable in the navigation graph, first define your`NavGraph`such that[each destination corresponds to a type](https://developer.android.com/guide/navigation/design#compose). For composables, you do so with the`composable()`function.

### Expose events from your composables

When a composable function needs to navigate to a new screen, you shouldn't pass it a reference to the`NavController`so that it can call`navigate()`directly. According to[Unidirectional Data Flow (UDF)](https://developer.android.com/jetpack/compose/architecture#udf)principles, the composable should instead expose an event that the`NavController`handles.

More directly put, your composable should have a parameter of type`() -> Unit`. When you add destinations to your`NavHost`with the[`composable()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.collections.Map,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))function, pass your composable a call to`NavController.navigate()`.

See the following subsection for an example of this.
| **Warning:** Don't pass your`NavController`to your composables. Expose an event as described here.

### Example

As a demonstration of the preceding sections, observe these points in the following snippet:

1. Each destination in the graph is created using a route, which is a serializable object or class describing the data required by that destination.
2. The`MyAppNavHost`composable holds the`NavController`instance.
3. Accordingly, calls to`navigate()`should occur there and not in a lower composable like`ProfileScreen`.
4. `ProfileScreen`contains a button that navigates the user to`FriendsList`when clicked. However, it does not call`navigate()`itself.
5. Instead, the button calls a function that is exposed as the parameter`onNavigateToFriends`.
6. When`MyAppNavHost`adds`ProfileScreen`to the navigation graph, for`onNavigateToFriends`it passes a lambda that calls`navigate(route =
   FriendsList`).
7. This ensures that when the user presses the button`ProfileScreen`, they navigate correctly to`FriendsListScreen`.

    @Serializable
    object Profile
    @Serializable
    object FriendsList

    @Composable
    fun MyAppNavHost(
        modifier: Modifier = Modifier,
        navController: NavHostController = rememberNavController(),
    ) {
        NavHost(
            modifier = modifier,
            navController = navController,
            startDestination = Profile
        ) {
            composable<Profile> {
                ProfileScreen(
                    onNavigateToFriends = { navController.navigate(route = FriendsList) },
                    /*...*/
                )
            }
            composable<FriendsList> { FriendsListScreen(/*...*/) }
        }
    }

    @Composable
    fun ProfileScreen(
        onNavigateToFriends: () -> Unit,
        /*...*/
    ) {
        /*...*/
        Button(onClick = onNavigateToFriends) {
            Text(text = "See friends list")
        }
    }

| **Warning:** You should only call`navigate()`as part of a callback and not as part of your composable itself. This avoids calling`navigate()`on every recomposition.

## Navigate using integer ID

To navigate to a destination using an integer ID, call the[`navigate(int)`](https://developer.android.com/reference/kotlin/androidx/navigation/NavController#navigate(kotlin.Int))overload. It takes the resource ID of either an action or a destination. The following code snippet shows how you can use this overload to navigate to the`ViewTransactionsFragment`:  

### Kotlin

    viewTransactionsButton.setOnClickListener { view ->
      view.findNavController().navigate(R.id.viewTransactionsAction)
    }

### Java

    viewTransactionsButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View view) {
          Navigation.findNavController(view).navigate(R.id.viewTransactionsAction);
      }
    });

When navigating using IDs, you should use[actions](https://developer.android.com/guide/navigation/design/actions)where possible. Actions provide additional information in your navigation graph, visually showing how your destinations connect to each other.
| **Note:** For buttons, there are three variants of[`Navigation.createNavigateOnClickListener()`](https://developer.android.com/reference/androidx/navigation/Navigation#createNavigateOnClickListener(androidx.navigation.NavDirections)). These variants are useful if you're using the Java programming language. If you're using Kotlin,`OnClickListener`is a SAM interface, so you can use a trailing lambda. This approach can be shorter and easier to read than calling`createNavigateOnClickListener()`directly.
| **Note:** To handle other common UI components, such as the top app bar and bottom navigation, see[Update UI components with NavigationUI](https://developer.android.com/guide/navigation/integrations/ui).

## Navigate using NavDeepLinkRequest

To navigate to an[implicit deep link destination](https://developer.android.com/guide/navigation/design/deep-link), use the[`navigate(NavDeepLinkRequest)`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(androidx.navigation.NavDeepLinkRequest))overload. The follow snippet provides an implementation of this method:  

### Kotlin

    val request = NavDeepLinkRequest.Builder
      .fromUri("android-app://androidx.navigation.app/profile".toUri())
      .build()
    findNavController().navigate(request)

### Java

    NavDeepLinkRequest request = NavDeepLinkRequest.Builder
      .fromUri(Uri.parse("android-app://androidx.navigation.app/profile"))
      .build()
    NavHostFragment.findNavController(this).navigate(request)

Unlike navigation using action or destination IDs, you can navigate to any deep link in your graph, regardless of whether the destination is visible. You can navigate to a destination on the current graph or a destination on a completely different graph.
| **Caution:** When navigating using`NavDeepLinkRequest`, the back stack does*not* reset. This behavior is unlike other forms of[deep link navigation](https://developer.android.com/guide/navigation/design/deep-link). However,`popUpTo()`and`popUpToInclusive()`still remove destinations from the back stack just as though you had navigated using an ID.
| **Note:** For convenience, you can also use[`navigate(Uri)`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(android.net.Uri)), which wraps a`Uri`in a`DeepLinkRequest`.

### Actions and MIME types

In addition to`Uri`,[`NavDeepLinkRequest`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkRequest)also supports deep links with actions and MIME types. To add an action to the request, use[`fromAction()`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkRequest.Builder#fromAction(java.lang.String))or[`setAction()`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkRequest.Builder#setAction(java.lang.String)). To add a MIME type to a request, use[`fromMimeType()`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkRequest.Builder#fromMimeType(java.lang.String))or[`setMimeType()`](https://developer.android.com/reference/androidx/navigation/NavDeepLinkRequest.Builder#setMimeType(java.lang.String)).

For a`NavDeepLinkRequest`to properly match an implicit deep link destination, the URI, action, and MIME type must all match the`NavDeepLink`in the destination. URIs must match the pattern, the actions must be an exact match, and the MIME types must be related. For example,`image/jpg`matches with`image/\*`

## Further contexts

This document covers how to use[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(int))in the most common use cases. However, the function has a range of overloads that you can use in different contexts, and in tandem with any Ui framework. See the reference documentation for more detail on these overloads.

## Further reading

For more information, see the following pages:

- [Create a navigation controller](https://developer.android.com/reference/androidx/navigation/NavController)
- [Navigation and the back stack](https://developer.android.com/guide/navigation/backstack)
- [Navigate with options](https://developer.android.com/guide/navigation/use-graph/navoptions)
- [Type safety in Kotlin DSL and Navigation Compose](https://developer.android.com/guide/navigation/design/type-safety#type-safe)