---
title: https://developer.android.com/kotlin/multiplatform/datastore
url: https://developer.android.com/kotlin/multiplatform/datastore
source: md.txt
---

The DataStore library stores data asynchronously, consistently, and
transactionally, overcoming some of the drawbacks of SharedPreferences. This
page focuses on creating DataStore in Kotlin Multiplatform (KMP) projects. For
more information on DataStore, see the [primary documentation for DataStore](https://developer.android.com/topic/libraries/architecture/datastore.md.txt).

> [!NOTE]
> **Note:** Only [DataStore Preferences](https://developer.android.com/topic/libraries/architecture/datastore.md.txt#preferences-datastore) is supported in KMP projects.

## Set up dependencies

> [!NOTE]
> **Note:** DataStore supports KMP in versions 1.1.0 and higher (`PreferencesFileSerializer` requires 1.2.0 or higher).

To set up DataStore in your KMP project, add the dependencies for the artifacts
in the `build.gradle.kts` file for your module:

```kotlin
commonMain.dependencies {
  // DataStore library
  implementation("androidx.datastore:datastore-core:1.3.0")
  // The Preferences DataStore library
  implementation("androidx.datastore:datastore-preferences-core:1.3.0")
}
```

## Define the DataStore classes

You can define the `DataStore` class with `DataStoreFactory` inside the common
source of your shared KMP module. Placing these classes in common sources allows
them to be shared across all target platforms. You can use [`actual` and
`expect` declarations](https://kotlinlang.org/docs/multiplatform-expect-actual.html) to create platform-specific
implementations.

## Create the DataStore instance

You need to define how to instantiate the DataStore object on each platform.
This is the only part of the API that is required to be in the specific platform
source sets due to the differences in file system APIs.

### Common


```kotlin
// shared/src/commonMain/kotlin/createDataStore.kt

/**
 *   Gets the singleton DataStore instance, creating it if necessary.
 */
fun createDataStore(storage: Storage<Preferences>): DataStore<Preferences> =
    DataStoreFactory.create(storage = storage)

internal const val dataStoreFileName = "dice.preferences_pb"
```

<br />

### Android

To create the `DataStore` instance on Android, you need a [`Context`](https://developer.android.com/reference/android/content/Context.md.txt) along
with the path.


```kotlin
// shared/src/androidMain/kotlin/createDataStore.android.kt

fun createDataStore(context: Context): DataStore<Preferences> = createDataStore(
    storage = FileStorage(
        serializer = PreferencesFileSerializer,
        produceFile = { context.filesDir.resolve(dataStoreFileName) }
    )
)
```

<br />

### iOS

On iOS, you can retrieve the path from the `NSDocumentDirectory`:


```kotlin
// shared/src/iosMain/kotlin/createDataStore.ios.kt

@OptIn(ExperimentalForeignApi::class)
fun createDataStore(): DataStore<Preferences> = createDataStore(
    storage = OkioStorage(
        fileSystem = FileSystem.SYSTEM,
        serializer = PreferencesSerializer,
        producePath = {
            val documentDirectory: NSURL? = NSFileManager.defaultManager.URLForDirectory(
                directory = NSDocumentDirectory,
                inDomain = NSUserDomainMask,
                appropriateForURL = null,
                create = false,
                error = null,
            )
            (requireNotNull(documentDirectory).path + "/$dataStoreFileName").toPath()
        }
    )
)
```

<br />

### Web

To create the `DataStore` instance on Web, you can use `WebLocalStorage` or
`WebSessionStorage`:

```kotlin
// shared/src/jsMain/kotlin/createDataStore.web.kt (also works for wasmJsMain)

fun createDataStore(): DataStore<Preferences> = createDataStore(
    storage = WebLocalStorage(
        serializer = PreferencesSerializer,
        name = dataStoreFileName
    )
)
```

### JVM (Desktop)

To create the `DataStore` instance on JVM (Desktop), provide a path using Java
or Kotlin APIs:

```kotlin
// shared/src/jvmMain/kotlin/createDataStore.desktop.kt

fun createDataStore(): DataStore<Preferences> = createDataStore(
    storage = FileStorage(
        serializer = PreferencesFileSerializer,
        produceFile = { File(System.getProperty("java.io.tmpdir"), dataStoreFileName) }
    )
)
```

> [!NOTE]
> **Note:** `System.getProperty("java.io.tmpdir")` points to the temporary folder on the system, which might be cleaned upon reboot. On macOS, you can instead use the `~/Library/Application Support/[your-app]` folder.