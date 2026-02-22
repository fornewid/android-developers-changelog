---
title: https://developer.android.com/topic/libraries/architecture/datastore
url: https://developer.android.com/topic/libraries/architecture/datastore
source: md.txt
---

# DataStore
Part of [Android Jetpack](https://developer.android.com/jetpack).


Try with Kotlin Multiplatform  
Kotlin Multiplatform allows sharing the data layer with other platforms. Learn how to set up and work with DataStore in KMP  
[Set up DataStore for KMP →](https://developer.android.com/kotlin/multiplatform/datastore)  
![](https://developer.android.com/static/images/android-kmp-logo.png)

<br />

Jetpack DataStore is a data storage solution that lets you store key-value
pairs or typed objects with [protocol buffers](https://developers.google.com/protocol-buffers). DataStore uses Kotlin
coroutines and Flow to store data asynchronously, consistently, and
transactionally.

If you're using [`SharedPreferences`](https://developer.android.com/reference/kotlin/android/content/SharedPreferences) to store data, consider migrating to
DataStore instead.
| **Note:** If you need to support large or complex datasets, partial updates, or referential integrity, consider using [Room](https://developer.android.com/training/data-storage/room) instead of DataStore. DataStore is ideal for small datasets and does not support partial updates or referential integrity.

## DataStore API

The [`DataStore`](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStore) interface provides the following API:

1. A flow that can be used to read data from the DataStore

       val data: Flow<T>

2. A function to update data in the DataStore

       suspend updateData(transform: suspend (t) -> T)

## DataStore Configurations

If you want to store and access data using keys, use the Preferences
DataStore implementation which does not require a predefined schema, and it does
not provide type safety. It has a [`SharedPreferences`](https://developer.android.com/reference/kotlin/android/content/SharedPreferences)-like API but doesn't
have the drawbacks associated with shared preferences.

DataStore lets you persist custom classes. To do this, you must define a
schema for the data and provide a `Serializer` to convert it into a persistable
format. You can choose to use Protocol Buffers, JSON or any other serialization
strategy.

## Setup

To use Jetpack DataStore in your app, add the following to your Gradle file
depending on which implementation you want to use:

### Preferences DataStore

Add the following lines to the dependencies part of your gradle file:  

### Groovy

```groovy
    dependencies {
        // Preferences DataStore (SharedPreferences like APIs)
        implementation "androidx.datastore:datastore-preferences:1.2.0"

        // Alternatively - without an Android dependency.
        implementation "androidx.datastore:datastore-preferences-core:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // Preferences DataStore (SharedPreferences like APIs)
        implementation("androidx.datastore:datastore-preferences:1.2.0")

        // Alternatively - without an Android dependency.
        implementation("androidx.datastore:datastore-preferences-core:1.2.0")
    }
    
```

To add optional RxJava support, add the following dependencies:  

### Groovy

```groovy
    dependencies {
        // optional - RxJava2 support
        implementation "androidx.datastore:datastore-preferences-rxjava2:1.2.0"

        // optional - RxJava3 support
        implementation "androidx.datastore:datastore-preferences-rxjava3:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // optional - RxJava2 support
        implementation("androidx.datastore:datastore-preferences-rxjava2:1.2.0")

        // optional - RxJava3 support
        implementation("androidx.datastore:datastore-preferences-rxjava3:1.2.0")
    }
    
```

### DataStore

Add the following lines to the dependencies part of your gradle file:  

### Groovy

```groovy
    dependencies {
        // Typed DataStore for custom data objects (for example, using Proto or JSON).
        implementation "androidx.datastore:datastore:1.2.0"

        // Alternatively - without an Android dependency.
        implementation "androidx.datastore:datastore-core:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // Typed DataStore for custom data objects (for example, using Proto or JSON).
        implementation("androidx.datastore:datastore:1.2.0")

        // Alternatively - without an Android dependency.
        implementation("androidx.datastore:datastore-core:1.2.0")
    }
    
```

Add the following optional dependencies for RxJava support:  

### Groovy

```groovy
    dependencies {
        // optional - RxJava2 support
        implementation "androidx.datastore:datastore-rxjava2:1.2.0"

        // optional - RxJava3 support
        implementation "androidx.datastore:datastore-rxjava3:1.2.0"
    }
    
```

### Kotlin

```kotlin
    dependencies {
        // optional - RxJava2 support
        implementation("androidx.datastore:datastore-rxjava2:1.2.0")

        // optional - RxJava3 support
        implementation("androidx.datastore:datastore-rxjava3:1.2.0")
    }
    
```

To serialize content, add dependencies for either Protocol Buffers or JSON serialization.

#### JSON serialization

To use JSON serialization, add the following to your Gradle file:  

### Groovy

```groovy
    plugins {
        id("org.jetbrains.kotlin.plugin.serialization") version "2.2.20"
    }

    dependencies {
        implementation "org.jetbrains.kotlinx:kotlinx-serialization-json:1.9.0"
    }
    
```

### Kotlin

```kotlin
    plugins {
        id("org.jetbrains.kotlin.plugin.serialization") version "2.2.20"
    }

    dependencies {
        implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.9.0")
    }
    
```

#### Protobuf serialization

To use Protobuf serialization, add the following to your Gradle file:  

### Groovy

```groovy
    plugins {
        id("com.google.protobuf") version "0.9.5"
    }
    dependencies {
        implementation "com.google.protobuf:protobuf-kotlin-lite:4.32.1"

    }

    protobuf {
        protoc {
            artifact = "com.google.protobuf:protoc:4.32.1"
        }
        generateProtoTasks {
            all().forEach { task ->
                task.builtins {
                    create("java") {
                        option("lite")
                    }
                    create("kotlin")
                }
            }
        }
    }
    
```

### Kotlin

```kotlin
    plugins {
        id("com.google.protobuf") version "0.9.5"
    }
    dependencies {
        implementation("com.google.protobuf:protobuf-kotlin-lite:4.32.1")
    }

    protobuf {
        protoc {
            artifact = "com.google.protobuf:protoc:4.32.1"
        }
        generateProtoTasks {
            all().forEach { task ->
                task.builtins {
                    create("java") {
                        option("lite")
                    }
                    create("kotlin")
                }
            }
        }
    }
    
```

## Use DataStore correctly

In order to use DataStore correctly always keep in mind the following rules:

1. **Never create more than one instance of `DataStore` for a given file in
   the same process.** Doing so can break all DataStore functionality. If there are
   multiple DataStores active for a given file in the same process, DataStore will
   throw `IllegalStateException` when reading or updating data.

2. **The generic type of the `DataStore<T>` must be immutable.** Mutating a type
   used in DataStore invalidates the consistency that DataStore provides and
   creates potentially serious, hard-to-catch bugs. We recommend that you use
   protocol buffers, which help ensure immutability, a clear API, and efficient
   serialization.

3. **Do not mix usages of `SingleProcessDataStore` and `MultiProcessDataStore`**
   for the same file. If you intend to access the `DataStore` from more than one
   process, you must use [`MultiProcessDataStore`](https://developer.android.com/topic/libraries/architecture/datastore#multiprocess).

## Data Definition

### Preferences DataStore

Define a key that will be used to persist data to disk.  

    val EXAMPLE_COUNTER = intPreferencesKey("example_counter")

### JSON DataStore

For JSON datastore, add a `@Serialization` annotation to the data that you
want to persist  

    @Serializable
    data class Settings(
        val exampleCounter: Int
    )

Define a class that implements `Serializer<T>`, where T is the type of the
class you added the earlier annotation to. Make sure you include a default
value for the serializer to be used if there is no file created yet.  

    object SettingsSerializer : Serializer<Settings> {

        override val defaultValue: Settings = Settings(exampleCounter = 0)

        override suspend fun readFrom(input: InputStream): Settings =
            try {
                Json.decodeFromString<Settings>(
                    input.readBytes().decodeToString()
                )
            } catch (serialization: SerializationException) {
                throw CorruptionException("Unable to read Settings", serialization)
            }

        override suspend fun writeTo(t: Settings, output: OutputStream) {
            output.write(
                Json.encodeToString(t)
                    .encodeToByteArray()
            )
        }
    }

### Proto DataStore

The Proto DataStore implementation uses DataStore and [protocol buffers](https://developers.google.com/protocol-buffers) to
persist typed objects to disk.

Proto DataStore requires a predefined schema in a proto file in the
`app/src/main/proto/` directory. This schema defines the type for the objects
that you persist in your Proto DataStore. To learn more about defining a proto
schema, see the [protobuf language guide](https://developers.google.com/protocol-buffers/docs/proto3).

Add a file called settings.proto inside `src/main/proto` folder:  

    syntax = "proto3";

    option java_package = "com.example.datastore.snippets.proto";
    option java_multiple_files = true;

    message Settings {
      int32 example_counter = 1;
    }

Define a class that implements `Serializer<T>`, where `T` is the type defined
in the proto file. This serializer class defines how DataStore reads and
writes your data type. Make sure you include a default value for the
serializer to be used if there is no file created yet.  

    object SettingsSerializer : Serializer<Settings> {
        override val defaultValue: Settings = Settings.getDefaultInstance()

        override suspend fun readFrom(input: InputStream): Settings {
            try {
                return Settings.parseFrom(input)
            } catch (exception: InvalidProtocolBufferException) {
                throw CorruptionException("Cannot read proto.", exception)
            }
        }

        override suspend fun writeTo(t: Settings, output: OutputStream) {
            return t.writeTo(output)
        }
    }

| **Note:** The class for your stored objects is generated at compile time from the message defined in the proto file. Make sure you rebuild your project.

## Create a DataStore

You need to specify a name for the file that is used to persist the data.  

### Preferences DataStore

The Preferences DataStore implementation uses the [`DataStore`](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStore) and
[`Preferences`](https://developer.android.com/reference/kotlin/androidx/datastore/preferences/core/Preferences) classes to persist key-value pairs to disk. Use the
property delegate created by [preferencesDataStore](https://developer.android.com/reference/kotlin/androidx/datastore/preferences/package-summary#dataStore) to create an instance
of `DataStore<Preferences>`. Call it once at the top level of your Kotlin
file. Access DataStore through this property throughout the rest of your
application. This makes it easier to keep your DataStore as a singleton.
Alternatively, use [RxPreferenceDataStoreBuilder](https://developer.android.com/reference/kotlin/androidx/datastore/rxjava2/RxDataStoreBuilder) if you're using RxJava.
The mandatory `name` parameter is the name of the Preferences DataStore.  

    // At the top level of your kotlin file:
    val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "settings")

### JSON DataStore

Use the property delegate created by `dataStore` to create an instance of
`DataStore<T>`, where T is the serializable data class. Call it once
at the top level of your kotlin file and access it through this property
delegate throughout the rest of your app. The `fileName` parameter tells
DataStore which file to use to store the data, and the `serializer` parameter
tells DataStore the name of the serializer class defined in step 1.  

    val Context.dataStore: DataStore<Settings> by dataStore(
        fileName = "settings.json",
        serializer = SettingsSerializer,
    )

### Proto DataStore

Use the property delegate created by `dataStore` to create an instance of
`DataStore<T>`, where `T` is the type defined in the proto file. Call it
once at the top level of your Kotlin file and access it through this property
delegate throughout the rest of your app. The `fileName` parameter tells
DataStore which file to use to store the data, and the `serializer` parameter
tells DataStore the name of the serializer class defined in step 1.  

    val Context.dataStore: DataStore<Settings> by dataStore(
        fileName = "settings.pb",
        serializer = SettingsSerializer,
    )

## Read from DataStore

You need to specify a name for the file that is used to persist the data.  

### Preferences DataStore

Because Preferences DataStore doesn't use a predefined schema, you must use
the corresponding key type function to define a key for each value that you
need to store in the `DataStore<Preferences>` instance. For example, to define
a key for an int value, use [`intPreferencesKey()`](https://developer.android.com/reference/kotlin/androidx/datastore/preferences/core/package-summary#intPreferencesKey(kotlin.String)). Then, use the
[DataStore.data](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStore#data) property to expose the appropriate stored value using a
Flow.  

    fun counterFlow(): Flow<Int> = context.dataStore.data.map { preferences ->
        preferences[EXAMPLE_COUNTER] ?: 0
    }

### JSON DataStore

Use `DataStore.data` to expose a `Flow` of the appropriate property from your
stored object.  

    fun counterFlow(): Flow<Int> = context.dataStore.data.map { settings ->
        settings.exampleCounter
    }

### Proto DataStore

Use `DataStore.data` to expose a `Flow` of the appropriate property from your
stored object.  

    fun counterFlow(): Flow<Int> = context.dataStore.data.map { settings ->
        settings.exampleCounter
    }

## Write to DataStore

DataStore provides an [updateData()](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStore#updatedata) function that transactionally updates a
stored object. `updateData` gives you the current state of the data as an
instance of your data type and updates the data transactionally in an atomic
read-write-modify operation. All of the code in the `updateData` block is
treated as a single transaction.  

### Preferences DataStore

    suspend fun incrementCounter() {
        context.dataStore.updateData {
            it.toMutablePreferences().also { preferences ->
                preferences[EXAMPLE_COUNTER] = (preferences[EXAMPLE_COUNTER] ?: 0) + 1
            }
        }
    }

| **Note:** You can also use the `[edit][11]` suspend function. This function provides a `MutablePreferences` object that you can modify.

### JSON DataStore

    suspend fun incrementCounter() {
        context.dataStore.updateData { settings ->
            settings.copy(exampleCounter = settings.exampleCounter + 1)
        }
    }

### Proto DataStore

    suspend fun incrementCounter() {
        context.dataStore.updateData { settings ->
            settings.copy { exampleCounter = exampleCounter + 1 }
        }
    }

## Compose Sample

You can put these functions together in a class and use it in a Compose app.  

### Preferences DataStore

We can now put these functions into a class called `PreferencesDataStore` and
use it in a Compose App.  

    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val preferencesDataStore = remember(context) { PreferencesDataStore(context) }

    // Display counter value.
    val exampleCounter by preferencesDataStore.counterFlow()
        .collectAsState(initial = 0, coroutineScope.coroutineContext)
    Text(
        text = "Counter $exampleCounter",
        fontSize = 25.sp
    )

    // Update the counter.
    Button(
        onClick = {
            coroutineScope.launch { preferencesDataStore.incrementCounter() }
        }
    ) {
        Text("increment")
    }

### JSON DataStore

We can now put these functions into a class called `JSONDataStore` and use it
in a Compose App.  

    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val jsonDataStore = remember(context) { JsonDataStore(context) }

    // Display counter value.
    val exampleCounter by jsonDataStore.counterFlow()
        .collectAsState(initial = 0, coroutineScope.coroutineContext)
    Text(
        text = "Counter $exampleCounter",
        fontSize = 25.sp
    )

    // Update the counter.
    Button(onClick = { coroutineScope.launch { jsonDataStore.incrementCounter() } }) {
        Text("increment")
    }

### Proto DataStore

We can now put these functions into a class called `ProtoDataStore` and use it
in a Compose App.  

    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val protoDataStore = remember(context) { ProtoDataStore(context) }

    // Display counter value.
    val exampleCounter by protoDataStore.counterFlow()
        .collectAsState(initial = 0, coroutineScope.coroutineContext)
    Text(
        text = "Counter $exampleCounter",
        fontSize = 25.sp
    )

    // Update the counter.
    Button(onClick = { coroutineScope.launch { protoDataStore.incrementCounter() } }) {
        Text("increment")
    }

## Use DataStore in synchronous code

| **Caution:** Avoid blocking threads on DataStore data reads whenever possible. Blocking the UI thread can cause [ANRs](https://developer.android.com/topic/performance/vitals/anr) or unresponsive UI, and blocking other threads can result in [deadlock](https://en.wikipedia.org/wiki/Deadlock).

One of the primary benefits of DataStore is the asynchronous API, but it may not
always be feasible to change your surrounding code to be asynchronous. This
might be the case if you're working with an existing codebase that uses
synchronous disk I/O or if you have a dependency that doesn't provide an
asynchronous API.

Kotlin coroutines provide the [`runBlocking()`](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) coroutine builder to help
bridge the gap between synchronous and asynchronous code. You can use
`runBlocking()` to read data from DataStore synchronously. RxJava offers
blocking methods on `Flowable`. The following code blocks the calling thread
until DataStore returns data:  

### Kotlin

    val exampleData = runBlocking { context.dataStore.data.first() }

### Java

    Settings settings = dataStore.data().blockingFirst();

Performing synchronous I/O operations on the UI thread can cause ANRs or
unresponsive UI. You can mitigate these issues by asynchronously preloading the
data from DataStore:  

### Kotlin

    override fun onCreate(savedInstanceState: Bundle?) {
        lifecycleScope.launch {
            context.dataStore.data.first()
            // You should also handle IOExceptions here.
        }
    }

### Java

    dataStore.data().first().subscribe();

This way, DataStore asynchronously reads the data and caches it in memory. Later
synchronous reads using `runBlocking()` may be faster or may avoid a disk I/O
operation altogether if the initial read has completed.

## Use DataStore in multi-process code

| **Note:** DataStore multi-process has been available since the 1.1.0 release

You can configure DataStore to access the same data across different processes
with the same data consistency properties as from within a single process. In
particular, DataStore provides:

- Reads only return the data that has been persisted to disk.
- Read-after-write consistency.
- Writes are serialized.
- Reads are never blocked by writes.

Consider a sample application with a service and an activity where the service
is running in a separate process and periodically updates the DataStore.

This example uses a JSON datastore, but you can also use a preferences or proto
datastore.  

    @Serializable
    data class Time(
        val lastUpdateMillis: Long
    )

A serializer tells `DataStore` how to read and write your data type. Make sure
you include a default value for the serializer to be used if there is no file
created yet. The following is an example implementation using
[kotlinx.serialization](https://github.com/Kotlin/kotlinx.serialization):  

    object TimeSerializer : Serializer<Time> {

        override val defaultValue: Time = Time(lastUpdateMillis = 0L)

        override suspend fun readFrom(input: InputStream): Time =
            try {
                Json.decodeFromString<Time>(
                    input.readBytes().decodeToString()
                )
            } catch (serialization: SerializationException) {
                throw CorruptionException("Unable to read Time", serialization)
            }

        override suspend fun writeTo(t: Time, output: OutputStream) {
            output.write(
                Json.encodeToString(t)
                    .encodeToByteArray()
            )
        }
    }

To be able to use `DataStore` across different processes, you need to construct
the DataStore object using the `MultiProcessDataStoreFactory` for both the app
and the service code:  

    val dataStore = MultiProcessDataStoreFactory.create(
        serializer = TimeSerializer,
        produceFile = {
            File("${context.cacheDir.path}/time.pb")
        },
        corruptionHandler = null
    )

Add the following to your `AndroidManifiest.xml`:  

    <service
        android:name=".TimestampUpdateService"
        android:process=":my_process_id" />

| **Important:** To run the service in a different process, use the android:process attribute. Note that the process ID is prefixed with a colon (':'). This makes the service run in a new process, private to the application.

The service periodically calls `updateLastUpdateTime()`, which writes to the
datastore using `updateData`.  

    suspend fun updateLastUpdateTime() {
        dataStore.updateData { time ->
            time.copy(lastUpdateMillis = System.currentTimeMillis())
        }
    }

The app reads the value written by the service using the data flow:  

    fun timeFlow(): Flow<Long> = dataStore.data.map { time ->
        time.lastUpdateMillis
    }

Now, we can put all these functions together in a class called
`MultiProcessDataStore` and use it in an App.

Here is the service code:  

    class TimestampUpdateService : Service() {
        val serviceScope = CoroutineScope(SupervisorJob() + Dispatchers.IO)
        val multiProcessDataStore by lazy { MultiProcessDataStore(applicationContext) }


        override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
            serviceScope.launch {
                while (true) {
                    multiProcessDataStore.updateLastUpdateTime()
                    delay(1000)
                }
            }
            return START_NOT_STICKY
        }

        override fun onDestroy() {
            super.onDestroy()
            serviceScope.cancel()
        }
    }

And the app code:  

    val context = LocalContext.current
    val coroutineScope = rememberCoroutineScope()
    val multiProcessDataStore = remember(context) { MultiProcessDataStore(context) }

    // Display time written by other process.
    val lastUpdateTime by multiProcessDataStore.timeFlow()
        .collectAsState(initial = 0, coroutineScope.coroutineContext)
    Text(
        text = "Last updated: $lastUpdateTime",
        fontSize = 25.sp
    )

    DisposableEffect(context) {
        val serviceIntent = Intent(context, TimestampUpdateService::class.java)
        context.startService(serviceIntent)
        onDispose {
            context.stopService(serviceIntent)
        }
    }

You can use [Hilt](https://developer.android.com/training/dependency-injection/hilt-android) dependency injection so that your DataStore
instance is unique per process:  

    @Provides
    @Singleton
    fun provideDataStore(@ApplicationContext context: Context): DataStore<Settings> =
       MultiProcessDataStoreFactory.create(...)

## Handle file corruption

There are rare occasions where DataStore's persistent on-disk file could get
corrupted. By default, DataStore doesn't automatically recover from corruption,
and attempts to read from it will cause the system to throw a
`CorruptionException`.

DataStore offers a corruption handler API that can help you recover gracefully
in such a scenario, and avoid throwing the exception. When configured, the
corruption handler replaces the corrupted file with a new one containing a
predefined default value.

To set up this handler, provide a `corruptionHandler` when creating the
DataStore instance in `by dataStore()` or in the `DataStoreFactory` factory
method:  

    val dataStore: DataStore<Settings> = DataStoreFactory.create(
       serializer = SettingsSerializer(),
       produceFile = {
           File("${context.cacheDir.path}/myapp.preferences_pb")
       },
       corruptionHandler = ReplaceFileCorruptionHandler { Settings(lastUpdate = 0) }
    )

## Provide feedback

Share your feedback and ideas with us through these resources:

[Issue tracker](https://issuetracker.google.com/issues/new?component=907884&template=1466542):
:   Report issues so we can fix bugs.

## Additional resources

To learn more about Jetpack DataStore, see the following additional resources:

### Samples

### Blogs

- [Prefer Storing Data with Jetpack DataStore](https://android-developers.googleblog.com/2020/09/prefer-storing-data-with-jetpack.html)

### Codelabs

- [Working with Preferences DataStore](https://codelabs.developers.google.com/codelabs/android-preferences-datastore)
- [Working with Proto DataStore](https://codelabs.developers.google.com/codelabs/android-proto-datastore)

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Load and display paged data](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data)
- [LiveData overview](https://developer.android.com/topic/libraries/architecture/livedata)
- [Layouts and binding expressions](https://developer.android.com/topic/libraries/data-binding/expressions)