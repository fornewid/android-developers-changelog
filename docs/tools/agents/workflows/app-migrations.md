---
title: https://developer.android.com/tools/agents/workflows/app-migrations
url: https://developer.android.com/tools/agents/workflows/app-migrations
source: md.txt
---

The New Project Wizard in Android Studio includes the Migration Assistant, which
can translate existing iOS, Flutter, and React Native projects into Kotlin and
Jetpack Compose. This guide explains how to set up, initiate, and monitor
agentic app migrations with the Migration Assistant.

## Install and set up Studio

Follow these steps to get the Migration Assistant ready for use:

1. Download the latest canary release of Android Studio from the [Android Studio
   preview](https://developer.android.com/studio/preview) page and install it. Preview releases of Android Studio don't interfere with existing stable version installations.
2. Launch Android Studio and follow the directions in [Get started with Gemini
   in Android Studio](https://developer.android.com/studio/gemini/get-started) to make sure you're signed in and Gemini in Android Studio is enabled.

> [!NOTE]
> **Note:** App migration is a long-horizon task. For best results, you should use the most powerful model you have access to. To learn more about using non-default models in Android Studio, see [Use a remote model](https://developer.android.com/studio/gemini/use-a-remote-model) and [Use a local
> model](https://developer.android.com/studio/gemini/use-a-local-model).

## Initiate a codebase migration with the New Project Wizard

The Migration Assistant transforms existing iOS, Flutter, and React Native
projects into idiomatic Kotlin and Jetpack Compose through an interactive,
multi-step agent workflow. Follow these steps to point the wizard to your
existing source repo:
![](https://developer.android.com/static/tools/agents/images/migration-assistant.png) **Figure 1**: Migration setup in the New Project Wizard.

1. Open the **New Project** window by selecting **New Project** from the Android Studio Welcome screen or by navigating to **File \> New \> New Project** from the menu bar.
2. Select **Migrate to New Project** from the left template pane in the **New
   Project** window.
3. Click **Select Folder** and browse to the location of the existing iOS, React Native, or Flutter codebase that you want to migrate to Kotlin and Jetpack Compose.
4. Select one of the following options under **Migration Strategy** :
   - **Autonomous Migration.** An automated migration process designed to run end-to-end without human intervention.
   - **Guided Migration.** A guided migration process that stops after each step to ask the developer for input on how to proceed.
5. Select one of the following options under **Validation Strategy** :
   - **Journeys for Android Studio.** The agent uses the [Journeys for Android
     Studio](https://developer.android.com/studio/gemini/journeys) feature to test critical user journeys during the migration process.
   - **Manual Validation.** The agent only runs the checks necessary to validate build stability and leaves it up to the developer to manually define and review critical user journeys.
6. Use the text field at the bottom of the window to supply additional context, such as special instructions, information about the source app, or output requirements. Use the **Attach Images** and **Attach Skills** buttons to supply images or skills to assist the agent in running the migration.
7. In the bottom-right corner of the window, select which model you want the agent to use for the migration from the list of models that you've enabled in **Settings \> Tools \> AI \> Model Providers**.
8. Click **Next** to proceed to entering standard information about the new project, such as package name and minimum SDK target.
9. Click **Finish** to begin the migration.

## Monitor a codebase migration

You can monitor the agent's progress in the **Agent** window. This window is
where you'll communicate with the agent in a guided migration to answer
questions as it plans and executes the migration.

> [!NOTE]
> **Note:** Even if you selected **Autonomous Migration**, the agent might periodically pause to ask a critical question. This is especially likely at the beginning of a migration. For best results, monitor the agent while it's running to prevent it from getting stuck.

The agent builds and tests your application throughout the migration process.
When the migration is complete, you should perform a manual review of your app's
critical user journeys. Depending on app complexity, you might need to continue
refining the resulting app to ensure that you achieve the desired results.