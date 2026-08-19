---
title: https://developer.android.com/training/data-storage/room/migration-2-to-3
url: https://developer.android.com/training/data-storage/room/migration-2-to-3
source: md.txt
---

Room 3.0 is a major version update that transitions the library to be
Kotlin-first. It supports Kotlin Multiplatform (KMP), requires Kotlin Symbol
Processing (KSP), and enforces coroutines for asynchronous operations.

To prevent compatibility issues with existing Room 2.x apps and transitive
dependencies, Room 3.0 resides in a new package: `androidx.room3`.

This guide outlines the steps required to migrate your existing Room 2.x
implementation to Room 3.0.

## Key changes in Room 3.0

Before starting the migration, familiarize yourself with the major differences:

- **New package and artifacts** : All classes reside in `androidx.room3`. Artifacts use the `room3` prefix, such as `androidx.room3:room3-runtime`.
- **Kotlin and KSP only**: Room 3.0 doesn't support Java code generation. Use KSP instead of KAPT or Java annotation processors. Room 3.0 still supports Java sources as inputs.
- **Coroutines first** : DAO functions must be `suspend` functions, except for observable types. `CoroutineContext` replaces executors.
- **No SupportSQLite** : `SQLiteDriver` APIs back Room. Room removes `SupportSQLiteDatabase` from core APIs.
- **API changes** : Migrations and database callbacks use `SQLiteConnection` instead of `SupportSQLiteDatabase`.
- **Converters for reactive types** : RxJava, LiveData, Guava, and Paging return types require that you register `@DaoReturnTypeConverters`.

*** ** * ** ***

We recommend migrating in two distinct phases: first preparing and modernizing
your codebase in Room 2.x, and then switching to Room 3.0.

*** ** * ** ***

## Prepare and modernize in Room 2.x

Before migrating to Room 3.0, you can perform most modernization work by
updating to the current Room 2.x release, like Room 2.8. Room 2.8 supports
Kotlin Multiplatform, or KMP, and includes many driver APIs that Room 3.0
uses.

### Update to Room 2.8 and higher

Update your build configuration to use the current Room 2.x release:

    [versions]
    room2 = "2.8.4" # Use the current Room 2.8 version

    [libraries]
    androidx-room-runtime = { module = "androidx.room:room-runtime", version.ref = "room2" }
    androidx-room-compiler = { module = "androidx.room:room-compiler", version.ref = "room2" }

### Migrate from KAPT to KSP

Room 3.0 doesn't support Java annotation processors or KAPT. You must use
Kotlin Symbol Processing (KSP). You can make this transition while still on
Room 2.x.

1. In your module's `build.gradle.kts`, apply the KSP plugin:

       plugins {
           id("com.google.devtools.ksp") version "<ksp_version>"
       }

   Ensure that the KSP version is compatible with your Kotlin version.
2. Replace `kapt` or `annotationProcessor` with `ksp` for the Room compiler
   dependency:

       dependencies {
           implementation(libs.androidx.room.runtime)
           ksp(libs.androidx.room.compiler)
       }

### Adopt coroutines

Room 3.0 requires coroutines for asynchronous operations.

- Update your DAOs: Unless they return an observable reactive type, like `Flow` or RxJava types, all DAO functions must be `suspend` functions.

    // Before (Blocking)
    @Dao
    interface UserDao {
        @Query("SELECT * FROM User")
        fun getAll(): List<User>
    }

    // After (Suspend)
    @Dao
    interface UserDao {
        @Query("SELECT * FROM User")
        suspend fun getAll(): List<User>
    }

- If you configured your `RoomDatabase` with a custom `Executor` to perform database operations, migrate to `CoroutineContext` using `setQueryCoroutineContext` on the builder:

    Room.databaseBuilder<AppDatabase>(context, "db")
        .setQueryCoroutineContext(Dispatchers.IO)
        .build()

### Adopt driver APIs and avoid Support SQLite

Room 3.0 is fully backed by `SQLiteDriver` and no longer supports
`SupportSQLiteDatabase` in its core APIs.

If you don't call `setDriver` to set a `SQLiteDriver` on your database builder,
Room 2.8 operates in a compatibility mode where both Support SQLite and Driver
APIs function. This compatibility mode lets you incrementally convert your
codebase before enabling the driver.

- **Convert migrations** : Migrate your `Migration` and `AutoMigrationSpec` subclasses to use `SQLiteConnection` instead of `SupportSQLiteDatabase`.

    // Before (SupportSQLiteDatabase)
    val MIGRATION_1_2 = object : Migration(1, 2) {
        override fun migrate(db: SupportSQLiteDatabase) {
            db.execSQL("ALTER TABLE User ADD COLUMN age INTEGER DEFAULT 0 NOT NULL")
        }
    }

    // After (SQLiteConnection - Room 2.8)
    import androidx.sqlite.SQLiteConnection
    import androidx.sqlite.execSQL

    val MIGRATION_1_2 = object : Migration(1, 2) {
        override fun migrate(connection: SQLiteConnection) {
            connection.execSQL(
                "ALTER TABLE User ADD COLUMN age INTEGER DEFAULT 0 NOT NULL"
            )
        }
    }

