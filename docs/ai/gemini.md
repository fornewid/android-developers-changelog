---
title: https://developer.android.com/ai/gemini
url: https://developer.android.com/ai/gemini
source: md.txt
---

The Gemini Pro and Gemini Flash model families offer Android developers
multimodal AI capabilities, running inference in the cloud and processing image,
audio, video, and text inputs in Android apps.

- **Gemini Pro**: Gemini Pro is Google's state-of-the-art thinking model, capable of reasoning over complex problems in code, math, and STEM, as well as analyzing large datasets, codebases, and documents using long context.
- **Gemini Flash**: The Gemini Flash models deliver next-gen features and improved capabilities, including superior speed, built-in tool use, and a 1M token context window.

> [!NOTE]
> **Note:** This document covers the cloud-based Gemini AI models. For on-device inference, [check out the Gemini Nano documentation](https://developer.android.com/ai/gemini-nano).

## Firebase AI Logic

[Firebase AI Logic](https://firebase.google.com/docs/ai-logic) enables developers to securely and directly add Google's
generative AI into their apps simplifying development, and offers tools and
product integrations for successful production readiness. It provides client
Android SDKs to directly integrate and call the Gemini API from client code,
simplifying development by eliminating the need for a backend.

## API providers

Firebase AI Logic lets you use the following Google Gemini API providers:
*Gemini Developer API* and *Agent Platform Gemini API* (formerly Vertex AI).
![Illustration that shows an Android app using the Firebase Android SDK
to send requests to the Firebase backend in the cloud. Requests can be
routed to either the Gemini Developer API or the Agent Platform Gemini API,
both leveraging Gemini Pro and Flash models.](https://developer.android.com/static/ai/assets/images/firebase-ai-logic.svg) **Figure 1.** Firebase AI Logic integration architecture.

Here are the primary differences for each API provider:

[**Gemini Developer API**](https://developer.android.com/ai/gemini/developer-api):

- Get started at no-cost with a generous free tier without payment information required.
- Optionally upgrade to the paid tier of the Gemini Developer API to scale as your user base grows.
- Iterate and experiment with prompts and even get code snippets using [Google AI Studio](https://aistudio.google.com/).

[**Agent Platform Gemini API**](https://developer.android.com/ai/gemini/agent-platform-api) (formerly Vertex AI):

- Granular control over [where you access the model](https://firebase.google.com/docs/ai-logic/locations?api=vertex).
- Ideal for developers already embedded in the Google Cloud ecosystem.
- Iterate and experiment with prompts and even get code snippets using [Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart).

Selecting the appropriate Gemini API provider for your app is based on your
business and technical constraints. Most Android developers just getting started
with Gemini Pro and Flash models should begin with the Gemini Developer API.
Switching between providers is done by changing the parameter in the model
constructor:


### Kotlin

```kotlin
// For the Agent Platform Gemini API, use `backend = GenerativeBackend.agentPlatform()`
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel("gemini-3.5-flash")

val response = model.generateContent("Write a story about a magic backpack")
val output = response.text
```

### Java

```java
// For the Agent Platform Gemini API, use `backend = GenerativeBackend.agentPlatform()`
GenerativeModel firebaseAI = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel("gemini-3.5-flash");

// Use the GenerativeModelFutures Java compatibility layer which offers
// support for ListenableFuture and Publisher APIs
GenerativeModelFutures model = GenerativeModelFutures.from(firebaseAI);

Content prompt = new Content.Builder()
    .addText("Write a story about a magic backpack.")
    .build();

ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        String resultText = result.getText();
        // ...
    }

    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

## Access models on-device, in the cloud, or hybrid

In addition to the cloud-hosted Gemini models described in the previous section,
the Firebase AI Logic SDK also lets you access on-device models to build your
app's AI features. If you configure the SDK for [hybrid inference](https://developer.android.com/ai/hybrid), your
app can use an on-device model when it's available, but fall back seamlessly to
a cloud-hosted model when needed (and vice-versa).

The key benefits of a hybrid approach include:

- **Smart routing:** Simple tasks are handled on your device, while complex
  questions are automatically sent to the cloud for deeper analysis.

- **Offline availability**: Your apps keep working without internet by running
  models directly on your device. When you're back online, the cloud-hosted
  models can be accessed.

- **Lower costs**: Running everyday tasks on device instead of in the cloud
  reduces inference expenses.

## Security for your AI features

Firebase AI Logic supports several features that let you securely build AI
features in your app:

- **Verify app authenticity** : When you call the Gemini API directly
  from your Android app, the API is vulnerable to abuse by unauthorized
  clients. You need to help protect it from abuse by using Firebase AI Logic
  and enforcing [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check). When you enforce App Check, it
  will only allow incoming requests that are verified to be from your actual
  app or an untampered device. App Check supports both [Play Integrity](https://firebase.google.com/docs/app-check/android/play-integrity-provider)
  and [reCAPTCHA Enterprise](https://firebase.google.com/docs/app-check/android/recaptcha-enterprise-provider) as production attestation providers.

- **Store prompts server-side**: For your requests to the Gemini API
  using Firebase AI Logic, you can store your prompt, schema, and
  configurations in server-side prompt templates. Your app only passes the
  key (the template ID) from the client to the server. Using server prompt
  templates helps protect against exposing your prompt client-side.

- **Access on-device models**: You can use Firebase AI Logic to route
  your requests to an on-device model when it's available. The request,
  including the prompt, never leaves the device.

## Build for production

Firebase AI Logic helps you build robust AI features in your app and ensure that
they work in production. For details, check out the
[Firebase AI Logic production checklist](https://firebase.google.com/docs/ai-logic/production-checklist).

### Access and security

- Enforce [Firebase App Check](https://firebase.google.com/docs/ai-logic/app-check) to help protect the Gemini API from abuse
  when it's called directly from your app. When App Check is enforced, it
  verifies that incoming requests originate from your authentic app or an
  untampered device.

- Enforce [authenticated-users mode](https://firebase.google.com/docs/ai-logic/auth-mode) so that all requests from Firebase AI
  Logic must include valid credentials from [Firebase Authentication](https://firebase.google.com/docs/auth).

### Monitoring, limits, and billing

- Set up [AI monitoring in the Firebase console](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console) to gain visibility into
  key performance metrics, like request counts, latency, token usage, and
  error rates.

- Set [rate limits per user](https://firebase.google.com/docs/ai-logic/quotas#per-user-rate-limits) (default is 100 RPM) to prevent individual
  client instances from consuming excessive quota.

- Avoid surprise bills with [budget alerts](https://firebase.google.com/docs/projects/billing/budget-alerts) and [spend caps](https://firebase.google.com/docs/projects/billing/spend-caps).

### Management of configurations

- Make on-demand changes to the model name used for your AI feature as
  new models are released or others are shut down. See details for using
  [Remote Config](https://firebase.google.com/docs/ai-logic/change-model-name-remotely) or [server prompt templates](https://firebase.google.com/docs/ai-logic/server-prompt-templates/get-started).

- Use Remote Config to [set a minimum version for your app](https://firebase.google.com/docs/remote-config/use-cases/minimum-version) so that you
  can either show an upgrade notification to users or force users to upgrade.

- Test models and prompts with small groups of users using Remote Config and
  [Firebase A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config).