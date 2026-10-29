---
title: https://developer.android.com/tools/agents/lightbuild/cli-reference
url: https://developer.android.com/tools/agents/lightbuild/cli-reference
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

The Lightbuild CLI is the official command-line tool for Lightbuild. This page
describes its commands and options. To install the Lightbuild CLI, see
[Install the Lightbuild CLI](https://developer.android.com/tools/agents/lightbuild/commands#install-lightbuild-cli). For common tasks, such as
building and testing your project, see
[Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands).

## Syntax

The Lightbuild CLI uses the following syntax:

    lightbuild [-V] [--project=path] [COMMAND]

It supports the following global options:

| Option | Description |
|---|---|
| `-V`, `--version` | Prints version information and exits. |
| `-p`, `--project=path` | The absolute path to your project. Defaults to the current directory, which must contain a project. |

To list the available commands, run [`lightbuild help`](https://developer.android.com/tools/agents/lightbuild/cli-reference#lightbuild-help). To get
help for a specific command, run `lightbuild help [command]`.

## `lightbuild build`

Builds a target in your project.

    lightbuild build [target]

| Argument | Description |
|---|---|
| `target` | The target to build. Defaults to all targets underneath the current directory. |

For example, to build the `app` module, run:

    lightbuild build app

To build all the targets in your project, run:

    lightbuild build

## `lightbuild clean`

Removes your project's build output and caches.

    lightbuild clean [target]

| Argument | Description |
|---|---|
| `target` | The target to clean. Defaults to all targets underneath the current directory. |

For example, to remove the build output and caches for your whole project, run:

    lightbuild clean

## `lightbuild help`

Lists the available commands, or shows the help for a specific command.

    lightbuild help [COMMAND]

| Argument | Description |
|---|---|
| `COMMAND` | The command to show the help for. Defaults to all commands. |

To list the commands that are available for your project, run:

    lightbuild help

To show the help for a specific command, such as `query`, run:

    lightbuild help query

## `lightbuild query`

Lists the build targets, generated output files, or source sets that match a
pattern across your project's modules.

    lightbuild query [target-pattern] [--format=format] [--output=type]

| Option or argument | Description |
|---|---|
| `target-pattern` | The target path pattern, for example `...` or `app`. |
| `--format=format` | The output format, for example `json`. Defaults to a table. |
| `--output=type` | The format of the output: `files` for the locations of the files that the matching targets produce, `sourcesets` for their source sets, or `sourceset_types` for the types of their source sets. |

To list all the targets in your project, run:

    lightbuild query ...

To print the locations of the files that the `app` target produces, run:

    lightbuild query app --output=files

## `lightbuild resolve`

Resolves your project's external dependencies and generates the offline
dependency lockfiles (`resolved.deps`) for its modules.

    lightbuild resolve [--cache=path] [--locked-dependencies] [target]

| Option or argument | Description |
|---|---|
| `target` | The module to resolve dependencies for, for example `app`. Defaults to all targets underneath the current directory. |
| `--locked-dependencies` | Exits with an error if the local dependency lockfile (`resolved.deps`) is out of sync. |
| `--cache=path` | The directory to store the dependency cache in. |

For example, to generate the `resolved.deps` files for all modules in your
project, run:

    lightbuild resolve

For more information about `resolved.deps` files, see
[Resolved dependencies](https://developer.android.com/tools/agents/lightbuild/structure#resolved-deps).

## `lightbuild test`

Runs the tests in your project: local tests, which run on your development
machine, and instrumented tests, which run on a connected device or a running
emulator. To test one module, specify its target, such as `app-core`. To run
only one type of test, add `:hostTest` for local tests or `:deviceTest` for
instrumented tests to the target.

    lightbuild test [target] [--locked-dependencies]

| Option or argument | Description |
|---|---|
| `target` | The target to test. Defaults to all the tests in your project. |
| `--locked-dependencies` | Fails the build if the local dependency lockfile (`resolved.deps`) is out of sync. |

For example, to run all the tests in your project, run:

    lightbuild test

To run the local tests in the `app-core` module, run:

    lightbuild test app-core:hostTest

To run the instrumented tests in the `app-core` module on a device or emulator,
run:

    lightbuild test app-core:deviceTest

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Build Lightbuild projects from the command line](https://developer.android.com/tools/agents/lightbuild/commands)
- [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup)
- [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema)
- [Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish)