---
title: https://developer.android.com/training/data-storage/room/async-queries
url: https://developer.android.com/training/data-storage/room/async-queries
source: md.txt
---

To prevent queries from blocking the UI, Room doesn't support database access
on the main thread. This restriction means you must make your [DAO queries](https://developer.android.com/training/data-storage/room/accessing-data)
asynchronous. The Room library includes integrations with several frameworks to
provide asynchronous query execution.

DAO queries fall into three categories:

- *One-shot write* queries that insert, update, or delete data in the database.
- *One-shot read* queries that read data from your database only once and return a result with the snapshot of the database at that time.
- *Observable read* queries that read data from your database every time the underlying database tables change and emit new values to reflect those changes.

## Language and framework options

Room provides integration support for interoperability with specific language
features and libraries. The following table shows applicable return types based
on query type and framework:

| Query type | Kotlin language features (Native) | RxJava | Guava | Jetpack Lifecycle\* |
|---|---|---|---|---|
| One-shot write | Coroutines (`suspend`) | `Single<T>`, `Maybe<T>`, `Completable` | `ListenableFuture<T>` | N/A |
| One-shot read | Coroutines (`suspend`) | `Single<T>`, `Maybe<T>` | `ListenableFuture<T>` | N/A |
| Observable read | `Flow<T>` | `Flowable<T>`, `Publisher<T>`, `Observable<T>` | N/A | `LiveData<T>` |

> [!NOTE]
> **Note:** Room supports RxJava, Guava, and LiveData return types using DAO return type converters. To use them, you must register the respective converter class. For more information, see [Custom DAO return type converters](https://developer.android.com/training/data-storage/room/async-queries#custom-converters).

This guide demonstrates three ways to use these integrations to implement
asynchronous queries in your DAOs.

### Kotlin with Flow and coroutines

Kotlin provides built-in language features that let you write asynchronous
queries without third-party frameworks:

- Room directly supports Kotlin's [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) to write observable queries.
- Room requires the `suspend` keyword to make your one-shot DAO queries asynchronous with [Kotlin coroutines](https://developer.android.com/kotlin/coroutines).

Coroutines and Flow support is built directly into the core Room runtime,
so no additional artifacts are required.

### RxJava for Kotlin and Java

Room 3.0 supports RxJava 3 return types. To use RxJava return types, you must
register the RxJava return type converters in your database or DAO:

1. Include the `androidx.room3:room3-rxjava3` artifact in your build configuration.
2. Annotate your `@Database` or `@Dao` declaration with `@DaoReturnTypeConverters(RxDaoReturnTypeConverters::class)`.

Room supports the following RxJava 3 return types:

- **One-shot queries** : [`Completable`](https://reactivex.io/RxJava/3.x/javadoc/3.1.12/io/reactivex/rxjava3/core/Completable.html), [`Single<T>`](https://reactivex.io/RxJava/3.x/javadoc/3.1.12/io/reactivex/rxjava3/core/Single.html), and [`Maybe<T>`](https://reactivex.io/RxJava/3.x/javadoc/3.1.12/io/reactivex/rxjava3/core/Maybe.html)
- **Observable queries** : [`Publisher<T>`](http://www.reactive-streams.org/reactive-streams-1.0.1-javadoc/org/reactivestreams/Publisher), [`Flowable<T>`](https://reactivex.io/RxJava/3.x/javadoc/3.1.12/io/reactivex/rxjava3/core/Flowable.html), and [`Observable<T>`](https://reactivex.io/RxJava/3.x/javadoc/3.1.12/io/reactivex/rxjava3/core/Observable.html)

### LiveData and Guava

Room 3.0 supports LiveData and Guava `ListenableFuture` return types using
converters:

- **LiveData** : Include the `androidx.room3:room3-livedata` artifact and annotate your database or DAO with `@DaoReturnTypeConverters(LiveDataDaoReturnTypeConverter::class)`.
- **Guava** : Include the `androidx.room3:room3-guava` artifact and annotate your database or DAO with `@DaoReturnTypeConverters(GuavaDaoReturnTypeConverter::class)`.

## Write asynchronous one-shot queries

One-shot queries are database operations that only run once and grab a snapshot
of data at the time of execution. Here are some examples of asynchronous
one-shot queries:


```kotlin
@Dao
interface UserDao {
    @Query("SELECT * FROM user WHERE id = :id")
    suspend fun loadUserById(id: Int): User

    @Query("SELECT * from user WHERE region IN (:regions)")
    suspend fun loadUsersByRegion(regions: List<String>): List<User>
}
```

<br />

## Write observable queries

Observable queries are read operations that emit new values whenever the
referenced tables change. For example, you can use this behavior to keep a
displayed list of items updated as the database changes. Here are some examples
of observable queries:


```kotlin
@Dao
interface ObservableUserDao {
    @Query("SELECT * FROM user WHERE id = :id")
    fun loadUserById(id: Int): Flow<User>

    @Query("SELECT * from user WHERE region IN (:regions)")
    fun loadUsersByRegion(regions: List<String>): Flow<List<User>>
}
```

<br />

> [!NOTE]
> **Note:** Observable queries in Room have one important limitation: the query reruns whenever any row in the table is updated, regardless of whether that row is in the result set. You can ensure that the UI is only notified when the actual query results change by applying the `distinctUntilChanged` operator from the corresponding library: [Flow](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/distinct-until-changed), [RxJava](http://reactivex.io/documentation/operators/distinct), or [`LiveData`](https://developer.android.com/reference/androidx/lifecycle/Transformations#(androidx.lifecycle.LiveData).distinctUntilChanged()).

### Track database invalidation manually

When you need to build observable database operations manually, you can use the
[`createFlow`](https://developer.android.com/reference/kotlin/androidx/room3/InvalidationTracker#createFlow(kotlin.Array,kotlin.Boolean)) API of [`InvalidationTracker`](https://developer.android.com/reference/kotlin/androidx/room3/InvalidationTracker). This API lets you
create a `Flow` that tracks modifications to specific tables and emits a
notification whenever those tables change.


```kotlin
fun getArtistTours(db: RoomDatabase, from: Date, to: Date): Flow<Map<Artist, TourState>> {
    return db.invalidationTracker.createFlow("Artist").map { _ ->
        val artists = artistsDao.getAllArtists()
        val tours = tourService.fetchStates(artists.map { it.id })
        associateTours(artists, tours, from, to)
    }
}
```

<br />

By default, the returned `Flow` emits an initial value containing all the
registered tables to kick-start the stream. You can disable this behavior by
setting the `emitInitialState` parameter to `false`.

### Custom DAO return type converters

For types that aren't directly supported by Room or its extension libraries,
you can define custom DAO return type converters to support additional return
types. To transform the result of a DAO function into your custom type,
annotate a converter function with [`@DaoReturnTypeConverter`](https://developer.android.com/reference/kotlin/androidx/room3/DaoReturnTypeConverter).

For example, you can define a converter that uses `androidx.tracing` to add
trace sections around the execution of a query to monitor performance-sensitive
queries by wrapping the execution in a custom `TracedQuery` type:


```kotlin
class TracedQuery<T>(val result: T)

object TracingDaoReturnTypeConverter {
    @DaoReturnTypeConverter([OperationType.READ])
    suspend fun <T> convert(
        rawQuery: RoomRawQuery,
        executeAndConvert: suspend () -> T
    ): TracedQuery<T> {
        val result = trace("TracedQuery: ${rawQuery.sql}") {
            executeAndConvert()
        }
        return TracedQuery(result)
    }
}
```

<br />

To use the converter, annotate your database or DAO with
[`@DaoReturnTypeConverters`](https://developer.android.com/reference/kotlin/androidx/room3/DaoReturnTypeConverters):


```kotlin
@Dao
@DaoReturnTypeConverters(TracingDaoReturnTypeConverter::class)
interface MusicDao {
    @Query("SELECT * FROM Song")
    suspend fun getAllSongs(): TracedQuery<List<Song>>
}
```

<br />

#### Control DAO return type converter initialization

Ordinarily, Room handles instantiation of DAO return type converters.
However, if you must pass additional dependencies to your converter classes,
your app must directly control their initialization. If so, annotate your
converter class with [`@ProvidedDaoReturnTypeConverter`](https://developer.android.com/reference/kotlin/androidx/room3/ProvidedDaoReturnTypeConverter):


```kotlin
@ProvidedDaoReturnTypeConverter
class TracingDaoReturnTypeConverter(val tracer: Tracer) {
    @DaoReturnTypeConverter([OperationType.READ])
    suspend fun <T> convert(
        rawQuery: RoomRawQuery,
        executeAndConvert: suspend () -> T
    ): TracedQuery<T> {
        val result = tracer.trace("TracedQuery: ${rawQuery.sql}") {
            executeAndConvert()
        }
        return TracedQuery(result)
    }
}
```

<br />

Then, in addition to declaring your converter class in
`@DaoReturnTypeConverters`, use the
[`RoomDatabase.Builder.addDaoReturnTypeConverter`](https://developer.android.com/reference/kotlin/androidx/room3/RoomDatabase.Builder#addDaoReturnTypeConverter(kotlin.Any)) function to pass an
instance of your converter class to the `RoomDatabase` builder:


```kotlin
val db = Room.databaseBuilder<MyDatabase>(applicationContext, "database-name")
    .addDaoReturnTypeConverter(TracingDaoReturnTypeConverter(myLoggerInstance))
    .build()
```

<br />

#### Converter function requirements

A `@DaoReturnTypeConverter` function must meet several requirements:

- It must have a functional parameter as its last argument, usually named `executeAndConvert`. This parameter is a `suspend` lambda that Room generates to execute the query and parse the result.
  - If the converter needs to transform the query, such as Paging, the lambda can take a `RoomRawQuery` parameter.
- It can optionally accept the following parameters before the lambda:
  - **`db: RoomDatabase`**: Accesses the database instance, which is useful for obtaining the coroutine scope or performing additional operations.
  - **`tableNames: Array<String>`** or **`List<String>`**: Provides the names of the tables accessed by the query, which is useful for observable types.
  - **`rawQuery: RoomRawQuery`**: Provides the runtime instance of the query.
  - **`inTransaction: Boolean`**: Indicates whether the query is executing within a transaction.