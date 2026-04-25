---
title: https://developer.android.com/blog/posts/ml-kit-s-prompt-api-unlock-custom-on-device-gemini-nano-experiences
url: https://developer.android.com/blog/posts/ml-kit-s-prompt-api-unlock-custom-on-device-gemini-nano-experiences
source: md.txt
---

#### [Product News](https://developer.android.com/blog/categories/product-news)

# ML Kit's Prompt API: Unlock Custom On-Device Gemini Nano Experiences

###### 2-min read

![](https://developer.android.com/static/blog/assets/kakao_8769e675f9_Z1GfWxl.webp) 30 Oct 2025 3 Authors

##### [Caren Chang,](https://developer.android.com/blog/authors/caren-chang)
[Chengji Yan,](https://developer.android.com/blog/authors/chengji-yan)
[Penny Li](https://developer.android.com/blog/authors/penny-li)

AI is making it easier to create personalized app experiences that transform content into the right format for users. We previously enabled developers to integrate with Gemini Nano through [ML Kit GenAI APIs](https://android-developers.googleblog.com/2025/05/on-device-gen-ai-apis-ml-kit-gemini-nano.html) tailored for specific use cases like summarization and image description.

Today marks a major milestone for Android's on-device generative AI. We're announcing the **Alpha release of the ML Kit GenAI Prompt API**. This API allows you to send natural language and multimodal requests to Gemini Nano, addressing the demand for more control and flexibility when building with generative models.

[Partners like Kakao are already building with Prompt API](https://android-developers.googleblog.com/2025/10/kakao-mobility-uses-gemini-nano-on.html), creating unique experiences with real-world impact. You can experiment with Prompt API's powerful features today with minimal code.

[Video](https://www.youtube.com/watch?v=PoqJh_60Wrw)

**Move beyond pre-built to custom on-device GenAI**

Prompt API moves beyond pre-built functionality to support custom, app-specific GenAI use cases, allowing you to create unique features with complex data transformation. Prompt API uses Gemini Nano on-device to process data locally, enabling offline capability and improved user privacy.

**Key use cases for Prompt API:**

Prompt API allows for highly customized GenAI use cases. Here are some recommended examples:

- Image understanding: Analyzing photos for classification (e.g., creating a draft social media post or identifying tags such as "pets," "food," or "travel").
- Intelligent document scanning: Using a traditional ML model to extract text from a receipt, and then categorizing each item with Prompt API.
- Transforming data for the UI: Analyzing long-form content to create a short, engaging notification title.
- Content prompting: Suggesting topics for new journal entries based on a user's preference for themes.
- Content analysis: Classifying customer reviews into a positive, neutral, or negative category.
- Information extraction: Extracting important details about an upcoming event from an email thread.

**Implementation**   
Prompt API lets you create custom prompts and set optional generation parameters with just a few lines of code:

```
Generation.getClient().generateContent(
   generateContentRequest(
       ImagePart(bitmapImage),
       TextPart("Categorize this image as one of the following: car, motorcycle, bike, scooter, other. Return only the category as the response."),
   ) {
       // Optional parameters
       temperature = 0.2f
       topK = 10
       candidateCount = 1
       maxOutputTokens = 10
   },
)
```

For more detailed examples of implementing Prompt API, check out the [official documentation](https://developers.google.com/ml-kit/genai/prompt/android) and [sample on Github](https://github.com/googlesamples/mlkit/tree/master/android/genai).

**Gemini Nano, performance, and prototyping**

Prompt API currently performs best on the Pixel 10 device series, which runs the latest version of Gemini Nano (nano-v3). This version of Gemini Nano is built on the same architecture as Gemma 3n, the model we first shared with the open model community at I/O.

The shared foundation between Gemma 3n and nano-v3 enables developers to more easily prototype features. For those without a Pixel 10 device, you can start experimenting with prompts today by prototyping with Gemma 3n locally.

For the full list of devices that support GenAI APIs, refer to our [device support documentation.](https://developers.google.com/ml-kit/genai#device-support)

**Learn more**

Start implementing Prompt API in your Android apps today with guidance from our [official documentation](https://developers.google.com/ml-kit/genai/prompt/android) and the [sample on Github](https://github.com/googlesamples/mlkit/tree/master/android/genai).

###### Written by:

-

  ## [Caren Chang](https://developer.android.com/blog/authors/caren-chang)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/caren-chang) ![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp) ![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)
-

  ## [Chengji Yan](https://developer.android.com/blog/authors/chengji-yan)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/chengji-yan) ![](https://developer.android.com/static/blog/assets/Chengji_Yan_575ccacca8_Z1RWjMU.webp) ![](https://developer.android.com/static/blog/assets/Chengji_Yan_575ccacca8_Z1RWjMU.webp)
-

  ## [Penny Li](https://developer.android.com/blog/authors/penny-li)

  ###### Software Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/penny-li) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg) ![](https://developer.android.com/static/blog/assets/default-avatar.DvQ_6oi6_pd2P1.svg)

## Continue reading

- [![](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang)[![](https://developer.android.com/static/blog/assets/David_Chou_226df78370_tqGIk.webp)](https://developer.android.com/blog/authors/david-chou) 02 Apr 2026 02 Apr 2026 ![](https://developer.android.com/static/blog/assets/announcing_gemma4_aicore_ce479292b9_Z15e7FP.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [Announcing Gemma 4 in the AICore Developer Preview](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview)

  [arrow_forward](https://developer.android.com/blog/posts/announcing-gemma-4-in-the-ai-core-developer-preview) At Google, we're committed to bringing the most capable AI models directly to the Android devices in your pocket. Today, we're thrilled to announce the release of our latest state-of-the-art open model: Gemma 4.

  ###### [Caren Chang](https://developer.android.com/blog/authors/caren-chang), [David Chou](https://developer.android.com/blog/authors/david-chou) •
  3 min read

- 4 Authors 28 Jan 2026 28 Jan 2026 ![](https://developer.android.com/static/blog/assets/Prompt_API_Banner_1_ff0c780828_1kyTTw.webp)

  #### [Product News](https://developer.android.com/blog/categories/product-news)

  ## [How Automated Prompt Optimization Unlocks Quality Gains for ML Kit's GenAI Prompt API](https://developer.android.com/blog/posts/how-automated-prompt-optimization-unlocks-quality-gains-for-ml-kit-s-gen-ai-prompt-api)

  [arrow_forward](https://developer.android.com/blog/posts/how-automated-prompt-optimization-unlocks-quality-gains-for-ml-kit-s-gen-ai-prompt-api) To further help bring your ML Kit Prompt API use cases to production, we are excited to announce Automated Prompt Optimization (APO) targeting On-Device models on Vertex AI. Automated Prompt Optimization is a tool that helps you automatically find the optimal prompt for your use cases.

  ###### [Chetan Tekur](https://developer.android.com/blog/authors/chetan-tekur), [Chao Zhao](https://developer.android.com/blog/authors/chao-zhao), [Paul Zhou](https://developer.android.com/blog/authors/paul-zhou), [Caren Chang](https://developer.android.com/blog/authors/caren-chang) •
  3 min read

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