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
both leveraging Gemini Pro & Flash models.](https://developer.android.com/static/ai/assets/images/firebase-ai-logic.svg) **Figure 1.** Firebase AI Logic integration architecture.

Here are the primary differences for each API provider:

[**Gemini Developer API**](https://developer.android.com/ai/gemini/developer-api):

- Get started at no-cost with a generous free tier without payment information required.
- Optionally upgrade to the paid tier of the Gemini Developer API to scale as your user base grows.
- Iterate and experiment with prompts and even get code snippets using [Google AI Studio](https://aistudio.google.com/).

[**Vertex AI Gemini API**](https://developer.android.com/ai/vertex-ai-firebase):

- Granular control over [where you access the model](https://cloud.google.com/compute/docs/regions-zones).
- Ideal for developers already embedded in the Vertex AI/Google Cloud ecosystem.
- Iterate and experiment with prompts and even get code snippets using [Vertex AI Studio](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart).

Selecting the appropriate API provider for your application is based on your
business and technical constraints, and familiarity with the Vertex AI and
Google Cloud ecosystem. Most Android developers just getting started with Gemini
Pro or Gemini Flash integrations should begin with the Gemini Developer API.
Switching between providers is done by changing the parameter in the model
constructor:


### Kotlin

```kotlin
// For Vertex AI, use `backend = GenerativeBackend.vertexAI()`
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel("gemini-2.5-flash")

val response = model.generateContent("Write a story about a magic backpack")
val output = response.texthttps://github.com/android/snippets/blob/3c1b5647e280eca2ba7dcf4433e22ad5f8197663/misc/src/main/java/com/example/snippets/ai/GeminiOverview.kt#L27-L32
```

### Java

```java
// For Vertex AI, use `backend = GenerativeBackend.vertexAI()`
GenerativeModel firebaseAI = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel("gemini-2.5-flash");

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

See the full [list of available generative AI models](https://firebase.google.com/docs/vertex-ai/models) supported
by Firebase AI Logic client SDKs.

## Firebase services

In addition to access to the Gemini API, Firebase AI Logic offers a set of
services to simplify the deployment of AI-enabled features to your app and get
ready for production:

### App Check

[Firebase App Check](https://firebase.google.com/docs/app-check) safeguards app backends from abuse by
ensuring only authorized clients access resources. It integrates with Google
services (including Firebase and Google Cloud) and custom backends. App Check
uses [Play Integrity](https://developer.android.com/google/play/integrity) to verify that requests originate from the authentic
app and an untampered device.

### Remote Config

Instead of hardcoding the model name in your app, we recommend using a
server-controlled variable using [Firebase Remote Config](https://firebase.google.com/docs/remote-config). This
lets you dynamically update the model your app uses without having to deploy a
new version of your app or require your users to pick up a new version. You can
also use Remote Config to [A/B test](https://firebase.google.com/docs/ab-testing/abtest-config) models and prompts.

### AI monitoring

To understand how your AI-enabled features are performing you can use the [AI
monitoring dashboard](https://firebase.google.com/docs/vertex-ai/monitoring) within the Firebase console. You'll get
valuable insights into usage patterns, performance metrics, and debugging
information for your Gemini API calls.

## Migrate to Firebase AI Logic

If you're already using the Vertex AI in Firebase SDK in your app, read the
[migration guide](https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk).