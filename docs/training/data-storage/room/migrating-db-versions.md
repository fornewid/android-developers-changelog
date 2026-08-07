---
title: https://developer.android.com/training/data-storage/room/migrating-db-versions
url: https://developer.android.com/training/data-storage/room/migrating-db-versions
source: md.txt
---

As you add and change features in your app, you need to modify your Room entity classes and underlying database tables to reflect these changes. It's important to preserve user data that is already in the on-device database when an app update changes the database schema.

Room supports both automated and manual options for incremental migration. Automatic migrations work for most basic schema changes, but you might need to manually define migration paths for more complex changes.

## Automated migrations

To declare an automated migration between two database versions, add an [`@AutoMigration`](https://developer.android.com/reference/kotlin/androidx/room/AutoMigration) annotation to the [`autoMigrations`](https://developer.android.com/reference/kotlin/androidx/room/Database#autoMigrations()) property in [`@Database`](https://developer.android.com/reference/kotlin/androidx/room/Database):

<br />

```kotlin
// Database class before the version update.
@Database(
  version = 1,
  entities = [User::class]
)
abstract class AppDatabaseV1 : RoomDatabase() {
  abstract fun userDao(): UserDao
}

// Database class after the version update.
@Database(
  version = 2,
  entities = [User::class],
  autoMigrations = [
    AutoMigration(from = 1, to = 2)
  ]
)
abstract class AppDatabaseV2 : RoomDatabase() {
  abstract fun userDao(): UserDao
}
   
```

<br />

> [!NOTE]
> **Note:** Automated Room migrations rely on the generated database schema for both the lower and the higher versions of the database. If [`exportSchema`](https://developer.android.com/reference/kotlin/androidx/room/Database#exportSchema()) is set to `false`, or if you haven't yet compiled the database with the higher version number, then automated migrations fail.

### Automatic migration specifications

If Room detects ambiguous schema changes and it can't generate a migration plan without more input, it throws a compile-time error and you must provide an [`AutoMigrationSpec`](https://developer.android.com/reference/kotlin/androidx/room/migration/AutoMigrationSpec) implementation. Most commonly, this occurs when a migration involves one of the following:

- Deleting or renaming a table.
- Deleting or renaming a column.

You can use `AutoMigrationSpec` to give Room the additional information that it needs to correctly generate migration paths. Define a class that implements `AutoMigrationSpec` in your `RoomDatabase` class and annotate it with one or more of the following:

- [`@DeleteTable`](https://developer.android.com/reference/kotlin/androidx/room/DeleteTable)
- [`@RenameTable`](https://developer.android.com/reference/kotlin/androidx/room/RenameTable)
- [`@DeleteColumn`](https://developer.android.com/reference/kotlin/androidx/room/DeleteColumn)
- [`@RenameColumn`](https://developer.android.com/reference/kotlin/androidx/room/RenameColumn)

To use the `AutoMigrationSpec` implementation for an automated migration, set the `spec` property in the corresponding `@AutoMigration` annotation:

<br />

```kotlin
@Database(
  version = 2,
  entities = [User::class],
  autoMigrations = [
    AutoMigration (
      from = 1,
      to = 2,
      spec = MigrationSpec1To2::class
    )
  ]
)
abstract class AppDatabaseWithSpec : RoomDatabase() {
  abstract fun userDao(): UserDao
}

@RenameTable(fromTableName = "User", toTableName = "AppUser")
internal class MigrationSpec1To2 : AutoMigrationSpec
    
```

<br />

If your app needs to do more work after the automated migration completes, you can implement [`onPostMigrate`](https://developer.android.com/reference/androidx/room3/migration/AutoMigrationSpec#onPostMigrate(androidx.sqlite.SQLiteConnection)). If you implement this function in your `AutoMigrationSpec`, Room calls it after the automated migration completes.

> [!NOTE]
> **Note:** In Kotlin, if you have multiple migrations of the same type, you must use a container for multiple annotations, such as [`@RenameTable.Entries`](https://developer.android.com/reference/kotlin/androidx/room/RenameTable.Entries).

## Manual migrations

If a migration involves complex schema changes, Room might not be able to generate an appropriate migration path automatically. For example, if you decide to split the data in a table into two tables, Room can't determine how to perform this split. In these situations, you must manually define a migration path by implementing a [`Migration`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration) class.

A `Migration` class explicitly defines a migration path between a `startVersion` and an `endVersion` by overriding the [`migrate`](https://developer.android.com/reference/kotlin/androidx/room/migration/Migration#migrate) function. Add your `Migration` classes to your database builder using the [`addMigrations`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#addmigrations) function:

<br />

```kotlin
val MIGRATION_1_2 = object : Migration(1, 2) {
  override suspend fun migrate(connection: SQLiteConnection) {
    connection.executeSQL("CREATE TABLE `Fruit` (`id` INTEGER, `name` TEXT, " +
      "PRIMARY KEY(`id`))")
  }
}

val MIGRATION_2_3 = object : Migration(2, 3) {
  override suspend fun migrate(connection: SQLiteConnection) {
    connection.executeSQL("ALTER TABLE Book ADD COLUMN pub_year INTEGER")
  }
}

Room.databaseBuilder<ManualMigrationDatabase>(applicationContext, "database-name")
  .addMigrations(MIGRATION_1_2, MIGRATION_2_3)
  .build()
   
```

<br />

> [!CAUTION]
> **Caution:** To keep your migration logic functioning as expected, use full queries instead of referencing constants that represent the queries.

When you define your migration paths, you can use automated migrations for some versions and manual migrations for others. If you define both an automated migration and a manual migration for the same version, then Room uses the manual migration.

## Test migrations

Migrations are often complex, and an incorrectly defined migration can cause your app to crash. To preserve your app's stability, test your migrations. Room provides a `room3-testing` Maven artifact to assist with the testing process for both automated and manual migrations. For this artifact to work, you must first export your database's schema.

### Export schemas

Room exports your database's schema information into a JSON file at compile time. The exported JSON files represent your database's schema history. Store these files in your version control system so that you can recreate lower versions of the database for testing and support automated migration generation.

#### Set schema location using Room Gradle Plugin

To specify the schema directory, apply the [Room Gradle Plugin](https://developer.android.com/jetpack/androidx/releases/room#gradle-plugin) and use the `room3` extension.

### Groovy

    plugins {
      id 'androidx.room3'
    }

    room3 {
      schemaDirectory "$projectDir/schemas"
    }

### Kotlin

    plugins {
      id("androidx.room3")
    }

    room3 {
      schemaDirectory("$projectDir/schemas")
    }

If your database schema differs based on the variant, flavor, or build type, you must specify different locations by using the `schemaDirectory` configuration multiple times, each with a `variantMatchName` as the first argument. Each configuration can match one or more variants based on simple comparison with the variant name.

Make sure these are exhaustive and cover all variants. You can also include a `schemaDirectory()` without a `variantMatchName` to handle variants not matched by any of the other configurations. For example, in an app with two build flavors `demo` and `full` and two build types `debug` and `release`, the following are valid configurations:

### Groovy

    room3 {
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

    room3 {
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

If you aren't using the Room Gradle plugin, set the schema location using the `room.schemaLocation` annotation processor option.

Gradle uses files in this directory as inputs and outputs for some Gradle tasks. For correctness and performance of incremental and cached builds, you must use Gradle's [`CommandLineArgumentProvider`](https://docs.gradle.org/current/javadoc/org/gradle/process/CommandLineArgumentProvider.html) to inform Gradle about this directory.

First, copy the following `RoomSchemaArgProvider` class into your module's Gradle build file. The `asArguments` function in the sample class passes `room.schemaLocation=${schemaDir.path}` to `KSP`. If you're using `KAPT` and `javac`, change this value to `-Aroom.schemaLocation=${schemaDir.path}` instead.

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
        return listOf("room.schemaLocation=${schemaDir.path}")
      }
    }

Then configure the compile options to use the `RoomSchemaArgProvider` with the specified schema directory:

### Groovy

    ksp {
      arg(new RoomSchemaArgProvider(new File(projectDir, "schemas")))
    }

### Kotlin

    ksp {
      arg(RoomSchemaArgProvider(File(projectDir, "schemas")))
    }

### Test a single migration

Before you can test your migrations, add the `androidx.room3:room3-testing` artifact to your test dependencies and add the location of the exported schema as an asset directory:

### Groovy

```groovy
android {
    ...
    sourceSets {
        // Adds exported schema location as test app assets if not using
        // the Room Gradle Plugin.
        androidTest.assets.srcDirs += files("$projectDir/schemas".toString())
    }
}

dependencies {
    ...
    androidTestImplementation "androidx.room3:room3-testing:3.0.1"
}
```

### Kotlin

```kotlin
android {
    ...
    sourceSets {
        // Adds exported schema location as test app assets if not using
        // the Room Gradle Plugin.
        getByName("androidTest").assets.srcDir("$projectDir/schemas")
    }
}

dependencies {
    ...
    testImplementation("androidx.room3:room3-testing:3.0.1")
}
```

The testing package provides a [`MigrationTestHelper`](https://developer.android.com/reference/kotlin/androidx/room3/testing/MigrationTestHelper) class, which can read exported schema files. The package also implements the JUnit4 [`TestRule`](https://junit.org/junit4/javadoc/4.12/org/junit/rules/TestRule) interface to manage created databases.

The following example demonstrates a test for a single migration:

<br />

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    private val TEST_DB = "migration-test"

    private val instrumentation = InstrumentationRegistry.getInstrumentation()

    @get:Rule
    val helper = MigrationTestHelper(
        instrumentation = instrumentation,
        databaseClass = MigrationDb::class,
        driver = AndroidSQLiteDriver(),
        file = instrumentation.targetContext.getDatabasePath(TEST_DB),
    )

    @Test
    fun migrate1To2() = runTest {
        val connection = helper.createDatabase(1)
        // Database has schema version 1. Insert some data using SQL queries.
        // You can't use DAO classes because they expect the latest schema.
        connection.execSQL("INSERT INTO User (id, name) VALUES (1, 'John Doe')")
        connection.close()

        // Re-open the database with version 2 and provide MIGRATION_1_2
        val migratedConnection = helper.runMigrationsAndValidate(2, listOf(MIGRATION_1_2))

        // MigrationTestHelper automatically verifies the schema changes,
        // but you need to validate that the data was migrated properly.
        val hasData = migratedConnection.prepare("SELECT COUNT(*) FROM User").use {
          it.step()
          it.getLong(0) > 0
        }
        assertTrue("Expected data was not migrated", hasData)
        migratedConnection.close()
    }
}
   
```

<br />

### Test all migrations

Although you can test a single incremental migration, you should include a test that covers all migrations defined for your app's database. This helps ensure that there's no discrepancy between a recently created database instance and an earlier instance that followed the defined migration paths.

The following example demonstrates a test for all defined migrations:

<br />

```kotlin
@RunWith(AndroidJUnit4::class)
class MigrationTest {
    private val TEST_DB = "migration-test"

    private val instrumentation = InstrumentationRegistry.getInstrumentation()

    // Array of all migrations.
    private val ALL_MIGRATIONS = arrayOf(MIGRATION_1_2, MIGRATION_2_3, MIGRATION_3_4)

    @get:Rule
    val helper: MigrationTestHelper = MigrationTestHelper(
        instrumentation = instrumentation,
        databaseClass = MigrationDb::class,
        driver = AndroidSQLiteDriver(),
        file = instrumentation.targetContext.getDatabasePath(TEST_DB),
    )

    @Test
    fun migrateAll() = runTest {
        // Create earliest version of the database.
        val connection = helper.createDatabase(1)
        connection.close()

        // Create latest version of the database.
        val db = Room.databaseBuilder<AppDatabase>(instrumentation.targetContext, TEST_DB)
          .setDriver(AndroidSQLiteDriver())
          .addMigrations(*ALL_MIGRATIONS)
          .build()
        // Open the database, Room validates the schema once all migrations
        // execute.
        db.useReaderConnection { connection ->
          // Perform additional validation
        }

        db.close()
    }
}
   
```

<br />

## Gracefully handle missing migration paths

If Room can't find a migration path to upgrade an existing database on a device to the current version, an [`IllegalStateException`](https://developer.android.com/reference/java/lang/IllegalStateException) occurs. If it's acceptable to lose existing data when a migration path is missing, call the [`fallbackToDestructiveMigration`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbackToDestructiveMigration(kotlin.Boolean)) builder function when you create the database:

<br />

```kotlin
Room.databaseBuilder<FallbackMigrationDatabase>(applicationContext, "database-name")
        .fallbackToDestructiveMigration()
        .build()
   
```

<br />

This function configures Room to destructively recreate the tables in your app's database when it needs to perform an incremental migration and there's no defined migration path.

> [!WARNING]
> **Warning:** Setting this option in your app's database builder means that Room *permanently deletes all data* from the tables in the user's database when it attempts to perform a migration and there's no defined migration path.

To fall back to destructive recreation only in certain situations, use one of the following alternatives to `fallbackToDestructiveMigration`:

- If specific versions of your schema history cause errors that you can't solve with migration paths, use [`fallbackToDestructiveMigrationFrom`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbackToDestructiveMigrationFrom(kotlin.Boolean,kotlin.IntArray)) instead. This function indicates that you want Room to fall back to destructive recreation only when migrating from specific versions.
- If you want Room to fall back to destructive recreation only when migrating from a higher database version to a lower one, use [`fallbackToDestructiveMigrationOnDowngrade`](https://developer.android.com/reference/kotlin/androidx/room/RoomDatabase.Builder#fallbackToDestructiveMigrationOnDowngrade(kotlin.Boolean)) instead.