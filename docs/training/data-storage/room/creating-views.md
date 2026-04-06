---
title: Create views into a database  |  App data and files  |  Android Developers
url: https://developer.android.com/training/data-storage/room/creating-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Create views into a database Stay organized with collections Save and categorize content based on your preferences.




Version 2.1.0 and higher of the [Room persistence
library](/training/data-storage/room) provides support for [SQLite database
views](https://www.sqlite.org/lang_createview.html), allowing you
to encapsulate a query into a class. Room refers to these query-backed classes
as *views*, and they behave the same as simple data objects when used in a
[DAO](/training/data-storage/room/accessing-data).

**Note:** Like [entities](/training/data-storage/room/defining-data), you can run
`SELECT` statements against views. However, you cannot run `INSERT`, `UPDATE`,
or `DELETE` statements against views.

## Create a view

To create a view, add the
[`@DatabaseView`](/reference/androidx/room/DatabaseView) annotation to a class.
Set the annotation's value to the query that the class should represent.

The following code snippet provides an example of a view:

### Kotlin

```
@DatabaseView("SELECT user.id, user.name, user.departmentId," +
        "department.name AS departmentName FROM user " +
        "INNER JOIN department ON user.departmentId = department.id")
data class UserDetail(
    val id: Long,
    val name: String?,
    val departmentId: Long,
    val departmentName: String?
)
```

### Java

```
@DatabaseView("SELECT user.id, user.name, user.departmentId," +
              "department.name AS departmentName FROM user " +
              "INNER JOIN department ON user.departmentId = department.id")
public class UserDetail {
    public long id;
    public String name;
    public long departmentId;
    public String departmentName;
}
```

## Associate a view with your database

To include this view as part of your app's database, include the
[`views`](/reference/androidx/room/Database#views) property in your app's
`@Database` annotation:

### Kotlin

```
@Database(entities = [User::class],
          views =[UserDetail::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

### Java

```
@Database(entities = {User.class}, views = {UserDetail.class},
          version = 1)
public abstract class AppDatabase extends RoomDatabase {
    public abstract UserDao userDao();
}
```

[Previous

arrow\_back

Write asynchronous DAO queries](/training/data-storage/room/async-queries)

[Next

Prepopulate your database

arrow\_forward](/training/data-storage/room/prepopulate)