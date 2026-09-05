---
title: https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4
url: https://developer.android.com/blog/posts/leverage-android-skills-and-gemma-4-in-android-studio-quail-4
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Leverage Android skills and Gemma 4 in Android Studio Quail 4

5 min read ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_c8d4ba2105_Z2bRC9Y.webp) 01 Sep 2026 [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) Product Manager, Android Studio **Android Studio Quail 4 is now stable and ready for you to use in production.**

This is the final stable release for Android Studio Quail. The new features in Android Studio enable you to build premium apps with AI efficiently and effectively. Check out the video below to see the most helpful new features from the last 4 releases that can help improve and speed up your development.
[Video](https://www.youtube.com/watch?v=lKqh34XT7Q8)

Here is a deep dive into what's new in Android Studio Quail 4:

### **Android skills bundled into Android Studio**

While LLMs are incredibly capable at generic coding queries, they frequently write incorrect or outdated code when confronted with rapidly evolving Android APIs, platform-specific migrations, or complex configuration structures.To solve this, we bundle [Android skills](https://developer.android.com/tools/agents/android-skills) that have been curated by the team who builds Android, directly into Android Studio. Following the open-standard [agent skills specification](https://agentskills.io/), these are modular, AI-optimized instructions designed specifically to guide LLMs through complex Android workflows. Android skills are now pre-loaded directly into the IDE, so you can start using them without having to manually download additional files.

When you prompt the Android Studio agent, we analyze your prompt and search against the metadata for installed skills, automatically invoking them when they're most relevant. Your agent gains instant domain expertise, applying Google's best practices with less overhead spent on long, manual setup prompts.

Android Studio comes preloaded with [23 curated skills](https://developer.android.com/tools/agents/android-skills/browse), including:

- **Need help upgrading your build?** You have the [Android Gradle Plugin (AGP) 9 Upgrade](https://github.com/android/skills/tree/main/build-system/agp/agp-9-upgrade) skill.
- **Want to profile your app for any performance issues?** You have the [Android Profiler](https://github.com/android/skills/tree/main/profilers/android-profiler) skill.
- **Ready for a Jetpack Navigation framework upgrade?** You have the [Navigation3](https://github.com/android/skills/tree/main/navigation/navigation-3) skill.
- **Adapting your app UI to different Android devices?** You have the [Adaptive](https://github.com/android/skills/tree/main/jetpack-compose/adaptive) skill.

We also encourage you to [create your own custom skills](https://developer.android.com/studio/gemini/skills) to extend Agent Mode with specialized experience and custom workflows for your team. And if you want to use Android skills with other command line interface (CLI) AIs outside of Android Studio, install Android CLI and run android skills add --all to quickly get started. If you ever want to disable bundled skills entirely, you can easily opt out via an IDE-wide toggle in Settings.
![as-agent-skill1.gif](https://developer.android.com/static/blog/assets/as_agent_skill1_94460a47aa_Zjq0Xo.webp) Android Studio comes preloaded with 23 curated Android skills.

### **Gemma 4 local model integration (private, secure, and offline AI coding)**

Many developers enjoy having access to local models, and Android Studio now natively integrates Gemma 4---Google's most powerful open model---for AI code assistance without the hassle of manual third-party setup.

- **System requirements:** You can run the smallest models with 12GB of RAM, but machines with 32GB+ RAM will run best. Please refer to [hardware requirements](https://developer.android.com/studio/gemini/use-a-local-model#try-the-gemma-4-model).
- **One-click management:** Simply select Gemma in the Agent model selector and then choose the model you'd like to download, or visit . Android Studio automatically downloads, verifies, and updates the model weights for you.
- **Bundled inference engine:** We have bundled a lightweight inference engine to run Gemma 4 models directly in the IDE.
- **On-device AI agent:** Because Gemma 4 features native agentic tool-calling capabilities, you can run complex, multi-file refactoring plans with the agent completely offline. Your source code never leaves your local machine and you never hit token quota limits.

![as-agent-gemma2.gif](https://developer.android.com/static/blog/assets/as_agent_gemma2_89c9104c58_1hTG1Y.webp) Choose the Gemma model you'd like to download and use.

### **Parallel Agents UX notifications and other enhancements**

In Android Studio Quail 2 we brought you [agentic multitasking with parallel chats](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent). And now Android Studio Quail 4 brings a several UI enhancements designed to make your AI interactions smoother, faster, and more transparent:

- **Hyperlinked code symbols in responses:** Class names, functions, methods, and file paths mentioned in agent responses are now automatically detected and rendered as clickable hyperlinks.
- **Real-time background agent notifications:** When multitasking with parallel chats, the **Recent Chats** panel now provides at-a-glance status indicators. You'll see a loading spinner when an agent is actively running tools, a red status indicator if an agent is waiting for your input, and a blue badge when a background task has finished and is ready for review.
- **Unified Summary of Changes:** After the agent completes a multi-step coding task, the separate **Task** and **Walkthrough** artifacts are now consolidated into a clean, dedicated **Summary of Changes** tab, giving you a clear diff and review experience before applying modifications.
- **Collapsible thought process rendering:** For reasoning models, the agent's step-by-step thinking process is neatly organized into collapsible blocks, keeping your chat conversation easy to scan while allowing you to inspect the underlying logic on demand.

![Qual4InlineAsset_Canavs.png](https://developer.android.com/static/blog/assets/Qual4_Inline_Asset_Canavs_367ae7672f_ZcsFEm.webp) You can now monitor the progress of parallel chats in real time in the Recent Chats panel

### **Upgrade for premium AI capabilities**

Android Studio gives developers access to a default Gemini model out-of-the-box. We adjust the capabilities of this model dynamically to ensure we're able to provide a great experience at no cost. However, if you want more granular access to Gemini's most powerful models or need additional quota for long coding sessions, you can upgrade your access using one of these 3 routes:

- **API Key:** Use the latest Gemini models, such as Gemini 3.7 Flash, in your development flow as soon as they are available with your [Google AI Studio API key](https://developer.android.com/studio/gemini/add-api-key). You can also use the [API key from other model providers](https://developer.android.com/studio/gemini/use-a-remote-model) like Anthropic or OpenAI right in Android Studio
- **Google AI plan:** Developers with a [Google AI Pro or Ultra plan](https://one.google.com/ai?g1_landing_page=75&utm_source=android_studio&utm_campaign=android_studio_settings&pli=1) can log in with their Google account to automatically unlock premium capacity and higher rate limits. With its expanded capabilities, Gemini can help you with analyzing, refactoring, and planning features across massive codebases.
- **Gemini Enterprise:** If your organization has access to [Gemini Enterprise](https://cloud.google.com/gemini-enterprise), Developers can log in to leverage the privacy and security benefits of Google Cloud while using the Android Studio AI agent. This is rolling to select organizations, and is currently available in the latest Android Studio [Canary](http://d.android.com/studio/preview/features#gemini-enterprise).

### **A Look Back: The Android Studio Quail Series Recap**

The Android Studio Quail 4 release continues our focus on accelerating developer productivity with AI. Check out our previous blog posts to learn more about the new features that recently landed.

#### [**Android Studio Quail**](https://android-developers.googleblog.com/2026/05/whats-new-android-developer-tools.html)

- **App Quality Insights Agent Integration:** We kicked off the Android Studio Quail cycle by integrating **App Quality Insights (AQI)** with Gemini.
- **Released in Android Studio Quail (Canary) at Google I/O:** We introduced tools built for the agentic era, including Agent Skills, Firebase integration and parallel conversations in Agent Mode, local model support with Gemma 4, Android CLI, peer-to-peer Android Emulator multi-device testing, ADB Wi-Fi 2.0, and native Google Play testing track publishing.

#### [**Android Studio Quail 2**](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

- **Parallel Chats:** We unlocked concurrent multitasking in the IDE. Developers can open multiple chats as side-by-side **Editor Tabs**---running a Compose refactor in one tab using Gemini 3.5 Flash while documenting code in a second tab with Gemma 4 in parallel. Active background tasks are easily monitored via real-time progress indicators (loading spinners, paused statuses, and errors) in the Recent Chats sidebar.
- **LeakCanary Profiling:** We natively integrated LeakCanary directly into the Android Studio Profiler. By lifting and shifting JVM heap analysis off the test device and running the Shark analyzer engine on your host computer, memory leak tracing became **five times faster** and completely jank-free, backed by **"Fix with Agent"** AI remediations.

#### [**Android Studio Quail 3**](https://developer.android.com/studio/releases/past-releases/as-quail-3-release-notes)

- **Simplified Planning Mode:** When using the /plan command or switching your conversation to "Planning," the agent steps back to evaluate its logic, mapping out an implementation plan before writing code.
- **MCP Marketplace:** Navigating to Settings \> Tools \> AI \> MCP Servers now lets you easily search, install, and manage Model Context Protocol (MCP) servers straight from the IDE, allowing you to connect your AI agent to external developer tools, registries, and custom databases.

### **Get Started Today**

Android Studio Quail 4 is now available in the stable channel. Ditch the manual configuration, multitask across parallel threads, and build with expert-grounded AI intelligence.

👉[**Download Android Studio Quail 4 Stable Today**](https://developer.android.com/studio)

As always, your feedback shapes the future of Android development. Please check out[known issues](https://developer.android.com/studio/known-issues) or file bug reports and feature requests directly on our[official bug tracker](https://developer.android.com/studio/report-bugs).

You can also join our vibrant developer community and stay up-to-date with the latest insights by following us on [Instagram](https://www.instagram.com/androiddev/),[LinkedIn](https://www.linkedin.com/showcase/androiddev),[YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or[X](https://twitter.com/androidstudio). We can't wait to see what you build!
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [#Android Skills](https://developer.android.com/blog/topics/android-skills)
Written by:

-

  ## [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/amman-asfaw) ![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp) ![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)
Continue reading
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 16 Jul 2026 16 Jul 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_ZzldHB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent) Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 3 min read
  - [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
  - [# Quail 2](https://developer.android.com/blog/topics/quail-2)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 2 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)