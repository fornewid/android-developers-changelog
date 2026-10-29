---
title: https://developer.android.com/blog/posts/ai-agents-android-studio-integration
url: https://developer.android.com/blog/posts/ai-agents-android-studio-integration
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Your favorite agents are now integrated in Android Studio

3 min read ![](https://developer.android.com/static/blog/assets/Rabbit2_Strapi_27563aeaf4_1BAzRM.webp) 28 Oct 2026 [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) Product Manager, Android Developer Experience Android Studio Rabbit 2 is now stable and ready for you to use in production. This release includes key features to improve your development such as Bring Your Own Agent, new XR Emulator features, a LeakCanary update, a new agent skills manager tool, AI code review, and more. You can learn more about these stable features, the features in [the latest Android Studio Canary release](https://developer.android.com/studio/preview/features), and check out the demos and talks we have to share at [Android Dev Summit](https://developer.android.com/events/dev-summit), which is being live-streamed today.

## **Bring Your Own Agent (BYOA): Integrate your preferred coding agents**

You told us how important flexibility is to your workflows. You can now access the best agents along with the best Android development tools. If you prefer a specific ACP compliant agent --- you've got it. If you need the cost efficiency of a particular agent for your project --- you've got it. If you need to use a specific provider to align with an enterprise agreement --- you've got it.
![BYOA_Claude_no_rounding.png](https://developer.android.com/static/blog/assets/BYOA_Claude_no_rounding_64d9b82578_Z2b5Xun.webp) Running Claude Agent in Android Studio

You can choose from over 40 coding agents --- including Claude Agent, Codex from OpenAI, Junie, and Google Antigravity. These agents have access to Android Studio tools like the Android Emulator, Build Systems, Logcat - and they also can use [Android skills](https://developer.android.com/tools/agents/android-skills) to complete complex tasks.

To get started with BYOA, open the agent window and select your preferred agent, or choose an agent from **Settings \> Tools \> AI \> Agents**, authenticate, and submit your first prompt.

## **Build for Android XR with Emulators**

The Android XR Emulators for XR glasses, audio glasses, and display glasses are now stable in Android Studio with new and updated features, so you can build, iterate, and test Android XR experiences right from your laptop. The updated display glasses Emulator lets you customize the environment with your own 360-degree photos or video feed from a connected camera so you can test real physical environments from anywhere. We've also introduced new hardware LED indicators for microphone and camera states and made improvements to the Pairing Wizard to pair a virtual phone with virtual audio and display glasses faster and more reliably. To get started, launch the XR, audio, or display glasses Emulators from Device Manager.
![emulator environment.png](https://developer.android.com/static/blog/assets/emulator_environment_86a016acf3_ZrhT3l.webp) Customizable environments for Intelligent Eyewear in the Android XR Emulator

## **Discover, install, and manage Android skills in Android Studio**

![installed-skills.png](https://developer.android.com/static/blog/assets/installed_skills_0845439fcc_Z1hj1AV.webp) Skill management in Android Studio

It is now easier to discover, install, and manage Android [skills](https://developer.android.com/studio/gemini/skills) directly in the skill manager in Android Studio, giving you granular control over the specialized workflows and procedural guidance available to the agent. Android Studio comes loaded with [Android skills](https://developer.android.com/tools/agents/android-skills) and [Firebase agent skills](https://firebase.google.com/docs/ai-assistance/agent-skills)---like migrating legacy XML Views to Jetpack Compose, upgrading to AGP 9, implementing adaptive layouts for foldables and tablets, or integrating CameraX and Firebase services.

Open the **Skills** editor tab from the Agent panel's three-dot menu (**Manage Agent Skills** ), by typing @ in the chat box and clicking **Manage skills** , or from **Settings \> Tools \> AI \> Skills Manager**.
![manage-skills.png](https://developer.android.com/static/blog/assets/manage_skills_58274d1f9f_Z2jOAyC.webp) Invoke installed skills directly in chat using @ or open the skills manager

## **Agentic fixes with LeakCanary**

Android Studio directly integrates LeakCanary with the built-in agent to help you diagnose and resolve memory leaks without leaving the IDE. This integration lets LeakCanary provide more meaningful narrative explanations of the underlying causes of memory leaks, and suggest specific code changes to correct them. Try this feature out in the LeakCanary task in the Profiler.
![LeakCanary - AI Fix Zoomed in.png](https://developer.android.com/static/blog/assets/Leak_Canary_AI_Fix_Zoomed_in_6c582c3d5a_Z17WTmJ.webp) Leverage AI to fix memory leaks within Android Studio Profiler

## **Gemini Enterprise in Android Studio**

For engineering teams requiring enterprise-grade governance, strict data privacy controls, and custom internal knowledge base integrations, full support for Gemini Enterprise has been available in Android Studio since Android Studio Rabbit 1. You can use Gemini Enterprise to connect to your design systems, internal SDKs, and private repositories to get highly relevant responses for your use cases.

Gemini Enterprise in Android Studio provides key capabilities for enterprise teams:

- **Strict Data Privacy:** Guarantees that source code and workspace context are never retained or used to train global foundation models.
- **Compliance \& Audit Logging:** Full visibility into agent activities, generated patches, and prompt history within your organization's security perimeter.
- **Admin Policies:** Centralized management for IT administrators to define approved skills, agents, and model endpoints across dev teams.

### **Go from raw diffs to guided code reviews with Change Review**

As agentic tools help you write and refactor code faster than ever, a new engineering bottleneck has emerged: reviewing and verifying all of that code. AI Change Review meets you wherever code changes live in Android Studio. You can launch a review from three visual entry points or directly from the Agent chat window.
![change-review-entry-points.png](https://developer.android.com/static/blog/assets/change_review_entry_points_eab09cc019_Z1p6439.webp) Change Review works across: 1. Agent Changes 2. Pending Commits, and 3. the Git Log

Change Review starts off by identifying Recommended Fixes where the agent independently reviews the agent changes, pending commits, or committed changes under review. Once you have addressed recommended fixes, you can click **Create Walkthrough** to kick off a guided walkthrough. Instead of forcing you to read files in alphabetical order, the guided walkthrough accelerates your review by grouping and prioritizing related diff chunks across your project into logical themes.

## **Getting Started**

You can start using these features by downloading the latest stable version of [Android Studio](https://developer.android.com/studio). If you find a bug, please [file an issue](https://developer.android.com/studio/report-bugs). Please connect with the Android developer community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), and [X](https://x.com/androidstudio).

You can see demos and talks about these features and more at [Android Dev Summit](https://developer.android.com/events/dev-summit), live-streaming today. You can also read more about [updates to agentic tools for Android](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance). We can't wait to see what you'll build!
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Written by:

-

  ## [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-warner) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)
Continue reading
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_2bzRoq.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_1Ctd29.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 2 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 24 Sep 2026 24 Sep 2026 ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build your way: Use any AI agent of your choice in Android Studio](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio) Last year, Android Studio opened up to any AI model. Today, we're taking the next step by introducing support for your choice of coding agents.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)