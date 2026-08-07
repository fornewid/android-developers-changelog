---
title: https://developer.android.com/training/data-storage/room/testing-db
url: https://developer.android.com/training/data-storage/room/testing-db
source: md.txt
---

When you create databases using the [Room persistence library](https://developer.android.com/training/data-storage/room), you should verify the stability of your app's database and your users' data. This page describes how to test your database and perform debugging steps to help your tests pass.

## Test your database

There are two ways to test your database:

- On a device that runs Android
- On your host development machine

> [!NOTE]
> **Note:** We don't recommend Android local unit tests with Robolectric. Use local JVM tests using Room KMP instead.

For information about testing that's specific to database migrations, see [Testing Migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test).

> [!NOTE]
> **Note:** When you run tests for your app, Room lets you create mock instances of your [data access object (DAO)](https://developer.android.com/training/data-storage/room/accessing-data) classes. That way, if you aren't testing the database itself, you don't need to create a full database because your DAOs don't leak any details of your database.

### Test on a device that runs Android

To test your database implementation, we recommend that you write a JUnit test that runs on a device that runs Android. Because these tests don't require an activity, they run faster than UI tests.

When setting up your tests, you should create an in-memory version of your database to make your tests more hermetic, as shown in the following example:

<br />

```kotlin
import kotlinx.coroutines.test.runTest

@RunWith(AndroidJUnit4::class)
class SimpleEntityReadWriteTest {
    private lateinit var userDao: UserDao
    private lateinit var db: TestDatabase

    @Before
    fun createDb() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        db = Room.inMemoryDatabaseBuilder<TestDatabase>(context)
                .setDriver(BundledSQLiteDriver())
                .build()
        userDao = db.userDao()
    }

    @After
    fun closeDb() {
        db.close()
    }

    @Test
    fun writeUserAndReadInList() = runTest {
        val user = User(3, "george")
        userDao.insert(user)
        val byName = userDao.findUsersByName("george")
        assertEquals(byName.single(), user)
    }
}
   
```

<br />

### Test on your host machine (JVM)

With Room KMP, you can run database tests on your host development machine using local JVM JUnit tests. This setup lets your tests run faster by eliminating the overhead of an Android emulator or device.

To help maintain consistency, use the `BundledSQLiteDriver`. This driver includes SQLite compiled from source, which uses the exact same version of SQLite on your host machine, Android devices, and iOS devices. Using this driver eliminates version mismatch issues.

To set up JVM tests, configure the `BundledSQLiteDriver` in your test database builder:

<br />

```kotlin
val db = Room.inMemoryDatabaseBuilder<TestDatabase>()
    .setDriver(BundledSQLiteDriver())
    .build()
   
```

<br />

> [!NOTE]
> **Note:** On JVM desktop targets, `inMemoryDatabaseBuilder` doesn't require a `Context` parameter.

### Test your migrations

Room supports [incremental database migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions) to retain existing app data in situations where an app update changes the database schema. However, an incorrectly defined migration could cause your app to crash. Make sure that you [test your Room database migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test).

## Debug your database

There are several tools and processes that you can use to debug your database.

### Use the Database Inspector

In Android Studio 4.1 and higher, the Database Inspector lets you inspect, query, and modify your app's databases while your app runs. The Database Inspector is compatible with the version of SQLite that is bundled with Android and includes special features for use with Room:

- Use gutter actions to run queries from your [DAO classes](https://developer.android.com/training/data-storage/room/accessing-data).
- When your running app makes changes to the data, you can immediately see live updates in the Database Inspector.

For more information about the Database Inspector, see [Debug your database with the Database Inspector](https://developer.android.com/studio/inspect/database).

### Dump data from the command line

The Android SDK includes a `sqlite3` database tool for examining your app's databases. It includes commands such as `.dump` to print the contents of a table, and `.schema` to print the `SQL CREATE` statement for an existing table.

You can also execute SQLite commands from the command line, as shown in the following snippet:

```bash
adb -s emulator-5554 shell sqlite3
/data/data/your-app-package/databases/rssitems.db
```

For more information, see the [`sqlite3` command line documentation](http://www.sqlite.org/cli.html), available on the SQLite website.

## Additional resources

To learn more about testing and debugging your Room database, see the following additional resources:

### Blog posts

- [Database Inspector: A live database tool we've been waiting for!](https://medium.com/androiddevelopers/database-inspector-9e91aa265316)

### Videos

- [Database Inspector](https://www.youtube.com/watch?v=UMc7Tu0nKYQ) (11 Weeks of Android)