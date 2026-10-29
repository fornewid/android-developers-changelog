---
title: https://developer.android.com/tools/agents/lightbuild/setup
url: https://developer.android.com/tools/agents/lightbuild/setup
source: md.txt
---

> [!WARNING]
> **Experimental:** Lightbuild is an experimental preview. Its design is still evolving, and it doesn't yet support all Android build features. For production apps, existing projects, or ambitious new apps, continue using Kotlin DSL. The Lightbuild preview is best suited for small apps, prototypes, and demos. For details about what it supports, see the [Kotlin DSL comparison](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison#module-type) and the [release notes](https://developer.android.com/tools/agents/lightbuild/release-notes).

This page shows you how to set up your environment for Lightbuild, create a
Lightbuild project, and then build and test it.

## Set up your environment

Lightbuild works in Android Studio and from the command line. For the best
experience, we recommend you set up both:

- **Android Studio Canary** : To work with Lightbuild projects in an IDE, install the latest [Canary version of Android Studio](https://developer.android.com/studio/preview). Stable versions of Android Studio don't support Lightbuild projects. You can [install a Canary version alongside your stable version](https://developer.android.com/studio/preview/install-preview).
- **Lightbuild CLI** : To build and test Lightbuild projects from the command line, or to have AI agents work on them, install the Lightbuild CLI. First, [install Android CLI](https://developer.android.com/tools/agents), or update it to the latest version with [`android update`](https://developer.android.com/tools/agents/android-cli/commands/update). Then, follow the steps in [Install the Lightbuild CLI](https://developer.android.com/tools/agents/lightbuild/commands#install-lightbuild-cli).

For recommendations about which tool to use for each task, see
[Ways to use Lightbuild](https://developer.android.com/tools/agents/lightbuild#ways-to-use).

## Create a project

You can create a Lightbuild project in Android Studio or with Android CLI.

### Create a project in Android Studio Canary

To create a Lightbuild project in Android Studio Canary, follow these steps:

1. In the Canary version of Android Studio, click **New Project** on the Android Studio Welcome screen, or select **File \> New \> New Project** from the main menu.
2. Select a template that's compatible with Lightbuild, such as **Empty
   Activity** or **Navigation UI Activity** , and click **Next**.
3. In the **Build configuration language** list, select **Lightbuild**.
4. Configure the rest of your project's settings, and click **Finish**.

To have AI generate your project instead, follow the steps in
[Create a new project with AI](https://developer.android.com/studio/gemini/create-a-new-project-with-ai), and select
**Lightbuild** as the build configuration language on the final configuration
screen before clicking **Finish**.

After Android Studio creates your project, you can build, run, test, and debug
it as you would any other project.

### Create a project with Android CLI

To create a Lightbuild project with Android CLI, run
[`android create`](https://developer.android.com/tools/agents/android-cli/commands/create) with the Lightbuild template name, your app's
name, and an output directory to create:

    android create empty-activity-lightbuild --name="Lightbuild Demo" --output=lightbuild-demo

## Build, run, and test your app

To build, run, and test your project from the command line, run the following
commands from your project's root directory.

To build the `app` module, run:

    lightbuild build app

To run the app on a connected device or a running emulator, use the
[`android run`](https://developer.android.com/tools/agents/android-cli/commands/run) command in Android CLI:

    android run --apks=app/build/app-debug.apk

> [!NOTE]
> **Note:** To learn what else you can do with Android CLI after you build your app, such as start an emulator, capture screenshots, and inspect your app's UI, see [Android CLI](https://developer.android.com/tools/agents/android-cli).

To run all tests in the `app-core` module, run:

    lightbuild test app-core

For more information, see [Build from the command line](https://developer.android.com/tools/agents/lightbuild/commands).

## Next steps

- Learn how a Lightbuild project is organized in [Lightbuild project structure](https://developer.android.com/tools/agents/lightbuild/structure).
- Learn about the settings in each build file in the [Lightbuild configuration reference](https://developer.android.com/tools/agents/lightbuild/schema).
- Learn how to sign your app and publish it on Google Play in [Publish your Lightbuild app](https://developer.android.com/tools/agents/lightbuild/publish).
- If you're familiar with Kotlin DSL, see how Kotlin DSL configuration maps to Lightbuild in [Compare Lightbuild with Kotlin DSL](https://developer.android.com/tools/agents/lightbuild/kotlin-dsl-comparison).