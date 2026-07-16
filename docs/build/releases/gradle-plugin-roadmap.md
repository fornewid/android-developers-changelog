---
title: https://developer.android.com/build/releases/gradle-plugin-roadmap
url: https://developer.android.com/build/releases/gradle-plugin-roadmap
source: md.txt
---

The Android Gradle Plugin (AGP) is the supported build system for Android
applications and includes support for compiling many different types of sources
and linking them together into an application that you can run on a physical
Android device or an emulator.

The following section describes the planned evolution of the AGP's DSL and API.
As new APIs are introduced in stable releases, old APIs will be marked as
deprecated. Those deprecated APIs will then become unavailable in the next
stable release. The following sections provide information about upcoming
changes in each major AGP release.

For a more detailed log of AGP API deprecations or removals, see the [AGP API
updates](https://developer.android.com/studio/releases/gradle-plugin-api-updates).

> [!NOTE]
> **Note:** The following timeframes are estimates and are subject to change.

## AGP 10.0 (late 2026)

### Android Gradle Plugin 10.0 API changes and modernization

AGP 10.0 completes the transition to a fully lazy,
configuration-cache-compatible build model. This release is the culmination of
a multi-year effort to replace legacy, non-lazy APIs with a safer, more
performant architecture.

#### Why a lazy build model?

In the legacy, non-lazy build model, Gradle eagerly evaluates objects, queries
variant data, and configures tasks across all project modules during every sync
or build invocation. This eager evaluation wastes CPU time and memory on
variants and tasks that aren't running, and causes evaluation ordering
conflicts across complex build scripts.

By transitioning to a fully lazy build model using lazy providers
(`Provider<T>`) and the modern Variant API (`androidComponents {}`), properties
and task wiring are computed lazily on demand only when needed by the
active build execution graph.

The legacy APIs being removed in this release were fundamentally incompatible
with this modern architecture. Removing them enables AGP to fully support
Gradle Configuration Cache and Project Isolation, which drastically improve
build speeds and sync times in Android Studio.

##### The core architectural difference

The legacy `BaseVariant` API (`applicationVariants.all {}`) was eager and
task-centric. It gave developers direct access to Gradle tasks and internal
configurations during the configuration phase, which inherently breaks modern
Gradle performance features.

The new Variant API (`androidComponents {}`) is lazy and artifact-centric. It
uses Gradle's Property API extensively and completely removes all references to
`Task` and `TaskProvider`, requiring you to interact cleanly with inputs and
outputs (`Variant.artifacts`) rather than the underlying tasks themselves.

#### What is being removed and replaced

All previous interfaces and classes used in the legacy DSL and the old Variant
API are deleted. To prepare your build scripts and custom plugins, migrate
away from the following end-of-life APIs and flags:

| Removed API or feature | Replacement or action needed |
|---|---|
| Direct task access: - `getJavaCompile()` - `getMergeResourcesProvider()` - `getAssembleProvider()` | **The Artifacts API:** Instead of fetching the task to change its behavior, use `variant.artifacts` to append, modify, or replace actual files (Artifacts) passing between tasks. |
| Eager source registration: - `registerJavaGeneratingTask()` - `registerResGeneratingTask()` | **The Sources API:** Wire your custom task's output directory using `variant.sources.java.addGeneratedSourceDirectory(...)`. |
| Classpath / configuration access: - `getCompileConfiguration()` - `getCompileClasspath()` | **The Instrumentation API:** To modify or inspect bytecode (the most common use case for classpath access), use `variant.instrumentation.transformClassesWith(...)` using `AsmClassVisitorFactory`. |
| Eager property mutation: - `buildConfigField()` - `resValue()` | **Lazy \`MapProperty\` instances:** Use `variant.buildConfigFields.put(...)` and `variant.manifestPlaceholders.put(...)`. |
| Opt-out flags: - `android.newDsl` - `android.builtInKotlin` | No direct replacement. Remove these flags from `gradle.properties`; the modern DSL and built-in Kotlin are strictly enforced. |
| Legacy Variant API extensions: - `applicationVariants` - `libraryVariants` - `testVariants` - `unitTestVariants` | Replace with `androidComponents.onVariants()`. |
| Variant filtering (`variantFilter` block) | Replace with `androidComponents.beforeVariants()` using variant selectors. |
| SDK and NDK components: - `sdkDirectory` - `ndkDirectory` - `bootClasspath` - `adbExecutable` | Access SDK components using `androidComponents.sdkComponents`. |
| Test environments: - `deviceProvider` - `testServer` | Migrate custom test device registration to Gradle-managed devices. |
| Obsolete registration APIs: - `registerArtifactType` - `registerBuildTypeSourceProvider` - `registerProductFlavorSourceProvider` - `registerJavaArtifact` - `registerMultiFlavorSourceProvider` - `wrapJavaSourceSet` | Deleted without direct replacement. |
| Transform API | Replace transforms with the Artifacts API and `AsmClassVisitorFactory`. |

To access all replacement DSL and Variant API (`androidComponents {}`)
interfaces and classes, always use the [`gradle-api`](https://maven.google.com/web/index.html#com.android.tools.build:gradle-api)
artifact when developing custom Gradle plugins or build logic.

#### Migration steps

To help make your upgrade to AGP 10.0 seamless and predictable, follow these
migration practices:

1. **Run the AGP Upgrade Assistant:** Before upgrading directly to 10.0, run the official [AGP Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant) in Android Studio (`Tools > AGP Upgrade Assistant`). It automates several common DSL and build script migrations and helps preserve existing build behaviors.
2. **Use Agent Mode skills in Android Studio:** Take advantage of AI upgrade skills (such as the AGP upgrade skills available in the [Android skills
   repository](https://github.com/android/skills)) to automate and simplify migrating complex build logic and DSLs inside Android Studio.
3. **Fix deprecation warnings in AGP 9.x first:** Upgrade your project to the latest AGP 9.x release and resolve all existing deprecation warnings. Once your project works with 9.x warning-free and without relying on `android.newDsl=false` or `android.builtInKotlin=false`, moving to 10.0 will be a smooth transition.
4. **Audit third-party Gradle plugins:** Ensure third-party plugins are upgraded to AGP 10.0 compatible versions. Plugins still relying on legacy extension types will cause build failures such as `ClassCastException: ... cannot be cast to class BaseExtension`.
5. **Use official migration recipes:** For complex, real-world migration examples and side-by-side comparisons, refer to the official [gradle-recipes GitHub repository](https://github.com/android/gradle-recipes).

Here is a before-and-after comparison showing how to migrate from eagerly
querying legacy variants to lazily configuring variants using
`androidComponents {}`:

**Before: Legacy Variant API (Removed in AGP 10.0)**

    // Eager evaluation using the legacy Variant API
    android {
        applicationVariants.all { variant ->
            if (variant.buildType.name == "release") {
                // Eagerly queries and modifies properties during evaluation
            }
        }
    }

**After: Modern Variant API (`androidComponents {}`)**

    // Lazy, Configuration Cache compatible Variant API
    androidComponents {
        onVariants(selector().withBuildType("release")) {> variant -
            // Safely and lazily configures properties
        }
    }

#### How to test AGP 10.0 behavior in AGP 9.x

You don't need to wait for the AGP 10.0 release to start testing its build
behaviors and validating compatibility. While running on any AGP 9.x
release, you can explicitly enforce AGP 10.0 behavior by verifying that your
`gradle.properties` disables any opt-outs and sets the following strict
behavior flags:

    # Enforce modern DSL and Variant API interfaces exclusively
    android.newDsl=true

    # Enforce built-in Kotlin support without optional opt-out
    android.builtInKotlin=true

By enforcing `android.newDsl=true` and `android.builtInKotlin=true`, you can
verify that your custom build logic and third-party plugins are fully
compatible with the strict API requirements of AGP 10.0.

#### Selective sub-project opt-out during migration

If you want to enable `android.newDsl=true` globally across your project to
test modern behaviors, but need more time to migrate specific sub-projects, you
can selectively opt out individual modules starting in AGP 9.4.0-alpha04.
Add `android.newDsl.optOut` to `gradle.properties` specifying project paths:

    # Enable modern DSL globally across the build
    android.newDsl=true

    # Selectively opt out specific sub-projects that still require legacy DSL APIs
    android.newDsl.optOut=:lib

> [!NOTE]
> **Note:** Sub-project opt-out (`android.newDsl.optOut`) is a temporary migration aid for AGP 9.x and will be removed along with `android.newDsl` in AGP 10.0.

#### Selective built-in Kotlin disablement per module

If you want to enable built-in Kotlin globally across your project
(`android.builtInKotlin=true`), but need more time to migrate specific
sub-projects off of `kotlin-android` (or for modules without Kotlin code),
configure those modules at the DSL level rather than the project level. Set
`enableKotlin = false` inside the module's build file:

    android {
        enableKotlin = false
    }

> [!NOTE]
> **Note:** Disabling built-in Kotlin at the module level (`enableKotlin = false`) on non-Kotlin sub-projects removes the Kotlin compiler task (improving build performance) and avoids adding dependencies on the Kotlin standard library.

#### Feedback and bug reporting workflow

We want to ensure the new Variant API supports your required use
cases. If you encounter a roadblock migrating away from the old APIs where the
new Variant API cannot accommodate your use case, follow these steps to give
feedback:

1. **Check existing items:** First, check the [AGP 10.0 Variant API Global
   Tracking Bug](https://issuetracker.google.com/532056644) to see if your migration blocker is already known, and +1 the issue.
2. **Report missing APIs:** If your use case is unique, [file a new feature
   request](https://issuetracker.google.com/issues/new?component=192708&template=840533) using our specific Variant API template so we can investigate and assist.

### (Tentative) Access to private internal AGP classes is removed

Dependency on the [`gradle`](https://maven.google.com/web/index.html#com.android.tools.build:gradle) artifact now hides all internal
classes and gives compilation access only to the interfaces and classes
available in the `gradle-api` artifact. This impacts
plugin compilation.

It isn't possible to manually add a dependency to get access to the internal
classes.

> [!IMPORTANT]
> **Important:** We would like your feedback on the removal of internal AGP classes. Tell us your use case, including specific examples of what you need access to, by submitting your feedback on this [tracking issue](https://issuetracker.google.com/219002669).

## AGP 9.0 (January 2026)

### New Variant APIs are stable, old APIs are deprecated

The [Variant APIs](https://medium.com/androiddevelopers/new-apis-in-the-android-gradle-plugin-f5325742e614) that were incubating in 4.1 and 4.2 are
stable and located in the [`gradle-api`](https://maven.google.com/web/index.html#com.android.tools.build:gradle-api) artifact. The
previous interfaces and classes used in the old Variant API are now
deprecated, and require [explicit opt-in](https://developer.android.com/build/releases/agp-9-0-0-release-notes#android-gradle-plugin-new-dsl) to use.

### New DSL interfaces are stable, old ones are deprecated

The [DSL interfaces](https://medium.com/androiddevelopers/new-apis-in-the-android-gradle-plugin-f5325742e614) that were incubating in 4.1, 4.2, and
7.0 are now stable and located in the `gradle-api` artifact. The previous
interfaces and classes used in the DSL are now deprecated, and require
[explicit opt-in](https://developer.android.com/build/releases/agp-9-0-0-release-notes#android-gradle-plugin-new-dsl) to use.

### Private internal AGP classes still accessible

Private internal classes from AGP, located in other artifacts, are still
accessible during compilation of build files and plugins, but we don't
recommend using them because they might change in breaking ways at any time.