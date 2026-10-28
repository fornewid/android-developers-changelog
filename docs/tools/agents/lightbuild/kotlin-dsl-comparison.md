---
title: https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison
url: https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

If you're familiar with configuring Android builds with Kotlin DSL, this page
shows how common Kotlin DSL configurations map to Lightbuild.

The examples on this page use Kotlin DSL and Android Gradle plugin (AGP) 9.0 or
higher, which includes [built-in Kotlin support](https://developer.android.com/build/migrate-to-built-in-kotlin).

## Build files

The following table shows the Lightbuild equivalent of each Kotlin DSL build
file:

| Kotlin DSL | Lightbuild | Purpose |
|---|---|---|
| `settings.gradle.kts` | `project.lightbuild.yaml` | Project name, modules, and repositories |
| Root `build.gradle.kts` and `gradle-wrapper.properties` | `project.lightbuild.yaml` | Build tool and toolchain versions |
| Module `build.gradle.kts` | Module `lightbuild.yaml` | Module type, Android settings, dependencies, and tests |
| `gradle.lockfile` | `resolved.deps` | Track dependency versions |

## Project settings

In Kotlin DSL, the `settings.gradle.kts` file defines the project's name, its
modules, and the repositories to resolve dependencies from:

    dependencyResolutionManagement {
        repositories {
            google()
            mavenCentral()
        }
    }

    rootProject.name = "MyApp"
    include(":app")
    include(":app-core")

In Lightbuild, the `project.lightbuild.yaml` file defines the same settings:

    project:
      name: MyApp
    modules:
      - app
      - app-core
    repositories:
      - google
      - mavenCentral

The following table compares project-wide settings:

| Concept | Kotlin DSL | Lightbuild |
|---|---|---|
| Project name | `rootProject.name` | `project.name` |
| Modules | `include(":app")` | `modules` |
| Repositories | `repositories` in `dependencyResolutionManagement` | `repositories` |
| Custom Maven repository | `maven { url = uri("https://maven.example.com/releases") }` | `maven` with `name` and `url` |
| Repository credentials | `credentials` in the `maven` block | `credentials` with keys that you define in `local.properties` |
| Build tool version | Gradle version in `gradle-wrapper.properties`, and AGP version in the `plugins` block | `lightbuild.version` |
| Kotlin version | Built into AGP. To use a newer version, add `kotlin-gradle-plugin` to the `buildscript` classpath. | `build.kotlin.version` |
| Java version | `kotlin { jvmToolchain(17) }` | `build.java.version` |

## Module type and plugins

In Kotlin DSL, you choose a module's type by applying a plugin, and you apply
other plugins to add features such as KSP. In Lightbuild, you set the module's
`type`, and Lightbuild applies the features that your configuration needs:

| Concept | Kotlin DSL | Lightbuild |
|---|---|---|
| App module | `id("com.android.application")` | `type: application` |
| Library module | `id("com.android.library")` | `type: library` |
| Kotlin Multiplatform (KMP) module | `id("org.jetbrains.kotlin.multiplatform")` | Not yet supported |
| Kotlin | Built into AGP 9.0 and higher | Built in |
| KSP | `id("com.google.devtools.ksp")` | Applied automatically when you declare `kspProcessors` |
| Protocol Buffers | `id("com.google.protobuf")` | `com.android.tools.lightbuild.protobuf` in `optionalFeatures` |
| Version catalogs | `libs.versions.toml` file | Not yet supported |
| Other plugins | Apply the Gradle plugin | Not yet supported |

## Android settings

In Kotlin DSL, you configure Android settings in the `android` block of a
module's `build.gradle.kts` file:

    plugins {
        id("com.android.application")
    }

    android {
        namespace = "com.example.myapp.app"
        compileSdk = 36

        defaultConfig {
            applicationId = "com.example.myapp"
            minSdk = 24
            targetSdk = 36
            versionCode = 1
            versionName = "1.0"
        }
    }

In Lightbuild, you configure the same settings in the `android` block of a
module's `lightbuild.yaml` file:

    platform: android
    type: application
    android:
      namespace: com.example.myapp.app
      compileSdk:
        version:
          release:
            apiLevel: 36
      minSdk:
        version:
          release:
            apiLevel: 24
      targetSdk:
        version:
          release:
            apiLevel: 36
      applicationId: com.example.myapp
      versionCode: 1
      versionName: "1.0"

The following table compares these settings:

| Setting | Kotlin DSL | Lightbuild |
|---|---|---|
| Namespace | `namespace` | `namespace` |
| Compile SDK | `compileSdk = 36` | `compileSdk.version.release.apiLevel: 36` |
| Minimum SDK | `minSdk = 24` in `defaultConfig` | `minSdk.version.release.apiLevel: 24` |
| Target SDK | `targetSdk = 36` in `defaultConfig` | `targetSdk.version.release.apiLevel: 36` |
| Application ID | `applicationId` in `defaultConfig` | `applicationId` |
| Version code | `versionCode` in `defaultConfig` | `versionCode` |
| Version name | `versionName` in `defaultConfig` | `versionName` |
| Release signing | `signingConfigs`, and `signingConfig` in the `release` build type | `packaging.release.signing`. For more information, see [Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish). |

## Dependencies

In Kotlin DSL, you declare dependencies in the `dependencies` block, using
configurations such as `implementation`:

    dependencies {
        implementation(project(":app-core"))
        implementation("androidx.core:core-ktx:1.18.0")
    }

In Lightbuild, you list module dependencies under `module`, and external
libraries under `maven`:

    android:
      dependencies:
        module:
          - //app-core
        maven:
          - androidx.core:core-ktx:1.18.0

Kotlin DSL uses other configurations, such as `api`, `compileOnly`, and
`runtimeOnly`, to control how a module uses a dependency:

    dependencies {
        api(project(":data"))
        compileOnly("androidx.annotation:annotation:1.9.1")
    }

In Lightbuild, you add `compile` and `runtime` settings to the dependency
instead:

    android:
      dependencies:
        module:
          - //data:
              compile: public
        maven:
          - androidx.annotation:annotation:1.9.1:
              runtime: off

For more information about these settings, see
[Dependency settings](https://developer.android.com/tools/agents/lightbuild/schema#dependency-settings).

The following table compares common dependency declarations:

| Dependency | Kotlin DSL | Lightbuild |
|---|---|---|
| Module in your project | `implementation(project(":app-core"))` | `//app-core` in `android.dependencies.module` |
| External library | `implementation("group:artifact:version")` | `group:artifact:version` in `android.dependencies.maven` |
| API dependency | `api("group:artifact:version")` | `group:artifact:version` in `android.dependencies.maven`, with `compile: public` |
| Compile-only dependency | `compileOnly("group:artifact:version")` | `group:artifact:version` in `android.dependencies.maven`, with `runtime: off` |
| Runtime-only dependency | `runtimeOnly("group:artifact:version")` | `group:artifact:version` in `android.dependencies.maven`, with `compile: off` |
| KSP processor | `ksp("group:artifact:version")` | `group:artifact:version` in `android.kspProcessors.maven` |
| Local test dependency | `testImplementation("group:artifact:version")` | `group:artifact:version` in `android.tests.test.dependencies.maven` |
| Instrumented test dependency | `androidTestImplementation("group:artifact:version")` | `group:artifact:version` in `android.tests.androidTest.dependencies.maven` |

## KSP

In Kotlin DSL, you apply the KSP plugin and add processors with the `ksp`
configuration:

    plugins {
        id("com.android.library")
        id("com.google.devtools.ksp")
    }

    dependencies {
        implementation("com.squareup.moshi:moshi:1.15.2")
        implementation("com.squareup.moshi:moshi-kotlin:1.15.2")
        ksp("com.squareup.moshi:moshi-kotlin-codegen:1.15.2")
    }

In Lightbuild, you add processors to the `kspProcessors` block, and Lightbuild
applies the KSP plugin automatically:

    type: library
    android:
      dependencies:
        maven:
          - com.squareup.moshi:moshi:1.15.2
          - com.squareup.moshi:moshi-kotlin:1.15.2
      kspProcessors:
        maven:
          - com.squareup.moshi:moshi-kotlin-codegen:1.15.2

## Tests

In Kotlin DSL, you set the instrumentation test runner in `defaultConfig`, and
you add test dependencies with the `testImplementation` and
`androidTestImplementation` configurations:

    android {
        defaultConfig {
            testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        }
    }

    dependencies {
        testImplementation("junit:junit:4.13.2")
        androidTestImplementation("androidx.test.ext:junit:1.3.0")
        androidTestImplementation("androidx.test.espresso:espresso-core:3.7.0")
    }

In Lightbuild, you configure local tests in `tests.test` and instrumented tests
in `tests.androidTest`:

    android:
      tests:
        test:
          dependencies:
            maven:
              - junit:junit:4.13.2
        androidTest:
          runner: androidx.test.runner.AndroidJUnitRunner
          dependencies:
            maven:
              - androidx.test.ext:junit:1.3.0
              - androidx.test.espresso:espresso-core:3.7.0

## Build commands

With Kotlin DSL, you build and test from the command line by running Gradle
tasks with the Gradle wrapper. With Lightbuild, you use the
[Lightbuild CLI](https://developer.android.com/tools/agents/lightbuild/commands).

| Task | Gradle wrapper | Lightbuild CLI |
|---|---|---|
| Build the app module | `./gradlew :app:assembleDebug` | `lightbuild build app` |
| Build all targets | `./gradlew assemble` | `lightbuild build` |
| Run a module's local tests | `./gradlew :app-core:test` | `lightbuild test app-core:hostTest` |
| Run a module's instrumented tests | `./gradlew :app-core:connectedAndroidTest` | `lightbuild test app-core:deviceTest` |
| Run all tests | `./gradlew test connectedAndroidTest` | `lightbuild test` |
| Remove build output and caches | `./gradlew clean` | `lightbuild clean` |

For more information, see [Build your app from the command line](https://developer.android.com/build/building-cmdline)
and [Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands).

## Dependency locking

With Kotlin DSL, [dependency locking](https://docs.gradle.org/current/userguide/dependency_locking.html) is optional:
you turn it on in your build scripts, and then write lockfiles by running a
build with the `--write-locks` flag. In Lightbuild, every module has a
`resolved.deps` file that records the module's resolved dependencies, which
Lightbuild generates automatically. As with Gradle lockfiles, check in your
`resolved.deps` files to version control.

To lock your dependencies, for example in a CI build, add the
`--locked-dependencies` flag to `lightbuild resolve` or `lightbuild test`. With
this flag, the command fails if a `resolved.deps` file doesn't match the
module's dependencies, instead of updating the file:

    lightbuild resolve --locked-dependencies

## Unsupported features

Lightbuild doesn't support the following Kotlin DSL features:

- Version catalogs and convention plugins
- Custom plugins
- Product flavors. Instead, create a separate app module for each version of your app. For more information, see [Multiple app modules](https://developer.android.com/tools/agents/lightbuild/structure#multiple-apps).
- Kotlin Multiplatform (KMP) modules
- Dependency resolution through a proxy server

In addition, a project can't mix Kotlin DSL and Lightbuild modules. For known
issues, see the [Lightbuild release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema)
- [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure)
- [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup)