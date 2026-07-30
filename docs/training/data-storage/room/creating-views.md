---
title: https://developer.android.com/training/data-storage/room/creating-views
url: https://developer.android.com/training/data-storage/room/creating-views
source: md.txt
---

The [Room persistence library](https://developer.android.com/training/data-storage/room) supports
[SQLite database views](https://www.sqlite.org/lang_createview.html), which let you encapsulate a query
in a class. Room refers to these query-backed classes as *views* , and you can
use them as data objects in a [data access object (DAO)](https://developer.android.com/training/data-storage/room/accessing-data).

> [!NOTE]
> **Note:** Like [entities](https://developer.android.com/training/data-storage/room/defining-data), you can run `SELECT` statements against views. However, you can't run `INSERT`, `UPDATE`, or `DELETE` statements against views.

## Create a view

To create a view, add the [`@DatabaseView`](https://developer.android.com/reference/kotlin/androidx/room3/DatabaseView) annotation to a class. Set the
annotation value to the query that the class represents.

The following code snippet provides an example of a view:


```kotlin
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
```

<br />

## Associate a view with your database

To include this view in your database, add the [`views`](https://developer.android.com/reference/kotlin/androidx/room3/Database#views()) property to your
app's `@Database` annotation:


```kotlin
@Database(
    entities = [User::class, Department::class],
    views = [UserDetail::class],
    version = 1
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun userDao(): UserDao
}
```

<br />