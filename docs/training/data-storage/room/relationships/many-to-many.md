---
title: https://developer.android.com/training/data-storage/room/relationships/many-to-many
url: https://developer.android.com/training/data-storage/room/relationships/many-to-many
source: md.txt
---

# Define and query many-to-many relationships

A*many-to-many relationship*between two entities is a relationship where each instance of the parent entity corresponds to zero or more instances of the child entity, and the reverse is also true.

In the music streaming app example, consider the songs in the user-defined playlists. Each playlist can include many songs, and each song can be a part of many different playlists. Therefore, there is a many-to-many relationship between the`Playlist`entity and the`Song`entity.

Follow these steps to define and query many-to-many relationships in your database:

1. **[Define the relationship](https://developer.android.com/training/data-storage/room/relationships/many-to-many#define)**: Establish the entities and the associative entity (cross-reference table) to represent the many-to-many relationship.
2. **[Query the entities](https://developer.android.com/training/data-storage/room/relationships/many-to-many#query)**: Determine how you want to query the related entities and create data classes to represent the intended output.

## Define the relationship

To define a many-to-many relationship, first create a class for each of your two entities. Many-to-many relationships are distinct from other relationship types because there is generally no reference to the parent entity in the child entity. Instead, create a third class to represent an[associative entity](https://en.wikipedia.org/wiki/Associative_entity), or*cross-reference table* , between the two entities. The cross-reference table must have columns for the primary key from each entity in the many-to-many relationship represented in the table. In this example, each row in the cross-reference table corresponds to a pairing of a`Playlist`instance and a`Song`instance where the referenced song is included in the referenced playlist.  

### Kotlin

    @Entity
    data class Playlist(
        @PrimaryKey val playlistId: Long,
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
    public class Playlist {
        @PrimaryKey public long playlistId;
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

## Query the entities

The next step depends on how you want to query these related entities.

- If you want to query*playlists* and a list of the corresponding*songs* for each playlist, create a new data class that contains a single`Playlist`object and a list of all of the`Song`objects that the playlist includes.
- If you want to query*songs* and a list of the corresponding*playlists* for each, create a new data class that contains a single`Song`object and a list of all of the`Playlist`objects in which the song is included.

In either case, model the relationship between the entities by using the[`associateBy`](https://developer.android.com/reference/kotlin/androidx/room/Relation#associateBy())property in the[`@Relation`](https://developer.android.com/reference/kotlin/androidx/room/Relation)annotation in each of these classes to identify the cross-reference entity providing the relationship between the`Playlist`entity and the`Song`entity.  

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

    data class SongWithPlaylists(
        @Embedded val song: Song,
        @Relation(
             parentColumn = "songId",
             entityColumn = "playlistId",
             associateBy = Junction(PlaylistSongCrossRef::class)
        )
        val playlists: List<Playlist>
    )

### Java

    public class PlaylistWithSongs {
        @Embedded public Playlist playlist;
        @Relation(
             parentColumn = "playlistId",
             entityColumn = "songId",
             associateBy = @Junction(PlaylistSongCrossref.class)
        )
        public List<Song> songs;
    }

    public class SongWithPlaylists {
        @Embedded public Song song;
        @Relation(
             parentColumn = "songId",
             entityColumn = "playlistId",
             associateBy = @Junction(PlaylistSongCrossref.class)
        )
        public List<Playlist> playlists;
    }

Finally, add a method to the DAO class to expose the query function your app needs.

- `getPlaylistsWithSongs`: this method queries the database and returns all the resulting`PlaylistWithSongs`objects.
- `getSongsWithPlaylists`: this method queries the database and returns all the resulting`SongWithPlaylists`objects.

These methods each require Room to run two queries, so add the[`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room/Transaction)annotation to both methods so that the whole operation is performed atomically.  

### Kotlin

    @Transaction
    @Query("SELECT * FROM Playlist")
    fun getPlaylistsWithSongs(): List<PlaylistWithSongs>

    @Transaction
    @Query("SELECT * FROM Song")
    fun getSongsWithPlaylists(): List<SongWithPlaylists>

### Java

    @Transaction
    @Query("SELECT * FROM Playlist")
    public List<PlaylistWithSongs> getPlaylistsWithSongs();

    @Transaction
    @Query("SELECT * FROM Song")
    public List<SongWithPlaylists> getSongsWithPlaylists();

| **Note:** If the`@Relation`annotation does not meet your specific use case, you might need to use the`JOIN`keyword in your SQL queries to manually define the appropriate relationships. To learn more about querying multiple tables manually, read[Accessing data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data#query-multiple-tables).