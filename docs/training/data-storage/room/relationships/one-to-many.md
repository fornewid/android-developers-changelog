---
title: https://developer.android.com/training/data-storage/room/relationships/one-to-many
url: https://developer.android.com/training/data-storage/room/relationships/one-to-many
source: md.txt
---

A *one-to-many relationship* between two entities is a relationship where each instance of the parent entity corresponds to zero or more instances of the child entity, but each instance of the child entity can only correspond to exactly one instance of the parent entity.

In the music streaming app example, suppose the user can organize their songs into playlists. Each user can create as many playlists as they want, but exactly one user creates each playlist. Therefore, there's a one-to-many relationship between the `User` entity and the `Playlist` entity.

Follow these steps to define and query one-to-many relationships in your database:

1. **[Define the relationship](https://developer.android.com/training/data-storage/room/relationships/one-to-many#define)**: Create classes for both entities, with the child entity referencing the parent's primary key.
2. **[Query the entities](https://developer.android.com/training/data-storage/room/relationships/one-to-many#query)**: Model the relationship in a new data class and implement a function to retrieve the related data.

## Define the relationship

To define a one-to-many relationship, first create a class for each entity. As in a one-to-one relationship, the child entity must include a variable that references the primary key of the parent entity.

<br />

```kotlin
@Entity
data class User(
    @PrimaryKey val userId: Long,
    val name: String,
    val age: Int
)

@Entity
data class Playlist(
    @PrimaryKey val playlistId: Long,
    val userCreatorId: Long,
    val playlistName: String
)
   
```

<br />

## Query the entities

To query the list of users and corresponding playlists, you must first model the one-to-many relationship between the two entities.

To model the relationship, create a new data class. Each instance of this class holds an instance of the parent entity and a list of all corresponding child entity instances. Add the [`@Relation`](https://developer.android.com/reference/kotlin/androidx/room3/Relation) annotation to the property that represents the list of child entities. Set [`parentColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#parentColumns()) to the name of the parent entity's primary key column, and set [`entityColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#entityColumns()) to the name of the child entity's column that references the parent entity's primary key.

<br />

```kotlin
data class UserWithPlaylists(
    @Embedded val user: User,
    @Relation(
        parentColumns = ["userId"],
        entityColumns = ["userCreatorId"]
    )
    val playlists: List<Playlist>
)
   
```

<br />

Finally, add a function to the data access object (DAO) class that returns all instances of the data class pairing the parent entity and the child entity. Add the [`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transaction) annotation so Room performs the entire operation atomically. This annotation is necessary because the function requires Room to run two queries.

<br />

```kotlin
@Transaction
@Query("SELECT * FROM User")
suspend fun getUsersWithPlaylists(): List<UserWithPlaylists>
    
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
data class Playlist(
    @PrimaryKey val playlistId: Long,
    val userFirstName: String,
    val userLastName: String,
    val playlistName: String
)

data class UserWithPlaylists(
    @Embedded val user: User,
    @Relation(
        parentColumns = ["firstName", "lastName"],
        entityColumns = ["userFirstName", "userLastName"]
    )
    val playlists: List<Playlist>
)
   
```

<br />