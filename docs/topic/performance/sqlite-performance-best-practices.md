---
title: https://developer.android.com/topic/performance/sqlite-performance-best-practices
url: https://developer.android.com/topic/performance/sqlite-performance-best-practices
source: md.txt
---

# Best practices for SQLite performance

Android offers[built-in support for SQLite](https://developer.android.com/training/data-storage/sqlite), an efficient SQL database. Follow these best practices to optimize your app's performance, ensuring it remains fast and predictably fast as your data grows. By using these best practices, you also reduce the possibility of encountering performance issues that are difficult to reproduce and troubleshoot.

To achieve faster performance, follow these performance principles:

- **Read fewer rows and columns**: Optimize your queries to retrieve only the necessary data. Minimize the amount of data read from the database, because excess data retrieval can impact performance.

- **Push work to SQLite engine**: Perform computations, filtering, and sorting operations within the SQL queries. Using SQLite's query engine can significantly improve performance.

- **Modify the database schema**: Design your database schema to help SQLite construct efficient query plans and data representations. Properly index tables and optimize table structures to enhance performance.

Additionally, you can use the available troubleshooting tools to measure the performance of your SQLite database to help identify areas that require optimization.

We recommend using the[Jetpack Room library](https://developer.android.com/training/data-storage/room).

## Configure the database for performance

Follow the steps in this section to configure your database for optimal performance in SQLite.

### Enable Write-Ahead Logging

SQLite implements mutations by appending them to a log, which it occasionally compacts into the database. This is called[Write-Ahead Logging (WAL)](https://www.sqlite.org/wal.html).

[Enable WAL](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#enableWriteAheadLogging())unless you are using[`ATTACH
DATABASE`](https://www.sqlite.org/lang_attach.html).

### Relax the synchronization mode

When using WAL, by default every commit issues an`fsync`to help ensure that the data reaches the disk. This improves data durability but slows down your commits.

SQLite has an option to[control synchronous mode](https://sqlite.org/pragma.html#pragma_synchronous). If you enable WAL, set synchronous mode to`NORMAL`:  

### Kotlin

```kotlin
// When opening the database
val paramsBuilder: SQLiteDatabase.OpenParams.Builder = SQLiteDatabase.OpenParams.Builder()
paramsBuilder.journalMode = SQLiteDatabase.SYNC_MODE_NORMAL

// Or: after having opened the database
db.execSQL("PRAGMA synchronous = NORMAL");
```

### Java

```java
// When opening the database
SQLiteDatabase.OpenParams.Builder paramsBuilder = new SQLiteDatabase.OpenParams.Builder();
paramsBuilder.setJournalMode(SQLiteDatabase.SYNC_MODE_NORMAL);

// Or: after having opened the database
db.execSQL("PRAGMA synchronous = NORMAL");
```

In this setting, a commit can return before the data is stored in a disk. If a device shutdown occurs, such as on loss of power or a kernel panic, the committed data might be lost. However, because of logging, your database isn't corrupted.

If only your app crashes, your data still reaches the disk. For most apps, this setting yields performance improvements at no material cost.
| **Note:** If your app has multiple databases, use the same synchronous setting everywhere in case there are data dependencies between different databases.

## Define efficient table schemas

To optimize performance and minimize data consumption, define an efficient table schema. SQLite constructs efficient query plans and data, leading to faster data retrieval. This section provides best practices for creating table schemas.

### Consider`INTEGER PRIMARY KEY`

For this example, define and populate a table as follows:  

    CREATE TABLE Customers(
      id INTEGER,
      name TEXT,
      city TEXT
    );
    INSERT INTO Customers Values(456, 'John Lennon', 'Liverpool, England');
    INSERT INTO Customers Values(123, 'Michael Jackson', 'Gary, IN');
    INSERT INTO Customers Values(789, 'Dolly Parton', 'Sevier County, TN');

The table output is as follows:

| rowid | id  |      name       |        city        |
|-------|-----|-----------------|--------------------|
| 1     | 456 | John Lennon     | Liverpool, England |
| 2     | 123 | Michael Jackson | Gary, IN           |
| 3     | 789 | Dolly Parton    | Sevier County, TN  |

The column[`rowid`](https://www.sqlite.org/rowidtable.html)is an index that preserves insertion order. Queries that filter by`rowid`are implemented as a fast B-tree search, but queries that filter by`id`are a slow table scan.

If you plan on doing lookups by`id`, you can avoid storing the`rowid`column for less data in storage and an overall faster database:  

    CREATE TABLE Customers(
      id INTEGER PRIMARY KEY,
      name TEXT,
      city TEXT
    );

Your table now looks as follows:

| id  |      name       |        city        |
|-----|-----------------|--------------------|
| 123 | Michael Jackson | Gary, IN           |
| 456 | John Lennon     | Liverpool, England |
| 789 | Dolly Parton    | Sevier County, TN  |

Since you don't need to store the`rowid`column,`id`queries are fast. Note that the table is now sorted based on`id`instead of insertion order.

### Accelerate queries with indexes

SQLite uses[indexes](https://www.sqlite.org/queryplanner.html#_lookup_by_index)to accelerate queries. When filtering (`WHERE`), sorting (`ORDER BY`), or aggregating (`GROUP BY`) a column, if the table has an index for the column, the query is accelerated.

In the previous example, filtering by`city`requires scanning the entire table:  

    SELECT id, name
    WHERE city = 'London, England';

For an app with a lot of city queries, you can accelerate those queries with an index:  

    CREATE INDEX city_index ON Customers(city);

An index is implemented as an additional table, sorted by the index column and mapped to`rowid`:

|        city        | rowid |
|--------------------|-------|
| Gary, IN           | 2     |
| Liverpool, England | 1     |
| Sevier County, TN  | 3     |

Note that the storage cost of the`city`column is now double, because it's now present in both the original table and the index. Since you are using the index, the cost of added storage is worth the benefit of faster queries. However, don't maintain an index that you're not using to avoid paying the storage cost for no query performance gain.

### Create multi-column indexes

If your queries combine multiple columns, you can create[multi-column indexes](https://www.sqlite.org/queryplanner.html#_multi_column_indices)to fully accelerate the query. You can also use an index on an outside column and let the inside search be done as a linear scan.

For instance, given the following query:  

    SELECT id, name
    WHERE city = 'London, England'
    ORDER BY city, name

You can accelerate the query with a multi-column index in the same order as specified in the query:  

    CREATE INDEX city_name_index ON Customers(city, name);

However, if you only have an index on`city`, the outside ordering is still accelerated, while the inside ordering requires a linear scan.

This also works with prefix inquiries. For example, an index`ON Customers (city, name)`also accelerates filtering, ordering, and grouping by`city`, since the index table for a multi-column index is ordered by the given indexes in the given order.

### Consider`WITHOUT ROWID`

By default, SQLite creates a`rowid`column for your table, where`rowid`is an implicit`INTEGER PRIMARY KEY AUTOINCREMENT`. If you already have a column that is`INTEGER PRIMARY KEY`, then this column becomes an alias of`rowid`.

For tables that have a primary key other than`INTEGER`or a composite of columns, consider[`WITHOUT
ROWID`](https://www.sqlite.org/withoutrowid.html).
| **Warning:** Tables using`WITHOUT ROWID`can incur performance penalties if their primary keys are large. For more information, see the[use cases](https://www.sqlite.org/withoutrowid.html#when_to_use_without_rowid).

### Store small data as a`BLOB`and large data as a file

If you want to associate large data with a row, such as a thumbnail of an image or a photo for a contact, you can store the data either in a`BLOB`column or in a file, and then store the file path in the column.

Files are generally rounded up to 4 KB increments. For very small files, where the rounding error is significant, it's more efficient to store them in the database as a`BLOB`. SQLite minimizes filesystem calls and is[faster than the underlying filesystem](https://www.sqlite.org/fasterthanfs.html)in some cases.
| **Note:** On Android, consider using a file for any data that is several multiples of 4 KB.

## Improve query performance

Follow these best practices to improve query performance in SQLite by minimizing response times and maximizing processing efficiency.
| **Note:** Many of the examples on this page include a`LIMIT`clause. This is good practice because queries that could return many rows have performance implications when returning large data sets. The exception to this is for queries that implicitly return a size constrained dataset. For example, searching on a field defined as`UNIQUE`can only return zero or one row.

### Read only the rows you need

Filters let you narrow down your results by specifying certain criteria, such as date range, location, or name. Limits let you control the number of results you see:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT name
    FROM Customers
    LIMIT 10;
    """.trimIndent(),
    null
).use { cursor ->
    while (cursor.moveToNext()) {
        // Process cursor data
    }
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT name
    FROM Customers
    LIMIT 10;
    """, null)) {
  while (cursor.moveToNext()) {
    // Process cursor data
  }
}
```

### Read only the columns you need

Avoid selecting unneeded columns, which can slow down your queries and waste resources. Instead, only select columns that are used.

In the following example, you select`id`,`name`, and`phone`:  

### Kotlin

```kotlin
// This is not the most efficient way of doing this.
// See the following example for a better approach.

db.rawQuery(
    """
    SELECT id, name, phone
    FROM customers;
    """.trimIndent(),
    null
).use { cursor ->
    while (cursor.moveToNext()) {
        val name = cursor.getString(1)
        // Further processing
    }
}
```

### Java

```java
// This is not the most efficient way of doing this.
// See the following example for a better approach.

try (Cursor cursor = db.rawQuery("""
    SELECT id, name, phone
    FROM customers;
    """, null)) {
  while (cursor.moveToNext()) {
    String name = cursor.getString(1);
    // Further processing
  }
}
```

However, you only need the`name`column:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT name
    FROM Customers;
    """.trimIndent(),
    null
).use { cursor ->
    while (cursor.moveToNext()) {
        val name = cursor.getString(0)
        // Further processing
    }
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT name
    FROM Customers;
    """, null)) {
  while (cursor.moveToNext()) {
    String name = cursor.getString(0);
    // Further processing
  }
}
```

### Parameterize queries

Your query string might include a parameter that is only known at runtime, such as the following:  

### Kotlin

```kotlin
fun getNameById(id: Long): String? 
    db.rawQuery(
        "SELECT name FROM customers WHERE id=$id", null
    ).use { cursor ->
        return if (cursor.moveToFirst()) {
            cursor.getString(0)
        } else {
            null
        }
    }
}
```

### Java

```java
@Nullable
public String getNameById(long id) {
  try (Cursor cursor = db.rawQuery(
      "SELECT name FROM customers WHERE id=" + id, null)) {
    if (cursor.moveToFirst()) {
      return cursor.getString(0);
    } else {
      return null;
    }
  }
}
```

In the preceding code, every query constructs a different string, and thus doesn't benefit from the statement cache. Each call requires SQLite to compile it before it can execute. Instead, you can replace the`id`argument with a[parameter](https://www.sqlite.org/lang_expr.html#varparam)and bind the value with`selectionArgs`:  

### Kotlin

```kotlin
fun getNameById(id: Long): String? {
    db.rawQuery(
        """
          SELECT name
          FROM customers
          WHERE id=?
        """.trimIndent(), arrayOf(id.toString())
    ).use { cursor ->
        return if (cursor.moveToFirst()) {
            cursor.getString(0)
        } else {
            null
        }
    }
}
```

### Java

```java
@Nullable
public String getNameById(long id) {
  try (Cursor cursor = db.rawQuery("""
          SELECT name
          FROM customers
          WHERE id=?
      """, new String[] {String.valueOf(id)})) {
    if (cursor.moveToFirst()) {
      return cursor.getString(0);
    } else {
      return null;
    }
  }
}
```

Now the query can be compiled once and cached. The compiled query is reused between different invocations of`getNameById(long)`.
| **Caution:** If the input argument is some other object less constrained than just a number, string concatenation might lead to a SQL injection security vulnerability. Always use parameters for variables or untrusted data.

### Iterate in SQL, not in code

Use a single query that returns all targeted results, instead of a programmatic loop iterating on SQL queries to return individual results. The programmatic loop is about 1000 times slower than a single SQL query.

### Use`DISTINCT`for unique values

Using the`DISTINCT`keyword can improve the performance of your queries by reducing the amount of data that needs to be processed. For example, if you want to return only the unique values from a column, use`DISTINCT`:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT DISTINCT name
    FROM Customers;
    """.trimIndent(),
    null
).use { cursor ->
    while (cursor.moveToNext()) {
        // Only iterate over distinct names in Kotlin
        // Process distinct name
    }
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT DISTINCT name
    FROM Customers;
    """, null)) {
  while (cursor.moveToNext()) {
    // Only iterate over distinct names in Java
    // Process distinct name
  }
}
```

### Use aggregate functions whenever possible

Use aggregate functions for aggregate results without row data. For example, the following code checks whether there is at least one matching row:  

### Kotlin

```kotlin
// This is not the most efficient way of doing this.
// See the following example for a better approach.

db.rawQuery("""
    SELECT id, name
    FROM Customers
    WHERE city = 'Paris';
    """.trimIndent(),
    null
).use { cursor ->
    if (cursor.moveToFirst()) {
        // At least one customer from Paris
        // Handle found
    } else {
        // No customers from Paris
        // Handle not found
}
```

### Java

```java
// This is not the most efficient way of doing this.
// See the following example for a better approach.

try (Cursor cursor = db.rawQuery("""
    SELECT id, name
    FROM Customers
    WHERE city = 'Paris';
    """, null)) {
  if (cursor.moveToFirst()) {
    // At least one customer from Paris
    // Handle found
  } else {
    // No customers from Paris
    // Handle not found
  }
}
```

To only fetch the first row, you can use`EXISTS()`to return`0`if a matching row does not exist and`1`if one or more rows match:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT EXISTS (
        SELECT null
        FROM Customers
        WHERE city = 'Paris';
    );
    """.trimIndent(),
    null
).use { cursor ->
    if (cursor.moveToFirst() && cursor.getInt(0) == 1) {
        // At least one customer from Paris
        // Handle found
    } else {
        // No customers from Paris
        // Handle not found
    }
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT EXISTS (
      SELECT null
      FROM Customers
      WHERE city = 'Paris'
    );
    """, null)) {
  if (cursor.moveToFirst() && cursor.getInt(0) == 1) {
    // At least one customer from Paris
    // Handle found
  } else {
    // No customers from Paris
    // Handle not found
  }
}
```

Use[SQLite aggregate functions](https://www.sqlite.org/lang_aggfunc.html)in your app code:

- `COUNT`: counts how many rows are in a column.
- `SUM`: adds all numerical values in a column.
- `MIN`or`MAX`: determines the lowest or highest value. Works for numeric columns,`DATE`types, and text types.
- `AVG`: finds the average numerical value.
- `GROUP_CONCAT`: concatenates strings with an optional separator.

### Use`COUNT()`instead of`Cursor.getCount()`

In the following example, the[`Cursor.getCount()`](https://developer.android.com/reference/android/database/Cursor#getCount())function reads all the rows from the database and returns all the row values:  

### Kotlin

```kotlin
// This is not the most efficient way of doing this.
// See the following example for a better approach.

