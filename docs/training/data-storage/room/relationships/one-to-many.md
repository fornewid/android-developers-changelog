---
title: https://developer.android.com/training/data-storage/room/relationships/one-to-many
url: https://developer.android.com/training/data-storage/room/relationships/one-to-many
source: md.txt
---

# Define and query one-to-many relationships

A*one-to-many relationship*between two entities is a relationship where each instance of the parent entity corresponds to zero or more instances of the child entity, but each instance of the child entity can only correspond to exactly one instance of the parent entity.

In the music streaming app example, suppose the user has the ability to organize their songs into playlists. Each user can create as many playlists as they want, but exactly one user creates each playlist. Therefore, there is a one-to-many relationship between the`User`entity and the`Playlist`entity.

Follow these steps to define and query one-to-many relationships in your database:

1. **[Define the relationship](https://developer.android.com/training/data-storage/room/relationships/one-to-many#define)**: Create classes for both entities, with the child entity referencing the parent's primary key.
2. **[Query the entities](https://developer.android.com/training/data-storage/room/relationships/one-to-many#query)**: Model the relationship in a new data class and implement a method to retrieve the related data.

## Define the relationship

To define a one-to-many relationship, first create a class for the two entities. As in a one-to-one relationship, the child entity must include a variable that is a reference to the primary key of the parent entity.  

### Kotlin

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

### Java

    @Entity
    public class User {
        @PrimaryKey public long userId;
        public String name;
        public int age;
    }

    @Entity
    public class Playlist {
        @PrimaryKey public long playlistId;
        public long userCreatorId;
        public String playlistName;
    }

## Query the entities

To query the list of users and corresponding playlists, you must first model the one-to-many relationship between the two entities

To do this, create a new data class where each instance holds an instance of the parent entity and a list of all corresponding child entity instances. Add the[`@Relation`](https://developer.android.com/reference/kotlin/androidx/room/Relation)annotation to the instance of the child entity, with[`parentColumn`](https://developer.android.com/reference/kotlin/androidx/room/Relation#parentColumn())set to the name of the primary key column of the parent entity and[`entityColumn`](https://developer.android.com/reference/kotlin/androidx/room/Relation#entityColumn())set to the name of the column of the child entity that references the parent entity's primary key.  

### Kotlin

    data class UserWithPlaylists(
        @Embedded val user: User,
        @Relation(
              parentColumn = "userId",
              entityColumn = "userCreatorId"
        )
        val playlists: List<Playlist>
    )

### Java

    public class UserWithPlaylists {
        @Embedded public User user;
        @Relation(
             parentColumn = "userId",
             entityColumn = "userCreatorId"
        )
        public List<Playlist> playlists;
    }

Finally, add a method to the DAO class that returns all instances of the data class that pairs the parent entity and the child entity. This method requires Room to run two queries, so add the[`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room/Transaction)annotation to this method so that the whole operation is performed atomically.  

### Kotlin

    @Transaction
    @Query("SELECT * FROM User")
    fun getUsersWithPlaylists(): List<UserWithPlaylists>

### Java

    @Transaction
    @Query("SELECT * FROM User")
    public List<UserWithPlaylists> getUsersWithPlaylists();