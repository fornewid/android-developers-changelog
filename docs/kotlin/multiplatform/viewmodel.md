---
title: https://developer.android.com/kotlin/multiplatform/viewmodel
url: https://developer.android.com/kotlin/multiplatform/viewmodel
source: md.txt
---

The AndroidX ViewModel serves as a bridge, establishing a clear contract between
your shared business logic and your UI components. This pattern helps ensure
data consistency across platforms, while enabling UIs to be customized for each
platform's distinct appearance. You can continue developing your UI with Jetpack
Compose on Android and SwiftUI on iOS.

Read more about benefits of using ViewModel and all the features in the [primary
documentation for ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel).

> [!NOTE]
> **Note:** You can see the implementation in practice [in our official sample](https://github.com/android/kotlin-multiplatform-samples/tree/main/Fruitties).

## Set up dependencies

> [!NOTE]
> **Note:** ViewModel supports KMP in versions 2.8.0 and higher.

To set up the KMP ViewModel in your project, define the dependency in the
`libs.versions.toml` file:

    [versions]
    androidx-viewmodel = 2.10.0

    [libraries]
    androidx-lifecycle-viewmodel = { module = "androidx.lifecycle:lifecycle-viewmodel", version.ref = "androidx-viewmodel" }

And then add the artifact to the `build.gradle.kts` file for your KMP module
and declare the dependency as `api`, because this dependency will be exported to
the binary framework:

    // You need the "api" dependency declaration here if you want better access to the classes from Swift code.
    commonMain.dependencies {
      api(libs.androidx.lifecycle.viewmodel)
    }

> [!NOTE]
> **Note:** JetBrains also provides a dependency for a [Common ViewModel](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-viewmodel.html#using-viewmodel-in-common-code). This dependency is only required if you want to retrieve a ViewModel in [Compose Multiplatform](https://www.jetbrains.com/compose-multiplatform/).

### Export ViewModel APIs for access from Swift

By default, any library that you add to your codebase won't be automatically
exported to the binary framework. If the APIs aren't exported, they are
available from the binary framework only if you use them in the shared code
(from the `iosMain` or `commonMain` source set). In that case, the APIs would
contain the package prefix, for example a `ViewModel` class would be available
as `Lifecycle_viewmodelViewModel` class. Check the [exporting dependencies to
binaries](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-build-native-binaries.html#export-dependencies-to-binaries) for more information about exporting
dependencies.

To improve the experience, you can export the ViewModel dependency to the binary
framework using the `export` setup in the `build.gradle.kts` file where you
define the iOS binary framework, which makes the ViewModel APIs accessible
directly from the Swift code the same as from Kotlin code:

    listOf(
      iosX64(),
      iosArm64(),
      iosSimulatorArm64(),
    ).forEach {
      it.binaries.framework {
        // Add this line to all the targets you want to export this dependency
        export(libs.androidx.lifecycle.viewmodel)
        baseName = "shared"
      }
    }

### (Optional) Using `viewModelScope` on JVM Desktop

When running coroutines in a ViewModel, the `viewModelScope` property is tied to
the `Dispatchers.Main.immediate`, which might be unavailable on desktop by
default. To make it work correctly, add the `kotlinx-coroutines-swing`
dependency to your project:

    // Optional if you use JVM Desktop
    desktopMain.dependencies {
        implementation("org.jetbrains.kotlinx:kotlinx-coroutines-swing:[KotlinX Coroutines version]")
    }

See the [`Dispatchers.Main` documentation](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-dispatchers/-main.html)
for more details.

## Use ViewModel from `commonMain` or `androidMain`

There is no specific requirement for using the ViewModel class in the shared
`commonMain`, nor from the `androidMain` sourceSet. The only consideration is
you can't use any platform-specific APIs and you need to abstract them. For
example, if you are using an Android `Application` as a ViewModel constructor
parameter, you need to migrate away from this API by abstracting it.

More information about how to use platform-specific code is available at
[platform-specific code in Kotlin
Multiplatform](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-connect-to-apis.html).

For example, in the following snippet is a ViewModel class with its factory,
defined in `commonMain`:


```kotlin
// commonMain/MainViewModel.kt

class MainViewModel(
    private val repository: DataRepository,
) : ViewModel() { /* some logic */ }

// ViewModelFactory that retrieves the data repository for your app.
val mainViewModelFactory = viewModelFactory {
    initializer {
        MainViewModel(repository = getDataRepository())
    }
}

fun getDataRepository(): DataRepository = DataRepository()
```

<br />

Then, in your UI code, you can retrieve the ViewModel as usual:


```kotlin
// androidApp/ui/MainScreen.kt

@Composable
fun MainScreen(
    viewModel: MainViewModel = viewModel(
        factory = mainViewModelFactory,
    ),
) {
// observe the viewModel state
}
```

<br />

## Use ViewModel from SwiftUI

On Android, the ViewModel lifecycle is automatically handled and scoped to a
`ComponentActivity`, `Fragment`, `NavBackStackEntry` (Navigation 2), or
`rememberViewModelStoreNavEntryDecorator` (Navigation 3). SwiftUI on iOS,
however, has no built-in equivalent for the AndroidX ViewModel.

To share the ViewModel with your SwiftUI app, you need to add some setup code.

### Create a function to help with generics

Instantiating a generic ViewModel instance uses a [class reference reflection
feature](https://kotlinlang.org/docs/reflection.html) on Android. Because [Objective-C
generics don't support all features](https://kotlinlang.org/docs/native-objc-interop.html#generics) of either
Kotlin or Swift, you can't directly retrieve a ViewModel of a generic type from
Swift.

To help with this issue, you can create a helper function that will use
`ObjCClass` instead of the generics type and then use `getOriginalKotlinClass`
to retrieve the ViewModel class to instantiate:


```kotlin
// iosMain/ViewModelResolver.ios.kt

/**
 *   This function allows retrieving any ViewModel from Swift Code with generics. We only get
 *   [ObjCClass] type for the [modelClass], because the interop between Kotlin and Swift code
 *   doesn't preserve the generic class, but we can retrieve the original KClass in Kotlin.
 */
@BetaInteropApi
@Throws(IllegalArgumentException::class)
fun ViewModelStore.resolveViewModel(
    modelClass: ObjCClass,
    factory: ViewModelProvider.Factory,
    key: String?,
    extras: CreationExtras? = null,
): ViewModel {
    @Suppress("UNCHECKED_CAST")
    val vmClass = getOriginalKotlinClass(modelClass) as? KClass<ViewModel>
    require(vmClass != null) { "The modelClass parameter must be a ViewModel type." }

    val provider = ViewModelProvider.Companion.create(this, factory, extras ?: CreationExtras.Empty)
    return key?.let { provider[key, vmClass] } ?: provider[vmClass]
}
```

<br />

Then, when you want to call the function from Swift, you can write a generic
function of type `T : ViewModel` and use `T.self`, which can pass the
`ObjCClass` into the `resolveViewModel` function.

### Connect ViewModel scope to SwiftUI Lifecycle

Next step is to create a `IosViewModelStoreOwner` that implements the
`ObservableObject` and `ViewModelStoreOwner` interfaces (protocols). The reason
for the `ObservableObject` is to be able to use this class as a `@StateObject`
in the SwiftUI code:


```kotlin
// iosApp/IosViewModelStoreOwner.swift

class IosViewModelStoreOwner: ObservableObject, ViewModelStoreOwner {

    let viewModelStore = ViewModelStore()

    /// This function allows retrieving the androidx ViewModel from the store.
    /// It uses the utilify function to pass the generic type T to shared code
    func viewModel<T: ViewModel>(
        key: String? = nil,
        factory: ViewModelProviderFactory,
        extras: CreationExtras? = nil
    ) -> T {
        do {
            return try viewModelStore.resolveViewModel(
                modelClass: T.self,
                factory: factory,
                key: key,
                extras: extras
            ) as! T
        } catch {
            fatalError("Failed to create ViewModel of type \(T.self)")
        }
    }

    /// This is called when this class is used as a `@StateObject`
    deinit {
        viewModelStore.clear()
    }
}
```

<br />

This owner allows retrieving multiple ViewModel types, similarly as on Android.
The lifecycle of those ViewModels is cleared when the screen using the
`IosViewModelStoreOwner` gets deinitialized and calls `deinit`. You can learn
more about deinitialization at the
[official documentation](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/deinitialization/).

At this point, you can just instantiate the `IosViewModelStoreOwner` as a
`@StateObject` in a SwiftUI View and call the `viewModel` function to retrieve a
ViewModel:


```kotlin
// iosApp/ContentView.swift

struct ContentView: View {

    /// Use the store owner as a StateObject to allow retrieving ViewModels and scoping it to this screen.
    @StateObject private var viewModelStoreOwner = IosViewModelStoreOwner()

    var body: some View {
        /// Retrieves the `MainViewModel` instance using the `viewModelStoreOwner`.
        /// The `MainViewModel.Factory` and `creationExtras` are provided to enable dependency injection
        /// and proper initialization of the ViewModel with its required `AppContainer`.
        let mainViewModel: MainViewModel = viewModelStoreOwner.viewModel(
            factory: MainViewModelKt.mainViewModelFactory
        )
        // ...
        // .. the rest of the SwiftUI code
    }
}
```

<br />

## Not Available in Kotlin Multiplatform

Some of the APIs that are available on Android are not available in Kotlin
Multiplatform.

### Integration with Hilt

Because [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) is not available for Kotlin Multiplatform projects,
you can't directly use ViewModels with `@HiltViewModel` annotation in
`commonMain` sourceSet. In that case you need to use some alternative DI
framework, for example, [Koin](https://insert-koin.io/),
[kotlin-inject](https://github.com/evant/kotlin-inject), [Metro](https://zacsweers.github.io/metro/), or
[Kodein](https://kosi-libs.org/kodein). You can find all the DI frameworks that work with
Kotlin Multiplatform at [klibs.io](https://klibs.io/?query=dependency+injection).

### Observe Flows in SwiftUI

Observing coroutines Flows in SwiftUI is not directly supported. However, you
can either use [KMP-NativeCoroutines](https://github.com/rickclephas/KMP-NativeCoroutines)
or [SKIE](https://skie.touchlab.co/) library to allow this feature.