db.rawQuery("""
    SELECT id
    FROM Customers;
    """.trimIndent(),
    null
).use { cursor ->
    val count = cursor.getCount()
    // Use count
}
```

### Java

```java
// This is not the most efficient way of doing this.
// See the following example for a better approach.

try (Cursor cursor = db.rawQuery("""
    SELECT id
    FROM Customers;
    """, null)) {
  int count = cursor.getCount();
  // Use count
}
```

However, by using`COUNT()`, the database returns only the count:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT COUNT(*)
    FROM Customers;
    """.trimIndent(),
    null
).use { cursor ->
    cursor.moveToFirst()
    val count = cursor.getInt(0)
    // Use count
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT COUNT(*)
    FROM Customers;
    """, null)) {
  cursor.moveToFirst();
  int count = cursor.getInt(0);
  // Use count
}
```

### Nest queries instead of code

SQL is composable and supports subqueries, joins, and foreign key constraints. You can use the result of one query in another query without going through app code. This reduces the need to copy data from SQLite and lets the database engine optimize your query.

In the following example, you can run a query to find which city has the most customers, then use the result in another query to find all the customers from that city:  

### Kotlin

```kotlin
// This is not the most efficient way of doing this.
// See the following example for a better approach.

db.rawQuery("""
    SELECT city
    FROM Customers
    GROUP BY city
    ORDER BY COUNT(*) DESC
    LIMIT 1;
    """.trimIndent(),
    null
).use { cursor ->
    if (cursor.moveToFirst()) {
        val topCity = cursor.getString(0)
        db.rawQuery("""
            SELECT name, city
            FROM Customers
            WHERE city = ?;
        """.trimIndent(),
        arrayOf(topCity)).use { innerCursor ->
            while (innerCursor.moveToNext()) {
                // Process inner cursor data
            }
        }
    }
}
```

### Java

```java
// This is not the most efficient way of doing this.
// See the following example for a better approach.

try (Cursor cursor = db.rawQuery("""
    SELECT city
    FROM Customers
    GROUP BY city
    ORDER BY COUNT(*) DESC
    LIMIT 1;
    """, null)) {
  if (cursor.moveToFirst()) {
    String topCity = cursor.getString(0);
    try (Cursor innerCursor = db.rawQuery("""
        SELECT name, city
        FROM Customers
        WHERE city = ?;
        """, new String[] {topCity})) {
        while (innerCursor.moveToNext()) {
          // Process inner cursor data
        }
    }
  }
}
```

To get the result in half the time of the previous example, use a single SQL query with nested statements:  

### Kotlin

```kotlin
db.rawQuery("""
    SELECT name, city
    FROM Customers
    WHERE city IN (
        SELECT city
        FROM Customers
        GROUP BY city
        ORDER BY COUNT (*) DESC
        LIMIT 1;
    );
    """.trimIndent(),
    null
).use { cursor ->
    if (cursor.moveToNext()) {
        // Process cursor data
    }
}
```

### Java

```java
try (Cursor cursor = db.rawQuery("""
    SELECT name, city
    FROM Customers
    WHERE city IN (
      SELECT city
      FROM Customers
      GROUP BY city
      ORDER BY COUNT(*) DESC
      LIMIT 1
    );
    """, null)) {
  while(cursor.moveToNext()) {
    // Process cursor data
  }
}
```

