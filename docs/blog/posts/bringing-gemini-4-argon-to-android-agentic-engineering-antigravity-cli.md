---
title: https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli
url: https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Bringing our latest frontier model to Android Developers

3 min read ![](https://developer.android.com/static/blog/assets/Blog_0140_strapi_8d85f71a6e_ZvGJv2.webp) 13 Oct 2026 [![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)](https://developer.android.com/blog/authors/jason-buchel) [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel) Creative Technologist, Platform \& Devices As agentic development accelerates, Android engineering is reaching an exciting new frontier: moving from assistive code completion to agents executing end-to-end under your direction. You have total choice and flexibility in the models and agents you use.

[Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/) excels at deep work in complex, real-world tasks across domains including coding, finance, legal, cybersecurity, and science.

Starting today, Android developers can access Gemini 4 Argon across their development surfaces, including Google Antigravity (standalone and in [Android Studio Canary](https://android-developers.googleblog.com/2026/09/build-your-way-use-any-ai-agent-in-android-studio.html)) for Google AI Ultra subscribers, and in Android Studio and Google AI Studio via the paid tier of the Gemini API.

### **Velocity \& Autonomy: Closed-loop build self-correction**

Argon has significant improvements in long-horizon autonomous execution and the ability to plan and run multi-step, complex software tasks over time.

- **Self-Healing Build Loops** : When a local build fails, the Antigravity execution harness captures error streams directly from Gradle daemons and Kotlin compiler logs. Using this feedback,the model iteratively diagnoses the root-cause of build failures to arrive at a revised solution. Gemini 4 Argon's training dramatically improves on this process. It's engineered to maintain a consistent hypothesis across successive rounds of editing, as well as making use of internal Abstract Syntax Tree (AST) awareness to better inform edits. This means Gemini 4 Argon is more resilient and better able to address the true root-cause of build failures.

[Video](https://www.youtube.com/watch?v=91oc9SyHxKI)

### **UI sophistication: Fluid motion \& shader-backed Jetpack Compose**

Argon demonstrates exceptional design craft, generating production-ready Jetpack Compose code out of the box:

- **AGSL Shaders on the GPU** *:*Argon possesses the advanced mathematical reasoning needed to write complex, production-ready Android Graphics Shading Language (AGSL) directly into Compose Modifier.graphicsLayer blocks and shader brushes. From live frosted glass shaders to dynamic lighting and ripple effects, Argon can handle complicated vector and rendering math that produces lightweight GPU shaders that run alongside fluid 120 FPS Compose animations.

### **A flexible developer experience with Android CLI**

Antigravity operates across multiple surfaces, from the desktop app and IDE extensions to the command line. No matter which surface you prefer, the official Android CLI plugin is the de-facto engine that connects your agent to local Android tools, enabling it to run programmatic commands for common tasks and execute custom developer skills.

Starting today, you can access and configure this agentic workspace in two primary ways:

*1. ***Setting up visually (Antigravity Desktop \& Android Studio Canary)**

- In the Antigravity Desktop App: Go to Settings \> Customizations \> Build With Google Plugins (or the Antigravity Plugin Marketplace), locate android-cli-plugin, and toggle it to Enabled
- In Android Studio Canary: Log in to your Antigravity account in the agent tool window to enable agentic workflows directly alongside your editor

*2. ***Setting up via the Terminal CLI**

- For Google Antigravity, run:

```
agy plugin install android-cli-plugin
```

3. **For any terminal agent (via Android CLI), run:**

```
android init
```

### **Availability \& getting started**

Starting today, Argon is rolling out globally to developers in supported regions. You can access and begin building with the model in your local environment across three primary development surfaces:

*1. ***Google Antigravity** *:*Google AI Ultra subscribers can build with Gemini 4 Argon in the standalone Antigravity desktop app (available for macOS, Windows, and Linux) or directly via the terminal CLI

*2. ***Android Studio** *:*

- Via Google Antigravity: Google AI Ultra subscribers can build with Gemini 4 Argon by logging into Antigravity within the latest Android Studio Canary.
- Via the Gemini API: Developers on the paid tier of the Gemini API can build with Gemini 4 Argon in Android Studio.

*3. ***Google AI Studio** *:* Google AI Ultra subscribers or developers on the paid tier of the Gemini API can build with Gemini 4 Argon via Playground and Build in Google AI Studio

4. **Firebase AI Logic** *: *Starting today, developers globally on the paid tier of the Gemini API can use Gemini 4 Argon client-side to build intelligent features in their mobile and web apps via [Firebase AI Logic](https://developer.android.com/ai/gemini).

To begin building with Argon in your local environment:

- **Choose your path** : Confirm you have an active [Google AI Ultra subscription](https://one.google.com/about/google-ai-plans/) to use Antigravity, or ensure you are on the paid tier of the [Gemini API](https://ai.google.dev/gemini-api/docs/pricing)to use standard API surfaces (with introductory pricing available through November 30, 2026).
- **Update your tools** : Download the latest version of the [Antigravity desktop app or CLI](https://antigravity.google/), and install the official Android CLI plugin (agy plugin install android-cli-plugin) to connect your agentic workspace directly to your Android Studio build tools.

We are eager to see the high-craft Android experiences you build at the frontier. Share your projects and feedback with us on[](https://github.com/android-samples/gemini-4-antigravity-quickstart)[X](https://x.com/AndroidDev)(@AndroidDev**)** and[LinkedIn](https://www.linkedin.com/showcase/androiddev/)!
- [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Written by:

-

  ## [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel)

  ###### Creative Technologist

  [read_more
  View profile](https://developer.android.com/blog/authors/jason-buchel) ![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp) ![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)
Continue reading
- [![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)](https://developer.android.com/blog/authors/simona-milanovic) 02 Oct 2026 02 Oct 2026 ![](https://developer.android.com/static/blog/assets/ABL_135_Android_CLI_and_Android_skills_Strapi_d22702426a_ZIUXgH.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Device Streaming and Android skills - available in Android CLI](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills) As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build.
  [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) • 4 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 24 Sep 2026 24 Sep 2026 ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build your way: Use any AI agent of your choice in Android Studio](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio)

  [arrow_forward](https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio) Last year, Android Studio opened up to any AI model. Today, we're taking the next step by introducing support for your choice of coding agents.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 17 Sep 2026 17 Sep 2026 ![](https://developer.android.com/static/blog/assets/Bench_2_0_Strapi_bench_8767d57564_ZmnAe.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Bench 2.0: Pushing the frontier with challenging long-horizon tasks](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks)

  [arrow_forward](https://developer.android.com/blog/posts/android-bench-2-0-pushing-the-frontier-with-challenging-long-horizon-tasks) Today we're releasing the first set of long-horizon tasks (LHT), which are tasks of great complexity that take an engineer multiple days or even a week to complete. We are also introducing agentic evaluation, starting with agents from corresponding model providers.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
  - [#Android Bench](https://developer.android.com/blog/topics/android-bench)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)