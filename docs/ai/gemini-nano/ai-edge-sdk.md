---
title: https://developer.android.com/ai/gemini-nano/ai-edge-sdk
url: https://developer.android.com/ai/gemini-nano/ai-edge-sdk
source: md.txt
---

> [!CAUTION]
> **Caution:** The experimental Google AI Edge SDK is deprecated. We recommend using the [ML Kit Prompt API](https://developers.google.com/ml-kit/genai/prompt/android) to send custom prompts to Gemini Nano.

Google AI Edge SDK allows experimental access for developers seeking to test
enhancement of their apps with on-device AI capabilities through Gemini Nano.

## Architecture through AICore

As a system-level module, you access AICore through a series of APIs in order to
run inference on-device. In addition, AICore has several built-in safety
features, ensuring a thorough evaluation against our safety filters. The
following diagram outlines how an app accesses AICore to run Gemini Nano
on-device.
![Google AI Edge SDK, AICore, and Gemini Nano.](https://developer.android.com/static/images/ai/aicore/gemini-architecture-google-ai-edge-sdk.png) **Figure 1.** Google AI Edge SDK, AICore, and Gemini Nano.

## Keep user data private and secure

On-device generative AI executes prompts locally, eliminating server calls. This
approach enhances privacy by keeping sensitive data on the device, enables
offline functionality, and reduces inference costs.

AICore adheres to the [Private Compute Core](https://arxiv.org/abs/2209.10317) principles, with the following
key characteristics:

- **Restricted Package Binding**: AICore is isolated from most other packages, with limited exceptions for specific system packages. Any modifications to this allowed list can only occur during a full Android OTA update.
- **Indirect Internet Access** : AICore does not have direct internet access. All internet requests, including model downloads, are routed through the open-source [Private Compute Services](https://github.com/google/private-compute-services) companion APK. APIs within Private Compute Services must explicitly demonstrate their privacy-centric nature.

Additionally, AICore is built to isolate each request and doesn't store
any record of the input data or the resulting outputs after processing
them to protect user privacy. Read the blog post
[An Introduction to Privacy and Safety for Gemini Nano](https://android-developers.googleblog.com/2024/10/introduction-to-privacy-and-safety-gemini-nano.html) to learn more.
![Illustration of the AICore architecture](https://developer.android.com/static/images/ai/aicore-architecture.png) **Figure 2.** AICore architecture

## Benefits of accessing AI foundation models with AICore

AICore enables the Android OS to provide and manage AI foundation models.
This significantly reduces the cost of using these large models in your app,
principally due to the following:

- **Ease of deployment**: AICore manages the distribution of Gemini Nano and handles future updates. You don't need to worry about downloading or updating large models over the network, nor impact on your app's disk and runtime memory budget.
- **Accelerated inference**: AICore leverages on-device hardware to accelerate inference. Your app gets the best performance on each device, and you don't need to worry about the underlying hardware interfaces.

## Supported functionality

- **Supported Devices** : Gemini Nano with the Google AI Edge SDK is available for [experimentation](https://developer.android.com/ai/gemini-nano/experimental) on Pixel 9 series devices.
- **Supported Modalities**: AICore supports text modality for Gemini Nano.

Additional device and modality support are areas of active investment.

## Use cases

Due to the resource constraints of mobile devices compared to cloud servers,
on-device generative AI models are designed with a focus on efficiency and size.
This optimization prioritizes specific, well-defined tasks over more generalized
applications. Suitable use cases include:

- **Text Rephrasing**: Modify the tone and style of text (e.g., casual to formal).
- **Smart Reply**: Generate contextually relevant responses within a chat thread.
- **Proofreading**: Identify and correct spelling and grammatical errors.
- **Summarization**: Condense lengthy documents into concise summaries (paragraph or bullet points).

For optimal performance, refer to the [prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
documentation.

Gemini Nano is used by several Google apps. Some examples include:

- **Talkback:** Android's accessibility app [Talkback](https://android-developers.googleblog.com/2024/09/talkback-uses-gemini-nano-to-increase-low-vision-accessibility.html) leverages Gemini Nano's multimodal input capabilities to improve image descriptions for visually impaired users.
- **Pixel Voice Recorder:** The [Pixel Voice Recorder](https://android-developers.googleblog.com/2024/08/recorder-app-on-pixel-sees-boost-in-engagement-with-gemini-nano.html) app uses Gemini Nano and AICore to power an on-device summarization feature. The Recorder team adopted the latest Gemini Nano model to support longer recordings and delivers higher quality summaries.
- **Gboard:** Gboard smart reply leverages on-device Gemini Nano with AICore to provide accurate smart replies.