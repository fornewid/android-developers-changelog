---
title: https://developer.android.com/training/data-storage/room/sqlite-room-migration
url: https://developer.android.com/training/data-storage/room/sqlite-room-migration
source: md.txt
---

The Room persistence library provides a number of benefits over using the SQLite APIs directly:

- Compile-time verification of SQL queries
- Convenience annotations that minimize repetitive and error-prone boilerplate code
- Streamlined database migration paths

If your app has a non-Room SQLite implementation, read this page to learn how to migrate to Room. If Room is the first SQLite implementation in your app, see [Save data in a local database using Room](https://developer.android.com/training/data-storage/room) for basic usage.

## Migration steps

Perform the following steps to migrate your SQLite implementation to Room. If your SQLite implementation uses a large database or complex queries, you might prefer to migrate to Room gradually. For more information about an incremental migration strategy, see [Incremental migration](https://developer.android.com/training/data-storage/room/sqlite-room-migration#incremental).

### Update dependencies

To use Room in your app, you must include the appropriate dependencies in your app's `build.gradle` file. For more information about Room dependencies, see [Setup](https://developer.android.com/training/data-storage/room#setup).

### Update model classes to data entities

Room uses [data entities](https://developer.android.com/training/data-storage/room/defining-data) to represent the tables in the database. Each entity class represents a table and has properties that represent columns in that table. Follow these steps to update your existing model classes to be Room entities:

1. Annotate the class declaration with [`@Entity`](https://developer.android.com/reference/kotlin/androidx/room3/Entity) to indicate that it's a Room entity. You can optionally use the [`tableName`](https://developer.android.com/reference/kotlin/androidx/room3/Entity#tableName()) property to indicate that the resulting table should have a name different from the class name.
2. Annotate the primary key property with [`@PrimaryKey`](https://developer.android.com/reference/kotlin/androidx/room3/PrimaryKey).
3. If any of the columns in the resulting table should have a name that is different from the name of the corresponding property, annotate the property with [`@ColumnInfo`](https://developer.android.com/reference/kotlin/androidx/room3/ColumnInfo) and set the [`name`](https://developer.android.com/reference/kotlin/androidx/room3/ColumnInfo#name()) property to the correct column name.
4. If the class has properties that you don't want to persist in the database, annotate those properties with [`@Ignore`](https://developer.android.com/reference/kotlin/androidx/room3/Ignore) to indicate that Room shouldn't create columns for them in the corresponding table.
5. If the class has more than one constructor, indicate which constructor Room should use by annotating all of the other constructors with `@Ignore`.

<br />

```kotlin
@Entity(tableName = "users")
data class User(
    @PrimaryKey @ColumnInfo(name = "userid") val id: String,
    @ColumnInfo(name = "username") val userName: String?,
    @ColumnInfo(name = "last_update") val date: Date?,
)
   
```

<br />

### Create DAOs

Room uses data access objects (DAOs) to define functions that access the database. Follow the guidance in [Accessing data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data) to replace your existing query functions with DAOs.

### Create a database class

Implementations of Room use a database class to manage an instance of the database. Your database class should extend [`RoomDatabase`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase) and reference all the entities and DAOs you've defined.

> [!NOTE]
> **Note:** The migration to Room represents a SQLite database version change, so make sure that you increment the version number by one.

<br />

```kotlin
@Database(entities = [User::class], version = 2)
@ColumnTypeConverters(DateConverter::class)
abstract class UsersDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
   
```

<br />

### Define a migration path

Because the database version number is changing, you must define a [`Migration`](https://developer.android.com/reference/kotlin/androidx/room3/migration/Migration) object to preserve the existing database data. If the database schema doesn't change, this migration can be empty.

<br />

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
    override suspend fun migrate(connection: SQLiteConnection) {
        // Empty implementation, because the schema isn't changing.
    }
}
   
```

<br />

For more information about database migration paths in Room, see [Migrate your database](https://developer.android.com/training/data-storage/room/migrating-db-versions).

### Update the database instantiation

After you've defined a database class and a migration path, you can use [`Room.databaseBuilder`](https://developer.android.com/reference/kotlin/androidx/room3/Room#databasebuilder) to create an instance of your database with the migration path applied:

<br />

```kotlin
val db =
    Room.databaseBuilder<UsersDatabase>(applicationContext, "database-name")
        .addMigrations(MIGRATION_1_2)
        .build()
   
```

<br />

### Test your implementation

Make sure you test your new Room implementation:

- Follow the guidance in [Test migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test) to test your database migration.
- Follow the guidance in [Test your database](https://developer.android.com/training/data-storage/room/testing-db#test) to test your DAO functions.

## Incremental migration

If your app uses a large, complex database, it might not be feasible to migrate your app to Room all at once. Instead, you can optionally implement the data entities and Room database as a first step and then migrate your query functions into DAOs later.

To implement an incremental migration, obtain a `SupportSQLiteDatabase` compatibility wrapper using the `roomDatabase.getSupportWrapper` extension function from the `androidx.room3:room3-sqlite-wrapper` artifact. This wrapper lets you execute direct Android-style SQL queries on the Room-managed database using Android SQLite APIs:

<br />

```kotlin
// Get SupportSQLiteDatabase wrapper
val legacyDb = roomDatabase.getSupportWrapper()
legacyDb.execSQL("INSERT INTO users ...")
   
```

<br />