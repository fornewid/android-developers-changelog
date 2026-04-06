---
title: https://developer.android.com/build/dependencies
url: https://developer.android.com/build/dependencies
source: md.txt
---

> [!NOTE]
> **Note:** When adding dependencies, consider enabling [Dependency verification](https://developer.android.com/build/dependency-verification) to help ensure the dependencies you download and include in your project are what you expect.

The Gradle build system in Android Studio lets you include external binaries or
other library modules to your build as dependencies. The dependencies can be
located on your machine or in a remote repository, and any transitive
dependencies they declare are automatically included as well. This page
describes how to use dependencies with your Android project, including details
about behaviors and configurations that are specific to the Android Gradle
plugin (AGP). For a deeper conceptual guide to Gradle dependencies, see the
[Gradle guide for dependency
management](https://docs.gradle.org/current/userguide/getting_started_dep_man.html),
but remember that your Android project must use only the [dependency
configurations](https://developer.android.com/build/dependencies#dependency_configurations) defined on this page.

> [!CAUTION]
> **Caution:** When specifying dependencies, you should not use dynamic version numbers, such as `'com.android.tools.build:gradle:3.+'`. Using this feature can cause unexpected version updates, difficulty resolving version differences, and poor performance.

## Add a library or plugin dependency

The best way to add and manage build dependencies is to use version catalogs,
the method new projects use by default. This section covers the most common
types of configurations used for Android projects; refer to the
[Gradle documentation](https://docs.gradle.org/current/userguide/platforms.html)
for more options. For an example of an app that uses version catalogs, see
[Now in Android](https://github.com/android/nowinandroid/blob/main/gradle/libs.versions.toml).
If you already have build dependencies set up
without version catalogs and have a multi-module project, we recommend
[migrating](https://developer.android.com/build/migrate-to-catalogs).

For guidance on adding and managing native dependencies (not common), see
[Native dependencies](https://developer.android.com/build/native-dependencies).

In the following example, we add a [remote binary
dependency](https://developer.android.com/build/remote-repositories) (the [Jetpack Macrobenchmark
library](https://developer.android.com/jetpack/androidx/releases/benchmark)), [local library module
dependency](https://developer.android.com/studio/projects/android-library) (`myLibrary`), and a plugin
dependency (the Android Gradle plugin) to our project. Here are the general
steps to add these dependencies to your project:

> [!NOTE]
> **Note:** It's possible to [declare version catalogs in the settings
> file](https://docs.gradle.org/current/userguide/platforms.html#sub:version-catalog-declaration), but we recommend using a separate `toml` file to get more support with code suggestions and highlighting from Android Studio.

1. Add an alias for the version of the dependency that you want in the
   `[versions]` section of the version catalog file, called
   `libs.versions.toml` (under the `gradle` directory in
   **Project** view or **Gradle Scripts** in **Android** view):

   ```
   [versions]
   agp = "8.3.0"
   androidx-macro-benchmark = "1.2.2"
   my-library = "1.4"

   [libraries]
   ...

   [plugins]
   ...
   ```

   Aliases can include dashes or underscores. These aliases generate nested values
   you can reference in build scripts. The references start with the name of the
   catalog, the `libs` part of `libs.versions.toml`. When
   using a single version catalog, we recommend keeping the default value of
   "libs."
2. Add an alias for the dependency in the `[libraries]` (for
   remote binaries or local library modules) or `[plugins]` (for
   plugins) sections of the `libs.versions.toml` file.

   ```
   [versions]
   ...

   [libraries]
   androidx-benchmark-macro = { group = "androidx.benchmark", name = "benchmark-macro-junit4", version.ref = "androidx-macro-benchmark" }
   my-library = { group = "com.myapplication", name = "mylibrary", version.ref = "my-library" }

   [plugins]
   androidApplication = { id = "com.android.application", version.ref = "agp" }
   ```

   Some libraries are available in a published Bill of Materials (BOM) that
   groups families of libraries and their versions. You can include a BOM in your
   version catalog and build files, and let it manage those versions for you. See
   [Using the Bill of Materials](https://developer.android.com/jetpack/compose/bom) for details.
3. Add a reference to dependency alias to the build script of the
   module(s) that require the dependency. Convert the alias' underscores and dashes
   to dots when you reference it from a build script. Our module-level build script
   would look like this:

   ### Kotlin

   ```kotlin
   plugins {
     alias(libs.plugins.androidApplication)
   }

   dependencies {
     implementation(libs.androidx.benchmark.macro)
     implementation(libs.my.library)
   }
   ```

   ### Groovy

   ```groovy
   plugins {
     alias 'libs.plugins.androidApplication'
   }

   dependencies {
     implementation libs.androidx.benchmark.macro
     implementation libs.my.library
   }
   ```

   Plugin references include `plugins` after the catalog name, and
   version references include `versions` after the catalog name (version
   references are uncommon; see [Dependencies
   with same version numbers](https://docs.gradle.org/current/userguide/platforms.html#sec:common-version-numbers) for examples of version references.) Library
   references don't include a `libraries` qualifier, so you can't use
   `versions` or `plugins` at the start of a library
   alias.

## Configure dependencies

Inside the `dependencies` block, you can declare a library dependency using one
of several different *dependency configurations* (such as `implementation` shown
earlier). Each dependency configuration provides Gradle with different
instructions about how to use the dependency. The following table describes each
of the configurations you can use for a dependency in your Android project.

| Configuration | Behavior |
|---|---|
| `implementation` | Gradle adds the dependency to the compile classpath and packages the dependency to the build output. When your module configures an `implementation` dependency, it's letting Gradle know that you don't want the module to leak the dependency to other modules at compile time. That is, the dependency isn't made available to other modules that depend on the current module. Using this dependency configuration instead of `api` can result in significant build time improvements because it reduces the number of modules that the build system needs to recompile. For example, if an `implementation` dependency changes its API, Gradle recompiles only that dependency and the modules that directly depend on it. Most app and test modules should use this configuration. |
| `api` | Gradle adds the dependency to the compile classpath and build output. When a module includes an `api` dependency, it's letting Gradle know that the module wants to transitively export that dependency to other modules, so that it's available to them at both runtime and compile time. Use this configuration with caution and only with dependencies that you need to transitively export to other upstream consumers. If an `api` dependency changes its external API, Gradle recompiles all modules that have access to that dependency at compile time. Having a large number of `api` dependencies can significantly increase build time. Unless you want to expose a dependency's API to a separate module, library modules should instead use `implementation` dependencies. |
| `compileOnly` | Gradle adds the dependency to the compile classpath only (that is, it's not added to the build output). This is useful when you're creating an Android module and you need the dependency during compilation, but it's optional to have it present at runtime. For example, if you depend on a library that only includes compile-time annotations---typically used to generate code but often not included in the build output---you could mark that library `compileOnly`. <br /> If you use this configuration, then your library module must include a runtime condition to check whether the dependency is available, and then gracefully change its behavior so it can still function if it's not provided. This helps reduce the size of the final app by not adding transient dependencies that aren't critical. **Note:** You can't use the `compileOnly` configuration with Android Archive (AAR) dependencies. |
| `runtimeOnly` | Gradle adds the dependency to the build output only, for use during runtime. That is, it isn't added to the compile classpath. This is rarely used on Android, but commonly used in server applications to provide logging implementations. For example, a library could use a logging API that doesn't include an implementation. Consumers of that library could add it as an `implementation` dependency and include a `runtimeOnly` dependency for the actual logging implementation to use. |
| `ksp kapt annotationProcessor` | These configurations supply libraries that process annotations and other symbols in your code before it is compiled. They typically validate your code or generate additional code, reducing the code you need to write. To add such a dependency, you must add it to the annotation processor classpath using the `ksp`, `kapt`, or `annotationProcessor` configurations. Using these configurations improves build performance by separating the compile classpath from the annotation processor classpath. If Gradle finds annotation processors on the compile classpath, it deactivates [compile avoidance](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_compile_avoidance), which negatively impacts build time (Gradle 5.0 and higher ignore annotation processors found on the compile classpath). The Android Gradle plugin assumes a dependency is an annotation processor if its JAR file contains the following file: `META-INF/services/javax.annotation.processing.Processor` If the plugin detects an annotation processor that's on the compile classpath, it produces a build error. `ksp` is a Kotlin Symbol Processor, and is run by the Kotlin compiler. `kapt` and `apt` are separate tools that process annotations before Kotlin or Java compilers execute. When deciding which configuration to use, consider the following: - If a processor is available as a Kotlin Symbol Processor, use it as a `ksp` dependency. See [Migrate from kapt to ksp](https://developer.android.com/build/migrate-to-ksp) for details on using Kotlin Symbol Processors. - If the processor isn't available as a Kotlin Symbol Processor: - If your project includes Kotlin source (but can also include Java source), [use `kapt`](https://kotlinlang.org/docs/reference/kapt.html) to include it. - If your project only uses Java source, use `annotationProcessor` to include it. For more information about using annotation processors, see [Add annotation processors](https://developer.android.com/build/annotation-processors). |
| `lintChecks` | Use this configuration to include a library containing lint checks you want Gradle to execute when building your Android app project. Note that AARs that contain a `lint.jar` file will automatically run checks defined in that `lint.jar` file; you don't need to add an explicit `lintChecks` dependency. This lets you define libraries and associated lint checks in a single dependency, ensuring that your checks are run when consumers use your library. |
| `lintPublish` | Use this configuration in Android library projects to include lint checks you want Gradle to compile into a `lint.jar` file and package in your AAR. This causes projects that consume your AAR to also apply those lint checks. If you were previously using the `lintChecks` dependency configuration to include lint checks in the published AAR, you need to migrate those dependencies to instead use the `lintPublish` configuration. ### Kotlin ```kotlin dependencies { // Executes lint checks from the ":checks" project at build time. lintChecks(project(":checks")) // Compiles lint checks from the ":checks-to-publish" into a // lint.jar file and publishes it to your Android library. lintPublish(project(":checks-to-publish")) } ``` ### Groovy ```groovy dependencies { // Executes lint checks from the ':checks' project at build time. lintChecks project(':checks') // Compiles lint checks from the ':checks-to-publish' into a // lint.jar file and publishes it to your Android library. lintPublish project(':checks-to-publish') } ``` |

<br />

### Configure dependencies for a specific build variant

All of the preceding configurations apply dependencies to all build variants. If
you instead want to declare a dependency for only a specific [build
variant](https://developer.android.com/studio/build/build-variants) source set or for a [testing source
set](https://developer.android.com/studio/test#sourcesets), you must capitalize the configuration
name and prefix it with the name of the build variant or testing source set.

For example, to add a remote binary dependency only to your "free" product
flavor using the `implementation` configuration, use this:

### Kotlin

```kotlin
dependencies {
    freeImplementation("com.google.firebase:firebase-ads:21.5.1")
}
```

### Groovy

```groovy
dependencies {
    freeImplementation 'com.google.firebase:firebase-ads:21.5.1'
}
```

However, if you want to add a dependency for a variant that combines a product
flavor and a build type, then you must initialize the configuration name:

### Kotlin

```kotlin
// Initializes a placeholder for the freeDebugImplementation dependency configuration.
val freeDebugImplementation by configurations.creating

dependencies {
    freeDebugImplementation(project(":free-support"))
}
```

### Groovy

```groovy
configurations {
    // Initializes a placeholder for the freeDebugImplementation dependency configuration.
    freeDebugImplementation {}
}

dependencies {
    freeDebugImplementation project(":free-support")
}
```

To add `implementation` dependencies for your local tests and instrumented tests
, it looks like this:

### Kotlin

```kotlin
dependencies {
    // Adds a remote binary dependency only for local tests.
    testImplementation("junit:junit:4.12")

    // Adds a remote binary dependency only for the instrumented test APK.
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}
```

### Groovy

```groovy
dependencies {
    // Adds a remote binary dependency only for local tests.
    testImplementation 'junit:junit:4.12'

    // Adds a remote binary dependency only for the instrumented test APK.
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.6.1'
}
```

However, certain configurations don't make sense in this situation. For example,
because other modules can't depend on `androidTest`, you get the following
warning if you use the `androidTestApi` configuration:

```
WARNING: Configuration 'androidTestApi' is obsolete and has been replaced with
'androidTestImplementation'.
```

## Dependency order

The order in which you list your dependencies indicates the priority for each:
the first library is higher priority than the second, the second is higher
priority than the third, and so on. This order is important in the event that
[resources are merged](https://developer.android.com/studio/write/add-resources#resource_merging) or
[manifest elements are merged](https://developer.android.com/studio/build/manage-manifests#merge-manifests)
into your app from the libraries.

For example, if your project declares the following:

- Dependency on `LIB_A` and `LIB_B` (in that order)
- And `LIB_A` depends on `LIB_C` and `LIB_D` (in that order)
- And `LIB_B` also depends on `LIB_C`

Then, the flat dependency order will be as follows:

1. `LIB_A`
2. `LIB_D`
3. `LIB_B`
4. `LIB_C`

This ensures that both `LIB_A` and `LIB_B` can override
`LIB_C`; and `LIB_D` is still higher priority than
`LIB_B` because `LIB_A` (which depends on it)
has higher priority than `LIB_B`.

For more information about how manifests from different project
sources/dependencies are merged, see
[Merge multiple manifest files](https://developer.android.com/studio/build/manage-manifests#merge-manifests).

## Dependency information for Play Console

When building your app, AGP includes metadata that describes the library
dependencies that are compiled into your app. When uploading your app, the Play
Console inspects this metadata to provide alerts for known issues with SDKs and
dependencies your app uses, and, in some cases, provide actionable feedback to
resolve those issues.

The data is compressed, encrypted by a Google Play signing key, and stored in
the signing block of your release app. We recommend keeping this dependencies
file for a safe and positive user experience. You can opt out by including the
following
[`dependenciesInfo`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/DependenciesInfo)
block in your module's `build.gradle.kts` file.

    android {
        dependenciesInfo {
            // Disables dependency metadata when building APKs.
            includeInApk = false
            // Disables dependency metadata when building Android App Bundles.
            includeInBundle = false
        }
    }

For more information on our policies and potential issues with dependencies, see
our support page on
[using third-party SDKs in your app](https://support.google.com/googleplay/android-developer/answer/10358880).

## SDK insights

Android Studio shows lint warnings in the version catalog file and the **Project
Structure Dialog** for public SDKs in the
[Google Play SDK Index](https://developer.android.com/distribute/sdk-index) when the following issues apply:

- The SDKs are marked as outdated by their authors.
- The SDKs violate Play policies.
- The SDKs have known security vulnerabilities.
- The SDKs have been deprecated by their authors.

The warnings are signals that you should update those dependencies, because
using outdated versions could prevent you from publishing to the Google Play
Console in the future.

## Add build dependencies without version catalogs

We recommend using version catalogs to add and manage dependencies, but simple
projects might not need them. Here's an example of a build file that doesn't use
version catalogs:

### Kotlin

```kotlin
plugins {
    id("com.android.application")
}

android { ... }

dependencies {
    // Dependency on a remote binary
    implementation("com.example.android:app-magic:12.3")
    // Dependency on a local library module
    implementation(project(":mylibrary"))
}
```

### Groovy

```groovy
plugins {
    id 'com.android.application'
}

android { ... }

dependencies {
    // Dependency on a remote binary
    implementation 'com.example.android:app-magic:12.3'
    // Dependency on a local library module
    implementation project(':mylibrary')
}
```

This build file declares a dependency on version 12.3 of the "app-magic"
library, inside the "com.example.android" namespace group. The remote binary
dependency declaration is shorthand for the following:

### Kotlin

```kotlin
implementation(group = "com.example.android", name = "app-magic", version = "12.3")
```

### Groovy

```groovy
implementation group: 'com.example.android', name: 'app-magic', version: '12.3'
```

The build file also declares a dependency on an [Android library module](https://developer.android.com/studio/projects/android-library) named
"mylibrary"; this name must match the library name defined with an `include:` in
your `settings.gradle.kts` file. When you build your app, the build system
compiles the library module and packages the resulting compiled contents in the
app.

The build file also declares a dependency on the Android Gradle plugin
(`com.application.android`). If you have multiple modules that use the same
plugin, you can only have a single version of the plugin on the build classpath
across all modules. Instead of specifying the version in each of the module
build scripts, you should include the plugin dependency in the root build script
with the version, and indicate to not apply it. Adding `apply false` tells
Gradle to note the version of the plugin but not to use it in the root build.
Typically the root build script is empty except for this `plugins` block.

### Kotlin

```kotlin
plugins {
    id("org.jetbrains.kotlin.android") version "1.9.0" apply false
}
```

### Groovy

```groovy
plugins {
    id 'com.android.application' version '8.3.0-rc02' apply false
}
```

If you have a single-module project you can specify the version explicitly in
the module-level build script and leave the project-level build script empty:

### Kotlin

```kotlin
plugins {
    id("com.android.application") version "8.3.0"
}
```

### Groovy

```groovy
plugins {
    id 'com.android.application' version '8.3.0-rc02'
}
```