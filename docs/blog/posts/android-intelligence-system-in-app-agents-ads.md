---
title: https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads
url: https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# From in-app agents to the Android intelligence system: What's new in intelligent apps at the Android Developer Summit

4 min read ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) 05 Nov 2026 [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi) [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) Developer Relations Manager In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices. To help you meet users where they are, we're unlocking new ways to build intelligent, agentic experiences in your Android apps:

- **Connect with the Android intelligence system:** Share your app's capabilities with the system agent with Android MCP. To let users connect directly with your app through the Gemini app and Google Search on Android, join the Connected Apps Platform preview program.
- **Bring intelligence into your app:**Build smart features and agents on-device with ML Kit GenAI APIs, bring your custom ML model with LiteRT in Google Play services. Leverage Gemini models on the Cloud with Firebase AI Logic, and enable your agent to build native Compose UI with the A2UI Compose renderer.

You've already seen some of these new APIs and developer tools at the [Android Developer Summit keynote](https://youtu.be/8Lmv7LGgL4E). Now, learn with our new deep-dive resources to help you build intelligent apps, including [10 new on-demand sessions](https://goo.gle/ADS26-Intelligent-Apps) around new intelligent experiences.

## Connect with the Android intelligence system

The Android intelligence system is the system foundation designed to protect users while connecting AI agents with apps on Android devices. It provides users with both prompted assistance and proactive assistance across the Android ecosystem of devices spanning phones, wearables, XR glasses, TVs, and automobiles.

