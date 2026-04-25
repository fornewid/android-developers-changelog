---
title: https://developer.android.com/blog/posts/build-smarter-apps-with-gemini-3-flash
url: https://developer.android.com/blog/posts/build-smarter-apps-with-gemini-3-flash
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# Build smarter apps with Gemini 3 Flash

###### 2-min read

![](https://developer.android.com/static/blog/assets/gemin3flash_d6f3bd27b1_O0qYl.webp) 17 Dec 2025 [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) [##### Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

###### Senior Developer Relations Engineer

Today, we're expanding the Gemini 3 model family with the [release of Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash), frontier intelligence built for speed at a fraction of the cost. You can start building with it immediately, as we're officially launching **Gemini 3 Flash** on [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/get-started?platform=android&api=dev). Available globally, you [can securely access the Gemini 3 Flash preview model](https://blog.google/technology/developers/build-with-gemini-3-flash/) directly from your app via the Gemini Developer API or the Vertex AI Gemini API using Firebase AI Logic client SDKs. Gemini 3 Flash's strong performance in reasoning, tool use, and multimodal capabilities is ideal for developers looking to do more complex video analysis, data extraction and visual Q\&A.

## Gemini 3 optimized for low-latency

Gemini 3 is our most intelligent model family to date. With the launch of Gemini 3 Flash, we are making that intelligence more accessible for low-latency and cost-effective use cases. While Gemini 3 Pro is designed for complex reasoning, Gemini 3 Flash is engineered to be significantly faster and more cost-effective for your production apps.

## Seamless integration with Firebase AI Logic

Just like the Pro model, Gemini 3 Flash is available in preview directly through the [Firebase AI Logic SDK](https://firebase.google.com/docs/ai-logic/get-started?platform=android&api=dev). This means you can integrate it into your Android app without needing to do any complex server side setup.

Here is how to add it to your Kotlin code:

```kotlin
val model = Firebase.ai(backend = GenerativeBackend.googleAI())

    .generativeModel(modelName = "gemini-3-flash-preview")
```

## Scale with Confidence

In addition, Firebase enables you to keep your growth secure and manageable with:

## AI Monitoring

The [Firebase AI monitoring](https://firebase.google.com/docs/ai-logic/monitoring#ai-monitoring-in-console) dashboard gives you visibility into latency, success rates, and costs, allowing you to slice data by model name to see exactly how the model performs.
![image.png](https://developer.android.com/static/blog/assets/image_161aa78890_Lip5R.webp)

## Server Prompt Templates

You can use [server prompt templates](https://firebase.blog/posts/2025/12/server-prompt-templates-ai-logic) to store your prompt and schema securely on Firebase servers instead of hardcoding them in your app binary. This capability ensures your sensitive prompts remain secure, prevents unauthorized prompt extraction, and allows for faster iteration without requiring app updates.

```kotlin
---

model: 'gemini-3-flash-preview'

input:

  schema:

    topic:

      type: 'string'

      minLength: 2

      maxLength: 40

    length:

      type: 'number'

      minimum: 1

      maximum: 200

    language:

      type: 'string'


---


{{role "system"}}

You're a storyteller that tells nice and joyful stories with happy endings.


{{role "user"}}

Create a story about {{topic}} with the length of {{length}} words in the {{language}} language.
```

*Server prompt template defined using the Firebase console *

```kotlin
val generativeModel = Firebase.ai.templateGenerativeModel()
val response = generativeModel.generateContent("storyteller-v10",
    mapOf(
        "topic" to topic,
        "length" to length,
        "language" to language
    )
)
_output.value = response.text
```

*Code snippet to access the server prompt template*

## Gemini 3 Flash for AI development assistance in Android Studio

Gemini 3 Flash is also available for [AI assistance in Android Studio](http://d.android.com/gemini-in-android). While [Gemini 3 Pro Preview is our best model for coding and agentic experiences](https://android-developers.googleblog.com/2025/11/gemini-3-is-now-available-for-ai.html), Gemini 3 Flash is engineered for speed, and great for common development tasks and questions.

The new model is rolling out to developers using Gemini in Android Studio at no-cost (default model) starting today. For higher usage rate limits and longer sessions with Agent Mode, you can [use an AI Studio API key](https://developer.android.com/studio/gemini/add-api-key) to leverage the full capabilities of either Gemini 3 Flash or Gemini 3 Pro. We're also rolling out Gemini 3 model family access with higher usage rate limits to developers who have Gemini Code Assist Standard or Enterprise licenses. Your[IT administrator will need to enable access](https://developers.google.com/gemini-code-assist/docs/configure-release-channels) to preview models through the Google Cloud console.

## Get started today

You can start experimenting with Gemini 3 Flash via Firebase AI Logic today. Learn more about it in the [Android](https://developer.android.com/ai/gemini) and [Firebase documentation](https://firebase.google.com/docs/ai-logic/get-started?api=dev). Try out any of the new Gemini 3 models in Android Studio for development assistance, and let us know what you think! As always you can follow us across [LinkedIn](https://www.linkedin.com/showcase/androiddev/posts/?feedView=all), [Blog](https://android-developers.googleblog.com/), [YouTube](https://www.youtube.com/user/androiddevelopers), and[X](https://x.com/AndroidDev).

###### Written by:

-

  ## [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/thomas-ezan) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp) ![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan) 17 Apr 2026 17 Apr 2026 ![](https://developer.android.com/static/blog/assets/Hybrid_inference_solution_for_Android_Blog_1_518db36e12_gOJm.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Experimental hybrid inference and new Gemini models for Android](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android)

  [arrow_forward](https://developer.android.com/blog/posts/experimental-hybrid-inference-and-new-gemini-models-for-android) If you are an Android developer looking to implement innovative AI features into your app, we recently launched powerful new updates.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan) •
  3 min read

- [![](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)](https://developer.android.com/blog/authors/thomas-ezan)[![](https://developer.android.com/static/blog/assets/Mozart_Louis_622373dab1_1RaA8T.webp)](https://developer.android.com/blog/authors/mozart-louis) 13 Oct 2025 13 Oct 2025 ![](https://developer.android.com/static/blog/assets/Android_Blog_banners_dd5c7be5f2_ZsFAUM.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Boost user engagement with AI Image Generation](https://developer.android.com/blog/posts/boost-user-engagement-with-ai-image-generation)

  [arrow_forward](https://developer.android.com/blog/posts/boost-user-engagement-with-ai-image-generation) Adding custom images to your app can significantly improve and personalize user experience and boost user engagement.

  ###### [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Mozart Louis](https://developer.android.com/blog/authors/mozart-louis) •
  5 min read

- [![](https://developer.android.com/static/blog/assets/meghan_d663ed9c69_e0a5b5a564_Z21FLk.webp)](https://developer.android.com/blog/authors/meghan-mehta) 22 Apr 2026 22 Apr 2026 ![](https://developer.android.com/static/blog/assets/0420_Compose_1_11_Strapi_9c17b19a5e_1zjMqo.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [What's new in the Jetpack Compose April '26 release](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release)

  [arrow_forward](https://developer.android.com/blog/posts/whats-new-in-the-jetpack-compose-april-26-release) The Jetpack Compose April '26 release is stable. This release contains version 1.11 of core Compose modules (see the full BOM mapping), shared element debug tools, trackpad events, and more.

  ###### [Meghan Mehta](https://developer.android.com/blog/authors/meghan-mehta) •
  5 min read

# Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)