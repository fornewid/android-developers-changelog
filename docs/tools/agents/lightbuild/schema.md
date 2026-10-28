---
title: https://developer.android.com/tools/agents/lightbuild/schema
url: https://developer.android.com/tools/agents/lightbuild/schema
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

A Lightbuild project's build configuration consists of YAML files: a
`project.lightbuild.yaml` file in the project's root directory, and a
`lightbuild.yaml` file in each module. This page describes the settings in each
file.

## Project file

Global project settings live in the `project.lightbuild.yaml` file in your
project's root directory. For example:

    project:
      name: MyApp

    modules:
      - app
      - app-core

    repositories:
      - google
      - mavenCentral

    lightbuild:
      version: 0.0.30

    build:
      java:
        version: 17
      kotlin:
        version: 2.3.20
      jvmTarget: "17"

The following table describes these settings:

| Setting | Description |
|---|---|
| `project.name` | The project's name, for example `MyApp`. Android Studio shows this name as the root of the **Project** window. Like `rootProject.name` in Kotlin DSL, it's separate from your app's name and application ID. |
| `modules` | The modules in the project, such as the app module (`app`) and library modules (`app-core`). |
| `repositories` | The remote repositories that Lightbuild resolves dependencies from. For details, see [Repositories](https://developer.android.com/tools/agents/lightbuild/schema#repositories). |
| `lightbuild.version` | The Lightbuild version that the project uses. |
| `build.kotlin.version` | The Kotlin version that the project uses. |
| `build.java.version` | The Java compiler version that the project requires. |
| `build.jvmTarget` | The target version of the generated JVM bytecode. |

### Repositories

Use `repositories` to list the repositories that Lightbuild resolves
dependencies from. You can list the built-in `google` and `mavenCentral`
repositories, and add custom Maven repositories with `maven`:

    repositories:
      - google
      - mavenCentral
      - maven:
          name: "Example Repo"
          url: "https://maven.example.com/releases"

A `maven` repository has the following settings:

| Setting | Description |
|---|---|
| `name` | A name for the repository. |
| `url` | The repository's URL. |
| `credentials` | Optional. The keys that map to the repository's username and password in your `local.properties` file. For details, see [Repository credentials](https://developer.android.com/tools/agents/lightbuild/schema#credentials). |

### Repository credentials

If a Maven repository requires a username and password, add a `credentials`
block to the repository. The `username` and `password` values aren't the
credentials themselves; they're keys that you define in your project's
`local.properties` file:

    repositories:

      - google
      - mavenCentral
      - maven:
          name: "Internal Repo"
          url: "https://maven.example.com/releases"
          credentials:
            username: internalRepoUser
            password: internalRepoPassword

Then, in your project's `local.properties` file, map each key to its value.
Replace `REPO_USERNAME` and `REPO_PASSWORD` with your credentials:

    # Also define sdk.dir, the path to your Android SDK.
    internalRepoUser=REPO_USERNAME
    internalRepoPassword=REPO_PASSWORD

> [!CAUTION]
> **Caution:** Don't add your `local.properties` file to version control, because it contains sensitive credentials.

## Module files

Each module has a `lightbuild.yaml` file in its directory that defines the
module's settings. The following table describes the top-level settings:

| Setting | Description |
|---|---|
| `platform` | The platform that the module targets: `android`. |
| `type` | The module type: `application` for an app module, or `library` for a library module. For more information, see [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure). |
| `optionalFeatures` | Optional features to enable for the module, such as `com.android.tools.lightbuild.protobuf` for Protocol Buffers support. For details, see [Protocol Buffers](https://developer.android.com/tools/agents/lightbuild/schema#protobuf). |
| `android` | The module's Android settings. For details, see [Android settings](https://developer.android.com/tools/agents/lightbuild/schema#android-settings). |

### Android settings

The `android` block contains the module's Android build settings:

| Setting | Description |
|---|---|
| `namespace` | The module's namespace. For more information, see [Set the namespace](https://developer.android.com/build/configure-app-module#set-namespace). |
| `compileSdk` | The API level that the module compiles against. For details, see [SDK versions](https://developer.android.com/tools/agents/lightbuild/schema#sdk-versions). |
| `minSdk` | The minimum API level that the module supports. |
| `targetSdk` | The API level that the app targets. Supported only in app modules. |
| `applicationId` | The app's application ID. Set in app modules. |
| `versionCode` | The app's version code. Set in app modules. |
| `versionName` | The app's version name. Set in app modules. |
| `packaging` | Settings for packaging the app's `debug` and `release` builds, such as release signing. Supported only in the app module. For details, see [Packaging](https://developer.android.com/tools/agents/lightbuild/schema#packaging). |
| `dependencies` | The module's dependencies on other modules and on external libraries. For details, see [Dependencies](https://developer.android.com/tools/agents/lightbuild/schema#dependencies). |
| `kspProcessors` | The KSP processors that generate code for the module. For details, see [KSP processors](https://developer.android.com/tools/agents/lightbuild/schema#ksp-processors). |
| `tests` | The module's local and instrumented tests. For details, see [Tests](https://developer.android.com/tools/agents/lightbuild/schema#tests). |

### SDK versions

Specify the `compileSdk`, `minSdk`, and `targetSdk` settings as API levels under
`version.release.apiLevel`. For example, the following settings compile the
module against API level 36, support API level 24 and higher, and target API
level 36:

    android:
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

Only app modules support the `targetSdk` setting. Library modules define only
the `compileSdk` and `minSdk` settings.

### Dependencies

Declare a module's dependencies in the `dependencies` block:

- `module`: Other modules in your project, written as `//` followed by the module's name, for example `//app-core` or `//features/search`.
- `maven`: External libraries, written as Maven coordinates in the format `group:artifact:version`.

For example, the following settings add dependencies on the `app-core` module
and on the AndroidX Core KTX library:

    android:
      dependencies:
        module:
          - //app-core
        maven:
          - androidx.core:core-ktx:1.18.0

### Dependency settings

By default, a module compiles against each of its dependencies and includes them
at runtime, but doesn't expose them to the modules that depend on it. To change
how a module uses a dependency, add a colon after the dependency, and then add
the `compile` setting, the `runtime` setting, or both below it:

    android:
      dependencies:
        module:
          - //data:
              compile: public
        maven:
          - androidx.core:core-ktx:1.18.0
          - androidx.annotation:annotation:1.9.1:
              runtime: off

In this example, modules that depend on this module can also use the `data`
module's classes. The Jetpack Annotation library is used only to compile this
module. Core KTX uses the default settings.

The `compile` setting controls which modules compile against the dependency:

- `private` (default): This module compiles against the dependency, but the modules that depend on this module don't.
- `public`: This module and the modules that depend on it compile against the dependency. Use `public` when your module's public API uses types from the dependency.
- `off`: This module doesn't compile against the dependency.

The `runtime` setting controls whether the dependency is available at runtime:

- `public` (default): The dependency is available at runtime, to this module and to the modules that depend on it.
- `off`: The dependency isn't available at runtime. Use `off` for dependencies that your code needs only at compile time, such as annotations.

`compile` and `runtime` can't both be `off`. In test dependencies, `compile` can
be only `private` or `off`.

To see how these settings correspond to Kotlin DSL configurations such as `api`
and `compileOnly`, see
[Compare Lightbuild with Kotlin DSL](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#dependencies).

### KSP processors

To use a code generator that's based on
[Kotlin Symbol Processing (KSP)](https://kotlinlang.org/docs/ksp-overview.html), such as Moshi or Room, add
the processor to the `kspProcessors` block, and add the libraries that your code
uses at runtime to the `dependencies` block. Lightbuild automatically applies
the KSP plugin and configures code generation during the build.

For example, the following settings configure Moshi with its KSP code generator:

    android:
      dependencies:
        maven:
          - com.squareup.moshi:moshi:1.15.2
          - com.squareup.moshi:moshi-kotlin:1.15.2
      kspProcessors:
        maven:
          - com.squareup.moshi:moshi-kotlin-codegen:1.15.2

> [!NOTE]
> **Note:** The `kspProcessors` block supports only external Maven dependencies. Local module dependencies aren't supported for KSP processors.

### Protocol Buffers

To generate code from [Protocol Buffers](https://protobuf.dev/) (`.proto`) files in a
library module, add the Protocol Buffers feature to the module's
`optionalFeatures` list, and add the Protocol Buffers runtime libraries to the
module's dependencies. `optionalFeatures` is a top-level setting, outside the
`android` block:

    optionalFeatures:
      - com.android.tools.lightbuild.protobuf

    android:
      dependencies:
        maven:
          - com.google.protobuf:protobuf-javalite:4.28.2
          - com.google.protobuf:protobuf-kotlin-lite:4.28.2

Put the module's `.proto` files in its `src/main/proto` directory. When you
build the module, Lightbuild generates Java and Kotlin classes for the Protocol
Buffers lite runtime, which is recommended for Android.

### Tests

Configure a module's tests in the `tests` block:

- `test`: [Local tests](https://developer.android.com/training/testing/local-tests) that run on your development machine's JVM. List the tests' dependencies under `dependencies`.
- `androidTest`: [Instrumented tests](https://developer.android.com/training/testing/instrumented-tests) that run on a device or emulator. Set `runner` to the test runner class, and list the tests' dependencies under `dependencies`.

For example:

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

### Packaging

In app modules, use the `packaging` block to configure the app's `debug` and
`release` builds. To sign your release build with your own key, add a `signing`
block to the `release` profile:

    android:
      packaging:
        release:
          signing:
            storeFile: "${RELEASE_STORE_FILE}"
            storePassword: "${RELEASE_STORE_PASSWORD}"
            keyAlias: "${RELEASE_KEY_ALIAS}"
            keyPassword: "${RELEASE_KEY_PASSWORD}"

The `signing` block supports the following settings:

- `storeFile`: The path to the keystore file, either relative to the module's directory or starting with `~/` for a location in your home directory.
- `storePassword`: The keystore's password.
- `keyAlias`: The alias of the signing key in the keystore.
- `keyPassword`: The signing key's password.

To keep your passwords out of your project's files, set these values to
environment variable references with the `${NAME}` syntax, as in the example.
You can write `storeFile` and `keyAlias` directly, or reference environment
variables for them too. When you build, Lightbuild replaces each reference with
the value of the environment variable. Each value must contain only the
reference: Lightbuild doesn't replace a reference that's part of a longer value,
such as `${HOME}/upload-keystore.jks`.

> [!IMPORTANT]
> **Important:** To prevent sensitive information from being exposed, don't write passwords directly in your `lightbuild.yaml` files or check your keystore into version control.

> [!WARNING]
> **Warning:** If an environment variable that a `signing` block references isn't set, all builds of the app module fail, including debug builds.

For more information about creating an upload key and publishing your app, see
[Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish).

## Examples

The following examples show complete module files for an app module and a
library module.

### App module

The following `app/lightbuild.yaml` file configures an app module that depends
on the `app-core` library module:

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
      dependencies:
        module:
          - //app-core

### Library module

The following `app-core/lightbuild.yaml` file configures a library module that
uses Jetpack Compose and Moshi and contains local and instrumented tests:

    platform: android
    type: library
    android:
      namespace: com.example.myapp
      compileSdk:
        version:
          release:
            apiLevel: 36
      minSdk:
        version:
          release:
            apiLevel: 24
      dependencies:
        maven:
          - androidx.core:core-ktx:1.18.0
          - androidx.lifecycle:lifecycle-runtime-ktx:2.10.0
          - androidx.activity:activity-compose:1.13.0
          - androidx.lifecycle:lifecycle-runtime-compose:2.10.0
          - androidx.lifecycle:lifecycle-viewmodel-compose:2.10.0
          - androidx.compose.ui:ui:1.10.4
          - androidx.compose.ui:ui-tooling-preview:1.10.4
          - androidx.compose.material3:material3:1.4.0
          - androidx.navigation3:navigation3-ui:1.0.1
          - androidx.navigation3:navigation3-runtime:1.0.1
          - androidx.lifecycle:lifecycle-viewmodel-navigation3:2.10.0
          - androidx.compose.ui:ui-tooling:1.10.4
          - androidx.compose.ui:ui-test-manifest:1.10.4
          - com.squareup.moshi:moshi:1.15.2
          - com.squareup.moshi:moshi-kotlin:1.15.2
      kspProcessors:
        maven:
          - com.squareup.moshi:moshi-kotlin-codegen:1.15.2
      tests:
        test:
          dependencies:
            maven:
              - junit:junit:4.13.2
              - org.jetbrains.kotlinx:kotlinx-coroutines-test:1.10.2
        androidTest:
          runner: androidx.test.runner.AndroidJUnitRunner
          dependencies:
            maven:
              - androidx.test:core:1.7.0
              - androidx.test.ext:junit:1.3.0
              - androidx.test:runner:1.7.0
              - androidx.test.espresso:espresso-core:3.7.0
              - androidx.compose.ui:ui-test-junit4:1.10.4

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure)
- [Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands)
- [Compare Lightbuild with Kotlin DSL](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison)
- [Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish)