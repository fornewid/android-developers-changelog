---
title: ViewModel Scoping APIs  |  App architecture  |  Android Developers
url: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-apis
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Design & Plan](https://developer.android.com/design)
* [App architecture](https://developer.android.com/topic/architecture/intro)

Stay organized with collections

Save and categorize content based on your preferences.



# ViewModel Scoping APIs   Part of [Android Jetpack](/jetpack).

Scope is key to using ViewModels effectively. Each ViewModel is scoped to an
object that implements the [`ViewModelStoreOwner`](/reference/androidx/lifecycle/ViewModelStoreOwner) interface. There are
several APIs that allow you to more easily manage the scope of your ViewModels.
This document outlines some of the key techniques you should know.

**Note:** For more information on scope and ViewModel lifecycle, see the
[ViewModel Overview](/topic/libraries/architecture/viewmodel#scope).

The `ViewModelProvider.get()` method lets you obtain an instance of a ViewModel
scoped to any `ViewModelStoreOwner`. For Kotlin users, there are different
extension functions available for the most common use cases. All Kotlin
extension function implementations use the ViewModelProvider API under the hood.

## ViewModels scoped to the closest ViewModelStoreOwner

You can scope a ViewModel to an Activity, Fragment, or destination of a
Navigation graph. The
[`viewModels()`](/reference/kotlin/androidx/activity/package-summary#(androidx.activity.ComponentActivity)) extension
functions provided by the Activity, Fragment and Navigation libraries, and the
`viewModel()` function in Compose allows you to get an instance of the ViewModel
scoped to the closest `ViewModelStoreOwner`.

### Views

```
import androidx.activity.viewModels

class MyActivity : AppCompatActivity() {
    // ViewModel API available in activity.activity-ktx
    // The ViewModel is scoped to `this` Activity
    val viewModel: MyViewModel by viewModels()
}

import androidx.fragment.app.viewModels

class MyFragment : Fragment() {
    // ViewModel API available in fragment.fragment-ktx
    // The ViewModel is scoped to `this` Fragment
    val viewModel: MyViewModel by viewModels()
}
```

### Views

```
import androidx.lifecycle.ViewModelProvider;

public class MyActivity extends AppCompatActivity {
    // The ViewModel is scoped to `this` Activity
    MyViewModel viewModel = new ViewModelProvider(this).get(MyViewModel.class);
}

public class MyFragment extends Fragment {
    // The ViewModel is scoped to `this` Fragment
    MyViewModel viewModel = new ViewModelProvider(this).get(MyViewModel.class);
}
```

### Compose

```
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MyScreen(
    modifier: Modifier = Modifier,
    // ViewModel API available in lifecycle.lifecycle-viewmodel-compose
    // The ViewModel is scoped to the closest ViewModelStoreOwner provided
    // via the LocalViewModelStoreOwner CompositionLocal. In order of proximity,
    // this could be the destination of a Navigation graph, the host Fragment,
    // or the host Activity.
    viewModel: MyViewModel = viewModel()
) { /* ... */ }
```

**Note:** If you're using Hilt and Jetpack Compose, replace the `viewModel()` calls
with `hiltViewModel()` as explained in the [Compose + Hilt documentation](/jetpack/compose/libraries#hilt).

## ViewModels scoped to any ViewModelStoreOwner

The `ComponentActivity.viewModels()` and `Fragment.viewModels()` functions in
the View system and the `viewModel()` function in Compose take an optional
`ownerProducer` parameter that you can use to specify to which
`ViewModelStoreOwner` the instance of the ViewModel is scoped to.
The following sample shows how to get an instance of a ViewModel scoped to the
parent fragment:

### Views

```
import androidx.fragment.app.viewModels

class MyFragment : Fragment() {

    // ViewModel API available in fragment.fragment-ktx
    // The ViewModel is scoped to the parent of `this` Fragment
    val viewModel: SharedViewModel by viewModels(
        ownerProducer = { requireParentFragment() }
    )
}
```

### Views

```
import androidx.lifecycle.ViewModelProvider;

public class MyFragment extends Fragment {

    SharedViewModel viewModel;

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        // The ViewModel is scoped to the parent of `this` Fragment
        viewModel = new ViewModelProvider(requireParentFragment())
            .get(SharedViewModel.class);
    }
}
```

### Compose

```
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MyScreen(
    context: Context = LocalContext.current,
    // ViewModel API available in lifecycle.lifecycle-viewmodel-compose
    // The ViewModel is scoped to the parent of the host Fragment
    // where this composable function is called
    viewModel: SharedViewModel = viewModel(
        viewModelStoreOwner = (context as Fragment).requireParentFragment()
    )
) { /* ... */ }
```

Getting an Activity-scoped ViewModel from a Fragment is a common use case. When
doing so, use the [`activityViewModels()`](/reference/kotlin/androidx/fragment/app/package-summary#(androidx.fragment.app.Fragment).activityViewModels(kotlin.Function0,kotlin.Function0))
Views extension function is available. If you're not using Views and Kotlin,
you can use the same APIs as above and by passing the right owner.

### Views

```
import androidx.fragment.app.activityViewModels

class MyFragment : Fragment() {

    // ViewModel API available in fragment.fragment-ktx
    // The ViewModel is scoped to the host Activity
    val viewModel: SharedViewModel by activityViewModels()
}
```

### Views

```
import androidx.lifecycle.ViewModelProvider;

public class MyFragment extends Fragment {

    SharedViewModel viewModel;

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        // The ViewModel is scoped to the host Activity
        viewModel = new ViewModelProvider(requireActivity())
            .get(SharedViewModel.class);
    }
}
```

### Compose

```
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MyScreen(
    context: Context = LocalContext.current,
    // ViewModel API available in lifecycle.lifecycle-viewmodel-compose
    // The ViewModel is scoped to the Activity of the host Fragment
    // where this composable function is called
    viewModel: SharedViewModel = viewModel(
        viewModelStoreOwner = (context as Fragment).requireActivity()
    )
) { /* ... */ }
```

**Note:** If you're using Hilt and Jetpack Compose, replace the `viewModel()` calls
with `hiltViewModel()` as explained in the
[Compose + Hilt documentation](/jetpack/compose/libraries#hilt).

## ViewModels scoped to the Navigation graph

Navigation graphs are also ViewModel store owners. If you're using
[Navigation Fragment](/guide/navigation) or
[Navigation Compose](/jetpack/compose/navigation), you can get an instance of a
ViewModel scoped to a Navigation graph with the
[`navGraphViewModels(graphId)`](/reference/kotlin/androidx/navigation/package-summary#(androidx.fragment.app.Fragment).navGraphViewModels(kotlin.Int,kotlin.Function0,kotlin.Function0))
Views extension function.

### Views

```
import androidx.navigation.navGraphViewModels

class MyFragment : Fragment() {

    // ViewModel API available in navigation.navigation-fragment
    // The ViewModel is scoped to the `nav_graph` Navigation graph
    val viewModel: SharedViewModel by navGraphViewModels(R.id.nav_graph)

    // Equivalent navGraphViewModels code using the viewModels API
    val viewModel: SharedViewModel by viewModels(
        { findNavController().getBackStackEntry(R.id.nav_graph) }
    )
}
```

### Views

```
import androidx.lifecycle.ViewModelProvider;

public class MyFragment extends Fragment {

    SharedViewModel viewModel;

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        NavController navController = NavHostFragment.findNavController(this);
        NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.my_graph);

        // The ViewModel is scoped to the `nav_graph` Navigation graph
        viewModel = new ViewModelProvider(backStackEntry).get(SharedViewModel.class);
    }
}
```

### Compose

```
import androidx.lifecycle.viewmodel.compose.viewModel

@Composable
fun MyAppNavHost() {
    // ...
    composable("myScreen") { backStackEntry ->
        // Retrieve the NavBackStackEntry of "parentNavigationRoute"
        val parentEntry = remember(backStackEntry) {
            navController.getBackStackEntry("parentNavigationRoute")
        }
        // Get the ViewModel scoped to the `parentNavigationRoute` Nav graph
        val parentViewModel: SharedViewModel = viewModel(parentEntry)
        // ...
    }
}
```

If you're using Hilt in addition to Jetpack Navigation, you can use the
[`hiltNavGraphViewModels(graphId)`](/reference/kotlin/androidx/hilt/navigation/fragment/package-summary#hiltnavgraphviewmodels)
API as follows.

### Views

```
import androidx.hilt.navigation.fragment.hiltNavGraphViewModels

class MyFragment : Fragment() {

    // ViewModel API available in hilt.hilt-navigation-fragment
    // The ViewModel is scoped to the `nav_graph` Navigation graph
    // and is provided using the Hilt-generated ViewModel factory
    val viewModel: SharedViewModel by hiltNavGraphViewModels(R.id.nav_graph)
}
```

### Views

```
import androidx.hilt.navigation.HiltViewModelFactory;
import androidx.lifecycle.ViewModelProvider;

public class MyFragment extends Fragment {

    SharedViewModel viewModel;

    @Override
    public void onViewCreated(View view, Bundle savedInstanceState) {
        NavController navController = NavHostFragment.findNavController(this);
        NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.my_graph);

        // The ViewModel is scoped to the `nav_graph` Navigation graph
        // and is provided using the Hilt-generated ViewModel factory
        viewModel = new ViewModelProvider(
            backStackEntry,
            HiltViewModelFactory.create(getContext(), backStackEntry)
        ).get(SharedViewModel.class);
    }
}
```

### Compose

```
import androidx.hilt.navigation.compose.hiltViewModel

@Composable
fun MyAppNavHost() {
    // ...
    composable("myScreen") { backStackEntry ->
        val parentEntry = remember(backStackEntry) {
            navController.getBackStackEntry("parentNavigationRoute")
        }

        // ViewModel API available in hilt.hilt-navigation-compose
        // The ViewModel is scoped to the `parentNavigationRoute` Navigation graph
        // and is provided using the Hilt-generated ViewModel factory
        val parentViewModel: SharedViewModel = hiltViewModel(parentEntry)
        // ...
    }
}
```

## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Layouts and binding expressions](/topic/libraries/data-binding/expressions)
* [ViewModel overview](/topic/libraries/architecture/viewmodel)