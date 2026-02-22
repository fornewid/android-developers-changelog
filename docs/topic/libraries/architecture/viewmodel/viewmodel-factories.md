---
title: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-factories
url: https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-factories
source: md.txt
---

# Create ViewModels with dependencies

# Create ViewModels with dependencies
Part of [Android Jetpack](https://developer.android.com/jetpack).

Following [dependency injection's](https://developer.android.com/dependency-injection) best practices, ViewModels can
take dependencies as parameters in their constructor. These are mostly of types
from the [domain](https://developer.android.com/topic/architecture/domain-layer) or [data](https://developer.android.com/topic/architecture/data-layer) layers. Because the framework provides the
ViewModels, a special mechanism is required to create instances of them. That
mechanism is the `ViewModelProvider.Factory` interface. Only **implementations
of this interface can instantiate ViewModels in the right scope**.
| **Note:** If the `ViewModel` takes no dependencies or just the [SavedStateHandle
| type as a dependency](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate), you don't need to provide a factory for the framework to instantiate instances of that `ViewModel` type.
| **Note:** When [injecting ViewModels using Hilt](https://developer.android.com/training/dependency-injection/hilt-jetpack#viewmodels) as a dependency injection solution, you don't have to define a `ViewModel` factory manually. Hilt generates a factory that knows how to create all ViewModels annotated with `@HiltViewModel` for you at compile time. Classes annotated with `@AndroidEntryPoint` can directly access the Hilt generated factory when calling the regular `ViewModel` APIs.

## ViewModels with CreationExtras

If a `ViewModel` class receives dependencies in its constructor, provide a
factory that implements the [`ViewModelProvider.Factory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory) interface.
Override the [`create(Class<T>, CreationExtras)`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory#create(java.lang.Class,androidx.lifecycle.viewmodel.CreationExtras)) function to provide a
new instance of the ViewModel.

[`CreationExtras`](https://developer.android.com/reference/androidx/lifecycle/viewmodel/CreationExtras) allows you to access relevant information that helps
instantiate a ViewModel. Here's a list of keys that can be accessed from extras:

|                                                                                               Key                                                                                               |                                           Functionality                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [`ViewModelProvider.NewInstanceFactory.VIEW_MODEL_KEY`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.NewInstanceFactory.Companion#VIEW_MODEL_KEY())             | Provides access to the custom key you passed to `ViewModelProvider.get()`.                        |
| [`ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.AndroidViewModelFactory.Companion#APPLICATION_KEY()) | Provides access to the instance of the `Application` class.                                       |
| [`SavedStateHandleSupport.DEFAULT_ARGS_KEY`](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#DEFAULT_ARGS_KEY())                                              | Provides access to the Bundle of arguments you should use to construct `SavedStateHandle`.        |
| [`SavedStateHandleSupport.SAVED_STATE_REGISTRY_OWNER_KEY`](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#SAVED_STATE_REGISTRY_OWNER_KEY())                  | Provides access to the `SavedStateRegistryOwner` that is being used to construct the `ViewModel`. |
| [`SavedStateHandleSupport.VIEW_MODEL_STORE_OWNER_KEY`](https://developer.android.com/reference/kotlin/androidx/lifecycle/package-summary#VIEW_MODEL_STORE_OWNER_KEY())                          | Provides access to the `ViewModelStoreOwner` that is being used to construct the `ViewModel`.     |

To create a new instance of [`SavedStateHandle`](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate), use the
[`CreationExtras.createSavedStateHandle()`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandleSupport#(androidx.lifecycle.viewmodel.CreationExtras)
function and pass it to the ViewModel.

### CreationExtras with APPLICATION_KEY

The following is an example of how to provide an instance of a `ViewModel` that
takes a [repository](https://developer.android.com/topic/architecture/data-layer#architecture) scoped to the `Application` class and
`SavedStateHandle` as dependencies:  

### Kotlin

        import androidx.lifecycle.SavedStateHandle
        import androidx.lifecycle.ViewModel
        import androidx.lifecycle.ViewModelProvider
        import androidx.lifecycle.ViewModelProvider.AndroidViewModelFactory.Companion.APPLICATION_KEY
        import androidx.lifecycle.createSavedStateHandle
        import androidx.lifecycle.viewmodel.CreationExtras

        class MyViewModel(
            private val myRepository: MyRepository,
            private val savedStateHandle: SavedStateHandle
        ) : ViewModel() {

            // ViewModel logic
            // ...

            // Define ViewModel factory in a companion object
            companion object {

                val Factory: ViewModelProvider.Factory = object : ViewModelProvider.Factory {
                    @Suppress("UNCHECKED_CAST")
                    override fun <T : ViewModel> create(
                        modelClass: Class<T>,
                        extras: CreationExtras
                    ): T {
                        // Get the Application object from extras
                        val application = checkNotNull(extras[APPLICATION_KEY])
                        // Create a SavedStateHandle for this ViewModel from extras
                        val savedStateHandle = extras.createSavedStateHandle()

                        return MyViewModel(
                            (application as MyApplication).myRepository,
                            savedStateHandle
                        ) as T
                    }
                }
            }
        }

### Java

    import static androidx.lifecycle.SavedStateHandleSupport.createSavedStateHandle;
    import static androidx.lifecycle.ViewModelProvider.AndroidViewModelFactory.APPLICATION_KEY;

    import androidx.lifecycle.SavedStateHandle;
    import androidx.lifecycle.ViewModel;
    import androidx.lifecycle.viewmodel.ViewModelInitializer;

    public class MyViewModel extends ViewModel {

        public MyViewModel(
            MyRepository myRepository,
            SavedStateHandle savedStateHandle
        ) { /* Init ViewModel here */ }

        static final ViewModelInitializer<MyViewModel> initializer = new ViewModelInitializer<>(
            MyViewModel.class,
            creationExtras -> {
                MyApplication app = (MyApplication) creationExtras.get(APPLICATION_KEY);
                assert app != null;
                SavedStateHandle savedStateHandle = createSavedStateHandle(creationExtras);

                return new MyViewModel(app.getMyRepository(), savedStateHandle);
            }
        );
    }

| **Note:** It's a good practice to place `ViewModel` factories in their ViewModel file for better context, readability, and easier discovery. The same ViewModel factory can be used for multiple ViewModels when they share dependencies, as it's the case for the [Architecture Blueprints](https://github.com/android/architecture-samples/blob/views/app/src/main/java/com/example/android/architecture/blueprints/todoapp/ViewModelFactory.kt) sample.

Then, you can use this factory when retrieving an instance of the ViewModel:  

### Kotlin

    import androidx.activity.viewModels

    class MyActivity : AppCompatActivity() {

        private val viewModel: MyViewModel by viewModels { MyViewModel.Factory }

        // Rest of Activity code
    }

### Java

    import androidx.appcompat.app.AppCompatActivity;
    import androidx.lifecycle.ViewModelProvider;

    public class MyActivity extends AppCompatActivity {

    MyViewModel myViewModel = new ViewModelProvider(
        this,
        ViewModelProvider.Factory.from(MyViewModel.initializer)
    ).get(MyViewModel.class);

    // Rest of Activity code
    }

### Jetpack Compose

    import androidx.lifecycle.viewmodel.compose.viewModel

    @Composable
    fun MyScreen(
        modifier: Modifier = Modifier,
        viewModel: MyViewModel = viewModel(factory = MyViewModel.Factory)
    ) {
        // ...
    }

Alternatively, use the `ViewModel` factory DSL to create factories using a more
idiomatic Kotlin API:  

    import androidx.lifecycle.SavedStateHandle
    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.ViewModelProvider
    import androidx.lifecycle.ViewModelProvider.AndroidViewModelFactory.Companion.APPLICATION_KEY
    import androidx.lifecycle.createSavedStateHandle
    import androidx.lifecycle.viewmodel.initializer
    import androidx.lifecycle.viewmodel.viewModelFactory

    class MyViewModel(
        private val myRepository: MyRepository,
        private val savedStateHandle: SavedStateHandle
    ) : ViewModel() {
        // ViewModel logic

        // Define ViewModel factory in a companion object
        companion object {
            val Factory: ViewModelProvider.Factory = viewModelFactory {
                initializer {
                    val savedStateHandle = createSavedStateHandle()
                    val myRepository = (this[APPLICATION_KEY] as MyApplication).myRepository
                    MyViewModel(
                        myRepository = myRepository,
                        savedStateHandle = savedStateHandle
                    )
                }
            }
        }
    }

### Pass custom parameters as CreationExtras

You can pass dependencies to your `ViewModel` through `CreationExtras` by
creating a custom key.
This can be useful if your `ViewModel` depends on objects which are not
accessible through the `Application` class and `APPLICATION_KEY`. An example of
this is when your `ViewModel` is created inside a Kotlin
Multiplatform module and therefore does not have access to Android dependencies.

In this example, the `ViewModel` defines a custom key and uses it in the
`ViewModelProvider.Factory`.  

    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.ViewModelProvider
    import androidx.lifecycle.viewModelScope
    import androidx.lifecycle.viewmodel.CreationExtras
    import androidx.lifecycle.viewmodel.initializer
    import androidx.lifecycle.viewmodel.viewModelFactory

    class MyViewModel(
        private val myRepository: MyRepository,
    ) : ViewModel() {
        // ViewModel logic

        // Define ViewModel factory in a companion object
        companion object {

            // Define a custom key for your dependency
            val MY_REPOSITORY_KEY = object : CreationExtras.Key<MyRepository> {}

            val Factory: ViewModelProvider.Factory = viewModelFactory {
                initializer {
                    // Get the dependency in your factory
                    val myRepository = this[MY_REPOSITORY_KEY] as MyRepository
                    MyViewModel(
                        myRepository = myRepository,
                    )
                }
            }
        }
    }

You can instantiate a `ViewModel` with a `CreationExtras.Key` from a
[`ViewModelStoreOwner`](https://developer.android.com/reference/androidx/lifecycle/ViewModelStoreOwner) such as
`ComponentActivity`, `Fragment`, or `NavBackStackEntry`, or with
Jetpack Compose.  

### Kotlin

    import androidx.lifecycle.ViewModelProvider
    import androidx.lifecycle.ViewModelStoreOwner
    import androidx.lifecycle.viewmodel.CreationExtras
    import androidx.lifecycle.viewmodel.MutableCreationExtras
    // ...
        // Use from ComponentActivity, Fragment, NavBackStackEntry,
        // or another ViewModelStoreOwner.
        val viewModelStoreOwner: ViewModelStoreOwner = this
        val myViewModel: MyViewModel = ViewModelProvider.create(
            viewModelStoreOwner,
            factory = MyViewModel.Factory,
            extras = MutableCreationExtras().apply {
                set(MyViewModel.MY_REPOSITORY_KEY, myRepository)
            },
        )[MyViewModel::class]

### Jetpack Compose

    import androidx.lifecycle.viewmodel.MutableCreationExtras
    import androidx.lifecycle.viewmodel.compose.viewModel
    // ...
    @Composable
    fun MyApp(myRepository: MyRepository) {
        val extras = MutableCreationExtras().apply {
            set(MyViewModel.MY_REPOSITORY_KEY, myRepository)
        }
        val viewModel: MyViewModel = viewModel(
            factory = MyViewModel.Factory,
            extras = extras,
        )
    }

## Factories for ViewModel version older than 2.5.0

If you're using a version of `ViewModel` older than 2.5.0, you need to provide
factories from a subset of classes that extend [`ViewModelProvider.Factory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory)
and implement the `create(Class<T>)` function. Depending on what dependencies
the `ViewModel` needs, a different class needs to be extended from:

- [`AndroidViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.AndroidViewModelFactory) if the `Application` class is needed.
- [`AbstractSavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/AbstractSavedStateViewModelFactory) if [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getStateFlow(kotlin.String,kotlin.Any)) needs to be passed as a dependency.

If `Application` or `SavedStateHandle` aren't needed, simply extend from
`ViewModelProvider.Factory`.

The following example uses an [`AbstractSavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/AbstractSavedStateViewModelFactory) for a
ViewModel that takes a repository and a [`SavedStateHandle`](https://developer.android.com/reference/androidx/lifecycle/SavedStateHandle#getStateFlow(kotlin.String,kotlin.Any)) type as a
dependency:  

### Kotlin

    class MyViewModel(
    private val myRepository: MyRepository,
    private val savedStateHandle: SavedStateHandle
    ) : ViewModel() {

    // ViewModel logic ...

    // Define ViewModel factory in a companion object
    companion object {
        fun provideFactory(
            myRepository: MyRepository,
            owner: SavedStateRegistryOwner,
            defaultArgs: Bundle? = null,
        ): AbstractSavedStateViewModelFactory =
            object : AbstractSavedStateViewModelFactory(owner, defaultArgs) {
                @Suppress("UNCHECKED_CAST")
                override fun <T : ViewModel> create(
                    key: String,
                    modelClass: Class<T>,
                    handle: SavedStateHandle
                ): T {
                    return MyViewModel(myRepository, handle) as T
                }
            }
        }
    }

### Java

    import androidx.annotation.NonNull;
    import androidx.lifecycle.AbstractSavedStateViewModelFactory;
    import androidx.lifecycle.SavedStateHandle;
    import androidx.lifecycle.ViewModel;

    public class MyViewModel extends ViewModel {
        public MyViewModel(
            MyRepository myRepository,
            SavedStateHandle savedStateHandle
        ) { /* Init ViewModel here */ }
    }

    public class MyViewModelFactory extends AbstractSavedStateViewModelFactory {

        private final MyRepository myRepository;

        public MyViewModelFactory(
            MyRepository myRepository
        ) {
            this.myRepository = myRepository;
        }

        @SuppressWarnings("unchecked")
        @NonNull
        @Override
        protected <T extends ViewModel> T create(
            @NonNull String key, @NonNull Class<T> modelClass, @NonNull SavedStateHandle handle
        ) {
            return (T) new MyViewModel(myRepository, handle);
        }
    }

| **Warning:** if you're using a version of `ViewModel` older than 2.5.0, you might have the option to override a create function with `CreationExtras` in its signature. Don't override that function. Instead, override the `create` function that has the `key, modelClass` and `savedStateHandle` parameters.

Then, you can use factory to retrieve your ViewModel:  

### Kotlin

    import androidx.activity.viewModels

    class MyActivity : AppCompatActivity() {

        private val viewModel: MyViewModel by viewModels {
            MyViewModel.provideFactory((application as MyApplication).myRepository, this)
        }

        // Rest of Activity code
    }

### Java

    import androidx.appcompat.app.AppCompatActivity;
    import androidx.lifecycle.ViewModelProvider;

    public class MyActivity extends AppCompatActivity {

        MyViewModel myViewModel = new ViewModelProvider(
            this,
            ViewModelProvider.Factory.from(MyViewModel.initializer)
        ).get(MyViewModel.class);

        // Rest of Activity code
    }

### Jetpack Compose

    import androidx.lifecycle.viewmodel.compose.viewModel

    @Composable
    fun MyScreen(
        modifier: Modifier = Modifier,
        viewModel: MyViewModel = viewModel(
            factory = MyViewModel.provideFactory(
                (LocalContext.current.applicationContext as MyApplication).myRepository,
                owner = LocalSavedStateRegistryOwner.current
            )
        )
    ) {
        // ...
    }

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
- [LiveData overview](https://developer.android.com/topic/libraries/architecture/livedata)