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
| Android Studio Quail 3 | Stable |
| Android Gradle plugin 9.3.0 | Stable |
| Android Studio Quail 4 | RC |
| Android Studio Rabbit 1 | Canary |

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

## Android Studio Quail 4

The following are new features in Android Studio Quail 4.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.1.4).

### Build full-stack apps with Firebase in Agent Mode

Firebase services like Authentication and Cloud Firestore databases can be
[enabled and configured directly in Agent Mode](https://firebase.blog/posts/2026/05/google-io-2026-announcements) in
Android Studio using [Firebase agent skills](https://firebase.google.com/docs/ai-assistance/agent-skills).
The agent can help you complete Firebase integration and configure backend
services. This integration lets you build robust, full-stack Android apps without
leaving your IDE.
![The agent guiding a user through Firebase Auth and Firestore setup in the IDE.](https://developer.android.com/static/studio/images/build-full-stack-apps-with-firebase-agent-mode.png) The agent guiding a user through Firebase integration in the chat interface.

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

### Gemma 4 integration

You can now run the powerful Gemma 4 model directly within Android Studio for AI
code assistance without relying on a third-party provider to host it. Powered
natively by an integrated runtime, this local execution gives you full control
to design new features, refactor code, and debug issues---all completely
on-device. To download Gemma models, go to **Settings \> Tools \> AI \> Model
Providers \> Gemma**.
![](https://developer.android.com/static/studio/releases/assistant/2026.1.4/gemma-4.png)

### Simulate back navigation transitions with Interactive Preview

Quail 4 introduces dedicated controls---including a **Navigate Back** action and a
**Predictive Back Progress** slider---allowing you to test back and forward
animations without deploying to a physical device or emulator. You can now step
through custom transition states and verify predictive back gesture behavior
directly within [Compose Interactive Preview](https://developer.android.com/develop/ui/compose/tooling/previews#preview-interactive).
![](https://developer.android.com/static/studio/releases/assistant/2026.1.4/interactive-preview.gif)

## Android Studio Rabbit 1

The following are new features in Android Studio Rabbit 1.

To see what's been fixed in this version of Android Studio, see the [closed
issues](https://developer.android.com/studio/releases/fixed-bugs/studio/2026.2.1).

### Compose Preview Screenshot Testing tool

Use the Compose Preview Screenshot Testing tool to test your Compose UIs and
prevent regressions. The new tool helps you generate HTML reports that let you
visually detect any changes to your app's UI. Learn more at [Compose Preview
Screenshot Testing](https://developer.android.com/studio/preview/compose-screenshot-testing).

### Publish to Google Play for testing

Android Studio now gives you the ability to upload new releases of your app
directly to Google Play Console test tracks. You can do this by selecting
a new option to continue to 'Publish for Testing' at the end of the Generate
Signed App Bundle flow. This integration supports uploading an initial
release of a brand-new app to a Play Console internal test track. You can
also use this feature to upload releases of existing apps to other types of
test tracks. You need to be registered on Google Play Console to take
advantage of this functionality.

### Android Studio is part of the Gemini Enterprise bundle

Android Studio is now included in the
[Gemini Enterprise subscription bundle](https://cloud.google.com/gemini-enterprise),
which enables enterprise development teams to deploy Android Studio using models
hosted directly in your organization's Google Cloud infrastructure. Every
session runs under Google Cloud's enterprise security controls, data residency
guarantees, and the Google Cloud Terms of Service. Android Studio comes with the
**Gemini Enterprise Standard** or **Gemini Enterprise Plus** subscription plans.

By connecting Android Studio to your Google Cloud project, your organization
gains the following benefits:

- Enterprise governance: Operate under your project's existing Google Cloud Terms of Service with centralized administrative controls.
- Data residency and security: Keep code and data inside your secure network. Your prompts, AI responses, code, and telemetry remain in your private network (through VPC Service Controls) and chosen data region.
- Consolidated billing: Pay-as-you-go directly with your existing Google Cloud Billing account with unified invoicing.

For more details about Google Enterprise support for AI developer tools, see
[AI developer tools overview](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview)
in the Google Cloud documentation.

#### Sign in to Android Studio with a Gemini Enterprise subscription

To sign in to Android Studio with a Gemini Enterprise subscription, follow these
steps:

1. Start Android Studio.
2. To open the agent tool window, click **Agent** ![](https://developer.android.com/static/studio/images/agent-icon.png) or click **View \> Tool Windows \> Agent**.
3. Click **Sign in to Google** to sign in using the browser.
4. Click **Business account**.
5. Click **Continue with Google Cloud** to sign in using the browser.
6. If a license (subscription type) is found, it'll be displayed in Android Studio. Select the license that corresponds to the project that you want to open.

![](https://developer.android.com/static/studio/images/ge-onboarding.png)

Instead of picking one of the listed licenses, you can self-assign a license:

1. Click **Auto-assign from project ID**.
2. Click **Next**.
3. Enter your project ID.
4. Enter your location: **Global** , **Europe (EU)** , or **United States (US)**.
5. Confirm the license to save your selection.

If you need to change your license selection or update your project ID later on,
go to **File** (**Android Studio** on macOS) **\> Settings \> AI \> Model
Providers** and change the selection under **Change License**.

#### Troubleshoot issues

If you encounter issues using Android Studio with a Gemini Enterprise
subscription, first check that you're using Android Studio Quail 4 Canary 4 or
higher. If the issue persists, you need to contact your admin to make
configuration changes:

- If no licenses appear during setup, contact your admin to request access. We recommend setting up auto-assignment of licenses.
- If you can't access the latest Gemini models in Android Studio, contact your admin to enable preview models.

### Model Assignment

The Model Assignment feature lets you pick different AI models for different
types of tasks in Android Studio. For example, you can assign a large, pro-tier
model for complex reasoning tasks in Agent Mode, and a faster, lightweight model
for simpler, latency-sensitive tasks like commit message generation or next edit
prediction. This lets you balance quality, speed, and quota usage across
features.
![](https://developer.android.com/static/studio/preview/images/model-assignment.png)

To configure this, go to **File** (**Android Studio** on macOS) **\> Settings \> Tools \>
AI \> Model Providers** , select the **Model Assignment** tab, and use the dropdowns
to assign a model to each feature category. You can also change the model directly
from the model selector dropdown in the Agent Mode panel---the Model Assignment
settings for **Thinking** features will automatically update to reflect your selection.