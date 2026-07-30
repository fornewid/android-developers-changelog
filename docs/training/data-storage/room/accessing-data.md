---
title: https://developer.android.com/training/data-storage/room/accessing-data
url: https://developer.android.com/training/data-storage/room/accessing-data
source: md.txt
---

When you use the Room persistence library to store your app's data, you interact
with the stored data by defining *data access objects*, or DAOs. Each DAO
includes functions that offer abstract access to your app's database. At compile
time, Room automatically generates implementations of the DAOs that you define.

By using DAOs to access your app's database instead of query builders or direct
queries, you can preserve [separation of concerns](https://developer.android.com/jetpack/guide#separation-of-concerns), a critical architectural
principle. DAOs also let you mock database access when you
[test your app](https://developer.android.com/training/data-storage/room/testing-db).

## Anatomy of a DAO

You can define each DAO as either an interface or an abstract class. For basic
use cases, you usually use an interface. In either case, you must always
annotate your DAOs with [`@Dao`](https://developer.android.com/reference/kotlin/androidx/room3/Dao). DAOs don't have properties, but they do
define one or more functions for interacting with the data in your app's
database.

The following code is an example of a DAO that defines functions for
inserting, deleting, and selecting `User` objects in a Room database:


```kotlin
@Dao
interface UserDao {
    @Insert
    suspend fun insertAll(vararg users: User)

    @Delete
    suspend fun delete(user: User)

    @Query("SELECT * FROM user")
    suspend fun getAll(): List<User>
}
```

<br />

There are two types of DAO functions that define database interactions:

- Convenience functions that let you insert, update, and delete rows in your database without writing any SQL code.
- Query functions that let you write your own SQL query to interact with the database.

The following sections demonstrate how to use both types of DAO functions to
define the database interactions that your app needs.

## Convenience functions

Room provides convenience annotations for defining functions that perform
insertions, updates, and deletions without requiring you to write a SQL
statement.

If you need to define more complex insertions, updates, or deletions, or if you
need to query the data in the database, use a [query function](https://developer.android.com/training/data-storage/room/accessing-data#query) instead.

### Insert

The [`@Insert`](https://developer.android.com/reference/kotlin/androidx/room3/Insert) annotation lets you define functions that insert their
parameters into the appropriate table in the database. The following code shows
examples of valid `@Insert` functions that insert one or more `User` objects
into the database:


```kotlin
@Dao
interface UserDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUsers(vararg users: User)

    @Insert
    suspend fun insertBothUsers(user1: User, user2: User)

    @Insert
    suspend fun insertUsersAndFriends(user: User, friends: List<User>)
}
```

<br />

Each parameter for an `@Insert` function must be either an instance of a [Room
data entity class](https://developer.android.com/training/data-storage/room/defining-data) annotated with `@Entity` or a collection of data entity
class instances. When an `@Insert` function is called, Room inserts each passed
entity instance into the corresponding database table.

If the `@Insert` function receives a single parameter, it can return a `Long`
value, which is the new `rowId` for the inserted item. If the parameter is an
array or a collection, then it should return an array or a collection of `Long`
values instead, with each value as the `rowId` for one of the inserted items.
To learn more about returning `rowId` values, see the reference
documentation for the [`@Insert`](https://developer.android.com/reference/kotlin/androidx/room3/Insert) annotation and the [SQLite documentation
for rowid tables](https://www.sqlite.org/rowidtable.html).

### Update

The [`@Update`](https://developer.android.com/reference/kotlin/androidx/room3/Update) annotation lets you define functions that update specific
rows in a database table. Like `@Insert` functions, `@Update` functions accept
data entity instances as parameters. The following code shows an example of an
`@Update` function that attempts to update one or more `User` objects in the
database:


```kotlin
@Dao
interface UserDao {
    @Update
    suspend fun updateUsers(vararg users: User)
}
```

<br />

Room uses the [primary key](https://developer.android.com/training/data-storage/room/defining-data#primary-key) to match entity instances in arguments to rows in
the database. If there's no row with the same primary key, Room makes no
changes.

An `@Update` function can optionally return an `Int` value indicating the number
of rows that were updated successfully.

### Delete

The [`@Delete`](https://developer.android.com/reference/kotlin/androidx/room3/Delete) annotation lets you
define functions that delete specific rows from a database table. Like
`@Insert` functions, `@Delete` functions accept data entity instances as
parameters. The following code shows an example of a `@Delete` function that
attempts to delete one or more `User` objects from the database:


```kotlin
@Dao
interface UserDao {
    @Delete
    suspend fun deleteUsers(vararg users: User)
}
```

<br />

Room uses the [primary key](https://developer.android.com/training/data-storage/room/defining-data#primary-key) to match entity instances in arguments to rows in
the database. If there's no row with the same primary key, Room makes no
changes.

A `@Delete` function can optionally return an `Int` value indicating the number
of rows that were deleted successfully.

### Upsert

The [`@Upsert`](https://developer.android.com/reference/kotlin/androidx/room3/Upsert) annotation lets you
define functions that insert entity instances when there's no matching row, or
update them if a row already exists with the same primary key.

Like `@Insert` and `@Update` functions, `@Upsert` functions accept data entity
instances as parameters. The following code shows an example of an `@Upsert`
function that attempts to upsert one or more `User` objects in the database:


```kotlin
@Dao
interface UserDao {
    @Upsert
    suspend fun upsertUsers(vararg users: User)
}
```

<br />

If the `@Upsert` function receives a single parameter, it can return a `Long`
value. If it results in a new row being inserted, it returns the `rowId` of the
newly inserted row. If it results in an existing row being updated, it returns
`-1`. If the parameter is an array or a collection, it should return an array or
a collection of `Long` values instead.

## Query functions

The [`@Query`](https://developer.android.com/reference/kotlin/androidx/room3/Query) annotation lets you
write SQL statements and expose them as DAO functions. Use these query functions
to query data from your app's database or when you need to perform more complex
insertions, updates, and deletions.

Room validates SQL queries at compile time. This means that if there's a problem
with your query, a compilation error occurs instead of a runtime failure.

### Simple queries

The following code defines a function that uses a `SELECT` query to return all
the `User` objects in the database:


```kotlin
@Query("SELECT * FROM user")
suspend fun loadAllUsers(): List<User>
```

<br />

The following sections demonstrate how to modify this example for typical use
cases.

### Return a subset of a table's columns

Most of the time, you need only return a subset of the columns from the table
that you're querying. For example, your UI might display only the first and
last name for a user instead of every detail about that user. To save resources
and streamline your query's execution, only query the properties that you need.

Room lets you return a data object from any of your queries as long as
you can map the set of result columns onto the returned object. For example, you
can define the following object to hold a user's first and last name:


```kotlin
data class NameTuple(
    @ColumnInfo(name = "first_name") val firstName: String,
    @ColumnInfo(name = "last_name") val lastName: String
)
```

<br />

Then, you can return that data object from your query function:


```kotlin
@Query("SELECT first_name, last_name FROM user")
suspend fun loadFullName(): List<NameTuple>
```

<br />

Because the query returns values for the `first_name` and `last_name` columns,
Room maps these values to the properties in the `NameTuple` class. If the
query returns a column that doesn't map onto a
property in the returned object, Room displays a warning.

Although the previous example uses a custom data class to retrieve a subset of
columns, Room also supports returning `kotlin.Pair` and `kotlin.Triple` for
convenience when a query returns exactly two or three columns. When using these
types, the columns are mapped by the order they're defined in the query
statement, so the order of columns in the `SELECT` statement must match the
order of types in the `Pair` or `Triple`.

### Pass simple parameters to a query

Most of the time, your DAO functions need to accept parameters so that they can
perform filtering operations. Room supports using function parameters as bind
parameters in your queries.

For example, the following code defines a function that returns all the users
above a certain age:


```kotlin
@Query("SELECT * FROM user WHERE age > :minAge")
suspend fun loadAllUsersOlderThan(minAge: Int): Array<User>
```

<br />

You can also pass multiple parameters or reference the same parameter multiple
times in a query, as demonstrated in the following code:


```kotlin
@Query("SELECT * FROM user WHERE age BETWEEN :minAge AND :maxAge")
suspend fun loadAllUsersBetweenAges(minAge: Int, maxAge: Int): Array<User>

@Query(
    """
    SELECT * FROM user
    WHERE first_name LIKE :search OR last_name LIKE :search
    """
)
suspend fun findUserWithName(search: String): List<User>
```

<br />

### Pass a collection of parameters to a query

Some of your DAO functions might require you to pass in a variable number of
parameters that isn't known until runtime. If a parameter represents a
collection, it's automatically expanded at runtime based on the number of
values.

For example, the following code defines a function that returns information
about all the users from a subset of regions:


```kotlin
@Query("SELECT * FROM user WHERE region IN (:regions)")
suspend fun loadUsersFromRegions(regions: List<String>): List<User>
```

<br />

### Query multiple tables

Some of your queries might require access to multiple tables to calculate the
result. You can use `JOIN` clauses in your SQL queries to reference more than
one table.

The following code defines a function that joins three tables together to return
the books that are currently on loan to a specific user:


```kotlin
@Query(
    """
    SELECT * FROM book
    INNER JOIN loan ON loan.book_id = book.id
    INNER JOIN user ON user.id = loan.user_id
    WHERE user.name LIKE :userName
    """
)
suspend fun findBooksBorrowedByName(userName: String): List<Book>
```

<br />

You can also define data objects to return a subset of columns from multiple
joined tables. For more information, see
[Return a subset of a table's columns](https://developer.android.com/training/data-storage/room/accessing-data#return-subset).
The following code defines a DAO with a function that returns the
names of users and the names of the books that they've borrowed:


```kotlin
interface UserBookDao {
    @Query(
        """
        SELECT user.name AS userName, book.name AS bookName
        FROM user, book
        WHERE user.id = book.user_id
        """
    )
    fun loadUserAndBookNames(): Flow<List<UserBook>>
}

data class UserBook(val userName: String, val bookName: String)
```

<br />

### Return a multimap

For joining operations, you can also query columns from multiple tables without
defining an additional data class by writing query functions that return a
[multimap](https://en.wikipedia.org/wiki/Multimap).

Consider the example from [Query multiple tables](https://developer.android.com/training/data-storage/room/accessing-data#multiple-tables). Instead of returning a
list of instances of a custom data class that holds pairings of `User` and
`Book` instances, you can return a mapping of `User` and `Book` directly from
your query function:


```kotlin
@Query(
    """
    SELECT * FROM user
    JOIN book ON user.id = book.user_id
    """
)
suspend fun loadUserAndBookNames(): Map<User, List<Book>>
```

<br />

When your query function returns a multimap, you can write queries that use
`GROUP BY` clauses, letting you take advantage of SQL's capabilities for
advanced calculations and filtering. For example, you can modify your
`loadUserAndBookNames` function to only return users with three or more books
checked out:


```kotlin
@Query(
    """
    SELECT * FROM user
    JOIN book ON user.id = book.user_id
    GROUP BY user.name HAVING COUNT(book.id) >= 3
    """
)
suspend fun loadUserAndBookNamesGrouped(): Map<User, List<Book>>
```

<br />

If you don't need to map entire objects, you can also return mappings between
specific columns in your query by using the [`@MapColumn`](https://developer.android.com/reference/kotlin/androidx/room3/MapColumn) annotation on the
return type's generic parameters.


```kotlin
@Query(
    """
    SELECT user.name AS username, book.name AS bookname FROM user
    JOIN book ON user.id = book.user_id
    """
)
suspend fun loadUserAndBookNamesColumns(): Map<
    @MapColumn(columnName = "username") String,
    List<@MapColumn(columnName = "bookname") String>
    >
```

<br />

## Special return types

Room provides some special return types for integration with other API
libraries.

> [!NOTE]
> **Note:** These special return types, such as RxJava, LiveData, and Guava, are supported in Room using **DAO Return Type Converters** and require registering the respective converter class. For more information, see the [Write asynchronous DAO queries](https://developer.android.com/training/data-storage/room/async-queries) guide.

### Paginated queries with the Paging library

Room supports paginated queries through integration with the
[Paging library](https://developer.android.com/topic/libraries/architecture/paging/v3-overview). To use Paging 3 return types, you must register the Paging
return type converters in your database or DAO:

1. Include the `androidx.room3:room3-paging` artifact in your build configuration.
2. Annotate your `@Database` or `@Dao` declaration with `@DaoReturnTypeConverters(PagingSourceDaoReturnTypeConverter::class)`.

Once registered, your DAOs can return [`PagingSource`](https://developer.android.com/reference/kotlin/androidx/paging/PagingSource) objects for use with
[Paging 3](https://developer.android.com/topic/libraries/architecture/paging/v3-overview):


```kotlin
@Dao
@DaoReturnTypeConverters(PagingSourceDaoReturnTypeConverter::class)
interface UserDao {
    @Query("SELECT * FROM users WHERE label LIKE :query")
    fun pagingSource(query: String): PagingSource<Int, User>
}
```

<br />

For more information about choosing type parameters for a `PagingSource`, see
[Select key and value types](https://developer.android.com/topic/libraries/architecture/paging/v3-paged-data#key-value).

### Direct database connection access

If your app's logic requires direct, low-level access to the database
connection, you can use Room's connection APIs instead. You can obtain a
connection using
[`useReaderConnection`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase#(androidx.room3.RoomDatabase).useReaderConnection(kotlin.coroutines.SuspendFunction1))
for read-only operations or
[`useWriterConnection`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase#(androidx.room3.RoomDatabase).useWriterConnection(kotlin.coroutines.SuspendFunction1))
for write operations on your `RoomDatabase` instance, and use
[`usePrepared`](https://developer.android.com/reference/kotlin/androidx/room3/PooledConnection#usePrepared(kotlin.String,kotlin.coroutines.SuspendFunction1))
to execute statements:


```kotlin
val result: List<Pair<Long, String>> =
    roomDatabase.useReaderConnection { connection ->
        connection.usePrepared(
            "SELECT * FROM user WHERE age > :minAge LIMIT 5"
        ) { stmt ->
            // Bind arguments if needed
            stmt.bindLong(1, minAge.toLong())
            buildList {
                // Step through the results
                while (stmt.step()) {
                    add(stmt.getLong(0) to stmt.getText(1))
                }
            }
        }
    }
```

<br />

If you need to perform low-level database transactions directly on the
connection, you can use the [`immediateTransaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transactor#(androidx.room3.Transactor).immediateTransaction(kotlin.coroutines.SuspendFunction1)),
[`deferredTransaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transactor#(androidx.room3.Transactor).deferredTransaction(kotlin.coroutines.SuspendFunction1)), or [`exclusiveTransaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transactor#(androidx.room3.Transactor).exclusiveTransaction(kotlin.coroutines.SuspendFunction1)) helper functions on
a [`Transactor`](https://developer.android.com/reference/kotlin/androidx/room3/Transactor) instance inside a `useWriterConnection` block:


```kotlin
roomDatabase.useWriterConnection { transactor ->
    transactor.immediateTransaction {
        // Perform transactional database operations using transactor
    }
}
```

<br />

Alternatively, if you only need to execute high-level DAO operations in a
transaction, use the [`withReadTransaction`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase#(androidx.room3.RoomDatabase).withReadTransaction(kotlin.coroutines.SuspendFunction1)) or [`withWriteTransaction`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase#(androidx.room3.RoomDatabase).withWriteTransaction(kotlin.coroutines.SuspendFunction1))
helper extension functions on your `RoomDatabase` instance:


```kotlin
// Perform transactional read operations (DEFERRED transaction)
val userCount = roomDatabase.withReadTransaction {
    userDao.countUsers()
}

// Perform transactional write operations (IMMEDIATE transaction)
roomDatabase.withWriteTransaction {
    userDao.insert(newUser)
    userDao.update(existingUser)
}
```

<br />

> [!IMPORTANT]
> **Important:** In Room 3.0, standard Android `Cursor` or `SupportSQLiteDatabase` types aren't supported by default. Perform low-level operations using `SQLiteConnection` and `SQLiteStatement` from the `androidx.sqlite` package. If your codebase relies extensively on legacy `SupportSQLiteDatabase` APIs and requires an incremental migration path, you can include the `androidx.room3:room3-sqlite-wrapper` compatibility artifact and use the `RoomDatabase.getSupportWrapper` extension function to obtain a wrapper.