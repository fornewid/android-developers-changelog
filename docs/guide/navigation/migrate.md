---
title: https://developer.android.com/guide/navigation/migrate
url: https://developer.android.com/guide/navigation/migrate
source: md.txt
---

The [Navigation component](https://developer.android.com/topic/libraries/architecture/navigation) is a
library that can manage complex navigation, transition animation, deep linking,
and compile-time checked argument passing between the screens in your app.

This document serves as a general-purpose guide to migrate an existing app to
use the Navigation component.
| **Note:** This documentation uses fragments as examples, as they allow for integration with other [Jetpack lifecycle-aware components](https://developer.android.com/jetpack#android-jetpack-components). In addition to fragments, the Navigation component also supports [custom destinations](https://developer.android.com/topic/libraries/architecture/navigation/navigation-add-new).

At a high level, migration involves these steps:

1. [Move screen-specific UI logic out of activities](https://developer.android.com/guide/navigation/migrate#move) - Move your app's UI
   logic out of activities, ensuring that each activity owns only the logic of
   global navigation UI components, such as a `Toolbar`, while delegating the
   implementation of each screen to a fragment or custom destination.

2. [Integrate the Navigation component](https://developer.android.com/guide/navigation/migrate#integrate) - For each activity, build a
   navigation graph which contains the one or more fragments managed by that
   activity. Replace fragment transactions with Navigation component operations.

3. [Add activity destinations](https://developer.android.com/guide/navigation/migrate#add) - Replace `startActivity()` calls with
   actions using activity destinations.

4. [Combine activities](https://developer.android.com/guide/navigation/migrate#combine) - Combine navigation graphs in cases where
   multiple activities share a common layout.

| **Important:** To ensure success, approach migration as an iterative process, thoroughly testing your app with each step. While a single-activity architecture allows you to take full advantage of the Navigation component, you do not need to fully migrate your app to benefit from Navigation.

## Prerequisites

This guide assumes that you have already migrated your app to use
[AndroidX](https://developer.android.com/jetpack/androidx) libraries. If you have not done so,
[migrate your project](https://developer.android.com/jetpack/androidx/migrate) to use AndroidX before
continuing.

## Move screen-specific UI logic out of activities

| **Note:** This section contains guidance on introducing fragments to an activity-based app. If your app is already using fragments, you can skip ahead to the [Integrate the Navigation component](https://developer.android.com/guide/navigation/migrate#integrate) section.

Activities are system-level components that facilitate a graphical interaction
between your app and Android. Activities are registered in your app's manifest
so that Android knows which activities are available to launch. The activity
class enables your app to react to Android changes as well, such as when your
app's UI is entering or leaving the foreground, rotating, and so on. The
activity can also serve as a place to
[share state between screens](https://developer.android.com/training/basics/fragments/communicating).

Within the context of your app, activities should serve as a host for navigation
and should hold the logic and knowledge of how to transition between screens,
pass data, and so on. However, managing the details of your UI is better left
to a smaller, reusable part of your UI. The recommended implementation for this
pattern is [fragments](https://developer.android.com/guide/components/fragments). See
[Single Activity: Why, When, and How](https://www.youtube.com/watch?v=2k8x8V77CrU)
to learn more about the advantages of using fragments. Navigation supports fragments via the *navigation-fragment* dependency. Navigation also supports
[custom destination types](https://developer.android.com/topic/libraries/architecture/navigation/navigation-add-new).

If your app is not using fragments, the first thing you need to do is migrate
each screen in your app to use a fragment. You aren't removing the activity at
this point. Rather, you're creating a fragment to represent the screen and break
apart your UI logic by responsibility.

### Introducing fragments

To illustrate the process of introducing fragments, let's start with an example
of an application that consists of two screens: a *product list* screen and a
*product details* screen. Clicking on a product in the list screen takes the
user to a details screen to learn more about the product.

![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-migrate-product-details.png)

In this example, the list and details screens are currently separate activities.
| **Note:** As you migrate to a fragment-based architecture, it's important to focus on one screen at a time. You may find it helpful to start from your app's launch screen and work your way through your app. This example focuses on migrating only the list screen.

### Create a New Layout to Host the UI

To introduce a fragment, start by creating a new layout file for the activity to
host the fragment. This replaces the activity's current content view layout.

For a simple view, you can use a `FrameLayout`, as shown in the following
example `product_list_host`:  

    <FrameLayout
       xmlns:app="http://schemas.android.com/apk/res-auto"
       xmlns:android="http://schemas.android.com/apk/res/android"
       android:id="@+id/main_content"
       android:layout_height="match_parent"
       android:layout_width="match_parent" />

The `id` attribute refers to the content section where we later add the
fragment.

Next, in your activity's `onCreate()` function, modify the layout file reference
in your activity's onCreate function to point to this new layout file:

<br />

### Kotlin

```kotlin
class ProductListActivity : AppCompatActivity() {
    ...
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
        // Replace setContentView(R.layout.product_list) with the line below
        setContentView(R.layout.product_list_host)
        ...
    }
}
```

### Java

```java
public class ProductListActivity extends AppCompatActivity {
    ...
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        ...
        // Replace setContentView(R.layout.product_list); with the line below
        setContentView(R.layout.product_list_host);
        ...
    }
}
```

<br />

The existing layout (`product_list`, in this example) is used as the root view
for the fragment you are about to create.

### Create a fragment

Create a new fragment to manage the UI for your screen. It's a good practice to
be consistent with your activity host name. The snippet below uses
`ProductListFragment`, for example:  

### Kotlin

```kotlin
class ProductListFragment : Fragment() {
    // Leave empty for now.
}
```

### Java

```java
public class ProductListFragment extends Fragment {
    // Leave empty for now.
}
```

### Move activity logic into a fragment

With the fragment definition in place, the next step is to move the UI logic for
this screen from the activity into this new fragment. If you are coming from an
activity-based architecture, you likely have a lot of view creation logic
happening in your activity's `onCreate()` function.

Here's an example activity-based screen with UI logic that we need to move:  

### Kotlin

```kotlin
class ProductListActivity : AppCompatActivity() {

    // Views and/or ViewDataBinding references, Adapters...
    private lateinit var productAdapter: ProductAdapter
    private lateinit var binding: ProductListActivityBinding

    ...

    // ViewModels, System Services, other Dependencies...
    private val viewModel: ProductListViewModel by viewModels()

    ...

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // View initialization logic
        DataBindingUtil.setContentView(this, R.layout.product_list_activity)

        // Post view initialization logic
        // Connect adapters
        productAdapter = ProductAdapter(productClickCallback)
        binding.productsList.setAdapter(productAdapter)

        // Initialize view properties, set click listeners, etc.
        binding.productsSearchBtn.setOnClickListener {...}

        // Subscribe to state
        viewModel.products.observe(this, Observer { myProducts ->
            ...
        })

        // ...and so on
    }
   ...
}
```

### Java

```java
public class ProductListActivity extends AppCompatActivity {

    // Views and/or ViewDataBinding references, adapters...
    private ProductAdapter productAdapter;
    private ProductListActivityBinding binding;

    ...

    // ViewModels, system services, other dependencies...
    private ProductListViewModel viewModel;

    ...

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // View initialization logic
        DataBindingUtil.setContentView(this, R.layout.product_list_activity);

        // Post view initialization logic
        // Connect adapters
        productAdapter = new ProductAdapter(productClickCallback);
        binding.productsList.setAdapter(productAdapter);

        // Initialize ViewModels and other dependencies
        ProductListViewModel viewModel = new ViewModelProvider(this).get(ProductListViewModel.java);

        // Initialize view properties, set click listeners, etc.
        binding.productsSearchBtn.setOnClickListener(v -> { ... });

        // Subscribe to state
        viewModel.getProducts().observe(this, myProducts ->
            ...
       );

       // ...and so on
   }
```

Your activity might also be controlling when and how the user navigates to the
next screen, as shown in the following example:  

### Kotlin

```kotlin
    // Provided to ProductAdapter in ProductListActivity snippet.
    private val productClickCallback = ProductClickCallback { product ->
        show(product)
    }

    fun show(product: Product) {
        val intent = Intent(this, ProductActivity::class.java)
        intent.putExtra(ProductActivity.KEY_PRODUCT_ID, product.id)
        startActivity(intent)
    }
```

### Java

```java
// Provided to ProductAdapter in ProductListActivity snippet.
private ProductClickCallback productClickCallback = this::show;

private void show(Product product) {
    Intent intent = new Intent(this, ProductActivity.class);
    intent.putExtra(ProductActivity.KEY_PRODUCT_ID, product.getId());
    startActivity(intent);
}
```

Inside your fragment, you distribute this work between
[`onCreateView()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onCreateView(android.view.LayoutInflater,%20android.view.ViewGroup,%20android.os.Bundle))
and
[`onViewCreated()`](https://developer.android.com/reference/androidx/fragment/app/Fragment#onViewCreated(android.view.View,%20android.os.Bundle)),
with only the navigation logic remaining in the activity:  

### Kotlin

```kotlin
class ProductListFragment : Fragment() {

    private lateinit var binding: ProductListFragmentBinding
    private val viewModel: ProductListViewModel by viewModels()

     // View initialization logic
    override fun onCreateView(inflater: LayoutInflater,
            container: ViewGroup?,
            savedInstanceState: Bundle?): View? {
        binding = DataBindingUtil.inflate(
                inflater,
                R.layout.product_list,
                container,
                false
        )
        return binding.root
    }

    // Post view initialization logic
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // Connect adapters
        productAdapter = ProductAdapter(productClickCallback)
        binding.productsList.setAdapter(productAdapter)

        // Initialize view properties, set click listeners, etc.
        binding.productsSearchBtn.setOnClickListener {...}

        // Subscribe to state
        viewModel.products.observe(this, Observer { myProducts ->
            ...
        })

        // ...and so on
    }

    // Provided to ProductAdapter
    private val productClickCallback = ProductClickCallback { product ->
        if (lifecycle.currentState.isAtLeast(Lifecycle.State.STARTED)) {
            (requireActivity() as ProductListActivity).show(product)
        }
    }
    ...
}
```

### Java

```java
public class ProductListFragment extends Fragment {

    private ProductAdapter productAdapter;
    private ProductListFragmentBinding binding;

    // View initialization logic
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater,
            @Nullable ViewGroup container,
            @Nullable Bundle savedInstanceState) {
        binding = DataBindingUtil.inflate(
                inflater,
                R.layout.product_list_fragment,
                container,
                false);
        return binding.getRoot();
    }

    // Post view initialization logic
    @Override
    public void onViewCreated(@NonNull View view,
            @Nullable Bundle savedInstanceState) {

        // Connect adapters
        binding.productsList.setAdapter(productAdapter);

        // Initialize ViewModels and other dependencies
        ProductListViewModel viewModel = new ViewModelProvider(this)
                .get(ProductListViewModel.class);

        // Initialize view properties, set click listeners, etc.
        binding.productsSearchBtn.setOnClickListener(...)

        // Subscribe to state
        viewModel.getProducts().observe(this, myProducts -> {
            ...
       });

       // ...and so on

    // Provided to ProductAdapter
    private ProductClickCallback productClickCallback = new ProductClickCallback() {
        @Override
        public void onClick(Product product) {
            if (getLifecycle().getCurrentState().isAtLeast(Lifecycle.State.STARTED)) {
                ((ProductListActivity) requireActivity()).show(product);
            }
        }
    };
    ...
}
```

In `ProductListFragment`, notice that there is no call to
[`setContentView()`](https://developer.android.com/reference/android/app/Activity#setContentView(int))
to inflate and connect the layout. In a fragment, `onCreateView()` initializes the
root view. `onCreateView()` takes an instance of a
[`LayoutInflater`](https://developer.android.com/reference/android/view/LayoutInflater) which can be used to
inflate the root view based on a layout resource file. This example reuses the
existing `product_list` layout which was used by the activity because nothing
needs to change to the layout itself.

If you have any UI logic residing in your activity's `onStart()`, `onResume()`,
`onPause()` or `onStop()` functions that are not related to navigation, you can
move those to corresponding functions of the same name on the fragment.
| **Note:** A fragment's lifecycle is managed by its host activity and has additional lifecycle callbacks other than the ones used in this example. Your app might have a reason to override other lifecycle functions, as well. For a complete list of fragment lifecycle functions and when to use them, see the [guide to fragments](https://developer.android.com/guide/components/fragments#Creating).

### Initialize the fragment in the host activity

Once you have moved all of the UI logic down to the fragment, only navigation
logic should remain in the activity.  

### Kotlin

```kotlin
class ProductListActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.product_list_host)
    }

    fun show(product: Product) {
        val intent = Intent(this, ProductActivity::class.java)
        intent.putExtra(ProductActivity.KEY_PRODUCT_ID, product.id)
        startActivity(intent)
    }
}
```

### Java

```java
public class ProductListActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.product_list_host);
    }

    public void show(Product product) {
        Intent intent = new Intent(this, ProductActivity.class);
        intent.putExtra(ProductActivity.KEY_PRODUCT_ID, product.getId());
        startActivity(intent);
    }
}
```

The last step is to create an instance of the fragment in `onCreate()`, just
after setting the content view:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.product_list_host)

    if (savedInstanceState == null) {
        val fragment = ProductListFragment()
        supportFragmentManager
                .beginTransaction()
                .add(R.id.main_content, fragment)
                .commit()
    }
}
```

### Java

```java
@Override
protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.product_list_host);

    if (savedInstanceState == null) {
        ProductListFragment fragment = new ProductListFragment();
        getSupportFragmentManager()
                .beginTransaction()
                .add(R.id.main_content, fragment)
                .commit();
    }
}
```

As shown in this example, `FragmentManager` automatically saves and restores
fragments over configuration changes, so you only need to add the fragment if
the `savedInstanceState` is null.

### Pass intent extras to the fragment

If your activity receives `Extras` through an intent, you can pass these to the
fragment directly as arguments.

In this example, the `ProductDetailsFragment` receives its arguments directly
from the activity's intent extras:  

### Kotlin

```kotlin
...

if (savedInstanceState == null) {
    val fragment = ProductDetailsFragment()

    // Intent extras and Fragment Args are both of type android.os.Bundle.
    fragment.arguments = intent.extras

    supportFragmentManager
            .beginTransaction()
            .add(R.id.main_content, fragment)
            .commit()
}

...
```

### Java

```java
...

if (savedInstanceState == null) {
    ProductDetailsFragment fragment = new ProductDetailsFragment();

    // Intent extras and fragment Args are both of type android.os.Bundle.
    fragment.setArguments(getIntent().getExtras());

    getSupportFragmentManager()
            .beginTransaction()
            .add(R.id.main_content, fragment)
            .commit();
}

...
```

At this point, you should be able to test running your app with the first screen
updated to use a fragment. Continue to migrate the rest of your activity-based
screens, taking time to test after each iteration.

## Integrate the Navigation component

Once you're using a fragment-based architecture, you are ready to start integrating the Navigation component.

First, add the most recent Navigation dependencies to your project, following
the instructions in the
[Navigation library release notes](https://developer.android.com/jetpack/androidx/releases/navigation).

### Create a navigation graph

The Navigation component represents your app's navigation configuration in a
resource file as a graph, much like your app's views are represented. This helps
keep your app's navigation organized outside of your codebase and provides a way
for you to edit your app navigation visually.

To create a navigation graph, start by creating a new resource folder called
`navigation`. To add the graph, right-click on this directory, and choose
**New \> Navigation resource file**.

![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-migrate-new-graph.png)

The Navigation component uses an activity as a
[host for navigation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-implementing)
and swaps individual fragments into that host as your users navigate through
your app. Before you can start to layout out your app's navigation visually, you
need to configure a `NavHost` inside of the activity that is going to host this
graph. Since we're using fragments, we can use the Navigation component's
default `NavHost` implementation,
[`NavHostFragment`](https://developer.android.com/reference/kotlin/androidx/navigation/fragment/NavHostFragment).
| **Note:** If your app uses multiple activities, each activity uses a separate navigation graph. To take full advantage of the Navigation component, your app should use multiple fragments in a single activity. However, activities can still benefit from the Navigation component. Note, however, that your app's UI must be visually broken up across several navigation graphs.

A `NavHostFragment` is configured via a [`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView)
placed inside of a host activity, as shown in the following example:  

    <androidx.fragment.app.FragmentContainerView
       android:name="androidx.navigation.fragment.NavHostFragment"
       app:navGraph="@navigation/product_list_graph"
       app:defaultNavHost="true"
       android:id="@+id/main_content"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />

The `app:NavGraph` attribute points to the navigation graph associated with this
navigation host. Setting this property inflates the nav graph and sets the graph
property on the `NavHostFragment`. The `app:defaultNavHost` attribute ensures
that your `NavHostFragment` intercepts the system Back button.

If you're using top-level navigation such as a `DrawerLayout` or
`BottomNavigationView`, this [`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView)
replaces your main content view element. See
[Update UI components with NavigationUI](https://developer.android.com/topic/libraries/architecture/navigation/navigation-ui)
for examples.

For a simple layout, you can include this [`FragmentContainerView`](https://developer.android.com/reference/androidx/fragment/app/FragmentContainerView)
element as a child of the root `ViewGroup`:  

    <FrameLayout
       xmlns:app="http://schemas.android.com/apk/res-auto"
       xmlns:android="http://schemas.android.com/apk/res/android"
       android:layout_height="match_parent"
       android:layout_width="match_parent">

    <androidx.fragment.app.FragmentContainerView
       android:id="@+id/main_content"
       android:name="androidx.navigation.fragment.NavHostFragment"
       app:navGraph="@navigation/product_list_graph"
       app:defaultNavHost="true"
       android:layout_width="match_parent"
       android:layout_height="match_parent" />

    </FrameLayout>

If you click on the **Design** tab at the bottom, you should see a graph similar
to the one shown below. In the upper left hand side of the graph, under
**Destinations** , you can see a reference to the `NavHost` activity in the form
of `layout_name (resource_id)`.

![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-migrate-nav-editor.png)

Click the plus button
![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-new-destination-icon.png)
near the top to add your fragments to this graph.

The Navigation component refers to individual screens as *destinations* .
Destinations can be fragments, activities, or custom destinations. You can add
any type of destination to your graph, but note that activity destinations are
considered *terminal destinations*, because once you navigate to an activity
destination, you are operating within a separate navigation host and graph.

The Navigation component refers to the way in which users get from one
destination to another as *actions*. Actions can also describe transition
animations and pop behavior.

### Remove fragment transactions

Now that you are using the Navigation component, if you are navigating between fragment-based screens under the same activity, you can remove
[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)
interactions.

If your app is using multiple fragments under the same activity or top-level
navigation such as a drawer layout or bottom navigation, then you are probably
using a `FragmentManager` and
[`FragmentTransactions`](https://developer.android.com/reference/androidx/fragment/app/FragmentTransaction)
to add or replace fragments in the main content section of your UI. This can now
be replaced and simplified using the Navigation component by providing actions
to link destinations within your graph and then navigating using the
`NavController`.

Here are a few scenarios you might encounter along with how you might approach
migration for each scenario.

#### Single activity managing multiple fragments

If you have a single activity that manages multiple fragments, your activity
code might look like this:  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Logic to load the starting destination
        //  when the Activity is first created
        if (savedInstanceState == null) {
            val fragment = ProductListFragment()
            supportFragmentManager.beginTransaction()
                    .add(R.id.fragment_container, fragment, ProductListFragment.TAG)
                    .commit()
        }
    }

    // Logic to navigate the user to another destination.
    // This may include logic to initialize and set arguments on the destination
    // fragment or even transition animations between the fragments (not shown here).
    fun navigateToProductDetail(productId: String) {
        val fragment = new ProductDetailsFragment()
        val args = Bundle().apply {
            putInt(KEY_PRODUCT_ID, productId)
        }
        fragment.arguments = args

        supportFragmentManager.beginTransaction()
                .addToBackStack(ProductDetailsFragment.TAG)
                .replace(R.id.fragment_container, fragment, ProductDetailsFragment.TAG)
                .commit()
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Logic to load the starting destination when the activity is first created.
        if (savedInstanceState == null) {
            val fragment = ProductListFragment()
            supportFragmentManager.beginTransaction()
                    .add(R.id.fragment_container, fragment, ProductListFragment.TAG)
                    .commit();
        }
    }

    // Logic to navigate the user to another destination.
    // This may include logic to initialize and set arguments on the destination
    // fragment or even transition animations between the fragments (not shown here).
    public void navigateToProductDetail(String productId) {
        Fragment fragment = new ProductDetailsFragment();
        Bundle args = new Bundle();
        args.putInt(KEY_PRODUCT_ID, productId);
        fragment.setArguments(args);

        getSupportFragmentManager().beginTransaction()
                .addToBackStack(ProductDetailsFragment.TAG)
                .replace(R.id.fragment_container, fragment, ProductDetailsFragment.TAG)
                .commit();
    }
}
```

Inside of the source destination, you might be invoking a navigation function in
response to some event, as shown below:  

### Kotlin

```kotlin
class ProductListFragment : Fragment() {
    ...
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // In this example a callback is passed to respond to an item clicked
        //  in a RecyclerView
        productAdapter = ProductAdapter(productClickCallback)
        binding.productsList.setAdapter(productAdapter)
    }
    ...

    // The callback makes the call to the activity to make the transition.
    private val productClickCallback = ProductClickCallback { product ->
            (requireActivity() as MainActivity).navigateToProductDetail(product.id)
    }
}
```

### Java

```java
public class ProductListFragment extends Fragment  {
    ...
    @Override
    public void onViewCreated(@NonNull View view,
            @Nullable Bundle savedInstanceState) {
    // In this example a callback is passed to respond to an item clicked in a RecyclerView
        productAdapter = new ProductAdapter(productClickCallback);
        binding.productsList.setAdapter(productAdapter);
    }
    ...

    // The callback makes the call to the activity to make the transition.
    private ProductClickCallback productClickCallback = product -> (
        ((MainActivity) requireActivity()).navigateToProductDetail(product.getId())
    );
}
```

This can be replaced by updating your navigation graph to set
the start destination and actions to link your destinations and define
arguments where required:  

    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/product_list_graph"
        app:startDestination="@id/product_list">

        <fragment
            android:id="@+id/product_list"
            android:name="com.example.android.persistence.ui.ProductListFragment"
            android:label="Product List"
            tools:layout="@layout/product_list">
            <action
                android:id="@+id/navigate_to_product_detail"
                app:destination="@id/product_detail" />
        </fragment>
        <fragment
            android:id="@+id/product_detail"
            android:name="com.example.android.persistence.ui.ProductDetailFragment"
            android:label="Product Detail"
            tools:layout="@layout/product_detail">
            <argument
                android:name="product_id"
                app:argType="integer" />
        </fragment>
    </navigation>

Then, you can update your activity:  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {

    // No need to load the start destination, handled automatically by the Navigation component
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {

    // No need to load the start destination, handled automatically by the Navigation component
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```

The activity no longer needs a `navigateToProductDetail()` method. In the next
section, we update `ProductListFragment` to use the `NavController` to navigate
to the next product detail screen.

##### Pass arguments safely

The Navigation component has a Gradle plugin called
[Safe Args](https://developer.android.com/topic/libraries/architecture/navigation/navigation-pass-data#Safe-args)
that generates simple object and builder classes for type-safe access to
arguments specified for destinations and actions.

Once the plugin is applied, any arguments defined on a destination in your
navigation graph causes the Navigation component framework to generate an
`Arguments` class that provides type safe arguments to the target destination.
Defining an action causes the plugin to generate a `Directions` configuration
class which can be used to tell the `NavController` how to navigate the user to
the target destination. When an action points to a destination that requires
arguments, the generated `Directions` class includes constructor methods which
require those parameters.

Inside the fragment, use `NavController` and the generated `Directions` class to
provide type-safe arguments to the target destination, as shown in the following
example:  

### Kotlin

```kotlin
class ProductListFragment : Fragment() {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        // In this example a callback is passed to respond to an item clicked in a RecyclerView
        productAdapter = ProductAdapter(productClickCallback)
        binding.productsList.setAdapter(productAdapter)
    }
    ...

    // The callback makes the call to the NavController to make the transition.
    private val productClickCallback = ProductClickCallback { product ->
        val directions = ProductListDirections.navigateToProductDetail(product.id)
        findNavController().navigate(directions)
    }
}
```

### Java

```java
public class ProductListFragment extends Fragment  {
    ...
    @Override
    public void onViewCreated(@NonNull View view,
            @Nullable Bundle savedInstanceState) {
        // In this example a callback is passed to respond to an item clicked in a RecyclerView
        productAdapter = new ProductAdapter(productClickCallback);
        binding.productsList.setAdapter(productAdapter);
    }
    ...

    // The callback makes the call to the activity to make the transition.
    private ProductClickCallback productClickCallback = product -> {
        ProductListDirections.ViewProductDetails directions =
                ProductListDirections.navigateToProductDetail(product.getId());
        NavHostFragment.findNavController(this).navigate(directions);
    };
}
```

#### Top-Level Navigation

If your app uses a `DrawerLayout`, you might have a lot of configuration logic
in your activity that manages opening and closing the drawer and navigating to
other destinations.

Your resulting activity might look something like this:  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity(),
    NavigationView.OnNavigationItemSelectedListener {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val toolbar: Toolbar = findViewById(R.id.toolbar)
        setSupportActionBar(toolbar)

        val drawerLayout: DrawerLayout = findViewById(R.id.drawer_layout)
        val navView: NavigationView = findViewById(R.id.nav_view)
        val toggle = ActionBarDrawerToggle(
                this,
                drawerLayout,
                toolbar,
                R.string.navigation_drawer_open, 
                R.string.navigation_drawer_close
        )
        drawerLayout.addDrawerListener(toggle)
        toggle.syncState()

        navView.setNavigationItemSelectedListener(this)
    }

    override fun onBackPressed() {
        val drawerLayout: DrawerLayout = findViewById(R.id.drawer_layout)
        if (drawerLayout.isDrawerOpen(GravityCompat.START)) {
            drawerLayout.closeDrawer(GravityCompat.START)
        } else {
            super.onBackPressed()
        }
    }

    override fun onNavigationItemSelected(item: MenuItem): Boolean {
        // Handle navigation view item clicks here.
        when (item.itemId) {
            R.id.home -> {
                val homeFragment = HomeFragment()
                show(homeFragment)
            }
            R.id.gallery -> {
                val galleryFragment = GalleryFragment()
                show(galleryFragment)
            }
            R.id.slide_show -> {
                val slideShowFragment = SlideShowFragment()
                show(slideShowFragment)
            }
            R.id.tools -> {
                val toolsFragment = ToolsFragment()
                show(toolsFragment)
            }
        }
        val drawerLayout: DrawerLayout = findViewById(R.id.drawer_layout)
        drawerLayout.closeDrawer(GravityCompat.START)
        return true
    }
}

private fun show(fragment: Fragment) {

    val drawerLayout = drawer_layout as DrawerLayout
    val fragmentManager = supportFragmentManager

    fragmentManager
            .beginTransaction()
            .replace(R.id.main_content, fragment)
            .commit()

    drawerLayout.closeDrawer(GravityCompat.START)
}
```

### Java

```java
public class MainActivity extends AppCompatActivity
        implements NavigationView.OnNavigationItemSelectedListener {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        NavigationView navigationView = findViewById(R.id.nav_view);
        ActionBarDrawerToggle toggle = new ActionBarDrawerToggle(
                this,
                drawer,
                toolbar,
                R.string.navigation_drawer_open,
                R.string.navigation_drawer_close);
        drawer.addDrawerListener(toggle);
        toggle.syncState();

        navigationView.setNavigationItemSelectedListener(this);
    }

    @Override
    public void onBackPressed() {
        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }

    @Override
    public boolean onNavigationItemSelected(MenuItem item) {
        // Handle navigation view item clicks here.
        int id = item.getItemId();

        if (id == R.id.home) {
            Fragment homeFragment = new HomeFragment();
            show(homeFragment);
        } else if (id == R.id.gallery) {
            Fragment galleryFragment = new GalleryFragment();
            show(galleryFragment);
        } else if (id == R.id.slide_show) {
            Fragment slideShowFragment = new SlideShowFragment();
            show(slideShowFragment);
        } else if (id == R.id.tools) {
            Fragment toolsFragment = new ToolsFragment();
            show(toolsFragment);
        }

        DrawerLayout drawer = findViewById(R.id.drawer_layout);
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    private void show(Fragment fragment) {

        DrawerLayout drawerLayout = findViewById(R.id.drawer_layout);
        FragmentManager fragmentManager = getSupportFragmentManager();

        fragmentManager
                .beginTransaction()
                .replace(R.id.main_content, fragment)
                .commit();

        drawerLayout.closeDrawer(GravityCompat.START);
    }
}
```

After you have added the Navigation component to your project and created a
navigation graph, add each of the content destinations from your graph (such as
*Home* , *Gallery* , *SlideShow* , and *Tools* from the example above). Be sure
that your menu item `id` values match their associated destination `id` values,
as shown below:  

    <!-- activity_main_drawer.xml -->
    <menu xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools"
        tools:showIn="navigation_view">

        <group android:checkableBehavior="single">
            <item
                android:id="@+id/home"
                android:icon="@drawable/ic_menu_camera"
                android:title="@string/menu_home" />
            <item
                android:id="@+id/gallery"
                android:icon="@drawable/ic_menu_gallery"
                android:title="@string/menu_gallery" />
            <item
                android:id="@+id/slide_show"
                android:icon="@drawable/ic_menu_slideshow"
                android:title="@string/menu_slideshow" />
            <item
                android:id="@+id/tools"
                android:icon="@drawable/ic_menu_manage"
                android:title="@string/menu_tools" />
        </group>
    </menu>

    <!-- activity_main_graph.xml -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/main_graph"
        app:startDestination="@id/home">

        <fragment
            android:id="@+id/home"
            android:name="com.example.HomeFragment"
            android:label="Home"
            tools:layout="@layout/home" />

        <fragment
            android:id="@+id/gallery"
            android:name="com.example.GalleryFragment"
            android:label="Gallery"
            tools:layout="@layout/gallery" />

        <fragment
            android:id="@+id/slide_show"
            android:name="com.example.SlideShowFragment"
            android:label="Slide Show"
            tools:layout="@layout/slide_show" />

        <fragment
            android:id="@+id/tools"
            android:name="com.example.ToolsFragment"
            android:label="Tools"
            tools:layout="@layout/tools" />

    </navigation>

If you match the `id` values from your menu and graph, then you can wire up the
`NavController` for this activity to handle navigation automatically based on
the menu item. The `NavController` also handles opening and closing the
`DrawerLayout` and handling Up and Back button behavior appropriately.

Your `MainActivity` can then be updated to wire up the `NavController` to the
`Toolbar` and `NavigationView`.

See the following snippet for an example:  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity()  {

    val drawerLayout by lazy { findViewById<DrawerLayout>(R.id.drawer_layout) }
    val navController by lazy {
      (supportFragmentManager.findFragmentById(R.id.main_content) as NavHostFragment).navController
    }
    val navigationView by lazy { findViewById<NavigationView>(R.id.nav_view) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val toolbar = findViewById<Toolbar>(R.id.toolbar)
        setSupportActionBar(toolbar)

        // Show and Manage the Drawer and Back Icon
        setupActionBarWithNavController(navController, drawerLayout)

        // Handle Navigation item clicks
        // This works with no further action on your part if the menu and destination id's match.
        navigationView.setupWithNavController(navController)

    }

    override fun onSupportNavigateUp(): Boolean {
        // Allows NavigationUI to support proper up navigation or the drawer layout
        // drawer menu, depending on the situation
        return navController.navigateUp(drawerLayout)
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {

    private DrawerLayout drawerLayout;
    private NavController navController;
    private NavigationView navigationView;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        drawerLayout = findViewById(R.id.drawer_layout);
        NavHostFragment navHostFragment = (NavHostFragment)
            getSupportFragmentManager().findFragmentById(R.id.main_content);
        navController = navHostFragment.getNavController();
        navigationView = findViewById(R.id.nav_view);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        // Show and Manage the Drawer and Back Icon
        NavigationUI.setupActionBarWithNavController(this, navController, drawerLayout);

        // Handle Navigation item clicks
        // This works with no further action on your part if the menu and destination id's match.
        NavigationUI.setupWithNavController(navigationView, navController);

    }

    @Override
    public boolean onSupportNavigateUp() {
        // Allows NavigationUI to support proper up navigation or the drawer layout
        // drawer menu, depending on the situation.
        return NavigationUI.navigateUp(navController, drawerLayout);

    }
}
```

You can use this same technique with both BottomNavigationView-based navigation
and Menu-based navigation. See
[Update UI components with NavigationUI](https://developer.android.com/topic/libraries/architecture/navigation/navigation-ui)
for more examples.

## Add activity destinations

Once each screen in your app is wired up to use the Navigation component, and
you are no longer using `FragmentTransactions` to transition between
fragment-based destinations, the next step is to eliminate `startActivity`
calls.

First, identify places in your app where you have two separate navigation graphs
and are using `startActivity` to transition between them.

This example contains two graphs (A and B) and a `startActivity()` call to
transition from A to B.

![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-migrate-two-graphs.png)  

### Kotlin

```kotlin
fun navigateToProductDetails(productId: String) {
    val intent = Intent(this, ProductDetailsActivity::class.java)
    intent.putExtra(KEY_PRODUCT_ID, productId)
    startActivity(intent)
}
```

### Java

```java
private void navigateToProductDetails(String productId) {
    Intent intent = new Intent(this, ProductDetailsActivity.class);
    intent.putExtra(KEY_PRODUCT_ID, productId);
    startActivity(intent);
```

Next, replace these with an activity destination in Graph A that represents the
navigation to the host activity of Graph B. If you have arguments to pass to the
start destination of Graph B, you can designate them in the activity destination
definition.

In the following example, Graph A defines an activity destination which takes a
`product_id` argument along with an action. Graph B contains no changes.

![](https://developer.android.com/static/images/topic/libraries/architecture/navigation-migrate-two-graphs-2.png)

The XML representation of Graphs A and B might look like this:  

    <!-- Graph A -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/product_list_graph"
        app:startDestination="@id/product_list">

        <fragment
            android:id="@+id/product_list"
            android:name="com.example.android.persistence.ui.ProductListFragment"
            android:label="Product List"
            tools:layout="@layout/product_list_fragment">
            <action
                android:id="@+id/navigate_to_product_detail"
                app:destination="@id/product_details_activity" />
        </fragment>

        <activity
            android:id="@+id/product_details_activity"
            android:name="com.example.android.persistence.ui.ProductDetailsActivity"
            android:label="Product Details"
            tools:layout="@layout/product_details_host">

            <argument
                android:name="product_id"
                app:argType="integer" />

        </activity>

    </navigation>

    <!-- Graph B -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        app:startDestination="@id/product_details">

        <fragment
            android:id="@+id/product_details"
            android:name="com.example.android.persistence.ui.ProductDetailsFragment"
            android:label="Product Details"
            tools:layout="@layout/product_details_fragment">
            <argument
                android:name="product_id"
                app:argType="integer" />
        </fragment>

    </navigation>

You can navigate to the host activity of Graph B using the same mechanisms you
use to navigate to fragment destinations:  

### Kotlin

```kotlin
fun navigateToProductDetails(productId: String) {
    val directions = ProductListDirections.navigateToProductDetail(productId)
    findNavController().navigate(directions)
}
```

### Java

```java
private void navigateToProductDetails(String productId) {
    ProductListDirections.NavigateToProductDetail directions =
            ProductListDirections.navigateToProductDetail(productId);
    Navigation.findNavController(getView()).navigate(directions);
```

### Pass activity destination args to a start destination fragment

If the destination activity receives extras, as with the previous example, you
can pass these to the start destination directly as arguments, but you need to
manually set your host's navigation graph inside the host activity's
`onCreate()` method so that you can pass the intent extras as arguments to the
fragment, as shown below:  

### Kotlin

```kotlin
class ProductDetailsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.product_details_host)
        val navHostFragment = supportFragmentManager.findFragmentById(R.id.main_content) as NavHostFragment
        val navController = navHostFragment.navController
        navController
                .setGraph(R.navigation.product_detail_graph, intent.extras)
    }

}
```

### Java

```java
public class ProductDetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.product_details_host);
        NavHostFragment navHostFragment = (NavHostFragment)
            getSupportFragmentManager().findFragmentById(R.id.main_content);
        NavController navController = navHostFragment.getNavController();
        navController
                .setGraph(R.navigation.product_detail_graph, getIntent().getExtras());
    }

}
```
| **Note:** In this case, you should avoid setting the `app:NavGraph` attribute in the `NavHostFragment` definition, because doing so results in inflating and setting the navigation graph twice.

The data can be pulled out of the fragment arguments `Bundle` using the
generated args class, as shown in the following example:  

### Kotlin

```kotlin
class ProductDetailsFragment : Fragment() {

    val args by navArgs<ProductDetailsArgs>()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val productId = args.productId
        ...
    }
    ...
```

### Java

```java
public class ProductDetailsFragment extends Fragment {

    ProductDetailsArgs args;

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        args = ProductDetailsArgs.fromBundle(requireArguments());
    }

    @Override
    public void onViewCreated(@NonNull View view,
            @Nullable Bundle savedInstanceState) {
       int productId = args.getProductId();
       ...
    }
    ...
```

## Combine activities

You can combine navigation graphs in cases where multiple activities share the
same layout, such as a simple `FrameLayout` containing a single fragment. In
most of these cases, you can just combine all of the elements from each
navigation graph and updating any activity destination elements to fragment
destinations.

The following example combines Graphs A and B from the previous section:

**Before combining:**  

    <!-- Graph A -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/product_list_graph"
        app:startDestination="@id/product_list">

        <fragment
            android:id="@+id/product_list"
            android:name="com.example.android.persistence.ui.ProductListFragment"
            android:label="Product List Fragment"
            tools:layout="@layout/product_list">
            <action
                android:id="@+id/navigate_to_product_detail"
                app:destination="@id/product_details_activity" />
        </fragment>
        <activity
            android:id="@+id/product_details_activity"
            android:name="com.example.android.persistence.ui.ProductDetailsActivity"
            android:label="Product Details Host"
            tools:layout="@layout/product_details_host">
            <argument android:name="product_id"
                app:argType="integer" />
        </activity>

    </navigation>

    <!-- Graph B -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/product_detail_graph"
        app:startDestination="@id/product_details">

        <fragment
            android:id="@+id/product_details"
            android:name="com.example.android.persistence.ui.ProductDetailsFragment"
            android:label="Product Details"
            tools:layout="@layout/product_details">
            <argument
                android:name="product_id"
                app:argType="integer" />
        </fragment>
    </navigation>

**After combining:**  

    <!-- Combined Graph A and B -->
    <navigation xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:app="http://schemas.android.com/apk/res-auto"
        xmlns:tools="http://schemas.android.com/tools"
        android:id="@+id/product_list_graph"
        app:startDestination="@id/product_list">

        <fragment
            android:id="@+id/product_list"
            android:name="com.example.android.persistence.ui.ProductListFragment"
            android:label="Product List Fragment"
            tools:layout="@layout/product_list">
            <action
                android:id="@+id/navigate_to_product_detail"
                app:destination="@id/product_details" />
        </fragment>

        <fragment
            android:id="@+id/product_details"
            android:name="com.example.android.persistence.ui.ProductDetailsFragment"
            android:label="Product Details"
            tools:layout="@layout/product_details">
            <argument
                android:name="product_id"
                app:argType="integer" />
        </fragment>

    </navigation>

Keeping your action names the same while merging can make this a seamless
process, requiring no changes to your existing code base. For example,
`navigateToProductDetail` remains the same here. The only difference is that
this action now represents navigation to a fragment destination within the same
`NavHost` instead of an activity destination:  

### Kotlin

```kotlin
fun navigateToProductDetails(productId: String) {
    val directions = ProductListDirections.navigateToProductDetail(productId)
    findNavController().navigate(directions)
}
```

### Java

```java
private void navigateToProductDetails(String productId) {
    ProductListDirections.NavigateToProductDetail directions =
            ProductListDirections.navigateToProductDetail(productId);
    Navigation.findNavController(getView()).navigate(directions);
```

## Additional Resources

For more navigation-related information, see the following topics:

- [Update UI components with NavigationUI](https://developer.android.com/topic/libraries/architecture/navigation/navigation-ui) - Learn how to manage navigation with the top app bar, the navigation drawer, and bottom navigation
- [Test Navigation](https://developer.android.com/topic/libraries/architecture/navigation/navigation-testing) - Learn how to test navigation workflows for your app