---
title: https://developer.android.com/topic/libraries/architecture/views/viewmodel/viewmodel-factories-views
url: https://developer.android.com/topic/libraries/architecture/views/viewmodel/viewmodel-factories-views
source: md.txt
---

# Create ViewModels with dependencies (Views)
Part of [Android Jetpack](https://developer.android.com/jetpack).

[Concepts and Jetpack Compose implementation](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-factories)

Following [dependency injection's](https://developer.android.com/dependency-injection) best practices, ViewModels can
take dependencies as parameters in their constructor. These are mostly of types
from the [domain](https://developer.android.com/topic/architecture/domain-layer) or [data](https://developer.android.com/topic/architecture/data-layer) layers. Because the framework provides the
ViewModels, a special mechanism is required to create instances of them. That
mechanism is the `ViewModelProvider.Factory` interface. Only **implementations
of this interface can instantiate ViewModels in the right scope**.

> [!NOTE]
> **Note:** If the `ViewModel` takes no dependencies or just the [SavedStateHandle
> type as a dependency](https://developer.android.com/topic/libraries/architecture/viewmodel-savedstate), you don't need to provide a factory for the framework to instantiate instances of that `ViewModel` type.

> [!NOTE]
> **Note:** When [injecting ViewModels using Hilt](https://developer.android.com/training/dependency-injection/hilt-jetpack#viewmodels) as a dependency injection solution, you don't have to define a `ViewModel` factory manually. Hilt generates a factory that knows how to create all ViewModels annotated with `@HiltViewModel` for you at compile time. Classes annotated with `@AndroidEntryPoint` can directly access the Hilt generated factory when calling the regular `ViewModel` APIs.

## ViewModels with CreationExtras

If a `ViewModel` class receives dependencies in its constructor, provide a
factory that implements the [`ViewModelProvider.Factory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory) interface.
Override the [`create(Class<T>, CreationExtras)`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory#create(java.lang.Class,androidx.lifecycle.viewmodel.CreationExtras)) function to provide a
new instance of the ViewModel.

### CreationExtras with APPLICATION_KEY

The following is an example of how to provide an instance of a `ViewModel` that
takes a [repository](https://developer.android.com/topic/architecture/data-layer#architecture) scoped to the `Application` class and
`SavedStateHandle` as dependencies:

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

> [!NOTE]
> **Note:** It's a good practice to place `ViewModel` factories in their ViewModel file for better context, readability, and easier discovery. The same ViewModel factory can be used for multiple ViewModels when they share dependencies, as it's the case for the [Architecture Blueprints](https://github.com/android/architecture-samples/blob/views/app/src/main/java/com/example/android/architecture/blueprints/todoapp/ViewModelFactory.kt) sample.

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
`ComponentActivity`, `Fragment`, or `NavBackStackEntry`.

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

## Factories for ViewModel version older than 2.5.0

If you're using a version of `ViewModel` older than 2.5.0, you need to provide
factories from a subset of classes that extend [`ViewModelProvider.Factory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.Factory)
and implement the `create(Class<T>)` function. Depending on what dependencies
the `ViewModel` needs, a different class needs to be extended from:

- [`AndroidViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/ViewModelProvider.AndroidViewModelFactory) if the `Application` class is needed.
- [`AbstractSavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/AbstractSavedStateViewModelFactory) if [`SavedStateHandle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle) needs to be passed as a dependency.

If `Application` or `SavedStateHandle` aren't needed, simply extend from
`ViewModelProvider.Factory`.

The following example uses an [`AbstractSavedStateViewModelFactory`](https://developer.android.com/reference/androidx/lifecycle/AbstractSavedStateViewModelFactory) for a
ViewModel that takes a repository and a [`SavedStateHandle`](https://developer.android.com/reference/kotlin/androidx/lifecycle/SavedStateHandle) type as a
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

> [!WARNING]
> **Warning:** if you're using a version of `ViewModel` older than 2.5.0, you might have the option to override a create function with `CreationExtras` in its signature. Don't override that function. Instead, override the `create` function that has the `key, modelClass` and `savedStateHandle` parameters.

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

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Saved State module for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
- [Save UI states](https://developer.android.com/topic/libraries/architecture/saving-states)
- [LiveData overview](https://developer.android.com/topic/libraries/architecture/livedata)