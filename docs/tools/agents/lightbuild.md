---
title: https://developer.android.com/tools/agents/lightbuild
url: https://developer.android.com/tools/agents/lightbuild
source: md.txt
---

Lightbuild is a brand-new, entirely declarative build experience aimed at
streamlining tasks in Android Studio and empowering agentic developer workflows
through Android CLI. We designed Lightbuild to be easier to use and understand,
naming it for the way it brings clarity to your project's build configuration.
Lightbuild is available to a select group of trusted testers to gather feedback
before a broader release.

## What is Lightbuild?

When creating a new project, you typically choose between Android's two
officially supported build configuration languages, Kotlin DSL (recommended) and
Groovy DSL. Once it's released to the general public, there will be a third
option: Lightbuild.

Lightbuild provides a declarative abstraction on top of imperative build
systems. This means that Lightbuild's config files don't require you to write
logic, only to declare how your project should be built. When you run your
project's build, Lightbuild converts your declarative config files to another
build system, such as Gradle. This other build system works behind the scenes to
build your project, and you only have to work with Lightbuild's config syntax.

## Benefits

By being strict about requiring declarative, YAML-based config files, Lightbuild
provides several benefits for agentic workflows and Android Studio users:

- **Agent-friendly config**: Lightbuild's YAML-based build config files are designed to enable AI agents to more efficiently parse your build config, update dependencies, and edit modules, all under your control.
- **Android CLI integration** : [Android CLI](https://developer.android.com/tools/agents/android-cli) is the primary tool for developing your apps from the command line or using your favorite agentic workflow. Lightbuild will allow you and your agents to use the same Android CLI build and test features to let you stay productive and keep your projects up to date.
- **Built into Android Studio** : Lightbuild-based projects are designed to be fully supported in Android Studio, bringing modern build capabilities directly to your development environment. If you have access, you can make a new Lightbuild-based project using a [template](https://developer.android.com/studio/projects/create-project) or by [creating a project using AI](https://developer.android.com/studio/gemini/create-a-new-project-with-ai). Lightbuild's declarative design means that you can spend less time managing AGP upgrades and waiting for projects to open and sync.

## What's next

We're prioritizing quality and stability through a focused testing program for
participants in the [Google Developer Experts](https://developers.google.com/community/experts) program before making the
new experience available to everyone to try out. Check back here for more
details on our path toward a broader public release.