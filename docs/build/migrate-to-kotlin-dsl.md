---
title: https://developer.android.com/build/migrate-to-kotlin-dsl
url: https://developer.android.com/build/migrate-to-kotlin-dsl
source: md.txt
---

Android Gradle plugin 4.0 added support for using Kotlin in your Gradle build
configuration as a replacement for Groovy, the programming language
traditionally used in Gradle configuration files.

Kotlin is preferred over the Groovy for writing Gradle scripts because Kotlin is
more readable and offers better compile-time checking and IDE support.

Although Kotlin currently offers better integration in Android Studio's code
editor when compared to Groovy, builds using Kotlin tend to be slower than
builds using Groovy, so consider build performance when deciding whether to
migrate.

This page provides basic information about converting your Android app's
Gradle build files from Groovy to Kotlin. For a more comprehensive migration
guide, see Gradle's
[official documentation](https://guides.gradle.org/migrating-build-logic-from-groovy-to-kotlin/).

## Timeline

> [!NOTE]
> **Note:** Kotlin is the default language for build configuration starting with Android Studio Giraffe. If you're using AGP 8.1 and the Kotlin DSL for build configuration, you should use Gradle 8.1 for the best experience.

Starting with Android Studio Giraffe, new projects use the Kotlin DSL
(`build.gradle.kts`) by default for build configuration. This offers a better
editing experience than the Groovy DSL (`build.gradle`) with syntax
highlighting, code completion, and navigation to declarations. To learn more,
see the
[Gradle Kotlin DSL Primer](https://docs.gradle.org/current/userguide/kotlin_dsl.html).

## Common terms

**Kotlin DSL:** Refers primarily to the [Android Gradle plugin Kotlin DSL](https://developer.android.com/reference/tools/gradle-api)
or, occasionally, to the
[underlying Gradle Kotlin DSL](https://docs.gradle.org/current/userguide/kotlin_dsl.html#kotlin_dsl).

In this migration guide, "Kotlin" and "Kotlin DSL" are used interchangeably.
Likewise, "Groovy" and "Groovy DSL" are used interchangeably.

### Script file naming

Script file extension names are based on the language the build file is written
in:

- Gradle build files written in Groovy use the `.gradle` file name extension.
- Gradle build files written in Kotlin use the `.gradle.kts` file name extension.

## Convert the syntax

There are some general differences in syntax between Groovy and Kotlin,
so you need to apply these changes throughout your build scripts.

### Add parentheses to method calls

> [!TIP]
> **Tip:** As a first step, even before changing the file extensions, add parentheses to your Groovy code. This makes the conversion to Kotlin easier.

Groovy lets you to omit parentheses in method calls, while Kotlin requires
them. To migrate your configuration, add parentheses to these sorts of
method calls. This code shows how to configure a setting in Groovy:

    compileSdkVersion 30

This is the same code written in Kotlin:

    compileSdkVersion(30)

### Add `=` to assignment calls

> [!TIP]
> **Tip:** Before changing file extensions, add `=` to your Groovy code. This makes the conversion to Kotlin easier.

The Groovy DSL lets you to omit the assignment operator `=` when
assigning properties, whereas Kotlin requires it. This code shows how to
assign properties in Groovy:

    java {
        sourceCompatibility JavaVersion.VERSION_17
        targetCompatibility JavaVersion.VERSION_17
    }

This code shows how to assign properties in Kotlin:

    java {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

### Convert strings

Here are the string differences between Groovy and Kotlin:

- **Double quotes for strings:** While Groovy allows strings to be defined using single quotes, Kotlin requires double quotes.
- **String interpolation on dotted expressions:** In Groovy, you can use
  just the `$` prefix for
  [string interpolations](https://groovy-lang.org/syntax.html#_string_interpolation)
  on dotted expressions, but Kotlin requires that you wrap the dotted expressions with curly braces. For example, in Groovy you can use
  `$project.rootDir` as shown in the following snippet:

  ```groovy
      myRootDirectory = "$project.rootDir/tools/proguard-rules-debug.pro"
      
  ```

  In Kotlin, however, the preceding code calls `toString()` on
  `project`, not on `project.rootDir`. To get the value
  of the root directory, wrap the `${project.rootDir}` expression
  with curly braces:

  ```kotlin
      myRootDirectory = "${project.rootDir}/tools/proguard-rules-debug.pro"
      
  ```

  To learn more, see
  [String templates](https://kotlinlang.org/docs/strings.html#string-templates)
  in the Kotlin documentation.

### Rename file extensions

Append `.kts` to each build file as you migrate its contents. For example,
select a build file, like the `settings.gradle` file. Rename the file to
`settings.gradle.kts` and convert the file's contents to Kotlin. Make sure your
project still compiles after the migration of each build file.

Migrate your smallest files first, gain experience, and then move on. You can
have a mix of Kotlin and Groovy build files in a project, so take your time to
carefully make the move.

### Replace `def` with `val` or `var`

Replace `def` with `val` or `var`, which is
[how you define variables in Kotlin](https://kotlinlang.org/docs/basic-syntax.html#variables).
This is a variable declaration in Groovy:

    def building64Bit = false

This is the same code written in Kotlin:

    val building64Bit = false

### Prefix boolean properties with `is`

Groovy uses [property deduction logic](https://groovy-lang.org/objectorientation.html#_property_naming_conventions)
based on the property names. For a boolean property `foo`, its *deduced methods*
can be `getFoo`, `setFoo`, or `isFoo`. Thus once converted to Kotlin,
you need to change the property names to the deduced methods
that are not supported by Kotlin. For example, for
`buildTypes` DSL boolean elements, you need to prefix them with `is`. This code
shows how to set boolean properties in Groovy:

    android {
        buildTypes {
            release {
                minifyEnabled true
                shrinkResources true
                ...
            }
            debug {
                debuggable true
                ...
            }
        ...

The following is the same code in Kotlin. Note that the properties are prefixed
by `is`.

    android {
        buildTypes {
            getByName("release") {
                isMinifyEnabled = true
                isShrinkResources = true
                ...
            }
            getByName("debug") {
                isDebuggable = true
                ...
            }
        ...

### Convert lists and maps

Lists and maps in Groovy and Kotlin are defined using different syntax. Groovy
uses `[]`, while Kotlin calls collection creation methods explicitly using
`listOf` or `mapOf`. Make sure to replace `[]` with `listOf` or `mapOf` when
migrating.

Here's how to define a list in Groovy versus Kotlin:

    jvmOptions += ["-Xms4000m", "-Xmx4000m", "-XX:+HeapDumpOnOutOfMemoryError</code>"]

This is the same code written in Kotlin:

    jvmOptions += listOf("-Xms4000m", "-Xmx4000m", "-XX:+HeapDumpOnOutOfMemoryError")

Here's how to define a map in Groovy versus Kotlin:

    def myMap = [key1: 'value1', key2: 'value2']

This is the same code written in Kotlin:

    val myMap = mapOf("key1" to "value1", "key2" to "value2")

### Configure build types

In the Kotlin DSL only the debug and release build types are available
implicitly. All other custom build types must be created manually.

In Groovy you can use the debug, release, and certain other build types without
creating them first. The following code snippet shows a configuration with the
`debug`, `release`, and
[`benchmark`](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview) build
types in Groovy.

    buildTypes {
     debug {
       ...
     }
     release {
       ...
     }
     benchmark {
       ...
     }
    }

To create the equivalent configuration in Kotlin, you must explicitly create the
`benchmark` build type.

    buildTypes {
     debug {
       ...
     }

     release {
       ...
     }
     register("benchmark") {
        ...
     }
    }

## Migrate from buildscript to plugins block

If your build uses the
[`buildscript {}`](https://docs.gradle.org/current/userguide/plugins.html#sec:old_plugin_application)
block to add plugins to the project, you should refactor to use the
[`plugins {}`](https://docs.gradle.org/current/userguide/plugins.html#sec:plugins_block)
block instead. The `plugins {}` block makes it easier to apply plugins, and it
works well with
[version catalogs](https://developer.android.com/studio/build/migrate-to-catalogs).

In addition, when you use the `plugins {}` block in your build files,
Android Studio is aware of the context even when the build fails. This context
helps make fixes to your Kotlin DSL files because it allows the Studio IDE to
perform code completion and provide other helpful suggestions.

### Find the plugin IDs

While the `buildscript {}` block adds the plugins to the build classpath using
the
[Maven coordinates](https://maven.apache.org/pom.html)
of the plugin, for example `com.android.tools.build:gradle:7.4.0`,
the `plugins {}` block uses the plugin IDs instead.

For most plugins, the plugin ID is the string used when you apply them using
`apply plugin`. For example, the following plugin IDs are part of
[Android Gradle Plugin](https://developer.android.com/studio/releases/gradle-plugin):

- `com.android.application`
- `com.android.library`
- `com.android.lint`
- `com.android.test`

You can find the full plugin list in the
[Google Maven repository](https://maven.google.com/web/index.html).

Kotlin plugins can be referenced by multiple plugin IDs. We recommend using the
namespaced plugin ID, and refactor from shorthand to namespaced plugin ID by the
following table:

| Shorthand plugin IDs | Namespaced plugin IDs |
|---|---|
| `kotlin` | `org.jetbrains.kotlin.jvm` |
| `kotlin-android` | `org.jetbrains.kotlin.android` |
| `kotlin-kapt` | `org.jetbrains.kotlin.kapt` |
| `kotlin-parcelize` | `org.jetbrains.kotlin.plugin.parcelize` |

You can also search for plugins on the
[Gradle Plugin Portal](https://plugins.gradle.org/),
the [Maven Central Repository](https://central.sonatype.com/)
and the
[Google Maven repository](https://maven.google.com/web/index.html).
Read
[Developing Custom Gradle Plugins](https://docs.gradle.org/current/userguide/custom_plugins.html#behind_the_scenes)
to learn more about how plugin IDs work.

### Perform the refactoring

Once you know the IDs of the plugins you use, perform the following steps:

1. If you still have repositories for plugins declared in the `buildscript {}`
   block, move them to the [`settings.gradle`](https://developer.android.com/studio/build#settings-file)
   file instead.

2. Add the plugins to the `plugins {}` block in the top-level
   `build.gradle` file. You need to specify the ID and the
   version of the plugin here. If the plugin doesn't need to
   be applied to the root project, use `apply false`.

3. Remove the `classpath` entries from the top-level `build.gradle.kts` file.

4. Apply the plugins by adding them to the `plugins {}` block in the
   module-level `build.gradle` file. You only need to specify the plugin's
   ID here because the version is inherited from the root project.

5. Remove the `apply plugin` call for the plugin from the module-level
   `build.gradle` file.

For example, this setup uses the `buildscript {}` block:

    // Top-level build.gradle file
    buildscript {
        repositories {
            google()
            mavenCentral()
            gradlePluginPortal()
        }
        dependencies {
            classpath("com.android.tools.build:gradle:7.4.0")
            classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.0")
            ...
        }
    }

    // Module-level build.gradle file
    apply(plugin: "com.android.application")
    apply(plugin: "kotlin-android")

This is an equivalent setup using the `plugins {}` block:

    // Top-level build.gradle file
    plugins {
       id 'com.android.application' version '7.4.0' apply false
       id 'org.jetbrains.kotlin.android' version '1.8.0' apply false
       ...
    }

    // Module-level build.gradle file
    plugins {
       id 'com.android.application'
       id 'org.jetbrains.kotlin.android'
       ...
    }

    // settings.gradle
    pluginManagement {
        repositories {
            google()
            mavenCentral()
            gradlePluginPortal()
        }
    }

## Convert the plugins block

Applying plugins from the `plugins {}` block is similar in Groovy and Kotlin.
The following code shows how to apply plugins in Groovy when you're using
[version catalogs](https://developer.android.com/studio/build/migrate-to-catalogs):

    // Top-level build.gradle file
    plugins {
       alias libs.plugins.android.application apply false
       ...
    }

    // Module-level build.gradle file
    plugins {
       alias libs.plugins.android.application
       ...
    }

The following code shows how to do the same in Kotlin:

    // Top-level build.gradle.kts file
    plugins {
       alias(libs.plugins.android.application) apply false
       ...
    }

    // Module-level build.gradle.kts file
    plugins {
       alias(libs.plugins.android.application)
       ...
    }

The following code shows how to apply plugins in Groovy when you're *not*
using version catalogs:

    // Top-level build.gradle file
    plugins {
       id 'com.android.application' version '7.3.0' apply false
       ...
    }

    // Module-level build.gradle file
    plugins {
       id 'com.android.application'
       ...
    }

The following code shows how to do the same in Kotlin:

    // Top-level build.gradle.kts file
    plugins {
       id("com.android.application") version "7.3.0" apply false
       ...
    }

    // Module-level build.gradle.kts file
    plugins {
       id("com.android.application")
       ...
    }

For more details about the `plugins {}` block, see [Applying
plugins](https://docs.gradle.org/nightly/userguide/migrating_from_groovy_to_kotlin_dsl.html#applying_plugins)
in the Gradle documentation.

## Miscellaneous

For Kotlin code samples for other functionalities, see the following
documentation pages:

- If you have a ProGuard configuration, refer to [Enable shrinking, obfuscation, and optimization](https://developer.android.com/studio/build/shrink-code#enable).
- If you have a `signingConfig {}` block, refer to [Remove signing information from
  your build files](https://developer.android.com/studio/publish/app-signing#secure-shared-keystore).
- If you use project-wide properties, refer to [Configure project-wide
  properties](https://developer.android.com/studio/build#project_wide_properties).

> [!CAUTION]
> **Caution:** Although Gradle lets you define project-wide properties at the module level, avoid doing so, because it causes the modules that share those properties to be coupled. Module coupling makes it more difficult to later export a module as a standalone project and prevents Gradle from using parallel project execution to speed up multi-module builds.

## Known issues

At present, a [known issue](https://github.com/gradle/gradle/issues/15886#issuecomment-1432923669)
is that build speed might be slower with Kotlin than with Groovy.

## How to report issues

For instructions on how to provide the info we need to triage your issue, see
[Details for build tools and Gradle bugs](https://developer.android.com/studio/report-bugs#build-bugs). Then,
file a bug using the Google
[public issue tracker](https://issuetracker.google.com/issues/new?component=192708&template=840533).

## More resources

For a working example of Gradle build files written with Kotlin, see the
[Now In Android sample app](https://github.com/android/nowinandroid)
on GitHub.