---
title: https://developer.android.com/build/publish-library/fused-library
url: https://developer.android.com/build/publish-library/fused-library
source: md.txt
---

In projects with many modules, it can be challenging to distribute Android
Libraries to your users while trying to maintain a clear project structure.
In many cases, many more libraries need to be published than intended.

The Fused Library plugin bundled with Android Gradle Plugin assists with
packaging multiple Android Library modules into a single publishable Android
Library. This lets you modularize your library's source code and
resources within your build as you see fit, while avoiding exposure of your
project's structure once distributed.

> [!TIP]
> **Tip:** Take a look at the [Fused Library Plugin Gradle recipe](https://github.com/android/gradle-recipes/tree/agp-8.13/applyFusedLibraryPlugin), which provides steps to configure a fused library and more practical guidance.

Distributing as a single library can have the following benefits:

- **Simplified dependencies:** replaces multiple library dependencies with a single AAR, streamlining project setup and version management for your users
- **Reduced library size:** may improve code shrinking, leading to smaller AARs
- **Improved security:** can offer better control over the internal implementation details of published libraries

## Create a fused library

To build a fused library, you have to create a new Android module, add
dependencies, and then publish the fused library.

### Prerequisites

To use the Fused Library plugin, use AGP 9.0 or higher.
Previous versions of the Fused Library plugin have different behavior and issues
which are fixed in AGP 9.0.

### Add a new fused library module

To use the plugin, you must add a new Android module to your project:

*In this example, the fused library module will be called `myFusedLibrary`.*

1. Append `include(":myFusedLibrary")` to the `settings.gradle.kts` file.
2. Add `android-fusedlibrary = { id = "com.android.fused-library", version.ref = "agp" }` under the `[plugins]` section in the `gradle/libs.versions.toml` file.
3. Add `alias(libs.plugins.android.fusedlibrary) apply false` in the plugins block in the top level `build.gradle.kts` file.
4. To create the `myFusedLibrary` module, create a new directory called `myFusedLibrary` (right-click 'My Application' \> New \> Directory).
5. Create a `build.gradle.kts` file in the `myFusedLibrary` module (right-click the `myFusedLibrary` module \> New \> File).
6. Paste the following into the `myFusedLibrary/build.gradle.kts` file:

### Kotlin

```kotlin
plugins {
    alias(libs.plugins.android.fusedlibrary)
    `maven-publish`
}

androidFusedLibrary {
    namespace = "com.example.myFusedLibrary"
    minSdk = 21
}

dependencies { }
```

### Groovy

```groovy
plugins {
    id 'com.android.fused-library'
}

androidFusedLibrary {
    namespace 'com.example.myFusedLibrary'
    minSdk 21
}

dependencies {

}
```

### Add dependencies

The core functionality of the fused library is to bundle dependencies. The
plugin supports adding local project dependencies and external libraries.
To specify dependencies to be packaged, use the `include` configuration.
Transitive dependencies are not packaged.

For example:

### Kotlin

```kotlin
dependencies {
    include(project(":image-rendering"))
    include("mycoolfonts:font-wingdings:5.0")
}
```

### Groovy

```groovy
dependencies {
    include project(':image-rendering')
    include 'mycoolfonts:font-wingdings:5.0'
}
```

> [!NOTE]
> **Note:** If a dependency is specified using an `include` statement depends on a local Android library project, you must publish the local Android library project to a local configured repository. For more information, see [Publish your library](https://developer.android.com/studio/publish-library)

### Publish your fused library

You should familiarize yourself with [publishing an Android library](https://developer.android.com/studio/publish-library)
before publishing a fused library. Publishing a fused library is similar
to publishing an Android Library, however there are some key differences
that you must consider to publish the fused library correctly:

- The Maven Publish Plugin must also be applied to any module that has the Fused Library plugin applied.
- The publication must inherit from the `fusedLibraryComponent` because this provides the required dependencies needed to compile the fused library artifact.

Here's an example of a publications configuration:

### Kotlin

```kotlin
plugins {
    alias(libs.plugins.android.fusedlibrary)
    `maven-publish`
}

androidFusedLibrary { ... }

dependencies { ... }

publishing {
    publications {
        register<MavenPublication>("release") {
             groupId = "my-company"
             artifactId = "my-fused-library"
             version = "1.0"
             from(components["fusedLibraryComponent"])
        }
    }
}
```

### Groovy

```groovy
plugins {
    id 'com.android.fused-library'
    id 'maven-publish'
}

androidFusedLibrary { ... }

dependencies { ... }

publishing {
    publications {
        release(MavenPublication) {
            groupId = "my-company"
            artifactId = "my-fused-library"
            version = "1.0"
            afterEvaluate {
            from components.fusedLibraryComponent
        }
    }
}
```

#### Publish your fused library for testing

You should test depending on a published fused library from an Android app or
Android library. The recommended method is to publish to the fused library and
its project dependencies to a local Maven repository.

To publish the fused library artifacts to a local repository, define a
configuration similar to the following:

### Kotlin

```kotlin
plugins {
    alias(libs.plugins.android.fusedlibrary)
    `maven-publish`
}

repositories {
    maven {
        name = "myLocalRepo"
        url = uri(layout.buildDirectory.dir("myLocalRepo"))
    }
}
```

### Groovy

```groovy
plugins {
    id 'com.android.fused-library'
    id 'maven-publish'
}

repositories {
    maven {
        name 'myLocalRepo'
        url layout.buildDirectory.dir('myLocalRepo')
    }
}
```

## Upload your fused library

To distribute your fused library, see [Upload your library](https://developer.android.com/studio/publish-library/upload-library).

## Behavior and safeguards

Combining Android libraries have intricacies that can make it challenging for
the plugin to reason about priorities. For example, two libraries with the same
classpath will cause a build failure when fusing the library. Resource merging
will consider the order of dependencies specified when selecting a resource
with the same name in different libraries.

- Fused libraries can only be published as an Android library artifact AAR in order to be added as a dependency.
- Fusing libraries that use data binding isn't supported.
- You can't fuse multiple build types and product flavors within a single fused library. Create separate fused libraries for different variants.

To balance the amount of configuration needed and ease of use, the
plugin will either fail the build on ambiguous conflicts or use heuristics when
fusing artifacts. The details of how artifacts are fused are found in the
following table:

| Type | Behavior |
|---|---|
| Classes | Libraries with the same classpath will cause a build failure when fusing the library. |
| Android Resources | Resource merging will consider the order of dependencies specified when selecting a resource with the same name in different. |
| AAR Metadata | AAR metadata versions are merged by prioritizing the highest value from each dependency library. There is a DSL provided to override these values. ### Kotlin ``` androidFusedLibrary { aarMetadata { minCompileSdk = 21 minCompileSdkExtension = 1 } } ``` |
| Java Resources | Java resource files in multiple libraries with identical paths are not permitted and will result in a build failure. |

**Known issues**

Fused Library is a new plugin and there are known issues that are being worked
on to fulfill all use cases. You can [report bugs](https://developer.android.com/studio/report-bugs) for any issues you
encounter.

- [Issue #454305444](https://issuetracker.google.com/454305444): Libraries containing consumer proguard rules that are not called 'proguard.txt' result in a build failure. Fixed in AGP 9.1 and higher.
- [Issue #374982739](https://issuetracker.google.com/374982739): Adding file dependencies on other .aar files
- [Issue #231433225](https://issuetracker.google.com/231433225): No support for fusing RenderScript and Prefab artifacts

> [!WARNING]
> **Experimental:** A fused library module is limited to publication as an external library. A local fused library project cannot be added a project dependency to another module, in Android app or Android library modules. The plugin restricts fused library modules for publication only. Direct project consumption is not fully supported by Studio. The publication only restriction can be disabled by adding `android.experimental.fusedLibrarySupport.publicationOnly=false` to the `gradle.properties` file.

## Understand the dependencies of a fused library

The fused library has no sources and effectively uses Android libraries
as its only source, it's important to understand what comes from where. To list
the dependencies that are merged into the resultant artifact and the
dependencies needed to build the artifact, run the `gradle :report` task on the
fused library. The task generates a JSON report that is saved in the
`build/reports` directory of the fused library.

For additional information related to internal plugin dependencies, run the
`gradle :dependencies` task to view the state of plugin configurations.