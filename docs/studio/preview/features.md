---
title: https://developer.android.com/studio/preview/features
url: https://developer.android.com/studio/preview/features
source: md.txt
---

> Documentation index: https://developer.android.com/studio/preview/llms.txt

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
[Android Studio release names](https://developer.android.com/studio/releases/studio-release-names.md.txt) to understand Android
Studio version naming.

For the latest news on Android Studio preview releases, including a list of
notable fixes in each preview release, see the [Release
Updates](https://androidstudio.googleblog.com/) in the Android Studio blog.


## Current versions of Android Studio

The following table lists the current versions of Android Studio and their
respective channels.

| Version | Channel |
|---|---|
| Android Studio Rabbit 2 | Stable |
| Android Gradle plugin 9.5.0 | Stable |
| Android Studio Rabbit 3 | RC |
| Android Studio Stingray 1 | Canary |

<br />

## Compatibility with Android Gradle plugin previews

Each preview version of Android Studio is published alongside a corresponding
version of the Android Gradle plugin (AGP). Preview versions of Studio should
work with any
[compatible](https://developer.android.com/studio/releases.md.txt#android_gradle_plugin_and_android_studio_compatibility)
stable version of AGP. However, if you're using a preview version of AGP, you
must use the corresponding preview version of Studio (for example, Android
Studio Chipmunk Canary 7 with AGP 7.2.0-alpha07). Attempts to use divergent
versions (for example, Android Studio Chipmunk Beta 1 with AGP
7.2.0-alpha07) will cause a Sync failure, which results in a prompt to update to
the corresponding version of AGP.

For a detailed log of Android Gradle plugin API deprecations and removals, see
the [Android Gradle plugin API
updates](https://developer.android.com/studio/releases/gradle-plugin-api-updates).

## Android Studio Rabbit 3

The following are new features in Android Studio Rabbit 3.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.2.3).

### Migrate Views to Jetpack Compose

![](https://developer.android.com/static/studio/releases/assistant/images/migrate-compose.png)

You can now migrate existing View-based UI to Jetpack Compose using automated
migration tooling in Android Studio. Right-click any XML layout and choose
**AI \> Migrate to Compose**, or run it across your whole project from the action
palette. The agent scopes the work with you, drafts a plan, and converts your
layouts, view binding code, and UI logic into idiomatic Compose. The integrated
Progress UI provides end-to-end visibility across planning, code transformation,
and build verification, producing migrated screens ready for review and testing.

### Progress UI for long-running agent tasks

![](https://developer.android.com/static/studio/releases/assistant/images/progress-ui.png)

The agent tool window now includes a Progress UI for long-running tasks. A
status bar and expandable timeline show the phases and steps of the task the
agent is working on, which step is currently running, how long each step took,
and what remains to be done. Progress UI appears automatically for migrations,
for planning mode, and whenever the agent takes on a complex multi-step task.
Progress is saved with the conversation, so you can step away, come back, and
pick up where the agent left off.

### Explore UI design options before changing your code

![](https://developer.android.com/static/studio/releases/assistant/images/ui-sandbox.png)

The agent in Android Studio can now prototype UI in a sandbox, rendering Jetpack
Compose previews without creating or modifying any file in your project. Ask for
a design change, a new screen, or several variations of a component, and the
agent compiles its proposals in memory against your module (using your real
composables, theme, and resources) and shows them as a gallery in the agent tool
window for you to compare. You can keep iterating on the proposals, and nothing
is written to your source code until you accept a design. When you do, the agent
applies the change to your project.

### Agentic Journeys

Journeys let you describe end-to-end user flows in natural language and run them
directly with the AI agent on a connected device or emulator. The agent steps
through the flow, verifies expected outcomes, and generates a pass or fail
report with screenshots. Ask the agent in the **Agent** window to create, edit,
or run a journey, or open a journey file and click **Run** in the toolbar.

To learn more, see [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys.md.txt).

## Android Studio Stingray 1

The following are new features in Android Studio Stingray 1.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.3.1).

### Test suites in the Android Gradle plugin

Group unit tests, instrumented tests, asset tests, or mixed combinations into
named test suites using the AGP `testOptions` DSL. Each suite defines its own
source sets, dependencies, JUnit Platform test engines, and target build
variants. For more information, see [Test suites in the Android Gradle
plugin](https://developer.android.com/studio/preview/test-suites), [Unit test suites](https://developer.android.com/studio/preview/unit-test-suites.md.txt), and [Instrumented
test suites](https://developer.android.com/studio/preview/instrumented-test-suites).

### Compose Preview Screenshot Testing tool

Use the Compose Preview Screenshot Testing tool to test your Compose UIs and
prevent regressions. The new tool helps you generate HTML reports that let you
visually detect any changes to your app's UI. Learn more at [Compose Preview
Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing-with-testsuites).

### Model Assignment

The Model Assignment feature lets you pick different AI models for different
types of tasks in Android Studio. For example, you can assign a large, pro-tier
model for complex reasoning tasks in Agent Mode, and a faster, lightweight model
for simpler, latency-sensitive tasks like commit message generation or next edit
prediction. This lets you balance quality, speed, and quota usage across
features.
![](https://developer.android.com/static/studio/preview/images/model-assignment.png) Model Assignment settings in Android Studio.

To configure this, go to **File** (**Android Studio** on macOS) **\> Settings \> Tools \>
AI \> Model Providers** , select the **Model Assignment** tab, and use the dropdowns
to assign a model to each feature category. You can also change the model directly
from the model selector dropdown in the Agent Mode panel---the Model Assignment
settings for **Thinking** features will automatically update to reflect your selection.

### Publish to Google Play for testing

Android Studio now gives you the ability to upload new releases of your app
directly to Google Play Console test tracks. You can do this by selecting
a new option to continue to 'Publish for Testing' at the end of the Generate
Signed App Bundle flow. This integration supports uploading an initial
release of a brand-new app to a Play Console internal test track. You can
also use this feature to upload releases of existing apps to other types of
test tracks. You need to be registered on Google Play Console to take
advantage of this functionality.