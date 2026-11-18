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

### Migrations in Android Studio

You can now migrate a project with views-based UI to a Kotlin and Jetpack
Compose-based app. This feature produces a functional project that's ready for
testing and verification.

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