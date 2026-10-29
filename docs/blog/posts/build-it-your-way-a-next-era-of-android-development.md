---
title: https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development
url: https://developer.android.com/blog/posts/build-it-your-way-a-next-era-of-android-development
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Agentic and Flexible: A next era of Android development

4 min read ![](https://developer.android.com/static/blog/assets/Mesa_de_trabajo_1_copy_8_3f8cf8a935_Z1799P4.webp) 28 Oct 2026 [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) Vice President, Product Management, Android Developer In a time when the way you work is changing, your craft, creativity, and expertise are needed more than ever. Today at the [Android Dev Summit](https://developer.android.com/events/dev-summit), we annouced the broad availability of many tools and APIs designed to remove everyday friction and give you more flexibility to build great Android apps. These updates help you code smarter and faster, offer solutions for agentic experiences, and help simplify scaling across a wide variety of screen sizes.
[Video](https://www.youtube.com/watch?v=8Lmv7LGgL4E)

## **Helping you build high quality apps with the tools and agents of your choice**

With the number of new models and agents increasing every day, we've heard that you want the flexibility to select the ones that suit your particular work best. You now have more flexibility than ever before with updates to Android Studio and Android CLI to make it even easier [for your agents to build high quality Android apps](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance).

### **Bring Your Own Agent**

[Android Studio Rabbit 2](https://developer.android.com/blog/posts/ai-agents-android-studio-integration) is stable today, letting you choose your preferred coding agent, such as Claude Agent, Codex, Antigravity, or any of over 40 ACP-compliant agents, directly in Android Studio to harness its full suite of developer tools.
![ADS - BYOA_All 4 agents.png](https://developer.android.com/static/blog/assets/ADS_BYOA_All_4_agents_3aff9e48fd_Z25SEqX.webp)

### What's new in Android CLI

- [**Android Device streaming**](https://developer.android.com/tools/agents/android-cli/commands/device?_gl=1*12mhw8m*_up*MQ..*_ga*OTI3OTc0MDM0LjE3OTMwMzA0Mzg.*_ga_6HH9YJMN9M*czE3OTMwMzA0MzgkbzEkZzAkdDE3OTMwMzA0MzgkajYwJGwwJGg3MzU0MDczMDY.)**and Compose** [**previews**](https://developer.android.com/tools/agents/android-cli/commands/preview?_gl=1*gog839*_up*MQ..*_ga*OTI3OTc0MDM0LjE3OTMwMzA0Mzg.*_ga_6HH9YJMN9M*czE3OTMwMzA0MzgkbzEkZzAkdDE3OTMwMzA0MzgkajYwJGwwJGg3MzU0MDczMDY.)**:**Test on real devices remotely with Android device streaming, powered by Firebase, now in Android CLI. Your agent can also now render Jetpack Compose previews, enabling instant visual validation without needing an Android Emulator or deploying an APK.
- [**Profiling**](https://developer.android.com/tools/agents/android-cli/commands/profiler?_gl=1*12mhw8m*_up*MQ..*_ga*OTI3OTc0MDM0LjE3OTMwMzA0Mzg.*_ga_6HH9YJMN9M*czE3OTMwMzA0MzgkbzEkZzAkdDE3OTMwMzA0MzgkajYwJGwwJGg3MzU0MDczMDY.)**:**Improve your app's performance and memory through system tracing. Captures production-grade system traces (Perfetto) to debug cold startup latency, UI jank, and background wakeups.
- [**Analyze**](https://developer.android.com/tools/agents/android-cli/commands/analyze)**:**Check your app bundles and libraries (AAs/Js) for quality signals like your obfuscation, optimization and shrinking score. You can use this to find quality problems using the same logic Google Play does before upload.
- **New** [**Android skills**](https://developer.android.com/tools/agents/android-skills)**:**We have 30+ skills that cover 20+ areas to give your agents the expertise for complex Android tasks, such as permissions security, Glance widget layouts, Compose performance optimizations, and more.
- **Official Android** [**agent plugins**](https://developer.android.com/tools/agents/android-cli/agent-plugins?_gl=1*1js8ckm*_up*MQ..*_ga*MTQ2MjcyMDk4MS4xNzkzMTQ0NzIx*_ga_5QGJFZTNG7*czE3OTMxNDQ3MjAkbzEkZzAkdDE3OTMxNDQ3MjAkajYwJGwwJGgw)**:** the Android plugin for Google Antigravity has been updated with all the latest capabilities of Android CLI, plus adds deeper integrations to enable you to view Compose previews and interact with real Android devices right from Antigravity. We've also launched official plugins for Claude Code and Codex by OpenAI.

## **Build intelligent, agentic experiences on Android**

To support developers and businesses in the emerging agentic landscape, we are introducing new APIs designed to simplify the creation of rich, engaging user experiences.

- **The Android intelligence system** provides users with both prompted assistance and proactive assistance across the Android ecosystem of devices.You can now prototype with a Connected App to share your app's services to Android users when Gemini is the system AI agent. Once ready, sign up for the Connected Apps Platform preview to publish to production across surfaces.
- **Share your app's capabilities with any agent through Android MCP.** Leverage the [AppFunctions](https://developer.android.com/ai/appfunctions) API -- Android's unified tool calling layer -- to expose functionality that can be used by their own on-device agent or system agents. AppFunctions is now in beta.
- **Turn agent replies into native app UI with A2UI for Jetpack Compose, in alpha.** Agent-to-UI (A2UI) lets agents respond with a real interactive UI built from your app's own components instead of a wall of text. The new native Jetpack Compose renderer makes it feel fully at home in your Android app.
- **Build on-device agents with Gemini Nano 4 via the new agentic APIs in** [**ML Kit**](https://developers.google.com/ml-kit/genai)**, in alpha.**We've expanded the ML Kit Prompt API, with the new Agentic API leveraging the new capabilities in Gemini Nano 4. The Agentic API auto-executes functions for you, saves conversation history, manages the orchestration loop, and includes automatic guardrails.

### **Bring your app's services to users right where they are**

To help developers connect with high-intent users across Gemini and Search, we are introducing the new [Connected Apps Platform](https://blog.google/innovation-and-ai/technology/developers-tools/connected-apps-one-place/). You can build natively using Android MCP or remote MCP, prototype using Gemini dev mode, and register through the Google Connected Console preview program when you are ready for production.

## **New API support to build across premium form factors**

Expanding your app across the growing Android ecosystem allows you to engage users wherever they are, creating new touchpoints and driving deeper interaction. We continuously develop new APIs to simplify app adaptation and enable unique experience layering. With new Jetpack Compose-first foundations, adaptive building blocks, and agentic UI features, you can seamlessly scale your app's architecture and UI across many form factors.

- **AppState, in alpha,**brings Compose's reactive model down to the state layer, providing Compose-first architecture building blocks that devs and AI agents can use to preserve state across device configurations.
- **Navigation 3 1.2** is stable with [deep links](https://developer.android.com/guide/navigation/navigation-3/deep-links) support and richer Predictive back handling.
- **Compose-first UI development expands with the upcoming Compose 1.13 stable release,**bringing built-in support for adaptive layouts with Grid and Flexbox migrating to stable and new functionality like Progressive Blur and Formatted Text.

### **Accelerate your reach with Googlebook and foldables with new skill support**

With the arrival of Googlebook, your apps can now scale seamlessly across phones and laptops without requiring a separate codebase. The [Compose adaptive skill](https://github.com/android/skills/blob/main/jetpack-compose/adaptive/SKILL.md) helps agents transform mobile apps to scale across phones, foldables, Googlebook, tablets, parked cars and XR.

Today we have updated it to make it faster and easier to make your existing apps ready for desktop. The Adaptive skill can now audit your Compose UI to find and implement keyboard shortcuts, custom pointer cursors, hover states and tooltips for buttons and controls. In addition to understanding navigation and migrating layouts to Grid, FlexBox, and mediaQuery, it now explicitly handles end-to-end state management across the app.

And finally the skill now also includes foldable posture optimizations, such as automatically refactoring media and camera screens into tabletop layouts. Next year Google Play will be looking closely at how your app or game runs on a foldable and providing you more opportunities to showcase how you've built adaptively. For apps, make sure to optimize by using the [Compose adaptive skill](https://github.com/android/skills/blob/main/jetpack-compose/adaptive/SKILL.md) and follow the [Android adaptive quality guidelines](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality). For games, follow the [adaptive games guidelines](https://developer.android.com/games/build-adaptive-apps). We'll announce details on what is required for the Google Play store later this year.

## **Build for an expanding lineup of Android XR devices**

![ManinOffice_V2.jpg](https://developer.android.com/static/blog/assets/Manin_Office_V2_1188022de5_15IwcL.webp)

Today, together with XREAL, we launched [XREAL AURA](http://xreal.com/aura), the world's first wired XR glasses powered by Android XR, along with the graduation of several core libraries and tools to stable.

- **Core Jetpack XR SDK libraries are now stable** and bring production-ready APIs, long-term API stability, and backward compatibility acrossJetpack SceneCore, ARCore for Jetpack XR, and XR Runtime.
- **Android XR emulators in Android Studio, now stable** , letting developers build, iterate, and visually validate experiences forXR Glasses, audio glasses, and display glasses without needing physical hardware.
- **Android XR Engine Hub, now stable,**delivers dedicated workflow and easy access to start and analyze performance traces across Unity, Godot and Unreal
- **Geospatial APIs in ARCore for Jetpack XR SDK and Unity**, enable developers to anchor digital content to the real world with accuracy and local tracking across wired XR glasses and intelligent eyewear.

We are eager to receive your feedback on these new tools and capabilities. We look forward to your ideas on how we can continue improving our tools to support your app development journey.
- [#Android](https://developer.android.com/blog/topics/android)
Written by:

-

  ## [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough)

  ###### Vice President, Product Management, Android Developer

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-mccullough) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp) ![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)
Continue reading
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 12 May 2026 12 May 2026 ![](https://developer.android.com/static/blog/assets/Tas_Developers_cut_Strapi_3636223c9c_DKPLL.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Building for the Intelligence System on Android](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android)

  [arrow_forward](https://developer.android.com/blog/posts/building-for-the-intelligence-system-on-android) Announced today during The Android Show, Android is transitioning from an operating system to an intelligence system, creating more opportunities for engagement with your apps.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Matthew McCullough's profile](https://developer.android.com/static/blog/assets/matthew_mccullough_dc22050a18_51Njy.webp)](https://developer.android.com/blog/authors/matthew-mccullough) 20 May 2025 20 May 2025 ![](https://developer.android.com/static/blog/assets/IO_25_Blog_Hero_Template_Art_Long_01_126026f6a9_ZPukDs.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Updates to the Android XR SDK: Introducing Developer Preview 2](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-2)

  [arrow_forward](https://developer.android.com/blog/posts/updates-to-the-android-xr-sdk-introducing-developer-preview-2) Since launching the Android XR SDK Developer Preview alongside Samsung, Qualcomm, and Unity last year, we've been blown away by all of the excitement we've been hearing from the broader Android community.
  [Matthew McCullough](https://developer.android.com/blog/authors/matthew-mccullough) • 4 min read
  - [#Android](https://developer.android.com/blog/topics/android)
- [![View Roxanna Aliabadi Walker's profile](https://developer.android.com/static/blog/assets/roxana_02dc1d3afc_1Q1ceg.webp)](https://developer.android.com/blog/authors/roxanna-walker) 21 Oct 2026 21 Oct 2026 ![](https://developer.android.com/static/blog/assets/1009_ABL_142_A_more_reliable_way_to_add_and_edit_contacts_on_Android_Strapi_b510ec4fc0_ZXfljU.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [A more reliable way to add and edit contacts on Android](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android)

  [arrow_forward](https://developer.android.com/blog/posts/reliable-way-to-add-and-edit-contacts-android) Apps that target the upcoming Android release will no longer be able to directly write to contacts with the WRITE_CONTACTS permission.
  [Roxanna Aliabadi Walker](https://developer.android.com/blog/authors/roxanna-walker) • 6 min read
  - [#Android](https://developer.android.com/blog/topics/android)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)