---
title: https://developer.android.com/ai-tools/guides/quickstart
url: https://developer.android.com/ai-tools/guides/quickstart
source: md.txt
---

Agent-assisted Android development spans a wide range of tools, from
browser-based app builders that generate working prototypes from a single prompt
to command-line interfaces and IDE-integrated agents built for production
engineering. Choosing the right combination of tools and agent harnesses depends
on what you want to accomplish, your general programming background, and your
familiarity with the Android platform.

Use this guide to identify the recommended developer tools and grounding
resources for your experience level and development goals. Once you select a
path, follow the recommendations in the corresponding section to accelerate your
workflow with official Android resources.

| What you want to do | Your experience level | Recommended developer tools and harnesses |
|---|---|---|
| Prototype an app idea | New to coding and new to Android | [Google AI Studio](https://aistudio.google.com/docs/aistudio-android) |
| Integrate Android into an existing CLI workflow | Experienced coder, new to Android | Your preferred coding agent (such as Claude Code or Google Antigravity) equipped with [Android CLI](https://developer.android.com/tools/agents/android-cli), [Android skills](https://developer.android.com/tools/agents/android-skills), and the [Android Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources#android-knowledge-base) |
| Build in an Android-specific IDE using your preferred agent | Experienced coder, new to Android | [Android Studio](https://developer.android.com/studio) with [Bring Your Own Agent (BYOA)](https://developer.android.com/studio/preview/features#bring-your-own-agent), [Use a remote model](https://developer.android.com/studio/gemini/use-a-remote-model), or [Create a project with AI](https://developer.android.com/studio/gemini/create-a-new-project-with-ai) |
| Migrate an existing app from another platform to Android | Experienced coder | Android Studio with the [Migration Assistant](https://developer.android.com/tools/agents/workflows/app-migrations) |
| Build, profile, and optimize a production Android app | Experienced Android developer | Android Studio |

## Prototype an app idea from scratch

If you're new to both coding and Android development, start with a builder
platform that handles code generation, UI layout, and project structure
automatically. For example, use [Google AI Studio](https://aistudio.google.com/docs/aistudio-android) to turn
natural-language prompts into a working Android prototype. Google AI Studio lets
you experiment with app concepts, iterate on layouts conversationally, and test
your prototype without installing local development tools. If you later decide
to transition into full-scale development, you can import your project into an
IDE such as Android Studio by downloading your project as a ZIP folder or
exporting it to GitHub.

If you want to start using Android Studio directly, you can [use AI to create a
new app in Android Studio](https://developer.android.com/studio/gemini/create-a-new-project-with-ai). The agent builds a
functional Jetpack Compose project from your prompt and reference images,
configuring dependencies and navigation so you can focus on learning the
codebase and iterating on features.

## Integrate Android into your existing agentic workflow

If you're an experienced software engineer who is new to Android, the optimal
setup depends on whether you prefer working in your existing terminal and code
editor or moving to Android Studio, an Android-specialized IDE.

### Add Android expertise to your workflow

If you already have an established workflow, you can stay in your preferred
environment and add Android-specific capabilities to your agent.
General-purpose models might not have access to the latest Android knowledge and
best practices, so grounding your agent is essential for reliable results:

- **Empower your agent with Android skills:** [Android skills](https://developer.android.com/tools/agents/android-skills) guide your agent to follow modern practices for Jetpack Compose, architecture, Gradle, and more.
- **Equip your agent with Android CLI:** [Android CLI](https://developer.android.com/tools/agents/android-cli) lets your agent configure the Android SDK, manage virtual devices, deploy APKs, inspect live UI hierarchies, and more. Your agent can also execute natural-language end-to-end tests headlessly using [Journeys](https://developer.android.com/tools/agents/android-cli/journeys).
- **Ground your agent with the Android Knowledge Base:** The [Android
  Knowledge Base](https://developer.android.com/studio/gemini/access-helpful-resources#android-knowledge-base) gives your agent access to fresh, authoritative documentation. Your agent can search and fetch official documentation automatically using the [`android docs`](https://developer.android.com/tools/agents/android-cli/commands/docs) command in Android CLI, but you can increase the chance that the agent will use it by specifically asking the agent to use Android documentation in your prompt.

### Use Android Studio with the agent of your choice

If you want the benefits of a dedicated Android IDE---such as visual UI
inspection, integrated emulators, and Android-specific lint diagnostics---without
giving up your existing AI subscriptions or starting a project from a blank
slate, use Android Studio with the agent of your choice. You can [connect
Android Studio with an Agent Client Protocol (ACP)-compliant agent](https://developer.android.com/studio/preview/features#bring-your-own-agent),
including Claude Agent, Codex, and Google Antigravity. Android Studio starts its
own instance of the agent through ACP, so it doesn't connect to an agent that's
already running, such as in a terminal. Your agent gets direct access to Android
Studio's project graph, build diagnostics, and emulator controls, reducing token
overhead.

## Migrate an existing app to Android

If you're an experienced developer bringing an existing app from another
platform to Android, you don't need to translate the codebase file by file or
configure a cross-platform migration pipeline from scratch. Use the [Migration
Assistant](https://developer.android.com/tools/agents/workflows/app-migrations) in Android Studio to translate your existing
repository into idiomatic Kotlin and Jetpack Compose. The Migration Assistant
supports both autonomous end-to-end migrations and guided, step-by-step
workflows that pause for your input.

## Build, profile, and optimize production Android apps

If you're an experienced Android developer working on production codebases,
[Android Studio](https://developer.android.com/studio) is the most capable environment for deep Android
engineering. While standalone terminal agents work well for isolated code
generation, production Android development requires tight integration with the
Gradle build graph, live UI rendering across form factors, and specialized
profiling tools. Android Studio still lets you use the agents and models of your
choice---you can use the built-in agent or [connect third-party agents](https://developer.android.com/studio/preview/features#bring-your-own-agent) and
[models](https://developer.android.com/studio/gemini/use-a-remote-model).

Working inside Android Studio unlocks platform-aware workflows that aren't
automatically available in general-purpose editors:

- **Design and adapt UIs across form factors:** Build and refine adaptive layouts for phones, tablets, foldables, and Wear OS by [generating Compose
  previews](https://developer.android.com/studio/gemini/generate-compose-previews) and using AI-assisted UI transformation tools.
- **Optimize performance:** Combine agentic coding with [Profile your app
  performance](https://developer.android.com/studio/profile) to inspect CPU, memory, and battery usage. When investigating bugs or production regressions, use the built-in agent to help [analyze runtime errors with Logcat](https://developer.android.com/studio/gemini/analyze-runtime-errors-with-logcat) or [analyze crashes with
  App Quality Insights](https://developer.android.com/studio/gemini/analyze-crashes-with-aqi) to correlate stack traces directly with your source code.
- **Navigate and test your app using AI:** Create and run functional tests using natural language with [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys).