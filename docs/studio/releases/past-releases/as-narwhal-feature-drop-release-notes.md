---
title: Android Studio Narwhal Feature Drop | 2025.1.2 (July 2025)  |  Android Developers
url: https://developer.android.com/studio/releases/past-releases/as-narwhal-feature-drop-release-notes
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [IDE guides](https://developer.android.com/studio/releases/past-releases)

# Android Studio Narwhal Feature Drop | 2025.1.2 (July 2025) Stay organized with collections Save and categorize content based on your preferences.




The following are new features in Android Studio Narwhal Feature Drop.

## Patch releases

The following is a list of patch releases in Android Studio Narwhal Feature
Drop.

### Android Studio Narwhal Feature Drop | 2025.1.2 Patch 1 (August 2025)

This is a minor update that includes [bug fixes](/studio/releases/fixed-bugs/studio/2025.1.2#android-studio-narwhal-feature-drop-%7C-2025.1.2-patch-1) and improvements to
Android Studio and the Android Gradle plugin.

#### Android Studio fixes and performance improvements

* Fixed an issue in the `code_search` tool used by the Agent.
* **Kotlin Multiplatform (KMP):** A bug has been fixed where Gradle tasks for
  **Android Gradle Managed Devices** were not being created correctly in KMP
  projects. Your managed device tasks should now resolve and run as expected.

#### Android Gradle plugin fixes and performance improvements

* The Android Gradle plugin (AGP) has been updated to version 8.12.1.

The following are new features in Android Studio Narwhal Feature Drop.

## Gemini in Android Studio's Agent Mode

Gemini in Android Studio's Agent Mode is a new AI feature designed to handle
complex, multi-stage development tasks that go beyond what you can experience by
chatting with Gemini. To use Agent Mode, click **Gemini** in the sidebar and
then select the **Agent** tab. You can describe a complex goal, like generating
unit tests or fixing errors, and the agent formulates an execution plan that
spans multiple files in your project. The agent suggests edits and iteratively
fixes bugs to reach the goal. You can review, accept, or reject the proposed
changes and ask the agent to iterate on your feedback.

![](/static/studio/images/agent-mode.png)

## Rules in Gemini

Rules in Gemini let you define preferred coding styles or output formats within
the [Prompt Library](/studio/gemini/prompt-library). You can also mention your
preferred tech stack and languages. When you set these preferences once, they
are automatically applied to all subsequent prompts sent to Gemini. Rules help
the AI understand project standards and preferences for more accurate and
tailored code assistance. For example, you can create a rule such as "Always
give me concise responses in Kotlin."

To set up a rule, go to **Android Studio > Settings > Tools > Gemini > Prompt
Library > Rules** and edit the text in the editor. Use the drop-down to store
rules at the IDE level or the project level:

* IDE-level rules are private to yourself and can be used across multiple
  projects.
* Project-level rules can be shared among teammates working on the same project.
  To share prompts across the team you must add the `.idea` folder to the version
  control system.

![](/static/studio/images/rules.png)

## Embedded XR Emulator

The XR Emulator now launches by default in the embedded state. You can now
deploy your application, navigate the 3D space and use the Layout Inspector
directly inside Android Studio.

![The XR Emulator now launches by default in the embedded state.](/static/studio/preview/features/images/embedded-xr-emulator.png)


Use the XR Emulator directly inside Android Studio.

## XR project template

Android Narwhal Feature Drop introduces a new project template specifically
designed for Jetpack XR. This provides a solid foundation with boilerplate code
to begin your immersive experience development journey right away.

## Embedded Layout Inspector for XR

The [embedded Layout Inspector](/studio/debug/layout-inspector) now supports XR
applications, which lets you inspect and optimize your UI layout within the XR
environment. Get detailed insights into your app's component structure and
identify potential layout issues to create more polished and performant
experiences.

## 16 KB page size support

Android Studio Narwhal Feature Drop adds improved support for [transitioning to
16 KB page sizes](/guide/practices/page-sizes). To help you navigate this
transition smoothly, Android Studio now offers proactive warnings when building
APKs or Android App Bundles that are incompatible with 16 KB devices. Using the
APK Analyzer, you can also find out which libraries are incompatible with 16 KB
devices. To test your apps in this new environment, a dedicated 16 KB emulator
target is also available in Android Studio alongside existing 4 KB images.

![](/static/studio/preview/features/images/16kb-page-size.png)

## Compose preview navigation improvements

Compose preview interaction is now more efficient with the latest navigation
improvements. Click on the preview name to jump to the preview definition or
click the individual component to jump to the function where it's defined. Hover
states provide immediate visual feedback as you mouse over a preview frame.
Improved keyboard arrow navigation eases movement through multiple previews,
enabling faster UI iteration and refinement.

[

](/static/studio/preview/features/images/compose-preview-navigation.mp4)

## Compose preview picker

The Compose preview picker is now available. To try it out, click any `@Preview`
annotation in your Compose code.

![](/static/studio/preview/features/images/compose-preview-picker.png)

## Child recomposition in Layout Inspector

Layout Inspector supports Child recomposition counts. You can now see
recomposition counts even if the composable that is recomposing is collapsed
under a parent in the component tree. When you see the child recomposition
counts increase, you can open up the tree and find where the recompositions are
happening.

![Layout Inspector supports Child recomposition counts](/static/studio/preview/features/images/li-child-recomposition.png)


Layout Inspector supports Child recomposition count.

## Partner Device Labs available with Android Device Streaming

Partner Device Labs are device labs operated by Google OEM partners, such as
Samsung, Xiaomi, OPPO, OnePlus, vivo, and others, and expand the selection of
devices available in Android Device Streaming. This service is in Beta and is
available in the latest Canary releases of Android Studio. To learn more, see
[Connect to Partner Device Labs](/studio/run/android-device-streaming#2P).

![](/static/studio/images/pdl-catalog.png)

## K2 mode by default

Android Studio now uses the K2 Kotlin compiler by default. This next-generation
compiler brings significant performance improvements to the IDE and your builds.
By enabling K2, we are paving the way for future Kotlin programming language
features and an even faster, more robust development experience in Kotlin.