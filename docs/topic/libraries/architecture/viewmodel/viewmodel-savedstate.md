---
title: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate
url: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate
source: md.txt
---

# Saved State module for ViewModel

# Saved State module for ViewModelPart of[Android Jetpack](https://developer.android.com/jetpack).

As mentioned in[Saving UI States](https://developer.android.com/topic/libraries/architecture/saving-states#use_onsaveinstancestate_as_backup_to_handle_system-initiated_process_death),[`ViewModel`](https://developer.android.com/reference/androidx/lifecycle/ViewModel)objects can handle configuration changes, so you don't need to worry about state in rotations or other cases. However, if you need to handle system-initiated process death, you might want to use the`SavedStateHandle`API as backup.

UI state is usually stored or referenced in`ViewModel`objects and not activities, so using`onSaveInstanceState()`or`rememberSaveable`requires some boilerplate that the[saved state module](https://developer.android.com/jetpack/androidx/releases/savedstate)can handle for you.

When using this module,`ViewModel`objects receive a[`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle)object through its constructor. This object is a key-value map that lets you write and retrieve objects to and from the saved state. These values persist after the process is killed by the system and remain available through the same object.

Saved state is tied to your task stack. If your task stack goes away, your saved state also goes away. This can occur when force stopping an app, removing the app from the recents menu, or rebooting the device. In such cases, the task stack disappears and you can't restore the information in saved state. In[User-initiated UI state dismissal](https://developer.android.com/topic/libraries/architecture/saving-states#ui-dismissal-system)scenarios, saved state isn't restored. In[system-initiated](https://developer.android.com/topic/libraries/architecture/saving-states#ui-dismissal-system)scenarios, it is.
| **Key Point:** Usually, data stored in saved instance state is transient state that depends on user input or navigation. Examples of this can be the scroll position of a list, the id of the item the user wants more detail about, the in-progress selection of user preferences, or input in text fields.
| **Important:** the API to use depends on where the state is held and the logic that it requires. For state that is used in[business logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#logic), hold it in a ViewModel and save it using`SavedStateHandle`. For state that is used in[UI logic](https://developer.android.com/topic/architecture/ui-layer/stateholders#logic), use the`onSaveInstanceState`API in the View system or`rememberSaveable`in Compose.
| **Note:** State must be simple and lightweight. For complex or large data, you should use[local persistence](https://developer.android.com/topic/libraries/architecture/saving-states#local).

## Setup

Beginning with[Fragment 1.2.0](https://developer.android.com/jetpack/androidx/releases/fragment#1.2.0)or its transitive dependency[Activity 1.1.0](https://developer.android.com/jetpack/androidx/releases/activity#1.1.0), you can accept a`SavedStateHandle`as a constructor argument to your`ViewModel`.  

### Kotlin

```kotlin
class SavedStateViewModel(private val state: SavedStateHandle) : ViewModel() { ... }
```

### Java

```java
public class SavedStateViewModel extends ViewModel {
    private SavedStateHandle state;

    public SavedStateViewModel(SavedStateHandle savedStateHandle) {
        state = savedStateHandle;
    }

    ...
}
```

You can then retrieve an instance of your`ViewModel`without any additional configuration. The default`ViewModel`factory provides the appropriate`SavedStateHandle`to your`ViewModel`.  

### Kotlin

```kotlin
class MainFragment : Fragment() {
    val vm: SavedStateViewModel by viewModels()

    ...
}
```

### Java

```java
class MainFragment extends Fragment {
    private SavedStateViewModel vm;

    public void onViewCreated(@NonNull View view, Bundle savedInstanceState) {
        vm = new ViewModelProvider(this).get(SavedStateViewModel.class);

        ...


    }

    ...
}
```

When providing a custom[`ViewModelProvider.Factory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory)instance, you can enable usage of`SavedStateHandle`by extending[`AbstractSavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/AbstractSavedStateViewModelFactory).
| **Note:** When using an earlier version of the fragments library, follow the instructions for declaring dependencies in the[Lifecycle release notes](https://developer.android.com/jetpack/androidx/releases/lifecycle#declaring_dependencies)to add a dependency on`lifecycle-viewmodel-savedstate`and use[`SavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/SavedStateViewModelFactory)as your factory.

## Working with SavedStateHandle

The`SavedStateHandle`class is a key-value map that allows you to write and retrieve data to and from the saved state through the[`set()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#set(kotlin.String,kotlin.Any))and[`get()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#get(kotlin.String))methods.

By using`SavedStateHandle`, the query value is retained across process death, ensuring that the user sees the same set of filtered data before and after recreation without the activity or fragment needing to manually save, restore, and forward that value back to the`ViewModel`.
| **Caution:** `SavedStateHandle`only saves data written to it when the`Activity`is stopped. Writes to`SavedStateHandle`while the`Activity`is stopped aren't saved unless the`Activity`receives`onStart`followed by`onStop`again.

`SavedStateHandle`also has other methods you might expect when interacting with a key-value map:

- [`contains(String key)`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#contains(kotlin.String))- Checks if there is a value for the given key.
- [`remove(String key)`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#remove(kotlin.String))- Removes the value for the given key.
- [`keys()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#keys())- Returns all keys contained within the`SavedStateHandle`.

Additionally, you can retrieve values from`SavedStateHandle`using an observable data holder. The list of supported types are:

- [`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData).
- [`StateFlow`](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow).
- [Compose's State APIs](https://developer.android.com/jetpack/compose/state).

| **Warning:** These integrations with observable data holders make it more convenient to display UI with state persisted by[saved instance state](https://developer.android.com/topic/libraries/architecture/saving-states#onsaveinstancestate). However, these integrations are also saved and restored using the same mechanisms as the basic`get()`and`set()`methods. A`SavedStateHandle`is saved when the[`onSaveInstanceState`](https://developer.android.com/reference/android/app/Activity#onSaveInstanceState(android.os.Bundle,%20android.os.PersistableBundle))is called on the connected activity or fragment. This means that while you can continue to update observable data holders from a`SavedStateHandle`while the app is in the background, all state updates might be lost if the app process is killed before becoming foregrounded again.

### LiveData

Retrieve values from`SavedStateHandle`that are wrapped in a[`LiveData`](https://developer.android.com/reference/androidx/lifecycle/LiveData)observable using[`getLiveData()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getLiveData(kotlin.String,kotlin.Any)). When the key's value is updated, the`LiveData`receives the new value. Most often, the value is set due to user interactions, such as entering a query to filter a list of data. This updated value can then be used to[transform`LiveData`](https://developer.android.com/topic/libraries/architecture/livedata#transform_livedata).  

### Kotlin

```kotlin
class SavedStateViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    val filteredData: LiveData<List<String>> =
        savedStateHandle.getLiveData<String>("query").switchMap { query ->
        repository.getFilteredData(query)
    }

    fun setQuery(query: String) {
        savedStateHandle["query"] = query
    }
}
```

### Java

```java
public class SavedStateViewModel extends ViewModel {
    private SavedStateHandle savedStateHandle;
    public LiveData<List<String>> filteredData;
    public SavedStateViewModel(SavedStateHandle savedStateHandle) {
        this.savedStateHandle = savedStateHandle;
        LiveData<String> queryLiveData = savedStateHandle.getLiveData("query");
        filteredData = Transformations.switchMap(queryLiveData, query -> {
            return repository.getFilteredData(query);
        });
    }

    public void setQuery(String query) {
        savedStateHandle.set("query", query);
    }
}
```

### StateFlow

| **Note:** `StateFlow`support was added in lifecycle version 2.5.0

Retrieve values from`SavedStateHandle`that are wrapped in a[`StateFlow`](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow)observable using[`getStateFlow()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getStateFlow(kotlin.String,kotlin.Any)). When you update the key's value, the`StateFlow`receives the new value. Most often, you might set the value due to user interactions, such as entering a query to filter a list of data. You can then transform this updated value using other[Flow operators](https://developer.android.com/kotlin/flow#modify).  

### Kotlin

```kotlin
class SavedStateViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {
    val filteredData: StateFlow<List<String>> =
        savedStateHandle.getStateFlow<String>("query")
            .flatMapLatest { query ->
                repository.getFilteredData(query)
            }

    fun setQuery(query: String) {
        savedStateHandle["query"] = query
    }
}
```

### Experimental Compose's State support

| **Note:** Experimental Compose State support was added in lifecycle version 2.5.0

The`lifecycle-viewmodel-compose`artifact provides the experimental[`saveable`](https://developer.android.com/reference/kotlin/androidx/lifecycle/viewmodel/compose/package-summary#(androidx.lifecycle.SavedStateHandle).saveable(kotlin.String,androidx.compose.runtime.saveable.Saver,kotlin.Function0))APIs that allow interoperability between`SavedStateHandle`and Compose's[`Saver`](https://developer.android.com/jetpack/compose/state#restore-ui-state)so that any`State`that you can save via[`rememberSaveable`](https://developer.android.com/jetpack/compose/state#restore-ui-state)with a custom`Saver`can also be saved with`SavedStateHandle`.  

### Kotlin

```kotlin
class SavedStateViewModel(private val savedStateHandle: SavedStateHandle) : ViewModel() {

    var filteredData: List<String> by savedStateHandle.saveable {
        mutableStateOf(emptyList())
    }

    fun setQuery(query: String) {
        withMutableSnapshot {
            filteredData += query
        }
    }
}
```

## Supported types

Data kept within a`SavedStateHandle`is saved and restored as a[`Bundle`](https://developer.android.com/reference/android/os/Bundle), along with the rest of the[`savedInstanceState`](https://developer.android.com/topic/libraries/architecture/saving-states)for the activity or fragment.

### Directly supported types

By default, you can call`set()`and`get()`on a`SavedStateHandle`for the same data types as a`Bundle`, as shown below:

|---------------------------|-------------------|
| **Type/Class support**    | **Array support** |
| `double`                  | `double[]`        |
| `int`                     | `int[]`           |
| `long`                    | `long[]`          |
| `String`                  | `String[]`        |
| `byte`                    | `byte[]`          |
| `char`                    | `char[]`          |
| `CharSequence`            | `CharSequence[]`  |
| `float`                   | `float[]`         |
| `Parcelable`              | `Parcelable[]`    |
| `Serializable`            | `Serializable[]`  |
| `short`                   | `short[]`         |
| `SparseArray`             |                   |
| `Binder`                  |                   |
| `Bundle`                  |                   |
| `ArrayList`               |                   |
| `Size (only in API 21+)`  |                   |
| `SizeF (only in API 21+)` |                   |

If the class does not extend one of those in the above list, consider making the class parcelable by adding the[`@Parcelize`](https://developer.android.com/kotlin/parcelize)Kotlin annotation or implementing[`Parcelable`](https://developer.android.com/reference/android/os/Parcelable)directly.

### Saving non-parcelable classes

If a class does not implement`Parcelable`or`Serializable`and cannot be modified to implement one of those interfaces, then it is not possible to directly save an instance of that class into a`SavedStateHandle`.

Beginning with[Lifecycle 2.3.0-alpha03](https://developer.android.com/jetpack/androidx/releases/lifecycle#2.3.0-alpha03),`SavedStateHandle`allows you to save any object by providing your own logic for saving and restoring your object as a[`Bundle`](https://developer.android.com/reference/android/os/Bundle)using the[`setSavedStateProvider()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#setSavedStateProvider(kotlin.String,androidx.savedstate.SavedStateRegistry.SavedStateProvider))method.[`SavedStateRegistry.SavedStateProvider`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry.SavedStateProvider)is an interface that defines a single[`saveState()`](https://developer.android.com/reference/androidx/savedstate/SavedStateRegistry.SavedStateProvider#saveState())method that returns a`Bundle`containing the state you want to save. When`SavedStateHandle`is ready to save its state, it calls`saveState()`to retrieve the`Bundle`from the`SavedStateProvider`and saves the`Bundle`for the associated key.

Consider an example of an app that requests an image from the camera app via the[`ACTION_IMAGE_CAPTURE`](https://developer.android.com/reference/android/provider/MediaStore#ACTION_IMAGE_CAPTURE)intent, passing in a temporary file for where the camera should store the image. The`TempFileViewModel`encapsulates the logic for creating that temporary file.  

### Kotlin

```kotlin
class TempFileViewModel : ViewModel() {
    private var tempFile: File? = null

    fun createOrGetTempFile(): File {
        return tempFile ?: File.createTempFile("temp", null).also {
            tempFile = it
        }
    }
}
```

### Java

```java
class TempFileViewModel extends ViewModel {
    private File tempFile = null;

    public TempFileViewModel() {
    }


    @NonNull
    public File createOrGetTempFile() {
        if (tempFile == null) {
            tempFile = File.createTempFile("temp", null);
        }
        return tempFile;
    }
}
```

To ensure the temporary file is not lost if the activity's process is killed and later restored,`TempFileViewModel`can use the`SavedStateHandle`to persist its data. To allow`TempFileViewModel`to save its data, implement`SavedStateProvider`and set it as a provider on the`SavedStateHandle`of the`ViewModel`:  

### Kotlin

```kotlin
private fun File.saveTempFile() = bundleOf("path", absolutePath)

class TempFileViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
    private var tempFile: File? = null
    init {
        savedStateHandle.setSavedStateProvider("temp_file") { // saveState()
            if (tempFile != null) {
                tempFile.saveTempFile()
            } else {
                Bundle()
            }
        }
    }

    fun createOrGetTempFile(): File {
        return tempFile ?: File.createTempFile("temp", null).also {
            tempFile = it
        }
    }
}
```

### Java

```java
class TempFileViewModel extends ViewModel {
    private File tempFile = null;

    public TempFileViewModel(SavedStateHandle savedStateHandle) {
        savedStateHandle.setSavedStateProvider("temp_file",
            new TempFileSavedStateProvider());
    }
    @NonNull
    public File createOrGetTempFile() {
        if (tempFile == null) {
            tempFile = File.createTempFile("temp", null);
        }
        return tempFile;
    }

    private class TempFileSavedStateProvider implements SavedStateRegistry.SavedStateProvider {
        @NonNull
        @Override
        public Bundle saveState() {
            Bundle bundle = new Bundle();
            if (tempFile != null) {
                bundle.putString("path", tempFile.getAbsolutePath());
            }
            return bundle;
        }
    }
}
```

To restore the`File`data when the user returns, retrieve the`temp_file``Bundle`from the`SavedStateHandle`. This is the same`Bundle`provided by`saveTempFile()`that contains the absolute path. The absolute path can then be used to instantiate a new`File`.  

### Kotlin

```kotlin
private fun File.saveTempFile() = bundleOf("path", absolutePath)

private fun Bundle.restoreTempFile() = if (containsKey("path")) {
    File(getString("path"))
} else {
    null
}

class TempFileViewModel(savedStateHandle: SavedStateHandle) : ViewModel() {
    private var tempFile: File? = null
    init {
        val tempFileBundle = savedStateHandle.get<Bundle>("temp_file")
        if (tempFileBundle != null) {
            tempFile = tempFileBundle.restoreTempFile()
        }
        savedStateHandle.setSavedStateProvider("temp_file") { // saveState()
            if (tempFile != null) {
                tempFile.saveTempFile()
            } else {
                Bundle()
            }
        }
    }

    fun createOrGetTempFile(): File {
      return tempFile ?: File.createTempFile("temp", null).also {
          tempFile = it
      }
    }
}
```

### Java

```java
class TempFileViewModel extends ViewModel {
    private File tempFile = null;

    public TempFileViewModel(SavedStateHandle savedStateHandle) {
        Bundle tempFileBundle = savedStateHandle.get("temp_file");
        if (tempFileBundle != null) {
            tempFile = TempFileSavedStateProvider.restoreTempFile(tempFileBundle);
        }
        savedStateHandle.setSavedStateProvider("temp_file", new TempFileSavedStateProvider());
    }

    @NonNull
    public File createOrGetTempFile() {
        if (tempFile == null) {
            tempFile = File.createTempFile("temp", null);
        }
        return tempFile;
    }

    private class TempFileSavedStateProvider implements SavedStateRegistry.SavedStateProvider {
        @NonNull
        @Override
        public Bundle saveState() {
            Bundle bundle = new Bundle();
            if (tempFile != null) {
                bundle.putString("path", tempFile.getAbsolutePath());
            }
            return bundle;
        }

        @Nullable
        private static File restoreTempFile(Bundle bundle) {
            if (bundle.containsKey("path") {
                return File(bundle.getString("path"));
            }
            return null;
        }
    }
}
```

## SavedStateHandle in tests

To test a`ViewModel`that takes a`SavedStateHandle`as a dependency, create a new instance of`SavedStateHandle`with the test values it requires and pass it to the`ViewModel`instance you are testing.  

### Kotlin

```kotlin
class MyViewModelTest {

    private lateinit var viewModel: MyViewModel

    @Before
    fun setup() {
        val savedState = SavedStateHandle(mapOf("someIdArg" to testId))
        viewModel = MyViewModel(savedState = savedState)
    }
}
```

## Additional resources

For further information about the Saved State module for`ViewModel`, see the following resources.

### Codelabs

- [Android lifecycle-aware components codelab](https://codelabs.developers.google.com/codelabs/android-lifecycles/#6)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
- [Work with observable data objects](https://developer.android.com/topic/libraries/data-binding/observability)
- [Create ViewModels with dependencies](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-factories)