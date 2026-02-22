---
title: https://developer.android.com/guide/fragments/communicate
url: https://developer.android.com/guide/fragments/communicate
source: md.txt
---

# Communicate with fragments

To reuse fragments, build them as completely self-contained components that define their own layout and behavior. Once you define these reusable fragments, you can associate them with an activity and connect them with the application logic to realize the overall composite UI.

To properly react to user events and to share state information, you often need to have channels of communication between an activity and its fragments or between two or more fragments. To keep fragments self-contained,*don't*have fragments communicate directly with other fragments or with their host activity.

The`Fragment`library provides two options for communication: a shared[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel)and the Fragment Result API. The recommended option depends on the use case. To share persistent data with custom APIs, use a`ViewModel`. For a one-time result with data that can be placed in a[`Bundle`](https://developer.android.com/reference/android/os/Bundle), use the Fragment Result API.

The following sections show you how to use`ViewModel`and the Fragment Result API to communicate between your fragments and activities.

## Share data using a ViewModel

[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)is an ideal choice when you need to share data between multiple fragments or between fragments and their host activity.`ViewModel`objects store and manage UI data. For more information about`ViewModel`, see[ViewModel overview](https://developer.android.com/topic/libraries/architecture/viewmodel).

### Share data with the host activity

In some cases, you might need to share data between fragments and their host activity. For example, you might want to toggle a global UI component based on an interaction within a fragment.

Consider the following`ItemViewModel`:  

### Kotlin

```kotlin
class ItemViewModel : ViewModel() {
    private val mutableSelectedItem = MutableLiveData<Item>()
    val selectedItem: LiveData<Item> get() = mutableSelectedItem

    fun selectItem(item: Item) {
        mutableSelectedItem.value = item
    }
}
```

### Java

```java
public class ItemViewModel extends ViewModel {
    private final MutableLiveData<Item> selectedItem = new MutableLiveData<Item>();
    public void selectItem(Item item) {
        selectedItem.setValue(item);
    }
    public LiveData<Item> getSelectedItem() {
        return selectedItem;
    }
}
```

In this example, the stored data is wrapped in a[`MutableLiveData`](https://developer.android.com/reference/androidx/lifecycle/MutableLiveData)class.[`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData)is a lifecycle-aware observable data holder class.`MutableLiveData`lets its value be changed. For more information about`LiveData`, see[LiveData overview](https://developer.android.com/topic/libraries/architecture/livedata).

Both your fragment and its host activity can retrieve a shared instance of a`ViewModel`with activity scope by passing the activity into the[`ViewModelProvider`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider)constructor. The`ViewModelProvider`handles instantiating the`ViewModel`or retrieving it if it already exists. Both components can observe and modify this data.  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {
    // Using the viewModels() Kotlin property delegate from the activity-ktx
    // artifact to retrieve the ViewModel in the activity scope.
    private val viewModel: ItemViewModel by viewModels()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        viewModel.selectedItem.observe(this, Observer { item ->
            // Perform an action with the latest item data.
        })
    }
}

class ListFragment : Fragment() {
    // Using the activityViewModels() Kotlin property delegate from the
    // fragment-ktx artifact to retrieve the ViewModel in the activity scope.
    private val viewModel: ItemViewModel by activityViewModels()

    // Called when the item is clicked.
    fun onItemClicked(item: Item) {
        // Set a new item.
        viewModel.selectItem(item)
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {
    private ItemViewModel viewModel;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        viewModel = new ViewModelProvider(this).get(ItemViewModel.class);
        viewModel.getSelectedItem().observe(this, item -> {
            // Perform an action with the latest item data.
        });
    }
}

public class ListFragment extends Fragment {
    private ItemViewModel viewModel;

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        viewModel = new ViewModelProvider(requireActivity()).get(ItemViewModel.class);
        ...
        items.setOnClickListener(item -> {
            // Set a new item.
            viewModel.select(item);
        });
    }
}
```
| **Caution:** Use the appropriate scope with`ViewModelProvider`. In the preceding example,`MainActivity`is used as the scope in both`MainActivity`and`ListFragment`, so they are both provided the same`ViewModel`. If`ListFragment`instead uses itself as the scope, it provides a different`ViewModel`than`MainActivity`.

### Share data between fragments

Two or more fragments in the same activity often need to communicate with each other. For example, imagine one fragment that displays a list and another that lets the user apply various filters to the list. Implementing this case isn't trivial without the fragments communicating directly, but then they are no longer self-contained. Additionally, both fragments must handle the scenario where the other fragment is not yet created or visible.

These fragments can share a`ViewModel`using their activity scope to handle this communication. By sharing the`ViewModel`in this way, the fragments don't need to know about each other, and the activity doesn't need to do anything to facilitate the communication.

The following example shows how two fragments can use a shared`ViewModel`to communicate:  

### Kotlin

```kotlin
class ListViewModel : ViewModel() {
    val filters = MutableLiveData<Set<Filter>>()

    private val originalList: LiveData<List<Item>>() = ...
    val filteredList: LiveData<List<Item>> = ...

    fun addFilter(filter: Filter) { ... }

    fun removeFilter(filter: Filter) { ... }
}

class ListFragment : Fragment() {
    // Using the activityViewModels() Kotlin property delegate from the
    // fragment-ktx artifact to retrieve the ViewModel in the activity scope.
    private val viewModel: ListViewModel by activityViewModels()
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewModel.filteredList.observe(viewLifecycleOwner, Observer { list ->
            // Update the list UI.
        }
    }
}

class FilterFragment : Fragment() {
    private val viewModel: ListViewModel by activityViewModels()
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewModel.filters.observe(viewLifecycleOwner, Observer { set ->
            // Update the selected filters UI.
        }
    }

    fun onFilterSelected(filter: Filter) = viewModel.addFilter(filter)

    fun onFilterDeselected(filter: Filter) = viewModel.removeFilter(filter)
}
```

### Java

```java
public class ListViewModel extends ViewModel {
    private final MutableLiveData<Set<Filter>> filters = new MutableLiveData<>();

    private final LiveData<List<Item>> originalList = ...;
    private final LiveData<List<Item>> filteredList = ...;

    public LiveData<List<Item>> getFilteredList() {
        return filteredList;
    }

    public LiveData<Set<Filter>> getFilters() {
        return filters;
    }

    public void addFilter(Filter filter) { ... }

    public void removeFilter(Filter filter) { ... }
}

public class ListFragment extends Fragment {
    private ListViewModel viewModel;

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        viewModel = new ViewModelProvider(requireActivity()).get(ListViewModel.class);
        viewModel.getFilteredList().observe(getViewLifecycleOwner(), list -> {
            // Update the list UI.
        });
    }
}

public class FilterFragment extends Fragment {
    private ListViewModel viewModel;

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        viewModel = new ViewModelProvider(requireActivity()).get(ListViewModel.class);
        viewModel.getFilters().observe(getViewLifecycleOwner(), set -> {
            // Update the selected filters UI.
        });
    }

    public void onFilterSelected(Filter filter) {
        viewModel.addFilter(filter);
    }

    public void onFilterDeselected(Filter filter) {
        viewModel.removeFilter(filter);
    }
}
```

Both fragments use their host activity as the scope for the`ViewModelProvider`. Because the fragments use the same scope, they receive the same instance of the`ViewModel`, which enables them to communicate back and forth.
| **Caution:** The`ViewModel`remains in memory until the[`ViewModelStoreOwner`](https://developer.android.com/reference/androidx/lifecycle/ViewModelStoreOwner)to which it's scoped goes away permanently. In a single activity architecture, if the`ViewModel`is scoped to the activity, it's essentially a singleton. After the`ViewModel`is first instantiated, subsequent calls to retrieve the`ViewModel`using the activity scope always returns the same existing`ViewModel`, along with the existing data until the activity's lifecycle has permanently ended.

#### Share data between a parent and child fragment

When working with child fragments, your parent fragment and its child fragments might need to share data with each other. To share data between these fragments, use the parent fragment as the`ViewModel`scope, as shown in the following example:  

### Kotlin

```kotlin
class ListFragment: Fragment() {
    // Using the viewModels() Kotlin property delegate from the fragment-ktx
    // artifact to retrieve the ViewModel.
    private val viewModel: ListViewModel by viewModels()
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewModel.filteredList.observe(viewLifecycleOwner, Observer { list ->
            // Update the list UI.
        }
    }
}

