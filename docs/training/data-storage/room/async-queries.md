---
title: Write asynchronous DAO queries  |  App data and files  |  Android Developers
url: https://developer.android.com/training/data-storage/room/async-queries
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Write asynchronous DAO queries Stay organized with collections Save and categorize content based on your preferences.



To prevent queries from blocking the UI, Room does not allow database access on
the main thread. This restriction means that you must make your [DAO
queries](/training/data-storage/room/accessing-data) asynchronous. The Room
library includes integrations with several different frameworks to provide
asynchronous query execution.

DAO queries fall into three categories:

* *One-shot write* queries that insert, update, or delete data in the database.
* *One-shot read* queries that read data from your database only once and return
  a result with the snapshot of the database at that time.
* *Observable read* queries that read data from your database every time the
  underlying database tables change and emit new values to reflect those
  changes.

## Language and framework options

Room provides integration support for interoperability with specific language
features and libraries. The following table shows applicable return types based
on query type and framework:

| Query type | Kotlin language features | RxJava | Guava | Jetpack Lifecycle |
| --- | --- | --- | --- | --- |
| One-shot write | Coroutines (`suspend`) | `Single<T>`, `Maybe<T>`, `Completable` | `ListenableFuture<T>` | N/A |
| One-shot read | Coroutines (`suspend`) | `Single<T>`, `Maybe<T>` | `ListenableFuture<T>` | N/A |
| Observable read | `Flow<T>` | `Flowable<T>`, `Publisher<T>`, `Observable<T>` | N/A | `LiveData<T>` |

This guide demonstrates three possible ways that you can use these integrations
to implement asynchronous queries in your DAOs.

### Kotlin with Flow and couroutines

Kotlin provides language features that allow you to write asynchronous queries
without third-party frameworks:

* In Room 2.2 and higher, you can use Kotlin's
  [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/)
  functionality to write observable queries.
* In Room 2.1 and higher, you can use the `suspend` keyword to make your DAO
  queries asynchronous using [Kotlin coroutines](/kotlin/coroutines).

