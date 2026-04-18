---
title: https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent
url: https://developer.android.com/blog/posts/android-cli-build-android-apps-3x-faster-using-any-agent
source: md.txt
---

#### [How-tos](https://developer.android.com/blog/categories/how-tos)

# Android CLI and skills: Build Android apps 3x faster using any agent

###### 4-min read

![](https://developer.android.com/static/blog/assets/hours_CLI_Dark_Strapi_2x_427f20cc78_Z1oqB1M.webp) 16 Apr 2026 [![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)](https://developer.android.com/blog/authors/adarsh-fernando)[![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)](https://developer.android.com/blog/authors/esteban-de-la-canal)

##### [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando)
\&
[Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal)

As Android developers, you have many choices when it comes to the agents, tools, and LLMs you use for app development. Whether you are using Gemini in Android Studio, Gemini CLI, Antigravity, or third-party agents like Claude Code or Codex, our mission is to ensure that high-quality Android development is possible everywhere.
[Video](https://www.youtube.com/watch?v=AhrXPjk22OE)

Today, we are introducing a new suite of [**Android tools and resources for agentic workflows**](http://d.android.com/tools/agents) --- Android CLI with Android skills and the Android Knowledge Base. This collection of tools is designed to eliminate the guesswork of core Android development workflows when you direct an agent's work outside of Android Studio, making your agents more efficient, effective, and capable of following the latest recommended patterns and best practices.

Whether you are just starting your development journey on Android, are a seasoned Android developer, or managing apps across mobile and web platforms, building your apps with the latest guidance, tools, and AI-assistance is easier than ever. No matter which environment you begin with these resources, you can always transition your development experience to Android Studio---where the state-of-the-art tools and agents for Android development are available to help your app experience truly shine.

### **(Re)Introducing the Android CLI**

Your agents perform best when they have a lightweight, programmatic interface to interact with the Android SDK and development environment. So, at the heart of this new workflow is a revitalized **Android CLI**. The new Android CLI serves as the primary interface for Android development from the terminal, featuring commands for environment setup, project creation, and device management---with more modern capabilities and easy updatability in mind.

*The *`*create*`* command makes an Android app project in seconds.*

In our internal experiments, Android CLI improved project and environment setup by reducing LLM token usage by more than **70%,** and tasks were completed **3X faster** than when agents attempted to navigate these tasks using only the standard toolsets.

Key capabilities available to you include:

- **SDK management** : Use `android sdk install` to download only the specific components needed, ensuring a lean development environment.
- **Snappy project creation** : The `android create` command generates new projects from official templates, ensuring the recommended architecture and best practices are applied from the very first line of code.
- **Rapid device creation and deployment** : Create and manage virtual devices with `android emulator` and deploy apps using `android run`, eliminating the guesswork involved in manual build and deploy cycles.
- **Updatability:** Run `android update` to ensure that you have the latest capabilities available.

*Android CLI can create a device, run your app on it, and make it easier for agents to navigate UI.*

While Android CLI will empower your agentic development flows, it's also been designed to streamline CI, maintenance, and any other scripted automation for the increasingly distributed nature of Android development. [Download](https://developer.android.com/tools/agents) and try out the Android CLI today!

### **Grounding LLMs with official Android Skills**

Traditional documentation can be descriptive, conceptual, and high-level. While perfect for learning, LLMs often require precise, actionable instructions to execute complex workflows without using outdated patterns and libraries.

To bridge this gap, we are launching the [**Android skills GitHub repository**](http://goo.gle/android-skills). Skills are modular, markdown-based (`SKILL.md`) instruction sets that provide a technical specification for a task and are designed to trigger automatically when your prompt matches the skill's metadata, saving you the hassle of manually attaching documentation to every prompt.

Android skills cover some of the most common workflows that some Android developers and LLMs may struggle with---they help models better understand and execute specific patterns that follow our best practices and guidance on Android development.

In our initial release, the repository includes skills like:

- **Navigation 3**setup and migration.
- Implementing **edge-to-edge** support.
- **AGP 9** and **XML-to-Compose** migrations.
- R8 config analysis, and more!

If you're using Android CLI, you can browse and set up your agent workflow with our growing collection of skills using the `android skills` command. These skills can also live alongside any other skills you create, or third-party skills created by the Android developer community. Learn more about getting started with [Android skills](http://d.android.com/tools/agents/android-skills).

*Install Android skills via the Android CLI to make your agent more effective and efficient. *

### **The latest guidance via the Android Knowledge Base**

The third component we are launching today is the **Android Knowledge Base.** Accessible through the `android docs` command and already available in the latest version of Android Studio, this specialized data source enables agents to search and fetch the latest authoritative developer guidelines to use as relevant context.

*The Android Knowledge Base ensures agents have the latest context, guidance, and best practices for Android.*

By accessing the frequently updated knowledge base, agents can ground their responses in the most recent information from Android developer docs, Firebase, Google Developers, and Kotlin docs. This ensures that even if an LLM's training cutoff is a year old, it can still provide guidance on the latest frameworks and patterns we recommend today.

### **Android Studio: The ultimate destination for premium apps**

In addition to empowering developers and agents to handle project setup and boilerplate code, we've also designed these new tools and resources to make it easier to transition to **Android Studio**. That means you can start a prototype quickly with an agent using Android CLI and then open the project in Android Studio to fine-tune your UI with visual tools for code editing, UI design, deep debugging, and advanced profiling that scale with the growing capabilities of your app.

And when it is time to build a high-quality app for large-scale publication across various device types, our agent in Android Studio is here to help, while leveraging the latest development best practices and libraries. Beyond the powerful **Agent and Planning Modes** for active development, we have introduced an **AI-powered New Project flow**, which provides an entry point to rapidly prototyping your next great idea for Android.

These built-in agents make it simple to extend your app ideas across phones, foldables, tablets, Wear OS, Android Auto, and Android TV. Equipped with full context of your project's source code and a comprehensive suite of debugging, profiling, and emulation tools, you have an end-to-end, AI-accelerated toolkit at your disposal.

### **Get started today**

Android CLI is available in preview today, along with a growing set of Android skills and knowledge for agents. To get started, head over to [**d.android.com/tools/agents**](https://developer.android.com/tools/agents) to download Android CLI.

###### Written by:

-

  ## [Adarsh Fernando](https://developer.android.com/blog/authors/adarsh-fernando)

  ###### Group Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/adarsh-fernando) ![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp) ![](https://developer.android.com/static/blog/assets/Adarsh_profile_picture_8e88f2831a_1Ut9s6.webp)
-

  ## [Esteban de la Canal](https://developer.android.com/blog/authors/esteban-de-la-canal)

  ###### Senior Staff Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/esteban-de-la-canal) ![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp) ![](https://developer.android.com/static/blog/assets/estebandlc_profile_800x800_1d536f02a7_Z2cAv7x.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 04 Mar 2026 04 Mar 2026 ![](https://developer.android.com/static/blog/assets/battery_Performance_08d6713f94_Z1IAO0P.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Battery Technical Quality Enforcement is Here: How to Optimize Common Wake Lock Use Cases](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases)

  [arrow_forward](https://developer.android.com/blog/posts/battery-technical-quality-enforcement-is-here-how-to-optimize-common-wake-lock-use-cases) In recognition that excessive battery drain is top of mind for Android users, Google has been taking significant steps to help developers build more power-efficient apps.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  8 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Ivy_Knight_3071ce592d_2j4ER1.webp)](https://developer.android.com/blog/authors/ivy-knight) 02 Dec 2025 02 Dec 2025 ![](https://developer.android.com/static/blog/assets/sample_readme_bazel_9348d9f325_Z57CJe.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Explore AI on Android with Our Sample Catalog App](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app)

  [arrow_forward](https://developer.android.com/blog/posts/explore-ai-on-android-with-our-sample-catalog-app) We wanted to provide you with examples of AI-enabled features using both on-device and Cloud models and inspire you to create delightful experiences for your users.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Ivy Knight](https://developer.android.com/blog/authors/ivy-knight) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/Alice_Yuan_552a4dd4ee_ZlDEgJ.webp)](https://developer.android.com/blog/authors/alice-yuan) 20 Nov 2025 20 Nov 2025 ![](https://developer.android.com/static/blog/assets/performance_Week8_4d6efcacbe_ZI6a5e.webp)

  #### [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Leveling Guide for your Performance Journey](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey)

  [arrow_forward](https://developer.android.com/blog/posts/leveling-guide-for-your-performance-journey) The performance leveling guide features 5 levels. We'll start with level 1, which introduces minimal adoption effort performance tooling, and we'll go up to level 5, ideal for apps that have the resourcing to maintain a bespoke performance framework.

  ###### [Alice Yuan](https://developer.android.com/blog/authors/alice-yuan) •
  9 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)