- **Prompted assistance** : When the user actively asks an agent to fulfill a goal (for example, "check my calendar, book a ride, and message Jingyu my ETA"), the agent orchestrates tools across apps to get it done. For the fastest, most reliable execution, you can use a [remote MCP](https://developers.google.com/connected-apps/mcp) server or local [Android MCP](https://developer.android.com/ai/appfunctions). Agents can also fall back to using Android's [Computer Control framework](https://developer.android.com/ai/computer-control) to complete actions without requiring any app-side integration.
- **Proactive assistance**: The system anticipates the user's needs and surfaces contextual suggestion chips directly on lock screens, notifications, virtual keyboards, and within apps.

We give you control over how your apps [integrate with the Android intelligence system](https://developer.android.com/ai/intelligence-system) by providing APIs and tools based on the familiar [MCP](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) standard. [Android MCP](https://developer.android.com/ai/appfunctions), powered by the [AppFunctions Jetpack library](https://developer.android.com/jetpack/androidx/releases/appfunctions), is our unified tool-calling framework. It lets you connect with qualified AI agents right on the device, whether the system agent or your own on-device in-app agent. Remote MCP server provides you with cross-platform reach.

Android MCP complements remote MCP as an Android native solution and is the recommended integration path when your user journey uses end-to-end encryption or sensitive local device data, requires device sensors and hardware, needs to execute locally, or when there's no server endpoint available.

To learn more about the Android intelligence system and integrate with Gemini as the system agent, watch this talk:
[Video](https://www.youtube.com/watch?v=UsqDEfyOH2E)

## Bring intelligence into your apps: from on-device agent to A2UI Compose renderer

With new capabilities available in Gemini Nano 4 like function calling, we are expanding the ML Kit GenAI APIs to build agentic workflows entirely on-device. We provide you the building blocks directly with ML Kit's [direct model access](https://developers.google.com/ml-kit/genai/prompt/android) with Prompt API and the new [Agentic API](https://developers.google.com/ml-kit/genai/agent/android) that auto-executes functions for you, saves conversation history, manages the orchestration loop, and includes automatic guardrails. Check out the [Jetpacker code sample on GitHub](https://github.com/android/ai-samples/tree/main/jetpacker) and watch this video for a deep dive into how you can unlock agentic capabilities in your app with ML Kit GenAI APIs:
[Video](https://www.youtube.com/watch?v=tAy7IifZXG0)

Besides the new Agentic APIs, we are bringing a suite of new capabilities on-device:

- Get an overview of [on-device ML Kit GenAI APIs](https://youtu.be/p-SZ1rWvErU?si=fjNFcsIOc7mufrws), from Prompt API features like [thinking mode](https://developers.google.com/ml-kit/genai/prompt/android/thinking-mode) and [system instructions](https://developers.google.com/ml-kit/genai/prompt/android/system-instructions) to new alpha APIs like the [Embeddings API](https://developers.google.com/ml-kit/genai/embedding/android), powered by [EmbeddingGemma 2](https://huggingface.co/google/embeddinggemma-2). You'll also learn about under-the-hood Android system optimizations and see common on-device GenAI use cases already in production.
- Take a [deep dive into the model architecture](https://youtu.be/ekS4_gV6Ojc?si=tb5P_Cdslh_r85YQ) of Gemini Nano 4, built on Gemma 4. Powered by per-layer embeddings, quantization-aware training, and multi-token prediction, Gemini Nano 4 delivers to 3x inference speedup while cuts memory usage by up to 4x compared to the previous version of Gemini Nano model under internal testing benchmarks.
- You can run your custom ML models with faster GPU performance using [LiteRT in Google Play services](https://developer.android.com/ai/custom) which removes the runtime from your APK making your APK about 8 MB smaller. Now also available on Wear OS and Android Automotive OS. Whether you are using the turn-key ML Kit APIs or bring your own custom edge model, read the[announcement](https://developers.googleblog.com/smaller-apps-and-faster-gpu-inference-with-litert-in-google-play-services/) and check out this [talk](https://youtu.be/LiBWWJ9IKag?si=1W7NnRg90Bgjwhwc).
- See how these APIs come together in real-world apps, from an [XR language teacher](https://youtu.be/tW3mg0iyi_w?si=6pZugc8ifajQJTKy) using the ML Kit [speech recognition](https://developers.google.com/ml-kit/genai/speech-recognition/android), [speech translation](https://developers.google.com/ml-kit/genai/speech-translation/android), and [text-to-speech](https://developers.google.com/ml-kit/genai/text-to-speech/android) APIs on phones and smart glasses, to a [Formula E AI co-driver](https://youtu.be/nV63eqjPeEI?si=Uzj9_8bjHzww5sRv) built with Gemini Nano, ML Kit direct model access, and the [Agent Development Kit (ADK)](https://developer.android.com/ai/adk).

For workflows that span cloud and local processing, [Firebase AI Logic](https://youtu.be/IPKerNnpddQ?si=1Io0uYXxpHAiSTLO) offers a straightforward hybrid solution. You can call advanced cloud models like Gemini 4 while using on-device inference with Gemini Nano when available. To protect your app and manage costs in production, use [Firebase App Check](https://firebase.google.com/docs/app-check), the new [server prompt templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started), and Firebase spend caps.

As showcased in the keynote demo with Jetpacker's live booking assistant, the Jetpack Compose A2UI renderer is now available in alpha to help your agents "speak UI". Your agents can stream rich, interactive native Compose UIs directly from a JSON protocol. Get started with the [A2UI Compose](https://goo.gle/a2ui-compose-docs) renderer and give us your feedback. Watch this [talk](https://youtu.be/qIvsFGvlHdo?si=3fbzopiUlyPj0mws)to see how to implement it in your app.

## Reach across Gemini and Search with Connected Apps Platform

Across Google surfaces, users are shifting from asking questions to taking action. We introduced the [Connected Apps Platform](https://developers.google.com/connected-apps) so you can reach high-intent users across Gemini and Search, combining Android MCP for native on-device execution with remote MCP servers for cross-platform reach. You can start building and testing locally today with [Gemini Apps Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode). When you're ready for production, [join the preview waitlist](https://goo.gle/connected-apps-interest); preview capacity is currently limited to selected production-ready apps in supported categories, with broader self-serve access coming later.

To walk you through building, testing, and publishing your first Connected App, watch Extend your app to Gemini and Search with the Connected Apps Platform.
[Video](https://www.youtube.com/watch?v=-4G-4w9FKDw)

## Start building intelligent apps with the latest updates

To start building, create on-device agents with [ML Kit agentic workflows](https://developers.google.com/ml-kit/genai/agent/android) alongside [direct model access](https://developers.google.com/ml-kit/genai/prompt/android) with new Android [skills](https://github.com/android/skills/tree/main/device-ai). Make sure you opt in to the [AIcore Developer Preview program](https://developers.google.com/ml-kit/genai/aicore-dev-preview) when testing with new capabilities in preview models. Bring intelligent features to your app with ML Kit APIs and run custom ML models with LiteRT in Google Play Services. Run Inference with Gemini models in the cloud with [Firebase AI Logic](https://developer.android.com/ai/gemini) directly and stream native Compose UIs from JSON using the [Jetpack Compose A2UI renderer](https://goo.gle/a2ui-compose-docs). Finally, integrate with the Android intelligence system, prototype with Android MCP using the AppFunctions [skill and sample agent](https://developer.android.com/ai/appfunctions#skills-and-samples) and sign up for the [Connected Apps Platform developer preview](https://goo.gle/connected-apps-interest).

We can't wait to see what you build!
- [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
Written by:

-

  ## [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi)

  ###### Developer Relations Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/jingyu-shi) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)
Continue reading
- [![View Fahd Imtiaz's profile](https://developer.android.com/static/blog/assets/Fahd_Imtiaz_259fcb7c47_Z2vO4ST.webp)](https://developer.android.com/blog/authors/fahd-imtiaz)[![View Loryn Hairston's profile](https://developer.android.com/static/blog/assets/unnamed_13_777347786d_24gdiI.webp)](https://developer.android.com/blog/authors/loryn-hairston) 22 Sep 2026 22 Sep 2026 ![](https://developer.android.com/static/blog/assets/Googlebook_Blog_Strapi_4a4a7d3291_Z1ReCnu.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Land your apps on Googlebook with adaptive development](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development)

  [arrow_forward](https://developer.android.com/blog/posts/land-your-apps-on-googlebook-with-adaptive-development) Googlebook introduces a new category of laptops built on a shared Android foundation. High-performance hardware from partners such as HP, Dell, Lenovo, Acer, and Asus, combines mobile convenience with desktop power.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston) • 4 min read
  - [#Googlebook](https://developer.android.com/blog/topics/googlebook)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +1 ↩
- [![View Nick Butcher's profile](https://developer.android.com/static/blog/assets/Nick_Butcher_5393f4552a_2d47S.webp)](https://developer.android.com/blog/authors/nick-butcher) 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Social_Android_Jetpack_Compose_January_24_ba31d9063b_ZrjgNw.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose August '26 release](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/what-s-new-in-the-jetpack-compose-august-26-release) Today, the Jetpack Compose August '26 release is stable!
  [Nick Butcher](https://developer.android.com/blog/authors/nick-butcher) • 5 min read
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
- 3 Authors 11 Aug 2026 11 Aug 2026 ![](https://developer.android.com/static/blog/assets/Strapi_2ca09e764b_1JLHid.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Enhance your app for the new Pixel lineup: Unveiled at Made by Google](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google)

  [arrow_forward](https://developer.android.com/blog/posts/enhance-your-app-for-the-new-pixel-lineup-unveiled-at-made-by-google) With the introduction of the Pixel 11 Pro Fold, Pixel Watch 5, and the entire Pixel family, users are moving seamlessly across diverse screen sizes, unique postures, and intelligent experiences.
  [Fahd Imtiaz](https://developer.android.com/blog/authors/fahd-imtiaz), [Loryn Hairston](https://developer.android.com/blog/authors/loryn-hairston), [Tracy Agyemang](https://developer.android.com/blog/authors/tracy-agyemang) • 4 min read
  - [#Wear OS 7](https://developer.android.com/blog/topics/wear-os-7)
  - [#made by google](https://developer.android.com/blog/topics/made-by-google)
  - [#Adaptive development](https://developer.android.com/blog/topics/adaptive-development)
  - [#Gemini Nano 4](https://developer.android.com/blog/topics/gemini-nano-4)
  - [#ML Kit Prompt API](https://developer.android.com/blog/topics/ml-kit-prompt-api)
  - [#Foldables](https://developer.android.com/blog/topics/foldables)
  - [#Jetpack Compose](https://developer.android.com/blog/topics/jetpack-compose)
  - +5 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)