class ChildFragment: Fragment() {
    // Using the viewModels() Kotlin property delegate from the fragment-ktx
    // artifact to retrieve the ViewModel using the parent fragment's scope
    private val viewModel: ListViewModel by viewModels({requireParentFragment()})
    ...
}
```

### Java

```java
public class ListFragment extends Fragment {
    private ListViewModel viewModel;

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        viewModel = new ViewModelProvider(this).get(ListViewModel.class);
        viewModel.getFilteredList().observe(getViewLifecycleOwner(), list -> {
            // Update the list UI.
        }
    }
}

public class ChildFragment extends Fragment {
    private ListViewModel viewModel;
    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        viewModel = new ViewModelProvider(requireParentFragment()).get(ListViewModel.class);
        ...
    }
}
```

#### Scope a ViewModel to the Navigation Graph

If you're using the[Navigation library](https://developer.android.com/guide/navigation), you can also scope a`ViewModel`to the lifecycle of a destination's[`NavBackStackEntry`](https://developer.android.com/reference/androidx/navigation/NavBackStackEntry). For example, the`ViewModel`can be scoped to the`NavBackStackEntry`for the`ListFragment`:  

### Kotlin

```kotlin
class ListFragment: Fragment() {
    // Using the navGraphViewModels() Kotlin property delegate from the fragment-ktx
    // artifact to retrieve the ViewModel using the NavBackStackEntry scope.
    // R.id.list_fragment == the destination id of the ListFragment destination
    private val viewModel: ListViewModel by navGraphViewModels(R.id.list_fragment)

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewModel.filteredList.observe(viewLifecycleOwner, Observer { item ->
            // Update the list UI.
        }
    }
}
```

### Java

```java
public class ListFragment extends Fragment {
    private ListViewModel viewModel;

