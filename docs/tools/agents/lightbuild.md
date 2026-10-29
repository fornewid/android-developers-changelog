---
title: https://developer.android.com/tools/agents/lightbuild
url: https://developer.android.com/tools/agents/lightbuild
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

Lightbuild is a declarative build experience for Android projects that makes
build configuration easier for both you and your agents to read and edit. You
describe your project in YAML files, and then build it with Android Studio
Canary or Lightbuild CLI.

## How Lightbuild works

When you create a new project, you typically use Android's officially supported
and recommended build configuration language, Kotlin DSL. Lightbuild is an
experimental alternative that takes a different approach.

Lightbuild config files are declarative: instead of writing executable build
logic, you declare what your project contains and how it should be built. A
Lightbuild project uses the following files:

- `project.lightbuild.yaml`: A file in your project's root directory that defines project-wide settings, such as the project's modules, the repositories to get dependencies from, and the Lightbuild version.
- `lightbuild.yaml`: A file in each module that defines the module's type, Android settings, dependencies, and tests.
- `resolved.deps`: An auto-generated file in each module managed by Lightbuild that records resolved dependencies, avoiding the need to re-resolve them on open or build. Don't edit manually.

For more information, see [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure) and the
[Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema).

## Benefits

By using declarative, YAML-based config files, Lightbuild provides several
benefits for agentic workflows and Android Studio Canary users:

- **Agent-friendly config**: Lightbuild's YAML-based build config files and powerful command-line interface are designed to let AI agents more efficiently parse your build config, understand your project layout and outputs, update dependencies, and edit modules, all under your control.
- **Built into Android Studio**: Lightbuild projects are fully supported in Android Studio Canary. Lightbuild's declarative architecture accelerates project opens and eliminates the need to manually sync after config changes, keeping you in the flow.
- **Command-line workflows** : Build, test, and inspect Lightbuild projects from your terminal with the Lightbuild CLI, or have your AI agents do it for you. Plus, Lightbuild projects are fully compatible with [Android CLI](https://developer.android.com/tools/agents/android-cli) and its powerful suite of helpful development features.
- **Pre-resolved dependencies** : Lightbuild resolves your dependencies proactively and records them in a `resolved.deps` file for each module. By checking these files into version control, your project bypasses dynamic resolution entirely, allowing it to open and build faster.

## Ways to use Lightbuild

You can use Lightbuild with Android Studio Canary, the Lightbuild CLI, and
Android CLI, separately or together. The following table recommends a tool for
common tasks:

| What you want to do | Recommended tool |
|---|---|
| Create a Lightbuild project | Android Studio Canary or Android CLI. See [Create a project](https://developer.android.com/tools/agents/lightbuild/setup#create-project) for details. |
| Write code, and run, test, and debug your app in an IDE | Android Studio Canary |
| Build, test, and inspect your project from the command line | [Lightbuild CLI](https://developer.android.com/tools/agents/lightbuild/commands): Run `lightbuild build` and `lightbuild test`. To inspect your project's structure and outputs, run `lightbuild query`. |
| Have an AI agent build, test, and edit your project | Your preferred coding agent, with the Lightbuild CLI for building your project and analyzing its structure and Android CLI for interacting with devices and emulators. Lightbuild new project templates include an `AGENTS.md` file that tells agents how to use it. |

You install the Lightbuild CLI with Android CLI. To set up your environment and
create your first project, see [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup).

## Report issues

If you find a bug or have feedback about Lightbuild,
[file an issue](https://goo.gle/lightbuild-feedback) in the Google Issue Tracker.

## Recommended for you

- Note: link text is displayed when JavaScript is off
- [Get started with Lightbuild](https://developer.android.com/tools/agents/lightbuild/setup)
- [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure)
- [Compare Lightbuild with Kotlin DSL](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison)