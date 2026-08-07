---
title: https://developer.android.com/training/data-storage/room/defining-data
url: https://developer.android.com/training/data-storage/room/defining-data
source: md.txt
---

When you use the [Room persistence library](https://developer.android.com/training/data-storage/room) to store your app's data, you define entities to represent the objects that you want to store. Each entity corresponds to a table in the associated Room database, and each instance of an entity represents a row of data in the corresponding table.

Using Room entities lets you define your [database schema](https://www.sqlite.org/schematab.html) without writing any SQL code.

## Anatomy of an entity

You define each Room entity as a class annotated with [`@Entity`](https://developer.android.com/reference/kotlin/androidx/room3/Entity). A Room entity includes properties for each column in the corresponding table in the database, including one or more columns that make up the [primary key](https://developer.android.com/training/data-storage/room/defining-data#primary-key).

The following code is an example of an entity that defines a `User` table with columns for ID, first name, and last name:

<br />

```kotlin
@Entity
data class User(
    @PrimaryKey val id: Int,
    val firstName: String,
    val lastName: String
)
   
```

<br />

> [!NOTE]
> **Note:** To persist a property, Room needs access to it. To make sure Room has access to a property, either make it public or provide getter and setter functions for it.

By default, Room uses the class name as the database table name. If you want the table to have a different name, set the [`tableName`](https://developer.android.com/reference/kotlin/androidx/room3/Entity#tableName()) property of the `@Entity` annotation. Similarly, Room uses the property names as column names in the database by default. If you want a column to have a different name, add the [`@ColumnInfo`](https://developer.android.com/reference/kotlin/androidx/room3/ColumnInfo) annotation to the property and set the [`name`](https://developer.android.com/reference/kotlin/androidx/room3/ColumnInfo#name()) property. The following example shows custom names for a table and its columns:

<br />

```kotlin
@Entity(tableName = "users")
data class User(
    @PrimaryKey val id: Int,
    @ColumnInfo(name = "first_name") val firstName: String,
    @ColumnInfo(name = "last_name") val lastName: String
)
   
```

<br />

> [!NOTE]
> **Note:** Table and column names in SQLite are *case-insensitive*.

## Define a primary key

You must define a [primary key](https://learn.microsoft.com/en-us/sql/relational-databases/tables/create-primary-keys?view=sql-server-ver16) for each Room entity to uniquely identify each row in the corresponding database table. To do this, annotate a single column with [`@PrimaryKey`](https://developer.android.com/reference/kotlin/androidx/room3/PrimaryKey):

<br />

```kotlin
@PrimaryKey val id: Int
    
```

<br />

> [!NOTE]
> **Note:** If you need Room to assign automatic IDs to entity instances, set the [`autoGenerate`](https://developer.android.com/reference/kotlin/androidx/room3/PrimaryKey#autoGenerate()) property of `@PrimaryKey` to `true`.

### Define a composite primary key

If you need instances of an entity to be uniquely identified by a combination of multiple columns, you can define a *composite primary key* by listing those columns in the [`primaryKeys`](https://developer.android.com/reference/kotlin/androidx/room3/Entity#primaryKeys()) property of `@Entity`:

<br />

```kotlin
@Entity(primaryKeys = ["firstName", "lastName"])
data class User(
    val firstName: String,
    val lastName: String
)
   
```

<br />

## Ignore properties

By default, Room creates a column for each property defined in the entity. To prevent Room from persisting a property, annotate it with [`@Ignore`](https://developer.android.com/reference/kotlin/androidx/room3/Ignore):

<br />

```kotlin
@Entity
data class User(
    @PrimaryKey val id: Int,
    val firstName: String,
    val lastName: String,
    @Ignore val picture: Bitmap? = null
)
   
```

<br />

> [!NOTE]
> **Note:** If an ignored property is declared in the entity's primary constructor, you must provide a default value for it, such as `null`. This default value is necessary because Room ignores the property when creating the database table. However, Room still calls the primary constructor when instantiating the class from query results.

If an entity inherits properties from a parent entity, use the [`ignoredColumns`](https://developer.android.com/reference/kotlin/androidx/room3/Entity#ignoredColumns()) property of the `@Entity` annotation:

<br />

```kotlin
open class User {
    var picture: Bitmap? = null
}

@Entity(ignoredColumns = ["picture"])
data class RemoteUser(
    @PrimaryKey val id: Int,
    val hasVpn: Boolean
) : User()
   
```

<br />

## Provide table search support

Room supports several annotations that let you search for details in your database tables.

### Support full-text search

If your app requires fast full-text search (FTS), back your entities with a virtual table. Use the [FTS3 or FTS4 SQLite extension](https://www.sqlite.org/fts3.html) or the [FTS5 SQLite extension](https://www.sqlite.org/fts5.html).

To use this capability, add the [`@Fts3`](https://developer.android.com/reference/kotlin/androidx/room3/Fts3), [`@Fts4`](https://developer.android.com/reference/kotlin/androidx/room3/Fts4), or [`@Fts5`](https://developer.android.com/reference/kotlin/androidx/room3/Fts5) annotation to an entity.

<br />

```kotlin
// Use `@Fts3` only if your app has strict disk space requirements.
@Fts4
@Entity(tableName = "users")
data class User(
    // Specifying a primary key for an FTS-table-backed entity is optional,
    // but if you include one, it must an INTEGER type and column name "rowid".
    @PrimaryKey @ColumnInfo(name = "rowid") val id: Long,
    @ColumnInfo(name = "first_name") val firstName: String
)
   
```

<br />

> [!NOTE]
> **Note:** FTS-enabled tables always use a primary key of type `INTEGER` and with the column name `"rowid"`. If your FTS-table-backed entity defines a primary key, it *must* use that type and column name.

To customize how database information is tokenized in FTS tables, use the `tokenizer` option. Room provides several built-in tokenizers through [`FtsOptions`](https://developer.android.com/reference/kotlin/androidx/room3/FtsOptions), including `TOKENIZER_SIMPLE`, `TOKENIZER_PORTER`, and `TOKENIZER_UNICODE61`:

<br />

```kotlin
@Fts4(tokenizer = FtsOptions.TOKENIZER_UNICODE61)
@Entity(tableName = "users")
data class User(
    @PrimaryKey @ColumnInfo(name = "rowid") val id: Long,
    @ColumnInfo(name = "first_name") val firstName: String
)
   
```

<br />

Room provides several other options for defining FTS-backed entities, including result ordering, removing indexes from columns, and tables managed as external content. For more information about these options, see the [`FtsOptions`](https://developer.android.com/reference/kotlin/androidx/room3/FtsOptions) reference.

### Index specific columns

If you're using [`AndroidSQLiteDriver`](https://developer.android.com/reference/kotlin/androidx/sqlite/driver/AndroidSQLiteDriver) and you need to support SDK versions that don't support FTS3-, FTS4-, or FTS5-table-backed entities, you can still index certain columns in the database to speed up your queries. If you use [`BundledSQLiteDriver`](https://developer.android.com/reference/kotlin/androidx/sqlite/driver/bundled/BundledSQLiteDriver), Room supports all FTS versions regardless of the Android SDK version.

To add indexes to an entity, include the [`indices`](https://developer.android.com/reference/kotlin/androidx/room3/Entity#indices()) property in the [`@Entity`](https://developer.android.com/reference/kotlin/androidx/room3/Entity) annotation. List the column names to include in the index or composite index. The following code snippet shows how to add indexes:

<br />

```kotlin
@Entity(indices = [Index(value = ["last_name", "address"])])
data class User(
    @PrimaryKey val id: Int,
    @ColumnInfo(name = "first_name") val firstName: String,
    @ColumnInfo(name = "last_name") val lastName: String,
    val address: String?,
)
   
```

<br />

Sometimes, certain columns or groups of columns in a database need to contain unique values. To enforce this uniqueness, set the [`unique`](https://developer.android.com/reference/kotlin/androidx/room3#unique()) property of an [`@Index`](https://developer.android.com/reference/kotlin/androidx/room3) annotation to `true`. The following code sample shows how to enforce this uniqueness:

<br />

```kotlin
@Entity(indices = [Index(value = ["first_name", "last_name"], unique = true)])
data class User(
    @PrimaryKey val id: Int,
    @ColumnInfo(name = "first_name") val firstName: String,
    @ColumnInfo(name = "last_name") val lastName: String,
)
   
```

<br />