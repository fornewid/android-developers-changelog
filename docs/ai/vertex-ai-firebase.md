---
title: https://developer.android.com/ai/vertex-ai-firebase
url: https://developer.android.com/ai/vertex-ai-firebase
source: md.txt
---

If you're new to the Gemini API, the [Gemini Developer API](https://developer.android.com/ai/gemini/developer-api) is the
recommended [API provider](https://developer.android.com/ai/gemini#api-providers) for Android Developers. But if you have specific
data [location requirements](https://firebase.google.com/docs/ai-logic/locations?api=vertex) or you are already embedded in the
Vertex AI or Google Cloud environment, you can use the Vertex AI Gemini API.

## Getting started

Before you interact with the Vertex AI Gemini API directly from your app, you
can experiment with prompts in [Vertex AI Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart).

### Set up a Firebase project and connect your app to Firebase

Once you're ready to call the API from your app, follow the instructions in
"Step 1" of the [Firebase AI Logic getting started guide](https://firebase.google.com/docs/ai-logic/get-started?api=vertex#set-up-firebase) to
set up Firebase and enable required APIs and services.

### Add the Gradle dependencies

Add the following Gradle dependencies to your app module:

### Kotlin

    dependencies {
      // ... other androidx dependencies

      // Import the BoM for the Firebase platform
      implementation(platform("com.google.firebase:firebase-bom:34.16.0"))

      // Add the dependencies for the Firebase AI Logic and App Check libraries
      // When using the BoM, you don't specify versions in Firebase library dependencies
      implementation("com.google.firebase:firebase-ai")
      implementation("com.google.firebase:firebase-appcheck-debug")
    }

### Java

    dependencies {
      // Import the BoM for the Firebase platform
      implementation(platform("com.google.firebase:34.16.0"))

      // Add the dependencies for the Firebase AI Logic and App Check libraries
      // When using the BoM, you don't specify versions in Firebase library dependencies
      implementation("com.google.firebase:firebase-ai")
      implementation("com.google.firebase:firebase-appcheck-debug")

      // Required for one-shot operations (to use `ListenableFuture` from Guava Android)
      implementation("com.google.guava:guava:31.0.1-android")

      // Required for streaming operations (to use `Publisher` from Reactive Streams)
      implementation("org.reactivestreams:reactive-streams:1.0.4")
    }

### Configure the App Check debug provider for local development

Starting early July 2026, as part of the guided setup workflow for AI Logic
in the Firebase console, Firebase App Check is automatically enforced to protect
the Gemini API. For local development, you need to configure the
App Check *debug provider* to bypass attestation while still maintaining the
enforcement of App Check.

1. In your debug build, configure App Check to use the debug provider
   factory:

   ### Kotlin

       Firebase.initialize(context = this)
       Firebase.appCheck.installAppCheckProviderFactory(
           DebugAppCheckProviderFactory.getInstance(),
       )

   ### Java

       FirebaseApp.initializeApp(/*context=*/ this);
       FirebaseAppCheck firebaseAppCheck = FirebaseAppCheck.getInstance();
       firebaseAppCheck.installAppCheckProviderFactory(
               DebugAppCheckProviderFactory.getInstance());

2. Obtain your debug token:

   1. Run your app in the emulator or on your test device.

   2. Look for the App Check debug token in your logs. For example:

          D DebugAppCheckProvider: Enter this debug secret into the allow list
          in the Firebase Console for your project: 123a4567-b89c-12d3-e456-789012345678

   3. Copy the token (for example, `123a4567-b89c-12d3-e456-789012345678`).

3. Register your debug token with App Check:

   1. In the Firebase console, go to the
      **Security** \> **App Check** \> [**Apps** tab](https://console.firebase.google.com/project/_/appcheck/apps/?useAutoProject=true).

   2. Find your app, click the overflow menu
      (), and then select
      **Manage debug tokens**.

   3. Follow the on-screen instructions to register your debug token.

For details about the debug provider (including how to get a new debug token),
check out the [official App Check docs](https://firebase.google.com/docs/app-check/android/debug-provider).

> [!CAUTION]
> **Here are some critical points about the
> App Check debug provider:**
>
> - **Keep your debug token and debug build private.** Don't commit your debug token to a public repository, and don't ship your debug token or debug build in production builds of your app.
> - **Register your app with a production attestation provider before
>   releasing to end users.** You'll need to [register your app with a production App Check attestation provider](https://firebase.google.com/docs/ai-logic/app-check) (for example, Play Integrity) so that your end-users can use your feature with App Check enforced.

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

In the Firebase documentation, you can learn more about the
[available Gemini models](https://firebase.google.com/docs/ai-logic/models). You can also learn about
[configuring model parameters](https://firebase.google.com/docs/ai-logic/model-parameters?api=vertex).

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
files with your text prompt. For details, see
[Interact with the Gemini Developer API from your app](https://developer.android.com/ai/gemini/developer-api#interact-gemini).

To learn more about Firebase AI Logic SDK, read the
[Firebase documentation](https://firebase.google.com/docs/ai-logic/get-started?api=vertex).