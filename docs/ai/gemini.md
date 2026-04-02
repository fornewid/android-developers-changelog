---
title: Gemini AI models  |  Android Developers
url: https://developer.android.com/ai/gemini
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [AI](https://developer.android.com/ai)
* [Guides](https://developer.android.com/ai/overview)

# Gemini AI models Stay organized with collections Save and categorize content based on your preferences.




The Gemini Pro and Gemini Flash model families offer Android developers
multimodal AI capabilities, running inference in the cloud and processing image,
audio, video, and text inputs in Android apps.

* **Gemini Pro**: Gemini Pro is Google's state-of-the-art thinking model,
  capable of reasoning over complex problems in code, math, and STEM, as well as
  analyzing large datasets, codebases, and documents using long context.
* **Gemini Flash**: The Gemini Flash models deliver next-gen features and
  improved capabilities, including superior speed, built-in tool use, and a 1M
  token context window.

**Note:** This document covers the cloud-based Gemini AI models. For on-device
inference, [check out the Gemini Nano documentation](/ai/gemini-nano).

## Firebase AI Logic

Firebase AI Logic enables developers to securely and directly add Google's
generative AI into their apps simplifying development, and offers tools and
product integrations for successful production readiness. It provides client
Android SDKs to directly integrate and call the Gemini API from client code,
simplifying development by eliminating the need for a backend.

## API providers

Firebase AI Logic lets you use the following Google Gemini API providers:
Gemini *Developer API* and Vertex *AI Gemini API*.

![Illustration that shows an Android app using the Firebase Android SDK
    to connect to Firebase in the cloud. From there, AI logic integrates using
    two paths: the Gemini Developer API or Google Cloud Platform's Vertex AI,
    both leveraging Gemini Pro & Flash models.](/static/ai/assets/images/firebase-ai-logic.svg)


**Figure 1.**
Firebase AI Logic integration architecture.

Here are the primary differences for each API provider:

[**Gemini Developer API**](/ai/gemini/developer-api):

* Get started at no-cost with a generous free tier without payment information
  required.
* Optionally upgrade to the paid tier of the Gemini Developer API to scale as
  your user base grows.
* Iterate and experiment with prompts and even get code snippets using
  [Google AI Studio](https://aistudio.google.com/).

[**Vertex AI Gemini API**](/ai/vertex-ai-firebase):

* Granular control over [where you access the model](https://cloud.google.com/compute/docs/regions-zones).
* Ideal for developers already embedded in the Vertex AI/Google Cloud ecosystem.
* Iterate and experiment with prompts and even get code snippets using
  [Vertex AI Studio](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart).

Selecting the appropriate API provider for your application is based on your
business and technical constraints, and familiarity with the Vertex AI and
Google Cloud ecosystem. Most Android developers just getting started with Gemini
Pro or Gemini Flash integrations should begin with the Gemini Developer API.
Switching between providers is done by changing the parameter in the model
constructor:

### Kotlin

```
// For Vertex AI, use `backend = GenerativeBackend.vertexAI()`
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel("gemini-2.5-flash")

val response = model.generateContent("Write a story about a magic backpack")
val output = response.text

GeminiOverview

.kt
```