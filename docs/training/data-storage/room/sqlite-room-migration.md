---
title: https://developer.android.com/training/data-storage/room/sqlite-room-migration
url: https://developer.android.com/training/data-storage/room/sqlite-room-migration
source: md.txt
---

# Migrate from SQLite to Room

The Room persistence library provides a number of benefits over using the SQLite APIs directly:

- Compile-time verification of SQL queries
- Convenience annotations that minimize repetitive and error-prone boilerplate code
- Streamlined database migration paths

If your app currently uses a non-Room implementation of SQLite, read this page to learn how to migrate your app to use Room instead. If Room is the first SQLite implementation that you are using in your app, see[Save data in a local database using Room](https://developer.android.com/training/data-storage/room)for basic usage information.

## Migration steps

Perform the following steps to migrate your SQLite implementation to Room. If your SQLite implementation uses a large database or complex queries, you might prefer to migrate to Room gradually. See[Incremental migration](https://developer.android.com/training/data-storage/room/sqlite-room-migration#incremental)for an incremental migration strategy.

### Update dependencies

To use Room in your app, you must include the appropriate dependencies in your app's`build.gradle`file. See[Setup](https://developer.android.com/training/data-storage/room#setup)for the most up-to-date Room dependencies.

### Update model classes to data entities

Room uses[data entities](https://developer.android.com/training/data-storage/room/defining-data)to represent the tables in the database. Each entity class represents a table and has fields that represent columns in that table. Follow these steps to update your existing model classes to be Room entities:

1. Annotate the class declaration with[`@Entity`](https://developer.android.com/reference/kotlin/androidx/room/Entity)to indicate that it is a Room entity. You can optionally use the[`tableName`](https://developer.android.com/reference/kotlin/androidx/room/Entity#tablename)property to indicate that the resulting table should have a name that is different from the class name.
2. Annotate the primary key field with[`@PrimaryKey`](https://developer.android.com/reference/kotlin/androidx/room/PrimaryKey).
3. If any of the columns in the resulting table should have a name that is different from the name of the corresponding field, annotate the field with[`@ColumnInfo`](https://developer.android.com/reference/kotlin/androidx/room/ColumnInfo)and set the[`name`](https://developer.android.com/reference/kotlin/androidx/room/ColumnInfo#name)property to the correct column name.
4. If the class has fields that you do not want to persist in the database, annotate those fields with[`@Ignore`](https://developer.android.com/reference/kotlin/androidx/room/Ignore)to indicate that Room should not create columns for them in the corresponding table.
5. If the class has more than one constructor method, indicate which constructor Room should use by annotating all of the other constructors with`@Ignore`.

### Kotlin

```kotlin
@Entity(tableName = "users")
data class User(
  @PrimaryKey
  @ColumnInfo(name = "userid") val mId: String,
  @ColumnInfo(name = "username") val mUserName: String?,
  @ColumnInfo(name = "last_update") val mDate: Date?,
)
```

### Java

```java
@Entity(tableName = "users")
public class User {

  @PrimaryKey
  @ColumnInfo(name = "userid")
  private String mId;

  @ColumnInfo(name = "username")
  private String mUserName;

  @ColumnInfo(name = "last_update")
  private Date mDate;

  @Ignore
  public User(String userName) {
    mId = UUID.randomUUID().toString();
    mUserName = userName;
    mDate = new Date(System.currentTimeMillis());
  }

  public User(String id, String userName, Date date) {
    this.mId = id;
    this.mUserName = userName;
    this.mDate = date;
  }

}
```

### Create DAOs

Room uses data access objects (DAOs) to define methods that access the database. Follow the guidance in[Accessing data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data)to replace your existing query methods with DAOs.

### Create a database class

Implementations of Room use a database class to manage an instance of the database. Your database class should extend[`RoomDatabase`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase)and reference all of the entities and DAOs that you have defined.
**Note:** The migration to Room represents a SQLite database version change, so make sure that you increment the version number by one.  

### Kotlin

```kotlin
@Database(entities = [User::class], version = 2)
@TypeConverters(DateConverter::class)
abstract class UsersDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### Java

```java
@Database(entities = {User.class}, version = 2)
@TypeConverters(DateConverter.class)
public abstract class UsersDatabase extends RoomDatabase {
  public abstract UserDao userDao();
}
```

### Define a migration path

Since the database version number is changing, you must define a[`Migration`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration)object to indicate a migration path so that Room keeps the existing data in the database. As long as the database schema does not change, this can be an empty implementation.  

### Kotlin

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
  override fun migrate(database: SupportSQLiteDatabase) {
    // Empty implementation, because the schema isn't changing.
  }
}
```

### Java

```java
static final Migration MIGRATION_1_2 = new Migration(1, 2) {
  @Override
  public void migrate(SupportSQLiteDatabase database) {
    // Empty implementation, because the schema isn't changing.
  }
};
```

To learn more about database migration paths in Room, see[Migrate your database](https://developer.android.com/training/data-storage/room/migrating-db-versions).

### Update the database instantiation

After you have defined a database class and a migration path, you can use[`Room.databaseBuilder`](https://developer.android.com/reference/kotlin/androidx/room/Room#databasebuilder)to create an instance of your database with the migration path applied:  

### Kotlin

```kotlin
val db = Room.databaseBuilder(
          applicationContext,
          AppDatabase::class.java, "database-name"
        )
          .addMigrations(MIGRATION_1_2).build()
```

### Java

```java
db = Room.databaseBuilder(
          context.getApplicationContext(),
          UsersDatabase.class, "database-name"
        )
          .addMigrations(MIGRATION_1_2).build();
```

### Test your implementation

Make sure you test your new Room implementation:

- Follow the guidance in[Test migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test)to test your database migration.
- Follow the guidance in[Test your database](https://developer.android.com/training/data-storage/room/testing-db#test)to test your DAO methods.

## Incremental migration

If your app uses a large, complex database, it might not be feasible to migrate your app to Room all at once. Instead, you can optionally implement the data entities and Room database as a first step and then migrate your query methods into DAOs later. You can do this by replacing your custom[database helper class](https://developer.android.com/training/data-storage/sqlite#DbHelper)with the[`SupportSQLiteOpenHelper`](https://developer.android.com/reference/kotlin/androidx/sqlite/db/SupportSQLiteOpenHelper)object that you receive from[`RoomDatabase.getOpenHelper()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase#getopenhelper).

## Additional resources

To learn more about migrating from SQLite to Room, see the following additional resources:

### Blogs

- [7 Steps to Room](https://medium.com/androiddevelopers/7-steps-to-room-27a5fe5f99b2)
- [Incrementally migrate from SQLite to Room](https://medium.com/androiddevelopers/incrementally-migrate-from-sqlite-to-room-66c2f655b377)