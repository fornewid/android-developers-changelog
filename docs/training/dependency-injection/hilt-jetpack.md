---
title: https://developer.android.com/training/dependency-injection/hilt-jetpack
url: https://developer.android.com/training/dependency-injection/hilt-jetpack
source: md.txt
---

Hilt includes extensions for providing classes from other Jetpack libraries.
Hilt currently supports the following Jetpack components:

- Compose
- `ViewModel`
- Navigation
- WorkManager

You must add the Hilt dependencies to take advantage of these integrations. For
more information about adding dependencies, see [Dependency injection with
Hilt](https://developer.android.com/training/dependency-injection/hilt-android#setup).

## Integration with Jetpack Compose

To see how Hilt integrates with Jetpack Compose, see the Hilt section of
[Compose and other libraries](https://developer.android.com/jetpack/compose/libraries#hilt).

## Inject ViewModel objects with Hilt

Provide a [`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel) by annotating
it with `@HiltViewModel` and using the `@Inject` annotation in the `ViewModel`
object's constructor.

```kotlin
@HiltViewModel
class ExampleViewModel @Inject constructor(
  private val savedStateHandle: SavedStateHandle,
  private val repository: ExampleRepository
) : ViewModel() {
  ...
}
```

Then, an activity that is annotated with `@AndroidEntryPoint` can
get the `ViewModel` instance as normal using `ViewModelProvider` or the
`by viewModels()` [KTX extensions](https://developer.android.com/kotlin/ktx):

```kotlin
@AndroidEntryPoint
class ExampleActivity : AppCompatActivity() {
  private val exampleViewModel: ExampleViewModel by viewModels()
  ...
}
```

### Use assisted injection with ViewModels

Hilt supports assisted injection for ViewModels. Assisted injection lets you
inject dynamic runtime arguments alongside Hilt-managed dependencies. To use
assisted injection, annotate your ViewModel constructor with `@AssistedInject`,
and mark dynamic parameters with `@Assisted`. You must also define an
`@AssistedFactory` interface, which acts as a bridge for Hilt to automatically
generate the necessary `@ViewModelProvider.Factory`.

```kotlin
@HiltViewModel(assistedFactory = MyViewModel.Factory::class)
class MyViewModel @AssistedInject constructor(
    @Assisted val userId: String,
    private val repository: MyRepository
) : ViewModel() {
    @AssistedFactory interface Factory {
        fun create(userId: String): MyViewModel
    }
}
```

In Compose, you can use the assisted factory by passing it into the
`hiltViewModel` function during navigation or screen initialization. This
approach eliminates the need for manual factory boilerplate while keeping your
ViewModel correctly scoped to the navigation back stack. For more information,
see the Hilt documentation on [assisted injection](https://dagger.dev/hilt/view-model#assisted-injection).

### @ViewModelScoped

All Hilt ViewModels are provided by the `ViewModelComponent` which follows the
same lifecycle as a `ViewModel`, and as such, can survive configuration changes.
To scope a dependency to a `ViewModel` use the `@ViewModelScoped` annotation.

A `@ViewModelScoped` type will make it so that a single instance of the scoped
type is provided across all dependencies injected into the `ViewModel`.
Other instances of a ViewModel that request the scoped instance will receive
a different instance.

If a single instance needs to be shared across various ViewModels, then it
should be scoped using either `@ActivityRetainedScoped` or `@Singleton`.

## Integration with the Jetpack navigation libraries

Add the following additional dependencies to your Gradle file:

app/build.gradle

### Kotlin

```kotlin
dependencies {
    ...
    implementation("androidx.hilt:hilt-lifecycle-viewmodel-compose:1.3.0")
}
```

### Groovy

```groovy
dependencies {
    ...
    implementation 'androidx.hilt:hilt-lifecycle-viewmodel-compose:1.3.0'
}
```

In Jetpack Compose, the Navigation Compose and Navigation 3 libraries
both use the `hiltViewModel` function to automatically retrieve a ViewModel
scoped to the current navigation destination.

In Navigation 3, navigation destinations are represented by `NavEntry`s.
[Scope ViewModels to `NavEntry`s](https://developer.android.com/guide/navigation/navigation-3/save-state#scoping-viewmodels) using
`rememberViewModelStoreNavEntryDecorator`. Use `hiltViewModel` inside the
provider for that `NavEntry` to retrieve the associated ViewModel.

```kotlin
NavDisplay(...,
  entryDecorators = listOf(..., rememberViewModelStoreNavEntryDecorator()),
  entryProvider = entryProvider {
    entry { key ->
      val viewModel = hiltViewModel()
      MyScreen(viewModel = viewModel)
    }
  }
)
```

In Navigation Compose, ViewModels are automatically scoped to navigation
destinations. For more information, see [Hilt and Navigation](https://developer.android.com/develop/ui/compose/libraries#hilt-navigation).

```kotlin
val viewModel = hiltViewModel()
```

## Inject WorkManager with Hilt

Add the following additional dependencies to your Gradle file. Note that in
addition to the library, you need to include an additional annotation processor
that works on top of the Hilt annotation processor:

app/build.gradle

### Kotlin

```kotlin
dependencies {
    implementation("androidx.hilt:hilt-work:1.0.0")
    // When using Kotlin.
    ksp("androidx.hilt:hilt-compiler:1.3.0")
}
```

### Groovy

```groovy
dependencies {
  ...
  implementation 'androidx.hilt:hilt-work:1.0.0'
  // When using Kotlin.
  ksp 'androidx.hilt:hilt-compiler:1.3.0'
}
```

Inject a [`Worker`](https://developer.android.com/reference/kotlin/androidx/work/Worker) using the
`@HiltWorker` annotation in the class and `@AssistedInject` in the `Worker`
object's constructor. You can use only `@Singleton` or unscoped bindings in
`Worker` objects. You must also annotate the `Context` and `WorkerParameters`
dependencies with `@Assisted`:

```kotlin
@HiltWorker
class ExampleWorker @AssistedInject constructor(
  @Assisted appContext: Context,
  @Assisted workerParams: WorkerParameters,
  workerDependency: WorkerDependency
) : Worker(appContext, workerParams) { ... }
```

Then, have your [`Application`](https://developer.android.com/reference/kotlin/android/app/Application) class
implement the `Configuration.Provider` interface, inject an instance of
`HiltWorkFactory`, and pass it into the `WorkManager` configuration as follows:

```kotlin
@HiltAndroidApp
class ExampleApplication : Application(), Configuration.Provider {

  @Inject lateinit var workerFactory: HiltWorkerFactory

  override fun getWorkManagerConfiguration() =
      Configuration.Builder()
            .setWorkerFactory(workerFactory)
            .build()
}
```

> [!NOTE]
> **Note:** Because this customizes the `WorkManager` configuration, you also must remove the default initializer from the `AndroidManifest.xml` file as specified in the [WorkManager docs](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration).