---
title: Best practices for SQLite performance (Views)  |  Android Developers
url: https://developer.android.com/topic/performance/views/sqlite-performance-best-practices-views
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Views](https://developer.android.com/develop/ui/views/layout/declaring-layout)
* [Guides](https://developer.android.com/topic/performance/views/benchmarking/macrobenchmark-control-app-views)

# Best practices for SQLite performance (Views) Stay organized with collections Save and categorize content based on your preferences.





[Concepts and Jetpack Compose implementationarrow\_forward](/topic/performance/sqlite-performance-best-practices)

Android offers [built-in support for SQLite](/training/data-storage/sqlite), an
efficient SQL database. Follow these best practices to optimize your app's
performance, ensuring it remains fast and predictably fast as your data grows.
By using these best practices, you also reduce the possibility of
encountering performance issues that are difficult to reproduce and
troubleshoot.

To achieve faster performance, follow these performance principles:

* **Read fewer rows and columns**: Optimize your queries to retrieve only the
  necessary data. Minimize the amount of data read from the database, because
  excess data retrieval can impact performance.
* **Push work to SQLite engine**: Perform computations, filtering, and sorting
  operations within the SQL queries. Using SQLite's query engine can significantly
  improve performance.
* **Modify the database schema**: Design your database schema to help SQLite
  construct efficient query plans and data representations. Properly index tables
  and optimize table structures to enhance performance.

Additionally, you can use the available troubleshooting tools to measure the
performance of your SQLite database to help identify areas that require
optimization.

We recommend using the [Jetpack Room library](/training/data-storage/room).

## Configure the database for performance

Follow the steps in this section to configure your database for optimal
performance in SQLite.

### Relax the synchronization mode

When using WAL, by default every commit issues an `fsync` to help ensure that
the data reaches the disk. This improves data durability but slows down your
commits.

SQLite has an option to [control synchronous mode](https://sqlite.org/pragma.html#pragma_synchronous). If you
enable WAL, set synchronous mode to `NORMAL`:

### Kotlin

```
// When opening the database
val paramsBuilder: SQLiteDatabase.OpenParams.Builder = SQLiteDatabase.OpenParams.Builder()
paramsBuilder.journalMode = SQLiteDatabase.SYNC_MODE_NORMAL

// Or: after having opened the database
db.execSQL("PRAGMA synchronous = NORMAL");
```

### Java

```
// When opening the database
SQLiteDatabase.OpenParams.Builder paramsBuilder = new SQLiteDatabase.OpenParams.Builder();
paramsBuilder.setJournalMode(SQLiteDatabase.SYNC_MODE_NORMAL);

// Or: after having opened the database
db.execSQL("PRAGMA synchronous = NORMAL");
```

In this setting, a commit can return before the data is stored in a disk. If a
device shutdown occurs, such as on loss of power or a kernel panic, the
committed data might be lost. However, because of logging, your database isn't
corrupted.

If only your app crashes, your data still reaches the disk. For most apps, this
setting yields performance improvements at no material cost.

**Note:** If your app has multiple databases, use the same synchronous setting
everywhere in case there are data dependencies between different databases.

## Improve query performance

Follow these best practices to improve query performance in SQLite by minimizing
response times and maximizing processing efficiency.

**Note:** Many of the examples on this page include a `LIMIT` clause. This is good
practice because queries that could return many rows have performance
implications when returning large data sets. The exception to this is for
queries that implicitly return a size constrained dataset. For example,
searching on a field defined as `UNIQUE` can only return zero or one row.

### Read only the rows you need

Filters let you narrow down your results by specifying certain criteria,
such as date range, location, or name. Limits let you control the number
of results you see:

### Kotlin

```
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

```
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

Avoid selecting unneeded columns, which can
slow down your queries and waste resources. Instead, only select columns
that are used.

In the following example, you select `id`, `name`, and `phone`:

### Kotlin

```
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

```
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

However, you only need the `name` column:

### Kotlin

```
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

```
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

Your query string might include a parameter that is only known at runtime, such
as the following:

### Kotlin

```
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

```
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

In the preceding code, every query constructs a different string, and thus
doesn't benefit from the statement cache. Each call requires SQLite to compile
it before it can execute. Instead, you can replace the `id` argument with a
[parameter](https://www.sqlite.org/lang_expr.html#varparam) and
bind the value with `selectionArgs`:

### Kotlin

```
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

```
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

Now the query can be compiled once and cached. The compiled query is reused
between different invocations of `getNameById(long)`.

**Caution:** If the input argument is some other object less constrained than just a
number, string concatenation might lead to a SQL injection security
vulnerability. Always use parameters for variables or untrusted data.

### Use `DISTINCT` for unique values

Using the `DISTINCT` keyword can improve the performance of your queries by
reducing the amount of data that needs to be processed. For example, if you want
to return only the unique values from a column, use `DISTINCT`:

### Kotlin

```
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

```
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

Use aggregate functions for aggregate results without row data. For example, the
following code checks whether there is at least one matching row:

### Kotlin

```
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

```
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

To only fetch the first row, you can use `EXISTS()` to return `0` if a matching
row does not exist and `1` if one or more rows match:

### Kotlin

```
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

```
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

Use [SQLite aggregate functions](https://www.sqlite.org/lang_aggfunc.html) in your app
code:

* `COUNT`: counts how many rows are in a column.
* `SUM`: adds all numerical values in a column.
* `MIN` or `MAX`: determines the lowest or highest value. Works for numeric
  columns,
  `DATE` types, and text types.
* `AVG`: finds the average numerical value.
* `GROUP_CONCAT`: concatenates strings with an optional separator.

### Use `COUNT()` instead of `Cursor.getCount()`

In the
following example, the
[`Cursor.getCount()`](/reference/android/database/Cursor#getCount()) function
reads all the rows from the database and returns all the row values:

### Kotlin

```
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

```
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

However, by using `COUNT()`, the database returns only the
count:

### Kotlin

```
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

```
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

SQL is composable and supports subqueries, joins, and foreign key constraints.
You can use the result of one query in another query without going through app
code. This reduces the need to copy data from SQLite and lets the database
engine optimize your query.

In the following example, you can run a query to find which city has the most
customers, then use the result in another query to find all the customers from
that city:

### Kotlin

```
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

```
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

To get the result in half the time of the previous example, use a single SQL
query with nested statements:

### Kotlin

```
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

```
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

If a row must not be inserted unless a particular column value is unique in the
table, then it might be more efficient to enforce that uniqueness as a column
constraint.

In the following example, one query is run to validate the row to be
inserted and another to actually insert:

### Kotlin

```
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

```
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

Instead of checking the unique constraint in Kotlin or Java, you can check it in
SQL when you define the table:

```
CREATE TABLE Customers(
  id INTEGER PRIMARY KEY,
  name TEXT,
  username TEXT UNIQUE
);
```

SQLite does the same as the following:

```
CREATE TABLE Customers(...);
CREATE UNIQUE INDEX CustomersUsername ON Customers(username);
```

**Note:** An index table is created for `username`, which uses extra storage. For
more information about querying an index table, see
[Accelerate queries with indexes](/topic/performance/sqlite-performance-best-practices#accelerate-queries).

Now you can insert a row and let SQLite check the constraint:

### Kotlin

```
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

```
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

**Note:** If you define [`INTEGER PRIMARY KEY`](/topic/performance/sqlite-performance-best-practices#consider-integer), then a unique
constraint applies to that column and doesn't use an extra index table.

SQLite supports unique indexes with multiple columns:

```
CREATE TABLE table(...);
CREATE UNIQUE INDEX unique_table ON table(column1, column2, ...);
```

SQLite validates constraints faster and with less overhead than Kotlin or Java
code. It is a best practice to use SQLite rather than app code.

### Batch multiple insertions in a single transaction

A transaction commits multiple operations, which improves not
only efficiency but also correctness. To improve data consistency and
accelerate performance, you can batch insertions:

### Kotlin

```
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

```
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

**Note:** Only one write transaction can occur at a time. Use
`MoreExecutors.newSequentialExecutor(Executor)` to serialize writes.


## Recommended for you

* Note: link text is displayed when JavaScript is off
* [Run benchmarks in Continuous Integration](/topic/performance/benchmarking/benchmarking-in-ci)
* [Frozen frames](/topic/performance/vitals/frozen)
* [Create and measure Baseline Profiles without Macrobenchmark](/topic/performance/baselineprofiles/manually-create-measure)