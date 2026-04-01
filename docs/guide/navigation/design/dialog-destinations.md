---
title: https://developer.android.com/guide/navigation/design/dialog-destinations
url: https://developer.android.com/guide/navigation/design/dialog-destinations
source: md.txt
---

# Dialog destinations

In Android navigation, the term*dialog destination*refers to destinations within the app's navigation graph which take the form of dialog windows, overlaying app UI elements and content.

Because dialog destinations appear over[hosted destinations](https://developer.android.com/guide/navigation/design)that fill the navigation host, there are some important considerations regarding how dialog destinations interact with your[`NavController`'s back stack](https://developer.android.com/guide/navigation/backstack/dialog).
| **Note:** Dialog destinations implement the[`FloatingWindow`](https://developer.android.com/reference/androidx/navigation/FloatingWindow)interface. Your app treats any destination that implements this interface as a dialog destination.

## Dialog composable

To create a dialog destination in Compose, add a destination to your`NavHost`using the[`dialog()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).dialog(kotlin.collections.Map,kotlin.Function1))function. The function behaves essentially the same as[`composable`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).composable(kotlin.collections.Map,kotlin.collections.List,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function1,kotlin.Function2))(), only it creates a dialog destination rather than a[hosted destination](https://developer.android.com/guide/navigation/design).

Consider the following example:  

    @Serializable
    object Home
    @Serializable
    object Settings
    @Composable
    fun HomeScreen(onNavigateToSettings: () -> Unit){
        Column {
            Text("Home")
            Button(onClick = onNavigateToSettings){
                Text("Open settings")
            }
        }
    }

    // This screen will be displayed as a dialog
    @Composable
    fun SettingsScreen(){
        Text("Settings")
        // ...
    }

    @Composable
    fun MyApp() {
        val navController = rememberNavController()
        NavHost(navController, startDestination = Home) {
            composable<Home> { HomeScreen(onNavigateToSettings = { navController.navigate(route = Settings) }) }
            dialog<Settings> { SettingsScreen() }
        }
    }

1. The start destination uses the`Home`route. Because`composable()`adds it to the graph, it is a hosted destination.
2. The other destination uses the`Settings`route.
   - Similarly, because`dialog()`adds it to the graph, it is a dialog destination.
   - When the user navigates from`HomeScreen`to`SettingsScreen`the latter appears over`HomeScreen`.
3. Although`SettingsScreen`doesn't include a`Dialog`composable itself, because it is a dialog destination, the`NavHost`displays it within a`Dialog`.

Dialog destinations appear over the previous destination in the`NavHost`. Use them when the dialog represents a separate screen in your app that needs its own lifecycle and saved state, independent of any other destination in your navigation graph. You might prefer to use an[`AlertDialog`](https://developer.android.com/jetpack/compose/components/dialog)or related composable if you want a dialog for a less complex prompt, such as a confirmation.
| **Note:** Because bottom sheets in Compose are not built on`Dialog`, they need their own destination type. See the[Accompanist Navigation Material documentation](https://google.github.io/accompanist/navigation-material/)for an example implementation.

## Kotlin DSL

If you are working with fragments and you are using the[Kotlin DSL](https://developer.android.com/guide/navigation/design/kotlin-dsl)to create your graph, adding a dialog destination is very similar to when using Compose.

Consider how in the following snippet also uses the[`dialog()`](https://developer.android.com/reference/kotlin/androidx/navigation/NavGraphBuilder#(androidx.navigation.NavGraphBuilder).dialog(kotlin.Int))function to add a dialog destination that uses a fragment:  

    // Define destinations with serializable classes or objects
    @Serializable
    object Home
    @Serializable
    object Settings

    // Add the graph to the NavController with `createGraph()`.
    navController.graph = navController.createGraph(
        startDestination = Home
    ) {
        // Associate the home route with the HomeFragment.
        fragment<HomeFragment, Home> {
            label = "Home"
        }

        // Define the settings destination as a dialog using DialogFragment.
        dialog<SettingsFragment, Settings> {
            label = "Settings"
        }
    }

## XML

If you have an existing[`DialogFragment`](https://developer.android.com/reference/androidx/fragment/app/DialogFragment), use the`<dialog>`element to add the dialog to your navigation graph, as shown in the following example:  

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation xmlns:android="http://schemas.android.com/apk/res/android"
            xmlns:app="http://schemas.android.com/apk/res-auto"
            android:id="@+id/nav_graph">

...

<dialog
    android:id="@+id/my_dialog_fragment"
    android:name="androidx.navigation.myapp.MyDialogFragment">
    <argument android:name="myarg" android:defaultValue="@null" />
        <action
            android:id="@+id/myaction"
            app:destination="@+id/another_destination"/>
</dialog>

...

</navigation>
```