> [!NOTE]
> **Note:** In Room 3.0, the `migrate` function becomes a `suspend` function. For more information, see [Update callbacks to suspend functions](https://developer.android.com/training/data-storage/room/migration-2-to-3#callbacks-3.0).

- **Convert database callbacks** : Update `RoomDatabase.Callback` implementations to use `SQLiteConnection`:

    // Before (SupportSQLiteDatabase)
    val callback = object : RoomDatabase.Callback() {
        override fun onCreate(db: SupportSQLiteDatabase) {
            // ...
        }
    }

    // After (SQLiteConnection - Room 2.8)
    val callback = object : RoomDatabase.Callback() {
        override fun onCreate(connection: SQLiteConnection) {
            // ...
        }
    }

> [!NOTE]
> **Note:** In Room 3.0, these callback functions become `suspend` functions.

- **Convert `@RawQuery` DAO functions** : For functions annotated with `@RawQuery`, use `RoomRawQuery` instead of `SupportSQLiteQuery`:

    // Before (SupportSQLiteQuery)
    @Dao
    interface UserDao {
        @RawQuery
        fun getUser(query: SupportSQLiteQuery): User
    }

    // After (RoomRawQuery)
    @Dao
    interface UserDao {
        @RawQuery
        suspend fun getUser(query: RoomRawQuery): User
    }

You can construct a `RoomRawQuery` at runtime:

    val query = RoomRawQuery(
        sql = "SELECT * FROM User WHERE id = ?",
        onBindStatement = { statement ->
            statement.bindInt(1, userId)
        }
    )

- **Convert transaction APIs** : Replace Android-only `withTransaction` and `runInTransaction` blocks with `useWriterConnection` and `immediateTransaction`:

    // Before (withTransaction)
    db.withTransaction {
        // perform database operations
    }

    // After (useWriterConnection - Room 2.8)
    import androidx.room.useWriterConnection
    import androidx.room.immediateTransaction

    db.useWriterConnection { connection ->
        connection.immediateTransaction {
            // perform database operations
        }
    }

> [!NOTE]
> **Note:** Once you adopt Room 3.0, you can clean up these calls to use `withWriteTransaction` or `withReadTransaction`.

- **Avoid direct usage of `SupportSQLiteDatabase`** : If you have extensive legacy code that still requires `SupportSQLiteDatabase` and you can't migrate it yet, use the `androidx.room:room-sqlite-wrapper` compatibility artifact:

    dependencies {
        implementation("androidx.room:room-sqlite-wrapper:$roomVersion")
    }

And then, use `getSupportWrapper` to obtain a `SupportSQLiteDatabase` from
your Room database instance:

    import androidx.room.support.getSupportWrapper

    val legacyDb: SupportSQLiteDatabase = roomDatabase.getSupportWrapper()

- **Set the SQLite driver** : After you migrate all Room API usages to driver APIs, configure a driver, like `BundledSQLiteDriver` or `AndroidSQLiteDriver`, by calling `setDriver` in your `RoomDatabase` builder:

    import androidx.sqlite.driver.bundled.BundledSQLiteDriver

    val db = Room.databaseBuilder<AppDatabase>(context, "db")
        .setDriver(BundledSQLiteDriver())
        .build()

> > [!CAUTION]
> > **Caution:** Set the driver as the final step. After you set a driver, Room disables compatibility mode, and any remaining direct calls to `SupportSQLiteDatabase` APIs, like `roomDatabase.openHelper.writableDatabase`, throw an exception.
>
### Adopt flow-based invalidation tracking

Room 2.8 introduces the `InvalidationTracker.createFlow` API. Use this API
to migrate away from legacy `InvalidationTracker.Observer` implementations
while still on Room 2.x. This prepares your codebase for Room 3.0, which
completely removes `Observer`.

    // Before (InvalidationTracker.Observer)
    val observer = object : InvalidationTracker.Observer("User") {
        override fun onInvalidated(tables: Set<String>) {
            // reload user data
        }
    }
    db.invalidationTracker.addObserver(observer)

    // After (createFlow - Room 2.8)
    val userFlow = db.invalidationTracker.createFlow("User").map { _ ->
        userDao.getAllUsers()
    }

*** ** * ** ***

## Migrate to Room 3.0

Once you modernize your application on Room 2.x, transitioning to Room 3.0
involves updating dependencies, package imports, and database callbacks.

### Update dependencies and package imports

- In your build configuration, replace `androidx.room` dependencies with `androidx.room3`:

    [versions]
    room3 = "3.0.0" # Use the current Room 3.0 version

    [libraries]
    androidx-room3-runtime = { module = "androidx.room3:room3-runtime", version.ref = "room3" }
    androidx-room3-compiler = { module = "androidx.room3:room3-compiler", version.ref = "room3" }

- Update your dependencies block:

    dependencies {
        implementation(libs.androidx.room3.runtime)
        ksp(libs.androidx.room3.compiler)
    }

- Update your package imports. Replace `import androidx.room.*` with `import androidx.room3.*`.

### Update type converter APIs

Room 3.0 renames the type converter APIs to clarify their usage for converting
column values and to avoid confusion with the DAO return type converters.

Update the following annotations and functions in your codebase:

- Rename `@TypeConverter` to `@ColumnTypeConverter`.
- Rename `@TypeConverters` to `@ColumnTypeConverters`.
- Rename `@ProvidedTypeConverter` to `@ProvidedColumnTypeConverter`.
- Rename `RoomDatabase.Builder.addTypeConverter` to `addColumnTypeConverter`.

Example:

    // Before
    @ProvidedTypeConverter
    class Converters {
      @TypeConverter
      fun fromTimestamp(value: Long?): Date? = ...
    }

    @Database(entities = [User::class], version = 1)
    @TypeConverters(Converters::class)
    abstract class AppDatabase : RoomDatabase()

    val db = Room.databaseBuilder<AppDatabase>(...)
      .addTypeConverter(convertersInstance)
      .build()

    // After
    import androidx.room3.ColumnTypeConverter
    import androidx.room3.ColumnTypeConverters
    import androidx.room3.ProvidedColumnTypeConverter

    @ProvidedColumnTypeConverter
    class Converters {
      @ColumnTypeConverter
      fun fromTimestamp(value: Long?): Date? = ...
    }

    @Database(entities = [User::class], version = 1)
    @ColumnTypeConverters(Converters::class)
    abstract class AppDatabase : RoomDatabase()

    val db = Room.databaseBuilder<AppDatabase>(...)
      .addColumnTypeConverter(convertersInstance)
      .build()

### Update callbacks to suspend functions

In Room 3.0, database callbacks and migrations use `SQLiteConnection` and are
`suspend` functions.

- Update your manual `Migration` classes:

    import androidx.sqlite.SQLiteConnection
    import androidx.sqlite.async.executeSQL

    val MIGRATION_1_2 = object : Migration(1, 2) {
        override suspend fun migrate(connection: SQLiteConnection) {
            connection.executeSQL(
                "ALTER TABLE User ADD COLUMN age INTEGER DEFAULT 0 NOT NULL"
            )
        }
    }

- Update your `RoomDatabase.Callback` implementations:

    val callback = object : RoomDatabase.Callback() {
        override suspend fun onCreate(connection: SQLiteConnection) {
            // ...
        }
    }

### Register DAO return type converters

In Room 3.0, reactive return types, such as RxJava, LiveData, Guava, and Paging,
require you to register DAO return type converters using
`@DaoReturnTypeConverters`.

    import androidx.room3.paging.PagingSourceDaoReturnTypeConverter

    @Dao
    @DaoReturnTypeConverters(PagingSourceDaoReturnTypeConverter::class)
    interface UserDao {
        @Query("SELECT * FROM User")
        fun getAllPaginated(): PagingSource<Int, User>
    }

- **Paging (`PagingSource`)** : Register `PagingSourceDaoReturnTypeConverter` from the `androidx.room3:room3-paging` artifact.
- **RxJava (`Observable`, `Flowable`, `Single`, `Maybe`, `Completable`)** : Register `RxDaoReturnTypeConverters` from the `androidx.room3:room3-rxjava3` artifact.
- **Guava (`ListenableFuture`)** : Register `GuavaDaoReturnTypeConverter` from the `androidx.room3:room3-guava` artifact.
- **LiveData (`LiveData`)** : Register `LiveDataDaoReturnTypeConverter` from the `androidx.room3:room3-livedata` artifact.

### Verify InvalidationTracker Observer removal

Room 3.0 completely removes `InvalidationTracker.Observer` and related
registration methods, like `addObserver` and `removeObserver`.

If you haven't already transitioned to coroutine flows in
[Phase 1](https://developer.android.com/training/data-storage/room/migration-2-to-3#invalidation-2.8), you must migrate all `Observer` usages to
`createFlow`:

    val userFlow = db.invalidationTracker.createFlow("User").map { _ ->
        userDao.getAllUsers()
    }