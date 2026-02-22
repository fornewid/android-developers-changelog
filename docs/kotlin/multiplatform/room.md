---
title: https://developer.android.com/kotlin/multiplatform/room
url: https://developer.android.com/kotlin/multiplatform/room
source: md.txt
---

The Room persistence library provides an abstraction layer over SQLite to allow for more robust database access while harnessing the full power of SQLite. This page focuses on using Room in**Kotlin Multiplatform (KMP)** projects. For more information on using Room, see[Save data in a local database using Room](https://developer.android.com/training/data-storage/room)or our[official samples](https://github.com/android/kotlin-multiplatform-samples/).

## Set up dependencies

| **Note:** Room supports KMP from version 2.7.0 or higher.

To setup Room in your KMP project, add the dependencies for the artifacts in the`build.gradle.kts`file for your KMP module.

Define the dependencies in the`libs.versions.toml`file:  

    [versions]
    room = "2.8.4"
    sqlite = "2.6.2"
    ksp = "<kotlinCompatibleKspVersion>"

    [libraries]
    androidx-sqlite-bundled = { module = "androidx.sqlite:sqlite-bundled", version.ref = "sqlite" }
    androidx-room-runtime = { module = "androidx.room:room-runtime", version.ref = "room" }
    androidx-room-compiler = { module = "androidx.room:room-compiler", version.ref = "room" }

    # Optional SQLite Wrapper available in version 2.8.0 and higher
    androidx-room-sqlite-wrapper = { module = "androidx.room:room-sqlite-wrapper", version.ref = "room" }

    [plugins]
    ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
    androidx-room = { id = "androidx.room", version.ref = "room" }

| **Note:** To help with migrating from`SupportSQLiteDatabase`to`SQLiteDriver`, use the new artifact`androidx.room:room-sqlite-wrapper`available in Room 2.8.0 and higher. Read more in the[Use Room SQLite Wrapper](https://developer.android.com/kotlin/multiplatform/room#migrate-room-sqlite-wrapper)section.

Add the Room Gradle Plugin to configure Room schemas and the[KSP plugin](https://kotlinlang.org/docs/ksp-multiplatform.html).  

    plugins {
      alias(libs.plugins.ksp)
      alias(libs.plugins.androidx.room)
    }

Add the Room runtime dependency and the bundled SQLite library:  

    commonMain.dependencies {
      implementation(libs.androidx.room.runtime)
      implementation(libs.androidx.sqlite.bundled)
    }

    // Optional when using Room SQLite Wrapper
    androidMain.dependencies {
      implementation(libs.androidx.room.sqlite.wrapper)
    }

| **Note:** You can use the[platform-specific implementation of SQLite](https://developer.android.com/kotlin/multiplatform/room#selecting-sqlitedriver), but we recommend bundling it with your app to prevent any inconsistencies between the platform implementations of SQLite.

Add the KSP dependencies to the**root** `dependencies`block. Note that you need to add all the targets your app uses. For more information, check[KSP with Kotlin Multiplatform](https://kotlinlang.org/docs/ksp-multiplatform.html).  

    dependencies {
        add("kspAndroid", libs.androidx.room.compiler)
        add("kspIosSimulatorArm64", libs.androidx.room.compiler)
        add("kspIosX64", libs.androidx.room.compiler)
        add("kspIosArm64", libs.androidx.room.compiler)
        // Add any other platform target you use in your project, for example kspDesktop
    }

Define the Room schema directory. For additional information, see[Set schema location using Room Gradle Plugin](https://developer.android.com/training/data-storage/room/migrating-db-versions#set_schema_location_using_room_gradle_plugin).  

    room {
        schemaDirectory("$projectDir/schemas")
    }

| **Warning:** If using Kotlin version 1.9.x, you must add the property`kotlin.native.disableCompilerDaemon = true`to the`gradle.properties`configuration file for Room's KSP processor to function properly. This property is not needed when using Kotlin version 2.0 or higher. For more information, see[KT-65761](https://youtrack.jetbrains.com/issue/KT-65761).

## Define the database classes

You need to create a database class annotated with`@Database`along with DAOs and entities inside the common source set of your shared KMP module. Placing these classes in common sources will allow them to be shared across all target platforms.  

    // shared/src/commonMain/kotlin/Database.kt

    @Database(entities = [TodoEntity::class], version = 1)
    @ConstructedBy(AppDatabaseConstructor::class)
    abstract class AppDatabase : RoomDatabase() {
      abstract fun getDao(): TodoDao
    }

    // The Room compiler generates the `actual` implementations.
    @Suppress("KotlinNoActualForExpect")
    expect object AppDatabaseConstructor : RoomDatabaseConstructor<AppDatabase> {
        override fun initialize(): AppDatabase
    }

When you declare an`expect`object with the interface`RoomDatabaseConstructor`, the Room compiler generates the`actual`implementations. Android Studio might issue the following warning, which you can suppress with`@Suppress("KotlinNoActualForExpect")`:  

    Expected object 'AppDatabaseConstructor' has no actual declaration in module`

Next, either define a new[DAO interface](https://developer.android.com/training/data-storage/room/accessing-data)or move an existing one to`commonMain`:  

    // shared/src/commonMain/kotlin/TodoDao.kt

    @Dao
    interface TodoDao {
      @Insert
      suspend fun insert(item: TodoEntity)

      @Query("SELECT count(*) FROM TodoEntity")
      suspend fun count(): Int

      @Query("SELECT * FROM TodoEntity")
      fun getAllAsFlow(): Flow<List<TodoEntity>>
    }

Define or move your[entities](https://developer.android.com/training/data-storage/room/defining-data)to`commonMain`:  

    // shared/src/commonMain/kotlin/TodoEntity.kt

    @Entity
    data class TodoEntity(
      @PrimaryKey(autoGenerate = true) val id: Long = 0,
      val title: String,
      val content: String
    )

| **Note:** You can optionally use[expect / actual declarations](https://kotlinlang.org/docs/multiplatform-expect-actual.html)to create platform-specific Room implementations. For example, you can add a platform-specific DAO that is defined in common code using`expect`and then specify the`actual`definitions with additional queries in platform-specific source sets.

## Create the platform-specific database builder

You need to define a database builder to instantiate Room on each platform. This is the only part of the API that is required to be in platform-specific source sets due to the differences in file system APIs.

### Android

On Android, database location is usually obtained through the[`Context.getDatabasePath()`](https://developer.android.com/reference/android/content/Context#getDatabasePath(java.lang.String))API. To create the database instance, specify a[`Context`](https://developer.android.com/reference/android/content/Context)along with the database path.  

    // shared/src/androidMain/kotlin/Database.android.kt

    fun getDatabaseBuilder(context: Context): RoomDatabase.Builder<AppDatabase> {
      val appContext = context.applicationContext
      val dbFile = appContext.getDatabasePath("my_room.db")
      return Room.databaseBuilder<AppDatabase>(
        context = appContext,
        name = dbFile.absolutePath
      )
    }

### iOS

To create the database instance on iOS, provide a database path using the[`NSFileManager`](https://developer.apple.com/documentation/foundation/nsfilemanager/1407693-urlfordirectory), usually located in the`NSDocumentDirectory`.  

    // shared/src/iosMain/kotlin/Database.ios.kt

    fun getDatabaseBuilder(): RoomDatabase.Builder<AppDatabase> {
        val dbFilePath = documentDirectory() + "/my_room.db"
        return Room.databaseBuilder<AppDatabase>(
            name = dbFilePath,
        )
    }

    private fun documentDirectory(): String {
      val documentDirectory = NSFileManager.defaultManager.URLForDirectory(
        directory = NSDocumentDirectory,
        inDomain = NSUserDomainMask,
        appropriateForURL = null,
        create = false,
        error = null,
      )
      return requireNotNull(documentDirectory?.path)
    }

### JVM (Desktop)

To create the database instance, provide a database path using Java or Kotlin APIs.  

    // shared/src/jvmMain/kotlin/Database.desktop.kt

    fun getDatabaseBuilder(): RoomDatabase.Builder<AppDatabase> {
        val dbFile = File(System.getProperty("java.io.tmpdir"), "my_room.db")
        return Room.databaseBuilder<AppDatabase>(
            name = dbFile.absolutePath,
        )
    }

| **Note:** `System.getProperty("java.io.tmpdir")`points to the temporary folder on the system, which might be cleaned upon reboot. For example, on macOS, you can instead use the`~/Library/Application Support/[your-app]`folder.

## Instantiate the database

Once you obtain the`RoomDatabase.Builder`from one of the platform-specific constructors, you can configure the rest of the Room database in common code along with the actual database instantiation.  

    // shared/src/commonMain/kotlin/Database.kt

    fun getRoomDatabase(
        builder: RoomDatabase.Builder<AppDatabase>
    ): AppDatabase {
      return builder
          .setDriver(BundledSQLiteDriver())
          .setQueryCoroutineContext(Dispatchers.IO)
          .build()
    }

### Select a SQLite driver

The previous code snippet calls the`setDriver`builder function to define what SQLite driver the Room database should use. These drivers differ based on the target platform. The previous code snippets use the[`BundledSQLiteDriver`](https://developer.android.com/reference/kotlin/androidx/sqlite/driver/bundled/BundledSQLiteDriver). This is the recommended driver that includes SQLite compiled from source, which provides the most consistent and up-to-date version of SQLite across all platforms.

If you want to use the OS-provided SQLite, use the`setDriver`API in the platform-specific source sets that specify a platform-specific driver. See[Driver implementations](https://developer.android.com/kotlin/multiplatform/sqlite#sqlite-driver-implementations)for descriptions of available driver implementations. You can use either of the following:

- [`AndroidSQLiteDriver`](https://developer.android.com/reference/androidx/sqlite/driver/AndroidSQLiteDriver)in`androidMain`
- [`NativeSQLiteDriver`](https://developer.android.com/reference/kotlin/androidx/sqlite/driver/NativeSQLiteDriver)in`iosMain`

To use`NativeSQLiteDriver`, you need to provide a linker option`-lsqlite3`so that the iOS app dynamically links with the system SQLite.  

    // shared/build.gradle.kts

    kotlin {
        listOf(
            iosX64(),
            iosArm64(),
            iosSimulatorArm64()
        ).forEach { iosTarget ->
            iosTarget.binaries.framework {
                baseName = "TodoApp"
                isStatic = true
                // Required when using NativeSQLiteDriver
                linkerOpts.add("-lsqlite3")
            }
        }
    }

### Set a Coroutine context (Optional)

A`RoomDatabase`object on Android can optionally be configured with shared application executors using`RoomDatabase.Builder.setQueryExecutor()`to perform database operations.

Because executors are not KMP compatible, Room's`setQueryExecutor()`API is not available in`commonMain`. Instead the`RoomDatabase`object must be configured with a`CoroutineContext`, which can be set using`RoomDatabase.Builder.setCoroutineContext()`. If no context is set, then the`RoomDatabase`object will default to using`Dispatchers.IO`.

## Minification and obfuscation

If the project is[minified or obfuscated](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-native-distribution.html#minification-and-obfuscation)then you must include the following ProGuard rule so that Room can find the generated implementation of the database definition:  

    -keep class * extends androidx.room.RoomDatabase { <init>(); }

## Migrate to Kotlin Multiplatform

Room was originally developed as an Android library and was later migrated to KMP with a focus on API compatibility. The KMP version of Room differs somewhat between platforms and from the Android-specific version. These differences are listed and described as follows.

### Migrate from Support SQLite to SQLite Driver

Any usages of`SupportSQLiteDatabase`and other APIs in[`androidx.sqlite.db`](https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary)need to be refactored with SQLite Driver APIs, because the APIs in[`androidx.sqlite.db`](https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary)are Android-only (note the different package than the KMP package).
| **Note:** If you're using any low-level SQLite APIs in your codebase, refer to[Migrate SQLite to Kotlin Multiplatform](https://developer.android.com/kotlin/multiplatform/sqlite#migrate).

For backwards compatibility, and as long as the`RoomDatabase`is configured with a`SupportSQLiteOpenHelper.Factory`(for example, no`SQLiteDriver`is set), then Room behaves in 'compatibility mode' where both Support SQLite and SQLite Driver APIs work as expected. This enables incremental migrations so that you don't need to convert all your Support SQLite usages to SQLite Driver in a single change.

### Use Room SQLite Wrapper (Optional)

The`androidx.room:room-sqlite-wrapper`artifact provides APIs to bridge between`SQLiteDriver`and`SupportSQLiteDatabase`during migration.

To get a`SupportSQLiteDatabase`from a`RoomDatabase`configured with a`SQLiteDriver`, use the new extension function`RoomDatabase.getSupportWrapper()`. This compatibility wrapper helps maintain existing usages of`SupportSQLiteDatabase`(often obtained from`RoomDatabase.openHelper.writableDatabase`) while adopting`SQLiteDriver`, especially for codebases with extensive`SupportSQLite`API usages that want to use`BundledSQLiteDriver`.

#### Convert Migrations Subclasses

Migrations subclasses need to be migrated to the SQLite driver counterparts:
**Note:** Converting the`RoomDatabase`Transaction APIs is described in[Convert Transaction APIs](https://developer.android.com/kotlin/multiplatform/room#transactions)section.  

### Kotlin Multiplatform

Migration subclasses  

    object Migration_1_2 : Migration(1, 2) {
      override fun migrate(connection: SQLiteConnection) {
        // ...
      }
    }

Auto migration specification subclasses  

    class AutoMigrationSpec_1_2 : AutoMigrationSpec {
      override fun onPostMigrate(connection: SQLiteConnection) {
        // ...
      }
    }

### Android-only

Migration subclasses  

    object Migration_1_2 : Migration(1, 2) {
      override fun migrate(db: SupportSQLiteDatabase) {
        // ...
      }
    }

Auto migration specification subclasses  

    class AutoMigrationSpec_1_2 : AutoMigrationSpec {
      override fun onPostMigrate(db: SupportSQLiteDatabase) {
        // ...
      }
    }

#### Convert database callback

Database callbacks need to be migrated to the SQLite driver counterparts:  

### Kotlin Multiplatform

    object MyRoomCallback : RoomDatabase.Callback() {
      override fun onCreate(connection: SQLiteConnection) {
        // ...
      }

      override fun onDestructiveMigration(connection: SQLiteConnection) {
        // ...
      }

      override fun onOpen(connection: SQLiteConnection) {
        // ...
      }
    }

### Android-only

    object MyRoomCallback : RoomDatabase.Callback() {
      override fun onCreate(db: SupportSQLiteDatabase) {
        // ...
      }

      override fun onDestructiveMigration(db: SupportSQLiteDatabase) {
        // ...
      }

      override fun onOpen(db: SupportSQLiteDatabase) {
        // ...
      }
    }

### Convert`@RawQuery`DAO functions

Functions annotated with`@RawQuery`that are compiled for non-Android platforms will need to declare a parameter of type`RoomRawQuery`instead of`SupportSQLiteQuery`.  

### Kotlin Multiplatform

Define the raw query  

    @Dao
    interface TodoDao {
      @RawQuery
      suspend fun getTodos(query: RoomRawQuery): List<TodoEntity>
    }

A`RoomRawQuery`can then be used to create a query at runtime:  

    suspend fun AppDatabase.getTodosWithLowercaseTitle(title: String): List<TodoEntity> {
        val query = RoomRawQuery(
            sql = "SELECT * FROM TodoEntity WHERE title = ?",
            onBindStatement = {
                it.bindText(1, title.lowercase())
            }
        )

        return todoDao().getTodos(query)
    }

### Android-only

Define the raw query  

    @Dao
    interface TodoDao {
      @RawQuery
      suspend fun getTodos(query: SupportSQLiteQuery): List<TodoEntity>
    }

A`SimpleSQLiteQuery`can then be used to create a query at runtime:  

    suspend fun AndroidOnlyDao.getTodosWithLowercaseTitle(title: String): List<TodoEntity> {
      val query = SimpleSQLiteQuery(
          query = "SELECT * FROM TodoEntity WHERE title = ?",
          bindArgs = arrayOf(title.lowercase())
      )
      return getTodos(query)
    }

### Convert blocking DAO functions

Room benefits from the feature-rich asynchronous`kotlinx.coroutines`library that Kotlin offers for multiple platforms. For optimal functionality,`suspend`functions are enforced for DAOs compiled in a KMP project, with the exception of DAOs implemented in`androidMain`to maintain backwards compatibility with the existing codebase. When using Room for KMP, all DAO functions compiled for non-Android platforms need to be`suspend`functions.
**Note:** Migrating existing DAO blocking functions to suspend functions can be complicated if the existing codebase does not already incorporate coroutines. Refer to[Coroutines in Android](https://developer.android.com/kotlin/coroutines)to get started on using coroutines and[Flows in Android](https://developer.android.com/kotlin/flow)to get started on using flows in your codebase.  

### Kotlin Multiplatform

Suspending queries  

    @Query("SELECT * FROM Todo")
    suspend fun getAllTodos(): List<Todo>

Suspending transactions  

    @Transaction
    suspend fun transaction() { ... }

### Android-only

Blocking queries  

    @Query("SELECT * FROM Todo")
    fun getAllTodos(): List<Todo>

Blocking transactions  

    @Transaction
    fun blockingTransaction() { ... }

### Convert reactive types to Flow

Not all DAO functions need to be suspend functions. DAO functions that return reactive types such as`LiveData`or RxJava's`Flowable`shouldn't be converted to suspend functions. Some types, however, such as`LiveData`are not KMP compatible. DAO functions with reactive return types must be migrated to coroutine flows.  

### Kotlin Multiplatform

Reactive types`Flows`  

    @Query("SELECT * FROM Todo")
    fun getTodosFlow(): Flow<List<Todo>>

### Android-only

Reactive types like`LiveData`or RxJava's`Flowable`  

    @Query("SELECT * FROM Todo")
    fun getTodosLiveData(): LiveData<List<Todo>>

### Convert transaction APIs

Database transaction APIs for Room KMP can differentiate between writing (`useWriterConnection`) and reading (`useReaderConnection`) transactions.
**Key Point:** The equivalent of the Android-only`withTransaction{ ... }`API is the`useWriterConnection{ it.immediateTransaction{ ... } }`.  

### Kotlin Multiplatform

    val database: RoomDatabase = ...
    database.useWriterConnection { transactor ->
      transactor.immediateTransaction {
        // perform database operations in transaction
      }
    }

### Android-only

    val database: RoomDatabase = ...
    database.withTransaction {
      // perform database operations in transaction
    }

#### Write transactions

Use write transactions to make sure that multiple queries write data atomically, so that readers can consistently access the data. You can do this using`useWriterConnection`with any of the three transaction types:

- `immediateTransaction`: In[Write-Ahead Logging (WAL)](https://www.sqlite.org/wal.html)mode (default), this type of transaction acquires a lock when it starts, but readers can continue to read.**This is the preferred choice for most cases.**

- `deferredTransaction`: The transaction won't acquire a lock until the first write statement. Use this type of transaction as an optimization when you're not sure if a write operation will be needed within the transaction. For example, if you start a transaction to delete songs from a playlist given just a name of the playlist and the playlist doesn't exist, then no write (delete) operation is needed.

- `exclusiveTransaction`: This mode behaves identical to`immediateTransaction`in the WAL mode. In other journaling modes, it prevents other database connections from reading the database while the transaction is underway.

| **Note:** The write transactions always block parallel write transactions. If the journal mode is rollback (non-WAL), then sticking to immediate is still the best choice for parallelism.

#### Read transactions

Use read transactions to consistently read from the database multiple times. For example, when you have two or more separate queries and you don't use a`JOIN`clause. Only deferred transactions are allowed in reader connections. Attempting to start an immediate or exclusive transaction in a reader connection will throw an exception, as these are considered 'write' operations.  

    val database: RoomDatabase = ...
    database.useReaderConnection { transactor ->
      transactor.deferredTransaction {
          // perform database operations in transaction
      }
    }

| **Note:** For more details about SQLite transactions, see the[SQLite documentation](https://www.sqlite.org/lang_transaction.html).

## Not Available in Kotlin Multiplatform

Some of the APIs that were available for Android are not available in Kotlin Multiplatform.

### Query Callback

The following APIs for configuring query callbacks are not available in common and are thus unavailable in platforms other than Android.

- `RoomDatabase.Builder.setQueryCallback`
- `RoomDatabase.QueryCallback`

We intend to add support for query callback in a future version of Room.

The API to configure a`RoomDatabase`with a query callback`RoomDatabase.Builder.setQueryCallback`along with the callback interface`RoomDatabase.QueryCallback`are not available in common and thus not available in other platforms other than Android.

### Auto Closing Database

The API to enable auto-closing after a timeout,`RoomDatabase.Builder.setAutoCloseTimeout`, is only available on Android and is not available in other platforms.

### Pre-package Database

The following APIs to create a`RoomDatabase`using an existing database (i.e. a pre-packaged database) are not available in common and are thus not available in other platforms other than Android. These APIs are:

- `RoomDatabase.Builder.createFromAsset`
- `RoomDatabase.Builder.createFromFile`
- `RoomDatabase.Builder.createFromInputStream`
- `RoomDatabase.PrepackagedDatabaseCallback`

We intend to add support for pre-packaged databases in a future version of Room.

### Multi-Instance Invalidation

The API to enable multi-instance invalidation,`RoomDatabase.Builder.enableMultiInstanceInvalidation`is only available on Android and is not available in common or other platforms.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Migrate existing apps to Room KMP Codelab](https://developer.android.com/codelabs/kmp-migrate-room)
- [Get Started with KMP Codelab](https://developer.android.com/codelabs/kmp-get-started)
- [Save data in local database with Room](https://developer.android.com/training/data-storage/room)