    @Override
    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
    NavController navController = NavHostFragment.findNavController(this);
        NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.list_fragment)

        viewModel = new ViewModelProvider(backStackEntry).get(ListViewModel.class);
        viewModel.getFilteredList().observe(getViewLifecycleOwner(), list -> {
            // Update the list UI.
        }
    }
}
```

For more information about scoping a`ViewModel`to a`NavBackStackEntry`, see[Interact programmatically with the Navigation component](https://developer.android.com/guide/navigation/navigation-programmatic).

## Get results using the Fragment Result API

In some cases, you might want to pass a one-time value between two fragments or between a fragment and its host activity. For example, you might have a fragment that reads QR codes, passing the data back to a previous fragment.

In Fragment version 1.3.0 and higher, each[`FragmentManager`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager)implements[`FragmentResultOwner`](https://developer.android.com/reference/androidx/fragment/app/FragmentResultOwner). This means that a`FragmentManager`can act as a central store for fragment results. This change lets components communicate with each other by setting fragment results and listening for those results, without requiring those components to have direct references to each other.

### Pass results between fragments

To pass data back to fragment A from fragment B, first set a result listener on fragment A, the fragment that receives the result. Call[`setFragmentResultListener()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#setfragmentresultlistener)on fragment A's`FragmentManager`, as shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Use the Kotlin extension in the fragment-ktx artifact.
    setFragmentResultListener("requestKey") { requestKey, bundle ->
        // We use a String here, but any type that can be put in a Bundle is supported.
        val result = bundle.getString("bundleKey")
        // Do something with the result.
    }
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getParentFragmentManager().setFragmentResultListener("requestKey", this, new FragmentResultListener() {
        @Override
        public void onFragmentResult(@NonNull String requestKey, @NonNull Bundle bundle) {
            // We use a String here, but any type that can be put in a Bundle is supported.
            String result = bundle.getString("bundleKey");
            // Do something with the result.
        }
    });
}
```
![fragment b sends data to fragment a using a FragmentManager](https://developer.android.com/static/images/guide/fragments/fragment-a-to-b.png)**Figure 1.** Fragment B sends data to fragment A using a`FragmentManager`.

In fragment B, the fragment producing the result, set the result on the same`FragmentManager`by using the same`requestKey`. You can do so by using the[`setFragmentResult()`](https://developer.android.com/reference/androidx/fragment/app/FragmentManager#setfragmentresult)API:  

### Kotlin

```kotlin
button.setOnClickListener {
    val result = "result"
    // Use the Kotlin extension in the fragment-ktx artifact.
    setFragmentResult("requestKey", bundleOf("bundleKey" to result))
}
```

### Java

```java
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Bundle result = new Bundle();
        result.putString("bundleKey", "result");
        getParentFragmentManager().setFragmentResult("requestKey", result);
    }
});
```

Fragment A then receives the result and executes the listener callback once the fragment is[`STARTED`](https://developer.android.com/reference/androidx/lifecycle/Lifecycle.State#STARTED).

You can have only a single listener and result for a given key. If you call`setFragmentResult()`more than once for the same key, and if the listener is not`STARTED`, the system replaces any pending results with your updated result.

If you set a result without a corresponding listener to receive it, the result is stored in the`FragmentManager`until you set a listener with the same key. Once a listener receives a result and fires the`onFragmentResult()`callback, the result is cleared. This behavior has two major implications:

- Fragments on the back stack do not receive results until they have been popped and are`STARTED`.
- If a fragment listening for a result is`STARTED`when the result is set, the listener's callback then fires immediately.

| **Note:** Because the fragment results are stored at the`FragmentManager`level, your fragment must be attached to call`setFragmentResultListener()`or`setFragmentResult()`with the parent`FragmentManager`.

#### Test fragment results

Use[`FragmentScenario`](https://developer.android.com/reference/androidx/fragment/app/testing/FragmentScenario)to test calls to`setFragmentResult()`and`setFragmentResultListener()`. Create a scenario for the fragment under test by using[`launchFragmentInContainer`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#launchFragmentInContainer(android.os.Bundle,kotlin.Int,androidx.lifecycle.Lifecycle.State,androidx.fragment.app.FragmentFactory))or[`launchFragment`](https://developer.android.com/reference/kotlin/androidx/fragment/app/testing/package-summary#top-level-functions), and then manually call the method that isn't being tested.

To test`setFragmentResultListener()`, create a scenario with the fragment that makes the call to`setFragmentResultListener()`. Next, call`setFragmentResult()`directly, and verify the result:  

    @Test
    fun testFragmentResultListener() {
        val scenario = launchFragmentInContainer<ResultListenerFragment>()
        scenario.onFragment { fragment ->
            val expectedResult = "result"
            fragment.parentFragmentManager.setFragmentResult("requestKey", bundleOf("bundleKey" to expectedResult))
            assertThat(fragment.result).isEqualTo(expectedResult)
        }
    }

    class ResultListenerFragment : Fragment() {
        var result : String? = null
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            // Use the Kotlin extension in the fragment-ktx artifact.
            setFragmentResultListener("requestKey") { requestKey, bundle ->
                result = bundle.getString("bundleKey")
            }
        }
    }

To test`setFragmentResult()`, create a scenario with the fragment that makes the call to`setFragmentResult()`. Next, call`setFragmentResultListener()`directly, and verify the result:  

    @Test
    fun testFragmentResult() {
        val scenario = launchFragmentInContainer<ResultFragment>()
        lateinit var actualResult: String?
        scenario.onFragment { fragment ->
            fragment.parentFragmentManager
                    .setFragmentResultListener("requestKey") { requestKey, bundle ->
                actualResult = bundle.getString("bundleKey")
            }
        }
        onView(withId(R.id.result_button)).perform(click())
        assertThat(actualResult).isEqualTo("result")
    }

    class ResultFragment : Fragment(R.layout.fragment_result) {
        override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
            view.findViewById(R.id.result_button).setOnClickListener {
                val result = "result"
                // Use the Kotlin extension in the fragment-ktx artifact.
                setFragmentResult("requestKey", bundleOf("bundleKey" to result))
            }
        }
    }

### Pass results between parent and child fragments

To pass a result from a child fragment to a parent, use`getChildFragmentManager()`from the parent fragment instead of`getParentFragmentManager()`when calling`setFragmentResultListener()`.  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // Set the listener on the child fragmentManager.
    childFragmentManager.setFragmentResultListener("requestKey") { key, bundle ->
        val result = bundle.getString("bundleKey")
        // Do something with the result.
    }
}
```

### Java

```java
@Override
public void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // Set the listener on the child fragmentManager.
    getChildFragmentManager()
        .setFragmentResultListener("requestKey", this, new FragmentResultListener() {
            @Override
            public void onFragmentResult(@NonNull String requestKey, @NonNull Bundle bundle) {
                String result = bundle.getString("bundleKey");
                // Do something with the result.
            }
        });
}
```
![a child fragment can use FragmentManager to send a result to its parent](https://developer.android.com/static/images/guide/fragments/pass-parent-child.png)**Figure 2** A child fragment can use`FragmentManager`to send a result to its parent.

The child fragment sets the result on its`FragmentManager`. The parent then receives the result once the fragment is`STARTED`:  

### Kotlin

```kotlin
button.setOnClickListener {
    val result = "result"
    // Use the Kotlin extension in the fragment-ktx artifact.
    setFragmentResult("requestKey", bundleOf("bundleKey" to result))
}
```

### Java

```java
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View v) {
        Bundle result = new Bundle();
        result.putString("bundleKey", "result");
        // The child fragment needs to still set the result on its parent fragment manager.
        getParentFragmentManager().setFragmentResult("requestKey", result);
    }
});
```

### Receive results in the host activity

To receive a fragment result in the host activity, set a result listener on the fragment manager using[`getSupportFragmentManager()`](https://developer.android.com/reference/androidx/fragment/app/FragmentActivity#getSupportFragmentManager()).  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        supportFragmentManager
                .setFragmentResultListener("requestKey", this) { requestKey, bundle ->
            // We use a String here, but any type that can be put in a Bundle is supported.
            val result = bundle.getString("bundleKey")
            // Do something with the result.
        }
    }
}
```

### Java

```java
class MainActivity extends AppCompatActivity {
    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getSupportFragmentManager().setFragmentResultListener("requestKey", this, new FragmentResultListener() {
            @Override
            public void onFragmentResult(@NonNull String requestKey, @NonNull Bundle bundle) {
                // We use a String here, but any type that can be put in a Bundle is supported.
                String result = bundle.getString("bundleKey");
                // Do something with the result.
            }
        });
    }
}
```