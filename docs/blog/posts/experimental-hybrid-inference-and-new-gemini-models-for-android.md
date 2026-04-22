---
title: https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android
url: https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Experimental hybrid inference and new Gemini models for Android

###### 3-min read

![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp) 17 Apr 2026 [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) [##### Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

###### Senior Developer Relations Engineer

If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates:

- Hybrid inference, a new API for Firebase AI Logic to leverage both on-device and Cloud inference,
- Support for new Gemini models including latest Nano Banana models for image generation.

Let's jump in!

### **Experiment with hybrid inference**

With the new [Firebase API for hybrid inference](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started?api=dev), we implemented a simple rule-based routing approach as an initial solution to let you use both on-device and cloud inference via a unified API. We are planning on providing more sophisticated routing capabilities in the future.

It allows your app to dynamically switch between Gemini Nano running locally on the device and cloud-hosted Gemini models. The on-device execution uses ML Kit's Prompt API. The cloud inference supports all the Gemini models from Firebase AI Logic in both Vertex AI and the Developer API.  

To use it, add the `firebase-ai-ondevice` dependencies to your app along with Firebase AI Logic:

```kotlin
dependencies {
 [...] 
 implementation("com.google.firebase:firebase-ai:17.10.1")
 implementation("com.google.firebase:firebase-ai-ondevice:16.0.0-beta01")
}
```

During initialization, you create a `GenerativeModel` instance and configure it with specific inference modes, such as `PREFER_ON_DEVICE` (falls back to cloud if Gemini Nano is not available on the device ) or `PREFER_IN_CLOUD` (falls back to on-device inference if offline):

```kotlin
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-3.1-flash-lite",
        onDeviceConfig = OnDeviceConfig(
           mode = InferenceMode.PREFER_ON_DEVICE
        )
    )

val response = model.generateContent(prompt)
```

The Firebase API for hybrid inference for Android is still experimental, and we encourage you to try it in your app, especially if you are already using Firebase AI Logic.   

Currently, on-device models are specialized for single-turn text generation based on text or single Bitmap image inputs. Review the [limitations](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started?api=dev#features-not-yet-available) for more details.  

We just published a [new sample in the AI Sample Catalog leveraging the Firebase API for hybrid](https://github.com/android/ai-samples/tree/main/samples/gemini-hybrid), it demonstrates how the Firebase API for hybrid inference can be used to generate a review based on a few selected topics and then translating it into various languages. Check out the code to see it in action!
![Hybrid_Inference-Inline-imagery.gif](https://developer.android.com/static/blog/assets/Hybrid_Inference_Inline_imagery_36760c3326_l3eiI.webp) The new hybrid inference sample in action

*The new hybrid inference sample in action*

### **Try our new models**

As part of the new Gemini models, we've released two models particularly helpful to Android developers and easy to integrate in your application via the Firebase AI Logic SDK.

**Nano Banana**   
Last year we released Nano Banana, a state-of-the-art image generation model. And a few weeks ago, we released a couple new Nana Banana models.

[Nano Banana Pro (Gemini 3 Pro Image)](https://deepmind.google/models/gemini-image/pro/) is designed for professional asset production and can render high-fidelity text, even in a specific font or simulating different types of handwriting.

[Nano Banana 2 (Gemini 3.1 Flash Image)](https://deepmind.google/models/gemini-image/flash/) is the high-efficiency counterpart to Nano Banana Pro. It's optimized for speed and high-volume use cases. It can be used for a broad range of use cases (infographics, virtual stickers, contextual illustrations, etc.). * *

The new Nano Banana models leverage real-world knowledge and deep reasoning capabilities to generate precise and detailed images.  

We updated our Magic Selfie sample (use image generation to change the background of your selfie!) to use Nano Banana 2. The background segmentation is now handled directly with the image generation model which makes the implementation easier and lets Nano Banana 2 improved image generation capabilities shine. See it in action [here](https://github.com/android/ai-samples/tree/main/samples/magic-selfie).
![magic_selfie.png](https://developer.android.com/static/blog/assets/magic_selfie_e5893f79e5_2ewAaS.webp) The updated Magic Selfie sample use Nanobana 2 to update a selfie background

You can use it via Firebase AI Logic SDK. Read more about it in the [Android documentation](https://developer.android.com/ai/gemini/developer-api#generate-images).

### **Gemini 3.1 Flash-Lite**

We also released [Gemini 3.1 Flash-Lite](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/), a new version of the Gemini Flash-Lite family. The Gemini Flash-Lite models have been particularly favored by Android developers for its good quality/latency ratio and low inference cost. It's been used by Android developers for various use-cases such as in-app messaging translation or generating a recipe from a picture of a dish.   

Gemini 3.1 Flash-Lite, currently in preview, will enable more advanced use cases with latency comparable to Gemini 2.5 Flash-Lite.  

To learn more about this model, review the [Firebase documentation](https://firebase.google.com/docs/ai-logic/models).

### **Conclusion**

It's a great time to explore the new Hybrid sample in our catalog to see these capabilities in action and understand the benefits of routing between on-device and cloud inference. We also encourage you to check out our documentation to test the new Gemini models.

###### Written by:

-

  ## [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/thomas-ezan) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Dec 2025 17 Dec 2025 ![](https://developer.android.com/static/blog/assets/gemin3flash_d6f3bd27b1_O0qYl.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Build smarter apps with Gemini 3 Flash](https://developer.android.com/blog/posts/build-smarter-apps-with-gemini-3-flash)

  [arrow_forward](https://developer.android.com/blog/posts/build-smarter-apps-with-gemini-3-flash) Today, we're expanding the Gemini 3 model family with the release of Gemini 3 Flash, frontier intelligence built for speed at a fraction of the cost.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  2 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Mozart_Louis_622373dab1_1RaA8T.webp)](https://developer.android.com/blog/authors/mozart-louis) 13 Oct 2025 13 Oct 2025 ![](https://developer.android.com/static/blog/assets/Android_Blog_banners_dd5c7be5f2_ZsFAUM.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boost user engagement with AI Image Generation](https://developer.android.com/blog/posts/boost-user-engagement-with-ai-image-generation)

  [arrow_forward](https://developer.android.com/blog/posts/boost-user-engagement-with-ai-image-generation) Adding custom images to your app can significantly improve and personalize user experience and boost user engagement.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Mozart Louis](https://developer.android.com/blog/authors/mozart-louis) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)](https://developer.android.com/blog/authors/matt-dyor) 21 Apr 2026 21 Apr 2026 ![](https://developer.android.com/static/blog/assets/as_Panda3_385cde5eac_Z1E8IhJ.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4)

  [arrow_forward](https://developer.android.com/blog/posts/level-up-your-development-with-planning-mode-and-next-edit-prediction-in-android-studio-panda-4) Android Studio Panda 4 is now stable and ready for you to use in production. This release brings Planning Mode, Next Edit Prediction, and more, making it easier than ever to build high-quality Android apps.

  ###### [Matt Dyor](https://developer.android.com/blog/authors/matt-dyor) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)