### Check uniqueness in SQL

If a row must not be inserted unless a particular column value is unique in the table, then it might be more efficient to enforce that uniqueness as a column constraint.

In the following example, one query is run to validate the row to be inserted and another to actually insert:  

### Kotlin

```kotlin
// This is not the most efficient way of doing this.
// See the following example for a better approach.

db.rawQuery(
    """
    SELECT EXISTS (
        SELECT null
        FROM customers
        WHERE username = ?
    );
    """.trimIndent(),
    arrayOf(customer.username)
).use { cursor ->
    if (cursor.moveToFirst() && cursor.getInt(0) == 1) {
        throw AddCustomerException(customer)
    }
}
db.execSQL(
    "INSERT INTO customers VALUES (?, ?, ?)",
    arrayOf(
        customer.id.toString(),
        customer.name,
        customer.username
    )
)
```

### Java

```java
// This is not the most efficient way of doing this.
// See the following example for a better approach.

try (Cursor cursor = db.rawQuery("""
    SELECT EXISTS (
      SELECT null
      FROM customers
      WHERE username = ?
    );
    """, new String[] { customer.username })) {
  if (cursor.moveToFirst() && cursor.getInt(0) == 1) {
    throw new AddCustomerException(customer);
  }
}
db.execSQL(
    "INSERT INTO customers VALUES (?, ?, ?)",
    new String[] {
      String.valueOf(customer.id),
      customer.name,
      customer.username,
    });
```

