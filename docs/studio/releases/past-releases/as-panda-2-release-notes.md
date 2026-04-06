---
title: Android Studio Panda 2 (March 2026)  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-panda-2-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

# Android Studio Panda 2 (March 2026) Stay organized with collections Save and categorize content based on your preferences.



The following are new features in Android Studio Panda 2.

## Custom View Preview deprecation

We are deprecating the
[Custom View](/develop/ui/views/layout/custom-views/custom-components)
Preview feature in the coming releases.

As the Android ecosystem shifts toward [Jetpack Compose](/compose),
building custom UI components has become significantly more efficient and
intuitive. Compose includes a powerful,
built-in [@Preview](/develop/ui/compose/tooling/previews) system that
provides a superior workflow for developing custom UI elements
compared to the legacy XML-based approach.

By deprecating the Custom View Preview, we are able to focus our resources
on enhancing the preview experience within the Compose ecosystem while
providing a leaner, more performant IDE.

## Create a new project with AI

Use the power of generative AI to accelerate your Android development workflow.
Starting with Android Studio Panda 2, the AI agent enables you go
from idea to app prototype in minutes.

The agent is capable of generating a variety of multiscreen applications:

* **Single-screen apps:** Build basic apps with static UI layouts.
* **Multipage apps:** Create applications with basic navigation between
  screens.
* **AI-enhanced apps:** Integrate Gemini APIs to add generative AI features.
* **Apps with public API integration:** Build apps that display data from
  public APIs.

To use the project setup agent, do the following:

1. Start Android Studio.
2. Select **New Project** on the **Welcome to Android Studio** screen (or
   **File > New > New Project** from within a project).

   ![The Welcome to Android Studion screen, which has the New Project, Open, and Clone Repository buttons.](/static/studio/gemini/images/welcome_to_android_studio.png)


   Start a new project.
3. Select **Create with AI**.

   ![The 'new project' dialog, which has cards for various kinds of
            app templates, such as Empty Activity, Navigation UI Activity, and
            so forth. The dialog also has the Create with AI control, which
            activates Gemini in Android Studio to set up a new project for
            you.](/static/studio/gemini/images/new_project.png)


   Select a project template or create your app with Gemini.
4. Type your prompt into the text entry field and click **Next**.

   ![The Create with AI dialog containing the prompt: A fitness
            tracker for a phone and watch, tracking running and cycling. The
            dialog includes buttons for selecting various types of apps,
            including a fitness tracker button.](/static/studio/gemini/images/what_do_you_want_to_build.png)


   Dialog for setting up a new project.
5. Name your app and click **Finish** to start the generation process.

Based on your prompt, Gemini in Android Studio generates a structured plan for
your app. Once you approve the plan, the agent begins an autonomous generation
loop to configure and build your app.

## Update dependencies with the AI agent

Upgrading dependencies can be a complex and time-consuming task. Starting with
Android Studio Otter 1 Canary 5, the AI agent automates and simplifies the
dependency upgrade process, eliminating tedious work and improving project
maintainability. With just a few clicks, you can seamlessly upgrade all your
dependencies and get the benefits of the latest versions, so you can focus on
building high-quality apps.

![Update libraries from the version catalog.](/static/studio/gemini/images/update-all-libraries-with-gemini.png)


Update libraries from the version catalog.

To update dependencies using the AI agent, do one of the following:

* Click **Refactor** (or right-click in the editor or project view) **> Update
  dependencies**.
* In the `libs.versions.toml` file, hover over a version that is underlined,
  click the **Show Context Actions**
  ![](/static/studio/images/buttons/show-context-actions.png)
  menu that appears, and then click **Update all libraries with Gemini**.

  **Note:** You should use the
  [Android Gradle plugin (AGP) Upgrade Assistant](/build/agp-upgrade-assistant)
  to upgrade versions of AGP. You can invoke the AGP Upgrade Assistant from the
  **Show Context Actions** menu for the AGP entry in your `libs.versions.toml`
  file. We recommend you run the AGP Upgrade Assistant before asking Gemini to
  update all the other dependencies.

During the process, the agent provides a high-level overview of its upgrade plan
so you can monitor progress step by step and review all changes before applying
them. The agent iterates through the build process, resolving any build errors
that arise from the upgrades. You can review, accept, or rollback changes or
stop the agent at any point.

## Monochrome icon support in Asset Studio

Android Studio Narwhal Feature Drop 2025.1.3 Canary 2 and higher simplify
the creation of themed app icons. With Android 13 (API level 33) and higher,
users can opt for themed app icons, which adapt to the wallpaper and theme of
the user's device.

To support this feature, Android Studio integrates a new monochrome icon option
directly into the **Image Asset Studio wizard**. When you're creating an adaptive
app icon, you now see a dedicated **Monochrome** tab in addition to the existing
**Foreground** and **Background** tabs. You can either provide a separate
monochrome app icon (see the [design specs](/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons)), or allow
Android Studio to default to reusing the foreground layer of the adaptive icon
for the monochrome layer.

You can access **Image Asset Studio** through the **Resource Manager**, or by
right-clicking a project directory and navigating to **New > Image Asset**.

Select **Launcher icons (Adaptive and Legacy)** as the icon type to see the
new **Monochrome** tab.

After importing the icons,
you can [preview your themed app icons](/studio/write/create-app-icons#preview-themed-app-icons).

![](/static/studio/images/design/monochrome-icon-support.png)


Monochrome Icon Support in Asset Studio

## Layout Inspector 3D mode deprecation

In Android Studio Panda 2, we deprecated the 3D Mode feature
in the [Layout Inspector](/studio/debug/layout-inspector). While 3D Mode provided a
way to visualize deep hierarchies,
usage data indicates that the standard 2D view and Component Tree meet
the vast majority of debugging needs. By removing this feature, we can direct
our resources toward improving the overall support, performance, and stability
of the Layout Inspector. You can continue to inspect view nesting and
z-ordering using the Component Tree and the standard 2D layout view.