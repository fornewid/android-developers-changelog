---
title: https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads
url: https://developer.android.com/blog/posts/android-intelligence-system-in-app-agents-ads
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news.md.txt)

# What's new in intelligent apps at the Android Developer Summit

4 min read ![Dark promotional banner with the phrase 'intelligent apps' displayed in bold white font in the center. In the bottom-right corner, a glossy, metallic 3D Android robot head peaks upward. The dark background is filled with repeating technical terms and API names related to Android artificial intelligence, including 'A2UI', 'Android MCP', 'Gemini Nano', 'ML Kit', 'AICore', and 'Connected Apps Platform'.](https://developer.android.com/static/blog/assets/ADS_Intelligent_Aps_df6b69d7ef_HGStR.webp) 05 Nov 2026 [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi.md.txt) [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt) Developer Relations Manager In the intelligence era, users are no longer just tapping through apps, they express high-level goals and expect AI agents like Gemini to complete multi-step workflows, sometimes across multiple apps on their devices. To help you meet users where they are, we're unlocking new ways to build intelligent, agentic experiences in your Android apps:

- **Connect with the Android intelligence system:** Share your app's capabilities with Android MCP. To let users connect directly with your app through the Gemini app and Google Search on Android, join the Connected Apps Platform preview program.
- **Bring intelligence into your app:**Build smart features and agents on-device with ML Kit GenAI APIs, bring your custom ML model with LiteRT in Google Play services. Leverage Gemini models on the Cloud with Firebase AI Logic, and enable your agent to build native Compose UI with the A2UI Compose renderer.

You've already seen some of these new APIs and developer tools at the [Android Developer Summit keynote](https://youtu.be/8Lmv7LGgL4E). Now, learn with our new deep-dive resources to help you build intelligent apps, including [10 new on-demand sessions](https://goo.gle/ADS26-Intelligent-Apps) around new intelligent experiences.

## Connect with the Android intelligence system

The Android intelligence system is the system foundation designed to protect users while connecting AI agents with apps on Android devices. It provides users with both prompted assistance and proactive assistance across the Android ecosystem of devices spanning phones, wearables, XR glasses, TVs, and automobiles.

- **Prompted assistance** : When the user actively asks an agent to fulfill a goal (for example, "check my calendar, book a ride, and message Jingyu my ETA"), the agent orchestrates tools across apps to get it done. For the fastest, most reliable execution, you can use a [remote MCP](https://developers.google.com/connected-apps/mcp) server or local [Android MCP](https://developer.android.com/ai/appfunctions.md.txt). Agents can also fall back to using Android's [Computer Control framework](https://developer.android.com/ai/computer-control.md.txt) to complete actions without requiring any app-side integration.
- **Proactive assistance**: The system anticipates the user's needs and surfaces contextual suggestion chips directly on lock screens, notifications, virtual keyboards, and within apps.

We give you control over how your apps [integrate with the Android intelligence system](https://developer.android.com/ai/intelligence-system.md.txt) by providing APIs and tools based on the familiar [MCP](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro) standard. [Android MCP](https://developer.android.com/ai/appfunctions.md.txt), powered by the [AppFunctions Jetpack library](https://developer.android.com/jetpack/androidx/releases/appfunctions.md.txt), is our unified tool-calling framework. It lets you connect with AI agents right on the device.

Remote MCP server provides you with cross-platform reach. Android MCP complements remote MCP as an Android native solution and is the recommended integration path when your user journey uses end-to-end encryption or sensitive local device data, requires device sensors and hardware, needs to execute locally, or when there's no server endpoint available.

You can integrate your app with Gemini using remote MCP, Android MCP or both depending on your use case. Learn more below:
[Video](https://www.youtube.com/watch?v=UsqDEfyOH2E)

## Bring intelligence into your apps: from on-device agent to A2UI Compose renderer

With new capabilities available in Gemini Nano 4 like function calling, we are expanding the ML Kit GenAI APIs to build agentic workflows entirely on-device. We provide you the building blocks directly with ML Kit's [direct model access](https://developers.google.com/ml-kit/genai/prompt/android) with Prompt API and the new [Agentic API](https://developers.google.com/ml-kit/genai/agent/android) that auto-executes functions for you, saves conversation history, manages the orchestration loop, and includes automatic guardrails. Check out the [Jetpacker code sample on GitHub](https://github.com/android/ai-samples/tree/main/jetpacker) and watch this video for a deep dive into how you can unlock agentic capabilities in your app with ML Kit GenAI APIs:
[Video](https://www.youtube.com/watch?v=tAy7IifZXG0)

Besides the new Agentic APIs, we are bringing a suite of new capabilities on-device:

- Get an overview of [on-device ML Kit GenAI APIs](https://youtu.be/p-SZ1rWvErU?si=fjNFcsIOc7mufrws), from Prompt API features like [thinking mode](https://developers.google.com/ml-kit/genai/prompt/android/thinking-mode) and [system instructions](https://developers.google.com/ml-kit/genai/prompt/android/system-instructions) to new alpha APIs like the [Embeddings API](https://developers.google.com/ml-kit/genai/embedding/android), powered by [EmbeddingGemma 2](https://huggingface.co/google/embeddinggemma-2). You'll also learn about under-the-hood Android system optimizations and see common on-device GenAI use cases already in production.
- Take a [deep dive into the model architecture](https://youtu.be/ekS4_gV6Ojc?si=tb5P_Cdslh_r85YQ) of Gemini Nano 4, built on Gemma 4. Powered by per-layer embeddings, quantization-aware training, and multi-token prediction, Gemini Nano 4 delivers to 3x inference speedup while cuts memory usage by up to 4x compared to the previous version of Gemini Nano model under internal testing benchmarks.
- You can run your custom ML models with faster GPU performance using [LiteRT in Google Play services](https://developer.android.com/ai/custom.md.txt) which removes the runtime from your APK making your APK about 8 MB smaller. Now also available on Wear OS and Android Automotive OS. Whether you are using the turn-key ML Kit APIs or bring your own custom edge model, read the[announcement](https://developers.googleblog.com/smaller-apps-and-faster-gpu-inference-with-litert-in-google-play-services/) and check out this [talk](https://youtu.be/LiBWWJ9IKag?si=1W7NnRg90Bgjwhwc).
- See how these APIs come together in real-world apps, from an [XR language teacher](https://youtu.be/tW3mg0iyi_w?si=6pZugc8ifajQJTKy) using the ML Kit [speech recognition](https://developers.google.com/ml-kit/genai/speech-recognition/android), [speech translation](https://developers.google.com/ml-kit/genai/speech-translation/android), and [text-to-speech](https://developers.google.com/ml-kit/genai/text-to-speech/android) APIs on phones and smart glasses, to a [Formula E AI co-driver](https://youtu.be/nV63eqjPeEI?si=Uzj9_8bjHzww5sRv) built with Gemini Nano, ML Kit direct model access, and the [Agent Development Kit (ADK)](https://developer.android.com/ai/adk.md.txt).

For workflows that span cloud and local processing, [Firebase AI Logic](https://youtu.be/IPKerNnpddQ?si=1Io0uYXxpHAiSTLO) offers a straightforward hybrid solution. You can call advanced cloud models like Gemini 4 while using on-device inference with Gemini Nano when available. To protect your app and manage costs in production, use [Firebase App Check](https://firebase.google.com/docs/app-check), the new [server prompt templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started), and Firebase spend caps.

As showcased in the keynote demo with Jetpacker's live booking assistant, the Jetpack Compose A2UI renderer is now available in alpha to help your agents "speak UI". Your agents can stream rich, interactive native Compose UIs directly from a JSON protocol. Get started with the [A2UI Compose](https://goo.gle/a2ui-compose-docs) renderer and give us your feedback. Watch this [talk](https://youtu.be/qIvsFGvlHdo?si=3fbzopiUlyPj0mws)to see how to implement it in your app.

## Reach across Gemini and Search with Connected Apps Platform

Across Google surfaces, users are shifting from asking questions to taking action. We introduced the [Connected Apps Platform](https://developers.google.com/connected-apps) so you can reach high-intent users across Gemini and Search, combining Android MCP for native on-device execution with remote MCP servers for cross-platform reach. You can start building and testing locally today with [Gemini Apps Developer Mode](https://developers.google.com/connected-apps/mcp/dev-mode). When you're ready for production, [join the preview waitlist](https://goo.gle/connected-apps-interest); preview capacity is currently limited to selected production-ready apps in supported categories, with broader self-serve access coming later.

To walk you through building, testing, and publishing your first Connected App, watch Extend your app to Gemini and Search with the Connected Apps Platform.
[Video](https://www.youtube.com/watch?v=-4G-4w9FKDw)

## Start building intelligent apps with the latest updates

To start building, create on-device agents with [ML Kit agentic workflows](https://developers.google.com/ml-kit/genai/agent/android) alongside [direct model access](https://developers.google.com/ml-kit/genai/prompt/android) with new Android [skills](https://github.com/android/skills/tree/main/device-ai). Make sure you opt in to the [AIcore Developer Preview program](https://developers.google.com/ml-kit/genai/aicore-dev-preview) when testing with new capabilities in preview models. Bring intelligent features to your app with ML Kit APIs and run custom ML models with LiteRT in Google Play Services. Run Inference with Gemini models in the cloud with [Firebase AI Logic](https://developer.android.com/ai/gemini.md.txt) directly and stream native Compose UIs from JSON using the [Jetpack Compose A2UI renderer](https://goo.gle/a2ui-compose-docs). Finally, integrate with the Android intelligence system, prototype with Android MCP using the AppFunctions [skill and sample agent](https://developer.android.com/ai/appfunctions.md.txt#skills-and-samples) and sign up for the [Connected Apps Platform developer preview](https://goo.gle/connected-apps-interest).

We can't wait to see what you build!
- [#Android MCP](https://developer.android.com/blog/topics/android-mcp.md.txt)
- [#Gemini Nano](https://developer.android.com/blog/topics/gemini-nano.md.txt)
- [#ML Kit](https://developer.android.com/blog/topics/ml-kit.md.txt)
- [#Connected Apps](https://developer.android.com/blog/topics/connected-apps.md.txt)
Written by:

-

  ## [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt)

  ###### Developer Relations Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/jingyu-shi) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp) ![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)
Continue reading
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_Z1OTydP.webp)](https://developer.android.com/blog/authors/jingyu-shi.md.txt) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_Zj9dt4.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26.md.txt) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi.md.txt) • 2 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o.md.txt)
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions.md.txt)
  - [#On-device](https://developer.android.com/blog/topics/on-device.md.txt)
  - +2 ↩
- [![View Michelle Martin's profile](https://developer.android.com/static/blog/assets/unnamed_29_8358471ffe_MSkhy.webp)](https://developer.android.com/blog/authors/michelle-martin.md.txt) 10 Nov 2026 10 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_Sign_in_with_Google_Plugin_for_Unity_Gaming_DESIGN_Header_and_metadata_V01_26433b75fe_Z260GOa.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Powering Seamless Player Sign-In: Introducing the Open-Source Sign in with Google Plugin for Unity](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/open-source-google-sign-in-unity.md.txt) With Unity powering over half of all mobile titles worldwide, first impressions matter. For game developers, a smooth, reliable player onboarding experience is essential to driving day-one retention and long-term engagement.
  [Michelle Martin](https://developer.android.com/blog/authors/michelle-martin.md.txt) • 1 min read
- [![View Amy Zeppenfeld's profile](https://developer.android.com/static/blog/assets/Amyzeppenfeld_50a8b9e7f8_Z17af4b.webp)](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt)[![View Vinny DaSilva's profile](https://developer.android.com/static/blog/assets/unnamed_5_cdab7ecfba_Z1iwWr5.webp)](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) 06 Nov 2026 06 Nov 2026 ![](https://developer.android.com/static/blog/assets/ABL_149_Strapi_A2_B_8fa837edce_1zewyL.webp) [Product News](https://developer.android.com/blog/categories/product-news.md.txt)

  ## [Build for an expanding lineup of Android XR devices with production-ready tools from Android Developer Summit](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-android-xr-devices-tools.md.txt) From full immersion at home to glanceable experiences on the go, building on Android XR lets you meet users at any moment across the entire spectrum of spatial applications. At Android Developer Summit, we marked an exciting milestone with the launch of XREAL AURA.
  [Amy Zeppenfeld](https://developer.android.com/blog/authors/amy-zeppenfeld.md.txt), [Vinny DaSilva](https://developer.android.com/blog/authors/vinny-da-silva.md.txt) • 3 min read
  - [#Android XR](https://developer.android.com/blog/topics/android-xr.md.txt)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)