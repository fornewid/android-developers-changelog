---
title: https://developer.android.com/training/data-storage/sqlite
url: https://developer.android.com/training/data-storage/sqlite
source: md.txt
---

Saving data to a database is ideal for repeating or structured data,
such as contact information. This page assumes that you are
familiar with SQL databases in general and helps you get started with
SQLite databases on Android. The APIs you'll need to use a database
on Android are available in the [android.database.sqlite](https://developer.android.com/reference/android/database/sqlite/package-summary) package.  
**Caution:** Although these APIs are powerful, they are fairly low-level
and require a great deal of time and effort to use:

- There is no compile-time verification of raw SQL queries. As your data graph changes, you need to update the affected SQL queries manually. This process can be time consuming and error prone.
- You need to use lots of boilerplate code to convert between SQL queries and data objects.

For these reasons, we **highly recommended** using the
[Room Persistence Library](https://developer.android.com/training/basics/data-storage/room)
as an abstraction layer for accessing information in your app's SQLite
databases.

## Define a schema and contract

One of the main principles of SQL databases is the schema: a formal
declaration of how the database is organized. The schema is reflected in the SQL
statements that you use to create your database. You may find it helpful to
create a companion class, known as a *contract* class, which explicitly specifies
the layout of your schema in a systematic and self-documenting way.

A contract class is a container for constants that define names for URIs,
tables, and columns. The contract class allows you to use the same constants
across all the other classes in the same package. This lets you change a column
name in one place and have it propagate throughout your code.

A good way to organize a contract class is to put definitions that are
global to your whole database in the root level of the class. Then create an inner
class for each table. Each inner class enumerates the corresponding table's columns.

**Note:** By implementing the [BaseColumns](https://developer.android.com/reference/android/provider/BaseColumns)
interface, your inner class can inherit a primary
key field called `_ID` that some Android classes such as [CursorAdapter](https://developer.android.com/reference/android/widget/CursorAdapter) expect it to have. It's not required, but this can help your database
work harmoniously with the Android framework.

For example, the following contract defines the table name and column names for a
single table representing an RSS feed:  

### Kotlin

```kotlin
object FeedReaderContract {
    // Table contents are grouped together in an anonymous object.
    object FeedEntry : BaseColumns {
        const val TABLE_NAME = "entry"
        const val COLUMN_NAME_TITLE = "title"
        const val COLUMN_NAME_SUBTITLE = "subtitle"
    }
}
```

### Java

```java
public final class FeedReaderContract {
    // To prevent someone from accidentally instantiating the contract class,
    // make the constructor private.
    private FeedReaderContract() {}

    /* Inner class that defines the table contents */
    public static class FeedEntry implements BaseColumns {
        public static final String TABLE_NAME = "entry";
        public static final String COLUMN_NAME_TITLE = "title";
        public static final String COLUMN_NAME_SUBTITLE = "subtitle";
    }
}
```

## Create a database using an SQL helper

Once you have defined how your database looks, you should implement methods
that create and maintain the database and tables. Here are some typical
statements that create and delete a table:  

### Kotlin

```kotlin
private const val SQL_CREATE_ENTRIES =
        "CREATE TABLE ${FeedEntry.TABLE_NAME} (" +
                "${BaseColumns._ID} INTEGER PRIMARY KEY," +
                "${FeedEntry.COLUMN_NAME_TITLE} TEXT," +
                "${FeedEntry.COLUMN_NAME_SUBTITLE} TEXT)"

private const val SQL_DELETE_ENTRIES = "DROP TABLE IF EXISTS ${FeedEntry.TABLE_NAME}"
```

### Java

```java
private static final String SQL_CREATE_ENTRIES =
    "CREATE TABLE " + FeedEntry.TABLE_NAME + " (" +
    FeedEntry._ID + " INTEGER PRIMARY KEY," +
    FeedEntry.COLUMN_NAME_TITLE + " TEXT," +
    FeedEntry.COLUMN_NAME_SUBTITLE + " TEXT)";

private static final String SQL_DELETE_ENTRIES =
    "DROP TABLE IF EXISTS " + FeedEntry.TABLE_NAME;
```

Just like files that you save on the device's [internal
storage](https://developer.android.com/guide/topics/data/data-storage#filesInternal), Android stores your database in your app's private folder. Your data is
secure, because by default this area is not
accessible to other apps or the user.

The [SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper) class contains a useful
set of APIs for managing your database.
When you use this class to obtain references to your database, the system
performs the potentially
long-running operations of creating and updating the database only when
needed and *not during app startup* . All you need to do is call
[getWritableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getWritableDatabase()) or
[getReadableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getReadableDatabase()).

**Note:** Because they can be long-running,
be sure that you call [getWritableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getWritableDatabase()) or [getReadableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getReadableDatabase()) in a background thread.
See [Threading on Android](https://developer.android.com/training/multiple-threads) for more information.

To use [SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper), create a subclass that
overrides the [onCreate()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#onCreate(android.database.sqlite.SQLiteDatabase)) and
[onUpgrade()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#onUpgrade(android.database.sqlite.SQLiteDatabase, int, int)) callback methods. You may
also want to implement the
[onDowngrade()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#onDowngrade(android.database.sqlite.SQLiteDatabase, int, int)) or
[onOpen()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#onOpen(android.database.sqlite.SQLiteDatabase)) methods,
but they are not required.

For example, here's an implementation of [SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper) that
uses some of the commands shown above:  

### Kotlin

```kotlin
class FeedReaderDbHelper(context: Context) : SQLiteOpenHelper(context, DATABASE_NAME, null, DATABASE_VERSION) {
    override fun onCreate(db: SQLiteDatabase) {
        db.execSQL(SQL_CREATE_ENTRIES)
    }
    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        // This database is only a cache for online data, so its upgrade policy is
        // to simply to discard the data and start over
        db.execSQL(SQL_DELETE_ENTRIES)
        onCreate(db)
    }
    override fun onDowngrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        onUpgrade(db, oldVersion, newVersion)
    }
    companion object {
        // If you change the database schema, you must increment the database version.
        const val DATABASE_VERSION = 1
        const val DATABASE_NAME = "FeedReader.db"
    }
}
```

### Java

```java
public class FeedReaderDbHelper extends SQLiteOpenHelper {
    // If you change the database schema, you must increment the database version.
    public static final int DATABASE_VERSION = 1;
    public static final String DATABASE_NAME = "FeedReader.db";

    public FeedReaderDbHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(SQL_CREATE_ENTRIES);
    }
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // This database is only a cache for online data, so its upgrade policy is
        // to simply to discard the data and start over
        db.execSQL(SQL_DELETE_ENTRIES);
        onCreate(db);
    }
    public void onDowngrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        onUpgrade(db, oldVersion, newVersion);
    }
}
```

To access your database, instantiate your subclass of
[SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper):  

### Kotlin

```kotlin
val dbHelper = FeedReaderDbHelper(context)
```

### Java

```java
FeedReaderDbHelper dbHelper = new FeedReaderDbHelper(getContext());
```

## Put information into a database

Insert data into the database by passing a [ContentValues](https://developer.android.com/reference/android/content/ContentValues)
object to the [insert()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#insert(java.lang.String, java.lang.String, android.content.ContentValues)) method:  

### Kotlin

```kotlin
// Gets the data repository in write mode
val db = dbHelper.writableDatabase

// Create a new map of values, where column names are the keys
val values = ContentValues().apply {
    put(FeedEntry.COLUMN_NAME_TITLE, title)
    put(FeedEntry.COLUMN_NAME_SUBTITLE, subtitle)
}

// Insert the new row, returning the primary key value of the new row
val newRowId = db?.insert(FeedEntry.TABLE_NAME, null, values)
```

### Java

```java
// Gets the data repository in write mode
SQLiteDatabase db = dbHelper.getWritableDatabase();

// Create a new map of values, where column names are the keys
ContentValues values = new ContentValues();
values.put(FeedEntry.COLUMN_NAME_TITLE, title);
values.put(FeedEntry.COLUMN_NAME_SUBTITLE, subtitle);

// Insert the new row, returning the primary key value of the new row
long newRowId = db.insert(FeedEntry.TABLE_NAME, null, values);
```

The first argument for [insert()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#insert(java.lang.String, java.lang.String, android.content.ContentValues))
is simply the table name.

The second argument tells the framework what to do in the event that the
[ContentValues](https://developer.android.com/reference/android/content/ContentValues) is empty (i.e., you did not
[put](https://developer.android.com/reference/android/content/ContentValues#put(java.lang.String, byte[])) any values).
If you specify the name of a column, the framework inserts a row and sets
the value of that column to null. If you specify `null`, like in this
code sample, the framework does not insert a row when there are no values.


The [insert()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#insert(java.lang.String, java.lang.String, android.content.ContentValues)) methods returns the ID for the
newly created row, or it will return -1 if there was an error inserting the data. This can happen
if you have a conflict with pre-existing data in the database.

## Read information from a database

To read from a database, use the [query()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#query(java.lang.String, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String, java.lang.String, java.lang.String)) method, passing it your selection criteria and desired columns.
The method combines elements of [insert()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#insert(java.lang.String, java.lang.String, android.content.ContentValues))
and [update()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#update(java.lang.String, android.content.ContentValues, java.lang.String, java.lang.String[])), except the column list
defines the data you want to fetch (the "projection"), rather than the data to insert. The results
of the query are returned to you in a [Cursor](https://developer.android.com/reference/android/database/Cursor) object.  

### Kotlin

```kotlin
val db = dbHelper.readableDatabase

// Define a projection that specifies which columns from the database
// you will actually use after this query.
val projection = arrayOf(BaseColumns._ID, FeedEntry.COLUMN_NAME_TITLE, FeedEntry.COLUMN_NAME_SUBTITLE)

// Filter results WHERE "title" = 'My Title'
val selection = "${FeedEntry.COLUMN_NAME_TITLE} = ?"
val selectionArgs = arrayOf("My Title")

// How you want the results sorted in the resulting Cursor
val sortOrder = "${FeedEntry.COLUMN_NAME_SUBTITLE} DESC"

val cursor = db.query(
        FeedEntry.TABLE_NAME,   // The table to query
        projection,             // The array of columns to return (pass null to get all)
        selection,              // The columns for the WHERE clause
        selectionArgs,          // The values for the WHERE clause
        null,                   // don't group the rows
        null,                   // don't filter by row groups
        sortOrder               // The sort order
)
```

### Java

```java
SQLiteDatabase db = dbHelper.getReadableDatabase();

// Define a projection that specifies which columns from the database
// you will actually use after this query.
String[] projection = {
    BaseColumns._ID,
    FeedEntry.COLUMN_NAME_TITLE,
    FeedEntry.COLUMN_NAME_SUBTITLE
    };

// Filter results WHERE "title" = 'My Title'
String selection = FeedEntry.COLUMN_NAME_TITLE + " = ?";
String[] selectionArgs = { "My Title" };

// How you want the results sorted in the resulting Cursor
String sortOrder =
    FeedEntry.COLUMN_NAME_SUBTITLE + " DESC";

Cursor cursor = db.query(
    FeedEntry.TABLE_NAME,   // The table to query
    projection,             // The array of columns to return (pass null to get all)
    selection,              // The columns for the WHERE clause
    selectionArgs,          // The values for the WHERE clause
    null,                   // don't group the rows
    null,                   // don't filter by row groups
    sortOrder               // The sort order
    );
```

The third and fourth arguments (`selection` and `selectionArgs`) are
combined to create a WHERE clause. Because the arguments are provided separately from the selection
query, they are escaped before being combined. This makes your selection statements immune to SQL
injection. For more detail about all arguments, see the
[query()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#query(java.lang.String, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String, java.lang.String, java.lang.String)) reference.

To look at a row in the cursor, use one of the [Cursor](https://developer.android.com/reference/android/database/Cursor) move
methods, which you must always call before you begin reading values. Since the cursor starts at
position -1, calling [moveToNext()](https://developer.android.com/reference/android/database/Cursor#moveToNext()) places the "read position" on the
first entry in the results and returns whether or not the cursor is already past the last entry in
the result set. For each row, you can read a column's value by calling one of the
[Cursor](https://developer.android.com/reference/android/database/Cursor) get methods, such as [getString()](https://developer.android.com/reference/android/database/Cursor#getString(int)) or [getLong()](https://developer.android.com/reference/android/database/Cursor#getLong(int)). For each of the get methods,
you must pass the index position of the column you desire, which you can get by calling
[getColumnIndex()](https://developer.android.com/reference/android/database/Cursor#getColumnIndex(java.lang.String)) or
[getColumnIndexOrThrow()](https://developer.android.com/reference/android/database/Cursor#getColumnIndexOrThrow(java.lang.String)). When finished
iterating through results, call [close()](https://developer.android.com/reference/android/database/Cursor#close()) on the cursor
to release its resources.
For example, the following shows how to get all the item IDs stored in a cursor
and add them to a list:  

### Kotlin

```kotlin
val itemIds = mutableListOf<Long>()
with(cursor) {
    while (moveToNext()) {
        val itemId = getLong(getColumnIndexOrThrow(BaseColumns._ID))
        itemIds.add(itemId)
    }
}
cursor.close()
```

### Java

```java
List itemIds = new ArrayList<>();
while(cursor.moveToNext()) {
  long itemId = cursor.getLong(
      cursor.getColumnIndexOrThrow(FeedEntry._ID));
  itemIds.add(itemId);
}
cursor.close();
```

## Delete information from a database

To delete rows from a table, you need to provide selection criteria that
identify the rows to the [delete()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#delete(java.lang.String, java.lang.String, java.lang.String[])) method. The
mechanism works the same as the selection arguments to the
[query()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#query(boolean, java.lang.String, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String, java.lang.String, java.lang.String, java.lang.String)) method. It divides the
selection specification into a selection clause and selection arguments. The
clause defines the columns to look at, and also allows you to combine column
tests. The arguments are values to test against that are bound into the clause.
Because the result isn't handled the same as a regular SQL statement, it is
immune to SQL injection.  

### Kotlin

```kotlin
// Define 'where' part of query.
val selection = "${FeedEntry.COLUMN_NAME_TITLE} LIKE ?"
// Specify arguments in placeholder order.
val selectionArgs = arrayOf("MyTitle")
// Issue SQL statement.
val deletedRows = db.delete(FeedEntry.TABLE_NAME, selection, selectionArgs)
```

### Java

```java
// Define 'where' part of query.
String selection = FeedEntry.COLUMN_NAME_TITLE + " LIKE ?";
// Specify arguments in placeholder order.
String[] selectionArgs = { "MyTitle" };
// Issue SQL statement.
int deletedRows = db.delete(FeedEntry.TABLE_NAME, selection, selectionArgs);
```


The return value for the [delete()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#delete(java.lang.String, java.lang.String, java.lang.String[])) method
indicates the number of rows that were deleted from the database.

## Update a database

When you need to modify a subset of your database values, use the
[update()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#update(java.lang.String, android.content.ContentValues, java.lang.String, java.lang.String[])) method.

Updating the table combines the [ContentValues](https://developer.android.com/reference/android/content/ContentValues) syntax of
[insert()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#insert(java.lang.String, java.lang.String, android.content.ContentValues)) with the `WHERE` syntax
of [delete()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#delete(java.lang.String, java.lang.String, java.lang.String[])).  

### Kotlin

```kotlin
val db = dbHelper.writableDatabase

// New value for one column
val title = "MyNewTitle"
val values = ContentValues().apply {
    put(FeedEntry.COLUMN_NAME_TITLE, title)
}

// Which row to update, based on the title
val selection = "${FeedEntry.COLUMN_NAME_TITLE} LIKE ?"
val selectionArgs = arrayOf("MyOldTitle")
val count = db.update(
        FeedEntry.TABLE_NAME,
        values,
        selection,
        selectionArgs)
```

### Java

```java
SQLiteDatabase db = dbHelper.getWritableDatabase();

// New value for one column
String title = "MyNewTitle";
ContentValues values = new ContentValues();
values.put(FeedEntry.COLUMN_NAME_TITLE, title);

// Which row to update, based on the title
String selection = FeedEntry.COLUMN_NAME_TITLE + " LIKE ?";
String[] selectionArgs = { "MyOldTitle" };

int count = db.update(
    FeedReaderDbHelper.FeedEntry.TABLE_NAME,
    values,
    selection,
    selectionArgs);
```


The return value of the [update()](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#update(java.lang.String, android.content.ContentValues, java.lang.String, java.lang.String[])) method is
the number of rows affected in the database.

## Persisting database connection

Since [getWritableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getWritableDatabase())
and [getReadableDatabase()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#getReadableDatabase()) are
expensive to call when the database is closed, you should leave your database connection
open for as long as you possibly need to access it. Typically, it is optimal to close the database
in the [onDestroy()](https://developer.android.com/reference/android/app/Activity#onDestroy()) of the calling Activity.  

### Kotlin

```kotlin
override fun onDestroy() {
    dbHelper.close()
    super.onDestroy()
}
```

### Java

```java
@Override
protected void onDestroy() {
    dbHelper.close();
    super.onDestroy();
}
```

## Debug your database

The Android SDK includes a `sqlite3` shell tool that allows you to browse
table contents, run SQL commands, and perform other useful functions on SQLite
databases. For more information, see how to [how to issue shell commands](https://developer.android.com/studio/command-line/adb#shellcommands).