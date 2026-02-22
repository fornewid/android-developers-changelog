---
title: https://developer.android.com/ai/vertex-ai-firebase
url: https://developer.android.com/ai/vertex-ai-firebase
source: md.txt
---

> [!NOTE]
> **Note:** if you previously integrated Vertex AI in Firebase (with Gradle `import
> com.google.firebase:vertex-ai`) you can continue using Vertex AI as an API provider with the Firebase AI Logic SDK.

If you are new to the Gemini API, the [Gemini Developer API](https://developer.android.com/ai/gemini-developer-api) is the
recommended [API provider](https://developer.android.com/ai/gemini#api-providers) for Android Developers. But if you have specific
data [location requirements](https://cloud.google.com/compute/docs/regions-zones) or you are already embedded in the
Vertex AI or Google Cloud environment, you can use the Vertex AI Gemini API.

## Migration from Vertex AI in Firebase

If you originally integrated the Gemini Flash and Pro models using Vertex AI in
Firebase, you can migrate to and continue using Vertex AI as an API provider.
Read the Firebase documentation for a detailed [migration guide](https://firebase.google.com/docs/vertex-ai/migrate-to-latest-sdk).

## Getting started

Before you interact with the Vertex AI Gemini API directly from your app, you
can experiment with prompts in [Vertex AI Studio](https://console.cloud.google.com/vertex-ai/studio).

### Set up a Firebase project and connect your app to Firebase

Once you're ready to call the Vertex AI Gemini API from your app, follow the
instructions in the "Step 1" Firebase AI Logic getting started guide to set up
Firebase and the SDK in your app.

### Add the Gradle dependency

Add the following Gradle dependency to your app module:

    dependencies {
      // ... other androidx dependencies

      // Import the BoM for the Firebase platform
      implementation(platform("com.google.firebase:firebase-bom:34.9.0"))

      // Add the dependency for the Firebase AI Logic library. When using the BoM,
      // you don't specify versions in Firebase library dependencies
      implementation("com.google.firebase:firebase-ai")
    }

### Initialize the generative model

Start by instantiating a `GenerativeModel` and specifying the model name:


### Kotlin

```kotlin
val model = Firebase.ai(backend = GenerativeBackend.vertexAI())
    .generativeModel("gemini-2.5-flash")
```

### Java

```java
GenerativeModel firebaseAI = FirebaseAI.getInstance(GenerativeBackend.vertexAI())
        .generativeModel("gemini-2.5-flash");

GenerativeModelFutures model = GenerativeModelFutures.from(firebaseAI);
```

<br />

In the Firebase documentation, you can learn more about the [available
models](https://firebase.google.com/docs/vertex-ai/gemini-models) for use with the Gemini Developer API. You can also learn
about [configuring model parameters](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=android).

### Generate text

To generate a text response, call `generateContent()` with your prompt.


### Kotlin

```kotlin
suspend fun generateText(model: GenerativeModel) {
    // Note: generateContent() is a suspend function, which integrates well
    // with existing Kotlin code.
    val response = model.generateContent("Write a story about a magic backpack.")
    // ...
}
```

### Java

```java
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

Similar to the Gemini Developer API, you can also pass images, audio, video, and
files with your text prompt. For details, see [Interact with the Gemini Developer
API from your app](https://developer.android.com/ai/gemini/developer-api#interact-gemini).

To learn more about Firebase AI Logic SDK, read the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/get-started?platform=android).