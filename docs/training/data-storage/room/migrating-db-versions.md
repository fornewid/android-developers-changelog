---
title: https://developer.android.com/training/data-storage/room/migrating-db-versions
url: https://developer.android.com/training/data-storage/room/migrating-db-versions
source: md.txt
---

As you add and change features in your app, you need to modify your Room entity classes and underlying database tables to reflect these changes. It's important to preserve user data that is already in the on-device database when an app update changes the database schema.

Room supports both automated and manual options for incremental migration. Automatic migrations work for most basic schema changes, but you might need to manually define migration paths for more complex changes.

## Automated migrations

| **Note:** Room supports automated migrations in version 2.4.0-alpha01 and higher. If your app uses a lower version of Room, you must[define your migrations manually](https://developer.android.com/training/data-storage/room/migrating-db-versions#manual).

To declare an automated migration between two database versions, add an[`@AutoMigration`](https://developer.android.com/reference/kotlin/androidx/room/AutoMigration)annotation to the[`autoMigrations`](https://developer.android.com/reference/kotlin/androidx/room/Database#autoMigrations())property in[`@Database`](https://developer.android.com/reference/kotlin/androidx/room/Database):  

### Kotlin

```kotlin
// Database class before the version update.
@Database(
  version = 1,
  entities = [User::class]
)
abstract class AppDatabase : RoomDatabase() {
  ...
}

// Database class after the version update.
@Database(
  version = 2,
  entities = [User::class],
  autoMigrations = [
    AutoMigration (from = 1, to = 2)
  ]
)
abstract class AppDatabase : RoomDatabase() {
  ...
}
```

### Java

```java
// Database class before the version update.
@Database(
  version = 1,
  entities = {User.class}
)
public abstract class AppDatabase extends RoomDatabase {
  ...
}

// Database class after the version update.
@Database(
  version = 2,
  entities = {User.class},
  autoMigrations = {
    @AutoMigration (from = 1, to = 2)
  }
)
public abstract class AppDatabase extends RoomDatabase {
  ...
}
```
| **Note:** Automated Room migrations rely on the generated database schema for both the old and the new versions of the database. If[`exportSchema`](https://developer.android.com/reference/kotlin/androidx/room/Database#exportSchema())is set to`false`, or if you have not yet compiled the database with the new version number, then automated migrations fail.

### Automatic migration specifications

If Room detects ambiguous schema changes and it can't generate a migration plan without more input, it throws a compile-time error and asks you to implement an[`AutoMigrationSpec`](https://developer.android.com/reference/kotlin/androidx/room/migration/AutoMigrationSpec). Most commonly, this occurs when a migration involves one of the following:

- Deleting or renaming a table.
- Deleting or renaming a column.

You can use`AutoMigrationSpec`to give Room the additional information that it needs to correctly generate migration paths. Define a static class that implements`AutoMigrationSpec`in your`RoomDatabase`class and annotate it with one or more of the following:

- [`@DeleteTable`](https://developer.android.com/reference/kotlin/androidx/room/DeleteTable)
- [`@RenameTable`](https://developer.android.com/reference/kotlin/androidx/room/RenameTable)
- [`@DeleteColumn`](https://developer.android.com/reference/kotlin/androidx/room/DeleteColumn)
- [`@RenameColumn`](https://developer.android.com/reference/kotlin/androidx/room/RenameColumn)

To use the`AutoMigrationSpec`implementation for an automated migration, set the`spec`property in the corresponding`@AutoMigration`annotation:  

### Kotlin

```kotlin
@Database(
  version = 2,
  entities = [User::class],
  autoMigrations = [
    AutoMigration (
      from = 1,
      to = 2,
      spec = AppDatabase.MyAutoMigration::class
    )
  ]
)
abstract class AppDatabase : RoomDatabase() {
  @RenameTable(fromTableName = "User", toTableName = "AppUser")
  class MyAutoMigration : AutoMigrationSpec
  ...
}
```

### Java

```java
@Database(
  version = 2,
  entities = {AppUser.class},
  autoMigrations = {
    @AutoMigration (
      from = 1,
      to = 2,
      spec = AppDatabase.MyAutoMigration.class
    )
  }
)
public abstract class AppDatabase extends RoomDatabase {
  @RenameTable(fromTableName = "User", toTableName = "AppUser")
  static class MyAutoMigration implements AutoMigrationSpec { }
  ...
}
```

If your app needs to do more work after the automated migration completes, you can implement[`onPostMigrate()`](https://developer.android.com/reference/androidx/room/migration/AutoMigrationSpec#onPostMigrate(androidx.sqlite.db.SupportSQLiteDatabase)). If you implement this method in your`AutoMigrationSpec`, Room calls it after the automated migration completes.
| **Note:** In Kotlin, if you have multiple migrations of the same type you must use a container for multiple annotations, such as[`@RenameTable.Entries`](https://developer.android.com/reference/kotlin/androidx/room/RenameTable.Entries).

## Manual migrations

In cases where a migration involves complex schema changes, Room might not be able to generate an appropriate migration path automatically. For example, if you decide to split the data in a table into two tables, Room can't tell how to perform this split. In cases like these, you must manually define a migration path by implementing a[`Migration`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration)class.

A`Migration`class explicitly defines a migration path between a`startVersion`and an`endVersion`by overriding the[`Migration.migrate()`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration#migrate)method. Add your`Migration`classes to your database builder using the[`addMigrations()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#addmigrations)method:  

### Kotlin

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
  override fun migrate(database: SupportSQLiteDatabase) {
    database.execSQL("CREATE TABLE `Fruit` (`id` INTEGER, `name` TEXT, " +
      "PRIMARY KEY(`id`))")
  }
}

val MIGRATION_2_3 = object : Migration(2, 3) {
  override fun migrate(database: SupportSQLiteDatabase) {
    database.execSQL("ALTER TABLE Book ADD COLUMN pub_year INTEGER")
  }
}

Room.databaseBuilder(applicationContext, MyDb::class.java, "database-name")
  .addMigrations(MIGRATION_1_2, MIGRATION_2_3).build()
```

### Java

```java
static final Migration MIGRATION_1_2 = new Migration(1, 2) {
  @Override
  public void migrate(SupportSQLiteDatabase database) {
    database.execSQL("CREATE TABLE `Fruit` (`id` INTEGER, "
      + "`name` TEXT, PRIMARY KEY(`id`))");
  }
};

static final Migration MIGRATION_2_3 = new Migration(2, 3) {
  @Override
  public void migrate(SupportSQLiteDatabase database) {
    database.execSQL("ALTER TABLE Book "
      + " ADD COLUMN pub_year INTEGER");
  }
};

Room.databaseBuilder(getApplicationContext(), MyDb.class, "database-name")
  .addMigrations(MIGRATION_1_2, MIGRATION_2_3).build();
```
| **Caution:** To keep your migration logic functioning as expected, use full queries instead of referencing constants that represent the queries.

When you define your migration paths, you can use automated migrations for some versions and manual migrations for others. If you define both an automated migration and a manual migration for the same version, then Room uses the manual migration.

## Test migrations

Migrations are often complex, and an incorrectly defined migration can cause your app to crash. To preserve your app's stability, test your migrations. Room provides a`room-testing`Maven artifact to assist with the testing process for both automated and manual migrations. For this artifact to work, you must first export your database's schema.

### Export schemas

Room can export your database's schema information into a JSON file at compile time. The exported JSON files represent your database's schema history. Store these files in your version control system so Room can create lower versions of the database for testing purposes and to enable auto-migration generation.

#### Set schema location using Room Gradle Plugin

If you are using Room version 2.6.0 or higher, you can apply the[Room Gradle Plugin](https://developer.android.com/jetpack/androidx/releases/room#gradle-plugin)and use the`room`extension to specify the schema directory.  

### Groovy

    plugins {
      id 'androidx.room'
    }

    room {
      schemaDirectory "$projectDir/schemas"
    }

### Kotlin

    plugins {
      id("androidx.room")
    }

    room {
      schemaDirectory("$projectDir/schemas")
    }

If your database schema differs based on the variant, flavor, or build type, you must specify different locations by using the`schemaDirectory()`configuration multiple times, each with a`variantMatchName`as the first argument. Each configuration can match one or more variants based on simple comparison with the variant name.

Make sure these are exhaustive and cover all variants. You can also include a`schemaDirectory()`without a`variantMatchName`to handle variants not matched by any of the other configurations. For example, in an app with two build flavors`demo`and`full`and two build types`debug`and`release`, the following are valid configurations:  

### Groovy

    room {
      // Applies to 'demoDebug' only
      schemaDirectory "demoDebug", "$projectDir/schemas/demoDebug"

      // Applies to 'demoDebug' and 'demoRelease'
      schemaDirectory "demo", "$projectDir/schemas/demo"

      // Applies to 'demoDebug' and 'fullDebug'
      schemaDirectory "debug", "$projectDir/schemas/debug"

      // Applies to variants that aren't matched by other configurations.
      schemaDirectory "$projectDir/schemas"
    }

### Kotlin

    room {
      // Applies to 'demoDebug' only
      schemaDirectory("demoDebug", "$projectDir/schemas/demoDebug")

      // Applies to 'demoDebug' and 'demoRelease'
      schemaDirectory("demo", "$projectDir/schemas/demo")

      // Applies to 'demoDebug' and 'fullDebug'
      schemaDirectory("debug", "$projectDir/schemas/debug")

      // Applies to variants that aren't matched by other configurations.
      schemaDirectory("$projectDir/schemas")
    }

#### Set schema location using annotation processor option

If you are using version 2.5.2 or lower of Room, or if you aren't using the Room Gradle Plugin, set the schema location using the`room.schemaLocation`annotation processor option.

Files in this directory are used as inputs and outputs for some Gradle tasks. For correctness and performance of incremental and cached builds, you must use Gradle's[`CommandLineArgumentProvider`](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html)to inform Gradle about this directory.

First, copy the`RoomSchemaArgProvider`class shown below into your module's Gradle build file. The`asArguments()`method in the sample class passes`room.schemaLocation=${schemaDir.path}`to`KSP`. If you're using`KAPT`and`javac`, change this value to`-Aroom.schemaLocation=${schemaDir.path}`instead.  

### Groovy

    class RoomSchemaArgProvider implements CommandLineArgumentProvider {

      @InputDirectory
      @PathSensitive(PathSensitivity.RELATIVE)
      File schemaDir

      RoomSchemaArgProvider(File schemaDir) {
        this.schemaDir = schemaDir
      }

      @Override
      Iterable<String> asArguments() {
        // Note: If you're using KAPT and javac, change the line below to
        // return ["-Aroom.schemaLocation=${schemaDir.path}".toString()].
        return ["room.schemaLocation=${schemaDir.path}".toString()]
      }
    }

### Kotlin

    class RoomSchemaArgProvider(
      @get:InputDirectory
      @get:PathSensitive(PathSensitivity.RELATIVE)
      val schemaDir: File
    ) : CommandLineArgumentProvider {

      override fun asArguments(): Iterable<String> {
        // Note: If you're using KAPT and javac, change the line below to
        // return listOf("-Aroom.schemaLocation=${schemaDir.path}").
        return listOf("room.schemaLocation=${schemaDir.path}")
      }
    }

Then configure the compile options to use the`RoomSchemaArgProvider`with the specified schema directory:  

### Groovy

    // For KSP, configure using KSP extension:
    ksp {
      arg(new RoomSchemaArgProvider(new File(projectDir, "schemas")))
    }

    // For javac or KAPT, configure using android DSL:
    android {
      ...
      defaultConfig {
        javaCompileOptions {
          annotationProcessorOptions {
            compilerArgumentProviders(
              new RoomSchemaArgProvider(new File(projectDir, "schemas"))
            )
          }
        }
      }
    }

### Kotlin

    // For KSP, configure using KSP extension:
    ksp {
      arg(RoomSchemaArgProvider(File(projectDir, "schemas")))
    }

    // For javac or KAPT, configure using android DSL:
    android {
      ...
      defaultConfig {
        javaCompileOptions {
          annotationProcessorOptions {
            compilerArgumentProviders(
              RoomSchemaArgProvider(File(projectDir, "schemas"))
            )
          }
        }
      }
    }

### Test a single migration

Before you can test your migrations, add the`androidx.room:room-testing`Maven artifact from Room into your test dependencies and add the location of the exported schema as an asset folder:

build.gradle  

### Groovy

```groovy
android {
    ...
    sourceSets {
        // Adds exported schema location as test app assets.
        androidTest.assets.srcDirs += files("$projectDir/schemas".toString())
    }
}

dependencies {
    ...
    androidTestImplementation "androidx.room:room-testing:2.8.4"
}
```

### Kotlin

```kotlin
android {
    ...
    sourceSets {
        // Adds exported schema location as test app assets.
        getByName("androidTest").assets.srcDir("$projectDir/schemas")
    }
}

dependencies {
    ...
    testImplementation("androidx.room:room-testing:2.8.4")
}
```

The testing package provides a[`MigrationTestHelper`](https://developer.android.com/reference/kotlin/androidx/room/testing/MigrationTestHelper)class, which can read exported schema files. The package also implements the JUnit4[`TestRule`](https://junit.org/junit4/javadoc/4.12/org/junit/rules/TestRule)interface, so it can manage created databases.

The following example demonstrates a test for a single migration:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    private val TEST_DB = "migration-test"

    @get:Rule
    val helper: MigrationTestHelper = MigrationTestHelper(
            InstrumentationRegistry.getInstrumentation(),
            MigrationDb::class.java.canonicalName,
            FrameworkSQLiteOpenHelperFactory()
    )

    @Test
    @Throws(IOException::class)
    fun migrate1To2() {
        var db = helper.createDatabase(TEST_DB, 1).apply {
            // Database has schema version 1. Insert some data using SQL queries.
            // You can't use DAO classes because they expect the latest schema.
            execSQL(...)

            // Prepare for the next version.
            close()
        }

        // Re-open the database with version 2 and provide
        // MIGRATION_1_2 as the migration process.
        db = helper.runMigrationsAndValidate(TEST_DB, 2, true, MIGRATION_1_2)

        // MigrationTestHelper automatically verifies the schema changes,
        // but you need to validate that the data was migrated properly.
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
public class MigrationTest {
    private static final String TEST_DB = "migration-test";

    @Rule
    public MigrationTestHelper helper;

    public MigrationTest() {
        helper = new MigrationTestHelper(InstrumentationRegistry.getInstrumentation(),
                MigrationDb.class.getCanonicalName(),
                new FrameworkSQLiteOpenHelperFactory());
    }

    @Test
    public void migrate1To2() throws IOException {
        SupportSQLiteDatabase db = helper.createDatabase(TEST_DB, 1);

        // Database has schema version 1. Insert some data using SQL queries.
        // You can't use DAO classes because they expect the latest schema.
        db.execSQL(...);

        // Prepare for the next version.
        db.close();

        // Re-open the database with version 2 and provide
        // MIGRATION_1_2 as the migration process.
        db = helper.runMigrationsAndValidate(TEST_DB, 2, true, MIGRATION_1_2);

        // MigrationTestHelper automatically verifies the schema changes,
        // but you need to validate that the data was migrated properly.
    }
}
```

### Test all migrations

Though it is possible to test a single incremental migration, we recommend that you include a test that covers all the migrations defined for your app's database. This helps ensure that there is no discrepancy between a recently created database instance and an older instance that followed the defined migration paths.

The following example demonstrates a test for all defined migrations:  

### Kotlin

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    private val TEST_DB = "migration-test"

    // Array of all migrations.
    private val ALL_MIGRATIONS = arrayOf(
            MIGRATION_1_2, MIGRATION_2_3, MIGRATION_3_4)

    @get:Rule
    val helper: MigrationTestHelper = MigrationTestHelper(
            InstrumentationRegistry.getInstrumentation(),
            AppDatabase::class.java.canonicalName,
            FrameworkSQLiteOpenHelperFactory()
    )

    @Test
    @Throws(IOException::class)
    fun migrateAll() {
        // Create earliest version of the database.
        helper.createDatabase(TEST_DB, 1).apply {
            close()
        }

        // Open latest version of the database. Room validates the schema
        // once all migrations execute.
        Room.databaseBuilder(
            InstrumentationRegistry.getInstrumentation().targetContext,
            AppDatabase::class.java,
            TEST_DB
        ).addMigrations(*ALL_MIGRATIONS).build().apply {
            openHelper.writableDatabase.close()
        }
    }
}
```

### Java

```java
@RunWith(AndroidJUnit4.class)
public class MigrationTest {
    private static final String TEST_DB = "migration-test";

    @Rule
    public MigrationTestHelper helper;

    public MigrationTest() {
        helper = new MigrationTestHelper(InstrumentationRegistry.getInstrumentation(),
                AppDatabase.class.getCanonicalName(),
                new FrameworkSQLiteOpenHelperFactory());
    }

    @Test
    public void migrateAll() throws IOException {
        // Create earliest version of the database.
        SupportSQLiteDatabase db = helper.createDatabase(TEST_DB, 1);
        db.close();

        // Open latest version of the database. Room validates the schema
        // once all migrations execute.
        AppDatabase appDb = Room.databaseBuilder(
                InstrumentationRegistry.getInstrumentation().getTargetContext(),
                AppDatabase.class,
                TEST_DB)
                .addMigrations(ALL_MIGRATIONS).build();
        appDb.getOpenHelper().getWritableDatabase();
        appDb.close();
    }

    // Array of all migrations.
    private static final Migration[] ALL_MIGRATIONS = new Migration[]{
            MIGRATION_1_2, MIGRATION_2_3, MIGRATION_3_4};
}
```

## Gracefully handle missing migration paths

If Room can't find a migration path to upgrade an existing database on a device to the current version, an[`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException)occurs. If it is acceptable to lose existing data when a migration path is missing, call the[`fallbackToDestructiveMigration()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbacktodestructivemigration)builder method when you create the database:  

### Kotlin

```kotlin
Room.databaseBuilder(applicationContext, MyDb::class.java, "database-name")
        .fallbackToDestructiveMigration()
        .build()
```

### Java

```java
Room.databaseBuilder(getApplicationContext(), MyDb.class, "database-name")
        .fallbackToDestructiveMigration()
        .build();
```

This method tells Room to destructively recreate the tables in your app's database when it needs to perform an incremental migration and there is no defined migration path.
| **Warning:** Setting this option in your app's database builder means that Room*permanently deletes all data*from the tables in the user's database when it attempts to perform a migration and there is no defined migration path.

If you only want to Room to fall back to destructive recreation in certain situations, there are a few alternatives to`fallbackToDestructiveMigration()`:

- If specific versions of your schema history cause errors that you can't solve with migration paths, use[`fallbackToDestructiveMigrationFrom()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbacktodestructivemigrationfrom)instead. This method indicates that you want Room to fall back to destructive recreation only when migrating from specific versions.
- If you want Room to fall back to destructive recreation only when migrating from a higher database version to a lower one, use[`fallbackToDestructiveMigrationOnDowngrade()`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbacktodestructivemigrationondowngrade)instead.

| **Note:** In 2.2.0 and higher, Room can use a prepackaged database file in some fallback migration cases instead of leaving an empty database. To learn more, see[Prepopulate your Room database](https://developer.android.com/training/data-storage/room/prepopulate#migrations).

## Handle column default values when upgrading to Room 2.2.0

In Room 2.2.0 and higher, you can define a default value for a column by using the annotation[`@ColumnInfo(defaultValue = "...")`](https://developer.android.com/reference/kotlin/androidx/room/ColumnInfo#defaultValue()). In versions lower than 2.2.0, the only way to define a default value for a column is by defining it directly in an executed SQL statement, which creates a default value that Room does not know about. This means that if a database is originally created by a version of Room lower than 2.2.0, upgrading your app to use Room 2.2.0 might require you to provide a special migration path for existing default values that you defined without using Room APIs.

For example, suppose that version 1 of a database defines a`Song`entity:  

### Kotlin

```kotlin
// Song entity, database version 1, Room 2.1.0.
@Entity
data class Song(
    @PrimaryKey
    val id: Long,
    val title: String
)
```

### Java

```java
// Song entity, database version 1, Room 2.1.0.
@Entity
public class Song {
    @PrimaryKey
    final long id;
    final String title;
}
```

Suppose also that version 2 of the same database adds a new`NOT NULL`column and defines a migration path from version 1 to version 2:  

### Kotlin

```kotlin
// Song entity, database version 2, Room 2.1.0.
@Entity
data class Song(
    @PrimaryKey
    val id: Long,
    val title: String,
    val tag: String // Added in version 2.
)

// Migration from 1 to 2, Room 2.1.0.
val MIGRATION_1_2 = object : Migration(1, 2) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL(
            "ALTER TABLE Song ADD COLUMN tag TEXT NOT NULL DEFAULT ''")
    }
}
```

### Java

```java
// Song entity, database version 2, Room 2.1.0.
@Entity
public class Song {
    @PrimaryKey
    final long id;
    final String title;
    @NonNull
    final String tag; // Added in version 2.
}


// Migration from 1 to 2, Room 2.1.0.
static final Migration MIGRATION_1_2 = new Migration(1, 2) {
    @Override
    public void migrate(SupportSQLiteDatabase database) {
        database.execSQL(
            "ALTER TABLE Song ADD COLUMN tag TEXT NOT NULL DEFAULT ''");
    }
};
```

This causes a discrepancy in the underlying table between updates and fresh installs of the app. Because the default value for the`tag`column is only declared in the migration path from version 1 to version 2, any users who install the app starting from version 2 don't have the default value for`tag`in their database schema.

In versions of Room lower than 2.2.0, this discrepancy is harmless. However, if the app later upgrades to use Room 2.2.0 or higher and changes the`Song`entity class to include a default value for`tag`using the[`@ColumnInfo`](https://developer.android.com/reference/kotlin/androidx/room/ColumnInfo)annotation, Room can then see this discrepancy. This results in failed schema validations.

To help ensure that the database schema is consistent across all users when column default values are declared in your earlier migration paths, do the following the first time you upgrade your app to use Room 2.2.0 or higher:

1. Declare column default values in their respective entity classes using the`@ColumnInfo`annotation.
2. Increase the database version number by 1.
3. Define a migration path to the new version that implements the[drop and recreate strategy](https://www.sqlite.org/lang_altertable.html#otheralter)to add the necessary default values to the existing columns.

| **Note:** If your app's database falls back to destructive migrations, or if there are no migration paths that add a column with a default value, then this process is not required.

The following example demonstrates this process:  

### Kotlin

```kotlin
// Migration from 2 to 3, Room 2.2.0.
val MIGRATION_2_3 = object : Migration(2, 3) {
    override fun migrate(database: SupportSQLiteDatabase) {
        database.execSQL("""
                CREATE TABLE new_Song (
                    id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT,
                    tag TEXT NOT NULL DEFAULT ''
                )
                """.trimIndent())
        database.execSQL("""
                INSERT INTO new_Song (id, name, tag)
                SELECT id, name, tag FROM Song
                """.trimIndent())
        database.execSQL("DROP TABLE Song")
        database.execSQL("ALTER TABLE new_Song RENAME TO Song")
    }
}
```

### Java

```java
// Migration from 2 to 3, Room 2.2.0.
static final Migration MIGRATION_2_3 = new Migration(2, 3) {
    @Override
    public void migrate(SupportSQLiteDatabase database) {
        database.execSQL("CREATE TABLE new_Song (" +
                "id INTEGER PRIMARY KEY NOT NULL," +
                "name TEXT," +
                "tag TEXT NOT NULL DEFAULT '')");
        database.execSQL("INSERT INTO new_Song (id, name, tag) " +
                "SELECT id, name, tag FROM Song");
        database.execSQL("DROP TABLE Song");
        database.execSQL("ALTER TABLE new_Song RENAME TO Song");
    }
};
```