---
title: https://developer.android.com/kotlin/multiplatform/sqlite
url: https://developer.android.com/kotlin/multiplatform/sqlite
source: md.txt
---

# Set up SQLite for KMP

The`androidx.sqlite`library contains abstract interfaces along with basic implementations which can be used to build your own libraries that access SQLite. You might want to consider using the[Room](https://developer.android.com/kotlin/multiplatform/room)library, which provides an abstraction layer over SQLite to allow for more robust database access while harnessing the full power of SQLite.

## Set up dependencies

To setup SQLite in your KMP project, add the dependencies for the artifacts in the`build.gradle.kts`file for your module:
**Note:** `androidx.sqlite`supports KMP in version 2.5.0 or higher.  

    [versions]
    sqlite = "2.6.2"

    [libraries]
    # The SQLite Driver interfaces
    androidx-sqlite = { module = "androidx.sqlite:sqlite", version.ref = "sqlite" }

    # The bundled SQLite driver implementation
    androidx-sqlite-bundled = { module = "androidx.sqlite:sqlite-bundled", version.ref = "sqlite" }

    [plugins]
    ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }

## SQLite Driver APIs

The`androidx.sqlite`library groups offer low-level APIs for communicating with the SQLite library either included in the library when using`androidx.sqlite:sqlite-bundled`or in the host platform, such as Android or iOS when using`androidx.sqlite:sqlite-framework`. The APIs closely follow the core functionality of SQLite C API.

There are 3 main interfaces:

- [`SQLiteDriver`](https://developer.android.com/reference/kotlin/androidx/sqlite/SQLiteDriver)- It is the entry point to use SQLite and is responsible for opening database connections.
- [`SQLiteConnection`](https://developer.android.com/reference/kotlin/androidx/sqlite/SQLiteConnection)- Is the representation of the`sqlite3`object.
- [`SQLiteStatement`](https://developer.android.com/reference/kotlin/androidx/sqlite/SQLiteStatement)- Is the representation of the`sqlite3_stmt`object.

The following example showcases the core APIs:  

    fun main() {
      val databaseConnection = BundledSQLiteDriver().open("todos.db")
      databaseConnection.execSQL(
        "CREATE TABLE IF NOT EXISTS Todo (id INTEGER PRIMARY KEY, content TEXT)"
      )
      databaseConnection.prepare(
        "INSERT OR IGNORE INTO Todo (id, content) VALUES (? ,?)"
      ).use { stmt ->
        stmt.bindInt(index = 1, value = 1)
        stmt.bindText(index = 2, value = "Try Room in the KMP project.")
        stmt.step()
      }
      databaseConnection.prepare("SELECT content FROM Todo").use { stmt ->
        while (stmt.step()) {
          println("Action item: ${stmt.getText(0)}")
        }
      }
      databaseConnection.close()
    }

Similar to SQLite C APIs the common usage is to:

- Open a database connection using the instantiated`SQLiteDriver`implementation.
- Prepare a SQL statement using`SQLiteConnection.prepare()`
- Execute a`SQLiteStatement`in the following way:
  1. Optionally bind arguments using the`bind*()`functions.
  2. Iterate over the result set using the`step()`function.
  3. Read columns from the result set using the`get*()`functions.

| **Caution:** Database connections and statements are resources that need to be managed. All prepared statements should be closed once they are no longer needed. Similarly if a database connection is no longer needed, then it should be closed.

### Driver Implementations

The following table summarizes the available driver implementations:

|-----------------------|------------------------------------|--------------------------------------------|
| Class Name            | Artifact                           | Supported Platforms                        |
| `AndroidSQLiteDriver` | `androidx.sqlite:sqlite-framework` | Android                                    |
| `NativeSQLiteDriver`  | `androidx.sqlite:sqlite-framework` | iOS, Mac, and Linux                        |
| `BundledSQLiteDriver` | `androidx.sqlite:sqlite-bundled`   | Android, iOS, Mac, Linux and JVM (Desktop) |

The recommended implementation to use is`BundledSQLiteDriver`available in`androidx.sqlite:sqlite-bundled`. It includes the SQLite library compiled from source, offering the most up-to-date version and consistency across all the supported KMP platforms.

### SQLite Driver and Room

The driver APIs are useful for low-level interactions with an SQLite database. For a feature rich library that provides a more robust access of SQLite then Room is recommended.

A`RoomDatabase`relies on a`SQLiteDriver`to perform database operations and an implementation is required to be configured using[`RoomDatabase.Builder.setDriver()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase#setDriver(androidx.sqlite.SQLiteDriver)). Room provides[`RoomDatabase.useReaderConnection`](https://developer.android.com/reference/kotlin/androidx/room/package-summary#(androidx.room.RoomDatabase).useReaderConnection(kotlin.coroutines.SuspendFunction1))and[`RoomDatabase.useWriterConnection`](https://developer.android.com/reference/kotlin/androidx/room/package-summary#(androidx.room.RoomDatabase).useWriterConnection(kotlin.coroutines.SuspendFunction1))for more direct access to the managed database connections.

## Migrate to Kotlin Multiplatform

Any usage of low-level Support SQLite API components (such as the`SupportSQLiteDatabase`interface) needs to be migrated to the equivalent SQLite Driver components.  

### Kotlin Multiplatform

Perform a transaction using low-level`SQLiteConnection`
**Note:** It is always recommended to use`RoomDatabase`transaction APIs as those allow nested transactions and are safer to use than the APIs available in`androidx.sqlite`.  

    val connection: SQLiteConnection = ...
    connection.execSQL("BEGIN IMMEDIATE TRANSACTION")
    try {
      // perform database operations in transaction
      connection.execSQL("END TRANSACTION")
    } catch(t: Throwable) {
      connection.execSQL("ROLLBACK TRANSACTION")
    }

Execute a query with no result  

    val connection: SQLiteConnection = ...
    connection.execSQL("ALTER TABLE ...")

Execute a query with result but no arguments  

    val connection: SQLiteConnection = ...
    connection.prepare("SELECT * FROM Pet").use { statement ->
      while (statement.step()) {
        // read columns
        statement.getInt(0)
        statement.getText(1)
      }
    }

Execute a query with result and arguments  

    connection.prepare("SELECT * FROM Pet WHERE id = ?").use { statement ->
      statement.bindInt(1, id)
      if (statement.step()) {
        // row found, read columns
      } else {
        // row not found
      }
    }

### Android-only

Perform a transaction using`SupportSQLiteDatabase`
**Note:** It is always recommended to use`RoomDatabase`transaction APIs as those allow nested transactions and are safer to use than the APIs available in`androidx.sqlite`.  

    val database: SupportSQLiteDatabase = ...
    database.beginTransaction()
    try {
      // perform database operations in transaction
      database.setTransactionSuccessful()
    } finally {
      database.endTransaction()
    }

Execute a query with no result  

    val database: SupportSQLiteDatabase = ...
    database.execSQL("ALTER TABLE ...")

Execute a query with result but no arguments  

    val database: SupportSQLiteDatabase = ...
    database.query("SELECT * FROM Pet").use { cursor ->
      while (cusor.moveToNext()) {
        // read columns
        cursor.getInt(0)
        cursor.getString(1)
      }
    }

Execute a query with result and arguments  

    database.query("SELECT * FROM Pet WHERE id = ?", id).use { cursor ->
      if (cursor.moveToNext()) {
        // row found, read columns
      } else {
        // row not found
      }
    }