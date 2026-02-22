---
title: https://developer.android.com/training/data-storage/room/relationships/nested
url: https://developer.android.com/training/data-storage/room/relationships/nested
source: md.txt
---

# Define and query nested relationships

Sometimes, you might need to query a set of three or more tables that are all related to each other. In that case, you define*nested relationships*between the tables.
| **Caution:** Querying data with nested relationships requires Room to manipulate a large volume of data and can affect performance. Use as few nested relationships as possible in your queries.

Suppose that in the music streaming app example, you want to query all the users, all the playlists for each user, and all the songs in each playlist for each user. Users have a[one-to-many relationship](https://developer.android.com/training/data-storage/room/relationships/one-to-many)with playlists, and playlists have a[many-to-many relationship](https://developer.android.com/training/data-storage/room/relationships/many-to-many)with songs. The following code example shows the classes that represent these entities as well as the cross-reference table for the many-to-many relationship between playlists and songs:  

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

    @Entity
    data class Song(
        @PrimaryKey val songId: Long,
        val songName: String,
        val artist: String
    )

    @Entity(primaryKeys = ["playlistId", "songId"])
    data class PlaylistSongCrossRef(
        val playlistId: Long,
        val songId: Long
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
    @Entity
    public class Song {
        @PrimaryKey public long songId;
        public String songName;
        public String artist;
    }

    @Entity(primaryKeys = {"playlistId", "songId"})
    public class PlaylistSongCrossRef {
        public long playlistId;
        public long songId;
    }

First, model the relationship between two of the tables in your set as you normally do, using a data class and the[`@Relation`](https://developer.android.com/reference/kotlin/androidx/room/Relation)annotation. The following example shows a`PlaylistWithSongs`class that models a many-to-many relationship between the`Playlist`entity class and the`Song`entity class:  

### Kotlin

    data class PlaylistWithSongs(
        @Embedded val playlist: Playlist,
        @Relation(
             parentColumn = "playlistId",
             entityColumn = "songId",
             associateBy = Junction(PlaylistSongCrossRef::class)
        )
        val songs: List<Song>
    )

### Java

    public class PlaylistWithSongs {
        @Embedded public Playlist playlist;
        @Relation(
             parentColumn = "playlistId",
             entityColumn = "songId",
             associateBy = Junction(PlaylistSongCrossRef.class)
        )
        public List<Song> songs;
    }

After you define a data class that represents this relationship, create another data class that models the relationship between another table from your set and the first relationship class, "nesting" the existing relationship within the new one. The following example shows a`UserWithPlaylistsAndSongs`class that models a one-to-many relationship between the`User`entity class and the`PlaylistWithSongs`relationship class:  

### Kotlin

    data class UserWithPlaylistsAndSongs(
        @Embedded val user: User
        @Relation(
            entity = Playlist::class,
            parentColumn = "userId",
            entityColumn = "userCreatorId"
        )
        val playlists: List<PlaylistWithSongs>
    )

### Java

    public class UserWithPlaylistsAndSongs {
        @Embedded public User user;
        @Relation(
            entity = Playlist.class,
            parentColumn = "userId",
            entityColumn = "userCreatorId"
        )
        public List<PlaylistWithSongs> playlists;
    }

The`UserWithPlaylistsAndSongs`class indirectly models the relationships between all three of the entity classes:`User`,`Playlist`, and`Song`. This is illustrated in figure 1.
![UserWithPlaylistsAndSongs models the relationship between User and PlaylistWithSongs, which in turn models the relationship between Playlist and Song.](https://developer.android.com/static/images/training/data-storage/room_nested_relationships.png)**Figure 1.**Diagram of relationship classes in the music streaming app example.

If there are any more tables in your set, create a class to model the relationship between each remaining table and the relationship class that models the relationships between all previous tables. This creates a chain of nested relationships among all the tables that you want to query.

Finally, add a method to the DAO class to expose the query function that your app needs. This method requires Room to run multiple queries, so add the[`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room/Transaction)annotation so that the whole operation is performed atomically:  

### Kotlin

    @Transaction
    @Query("SELECT * FROM User")
    fun getUsersWithPlaylistsAndSongs(): List<UserWithPlaylistsAndSongs>

### Java

    @Transaction
    @Query("SELECT * FROM User")
    public List<UserWithPlaylistsAndSongs> getUsersWithPlaylistsAndSongs();