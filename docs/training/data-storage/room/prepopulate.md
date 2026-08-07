---
title: https://developer.android.com/training/data-storage/room/prepopulate
url: https://developer.android.com/training/data-storage/room/prepopulate
source: md.txt
---

If you want your app to start with a database that's already loaded with a specific set of data, you can prepopulate the database. In Room, you can use APIs to prepopulate a database at initialization with contents from a prepackaged database file in the device's file system.

> [!NOTE]
> **Note:** [In-memory Room databases](https://developer.android.com/reference/kotlin/androidx/room3/Room#inmemorydatabasebuilder) don't support prepopulating the database using [`createFromAsset`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromasset) or [`createFromFile`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromfile).

## Prepopulate from an app asset

To prepopulate a Room database from a prepackaged database file that's located anywhere in your app's `assets/` directory, call the [`createFromAsset`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromasset) function from your `RoomDatabase.Builder` object before calling [`build`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#build):

<br />

```kotlin
Room.databaseBuilder<AppDatabase>(appContext, "sample.db")
    .createFromAsset("database/myapp.db")
    .build()
   
```

<br />

The `createFromAsset` function accepts a string argument that contains a relative path from the `assets/` directory to the prepackaged database file.

> [!NOTE]
> **Note:** When prepopulating from an asset, Room validates the database to ensure that its schema matches the schema of the prepackaged database. To use your database's schema as a reference when you create the prepackaged database file, [export the schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schemas).

## Prepopulate from the file system

To prepopulate a Room database from a prepackaged database file that's located anywhere in the device's file system *except* your app's `assets/` directory, call the [`createFromFile`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#createfromfile) function from your `RoomDatabase.Builder` object before calling [`build`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#build):

<br />

```kotlin
Room.databaseBuilder<AppDatabase>(appContext, "sample.db")
    .createFromFile(File("mypath"))
    .build()
   
```

<br />

The `createFromFile` function accepts a [`File`](https://developer.android.com/reference/java/io/File) argument for the prepackaged database file. Room creates a copy of the designated file rather than opening it directly, so make sure your app has read permissions on the file.

> [!NOTE]
> **Note:** When prepopulating from the file system, Room validates the database to ensure that its schema matches the schema of the prepackaged database. To use your database's schema as a reference when you create the prepackaged database file, [export the schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schemas).

## Handle migrations that include prepackaged databases

Prepackaged database files can also change the way your Room database handles fallback migrations. Ordinarily, when [destructive migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#handle-missing-migrations) are enabled and Room must perform a migration without a migration path, Room drops all tables in the database and creates an empty database with the specified schema for the target version. However, if you include a prepackaged database file with the same number as the target version, Room populates the newly recreated database with the contents of the prepackaged database file after performing the destructive migration.

For more information about Room database migrations, see [Migrate your Room database](https://developer.android.com/training/data-storage/room/migrating-db-versions).

The following sections present a few examples of how this works in practice.

### Example: Fallback migration with a prepackaged database

Suppose the following:

- Your app defines a Room database on version 3.
- The database instance that's already installed on the device is on version 2.
- There's a prepackaged database file that's on version 3.
- There's no implemented migration path from version 2 to version 3.
- Destructive migrations are enabled.

<br />

```kotlin
// Database class definition declaring version 3.
@Database(entities = [SampleEntity::class], version = 3)
abstract class FallbackAppDatabase : RoomDatabase() {
    // ...
}

fun createFallbackDb(appContext: Context) {
    Room.databaseBuilder<FallbackAppDatabase>(appContext, "sample.db")
        .createFromAsset("database/myapp.db")
        .fallbackToDestructiveMigration()
        .build()
}
   
```

<br />

Here's what happens in this situation:

1. Because the database defined in your app is on version 3 and the database instance already installed on the device is on version 2, a migration is necessary.
2. Because there's no implemented migration plan from version 2 to version 3, the migration is a fallback migration.
3. Because you call the [`fallbackToDestructiveMigration`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#fallbacktodestructivemigration) builder function, the fallback migration is destructive. Room drops the database instance that's installed on the device.
4. Because there's a prepackaged database file that's on version 3, Room recreates the database and populates it using the contents of the prepackaged database file. If your prepackaged database file is on version 2, Room determines that it doesn't match the target version and doesn't use it for the fallback migration.

### Example: Implemented migration with a prepackaged database

Suppose instead that your app implements a migration path from version 2 to version 3:

<br />

```kotlin
// Database class definition declaring version 3.
@Database(entities = [SampleEntity::class], version = 3)
abstract class ImplementedAppDatabase : RoomDatabase() {
    // ...
}

// Migration path definition from version 2 to version 3.
val MIGRATION_2_3 = object : Migration(2, 3) {
    override suspend fun migrate(connection: SQLiteConnection) {
        // ...
    }
}

fun createImplementedDb(appContext: Context) {
    Room.databaseBuilder<ImplementedAppDatabase>(appContext, "sample.db")
        .createFromAsset("database/myapp.db")
        .addMigrations(MIGRATION_2_3)
        .build()
}
   
```

<br />

Here's what happens in this situation:

1. Because the database defined in your app is on version 3 and the database already installed on the device is on version 2, a migration is necessary.
2. Because there's an implemented migration path from version 2 to version 3, Room runs the defined [`migrate`](https://developer.android.com/reference/kotlin/androidx/room3/migration/Migration#migrate) function to update the database instance on the device to version 3, preserving the data that's already in the database. Room doesn't use the prepackaged database file, because Room uses prepackaged database files only in the case of a fallback migration.

### Example: Multi-step migration with a prepackaged database

Prepackaged database files can also affect migrations that consist of multiple steps. Consider the following case:

- Your app defines a Room database on version 4.
- The database instance that's already installed on the device is on version 2.
- There's a prepackaged database file that's on version 3.
- There's an implemented migration path from version 3 to version 4, but not from version 2 to version 3.
- Destructive migrations are enabled.

<br />

```kotlin
// Database class definition declaring version 4.
@Database(entities = [SampleEntity::class], version = 4)
abstract class MultiStepAppDatabase : RoomDatabase() {
    // ...
}

val MIGRATION_3_4 = object : Migration(3, 4) {
    override suspend fun migrate(connection: SQLiteConnection) {
        // ...
    }
}

fun createMultiStepDb(appContext: Context) {
    Room.databaseBuilder<MultiStepAppDatabase>(appContext, "sample.db")
        .createFromAsset("database/myapp.db")
        .addMigrations(MIGRATION_3_4)
        .fallbackToDestructiveMigration()
        .build()
}
   
```

<br />

Here's what happens in this situation:

1. Because the database defined in your app is on version 4 and the database instance already installed on the device is on version 2, a migration is necessary.
2. Because there's no implemented migration path from version 2 to version 3, the migration is a fallback migration.
3. Because you call the [`fallbackToDestructiveMigration`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#fallbacktodestructivemigration) builder function, the fallback migration is destructive. Room drops the database instance on the device.
4. Because there's a prepackaged database file that's on version 3, Room recreates the database and populates it using the contents of the prepackaged database file.
5. The database installed on the device is now on version 3. Because it's still lower than the version defined in your app, another migration is necessary.
6. Because there's an implemented migration path from version 3 to version 4, Room runs the defined [`migrate`](https://developer.android.com/reference/kotlin/androidx/room3/migration/Migration#migrate) function to update the database instance on the device to version 4, preserving the data that was copied over from the version 3 prepackaged database file.