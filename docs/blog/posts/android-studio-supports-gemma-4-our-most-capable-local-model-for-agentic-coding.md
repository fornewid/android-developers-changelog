---
title: https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding
url: https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Android Studio supports Gemma 4: our most capable local model for agentic coding

2-min read ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp) 02 Apr 2026 [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) Product Manager Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced [the ability to choose any local or remote AI model to power AI functionality in Android Studio,](https://android-developers.googleblog.com/2026/01/llm-flexibility-agent-mode-improvements.html) and today, we're announcing the availability of [Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/) for AI coding assistance in Android Studio. This new local model trained on Android development provides the best of both worlds: the privacy and cost-efficiency of on-device processing alongside state-of-the-art reasoning and tool-calling capabilities.

### AI assistance, locally delivered

By running locally on your machine, Gemma 4 gives you AI code assistance that doesn't require an internet connection or an API key for its core operations. Key benefits include:

- **Privacy and security:** Your code stays on your machine. Gemma 4 processes all Agent Mode requests locally, making it an ideal choice for developers working with data privacy requirements or in secure corporate environments.
- **Cost efficiency:** Run complex agentic workflows without worrying about hitting quotas. Gemma 4 is optimized to run efficiently on modern development hardware, utilizing local GPU and RAM to provide snappy, responsive assistance.
- **Offline availability:** Use the agent to write code even when you don't have an internet connection.
- **State-of-the-art reasoning:** Gemma 4 delivers best-in-class reasoning, capable of complex multi-step coding tasks in Agent Mode.

### Powerful agentic coding

Gemma 4 was trained for Android development with agentic tool calling capabilities. When you select Gemma 4 as your local model, you can leverage Agent Mode for a variety of development use cases, such as:

- **Designing new features:** Developers can ask the agent to build a new feature or an entire app with commands like "build a calculator app" and the agent will not only generate the UI code but will use Android best practices like writing in Kotlin and using Jetpack Compose.
- **Refactoring:** You can give high-level commands such as "Extract all hardcoded strings and migrate them to strings.xml." The agent will scan your codebase, identify instances requiring changes, and apply the edits across multiple files simultaneously.
- **Bug fixing and build resolution:** If a project fails to build or has persistent lint errors, you can prompt the agent to "Build my project and fix any errors." The agent will navigate to the offending code and iteratively apply fixes until the build is successful.

[Video](https://www.youtube.com/watch?v=4iPn1qRVsNY)

### Recommended hardware requirements

The 26B MoE is recommended for Android app developers using a machine with the minimum hardware requirements. Total RAM needed includes both Android Studio and Gemma.

| Model | Total RAM needed | Storage needed |
|---|---|---|
| Gemma E2B | 8GB | 2 GB |
| Gemma E4B | 12 GB | 4 GB |
| Gemma 26B MoE | 24 GB | 17 GB |

### Get started

To get started, ensure you have the latest version of **Android Studio** installed.

1. Install an LLM provider, such as [LM Studio](https://lmstudio.ai/) or [Ollama](https://ollama.com/), on your local computer.
2. In **Settings \> Tools \> AI \> Model Providers** add your LM Studio or Ollama instance.
3. ![large_Screenshot_gemma4.png](https://developer.android.com/static/blog/assets/large_Screenshot_gemma4_e5d1d69bf8_2an2Nb.webp)
4. Download the Gemma 4 model from [Ollama](https://ollama.com/library?sort=newest&q=gemma) or [LM Studio](https://lmstudio.ai/models). Refer to hardware requirements for model size selection.
5. In Agent Mode, select **Gemma 4** as your active model.

For a detailed walkthrough on configuration, check out the official documentation on [how to use a local model](https://developer.android.com/studio/gemini/use-a-local-model).

We are excited to see how Gemma 4 enables more private, secure, and powerful development workflows. As always, your feedback is essential as we continue to refine the AI experience in Android Studio. If you find a bug or issue, please [file an issue](https://developer.android.com/studio/report-bugs). Also you can be part of our vibrant Android developer community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://x.com/androidstudio). Happy coding!
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Written by:

-

  ## [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-warner) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)
Continue reading
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 16 Jul 2026 16 Jul 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_ZzldHB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent) Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 3 min read
  - [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
  - [# Quail 2](https://developer.android.com/blog/topics/quail-2)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
- [![View Matt Dyor's profile](https://developer.android.com/static/blog/assets/matt_dyor_b779fca40e_Z2hl456.webp)](https://developer.android.com/blog/authors/matt-dyor) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow_forward](https://developer.android.com/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3) Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.
  [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) • 3 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)