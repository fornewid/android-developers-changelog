---
title: https://developer.android.com/guide/navigation/use-graph/navoptions
url: https://developer.android.com/guide/navigation/use-graph/navoptions
source: md.txt
---

# Navigate with options

When you define an action in the navigation graph using the Kotlin DSL, Navigation generates a corresponding[`NavAction`](https://developer.android.com/reference/androidx/navigation/NavAction)class, which contains the configurations defined for that action, including the following:

- **[Destination](https://developer.android.com/reference/kotlin/androidx/navigation/NavAction#getDestinationId()):**The resource ID of the target destination.
- **[Default arguments](https://developer.android.com/reference/kotlin/androidx/navigation/NavAction#getDefaultArguments()):** An`android.os.Bundle`containing default values for the target destination, if supplied.
- **[Navigation options](https://developer.android.com/reference/kotlin/androidx/navigation/NavAction#getNavOptions()):** Navigation options, represented as[`NavOptions`](https://developer.android.com/reference/androidx/navigation/NavOptions). This class contains all of the special configuration for transitioning to and back from the target destination, including animation resource configuration, pop behavior, and whether the destination should be launched in single top mode.

## Options with Compose

By default,`navigate()`adds your new destination to the back stack. You can modify the behavior of`navigate()`by passing additional navigation options to your`navigate()`call.

You can create an instance of`NavOptions`using a simple lambda. Pass`navigate()`the arguments you might otherwise explicitly pass to the`NavOptions.Builder`. Consider the following examples:

For examples, see the[back stack guide](https://developer.android.com/guide/navigation/backstack#compose-examples)for examples on how to pass options to`navigate()`in context.
| **Note:** You cannot use[`anim`block](https://developer.android.com/reference/kotlin/androidx/navigation/NavAction#getDefaultArguments())with Navigation Compose. There is a[feature request](https://developer.android.com/reference/kotlin/androidx/navigation/NavAction#getNavOptions())that tracks Transition Animations in Navigation Compose.
| **Note:** The user's current location is already in the back stack. It appears in the back stack when the user first navigates to the destination, not when they navigate away.

## Options with XML

The following is an example graph consisting of two screens along with an action to navigate from one to the other:  

    <?xml version="1.0" encoding="utf-8"?>
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
                xmlns:app="http://schemas.android.com/apk/res-auto"
                xmlns:tools="http://schemas.android.com/tools"
                android:id="@+id/nav_graph"
                app:startDestination="@id/a">

        <fragment android:id="@+id/a"
                  android:name="com.example.myapplication.FragmentA"
                  android:label="a"
                  tools:layout="@layout/a">
            <action android:id="@+id/action_a_to_b"
                    app:destination="@id/b"
                    app:enterAnim="@anim/nav_default_enter_anim"
                    app:exitAnim="@anim/nav_default_exit_anim"
                    app:popEnterAnim="@anim/nav_default_pop_enter_anim"
                    app:popExitAnim="@anim/nav_default_pop_exit_anim"/>
        </fragment>

        <fragment android:id="@+id/b"
                  android:name="com.example.myapplication.FragmentB"
                  android:label="b"
                  tools:layout="@layout/b">
            <action android:id="@+id/action_b_to_a"
                    app:destination="@id/a"
                    app:enterAnim="@anim/nav_default_enter_anim"
                    app:exitAnim="@anim/nav_default_exit_anim"
                    app:popEnterAnim="@anim/nav_default_pop_enter_anim"
                    app:popExitAnim="@anim/nav_default_pop_exit_anim"
                    app:popUpTo="@+id/a"
                    app:popUpToInclusive="true"/>
        </fragment>
    </navigation>

When the navigation graph is inflated, these actions are parsed, and corresponding`NavAction`objects are generated with the configurations defined in the graph. For example,`action_b_to_a`is defined as navigating from destination`b`to destination`a`. The action includes animations along with`popTo`behavior that removes all destinations from the backstack. All of these settings are captured as`NavOptions`and are attached to the`NavAction`.

To follow this`NavAction`, use`NavController.navigate()`, passing the ID of the action, as shown in the following example:  

        navController.navigate(R.id.action_b_to_a)

### Apply options programmatically

The previous examples show how to specify`NavOptions`within the navigation graph XML. However, specific options can vary depending on constraints that are unknown at build time. In such cases, the`NavOptions`must be created and set programmatically, as shown in the following example:  

### Kotlin

    findNavController().navigate(
    R.id.action_fragmentOne_to_fragmentTwo,
    null,
    navOptions { // Use the Kotlin DSL for building NavOptions
        anim {
            enter = android.R.animator.fade_in
            exit = android.R.animator.fade_out
        }
      }
    )

### Java

    NavController navController = NavHostFragment.findNavController(this);
      navController.navigate(
        R.id.action_fragmentOne_to_fragmentTwo,
        null,
        new NavOptions.Builder()
          .setEnterAnim(android.R.animator.fade_in)
          .setExitAnim(android.R.animator.fade_out)
          .build()
      );

This example uses an extended form of[`navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(int,%20android.os.Bundle,%20androidx.navigation.NavOptions))and contains additional`Bundle`and`NavOptions`arguments. All variants of`navigate()`have extended versions that accept a`NavOptions`argument.
| **Note:** `NavOptions`that are applied programmatically override any and all options that have been set in XML.

You can also programmatically apply`NavOptions`when navigating to implicit deep links:  

### Kotlin

    findNavController().navigate(
        deepLinkUri,
        navOptions { // Use the Kotlin DSL for building NavOptions
            anim {
                enter = android.R.animator.fade_in
                exit = android.R.animator.fade_out
            }
        }
    )

### Java

    NavController navController = NavHostFragment.findNavController(this);
    navController.navigate(
            deepLinkUri,
            new NavOptions.Builder()
                    .setEnterAnim(android.R.animator.fade_in)
                    .setExitAnim(android.R.animator.fade_out)
                    .build()
    );

This variant of[`navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate(android.net.Uri,%20androidx.navigation.NavOptions))takes a[`Uri`](https://developer.android.com/reference/android/net/Uri)for the implicit deep link, as well as the`NavOptions`instance.