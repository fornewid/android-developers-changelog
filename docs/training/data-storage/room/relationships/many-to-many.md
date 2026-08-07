---
title: https://developer.android.com/training/data-storage/room/relationships/many-to-many
url: https://developer.android.com/training/data-storage/room/relationships/many-to-many
source: md.txt
---

A *many-to-many relationship* between two entities is a relationship where each instance of the parent entity corresponds to zero or more instances of the child entity, and the reverse is also true.

In the music streaming app example, consider the songs in user-defined playlists. Each playlist can include many songs, and each song can belong to many playlists. Therefore, there's a many-to-many relationship between the `Playlist` and `Song` entities.

Follow these steps to define and query many-to-many relationships in your database:

1. **[Define the relationship](https://developer.android.com/training/data-storage/room/relationships/many-to-many#define)**: Establish the entities and the associative entity, or cross-reference table, to represent the many-to-many relationship.
2. **[Query the entities](https://developer.android.com/training/data-storage/room/relationships/many-to-many#query)**: Determine how you want to query the related entities, and create data classes to represent the intended output.

## Define the relationship

To define a many-to-many relationship, first create a class for each of your two entities. Many-to-many relationships are distinct from other relationship types because there's generally no reference to the parent entity in the child entity. Instead, create a third class to represent an [associative entity](https://en.wikipedia.org/wiki/Associative_entity), or *cross-reference table* , between the two entities. The cross-reference table must have columns for the primary key from each entity in the many-to-many relationship represented in the table. In this example, each row in the cross-reference table corresponds to a pairing of a `Playlist` instance and a `Song` instance where the referenced playlist includes the referenced song.

<br />

```kotlin
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

@Entity(primaryKeys = ["playlistId", "songId"], indices = [Index("playlistId", "songId")])
data class PlaylistSongCrossRef(
    val playlistId: Long,
    val songId: Long
)
   
```

<br />

## Query the entities

The next step depends on how you want to query these related entities.

- If you want to query *playlists* and a list of the corresponding *songs* for each playlist, create a new data class that contains a single `Playlist` object and a list of the `Song` objects that the playlist includes.
- If you want to query *songs* and a list of the corresponding *playlists* for each song, create a new data class that contains a single `Song` object and a list of the `Playlist` objects that include the song.

In either case, model the relationship between the entities by using the [`associateBy`](https://developer.android.com/reference/kotlin/androidx/room3/Relation#associateBy()) property in the [`@Relation`](https://developer.android.com/reference/kotlin/androidx/room3/Relation) annotation in each of these classes to identify the cross-reference entity providing the relationship between the `Playlist` entity and the `Song` entity.

<br />

```kotlin
data class PlaylistWithSongs(
    @Embedded val playlist: Playlist,
    @Relation(
        parentColumns = ["playlistId"],
        entityColumns = ["songId"],
        associateBy = Junction(PlaylistSongCrossRef::class)
    )
    val songs: List<Song>
)

data class SongWithPlaylists(
    @Embedded val song: Song,
    @Relation(
        parentColumns = ["songId"],
        entityColumns = ["playlistId"],
        associateBy = Junction(PlaylistSongCrossRef::class)
    )
    val playlists: List<Playlist>
)
   
```

<br />

Finally, add a function to the data access object (DAO) class to expose the query function your app needs.


`getPlaylistsWithSongs`
:
    Queries the database and returns all resulting `PlaylistWithSongs` objects.


`getSongsWithPlaylists`
:
    Queries the database and returns all resulting `SongWithPlaylists` objects.

Each function requires Room to run two queries. Add the [`@Transaction`](https://developer.android.com/reference/kotlin/androidx/room3/Transaction) annotation to both functions to ensure the operation runs atomically.

<br />

```kotlin
@Transaction
@Query("SELECT * FROM Playlist")
suspend fun getPlaylistsWithSongs(): List<PlaylistWithSongs>

@Transaction
@Query("SELECT * FROM Song")
suspend fun getSongsWithPlaylists(): List<SongWithPlaylists>
    
```

<br />

> [!NOTE]
> **Note:** If the `@Relation` annotation doesn't meet your specific use case, you might need to use the `JOIN` keyword in your SQL queries to manually define the appropriate relationships. For more information about querying multiple tables manually, see [Accessing data using Room DAOs](https://developer.android.com/training/data-storage/room/accessing-data#query-multiple-tables).

### Composite keys

If you define the relationship using composite keys, specify multiple columns in `parentColumns` and `entityColumns` of the `@Relation` annotation.

If you need to specify columns in the `Junction`, use `parentColumns` and `entityColumns` in the `Junction` annotation as well.

In the following example, `Playlist` has a composite primary key consisting of `playlistId` and `creatorId`. The cross-reference table `PlaylistSongCrossRef` also includes these columns to reference the playlist.

<br />

```kotlin
@Entity(primaryKeys = ["playlistId", "creatorId"])
data class Playlist(
    val playlistId: Long,
    val creatorId: Long,
    val playlistName: String
)

@Entity
data class Song(
    @PrimaryKey val songId: Long,
    val songName: String,
    val artist: String
)

@Entity(primaryKeys = ["playlistId", "creatorId", "songId"])
data class PlaylistSongCrossRef(
    val playlistId: Long,
    val creatorId: Long,
    val songId: Long
)

data class PlaylistWithSongs(
    @Embedded val playlist: Playlist,
    @Relation(
        parentColumns = ["playlistId", "creatorId"],
        entityColumns = ["songId"],
        associateBy = Junction(PlaylistSongCrossRef::class)
    )
    val songs: List<Song>
)
   
```

<br />