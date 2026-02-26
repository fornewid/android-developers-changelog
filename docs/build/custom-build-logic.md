---
title: https://developer.android.com/build/custom-build-logic
url: https://developer.android.com/build/custom-build-logic
source: md.txt
---

This section describes advanced topics that are useful when you want to extend
the Android Gradle plugin or write your own plugin.

## Publish variant dependencies to custom logic

A library can have functionalities that other projects or sub-projects might
want to use. Publishing a library is the process by which the library is made
available to its consumers. Libraries can control which dependencies its
consumers have access to at compile time and runtime.

There are two separate configurations that hold the transitive dependencies of
each classpath which must be used by consumers to consume the library as
described below:

- `variant_nameApiElements`: This configuration holds the transitive dependencies that are available to consumers at compile time.
- `variant_nameRuntimeElements`: This configuration holds the transitive dependencies that are available to consumers at runtime.

To learn more about the relationships between the different configurations,
go to [The Java Library
plugin configurations](https://docs.gradle.org/current/userguide/java_library_plugin.html#s
ec:java_library_configurations_graph).

## Custom dependency resolution strategies

A project may include a dependency on two different versions of the same library
which can lead to dependency conflicts.
For example, if your project depends on version 1 of module A and version 2 of
module B, and module A transitively depends on version 3 of module B,
there arises a dependency version conflict.

To resolve this conflict, the Android Gradle plugin uses the following
dependency resolution strategy: when the plugin detects that different versions
of the same module are in the dependency graph, by default, it chooses the one
with the highest version number.

However, this strategy might not always work as you intend. To customize the
dependency resolution strategy, use the following configurations to
resolve specific dependencies of a variant that are needed for your task:

- `variant_nameCompileClasspath`: This configuration contains the resolution strategy for a given variant's compile classpath.
- `variant_nameRuntimeClasspath`: This configuration contains the resolution strategy for a given variant's runtime classpath.

The Android Gradle plugin includes getters that you can use to access the
configuration objects of each variant. Thus, you can use the variant API to
query the dependency resolution as shown in the example below:

### Kotlin

```kotlin
android {
    applicationVariants.all {
        // Return compile configuration objects of a variant.
        compileConfiguration.resolutionStrategy {
        // Use Gradle's https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html
        // to customize how this variant resolves dependencies.
            ...
        }
        // Return runtime configuration objects of a variant.
        runtimeConfiguration.resolutionStrategy {
            ...
        }
        // Return annotation processor configuration of a variant.
        annotationProcessorConfiguration.resolutionStrategy {
            ...
        }
    }
}
```

### Groovy

```groovy
android {
    applicationVariants.all { variant ->
        // Return compile configuration objects of a variant.
        variant.getCompileConfiguration().resolutionStrategy {
        // Use Gradle's https://docs.gradle.org/current/dsl/org.gradle.api.artifacts.ResolutionStrategy.html
        // to customize how this variant resolves dependencies.
            ...
        }
        // Return runtime configuration objects of a variant.
        variant.getRuntimeConfiguration().resolutionStrategy {
            ...
        }
        // Return annotation processor configuration of a variant.
        variant.getAnnotationProcessorConfiguration().resolutionStrategy {
            ...
        }
    }
}
```