**Note:** To use Kotlin Flow and coroutines with Room, you must include the
`room-ktx` artifact in your `build.gradle` file. For more information, see
[Declaring
dependencies](/jetpack/androidx/releases/room#declaring_dependencies).

### Java with RxJava

If your app uses the Java programming language, you can use specialized return
types from the RxJava framework to write asynchronous DAO methods. Room provides
support for the following RxJava 2 return types:

* For one-shot queries, Room 2.1 and higher supports the
  [`Completable`](http://reactivex.io/RxJava/javadoc/io/reactivex/Completable),
  [`Single<T>`](http://reactivex.io/RxJava/javadoc/io/reactivex/Single),
  and [`Maybe<T>`](http://reactivex.io/RxJava/javadoc/io/reactivex/Maybe)
  return types.
* For observable queries, Room supports the
  [`Publisher<T>`](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher),
  [`Flowable<T>`](http://reactivex.io/RxJava/2.x/javadoc/io/reactivex/Flowable),
  and [`Observable<T>`](http://reactivex.io/RxJava/2.x/javadoc/io/reactivex/Observable)
  return types.

Additionally, Room 2.3 and higher supports RxJava 3.

**Note:** To use RxJava with Room, you must include either the `room-rxjava2`
artifact or the `room-rxjava3` artifact in your `build.gradle` file. For more
information, see [Declaring
dependencies](/jetpack/androidx/releases/room#declaring_dependencies).

### Java with LiveData and Guava

If your app uses the Java programming language and you do not want to use the
RxJava framework, you can use the following alternatives to write asynchronous
queries:

* You can use the [`LiveData`](/reference/androidx/lifecycle/LiveData) wrapper
  class from Jetpack to write asynchronous observable queries.
* You can use the
  [`ListenableFuture<T>`](https://guava.dev/releases/21.0/api/docs/com/google/common/util/concurrent/ListenableFuture)
  wrapper from Guava to write asynchronous one-shot queries.

**Note:** To use Guava with Room, you must include the `room-guava` artifact in your
`build.gradle` file. For more information, see [Declaring
dependencies](/jetpack/androidx/releases/room#declaring_dependencies).

## Write asynchronous one-shot queries

One-shot queries are database operations that only run once and grab a snapshot
of data at the time of execution. Here are some examples of asynchronous
one-shot queries:

### Kotlin

```
@Dao
interface UserDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun insertUsers(vararg users: User)

    @Update
    suspend fun updateUsers(vararg users: User)

    @Delete
    suspend fun deleteUsers(vararg users: User)

    @Query("SELECT * FROM user WHERE id = :id")
    suspend fun loadUserById(id: Int): User

    @Query("SELECT * from user WHERE region IN (:regions)")
    suspend fun loadUsersByRegion(regions: List<String>): List<User>
}
```

### Java

```
@Dao
public interface UserDao {
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    public Completable insertUsers(List<User> users);

    @Update
    public Completable updateUsers(List<User> users);

    @Delete
    public Completable deleteUsers(List<User> users);

    @Query("SELECT * FROM user WHERE id = :id")
    public Single<User> loadUserById(int id);

    @Query("SELECT * from user WHERE region IN (:regions)")
    public Single<List<User>> loadUsersByRegion(List<String> regions);
}
```

### Java

```
@Dao
public interface UserDao {
    // Returns the number of users inserted.
    @Insert(onConflict = OnConflictStrategy.REPLACE)
    public ListenableFuture<Integer> insertUsers(List<User> users);

    // Returns the number of users updated.
    @Update
    public ListenableFuture<Integer> updateUsers(List<User> users);

    // Returns the number of users deleted.
    @Delete
    public ListenableFuture<Integer> deleteUsers(List<User> users);

    @Query("SELECT * FROM user WHERE id = :id")
    public ListenableFuture<User> loadUserById(int id);

    @Query("SELECT * from user WHERE region IN (:regions)")
    public ListenableFuture<List<User>> loadUsersByRegion(List<String> regions);
}
```

## Write observable queries

Observable queries are read operations that emit new values whenever there are
changes to any of the tables that are referenced by the query. One way you might
use this is to help you keep a displayed list of items up to date as the items
in the underlying database are inserted, updated, or removed. Here are some
examples of observable queries:

### Kotlin

```
@Dao
interface UserDao {
    @Query("SELECT * FROM user WHERE id = :id")
    fun loadUserById(id: Int): Flow<User>

    @Query("SELECT * from user WHERE region IN (:regions)")
    fun loadUsersByRegion(regions: List<String>): Flow<List<User>>
}
```

### Java

```
@Dao
public interface UserDao {
    @Query("SELECT * FROM user WHERE id = :id")
    public Flowable<User> loadUserById(int id);

    @Query("SELECT * from user WHERE region IN (:regions)")
    public Flowable<List<User>> loadUsersByRegion(List<String> regions);
}
```

### Java

```
@Dao
public interface UserDao {
    @Query("SELECT * FROM user WHERE id = :id")
    public LiveData<User> loadUserById(int id);

    @Query("SELECT * from user WHERE region IN (:regions)")
    public LiveData<List<User>> loadUsersByRegion(List<String> regions);
}
```

**Note:** Observable queries in Room have one important limitation: the query reruns
whenever any row in the table is updated, whether or not that row is in the
result set. You can ensure that the UI is only notified when the actual query
results change by applying the `distinctUntilChanged()` operator from the
corresponding library:
[Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/distinct-until-changed),
[RxJava](http://reactivex.io/documentation/operators/distinct), or
[LiveData](/reference/androidx/lifecycle/Transformations#distinctUntilChanged(androidx.lifecycle.LiveData%3CX%3E)).

## Additional resources

To learn more about asynchronous DAO queries, see the following additional
resources:

### Blogs

* [Room & Flow](https://medium.com/androiddevelopers/room-flow-273acffe5b57)

[Previous

arrow\_back

Access data using DAOs](/training/data-storage/room/accessing-data)

[Next

Create views into a database

arrow\_forward](/training/data-storage/room/creating-views)