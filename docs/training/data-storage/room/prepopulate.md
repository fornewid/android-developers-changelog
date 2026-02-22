---
title: https://developer.android.com/training/data-storage/room/prepopulate
url: https://developer.android.com/training/data-storage/room/prepopulate
source: md.txt
---

# Prepopulate your Room database

Sometimes, you might want your app to start with a database that is already loaded with a specific set of data. This is called*prepopulating*a database. In Room 2.2.0 and higher, you can use API methods to prepopulate a Room database at initialization with contents from a prepackaged database file in the device's file system.
| **Note:** [In-memory Room databases](https://developer.android.com/reference/kotlin/androidx/room/Room#inmemorydatabasebuilder)don't support prepopulating the database using[`createFromAsset()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#createfromasset)or[`createFromFile()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#createfromfile).

## Prepopulate from an app asset

To prepopulate a Room database from a prepackaged database file that is located anywhere in your app's`assets/`directory, call the[`createFromAsset()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#createfromasset)method from your`RoomDatabase.Builder`object before calling[`build()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#build):  

### Kotlin

```kotlin
Room.databaseBuilder(appContext, AppDatabase::class.java, "Sample.db")
    .createFromAsset("database/myapp.db")
    .build()
```

### Java

```java
Room.databaseBuilder(appContext, AppDatabase.class, "Sample.db")
    .createFromAsset("database/myapp.db")
    .build();
```

The`createFromAsset()`method accepts a string argument that contains a relative path from the`assets/`directory to the prepackaged database file.
| **Note:** When prepopulating from an asset, Room validates the database to ensure that its schema matches the schema of the prepackaged database. You should[export your database's schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schema)to use as a reference as you create the prepackaged database file.

## Prepopulate from the file system

To prepopulate a Room database from a prepackaged database file that is located anywhere in the device's file system*except* your app's`assets/`directory, call the[`createFromFile()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#createfromfile)method from your`RoomDatabase.Builder`object before calling[`build()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#build):  

### Kotlin

```kotlin
Room.databaseBuilder(appContext, AppDatabase::class.java, "Sample.db")
    .createFromFile(File("mypath"))
    .build()
```

### Java

```java
Room.databaseBuilder(appContext, AppDatabase.class, "Sample.db")
    .createFromFile(new File("mypath"))
    .build();
```

The`createFromFile()`method accepts a[`File`](https://developer.android.com/reference/java/io/File)argument for the prepackaged database file. Room creates a copy of the designated file rather than opening it directly, so make sure your app has read permissions on the file.
| **Note:** When prepopulating from the file system, Room validates the database to ensure that its schema matches the schema of the prepackaged database. You should[export your database's schema](https://developer.android.com/training/data-storage/room/migrating-db-versions#export-schema)to use as a reference as you create the prepackaged database file.

## Handle migrations that include prepackaged databases

Prepackaged database files can also change the way your Room database handles fallback migrations. Ordinarily, when[destructive migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#handle-missing-migrations)are enabled and Room must perform a migration without a migration path, Room drops all tables in the database and creates an empty database with the specified schema for the target version. However, if you include a prepackaged database file with the same number as the target version, Room attempts to populate the newly recreated database with the contents of the prepackaged database file after performing the destructive migration.

For more information on Room database migrations, see[Migrating Room databases](https://developer.android.com/training/data-storage/room/migrating-db-versions).

The following sections present a few examples of how this works in practice.

### Example: Fallback migration with a prepackaged database

Suppose the following:

- Your app defines a Room database on version 3.
- The database instance that is already installed on the device is on version 2.
- There is a prepackaged database file that is on version 3.
- There is no implemented migration path from version 2 to version 3.
- Destructive migrations are enabled.

### Kotlin

```kotlin
// Database class definition declaring version 3.
@Database(version = 3)
abstract class AppDatabase : RoomDatabase() {
    ...
}

// Destructive migrations are enabled and a prepackaged database
// is provided.
Room.databaseBuilder(appContext, AppDatabase::class.java, "Sample.db")
    .createFromAsset("database/myapp.db")
    .fallbackToDestructiveMigration()
    .build()
```

### Java

```java
// Database class definition declaring version 3.
@Database(version = 3)
public abstract class AppDatabase extends RoomDatabase {
    ...
}

// Destructive migrations are enabled and a prepackaged database
// is provided.
Room.databaseBuilder(appContext, AppDatabase.class, "Sample.db")
    .createFromAsset("database/myapp.db")
    .fallbackToDestructiveMigration()
    .build();
```

Here is what happens in this situation:

1. Because the database defined in your app is on version 3 and the database instance already installed on the device is on version 2, a migration is necessary.
2. Because there is no implemented migration plan from version 2 to version 3, the migration is a fallback migration.
3. Because the[`fallbackToDestructiveMigration()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbacktodestructivemigration)builder method is called, the fallback migration is destructive. Room drops the database instance that's installed on the device.
4. Because there is a prepackaged database file that is on version 3, Room recreates the database and populates it using the contents of the prepackaged database file. If, on the other hand, you prepackaged database file were on version 2, then Room would note that it does not match the target version and would not use it as part of the fallback migration.

### Example: Implemented migration with a prepackaged database

Suppose instead that your app implements a migration path from version 2 to version 3:  

### Kotlin

```kotlin
// Database class definition declaring version 3.
@Database(version = 3)
abstract class AppDatabase : RoomDatabase() {
    ...
}

// Migration path definition from version 2 to version 3.
val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(database: SupportSQLiteDatabase) {
        ...
    }
}

// A prepackaged database is provided.
Room.databaseBuilder(appContext, AppDatabase::class.java, "Sample.db")
    .createFromAsset("database/myapp.db")
    .addMigrations(MIGRATION_2_3)
    .build()
```

### Java

```java
// Database class definition declaring version 3.
@Database(version = 3)
public abstract class AppDatabase extends RoomDatabase {
    ...
}

// Migration path definition from version 2 to version 3.
static final Migration MIGRATION_2_3 = new Migration(2, 3) {
    @Override
    public void migrate(SupportSQLiteDatabase database) {
        ...
    }
};

// A prepackaged database is provided.
Room.databaseBuilder(appContext, AppDatabase.class, "Sample.db")
    .createFromAsset("database/myapp.db")
    .addMigrations(MIGRATION_2_3)
    .build();
```

Here is what happens in this situation:

1. Because the database defined in your app is on version 3 and the database already installed on the device is on version 2, a migration is necessary.
2. Because there is an implemented migration path from version 2 to version 3, Room runs the defined[`migrate()`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration#migrate)method to update the database instance on the device to version 3, preserving the data that is already in the database. Room does not use the prepackaged database file, because Room uses prepackaged database files only in the case of a fallback migration.

### Example: Multi-step migration with a prepackaged database

Prepackaged database files can also affect migrations that consist of multiple steps. Consider the following case:

- Your app defines a Room database on version 4.
- The database instance that is already installed on the device is on version 2.
- There is a prepackaged database file that is on version 3.
- There is an implemented migration path from version 3 to version 4, but not from version 2 to version 3.
- Destructive migrations are enabled.

### Kotlin

```kotlin
// Database class definition declaring version 4.
@Database(version = 4)
abstract class AppDatabase : RoomDatabase() {
    ...
}

// Migration path definition from version 3 to version 4.
val MIGRATION_3_4 = object : Migration(3, 4) {
    override fun migrate(database: SupportSQLiteDatabase) {
        ...
    }
}

// Destructive migrations are enabled and a prepackaged database is
// provided.
Room.databaseBuilder(appContext, AppDatabase::class.java, "Sample.db")
    .createFromAsset("database/myapp.db")
    .addMigrations(MIGRATION_3_4)
    .fallbackToDestructiveMigration()
    .build()
```

### Java

```java
// Database class definition declaring version 4.
@Database(version = 4)
public abstract class AppDatabase extends RoomDatabase {
    ...
}

// Migration path definition from version 3 to version 4.
static final Migration MIGRATION_3_4 = new Migration(3, 4) {
    @Override
    public void migrate(SupportSQLiteDatabase database) {
        ...
    }
};

// Destructive migrations are enabled and a prepackaged database is
// provided.
Room.databaseBuilder(appContext, AppDatabase.class, "Sample.db")
    .createFromAsset("database/myapp.db")
    .addMigrations(MIGRATION_3_4)
    .fallbackToDestructiveMigration()
    .build();
```

Here is what happens in this situation:

1. Because the database defined in your app is on version 4 and the database instance already installed on the device is on version 2, a migration is necessary.
2. Because there is no implemented migration path from version 2 to version 3, the migration is a fallback migration.
3. Because the[`fallbackToDestructiveMigration()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbacktodestructivemigration)builder method is called, the fallback migration is destructive. Room drops the database instance on the device.
4. Because there is a prepackaged database file that is on version 3, Room recreates the database and populates it using the contents of the prepackaged database file.
5. The database installed on the device is now on version 3. Because this is still lower than the version defined in your app, another migration is necessary.
6. Because there is an implemented migration path from version 3 to version 4, Room runs the defined[`migrate()`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration#migrate)method to update the database instance on the device to version 4, preserving the data that was copied over from the version 3 prepackaged database file.

## Additional resources

To learn more about prepopulating a Room database, see the following additional resources.

### Videos

- [What's New in Room](https://www.youtube.com/watch?v=_aJsh6P00c0)(Android Dev Summit '19)

### Blogs

- [Packing the Room: Pre-populate your database with this one method](https://medium.com/androiddevelopers/packing-the-room-pre-populate-your-database-with-this-one-method-333ae190e680)