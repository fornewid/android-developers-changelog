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
| Android Studio Panda 3 | Stable |
| Android Gradle plugin 9.1.0 | Stable |
| Android Studio Panda 4 | RC |

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
| Journeys for Android Studio | Use natural language to describe steps and assertions for end-to-end tests. | [Journeys for Android Studio](https://developer.android.com/studio/gemini/journeys) |

## Android Studio Panda 4

The following are new features in Android Studio Panda 4.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2025.3.4).

### Gemini API Starter template

The Gemini API Starter template provides a straightforward path for Android
developers to integrate AI features into their applications. By leveraging
Firebase AI Logic, developers can avoid manual configuration and security
management.
![](https://developer.android.com/static/studio/preview/features/images/GeminiAPIStarter.png) Gemini API Starter new project template

Key Features:

- **No API Key Management**: Eliminates the need to manually provision, embed, or rotate API keys within your client-side code, reducing security risks and setup time.
- **Automated Firebase Integration**: Seamlessly connects your Android Studio project to Firebase services. The template handles the backend plumbing required to communicate with Gemini models securely.
- **Production-Ready Architecture**: Built on top of Firebase's managed infrastructure, ensuring that your AI features can scale from a local prototype to a production environment without architectural changes.

To get started, go to **File** \> **New** \> **New Project** and select the
**Gemini API Starter** template from the list of available project types.

### Generate unit tests with Gemini

Gemini in Android Studio can generate comprehensive, compilable unit tests for
your Kotlin and Java code. Gemini analyzes your source code to identify
constructor dependencies, business logic branches, and edge cases, and then
automatically creates a complete test class. This includes the generation of
`setUp` methods, mock initialization, and individual test cases tailored to your
project's specific architecture and coding style.

To get started, open a source file, right-click the code you want to test, and
select **AI \> Generate Unit Tests** . For more details, see
[Generate unit tests with Gemini](https://developer.android.com/studio/gemini/generate-unit-tests#prerequisites).
Unit test generation demo

### Google One integration for Gemini in Android Studio

Android Studio Panda 4 Canary 2 introduces access to an enhanced Agent Mode
experience when you subscribe to the [Google One AI Pro or Ultra
plans](https://one.google.com/about/google-ai-plans/). The Google One
integration supercharges your Android development with higher rate limits and an
expanded context window for the default Gemini model. If you are subscribed to a
Google One AI Pro or Ultra plan, you can take advantage of these benefits
automatically when you sign in to your Google Account in Android Studio.
![](https://developer.android.com/static/studio/images/google-one-integration.png) Google One integration for Gemini in Android Studio.