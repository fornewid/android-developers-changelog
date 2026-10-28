---
title: https://developer.android.com/ai/overview
url: https://developer.android.com/ai/overview
source: md.txt
---

This guide helps you find the right AI/ML solution for your use case. It
provides guidance to help you navigate the various solutions available and
choose the one that best fits your needs, given the requirements of the feature
you want to implement.

In general, when choosing tools and models to implement your AI/ML feature, you
should use the simplest model that fulfills your needs. To identify the optimal
solution, you need to think through the following:

> [!IMPORTANT]
> **Key Point:** You should use the simplest model and tooling that fulfills your needs.

- Does the feature need to generate new content (generative AI), or predict/categorize in a deterministic way (traditional ML)?
- Feature scope: can the task be done entirely within your app (in-app intelligence), or does it require multiple apps to accomplish (system-level intelligence)?
- Model location: can the task be done offline (on-device model), or does it require interacting with a server (cloud-based model)?
- Toolkit or model version: how complex is the task, ranging from simple, single-inference tasks to multi-agent orchestration?

The following flow chart shows the decision process at a high level:
Yes No Yes No Yes No Yes Not all Yes No Feature Do you need to generate new content (rather than predict or classify data)? Generative AI Is it a cross-app task? Traditional ML System intelligence Use AppFunctions In-app intelligence Can the feature run offline, or do you have cost constraints? Do the target devices support on-device models? Do you need the feature to keep running (the state to be preserved) when the app is closed, or need private database access? On-device model Use Gemini Nano through ML Kit, or LiteRT Hybrid approach Prefer on-device models, but use cloud models as fallback Cloud-based model Use custom self-hosted server Cloud-based model Use managed backend through Firebase AI Logic [](https://developer.android.com/ai/overview#system-level-intelligence) [](https://developer.android.com/ai/overview#on-device-models) [](https://developer.android.com/ai/overview#hybrid-approach) [](https://developer.android.com/ai/overview#cloud-based-models) [](https://developer.android.com/ai/overview#cloud-based-models) **Figure 1.** High-level decision process for choosing an AI/ML solution.

To inform your decision at each step, refer to sections in the rest of this
document.

## Generative AI versus traditional ML

Generative AI models create new content, whereas traditional ML models predict
outcomes or categorize data in a completely deterministic manner. If your
feature doesn't involve generating new content, then traditional ML solutions
might be sufficient. The following table summarizes some traditional ML
solutions:

> [!NOTE]
> **Note:** Most of these toolkits offer both GenAI and traditional ML solutions. Refer to the non-GenAI documentation sections for the traditional ML guides.

| Toolkit / Solution | Type | Primary use case | Examples |
|---|---|---|---|
| [ML Kit SDK](https://developers.google.com/ml-kit) | On-device | Pre-built vision and natural language processing tasks | - OCR receipt scanner - Fast event QR check-ins - Offline menu translation |
| [LiteRT](https://developer.android.com/ai/custom) | On-device | Custom model runtimes | - Medical image classification - Smart keyboard word prediction for niche subject matter |
| [MediaPipe](https://developers.google.com/edge/mediapipe/solutions/guide) | On-device | Real-time video or audio stream perception tasks | - Real-time workout pose coaching - Facial filters and effects - Hand gesture recognition |
| Google Cloud APIs including [Cloud Vision API](https://docs.cloud.google.com/vision/docs) and [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs) | Cloud-based | Pre-built vision and natural language processing tasks | - Automated video captioning - Image quality control and compliance |
| [Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning) | Cloud-based | End-to-end custom model training and deployment | - Specialized image recognition at scale - Stock photo search |

The rest of this document is about generative AI solutions.

## In-app versus system-level intelligence

To identify the best generative AI solution, decide whether your AI feature
works entirely within your app or if it requires interacting with other apps or
the Android OS, outside of any app. If your feature is triggered by the system,
outside of any app, then it counts as system-level intelligence. The following
table summarizes the differences between in-app and system-level intelligence
features:

|   | In-app intelligence | System-level intelligence |
|---|---|---|
| **Task scope** | In-app | Across apps (or triggered by the system, outside any app) |
| **Tools** | ML Kit SDK, LiteRT, Firebase AI Logic, or self-hosted backend | AppFunctions |
| **Use cases** | - Summarize, proofread, or transcribe text - Describe images - Build an in-app chatbot - Generate images | - Build a grocery list in a delivery app based on what you wrote in a notes document - Book a ride to the office and message your coworker your estimated time of arrival - Find a restaurant recommendation in your email inbox and make a reservation |

## In-app intelligence

In-app intelligence features don't need to interact with other apps or the
system beyond the app. Once you determine that your AI feature is entirely
in-app, you need to decide whether you can run the feature completely on-device,
use a cloud-based model, or do a hybrid approach that combines both.

If you're doing anything that requires video input or tasks that involve
multiple agents, then you should use a cloud-based model. The following table
compares the capabilities of on-device versus cloud-based models:

|   | On-device | Cloud |
|---|---|---|
| **Tools** | ML Kit SDK or LiteRT | Firebase AI Logic or self-hosted backend |
| **Input type** | - Text - Image - Audio | - Text - Image - Audio - Video |
| **Output type** | - Text | - Text - Image - Audio |
| **User data sensitivity** | Higher | Lower |
| **Models** | - Gemma - Gemini Nano | - Gemini Flash - Gemini Flash Lite - Gemini Pro |
| **Use cases** | - Process short content, for example summarize, proofread, or rewrite a short chat message or email - Describe images - Personalize output for users based on their interests - Handle sensitive user data - Transcribe a short audio clip | - Build a chatbot - Generate images - Translate conversations real-time - In-app photo editing - Multi-agent tasks |

### On-device models

On-device models are probably preferable if any of the following apply:

- Cost constraints
- Feature must be able to run offline
- Privacy requirements
- The task at hand is relatively simple---it doesn't require multi-agent orchestration

Keep in mind that your users' devices must be able to support on-device models.
On-device models typically require more premium devices that can support the
local processing.

Once you've determined that on-device models are sufficient for your feature,
the optimal toolkit or solution depends primarily on the task complexity. The
following table summarizes the options for on-device, in-app generative AI
tooling:

| Task complexity | Feature characteristics | Example | Toolkit/Solution |
|---|---|---|---|
| Low | - Single inference - Pure generation | Summarize text | - [ML Kit SDK](https://developers.google.com/ml-kit/genai) - [LiteRT](https://developers.google.com/edge/litert) for fine-tuned models (niche domains) |
| Medium | - Augmented LLM - Function calling - Conversation history | Query and response | - [ML Kit Prompt API](https://developers.google.com/ml-kit/genai/prompt/android) |
| High | - Single-agent loop, cycling through until task is completed | Customer feedback or bug triage | - [ML Kit GenAI Agent API](https://developers.google.com/ml-kit/genai/agent/android) |

Use the ML Kit Prompt API for straightforward single-turn or multi-turn
conversational text generation. When your feature requires autonomous,
multi-step execution on-device, use the ML Kit GenAI Agent API. The Agent API
supports on-device reasoning loops that can plan, invoke typed tools using
`@Tool` annotations, persist session context across interactions, and enforce
turn limits using `maxTurns`.

### Cloud-based models

If your feature can't be run entirely on-device, you need to use a cloud-based
model. There are two main options for how to use a cloud-based model:

- Managed backend using [Firebase AI Logic](https://firebase.google.com/docs/ai-logic). If you're
  already a Firebase user or want to prototype something relatively quickly,
  Firebase AI Logic is probably the best solution.

  > [!NOTE]
  > **Note:** Firebase AI Logic SDK only supports Gemini models.

- Custom backend, or self-hosted server. If you want to use non-Gemini models,
  have strict privacy requirements, or need to complete a very complex task, you
  probably need to use a custom backend. We also recommend the following tools
  for the custom backend setup:

  - Have your custom backend run an agentic framework such as [Agent Development Kit](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk)
  - Connect the app frontend to the agentic backend using [AG-UI](https://github.com/ag-ui-protocol/ag-ui)
  - Enable agents to generate rich, interactive UIs using [A2UI](https://github.com/a2ui-project/a2ui)

The following table summarizes when to use Firebase AI Logic or a custom backend
for cloud-based, in-app generative AI tooling:

| Task complexity | Feature characteristics | Example | Toolkit/Solution |
|---|---|---|---|
| Low | - Single inference - Pure generation | Summarize text | - Firebase AI Logic - Custom backend |
| Medium | - Augmented LLM - Function calling - Conversation history | Query and response | - Firebase AI Logic - Custom backend |
| High | - Single-agent loop, cycling through until task is completed | Customer feedback or bug triage | - Custom backend |
| Very high | - Multi-agent orchestration | Create an agent team for managing different aspects of a trip | - Custom backend |

### Hybrid approach

Use a hybrid approach when your feature can run locally, but not all of your
users have devices that support on-device models and you need to use cloud
models as a fallback. For more information, see [Hybrid inference](https://developer.android.com/ai/hybrid).

## System-level intelligence

System-level intelligence enables the Android platform to act as a task
orchestrator. System-level intelligence enables system agents, such as Gemini,
to complete user requests across multiple apps and web services.

To connect your app with the Android intelligence system, choose an integration
method based on whether you want programmatic control or automated UI-driven
actions:

| Integration option | Use case |
|---|---|
| [AppFunctions](https://developer.android.com/ai/appfunctions) | Make specific capabilities on your app available for agents to discover and execute on-device. |
| Remote MCP server | Make specific capabilities on your app available to integrate directly with the agent's backend. Good for cross-platform development. |
| [Computer Control](https://developer.android.com/ai/computer-control) | Allows an OEM-preloaded assistant to automate tasks by interacting directly with an app's UI. |

For more information on system-level intelligence tooling options, see
[Connect your app to the Android intelligence system](https://developer.android.com/ai/intelligence-system).