---
title: https://developer.android.com/ai/gemini/developer-api
url: https://developer.android.com/ai/gemini/developer-api
source: md.txt
---

The *Gemini Developer API* gives you access to Google's Gemini models, letting
you build cutting-edge generative AI features into your Android apps---including
conversational chat, image generation (with Nano Banana), and text generation
based on text, image, audio, and video input.

To access the Gemini Pro and Flash models, you can use the Gemini Developer API
with Firebase AI Logic. It lets you get started without requiring a credit card,
and provides a generous free tier. Once you validate your integration with a
small user base, you can scale by switching to the paid tier.
![Illustration of an Android App that contains a Firebase Android
SDK. An arrow points from the SDK to Firebase within a Cloud environment. From
Firebase, another arrow points to Gemini Developer API, which is connected to
Gemini Pro & Flash, also within the Cloud.](https://developer.android.com/static/ai/assets/images/firebase-ai-logic-gemini-dev.svg) **Figure 1.** Firebase AI Logic integration architecture to access the Gemini Developer API.

> [!NOTE]
> **Note:** If you have strict [data location](https://cloud.google.com/compute/docs/regions-zones) requirements or are already using Vertex AI, you can look at the support of Vertex AI Gemini API as an API provider for the [Firebase AI Logic](https://firebase.google.com/docs/vertex-ai/get-started?platform=android) SDK.

### Getting started

Before you interact with the Gemini API directly from your app, you'll need to
do a few things first, including getting familiar with prompting as well as
setting up Firebase and your app to use the SDK.

### Experiment with prompts

Experimenting with prompts can help you find the best phrasing, content, and
format for your Android app. [Google AI Studio](https://aistudio.google.com/) is an Integrated
Development Environment (IDE) that you can use to prototype and design prompts
for your app's use cases.

Creating effective prompts for your use case involves extensive experimentation,
which is a critical part of the process. You can learn more about prompting in
the [Firebase documentation](https://firebase.google.com/docs/vertex-ai/prompt-design).

Once you are happy with your prompt, click the **\<\>** button to get code
snippets that you can add to your code.

### Set up a Firebase project and connect your app to Firebase

Once you're ready to call the API from your app, follow the instructions in
"Step 1" of the [Firebase AI Logic getting started guide](https://firebase.google.com/docs/vertex-ai/get-started?platform=android) to set up Firebase
and the SDK in your app.

### Add the Gradle dependency

Add the following Gradle dependency to your app module:

### Kotlin

```kotlin
dependencies {
  // ... other androidx dependencies

  // Import the BoM for the Firebase platform
  implementation(platform("com.google.firebase:firebase-bom:34.9.0"))

  // Add the dependency for the Firebase AI Logic library When using the BoM,
  // you don't specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai")
}
      
```

### Java

```java
dependencies {
  // Import the BoM for the Firebase platform
  implementation(platform("com.google.firebase:34.9.0"))

  // Add the dependency for the Firebase AI Logic library When using the BoM,
  // you don't specify versions in Firebase library dependencies
  implementation("com.google.firebase:firebase-ai")

  // Required for one-shot operations (to use `ListenableFuture` from Guava
  // Android)
  implementation("com.google.guava:guava:31.0.1-android")

  // Required for streaming operations (to use `Publisher` from Reactive
  // Streams)
  implementation("org.reactivestreams:reactive-streams:1.0.4")
}
      
```

### Initialize the generative model

> [!NOTE]
> **Note:** Gemini 3 Flash and Gemini 3.1 Pro are now available in preview. [Learn more about the models supported by Firebase AI Logic](https://firebase.google.com/docs/ai-logic/models).

Start by instantiating a `GenerativeModel` and specifying the model name:


### Kotlin

```kotlin
// Start by instantiating a GenerativeModel and specifying the model name:
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel("gemini-2.5-flash")
```

### Java

```java
GenerativeModel firebaseAI = FirebaseAI.getInstance(GenerativeBackend.googleAI())
        .generativeModel("gemini-2.5-flash");

GenerativeModelFutures model = GenerativeModelFutures.from(firebaseAI);
```

<br />

Learn more about the [available models](https://firebase.google.com/docs/vertex-ai/gemini-models) for use with the Gemini
Developer API. You can also learn more about [configuring model
parameters](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=android).

## Interact with the Gemini Developer API from your app

Now that you've set up Firebase and your app to use the SDK, you're ready to
interact with the Gemini Developer API from your app.

### Generate text

To generate a text response, call `generateContent()` with your prompt.


### Kotlin

```kotlin
scope.launch {
    val response = model.generateContent("Write a story about a magic backpack.")
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
    }

    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

### Generate text from images and other media

You can also generate text from a prompt that includes text plus images or other
media. When you call `generateContent()`, you can pass the media as inline data.

For example, to use a bitmap, use the `image` content type:


### Kotlin

```kotlin
scope.launch {
    val response = model.generateContent(
        content {
            image(bitmap)
            text("what is the object in the picture?")
        }
    )
}
```

### Java

```java
Content content = new Content.Builder()
        .addImage(bitmap)
        .addText("what is the object in the picture?")
        .build();

ListenableFuture<GenerateContentResponse> response = model.generateContent(content);
Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        String resultText = result.getText();
    }

    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

To pass an audio file, use the `inlineData` content type:


### Kotlin

```kotlin
scope.launch {
    val contentResolver = applicationContext.contentResolver
    contentResolver.openInputStream(audioUri).use { stream ->
        stream?.let {
            val bytes = it.readBytes()

            val prompt = content {
                inlineData(bytes, "audio/mpeg") // Specify the appropriate audio MIME type
                text("Transcribe this audio recording.")
            }

            val response = model.generateContent(prompt)
        }
    }
}
```

### Java

```java
ContentResolver resolver = applicationContext.getContentResolver();

try (InputStream stream = resolver.openInputStream(audioUri)) {
    File audioFile = new File(new URI(audioUri.toString()));
    int audioSize = (int) audioFile.length();
    byte[] audioBytes = new byte[audioSize];
    if (stream != null) {
        stream.read(audioBytes, 0, audioBytes.length);
        stream.close();

        // Provide a prompt that includes audio specified earlier and text
        Content prompt = new Content.Builder()
                .addInlineData(audioBytes, "audio/mpeg")  // Specify the appropriate audio MIME type
                .addText("Transcribe what's said in this audio recording.")
                .build();

        // To generate text output, call `generateContent` with the prompt
        ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
        Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
            @Override
            public void onSuccess(GenerateContentResponse result) {
                String text = result.getText();
                Log.d(TAG, (text == null) ? "" : text);
            }
            @Override
            public void onFailure(Throwable t) {
                Log.e(TAG, "Failed to generate a response", t);
            }
        }, executor);
    } else {
        Log.e(TAG, "Error getting input stream for file.");
        // Handle the error appropriately
    }
} catch (IOException e) {
    Log.e(TAG, "Failed to read the audio file", e);
} catch (URISyntaxException e) {
    Log.e(TAG, "Invalid audio file", e);
}
```

<br />

And to provide a video file, continue using the `inlineData` content type:


### Kotlin

```kotlin
scope.launch {
    val contentResolver = applicationContext.contentResolver
    contentResolver.openInputStream(videoUri).use { stream ->
        stream?.let {
            val bytes = it.readBytes()

            val prompt = content {
                inlineData(bytes, "video/mp4") // Specify the appropriate video MIME type
                text("Describe the content of this video")
            }

            val response = model.generateContent(prompt)
        }
    }
}
```

### Java

```java
ContentResolver resolver = applicationContext.getContentResolver();

try (InputStream stream = resolver.openInputStream(videoUri)) {
    File videoFile = new File(new URI(videoUri.toString()));
    int videoSize = (int) videoFile.length();
    byte[] videoBytes = new byte[videoSize];
    if (stream != null) {
        stream.read(videoBytes, 0, videoBytes.length);
        stream.close();

        // Provide a prompt that includes video specified earlier and text
        Content prompt = new Content.Builder()
                .addInlineData(videoBytes, "video/mp4")
                .addText("Describe the content of this video")
                .build();

        // To generate text output, call generateContent with the prompt
        ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
        Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
            @Override
            public void onSuccess(GenerateContentResponse result) {
                String resultText = result.getText();
                System.out.println(resultText);
            }

            @Override
            public void onFailure(Throwable t) {
                t.printStackTrace();
            }
        }, executor);
    }
} catch (IOException e) {
    e.printStackTrace();
} catch (URISyntaxException e) {
    e.printStackTrace();
}
```

<br />

Similarly, you can also pass PDF (`application/pdf`) and plain text
(`text/plain`) documents by passing their respective MIME Type as a parameter.

### Multi-turn chat

You can also support multi-turn conversations. Initialize a chat with the
`startChat()` function. You can optionally provide the model with a message
history. Then call the `sendMessage()` function to send chat messages.


### Kotlin

```kotlin
val chat = model.startChat(
    history = listOf(
        content(role = "user") { text("Hello, I have 2 dogs in my house.") },
        content(role = "model") { text("Great to meet you. What would you like to know?") }
    )
)

scope.launch {
    val response = chat.sendMessage("How many paws are in my house?")
}
```

### Java

```java
Content.Builder userContentBuilder = new Content.Builder();
userContentBuilder.setRole("user");
userContentBuilder.addText("Hello, I have 2 dogs in my house.");
Content userContent = userContentBuilder.build();

Content.Builder modelContentBuilder = new Content.Builder();
modelContentBuilder.setRole("model");
modelContentBuilder.addText("Great to meet you. What would you like to know?");
Content modelContent = modelContentBuilder.build();

List<Content> history = Arrays.asList(userContent, modelContent);

// Initialize the chat
ChatFutures chat = model.startChat(history);

// Create a new user message
Content.Builder messageBuilder = new Content.Builder();
messageBuilder.setRole("user");
messageBuilder.addText("How many paws are in my house?");

Content message = messageBuilder.build();

// Send the message
ListenableFuture<GenerateContentResponse> response = chat.sendMessage(message);
Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        String resultText = result.getText();
        System.out.println(resultText);
    }

    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

### Generate images on Android with Nano Banana

> [!NOTE]
> **Note:** Gemini 3 Pro Image (Nano Banana Pro) is now available in preview as `gemini-3-pro-image-preview`. [Learn more about the capabilities of Gemini 3 Pro Image](https://deepmind.google/models/gemini-image/pro/).

The Gemini 2.5 Flash Image model (a.k.a Nano Banana) can generate and edit
images leveraging world knowledge and reasoning. It generates contextually
relevant images, seamlessly blending or interleaving text and image outputs. It
can also generate accurate visuals with long text sequences and supports
conversational image editing while maintaining context.

As an alternative to Gemini, you can use Imagen models, especially for
high-quality image generation that requires photorealism, artistic detail, or
specific styles. However, for the majority of client-side use cases for Android
apps, Gemini will be more than sufficient.

This guide describes how to use the Gemini 2.5 Flash Image model (Nano Banana)
using the Firebase AI Logic SDK for Android. For more details on generating
images with Gemini, see the [Generate images with Gemini on
Firebase](https://firebase.google.com/docs/ai-logic/generate-images-gemini?api=dev) documentation. If you're interested in using [Imagen
models](https://developer.android.com/ai/imagen), check out the documentation.

> [!NOTE]
> **Note:** Using Gemini models for image generation using the Firebase AI Logic SDK is in Preview. This means the feature isn't subject to any SLA or deprecation policy and could change in backward-incompatible ways.

![Google AI Studio interface showing a text input field
with the prompt 'A hyper realistic picture of a t-rex with a blue bag pack
roaming a pre-historic forest.' and a generated image of a t-rex in a forest
with a blue backpack.](https://developer.android.com/static/ai/assets/images/t-rex-nano-banana.png) **Figure 2.** Use Google AI Studio to refine your Nano Banana image generation prompts for Android

#### Initialize the generative model

Instantiate a `GenerativeModel` and specify the model name
`gemini-2.5-flash-image-preview`. Verify that you configure `responseModalities`
to include both `TEXT` and `IMAGE`.


### Kotlin

```kotlin
val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
    modelName = "gemini-2.5-flash-image-preview",
    // Configure the model to respond with text and images (required)
    generationConfig = generationConfig {
        responseModalities = listOf(
            ResponseModality.TEXT,
            ResponseModality.IMAGE
        )
    }
)
```

### Java

```java
GenerativeModel ai = FirebaseAI.getInstance(GenerativeBackend.googleAI()).generativeModel(
        "gemini-2.5-flash-image-preview",
        // Configure the model to respond with text and images (required)
        new GenerationConfig.Builder()
                .setResponseModalities(Arrays.asList(ResponseModality.TEXT, ResponseModality.IMAGE))
                .build()
);
GenerativeModelFutures model = GenerativeModelFutures.from(ai);
```

<br />

#### Generate images (text-only input)

You can instruct a Gemini model to generate images by providing a text-only
prompt:


### Kotlin

```kotlin
scope.launch {
    // Provide a text prompt instructing the model to generate an image
    val prompt =
        "A hyper realistic picture of a t-rex with a blue bag pack roaming a pre-historic forest."
    // To generate image output, call `generateContent` with the text input
    val generatedImageAsBitmap: Bitmap? = model.generateContent(prompt)
        .candidates.first().content.parts.filterIsInstance<ImagePart>()
        .firstOrNull()?.image
}
```

### Java

```java
// Provide a text prompt instructing the model to generate an image
Content prompt = new Content.Builder()
        .addText("Generate an image of the Eiffel Tower with fireworks in the background.")
        .build();
// To generate an image, call `generateContent` with the text input
ListenableFuture<GenerateContentResponse> response = model.generateContent(prompt);
Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        // iterate over all the parts in the first candidate in the result object
        for (Part part : result.getCandidates().get(0).getContent().getParts()) {
            if (part instanceof ImagePart) {
                ImagePart imagePart = (ImagePart) part;
                // The returned image as a bitmap
                Bitmap generatedImageAsBitmap = imagePart.getImage();
                break;
            }
        }
    }
    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

#### Edit images (text and image input)

You can ask a Gemini model to edit existing images by providing both text and
one or more images in your prompt:


### Kotlin

```kotlin
scope.launch {
    // Provide a text prompt instructing the model to edit the image
    val prompt = content {
        image(bitmap)
        text("Edit this image to make it look like a cartoon")
    }
    // To edit the image, call `generateContent` with the prompt (image and text input)
    val generatedImageAsBitmap: Bitmap? = model.generateContent(prompt)
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image
    // Handle the generated text and image
}
```

### Java

```java
// Provide an image for the model to edit
Bitmap bitmap = BitmapFactory.decodeResource(resources, R.drawable.scones);
// Provide a text prompt instructing the model to edit the image
Content promptcontent = new Content.Builder()
        .addImage(bitmap)
        .addText("Edit this image to make it look like a cartoon")
        .build();
// To edit the image, call `generateContent` with the prompt (image and text input)
ListenableFuture<GenerateContentResponse> response = model.generateContent(promptcontent);
Futures.addCallback(response, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        // iterate over all the parts in the first candidate in the result object
        for (Part part : result.getCandidates().get(0).getContent().getParts()) {
            if (part instanceof ImagePart) {
                ImagePart imagePart = (ImagePart) part;
                Bitmap generatedImageAsBitmap = imagePart.getImage();
                break;
            }
        }
    }
    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

#### Iterate and edit images through multi-turn chat

For a conversational approach to image editing, you can use multi-turn chat.
This allows for follow-up requests to refine edits without needing to re-send
the original image.

First, initialize a chat with `startChat()`, optionally providing a message
history. Then, use `sendMessage()` for subsequent messages:


### Kotlin

```kotlin
scope.launch {
    // Create the initial prompt instructing the model to edit the image
    val prompt = content {
        image(bitmap)
        text("Edit this image to make it look like a cartoon")
    }
    // Initialize the chat
    val chat = model.startChat()
    // To generate an initial response, send a user message with the image and text prompt
    var response = chat.sendMessage(prompt)
    // Inspect the returned image
    var generatedImageAsBitmap: Bitmap? = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image
    // Follow up requests do not need to specify the image again
    response = chat.sendMessage("But make it old-school line drawing style")
    generatedImageAsBitmap = response
        .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image
}
```

### Java

```java
// Provide an image for the model to edit
Bitmap bitmap = BitmapFactory.decodeResource(resources, R.drawable.scones);
// Initialize the chat
ChatFutures chat = model.startChat();
// Create the initial prompt instructing the model to edit the image
Content prompt = new Content.Builder()
        .setRole("user")
        .addImage(bitmap)
        .addText("Edit this image to make it look like a cartoon")
        .build();
// To generate an initial response, send a user message with the image and text prompt
ListenableFuture<GenerateContentResponse> response = chat.sendMessage(prompt);
// Extract the image from the initial response
ListenableFuture<Bitmap> initialRequest = Futures.transform(response,
        result -> {
            for (Part part : result.getCandidates().get(0).getContent().getParts()) {
                if (part instanceof ImagePart) {
                    ImagePart imagePart = (ImagePart) part;
                    return imagePart.getImage();
                }
            }
            return null;
        }, executor);
// Follow up requests do not need to specify the image again
ListenableFuture<GenerateContentResponse> modelResponseFuture = Futures.transformAsync(
        initialRequest,
        generatedImage -> {
            Content followUpPrompt = new Content.Builder()
                    .addText("But make it old-school line drawing style")
                    .build();
            return chat.sendMessage(followUpPrompt);
        }, executor);
// Add a final callback to check the reworked image
Futures.addCallback(modelResponseFuture, new FutureCallback<GenerateContentResponse>() {
    @Override
    public void onSuccess(GenerateContentResponse result) {
        for (Part part : result.getCandidates().get(0).getContent().getParts()) {
            if (part instanceof ImagePart) {
                ImagePart imagePart = (ImagePart) part;
                Bitmap generatedImageAsBitmap = imagePart.getImage();
                break;
            }
        }
    }
    @Override
    public void onFailure(Throwable t) {
        t.printStackTrace();
    }
}, executor);
```

<br />

#### Considerations and limitations

Note the following considerations and limitations:

- **Output Format**: Images are generated as PNGs with a maximum dimension of 1024 px.
- **Input Types**: The model doesn't support audio or video inputs for image generation.
- **Language Support** : For best performance, use the following languages: English (`en`), Mexican Spanish (`es-mx`), Japanese (`ja-jp`), Simplified Chinese (`zh-cn`), and Hindi (`hi-in`).
- **Generation Issues** :
  - Image generation may not always trigger, sometimes resulting in text-only output. **Try asking for image outputs explicitly** (for example, "generate an image", "provide images as you go along", "update the image").
  - The model may stop generating partway through. **Try again or try a
    different prompt**.
  - The model may generate text as an image. **Try asking for text outputs
    explicitly** (for example, "generate narrative text along with illustrations").

See the [Firebase documentation](https://firebase.google.com/docs/ai-logic/generate-images-gemini?api=dev) for more details.

## Next steps

After setting up your app, consider the following next steps:

- Review the Android Quickstart Firebase [sample app](https://github.com/firebase/quickstart-android/tree/master/vertexai) and the [Android AI Sample Catalog](https://github.com/android/ai-samples) on GitHub.
- [Prepare your app for production](https://firebase.google.com/docs/vertex-ai/production-checklist), including [setting up
  Firebase App Check](https://firebase.google.com/docs/vertex-ai/app-check) to protect the Gemini API from abuse by unauthorized clients.
- Learn more about Firebase AI Logic in the [Firebase
  documentation](https://firebase.google.com/docs/vertex-ai/).