Instead of checking the unique constraint in Kotlin or Java, you can check it in SQL when you define the table:  

    CREATE TABLE Customers(
      id INTEGER PRIMARY KEY,
      name TEXT,
      username TEXT UNIQUE
    );

SQLite does the same as the following:  

    CREATE TABLE Customers(...);
    CREATE UNIQUE INDEX CustomersUsername ON Customers(username);

| **Note:** An index table is created for`username`, which uses extra storage. For more information about querying an index table, see[Accelerate queries with indexes](https://developer.android.com/topic/performance/sqlite-performance-best-practices#accelerate-queries).

Now you can insert a row and let SQLite check the constraint:  

### Kotlin

```kotlin
try {
    db.execSql(
        "INSERT INTO Customers VALUES (?, ?, ?)",
        arrayOf(customer.id.toString(), customer.name, customer.username)
    )
} catch(e: SQLiteConstraintException) {
    throw AddCustomerException(customer, e)
}
```

### Java

```java
try {
  db.execSQL(
      "INSERT INTO Customers VALUES (?, ?, ?)",
      new String[] {
        String.valueOf(customer.id),
        customer.name,
        customer.username,
      });
} catch (SQLiteConstraintException e) {
  throw new AddCustomerException(customer, e);
}
```
| **Note:** If you define[`INTEGER PRIMARY KEY`](https://developer.android.com/topic/performance/sqlite-performance-best-practices#consider-integer), then a unique constraint applies to that column and doesn't use an extra index table.

SQLite supports unique indexes with multiple columns:  

    CREATE TABLE table(...);
    CREATE UNIQUE INDEX unique_table ON table(column1, column2, ...);

SQLite validates constraints faster and with less overhead than Kotlin or Java code. It is a best practice to use SQLite rather than app code.

### Batch multiple insertions in a single transaction

A transaction commits multiple operations, which improves not only efficiency but also correctness. To improve data consistency and accelerate performance, you can batch insertions:  

### Kotlin

```kotlin
db.beginTransaction()
try {
    customers.forEach { customer ->
        db.execSql(
            "INSERT INTO Customers VALUES (?, ?, ?)",
            arrayOf(customer.id.toString(), customer.name, "customerValue")
        )
    }
} finally {
    db.endTransaction()
}
```

### Java

```java
db.beginTransaction();
try {
  for (customer : Customers) {
    db.execSQL(
        "INSERT INTO Customers VALUES (?, ?, ?)",
        new String[] {
          String.valueOf(customer.id),
          customer.name,
          "customerValue"
        });
  }
} finally {
  db.endTransaction()
}
```
| **Note:** Only one write transaction can occur at a time. Use`MoreExecutors.newSequentialExecutor(Executor)`to serialize writes.

## Use troubleshooting tools

SQLite provides the following troubleshooting tools to help measure performance.

### Use SQLite's interactive prompt

Run SQLite on your machine to run queries and learn. Different Android platform versions use different revisions of SQLite. To use the same engine that's on an Android-powered device, use`adb shell`and run`sqlite3`on your target device.

You can ask SQLite to time queries:  

    sqlite> .timer on
    sqlite> SELECT ...
    Run Time: real ... user ... sys ...

### `EXPLAIN QUERY PLAN`

You can ask SQLite to explain how it intends to answer a query by using[`EXPLAIN QUERY PLAN`](https://www.sqlite.org/eqp.html):  

    sqlite> EXPLAIN QUERY PLAN
    SELECT id, name
    FROM Customers
    WHERE city = 'Paris';
    QUERY PLAN
    `--SCAN Customers

The previous example requires a full table scan without an index to find all customers from Paris. This is called*linear complexity*. SQLite needs to read all the rows and only keep the rows that match customers from Paris. To fix this, you can add an index:  

    sqlite> CREATE INDEX Idx1 ON Customers(city);
    sqlite> EXPLAIN QUERY PLAN
    SELECT id, name
    FROM Customers
    WHERE city = 'Paris';
    QUERY PLAN
    `--SEARCH test USING INDEX Idx1 (city=?

If you're using the interactive shell, you can ask SQLite to always explain query plans:  

    sqlite> .eqp on

For more information, see[Query Planning](https://www.sqlite.org/queryplanner.html).

### SQLite Analyzer

SQLite offers the[`sqlite3_analyzer`](https://www.sqlite.org/sqlanalyze.html)command-line interface (CLI) to dump additional information that can be used to troubleshoot performance. To install, visit the[SQLite Download Page](https://sqlite.org/download.html).

You can use`adb pull`to download a database file from a target device to your workstation for analysis:  

    adb pull /data/data/<app_package_name>/databases/<db_name>.db

### SQLite Browser

You can also install the GUI tool[SQLite Browser](https://sqlitebrowser.org/)on the SQLite[Downloads page](https://sqlitebrowser.org/dl/).

### Android logging

Android times SQLite queries and logs them for you:  

    # Enable query time logging
    $ adb shell setprop log.tag.SQLiteTime VERBOSE
    # Disable query time logging
    $ adb shell setprop log.tag.SQLiteTime ERROR

### Perfetto tracing

When[configuring Perfetto](https://perfetto.dev/docs/concepts/config), you may add the following to include tracks for individual queries:  

    data_sources {
      config {
        name: "linux.ftrace"
        ftrace_config {
          atrace_categories: "database"
        }
      }
    }

### `dumpsys meminfo`

`adb shell dumpsys meminfo <package-name>`will print stats related to the app's memory usage, including some details about SQLite memory. For example, this was taken from the output of`adb shell dumpsys meminfo com.google.android.gms.persistent`on a developer's device:  

    DATABASES
          pgsz     dbsz   Lookaside(b) cache hits cache misses cache size  Dbname
    PER CONNECTION STATS
             4       52             45     8    41     6  /data/user/10/com.google.android.gms/databases/gaia-discovery
             4        8                    0     0     0    (attached) temp
             4       52             56     5    23     6  /data/user/10/com.google.android.gms/databases/gaia-discovery (1)
             4      252             95   233   124    12  /data/user_de/10/com.google.android.gms/databases/phenotype.db
             4        8                    0     0     0    (attached) temp
             4      252             17     0    17     1  /data/user_de/10/com.google.android.gms/databases/phenotype.db (1)
             4     9280            105 103169 69805    25  /data/user/10/com.google.android.gms/databases/phenotype.db
             4       20                    0     0     0    (attached) temp
             4     9280            108 13877  6394    25  /data/user/10/com.google.android.gms/databases/phenotype.db (2)
             4        8                    0     0     0    (attached) temp
             4     9280            105 12548  5519    25  /data/user/10/com.google.android.gms/databases/phenotype.db (3)
             4        8                    0     0     0    (attached) temp
             4     9280            107 18328  7886    25  /data/user/10/com.google.android.gms/databases/phenotype.db (1)
             4        8                    0     0     0    (attached) temp
             4       36             51   156    29     5  /data/user/10/com.google.android.gms/databases/mobstore_gc_db_v0
             4       36             97    47    27    10  /data/user/10/com.google.android.gms/databases/context_feature_default.db
             4       36             56     3    16     4  /data/user/10/com.google.android.gms/databases/context_feature_default.db (2)
             4      300             40  2111    24     5  /data/user/10/com.google.android.gms/databases/gservices.db
             4      300             39     3    17     4  /data/user/10/com.google.android.gms/databases/gservices.db (1)
             4       20             17     0    14     1  /data/user/10/com.google.android.gms/databases/gms.notifications.db
             4       20             33     1    15     2  /data/user/10/com.google.android.gms/databases/gms.notifications.db (1)
             4      120             40   143   163     4  /data/user/10/com.google.android.gms/databases/android_pay
             4      120            123    86    32    19  /data/user/10/com.google.android.gms/databases/android_pay (1)
             4       28             33     4    17     3  /data/user/10/com.google.android.gms/databases/googlesettings.db
    POOL STATS
         cache hits  cache misses    cache size  Dbname
                 13            68            81  /data/user/10/com.google.android.gms/databases/gaia-discovery
                233           145           378  /data/user_de/10/com.google.android.gms/databases/phenotype.db
             147921         89616        237537  /data/user/10/com.google.android.gms/databases/phenotype.db
                156            30           186  /data/user/10/com.google.android.gms/databases/mobstore_gc_db_v0
                 50            57           107  /data/user/10/com.google.android.gms/databases/context_feature_default.db
               2114            43          2157  /data/user/10/com.google.android.gms/databases/gservices.db
                  1            31            32  /data/user/10/com.google.android.gms/databases/gms.notifications.db
                229           197           426  /data/user/10/com.google.android.gms/databases/android_pay
                  4            18            22  /data/user/10/com.google.android.gms/databases/googlesettings.db

Under`DATABASES`you'll find:

- `pgsz`: the size of one database page, in KB.
- `dbsz`: the size of the entire database, in pages. To get the size in KB, multiply`pgsz`by`dbsz`.
- `Lookaside(b)`: memory allocated to the SQLite lookaside buffer per connection, in bytes. These are typically very small.
- `cache hits`: SQLite maintains a cache of database pages. This is the number of page cache hits (count).
- `cache misses`: number of page cache misses (count).
- `cache size`: number of pages in the cache (count). To get the size in KB, multiply this number by`pgsz`.
- `Dbname`: path to DB file. In our example some DBs have`(1)`or another number appended to their name, to indicate that there is more than one connection to the same underlying database. Stats are tracked per connection.

Under`POOL STATS`you'll find:

- `cache hits`: SQLite caches prepared statements and attempts to reuse them when running queries, to save some effort and memory in compiling SQL statements. This is the number of statement cache hits (count).
- `cache misses`: number of statement cache misses (count).
- `cache size`: starting with Android 17, this lists the total number of prepared statements in the cache. In earlier versions, this value is equivalent to the sum of hits and misses listed in the other two columns, and does not represent the cache size.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Run benchmarks in Continuous Integration](https://developer.android.com/topic/performance/benchmarking/benchmarking-in-ci)
- [Frozen frames](https://developer.android.com/topic/performance/vitals/frozen)
- [Create and measure Baseline Profiles without Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/manually-create-measure)