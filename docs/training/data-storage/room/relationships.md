---
title: https://developer.android.com/training/data-storage/room/relationships
url: https://developer.android.com/training/data-storage/room/relationships
source: md.txt
---

Because SQLite is a relational database, you can define relationships between
entities. But while most object-relational mapping libraries let entity objects
reference each other, Room explicitly forbids this. To learn about the technical
reasoning behind this decision, see [Understand why Room doesn't allow object
references](https://developer.android.com/training/data-storage/room/referencing-data#understand-no-object-references).

## Types of relationships

Room supports the following relationship types:

- [**One-to-one**](https://developer.android.com/training/data-storage/room/relationships/one-to-one): Represents a relationship where a single entity is related to another single entity.
- [**One-to-many**](https://developer.android.com/training/data-storage/room/relationships/one-to-many): Represents a relationship where a single entity can be related to multiple entities of another type.
- [**Many-to-many**](https://developer.android.com/training/data-storage/room/relationships/many-to-many): Represents a relationship where multiple entities of one type can be related to multiple entities of another type. This usually requires a junction table.
- [**Nested relationships using embedded objects**](https://developer.android.com/training/data-storage/room/relationships/nested): Represents a relationship where an entity contains another entity as a property, and this nested entity can further contain other entities. This uses the `@Embedded` annotation.

## Choose between two approaches

In Room, there are two ways to define and query a relationship between entities.
You can use either:

- An intermediate data class with embedded objects, or
- A relational query function with a multimap return type.

If you don't have a specific reason to use intermediate data classes, we
recommend using the multimap return type approach. To learn more about this
approach, see [Return a multimap](https://developer.android.com/training/data-storage/room/accessing-data#multimap).

The intermediate data class approach lets you avoid writing complex SQL queries,
but it can also result in increased code complexity because it requires
additional data classes. In short, the multimap return type approach requires
your SQL queries to do more work, and the intermediate data class approach
requires your code to do more work.

### Use the intermediate data class approach

In the intermediate data class approach, you define a data class that models the
relationship between your Room entities. This data class holds the pairings
between instances of one entity and instances of another entity as [embedded
objects](https://developer.android.com/training/data-storage/room/relationships#nested-objects). Your query functions can then return instances of this data class
for use in your app.

For example, you can define a `UserBook` data class to represent library users
with specific books checked out, and define a query function to retrieve a list
of `UserBook` instances from the database:


```kotlin
@Dao
interface UserBookDao {
    @Query(
        """
        SELECT user.name AS userName, book.name AS bookName
        FROM user JOIN book ON user.id = book.user_id
        """
    )
    fun loadUserAndBookNames(): LiveData<List<UserBook>>
}

data class UserBook(val userName: String, val bookName: String)
```

<br />

### Use the multimap return type approach

In the multimap return type approach, you don't need to define any additional
data classes. Instead, you define a [multimap](https://en.wikipedia.org/wiki/Multimap) return type for
your function based on the map structure that you want and define the
relationship between your entities directly in your SQL query.

For example, the following query function returns a mapping of `User` and `Book`
instances to represent library users with specific books checked out:


```kotlin
@Query(
    """
    SELECT *
    FROM user JOIN book ON user.id = book.user_id
    """
)
suspend fun loadUserAndBookNames(): Map<User, List<Book>>
```

<br />

With multimap return types, you can also query one-to-one relationships that
don't involve another entity. The following query function returns a mapping of
`User` and the number of books they have checked out using the
[`@MapColumn`](https://developer.android.com/reference/kotlin/androidx/room3/MapColumn) annotation:


```kotlin
@Query(
    """
    SELECT user.*, COUNT(book.id) AS book_count
    FROM user LEFT JOIN book ON user.id = book.user_id
    GROUP BY user.id
    """
)
suspend fun loadUserAndBookCount(): Map<User, @MapColumn(columnName = "book_count") Int>
```

<br />

## Create embedded objects

Sometimes, you want to express an entity or data object as a cohesive whole in
your database logic, even if the object contains several properties. In these
situations, use the [`@Embedded`](https://developer.android.com/reference/kotlin/androidx/room3/Embedded) annotation to decompose an object into
its subproperties within a table. You can then query the embedded properties
just as you do for other columns.

For example, your `User` class can include an `Address` property that
represents a composition of `street`, `city`, `state`, and `postCode`
properties. To store the composed columns separately in the table, annotate
the `Address` property in the `User` class with `@Embedded`. The following
code snippet shows this setup:


```kotlin
data class Address(
    val street: String?,
    val state: String?,
    val city: String?,
    @ColumnInfo(name = "post_code") val postCode: Int
)

@Entity
data class User(
    @PrimaryKey val id: Int,
    val firstName: String,
    @Embedded val address: Address?
)
```

<br />

The table representing a `User` object then contains columns with the following
names: `id`, `firstName`, `street`, `state`, `city`, and `post_code`.

> [!NOTE]
> **Note:** Embedded properties can also include other embedded properties.

If an entity has multiple embedded properties of the same type, you can keep
each column unique by setting the [`prefix`](https://developer.android.com/reference/kotlin/androidx/room3/Embedded#prefix()) property. Room then adds the
provided value to the beginning of each column name in the embedded object.