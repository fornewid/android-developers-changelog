---
title: https://developer.android.com/ai/intelligence-system
url: https://developer.android.com/ai/intelligence-system
source: md.txt
---

<br />

User expectations for AI on their devices are fundamentally shifting how they interact with their apps. Instead of opening apps to do tasks step-by-step, they're asking AI to perform steps for them, often across multiple apps. ![user-evolution](https://developer.android.com/static/ai/images/user-evolution.png)

<br />

To meet these user needs, the Android platform is evolving into an intelligence system that transitions the OS from an application launchpad into an active task orchestrator. Android provides you with the following new capabilities that include on-device APIs and complementary cloud integrations, enabling system agents such as Google Gemini to execute tasks across local applications and web services securely and contextually.

> [!WARNING]
> **Preview:** While we're in the early stages of this journey, we're designing these features with privacy and security at their core as our first step in exploring this paradigm shift as an app ecosystem.

- You're fully in control with the following options:

  - **AppFunctions** : AppFunctions is an Android platform API with an accompanying Jetpack library to simplify Android MCP integration. AppFunctions lets your app make specific capabilities available as discrete functions that agents can discover and execute on-device. This enables deep, secure, and performant integrations. Browse our resources for AppFunctions, including [documentation](https://developer.android.com/ai/appfunctions), [samples](https://github.com/android/appfunctions), and [skills](https://github.com/android/skills/tree/main/device-ai/appfunctions).

  - **Remote MCP server** : With the server-side MCP approach, your app makes specific capabilities available to agents that can directly integrate with its backend. It's a complementary approach that is a good option for coverage across Android and other platforms. Read the [Model Context Protocol docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers) for details.

- With this feature, the OEM-preloaded assistant is in control:

  - **Computer Control** : Computer Control is an upcoming Android API that allows an OEM-preloaded assistant to automate tasks by interacting directly with an app's user interface. The target app doesn't need any explicit code changes to integrate. Read about [Computer Control](https://developer.android.com/ai/computer-control).