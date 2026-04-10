---
title: https://developer.android.com/build/tool-and-library-dependencies
url: https://developer.android.com/build/tool-and-library-dependencies
source: md.txt
---

Build dependencies are external components required to successfully build your
project. A build can depend on [libraries, plugins, subprojects](https://developer.android.com/build/gradle-build-overview#external-dependencies), the Android
SDK, tooling such as [Kotlin](http://kotlinlang.org) and [Java](https://www.java.com/)
compilers, development environments like [Android Studio](https://developer.android.com/studio), and
[Gradle](https://gradle.org/) itself.

Each dependency can itself require other dependencies. We call these *transitive
dependencies*, and can rapidly increase the overall dependencies used by your
application. When you want to upgrade a dependency, whether it's a library,
tool, or the Android SDK, that upgrade can cascade, upgrading many other
dependencies.

Often, this will cause no pain, as many libraries follow a scheme known as
[Semantic Versioning](https://semver.org/). These libraries restrict the types of
changes they make to provide compatibility with their lower versions.

Semantic versioning follows a `major.minor.patch` format. For example, in the
version number 4.8.3, 4 is the `major` version, 8 is the `minor` version and 3
is the `patch` number. When the `major` part changes, the library might have
breaking changes in API or behavior. This can impact your build or application
behavior.

When the `minor` (new features) or `patch` (bug fixes) parts change, the library
developers are telling you that the library is still compatible and shouldn't
impact your application.

> [!NOTE]
> **Note:** Some libraries may expose *experimental* or *opt-in* APIs. These APIs may change, even in *minor* or *patch* releases. These APIs exist to allow developers to try new features or API changes and submit feedback while they are being stabilized. Use these APIs with caution, as they can change and force you to change your code between `minor` and `patch` upgrades.

## Relationships in your build

Android builds contain relationships between:

- Source code - the code and resources that you have control over
- Library dependencies - external libraries or modules that your project and subprojects include when building
- Tools - compilers, plugins, and SDKs that translate your source into an application or library

![Build dependencies and their relationships](https://developer.android.com/static/images/build/build-dependencies.svg) **Figure 1.** Build relationships

### Source code

Your source code is Kotlin or Java code that you write in your application or
library. (For details on using C++, see [Android NDK](https://developer.android.com/ndk).)

Source code depends on libraries (including Kotlin and Java runtime libraries)
and the Android SDK, and requires its corresponding Kotlin or Java compiler.

Some source code includes annotations that require additional processing. For
example, if you're writing [Jetpack Compose](https://developer.android.com/compose) code, you add annotations such
as [`@Composable`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/Composable) that need to be processed by the [Compose Kotlin compiler
plugin](https://developer.android.com/jetpack/androidx/releases/compose-compiler). Other annotations may be processed by a [Kotlin Symbol
Processor](https://developer.android.com/build/migrate-to-ksp) (KSP) or separate [annotation-processing tools](https://developer.android.com/build/annotation-processors).

### Library dependencies

Libraries contain bytecode pulled in as part of your application. This could be
a Java JAR, [Android library](https://developer.android.com/studio/projects/android-library) (AAR), or a subproject in your build. Many
libraries follow [Semantic Versioning](https://semver.org/), which can help you
understand when they remain compatible (or not) when upgraded.

Libraries may depend on other libraries for reuse, called a [transitive
dependency](https://docs.gradle.org/current/userguide/dependency_constraints.html). This reduces the dependencies that you must
explicitly manage; you specify the dependencies that you directly use, and
Gradle pulls them in along with those transitive dependencies. Be aware that as
you upgrade your direct dependencies, they may upgrade those transitive
dependencies.

Sometimes a library may require minimum versions of the Android SDK at runtime
([`minSdk`](https://developer.android.com/build#android_sdk_settings)) or compile time ([`compileSdk`](https://developer.android.com/build#android_sdk_settings)). This is necessary when a
library uses functions included in the Android SDK or its provided JDK APIs. The
effective `minSdk` of your application is the highest `minSdk` requested by your
application and all of its direct and transitive library dependencies.

Using some libraries may require use of a specific Gradle plugin. These helper
plugins often install Kotlin Symbol Processors or other annotation processors
that generate code or modify compilation of your source to support your use of
library features. For example, [Jetpack Room](https://developer.android.com/jetpack/androidx/releases/room) includes annotations and a KSP
that transforms them into generated code to retrieve and modify data in a
database. Jetpack Compose requires the Compose compiler plugin to modify
annotated functions to manage how and when that function is re-run.

### Tools

|---|---|
| Gradle | Gradle is the build tool that reads your build files and generates your application or library, and also exposes an API for plugins to extend its capabilities. Gradle runs multiple processes on one or more Java virtual machines, and its Java plugins call the Java tooling inside the JDK. |
| Gradle plugins | Gradle plugins extend Gradle by defining new tasks and configuration. Applying a plugin to your build enables specific build capabilities, configured as data in your build scripts. For Android builds, the most important Gradle plugin is the [Android Gradle Plugin](https://developer.android.com/build/releases/gradle-plugin) (AGP). |
| Compilers | The Kotlin or Java compiler transforms your source code into executable bytecode. The Kotlin compiler exposes a plugin API that enables external analysis and code generation to be run directly inside the compiler, accessing parsed code structure. |
| Compiler plugins | Compiler plugins perform analysis and code generation *inside* the Kotlin compiler while the Kotlin compiler is analyzing your code, and are installed when you apply their Gradle plugins to the build. |
| Android SDK | The Android SDK contains the Android Platform and Java APIs for a specific version of Android, and its corresponding tools. These tools help you manage the SDK, build your applications, and communicate with and emulate Android devices. Each version of the Android SDK provides specific Java APIs that your source code can access, and [desugaring](https://developer.android.com/studio/write/java8-support) support to use those APIs on earlier versions of Android. |
| JDK | The Java Development Kit, containing Java libraries and executables to compile Java source and run Java applications. There are several JDKs at play in an Android build. See [Java versions in Android builds](https://developer.android.com/build/jdks) for more details. |

## Gradle scopes

Gradle groups library dependencies into different scopes (called
[configurations](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) in the Gradle API), allowing you to specify
different sets of library dependencies to be used in different parts of your
build. For example, you probably don't want to include test libraries such as
JUnit in your published application or library, but you do want them when
building and executing your unit tests. You also use scopes to add symbol or
annotation processors to analyze your code.

For example, AGP defines `implementation` and `api` scopes, your way of
specifying whether a dependency should be exposed to users of your subproject.
See [Configure dependencies](https://developer.android.com/build/dependencies#dependency_configurations) for descriptions of these and other scopes used
in an Android build.

Add library dependencies in your build files' `dependencies` block, either as
`group:artifact:version` strings:

### Kotlin

```kotlin
// In a module-level build script
// explicit dependency strings ("group:artifact:version")
dependencies {
    implementation("com.example:library1:1.2.3")
    api("com.example:library2:1.1.1")
}
```

### Groovy

```groovy
// In a module-level build script
// explicit dependency strings ("group:artifact:version")
dependencies {
    implementation 'com.example:library1:1.2.3'
    api 'com.example:library2:1.1.1'
}
```

or in a [Version Catalog](https://developer.android.com/build/migrate-to-catalogs):

    # Version catalog - gradle/libs.versions.toml
    [versions]
    exampleLib = "1.2.3"
    examplePlugin = "2.3.4"

    [libraries]
    example-library = { group = "com.example", name = "library", version.ref = "exampleLib" }

    [plugins]
    example-plugin = { id = "com.example.plugin", version.ref = "examplePlugin" }

and specify the generated variables in your build files:

### Kotlin

```kotlin
// In a module-level build script
// Using a version catalog
plugins {
    alias(libs.plugins.example.plugin)
}

dependencies {
    implementation(libs.example.library)
}
```

### Groovy

```groovy
// In a module-level build script
// Using a version catalog
plugins {
    alias(libs.plugins.example.plugin)
}

dependencies {
    implementation libs.example.library
}
```