---
title: https://developer.android.com/training/dependency-injection/hilt-jetpack
url: https://developer.android.com/training/dependency-injection/hilt-jetpack
source: md.txt
---

# Use Hilt with other Jetpack libraries

Hilt includes extensions for providing classes from other Jetpack libraries. Hilt currently supports the following Jetpack components:

- `ViewModel`
- Navigation
- Compose
- WorkManager

You must add the Hilt dependencies to take advantage of these integrations. For more information about adding dependencies, see[Dependency injection with Hilt](https://developer.android.com/training/dependency-injection/hilt-android#setup).

## Inject ViewModel objects with Hilt

Provide a[`ViewModel`](https://developer.android.com/topic/libraries/architecture/viewmodel)by annotating it with`@HiltViewModel`and using the`@Inject`annotation in the`ViewModel`object's constructor.  

### Kotlin

```kotlin
@HiltViewModel
class ExampleViewModel @Inject constructor(
  private val savedStateHandle: SavedStateHandle,
  private val repository: ExampleRepository
) : ViewModel() {
  ...
}
```

### Java

```java
@HiltViewModel
public class ExampleViewModel extends ViewModel {

  private final ExampleRepository repository;
  private final SavedStateHandle savedStateHandle;

  @Inject
  ExampleViewModel(
      SavedStateHandle savedStateHandle,
      ExampleRepository repository)
    {
    this.savedStateHandle = savedStateHandle;
    this.repository = repository;
  }
  ...
}
```

Then, an activity or a fragment that is annotated with`@AndroidEntryPoint`can get the`ViewModel`instance as normal using`ViewModelProvider`or the`by viewModels()`[KTX extensions](https://developer.android.com/kotlin/ktx):  

### Kotlin

```kotlin
@AndroidEntryPoint
class ExampleActivity : AppCompatActivity() {
  private val exampleViewModel: ExampleViewModel by viewModels()
  ...
}
```

### Java

```java
@AndroidEntryPoint
public class ExampleActivity extends AppCompatActivity {

  private ExampleViewModel exampleViewModel;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    exampleViewModel = new ViewModelProvider(this).get(ExampleViewModel.class);
  }
  ...
}
```
| **Note:** To use Dagger's assisted injection with ViewModels, see the following[Github issue](https://github.com/google/dagger/issues/2287).

### @ViewModelScoped

All Hilt ViewModels are provided by the`ViewModelComponent`which follows the same lifecycle as a`ViewModel`, and as such, can survive configuration changes. To scope a dependency to a`ViewModel`use the`@ViewModelScoped`annotation.

A`@ViewModelScoped`type will make it so that a single instance of the scoped type is provided across all dependencies injected into the`ViewModel`. Other instances of a ViewModel that request the scoped instance will receive a different instance.

If a single instance needs to be shared across various ViewModels, then it should be scoped using either`@ActivityRetainedScoped`or`@Singleton`.

## Integration with the Jetpack navigation library

Add the following additional dependencies to your Gradle file:

app/build.gradle  

### Groovy

```groovy
dependencies {
    ...
    implementation 'androidx.hilt:hilt-navigation-fragment:1.0.0'
}
```

### Kotlin

```kotlin
dependencies {
    ...
    implementation("androidx.hilt:hilt-navigation-fragment:1.0.0")
}
```

If your`ViewModel`is[scoped to the navigation graph](https://developer.android.com/guide/navigation/navigation-programmatic#share_ui-related_data_between_destinations_with_viewmodel), use the`hiltNavGraphViewModels`function that works with fragments that are annotated with`@AndroidEntryPoint`.  

### Kotlin

```kotlin
val viewModel: ExampleViewModel by hiltNavGraphViewModels(R.id.my_graph)
```

### Java

```java
NavBackStackEntry backStackEntry = navController.getBackStackEntry(R.id.my_graph);

ExampleViewModel exampleViewModel = new ViewModelProvider(
  backStackEntry,
  HiltViewModelFactory.create(context, backStackEntry)
).get(ExampleViewModel.class)
```

## Integration with Jetpack Compose

To see how Hilt integrates with Jetpack Compose, see the Hilt section of[Compose and other libraries](https://developer.android.com/jetpack/compose/libraries#hilt).

## Inject WorkManager with Hilt

Add the following additional dependencies to your Gradle file. Note that in addition to the library, you need to include an additional annotation processor that works on top of the Hilt annotation processor:

app/build.gradle  

### Groovy

```groovy
dependencies {
  ...
  implementation 'androidx.hilt:hilt-work:1.0.0'
  // When using Kotlin.
  kapt 'androidx.hilt:hilt-compiler:1.0.0'
  // When using Java.
  annotationProcessor 'androidx.hilt:hilt-compiler:1.0.0'
}
```

### Kotlin

```kotlin
dependencies {
    implementation("androidx.hilt:hilt-work:1.0.0")
    // When using Kotlin.
    kapt("androidx.hilt:hilt-compiler:1.0.0")
    // When using Java.
    annotationProcessor("androidx.hilt:hilt-compiler:1.0.0")
}
```

Inject a[`Worker`](https://developer.android.com/reference/kotlin/androidx/work/Worker)using the`@HiltWorker`annotation in the class and`@AssistedInject`in the`Worker`object's constructor. You can use only`@Singleton`or unscoped bindings in`Worker`objects. You must also annotate the`Context`and`WorkerParameters`dependencies with`@Assisted`:  

### Kotlin

```kotlin
@HiltWorker
class ExampleWorker @AssistedInject constructor(
  @Assisted appContext: Context,
  @Assisted workerParams: WorkerParameters,
  workerDependency: WorkerDependency
) : Worker(appContext, workerParams) { ... }
```

### Java

```java
@HiltWorker
public class ExampleWorker extends Worker {

  private final WorkerDependency workerDependency;

  @AssistedInject
  ExampleWorker(
    @Assisted @NonNull Context context,
    @Assisted @NonNull WorkerParameters params,
    WorkerDependency workerDependency
  ) {
    super(context, params);
    this.workerDependency = workerDependency;
  }
  ...
}
```

Then, have your[`Application`](https://developer.android.com/reference/android/app/Application)class implement the`Configuration.Provider`interface, inject an instance of`HiltWorkFactory`, and pass it into the`WorkManager`configuration as follows:  

### Kotlin

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

### Java

```java
@HiltAndroidApp
public class ExampleApplication extends Application implements Configuration.Provider {

  @Inject HiltWorkerFactory workerFactory;

  @Override
  public Configuration getWorkManagerConfiguration() {
    return new Configuration.Builder()
             .setWorkerFactory(workerFactory)
             .build();
  }
}
```
| **Note:** Because this customizes the`WorkManager`configuration, you also must remove the default initializer from the`AndroidManifest.xml`file as specified in the[WorkManager docs](https://developer.android.com/topic/libraries/architecture/workmanager/advanced/custom-configuration).
| **Warning:** `WorkManager`version`2.6.0-alpha01`or higher uses the`androidx.startup`initializer. To properly configure`WorkManager`in this version with Hilt, check out the[`WorkManager`release notes](https://developer.android.com/jetpack/androidx/releases/work#2.6.0-alpha01).