---
title: https://developer.android.com/build/gradle-build-overview
url: https://developer.android.com/build/gradle-build-overview
source: md.txt
---

Android applications are typically built using the [Gradle](https://gradle.org/) build
system. Before we dive into the details of how to configure your build, we'll
explore the concepts behind the build so you can see the system as a whole.

## What is a build?

A build system transforms your source code into an executable application.
Builds often involve multiple tools, to analyze, compile, link, and package your
application or library. Gradle uses a task-based approach to organize and run
these commands.

[Tasks](https://docs.gradle.org/current/userguide/more_about_tasks.html) encapsulate commands that translate their inputs into
outputs. [Plugins](https://docs.gradle.org/current/userguide/custom_plugins.html) define tasks and their configuration. Applying
a plugin to your build registers its tasks, and wires them together using their
inputs and outputs. For example, applying the [Android Gradle Plugin](https://developer.android.com/build/releases/gradle-plugin) (AGP)
to your build file will register all the tasks necessary to build an APK, or an
Android Library. The `java-library` plugin lets you build a jar from Java source
code. Similar plugins exist for Kotlin, and other languages, but other plugins
are meant to extend plugins. For example, the `protobuf` plugin is meant to add
protobuf support to existing plugins like AGP or `java-library`.

Gradle prefers convention over configuration so plugins will come with good
default values out of the box, but you can further configure the build through a
declarative [Domain-Specific Language](https://docs.gradle.org/current/dsl) (DSL). The DSL is designed
so you can specify *what* to build, rather than *how* to build it. The logic in
the plugins manages the "how". That configuration is specified across several
[build files](https://developer.android.com/build/android-build-structure) in your [project](https://docs.gradle.org/current/userguide/multi_project_builds.html) (and subprojects).

Task inputs can be files and directories as well as other information encoded as
Java types (integer, strings, or custom classes). Outputs can only be directory
or files as they have to be written on disk. Wiring a task output into another
task input, links the tasks together so that one has to run before the other.

While Gradle supports writing arbitrary code and task declarations in your build
files, this can make it more difficult for tooling to understand your build and
for you to maintain. For example, you can write tests for code inside plugins
but not in build files. Instead, you should restrict build logic and task
declarations to plugins (that you or someone else define) and declare how you
want to use that logic in your build files.

## What happens when a Gradle build runs?

Gradle builds run in three phases. Each of these phases executes different parts
of code that you define in your build files.

- **Initialization** determines which projects and subprojects are included in the build, and sets up classpaths containing your build files and applied plugins. This phase focuses on a settings file where you declare projects to build and the locations from which to fetch plugins and libraries.
- **Configuration** registers tasks for each project, and executes the build file to apply the user's build specification. It's important to understand that your configuration code won't have access to data or files produced during execution.
- **Execution** performs the actual "building" of your application. The output of configuration is a [Directed Acyclic Graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) (DAG) of tasks, representing all required build steps that were requested by the user (the tasks provided on the command line or as defaults in the build files). This graph represents the relationship between tasks, either explicit in a task's declaration, or based on its inputs and outputs. If a task has an input that is the output of another task, then it must run after the other task. This phase runs out-of-date tasks in the order defined in the graph; if a task's inputs haven't changed since its last execution, Gradle will skip it.

For more information see the Gradle [Build lifecycle](https://docs.gradle.org/current/userguide/build_lifecycle.html).

## Configuration DSLs

Gradle uses a [Domain-Specific Language](https://docs.gradle.org/current/dsl) (DSL) to configure
builds. This declarative approach focuses on specifying your data rather than
writing step-by-step (imperative) instructions. You can write your build files
using Kotlin or Groovy, but we strongly recommend using Kotlin.

DSLs attempt to make it easier for everyone, domain experts and programmers, to
contribute to a project, defining a small language that represents data in a
more natural way. Gradle plugins can extend the DSL to configure the data they
need for their tasks.

For example, configuring the Android part of your build might look like:  

### Kotlin

```kotlin
android {
    namespace = "com.example.app"
    compileSdk {
        version = release(36) {
            minorApiLevel = 1
        }
    }
    // ...

    defaultConfig {
        applicationId = "com.example.app"
        minSdk {
            version = release(23)
        }
        targetSdk {
            version = release(36)
        }
        // ...
    }
}
```

### Groovy

```groovy
android {
    namespace = 'com.example.app'
    compileSdk {
        version = release(36) {
            minorApiLevel = 1
        }
    }
    // ...

    defaultConfig {
        applicationId = 'com.example.app'
        minSdk {
            version = release(23)
        }
        targetSdk {
            version = release(36)
        }
        // ...
    }
}
```

Behind the scenes, the DSL code is similar to:  

    fun Project.android(configure: ApplicationExtension.() -> Unit) {
        ...
    }

    interface ApplicationExtension {
        var namespace: String?

        fun compileSdk(configure: CompileSdkSpec.() -> Unit) {
            ...
        }

        val defaultConfig: DefaultConfig

        fun defaultConfig(configure: DefaultConfig.() -> Unit) {
            ...
        }
    }

Each block in the DSL is represented by a function that takes a lambda to
configure it, and a property with the same name to access it. This makes the
code in your build files feel more like a data specification.
| **Note:** If you're interested in the details that make this work in Kotlin, see [Type-safe builders](https://kotlinlang.org/docs/type-safe-builders.html). For more details on DSLs in general, see the book [Domain Specific Languages](https://martinfowler.com/books/dsl.html), by Martin Fowler and Rebecca Parsons.

## External dependencies

The Maven build system introduced a [dependency](https://docs.gradle.org/current/userguide/declaring_dependencies.html) specification,
storage and management system. Libraries are stored in
[repositories](https://docs.gradle.org/current/userguide/declaring_repositories.html) (servers or directories), with metadata including
their version and dependencies on other libraries. You specify which
repositories to search, versions of the dependencies you want to use, and the
build system downloads them during the build.

Maven Artifacts are identified by group name (company, developer, etc), artifact
name (the name of the library) and version of that artifact. This is typically
represented as `group:artifact:version`.

This approach significantly improves build management. You'll often hear such
repositories called "Maven repositories", but it's all about the way the
artifacts are packaged and published. These repositories and metadata have been
reused in several build systems, including Gradle (and Gradle can publish to
these repositories). Public repositories allow sharing for all to use, and
company repositories keep internal dependencies in-house.

You can also [modularize](https://developer.android.com/topic/modularization) your project into [subprojects](https://docs.gradle.org/current/userguide/multi_project_builds.html#sec:creating_multi_project_builds)
(also known as "modules" in Android Studio), which can also be used as
dependencies. Each subproject produces outputs (such as jars) that can be
consumed by subprojects or your top-level project. This can improve build time
by isolating which parts need to be rebuilt, as well as better separate
responsibilities in the application.

We'll go into more detail on how to specify dependencies in [Add build
dependencies](https://developer.android.com/build/dependencies).

## Build variants

When you create an Android application, you'll typically want to build multiple
[variants](https://developer.android.com/build/build-variants). Variants contain different code or are built with different
options, and are composed of build types and product flavors.

[Build types](https://developer.android.com/build/build-variants#build-types) vary declared build options. By default, AGP sets up "release"
and "debug" build types, but you can adjust them and add more (perhaps for
staging or internal testing).

A debug build doesn't minify or obfuscate your application, speeding up its
build and preserving all symbols as is. It also marks the application as
"debuggable", signing it with a generic debug key and enabling access to the
installed application files on the device. This makes it possible to explore
saved data in files and databases while running the application.

A release build optimizes the application, signs it with your release key, and
protects the installed application files.

Using [product flavors](https://developer.android.com/build/build-variants#product-flavors), you can change the included source and [dependency
variants](https://developer.android.com/build/build-variants#variant_aware) for the application. For example, you may want to create "demo"
and "full" flavors for your application, or perhaps "free" and "paid" flavors.
You write your common source in a "main" [source set](https://developer.android.com/build/build-variants#sourcesets) directory, and
override or add source in a source set named after the flavor.

AGP creates variants for each combination of build type and product flavor. If
you don't define flavors, the variants are named after the build types. If you
define both, the variant is named `<flavor><Buildtype>`. For example, with build
types `release` and `debug`, and flavors `demo` and `full`, AGP will create
variants:

- `demoRelease`
- `demoDebug`
- `fullRelease`
- `fullDebug`

## Next steps

Now that you've seen the build concepts, take a look at the [Android build
structure](https://developer.android.com/build/android-build-structure) in your project.