---
title: https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-panda-4-release-notes
source: md.txt
---

The following are the release notes for Android Studio Panda 4.

## Patch releases

The following is a list of patch releases in Android Studio Panda 4.

### Android Studio Panda 4 \| 2025.3.4 Patch 1 (May 2026)

This minor update includes [these bug
fixes](https://developer.android.com/studio/releases/fixed-bugs/studio/2025.3.4#android-studio-panda-4-%7C-2025.3.4-patch-1).

The following are new features in Android Studio Panda 4.

## Gemini API Starter template

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

## Generate unit tests with Gemini

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

## Google One integration for Gemini in Android Studio

Android Studio Panda 4 introduces access to an enhanced Agent Mode
experience when you subscribe to the [Google One AI Pro or Ultra
plans](https://one.google.com/about/google-ai-plans/). The Google One
integration supercharges your Android development with higher rate limits for
the default Gemini model. If you are subscribed to a Google One AI Pro or Ultra
plan, you can take advantage of these benefits automatically when you sign in to
your Google Account in Android Studio. Using Gemini in Android Studio with a
Google One AI Pro or Ultra plan doesn't affect your quota for other AI tools,
such as Gemini CLI or Antigravity.

## Next Edit Prediction (NEP)

Android Studio Panda 4 introduces Next Edit Prediction (NEP), a major evolution
of the editor's AI capabilities. While traditional [AI Code Completion](https://developer.android.com/studio/gemini/code-completion)
focuses on suggesting code at your current cursor position, NEP is designed for
"away from cursor" updates.

By using Gemini to analyze your recent edits across multiple files, NEP
anticipates your next logical move. It proactively suggests changes elsewhere in
your codebase---helping you maintain consistency and speed up repetitive
refactoring tasks.

## Ask Mode

In Android Studio Panda 4, we are removing the *Ask* tab and replacing it with a
dedicated conversation mode, allowing you to ask the agent questions and get
answers without prompting it to execute tasks.

## Planning Mode

The new Planning Mode prompts the agent to come up with a detailed project plan
before it begins executing tasks. Instead of a single pass where the model
directly predicts the next token of code, Planning Mode facilitates a
multi-stage reasoning process, giving the agent additional space to evaluate its
own proposed logic before presenting it to you.

## Developer verification support

To help you meet the upcoming Android developer verification requirements, we
are bringing registration checks directly into your workflow. You will now see
your app's registration status right in Android Studio when you generate a
signed App Bundle or APK. By moving these checks closer to build time, you
can catch any issues early and ensure your apps are ready before the
[verification requirement](https://developer.android.com/developer-verification) goes into effect for certified
Android devices starting in September 2026.

## Agent Web Search

While Android Studio's agent already leverages the [Android Knowledge Base](https://developer.android.com/studio/gemini/knowledge-base)
for official documentation, modern Android development relies on a vast
ecosystem of external libraries. Agent Web Search expands Gemini's reach,
allowing it to query Google directly to fetch current reference material from
across the web. From checking the latest setup guides for Coil to finding
advanced configuration tips for Koin or Moshi, the agent can now pull in the
most up-to-date information in real time.