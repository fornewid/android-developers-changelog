---
title: https://developer.android.com/guide/navigation/backstack
url: https://developer.android.com/guide/navigation/backstack
source: md.txt
---

# Navigation and the back stack

The`NavController`holds a "back stack" that contains the destinations the user has visited. As the user navigates to screens throughout your app, the`NavController`adds and removes destinations to and from the back stack.

In being a stack, the back stack is a "last in, first out" data structure. The`NavController`therefore pushes items to and pops items from the top of the stack.
| **Important:** As the back stack is fundamentally a part of the`NavController`class, its behavior is consistent regardless of which UI framework you use.

## Basic behavior

These are the core facts you should consider regarding the behavior of the back stack:

- **First destination:** When the user opens the app, the`NavController`pushes the first destination to the top of the back stack.
- **Pushing to the stack:** Each call[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(int))pushes the given destination to the top of the stack.
- **Popping top destination:** Tapping**Up** or**Back** calls the[`NavController.navigateUp()`](https://developer.android.com/reference/androidx/navigation/NavController#navigateUp())and[`NavController.popBackStack()`](https://developer.android.com/reference/androidx/navigation/NavController#popBackStack())methods, respectively. They pop the top destination off the stack. See the[Principles of Navigation](https://developer.android.com/guide/navigation/principles)page for more information about the difference between**Up** and**Back**.

## Pop back

The[`NavController.popBackStack()`](https://developer.android.com/reference/androidx/navigation/NavController#popBackStack())method attempts to pop the current destination off the back stack and navigate to the previous destination. This effectively moves the user back one step in their navigation history. It returns a boolean indicating whether it successfully popped back to the destination.

### Pop back to a particular destination

You can also use`popBackStack()`to navigate to a particular destination. To do so, use one of its overloads. There are several that allow you to pass in an identifier, such as an integer`id`or a string`route`. These overloads take the user to the destination associated with the given identifier. Critically, they pop everything on the stack above that destination.

These overloads also take an`inclusive`boolean. It determines whether the`NavController`should also pop the specified destination off the back stack after having navigated to it.

Consider this brief snippet for an example:  

    navController.popBackStack(R.id.destinationId, true)

Here the`NavController`pops back to the destination with the integer id`destinationId`. As the value of the`inclusive`argument is`true`, the`NavController`also pops the given destination from the back stack.

### Handle a failed pop back

When the`popBackStack()`returns`false`, a subsequent call to`NavController.getCurrentDestination()`returns`null`. This means the app has popped the last destination off the back stack. In this case, the user sees only a blank screen.

This can occur in the following cases:

- `popBackStack()`did not pop anything from the stack.
- `popBackStack()`did pop a destination off the back stack and the stack is now empty.

To resolve this, you must then navigate to a new destination or call`finish()`on your activity to end it. The following snippet demonstrates this:  

### kotlin

    ...

    if (!navController.popBackStack()) {
        // Call finish() on your Activity
        finish()
    }

### java

    ...

    if (!navController.popBackStack()) {
        // Call finish() on your Activity
        finish();
    }

| **Note:** The most common case when`popBackStack()`returns`false`is when you have manually popped the start destination off the back stack as that should be the last destination left on the back stack.

## Pop up to a destination

To remove destinations from the back stack when navigating from one destination to another, add a`popUpTo()`argument to the associated`navigate()`function call.`popUpTo()`instructs the Navigation library to remove some destinations from the back stack as part of the call to`navigate()`. The parameter value is the identifier of a destination on the back stack. The identifier can be an integer`id`or string`route`.

You can include an argument for the`inclusive`parameter with a value of`true`to indicate that the destination you have specified in`popUpTo()`should also pop off back stack.

To implement this programmatically, pass`popUpTo()`to`navigate()`as part of[`NavOptions`](https://developer.android.com/guide/navigation/use-graph/navoptions)with`inclusive`set to`true`. This works in both Compose and Views.
| **Note:** In Views, add an`app:popUpTo`attribute to the associated`<action>`element. Set the inclusive parameter with the`app:popUpToInclusive="true"`attribute.

### Save state when popping up

When you use`popUpTo`to navigate to a destination, you can optionally save the back stack and the states of all destinations popped off the back stack. You can then restore the back stack and destinations when navigating to that destination at a later time. This lets you preserve state for a given destination and have[multiple back stacks](https://developer.android.com/guide/navigation/backstack/multi-back-stacks).

To do this programmatically, specify`saveState = true`when adding`popUpTo`to your navigation options.

You can also specify`restoreState = true`in your navigation options to automatically restore the back stack and the state associated with the destination.

For example:  

    navController.navigate(
        route = route,
        navOptions =  navOptions {
            popUpTo<A>{ saveState = true }
            restoreState = true
        }
    )

To enable saving and restoring state in XML, define`popUpToSaveState`as`true`and`restoreState`as`true`respectively in the associated`action`.

### XML example

Here is an example of`popUpTo`in XML, using an action:  

    <action
      android:id="@+id/action_a_to_b"
      app:destination="@id/b"
      app:popUpTo="@+id/a"
      app:popUpToInclusive="true"
      app:restoreState="true"
      app:popUpToSaveState="true"/>

### Compose example

The following is a complete example of the same in Compose:  

    @Composable
    fun MyAppNavHost(
        modifier: Modifier = Modifier,
        navController: NavHostController = rememberNavController(),
        startDestination: Any = A
    ) {
        NavHost(
            modifier = modifier,
            navController = navController,
            startDestination = startDestination
        ) {
            composable<A> {
                DestinationA(
                    onNavigateToB = {
                    // Pop everything up to, and including, the A destination off
                    // the back stack, saving the back stack and the state of its
                    // destinations.
                    // Then restore any previous back stack state associated with
                    // the B destination.
                    // Finally navigate to the B destination.
                        navController.navigate(route = B) {
                            popUpTo<A> {
                                inclusive = true
                                saveState = true
                            }
                            restoreState = true
                        }
                    },
                )
            }
            composable<B> { DestinationB(/* ... */) }
        }
    }

    @Composable
    fun DestinationA(onNavigateToB: () -> Unit) {
        Button(onClick = onNavigateToB) {
            Text("Go to A")
        }
    }

More granularly, you can change how you call`NavController.navigate()`in the following ways:  

    // Pop everything up to the destination_a destination off the back stack before
    // navigating to the "destination_b" destination
    navController.navigate("destination_b") {
        popUpTo("destination_a")
    }

    // Pop everything up to and including the "destination_a" destination off
    // the back stack before navigating to the "destination_b" destination
    navController.navigate("destination_b") {
        popUpTo("destination_a") { inclusive = true }
    }

    // Navigate to the "search" destination only if we're not already on
    // the "search" destination, avoiding multiple copies on the top of the
    // back stack
    navController.navigate("search") {
        launchSingleTop = true
    }

For general information about passing options to`NavController.navigate()`, see the[Navigate with options guide](https://developer.android.com/guide/navigation/use-graph/navoptions).

## Pop using actions

When navigating using an action, you can optionally pop additional destinations off of the back stack. For example, if your app has an initial login flow, once a user has logged in, you should pop all of the login-related destinations off of the back stack so that the Back button doesn't take users back into the login flow.

## Additional reading

For more information, read the following pages:

- **[Circular navigation](https://developer.android.com/guide/navigation/backstack/circular)**: Learn how you can avoid an overstuffed back stack in cases where navigation flows are circular.
- **[Dialog destinations](https://developer.android.com/guide/navigation/backstack/dialog)**: Read about how dialog destinations introduce unique considerations to how you manage your back stack.