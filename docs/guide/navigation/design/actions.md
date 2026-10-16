---
title: https://developer.android.com/guide/navigation/design/actions
url: https://developer.android.com/guide/navigation/design/actions
source: md.txt
---

# Use Navigation actions and Fragments

You can build connections between fragments using navigation actions. Evoking a navigation action takes the user from one destination to another. This guide explains what actions are and demonstrates how you can create and use them.
| **Warning:** The navigation actions API is available only when using the views UI framework.

## Overview

Each action has a unique ID and can contain additional attributes, such as a destination. The destination defines the screen to which the app takes the user when they trigger the action. The action can also use arguments to carry data from one destination to another.

- **Safe Args:** Using actions, you can replace resource IDs with[Safe Args-generated operations](https://developer.android.com/guide/navigation/design/actions), providing additional compile-time safety.
- **Animations:** You can also animate transitions between the destinations. For more information, see[Animate transitions between destinations](https://developer.android.com/reference/androidx/navigation/Navigation#createNavigateOnClickListener(int)).

## Examples

Define actions in your navigation graph XML file using the`<action>`tags. The following snippet implements an action that represents a transition from`FragmentA`to`FragmentB`.  

    <fragment
        android:id="@+id/fragmentA"
        android:name="com.example.FragmentA">
        <action
            android:id="@+id/action_fragmentA_to_fragmentB"
            app:destination="@id/fragmentB" />
    </fragment>

### Navigate using an action

To navigate using this action, you call[`NavController.navigate()`](https://developer.android.com/reference/androidx/navigation/NavController#navigate)and pass it the action's`id`:  

    navController.navigate(R.id.action_fragmentA_to_fragmentB)

| **Important:** For more information about how to use`NavController.navigate()`and its various overloads, see the[Navigate to a destination](https://developer.android.com/guide/navigation/use-graph/navigate)guide.

## Global actions

You can use global actions to navigate to a destination from anywhere.

For any destination in your app that is accessible through more than one path, define a corresponding global action that navigates to that destination.

Consider the following example. The`results_winner`and`game_over`destinations both need to pop up to the home destination. The`action_pop_out_of_game`action provides the ability to do so;`action_pop_out_of_game`is a global action outside of any specific fragment. That means you can reference and call it anywhere within the`in_game_nav_graph`.  

    <?xml version="1.0" encoding="utf-8"?>
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
       xmlns:app="http://schemas.android.com/apk/res-auto"
       android:id="@+id/in_game_nav_graph"
       app:startDestination="@id/in_game">

       <!-- Action back to destination which launched into this in_game_nav_graph -->
       <action android:id="@+id/action_pop_out_of_game"
                           app:popUpTo="@id/in_game_nav_graph"
                           app:popUpToInclusive="true" />

       <fragment
           android:id="@+id/in_game"
           android:name="com.example.android.gamemodule.InGame"
           android:label="Game">
           <action
               android:id="@+id/action_in_game_to_resultsWinner"
               app:destination="@id/results_winner" />
           <action
               android:id="@+id/action_in_game_to_gameOver"
               app:destination="@id/game_over" />
       </fragment>

       <fragment
           android:id="@+id/results_winner"
           android:name="com.example.android.gamemodule.ResultsWinner" />

       <fragment
           android:id="@+id/game_over"
           android:name="com.example.android.gamemodule.GameOver"
           android:label="fragment_game_over"
           tools:layout="@layout/fragment_game_over" />

    </navigation>