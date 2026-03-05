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
| Android Studio Panda 2 | Stable |
| Android Gradle plugin 9.1.0 | Stable |
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

## Android Studio Panda 3

The following are new features in Android Studio Panda 3.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2025.3.3).

### Suggested fixes for crashes with Agent integration in AQI

The [App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights) tool
window is now integrated with the AI agent to analyze crash data along with
your source code to provide detailed explanations and suggest potential fixes.
After selecting a crash in the App Quality Insights tool window, navigate to
the **Insights** tab and click **See more** to see a detailed explanation of
the crash. Click **Fix with AI** to have the agent suggest code changes that
you can review and accept.
![](https://developer.android.com/static/studio/preview/features/images/aqi-agent-integration.png) New agent integration in AQI with options to "See more" and "Fix with AI"

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
Recomposition state reads to the [Layout
Inspector](https://developer.android.com/studio/debug/layout-inspector). Available in Panda 3 canary, this
feature helps you identify the state variables that triggered a recomposition by
providing a detailed list of state reads performed during that cycle. To use
this feature, use `compose.ui:ui:1.10.0 (BOM 2025.12.01)` or higher.

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