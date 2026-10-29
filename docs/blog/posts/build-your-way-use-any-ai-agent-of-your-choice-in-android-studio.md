---
title: https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio
url: https://developer.android.com/blog/posts/build-your-way-use-any-ai-agent-of-your-choice-in-android-studio
source: md.txt
---

[Product News](https://developer.android.com/blog/categories/product-news)

# Build your way: Use any AI agent of your choice in Android Studio

3 min read ![](https://developer.android.com/static/blog/assets/BYOA_Backup_Strapi_1_5c3f94f766_Z1WI1Mt.webp) 24 Sep 2026 [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) Product Manager, Android Developer Experience AI-powered developer tools have become an essential multiplier for engineering productivity, with teams adopting specialized AI coding agents, custom enterprise harnesses, and autonomous tools. It's important for you to be able to build Android apps in the way that works best for you and your team, and agentic Android development is more open and flexible than ever before.

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
- [![View Matthew Warner's profile](https://developer.android.com/static/blog/assets/matthew_warner_67a99317e4_ZNF3fo.webp)](https://developer.android.com/blog/authors/matthew-warner) 28 Oct 2026 28 Oct 2026 ![](https://developer.android.com/static/blog/assets/Rabbit2_Strapi_27563aeaf4_1BAzRM.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Your favorite agents are now integrated in Android Studio](https://developer.android.com/blog/posts/ai-agents-android-studio-integration)

  [arrow_forward](https://developer.android.com/blog/posts/ai-agents-android-studio-integration) Android Studio Rabbit 2 is now stable and ready for you to use in production. This release includes key features to improve your development such as Bring Your Own Agent, new XR Emulator features, a LeakCanary update, a new agent skills manager tool, AI code review, and more.
  [Matthew Warner](https://developer.android.com/blog/authors/matthew-warner) • 3 min read
  - [#Android Studio](https://developer.android.com/blog/topics/android-studio)
- [![View Jason Buchel's profile](https://developer.android.com/static/blog/assets/unnamed_25_28af9250eb_I4mHO.webp)](https://developer.android.com/blog/authors/jason-buchel) 13 Oct 2026 13 Oct 2026 ![](https://developer.android.com/static/blog/assets/Blog_0140_strapi_8d85f71a6e_ZvGJv2.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Bringing our latest frontier model to Android Developers](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli)

  [arrow_forward](https://developer.android.com/blog/posts/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli) As agentic development accelerates, Android engineering is reaching an exciting new frontier: moving from assistive code completion to agents executing end-to-end under your direction. You have total choice and flexibility in the models and agents you use.
  [Jason Buchel](https://developer.android.com/blog/authors/jason-buchel) • 3 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
- [![View Simona Milanovic's profile](https://developer.android.com/static/blog/assets/Screenshot_2026_05_19_at_9_30_31_AM_4ebf3b750d_OxFbo.webp)](https://developer.android.com/blog/authors/simona-milanovic) 02 Oct 2026 02 Oct 2026 ![](https://developer.android.com/static/blog/assets/ABL_135_Android_CLI_and_Android_skills_Strapi_d22702426a_ZIUXgH.webp) [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Device Streaming and Android skills - available in Android CLI](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills)

  [arrow_forward](https://developer.android.com/blog/posts/android-cli-device-streaming-and-skills) As Android developers, you have many choices when it comes to the agents, LLMs, tools, and command-line interfaces (CLI) you use for app development. Our goal is to help you build beautiful, high-quality Android apps, no matter how you choose to build.
  [Simona Milanovic](https://developer.android.com/blog/authors/simona-milanovic) • 4 min read
  - [#Agentic Android development](https://developer.android.com/blog/topics/agentic-android-development)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)