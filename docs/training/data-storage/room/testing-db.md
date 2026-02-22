---
title: https://developer.android.com/training/data-storage/room/testing-db
url: https://developer.android.com/training/data-storage/room/testing-db
source: md.txt
---

# Test and debug your database

It's important to verify the stability of your app's database and your users' data when creating databases using the[Room persistence library](https://developer.android.com/training/data-storage/room). This page discusses how to test your database and perform debugging steps to help your tests pass.

## Test your database

There are 2 ways to test your database:

- On an Android device.
- On your host development machine (not recommended).

For information about testing that's specific to database migrations, see[Testing Migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test).
| **Note:** When running tests for your app, Room allows you to create mock instances of your[DAO](https://developer.android.com/training/data-storage/room/accessing-data)classes. That way, you don't need to create a full database if you aren't testing the database itself. This functionality is possible because your DAOs don't leak any details of your database.

### Test on an Android device

The recommended approach for testing your database implementation is writing a JUnit test that runs on an Android device. Because these tests don't require creating an activity, they should be faster to execute than your UI tests.

When setting up your tests, you should create an in-memory version of your database to make your tests more hermetic, as shown in the following example:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
class SimpleEntityReadWriteTest {
    private lateinit var userDao: UserDao
    private lateinit var db: TestDatabase

    @Before
    fun createDb() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        db = Room.inMemoryDatabaseBuilder(
                context, TestDatabase::class.java).build()
        userDao = db.getUserDao()
    }

    @After
    @Throws(IOException::class)
    fun closeDb() {
        db.close()
    }

    @Test
    @Throws(Exception::class)
    fun writeUserAndReadInList() {
        val user: User = TestUtil.createUser(3).apply {
            setName("george")
        }
        userDao.insert(user)
        val byName = userDao.findUsersByName("george")
        assertThat(byName.get(0), equalTo(user))
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
public class SimpleEntityReadWriteTest {
    private UserDao userDao;
    private TestDatabase db;

    @Before
    public void createDb() {
        Context context = ApplicationProvider.getApplicationContext();
        db = Room.inMemoryDatabaseBuilder(context, TestDatabase.class).build();
        userDao = db.getUserDao();
    }

    @After
    public void closeDb() throws IOException {
        db.close();
    }

    @Test
    public void writeUserAndReadInList() throws Exception {
        User user = TestUtil.createUser(3);
        user.setName("george");
        userDao.insert(user);
        List<User> byName = userDao.findUsersByName("george");
        assertThat(byName.get(0), equalTo(user));
    }
}
```

### Test on your host machine

Room uses the SQLite Support Library, which provides interfaces that match those in the Android Framework classes. This support allows you to pass custom implementations of the support library to test your database queries.
| **Note:** Even though this setup allows your tests to run very quickly, it isn't recommended because the version of SQLite running on your device---and your users' devices---might not match the version on your host machine.

### Test your migrations

Room supports[incremental database migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions)to retain existing app data in situations where an app update changes the database schema. However, an incorrectly defined migration could cause your app to crash. Make sure that you[test your Room database migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test).

## Debug your database

There are several tools and processes that you can use to debug your database.

### Use the Database Inspector

In Android Studio 4.1 and higher, the Database Inspector allows you to inspect, query, and modify your app's databases while your app is running. The Database Inspector is compatible with the version of SQLite that is bundled with Android and includes special features for use with Room:

- Use gutter actions to quickly run queries from your[DAO classes](https://developer.android.com/training/data-storage/room/accessing-data).
- Immediately see live updates in the Database Inspector when your running app makes changes to the data.

To learn more about the Database Inspector, see[Debug your database with the Database Inspector](https://developer.android.com/studio/inspect/database).

### Dump data from the command line

The Android SDK includes a`sqlite3`database tool for examining your app's databases. It includes commands such as`.dump`to print the contents of a table, and`.schema`to print the`SQL CREATE`statement for an existing table.

You can also execute SQLite commands from the command line, as shown in the following snippet:  

```bash
adb -s emulator-5554 shell
sqlite3 /data/data/your-app-package/databases/rssitems.db
```

For more information, see the[`sqlite3`command line documentation](http://www.sqlite.org/cli.html), available on the SQLite website.

## Additional resources

To learn more about testing and debugging your Room database, see the following additional resources:

### Blog posts

- [Database Inspector: A live database tool we've been waiting for!](https://medium.com/androiddevelopers/database-inspector-9e91aa265316)

### Videos

- [Database Inspector](https://www.youtube.com/watch?v=UMc7Tu0nKYQ)(11 Weeks of Android)