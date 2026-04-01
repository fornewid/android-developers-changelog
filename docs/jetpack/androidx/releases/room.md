---
title: https://developer.android.com/jetpack/androidx/releases/room
url: https://developer.android.com/jetpack/androidx/releases/room
source: md.txt
---

# Room

[User Guide](https://developer.android.com/training/data-storage/room) [Codelab](https://codelabs.developers.google.com/codelabs/android-room-with-a-view-kotlin/#0) API Reference  
[androidx.room](https://developer.android.com/reference/kotlin/androidx/room/package-summary)  
[androidx.room.migration](https://developer.android.com/reference/kotlin/androidx/room/migration/package-summary)  
[androidx.room.testing](https://developer.android.com/reference/kotlin/androidx/room/testing/package-summary)  
The Room persistence library provides an abstraction layer over SQLite to allow for more robust database access while harnessing the full power of SQLite.

| Latest Update | Stable Release | Release Candidate | Beta Release | Alpha Release |
|---|---|---|---|---|
| November 19, 2025 | [2.8.4](https://developer.android.com/jetpack/androidx/releases/room#2.8.4) | - | - | - |

## Declaring dependencies

To add a dependency on Room, you must add the Google Maven repository to your
project. Read [Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)
for more information.

Dependencies for Room include
[testing Room migrations](https://developer.android.com/training/data-storage/room#db-migration-testing) and
[Room RxJava](https://developer.android.com/training/data-storage/room/accessing-data#query-rxjava)

Add the dependencies for the artifacts you need in the `build.gradle` file for
your app or module:

### Kotlin

```kotlin
dependencies {
    val room_version = "2.8.4"

    implementation("androidx.room:room-runtime:$room_version")

    // If this project uses any Kotlin source, use Kotlin Symbol Processing (KSP)
    // See https://developer.android.com/build/migrate-to-ksp#add-ksp
    ksp("androidx.room:room-compiler:$room_version")

    // If this project only uses Java source, use the Java annotationProcessor
    // No additional plugins are necessary
    annotationProcessor("androidx.room:room-compiler:$room_version")

    // optional - Kotlin Extensions and Coroutines support for Room
    implementation("androidx.room:room-ktx:$room_version")

    // optional - RxJava2 support for Room
    implementation("androidx.room:room-rxjava2:$room_version")

    // optional - RxJava3 support for Room
    implementation("androidx.room:room-rxjava3:$room_version")

    // optional - Guava support for Room, including Optional and ListenableFuture
    implementation("androidx.room:room-guava:$room_version")

    // optional - Test helpers
    testImplementation("androidx.room:room-testing:$room_version")

    // optional - Paging 3 Integration
    implementation("androidx.room:room-paging:$room_version")
}
```

### Groovy

```groovy
dependencies {
    def room_version = "2.8.4"

    implementation "androidx.room:room-runtime:$room_version"

    // If this project uses any Kotlin source, use Kotlin Symbol Processing (KSP)
    // See https://kotlinlang.org/docs/ksp-quickstart.html to add KSP to your build
    ksp "androidx.room:room-compiler:$room_version"

    // If this project only uses Java source, use the Java annotationProcessor
    // No additional plugins are necessary
    annotationProcessor "androidx.room:room-compiler:$room_version"

    // optional - RxJava2 support for Room
    implementation "androidx.room:room-rxjava2:$room_version"

    // optional - RxJava3 support for Room
    implementation "androidx.room:room-rxjava3:$room_version"

    // optional - Guava support for Room, including Optional and ListenableFuture
    implementation "androidx.room:room-guava:$room_version"

    // optional - Test helpers
    testImplementation "androidx.room:room-testing:$room_version"

    // optional - Paging 3 Integration
    implementation "androidx.room:room-paging:$room_version"
}
```

For information on using the KAPT plugin, see the [KAPT documentation](https://kotlinlang.org/docs/kapt.html).

For information on using the KSP plugin, see the [KSP quick-start documentation](https://kotlinlang.org/docs/ksp-quickstart.html).

For information on using Kotlin extensions, see the [ktx documentation](https://developer.android.com/kotlin/ktx).

For more information about dependencies, see [Add Build Dependencies](https://developer.android.com/studio/build/dependencies).

Optionally, for non-Android libraries (i.e. Java or Kotlin only Gradle modules)
you can depend on `androidx.room:room-common` to use Room annotations.

## Configuring Compiler Options

Room has the following annotation processor options.

|---|---|
| `room.schemaLocation` | `directory` Enables exporting database schemas into JSON files in the given directory. See [Room Migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#test) for more information. |
| `room.incremental` | `boolean` Enables Gradle incremental annotation processor. Default value is `true`. |
| `room.generateKotlin` | `boolean` Generate Kotlin source files instead of Java. Requires KSP. Default value is `true` as of [version 2.7.0](https://developer.android.com/jetpack/androidx/releases/room#2.7.0). See [version 2.6.0](https://developer.android.com/jetpack/androidx/releases/room#2.6.0) notes, when it was introduced, for more details. |

### Use the Room Gradle Plugin

With Room version 2.6.0 and higher, you can use the Room Gradle Plugin to
configure options for the Room compiler. The plugin configures the project such
that generated schemas (which are an output of the compile tasks and are
consumed for auto-migrations) are correctly configured to have reproducible and
cacheable builds.

To add the plugin, in your top-level Gradle build file, define the
plugin and its version.

### Groovy

```groovy
plugins {
    id 'androidx.room' version "$room_version" apply false
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.room") version "$room_version" apply false
}
```

In the module-level Gradle build file, apply the plugin and use the `room`
extension.

### Groovy

```groovy
plugins {
    id 'androidx.room'
}

android {
    ...
    room {
        schemaDirectory "$projectDir/schemas"
    }
}
```

### Kotlin

```kotlin
plugins {
    id("androidx.room")
}

android {
    ...
    room {
        schemaDirectory("$projectDir/schemas")
    }
}
```

Setting a `schemaDirectory` is required when using the Room Gradle Plugin. This
will configure the Room compiler and the various compile tasks and its backends
(javac, KAPT, KSP) to output schema files into flavored folders, for example
`schemas/flavorOneDebug/com.package.MyDatabase/1.json`. These files should be
checked into the repository to be used for validation and auto-migrations.

Some options cannot be configured in all versions of the Room Gradle Plugin,
even though they are supported by the Room compiler. The table below lists each
option and shows the version of the Room Gradle Plugin that added support for
configuring that option using the `room` extension. If your version is lower,
or if the option is not supported yet, you can use
[annotation processor options](https://developer.android.com/jetpack/androidx/releases/room#annotation-processor-options) instead.

| Option | Since version |
|---|---|
| `room.schemaLocation` (required) | 2.6.0 |
| `room.incremental` | - |
| `room.generateKotlin` | - |

### Use annotation processor options

If you aren't using the Room Gradle Plugin, or if the option you want isn't
supported by your version of the plugin, you can configure Room using
annotation processor options, as described in
[Add build dependencies](https://developer.android.com/build/dependencies#processor-arguments). How you
specify annotation options depends on whether you use KSP or KAPT for Room.

### Groovy

```groovy
// For KSP
ksp {
    arg("option_name", "option_value")
    // other otions...
}

// For javac and KAPT
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                arguments += [
                    "option_name":"option_value",
                    // other options...
                    ]
            }
        }
    }
}
```

### Kotlin

```kotlin
// For KSP
ksp {
    arg("option_name", "option_value")
    // other options...
}

// For javac and KAPT
android {
    ...
    defaultConfig {
        ...
        javaCompileOptions {
            annotationProcessorOptions {
                arguments += mapOf(
                    "option_name" to "option_value",
                    // other options...
                )
            }
        }
    }
}
```

Because `room.schemaLocation` is a directory and not a primitive type, it is
necessary to use a `CommandLineArgumentsProvider` when adding this option so
that Gradle knows about this directory when conducting up-to-date checks.
[Migrate your Room database](https://developer.android.com/training/data-storage/room/migrating-db-versions#set_schema_location_using_annotation_processor_option)
shows a complete implementation of `CommandLineArgumentsProvider` that provides
the schema location.

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
[existing issues](https://issuetracker.google.com/issues?q=componentid:413107+status:open)
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=413107&template=1096568)

See the [Issue Tracker documentation](https://developers.google.com/issue-tracker)
for more information.

## Version 2.8

### Version 2.8.4

November 19, 2025

`androidx.room:room-*:2.8.4` is released. Version 2.8.4 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/84011c8ceb69163ef306a69e7f317202675eeb4b..75ef81cced187631f0dd74666188bd9d4cd3358f/room).

**Bug Fixes**

- Added a prepared statement cache to Room's connection pool when using a `SQLiteDriver` that does not internally have a pool, such as the `BundledSQLiteDriver`. This improves performance on repeated execution of the same SQL statement. ([5f43bc](https://android-review.googlesource.com/#/q/5f43bc4fa8ad4e19a1db2f2c9c1e7c5cd09e2c87), [b/319653917](https://issuetracker.google.com/319653917))
- Fix an issue where the actual / expected error message on schema validation was missing information. ([8b23da](https://android-review.googlesource.com/#/q/8b23da648c05461fb66b3f227db5f93259da417c), [b/454531083](https://issuetracker.google.com/454531083))
- Fix an issue with Room's Kotlin code generation missing `@Transaction` DAO functions with type variables. ([a8365d](https://android-review.googlesource.com/#/q/a8365de1779bdc7901f34ab4c6186fffea4acc75), [b/251316420](https://issuetracker.google.com/251316420))
- Improve Room's `SupportSQLite` Wrapper performance by avoiding thread hops maintaining the same blocking behaviour as the `SupportSQLiteDatabase` APIs. ([fc70e4](https://android-review.googlesource.com/#/q/fc70e487b804f94e5b5a1296213c14450e5582fb))

### Version 2.8.3

October 22, 2025

`androidx.room:room-*:2.8.3` is released. Version 2.8.3 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/a37d451cf0f84a1a567d5e79e2e7ca692f26be34..50911483989c265f0ee37fe881379b21cd9ac67f/room).

**Bug Fixes**

- Fix a performance issue with the Room SQLite Wrapper that was causing excessive JNI calls and significant performance degradation when iterating over a Cursor.

### Version 2.8.2

October 08, 2025

`androidx.room:room-*:2.8.2` is released. Version 2.8.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/29d2252aa09a2286891db24dd194967a89984962..a37d451cf0f84a1a567d5e79e2e7ca692f26be34/room).

**Bug Fixes**

- Fix a deadlock that could occur when re-opening an auto-closed database from a Flow emission ([b/446643789](https://issuetracker.google.com/446643789)).

### Version 2.8.1

September 24, 2025

`androidx.room:room-*:2.8.1` is released. Version 2.8.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0cf53e68a1c9a8a88886b1efd1aacc3f791351c9..29d2252aa09a2286891db24dd194967a89984962/room).

**Bug Fixes**

- Fix a processor crash that would occur when processing a DAO function with a suspend lambda. ([b/442220723](https://issuetracker.google.com/442220723)).
- Fix a race condition that would prevent Flows from receiving the latest updated.

### Version 2.8.0

September 10, 2025

`androidx.room:room-*:2.8.0` is released. Version 2.8.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/cae482df887aba2cf7d8b0d016366955f3856895..0cf53e68a1c9a8a88886b1efd1aacc3f791351c9/room).

**Important changes since 2.7.0:**

- Added a new artifact `androidx.room:room-sqlite-wrapper` which contains APIs to get a `SupportSQLiteDatabase` wrapper from a `RoomDatabase` with a configured `SQLiteDriver`. To get the wrapper use the new extension function `RoomDatabase.getSupportWrapper()`. This is a compatibility artifact to maintain usages of `SupportSQLiteDatabase`, usually obtained from `roomDatabase.openHelper.writableDatabase`, even if the Room database is configured with a `SQLiteDriver`. This wrapper is useful for incremental migration of codebases who wish to adopt SQLiteDriver APIs but have extensive usages of the SupportSQLite APIs yet they want to take advantage of the `BundledSQLiteDriver`. Checkout the [migration guide](https://developer.android.com/kotlin/multiplatform/room#migrate-from-support-sqlite) for more information.
- Added support for KMP targets Watch OS and Tv OS.
- Updated the library's Android minSDK from API 21 to API 23

### Version 2.8.0-rc02

August 27, 2025

`androidx.room:room-*:2.8.0-rc02` is released. Version 2.8.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2238b2db7ad0a9cd17e13afa5e21725583710e5..cae482df887aba2cf7d8b0d016366955f3856895/room).

**API Changes**

- Update the minSDK from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df), [b/380448311](https://issuetracker.google.com/issues/380448311), [b/435705964](https://issuetracker.google.com/issues/435705964), [b/435705223](https://issuetracker.google.com/issues/435705223))
- Update the minimum Android Gradle Plugin (AGP) version compatible with the Room Gradle Plugin from 8.1 to 8.4. ([Ia0d28](https://android-review.googlesource.com/#/q/Ia0d28a628a6de78c5aee3c6632e45e5ded567a3b))

**Bug Fixes**

- Fix an issue where a destructive migration was being performed even if a migration path was available for a pre-packaged database ([b/432634197](https://issuetracker.google.com/432634197)).

### Version 2.8.0-rc01

August 13, 2025

`androidx.room:room-*:2.8.0-rc01` is released. Version 2.8.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/e788f9f7947a19e5893e27b87e3d7e5be0921ff2..b2238b2db7ad0a9cd17e13afa5e21725583710e5/room).

**API Changes**

- Removing obsolete `@RequiresApi(21)` annotations ([Ic4792](https://android-review.googlesource.com/#/q/Ic47923dcc82f4b7c4638fadb10c2c0268b414fcd), [I9103b](https://android-review.googlesource.com/#/q/I9103beb2d5f73470f3abfdf034bc2b473be923e6))

**Bug Fixes**

- Fix a race condition where Room Flows would not emit the latest query result in an asynchronous multi-query/write situation. ([Ic9a3c](https://android-review.googlesource.com/#/q/Ic9a3c7c3470578d08467841e552845b4787ca8af))

### Version 2.8.0-beta01

August 1, 2025

`androidx.room:room-*:2.8.0-beta01` is released. Version 2.8.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..e788f9f7947a19e5893e27b87e3d7e5be0921ff2/room).

**Bug Fixes**

- Table and view names are now escaped properly during destructive migrations. ([9e55f8](https://android-review.googlesource.com/c/platform/frameworks/support/+/3702219), [b/427095319](https://issuetracker.google.com/427095319))

### Version 2.8.0-alpha01

July 16, 2025

`androidx.room:room-*:2.8.0-alpha01` is released. Version 2.8.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/room).

**New Features**

- Added a new artifact `androidx.room:room-sqlite-wrapper` which contains APIs to get a `SupportSQLiteDatabase` wrapper of `RoomDatabase` with a configured `SQLiteDriver`. To get the wrapper use the new extension function `RoomDatabase.getSupportWrapper()`. This is a compatibility artifact to maintain usages of `SupportSQLiteDatabase`, usually obtained from `RoomDatabase.openHelper.writableDatabase`, even if the Room database is configured with a `SQLiteDriver`. This wrapper is useful for incremental migration of codebases who wish to adopt `SQLiteDriver` but have extensive usages of the `SupportSQLite` APIs yet they want to take advantage of the `BundledSQLiteDriver`. ([Icf6ac](https://android-review.googlesource.com/#/q/Icf6ac2215f2b5f36b0a79081d431fd31df9e5901))
- Add KMP targets for Watch OS and TV OS ([I228f6](https://android-review.googlesource.com/#/q/I228f696505461888e870e6f47ab28d28c9cd2c2a), [b/394238801](https://issuetracker.google.com/issues/394238801))

**Bug Fixes**

- Fix a deadlock that could occasionally occur when using suspending transactions and the `AndroidSQLiteDriver`. ([b/415006268](https://issuetracker.google.com/issues/415006268))

## Version 2.7

### Version 2.7.2

June 18, 2025

`androidx.room:room-*:2.7.2` is released. Version 2.7.2 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/db199fa1cdf3ee91ee0a9aa2dc9c38c67fe1bf91..74f1496f0be2b5b29f86d368ea726c587d9981b7/room).

**Bug Fixes**

- Fix an issue where annotation values would be incorrectly read when processing native sources with KSP, sometimes missing schema exports. ([b/416549580](https://issuetracker.google.com/416549580))
- Fix a bug where leading comments in a SQL would cause statements to be executed as if they were non-read queries. ([b/413061402](https://issuetracker.google.com/413061402))
- Fix an issue with Room's Gradle Plugin failing to configure due to the schema directory being empty. ([b/417823384](https://issuetracker.google.com/417823384))
- No longer throw a `SQLiteException` when obtaining a connection takes too long, instead a log message will be sent by the library. Logging instead of throwing works around iOS suspending loopers causing Room to misinterpret the timeout that occurs in the Kotlin Coroutine acquiring the connection and thus preventing the exception from being thrown when an iOS app is backgrounded and later resumed in the middle of a database operation. ([b/422448815](https://issuetracker.google.com/422448815))

### Version 2.7.1

April 23, 2025

`androidx.room:room-*:2.7.1` is released. Version 2.7.1 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ba49ce890ee5d5dd8caf7246ad43ec01d6b9e0e6..db199fa1cdf3ee91ee0a9aa2dc9c38c67fe1bf91/room).

**Bug Fixes**

- Fix `IndexOutOfBoundsException` bug during provided type converter validation. ([b/409804755](https://issuetracker.google.com/409804755)).
- Support `RoomDatabase.runInTransaction()` when a `SQLiteDriver` is configured with Room. ([b/408364828](https://issuetracker.google.com/408364828)).

### Version 2.7.0

April 9, 2025

`androidx.room:room-*:2.7.0` is released. Version 2.7.0 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/55a3f2ab7dff00891c1744db27450f9f1471bff7..ba49ce890ee5d5dd8caf7246ad43ec01d6b9e0e6/room).

**Important changes since 2.6.0**

- **Kotlin Multiplatform (KMP) Support:** In this release, Room has been refactored to become a Kotlin Multiplatform (KMP) library. Current supported platforms are Android, iOS, JVM (Desktop), native Mac and native Linux. For more information on how to get started using Room KMP, please refer to the [official Room KMP documentation](https://developer.android.com/kotlin/multiplatform/room). As part of the KMP support, Room can also be configured with an [`SQLiteDriver`](https://developer.android.com/kotlin/multiplatform/sqlite), for information on how to migrate an existing app to the driver APIs and to Room KMP, see the [migration documentation](https://developer.android.com/kotlin/multiplatform/sqlite).
- **Kotlin Code Generation on KSP** has been turned ON by default if processing is done via KSP. For KAPT or Java only projects, Room will still generate Java sources.
- **Kotlin 2.0 and KSP2:** Room now targets Kotlin language 2.0 and will require projects to also compile with Kotlin 2.0 and equivalent or higher language version. Support for KSP2 is also added and is recommended when using Room with Kotlin 2.0 or higher.

### Version 2.7.0-rc03

March 26, 2025

`androidx.room:room-*:2.7.0-rc03` is released. Version 2.7.0-rc03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/353ae5d7857ddd6c4fffc20a360ac2ca5ebaf79a..55a3f2ab7dff00891c1744db27450f9f1471bff7/room).

**Bug Fixes**

- No longer throw `InterruptedException`when a thread is interrupted during the execution of Room blocking APIs, including blocking DAO functions ([b/400584611](https://issuetracker.google.com/400584611)).
- Re-implement Room's connection pool in an attempt to alleviate `SQLException: Error code: 5, message: Timed out attempting to acquire a reader connection.` and similar issues ([b/380088809](https://issuetracker.google.com/380088809)).

### Version 2.7.0-rc02

March 12, 2025

`androidx.room:room-*:2.7.0-rc02` is released. Version 2.7.0-rc02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b2f2de7ed39512b3a3bf7baafa35cb9461df1499..353ae5d7857ddd6c4fffc20a360ac2ca5ebaf79a/room).

**Bug Fixes**

- Fix Auto Migrations incorrectly handling a new column on an FTS table. ([b/348227770](https://issuetracker.google.com/348227770), [Ic53f3](https://android-review.googlesource.com/#/q/Ic53f33be4140a95d76bc9a1bd40f3554684781ac))
- Fix a room-compiler crash due to a `NullPointerException` when processing non-JVM sources via KSP. ([b/396607230](https://issuetracker.google.com/396607230), [I693c9](https://android-review.googlesource.com/#/q/I693c912910dd5dd7cfae73abef18e9076c11f0af))
- Fix an issue where Room would not invalidate tables at the end of using the writer connection. ([b/340606803](https://issuetracker.google.com/340606803), [I73ef6](https://android-review.googlesource.com/#/q/I73ef6de36166bd339e388196a4cfd559669a8e66))

### Version 2.7.0-rc01

February 26, 2025

`androidx.room:room-*:2.7.0-rc01` is released. Version 2.7.0-rc01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..b2f2de7ed39512b3a3bf7baafa35cb9461df1499/room).

**Bug Fixes**

- Fix an issue where Room would not be setting the `busy_timeout` in the initial database connection that would lead to `SQLException: Error code: 5, message: database is locked` issues ([I93208](https://android-review.googlesource.com/#/q/I9320856f64363b05bcf6407eed0efe36ef3312a3), [b/380088809](https://issuetracker.google.com/380088809)).
- Fix an issue in Room's compiler that would cause the KSP processor to crash when processing native source sets (such as iOS) on Kotlin 2.1.x and KSP1 ([I883b8](https://android-review.googlesource.com/#/q/I883b890f6e844ef3efd351ed7c5cf3004969e44c), [b/396607230](https://issuetracker.google.com/396607230)).

### Version 2.7.0-beta01

February 12, 2025

`androidx.room:room-*:2.7.0-beta01` is released. Version 2.7.0-beta01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f383921582ae43bfe6fb2f11d71b8ace3f9ceb65..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/room).

**Bug Fixes**

- Fix an issue with `RoomDatabase.inTransaction()` opening a closed database when it shouldn't and should quickly return false if the database is closed ([b/325432967](https://issuetracker.google.com/issues/325432967)).
- Fix a crash (`IllegalArgumentException: not a valid name`) in Room's compiler when processing DAO functions with Kotlin inline / value classes ([b/388299754](https://issuetracker.google.com/issues/388299754)).
- Include Proguard rules in the JVM artifact of `room-runtime` so that the default constructor of the generated database implementation is not removed since it is used by Room's default initialization that uses reflection ([b/392657750](https://issuetracker.google.com/issues/392657750)).

### Version 2.7.0-alpha13

January 29, 2025

`androidx.room:room-*:2.7.0-alpha13` is released. Version 2.7.0-alpha13 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..f383921582ae43bfe6fb2f11d71b8ace3f9ceb65/room).

**API Changes**

- Room now targets Kotlin language 2.0 and will require projects to also compile with Kotlin 2.0 and equivalent or high language version. ([I8efb0](https://android-review.googlesource.com/#/q/I8efb015c88682921780370c8bed5931d9933a319), [b/315461431](https://issuetracker.google.com/issues/315461431), [b/384600605](https://issuetracker.google.com/issues/384600605))

**Bug Fixes**

- Fix an issue in Room KMP database builder when a simple name instead of a path was used in Android and the database file resolved path would not be located in the app's data directory. ([I83315](https://android-review.googlesource.com/#/q/I833154e2855a38520e5a0e8c802964bd455000e8), [b/377830104](https://issuetracker.google.com/issues/377830104))
- Fix an issue with the Room Gradle Plugin where configuring the schema inputs and output was causing an issue on Android projects: `property 'inputDirectory' is final and cannot be changed any further.` ([1dbb4c](https://android-review.googlesource.com/#/q/1dbb4c1876e1e8a8e930bec4625741ac6dc05a0b), [b/376071291](https://issuetracker.google.com/issues/376071291))
- Add support for KSP2 in Room Gradle Plugin fixing an issue where the schema directory was not being properly set up by the plugin. ([Iec3c4](https://android-review.googlesource.com/#/q/Iec3c435cbdfb994034500668f1ec602d5ebde3ce), [b/379159770](https://issuetracker.google.com/issues/379159770))

**External Contribution**

- Fix an issue with `Room` paging integration causing UI jumps when the initial key to refresh is too close to the end of the list. Thanks to Eva! ([I2abbe](https://android-review.googlesource.com/#/q/I2abbe92633bf95aa3306e4c2ebc47eacebfffa8c), [b/389729367](https://issuetracker.google.com/issues/389729367))

### Version 2.7.0-alpha12

December 11, 2024

`androidx.room:room-*:2.7.0-alpha12` is released. Version 2.7.0-alpha12 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..46295bc0b75a16f452e8e0090e8de41073d4dbb6/room).

**API Changes**

- Add the experimental API `RoomDatabase.Builder.setInMemoryTrackingMode()` to configure whether Room will use an in-memory table or not for invalidation tracking. ([I2a9b2](https://android-review.googlesource.com/#/q/I2a9b2784f3418ece9814e3c077aef512309cdc26), [b/185414040](https://issuetracker.google.com/issues/185414040))

**Bug Fixes**

- Destructive migrations now drop views to ensure they are recreated, aligning behavior when `allowDestructiveMigrationForAllTables` is ON (KMP default) with the existing behavior when it's OFF. ([0a3e83](https://android-review.googlesource.com/3392720), [b/381518941](https://issuetracker.google.com/381518941))

### Version 2.7.0-alpha11

October 30, 2024

`androidx.room:room-*:2.7.0-alpha11` is released. Version 2.7.0-alpha11 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/room).

**API Changes**

- Revisit the newly added `convertRows()` method signature to be a suspend function that receives a `RawRoomQuery` for room-paging. ([Ie57b5](https://android-review.googlesource.com/#/q/Ie57b558e217ce995a7d3dfe772c314aabbfcda8c), [b/369136627](https://issuetracker.google.com/issues/369136627))

**Bug Fixes**

- Fixed the issue in room-paging where invalid code was being generated when using `@Relation` in conjunction with `PagingSource`.

### Version 2.7.0-alpha10

October 16, 2024

`androidx.room:room-*:2.7.0-alpha10` is released. Version 2.7.0-alpha10 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/room).

**API Changes**

- Create internal `ByteArrayWrapper` class to support Relations with `ByteBuffer` in non-Android \& non-JVM platforms. ([I75543](https://android-review.googlesource.com/#/q/I755433b8d624c88a6d645d40cf845d9bd3123398), [b/367205685](https://issuetracker.google.com/issues/367205685))
- Add `SQLiteStatement.getColumnType()` along with the various `SQLITE_DATA_*` result constants to enable retrieving the data type of a column. ([I1985c](https://android-review.googlesource.com/#/q/I1985c7b267ba4d6342cb487cbe6e889bed3ff26d), [b/369636251](https://issuetracker.google.com/issues/369636251))

### Version 2.7.0-alpha09

October 2, 2024

`androidx.room:room-*:2.7.0-alpha09` is released. Version 2.7.0-alpha09 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/room).

**Bug Fixes**

- Fix an issue with the KMP implementation of `room-paging` that would cause an `Error code: 8, message: attempt to write a readonly database` due to starting a write transaction on a read connection. ([b/368380988](https://issuetracker.google.com/368380988))

### Version 2.7.0-alpha08

September 18, 2024

`androidx.room:room-*:2.7.0-alpha08` is released. Version 2.7.0-alpha08 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..0431b84980e97d6bafdfda7c9038bc4d9529564f/room).

**New Features**

- The `room-paging` artifacts have been migrated to be KMP compatible. ([Ib8756](https://android-review.googlesource.com/#/q/Ib875670e864fba5fbf2a2835d81713d8823724c6), [b/339934824](https://issuetracker.google.com/issues/339934824))
- The API `invalidationTrackerFlow()` has been commonized as a first-party API as `InvalidationTracker.createFlow()` and is now available for non-Android source sets in KMP projects. ([I1fbfa](https://android-review.googlesource.com/#/q/I1fbfa9a45041f774eb08ee9d6457a2cde6a236a1), ([I8fb29](https://android-review.googlesource.com/#/q/I8fb29221e382b7a78259c47d9d93add4c59584ce)), [b/329291639](https://issuetracker.google.com/issues/329291639), [b/329315924](https://issuetracker.google.com/issues/329315924))

**API Changes**

- All warnings and error messages in Room that use the word `Cursor` have been removed or replaced, as `Cursor` is no longer an accurate general term to use in the KMP version of Room. ([Id8cd9](https://android-review.googlesource.com/#/q/Id8cd9a6a58809fd974808605b60b8c7ec5f853e8), [b/334087492](https://issuetracker.google.com/issues/334087492))

**Bug Fixes**

- Fixed an issue where Room KMP would try to emit code using `UUID` for non-JVM platforms. ([b/362994709](https://issuetracker.google.com/362994709))
- Fixed an issue with the Room Gradle Plugin that would cause an error such as 'Cannot change attributes of configuration ... after it has been locked for mutation' when being used in a KMP project with Compose Multiplatform. ([b/343408758](https://issuetracker.google.com/343408758))

### Version 2.7.0-alpha07

August 21, 2024

`androidx.room:room-*:2.7.0-alpha07` is released. Version 2.7.0-alpha07 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/851bf84c0a2be5c65b9a8ad1add25fc42d701f48..8c4071562bd7e22b937284d71fb7aca9c4cd662c/room).

**New Features**

- The Room Gradle Plugin will now automatically add the exported schemas into the Android Instrumentation Test resource sources so they can be used by the `MigrationTestHelper`.

**Bug Fixes**

- Fixed an issue with the generated 'actual' of the `RoomDatabaseConstructor` missing the 'actual' modifier in the `initialize` function if such function is also overridden in the 'expect' declaration. ([359631627](https://issuetracker.google.com/359631627))
- Fixed an issue with the generated 'actual' of the `RoomDatabaseConstructor` not matching the visibility of the 'expect' declaration. ([358138953](https://issuetracker.google.com/358138953))

### Version 2.7.0-alpha06

August 7, 2024

`androidx.room:room-*:2.7.0-alpha06` is released. Version 2.7.0-alpha06 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..851bf84c0a2be5c65b9a8ad1add25fc42d701f48/room).

**API Changes**

- Change the instantiation setup for a `RoomDatabase` in a KMP project.

Due to Kotlin 2.0 compilation model, the strategy of referencing a to-be-generated function, named `instantiateImpl()` is longer viable. Two new APIs, `@ConstructedBy` and `RoomDatabaseConstructor` are introduced that replace the `instantiateImpl()` strategy. The new strategy is as follow:

1. Define an expect object that implements `RoomDatabaseConstructor`

         expect object MyDatabaseCtor : RoomDatabaseConstructor<MyDatabase>

2. Link the object with the `@Database` declaration using `@ConstructedBy`

         @Database(...)
         @ConstructedBy(MyDatabaseCtor::class) // NEW
         abstract class MyDatabase : RoomDatabase

3. Create a new database instance but without passing a factory argument

         fun createNewDatabase(path: String) =
           Room.databaseBuilder<AppDatabase>(name = path)
             .setDriver(BundledSQLiteDriver())
             .setQueryCoroutineContext(Dispatchers.IO)
             .build()

Fixes [b/316978491](https://issuetracker.google.com/issues/316978491),
[b/338446862](https://issuetracker.google.com/issues/338446862), and
[b/342905180](https://issuetracker.google.com/issues/342905180)

- Support for `@RawQuery` in Room KMP by adding a new API called `RoomRawQuery` that is similar to `SupportSQLiteQuery` in terms of holding into the raw SQL string and a function to bind arguments into a statement. `@RawQuery` annotated functions can now accept a `RoomRawQuery` as their single parameter. ([Iea844](https://android-review.googlesource.com/#/q/Iea84484b18c0c969b4012977e737eb12c4b4f2c6), [b/330586815](https://issuetracker.google.com/issues/330586815))
- Add an overload of `setQueryCallback()` that accepts a `CoroutineContext`. ([Id66ff](https://android-review.googlesource.com/#/q/Id66ff055ce126085d50cad15f8982ad88c34267e), [b/309996304](https://issuetracker.google.com/issues/309996304))
- Added support for `linuxArm64` Kotlin Multiplatform targets ([I139d3](https://android-review.googlesource.com/#/q/I139d36226a3d06d9768bd63302de98b576a12a48), [b/338268719](https://issuetracker.google.com/issues/338268719))

**Bug Fixes**

- Fix an issue where Room would incorrectly generate a call to `recursiveFetchArrayMap` in non-Android targets. ([710c36](https://android-review.googlesource.com/#/q/3b10c6e1a87df1f97e64364f1dd1a15ec9710c36), [b/352482325](https://issuetracker.google.com/issues/352482325))
- Fix an issue where sometimes Room would throw an exception about 'Timed out attempting a connection' in a KMP project. ([fa72d0](https://android-review.googlesource.com/#/q/241d1fe6eaf04405a4d3118384d7831a69fa72d0), [b/347737870](https://issuetracker.google.com/issues/347737870))
- Fix an issue in auto-migrations that would check for foreign keys too early before other tables changed their schemas to conform to the new foreign keys. ([7672c0](https://android-review.googlesource.com/#/q/a499a0c267f712fcc62d8227d23878a5757672c0), [b/352085724](https://issuetracker.google.com/issues/352085724))

### Version 2.7.0-alpha05

July 10, 2024

`androidx.room:room-*:2.7.0-alpha05` is released. Version 2.7.0-alpha05 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..56579bc30499ce39f0d7a6713a065b00c6194206/room).

**API Changes**

- Renamed `SQLiteKt` to `SQLite` and `BundledSQLiteKt` to `BundledSQLite`. ([I8b501](https://android-review.googlesource.com/#/q/I8b5016b9769244342bab288bab976ebe9fe5d11d))

**Bug Fixes**

- Fixed a bug where a `RoomDatabase` would deadlock or error out with a connection timeout when using the `AndroidSQLiteDriver`.

### Version 2.7.0-alpha04

June 12, 2024

`androidx.room:room-*:2.7.0-alpha04` is released. Version 2.7.0-alpha04 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..f5541f29d045c6ba9734689ec67891f8d667412b/room).

**Bug Fixes**

- Fixed an issue in Room's annotation processor would generate incompatible KMP code when a multi-map return type was defined in a DAO. ([b/340983093](https://issuetracker.google.com/340983093))
- Fixed an issue where Room would fail to find the generated database implementation if the `@Database` annotated class had no package. ([b/342097292](https://issuetracker.google.com/342097292))
- Fixed an issue where enabling auto-close and multi-instance invalidation would sometimes cause a `ConcurrentModificationException` when the database was auto-closed due to being idle.

### Version 2.7.0-alpha03

May 29, 2024

`androidx.room:room-*:2.7.0-alpha03` is released. Version 2.7.0-alpha03 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/room).

**Bug Fixes**

- Fix various issues regarding Kotlin 2.0 and KSP 2.0. Note that Kotlin 2.0 with KSP 2 support is not complete and the team is working on the various APIs and behavior changes in the new compiler. ([b/314151707](https://issuetracker.google.com/issues/314151707))

### Version 2.7.0-alpha02

May 14, 2024

`androidx.room:room-*:2.7.0-alpha02` is released. Version 2.7.0-alpha02 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/291c06f46eebb10fbf9d07b9d36e41dd1bd6f980..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/room).

**Bug Fixes**

- Fixed various KSP issues.

### Version 2.7.0-alpha01

May 1, 2024

`androidx.room:room-*:2.7.0-alpha01` is released. Version 2.7.0-alpha01 contains [these commits](https://android.googlesource.com/platform/frameworks/support/+log/291c06f46eebb10fbf9d07b9d36e41dd1bd6f980/room).

**New Features**

- **Kotlin Multiplatform (KMP) Support**: In this release, Room has been refactored to become a Kotlin Multiplatform (KMP) library. Although there is still some work to be done, this release introduces a new version of Room where the majority of the functionality has been "common-ized" (made to be multiplatform). Current supported platforms are Android, iOS, JVM (Desktop), native Mac and native Linux. Any missing functionality in the newly supported platforms will be made "feature-complete" in upcoming Room releases.

For more information on how to get started using Room KMP, please refer to the [official Room KMP documentation](https://developer.android.com/kotlin/multiplatform/room).

- **Kotlin Code Generation on KSP** has been turned ON by default if processing is done via KSP. For KAPT or Java only projects, Room will still generate Java sources.

**API Changes**

- An overload of `Room.databaseBuilder()` has been added that takes a lambda parameter that is meant to be used with a Room generated function to avoid using reflection when instantiating the generated `RoomDatabase` implementation. Example usage is:

    Room.databaseBuilder<MyDatabase>(
        context = appContext,
        name = dbFilePath,
        factory =  { MyDatabase::class.instantiateImpl() }
    )

- An API for configuring a Room with a `CoroutineContext` has been added to the builder: `RoomDatabase.Builder.setQueryCoroutineContext`. Note that a `RoomDatabase` can only be configured with either executors using `setQueryExecutor` or with a Coroutine context but not both.
- An API for configuring Room with a `SQLite` Driver has been added: `RoomDatabase.Builder.setDriver()`. For more information about the `SQLite` Driver API refer to the [SQLite KMP documentation](https://developer.android.com/kotlin/multiplatform/sqlite)
- APIs for accessing the underlying `SQLiteConnection` from driver APIs have been added: `RoomDatabase.useReaderConnection` and `RoomDatabase.useWriterConnection`.
- Varios Room related callbacks now have an overloaded version that receive `SQLiteConnection` instead of `SupportSQLiteDatabase`. These are intended to be overridden when migrating to a KMP project. For more information about migrating Room usages in an Android app to a common KMP module refer to the [migration guide](https://developer.android.com/training/data-storage/room/room-kmp-migration). The callbacks are:
  - `Migration.migrate(SQLiteConnection)`
  - `AutoMigrationSpec.onPostMigrate(SQLiteConnection)`
  - `RoomDatabase.Callback.onCreate(SQLiteConnection)`
  - `RoomDatabase.Callback.onDestructiveMigration(SQLiteConnection)`
  - `RoomDatabase.Callback.onOpen(SQLiteConnection)`
- The KTX artifact `androidx.room:room-ktx` has been merged to `androidx.room:room-runtime` along with all its APIs, the artifact is now blank. Please remove it from your dependency list.

## Version 2.6

### Version 2.6.1

November 29, 2023

`androidx.room:room-*:2.6.1` is released. [Version 2.6.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ec9bfe9db962dfb9b86a707c0b84ff1e24ef3c7d..04d99ffb15b386a8708eb883c780d45a3a5cece8/room)

**Bug Fixes**

- Resolved issue in generated code where the default value for Double columns in `EntityCursorConverter` was being set to 0 instead of 0.0. A potential fix for a similar edge-case for Float type columns has also been included. ([Id75f5](https://android-review.googlesource.com/q/commit:6aa7e7e786298cad202cda711e05d514cf50fe30), [b/304584179](https://issuetracker.google.com/304584179))
- Exceptions thrown from `PagingSource` loads will now be propagated as a `LoadStateUpdate` of `LoadResult.Error` containing the Throwable. This error state is observable through `PagingDataAdapter.loadStateFlow(Views)` or `LazyPagingItems.loadState(Compose)`. Note that this marks a behavioral change where in the past load errors will bubble up as an Exception thrown by the dao method that triggered the load. ([I93887](https://android-review.googlesource.com/#/q/I93887de62a4fc76d1abe4ade60ed524a41d9d4e8), [b/302708983](https://issuetracker.google.com/issues/302708983))

### Version 2.6.0

October 18, 2023

`androidx.room:room-*:2.6.0` is released. [Version 2.6.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5b7df8b23daa6000a04ba680f5d5979df6fd2560..ec9bfe9db962dfb9b86a707c0b84ff1e24ef3c7d/room)

**Important changes since 2.5.0**

- The option to enable Kotlin code generation (or "Kotlin CodeGen") is now available in Room KSP. ([4297ec0](https://android.googlesource.com/platform/frameworks/support/+/4297ec00790d6d88f86c6c5d9dfb9a260a7131ad)). To turn on Kotlin CodeGen in Room, add the `room.generateKotlin` option name to your processor options for KSP. For more details on how to pass processor options for KSP, see the [KSP documentation](https://kotlinlang.org/docs/ksp-quickstart.html#pass-options-to-processors).

**Note:** When using Kotlin CodeGen, it is important to note that there are additional restrictions that have been added. Abstract properties as DAO getters or DAO queries in Kotlin CodeGen are disallowed, and instead expected to be rewritten as functions to avoid the false notion that the property value is immutable and has a fixed stored result. Another restriction that has been added is that Nullable collection return types are no longer allowed in Room for Kotlin CodeGen.

**Warning:** You may find that your projects are more strict in terms of nullability when using Kotlin CodeGen. In Kotlin CodeGen, the nullability of type arguments is important, wheras in Java this is mostly ignored. For example, let's say you have a \`Flow\` return type and the table is empty. In Java CodeGen, this will not cause any issues, but in Kotlin CodeGen, you will get an error. To avoid this, you will need to use \`Flow\`, assuming a null is emitted.

- The new artifact for the Room Gradle Plugin has been added to Room with the id `androidx.room`, which solves various existing issues in Room regarding having inputs and outputs of schemas via Gradle annotation processor options. For more details, refer to the [Room Version 2.6.0-alpha02 release notes](https://developer.android.com/jetpack/androidx/releases/room#2.6.0-alpha02).
- Value classes in Room Entities are now supported for KSP. ([4194095](https://android.googlesource.com/platform/frameworks/support/+/4194095366032c1c06d9e472e4e78b822c82cbe6))
- Nested Map return types in DAO functions are now supported in Room. ([I13f48](https://android.googlesource.com/platform/frameworks/support/+/3c46fef7382077611c9d9b4cb330bc52373ccc6d), [203008711](https://issuetracker.google.com/issues/203008711))

### Version 2.6.0-rc01

September 20, 2023

`androidx.room:room-*:2.6.0-rc01` is released. [Version 2.6.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e66623af18d7217bf7988b41e431f210a3150223..5b7df8b23daa6000a04ba680f5d5979df6fd2560/room)

### Version 2.6.0-beta01

August 23, 2023

`androidx.room:room-*:2.6.0-beta01` is released. [Version 2.6.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..3315f1ef094c312203fe26841287902916fbedf5/room)

**Bug Fixes**

- Handling the special case `SQLite` exception during upsert encountered when the `2067 SQLITE_CONSTRAINT_UNIQUE` exception is thrown during an upsert, upsert should perform an update. ([If2849](https://android.googlesource.com/platform/frameworks/support/+/01002bedc549e0264a5f920dc554ed7dd7785cfe), [b/243039555](https://issuetracker.google.com/243039555))

### Version 2.6.0-alpha03

August 9, 2023

`androidx.room:room-*:2.6.0-alpha03` is released. [Version 2.6.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..5d7dd999525725bd038a00ca4e89e0fef624a6da/room)

**New Features**

- Nested Map return types in DAO functions are now supported in Room. ([I13f48](https://android.googlesource.com/platform/frameworks/support/+/3c46fef7382077611c9d9b4cb330bc52373ccc6d), [203008711](https://issuetracker.google.com/issues/203008711))

**API Changes**

- A new type annotation called `@MapColumn` has been created to replace `@MapInfo`, which is now deprecated. For each column name (`keyColumnName`, `valueColumnName`, or both) provided in a `@MapInfo` annotation, you will need to declare a `@MapColumn` annotation with just the `columnName` and use the annotation on the specific type argument that is being referenced (the key or value of the Map) in the return type of the DAO function. This is because the `@MapColumn` annotation is used directly on the type argument within the return type of a DAO function, instead of on the function itself like `@MapInfo`. For more information, please refer to the `@MapColumn` documentation. ([Ib0305](https://android-review.googlesource.com/#/q/Ib0305c9ba7c0bd73fd885f22b5fac4f6c90f0b24), [b/203008711](https://issuetracker.google.com/issues/203008711))
- Updated API files to annotate compatibility suppression ([I8e87a](https://android-review.googlesource.com/#/q/I8e87ae292b38fac1886001f5317acda1592f174b), [b/287516207](https://issuetracker.google.com/issues/287516207))
- The Room Gradle plugin APIs have been updated to not always require per-variant configurations. This means that the plugin can accept a global location for all variants without creating multiple directories, enabling smoother migrations that but is also flexible enough to manually configure flavors or build type schemas while still retaining the benefits of the plugin (reproducible and cacheable builds). ([I09d6f](https://android.googlesource.com/platform/frameworks/support/+/ef1265ecca338a7bb3929def8085236d45ace500.), [b/278266663](https://issuetracker.google.com/278266663))

**Bug Fixes**

- Fixed potential memory leak vulnerability in `QueryInterceptorStatement`. ([I193d1](https://android.googlesource.com/platform/frameworks/support/+/22935cee019fb17ba23ddbf3768700552940d205))
- Fixed incorrect behavior in the `QueryInterceptorDatabase execSQL()` function. ([Iefdc8](https://android.googlesource.com/platform/frameworks/support/+/80d2aff497f0becfcda53b3e6195bb0ca3e79c9f))

### Version 2.6.0-alpha02

June 21, 2023

`androidx.room:room-*:2.6.0-alpha02` is released. [Version 2.6.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..3b5b931546a48163444a9eddc533489fcddd7494/room)

**Room Gradle Plugin**

This new release contains a new artifact for the Room Gradle Plugin with id `androidx.room`, which solves various existing issues in Room regarding having inputs and outputs of schemas via Gradle annotation processor options. The Room Gradle Plugin configures the project such that generated schemas that are consumed for auto-migrations and are output of the compile tasks are correctly configured to have reproducible and cacheable builds. The plugin offers a DSL to configure the base schema location:

    room {
        schemaDirectory("$projectDir/schemas/")
    }

The plugin will then configure the Room compiler and the various compile tasks and its backends (javac, KAPT, KSP) to output schema files into flavored folders, i.e. `schemas/flavorOneDebug/com.package.MyDatabase/1.json`. As usual these files are checks-in into the repository to be used for validation and auto-migrations. Upon migrating to using the plugin instead of the annotation processor options the existing schema files must be copied to the generated flavor directories created by the plugin, this is a one-time migration operation that must be done manually. The schema documentation in [developers.android.com](https://developer.android.com/) will be updated in the future once feedback is addressed and the plugin reaches stable, so please give it a try.

**API Changes**

- `RoomDatabase.QueryCallback` has been defined as a functional interface to allow SAM conversion usages. ([Iab8ea](https://android-review.googlesource.com/#/q/Iab8eafa11bf7f6fde9d6c0a7ce7e2933cd248841), [b/281008549](https://issuetracker.google.com/issues/281008549))

**Bug Fixes**

- Resolving issue arising when instantiating the database in Robolectric after the migration of Room sources from Java to Kotlin. ([Ic053c](https://android-review.googlesource.com/c/platform/frameworks/support/+/2507218), [b/274924903](https://issuetracker.google.com/issues/274924903))

### Version 2.6.0-alpha01

March 22, 2023

`androidx.room:room-*:2.6.0-alpha01` is released. [Version 2.6.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e45926c282f76fcba0b4e86bfa74bc6e5a5ca642..5e7d256f82fbafb6d059ab7b18fddd87c7531553/room)

**New Features**

- Supporting value classes in Room for KSP. Room is now able to support value classes in Entities. ([4194095](https://android.googlesource.com/platform/frameworks/support/+/4194095366032c1c06d9e472e4e78b822c82cbe6))
- Kotlin code generation(or "Kotlin CodeGen") can now be enabled in Room ([4297ec0](https://android.googlesource.com/platform/frameworks/support/+/4297ec00790d6d88f86c6c5d9dfb9a260a7131ad)). To turn on Kotlin CodeGen in Room, add the `room.generateKotlin` option name to your processor options for KSP. For more details on how to pass processor options for KSP, see the [KSP documentation](https://kotlinlang.org/docs/ksp-quickstart.html#pass-options-to-processors).

**Note:** When using Kotlin CodeGen, it is important to note that there are additional restrictions that have been added. Abstract properties as DAO getters or DAO queries in Kotlin CodeGen are disallowed, and instead expected to be rewritten as functions to avoid the false notion that the property value is immutable and has a fixed stored result. Another restriction that has been added is that Nullable collection return types are no longer allowed in Room for Kotlin CodeGen.

**Warning:** You may find that your projects are more strict in terms of nullability when using Kotlin CodeGen. In Kotlin CodeGen, the nullability of type arguments is important, wheras in Java this is mostly ignored. For example, let's say you have a \`Flow\` return type and the table is empty. In Java CodeGen, this will not cause any issues, but in Kotlin CodeGen, you will get an error. To avoid this, you will need to use \`Flow\`, assuming a null is emitted.

**API Changes**

- Guarding against meaningless usage of nullable collections in DAO method return types. ([I777dc](https://android-review.googlesource.com/#/q/I777dca93da0fb30e1712bcbd20dbf57044cdbc2a), [b/253271782](https://issuetracker.google.com/issues/253271782), [b/259426907](https://issuetracker.google.com/issues/259426907))
- Add an API for creating a Flow that emits invalidation tracker changes. The API is useful for creating streams that need to react to database changes. ([I8c790](https://android-review.googlesource.com/#/q/I8c7904f0d630bfc48574af96e288e8c7b5bf777a), [b/252899305](https://issuetracker.google.com/issues/252899305))

**Bug Fixes**

- Disallow abstract properties as DAO getters or DAO queries in Kotlin codegen, instead they should be rewritten as functions to avoid the false notion that the property value is immutable and has a fixed stored result. ([If6a13](https://android-review.googlesource.com/#/q/If6a13382b351fbcf9072a40c496d600cd329fd38), [b/127483380](https://issuetracker.google.com/issues/127483380), [b/257967987](https://issuetracker.google.com/issues/257967987))

## Version 2.5.2

### Version 2.5.2

June 21, 2023

`androidx.room:room-*:2.5.2` is released. [Version 2.5.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2f3269d9f8da6386519f59da82b374779e22c515..0c21d31673c507b0cddf8cf3b21235810f879a39/room)

**Bug Fixes**

- Fix an incompatibility issue with the kotlinx-metadata-jvm. ([386d5c](https://android-review.googlesource.com/#/q/29dfed77605e8f58a1acc6c452f4c70d5a386d5c))
- Fix an issue that causes Room to throw an error when being used in a Robolectric test. ([f79bea](https://android-review.googlesource.com/#/q/05f5f7173f40b012dc58c773391ed72336f79bea), [b/274924903](https://issuetracker.google.com/issues/274924903))

## Version 2.5.1

### Version 2.5.1

March 22, 2023

`androidx.room:room-*:2.5.1` is released. [Version 2.5.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/e45926c282f76fcba0b4e86bfa74bc6e5a5ca642..2f3269d9f8da6386519f59da82b374779e22c515/room)

**Bug Fixes**

- Avoid checking the database parent directory in `FrameworkSQLiteHelper` if the database is already open. ([5de86b8](https://android.googlesource.com/platform/frameworks/support/+/5de86b82c00590651c4b60acddf7873b1a1e4509))
- Use an `isOpenInternal` check when checking if the database is already open. ([e91fb35](https://android.googlesource.com/platform/frameworks/support/+/e91fb356ef871317583b8dad84d0ee0eedbf9978))
- Better handling of the reentrant case in `acquireTransactionThread()` of `Room` is now available. ([219f98b](https://android.googlesource.com/platform/frameworks/support/+/219f98b7526323e0fac23b6e84136419ba4768df)). During a suspending transaction, Room uses a thread from the transaction executor, starts an event loop in it and dispatches suspending database operations to it so they are all encapsulated within the transaction coroutine. It is usually expected that the transaction thread is different from the one starting the transaction, but in some cases they are the same. To handle such reentrant cases the `withTransaction()` has been refactored to no longer rely on a control job and instead it will execute the suspending transaction block from within the `runBlocking` in the transaction thread.

## Version 2.5.0

### Version 2.5.0

February 22, 2023

`androidx.room:room-paging-guava:2.5.0`, `androidx.room:room-paging-rxjava2:2.5.0`, and `androidx.room:room-paging-rxjava3:2.5.0` are released. [Version 2.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..e45926c282f76fcba0b4e86bfa74bc6e5a5ca642/room)

### Version 2.5.0

January 11, 2023

`androidx.room:room-*:2.5.0` is released. [Version 2.5.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/18e4de7c7333c7b4451036bba19d03090dabd38a..e45926c282f76fcba0b4e86bfa74bc6e5a5ca642/room)

**Important changes since 2.4.0**

- All of `room-runtime` sources has been converted from Java to Kotlin. Note that you may encounter source incompatibility issues if your code is in Kotlin due to the library conversion to Kotlin. For example, a known source incompatible change is that in `InvalidationTracker` you will now need to declare `onInvalidate()` in `Observer` to have a param of type `Set` and not `MutableSet`. Moreover, certain getter methods were converted to properties requiring the property access syntax on Kotlin files. Please file a bug if there are any significant incompatibilities.
- Added a new shortcut annotation, `@Upsert`, which attempts to insert an entity when there is no uniqueness conflict or update the entity if there is a conflict. ([I7aaab](https://android-review.googlesource.com/#/q/I7aaab5416551ed70e0130a60b6b629a531757a16), [b/241964353](https://issuetracker.google.com/issues/241964353))
- New room-paging artifacts `room-paging-rxjava2`, `room-paging-rxjava3` and `room-paging-guava` have been added for support in Room Paging.
- Added APIs for providing key and value tables names for disambiguation in `@MapInfo` ([Icc4b5](https://android-review.googlesource.com/#/q/Icc4b50a029d33c49fbfe7265d10b6be1b15da9c3))

### Version 2.5.0-rc01

December 7, 2022

`androidx.room:room-*:2.5.0-rc01` is released. [Version 2.5.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6ecaa0b12494ad2afa228180adbbe811cfd89dc1..18e4de7c7333c7b4451036bba19d03090dabd38a/room)

- This release is identical to `2.5.0-beta02`.

### Version 2.5.0-beta02

November 9, 2022

`androidx.room:room-*:2.5.0-beta02` is released. [Version 2.5.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..6ecaa0b12494ad2afa228180adbbe811cfd89dc1/room)

**API Changes**

- Fix various APIs that take query arguments from invariant (`Array<Any?>`) to contravariant (`Array<out Any?>`) to match Java's array behavior. ([b/253531073](https://issuetracker.google.com/issues/253531073))

### Version 2.5.0-beta01

October 5, 2022

`androidx.room:room-*:2.5.0-beta01` is released. [Version 2.5.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/room)

**API Changes**

- Restrict the minimum version that supports `@Upsert` to be API 16. This is due to the inability to identity a primary key constraint conflict in older APIs. ([I5f67f](https://android-review.googlesource.com/#/q/I5f67f2ab5d41a313c48dac42f485f8345f74c1b1), [b/243039555](https://issuetracker.google.com/issues/243039555))

**Bug Fixes**

- Fixed an issue where shadow tables where incorrectly exported to the schema `.json` files, corrupting them. ([I4f83b](https://android-review.googlesource.com/#/q/I4f83b2d6ead57d5110977c00c46c17601f75627f), [b/246751839](https://issuetracker.google.com/issues/246751839))

### Version 2.5.0-alpha03

August 24, 2022

`androidx.room:room-*:2.5.0-alpha03` is released. [Version 2.5.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..dd1e45e8550560087f6447a34a9145048b5766f4/room)

**New Features**

- Added a new shortcut annotation, `@Upsert`, which attempts to insert an entity when there is no uniqueness conflict or update the entity if there is a conflict. ([I7aaab](https://android-review.googlesource.com/#/q/I7aaab5416551ed70e0130a60b6b629a531757a16), [b/241964353](https://issuetracker.google.com/issues/241964353))

**Bug Fixes**

- Room will now throw a `SQLiteConstraintException` instead of a `IllegalStateException` during an auto-migration foreign key constraint check. ([I328dd](https://android-review.googlesource.com/#/q/I328ddbdce6df3947f49b304af708840f6d9056df))
- Fix a Kotlin source incompatible change for getter / properties of `getOpenHelper`, `getQueryExecutor` and `getTransactionExecutor`. ([Iad0ac](https://android-review.googlesource.com/#/q/Iad0ac5775730c80127f57fe6eec58796c0aff5d6))

### Version 2.5.0-alpha02

June 1, 2022

`androidx.room:room-*:2.5.0-alpha02` is released. [Version 2.5.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..7cbb37cc779160b89644d03e042c129d0ce025d2/room)

**New Features**

- New `room-paging` artifacts `room-paging-rxjava2`, `room-paging-rxjava3` and `room-paging-guava`have been added for support in Room Paging.([41a1d4](https://android.googlesource.com/platform/frameworks/support/+/41a1d4f8677c57db934d37bb0cd8db9d3f3aae6c),[b/203666906](https://issuetracker.google.com/203666906)),([eb6098](https://android.googlesource.com/platform/frameworks/support/+/eb60980fbbeb3a9d824e721969a54db902c44857),[b/203666906](https://issuetracker.google.com/203666906)),([1b9ae4](https://android.googlesource.com/platform/frameworks/support/+/1b9ae441be4de3443b138e789c85722bba29c356),[b/203666906](https://issuetracker.google.com/203666906))

**API Changes**

- All of `room-runtime` has been converted from Java to Kotlin. ([If2069](https://android-review.googlesource.com/#/q/If2069426a29fffe312a58fcd3e116551090c0b4e), [b/206859668](https://issuetracker.google.com/issues/206859668)),([Ie4b55](https://android-review.googlesource.com/#/q/Ie4b55827902c6ddcc4cc004de8bb5286823e9ab5), [b/206859668](https://issuetracker.google.com/issues/206859668)), ([I697ee](https://android-review.googlesource.com/#/q/I697ee52d9234358fd83dc8d94c66d4f2b849fc1b), [b/206859668](https://issuetracker.google.com/issues/206859668)), ([I96c25](https://android-review.googlesource.com/#/q/I96c25112c3ab32f8df71c1408c8006bdae1b3b7f), [b/206859668](https://issuetracker.google.com/issues/206859668))

  **Note:** You may encounter source incompatibility issues due to the library conversion to Kotlin. If your code was in Kotlin and calling the old version of Room, the new version will need to handle these cases. For example, a known source incompatible change is that in `InvalidationTracker` you will now need to declare `onInvalidate()` in `Observer` to have a param of type `Set` and not `MutableSet`.
- Added APIs for providing key and value tables names for disambiguation in `@MapInfo` ([Icc4b5](https://android-review.googlesource.com/#/q/Icc4b50a029d33c49fbfe7265d10b6be1b15da9c3))
- Fix a source compatibility issue to re-allow `@Ignore` in property getters. ([Ifc2fb](https://android-review.googlesource.com/#/q/Ifc2fb4922956bb84d5dbd855911da61a1b4ec69a))

**Bug Fixes**

- Duplicate column resolution heuristic algorithm. Room will now attempt to resolve ambiguous columns in a multimap query. This allows for JOINs with tables containing same-name tables to be correctly mapped to a result data object. ([I4b444](https://android-review.googlesource.com/#/q/I4b444b042245a334cc3f362f3239721ce0b6bd1e), [b/201306012](https://issuetracker.google.com/issues/201306012), [b/212279118](https://issuetracker.google.com/issues/212279118))

### Version 2.5.0-alpha01

February 23, 2022

`androidx.room:room-*:2.5.0-alpha01` is released. [Version 2.5.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3dda6c958a641fad4196ebc9b2e58a6f381ffdb4..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/room)

**API Changes**

- Fixed an issue where Room `@IntDef` usage were not being enforced in Kotlin sources. ([I75f41](https://android-review.googlesource.com/#/q/I75f413c3d66ee4bf0f156f3570705fcfb48f3c6b), [b/217951311](https://issuetracker.google.com/issues/217951311))
- Fixed a source compatibility issue to re-allow `@Query` in property getters. ([I0a09b](https://android-review.googlesource.com/#/q/I0a09bbf91ba813e3fd5f98633c1f6290861de565))
- Converted room-common from Java to Kotlin. ([I69c48](https://android-review.googlesource.com/#/q/I69c4832704c00c17dc989109992d3059261695a9), [b/206858235](https://issuetracker.google.com/issues/206858235))

  **Note:** You may encounter source incompatibility issues as some properties have been moved into companion objects during the library conversion to Kotlin. If your code was in Kotlin and calling the old version of Room, the new version will need the ".Companion" suffix when accessing these properties.
- Converted room-migration from Java to Kotlin. ([I2724b](https://android-review.googlesource.com/#/q/I2724b688fc6dcd3c632dfe167364924edc5248b9), [b/206858622](https://issuetracker.google.com/issues/206858622))
- Converted `paging` related files in `room-runtime` from Java to Kotlin. ([I82fc8](https://android-review.googlesource.com/#/q/I82fc81469540315dbe4865ccde68396a4339dfd9), [b/206859668](https://issuetracker.google.com/issues/206859668))
- Added API for multi-process lock and usage at the FrameworkSQLite\* level, to protect multi-process 1st time database creation and migrations. ([Ied267](https://android-review.googlesource.com/#/q/Ied267cd32e3248cec5ebb772778d2e94fd450270), [b/193182592](https://issuetracker.google.com/issues/193182592))

**Bug Fixes**

- Added support for internal properties in Kotlin sources. This is a slight behavior change in Room where it will use the source name of functions while matching them to properties as getters/setters (previously, it was using JVM name of the function which is different for internal functions/properties). If you are using custom `@JvmName` annotations to match getters/setters to private properties, please double check the generated code after the update ([If6531](https://android-review.googlesource.com/#/q/If653164362c49fd00650d9a953f330afdb309c1c), [b/205289020](https://issuetracker.google.com/issues/205289020))

## Version 2.4.3

### Version 2.4.3

July 27, 2022

`androidx.room:room-*:2.4.3` is released. [Version 2.4.3 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1048920be8e82e68b73b842a9219b7b96f905ede..4c4f7b4cd651cdc3dacb6ba8e66c66d6f81460aa/room)

**Bug Fixes**

- Fixed an issue that would cause Room to not recognize suspend functions in Kotlin 1.7 ([b/236612358](https://issuetracker.google.com/236612358))

## Version 2.4.2

### Version 2.4.2

February 23, 2022

`androidx.room:room-*:2.4.2` is released. [Version 2.4.2 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3dda6c958a641fad4196ebc9b2e58a6f381ffdb4..1048920be8e82e68b73b842a9219b7b96f905ede/room)

**Bug Fixes**

- Fix an issue generating code for a Dao `@Transaction` suspend function with a body that generates a default interface method due to compilation with `-Xjvm-default=all` or equivalent. ([Ia4ce5](https://android-review.googlesource.com/#/q/Ia4ce5c87c3886bc78e0386922e7eb2188fb14539))
- Resolving a bug where Room generates code for a `Array<ByteArray>` return type query method. ([If086e](https://android-review.googlesource.com/#/q/If086ef555768089adea98f8ff20e785cb06f9597), [b/213789489](https://issuetracker.google.com/issues/213789489))

## Version 2.4.1

### Version 2.4.1

January 12, 2022

`androidx.room:room-*:2.4.1` is released. [Version 2.4.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/11c93b38ca49928eecf09ce48d7e6909a7264e05..3dda6c958a641fad4196ebc9b2e58a6f381ffdb4/room)

**Bug Fixes**

- Added support for internal properties in Kotlin sources. This is a slight behavior change in Room where it will use the source name of functions while matching them to properties as getters/setters (previously, it was using JVM name of the function which is different for internal functions/properties). If you are using custom `@JvmName` annotations to match getters/setters to private properties, please double check the generated code after the update ([If6531](https://android-review.googlesource.com/#/q/If653164362c49fd00650d9a953f330afdb309c1c), [b/205289020](https://issuetracker.google.com/issues/205289020))

## Version 2.4.0

### Version 2.4.0

December 15, 2021

`androidx.room:room-*:2.4.0` is released. [Version 2.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/2c190565e1d506313ad852188959a8fa46f80e97..11c93b38ca49928eecf09ce48d7e6909a7264e05/room)

**Important changes since 2.3.0**

- **Auto Migrations** : Room now offers an API for automatically generating migrations as long as schemas are exported. To let Room know that it should generate an auto-migration a new property `@Database#autoMigrations` can be used to declare the versions to auto-migrate from and to. When Room needs additional information regarding tables and column renames or deletes, then the `@AutoMigration` annotation can declare a specification class containing such inputs. See the `@AutoMigration` documentation for more details.
- **Dependency Injection in Auto Migrations** : `@ProvidedAutoMigrationSpec` is a new API for declaring that an `AutoMigrationSpec` will be provided at runtime via `RoomDatabase.Builder#addAutoMigrationSpec()`. This allows for a dependency injection framework to provide such specs when they need complex dependencies.
- **Migration Test Helper Support for Auto Migrations** : Room's `MigrationTestHelper` was updated to support auto migrations by providing a new constructor API that receives the database class under test. This allows the helper to automatically add auto migrations the same way during `runMigrationsAndValidate`.
- **Room-Paging Support** : `androidx.room:room-paging` is released, providing native Paging 3.0 support for Room queries returning `androidx.paging.PagingSource`.
- **Relational Query Methods** : Room now supports multimap return types `@Dao` methods, useful for JOIN statements. The supported types of multimaps are `Map`, `SparseArray`, `LongSparseArray`, along with Guava's `ImmutableMap`, `ImmutableSetMultimap` and `ImmutableListMultimap`.

### Version 2.4.0-rc01

December 1, 2021

`androidx.room:room-*:2.4.0-rc01` is released. [Version 2.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/cc1240d00b28657ee0c1a937f60430eaf1b03b09..2c190565e1d506313ad852188959a8fa46f80e97/room)

**New Features**

- Update Room's dependency on KSP to `1.6.0-1.0.1` to support Kotlin 1.6

### Version 2.4.0-beta02

November 17, 2021

`androidx.room:room-*:2.4.0-beta02` is released. [Version 2.4.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..cc1240d00b28657ee0c1a937f60430eaf1b03b09/room)

**New Features**

- We've added support for SparseArray and LongSparseArray in @MapInfo. ([Ic91a2](https://android-review.googlesource.com/c/platform/frameworks/support/+/1809044)[b/138910317](https://issuetracker.google.com/138910317))

**Bug Fixes**

- We've added a new TypeConverter analyzer that takes nullability information in types into account. As this information is only available in KSP, it is turned on by default only in KSP. If it causes any issues, you can turn it off by passing room.useNullAwareTypeAnalysis=false to the annotation processor. If that happens, please a file bug as this flag will be removed in the future. With this new TypeConverter analyzer, it is suggested to only provide non-null receiving TypeConverters as the new analyzer has the ability to wrap them with a null check. Note that this has no impact for users using KAPT or Java as the annotation processors (unlike KSP), don't have nullability information in types. ([Ia88f9](https://android-review.googlesource.com/#/q/Ia88f916de3c15424ac8cc275d23223c6b5e47a6d), [b/193437407](https://issuetracker.google.com/issues/193437407))
- Fix a bug where Room would fail to compile with a SQL error when an FTS entity declared to use the ICU tokenizer. ([I00db9](https://android-review.googlesource.com/#/q/I00db9e36315f69a872a1498b4f5360ec6b576645), [b/201753224](https://issuetracker.google.com/issues/201753224))
- Resolved issue in auto migrations regarding a new column added to an embedded Entity between versions. ([I5fcb1](https://android-review.googlesource.com/c/platform/frameworks/support/+/1771292)[b/193798291](https://issuetracker.google.com/193798291))
- We have resolved an issue regarding the relational query method return types in LEFT JOIN queries. With these changes, in the case where a 1-many mapping is present, the collection returned for a key will not include the invalid value object if it is not found in the cursor. If no valid values are found, then a key will be mapped to an empty collection. ([Id5552](https://android-review.googlesource.com/c/platform/frameworks/support/+/1874056)[b/201946438](https://issuetracker.google.com/201946438))
- Resolved the auto migration issue where SQLite keywords failed to be escaped in column names. ([Idbed4](https://android-review.googlesource.com/c/platform/frameworks/support/+/1870037)[b/197133152](https://issuetracker.google.com/197133152))

### Version 2.4.0-beta01

October 13, 2021

`androidx.room:room-*:2.4.0-beta01` is released. [Version 2.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/room)

**Bug Fixes**

- Fixed an issue with auto-migrations not adding new columns when another table in the same auto-migration also had a new column with the same name. ([Ia5db5](https://android-review.googlesource.com/#/q/Ia5db52982e050714f224805d9949215b6caeff56), [b/200818663](https://issuetracker.google.com/issues/200818663))
- The PagingSource implementation generated by room-paging now uses the `queryExecutor` passed through `RoomDatabase.Builder`, so it can be overridden, instead of `Dispatchers.IO` previously. ([Iae259](https://android-review.googlesource.com/#/q/Iae2598b4c865904a295a1de1e6722bff14ed08cf))

### Version 2.4.0-alpha05

September 29, 2021

`androidx.room:room-*:2.4.0-alpha05` is released. [Version 2.4.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..1f6bc4d47b7be46a5af151ed726e84db0a1cf9f9/room)

**New Features**

- Added a built-in type converter for [UUID](https://docs.oracle.com/javase/8/docs/api/java/util/UUID.html). ([I671e8](https://android-review.googlesource.com/#/q/I671e8b1a8eb71d3309da04feaf6f9b18719489fc), [b/73132006](https://issuetracker.google.com/issues/73132006))

**API Changes**

- Added a new property to the TypeConverters annotation to let developers disable built-in Enum and UUID converters. By default, these converters are on but you can disable them for a certain scope, or for the whole database. See TypeConverters documentation for details. ([36ae9e](https://android-review.googlesource.com/#/q/36ae9ec7a21c7a4fd43da5a250494c6196da1ca9), [b/195413406](https://issuetracker.google.com/issues/195413406))

- Supporting non-POJO keys/values for Multimap return types in DAOs via the `@MapInfo` annotation. ([I4d704](https://android-review.googlesource.com/#/q/I4d7048542b73b963fdb0b901dcab76f19ef3b5b8))

`@MapInfo` will be required when the key or value column of the map are from a single column. See example:

    @MapInfo(valueColumn = "songCount")
    @Query("""
           SELECT *, COUNT(mSongId) as songCount
           FROM Artist JOIN Song ON Artist.artistName = Song.artist
           GROUP BY artistName
           """)
    fun getArtistAndSongCounts(): Map<Artist, Integer>

- Make `room-paging` a required artifact when using Paging3 with Room. ([Ieaffe](https://android-review.googlesource.com/#/q/Ieaffeb61c176fae19663544d7f891e2c328172ca))

**Bug Fixes**

- Fix an issue where multimap queries results were not correctly ordered when the query contained an ORDER BY clause of a column from the map's key. ([I6b887](https://android-review.googlesource.com/#/q/I6b887d3a5d96b0c7dbe9aa525a33090066cd07f4))

**External Contribution**

- Added new API to specify index order in @Index. Thanks to Nikita Zhelonkin. ([I033fc](https://android-review.googlesource.com/#/q/I033fc476e5dba9cd01fbee985704e7fbdd0c0f6d))

### Version 2.4.0-alpha04

July 21, 2021

`androidx.room:room-*:2.4.0-alpha04` is released. [Version 2.4.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/room)

**New Features**

- Room now supports multimap return types `@Dao` methods, useful for JOIN statements. The supported types of multimaps are `Map` along with Guava's `ImmutableMap`, `ImmutableSetMultimap` and `ImmutableListMultimap`.

  The following are examples of multimap queries:

  *One-to-One Relation Map*

      @Query("SELECT * FROM Song JOIN Artist ON Song.artistId = Artist.artistId")
      fun getSongAndArtist(): Map<Song, Artist>

  *One-to-Many Relation Map (Standard multimap)*

      @Query("SELECT * FROM Artist JOIN Album ON Artist.id = Album.artistId")
      fun getArtistAndAlbums(): Map<Artist, List<Album>>

  The multimap result can also be wrapped in the supported async return types, such as `LiveData`, Rx's `Observable`, or coroutines `Flow`.
  | **Note:** In version 2.4.0-alpha04, only multimaps with POJOs as type parameters are supported, but in a future version String and primitives will also be supported.

**Room-Paging**

- `androidx.room:room-paging` is released, providing native Paging 3.0 support for Room queries returning `androidx.paging.PagingSource`.

      @Dao
      interface UserDao {
        @Query("SELECT * FROM users ORDER BY id ASC")
        fun loadUsers(): PagingSource<Int, User>
      }

- This artifact replaces the `androidx.paging.PagingSource` implementation generated by Room with one built on top of Paging 3.0 APIs. The new PagingSource implementation parses keys differently, so any key manually supplied to Room's PagingSource would need to account for this behavior change, including the initialKey passed via Pager's constructor. Pages will start loading from the `Key` with `Key` being the first loaded item. This deviates from existing behavior where `LoadParams.Refresh.Key` is treated as the user's scroll position and items are loaded both before and after the key.

- The artifact is optional and opting out will fallback to existing support for Paging 3.0 that was introduced in Room 2.3. However, this artifact will become non-optional in future release for those using Room with Paging 3.0. To opt-in, add the new room-paging artifact to your classpath. If you are using Gradle, you can add the following snippet to your build.gradle:

      dependency {
        implementation("androidx.room:room-paging:2.4.0-alpha04")
      }

**Bug Fixes**

- Fix an issue in auto migrations regarding handling foreign key violations. ([b/190113935](https://issuetracker.google.com/190113935))

### Version 2.4.0-alpha03

June 16, 2021

`androidx.room:room-*:2.4.0-alpha03` is released. [Version 2.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a..ccf79f53033e665475116a4e78ff124df2a52c4b/room)

**API Changes**

- Update Room's `MigrationTestHelper` to support auto migrations by providing a new constructor API that receives the database class under test. This allows the helper to automatically add auto migrations the same way during `runMigrationsAndValidate`.

**Bug Fixes**

- Fixed an issue with Room's SQLite native library to support Apple's M1 chips. ([b/174695268](https://issuetracker.google.com/issues/174695268)

- Fixed an issue where Room would not error out when the return type of a @Transaction function was a Flow ([I56ddd](https://android-review.googlesource.com/#/q/I56ddd221f0fe636f6c1bd91ac812fa589fa65955), [b/190075899](https://issuetracker.google.com/issues/190075899))

- Fix an issue in auto migrations regarding indices. [b/177673291](https://issuetracker.google.com/issues/190075899)

**Dependency Updates**

- Room's KSP support now depends on KSP `1.5.10-1.0.0-beta01`. ([1ecb11](https://android-review.googlesource.com/#/q/1ecb11aef121d1970384250c8369a5edaa96dc73), [b/160322705](https://issuetracker.google.com/issues/160322705))

### Version 2.4.0-alpha02

May 5, 2021

`androidx.room:room-*:2.4.0-alpha02` is released. [Version 2.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ab8f8cb3fbe8e7409d54bb7251e636d8a92226e2..3d6f168394d1dd14e1d6f5b6dc4a0d405cb1a26a/room)

**API Changes**

- `@ProvidedAutoMigrationSpec` is a new API for declaring that an `AutoMigrationSpec` will be provided at runtime via `RoomDatabase.Builder#addAutoMigrationSpec()`. This allows for a dependency injection framework to provide such specs when they need complex dependencies.

**Bug Fixes**

- Fix an issue with auto migrations where `@DatabaseView`s where not being properly re-created.

**External Contribution**

- Fix an issue in Room's `JournalMode.TRUNCATE` where the `InvalidationTracker` callback was sometimes being invoked invalidly, too late, or not at all. Thanks to `Uli Bubenheimer | bubenheimer@users.noreply.github.com` ([b/154040286](https://issuetracker.google.com/154040286))

### Version 2.4.0-alpha01

April 21, 2021

`androidx.room:room-*:2.4.0-alpha01` is released. [Version 2.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29ce56e372f451c2dbf8036b1b9754733a15f32e..4ddfc1583c09aaa878d34437fbfee1b995b60d3a/room)

**New Features**

- **Auto Migrations** : Room now offers an API for automatically generating migrations as long as schemas are exported. To let Room know that it should generate an auto-migration a new property `@Database#autoMigrations` can be used to declare the versions to auto-migrate from and to. When Room needs additional information regarding tables and column renames or deletes, then the `@AutoMigration` annotation can declare a specification class containing such inputs. See the [`@AutoMigration`](https://developer.android.com/reference/androidx/room/AutoMigration) documentation for more details.

**Bug Fixes**

- Fix an issue where `defaultValue` with extra parenthesis were being incorrectly validated by Room's schema validation. [b/182284899](https://issuetracker.google.com/182284899)

## Version 2.3.0

### Version 2.3.0

April 21, 2021

`androidx.room:room-*:2.3.0` is released. [Version 2.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/29ce56e372f451c2dbf8036b1b9754733a15f32e..9666e15e33983547016363106d116b9a82974bda/room)

**Important changes since 2.2.0**

- **Built-in Enum Support**: Room will now default to using an Enum to String and vice versa type converter if none is provided. If a type converter for an enum already exists, Room will prioritize using it over the default one.
- **Query Callback** : Room now offers a general callback API RoomDatabase.QueryCallback, for when queries are about to execute, which can be useful for logging in debug builds. The callback can be set via `RoomDatabase.Builder#setQueryCallback()`.
- **Pre-packaged Improvement**: Room now has APIs for creating a database using a pre-packaged database read from an input stream. This allows for cases such as when the pre-package database is gzipped.
- **Provided Type Converters**: Room now has APIs for providing instances of type converters such that the app can control their initialization. To mark a type converter that will be provided to Room use the new annotation @ProvidedTypeConverter.
- **RxJava3 Support** : Room now supports RxJava3 types. Similar to RxJava2 you can declare DAO methods whose return type are Flowable, Single, Maybe and Completable. Additionally a new artifact `androidx.room:room-rxjava3` is available to support RxJava3.
- **Paging 3.0 Support** : Room will now support generating implementations for `@Query` annotated methods whose return type is `androidx.paging.PagingSource`.

### Version 2.3.0-rc01

March 24, 2021

`androidx.room:room-*:2.3.0-rc01` is released. [Version 2.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/fe0dc921b17e832473de7029a40ca518f2e50266..29ce56e372f451c2dbf8036b1b9754733a15f32e/room)

**Bug Fixes**

- Fix an issue that prevented Coroutine Flow queries created by Room to be consumed in a suspending `withTransaction` block. ([I797bf](https://android-review.googlesource.com/q/I797bf24d579e11cc51eeb49098228caa5c7b4a7c))

### Version 2.3.0-beta03

March 10, 2021

`androidx.room:room-*:2.3.0-beta03` is released. [Version 2.3.0-beta03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/028c82c1173bb9300dd314de4118eb21d92156d1..fe0dc921b17e832473de7029a40ca518f2e50266/room)

**New Features**

- Added incremental compilation support for KSP. ([I031c1](https://android-review.googlesource.com/#/q/I031c1f94890ebe2a382c26f7f0745edb790a5a7b), [b/176453350](https://issuetracker.google.com/issues/176453350))

**Bug Fixes**

- Fixed a bug where creating PagingSource on the main thread could trigger an ANR. ([I42b74](https://android-review.googlesource.com/#/q/I42b74e397bcf717f509b1d53203d2edced89afb0), [b/181221318](https://issuetracker.google.com/issues/181221318))
- Fixed `@ExperimentalRoomApi` visibility to be public instead of package private. ([b/181356119](https://issuetracker.google.com/issues/181356119))

**External Contribution**

- Allow Room to accept a POJO return type in a `@Query` annotated DAO method when it is also annotated with `@SkipQueryVerification`. Room will do a best-effort to convert the result of the query to the POJO return type the same way it is done for a `@RawQuery` annotated DAO method. Thanks to 'Markus Riegel \| hey@marcorei.com'. ([I45acb](https://android-review.googlesource.com/c/platform/frameworks/support/+/1605977))

### Version 2.3.0-beta02

February 18, 2021

`androidx.room:room-*:2.3.0-beta02` is released. [Version 2.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/aee18b103203a91ee89df91f0af5df2ecff356d6..028c82c1173bb9300dd314de4118eb21d92156d1/room)

**New Features**

- Room now has experimental support for Kotlin Symbol Processing [KSP](http://github.com/google/ksp).

  KSP is a replacement for KAPT to run annotation processors natively on the Kotlin compiler, significantly reducing build times.

  To use Room with KSP, you can apply the KSP Gradle plugin and replace the `kapt` configuration in your build file with `ksp`. For example, instead of `kapt 'androidx.room:room-compiler:2.3.0-beta02'` use `ksp 'androidx.room:room-compiler:2.3.0-beta02'`. See the [KSP documentation](https://github.com/google/ksp/blob/master/docs/quickstart.md) for more details.

  Note that since KSP is experimental, it is recommended to still use KAPT for production code. The reduction of build times is only applicable if there are no other processors that use KAPT. See [b/160322705](https://issuetracker.google.com/issues/160322705) for known issues.

### Version 2.3.0-beta01

January 27, 2021

`androidx.room:room-*:2.3.0-beta01` is released. [Version 2.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd3c8e9c2424b78e44f55db599251891fd1cadb4..aee18b103203a91ee89df91f0af5df2ecff356d6/room)

**New Features**

- *Auto Closable Databases* : Room now has the ability to close databases that are not accessed after a given amount of time. This is an experimental feature and can be enabled by calling `RoomDatabase.Builder#setAutoCloseTimeout()`. This feature is useful for applications with multiple databases.

**Bug Fixes**

- Fix an issue where Dao methods with multiple `@Update` or `@Delete` methods with different conflict strategies would generate code with only one of the strategies, effectively ignoring the defined one. ([/I0b90d](https://android-review.googlesource.com/#/q/I0b90daccfbfe784cd44c507d05edf84e6ba80052), [b/176138543](https://issuetracker.google.com/issues/176138543))

### Version 2.3.0-alpha04

December 16, 2020

`androidx.room:room-*:2.3.0-alpha04` is released. [Version 2.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/f413b8be76bfa0a4d109a3afb583188c580a2aa6..dd3c8e9c2424b78e44f55db599251891fd1cadb4/room)

**New Features**

- Room now offers a general callback API `RoomDatabase.QueryCallback`, for when queries are about to execute, which can be useful for logging in debug builds. The callback can be set via `RoomDatabase.Builder#setQueryCallback()`. ([Iaa513](https://android-review.googlesource.com/#/q/Iaa513e39115f0c9c68359774fa70e1d3dd022c39), [b/174478034](https://issuetracker.google.com/issues/174478034), [b/74877608](https://issuetracker.google.com/issues/74877608))
- Room will now default to using an Enum to String and vice versa type converter if none is provided. If a type converter for an enum already exists, Room will prioritize using it over the default one. ([b/73132006](https://issuetracker.google.com/issues/174478034))

**Known Issue**

- If a one-way type converter for reading already exists for the Enum, Room might accidentally use the built-in String to Enum converter which might not be desired. This is a known issue and can be fixed by making it a two-way converter. See: [b/175707691](https://issuetracker.google.com/issues/175707691)

**Bug Fixes**

- Fixed an issue where Room would incorrectly disabled incremental annotation processing in newer JDK versions. ([b/171387388](https://issuetracker.google.com/issues/74877608))
- Fixed an issue with Room finding the generated class when multiple class loaders are used. Thanks for the fix 'Serendipity \| 892449346@qq.com'! ([b/170141113](https://issuetracker.google.com/issues/174478034))
- Fixed an issue where Room would generate incorrect code when a Kotlin `@Dao` had a base class whose generics are primitives in the JVM. ([b/160258066](https://issuetracker.google.com/issues/174478034))

**External Contribution**

- Room will now default to using `beginTransactionNonExclusive` if WAL mode is enabled and API is 16 or more. Thanks to 'Ahmed I. Khalil \| ahmedibrahimkhali@gmail.com'! ([b/126258791](https://issuetracker.google.com/issues/174478034))

### Version 2.3.0-alpha03

October 14, 2020

`androidx.room:room-*:2.3.0-alpha03` is released. [Version 2.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9f60cc700129e30cee9df020005c317fb39d32ec..f413b8be76bfa0a4d109a3afb583188c580a2aa6/room)

**New Features**

- Room now has APIs for providing instances of type converters such that the app can control their initialization. To mark a type converter that will be provided to Room use the new annotation `@ProvidedTypeConverter`. Thanks to 'mzgreen [yairobbe@gmail.com](mailto:yairobbe@gmail.com)'. ([Ie4fa5](https://android-review.googlesource.com/#/q/Ie4fa505b36f8aa3c98091f60af9cbbdb10ca3f33), [b/121067210](https://issuetracker.google.com/issues/121067210))

- Room now has APIs for creating a database using a pre-packaged database read from an input stream. This allows for cases such as when the pre-package database is gzipped. Thanks to 'Ahmed El-Helw [ahmedre@gmail.com](mailto:ahmedre@gmail.com)' ([3e6792](https://android.googlesource.com/platform/frameworks/support/+/3e6792c7521cdf41c295a1c0037137ecf9c7a005), [b/146911060](https://issuetracker.google.com/issues/146911060))

**API Changes**

- Added missing target to `@ForeignKey` annotation preventing its usage outside of the `@Entity` annotation. ([Iced1e](https://android-review.googlesource.com/#/q/Iced1e9480e5f5bf1a93815e4581e0a4123d22509))

- The field `mCallbacks` in`RoomDatabase.java` is now hidden. ([d576cb](https://android.googlesource.com/platform/frameworks/support/+/d576cbdc911cba16638a44fd8223391a90a07ef7), [b/76109329](https://issuetracker.google.com/issues/76109329))

**Bug Fixes**

- Update to TypeConverters documentation to clarify that TypeConverters can only be used to convert columns / fields and not rows. ([I07c56](https://android-review.googlesource.com/#/q/I07c56c02866b27e8e2e4802f2426130f8713f472), [b/77307836](https://issuetracker.google.com/issues/77307836))

- Update to the DaoProcessor to fix compiler error on Dao with a generic super type with Kotlin "primitives". ([Ice6bb](https://android-review.googlesource.com/#/q/Ice6bbd327c1a2693bafd371da0bfdfea8769b4c8), [b/160258066](https://issuetracker.google.com/issues/160258066))

- Update add/remove observer methods documentation to clarify threading ([Ifd1d9](https://android-review.googlesource.com/#/q/Ifd1d988bf88ca54415aca08e82ed9e45a654a02c), [b/153948821](https://issuetracker.google.com/issues/153948821))

- Fix an issue with Room incorrectly validating FTS tables that declared their rowid column. ([d62ebc](https://android.googlesource.com/platform/frameworks/support/+/d62ebcd6f4a555e25596db7bdc46e6b339391045), [b/145858914](https://issuetracker.google.com/issues/145858914))

**External Contributions**

- Fix upper/lowercase locale issues related to Turkish ([5746e3](https://android.googlesource.com/platform/frameworks/support/+/5746e3392b60a9f79bca2d7f93774cc5cf50383f)), [b/68159494](https://issuetracker.google.com/issues/68159494)

- Replace the `ConcurrentHashMap` inside `RoomDatabase` with `Collections.synchronizedMap()` to avoid issues on Android Lollipop ([d1cfc7](https://android.googlesource.com/platform/frameworks/support/+/d1cfc7d2f73f5ea75da8ab2ab0d5f195f7eaf829), [b/162431855](https://issuetracker.google.com/issues/162431855))

- Add a onOpenPrepackagedDatabase callback for when a prepackaged
  DB is copied. ([I1ba74](https://android-review.googlesource.com/#/q/I1ba740f679565f5c97548f6683de40b0f40f9024), [b/148934423](https://issuetracker.google.com/issues/148934423))

### Version 2.3.0-alpha02

July 22, 2020

`androidx.room:room-*:2.3.0-alpha02` is released. [Version 2.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/945594abd75f83bd14daf4fbcd8621796161281e..9f60cc700129e30cee9df020005c317fb39d32ec/room)

**New Features**

- **RxJava3 Support** : Room now supports RxJava3 types. Similar to RxJava2 you can declare DAO methods whose return type are Flowable, Single, Maybe and Completable. Additionally a new artifact `androidx.room:room-rxjava3` is available to support RxJava3. ([b/152427884](https://issuetracker.google.com/152427884))

**API Changes**

- Declaring a `@TypeConverter` in Kotlin Object class is now supported. ([b/151110764](https://issuetracker.google.com/151110764))
- `Room` incremental annotation processing option is now ON by default. ([b/112110217](https://issuetracker.google.com/112110217))

### Version 2.3.0-alpha01

June 10, 2020

`androidx.room:room-*:2.3.0-alpha01` is released. [Version 2.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6880f4a443ed0d4e88e15c18044fbfc644c766e2..945594abd75f83bd14daf4fbcd8621796161281e/room)

**New Features**

- **Paging 3.0 Support** : Room will now support generating implementations for`@Query` annotated methods whose return type is `androidx.paging.PagingSource`.

      @Dao
      interface UserDao {
        @Query("SELECT * FROM users ORDER BY id ASC")
        fun pagingSource(): PagingSource<Int, User>
      }

**API Changes**

- `@RewriteQueriesToDropUnusedColumns` is a new convenient annotation that makes Room rewrite the '\*' projection in a query such that unused columns in the result are removed.
- The processor option `room.expandProjection` is now deprecated. Use `@RewriteQueriesToDropUnusedColumns` as a replacement for Room optimizing queries with star projections. Note that `@RewriteQueriesToDropUnusedColumns` does not replace the column conflict solution `room.expandProjection` offered with regards to return types that contained `@Embedded` fields.

**Bug Fixes**

- Fixed a bug where Room would not correctly detect the JDK version used to enable incremental annotation processor. Thanks to Blaz Solar (me@blaz.solar) ([b/155215201](https://issuetracker.google.com/155215201))
- Room now embeds its ANTLR dependency with the annotation processor to avoid version conflicts with other processors that also use ANTLR. ([b/150106190](https://issuetracker.google.com/150106190))

## Version 2.2.6

### Version 2.2.6

December 16, 2020

`androidx.room:room-*:2.2.6` is released. [Version 2.2.6 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/6880f4a443ed0d4e88e15c18044fbfc644c766e2..b488666805d0b8cef27e52ef171d7833a4bcfa9a/room)

**Bug Fixes**

- Fixed an issue where Room would incorrectly disabled incremental annotation processing in newer JDK versions. ([b/171387388](https://issuetracker.google.com/issues/74877608))

## Version 2.2.5

### Version 2.2.5

March 18, 2020

`androidx.room:room-*:2.2.5` is released. [Version 2.2.5 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/c4faf1724c897234f083f07e15f0156873fd6a8a..6880f4a443ed0d4e88e15c18044fbfc644c766e2/room)

**Bug Fixes**

- Make `MultiInstanceInvalidationService` directBootAware. Thanks to 'Mygod [contact-git@mygod.be](mailto:contact-git@mygod.be)' ([b/148240967](https://issuetracker.google.com/issues/148240967))
- Fixed a bug that would cause a crash when multi-instance invalidation was enabled and the database contained a FTS entity. ([b/148969394](https://issuetracker.google.com/issues/148969394))
- Fixed an issue when loading the SQLite native libraries in the Room annotation processor that would cause the compiler to crash due to parallel compilations. ([b/146217083](https://issuetracker.google.com/issues/146217083))

## Version 2.2.4

### Version 2.2.4

February 19, 2020

`androidx.room:room-common:2.2.4`, `androidx.room:room-compiler:2.2.4`, `androidx.room:room-guava:2.2.4`, `androidx.room:room-ktx:2.2.4`, `androidx.room:room-migration:2.2.4`, `androidx.room:room-runtime:2.2.4`, `androidx.room:room-rxjava2:2.2.4`, and `androidx.room:room-testing:2.2.4` are released. [Version 2.2.4 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/31d127394de2acb29cd81204796b413f5a1db8b2..c4faf1724c897234f083f07e15f0156873fd6a8a/room)

**Bug Fixes**

- Fixed an issue with suspending transactions where they would deadlock if the coroutine was canceled quickly before the transaction actually started. ([b/148181325](https://issuetracker.google.com/issues/148181325))
- Fixed an issue with the @Generated being wrongly used when building with JDK 9. ([b/146538330](https://issuetracker.google.com/issues/146538330))
- Fixed an issue where Room would generate incorrect code when a DAO interface in Kotlin had a concrete function. ([b/146825845](https://issuetracker.google.com/issues/146825845))

## Version 2.2.3

### Version 2.2.3

December 18, 2019

`androidx.room:room-*:2.2.3` is released. [Version 2.2.3 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/a04145cf715ff88c1aa0dd36f3447be35a5c3e62..65f69af711a37fa7729dfd4d120a17010d1c27f0/room).

**Bug fixes**

- Fixed a bug where Room would fail to validate a database that had not gone through any migration and contained a legacy hash with indices in its schema. ([b/139306173](https://issuetracker.google.com/issues/139306173))

## Version 2.2.2

### Version 2.2.2

November 20, 2019

`androidx.room:room-*:2.2.2` is released. [Version 2.2.2 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/33f1d55259b216abd7f9f5a8bcb2a363f8a0070c..a04145cf715ff88c1aa0dd36f3447be35a5c3e62/room).

**Bug fixes**

- Fixed a bug where collecting a one-to-one relationship with more than 999 rows would cause Room to return null relating items. ([b/143105450](http://issuetracker.google.com/143105450))

## Version 2.2.1

### Version 2.2.1

October 23, 2019

`androidx.room:room-*:2.2.1` is released. [Version 2.2.1 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/31d127394de2acb29cd81204796b413f5a1db8b2..33f1d55259b216abd7f9f5a8bcb2a363f8a0070c/room).

**Bug fixes**

- Fixed a bug where Room would incorrectly warn about `CURSOR_MISMATCH` with the compiler option`expandProjection` turned ON. ([b/140759491](http://issuetracker.google.com/140759491))
- Added a retry mechanism for handling the missing native library used for verifying queries during compile time.

## Version 2.2.0

### Version 2.2.0

October 9, 2019

`androidx.room:room-*:2.2.0` is released. [Version 2.2.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/aa36228c061a81036f6b98fd4fe2e0814415303d..31d127394de2acb29cd81204796b413f5a1db8b2/room).

**Important changes since version 2.1.0**

- **Pre-packaged Database** : Two new APIs in `RoomDatabase.Builder` are now available for creating a `RoomDatabase` given an already populated database file. `createFromAsset()` is for when the pre-populated database file is in the assets folder of the APK, while `createFromFile()` is for when the file is in an arbitrary location. The usages of these API change the behaviour of destructive migrations such that during a fallback migration, Room will try to re-copy the pre-populated database if available, otherwise it fallbacks to just dropping and re-creating all tables. [b/62185732](https://issuetracker.google.com/issues/62185732)
- **Schema Default Values** : `@ColumnInfo` now has a new property `defaultValue` that can be used to specify the default value of a column. Default values are part of a database schema and will be validated during migrations if specified. [b/64088772](https://issuetracker.google.com/issues/64088772)
- **Many-to-Many Relations** : `@Relation` now has a new property `associateBy`, that takes in a new annotation `@Junction`, used to declare a relation that needs to be satisfied via a junction table (also known as a join table). [b/69201917](https://issuetracker.google.com/issues/69201917)
- **One-to-One Relations** : The restriction in POJO fields annotated with `@Relation` to be of type `List` or `Set` has been lifted, effectively allowing single-value relations to be represented. [b/62905145](https://issuetracker.google.com/issues/62905145)
- **Target Entity** : The DAO annnotations `@Insert`, `@Update` and `@Delete` now has a new property `targetEntity`, that allows specifying the target table the DAO method is meant to act on. This allows for the parameters of those DAO methods to be arbitrary POJOs which will be interpreted as partial entities. In practice, this allows partial inserts, deletes and updates. [b/127549506](https://issuetracker.google.com/issues/127549506)
- **Coroutines Flow** : `@Query` DAO methods can now be of return type `Flow<T>`. The returned Flow will re-emit a new set of values if the observing tables in the query are invalidated. Declaring a DAO function with a `Channel<T>` return type is an error, Room instead encourages you to use `Flow` and then use the neighboring functions to convert the `Flow` into a `Channel`. [b/130428884](https://issuetracker.google.com/issues/130428884)
- **Gradle Incremental Annotation Processor** : Room is now a Gradle isolating annotation processor and incrementability can be enabled via the processor option `room.incremental`. See [Room Compiler Options](https://developer.android.com/jetpack/androidx/releases/room#compiler-options) for more information. If you encounter any issues please file a bug [here](https://issuetracker.google.com/issues/new?component=413107&template=1096568). We plan to enable incrementability by default in a future, stable version. [b/112110217](https://issuetracker.google.com/issues/112110217)
- **Expanding Projections** : A new experimental compiler option `room.expandProjection` was added that causes Room to rewrite a query with a star projection to only contain the columns in the returning type POJO. For example, for a DAO method with `@Query("SELECT * FROM Song")` that returns a POJO named `SongIdAndTitle` with only two fields. Then Room will rewrite the query to `SELECT id, title FROM Song` such that the minimum set of columns to satisfy the return type are fetched. This essentially eliminates the `CURSOR_MISMATCH` warning that is presented when the query returns extra columns that do not match any field in the returning POJO type.

### Version 2.2.0-rc01

September 5, 2019

`androidx.room:room:2.2.0-rc01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform%2Fframeworks%2Fsupport/+log/603df7ced432238f83d1a244f10bfc1968d466ff..aa36228c061a81036f6b98fd4fe2e0814415303d/room).

No public changes since Room `2.2.0-beta01`.

### Version 2.2.0-beta01

August 22, 2019

`androidx.room:room-*:2.2.0-beta01` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform%2Fframeworks%2Fsupport/+log/45e343f257a0efd3f0f69546ee9923a9ceb0a8cb..603df7ced432238f83d1a244f10bfc1968d466ff/room).

**Bug fixes**

- Fixed a bug where a Coroutine Flow query would stop reemitting new values after a certain time. ([b/139175786](https://issuetracker.google.com/issues/139175786))
- Fixed a bug where Room would not accept a legacy schema hash code while opening a database that had not gone a migration since Room 1.0, causing a runtime crash due to invalid schema. ([b/139306173](https://issuetracker.google.com/issues/139306173))

### Version 2.2.0-alpha02

August 7, 2019

`androidx.room:room-*:2.2.0-alpha02` is released. The commits included in this version can be found [here](https://android.googlesource.com/platform%2Fframeworks%2Fsupport/+log/f3fa99365aa7db9e882cb3f91fc486b1d9445814..45e343f257a0efd3f0f69546ee9923a9ceb0a8cb/room).

**New Features**

- **Coroutines Flow** : `@Query` DAO methods can now be of return type `Flow<T>`. The returned Flow will re-emit a new set of values if the observing tables in the query are invalidated. Declaring a DAO function with a `Channel<T>` return type is an error, Room instead encourages you to use `Flow` and then use the neighboring functions to convert the `Flow` into a `Channel`. [b/130428884](https://issuetracker.google.com/issues/130428884)
- **Expanding Projections** : A new experimental compiler option `room.expandProjection` was added that causes Room to rewrite a query with a star projection to only contain the columns in the returning type POJO. For example, for a DAO method with `@Query("SELECT * FROM Song")` that returns a POJO named `SongIdAndTitle` with only two fields. Then Room will rewrite the query to `SELECT id, title FROM Song` such that the minimum set of columns to satisfy the return type are fetched. This essentially eliminates the `CURSOR_MISMATCH` warning that is presented when the query returns extra columns that do not match any field in the returning POJO type.
- `onDestructiveMigrate` is a new callback API added to `RoomDatabase.Callback` for when Room destructively migrates a database. [b/79962330](https://issuetracker.google.com/issues/79962330)

**Bug Fixes**

- Fixed a bug where Room would generate incorrect code using a method as field setter when the field is protected. [b/136194628](https://issuetracker.google.com/issues/136194628)
- Fixed a bug that caused the InvalidationTracker to throw a NPE in a second process when multi-instance invalidation was enabled and the invalidation Service was killed. [b/137454915](https://issuetracker.google.com/issues/137454915)
- Fixed a bug where Room would not correctly identify the return type of an inherited suspend function annotated with `@RawQuery`. [b/137878827](https://issuetracker.google.com/issues/137878827)
- Updated the generated code for `@Relation` when the relating key is of type BLOB to use a `ByteBuffer` that is comparable. [b/137881998](https://issuetracker.google.com/issues/137881998)
- Fixed a bug where Room would complain about missing setters on POJOs used as partial entity parameters of `@Insert`, `@Update` and `@Delete`. [b/138664463](https://issuetracker.google.com/issues/138664463)
- Fixed a bug where Room would complain about missing getters \& setters for an ignored column via `@Entity` when the entity class was used in certain DAO methods. [b/138238182](https://issuetracker.google.com/issues/138238182)
- Fixed a bug where Room would not correctly convert named binding args to positional args causing a runtime exception when executing a query with re-used parameters. [b/137254857](https://issuetracker.google.com/issues/137254857)

### Version 2.2.0-alpha01

July 10, 2019

**New Features**

- **Pre-packaged Database** : Two new APIs in `RoomDatabase.Builder` are now available for creating a `RoomDatabase` given an already populated database file. `createFromAsset()` is for when the pre-populated database file is in the assets folder of the APK, while `createFromFile()` is for when the file is in an arbitrary location. The usages of these API change the behaviour of destructive migrations such that during a fallback migration, Room will try to re-copy the pre-populated database if available, otherwise it fallbacks to just dropping and re-creating all tables. [b/62185732](https://issuetracker.google.com/issues/62185732)
- **Schema Default Values** : `@ColumnInfo` now has a new property `defaultValue` that can be used to specify the default value of a column. Default values are part of a database schema and will be validated during migrations if specified. [b/64088772](https://issuetracker.google.com/issues/64088772)

  **Note:** If your database schema already has default
  values, such as those added via `ALTER TABLE x ADD COLUMN y INTEGER NOTNULL
  DEFAULT z`, and you decide to define default values via `@ColumnInfo` to the
  same columns, then you might need to provide a migration to validate the
  unaccounted default values. See
  [Room Migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions#handle-default-values-migrations)
  for more information.
- **Many-to-Many Relations** : `@Relation` now has a new property `associateBy`, that takes in a new annotation `@Junction`, used to declare a relation that needs to be satisfied via a junction table (also known as a join table). [b/69201917](https://issuetracker.google.com/issues/69201917)
- **One-to-One Relations** : The restriction in POJO fields annotated with `@Relation` to be of type `List` or `Set` has been lifted, effectively allowing single-value relations to be represented. [b/62905145](https://issuetracker.google.com/issues/69201917)
- **Target Entity** : The DAO annnotations `@Insert`, `@Update` and `@Delete` now has a new property `targetEntity`, that allows specifying the target table the DAO method is meant to act on. This allows for the parameters of those DAO methods to be arbitrary POJOs which will be interpreted as partial entities. In practice, this allows partial inserts, deletes and updates. [b/127549506](https://issuetracker.google.com/issues/127549506)
- **Gradle Incremental Annotation Processor** : Room is now a Gradle isolating annotation processor and incrementability can be enabled via the processor option `room.incremental`. See [Room Compiler Options](https://developer.android.com/jetpack/androidx/releases/room#compiler-options) for more information. If you encounter any issues please file a bug [here](https://issuetracker.google.com/issues/new?component=413107&template=1096568). We plan to enable incrementability by default in a future, stable version. [b/112110217](https://issuetracker.google.com/issues/112110217)

**Bug Fixes**

- Room will no longer propagate the `EmptySetResultException` to the global error handler when the Rx stream of a query has been disposed before the query is complete. [b/130257475](https://issuetracker.google.com/issues/130257475)
- Fixed a bug where Room would show an incorrect error message when a suspend DAO function annotated with `@RawQuery` didn't have a return type. [b/134303897](https://issuetracker.google.com/issues/134303897)
- Room will no longer generate DAO adapters with raw types. [b/135747255](https://issuetracker.google.com/issues/135747255)

## Version 2.1.0

### Version 2.1.0

June 13, 2019

Room 2.1.0 is released with no changes from `2.1.0-rc01`. The commits included in the version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/c335f0223fafd3f8ce8658a472bc249d25992ff1..a0ad74d00bf98712b6d07b70214cac23154ff49c/room).

**Important changes since 2.0.0**

- **FTS** : Room now supports entities with a mapping [FTS3 or FTS4](https://www.sqlite.org/fts3.html) table. Classes annotated with `@Entity` can now be additionally annotated with `@Fts3` or `@Fts4` to declare a class with a mapping full-text search table. FTS options for further customization are available via the annotation's methods.
- **Views** : Room now supports declaring a class as a stored query, also known as a [view](https://www.sqlite.org/lang_createview.html), using the `@DatabaseView` annotation.
- **Couroutines** : DAO methods can now be suspend functions. Include `room-ktx` in your dependencies to take advantage of this functionality. The ktx artifact also provides the extension function `RoomDatabase.withTransaction` for performing database transactions within a coroutine.
- **Auto Value** : Room now supports declaring [AutoValue](https://github.com/google/auto/blob/master/value/userguide/index.md) annotated classes as entities and POJOs. The Room annotations `@PrimaryKey`, `@ColumnInfo`, `@Embedded` and `@Relation` can now be declared in an auto value annotated class's abstract methods. Note that these annotation must also be accompanied by `@CopyAnnotations` for Room to properly understand them.
- **Additional Async Support** : DAO methods annotated with `@Insert`, `@Delete` or `@Update`, along with `@Query` containing `INSERT`, `DELETE` or `UPDATE` statements, now support Rx return types `Completable`, `Single`, `Maybe`, and Guava's return type `ListenableFuture`, and they can also be suspend functions.
- `enableMultiInstanceInvalidation` is a new API in `RoomDatabase.Builder` to enable invalidation across multiple instances of RoomDatabase using the same database file.
- `fallbackToDestructiveMigrationOnDowngrade` is a new API in `RoomDatabase.Builder` to automatically re-create the database if a downgrade happens.
- `ignoredColumns` is a new API in the `@Entity` annotation that can be used to list ignored fields by name.
- Room will now properly use Kotlin's primary constructor in data classes avoiding the need to declare the properties as `vars`.

### Version 2.1.0-rc01

May 29, 2019

**Bug Fixes**

- Fixed a Room initialization error that might occur due to an already setup temp_store configuration. [b/132602198](https://issuetracker.google.com/issues/132602198)
- Fixed a double quote usage warning for users with SQLite 3.27.0 and above. [b/131712640](https://issuetracker.google.com/issues/131712640)
- Fixed a bug where the InvalidationTracker would cause a crash when multiple invalidation checks would occur in parallel. [b/133457594](https://issuetracker.google.com/issues/133457594)

### Version 2.1.0-beta01

May 7, 2019

`androidx.room 2.1.0-beta01` is released with no changes from 2.1.0-alpha07. The commits included in this version can be found [here](https://android.googlesource.com/platform/frameworks/support/+log/9a00dbb5a21ad46c78b5ce525c761542f95d7cc3..92174716bb8c7d3088badc0b72b4e83dc8bf2c1b/room).

### Version 2.1.0-alpha07

April 25, 2019

**API / Behavior Changes**

- The extension function `RoomDatabase.withTransaction` has been changed to no longer take a function block with a `CoroutineScope` as receiver. This prevents skipping the additional `coroutineScope { }` wrapper required to run things in the transaction block concurrently.

**Bug Fixes**

- Fixed a bug where Room would fail to match a TypeConverter for a Kotlin DAO function containing a parameter of Collection type. [b/122066791](https://issuetracker.google.com/issues/122066791)

### Version 2.1.0-alpha06

March 22, 2019

**API / Behavior Changes**

- Async transaction queries are now serialized such that Room will not use more than one thread for executing database transactions. `RoomDatabase.Builder.setTransactionExecutor(Executor)` was added to allow configuring the executor to be used for transactions.
- `RoomDatabase.runInTransaction(Callable)` will no longer wrap checked exceptions into RuntimeExceptions. [b/128623748](https://issuetracker.google.com/issues/128623748)

**Bug Fixes**

- Fixed a bug where the invalidation tracker would stop observing a content table if observers for both the content table and an external content FTS table were added. [b/128508917](https://issuetracker.google.com/issues/128508917)
- Updated `Room` SQLite grammar to match SQLite 3.24.0. [b/110883668](https://issuetracker.google.com/issues/110883668)

### Version 2.1.0-alpha05

March 13, 2019

**New Features**

- The extension function `RoomDatabase.withTransaction` allows you to safely perform database transactions within a coroutine. Room extensions functions along with coroutines support are available in the `room-ktx` artifact.
- Non-abstract DAO methods annotated with `@Transaction` can now be suspend functions. [b/120241587](https://issuetracker.google.com/issues/120241587)

**API / Behavior Changes**

- The artifact `room-coroutines` has been renamed to `room-ktx` following the same naming as other androidx artifacts.
- `beginTransaction`, `setTransactionSuccessful` and `endTransaction` in `RoomDatabase` have been deprecated in favor of `runInTransaction` and the `room-ktx` extension function `withTransaction`.

**Bug Fixes**

- Fixed a bug where tokenizer arguments were being dropped if the tokenizer used was SIMPLE. [b/125427014](https://issuetracker.google.com/issues/125427014)
- Fixed a bug where Room would fail to correctly identify suspending functions with parameters whos type were an inner class. [b/123767877](https://issuetracker.google.com/issues/123767877)
- Fixed a bug where deferred `@Query` DAO method with `INSERT`, `UPDATE` or `DELETE` statements were eagerly preparing the query in the main thread. [b/123695593](https://issuetracker.google.com/issues/123695593)
- Fixed various bugs where Room would generate incorrect code for certain suspend functions. [b/123466702](https://issuetracker.google.com/issues/123466702) and [b/123457323](https://issuetracker.google.com/issues/123466702)
- Fixed a bug where deprecated usage of methods were not being correctly suppressed in generated code. [b/117602586](https://issuetracker.google.com/issues/117602586)
- Updated Room dependency of androidx.sqlite to 1.0.2 which contain fixes for correctly handling corrupted databases. [b/124476912](https://issuetracker.google.com/issues/124476912)

**Known Issues**

- Room 2.1.0-alpha05 depends on the `kotlinx-metadata-jvm` artifact which is not currently available in Maven Central ([KT-27991](https://youtrack.jetbrains.com/issue/KT-27991)). This dependency can be resolved by adding `maven { url "https://kotlin.bintray.com/kotlinx/" }` to your project repositories.

### Version 2.1.0-alpha04

January 25, 2019

**New Features**

- DAO methods annotated with `@Query` containing `INSERT`, `UPDATE` or `DELETE` statements can now return async types `Single`, `Mayble`, `Completable` and `ListenableFuture`. Additionally they can also be suspend functions. [b/120227284](https://issuetracker.google.com/120227284)

**API / Behavior Changes**

- Room will now throw an error if a non-abstract DAO method annotated with `@Transaction` returns an async type such as `Single`, `Mayble`, `Completable`, `LiveData` or `ListenableFuture`. Since transactions are thread confined it is currently impossible for Room to begin and end a transaction around a function that may peform queries in different threads. [b/120109336](https://issuetracker.google.com/120109336)
- `OnConflictStrategy.FAIL` and `OnConflictStrategy.ROLLBACK` have been `@Deprecated` since they do not behave as intended with Android's current SQLite bindings. [b/117266738](https://issuetracker.google.com/117266738)

**Bug Fixes**

- Fixed a bug where Room wouldn't correctly use the TypeConverter of a return type if the DAO method was a suspend function. [b/122988159](https://issuetracker.google.com/122988159)
- Fixed a bug where Room would incorrectly identify inherited suspend functions as non-suspending. [b/122902595](https://issuetracker.google.com/122902595)
- Fixed a bug where Room would generate incorrect code when an `@Embedded` field was in a parent class and used in multiple child classes. [b/121099048](https://issuetracker.google.com/121099048)
- Fixed an issue where the database would deadlock when invoking DAO suspend functions between a `beginTransaction()` and `endTransaction()`. [b/120854786](https://issuetracker.google.com/120854786)

### Version 2.1.0-alpha03

December 4, 2018

**API Changes**

- The FTS `tokenizer` in `@Fts3`/`@Fts4` now takes a String instead of an Enum. This allows custom tokenizers to be used by Room. Built-in tokenizers are still defined in `FtsOptions` as string constants. [b/119234881](https://issuetracker.google.com/119234881)

**New Features**

- **Couroutines** : DAO methods can now be suspend functions. To support suspend functions in Room a new artifact has been released, `room-coroutines`. [b/69474692](https://issuetracker.google.com/69474692)
- DAO methods annotated with `@Insert`, `@Delete` or `@Update` now support `ListenableFuture` as return type. [b/119418331](https://issuetracker.google.com/119418331)

**Bug Fixes**

- Fixed a bug where Room would incorrectly attempt to find a constructor with columns in the `ignoredColumns` property of `@Entity`. [b/119830714](https://issuetracker.google.com/119830714)
- Fixed a bug where Room would not mark DAO method parameters as final in their generated implementation. [b/118015483](https://issuetracker.google.com/118015483)
- Fixed a bug where `Room` processor would crash when reporting an error on a query with special symbols. [b/119520136](https://issuetracker.google.com/119520136)
- Fixed a bug where Room would decline other various `Collection` implementations as arguments of an `IN` expression. [b/119884035](https://issuetracker.google.com/119884035)
- Fixed a bug where LiveData returned from Room would get garbage collected when observed forever causing it to no longer emit new data. [b/74477406](https://issuetracker.google.com/74477406)
- Updated `RoomDatabase`'s close lock to reduce lock contention. [b/117900450](https://issuetracker.google.com/117900450)

### Version 2.1.0-alpha02

October 30, 2018

**New Features**

- Added support for referencing a `@DatabaseView` in a `@Relation`. [b/117680932](https://issuetracker.google.com/117680932)

**Bug Fixes**

- Fixed a bug where Room would perform disk I/O in the main thread when subscribing and disposing from an Rx return type. [b/117201279](https://issuetracker.google.com/117201279)
- Fixed a bug where Room would fail to find an appropriate type converter for a field in a Kotlin entity class. [b/111404868](https://issuetracker.google.com/111404868)
- Fixed a bug where Room would generate incorrect code for a `DAO` interface implementation containing a Kotlin default method that has no arguments. [b/117527454](https://issuetracker.google.com/117527454)
- Updated `Room` SQLite grammar parser, fixing a performance issue that would cause long build times. [b/117401230](https://issuetracker.google.com/117401230)

### Version 2.1.0-alpha01

October 8, 2018

**New Features**

- **FTS** : Room now supports entities with a mapping [FTS3 or FTS4](https://www.sqlite.org/fts3.html) table. Classes annotated with `@Entity` can now be additionally annotated with `@Fts3` or `@Fts4` to declare a class with a mapping full-text search table. FTS options for further customization are available via the annotation's methods. [b/62356416](https://issuetracker.google.com/62356416)
- **Views** : Room now supports declaring a class as a stored query, also known as a [view](https://www.sqlite.org/lang_createview.html) using the @DatabaseView annotation. [b/67033276](https://issuetracker.google.com/67033276)
- **Auto Value** : Room now supports declaring [AutoValue](https://github.com/google/auto/blob/master/value/userguide/index.md) annotated classes as entities and POJOs. The Room annotations `@PrimaryKey`, `@ColumnInfo`, `@Embedded` and `@Relation` can now be declared in an auto value annotated class' abstract methods. Note that these annotation must also be accompanied by `@CopyAnnotations` for Room to properly understand them. [b/62408420](https://issuetracker.google.com/62408420)
- **Additional Rx Return Types Support** : DAO methods annotated with `@Insert`, `@Delete` or `@Update` now support Rx return types `Completable`, `Single<T>` and `Maybe<T>`. [b/63317956](https://issuetracker.google.com/63317956)
- **Immutable Types with `@Relation`** : Room previously required `@Relation` annotated fields to be settable but now they can be constructor parameters.
- `enableMultiInstanceInvalidation`: Is a new API in `RoomDatabase.Builder` to enable invalidation across multiple instances of RoomDatabase using the same database file. This multi-instance invalidation mechanism also works across multiple processes. [b/62334005](https://issuetracker.google.com/62334005)
- `fallbackToDestructiveMigrationOnDowngrade`: Is a new API in `RoomDatabase.Builder` to automatically re-create the database if a downgrade happens. [b/110416954](https://issuetracker.google.com/110416954)
- `ignoredColumns`: Is a new API in the `@Entity` annotation that can be used to list ignored fields by name. Useful for ignoring inherited fields on an entity. [b/63522075](https://issuetracker.google.com/63522075)

**API / Behavior Changes**

- `mCallback` and `mDatabase` in `RoomDatabase` are now `@Deprecated` and will be removed in the next major version of Room. [b/76109329](https://issuetracker.google.com/76109329)

**Bug Fixes**

- Fixed two issues where Room wouldn't properly recover from a corrupted database or a bad migration during initialization. [b/111504749](https://issuetracker.google.com/111504749) and [b/111519144](https://issuetracker.google.com/111519144)
- Room will now properly use Kotlin's primary constructor in data classes avoiding the need to declare the fields as `vars`. [b/105769985](https://issuetracker.google.com/105769985)

## Version 2.0.0

### Version 2.0.0

October 1, 2018

`androidx.room 2.0.0` is released with no changes from 2.0.0-rc01.

### Version 2.0.0-rc01

September 20, 2018

`androidx.room 2.0.0-rc01` is released with no changes from 2.0.0-beta01.

### Version 2.0.0-beta01

July 2, 2018

**API / Behavior Changes**

- Added `RoomDatabase.Builder.setQueryExecutor()` to allow customization of where queries are run
- Added RxJava2 `Observable` support
- Generated DAO and Database implementations are now final

**Bug Fixes**

- Specify class/field name in "cannot find getter for field" error [b/73334503](https://issuetracker.google.com/issues/73334503)
- Fixed RoomOpenHelper backwards compatibility with older versions of Room [b/110197391](https://issuetracker.google.com/issues/110197391)

## Pre-AndroidX Dependencies

For the pre-AndroidX versions of Room, include these dependencies:

    dependencies {
        def room_version = "1.1.1"

        implementation "android.arch.persistence.room:runtime:$room_version"
        annotationProcessor "android.arch.persistence.room:compiler:$room_version" // For Kotlin use kapt instead of annotationProcessor

        // optional - RxJava support for Room
        implementation "android.arch.persistence.room:rxjava2:$room_version"

        // optional - Guava support for Room, including Optional and ListenableFuture
        implementation "android.arch.persistence.room:guava:$room_version"

        // Test helpers
        testImplementation "android.arch.persistence.room:testing:$room_version"
    }

## Version 1.1.1

### Version 1.1.1

June 19, 2018

Room `1.1.1` is identical to Room `1.1.1-rc1`.

### Version 1.1.1-rc1

May 16, 2018
We highly
recommend using Room `1.1.1-rc1` instead of `1.1.0` if you are using migrations.

Fixed a bug where Room would not handle post migration initialization properly [b/79362399](https://issuetracker.google.com/issues/79362399)

## Version 1.1.0

### Version 1.1.0-beta3

April 19, 2018

**Bug Fixes**

- Fix compilation error when a Kotlin POJO references a relation entity that was defined in Java [b/78199923](https://issuetracker.google.com/issues/78199923)

### Version 1.1.0-beta2

April 5, 2018

**Bug Fixes**

- Fixed a critical bug in `Room` Rx `Single` and `Maybe` implementations where
  it would recycle the query ahead of time, causing problems if you add more than
  1 observer to the returned `Single` or `Maybe` instances.
  [b/76031240](https://issuetracker.google.com/issues/76031240)

- \[RoomDatabase.clearAllTables\]\[ref-clearAllTables\] will not `VACUUM` the
  database if it is called inside a transaction.
  [b/77235565](https://issuetracker.google.com/issues/77235565)

### Version 1.1.0-beta1

March 21, 2018

**API Changes**

- Based on API Review feedback, `@RawQuery` does not accept passing a `String` as the query parameter anymore. You need to use \[SupportSQLiteQuery\]\[ref-SupportSQLiteQuery\]. (see \[SimpleSQLiteQuery\]\[ref-SimpleSQLiteQuery\] to easily create an instance of \[SupportSQLiteQuery\]\[ref-SupportSQLiteQuery\] with argument support).
- RoomDatabase.Builder's \[fallbackToDestructiveMigrationFrom\]\[ref-fallbackToDestructiveMigrationFrom\] method now accepts `vararg int` instead of `vararg Integer`.

**Bug Fixes**

- \[RoomDatabase.clearAllTables\]\[ref-clearAllTables\] now tries to return space back to the operating system by setting a WAL checkpoint and `VACUUM`ing the database.
- \[`@RawQuery`\]\[ref-RawQuery\] now accepts any Pojo for the `observedEntities` property as long as the Pojo references to one or more entities via its `Embedded` fields or `Relation`s. [b/74041772](https://issuetracker.google.com/issues/74041772)
- Paging: Room's DataSource implementation now correctly handles multi-table dependencies (such as relations, and joins). Previously these would fail to trigger new results, or could fail to compile. [b/74128314](https://issuetracker.google.com/issues/74128314)

### Version 1.1.0-alpha1

January 22, 2018

**New Features**

- `RawQuery`: This new API allows `@Dao` methods to receive the SQL as a query parameter [b/62103290](https://issuetracker.google.com/issues/62103290), [b/71458963](https://issuetracker.google.com/issues/71458963)
- `fallBackToDestructiveMigrationsFrom`: This new API in `RoomDatabase.Builder` allows for finer grained control over from which starting schema versions destructive migrations are allowed (as compared to fallbackToDestructiveMigration) [b/64989640](https://issuetracker.google.com/issues/64989640)
- Room now only supports newer Paging APIs (alpha-4+), dropping support for the deprecated `LivePagedListProvider`. To use the new Room alpha, you'll need to use paging `alpha-4` or higher, and switch from `LivePagedListProvider` to `LivePagedListBuilder` if you haven't already.

**Bug Fixes**

- Improved support for Kotlin Kapt types. [b/69164099](https://issuetracker.google.com/issues/69164099)
- Order of fields do not invalidate schema anymore. [b/64290754](https://issuetracker.google.com/issues/64290754)