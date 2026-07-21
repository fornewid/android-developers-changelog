---
title: https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools
url: https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Android Studio I/O Edition: What's new in Android Developer tools

8-min read ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_ZVoYvg.webp) 19 May 2026 [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) Product Manager This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase. So, whether you are building exclusively with AI or you prefer being the architect of every line of code, our tools will keep you ahead of the curve.

As we move from "AI-assisted" to "Agentic" development, we're making it easier than ever to turn a spark of an idea into a high-quality production app with significantly less developer effort.
[Video](https://www.youtube.com/watch?v=N4GgGBKnHe4)

So what's new with Android developer tools? We will cover 3 main areas in this blog:

- **Let your agent handle it:** Whatever development task you are working on, the Android Studio agent can help: from planning the app architecture and design, to writing code, to unit testing and bug fixing.
- **Any AI provider, anywhere you build:** In Android Studio, you can use any model and we even help guide you to the best performing ones. Choose any of the top remote models from Google, Anthropic, OpenAI, or if you need to run locally - Gemma 4 is our most capable and efficient local model! And with Android CLI, you can build Android apps faster and easier using the agents and developer environments of your choice.
- **As always, performance and quality remain top priorities:** We continue to invest in the Android developer tools you love: from the Emulator, to Profilers, performance analyzers, and more!

## 1: Let your agent handle it

### Agent skills

Android Studio now supports [Agent Skills](https://www.youtube.com/watch?v=AhrXPjk22OE&t=148s), modular instruction sets that ground LLMs in specialized workflows and domain-specific knowledge. By adding skills to your project, you can teach the agent to follow specific best practices, architecture patterns, or library workflows. This enables more accurate, context-aware code generation and automated skill activation for an appropriate task, ensuring the agent acts as an expert. We've bundled many of the top Android and Firebase agent skills in the latest Android Studio [Canary](https://developer.android.com/studio/preview) build, so you can skip straight to building!
![Agent_Skills.png](https://developer.android.com/static/blog/assets/Agent_Skills_9633868f1c_26LRVt.webp) Skills in Agent Mode

You can create your own skill, or use [Android CLI](https://developer.android.com/tools/agents/android-skills#android-cli) to install our [official skills](https://github.com/android/skills) - a repository that covers some of the most common workflows that some Android developers and LLMs may struggle with. They help models better understand and execute specific patterns that follow our best practices and guidance on Android development, such as XML to Compose migration, Edge-to-edge, Navigation 3, and more. You can even use skills for Android XR, starting with a beautiful Display Glasses app with Jetpack Compose [Glimmer](https://github.com/android/skills/tree/main/xr/display-glasses-with-jetpack-compose-glimmer).

### Build full-stack apps with Firebase in Agent Mode

Firebase services like Auth and Firestore databases can now be [enabled directly within Agent Mode](https://firebase.blog/posts/2026/05/google-io-2026-announcements) in Android Studio using the [Agent Skills for Firebase](https://firebase.google.com/docs/ai-assistance/agent-skills). Your agent will be able to complete Firebase integration and configure backend services. This integration empowers you to build robust, full-stack Android applications without ever leaving your IDE!
![Firebase_FullStack_apps.png](https://developer.android.com/static/blog/assets/Firebase_Full_Stack_apps_4c025a53da_2lEG6o.webp) Building a full-stack app with Firebase via Agent Mode

### Parallel conversations

You can now run multiple conversations with Agent Mode in parallel. In one conversation, run tests and while you are waiting, you can kick off planning mode for a new feature in your app while using a third conversation thread to write documentation for your app. These improvements will save you time and improve your productivity.
![parallel_threads.png](https://developer.android.com/static/blog/assets/parallel_threads_971ee620f0_rKJb.webp) Parallel conversations in Agent Mode

### A more capable New Project Agent

Android Studio's New Project Agent has evolved into a powerful full-stack development tool, utilizing a multi-step execution plan and an autonomous "generation loop" that self-corrects build errors and configures dependencies across multiple files. This advanced capability is significantly amplified by its new integration with Firebase Agent Skills, allowing developers to seamlessly build, debug, and deploy complete full-stack applications directly from a single prompt to final production.
![NewProjectAgent.png](https://developer.android.com/static/blog/assets/New_Project_Agent_4382dffd0b_AYlGT.webp) Building an app with New Project Agent

Additionally, it now offers support for large screens. You can scaffold your project with layouts, navigation, and components optimized for tablets, foldables, and laptop devices from the get-go. It has additional logic to test your app on large-screen emulators if you have one enabled. Simply configure the required device in the Android Emulator and the Agent can test it out!
![LargeFormFactors_NPA.png](https://developer.android.com/static/blog/assets/Large_Form_Factors_NPA_72ac3b31ce_Znv7TJ.webp) Build large screen apps for foldables and tablet devices

## 2: Any AI provider, anywhere you build

### Build Android apps in Google AI Studio

Google AI Studio now features [full Android app development capabilities](http://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html). Users can generate new applications, preview them instantly via an embedded Android Emulator, and deploy them directly to physical devices using ADB over USB. Additionally, developers can publish straight to Google Play; AI Studio handles the app record creation, bundles the package, and uploads it to an internal testing track. For advanced development and production readiness, projects can be exported as a ZIP file and opened seamlessly in Android Studio. To get started, visit [Google AI Studio](https://ai.dev/apps?features=build_android_app) today and start building!
![Build_Android_apps_AI_Studio.png](https://developer.android.com/static/blog/assets/Build_Android_apps_AI_Studio_a739f8a441_2fvMRM.webp) Google AI Studio build mode with Android framework

### Android CLI helps you build faster, more efficiently with any agent

Android CLI enables you to build apps using any agent, LLM, and tool of your choice. Android CLI is [designed to help AI agents build faster](https://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html), and use less tokens when compared to only using generic LLM tools. By grounding agents with Android Knowledge Base and Android skills, you can now have your agent of choice follow the latest best practices across any coding environment.

Additionally, when using the latest Canary version of Android Studio Quail, Android CLI enables your agent to leverage powerful capabilities of the IDE, such as analyzing files for issues or finding symbol declarations. Google Antigravity 2.0 now offers official support for Android development with [Android CLI](http://d.android.com/tools/agents).
![AndroidCLI_2.png](https://developer.android.com/static/blog/assets/Android_CLI_2_b151f81556_ZynjP4.webp) Android CLI enables any agent with the tools and knowledge to build for Android.

### Google AI plan

You can now use your [Google AI Pro or Ultra](https://one.google.com/about/google-ai-plans/) plan to get access to dedicated capacity and higher rate limits for Gemini in Android Studio. This is especially helpful for long agentic Android development sessions, which can require using more tokens. Android Studio detects your subscription automatically when you log in with your Google account.
![Google_AI_Plan.png](https://developer.android.com/static/blog/assets/Google_AI_Plan_c886c328e3_kSzjX.webp) Use your Google AI plan in Agent Mode

### Gemma 4 for local code assist and on-device AI

[Gemma 4](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) is a state-of-the-art local model trained for Android development. It's our most efficient local model and is capable of complex multi-step agentic coding in Android Studio. It's ideal for developers who require data privacy, offline access, or have run into quota issues with other models.
[Video](https://www.youtube.com/watch?v=4iPn1qRVsNY)

And now in the latest Canary build, you can download and run Gemma 4 directly from the IDE, without needing to set up an external server.
![Gemma4_Default_Model_Selector.png](https://developer.android.com/static/blog/assets/Gemma4_Default_Model_Selector_aad6c91d3f_w8eug.webp) Model selector in Agent Mode

### Bring your own model to Android Studio

Android Studio allows developers to bring any model they choose into the IDE for agentic AI assistance. Power your workflow with models like Gemini, GPT, and Claude or use a local model like Gemma 4. This flexibility offers developers greater control over performance, privacy, and cost.
![BYOM.png](https://developer.android.com/static/blog/assets/BYOM_ceafd170b9_Z1zMyR6.webp) Settings, Model Provider

### Android Bench highlights the top models

Earlier this year we launched Android Bench, the benchmark and leaderboard designed to evaluate how effectively LLMs handle real-world Android development tasks. The goal is to accelerate AI improvements, leading to more helpful models for you to use for AI assistance, which will lead to better quality apps for Android users.  

You asked us to evaluate open models, so we added them to [the leaderboard](http://d.android.com/bench) to help you see how LLMs with additional privacy and offline access measure up. We are also working on significantly increasing the difficulty of challenges we're giving LLMs, to continue encouraging improvements. This includes creating long running tasks, which take a typical Android engineer multiple days to complete.
![Android_Bench_update.png](https://developer.android.com/static/blog/assets/Android_Bench_update_6c56b8335f_Z1bTJsG.webp) Latest results as of May 18th 2026, check here for updates

## 3: As always, performance and quality remain top priorities:

### Test multi-device interactions with the Android Emulator

The Android Emulator now features a new networking stack that enables zero-configuration, peer-to-peer connectivity between multiple virtual devices on the same host machine. [This update](https://android-developers.googleblog.com/2026/04/Test-Multi-Device-Interactions-with-the-Android-Emulator.html) eliminates the need for manual port forwarding, allowing developers to easily test multi-device scenarios like local multiplayer gaming, file sharing, and companion app pairing. By creating a shared virtual network backplane, the Android Emulator provides a more stable and consistent environment for building complex, interconnected app experiences across different form factors.
![Emulator.jpg](https://developer.android.com/static/blog/assets/Emulator_f2b7b647d7_2gkVBs.webp) Multi -device testing with the Android Emulator

### Android Debug Bridge Wi-Fi 2.0

ADB Wi-Fi 2.0 offers significantly more reliable wireless debugging. With the latest ADB command line tool from Android Platform Tools v37 and an Android 17 device, you can now change networks, shut down your machine, and go about your typical day and your devices will stay connected. Additionally, devices with wireless debugging enabled will automatically show in Android Studio's Device Manager, streaming the pairing process and making it easier than ever to connect Android phones, watches, and more.
![ADB_wifi.png](https://developer.android.com/static/blog/assets/ADB_wifi_f344011a01_ZAFf1n.webp) Pair devices with Wi-Fi

### Android Studio now lets you publish to Google Play for testing

Android Studio now gives you the ability to upload new releases of your app directly to Google Play Console test tracks. You can do this by selecting a new option to continue to "Publish for Testing" at the end of the Generate Signed App Bundle flow. This integration supports uploading an initial release of a brand-new app to Play Console's internal test track. You can also use this feature to upload releases to existing apps to test tracks. You need to be registered on Google Play Console to take advantage of this functionality. Read the ['What's new in Google Play' blog](https://goo.gle/play-io26) to learn about all the updates from Play at I/O.
![upload_to_play_square.png](https://developer.android.com/static/blog/assets/upload_to_play_square_0095fb1ec3_1Fr6QR.webp) Upload App Bundle to Google Play

### Android developer verification support

You can now see your app's registration status right in Android Studio when you generate a signed App Bundle or APK. Seeing this information in Android Studio enables you to address registration issues early and ensure your apps are ready before the [verification requirement](https://developer.android.com/developer-verification) goes into effect for certified Android devices starting in September 2026.
![DeveloperVerificationAndroidStudio.png](https://developer.android.com/static/blog/assets/Developer_Verification_Android_Studio_ef245fd61d_1YTHGc.webp) App registration status with Android developer verification

### Memory leak detection with LeakCanary

Memory leaks in Android occur when your code holds onto an object's reference long after its life cycle has ended. This prevents the Garbage Collector (GC) from reclaiming that memory, eventually leading to sluggish performance or OutOfMemoryError (OOM).  

The Android Studio [LeakCanary](https://square.github.io/leakcanary/) profiler task significantly enhances developer productivity by enabling the analysis and inspection of memory leak traces directly on the desktop development environment rather than on the mobile device. Furthermore, Android Studio streamlines troubleshooting by providing tools like "Go to declaration" to map the leak analysis directly to the codebase, allowing developers to quickly locate and resolve memory leaks.  

Starting from the Android Studio Quail 1 release, you can now also request Gemini to review the memory leak for you using the "Fix with Agent" button.
![LeakCanary.png](https://developer.android.com/static/blog/assets/Leak_Canary_4e3675ccb2_ZXI2sE.webp) Review memory leaks identified via LeakCanary through the "Fix with Agent" button

### Android Performance Analyzer (APA)

[Android Performance Analyzer](https://developer.android.com/android-performance-analyzer)(APA) is the next generation of performance profiler for Android and provides a cohesive analysis of CPU, GPU, memory, and power usage for your apps and games running on Android 12+ devices. APA is engineered for reliability and performance with trace rendering speeds which are up to **26x faster** from previous tooling.
![square_APA.png](https://developer.android.com/static/blog/assets/square_APA_2f42840698_Z1kVG7R.webp) Android Performance Analyzer (APA) running in Android Studio showing two traces side by side

APA integrates natively with AI agents and offers two new skills: **Perfetto SQL skill** and the **Perfetto Analysis skill** , which helps with questions like "**Why is my app startup slow?**"
![Perf_analyzer_Agent_Chat.png](https://developer.android.com/static/blog/assets/Perf_analyzer_Agent_Chat_70d718b8f6_2cOXew.webp) Analysis of traces using Perfetto Analysis skill

### R8 Configuration Analyzer

[R8](https://developer.android.com/topic/performance/app-optimization/enable-app-optimization) is one of the best ways to improve your app's performance and reduce memory footprint. The performance benefits you can get from R8 are directly correlated to how much of your codebase R8 is able to optimize. We've introduced a new tool to help you to unlock the maximum optimization from R8 -- the R8 Configuration Analyzer. It provides insights into R8 configuration quality and how your keep rules impact your app. We have also introduced three scores that show how much of your codebase is available for optimization, obfuscation, and shrinking.

### Suggested fixes for crashes with Agent integration in AQ**I**

The [App Quality Insights](https://developer.android.com/studio/debug/app-quality-insights) tool window is now integrated with the AI agent to analyze crash data along with your source code to provide detailed explanations and suggest potential fixes. After selecting a crash in the App Quality Insights tool window, navigate to the Insights tab and click "See more" to see a detailed explanation of the crash. Click "Fix with AI" to have the agent suggest code changes that you can review and accept.  
![aqi-agent-integration.png](https://developer.android.com/static/blog/assets/aqi_agent_integration_a97c103aa9_25F7os.webp) App Quality Insights and Fix with AI

## Get started

Android Studio is closing the gap between ideation and implementation. With powerful tools built for agentic development, it's never been easier to build and ship high-quality Android apps.  

Download the latest [Android Studio Quail preview build](https://developer.android.com/studio/preview) and try these new features. As always, your feedback is crucial to us. Check known issues, report bugs, and be part of our vibrant community on [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [YouTube](https://www.youtube.com/c/AndroidDevelopers/videos), or [X](https://x.com/androidstudio). Happy coding!

Explore this announcement and all Google I/O 2026 updates on [io.google](https://io.google/2026/?utm_source=blogpost&utm_medium=pr&utm_campaign=devblogs&utm_content).
- [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
- [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
- [#Android](https://developer.android.com/blog/topics/android)
- [#Android Studio](https://developer.android.com/blog/topics/android-studio)
Written by:

-

  ## [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-warner) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)
Continue reading
- [![View Jingyu Shi's profile](https://developer.android.com/static/blog/assets/Jingyu_Shi_ab6f01bd32_ZXPVGC.webp)](https://developer.android.com/blog/authors/jingyu-shi) 26 May 2026 26 May 2026 ![](https://developer.android.com/static/blog/assets/Blog_hero_Strapi_2x_0147a8b012_1yD2LQ.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Top AI on Android updates for building intelligent experiences from Google I/O '26](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26)

  [arrow_forward](https://developer.android.com/blog/posts/top-ai-on-android-updates-for-building-intelligent-experiences-from-google-i-o-26) At Google I/O 2026, we introduced Android's shift from an operating system to an intelligence system. We also demonstrated how you can build intelligent experiences natively with the system and bring the power of Google's AI into your apps.
  [Jingyu Shi](https://developer.android.com/blog/authors/jingyu-shi) • 2 min read
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#AppFunctions](https://developer.android.com/blog/topics/app-functions)
  - [#On-device](https://developer.android.com/blog/topics/on-device)
  - +2 ↩
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](https://developer.android.com/blog/authors/matthew-warner) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding) Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 2 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Amman Asfaw's profile](https://developer.android.com/static/blog/assets/unnamed_11_a00df7e0e8_ZARb6S.webp)](https://developer.android.com/blog/authors/amman-asfaw) 16 Jul 2026 16 Jul 2026 ![](https://developer.android.com/static/blog/assets/Quail_Blog_Strapi_46fcc9f1a1_ZzldHB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-quail-2-is-stable-multi-task-with-the-android-studio-ai-agent) Android Studio Quail 2 is now stable and ready for you to use in production, bringing a shift to your IDE with concurrent agentic workflows, natively integrated memory leak profiling, and context-aware crash remediation.
  [Amman Asfaw](https://developer.android.com/blog/authors/amman-asfaw) • 3 min read
  - [#Gemini in Android Studio](https://developer.android.com/blog/topics/gemini-in-android-studio)
  - [# Quail 2](https://developer.android.com/blog/topics/quail-2)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)