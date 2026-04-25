---
title: https://developer.android.com/blog/posts/modernizing-the-room
url: https://developer.android.com/blog/posts/modernizing-the-room
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Room 3.0 - Modernizing the Room

###### 4-min read

![](https://developer.android.com/static/blog/assets/elevating_Media2_20563cb635_1XxrMX.webp) 13 Mar 2026 [![](https://developer.android.com/static/blog/assets/Daniel_Santiago_Rivera_157422eedb_Z1DQYwY.webp)](https://developer.android.com/blog/authors/daniel-santiago-rivera) [##### Daniel Santiago Rivera](https://developer.android.com/blog/authors/daniel-santiago-rivera)

###### Software Engineer

The first alpha of Room 3.0 has been released! Room 3.0 is a major breaking version of the library that focuses on Kotlin Multiplatform (KMP) and adds support for JavaScript and WebAssembly (WASM) on top of the existing Android, iOS and JVM desktop support.

In this blog we outline the breaking changes, the reasoning behind Room 3.0, and the various things you can do to migrate from Room 2.0.

## Breaking changes

Room 3.0 includes the following breaking API changes:

- **Dropping SupportSQLite APIs:** Room 3.0 is fully backed by the [androidx.sqlite driver APIs](https://developer.android.com/kotlin/multiplatform/sqlite#sqlite-driver). The SQLiteDriver APIs are KMP-compatible and removing Room's dependency on Android's API simplifies the API surface for Android since it avoids having two possible backends.
- **No more Java code generation:** Room 3.0 exclusively generates Kotlin code. This aligns with the evolving Kotlin-first paradigm but also simplifies the codebase and development process, enabling faster iterations.
- **Focus on KSP:** We are also dropping support for Java Annotation Processing (AP) and KAPT. Room 3.0 is solely a KSP (Kotlin Symbol Processing) processor, allowing for better processing of Kotlin codebases without being limited by the Java language.
- **Coroutines first:**Room 3.0 embraces Kotlin coroutines, making its APIs coroutine-first. Coroutines is the KMP-compatible asynchronous framework and making Room be asynchronous by nature is a critical requirement for supporting web platforms.

## A new package

To prevent compatibility issues with existing Room 2.x implementations and for libraries with transitive dependencies to Room (for example, WorkManager), Room 3.0 resides in a new package which means it also has a new maven group and artifact ids. For example, `androidx.room:room-runtime` has become `androidx.room3:room3-runtime` and classes such as `androidx.room.RoomDatabase` will now be located at `androidx.room3.RoomDatabase`.

## Kotlin and Coroutines First

With no more Java code generation, Room 3.0 also requires KSP and the Kotlin compiler even if the codebase interacting with Room is in Java. It is recommended to have a multi-module project where Room usage is concentrated and the Kotlin Gradle Plugin and KSP can be applied without affecting the rest of the codebase.

Room 3.0 also requires Coroutines and more specifically DAO functions have to be suspending unless they are returning a reactive type, such as a Flow. Room 3.0 disallows blocking DAO functions. See the [Coroutines on Android documentation](https://developer.android.com/kotlin/coroutines) on getting started integrating Coroutines into your application.

## Migration to SQLiteDriver APIs

With the shift away from SupportSQLite, apps will need to migrate to the SQLiteDriver APIs. This migration is essential to leveraging the full benefits of Room 3.0, including allowing the use of the bundled SQLite library via the `BundledSQLiteDriver`. You can start migrating to the driver APIs today with Room 2.7.0+. We strongly encourage you to avoid any further usage of SupportSQLite. If you migrate your Room integrations to SQLiteDriver APIs, then the transition to Room 3.0 is easier since the package change mostly involves updating symbol references (imports) and might require minimal changes to call-sites.

For a brief overview of the SQLiteDriver APIs, check out the [SQLiteDriver APIs documentation](https://developer.android.com/kotlin/multiplatform/sqlite#sqlite-driver).

For more details on how to migrate Room to use SQLiteDriver APIs, check out the official [documentation to migrate from SupportSQLite](https://developer.android.com/kotlin/multiplatform/room#migrate-from-support-sqlite).

## Room SupportSQLite wrapper

We understand completely removing SupportSQLite might not be immediately feasible for all projects. To ease this transition, Room 2.8.0, the latest version of the Room 2.0 series, introduced a new artifact called `androidx.room:room-sqlite-wrapper`. This artifact offers a compatibility API that allows you to convert a `RoomDatabase` into a `SupportSQLiteDatabase`, even if the SupportSQLite APIs in the database have been disabled due to a `SQLiteDriver` being installed. This provides a temporary bridge for developers who need more time to fully migrate their codebase. This artifact continues to exist in Room 3.0 as `androidx.room3:room3-sqlite-wrapper` to enable the migration to Room 3.0 while still supporting critical SupportSQLite usage.

For example, invocations of `roomDatabase.openHelper.writableDatabase` can be replaced by `roomDatabase.getSupportWrapper()` and a wrapper would be provided even if `setDriver()` is called on Room's builder.

For more details check out the [room-sqlite-wrapper documentation](https://developer.android.com/kotlin/multiplatform/room#migrate-room-sqlite-wrapper).

## Room and SQLite Web Support

Support for the Kotlin Multiplatform targets JS and WasmJS and brings some of the most significant API changes. Specifically, many APIs in Room 3.0 are suspend functions since proper support for web storage is asynchronous. The SQLiteDriver APIs have also been updated to support the Web and a new web asynchronous driver is available in `androidx.sqlite:sqlite-web`. It is a [Web Worker](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) based driver that enables persisting the database in the Origin private file system (OPFS).

For more details on how to set up Room for the Web check out the [Room 3.0 release notes](https://developer.android.com/jetpack/androidx/releases/room3#3.0.0-alpha01).

## Custom DAO Return Types

Room 3.0 introduces the ability to add custom integrations to Room similar to RxJava and Paging. Through a new annotation API called `@DaoReturnTypeConverter` you can create your own integration such that Room's generated code becomes accessible at runtime, this enables `@Dao` functions having their custom return types without having to wait for the Room team to add the support. Existing integrations are migrated to use this functionality and thus will now require for those who rely on it to add the converters to the `@Database` or `@Dao` definitions.

For example, the Paging converter will be located in the `androidx.room3:room3-paging` artifact and it's called `PagingSourceDaoReturnTypeConverter`. Meanwhile for `LiveData` the converter is in `androidx.room3:room3-livedata` and is called `LiveDataDaoReturnTypeConverter`.

For more details check out the DAO Return Type Converters section in the [Room 3.0 release notes](https://developer.android.com/jetpack/androidx/releases/room3#3.0.0-alpha01).

## Maintenance mode of Room 2.x

Since the development of Room will be focused on Room 3, the current Room 2.x version enters maintenance mode. This means that no major features will be developed but patch releases (2.8.1, 2.8.2, etc.) will still occur with bug fixes and dependency updates. The team is committed to this work until Room 3 becomes stable.

## Final thoughts

We are incredibly excited about the potential of Room 3.0 and the opportunities it unlocks for the Kotlin ecosystem. Stay tuned for more updates as we continue this journey!

###### Written by:

-

  ## [Daniel Santiago Rivera](https://developer.android.com/blog/authors/daniel-santiago-rivera)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/daniel-santiago-rivera) ![](https://developer.android.com/static/blog/assets/Daniel_Santiago_Rivera_157422eedb_Z1DQYwY.webp) ![](https://developer.android.com/static/blog/assets/Daniel_Santiago_Rivera_157422eedb_Z1DQYwY.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)