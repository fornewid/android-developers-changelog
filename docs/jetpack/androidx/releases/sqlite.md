---
title: https://developer.android.com/jetpack/androidx/releases/sqlite
url: https://developer.android.com/jetpack/androidx/releases/sqlite
source: md.txt
---

# Sqlite

# Sqlite

[User Guide](https://developer.android.com/training/data-storage/sqlite)  
API Reference  
[androidx.sqlite.db](https://developer.android.com/reference/kotlin/androidx/sqlite/db/package-summary)  
[androidx.sqlite.db.framework](https://developer.android.com/reference/kotlin/androidx/sqlite/db/framework/package-summary)  
The`androidx.sqlite`library contains abstract interfaces along with basic implementations which can be used to build your own libraries that access SQLite.

<br />

You might want to consider using the[Room](https://developer.android.com/training/data-storage/room)library, which provides an abstraction layer over SQLite to allow for more robust database access while harnessing the full power of SQLite.  

|   Latest Update   |                                Stable Release                                 | Release Candidate | Beta Release | Alpha Release |
|-------------------|-------------------------------------------------------------------------------|-------------------|--------------|---------------|
| November 19, 2025 | [2.6.2](https://developer.android.com/jetpack/androidx/releases/sqlite#2.6.2) | -                 | -            | -             |

## Declaring dependencies

To add a dependency on SQLite, you must add the Google Maven repository to your project. Read[Google's Maven repository](https://developer.android.com/studio/build/dependencies#google-maven)for more information.

Add the dependencies for the artifacts you need in the`build.gradle`file for your app or module:  

### Groovy

```groovy
dependencies {
    def sqlite_version = "2.6.2"

    // Java language implementation
    implementation "androidx.sqlite:sqlite:$sqlite_version"

    // Kotlin
    implementation "androidx.sqlite:sqlite-ktx:$sqlite_version"

    // Implementation of the AndroidX SQLite interfaces via the Android framework APIs.
    implementation "androidx.sqlite:sqlite-framework:$sqlite_version"
}
```

### Kotlin

```kotlin
dependencies {
    val sqlite_version = "2.6.2"

    // Java language implementation
    implementation("androidx.sqlite:sqlite:$sqlite_version")

    // Kotlin
    implementation("androidx.sqlite:sqlite-ktx:$sqlite_version")

    // Implementation of the AndroidX SQLite interfaces via the Android framework APIs.
    implementation("androidx.sqlite:sqlite-framework:$sqlite_version")
}
```

For more information about dependencies, see[Add build dependencies](https://developer.android.com/studio/build/dependencies).

## Feedback

Your feedback helps make Jetpack better. Let us know if you discover new issues or have ideas for improving this library. Please take a look at the[existing issues](https://issuetracker.google.com/issues?q=componentid:460784+status:open)in this library before you create a new one. You can add your vote to an existing issue by clicking the star button.

[Create a new issue](https://issuetracker.google.com/issues/new?component=460784&template=1422805)

See the[Issue Tracker documentation](https://developers.google.com/issue-tracker)for more information.

## Version 2.6

### Version 2.6.2

November 19, 2025

`androidx.sqlite:sqlite-*:2.6.2`is released. Version 2.6.2 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/3dedecfe17d38214f45bae25dc56ebda7396fd9b..fe30df161d480829efb21f37ff67a9f8cac9c620/sqlite).

**Bug Fixes**

- Improve`BundledSQLiteDriver`performance by using`@FastNative`to improve JNI calls. ([952b92](https://android-review.googlesource.com/#/q/952b92a57fa36d38a644237dab9da1001655fb42),[b/313895287](https://issuetracker.google.com/313895287))
- Enable extended error codes on the`SQLite`connections created by`BundledSQLiteDriver`. This means error messages coming from`SQLite`will have a more detailed code which is useful for diagnosing I/O issues and constraint violations. ([f1ec6f](https://android-review.googlesource.com/#/q/f1ec6f57459dafc7611c091bd3570a9923905112))

### Version 2.6.1

September 24, 2025

`androidx.sqlite:sqlite-*:2.6.1`is released. Version 2.6.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/a2faf658056991fffccb741a8bf6d294986fb06c..3dedecfe17d38214f45bae25dc56ebda7396fd9b/sqlite).

**Bug Fixes**

- Fixed R8 rule for native functions to allow proper obfuscation ([b/442489402](https://issuetracker.google.com/442489402)).
- Fix a NPE that could happen when using the support API`getBeginTransactionMethod`on a concurrent scenario. ([b/444049518](https://issuetracker.google.com/444049518)).
- Reduce the JNI/native dependencies of bundled-sqlite to increase compatibility when loading the library. ([b/442489402](https://issuetracker.google.com/442489402)).
- Fix an issue with the`AndroidSQLiteDriver`that would disable the multiple connections pool even if the journal was set to WAL mode ([b/444286035](https://issuetracker.google.com/444286035)).

### Version 2.6.0

September 10, 2025

`androidx.sqlite:sqlite-*:2.6.0`is released. Version 2.6.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ead4fdfdf41033c69b4e9c81b64f36961afac7f8..a2faf658056991fffccb741a8bf6d294986fb06c/sqlite).

**Important changes since 2.5.0:**

- Support loading SQLite extensions by adding the`addExtension`function to`BundledSQLiteDriver`, which can be used to register extensions that SQLite should dynamically load for connections opened with that particular driver.
- Added support for KMP targets Watch OS and Tv OS.
- Updated the library's Android minSDK from API 21 to API 23.

### Version 2.6.0-rc02

August 27, 2025

`androidx.sqlite:sqlite-*:2.6.0-rc02`is released. Version 2.6.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/78f6397a66261c0f56a9f1abd035301011f473d4..ead4fdfdf41033c69b4e9c81b64f36961afac7f8/sqlite).

**API Changes**

- Update the minSDK from API 21 to API 23 ([Ibdfca](https://android-review.googlesource.com/#/q/Ibdfca5942dbb414ca07594ba240093db14aad4df),[b/380448311](https://issuetracker.google.com/issues/380448311),[b/435705964](https://issuetracker.google.com/issues/435705964),[b/435705223](https://issuetracker.google.com/issues/435705223))

### Version 2.6.0-rc01

August 13, 2025

`androidx.sqlite:sqlite-*:2.6.0-rc01`is released. Version 2.6.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/e788f9f7947a19e5893e27b87e3d7e5be0921ff2..78f6397a66261c0f56a9f1abd035301011f473d4/sqlite).

### Version 2.6.0-beta01

August 1, 2025

`androidx.sqlite:sqlite-*:2.6.0-beta01`is released. Version 2.6.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d..e788f9f7947a19e5893e27b87e3d7e5be0921ff2/sqlite).

**New Features**

- `androidx.sqlite`now supports loading SQLite extensions by adding the`addExtension`method to`BundledSQLiteDriver`, which can be used to register extensions that`SQLite`should dynamically load against connections opened against that particular driver. Thanks to Simon Binder for this contribution! ([I64d6f](https://android-review.googlesource.com/#/q/I64d6f5da7d55c7ee5c4f8207451697524121749e),[I2721b](https://android-review.googlesource.com/#/q/I2721b3b5df66aa315f0b5da4db933328aabdd268),[b/430960837](https://issuetracker.google.com/issues/430960837),[b/434203987](https://issuetracker.google.com/issues/434203987))

### Version 2.6.0-alpha01

July 16, 2025

`androidx.sqlite:sqlite-*:2.6.0-alpha01`is released. Version 2.6.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/98552a7cab42f1d19ee63ca0b2cd5f5bb862510d/sqlite).

**New Features**

- Added KMP targets for Watch OS and TV OS ([I45883](https://android-review.googlesource.com/#/q/I4588365177ad121dd7523b064935ef356a4ba6e4),[b/427889948](https://issuetracker.google.com/issues/427889948))

**API Changes**

- Add an API for checking if a`SQLiteConnection`has an active transaction. Since`SQLite`transactions are not nested this API can help the applications determine if they should use BEGIN / COMMIT or SAVEPOINT / RELEASE. ([I5bf5e](https://android-review.googlesource.com/#/q/I5bf5e63678767d6894250d6eec4a879c7b8ac1fa),[b/319627988](https://issuetracker.google.com/issues/319627988))
- Add an API to`SQLiteDriver`to report if internally it has a connection pool or not. ([I52a51](https://android-review.googlesource.com/#/q/I52a5148dfeab4e576b613bb9d25f725d0c641a8e),[b/408010324](https://issuetracker.google.com/issues/408010324))

## Version 2.5

### Version 2.5.2

June 18, 2025

`androidx.sqlite:sqlite-*:2.5.2`is released. Version 2.5.2 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9f17a3139a3fbb6b40703a8357a7ef29e87e53ca..4dfb0ab4cfef2fe41ce417f4c7eba66a397a631c/sqlite).

**Bug Fixes**

- Add missing R8 / Proguard rules to keep JNI / external functions from being obfuscated. ([b/421626199](https://issuetracker.google.com/421626199))
- Fix a bug where leading comments in a SQL would cause statements to be executed as if they were non-read queries. ([b/413061402](https://issuetracker.google.com/413061402))

### Version 2.5.1

May 7, 2025

`androidx.sqlite:sqlite-*:2.5.1`is released. Version 2.5.1 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/185681c8628221c6ed490c001383096e41e1c5c9..9f17a3139a3fbb6b40703a8357a7ef29e87e53ca/sqlite).

**API Changes**

- Allow`androidx.sqlite:sqlite-bundled`to load its native component from a specified path via the system property named`androidx.sqlite.driver.bundled.path`.[b/381282544](https://issuetracker.google.com/381282544)

### Version 2.5.0

April 9, 2025

`androidx.sqlite:sqlite-*:2.5.0`is released. Version 2.5.0 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/c53731a05bcf93fc76e9934fd0b0d76cb2bbe34f..185681c8628221c6ed490c001383096e41e1c5c9/sqlite).

**Important changes since 2.4.0**

- **Kotlin Multi-Platform (KMP) Support:** With the release of Room KMP version 2.7.0 the`SQLite`APIs that enable Room to be KMP have also been updated. The package`andriodx.sqlite`contains three interfaces that define low-level`SQLite`APIs:`SQLiteDriver`,`SQLiteConnection`and`SQLiteStatement`. The artifact`androidx.sqlite:sqlite-framework`offers implementation of the interfaces for Android and iOS natively, while`androidx.sqlite:sqlite-bundled`offers an implementation that uses SQLite compiled from source (also known as "bundled SQLite"). For more information about the`SQLite`Driver API refer to the[official SQLite KMP documentation](https://developer.android.com/kotlin/multiplatform/sqlite).

### Version 2.5.0-rc03

March 26, 2025

`androidx.sqlite:sqlite-*:2.5.0-rc03`is released. Version 2.5.0-rc03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/28604964f808b04cbb5768fbcc81d4f76e6ce14d..c53731a05bcf93fc76e9934fd0b0d76cb2bbe34f/sqlite).

**Bug Fixes**

- Revert a binary breaking incompatible change that incorrectly removed`SupportSQLiteCompat`APIs used by other libraries such as Room ([b/402796648](https://issuetracker.google.com/402796648)).

### Version 2.5.0-rc02

March 12, 2025

`androidx.sqlite:sqlite-*:2.5.0-rc02`is released with no notable changes since the last release. Version 2.5.0-rc02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/fd7408b73d9aac0f18431c22580d9ab612278b1e..28604964f808b04cbb5768fbcc81d4f76e6ce14d/sqlite).

### Version 2.5.0-rc01

February 26, 2025

`androidx.sqlite:sqlite-*:2.5.0-rc01`is released. Version 2.5.0-rc01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/24c00eb294d9cda579d8d6e48a29497fe0f8d3f7..fd7408b73d9aac0f18431c22580d9ab612278b1e/sqlite).

**Bug Fixes**

- Fix the Gradle Metadata of the`androidx.sqlite`artifacts for JVM that would cause JVM projects to resolve the Android variant and would lead to`NoClassDefFoundError: androidx/sqlite/SQLiteDriver`([b/396148592](https://issuetracker.google.com/396148592)and[b/396184120](https://issuetracker.google.com/396184120)).

### Version 2.5.0-beta01

February 12, 2025

`androidx.sqlite:sqlite-*:2.5.0-beta01`is released with no notable changes since the last alpha. Version 2.5.0-beta01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f383921582ae43bfe6fb2f11d71b8ace3f9ceb65..24c00eb294d9cda579d8d6e48a29497fe0f8d3f7/sqlite).

### Version 2.5.0-alpha13

January 29, 2025

`androidx.sqlite:sqlite-*:2.5.0-alpha13`is released. Version 2.5.0-alpha13 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/46295bc0b75a16f452e8e0090e8de41073d4dbb6..f383921582ae43bfe6fb2f11d71b8ace3f9ceb65/sqlite).

**API Changes**

- Remove`androidx.sqlite.use`which is now replaced by Kotlin's`AutoCloseable.use`in the stdlib. ([I470f0](https://android-review.googlesource.com/#/q/I470f02620d43bbe641c58e3fc3637119e8c44532),[b/315461431](https://issuetracker.google.com/issues/315461431))
- The library is now compiled with Kotlin 2.0 and will require at least 2.0 in projects to be used. ([I8efb0](https://android-review.googlesource.com/#/q/I8efb015c88682921780370c8bed5931d9933a319),[b/315461431](https://issuetracker.google.com/issues/315461431),[b/384600605](https://issuetracker.google.com/issues/384600605))

**Bug Fixes**

- Move the native library loading of`BundledSQLiteDriver`to be lazy and when the first connection is opened to avoid the possibility of performing IO in the main thread. ([I78e92](https://android-review.googlesource.com/#/q/4f69d19088dae47b6a7bcf454ea22f7e2da78e92),[b/363985585](https://issuetracker.google.com/issues/363985585))

### Version 2.5.0-alpha12

December 11, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha12`is released. Version 2.5.0-alpha12 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/ccd90a76bd7c4acf4f4f01eca76350e383bc441e..46295bc0b75a16f452e8e0090e8de41073d4dbb6/sqlite).

### Version 2.5.0-alpha11

October 30, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha11`is released. Version 2.5.0-alpha11 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b8a68b0896897fa158508d73a31998a26161d9a7..ccd90a76bd7c4acf4f4f01eca76350e383bc441e/sqlite).

### Version 2.5.0-alpha10

October 16, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha10`is released. Version 2.5.0-alpha10 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6..b8a68b0896897fa158508d73a31998a26161d9a7/sqlite).

**API Changes**

- Add`SQLiteStatement.getColumnType()`along with the various`SQLITE_DATA_*`result constants to enable retrieving the data type of a column. ([I1985c](https://android-review.googlesource.com/#/q/I1985c7b267ba4d6342cb487cbe6e889bed3ff26d),[b/369636251](https://issuetracker.google.com/issues/369636251))

### Version 2.5.0-alpha09

October 2, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha09`is released. Version 2.5.0-alpha09 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/0431b84980e97d6bafdfda7c9038bc4d9529564f..b6ae8d0a0e8cd803f7b84f30101eda1af4f1d6b6/sqlite).

### Version 2.5.0-alpha08

September 18, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha08`is released. Version 2.5.0-alpha08 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/8c4071562bd7e22b937284d71fb7aca9c4cd662c..0431b84980e97d6bafdfda7c9038bc4d9529564f/sqlite).

### Version 2.5.0-alpha07

August 21, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha07`is released. Version 2.5.0-alpha07 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/9130b719318a69f2f3eaf82c32b131232fd721cb..8c4071562bd7e22b937284d71fb7aca9c4cd662c/sqlite).

**New Features**

- Add support for Linux ARM 64 in JVM / Desktop targets. ([b/358045505](https://issuetracker.google.com/358045505))

### Version 2.5.0-alpha06

August 7, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha06`is released. Version 2.5.0-alpha06 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/56579bc30499ce39f0d7a6713a065b00c6194206..9130b719318a69f2f3eaf82c32b131232fd721cb/sqlite).

**New Features**

- Add support for`linuxArm64`Kotlin Multiplatform target ([I139d3](https://android-review.googlesource.com/#/q/I139d36226a3d06d9768bd63302de98b576a12a48),[b/338268719](https://issuetracker.google.com/issues/338268719))

### Version 2.5.0-alpha05

July 10, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha05`is released. Version 2.5.0-alpha05 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/f5541f29d045c6ba9734689ec67891f8d667412b..56579bc30499ce39f0d7a6713a065b00c6194206/sqlite).

**API Changes**

- Renamed`SQLiteKt`to`SQLite`and`BundledSQLiteKt`to`BundledSQLite`. ([I8b501](https://android-review.googlesource.com/#/q/I8b5016b9769244342bab288bab976ebe9fe5d11d))

### Version 2.5.0-alpha04

June 12, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha04`is released. Version 2.5.0-alpha04 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/473554f275109d78164adca6b6cea539aed8b68b..f5541f29d045c6ba9734689ec67891f8d667412b/sqlite).

**API Changes**

- Added an`open()`overload API to`BundledSQLiteDriver`to pass open flags when opening a database connection. Useful for opening a database in read-only mode or using the serialized thread safe mode instead of the multi-thread mode bundled SQLite is compiled with ([b/340949940](https://issuetracker.google.com/issues/340949940)).

**Bug Fixes**

- Fixed a linking issue in the Bundled SQLite Driver that would cause`UnsatisfiedLinkError`to be thrown due to missing atomic symbols in Android devices with an ARM32. ([b/341639198](https://issuetracker.google.com/341639198))
- Fixed an issue in the drivers where binding a zero-length byte array into a column would lead to a null value when reading from it.

### Version 2.5.0-alpha03

May 29, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha03`is released. Version 2.5.0-alpha03 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/6a69101fd0edc8d02aa316df1f43e0552fd2d7c4..473554f275109d78164adca6b6cea539aed8b68b/sqlite).

**Bug Fixes**

- Fix an issue with the`BundledSQLiteDriver`where databases created with it would contain the C null terminator character. ([b/340822359](https://issuetracker.google.com/issues/314151707))

### Version 2.5.0-alpha02

May 14, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha02`is released with no significant changes since 2.5.0-alpha01 . Version 2.5.0-alpha02 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/291c06f46eebb10fbf9d07b9d36e41dd1bd6f980..6a69101fd0edc8d02aa316df1f43e0552fd2d7c4/sqlite).

### Version 2.5.0-alpha01

May 1, 2024

`androidx.sqlite:sqlite-*:2.5.0-alpha01`is released. Version 2.5.0-alpha01 contains[these commits](https://android.googlesource.com/platform/frameworks/support/+log/291c06f46eebb10fbf9d07b9d36e41dd1bd6f980/sqlite).

**New Features**

- **Kotlin Multi-Platform (KMP) Support** : With the release of Room 2.7.0-alpha01 which is the first release of Room KMP, the`SQLite`APIs that enable Room to be KMP have also been updated. The package`andriodx.sqlite`contains three interfaces that define low-level SQLite APIs:`SQLiteDriver`,`SQLiteConnection`and`SQLiteStatement`. The artifact`androidx.sqlite:sqlite-framework`offers implementation of the interfaces for Android and iOS Natively, while`androidx.sqlite:sqlite-bundled`offers an implementation that uses`SQLite`compiled from source (also known as "bundled SQLite"). For more information about the SQLite Driver API refer to the[official SQLite KMP documentation](https://developer.android.com/kotlin/multiplatform/sqlite).

## Version 2.4

### Version 2.4.0

October 18, 2023

`androidx.sqlite:sqlite:2.4.0`,`androidx.sqlite:sqlite-framework:2.4.0`, and`androidx.sqlite:sqlite-ktx:2.4.0`are released.[Version 2.4.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/761ab24acbd0dd0fbc675c82f9c1cf42ad6c8fc3..c2576dcd7beccce96617f96da4c5293e1924885a/sqlite)

**Important changes since 2.3.0**

- Various bug fixes have been added.

### Version 2.4.0-rc01

September 20, 2023

`androidx.sqlite:sqlite:2.4.0-rc01`,`androidx.sqlite:sqlite-framework:2.4.0-rc01`, and`androidx.sqlite:sqlite-ktx:2.4.0-rc01`are released.[Version 2.4.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3315f1ef094c312203fe26841287902916fbedf5..761ab24acbd0dd0fbc675c82f9c1cf42ad6c8fc3/sqlite)

### Version 2.4.0-beta01

August 23, 2023

`androidx.sqlite:sqlite:2.4.0-beta01`,`androidx.sqlite:sqlite-framework:2.4.0-beta01`, and`androidx.sqlite:sqlite-ktx:2.4.0-beta01`are released.[Version 2.4.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5d7dd999525725bd038a00ca4e89e0fef624a6da..3315f1ef094c312203fe26841287902916fbedf5/sqlite)

### Version 2.4.0-alpha03

August 9, 2023

`androidx.sqlite:sqlite:2.4.0-alpha03`,`androidx.sqlite:sqlite-framework:2.4.0-alpha03`, and`androidx.sqlite:sqlite-ktx:2.4.0-alpha03`are released.[Version 2.4.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/3b5b931546a48163444a9eddc533489fcddd7494..5d7dd999525725bd038a00ca4e89e0fef624a6da/sqlite)

### Version 2.4.0-alpha02

June 21, 2023

`androidx.sqlite:sqlite:2.4.0-alpha02`,`androidx.sqlite:sqlite-framework:2.4.0-alpha02`, and`androidx.sqlite:sqlite-ktx:2.4.0-alpha02`are released with no changes.[Version 2.4.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/5e7d256f82fbafb6d059ab7b18fddd87c7531553..3b5b931546a48163444a9eddc533489fcddd7494/sqlite)

### Version 2.4.0-alpha01

March 22, 2023

`androidx.sqlite:sqlite:2.4.0-alpha01`,`androidx.sqlite:sqlite-framework:2.4.0-alpha01`, and`androidx.sqlite:sqlite-ktx:2.4.0-alpha01`are released.[Version 2.4.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b06d4b8c52b58338b7e3a9a32bd153c0c464d224..5e7d256f82fbafb6d059ab7b18fddd87c7531553/sqlite)

**Bug Fixes**

- Fixed a`NullPointerException`that could occur in`SupportSQLiteQueryBuilder`. ([5df8698](https://android.googlesource.com/platform/frameworks/support/+/5df8698b5413f15c9e005762c988eb809f2676d9))

## Version 2.3.1

### Version 2.3.1

March 22, 2023

`androidx.sqlite:sqlite:2.3.1`,`androidx.sqlite:sqlite-framework:2.3.1`, and`androidx.sqlite:sqlite-ktx:2.3.1`are released.[Version 2.3.1 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/b06d4b8c52b58338b7e3a9a32bd153c0c464d224..4bfc36b857955ac99fc6ee686456b6e54dd1c545/sqlite)

**Bug Fixes**

- Avoid a framework issue where SQL queries would not get invalidated after a schema change during migrations.`FrameworkSupportSQLiteOpenHelper`will now set the minimum SQL statement cache during migrations to avoid the problem. ([0ad2a8f](https://android.googlesource.com/platform/frameworks/support/+/0ad2a8f5fc6359fba216519a1bc9af30b7804022))
- Fixed an issue where the cache directory might not be available to use for`SupportSQLiteLock`, thus a null File must be gracefully handled. ([9d177dc](https://android.googlesource.com/platform/frameworks/support/+/9d177dc60d6820ce12e7c3d10d2b5ed9c9a7f8b7))
- Fixed an issue where`attachedDbs`was not returning the full list of attached databases. ([5f008e1](https://android.googlesource.com/platform/frameworks/support/+/5f008e15829528b3d048fbc7e374d8fb4a5ed3fd))

## Version 2.3.0

### Version 2.3.0

January 11, 2023

`androidx.sqlite:sqlite:2.3.0`,`androidx.sqlite:sqlite-framework:2.3.0`, and`androidx.sqlite:sqlite-ktx:2.3.0`are released.[Version 2.3.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/12dae2c26b3e222a26e61ec6ce33cc8dcda28436..b06d4b8c52b58338b7e3a9a32bd153c0c464d224/sqlite)

**Important changes since 2.2.0**

- The library group`androidx.sqlite`sources has been converted from Java to Kotlin. Be aware that because`androidx.sqlite`had some missing nullability annotations you might experience source incompatibility errors if your sources are in Kotlin and the code was inferring the wrong nullability. Moreover, certain getter methods were converted to properties requiring the property access syntax on Kotlin files. Please file a bug if there are any significant incompatibilities. ([b/240707042](https://issuetracker.google.com/issues/240707042))
- Add an API in`SupportSQLite's`configuration to allow data loss during the recovery mechanism. ([I1b830](https://android-review.googlesource.com/c/platform/frameworks/support/+/1971361),[b/215592732](https://issuetracker.google.com/issues/215592732))
- Added API for multi-process lock and usage at the`FrameworkSQLite*`level, to protect multi-process 1st time database creation and migrations. ([Ied267](https://android-review.googlesource.com/c/platform/frameworks/support/+/1797472),[b/193182592](https://issuetracker.google.com/issues/193182592))

### Version 2.3.0-rc01

December 7, 2022

`androidx.sqlite:sqlite:2.3.0-rc01`,`androidx.sqlite:sqlite-framework:2.3.0-rc01`, and`androidx.sqlite:sqlite-ktx:2.3.0-rc01`are released.[Version 2.3.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0e1f344bf2f068d9f829727fd617366a5ec529f1..12dae2c26b3e222a26e61ec6ce33cc8dcda28436/sqlite)

**Bug Fixes**

- Resolving NPE issue in`SupportSQLiteQueryBuilder`for nullable columns. ([Ica8f5](https://android-review.googlesource.com/c/platform/frameworks/support/+/231901))

### Version 2.3.0-beta02

November 9, 2022

`androidx.sqlite:sqlite:2.3.0-beta02`,`androidx.sqlite:sqlite-framework:2.3.0-beta02`, and`androidx.sqlite:sqlite-ktx:2.3.0-beta02`are released.[Version 2.3.0-beta02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/4586cf6e518f0c59410ef2b291e34ff9fdcff4e1..0e1f344bf2f068d9f829727fd617366a5ec529f1/sqlite)

- Fix various APIs that take query arguments from invariant (`Array<Any?>`) to contravariant (`Array<out Any?>`) to match Java's array behavior. ([b/253531073](https://issuetracker.google.com/issues/253531073))

### Version 2.3.0-beta01

October 5, 2022

`androidx.sqlite:sqlite:2.3.0-beta01`,`androidx.sqlite:sqlite-framework:2.3.0-beta01`, and`androidx.sqlite:sqlite-ktx:2.3.0-beta01`are released.[Version 2.3.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/dd1e45e8550560087f6447a34a9145048b5766f4..4586cf6e518f0c59410ef2b291e34ff9fdcff4e1/sqlite)

**API Changes**

- All of android.sqlite sources have been converted from Java to Kotlin.[b/240707042](https://issuetracker.google.com/240707042)
- One notable change of the conversion is that the following getter functions have become properties:
  - In`SupportSQLiteDatabase`:
  - `attachedDbs`
  - `isDatabaseIntegrityOk`
  - `isDbLockedByCurrentThread`
  - `isOpen`
  - `isReadOnly`
  - `isWriteAheadLoggingEnabled`
  - `maximumSize`
  - `pageSize`
  - `path`
  - `version`
  - In`SupportSQLiteOpenHelper`:
  - `databaseName`
  - `readableDatabase`
  - `writableDatabase`

| **Note:** You may experience source incompatibility issues due to the library conversion to Kotlin. If your code is in Kotlin and is using certain APIs, then updating to this new version might require changes in your code. Specifically if you had implementations with overrides with any of the getter functions mentioned above then you need to override them as property getters and not functions.

### Version 2.3.0-alpha05

August 24, 2022

`androidx.sqlite:sqlite:2.3.0-alpha05`,`androidx.sqlite:sqlite-framework:2.3.0-alpha05`, and`androidx.sqlite:sqlite-ktx:2.3.0-alpha05`are released.[Version 2.3.0-alpha05 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/bea814b246f89ff7244e3c6b0648f0b57e47897c..dd1e45e8550560087f6447a34a9145048b5766f4/sqlite)

**API Changes**

- The library group androidx.sqlite sources has been converted from Java to Kotlin. Be aware that because androidx.sqlite had some missing nullability annotations you might experience source incompatibility errors if your sources are in Kotlin and the code was inferring the wrong nullability. Please file a bug if there are any significant incompatibility. ([b/240707042](https://issuetracker.google.com/issues/240707042))

### Version 2.3.0-alpha04

August 10, 2022

`androidx.sqlite:sqlite:2.3.0-alpha04`,`androidx.sqlite:sqlite-framework:2.3.0-alpha04`, and`androidx.sqlite:sqlite-ktx:2.3.0-alpha04`are released.[Version 2.3.0-alpha04 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7cbb37cc779160b89644d03e042c129d0ce025d2..bea814b246f89ff7244e3c6b0648f0b57e47897c/sqlite)

**API Changes**

- Updated nullability ([I29fbd](https://android-review.googlesource.com/#/q/I29fbd53511fe03b2153aa17b90fd30af0c63931a))

### Version 2.3.0-alpha03

June 1, 2022

`androidx.sqlite:sqlite:2.3.0-alpha03`,`androidx.sqlite:sqlite-framework:2.3.0-alpha03`, and`androidx.sqlite:sqlite-ktx:2.3.0-alpha03`are released.[Version 2.3.0-alpha03 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/7ca43e00a517eaeeedc0a21f482b17f06e3d2181..7cbb37cc779160b89644d03e042c129d0ce025d2/sqlite)

**API Changes**

- Make`androidx.sqlite.ProcessLock`restricted. The API is scoped and limited to its function within`androidx.sqlite`and should not be used as a general purpose multi-process lock. ([I1643f](https://android-review.googlesource.com/#/q/I1643fd9874b50a25600581e1ef79af68022998b7))

### Version 2.3.0-alpha02

April 6, 2022

`androidx.sqlite:sqlite:2.3.0-alpha02`,`androidx.sqlite:sqlite-framework:2.3.0-alpha02`, and`androidx.sqlite:sqlite-ktx:2.3.0-alpha02`are released.[Version 2.3.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8..7ca43e00a517eaeeedc0a21f482b17f06e3d2181/sqlite)

- No significant changes since 2.3.0-alpha01

### Version 2.3.0-alpha01

February 23, 2022

`androidx.sqlite:sqlite:2.3.0-alpha01`,`androidx.sqlite:sqlite-framework:2.3.0-alpha01`, and`androidx.sqlite:sqlite-ktx:2.3.0-alpha01`are released.[Version 2.3.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/22d2b6205716d703553cb65f2808040f700ac3e3..9b2b3d8efd5f00bd4af903bbaa926f6a712d0bd8/sqlite)

**API Changes**

- Add an API in SupportSQLite's configuration to allow data loss during the recovery mechanism. ([I1b830](https://android-review.googlesource.com/#/q/I1b83020d4b49cf05b3a64617dceb6c62d04ff663),[b/215592732](https://issuetracker.google.com/issues/215592732))
- Added API for multi-process lock and usage at the FrameworkSQLite\* level, to protect multi-process 1st time database creation and migrations. ([Ied267](https://android-review.googlesource.com/#/q/Ied267cd32e3248cec5ebb772778d2e94fd450270),[b/193182592](https://issuetracker.google.com/issues/193182592))

## Version 2.2.0

### Version 2.2.0

December 15, 2021

`androidx.sqlite:sqlite:2.2.0`,`androidx.sqlite:sqlite-framework:2.2.0`, and`androidx.sqlite:sqlite-ktx:2.2.0`are released.[Version 2.2.0 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/75784ce6dbac6faa5320e5898e9472f02ab8710c..22d2b6205716d703553cb65f2808040f700ac3e3/sqlite)

**Important changes since 2.1.0**

Add default method for`execPerConnectionSQL()`in`SupportSQLiteDatabase`.

### Version 2.2.0-rc01

December 1, 2021

`androidx.sqlite:sqlite:2.2.0-rc01`,`androidx.sqlite:sqlite-framework:2.2.0-rc01`, and`androidx.sqlite:sqlite-ktx:2.2.0-rc01`are released.[Version 2.2.0-rc01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/db0888af4fa9a8eaeaf55cc1f120724bc67bdb20..75784ce6dbac6faa5320e5898e9472f02ab8710c/sqlite)

No significant changes since 2.2.0-beta01.

### Version 2.2.0-beta01

October 13, 2021

`androidx.sqlite:sqlite:2.2.0-beta01`,`androidx.sqlite:sqlite-framework:2.2.0-beta01`, and`androidx.sqlite:sqlite-ktx:2.2.0-beta01`are released.[Version 2.2.0-beta01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/97264aa4532db7f7db1ffb3f42f3a9204971dbfc..db0888af4fa9a8eaeaf55cc1f120724bc67bdb20/sqlite)

- No changes from previous alpha version.

### Version 2.2.0-alpha02

July 21, 2021

`androidx.sqlite:sqlite:2.2.0-alpha02`,`androidx.sqlite:sqlite-framework:2.2.0-alpha02`, and`androidx.sqlite:sqlite-ktx:2.2.0-alpha02`are released.[Version 2.2.0-alpha02 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/ccf79f53033e665475116a4e78ff124df2a52c4b..97264aa4532db7f7db1ffb3f42f3a9204971dbfc/sqlite)

No significant changes since 2.2.0-alpha01. This release is just to align with[Room`2.4.0-alpha04`](https://developer.android.com/jetpack/androidx/releases/room#2.4.0-alpha04)release.

### Version 2.2.0-alpha01

June 16, 2021

`androidx.sqlite:sqlite:2.2.0-alpha01`,`androidx.sqlite:sqlite-framework:2.2.0-alpha01`, and`androidx.sqlite:sqlite-ktx:2.2.0-alpha01`are released.[Version 2.2.0-alpha01 contains these commits.](https://android.googlesource.com/platform/frameworks/support/+log/0642b56f5157707d35974d776ed1eccae38517f5..ccf79f53033e665475116a4e78ff124df2a52c4b/sqlite)

**API Changes**

- Add default method for`execPerConnectionSQL()`in SupportSQLiteDatabase ([I86326](https://android-review.googlesource.com/#/q/I86326d81aad82c1efccbb2087c439655c9b4100f),[b/172270145](https://issuetracker.google.com/issues/172270145))

## Version 2.1.0

| **Note:** newer versions androidx libraries now correctly reflect`implementation`dependencies versus`api`dependencies. If your project relies on an implicit dependency exposed through an`implementation`dependency in version`2.1.0`, it will be necessary to explicitly depend on that dependency in your`build.gradle`.

### Version 2.1.0

January 22, 2020

`androidx.sqlite:sqlite:2.1.0`,`androidx.sqlite:sqlite-framework:2.1.0`, and`androidx.sqlite:sqlite-ktx:2.1.0`are released with no changes since`2.1.0-rc01`.[Version 2.1.0 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/1c41b4cf882cca6eac765d7f2b0911addd0edc0c..0642b56f5157707d35974d776ed1eccae38517f5/sqlite).

**Important changes since 2.0.1**

- Support for`useNoBackupDirectory`which can be used to indicate that the database should be created in the no backup directory when using`SupportSQLiteOpenHelper`.

### Version 2.1.0-rc01

January 8, 2020

`androidx.sqlite:sqlite-*:2.1.0-rc01`is released.[Version 2.1.0-rc01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/ce2902e01f920f17637879b6c918ffe987d2f35b..1c41b4cf882cca6eac765d7f2b0911addd0edc0c/sqlite).

This release is identical to[`2.1.0-beta01`](https://developer.android.com/jetpack/androidx/releases/sqlite#2.1.0-alpha01).

### Version 2.1.0-beta01

December 4, 2019

`androidx.sqlite:sqlite:2.1.0-beta01`,`androidx.sqlite:sqlite-framework:2.1.0-beta01`, and`androidx.sqlite:sqlite-ktx:2.1.0-beta01`are released with no changes since`2.1.0-alpha01`.[Version 2.1.0-beta01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/0b58731e733ba8c3fd60fb2edf2806d134dc19c9..ce2902e01f920f17637879b6c918ffe987d2f35b/sqlite).

### Version 2.1.0-alpha01

November 7, 2019

`androidx.sqlite:sqlite:2.1.0-alpha01`,`androidx.sqlite:sqlite-framework:2.1.0-alpha01`, and`androidx.sqlite:sqlite-ktx:2.1.0-alpha01`are released.[Version 2.1.0-alpha01 contains these commits](https://android.googlesource.com/platform/frameworks/support/+log/eace942fd0bbc3d2ee2ee3380ad48e2cfe8d6da9..0b58731e733ba8c3fd60fb2edf2806d134dc19c9/sqlite).

**API changes**

- Added a new property to`SupportSQLiteOpenHelper.Configuration`called`useNoBackupDirectory`to indicate that a file based database should be created and located from the no backup directory.

## Version 2.0.1

### Version 2.0.1

March 13, 2019

Version 2.0.1 of the`androidx.sqlite`artifact group is released with two bug fixes.

**Bug Fixes**

- Fixed two issues where`FrameworkSQLiteOpenHelper`wouldn't properly recover from a corrupted database or a bad migration during initialization. ([b/111504749](https://issuetracker.google.com/111504749)and[b/111519144](https://issuetracker.google.com/111519144))