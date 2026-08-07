---
title: https://developer.android.com/training/data-storage/room/relationships/one-to-one
url: https://developer.android.com/training/data-storage/room/relationships/one-to-one
source: md.txt
---

A *one-to-one relationship* between two entities is a relationship where each instance of the parent entity corresponds to exactly one instance of the child entity, and the reverse is also true.

For example, consider a music streaming app where the user has a library of songs that they own. Each user has only one library, and each library corresponds to exactly one user. Therefore, there's a one-to-one relationship between the `User` entity and the `Library` entity.

Follow these steps to define and query one-to-one relationships in your database:

1. **[Define the relationship](https://developer.android.com/training/data-storage/room/relationships/one-to-one#define)**: Create classes for both entities, and ensure that one references the other's primary key.
2. **[Query the entities](https://developer.android.com/training/data-storage/room/relationships/one-to-one#query)**: Model the relationship in a new data class, and create a function to retrieve the related data.

## Define the relationship

To define a one-to-one relationship, first create a class for each of your two entities. One of the entities must include a variable that references the primary key of the other entity.

<br />

```kotlin
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

<br />

## Query the entities

To query the list of users and corresponding libraries, you must first model the one-to-one relationship between the two entities.

To model the relationship, create a new data class where each instance holds an instance of the parent entity and the corresponding child entity. Add the [`@Relation`](https://developer.android.com/reference/kotlin/androidx/room3/Relation) annotation to the child entity. Set [`parentColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#parentColumns()) to the name of the parent entity's primary key column, and set [`entityColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#entityColumns()) to the name of the child entity's column that references the parent's primary key.

<br />

```kotlin
data class UserAndLibrary(
    @Embedded val user: User,
    @Relation(
        parentColumns = ["userId"],
        entityColumns = ["userOwnerId"]
    )
    val library: Library
)
   
```

<br />

Finally, add a function to the data access object (DAO) class that returns all instances of the data class that pairs the parent entity with the child entity. Add the [`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transaction) annotation to ensure that Room performs the entire operation atomically, because this function requires Room to run two queries.

<br />

```kotlin
@Transaction
@Query("SELECT * FROM User")
suspend fun getUsersAndLibraries(): List<UserAndLibrary>
    
```

<br />

### Composite keys

If you define the relationship using composite keys, specify multiple columns in `parentColumns` and `entityColumns`. The order of columns in `parentColumns` must match the order of columns in `entityColumns`.

<br />

```kotlin
@Entity(primaryKeys = ["firstName", "lastName"])
data class User(
    val firstName: String,
    val lastName: String,
    val age: Int
)

@Entity
data class Library(
    @PrimaryKey val libraryId: Long,
    val userFirstName: String,
    val userLastName: String
)

data class UserAndLibrary(
    @Embedded val user: User,
    @Relation(
        parentColumns = ["firstName", "lastName"],
        entityColumns = ["userFirstName", "userLastName"]
    )
    val library: Library
)
   
```

<br />