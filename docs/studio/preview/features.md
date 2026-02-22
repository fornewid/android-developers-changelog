---
title: https://developer.android.com/studio/preview/features
url: https://developer.android.com/studio/preview/features
source: md.txt
---

This page lists the new features introduced in Android Studio preview releases.
The preview builds provide early access to the latest features and improvements
in Android Studio. [You can download these preview versions](https://developer.android.com/studio/preview).
If you encounter any problems using a preview version of Android Studio, [let us
know](https://developer.android.com/studio/report-bugs). Your bug reports help to make Android Studio better.

Canary releases contain leading edge features under active development, and are
lightly tested. While you can use Canary builds for development, be aware that
features might be added or changed. Release Candidates (RC) are the next version
of Android Studio, and are almost ready for stable release. The feature set for
the next version has been stabilized. See
[Android Studio release names](https://developer.android.com/studio/releases/studio-release-names) to understand Android
Studio version naming.

For the latest news on Android Studio preview releases, including a list of
notable fixes in each preview release, see the [Release
Updates](https://androidstudio.googleblog.com/) in the Android Studio blog.


## Current versions of Android Studio

The following table lists the current versions of Android Studio and their
respective channels.

| Version | Channel |
|---|---|
| Android Studio Panda 1 | Stable |
| Android Gradle plugin 9.0.0 | Stable |
| Android Studio Panda 2 | RC |
| Android Studio Panda 3 | Canary |

<br />

## Compatibility with Android Gradle plugin previews

Each preview version of Android Studio is published alongside a corresponding
version of the Android Gradle plugin (AGP). Preview versions of Studio should
work with any
[compatible](https://developer.android.com/studio/releases#android_gradle_plugin_and_android_studio_compatibility)
stable version of AGP. However, if you're using a preview version of AGP, you
must use the corresponding preview version of Studio (for example, Android
Studio Chipmunk Canary 7 with AGP 7.2.0-alpha07). Attempts to use divergent
versions (for example, Android Studio Chipmunk Beta 1 with AGP
7.2.0-alpha07) will cause a Sync failure, which results in a prompt to update to
the corresponding version of AGP.

For a detailed log of Android Gradle plugin API deprecations and removals, see
the [Android Gradle plugin API
updates](https://developer.android.com/studio/releases/gradle-plugin-api-updates).

## Studio Labs

Studio Labs lets you try out the latest AI experimental features in a stable
version of Android Studio, so you can more quickly integrate our AI assistance
offerings in your development workflow. For more information, see
[Studio Labs](https://developer.android.com/studio/gemini/labs).

> [!NOTE]
> **Note:** Studio Labs is accessible in RC and stable releases starting with Android Studio Narwhal. In the corresponding canary versions of Android Studio, the features are enabled by default.

The following are features currently available in Studio Labs.

| Feature | Description | Docs |
|---|---|---|
| Compose preview generation | Gemini can automatically generate Compose previews, including mock data for preview parameters, for a specific composable or all composables in a file. | [Generate Compose previews](https://developer.android.com/studio/gemini/generate-compose-previews) |
| Transform UI | Use natural language to update your app UI directly from the Compose preview panel. | [Transform UI](https://developer.android.com/studio/gemini/transform-ui) |
| Journeys for Android Studio | Use natural language to describe steps and assertions for end-to-end tests. | [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys) |

## Android Studio Panda 2

The following are new features in Android Studio Panda 2.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2025.3.2).

### Custom View Preview deprecation

We are deprecating the
[Custom View](https://developer.android.com/develop/ui/views/layout/custom-views/custom-components)
Preview feature in the coming releases.

As the Android ecosystem shifts toward [Jetpack Compose](https://developer.android.com/compose),
building custom UI components has become significantly more efficient and
intuitive. Compose includes a powerful,
built-in [@Preview](https://developer.android.com/develop/ui/compose/tooling/previews) system that
provides a superior workflow for developing custom UI elements
compared to the legacy XML-based approach.

By deprecating the Custom View Preview, we are able to focus our resources
on enhancing the preview experience within the Compose ecosystem while
providing a leaner, more performant IDE.

### Create a new project with AI

Use the power of generative AI to accelerate your Android development workflow.
Starting with Android Studio Otter 1 Canary 5, the AI agent enables you go
from idea to app prototype in minutes.

The agent is capable of generating a variety of multiscreen applications:

- **Single-screen apps:** Build basic apps with static UI layouts.
- **Multipage apps:** Create applications with basic navigation between screens.
- **AI-enhanced apps:** Integrate Gemini APIs to add generative AI features.
- **Apps with public API integration:** Build apps that display data from public APIs.

To use the project setup agent, do the following:

1. Start Android Studio.
2. Select **New Project** on the **Welcome to Android Studio** screen (or
   **File \> New \> New Project** from within a project).

   ![The Welcome to Android Studion screen, which has the New Project, Open, and Clone Repository buttons.](https://developer.android.com/static/studio/gemini/images/welcome_to_android_studio.png) Start a new project.
3. Select **Create with AI**.

   ![The 'new project' dialog, which has cards for various kinds of
   app templates, such as Empty Activity, Navigation UI Activity, and
   so forth. The dialog also has the Create with AI control, which
   activates Gemini in Android Studio to set up a new project for
   you.](https://developer.android.com/static/studio/gemini/images/new_project.png) Select a project template or create your app with Gemini.
4. Type your prompt into the text entry field and click **Next**.

   ![The Create with AI dialog containing the prompt: A fitness
   tracker for a phone and watch, tracking running and cycling. The
   dialog includes buttons for selecting various types of apps,
   including a fitness tracker button.](https://developer.android.com/static/studio/gemini/images/what_do_you_want_to_build.png) Dialog for setting up a new project.
5. Name your app and click **Finish** to start the generation process.

Based on your prompt, Gemini in Android Studio generates a structured plan for
your app. Once you approve the plan, the agent begins an autonomous generation
loop to configure and build your app.

### Update dependencies with the AI agent

Upgrading dependencies can be a complex and time-consuming task. Starting with
Android Studio Otter 1 Canary 5, the AI agent automates and simplifies the
dependency upgrade process, eliminating tedious work and improving project
maintainability. With just a few clicks, you can seamlessly upgrade all your
dependencies and get the benefits of the latest versions, so you can focus on
building high-quality apps.
![Update libraries from the version catalog.](https://developer.android.com/static/studio/gemini/images/update-all-libraries-with-gemini.png) Update libraries from the version catalog.

To update dependencies using the AI agent, do one of the following:

- Click **Refactor** (or right-click in the editor or project view) **\> Update
  dependencies**.
- In the `libs.versions.toml` file, hover over a version that is underlined,
  click the **Show Context Actions**
  ![](https://developer.android.com/static/studio/images/buttons/show-context-actions.png)
  menu that appears, and then click **Update all libraries with Gemini**.

  > [!NOTE]
  > **Note:** You should use the [Android Gradle plugin (AGP) Upgrade Assistant](https://developer.android.com/build/agp-upgrade-assistant) to upgrade versions of AGP. You can invoke the AGP Upgrade Assistant from the **Show Context Actions** menu for the AGP entry in your `libs.versions.toml` file. We recommend you run the AGP Upgrade Assistant before asking Gemini to update all the other dependencies.

During the process, the agent provides a high-level overview of its upgrade plan
so you can monitor progress step by step and review all changes before applying
them. The agent iterates through the build process, resolving any build errors
that arise from the upgrades. You can review, accept, or rollback changes or
stop the agent at any point.

### Monochrome icon support in Asset Studio

Android Studio Narwhal Feature Drop 2025.1.3 Canary 2 and higher simplify
the creation of themed app icons. With Android 13 (API level 33) and higher,
users can opt for themed app icons, which adapt to the wallpaper and theme of
the user's device.

To support this feature, Android Studio integrates a new monochrome icon option
directly into the **Image Asset Studio wizard** . When you're creating an adaptive
app icon, you now see a dedicated **Monochrome** tab in addition to the existing
**Foreground** and **Background** tabs. You can either provide a separate
monochrome app icon (see the [design specs](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive#design-adaptive-icons)), or allow
Android Studio to default to reusing the foreground layer of the adaptive icon
for the monochrome layer.

You can access **Image Asset Studio** through the **Resource Manager** , or by
right-clicking a project directory and navigating to **New \> Image Asset**.

Select **Launcher icons (Adaptive and Legacy)** as the icon type to see the
new **Monochrome** tab.

After importing the icons,
you can [preview your themed app icons](https://developer.android.com/studio/write/create-app-icons#preview-themed-app-icons).
![](https://developer.android.com/static/studio/images/design/monochrome-icon-support.png) Monochrome Icon Support in Asset Studio

### Layout Inspector 3D mode deprecation

In Android Studio Panda 2, we deprecated the 3D Mode feature
in the [Layout Inspector](https://developer.android.com/debug/layout-inspector). While 3D Mode provided a
way to visualize deep hierarchies,
usage data indicates that the standard 2D view and Component Tree meet
the vast majority of debugging needs. By removing this feature, we can direct
our resources toward improving the overall support, performance, and stability
of the Layout Inspector. You can continue to inspect view nesting and
z-ordering using the Component Tree and the standard 2D layout view.

## Android Studio Panda 3

The following are new features in Android Studio Panda 3.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2025.3.3).

### Suggested fixes for crashes

In Android Studio Meerkat Feature Drop, we launched Gemini insights for crashes
reported in the [App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights) tool
window. Now, Android Studio can use Gemini to analyze the crash data along with
your source code to suggest potential fixes. After selecting a crash in the App
Quality Insights tool window, navigate to the **Insights** tab and click
**Suggest a fix** after Gemini generates an insight for the crash. Gemini then
generates suggested code changes that you can review and accept in an editor
diff tab.
![](https://developer.android.com/static/studio/preview/features/images/suggested-fixes.png)

> [!NOTE]
> **Note:** Before you get started, make sure you enable context sharing in the Gemini settings (**Android Studio \> Settings \> Gemini** ) under **Context Awareness**.

### Compose Preview Screenshot Testing tool

Use the Compose Preview Screenshot Testing tool to test your Compose UIs and
prevent regressions. The new tool helps you generate HTML reports that let you
visually detect any changes to your app's UI. Learn more at [Compose Preview
Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing).

### LeakCanary in Android Studio Profiler

Android Studio Panda includes a
[LeakCanary](http://square.github.io/leakcanary/) integration directly in the Android Studio
Profiler as a dedicated task.
![](https://developer.android.com/static/studio/preview/features/images/leakcanary-task.png) New task in Android Studio Profiler to analyze leaks with LeakCanary

The LeakCanary profiler task in Android Studio actively moves the memory leak
analysis from your device to your development machine, resulting in a
significant performance boost during the leak analysis phase as compared to
on-device leak analysis.

Additionally, the leak analysis is now contextualized within the IDE and fully
integrated with your source code, providing features like **Jump to Source** and
other helpful code connections that drastically reduce the friction and time
required to investigate and fix memory leaks. You can also copy the entire leak
analysis for further processing with Gemini. This can dramatically increase your
productivity and improve your workflow during the development phase.
![](https://developer.android.com/static/studio/preview/features/images/leakcanary-analysis.png) LeakCanary memory leak analysis contextualized with **Go to
declaration** for debugging

### Material symbols support in Android Studio

Add and customize the latest Material symbols in your app with Android
Studio Otter 2 Feature Drop. The [Vector Asset Studio](https://developer.android.com/studio/write/vector-asset-studio) is
now fully integrated with the [Material symbols](https://fonts.google.com/icons)
library from Google Fonts, giving you access to the complete catalog
right inside the IDE.

You can now customize icon attributes like weight, grade, and optical size
directly in the studio to perfectly match your design. Try it out in the latest canary build!
![](https://developer.android.com/static/studio/images/design/material-symbols.gif) Material Symbol support in Vector Asset Studio

### Recomposition state reads in the Layout Inspector

We've made it easier to diagnose high
[recomposition](https://developer.android.com/develop/ui/compose/mental-model#recomposition) counts by adding
Recomposition state reads to the [Layout Inspector](https://developer.android.com/debug/layout-inspector). Available
in Panda 2 canary, this feature helps you identify the state variables that triggered a
recomposition by providing a detailed list of state reads performed during that cycle.
To use this feature, use `compose.ui:ui:1.10.0 (BOM 2025.12.01)` or higher.

**Key capabilities**

Key capabilities of this feature are the following:

- **Trace state invalidation**: When a node recomposes, click the recomposition count link in the Component Tree to open the State Inspection panel.
- **Detailed stack traces** : Identify the specific state variables being read, including as counts, lists, or elevation values. Check which ones were `invalidated` (changed) to trigger the update.
- **Navigate recomposition history**: Use the navigation arrows in the panel header to cycle through the state data of previous recompositions for a specific node.
- **AI-powered explanations** : Click **Explain with AI** in the State Inspection panel to display a natural-language breakdown of the state read and why it caused a recomposition.

**Get started**

Follow these steps to try out these features.

1. Open the Layout Inspector.
2. Right-click the recomposition column and do one of the following:

   - For all nodes, select **Observe Recomposition \> Observe
     All**.
   - For specific notes, select **Recomposition \> Observe Node**.

   ![](https://developer.android.com/static/studio/images/design/compose-state-inspector-entry.png) Turn on recomposition state reads in the Layout Inspector
3. Interact with your app. When recompositions occur, click the blue count
   links in the Component Tree to inspect the state.

   ![](https://developer.android.com/static/studio/images/design/compose-state-inspector.png) Sample result of recomposition state reads in the Layout Inspector
4. Click "Explain with AI" to get a breakdown analysis of why recomposition happened.

   ![](https://developer.android.com/static/studio/images/design/explain-with-ai-state.png) Sample result of "Explain with AI" for state reads in Layout Inspector