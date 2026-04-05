---
title: https://developer.android.com/build/releases/gradle-plugin-api-updates
url: https://developer.android.com/build/releases/gradle-plugin-api-updates
source: md.txt
---

This page tracks Android Gradle plugin (AGP) API deprecation and removals, and
provides info on how to update your code accordingly.

## API deprecations and removals tracker

The following table summarizes when AGP APIs are deprecated and removed, in
terms of AGP version.

| API | Deprecated in AGP version | Removed from AGP version |
|---|---|---|
| [`Component.setAsmFramesComputationMode`](https://developer.android.com/build/releases/gradle-plugin-api-updates#instrumentatin-apis-deprecated) | 7.2 |   |
| [`Component.transformClassesWith`](https://developer.android.com/build/releases/gradle-plugin-api-updates#instrumentatin-apis-deprecated) | 7.2 |   |
| [RenderScript](https://developer.android.com/build/releases/gradle-plugin-api-updates#renderscript-deprecated) | 7.2 |   |
| [Transform](https://developer.android.com/build/releases/gradle-plugin-api-updates#transform-removed) | 7.2 | 8.0 |

## AGP 8.12

Android Gradle plugin 8.12.0 contains the following notable API changes.

### Behavior change: `includeAndroidResources` option merges manifest from test directory

You can now create an `AndroidManifest.xml` file in your test source directory to
customize the manifest for unit tests with the
`android.testOptions.unitTests.includeAndroidResources` option. The
test manifest file will merge into the app's main manifest.
[Issue #127986458](https://issuetracker.google.com/127986458)

## AGP 8.10

Android Gradle plugin 8.10.0 contains the following notable API changes.

### Source level breaking change: `finalizeDsl` now requires use of parameterized types

To allow `AndroidComponentsExtension` to be used directly with the
`com.android.kotlin.multiplatform.library` plugin, the type bound on
`finalizeDsl` was relaxed.

For example, if you were using raw types of `AndroidComponentsExtension` to
address applications and libraries:

    extensions.getByType(AndroidComponentsExtension::class).finalizeDsl { androidExtension ->
      androidExtension.experimentalProperties["android.example"] = true
    }

You will need to adapt your source code before or during upgrade to something
like:

    extensions.getByType<AndroidComponentsExtension<CommonExtension<*, *, *, *, *, *>, *, *>>().finalizeDsl { androidExtension ->
      androidExtension.experimentalProperties["android.example"] = true
    }

Note that if you want to write `finalizeDsl` code that works against both the
current `com.android.library` and `com.android.application` plugins and the
new `com.android.kotlin.multiplatform.library` plugin, you might need to check
the types at runtime:

    extensions.getByType<AndroidComponentsExtension<*, *, *>>().finalizeDsl { androidExtension ->
      when(androidExtension) {
        is CommonExtension<*, *, *, *, *, *> -> androidExtension.experimentalProperties["android.example"] = true
        is KotlinMultiplatformAndroidLibraryExtension -> androidExtension.experimentalProperties["android.example"] = true
      }
    }

This is a source level breaking change only, and won't affect binary plugins.

## AGP 8.8

The following are important API updates for AGP 8.8.

### Resource Configurations have been deprecated

[Resource Configurations](https://developer.android.com/build/shrink-code#unused-alt-resources) have been
[deprecated as of AGP 8.8](https://developer.android.com/reference/tools/gradle-api/8.8/com/android/build/api/dsl/BaseFlavor#resourceConfigurations()).
This was done because AGP no longer supports different resource densities
and the Google Play Console now requires apps to be published as App Bundles.
For language configuration, you can specify
[the locales that your app supports](https://developer.android.com/reference/tools/gradle-api/8.8/com/android/build/api/dsl/ApplicationAndroidResources#localeFilters()) using the `localeFilters` DSL to map locale configurations to the
corresponding resources.

## AGP 8.0

The following are important API updates for AGP 8.0.

### Transform API is removed

Starting with AGP 8.0, the
[Transform](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/transform/Transform)
API is removed. This means that all classes in the package
`com.android.build.api.transform` are removed.

The Transform API is being removed to improve build performance. Projects that
use the Transform API force AGP to use a less optimized flow for the build that
can result in large regressions in build times. It's also difficult to use the
Transform API and combine it with other Gradle features; the replacement APIs
aim to make it easier to extend AGP without introducing performance or build
correctness issues.

#### Replacement APIs

There is no single replacement for the Transform API---there are new, targeted
APIs for each use case. All the replacement APIs are in the `androidComponents
{}` block. These APIs are all available by AGP 7.2.

##### Support for transforming bytecode

To transform bytecode, use the Instrumentation API. For libraries, you can
register an instrumentation for local project classes only; for apps and tests,
you can choose to register an instrumentation for only local classes or all
classes, including local and remote dependencies. To use this API, the
instrumentation runs independently on each class, with limited access to other
classes in the classpath (see
[`createClassVisitor()`](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/instrumentation/AsmClassVisitorFactory#createClassVisitor(com.android.build.api.instrumentation.ClassContext,org.objectweb.asm.ClassVisitor))
for more information). This restriction improves the performance of
both full and incremental builds, and keeps the API surface simple. Each library
is instrumented in parallel as soon as it is ready, rather than after all
compilation is complete. In addition, a change in a single class
means that only affected classes have to be reinstrumented in an incremental
build. For example of how to use the Instrumentation API, see the
[Transforming classes with ASM](https://github.com/android/gradle-recipes/tree/agp-7.2/BuildSrc/testAsmTransformApi)
AGP recipe.

##### Support for adding generated classes to your app

To add additional generated classes to the app, use the
[Artifacts](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/artifact/Artifacts#use(org.gradle.api.tasks.TaskProvider))
API with
[`MultipleArtifact.ALL_CLASSES_DIRS`](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/artifact/MultipleArtifact.ALL_CLASSES_DIRS).
Specifically, use

    artifacts.use(TaskProvider)
      .wiredWith(...)
      .toAppend(Artifact.Multiple)

with `MultipleArtifact.ALL_CLASSES_DIRS` to append additional generated
directories to the project classes. The Artifacts API will automatically select
a unique location for your custom task to output to. See the
[addToAllClasses recipe](https://github.com/android/gradle-recipes/tree/agp-7.1/Kotlin/addToAllClasses)
for an example of how to use this API.

##### Support for transformations based on whole program analysis

To implement transformations based on whole program analysis, all classes can be
transformed together in a single task. This approach should be used with caution
as it has a much higher build performance cost than using the Instrumentation
API. If your plugin uses this API, it is recommended to have the transformation
be opt-in per build type, so that the app developer can disable it for
development builds.

To register a task that transforms all classes together, Android Gradle plugin 7.4
introduces the
[Artifacts.forScope](https://developer.android.com/reference/tools/gradle-api/7.4/com/android/build/api/artifact/Artifacts#forScope(com.android.build.api.variant.ScopedArtifacts.Scope))
API. To transform all classes in the current project, use
`Artifacts.forScope.PROJECT`. To transform all classes in the current project,
imported projects, and all external dependencies, use `Artifacts.forScope.ALL`.
The following code shows how to use `Artifacts.forScope.ALL` to register a
task that transforms all classes together:

    variant.artifacts.forScope(ScopedArtifacts.Scope.ALL)
        .use(taskProvider)
        .toTransform(
            ScopedArtifact.CLASSES,
            ModifyClassesTask::allJars,
            ModifyClassesTask::allDirectories,
            ModifyClassesTask::output,
        )

See the
[modifyProjectClasses recipe](https://github.com/android/gradle-recipes/blob/agp-7.4/Kotlin/modifyProjectClasses/app/build.gradle.kts)
for an example of how to use this API, and the
[customizeAgpDsl recipe](https://github.com/android/gradle-recipes/tree/agp-7.2/BuildSrc/customizeAgpDsl)
for an example of how to register custom extensions to the Android build types.

If your use case is not covered by any of the
[AndroidComponents](https://developer.android.com/reference/tools/gradle-api/7.2/com/android/build/api/variant/AndroidComponentsExtension)
APIs, please [file a bug](https://developer.android.com/studio/report-bugs).

Several commonly used plugins have already migrated to use these new APIs,
including the Firebase performance monitoring plugin (1.4.1 is compatible with
AGP 8.0) and the Hilt Gradle plugin (2.40.1 is compatible with AGP 8.0). The AGP
Upgrade Assistant will also help project developers upgrade commonly used
plugins as needed.

If you're using the Transform API through a third-party plugin, please let the
author know that their plugin will need to be updated to work with the new APIs
for AGP 8.0.

## AGP 7.2

The following are important API updates for AGP 7.2.

### RenderScript is deprecated

Starting with AGP 7.2, the RenderScript APIs are deprecated. They will continue
to function, but invoke warnings, and will be completely removed in future
versions of AGP. For guidance on how to transition off of RenderScript, see
[Migrate from RenderScript](https://developer.android.com/guide/topics/renderscript/migrate).

### `Component.transformClassesWith` and `Component.setAsmFramesComputationMode` are deprecated

Starting with AGP 7.2, the class bytecode instrumentation APIs
[`Component.transformClassesWith`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/variant/Component#transformclasseswith) and
[`Component.setAsmFramesComputationMode`](https://developer.android.com/reference/tools/gradle-api/7.0/com/android/build/api/variant/Component#setAsmFramesComputationMode) are deprecated. They have moved to a new block, `Component.instrumentation`, which
contains all APIs related to configuring the instrumentation process. To
continue using these instrumentation features, use the corresponding APIs in
the new block instead, as shown by the following code snippet:

    androidComponents {
          onVariants(selector().all(), {
              instrumentation.transformClassesWith(AsmClassVisitorFactoryImpl.class,
                                                   InstrumentationScope.Project) { params ->
                  params.x = "value"
              }
              instrumentation.setAsmFramesComputationMode(
                  COMPUTE_FRAMES_FOR_INSTRUMENTED_METHODS
              )
          })
      }