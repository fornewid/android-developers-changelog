---
title: https://developer.android.com/kotlin/multiplatform/datastore
url: https://developer.android.com/kotlin/multiplatform/datastore
source: md.txt
---

The DataStore library stores data asynchronously, consistently, and
transactionally, overcoming some of the drawbacks of SharedPreferences. This
page focuses on creating DataStore in Kotlin Multiplatform (KMP) projects. For
more information on DataStore, see the [primary documentation for DataStore](https://developer.android.com/topic/libraries/architecture/datastore)
and [official samples](https://github.com/android/kotlin-multiplatform-samples).

> [!NOTE]
> **Note:** Only [DataStore Preferences](https://developer.android.com/topic/libraries/architecture/datastore#preferences-datastore) is supported in KMP projects.

## Set up dependencies

> [!NOTE]
> **Note:** DataStore supports KMP in versions 1.1.0 and higher.

To set up DataStore in your KMP project, add the dependencies for the artifacts
in the `build.gradle.kts` file for your module:

    commonMain.dependencies {
      // DataStore library
      implementation("androidx.datastore:datastore:1.2.0")
      // The Preferences DataStore library
      implementation("androidx.datastore:datastore-preferences:1.2.0")
    }

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

    // shared/src/commonMain/kotlin/createDataStore.kt

    /**
     *   Gets the singleton DataStore instance, creating it if necessary.
     */
    fun createDataStore(producePath: () -> String): DataStore<Preferences> =
            PreferenceDataStoreFactory.createWithPath(
                produceFile = { producePath().toPath() }
            )

    internal const val dataStoreFileName = "dice.preferences_pb"

### Android

To create the `DataStore` instance on Android, you need a [`Context`](https://developer.android.com/reference/android/content/Context) along
with the path.

    // shared/src/androidMain/kotlin/createDataStore.android.kt

    fun createDataStore(context: Context): DataStore<Preferences> = createDataStore(
        producePath = { context.filesDir.resolve(dataStoreFileName).absolutePath }
    )

### iOS

On iOS, you can retrieve the path from the `NSDocumentDirectory`:

    // shared/src/iosMain/kotlin/createDataStore.ios.kt

    fun createDataStore(): DataStore<Preferences> = createDataStore(
        producePath = {
            val documentDirectory: NSURL? = NSFileManager.defaultManager.URLForDirectory(
                directory = NSDocumentDirectory,
                inDomain = NSUserDomainMask,
                appropriateForURL = null,
                create = false,
                error = null,
            )
            requireNotNull(documentDirectory).path + "/$dataStoreFileName"
        }
    )

### JVM (Desktop)

To create the `DataStore` instance on JVM (Desktop), provide a path using Java
or Kotlin APIs:

    // shared/src/jvmMain/kotlin/createDataStore.desktop.kt

    fun createDataStore(): DataStore<Preferences> = createDataStore(
        producePath = {
          val file = File(System.getProperty("java.io.tmpdir"), dataStoreFileName)
          file.absolutePath
        }
    )

> [!NOTE]
> **Note:** `System.getProperty("java.io.tmpdir")` points to the temporary folder on the system, which might be cleaned upon reboot. On macOS, you can instead use the `~/Library/Application Support/[your-app]` folder.