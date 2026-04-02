---
title: Define and query one-to-one relationships  |  App data and files  |  Android Developers
url: https://developer.android.com/training/data-storage/room/relationships/one-to-one
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [App data and files](https://developer.android.com/training/data-storage)

# Define and query one-to-one relationships Stay organized with collections Save and categorize content based on your preferences.




A *one-to-one relationship* between two entities is a relationship where each
instance of the parent entity corresponds to exactly one instance of the child
entity, and the reverse is also true.

For example, consider a music streaming app where the user has a library of
songs that they own. Each user has only one library, and each library
corresponds to exactly one user. Therefore, there is a one-to-one relationship
between the `User` entity and the `Library` entity.

Follow these steps to define and query one-to-one relationships in your
database:

1. **[Define the relationship](#define)**: Create classes for both entities,
   ensuring one references the other's primary key.
2. **[Query the entities](#query)**: Model the relationship in a new data class
   and create a method to retrieve the related data.

## Define the relationship

To define a one-to-one relationship, first create a class for each of your two
entities. One of the entities must include a variable that is a reference to the
primary key of the other entity.

### Kotlin

```
@Entity
data class User(
    @PrimaryKey val userId: Long,
    val name: String,
    val age: Int
)

@Entity
data class Library(
    @PrimaryKey val libraryId: Long,
    val userOwnerId: Long
)
```

### Java

```
@Entity
public class User {
    @PrimaryKey public long userId;
    public String name;
    public int age;
}

@Entity
public class Library {
    @PrimaryKey public long libraryId;
    public long userOwnerId;
}
```

## Query the entities

To query the list of users and corresponding libraries, you must first model the
one-to-one relationship between the two entities.

To do this, create a new data class where each instance holds an instance of the
parent entity and the corresponding instance of the child entity. Add the
[`@Relation`](/reference/kotlin/androidx/room/Relation) annotation to the instance of the child entity, with
[`parentColumn`](/reference/kotlin/androidx/room/Relation#parentcolumn()) set to the name of the primary key column of the parent
entity and [`entityColumn`](/reference/kotlin/androidx/room/Relation#entitycolumn()) set to the name of the column of the child entity
that references the parent entity's primary key.

### Kotlin

```
data class UserAndLibrary(
    @Embedded val user: User,
    @Relation(
         parentColumn = "userId",
         entityColumn = "userOwnerId"
    )
    val library: Library
)
```

### Java

```
public class UserAndLibrary {
    @Embedded public User user;
    @Relation(
         parentColumn = "userId",
         entityColumn = "userOwnerId"
    )
    public Library library;
}
```

Finally, add a method to the DAO class that returns all instances of the data
class that pairs the parent entity and the child entity. This method requires
Room to run two queries. You should therefore add the [`@Transaction`](/reference/kotlin/androidx/room/Transaction)
annotation to this method. This ensures that the whole operation runs
atomically.

### Kotlin

```
@Transaction
@Query("SELECT * FROM User")
fun getUsersAndLibraries(): List<UserAndLibrary>
```

### Java

```
@Transaction
@Query("SELECT * FROM User")
public List<UserAndLibrary> getUsersAndLibraries();
```