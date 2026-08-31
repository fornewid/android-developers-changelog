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





The [Room persistence library](/training/data-storage/room) supports
[SQLite database views](https://www.sqlite.org/lang_createview.html), which let you encapsulate a query
in a class. Room refers to these query-backed classes as *views*, and you can
use them as data objects in a [data access object (DAO)](/training/data-storage/room/accessing-data).

**Note:** Like [entities](/training/data-storage/room/defining-data), you can run `SELECT` statements against views.
However, you can't run `INSERT`, `UPDATE`, or `DELETE` statements against
views.

## Create a view

To create a view, add the [`@DatabaseView`](/reference/kotlin/androidx/room3/DatabaseView) annotation to a class. Set the
annotation value to the query that the class represents.

The following code snippet provides an example of a view:

```
@DatabaseView(
    """
    SELECT User.id, User.name, User.departmentId, Department.name AS departmentName
    FROM User INNER JOIN Department ON User.departmentId = Department.id
    """
)
data class UserDetail(
    val id: Long,
    val name: String?,
    val departmentId: Long,
    val departmentName: String?
)

CreatingViewsSnippets.kt
```

## Associate a view with your database

To include this view in your database, add the [`views`](/reference/kotlin/androidx/room3/Database#views()) property to your
app's `@Database` annotation:

```
@Database(
    entities = [User::class, Department::class],
    views = [UserDetail::class],
    version = 1
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}

CreatingViewsSnippets.kt
```

[Previous

arrow\_back

Write asynchronous DAO queries](/training/data-storage/room/async-queries)

[Next

Prepopulate your database

arrow\_forward](/training/data-storage/room/prepopulate)