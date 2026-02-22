---
title: https://developer.android.com/build/migrate-to-catalogs
url: https://developer.android.com/build/migrate-to-catalogs
source: md.txt
---

# Migrate your build to version catalogs

[Gradle version catalogs](https://docs.gradle.org/current/userguide/platforms.html)
enable you to add and maintain dependencies and plugins in a scalable way.
Using Gradle version catalogs makes managing dependencies and plugins easier
when you have [multiple modules](https://developer.android.com/topic/modularization). Instead of hardcoding
dependency names and versions in individual build files and updating each
entry whenever you need to upgrade a dependency, you can create a central
*version catalog* of dependencies that various modules can reference in
a type-safe way with Android Studio assistance.

This page provides basic information about migrating your Android app to
version catalogs. To learn more, see
[Add build dependencies](https://developer.android.com/build/dependencies) and the Gradle documentation.

## Create a version catalog file

Start by creating a version catalog file. In your root project's `gradle`
folder, create a file called `libs.versions.toml`. Gradle looks for the catalog
in the `libs.versions.toml` file by [default](https://docs.gradle.org/current/userguide/platforms.html#sub:conventional-dependencies-toml),
so we recommend using this default name.
| **Note:** It's possible to change the catalog file name; however, this requires changing your build files, so we don't recommend doing it.

In your `libs.versions.toml` file, add these sections:  

    [versions]

    [libraries]

    [plugins]

The sections are used as follows:

- In the `versions` block, define variables that hold the versions of your dependencies and plugins. You use these variables in the subsequent blocks (the `libraries` and `plugins` blocks).
- In the `libraries` block, define your dependencies.
- In the `plugins` block, define your plugins.

## Migration steps

We recommend you do the steps in the order listed. A build can consume
dependencies and plugins from build scripts and catalogs simultaneously, so
take your time to migrate your dependencies and plugins individually.

The migration process is:

1. Add the new entry to the catalog.
2. Sync your Android project.
3. Replace the previous string declaration with the catalog type-safe accessor.

### Migrate dependencies

Add an entry for each dependency in both the `versions` and `libraries` sections
of the `libs.versions.toml` file. Sync your project, and then replace their
declarations in the build files with their catalog names.

This code snippet shows the `build.gradle.kts` file before removing the
dependency:  

### Kotlin

```kotlin
dependencies {
    implementation("androidx.core:core-ktx:1.9.0")

}
```

### Groovy

```groovy
dependencies {
    implementation 'androidx.core:core-ktx:1.9.0'

}
```

This code snippet shows how to define the dependency in the version
catalog file:  

    [versions]
    ktx = "1.9.0"

    [libraries]
    androidx-ktx = { group = "androidx.core", name = "core-ktx", version.ref = "ktx" }

The recommended naming for dependencies block in catalogs is kebab case (such as
`androidx-ktx`) for better
[code completion assistance](https://www.jetbrains.com/help/idea/auto-completing-code.html)
in your build files.

In the `build.gradle.kts` file of each module that requires the dependency,
define the dependencies by the names you defined in the TOML file.  

### Kotlin

```kotlin
dependencies {
   implementation(libs.androidx.ktx)

}
```

### Groovy

```groovy
dependencies {
   implementation libs.androidx.ktx

}
```

### Migrate plugins

Add an entry for each plugin in both the versions and the plugins sections of
the `libs.versions.toml` file. Sync your project, and then replace their
declarations in the `plugins{}` block in the build files with their catalog
names.

This code snippet shows the `build.gradle.kts` file before removing the
plugin:  

### Kotlin

```kotlin
// Top-level `build.gradle.kts` file
plugins {
   id("com.android.application") version "7.4.1" apply false

}

// Module-level `build.gradle.kts` file
plugins {
   id("com.android.application")

}
```

### Groovy

```groovy
// Top-level `build.gradle` file
plugins {
   id 'com.android.application' version '7.4.1' apply false

}

// Module-level `build.gradle` file
plugins {
   id 'com.android.application'

}
```

This code snippet shows how to define the plugin in the version catalog file:  

    [versions]
    androidGradlePlugin = "7.4.1"

    [plugins]
    android-application = { id = "com.android.application", version.ref = "androidGradlePlugin" }

As with dependencies, the recommended formatting for `plugins` block catalog
entries is kebab case (such as `android-application`) for better
[code completion assistance](https://www.jetbrains.com/help/idea/auto-completing-code.html)
in your build files.

The following code shows how to define the `com.android.application` plugin in
the top and module level `build.gradle.kts` files. Use `alias` for plugins
that come from the version catalog file and `id` for plugins that don't come
from the version catalog file, such as
[convention plugins](https://docs.gradle.org/current/samples/sample_convention_plugins.html#organizing_build_logic).  

### Kotlin

```kotlin
// Top-level build.gradle.kts
plugins {
   alias(libs.plugins.android.application) apply false

}

// module build.gradle.kts
plugins {
   alias(libs.plugins.android.application)

}
```

### Groovy

```groovy
// Top-level build.gradle
plugins {
   alias libs.plugins.android.application apply false

}

// module build.gradle
plugins {
   alias libs.plugins.android.application

}
```
| **Note:** If you are using a version of Gradle below 8.1, you need to annotate the `plugins{}` block with `@Suppress("DSL_SCOPE_VIOLATION")` when using version catalogs. Refer to [issue #22797](https://github.com/gradle/gradle/issues/22797) for more info.

## Learn more

To learn about additional options for configuring your version catalog, see
these resources:

- [The version catalog TOML file format](https://docs.gradle.org/current/userguide/platforms.html#sub::toml-dependencies-format) documents additional options for configuring your catalog file.
- [Now in Android](https://github.com/android/nowinandroid) is our sample app that uses version catalogs.