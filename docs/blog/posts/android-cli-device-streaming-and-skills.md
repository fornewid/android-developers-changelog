---
title: https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills
url: https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Device Streaming and Android skills - available in Android CLI

4 min read ![](https://developer.android.com/static/blog/assets/ABL_135_Android_CLI_and_Android_skills_Strapi_d22702426a_ZIUXgH.webp) 02 Oct 2026 [![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)](https://developer.android.com/blog/authors/simona-milanovic) [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) Developer Relations Engineer As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build. We're announcing updates to our [Android CLI](https://developer.android.com/tools/agents/android-cli) command-line tooling, including the ability to access real devices through Android Device Streaming. We're also sharing more [Android skills](https://developer.android.com/tools/agents/android-skills), and giving you a deep dive into the Wear OS Compose Material 3 skill.
[Video](https://www.youtube.com/watch?v=JMPd2jbQEqo)

## Android CLI for command-line development

Android CLI is our tool to make command-line interface Android development easier. It supports any AI agent or tool in building more efficiently for Android.

Along with the `android-cli` skill, your agents use Android CLI to create, build, test, and manage Android projects, help you set up the development environment, create and run emulators, and execute test runs.

## Android Device Streaming now available in CLI

It's important to test your app on real devices to catch issues that are hardware- or OS-specific, but sometimes you don't have access to the ones you need. Android Device Streaming gives you access to real physical devices, remotely. Your agent can now use Android Device Streaming anywhere, through Android CLI.

*Connecting to a Pixel 10 Pro through Android Device Streaming*

The agent can interact with physical devices (as if they were plugged in over USB) over a secure ADB over SSL connection. This enables spinning up devices, deploying builds, collecting logs and traces, and even capturing screenshots headlessly---all through the terminal.

To get started, link your project, instruct your agent to list available remote devices and decide which device you want next. [Read the documentation](https://developer.android.com/tools/agents/android-cli/commands/device_remote) to learn more, and see the [Android CLI release notes](https://developer.android.com/tools/agents/android-cli/release-notes).

## Grounding agents with Android skills

To bridge the gap between LLMs' default knowledge and platform-specific standards and updates, we keep growing our **Android skills repository**.

Android skills are structured instructions (`SKILL.md` files) that ground AI agents with our official guidance from [developer.android.com](http://developer.android.com/). Instead of relying on a model's training cutoff, skills provide more precise and fresher data, API references and samples, and architectural patterns directly into your agent's context.
![Android skills rolodex.gif](https://developer.android.com/static/blog/assets/Android_skills_rolodex_5a873557a7_1vpi1E.webp) Android Skills

With [over 20 skills available](https://developer.android.com/tools/agents/android-skills/browse), you can now equip your AI agents to handle more complex and specialized development tasks such as:

- **Audit Play policy compliance:** Audit app manifests, runtime permissions, target SDK levels, and privacy disclosures before submitting your app for Play Policy review.
- Implement Restore Credentials: Implement re-authentication across device setup and cloud restores using Jetpack Credential Manager.
- **Android Intent security:** Detect and prevent implicit intent hijacking, secure broadcast receivers, and validate PendingIntent declarations.
- **Use Android profilers:** Diagnose UI frame drops, interpret CPU/memory traces, and query trace data using natural language mapped to PerfettoSQL.
- **CameraX:**Replace legacy Camera1/Camera2 code with lifecycle-aware CameraX.
- **Migrate Leanback to Compose for TV:**Modernize Android TV experiences by transitioning from Leanback to Compose for TV.
- **Integrate Media3 Cast:**Connect Jetpack Media3 media sessions with Google Cast receiver devices and sync playback states.
- **Integrate Play Engage SDK:** Integrate the Google Play Engage SDK to publish user recommendations and cluster surfaces.
- **Set up testing strategy:** Configure unit test suites, Compose UI testing rules, and screenshot testing infrastructure.
- **Audit R8 configuration:** Optimize your app's performance by auditing your R8 configuration.

Our Android skills are thoroughly evaluated. To understand the philosophy and methodology behind this project, as well as why all skills should come with evals, make sure to read [Inside Android Skills - Built for deprecation](https://developer.android.com/blog/posts/inside-android-skills-built-for-deprecation).

Managing skills across projects and individual agent directories is pretty straightforward with Android CLI:

1. Install [Android CLI](https://goo.gle/android-cli)
2. Run `android init` to install the `android-cli` skill
3. To list all available official skills, run: `android skills list`
4. To install individual skills into a single project root: `android skills` add `wear-compose-m3 --project=`.
5. To update skills, use:
6. `android skills update --all`
7. `android skills update wear-compose-m3` (for an individual skills)

Skills are designed to be **environment-agnostic**. From writing code in Android Studio and Antigravity, to pairing with third-party agents like Claude and Codex, our Android skills work across your entire setup.
![coding agents (1).gif](https://developer.android.com/static/blog/assets/coding_agents_1_92e34fcef5_Z2j9b4q.webp) Android skills work across your entire setup

## Skill spotlight: Wear Compose Material 3

Building for Wear OS means distinct design and development decisions: round viewports, rotary input, ambient display mode, minimizing power consumption, preferring `TransformingLazyColumn`, and using the `AppScaffold` and `ScreenScaffolds` containers.

Without explicit guidance, LLMs lack the understanding and knowledge of these distinct patterns that make the Wear apps really stand out and shine.

To help agents with this, we released the **Wear Compose Material 3 skill** (wear/wear-compose-m3).  
Check out this video for more information on how powerful this skill is:
[Video](https://www.youtube.com/watch?v=lBzZQmaC_2w)

Early adopters are already seeing significant productivity impact with this skill. The **engineering team at** **FotMob** used it for tasks like modernizing their existing Wear M3-based app, migrating multiple lists to `TransformingLazyColumn` with `ScreenScaffold` content padding, `ListHeader` titles, `SurfaceTransformation` on cards and buttons, theme typography, and Wear previews.

The result? The changes compiled successfully and were verified on the emulator for scrolling, rotary, edge morphing and RTL. This enabled the team to delete their legacy wrapper, and all rotary and focus boilerplate.

The skill caught mistakes that the underlying model missed, such as forgetting to forward `ScreenScaffold`'s `contentPadding` into the list, and using theme typography over hardcoded sp.

*"One skill, one afternoon, eight lists migrated and a pile of custom rotary code gone!" - Roy Solberg, Android Tech Lead at FotMob.*
![TransformingLazyColumn (1).gif](https://developer.android.com/static/blog/assets/Transforming_Lazy_Column_1_4e63d5b97f_Zdb6OI.webp) A Wear OS app built with the skill

## Get started today

When you're ready to get started, [install Android CLI with just one command](https://developer.android.com/tools/agents). You can learn more about Android CLI by reading the [developer documentation](https://developer.android.com/tools/agents/android-cli), and as well as checking out the [latest updates in the Android CLI release notes](https://developer.android.com/tools/agents/android-cli/release-notes).

After installing Android CLI, run android init to configure your agent, then browse the latest Android skills available for use and install them with android skills add.

Also check out the [Android Device Streaming documentation](https://developer.android.com/studio/run/android-device-streaming) to learn more about how this feature allows you to access real devices on the cloud inside both Android Studio and via your agents.
- [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Written by:

-

  ## [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/simona-milanovic) ![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp) ![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)
Continue reading
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
- [![View Zoe Lopez-Latorre 's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_07_07_at_1_15_58_PM_eb87f2f61a_Z1DSyTI.webp)](https://developer.android.com/blog/authors/zoe-lopez-latorre) 08 Jul 2026 08 Jul 2026 ![](https://developer.android.com/static/blog/assets/Bench_July_releas_V01_Strapi_6ee24bdb6b_Z16uIB.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Evolving how LLMs are measured for Android: the next era of Android Bench](https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench)

  [arrow_forward](https://developer.android.com/blog/posts/evolving-how-ll-ms-are-measured-for-android-the-next-era-of-android-bench) Back in March, we introduced Android Bench---our LLM leaderboard for real-world Android development tasks. Since then, we have enhanced the benchmark based on your feedback, including evaluating open-weight models and adding cost and efficiency dimensions to the leaderboard.
  [Zoe Lopez-Latorre](https://developer.android.com/blog/authors/zoe-lopez-latorre) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)