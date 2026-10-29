---
title: https://developer.android.com/tools/agents/lightbuild/structure
url: https://developer.android.com/tools/agents/lightbuild/structure
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

A Lightbuild project separates app assembly from app code: an app module (or
"app shell") assembles your app, and library modules contain your app's
features, UI, and business logic. This page describes the layout of a new
Lightbuild project and the role of each module and build file.

## Project layout

The default Lightbuild project template has the following build files and
modules:

    MyApp/
    ├── project.lightbuild.yaml  # Project-wide settings
    ├── app/                     # App module
    │   ├── lightbuild.yaml
    │   └── resolved.deps
    └── app-core/                # Library module
        ├── lightbuild.yaml
        ├── resolved.deps
        └── src/                 # The app's source code

The project has three build config files: a `project.lightbuild.yaml` file in
the root directory, and a `lightbuild.yaml` file in each module. Each module
also has a `resolved.deps` file. For details about the settings in each config
file, see the [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema).

## App module

Lightbuild projects use an app module as the basis for your app. It's also
referred to as an "app shell" because it handles project assembly without
containing any source code. All your features and logic stay in separate library
modules, and the app shell focuses on final configuration, such as signing and
optimization.

The app module's `lightbuild.yaml` file sets the module's `type` to
`application` and specifies how the final app is put together, including the
following:

- The app's identity: its application ID, version code, and version name
- The app's SDK requirements: its `compileSdk`, `minSdk`, and `targetSdk` versions
- The modules that the app depends on, in this example `app-core`

## Library modules

Library modules contain the code that the app module assembles, such as your
app's features, UI components, and business logic. In the new project template,
the `app-core` library module contains the `MainActivity.kt` file with example
code.

A library module's `lightbuild.yaml` file sets the module's `type` value to
`library`. Library modules define their `compileSdk` and `minSdk` versions, but
they don't support the `targetSdk` setting. A library module's `lightbuild.yaml`
file also declares the module's dependencies, KSP processors, and tests.

> [!NOTE]
> **Note:** To add a module, create a directory for it that contains a `lightbuild.yaml` file, and add the module's name to the `modules` list in `project.lightbuild.yaml`.

## Multiple app modules

A project can have more than one app module. Lightbuild doesn't support product
flavors and custom build types in the traditional sense. Instead, you create a
separate app module for each version of your app, such as `dev` and `prod`
versions, or `free` and `paid` versions.

Each app module depends on the library modules that its version needs. App
modules can share library modules, depend on different library modules for
version-specific code and settings (such as separate dependency injection (DI)
modules), and leave out library modules for features that a version doesn't
include.

For example, a project with free and paid versions of an app might have the
following modules:

    MyApp/
    ├── project.lightbuild.yaml
    ├── app-free/   # App module for the free version
    ├── app-paid/   # App module for the paid version
    ├── core/       # Library module that both versions use
    ├── di-free/    # DI module for the free version
    ├── di-paid/    # DI module for the paid version
    └── premium/    # Library module for paid-only features

The paid version's `app-paid/lightbuild.yaml` file depends on all the paid
version's modules:

    android:
      applicationId: com.example.myapp.paid
      dependencies:
        module:
          - //core
          - //di-paid
          - //premium

The free version's `app-free/lightbuild.yaml` file depends on the shared `core`
module and its own DI module, and leaves out the `premium` module:

    android:
      applicationId: com.example.myapp.free
      dependencies:
        module:
          - //core
          - //di-free

Each app module has its own settings, such as its application ID and release
signing, so you can build, install, and publish each version separately. To
build a specific version, specify its app module when running the `build`
command. For example:

    lightbuild build app-free

## Resolved dependencies

Each module in a Lightbuild project includes a `resolved.deps` file, which
records all the module's resolved dependencies, including transitive
dependencies. Lightbuild generates this file automatically, so that it doesn't
need to resolve dependencies dynamically every time you open or build your
project. You shouldn't edit this file by hand.

Check in your `resolved.deps` files to version control, along with your
project's `lightbuild.yaml` files.

To lock your dependencies, for example in a CI build, add the
`--locked-dependencies` flag to `lightbuild resolve` or `lightbuild test`. With
this flag, the command fails if a `resolved.deps` file doesn't match the
module's dependencies, instead of updating the file:

    lightbuild resolve --locked-dependencies

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema)
- [Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands)
- [Compare Lightbuild with Kotlin DSL](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison)