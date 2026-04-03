---
title: https://developer.android.com/privacy-and-security/risks/sql-injection
url: https://developer.android.com/privacy-and-security/risks/sql-injection
source: md.txt
---

# SQL injection

<br />

**OWASP category:** [MASVS-CODE: Code Quality](https://mas.owasp.org/MASVS/10-MASVS-CODE)

## Overview

SQL injection exploits vulnerable applications by inserting code into SQL statements to access underlying databases beyond their intentionally-exposed interfaces. The attack can expose private data, corrupt database contents, and even compromising of backend infrastructure.

SQL can be vulnerable to injection via queries that are created dynamically by concatenating user input before execution. Targeting web, mobile and any SQL database application, SQL injection usually features in the[OWASP Top Ten](https://owasp.org/www-community/attacks/SQL_Injection)of web vulnerabilities. Attackers used the technique in several high-profile breaches.

In this basic example, an unescaped input by a user into an order number box can be inserted into the SQL string and interpreted as the following query:  

    SELECT * FROM users WHERE email = 'example@example.com' AND order_number = '251542'' LIMIT 1

Such code would generate a database syntax error in a web console, which shows the application may be vulnerable to SQL injection. Replacing the order number with`'OR 1=1--`means authentication can be achieved since the database evaluates the statement to`True`, as one always equals one.

Similarly, this query returns all rows from a table:  

    SELECT * FROM purchases WHERE email='admin@app.com' OR 1=1;

### Content providers

Content providers offer a structured storage mechanism that can be limited to an application or exported for sharing with other apps. Permissions should be set based on the principle of least privilege; an exported`ContentProvider`can have a single specified permission for reading and writing.

It is worth noting that not all SQL injections lead to exploitation. Some content providers already grant readers complete access to the SQLite database; being able to execute arbitrary queries yields little advantage. Patterns that can represent a security issue include:

- **Multiple content providers sharing a single SQLite database file.**
  - In this case, each table may be intended for a unique content provider. A successful SQL injection in one content provider would grant access to any other tables.
- **A content provider has multiple permissions for content within the same database.**
  - SQL injection in a single content provider that grants access with different permission levels could lead to local bypass of security or privacy settings.

## Impact

SQL injection can expose sensitive user or application data, overcome authentication and authorization restrictions, and leave databases vulnerable to corruption or deletion. Impacts can include dangerous and lasting implications for users whose personal data has been exposed. Providers of apps and services risk losing intellectual property or user trust.

## Mitigations

### Replaceable parameters

Using`?`as a replaceable parameter in selection clauses and a separate array of selection arguments binds the user input directly to the query rather than interpreting it as part of a SQL statement.  

### Kotlin

    // Constructs a selection clause with a replaceable parameter.
    val selectionClause = "var = ?"

    // Sets up an array of arguments.
    val selectionArgs: Array<String> = arrayOf("")

    // Adds values to the selection arguments array.
    selectionArgs[0] = userInput

### Java

    // Constructs a selection clause with a replaceable parameter.
    String selectionClause =  "var = ?";

    // Sets up an array of arguments.
    String[] selectionArgs = {""};

    // Adds values to the selection arguments array.
    selectionArgs[0] = userInput;

The user input is bound directly to the query rather than being treated as SQL, preventing code injection.

Here's a more elaborate example showing a shopping app's query to retrieve purchase details with replaceable parameters:  

### Kotlin

    fun validateOrderDetails(email: String, orderNumber: String): Boolean {
        val cursor = db.rawQuery(
            "select * from purchases where EMAIL = ? and ORDER_NUMBER = ?",
            arrayOf(email, orderNumber)
        )

        val bool = cursor?.moveToFirst() ?: false
        cursor?.close()

        return bool
    }

### Java

    public boolean validateOrderDetails(String email, String orderNumber) {
        boolean bool = false;
        Cursor cursor = db.rawQuery(
          "select * from purchases where EMAIL = ? and ORDER_NUMBER = ?", 
          new String[]{email, orderNumber});
        if (cursor != null) {
            if (cursor.moveToFirst()) {
                bool = true;
            }
            cursor.close();
        }
        return bool;
    }

### Use PreparedStatement objects

The[`PreparedStatement`](https://developer.android.com/reference/java/sql/PreparedStatement)interface precompiles SQL statements as an object which can then be executed efficiently multiple times. PreparedStatement uses`?`as a placeholder for parameters, which would make the following compiled injection attempt ineffective:  

    WHERE id=295094 OR 1=1;

In this case,`295094 OR 1=1`statement is read as the value for ID, likely yielding no results, whereas a raw query would interpret the`OR 1=1`statement as another part of the`WHERE`clause. The example below shows a parametrized query:  

### Kotlin

    val pstmt: PreparedStatement = con.prepareStatement(
            "UPDATE EMPLOYEES SET ROLE = ? WHERE ID = ?").apply {
        setString(1, "Barista")
        setInt(2, 295094)
    }

### Java

    PreparedStatement pstmt = con.prepareStatement(
                                    "UPDATE EMPLOYEES SET ROLE = ? WHERE ID = ?");
    pstmt.setString(1, "Barista")   
    pstmt.setInt(2, 295094)

### Use query methods

In this longer example, the`selection`and`selectionArgs`of the`query()`method are combined to make a`WHERE`clause. Since the arguments are provided separately, they are escaped before their combination, preventing SQL injection.  

### Kotlin

    val db: SQLiteDatabase = dbHelper.getReadableDatabase()
    // Defines a projection that specifies which columns from the database
    // should be selected.
    val projection = arrayOf(
        BaseColumns._ID,
        FeedEntry.COLUMN_NAME_TITLE,
        FeedEntry.COLUMN_NAME_SUBTITLE
    )

    // Filters results WHERE "title" = 'My Title'.
    val selection: String = FeedEntry.COLUMN_NAME_TITLE.toString() + " = ?"
    val selectionArgs = arrayOf("My Title")

    // Specifies how to sort the results in the returned Cursor object.
    val sortOrder: String = FeedEntry.COLUMN_NAME_SUBTITLE.toString() + " DESC"

    val cursor = db.query(
        FeedEntry.TABLE_NAME,  // The table to query
        projection,            // The array of columns to return
                               //   (pass null to get all)
        selection,             // The columns for the WHERE clause
        selectionArgs,         // The values for the WHERE clause
        null,                  // Don't group the rows
        null,                  // Don't filter by row groups
        sortOrder              // The sort order
    ).use {
        // Perform operations on the query result here.
        it.moveToFirst()
    }

### Java

    SQLiteDatabase db = dbHelper.getReadableDatabase();
    // Defines a projection that specifies which columns from the database
    // should be selected.
    String[] projection = {
        BaseColumns._ID,
        FeedEntry.COLUMN_NAME_TITLE,
        FeedEntry.COLUMN_NAME_SUBTITLE
    };

    // Filters results WHERE "title" = 'My Title'.
    String selection = FeedEntry.COLUMN_NAME_TITLE + " = ?";
    String[] selectionArgs = { "My Title" };

    // Specifies how to sort the results in the returned Cursor object.
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

### Use properly configured SQLiteQueryBuilder

Developers can further protect applications by using[`SQLiteQueryBuilder`](https://developer.android.com/reference/android/database/sqlite/SQLiteQueryBuilder), a class that helps build queries to be sent to`SQLiteDatabase`objects. Recommended configurations include:

- [`setStrict()`](https://developer.android.com/reference/android/database/sqlite/SQLiteQueryBuilder#setStrict(boolean))mode for query validation.
- [`setStrictColumns()`](https://developer.android.com/reference/android/database/sqlite/SQLiteQueryBuilder#setStrictColumns(boolean))to validate that columns are allow-listed in the setProjectionMap.
- [`setStrictGrammar()`](https://developer.android.com/reference/android/database/sqlite/SQLiteQueryBuilder#setStrictGrammar(boolean))to limit subqueries.

### Use Room library

The`android.database.sqlite`package provides APIs necessary for using databases on Android. However, this approach requires writing low-level code and lacks compile-time verification of raw SQL queries. As data graphs change, affected SQL queries need to be updated manually -- a time-consuming and error-prone process.

A high-level solution is to use the[Room Persistence Library](https://developer.android.com/training/basics/data-storage/room)as an abstraction layer for SQLite databases. Room's features comprise:

- A database class which serves as the main access point for connecting to the app's persisted data.
- Data entities representing the database's tables.
- Data access objects (DAOs), which provide methods the app can use to query, update, insert, and delete data.

Room's benefits include:

- Compile-time verification of SQL queries.
- Reduction of error-prone boilerplate code.
- Streamlined database migration.

### Best practices

SQL injection is a potent attack against which it can be difficult to be entirely resilient, particularly with large and complex applications. Additional security considerations should be in place to limit the severity of potential flaws in data interfaces, including:

- Robust, one-way and salted hashes to encrypt passwords:
  - 256-bit AES for commercial applications.
  - 224- or 256-bit public key sizes for elliptic curve cryptography.
- Limiting permissions.
- Precisely structuring data formats and verifying that the data conforms to the expected format.
- Avoiding storing personal or sensitive user data where possible (for example, implementing application logic by hashing rather than transmitting or storing data).
- Minimising APIs and third-party applications that access sensitive data.

## Resources

- [Save data using SQLite](https://developer.android.com/training/data-storage/sqlite)

- [Content provider basics](https://developer.android.com/guide/topics/providers/content-provider-basics)

- [Saving data in local database using Room](https://developer.android.com/training/data-storage/room)

- [Security tips](https://developer.android.com/training/articles/security-tips)

- [Kotlin SQL injection prevention guide](https://www.stackhawk.com/blog/kotlin-sql-injection-guide-examples-and-prevention/)