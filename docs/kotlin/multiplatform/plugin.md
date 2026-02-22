---
title: https://developer.android.com/kotlin/multiplatform/plugin
url: https://developer.android.com/kotlin/multiplatform/plugin
source: md.txt
---

The `com.android.kotlin.multiplatform.library` Gradle plugin is the officially
supported tool for adding an Android target to a Kotlin Multiplatform (KMP)
[library module](https://developer.android.com/studio/projects/android-library). It simplifies project configuration, improves
build performance, and offers better integration with Android Studio.

Using the `com.android.library` plugin for KMP development depends on Android
Gradle Plugin APIs that are deprecated and [require opt-in](https://developer.android.com/r/tools/new-dsl) in Android
Gradle plugin 9.0 and higher (Q4 2025). These APIs
[are expected to be removed](https://developer.android.com/build/releases/gradle-plugin-roadmap) in Android Gradle plugin 10.0
(second half of 2026).

> [!NOTE]
> **Note:** There isn't a direct replacement for configuring a Kotlin Multiplatform module using `com.android.application` plugin. To migrate, extract your Android **application** to a separate Gradle module.

To apply this plugin, refer to the [Apply the Android-KMP plugin](https://developer.android.com/kotlin/multiplatform/plugin#apply)
section. If you need to migrate from the legacy APIs, check the [Migration
Guide](https://developer.android.com/kotlin/multiplatform/plugin#migrate).

> [!CAUTION]
> **Caution:** Before you migrate to the new plugin, be aware of the [known issues](https://developer.android.com/kotlin/multiplatform/plugin#known-issues) and [unsupported features](https://developer.android.com/kotlin/multiplatform/plugin#unsupported-features-and-workarounds).

## Key features and differences

The Android-KMP plugin is tailored specifically for KMP projects and differs
from the standard `com.android.library` plugin in several key aspects:

- **Single variant architecture:** The plugin uses a single variant, removing
  support for product flavors and build types, which simplifies configuration
  and enhances build performance.

- **Optimized for KMP:** The plugin is designed for KMP libraries, focusing on
  shared Kotlin code and interoperability, omitting support for
  Android-specific native builds, AIDL, and RenderScript.

- **Tests disabled by default:** Both unit and device (instrumentation) tests
  are disabled by default to enhance build speed. You can enable them if
  required.

- **No top-Level Android extension:** Configuration is handled with an
  `androidLibrary` block within the Gradle KMP DSL, maintaining a consistent
  KMP project structure. There's no top-level `android` extension block.

- **Opt-in Java compilation:** Java compilation is disabled by default. Use
  `withJava()` in the `androidLibrary` block to enable it. This improves build
  times when Java compilation is not needed.

## Benefits of the Android-KMP library plugin

The Android-KMP plugin provides the following benefits for KMP projects:

- **Improved build performance and stability:** It's engineered for optimized
  build speeds and enhanced stability within KMP projects. It's focus on KMP
  workflows contribute to a more efficient and reliable build process.

- **Enhanced IDE integration:** It provides better code completion,
  navigation, debugging, and overall developer experience when working with
  KMP Android libraries.

- **Simplified project configuration:** The plugin simplifies configuration
  for KMP projects by removing Android-specific complexities like build
  variants. This leads to cleaner and more maintainable build files.
  Previously, using the `com.android.library` plugin in KMP project could
  create confusing source set names, such as `androidAndroidTest`. This naming
  convention was less intuitive for developers familiar with standard KMP
  project structures.

## Workarounds for unsupported features

When compared to KMP integration with the `com.android.library` plugin, some
features are missing from the
`com.android.kotlin.multiplatform.library` plugin. Here are the workarounds
for the unsupported features:

- **Build variants**

  Build types and product flavors are not supported. This is because the new
  plugin uses a single variant architecture, which simplifies configuration and
  improves build performance.

  If you require build variants, our recommendation
  is to create a separate standalone Android library module using
  the `com.android.library` plugin, configure build types and product flavors
  within that module, and then consume it as a standard project dependency
  from your Kotlin Multiplatform library's `androidMain` source set.
  For more details, see [Create an Android library](https://developer.android.com/studio/projects/android-library) and
  [Configure build variants](https://developer.android.com/build/build-variants).
- **Data binding and View binding**

  These are Android-specific UI framework features tightly coupled to the
  Android View system and XML layouts. In the new Android-KMP library plugin we
  recommend that you handle the UI using a multiplatform framework like
  [Compose Multiplatform](https://www.jetbrains.com/compose-multiplatform/). Data binding and View binding
  are considered implementation details of a final Android app, not a shareable
  library.
- **Native build support**

  The new plugin focuses on producing a standard AAR for the Android target.
  Native code integration in Kotlin Multiplatform is handled directly by KMP's
  own native targets (such as `androidNativeArm64` and `androidNativeX86`) and
  its C-interop capabilities. If you need to include native C/C++ code, you
  should define it as part of a common or native source set and configure the
  C-interop within the `kotlin` block, rather than using the Android-specific
  `externalNativeBuild` mechanism.

  Alternatively, if you need native build support via `externalNativeBuild`, our
  recommendation is to create a separate standalone `com.android.library` module
  where you can integrate native code, and consume that standalone library from
  your Kotlin Multiplatform library project's `androidMain` source set.
  For more details, see [Create an Android library](https://developer.android.com/studio/projects/android-library) and
  [Add C and C++ code to your project](https://developer.android.com/studio/projects/add-native-code).
- **`BuildConfig` class**

  The `BuildConfig` feature is most useful in multi-variant environments.
  Since the new Kotlin Multiplatform library plugin is variant-agnostic and
  lacks support for build types and product flavors, this feature is not
  implemented. As an alternative, we recommend using the `BuildKonfig` plugin
  or similar community solutions to generate metadata for all targets.

## Prerequisites

To use the `com.android.kotlin.multiplatform.library` plugin, your project must
be configured with the following minimum versions or higher:

- **Android Gradle Plugin (AGP)**: 8.10.0
- **Kotlin Gradle Plugin (KGP)**: 2.0.0

## Apply the Android-KMP plugin to an existing module

To apply the Android-KMP plugin to an existing KMP library module, follow these
steps:

1. **Declare plugins in version catalog.** Open the version catalog TOML file
   (usually `gradle/libs.versions.toml`) and add the plugin definitions
   section:

       # To check the version number of the latest Kotlin release, go to
       # https://kotlinlang.org/docs/releases.html

       [versions]
       androidGradlePlugin = "9.0.0"
       kotlin = "KOTLIN_VERSION"

       [plugins]
       kotlin-multiplatform = { id = "org.jetbrains.kotlin.multiplatform", version.ref = "kotlin" }
       android-kotlin-multiplatform-library = { id = "com.android.kotlin.multiplatform.library", version.ref = "androidGradlePlugin" }

2. **Apply the plugin declaration in root build file.** Open the
   `build.gradle.kts` file located in the root directory of your project. Add
   the plugin aliases to the `plugins` block using `apply false`. This makes
   the plugin aliases available to all subprojects without applying the plugin
   logic to the root project itself.

   ### Kotlin

   ```kotlin
   // Root build.gradle.kts file

   plugins {
      alias(libs.plugins.kotlin.multiplatform) apply false

      // Add the following
      alias(libs.plugins.android.kotlin.multiplatform.library) apply false
   }
   ```

   ### Groovy

   ```groovy
   // Root build.gradle file

   plugins {
      alias(libs.plugins.kotlin.multiplatform) apply false

      // Add the following
      alias(libs.plugins.android.kotlin.multiplatform.library) apply false
   }
   ```
3. **Apply the plugin in a KMP library module build file.** Open the
   `build.gradle.kts` file in your KMP library module and apply the plugin at
   the top of your file within the `plugins` block:

   ### Kotlin

   ```kotlin
   // Module-specific build.gradle.kts file

   plugins {
      alias(libs.plugins.kotlin.multiplatform)

      // Add the following
      alias(libs.plugins.android.kotlin.multiplatform.library)
   }
   ```

   ### Groovy

   ```groovy
   // Module-specific build.gradle file

   plugins {
      alias(libs.plugins.kotlin.multiplatform)

      // Add the following
      alias(libs.plugins.android.kotlin.multiplatform.library)
   }
   ```
4. **Configure Android KMP target.** Configure the Kotlin Multiplatform block
   (`kotlin`) to define the Android target. Within the `kotlin` block, specify
   the Android target using `androidLibrary`:

   ### Kotlin

   ```kotlin
   kotlin {
      androidLibrary {
          namespace = "com.example.kmpfirstlib"
          compileSdk = 33
          minSdk = 24

          withJava() // enable java compilation support
          withHostTestBuilder {}.configure {}
          withDeviceTestBuilder {
              sourceSetTreeName = "test"
          }

          compilerOptions.configure {
              jvmTarget.set(
                  org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_1_8
              )
          }
      }

      sourceSets {
          androidMain {
              dependencies {
                  // Add Android-specific dependencies here
              }
          }
          getByName("androidHostTest") {
              dependencies {
              }
          }

          getByName("androidDeviceTest") {
              dependencies {
              }
          }
      }
      // ... other targets (JVM, iOS, etc.) ...
   }
   ```

   ### Groovy

   ```groovy
   kotlin {
      androidLibrary {
          namespace = "com.example.kmpfirstlib"
          compileSdk = 33
          minSdk = 24

          withJava() // enable java compilation support
          withHostTestBuilder {}.configure {}
          withDeviceTestBuilder {
              it.sourceSetTreeName = "test"
          }

          compilerOptions.options.jvmTarget.set(
              org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_1_8
          )
      }

      sourceSets {
          androidMain {
              dependencies {
              }
          }
          androidHostTest {
              dependencies {
              }
          }
          androidDeviceTest {
              dependencies {
              }
          }
      }
      // ... other targets (JVM, iOS, etc.) ...
   }
   ```
5. **Apply changes.** After applying the plugin and configuring the `kotlin`
   block, sync your Gradle project to apply the changes.

## Migrate from the legacy plugin

This guide helps you migrate from the legacy `com.android.library` plugin to the
`com.android.kotlin.multiplatform.library` plugin.

> [!NOTE]
> **Note:** Since Kotlin Gradle Plugin version 2.2.0-Beta2 and Android Gradle Plugin version 8.12.0-alpha04, a new configuring block exists called `android{}` alongside the `androidLibrary{}` one. The `androidLibrary{}` block is deprecated and will be removed in a future release of AGP, so migrate to the `android{}` block.

### 1. Moving Sources

The legacy plugin allowed you to use `src/main`, `src/test`,
and `src/androidTest` sourcesets,
in addition to `src/androidMain`, `src/androidHostTest`, and
`src/androidDeviceTest`. The new plugin only uses the latter source
directories, so
you will need to move sources from `src/main` to `src/androidMain`, from
`src/test` to `src/androidHostTest`, and from
`src/androidTest` to `src/androidDeviceTest`.

### 2. Declaring Dependencies

A common task is declaring dependencies for Android-specific source sets. The
new plugin requires these to be explicitly placed within the `sourceSets` block,
unlike the general `dependencies` block used previously.

### Android-KMP

The new plugin promotes a cleaner structure by grouping Android dependencies
within the `androidMain` source set. In addition to the main source set,
there are two test source sets, which are created on demand:
`androidDeviceTest` and `androidHostTest` (check the [configuring host and
device tests](https://developer.android.com/kotlin/multiplatform/plugin#configure-tests) for more information).

    // build.gradle.kts

    kotlin {
        androidLibrary {}
        //... other targets

        sourceSets {
            commonMain.dependencies {
                implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.0")
            }

            // Dependencies are now scoped to the specific Android source set
            androidMain.dependencies {
                implementation("androidx.appcompat:appcompat:1.7.0")
                implementation("com.google.android.material:material:1.11.0")
            }
        }
    }

The source sets have corresponding Kotlin
[compilations](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-configure-compilations.html) named `main`, `deviceTest`,
and `hostTest`. The source sets and compilations can be configured in the
build script like so:

    // build.gradle.kts

    kotlin {
        androidLibrary {
            compilations.getByName("deviceTest") {
                kotlinOptions.languageVersion = "2.0"
            }
        }
    }

### Legacy Plugin

With the old plugin, you could declare Android-specific dependencies in the
top-level dependencies block, which could sometimes be confusing in a
multiplatform module.

    // build.gradle.kts

    kotlin {
      androidTarget()
      //... other targets
    }

    // Dependencies for all source sets were often mixed in one block
    dependencies {
      // Common dependencies
      commonMainImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.8.0")

      // Android-specific dependencies
      implementation("androidx.appcompat:appcompat:1.7.0")
      implementation("com.google.android.material:material:1.11.0")
    }

### 3. Enabling Android Resources

Support for Android Resources (`res` folders) is not enabled by default in the
new plugin to optimize build performance. You must opt-in to use them. This
change helps ensure that projects not requiring Android-specific resources are
not burdened by the associated build overhead.

### Android-KMP

You must explicitly enable Android resource processing. The resources should
be placed in `src/androidMain/res`.

    // build.gradle.kts

    kotlin {
      androidLibrary {
        // ...
        // Enable Android resource processing
        androidResources {
          enable = true
        }
      }
    }

    // Project Structure
    // └── src
    //     └── androidMain
    //         └── res
    //             ├── values
    //             │   └── strings.xml
    //             └── drawable
    //                 └── icon.xml

### Legacy Plugin

Resource processing was enabled by default. You could immediately add a
`res` directory in `src/main` and start adding XML drawables, values, etc.

    // build.gradle.kts

    android {
        namespace = "com.example.library"
        compileSdk = 34
        // No extra configuration was needed to enable resources.
    }

    // Project Structure
    // └── src
    //     └── main
    //         └── res
    //             ├── values
    //             │   └── strings.xml
    //             └── drawable
    //                 └── icon.xml

### 4. Configuring Host and Device Tests

A significant change in the new plugin is that **Android host-side (unit) and
device-side (instrumented) tests are disabled by default**. You must explicitly
opt-in to create the test source sets and configurations, whereas the old plugin
created them automatically.

This opt-in model helps verify that your project remains lean and only includes
the build logic and source sets that you actively use.

### Android-KMP

In the new plugin, you enable and configure tests inside the
`kotlin.androidLibrary` block. This makes the setup more explicit and avoids
creating unused test components. The `androidUnitTest` source set becomes
`androidHostTest` (the test directory changes from `src/androidUnitTest` to
`src/androidHostTest`), and `androidInstrumentedTest` becomes
`androidDeviceTest` (the test directory changes from
`src/androidInstrumentedTest` to `src/androidDeviceTest`).

    // build.gradle.kts

    kotlin {
      androidLibrary {
        // ...

        // Opt-in to enable and configure host-side (unit) tests
        withHostTest {
          isIncludeAndroidResources = true
        }

        // Opt-in to enable and configure device-side (instrumented) tests
        withDeviceTest {
          instrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
          execution = "HOST"
        }
      }
    }

    // Project Structure (After Opt-in)
    // └── src
    //     ├── androidHostTest
    //     └── androidDeviceTest

### Legacy Plugin

With the `com.android.library` plugin, the `androidUnitTest` and
`androidInstrumentedTest` source sets are created by default. You
configure their behavior inside the `android` block, typically using the
`testOptions` DSL.

    // build.gradle.kts

    android {
      defaultConfig {
        // Runner was configured in defaultConfig
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
      }

      testOptions {
        // Configure unit tests (for the 'test' source set)
        unitTests.isIncludeAndroidResources = true

        // Configure device tests (for the 'androidTest' source set)
        execution = "HOST"
      }
    }

    // Project Structure (Defaults)
    // └── src
    //     ├── test
    //     └── androidTest

### 5. Enable Java source compilation

If your KMP library needs to compile Java sources for its Android target, you
must explicitly enable this functionality with the new plugin. Note that this
enables compilation for Java files located directly within your project, not for
its dependencies. The method for setting the Java and Kotlin compiler's JVM
target version also changes.

### Android-KMP

You must opt-in to Java compilation by calling `withJava()`. The JVM target
is now configured directly inside the `kotlin { androidLibrary {} }` block
for a more unified setup. Setting `jvmTarget` here applies to both Kotlin
and Java compilation for the Android target.

    // build.gradle.kts

    kotlin {
      androidLibrary {
        //  Opt-in to enable Java source compilation
        withJava()
        // Configure the JVM target for both Kotlin and Java sources
        compilerOptions {
          jvmTarget.set(org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_1_8)
        }
      }
      // ...
    }

    // Project Structure:
    // └── src
    //     └── androidMain
    //         ├── kotlin
    //         │   └── com/example/MyKotlinClass.kt
    //         └── java
    //             └── com.example/MyJavaClass.java

### Legacy Plugin

Java compilation was enabled by default. The JVM target for both Java and
Kotlin sources was set in the android block using compileOptions.

    // build.gradle.kts

    android {
      // ...
      compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
      }
    }

    kotlin {
      androidTarget {
        compilations.all {
          kotlinOptions.jvmTarget = "1.8"
        }
      }
    }

### 6. Interact with build variants using `androidComponents`

The `androidComponents` extension is still available for interacting with build
artifacts programmatically. While much of the `Variant` API remains the same,
the new `AndroidKotlinMultiplatformVariant` interface is more limited because
the plugin only produces a single variant.

Consequently, properties related to build types and product flavors are no
longer available on the variant object.

### Android-KMP

The `onVariants` block now iterates over a single variant. You can still
access common properties like `name` and `artifacts`, but not
build-type-specific ones.

    // build.gradle.kts

    androidComponents {
      onVariants { variant ->
          val artifacts = variant.artifacts
      }
    }

### Legacy Plugin

With multiple variants, you could access build-type-specific properties to
configure tasks.

    // build.gradle.kts

    androidComponents {
      onVariants(selector().withBuildType("release")) { variant ->
        // ...
      }
    }

### 7. Select variants of Android library dependencies

Your KMP library produces a single variant for Android. However, you might
depend on a standard Android library (`com.android.library`) that has multiple
variants (e.g., `free/paid` product flavors). Controlling how your project
selects a variant from that dependency is a common requirement.

### Android-KMP

The new plugin centralizes and clarifies this logic within the
`kotlin.androidLibrary.localDependencySelection` block. This makes it much
clearer which variants of external dependencies will be selected for your
single-variant KMP library.

    // build.gradle.kts
    kotlin {
      androidLibrary {
        localDependencySelection {
          // For dependencies with multiple build types, select 'debug' first, and 'release' in case 'debug' is missing
          selectBuildTypeFrom.set(listOf("debug", "release"))

          // For dependencies with a 'type' flavor dimension...
          productFlavorDimension("type") {
            // ...select the 'typeone' flavor.
            selectFrom.set(listOf("typeone"))
          }
        }
      }
    }

### Legacy Plugin

You configured dependency selection strategies inside the `buildTypes and
productFlavors` blocks. This often involved using `missingDimensionStrategy`
to provide a default flavor for a dimension that your library didn't have,
or `matchingFallbacks` within a specific flavor to define a search order.

Refer to [Resolve Matching Errors](https://developer.android.com/build/build-variants#resolve_matching_errors) for more
detailed information on the API usage.

### 8. Compose preview dependencies

Usually, we want to have specific libraries scoped to our local development
environment to prevent internal tools from leaking into the final published
artifact. This becomes a challenge with the new KMP Android plugin because it
removes the build type architecture used to separate development
dependencies from release code.

### Android-KMP

To add a dependency only for local development and testing, add the
dependency directly to the runtime classpath configuration (in the top-level
`dependencies` block) of the main Android compilation. This helps ensure the
dependency is available at runtime (for example for tools like
[Compose Preview](https://developer.android.com/develop/ui/compose/tooling/previews)) but is not part of the compile
classpath or the published API of your library.

> [!WARNING]
> **Preview:** This workaround is only available in Android Gradle plugin version 9.0.0-beta01 and higher.

    // build.gradle.kts
    dependencies {
      "androidRuntimeClasspath"(libs.androidx.compose.ui.tooling)
    }

### Legacy Plugin

Kotlin Multiplatform projects that use the `com.android.library` plugin
for the Android target should use the `debugImplementation` configuration,
which scopes the dependency to the debug build type and prevents it
from being included in the library's release variant used by the consumers.

    // build.gradle.kts
    dependencies {
      debugImplementation(libs.androidx.compose.ui.tooling)
    }

### 9. Configure the JVM target for the KMP Android target

The KMP Android plugin sets the JVM target using
`androidLibrary.compilerOptions.jvmTarget`, which applies to both Java and
Kotlin, simplifying the configuration compared to the separate
`compileOptions` and `kotlinOptions` blocks in pure Android projects.

### Android-KMP

When working with a Kotlin Multiplatform (KMP) project that includes an
Android target, you have several ways to configure the JVM target version
for both Kotlin and Java compiler. Understanding the scope and hierarchy of
these configurations is key to managing your project's bytecode
compatibility.

Here are the three primary ways to set the JVM target, ordered from
lowest to highest precedence. JVM target values that take higher precedence
apply to smaller subset of your configured targets and override values that
take lower precedence, which means that you can set different JVM versions
for different targets and compilations within targets in your project.

**Using kotlin toolchain (lowest precedence)**

The most general way to set the JVM target is by specifying the toolchain
in the `kotlin` block of your `build.gradle.kts` file. This approach sets
the target for both Kotlin and Java compilation tasks across all JVM-based
targets in your project, including Android.

    // build.gradle.kts
    kotlin {
        jvmToolchain(21)
    }

This configuration makes both `kotlinc` and `javac` target JVM 21. It's
a great way to establish a consistent baseline for your entire project.

**Using android target-level compiler options (medium precedence)**

You can specify the JVM target specifically for the Android KMP target
within the `android` block. This setting overrides the project-wide
`jvmToolchain` configuration and applies to all Android compilations.

    // build.gradle.kts
    kotlin {
        androidLibrary {
            compilerOptions {
                jvmTarget.set(JvmTarget.JVM_11)
            }
        }
    }

In this case, even if a `jvmToolchain` is set to a different version, the
Android target's Kotlin and Java code will be compiled to target JVM 11.

**Using compilation-level compiler options (highest precedence)**

For the most granular control, you can configure compiler options on a
per-compilation basis (for example on `androidMain` or `androidHostTest`
only). This is useful if a specific compilation needs to target a different
JVM version. This setting overrides both the Kotlin toolchain and the
Android target-level options.

    // build.gradle.kts
    kotlin {
        androidLibrary {
            compilations.all {
                compileTaskProvider.configure {
                    compilerOptions.jvmTarget.set(JvmTarget.JVM_11)
                }
            }
        }
    }

This configuration helps ensure that all compilations within the Android
target use JVM 11, providing fine-grained control.

### Legacy Plugin

In a KMP project using the standard Android library plugin
(`com.android.library`), the configuration is slightly different from when
you use the KMP Android plugin (but conceptually similar).

**Using kotlin toolchain**

The `kotlin.jvmToolchain()` method works identically, setting the
`sourceCompatibility` and `targetCompatibility` for Java and the
`jvmTarget` for Kotlin. We recommend using this approach.

    // build.gradle.kts
    kotlin {
        jvmToolchain(21)
    }

**compileOptions and kotlinOptions**

If you don't use Kotlin toolchain, you have to configure the JVM
targets using separate blocks for Java and Kotlin.

    // build.gradle.kts
    android {
        compileOptions {
            sourceCompatibility = JavaVersion.VERSION_11
            targetCompatibility = JavaVersion.VERSION_11
        }

        kotlinOptions {
            jvmTarget = "11"
        }
    }

### 10. Publish consumer keep rules

If your KMP library needs to ship consumer keep rules (such as ProGuard rules
for R8) for its consumers, you need to explicitly enable publishing in the new
plugin. Previously, consumer keep rules were published by default if specified.

### Android-KMP

With the new plugin, you must set
`optimization.consumerKeepRules.publish = true` and specify rule files
within the `consumerKeepRules` block to publish consumer keep rules.

    // build.gradle.kts
    kotlin {
      androidLibrary {
        optimization {
          consumerKeepRules.apply {
            publish = true
            file("consumer-proguard-rules.pro")
          }
        }
      }
    }

### Legacy Plugin

With `com.android.library`, any rules files specified with
`consumerProguardFiles` in `android.defaultConfig` are published in
the library's artifacts by default.

    // build.gradle.kts
    android {
      defaultConfig {
        consumerProguardFiles("consumer-proguard-rules.pro")
      }
    }

### 11. Publish your library to Maven

If you plan to publish your KMP library to Maven for consumption by other
projects, the process differs depending on whether you are using the new
Android-KMP plugin or the legacy plugin.

### Android-KMP

The `com.android.kotlin.multiplatform.library` plugin integrates with the
standard Kotlin Multiplatform publishing mechanisms. There are no
Android-specific steps required beyond the standard KMP library publishing
process.

To publish your library, follow JetBrains' official documentation:
[Set up publishing for a multiplatform library](https://kotlinlang.org/docs/multiplatform/multiplatform-publish-lib-setup.html).

### Legacy Plugin

When using `com.android.library` for the Android target in a KMP project,
you need to follow the standard Android library publishing guide to
prepare and publish the Android-specific artifact (`.aar`).

For detailed instructions, see
[Prepare your library for release](https://developer.android.com/build/publish-library/prep-lib-release).

## Plugin API reference

The new plugin has a different API surface than `com.android.library`. For
detailed information on the new DSL and interfaces, see the API references:

- [`KotlinMultiplatformAndroidLibraryExtension`](https://developer.android.com/reference/tools/gradle-api/8.11/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryExtension)
- [`KotlinMultiplatformAndroidLibraryTarget`](https://developer.android.com/reference/tools/gradle-api/8.11/com/android/build/api/dsl/KotlinMultiplatformAndroidLibraryTarget)
- [`KotlinMultiplatformAndroidDeviceTest`](https://developer.android.com/reference/tools/gradle-api/8.11/com/android/build/api/dsl/KotlinMultiplatformAndroidDeviceTest)
- [`KotlinMultiplatformAndroidHostTest`](https://developer.android.com/reference/tools/gradle-api/8.11/com/android/build/api/dsl/KotlinMultiplatformAndroidHostTest)
- [`KotlinMultiplatformAndroidVariant`](https://developer.android.com/reference/tools/gradle-api/8.11/com/android/build/api/variant/KotlinMultiplatformAndroidVariant)

## Known issues in Android-KMP library plugin

These are the known issues that might occur when you apply the new
`com.android.kotlin.multiplatform.library` plugin:

- [Compose preview fails when using new android-KMP plugin](https://issuetracker.google.com/issues/422373442)

  - Fixed in `Android Studio Otter 2 Feature Drop | 2025.2.2 Canary 3` and `Android Gradle Plugin 9.0.0-alpha13`
- [NullPointerException in Compose Multiplatform previews with
  `com.android.kotlin.multiplatform.library` plugin](https://issuetracker.google.com/issues/449677824)

  - Fixed in `Android Studio Otter 2 Feature Drop | 2025.2.2 Canary 3` and `Android Gradle Plugin 9.0.0-alpha13`
- [KMP stores common compilation dependency resolution in Configuration cache
  leading to error when deserializing (Android only)](https://youtrack.jetbrains.com/issue/KT-81060)

  - Fixed in `Kotlin Gradle Plugin 2.3.0-Beta2`
- [Support instrumented sourceSetTree for androidLibrary target](https://youtrack.jetbrains.com/issue/KT-72628)

  - Fixed in `Android Studio Otter 2 Feature Drop | 2025.2.2 Canary 3` and `Android Gradle Plugin 9.0.0-alpha13`

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Set up your environment](https://developer.android.com/kotlin/multiplatform/setup)
- [Add KMP module to a project](https://developer.android.com/kotlin/multiplatform/migrate)