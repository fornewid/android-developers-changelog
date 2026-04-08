---
title: https://developer.android.com/courses/extras/sql-primer
url: https://developer.android.com/courses/extras/sql-primer
source: md.txt
---

SQL primer

# SQLite primer

The[Developing Android Apps in Kotlin course](https://codelabs.developers.google.com/codelabs/kotlin-android-training-welcome/index.html?index=../..index#0)assumes that you are familiar with the following subjects:

- Databases in general
- SQL databases in particular
- The SQL language used to interact with databases

This page is a refresher and quick reference.

## SQL databases

SQL databases store data in tables of rows and columns:

- The intersection of a row and column is called a*field*.
- Fields contain data, references to other fields, or references to other tables.
- Each row contains one entity. The entity is identified by a unique ID which is usually used as its*primary key*.
- Each column is identified by a name that is unique per table.

## SQLite

SQLite implements an SQL database engine that has the following characteristics:

- Self-contained (requires no other components)
- Serverless (requires no server backend)
- Zero-configuration (does not need to be configured for your app)
- Transactional (the changes within a single transaction in SQLite either occur completely or not at all)

SQLite is the most widely deployed database engine in the world. The source code for SQLite is in the public domain. For details of the SQLite database, see the[SQLite website](https://www.sqlite.org/about.html).

### Example table

- A database named`DATABASE_NAME`
- A table named`WORD_LIST_TABLE`
- Columns for`_id`,`word`and`definition`

After inserting the words`alpha`and`beta`, where`alpha`has two definitions, the table might look like this:

DATABASE_NAME

| WORD_LIST_TABLE |         |                 |
|-----------------|---------|-----------------|
| _id             | word    | definition      |
| 1               | "alpha" | "first letter"  |
| 2               | "beta"  | "second letter" |
| 3               | "alpha" | "particle"      |

To find what's in a specific row, use the`_id`, or retrieve rows by formulating queries that select rows from the table by specifying constraints.

## Transactions

A*transaction*is a sequence of operations performed as a single logical unit of work. To qualify as a transaction, a logical unit of work must exhibit four properties: atomicity, consistency, isolation, and durability (ACID):

- **Atomicity.**Either all of a transaction's data modifications are performed, or none of the modifications are performed. Atomicity is true even if a program crash, operating-system crash, or power failure interrupts the act of writing the change to the disk.
- **Consistency.**When a transaction is completed, the transaction must leave all data in a consistent state.
- **Isolation.**Modifications made by concurrent transactions must be isolated from modifications made by concurrent transactions. A transaction either recognizes data in the state the data was in before another concurrent transaction modified it, or the transaction recognizes the data after the second transaction has completed. The transaction does not recognize an intermediate state.
- **Durability.**After a transaction has completed, its effects are permanently in place in the system. The modifications persist even in the event of a system failure.

Examples of transactions:

- Transferring money from a savings account to a checking account.
- Entering a term and definition into dictionary.
- Committing a changelist to the master branch.

For more on transactions, see[Atomic Commit In SQLite](https://www.sqlite.org/atomiccommit.html).

## Query language

You use the SQL query language to interact with the database. Queries can be very complex, but there are four basic operations:

- Inserting rows
- Deleting rows
- Updating values in rows
- Retrieving rows that meet given criteria

On Android, the data access object (DAO) provides convenience methods for inserting, deleting, and updating the database. For a full description of the query language, see[SQL As Understood By SQLite](https://www.sqlite.org/lang.html).

### Query structure

An SQL query is highly structured. Sample query:

- `SELECT word`*,*`definition FROM WORD_LIST_TABLE WHERE
  word="alpha"`

Generic version of the sample query:

- `SELECT`*columns* `FROM`*table* `WHERE`*column="value"*

Parts of the sample query:

- `SELECT`*columns* : Select the columns to return. Use`*`to return all columns.
- `FROM`*table*: Specify the table from which to get results.
- `WHERE`: Optional keyword that precedes conditions that have to be met, for example*column="value"* . Common operators are`=`,`LIKE`,`<`, and`>`. To connect multiple conditions, use`AND`or`OR`.

Other parts of queries:

- `ORDER BY`: Optional key phrase for ordering results by a column. Specify`ASC`for ascending and`DESC`for descending. If you don't specify an order, you get the default order, which might be unordered.
- `LIMIT`: Keyword to specify a limited number of results.

### Sample queries and results

The following queries use the previously defined table:

|                         SELECT \* FROM WORD_LIST_TABLE                         |                                                                                          Gets all the rows in`WORD_LIST_TABLE`table.                                                                                          |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SELECT word, definition FROM WORD_LIST_TABLE WHERE _id \> 2                    | Selects the`word`and`definition`columns of all items with an`id`greater than 2. Returns \[\["alpha", "particle"\]\]                                                                                                           |
| SELECT _id FROM WORD_LIST_TABLE WHERE word="alpha" AND definition LIKE "%art%" | Returns the`id`of the word`alpha`with the substring`art`in the definition. \[\["3"\]\]                                                                                                                                        |
| SELECT definition FROM WORD_LIST_TABLE ORDER BY word DESC LIMIT 1              | Selects all definitions. Sorts in reverse and gets the first row after the list is sorted. Sorting is by the column specified which is`word`. Note that we can sort by a column that we don't return! \[\["second letter"\]\] |
| SELECT \* FROM WORD_LIST_TABLE LIMIT 2,1                                       | Returns 1 item starting at position 2. Position counting starts at 1 (not zero!). Returns`[["2", "beta", "second letter"]]`                                                                                                   |

You can practice creating and querying databases at this[SQL Fiddle website](http://sqlfiddle.com/).

## Queries for Android SQLite

You can send queries to the SQLite database of the Android system as raw queries or as parameters.

The[rawQuery(String
sql, String[] selectionArgs)](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase#rawQuery(java.lang.String,%20java.lang.String[]))method runs the provided SQL. The method returns a[Cursor](https://developer.android.com/reference/android/database/Cursor)of the result set. The following table shows how the first two sample queries from above would look as raw queries:

| 1 |                                        String query = "SELECT \* FROM WORD_LIST_TABLE"; rawQuery(query, null);                                         |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2 | query = "SELECT word, definition FROM WORD_LIST_TABLE WHERE _id\> ? "; String\[\] selectionArgs = new String\[\]{"2"} rawQuery(query, selectionArgs) ; |

The[query(String
table, String[] columns, String selection, String[] selectionArgs, String
groupBy, String having, String orderBy, String limit)](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html#query(java.lang.String,%20java.lang.String[],%20java.lang.String,%20java.lang.String[],%20java.lang.String,%20java.lang.String,%20java.lang.String,%20java.lang.String))method queries the given table. The method returns a`Cursor`over the result set. Here's a query showing how to fill in the arguments:

| SELECT \* FROM WORD_LIST_TABLE WHERE word="alpha" ORDER BY word ASCLIMIT 2,1; |
|-------------------------------------------------------------------------------|

The query returns the following:

| \[\["alpha", "particle"\]\] |
|-----------------------------|

Example of arguments that you can use:

| String table = "WORD_LIST_TABLE" String\[\] columns = new String\[\]{"\*"}; String selection = "word = ?" String\[\] selectionArgs = new String\[\]{"alpha"}; String groupBy = null; String having = null; String orderBy = "word ASC" String limit = "2,1" query(table, columns, selection, selectionArgs, groupBy, having, orderBy, limit); |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

**Note:** In real code, you wouldn't create variables for`null`values. See the Android[SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase)documentation for versions of this method with different parameters.

## Cursors

A*cursor*is a pointer into a row of structured data. You can think of a cursor as a pointer to a table row.

A query returns a[Cursor](https://developer.android.com/reference/android/database/Cursor)object that points to the first element in the query result. The`Cursor`class provides methods for moving the cursor through the query result, and methods to get the data from the columns of each row in the result.

When a method returns a`Cursor`object, you iterate over the result, extract the data, do something with the data, and close the cursor to release the memory.

## Learn more

- [SQLite website](https://www.sqlite.org/about.html)
- [Full description of SQL as understood by SQLite](https://www.sqlite.org/lang.html)
- [SQLiteDatabase](https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase)class
- [Cursor](https://developer.android.com/reference/android/database/Cursor)class