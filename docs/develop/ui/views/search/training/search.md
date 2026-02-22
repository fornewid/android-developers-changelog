---
title: https://developer.android.com/develop/ui/views/search/training/search
url: https://developer.android.com/develop/ui/views/search/training/search
source: md.txt
---

Try the Compose way  
Jetpack Compose is the recommended UI toolkit for Android. Learn how to add search functionality in Compose.  
[Filter a list →](https://developer.android.com/develop/ui/compose/quick-guides/content/filter-list-while-typing)  
![](https://developer.android.com/static/images/android-compose-ui-logo.png)

There are many ways to store your data, such as in an online database, in a local SQLite
database, or even in a text file. It is up to you to decide what is the best solution for your
application. This lesson shows you how to create a SQLite virtual table that can provide robust
full-text searching. The table is populated with data from a text file that contains a word and
definition pair on each line in the file.

## Create the Virtual Table

A virtual table behaves similarly to a SQLite table, but reads and writes to an object in
memory via callbacks, instead of to a database file. To create a virtual table, create a class
for the table:  

### Kotlin

```kotlin
class DatabaseTable(context: Context) {

    private val databaseOpenHelper = DatabaseOpenHelper(context)

}
```

### Java

```java
public class DatabaseTable {
    private final DatabaseOpenHelper databaseOpenHelper;

    public DatabaseTable(Context context) {
        databaseOpenHelper = new DatabaseOpenHelper(context);
    }
}
```

Create an inner class in `DatabaseTable` that extends [SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper). The [SQLiteOpenHelper](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper) class
defines abstract methods that you must override so that your database table can be created and
upgraded when necessary. For example, here is some code that declares a database table that will
contain words for a dictionary app:  

### Kotlin

```kotlin
private const val TAG = "DictionaryDatabase"

// The columns we'll include in the dictionary table
const val COL_WORD = "WORD"
const val COL_DEFINITION = "DEFINITION"

private const val DATABASE_NAME = "DICTIONARY"
private const val FTS_VIRTUAL_TABLE = "FTS"
private const val DATABASE_VERSION = 1

private const val FTS_TABLE_CREATE =
        "CREATE VIRTUAL TABLE $FTS_VIRTUAL_TABLE USING fts3 ($COL_WORD, $COL_DEFINITION)"

class DatabaseTable(context: Context) {

    private val databaseOpenHelper: DatabaseOpenHelper

    init {
        databaseOpenHelper = DatabaseOpenHelper(context)
    }

    private class DatabaseOpenHelper internal constructor(private val helperContext: Context) :
            SQLiteOpenHelper(helperContext, DATABASE_NAME, null, DATABASE_VERSION) {
        private lateinit var mDatabase: SQLiteDatabase

        override fun onCreate(db: SQLiteDatabase) {
            mDatabase = db
            mDatabase.execSQL(FTS_TABLE_CREATE)
        }

        override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
            Log.w(
                    TAG,
                    "Upgrading database from version $oldVersion to $newVersion , which will " +
                            "destroy all old data"
            )

            db.execSQL("DROP TABLE IF EXISTS $FTS_VIRTUAL_TABLE")
            onCreate(db)
        }

    }
}
```

### Java

```java
public class DatabaseTable {

    private static final String TAG = "DictionaryDatabase";

    // The columns we'll include in the dictionary table
    public static final String COL_WORD = "WORD";
    public static final String COL_DEFINITION = "DEFINITION";

    private static final String DATABASE_NAME = "DICTIONARY";
    private static final String FTS_VIRTUAL_TABLE = "FTS";
    private static final int DATABASE_VERSION = 1;

    private final DatabaseOpenHelper databaseOpenHelper;

    public DatabaseTable(Context context) {
        databaseOpenHelper = new DatabaseOpenHelper(context);
    }

    private static class DatabaseOpenHelper extends SQLiteOpenHelper {

        private final Context helperContext;
        private SQLiteDatabase mDatabase;

        private static final String FTS_TABLE_CREATE =
                    "CREATE VIRTUAL TABLE " + FTS_VIRTUAL_TABLE +
                    " USING fts3 (" +
                    COL_WORD + ", " +
                    COL_DEFINITION + ")";

        DatabaseOpenHelper(Context context) {
            super(context, DATABASE_NAME, null, DATABASE_VERSION);
            helperContext = context;
        }

        @Override
        public void onCreate(SQLiteDatabase db) {
            mDatabase = db;
            mDatabase.execSQL(FTS_TABLE_CREATE);
        }

        @Override
        public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
            Log.w(TAG, "Upgrading database from version " + oldVersion + " to "
                    + newVersion + ", which will destroy all old data");
            db.execSQL("DROP TABLE IF EXISTS " + FTS_VIRTUAL_TABLE);
            onCreate(db);
        }
    }
}
```

## Populate the Virtual Table

The table now needs data to store. The following code shows you how to read a text file
(located in `res/raw/definitions.txt`) that contains words and their definitions, how
to parse that file, and how to insert each line of that file as a row in the virtual table. This
is all done in another thread to prevent the UI from locking. Add the following code to your
`DatabaseOpenHelper` inner class.

**Tip:** You also might want to set up a callback to notify your UI
activity of this thread's completion.  

### Kotlin

```kotlin
private fun loadDictionary() {
    Thread(Runnable {
        try {
            loadWords()
        } catch (e: IOException) {
            throw RuntimeException(e)
        }
    }).start()
}

@Throws(IOException::class)
private fun loadWords() {
    val inputStream = helperContext.resources.openRawResource(R.raw.definitions)

    BufferedReader(InputStreamReader(inputStream)).use { reader ->
        var line: String? = reader.readLine()
        while (line != null) {
            val strings: List<String> = line.split("-").map { it.trim() }
            if (strings.size < 2) continue
            val id = addWord(strings[0], strings[1])
            if (id < 0) {
                Log.e(TAG, "unable to add word: ${strings[0]}")
            }
            line = reader.readLine()
        }
    }
}

fun addWord(word: String, definition: String): Long {
    val initialValues = ContentValues().apply {
        put(COL_WORD, word)
        put(COL_DEFINITION, definition)
    }

    return database.insert(FTS_VIRTUAL_TABLE, null, initialValues)
}
```

### Java

```java
private void loadDictionary() {
        new Thread(new Runnable() {
            public void run() {
                try {
                    loadWords();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }).start();
    }

private void loadWords() throws IOException {
    final Resources resources = helperContext.getResources();
    InputStream inputStream = resources.openRawResource(R.raw.definitions);
    BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

    try {
        String line;
        while ((line = reader.readLine()) != null) {
            String[] strings = TextUtils.split(line, "-");
            if (strings.length < 2) continue;
            long id = addWord(strings[0].trim(), strings[1].trim());
            if (id < 0) {
                Log.e(TAG, "unable to add word: " + strings[0].trim());
            }
        }
    } finally {
        reader.close();
    }
}

public long addWord(String word, String definition) {
    ContentValues initialValues = new ContentValues();
    initialValues.put(COL_WORD, word);
    initialValues.put(COL_DEFINITION, definition);

    return database.insert(FTS_VIRTUAL_TABLE, null, initialValues);
}
```

Call the `loadDictionary()` method wherever appropriate to populate the table. A
good place would be in the [onCreate()](https://developer.android.com/reference/android/database/sqlite/SQLiteOpenHelper#onCreate(android.database.sqlite.SQLiteDatabase))
method of the `DatabaseOpenHelper` class, right after you create the table:  

### Kotlin

```kotlin
override fun onCreate(db: SQLiteDatabase) {
    database = db
    database.execSQL(FTS_TABLE_CREATE)
    loadDictionary()
}
```

### Java

```java
@Override
public void onCreate(SQLiteDatabase db) {
    database = db;
    database.execSQL(FTS_TABLE_CREATE);
    loadDictionary();
}
```

## Search for the Query

When you have the virtual table created and populated, use the query supplied by your [SearchView](https://developer.android.com/reference/android/widget/SearchView) to search the data. Add the following methods to the
`DatabaseTable` class to build a SQL statement that searches for the query:  

### Kotlin

```kotlin
fun getWordMatches(query: String, columns: Array<String>?): Cursor? {
    val selection = "$COL_WORD MATCH ?"
    val selectionArgs = arrayOf("$query*")

    return query(selection, selectionArgs, columns)
}

private fun query(
        selection: String,
        selectionArgs: Array<String>,
        columns: Array<String>?
): Cursor? {
    val cursor: Cursor? = SQLiteQueryBuilder().run {
        tables = FTS_VIRTUAL_TABLE
        query(databaseOpenHelper.readableDatabase,
                columns, selection, selectionArgs, null, null, null)
    }

    return cursor?.run {
        if (!moveToFirst()) {
            close()
            null
        } else {
            this
        }
    } ?: null
}
```

### Java

```java
public Cursor getWordMatches(String query, String[] columns) {
    String selection = COL_WORD + " MATCH ?";
    String[] selectionArgs = new String[] {query+"*"};

    return query(selection, selectionArgs, columns);
}

private Cursor query(String selection, String[] selectionArgs, String[] columns) {
    SQLiteQueryBuilder builder = new SQLiteQueryBuilder();
    builder.setTables(FTS_VIRTUAL_TABLE);

    Cursor cursor = builder.query(databaseOpenHelper.getReadableDatabase(),
            columns, selection, selectionArgs, null, null, null);

    if (cursor == null) {
        return null;
    } else if (!cursor.moveToFirst()) {
        cursor.close();
        return null;
    }
    return cursor;
}
```

Search for a query by calling `getWordMatches()`. Any matching results are returned
in a [Cursor](https://developer.android.com/reference/android/database/Cursor) that you can iterate through or use to build a [ListView](https://developer.android.com/reference/android/widget/ListView).
This example calls `getWordMatches()` in the `handleIntent()` method of the searchable
activity. Remember that the searchable activity receives the query inside of the [ACTION_SEARCH](https://developer.android.com/reference/android/content/Intent#ACTION_SEARCH) intent as an extra, because of the intent filter that you
previously created:  

### Kotlin

```kotlin
private val db = DatabaseTable(this)

...

private fun handleIntent(intent: Intent) {

    if (Intent.ACTION_SEARCH == intent.action) {
        val query = intent.getStringExtra(SearchManager.QUERY)
        val c = db.getWordMatches(query, null)
        // process Cursor and display results
    }
}
```

### Java

```java
DatabaseTable db = new DatabaseTable(this);

...

private void handleIntent(Intent intent) {

    if (Intent.ACTION_SEARCH.equals(intent.getAction())) {
        String query = intent.getStringExtra(SearchManager.QUERY);
        Cursor c = db.getWordMatches(query, null);
        // process Cursor and display results
    }
}
```