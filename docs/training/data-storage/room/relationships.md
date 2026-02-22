---
title: https://developer.android.com/training/data-storage/room/relationships
url: https://developer.android.com/training/data-storage/room/relationships
source: md.txt
---

# Choose relationship types between objects

Because SQLite is a relational database, you can define relationships between entities. But while most object-relational mapping libraries let entity objects reference each other, Room explicitly forbids this. To learn about the technical reasoning behind this decision, see[Understand why Room doesn't allow object references](https://developer.android.com/training/data-storage/room/referencing-data#understand-no-object-references).

## Types of relationships

Room supports the following relationship types:

- [**One-to-one**](https://developer.android.com/training/data-storage/room/relationships/one-to-one): Represents a relationship where a single entity is related to another single entity.
- [**One-to-many**](https://developer.android.com/training/data-storage/room/relationships/one-to-many): Represents a relationship where a single entity can be related to multiple entities of another type.
- [**Many-to-many**](https://developer.android.com/training/data-storage/room/relationships/many-to-many): Represents a relationship where multiple entities of one type can be related to multiple entities of another type. This usually requires a junction table.
- [**Nested Relationships (using embedded objects)**](https://developer.android.com/training/data-storage/room/relationships/nested): Represents a relationship where an entity contains another entity as a field, and this nested entity can further contain other entities. This uses the`@Embedded`annotation.

## Choose between two approaches

In Room, there are two ways to define and query a relationship between entities. You can use either:

- An intermediate data class with embedded objects, or
- A relational query method with a multimap return type.

If you don't have a specific reason to use intermediate data classes, we recommend using the multimap return type approach. To learn more about this approach, see[Return a multimap](https://developer.android.com/training/data-storage/room/accessing-data#multimap).

The intermediate data class approach lets you avoid writing complex SQL queries, but it can also result in increased code complexity because it requires additional data classes. In short, the multimap return type approach requires your SQL queries to do more work, and the intermediate data class approach requires your code to do more work.

### Use the intermediate data class approach

In the intermediate data class approach, you define a data class that models the relationship between your Room entities. This data class holds the pairings between instances of one entity and instances of another entity as[embedded objects](https://developer.android.com/training/data-storage/room/relationships#nested-objects). Your query methods can then return instances of this data class for use in your app.

For example, you can define a`UserBook`data class to represent library users with specific books checked out, and define a query method to retrieve a list of`UserBook`instances from the database:  

### Kotlin

    @Dao
    interface UserBookDao {
        @Query(
            "SELECT user.name AS userName, book.name AS bookName " +
            "FROM user, book " +
            "WHERE user.id = book.user_id"
        )
        fun loadUserAndBookNames(): LiveData<List<UserBook>>
    }

    data class UserBook(val userName: String?, val bookName: String?)

### Java

    @Dao
    public interface UserBookDao {
       @Query("SELECT user.name AS userName, book.name AS bookName " +
              "FROM user, book " +
              "WHERE user.id = book.user_id")
       public LiveData<List<UserBook>> loadUserAndBookNames();
    }

    public class UserBook {
        public String userName;
        public String bookName;
    }

### Use the multimap return types approach

| **Note:** Room only supports multimap return types in version 2.4 and higher.

In the multimap return type approach, you don't need to define any additional data classes. Instead, you define a[multimap](https://en.wikipedia.org/wiki/Multimap)return type for your method based on the map structure that you want and define the relationship between your entities directly in your SQL query.

For example, the following query method returns a mapping of`User`and`Book`instances to represent library users with specific books checked out:  

### Kotlin

    @Query(
        "SELECT * FROM user" +
        "JOIN book ON user.id = book.user_id"
    )
    fun loadUserAndBookNames(): Map<User, List<Book>>

### Java

    @Query(
        "SELECT * FROM user" +
        "JOIN book ON user.id = book.user_id"
    )
    public Map<User, List<Book>> loadUserAndBookNames();

## Create embedded objects

Sometimes, you'd like to express an entity or data object as a cohesive whole in your database logic, even if the object contains several fields. In these situations, you can use the[`@Embedded`](https://developer.android.com/reference/androidx/room/Embedded)annotation to represent an object that you'd like to decompose into its subfields within a table. You can then query the embedded fields just as you do for other individual columns.

For example, your`User`class can include a field of type`Address`that represents a composition of fields named`street`,`city`,`state`, and`postCode`. To store the composed columns separately in the table, include an`Address`field. This should appear in the`User`class annotated with`@Embedded`. The following code snippet demonstrates this:  

### Kotlin

    data class Address(
        val street: String?,
        val state: String?,
        val city: String?,
        @ColumnInfo(name = "post_code") val postCode: Int
    )

    @Entity
    data class User(
        @PrimaryKey val id: Int,
        val firstName: String?,
        @Embedded val address: Address?
    )

### Java

    public class Address {
        public String street;
        public String state;
        public String city;

        @ColumnInfo(name = "post_code") public int postCode;
    }

    @Entity
    public class User {
        @PrimaryKey public int id;

        public String firstName;

        @Embedded public Address address;
    }

The table representing a`User`object then contains columns with the following names:`id`,`firstName`,`street`,`state`,`city`, and`post_code`.
| **Note:** Embedded fields can also include other embedded fields.

If an entity has multiple embedded fields of the same type, you can keep each column unique by setting the[`prefix`](https://developer.android.com/reference/androidx/room/Embedded#getPrefix())property. Room then adds the provided value to the beginning of each column name in the embedded object.

## Additional resources

To learn more about defining relationships between entities in Room, see the following additional resources.

### Videos

- [What's New in Room](https://www.youtube.com/watch?v=_aJsh6P00c0)(Android Dev Summit '19)

### Blogs

- [Database relations with Room](https://medium.com/androiddevelopers/database-relations-with-room-544ab95e4542)