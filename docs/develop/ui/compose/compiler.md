---
title: https://developer.android.com/develop/ui/compose/compiler
url: https://developer.android.com/develop/ui/compose/compiler
source: md.txt
---

For Gradle users, you can use the Compose Compiler Gradle plugin to make setting
up and configuring Compose easier.
| **Note:** The Compose Compiler Gradle Plugin is only available from Kotlin 2.0+. For migration instructions, see ["Jetpack Compose compiler moving to the Kotlin
| repository"](https://android-developers.googleblog.com/2024/04/jetpack-compose-compiler-moving-to-kotlin-repository.html). For an example migration, see the [Compose Samples
| PR](https://github.com/android/compose-samples/pull/1354) in the Compose samples.

## Set up with Gradle version catalogs

The following instructions outline how you can set up the Compose Compiler
Gradle plugin:

1. In your `libs.versions.toml` file, remove any reference to the Compose compiler
2. In the plugins section, add the following new dependency

    [versions]
    kotlin = "2.0.0"

    [plugins]
    org-jetbrains-kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }

    // Add this line
    compose-compiler = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }

1. In your projects root `build.gradle.kts` file, add the following to the plugins section:

    plugins {
       // Existing plugins
       alias(libs.plugins.compose.compiler) apply false
    }

1. In each module that uses Compose, apply the plugin:

    plugins {
       // Existing plugins
       alias(libs.plugins.compose.compiler)
    }

Your app should now build and compile if you are using the default set up. If
you had configured custom options on the Compose compiler, see the following
section.

## Set up without Gradle version catalogs

To set up the Compose Compiler Gradle plugin without version catalogs, add the
following plugin to `build.gradle.kts` files associated with modules you use
Compose:  

    plugins {
        id("org.jetbrains.kotlin.plugin.compose") version "2.0.0" // this version matches your Kotlin version
    }

You might also need to add this classpath to your top-level project
`build.gradle.kts` file:  

    buildscript {
        dependencies {
            classpath("org.jetbrains.kotlin.plugin.compose:org.jetbrains.kotlin.plugin.compose.gradle.plugin:2.0.0")
        }
    }

## Configuration options with the Compose Compiler Gradle Plugin

To configure the Compose compiler using the Gradle plugin, add the
`composeCompiler` block to the module's `build.gradle.kts` file at the top
level.  

    android { ... }

    composeCompiler {
        reportsDestination = layout.buildDirectory.dir("compose_compiler")
        stabilityConfigurationFile = rootProject.layout.projectDirectory.file("stability_config.conf")
    }

For the full list of available options, see the [documentation](https://www.jetbrains.com/help/kotlin-multiplatform-dev/compose-compiler.html#compose-compiler-options-dsl).