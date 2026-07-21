---
title: https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26
url: https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Top AI on Android updates for building intelligent experiences from Google I/O '26

2-min read ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp) 26 May 2026 [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) Staff Developer Relations Engineer At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps. If you missed these updates, check out our quick recap video here:
[Video](https://www.youtube.com/watch?v=TZNu9u9TfN4)

#### 1. **Putting your apps at the center of the intelligence system**

The Android OS already enables agents like [Gemini](https://www.android.com/gemini-intelligence/?utm_source=blog.google&utm_medium=owned&utm_campaign=next) to complete task automation, where it can navigate an app on the users behalf.

[AppFunctions](https://developer.android.com/ai/appfunctions) (Android MCP) provides you with more control over how your app integrates with the intelligence system. This new platform API and Jetpack library are currently available in experimental preview.

- **Android MCP:** AppFunctions allows your application to act as an on-device Model Context Protocol (MCP) server. It means you seamlessly share your app's tools, services and data to the system and agents.
- **Streamlined Development:** You can leverage the new [skill](https://github.com/android/skills/tree/main/device-ai/appfunctions) to easily generate AppFunctions within your codebase.
- **Exploration and Testing:** We've released a new [test agent](https://github.com/android/appfunctions/releases) that allows you to experiment and debug your AppFunctions in a simulated agent environment.

|---|
| **Early Access Program** : Want to be among the first apps to deploy app functions in production? [Join](https://docs.google.com/forms/d/e/1FAIpQLScEoIsgzE-LbgRrYcQMc-Lit_5VlKRA0iWw7Pvg1brIc8wXAw/viewform) our early access program today! |

To see it in action, check out the live demo showcased during the *What's New in Android* presentation.
[Video](https://www.youtube.com/watch?v=2K7VVAMUYPw)

#### 2. **On-Device Power with Gemini Nano 4 Preview**

Last month, we launched [Gemma 4](https://android-developers.googleblog.com/2026/04/gemma-4-new-standard-for-local-agentic-intelligence.html), our state-of-the-art open models. You can already preview and prototype with the next generation of Gemini Nano (Nano 4) models with the [AIcore developer preview](https://developers.google.com/ml-kit/genai/aicore-dev-preview). To make productionizing with Gemini Nano more reliable and performant, we are adding a few new features in **ML Kit GenAI APIs**:

- **Prototype to Production:** Transition from prototyping in the AICore Developer Preview to building production-ready apps using the ML Kit GenAI [**Prompt API**](https://developers.google.com/ml-kit/genai/prompt/android/get-started) to leverage Gemini Nano 4 that's launching in flagship devices later this year.
- **Structured Output:** The upcoming Structured Output API will allow you to define object classes to be returned as outputs from Prompt API, ensuring reliable outputs in productionizing your intelligent features.
- [**Prefix Caching**](https://developers.google.com/ml-kit/genai/prompt/android/prefix-caching)**:** It optimizes your on-device inference performance with the prompt API. The new Prefix caching reduces inference time by storing and reusing the intermediate LLM state of processing a shared and recurring part of the prompt.

For highly customized or niche use cases, you can also use **LiteRT-LM** to [bring your own](https://youtu.be/boy-UjB8hpA?si=MCPddRD7eblz8ICr) fine-tuned small language model to Android.
[Video](https://www.youtube.com/watch?v=Z7zx_sTbFPI)

#### **3. Hybrid Inference \& Agents**

To help you build more advanced AI features like hybrid inference and explore building in-app agents, we've released new APIs, framework and guidances:

- [**Firebase AI Logic Hybrid Inference**](https://android-developers.googleblog.com/2026/04/Hybrid-inference-and-new-AI-models-are-coming-to-Android.html)**:** This new API provides the simple routing capability between on-device models and powerful cloud infrastructure. You can set explicit orchestration modes, such as `PREFER_ON_DEVICE`, `PREFER_CLOUD`, `ONLY_ON_DEVICE`, or `ONLY_CLOUD`, based on your need.
- **A2UI Jetpack Compose Renderer:** The new A2UI library allows your agents to "speak UI". With the upcoming Jetpack Compose Renderer, you can automatically render these A2UI messages as native UI components.
- [**ADK for Android**](https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/): The first version of ADK for Android is available for experimentation. It allows you to build multi-agent workflows across both on-device and Cloud models while managing orchestration, context handling and sessions between agents.

From building with on-device models, exploring hybrid inference to building agents, you can see them in action in this talk:
[Video](https://www.youtube.com/watch?v=_iuXykdlTkk)

### **Start Building Today**

Whether you are experimenting with AppFunctions to prepare for the intelligence system, or looking to bring the power of Google's AI within your own app, we've got you covered. Dive deeper into the code snippets, samples and comprehensive developer guides on the Android AI [hub](https://developer.android.com/ai). For the full breakdown of what's new, check out the official **AI on Android at Google I/O 2026** [playlist](https://www.youtube.com/playlist?list=PLWz5rJ2EKKc-GL3584TkxUyoPfzPkB1mV).

We are excited to see what you build!
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [#Android](https://developer.android.com/blog/topics/android)
- [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
- [#On-device](https://developer.android.com/blog/topics/on-device)
Written by:

-

  ## [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi)

  ###### Staff Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jingyu-shi) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)
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
- [![View Luke Hopkins's profile](https://developer.android.com/static/blog/assets/Luke_Hopkins_9c1e15d778_Z2o9b3q.webp)](https://developer.android.com/blog/authors/luke-hopkins)[![View Ryan Bartley's profile](https://developer.android.com/static/blog/assets/Ryan_Bartley_35cf836cd8_ZgTUAO.webp)](https://developer.android.com/blog/authors/ryan-bartley) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo3_Strapi_2000x1000_56726aebea_Z1kvKHr.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android XR Updates for Unity, Unreal, and Godot](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot)

  [arrow_forward](https://developer.android.com/blog/posts/android-xr-updates-for-unity-unreal-and-godot) We are excited to announce that official support for Unreal Engine and Godot has arrived for Android XR. We are also launching new tools designed to boost your productivity and enable new XR capabilities: the Android XR Engine Hub and the Android XR Interaction Framework.
  [Luke Hopkins](https://developer.android.com/blog/authors/luke-hopkins), [Ryan Bartley](https://developer.android.com/blog/authors/ryan-bartley) • 4 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Game engine development](https://developer.android.com/blog/topics/game-engine-development)
  - +1 ↩
- [![View Paul Feng's profile](https://developer.android.com/static/blog/assets/paul_feng_759ac95845_spvRU.webp)](https://developer.android.com/blog/authors/paul-feng) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/IO_26_Blog_Strapi_Icons_2000x1000px_0a8b06b49b_Z1e2APA.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [I/O 2026: What's new in Google Play](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)

  [arrow_forward](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play) At this year's Google I/O, we talked about our evolving business model that offers more choice and new ways for your apps and content to be discovered on and off the store. We also unveiled advanced tools and insights that will help scale your business with less complexity.

  [Paul Feng](https://developer.android.com/blog/authors/paul-feng) • 6 min read
  - [#Google Play](https://developer.android.com/blog/topics/google-play)
  - [#Play Console](https://developer.android.com/blog/topics/play-console)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android Developers](https://developer.android.com/blog/topics/android-developers)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)