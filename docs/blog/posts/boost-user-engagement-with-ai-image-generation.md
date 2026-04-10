---
title: Boost user engagement with AI Image Generation  |  Android Developers' Blog
url: https://developer.android.com/blog/posts/boost-user-engagement-with-ai-image-generation
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Android Developers' Blog](https://developer.android.com/)
* [Blog](https://developer.android.com/blog)

Stay organized with collections

Save and categorize content based on your preferences.



#### [Product News](/blog/categories/product-news)

# Boost user engagement with AI Image Generation

###### 5-min read

![](/static/blog/assets/Android_Blog_banners_dd5c7be5f2_ZsFAUM.webp)

13

Oct
2025

[![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)[![](/static/blog/assets/Mozart_Louis_622373dab1_1RaA8T.webp)](/blog/authors/mozart-louis)

##### [Thomas Ezan](/blog/authors/thomas-ezan) & [Mozart Louis](/blog/authors/mozart-louis)

Adding custom images to your app can significantly improve and personalize user experience and boost user engagement. This post explores two new capabilities for image generation with Firebase AI Logic: the specialized Imagen editing features, currently in preview, and the general availability of Gemini 2.5 Flash Image (a.k.a "Nano Banana"), designed for contextual or conversational image generation.

**Boost user engagement with images generated via Firebase AI Logic**

Image generation models can be used to create custom user profile avatars or to integrate personalized visual assets directly into key screen flows.

For example, Imagen offers new editing features (in developer preview). You can now draw a mask and utilize inpainting to generate pixels within the masked area. Additionally, outpainting is available to generate pixels outside the mask.

![Imagen inpainting.png](/static/blog/assets/Imagen_inpainting_d99f009550_Z15Eg9B.webp)

*Imagen supports inpainting, letting generate only a part of an image.*

Alternatively, Gemini 2.5 Flash Image (a.k.a Nano Banana), can use extended world knowledge and the reasoning capabilities of the Gemini models to generate contextually relevant images, which is ideal for creating dynamic illustrations that align with a user's current in-app experience.

![In-context nano banana illustration.png](/static/blog/assets/In_context_nano_banana_illustration_af21b7247f_dveip.webp)

*Use Gemini 2.5 Flash Image to create dynamic illustrations contextually relevant to your app.*

Finally, the ability to conversationally and iteratively edit images allow users to edit a photo using natural language.

![photo edit natural language.png](/static/blog/assets/photo_edit_natural_language_52f7a73044_ZFdaDz.webp)

*Use Gemini 2.5 Flash Image to edit a picture using natural language.*

When starting to integrate AI to your application, it is important to learn about [AI safety](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen). It is particularly key to assess your application's security risks, consider adjustments to mitigate safety risks, perform safety testing appropriate to your use case and solicit user feedback and monitor content.

**Imagen or Gemini: The choice is yours**

The difference between [Gemini 2.5 Flash Image](https://ai.google.dev/gemini-api/docs/image-generation) ("Nano Banana") and [Imagen](https://ai.google.dev/gemini-api/docs/imagen) lies in their primary focus and advanced capabilities. Gemini 2.5 Flash Image, as an image model within the larger Gemini family, excels in conversational image editing, maintaining context and subject consistency across multiple iterations, and leveraging "world knowledge and reasoning" to create contextually relevant visuals or embed accurate visuals within long text sequences.

Imagen is Google’s specialized image generation model, designed for greater creative control, specializing in highly photorealistic outputs, artistic detail, specific styles, and providing explicit controls for specifying the aspect ratio or format of the generated image.

|  |  |
| --- | --- |
| **Gemini 2.5 Flash Images** **(Nano Banana 🍌)** | **Imagen** |
| 🌎 world knowledge and reasoning for more contextually relevant images  💬 edit images conversationally while maintaining context  📖 embed accurate visuals within long text sequences | 📐 specify the aspect ratio or format of generated images    🖌️Support of mask-based editing for in-painting and out-painting.    🎚️ greater control over details of the generated image (quality, artistic detail and specific styles) |

Let’s see how to use them in your app.

**Inpainting with Imagen**

A few months ago, we released new editing features for Imagen. Although Imagen is now ready for production for image generation, editing features are still in *developer preview*.

Imagen editing features include *inpainting* and *outpainting*, mask-based image editing features. This new capability allows users to modify specific areas of an image without regenerating the entire picture. This means you can preserve the best parts of your image and only alter what you wish to change.

![Imagen inpainting dog.png](/static/blog/assets/Imagen_inpainting_dog_f415940aad_RQtQD.webp)

*Use Imagen editing features to make precise targeted changes in an image and guaranteeing the rest of the image integrity*

These changes are made while maintaining the core elements and overall integrity of the original image and modifying only the area in the mask.

To implement inpainting with Imagen, first initialize `imagen-3.0-capability-001` a specific Imagen model supporting editing features:

```
  // Copyright 2025 Google LLC.
// SPDX-License-Identifier: Apache-2.0
val editingModel =
        Firebase.ai(backend = GenerativeBackend.vertexAI()).imagenModel(
            "imagen-3.0-capability-001",
            generationConfig = ImagenGenerationConfig(
                numberOfImages = 1,
                aspectRatio = ImagenAspectRatio.SQUARE_1x1,
                imageFormat = ImagenImageFormat.jpeg(compressionQuality = 75),
            ),
        )
```

From there, define the inpainting function:

```
  // Copyright 2025 Google LLC.
// SPDX-License-Identifier: Apache-2.0

val prompt = "remove the pancakes and make it an omelet instead"

suspend fun inpaintImageWithMask(sourceImage: Bitmap, maskImage: Bitmap, prompt: String, editSteps: Int = 50): Bitmap {
        val imageResponse = editingModel.editImage(
            referenceImages = listOf(
                ImagenRawImage(sourceImage.toImagenInlineImage()),
                ImagenRawMask(maskImage.toImagenInlineImage()),
            ),
            prompt = prompt,
            config = ImagenEditingConfig(
                editMode = ImagenEditMode.INPAINT_INSERTION,
                editSteps = editSteps,
            ),
        )
        return imageResponse.images.first().asBitmap()
    }
```

You provide both a sourceImage, a maskImage and a prompt for the edit and the number of edit steps to be performed.

You can see it in action in the [Imagen Editing Sample](https://github.com/android/ai-samples/tree/main/samples/imagen-editing) in the Android AI Sample catalog!

And Imagen also supports *outpainting* that enables you to let the model generate the pixels outside of a mask. You can also use Imagen’s Image customization capabilities to change the style of a picture or update a subject in a picture. Read more about it in the [Android developer documentation](/ai/imagen#editing).

**Conversational image generation with Gemini 2.5 Flash Image**

One way to edit images with Gemini 2.5 Flash Image is to use the model’s multi-turn chat capabilities.

First, initialize the model:

```
  // Copyright 2025 Google LLC.
// SPDX-License-Identifier: Apache-2.0

val model = Firebase.ai(backend = GenerativeBackend.googleAI()).generativeModel(
    modelName = "gemini-2.5-flash-image",
    // Configure the model to respond with text and images (required)
    generationConfig = generationConfig {
        responseModalities = listOf(ResponseModality.TEXT,
        ResponseModality.IMAGE)
    }
)
```

To achieve a similar outcome to the mask-based Imagen method described above, we can utilize the `chat` API to initiate a conversation with Gemini 2.5 Flash Image.

```
  // Copyright 2025 Google LLC.
// SPDX-License-Identifier: Apache-2.0

// Initialize the chat
val chat = model.startChat()


// Load a bitmap
val source = ImageDecoder.createSource(context.contentResolver, uri)
val bitmap = ImageDecoder.decodeBitmap(source)


// Create the initial prompt instructing the model to edit the image
val prompt = content {
    image(bitmap)
    text("remove the pancakes and add an omelet")
}

// To generate an initial response, send a user message with the image and text prompt
var response = chat.sendMessage(prompt)

// Inspect the returned image
var generatedImageAsBitmap = response
    .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image

// Follow up requests do not need to specify the image again
response = chat.sendMessage("Now, center the omelet in the pan")
generatedImageAsBitmap = response
    .candidates.first().content.parts.filterIsInstance<ImagePart>().firstOrNull()?.image
```

You can see it in action in the [Gemini Image Chat sample](https://github.com/android/ai-samples/tree/main/samples/gemini-image-chat) in the Android AI Sample catalog and read more about it in the [Android documentation](/ai/gemini/developer-api#generate-images).

**Conclusion**

Both Imagen and Gemini 2.5 Flash Image offer powerful capabilities, allowing you to select the ideal image generation model to personalize your app and boost user engagement, depending on your specific use case.

###### Written by:

* ## [Thomas Ezan](/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/thomas-ezan)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

  ![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)
* ## [Mozart Louis](/blog/authors/mozart-louis)

  ###### Developer Relations Engineer

  [read\_more
  View profile](/blog/authors/mozart-louis)

  ![](/static/blog/assets/Mozart_Louis_622373dab1_1RaA8T.webp)

  ![](/static/blog/assets/Mozart_Louis_622373dab1_1RaA8T.webp)

## Continue reading

* [![](/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](/blog/authors/thomas-ezan)

  17

  Dec
  2025

  17

  Dec
  2025

  ![](/static/blog/assets/gemin3flash_d6f3bd27b1_O0qYl.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Build smarter apps with Gemini 3 Flash](/blog/posts/build-smarter-apps-with-gemini-3-flash)

  [arrow\_forward](/blog/posts/build-smarter-apps-with-gemini-3-flash)

  Today, we're expanding the Gemini 3 model family with the release of Gemini 3 Flash, frontier intelligence built for speed at a fraction of the cost.

  ###### [Thomas Ezan](/blog/authors/thomas-ezan) • 2 min read
* [![](/static/blog/assets/matthew_warner_67a99317e4_Z2c1VNu.webp)](/blog/authors/matthew-warner)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/android_studio_gemma4_73370772af_2lUopR.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Android Studio supports Gemma 4: our most capable local model for agentic coding](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  [arrow\_forward](/blog/posts/android-studio-supports-gemma-4-our-most-capable-local-model-for-agentic-coding)

  Every developer's AI workflow and needs are unique, and it's important to be able to choose how AI helps your development. In January, we introduced the ability to choose any local or remote AI model to power AI functionality in Android Studio

  ###### [Matthew Warner](/blog/authors/matthew-warner) • 2 min read

  + [#Android Studio](/blog/topics/android-studio)
* [![](/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](/blog/authors/matt-dyor)

  02

  Apr
  2026

  02

  Apr
  2026

  ![](/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](/blog/categories/product-news)

  ## [Increase Guidance and Control over Agent Mode with Android Studio Panda 3](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  [arrow\_forward](/blog/posts/increase-guidance-and-control-over-agent-mode-with-android-studio-panda-3)

  Android Studio Panda 3 is now stable and ready for you to use in production. This release gives you even more control and customization over your AI-powered workflows, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](/blog/authors/matt-dyor) • 3 min read

  + [#Android Studio](/blog/topics/android-studio)

# Stay in the loop

Get the latest Android development insights delivered to your inbox
weekly.

[mail
Subscribe](/subscribe)

![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)