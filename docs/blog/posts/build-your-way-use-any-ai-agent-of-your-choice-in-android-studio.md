---
title: https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio
url: https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Build your way: Use any AI agent of your choice in Android Studio

3 min read ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) 24 Sep 2026 [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) Product Manager AI-powered developer tools have become an essential multiplier for engineering productivity, with teams adopting specialized AI coding agents, custom enterprise harnesses, and autonomous tools. It's important for you to be able to build Android apps in the way that works best for you and your team, and agentic Android development is more open and flexible than ever before.

Last year, Android Studio opened up to [any AI model](https://developer.android.com/studio/gemini/use-a-remote-model). Today, we're taking the next step by introducing support for your choice of coding agents. With our new **Bring Your Own Agent (BYOA)** feature, you can seamlessly integrate your preferred coding agent into Android Studio---featuring Anthropic's Claude Agent, Open AI's Codex, and Google's Antigravity---and supercharge it with Android Studio's AI-optimized infrastructure and tool support.
![BYOALarger.gif](https://developer.android.com/static/blog/assets/BYOA_Larger_a7e6190537_2hT1RN.webp) Claude Agent in Android Studio

## Your agents, your AI plan

BYOA pairs your favorite agent with IDE-native intelligence, making it faster, more accurate, and more cost-effective. BYOA is available in the latest [Android Studio Canary](https://developer.android.com/studio/preview) with benefits including:

- **Codebase awareness and token efficiency:** Android Studio provides the full project graph, build setup, and platform details directly into your agent using [Agent Client Protocol (ACP)](https://agentclientprotocol.com/get-started/introduction) . The agent can then filter to relevant files or details for efficient token usage, lower latency, and sharper answers.
- **Seamless workflow continuity:** Transition smoothly between multiple conversational agent prompts and Android Studio's purpose-built tools, keeping your flow state intact as you effortlessly jump between tasks.
- **Agent flexibility:** Connect any ACP-compliant agent directly into Android Studio, and sign in with your plan. If one agent runs out of quota or isn't meeting your performance expectations, you can have another agent take over.
- **Native tool injection:** We wire up build diagnostics, UI tools like Jetpack Compose Previews, Android SDK tools, and Android emulator control so your agent has access and can test, diagnose, and execute directly in Android Studio.

## Powerful, capable, and reliable coding agents

Agents can plan and execute complete technical workflows directly in your environment, unlocking powerful use cases:

- **Execute in the environment:** Read, write, and edit files, run shell commands, run tests, and search the web.
- **Delegate to subagents:** Break down complex projects by spawning specialized agents for subtasks like code review or testing.
- **Stay in control:** Granular permissions let the agent act on its own for routine work, and pause for your approval on riskier actions.
- **Persist context and configuration:** Maintain long-running sessions and automatically load project skills, slash commands, and memory.

Agents running in Android Studio also benefit from Android skills and the Android Knowledge Base, ensuring they have access to the latest Android best practices. And if you want to learn more about how agents impact model performance, read more about our [latest updates to Android Bench](http://android-developers.googleblog.com/2026/09/android-bench-2-long-horizon-tasks.html).

## Using Gemini with Google Antigravity

Many developers have been using Gemini directly in Android Studio through the built-in agent, and we will continue to offer this experience in Android Studio. However, for the best experience with Gemini, we recommend selecting the Google Antigravity agent for access to the latest Gemini models such as Gemini Flash 3.8, along with increased AI usage quota. You can also login to the Google Antigravity agent with your [Google AI Pro or Ultra plan](https://one.google.com/intl/en_us/about/google-ai-plans/#code) to take advantage of your benefits in Android Studio, or pay per token rates with a Gemini API key.
![Antigravity_AgentSelector.png](https://developer.android.com/static/blog/assets/Antigravity_Agent_Selector_4a00f63d05_7KWCV.webp) Selecting the Google Antigravity agent

## Selecting the Google Antigravity agent

If your organization is using [Gemini Enterprise](https://developer.android.com/ai-in-android#why-enterprise-developers-choose-ai-in-android-studio), you can continue to use the built-in agent or the Antigravity agent. In either case, your organization continues to benefit from the added security and privacy of Google Cloud.
![Antigravity_Agent_Registry.png](https://developer.android.com/static/blog/assets/Antigravity_Agent_Registry_8df46674a8_1gxDWk.webp) Log in to the Antigravity Agent using a Google account, Gemini Enterprise license, Enterprise Agent platform or Gemini API key

## Get started

BYOA support is rolling out in preview starting with the [canary release of Android Studio Rabbit 2](https://developer.android.com/studio/preview) featuring commonly used agents like Google Antigravity, Claude Agent, and Codex. Both enterprise and consumer AI plans are supported - subject to the agent provider. To connect an agent, follow these steps:

1. **Update Android Studio:** Ensure you are running the latest from the [canary release channel](https://developer.android.com/studio/preview).
2. **Connect your agent(s):** In the agent window, select one of the agents (Claude Agent, Codex, or Antigravity) and sign-in or provide an API key. Additional agents can be found in the registry Settings \> Tools \> AI \> Agents
3. **Explore the docs:** Check out our [preview release note](http://d.android.com/studio/preview/features#bring-your-own-agent) here.

Your feedback is essential as we continue to refine the AI experience in Android Studio. If you find a bug or issue, please [file an issue](https://developer.android.com/studio/report-bugs). We can't wait to see what you build!
- [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Written by:

-

  ## [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner)

  ###### Product Manager

  [read_more
  View profile](https://developer.android.com/blog/authors/matthew-warner) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp) ![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)
Continue reading
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
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 19 May 2026 19 May 2026 ![](https://developer.android.com/static/blog/assets/Google_For_Developers_Android_Combo_Strapi_2000x1000_5793c01e36_2bzRoq.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Android Studio I/O Edition: What's new in Android Developer tools](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools)

  [arrow_forward](https://developer.android.com/blog/posts/android-studio-i-o-edition-what-s-new-in-android-developer-tools) This year at Google I/O we are going beyond iterative changes, towards a fundamental shift in how apps are built. Our newest tools are built for the agentic era with features that boost productivity for you as an Android developer AND supercharge the AI agents you deploy in your codebase.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 8 min read
  - [#Agent Skills](https://developer.android.com/blog/topics/agent-skills)
  - [#Google I/O](https://developer.android.com/blog/topics/google-i-o)
  - [#Android](https://developer.android.com/blog/topics/android)
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
  - +2 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)