---
title: https://developer.android.com/ai/gemini-nano
url: https://developer.android.com/ai/gemini-nano
source: md.txt
---

Gemini Nano lets you deliver rich generative AI experiences without needing
a network connection or sending data to the cloud. On-device AI is a great
solution for use-cases where low cost and privacy safeguards are your primary
concerns.

For on-device use-cases, you can take advantage of Google's Gemini Nano
foundation model. [Gemini Nano runs in Android's AICore system service](https://android-developers.googleblog.com/2023/12/a-new-foundation-for-ai-on-android.html),
which leverages device hardware to enable low inference latency and keeps the
model up-to-date.

## ML Kit GenAI APIs

ML Kit's GenAI APIs harness the power of Gemini Nano to help your apps perform
on-device generative AI tasks. These APIs are built on top of AICore, an
Android system service that enables on-device execution of GenAI foundation
models to facilitate features such as enhanced app functionality and improved
user privacy by processing data locally. [Learn more](https://developers.google.com/ml-kit/genai).

> [!NOTE]
> **Note:** The [ML Kit GenAI API Additional Terms of Service](https://developers.google.com/ml-kit/genai-terms) apply to the use of the GenAI APIs. Developers are solely responsible for the safety of their API client and their app's user experience.

### Key features

ML Kit organizes its GenAI capabilities into the following categories:

#### Custom generation and agents

Work directly with the Gemini Nano foundation model for custom use cases:

- [**Direct model access**](https://developers.google.com/ml-kit/genai/prompt/android) (using the `GenerativeModel` class): Generate text or typed structured output from custom text-only or multimodal prompts, or manage your own multi-turn chat history directly by using a `List<Content>` object with `USER` and `MODEL` roles and a `sessionId` value.
- [**Agentic workflows**](https://developers.google.com/ml-kit/genai/agent/android) (using the `AgentRunner` class): Built on top of the `GenerativeModel` class, automating multi-turn session management (including in-memory conversation history) and multi-step tool-calling loops.

#### Speech and audio

Transcribe, translate, and synthesize speech audio on-device:

- [**Speech Recognition**](https://developers.google.com/ml-kit/genai/speech-recognition/android): Transcribe spoken audio content into text in the same language.
- [**Speech Translation**](https://developers.google.com/ml-kit/genai/speech-translation/android): Translate spoken audio into text in another language in real time.
- [**Text to Speech**](https://developers.google.com/ml-kit/genai/text-to-speech/android): Synthesize natural-sounding speech audio from text.

#### Text and image tasks

Use task-specific APIs optimized for common vision, writing, and search tasks
through a high-level interface:

- [**Image Description**](https://developers.google.com/ml-kit/genai/image-description/android): Generate a short description of a given image.
- [**Summarization**](https://developers.google.com/ml-kit/genai/summarization/android): Summarize articles or conversations as a bulleted list.
- [**Proofreading**](https://developers.google.com/ml-kit/genai/proofreading/android): Proofread short chat messages.
- [**Rewriting**](https://developers.google.com/ml-kit/genai/rewriting/android): Rewrite short chat messages in different tones or styles.
- [**Semantic Search**](https://developers.google.com/ml-kit/genai/embedding/android): Generate vector embeddings for text and images using the Embedding API and pair them with AndroidX AppSearch to find content by meaning.


## Android skills

[View on GitHub](https://github.com/android/skills/tree/main/device-ai/ml-kit-genai-prompt-api)

### Use the ML Kit Prompt API

Use an [Android skill](https://developer.android.com/tools/agents/android-skills) to integrate and optimize the ML Kit Prompt API in your app. To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:

    android skills add ml-kit-genai-prompt-api

<br />

## Architecture through AICore

As a system-level module, you access AICore through a series of APIs in order to
run inference on-device. In addition, AICore has several built-in safety
features, ensuring a thorough evaluation against our safety filters. The
following diagram outlines how an app accesses AICore to run Gemini Nano
on-device.
![A diagram showing how an Android app uses the Google AI Edge SDK to
access AICore, where Gemini Nano, LoRA, and safety features are managed
and run on hardware accelerators.](https://developer.android.com/static/images/ai/aicore/gemini-architecture-google-ai-edge-sdk.png) **Figure 1.** AICore serves as the interface between your app and the Gemini Nano model, managing model updates and safety while leveraging on-device hardware.

## Keep user data private and secure

On-device generative AI executes prompts locally, eliminating server calls.
While this removes network latency, inference speed depends on device hardware.
This approach enhances privacy by keeping sensitive data on the device,
enables offline functionality, and reduces inference costs.

AICore adheres to the [Private Compute Core](https://arxiv.org/abs/2209.10317) principles, with the following
key characteristics:

- **Restricted Package Binding**: AICore is isolated from most other packages, with limited exceptions for specific system packages. Any modifications to this allowed list can only occur during a full Android OTA update.
- **Indirect Internet Access** : AICore does not have direct internet access. All internet requests, including model downloads, are routed through the open-source [Private Compute Services](https://github.com/google/private-compute-services) companion APK. APIs within Private Compute Services must explicitly demonstrate their privacy-centric nature.

Additionally, AICore is built to isolate each request and doesn't store
any record of the input data or the resulting outputs after processing
them to protect user privacy. Read the blog post
[An Introduction to Privacy and Safety for Gemini Nano](https://android-developers.googleblog.com/2024/10/introduction-to-privacy-and-safety-gemini-nano.html) to learn more.
![A detailed architecture diagram of AICore showing the request flow:
API surface, input processing with safety signals, feature configuration,
runtime with model weights and LoRAs, and output processing with safety
signals. It also shows model downloads via Private Compute Services.](https://developer.android.com/static/images/ai/aicore-architecture.png) **Figure 2.** The AICore architecture manages input and output safety, request processing, and model weights to provide a secure environment for on-device AI.

## Benefits of accessing AI foundation models with AICore

AICore enables the Android OS to provide and manage AI foundation models.
This significantly reduces the cost of using these large models in your app,
principally due to the following:

- **Ease of deployment**: AICore manages the distribution of Gemini Nano and handles future updates. You don't need to worry about downloading or updating large models over the network, nor impact on your app's disk and runtime memory budget.
- **Accelerated inference**: AICore leverages on-device hardware to accelerate inference. Your app gets the best performance on each device, and you don't need to worry about the underlying hardware interfaces.

## When to use hybrid inference

Although Gemini Nano is ideal for offline and privacy-sensitive tasks, it has
on-device constraints such as token limits, device hardware limitations, and
model capability boundaries. In these scenarios, you can use
[hybrid inference](https://developer.android.com/ai/hybrid) to balance AI workloads between the local device and the
cloud.

To ensure a consistent user experience across all devices and handle complex
queries, you can use the [Firebase AI Logic Hybrid API](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started). This lets your app
do the following:

- **Fall back gracefully**: Automatically route requests to Gemini Flash or Gemini Pro models in the cloud when Gemini Nano is unavailable or unsupported on the user's device.
- **Enforce security** : Protect cloud inference with [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) (and its supported attestation providers, like Play Integrity) and keep sensitive system prompts server-side.