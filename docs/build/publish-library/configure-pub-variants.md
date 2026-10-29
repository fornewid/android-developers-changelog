---
title: https://developer.android.com/build/publish-library/configure-pub-variants
url: https://developer.android.com/build/publish-library/configure-pub-variants
source: md.txt
---

Publication variants let you create a more customized experience for your users.
Configuring publication variants lets you publish different build variants,
each with its own attributes.

Publishing multiple build variants of your library lets your user choose the
appropriate features for their needs. For example, you can publish different
artifacts for the
[debug versus release](https://developer.android.com/studio/build/build-variants#build-types)
build types. The debug publication artifact might have extra logging code and
different dependencies to enable this extra logging.

Before you proceed, make sure you
[prepare your library for release](https://developer.android.com/studio/publish-library/prep-lib-release).

### Use Gradle Module Metadata

In order to publish variants of your library, you must use
[Gradle Module Metadata (GMM)](https://docs.gradle.org/current/userguide/publishing_gradle_module_metadata.html).
GMM describes your publication and maintains
[variant-aware dependency management](https://developer.android.com/studio/build/build-variants#variant_aware).
GMM is published with your library by default.

The benefits of using GMM include:

- If you use GMM with Gradle 6.0 or higher, you can publish multiple publication variants or multiple artifacts---each with its own attributes and dependencies. If you use Maven's [POM file](https://maven.apache.org/pom.html) instead of GMM, you can only publish one artifact. If you use a POM file, you can publish additional artifacts using classifiers, but the additional artifacts can't have their own dependencies.
- Gradle automatically creates one variant for compilation and one for runtime, each with its own dependencies. You might publish one variant for compilation and one for runtime, so the consumer can choose based on when they are using your library. GMM lets consumers see different dependencies for compile and runtime, based on the published library's usage of `api`, `implementation`, or `compileOnly`/`runtimeOnly`. See [Dependency configurations](https://developer.android.com/studio/build/dependencies?agpversion=4.1&buildsystem=ndk-build#dependency_configurations) for a full list of dependencies. This is available even if you publish a single publication variant.
- When using test fixtures, you can publish an additional variant with special metadata or [capabilities](https://docs.gradle.org/current/userguide/component_capabilities.html) that let the consumer select it. This is available even if you publish a single publication variant.

### Understand publication variants

To understand how publication variants work, it is helpful to be familiar with
Gradle's
[basic publishing steps](https://docs.gradle.org/current/userguide/publishing_setup.html#sec:basic_publishing).
Here are some publication key concepts:

- **Build variant** : The configuration Gradle uses to build your library, which is the cross product of build type and product flavor. To learn more, see the [Android build glossary](https://developer.android.com/studio/build#build-config).
- [**Artifact**](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_artifact): A file or directory that a build produces. In the context of library publishing, an artifact is usually a JAR or AAR file.
- [**Publication variant**](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_variant): An artifact with its associated attributes, features, and dependencies. Note that Gradle calls publication variants *variants* . However, they are called *publication variants* in these docs to distinguish them from *build variants*.
- [**Attribute**](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_attribute): Gradle uses attributes to identify and select publication variants when there are multiple options. For example, `org.gradle.usage=java-api` and `org.gradle.jvm.version=11` are variant attributes.
- [**Software component**](https://docs.gradle.org/current/javadoc/org/gradle/api/component/SoftwareComponent.html): A Gradle object that can hold one or more publication variants and is published to a single set of Maven coordinates (`groupdId:artifactId:version`). It is exposed in Gradle's DSL through [`Project.getComponents()`](https://docs.gradle.org/current/javadoc/org/gradle/api/Project.html#getComponents--).
- [**Publication**](https://docs.gradle.org/current/userguide/dependency_management_terminology.html#sub:terminology_publication): What gets published to the repository and consumers use. Publications consist of one software component and its metadata-for instance, its identity (`groupId:artifactId:version`).

The [Android Gradle plugin](https://developer.android.com/studio/releases/gradle-plugin?buildsystem=cmake) (AGP) 7.1 introduces a
domain-specific language (DSL) to control which build variants are used during
publication and which are ignored. The DSL lets you create instances of
`SoftwareComponent` that contain either of the following:

- One publication variant from one build variant
- Several publication variants from several build variants

When creating a software component with multiple publication variants, AGP sets
up attributes on each variant that let the consumer select the
appropriate variant they need. These attributes come directly from the build
type and flavors used to create the build variant. Creating a
component with a single publication variant doesn't require attributes because
there's no need to distinguish.

## Create a software component with a single publication variant

The following snippet configures a software component with a single publication
variant created from the `release` build variant and adds the source JAR as a
secondary artifact:

### Kotlin

```kotlin
android {
  publishing {
    singleVariant("release") {
        withSourcesJar()
    }
  }
}
```

### Groovy

```groovy
android {
  publishing {
    singleVariant('release') {
        withSourcesJar()
    }
  }
}
```

You can create several components, each with a single publication variant, and
distribute them under different Maven coordinates. In this case, attributes
aren't set on the publication variant. You can't tell that this publication
variant is from the `release` build variant by looking at the publication
metadata. Since there's only one publication variant involved, there's no need
for disambiguation.

## Create a software component with multiple publication variants

You can select all or a subset of build variants to put in a single software
component. AGP automatically uses the build type names, product flavor
names, and product flavor dimension names to create attributes so that the
consuming project can distinguish between them.

To publish all build variants in a single component, specify `allVariants()`
in the `multipleVariants{}` block in the module-level `build.gradle` file:

### Kotlin

```kotlin
android {
  publishing {
    multipleVariants {
      allVariants()
      withJavadocJar()
    }
  }
}
```

### Groovy

```groovy
android {
  publishing {
    multipleVariants {
      allVariants()
      withJavadocJar()
    }
  }
}
```

This creates a single component called `default`. To name your component
something else, use `multipleVariants({name})`.
In this case, all build type and product flavor dimensions are used as
attributes.

You can also select which variants are published by using
`includeBuildTypeValues()` and `includeFlavorDimensionAndValues()`:

### Kotlin

```kotlin
android {
  publishing {
    multipleVariants("custom") {
      includeBuildTypeValues("debug", "release")
      includeFlavorDimensionAndValues(
        dimension = "color",
        values = arrayOf("blue", "pink")
      )
        includeFlavorDimensionAndValues(
          dimension = "shape",
          values = arrayOf("square")
      )
    }
  }
}
```

### Groovy

```groovy
android {
  publishing {
    multipleVariants('custom') {
      includeBuildTypeValues('debug', 'release')
      includeFlavorDimensionAndValues(
        /*dimension =*/ 'color',
        /*values =*/ 'blue', 'pink'
      )
      includeFlavorDimensionAndValues(
        /*dimension =*/ 'shape',
        /*values =*/ 'square'
      )
    }
  }
}
```

In this example, the custom component contains all the combinations of
(`debug`, `release`) for build type, (`blue`, `pink`) for the dimension `color`,
and (`square`) for the dimension `shape` .

All flavor dimensions must be listed, even if you are only publishing one value
from a dimension, so AGP knows which value to use for every dimension.

The following table lists the resulting publication variants and their
associated attributes.

> [!NOTE]
> **Note:** As specified in the build file, build variants that use values of `shape` other than `square` are not included in the publication. Because of this, the attribute for the product flavor dimension `shape` is not included. The consumer doesn't need to select a value for this dimension. For more information on how Gradle prioritizes product flavors and dimensions when naming build variants, see [Combine multiple product flavors
> with flavor dimensions](https://developer.android.com/studio/build/build-variants#flavor-dimensions).

| Variant | Attributes |
|---|---|
| `blueSquareDebug` | [`com.android.build.api.attributes.BuildTypeAttr`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/attributes/BuildTypeAttr)`="debug"` [`com.android.build.api.attributes.ProductFlavorAttr:color`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/attributes/ProductFlavorAttr)`="blue"` |
| `blueSquareRelease` | ` com.android.build.api.attributes.BuildTypeAttr="release" com.android.build.api.attributes.ProductFlavorAttr:color="blue"` |
| `pinkSquareDebug` | ` com.android.build.api.attributes.BuildTypeAttr="debug" com.android.build.api.attributes.ProductFlavorAttr:color="pink"` |
| `pinkSquareRelease` | ` com.android.build.api.attributes.BuildTypeAttr="release" com.android.build.api.attributes.ProductFlavorAttr:color="pink"` |

In practice, more variants get published. For instance,
each of the above variants is published twice, once for compilation and once for
runtime, with different dependencies (based on whether the declared dependencies
use `implementation` or `api`) and with a different value for the attribute
`org.gradle.Usage`. However, the artifacts (AAR file) for these two variants are
the same.

For more information, see the
[`publishing`](https://developer.android.com/reference/tools/gradle-api/7.1/com/android/build/api/dsl/LibraryExtension#publishing)
API documentation.

> [!IMPORTANT]
> **Important:** When publishing multiple publication variants, the names of the product flavors and flavor dimensions become part of the publishing API. So, the consuming project should either have matching flavor and dimension names or use methods to [add build dependencies](https://developer.android.com/studio/build/dependencies?agpversion=4.1&buildsystem=ndk-build) and manually select the artifact needed. For build types, because the dimension is built in, only build type names need to match, or the consumer project must use fallbacks as well.

## Compatibility issue for publishing multi-flavor libraries

A project using AGP 7.0 or below cannot consume multi-flavor libraries published
with AGP 7.1 or above. This is a known issue caused by a change to the attribute
name for product flavor dimension from `dimensionName` to
`com.android.build.api.attributes.ProductFlavor:dimensionName` in AGP 7.1.
Depending on your project setup, you can use [`missingDimensionStrategy` in
the old variant API](https://developer.android.com/build/build-variants#resolve_matching_errors) to work
around this issue.

For example, suppose your application project only has a version product
flavor dimension:

<br />

### Kotlin

<br />

    android {
        applicationVariants.forEach { variant ->
            val flavor = variant.productFlavors[0].name
            val attributePrefix = "com.android.build.api.attributes.ProductFlavor"
            val dimensionName = "version"
            variant.missingDimensionStrategy("$attributePrefix:$dimensionName", flavor)
        }
    }

<br />

### Groovy

<br />

    android {
        applicationVariants.forEach { variant ->
            def flavor = variant.getProductFlavors()[0].name
            def attributePrefix = "com.android.build.api.attributes.ProductFlavor"
            def dimensionName = "version"
            variant.missingDimensionStrategy("$attributePrefix:$dimensionName", flavor)
        }
    }

<br />

<br />