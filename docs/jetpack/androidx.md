---
title: https://developer.android.com/jetpack/androidx
url: https://developer.android.com/jetpack/androidx
source: md.txt
---

# AndroidX overview

The`androidx`namespace comprises the[Android Jetpack](https://developer.android.com/jetpack)libraries. Like the Support Library, libraries in the`androidx`namespace ship separately from the Android platform and provide backward compatibility across Android releases.

AndroidX is a major improvement to the original Android[Support Library](https://developer.android.com/topic/libraries/support-library), which is no longer maintained.`androidx`packages fully replace the Support Library by providing feature parity and new libraries.

In addition, AndroidX includes the following features:

- All packages in AndroidX live in a consistent namespace starting with the string`androidx`. The Support Library packages have been mapped into corresponding`androidx.*`packages. For a full mapping of all the old classes and build artifacts to the new ones, see the[Package Refactoring](https://developer.android.com/jetpack/androidx/refactor)page.

- Unlike the Support Library,`androidx`packages are separately maintained and updated. The`androidx`packages use strict[Semantic Versioning](https://semver.org/), starting with version 1.0.0. You can update AndroidX libraries in your project independently.

- [Version 28.0.0](https://developer.android.com/topic/libraries/support-library/revisions#28-0-0)is the last release of the Support Library. There will be no more`android.support`library releases. All new feature development will be in the`androidx`namespace.

| **Note:** Jetpack libraries don't send any user data to a backend service of any kind. This means that integrating a Jetpack library into your app has no impact on your app's[Data safety form](https://developer.android.com/guide/topics/data/collect-share)in the Play Console.

## Using`androidx`libraries in your project

See[Migrating to AndroidX](https://developer.android.com/jetpack/androidx/migrate)to learn how to migrate an existing project.

If you want to use`androidx`-namespaced libraries in a new project, you need to set the compile SDK to Android 14.0 (API level 34) or higher and set both of the following Android Gradle plugin flags to`true`in your[`gradle.properties`](https://developer.android.com/studio/build#properties-files)file.

- `android.useAndroidX`: When this flag is set to`true`, the Android plugin uses the appropriate AndroidX library instead of a Support Library. The flag is`false`by default if it is not specified.
- `android.enableJetifier`: When this flag is set to`true`, the Android plugin automatically migrates existing third-party libraries to use AndroidX dependencies by rewriting their binaries. The flag is`false`by default if it is not specified.

| **Note:** Libraries in`androidx`officially support the[Gradle](https://gradle.org/)build tool with[Android Gradle plugin](https://developer.android.com/build/releases/gradle-plugin)and don't test or maintain compatibility with any other build configuration.

## API Reference

All the packages and classes in the`androidx`namespace can be found in the[AndroidX reference section](https://developer.android.com/reference/androidx/packages).

## Additional Resources

Learn more about components on the Jetpack[home page](https://developer.android.com/jetpack). For more information about the package refactoring from the Support Library to`androidx`, see[the blog post](https://android-developers.googleblog.com/2018/05/hello-world-androidx.html)on that topic.