---
title: https://developer.android.com/studio/platform/projects
url: https://developer.android.com/studio/platform/projects
source: md.txt
---

A project in Android Studio for Platform (ASfP) contains everything that defines
your workspace for your AOSP codebase, from source code and assets to test code
and build configurations.

When you start a new project, ASfP creates the necessary structure for all your
files and makes them visible in the **Project** window. To open the window,
select
**View \> Tool Windows \> Project**.

This page provides an overview of the key components inside your project
configuration.

## Project configuration (`.asfp-project`)

The ASfP project configuration is controlled by the `.asfp-project` file,
located in the root of your project directory. This YAML file is essential for
controlling what goes into your project and how critical features operate. You
can open it through the main menu using **ASfP \> Project \> Open Config** or by
finding it in the project view.

Upon project creation, a config is constructed based on user-provided specs. All
parameters in the config can be edited at any time to modify the project specs,
for example to update project directories or modules, after which a sync is
required for changes to be reflected.

### Configuration parameters

Here are the key parameters you can configure in the `.asfp-project` file:

#### `repo`

*Required*

An absolute path to your Android platform repository root.  

    repo: /path/to/aosp

#### `lunch`

*Required*

The lunch target that will be coupled with your project. This is used for all
Soong build actions, including sync and relevant run configurations.  

    lunch: your-product-variant-userdebug

#### `directories`

*Optional*

Directories to either include in or exclude from your project. These should be
relative paths with respect to the `repo` root.  

    directories:
      include:
        -   frameworks/base
        -   packages/apps/Settings
      exclude:
        -   vendor
        -   out/soong

#### `modules`

*Optional*

Modules to either include in or exclude from your project. These work in
conjunction with the previously specified `directories`. Both full and abridged
names are supported.  

    modules:
      include:
        -   SystemUIGoogle
        -   frameworks/base/services/core/java:services
      exclude:
        -   UnusedModule

#### `test_sources`

*Optional*

ASfP attempts to differentiate between production and test sources, but in some
cases, you might need to explicitly denote test sources. Provide these as
relative paths with respect to the `repo` root. Any source roots that are
subdirectories of the specified path(s) will be marked as test.  

    test_sources:
      -   cts/tests/tests/example
      -   tests/mytests

#### `other_languages`

*Optional*

Java support is included by default. You can add support for other languages.
ASfP also supports C/C++ (`cpp`) and Rust (`rust`).  

    other_languages:
      -   cpp
      -   rust

#### `build_config`

*Optional*

This parameter lets you add custom flags or environment variables to Soong build
events. This configuration applies to all actions in the IDE that result in a
Soong build, including sync and run configurations.  

    build_config:
      flags:
        -   -j64
      env:
        SOONG_ALLOW_MISSING_DEPENDENCIES: true
        MY_CUSTOM_VAR: value