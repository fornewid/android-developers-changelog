---
title: https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference
url: https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference
source: md.txt
---

[How-tos](https://developer.android.com/blog/categories/how-tos)

# Build intelligent Android apps: On-device inference

6-min read ![](https://developer.android.com/static/blog/assets/0625_Building_Jet_Packer_with_Intelligent_On_Device_features_Strapi_v02_3f5a8b17b0_1UrFxh.webp) 22 Jul 2026 [![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang) [Caren Chang](https://developer.android.com/blog/authors/caren-chang) Developer Relations Engineer Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a **personalized** , **intelligent** , and **agentic** experience. In our [previous post we introduced Jetpacker](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html), the demo app we'll use throughout this series.

In this blog post, we will share how you can use Gemini Nano through [ML Kit's Prompt API](https://developers.google.com/ml-kit/genai/prompt/android) to build intelligent on-device features.

Building intelligent on-device features refers to the ability to process prompts and data directly on a device without sending data to a server. This offers a few advantages:

- User data can be processed **locally** on the device, preserving user privacy
- Functionality of the model is **reliable** even with spotty or no internet connection
- No additional cloud inference **cost**, since everything runs on the user's hardware

With the benefits of on-device in mind, we identified three features to add in Jetpacker that can improve the user experience: summarizing trip itineraries, managing expenses, and capturing voice notes.
![Screenshot 2026-07-02 at 12.57.08 PM.png](https://developer.android.com/static/blog/assets/Screenshot_2026_07_02_at_12_57_08_PM_808698b355_1A8yMF.webp) On-device features in Jetpacker: Summarizing trip itineraries, managing expenses, and voice notes

### High quality tailored summarization of short texts

The itinerary screen gives users a quick overview of all activities for a given trip. Since this screen contains a lot of information, it can quickly become overwhelming. To help users prepare without feeling overwhelmed, we can add a **'Get ready for your trip'** section at the top.
![Screenshot_20260702_111934.png](https://developer.android.com/static/blog/assets/Screenshot_20260702_111934_b931d91d9d_uKc3d.webp) The romantic Paris trip is summarized as a classic Parisian adventure blending art, sights, and delicious food. A tip and some useful phrases are also added.

By inputting a trip itinerary and asking an LLM to summarize it, we can generate a quick summary of the trip along with packing tips and useful local phrases. This is a great use case for an on-device model for several reasons:

- **Performance and quality:** Both the input and output text are relatively short. With that, we can expect the performance and quality of an on-device solution to be on par with more powerful cloud models.
- **Scalability:** Shifting inference on-device allows us to scale this feature from a few users to millions without worrying about managing increasing cloud inference costs.
- **Low latency and reliability:** On-device inference guarantees low latency, providing a reliable experience even when users are offline.

To build with on-device, we use **Gemini Nano** , Google's most efficient model optimized for mobile devices. Gemini Nano was first introduced a few years ago, and is now running on over 140 million devices. The latest version of the model, [Gemini Nano 4, is built on the architecture foundation of the recently released Gemma 4 model](https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html), and is further optimized for maximum battery and performance efficiency.

Using ML Kit's**Prompt API**, we can take advantage of Gemini Nano 4's new model capabilities to prototype our on-device features. We'll create a prompt that includes the itinerary of a trip and ask the model to generate a summary along with any preparation tips.

Finding the optimal prompt usually requires some iteration, and the AICore app is perfect for this step in the process. After opting into the [developer preview option for AICore](https://developers.google.com/ml-kit/genai/aicore-dev-preview), we can download preview models such as Gemini Nano 4 to test prompts and see the model's expected outputs. With a few iterations on the prompt, we were able to improve the speed of the response from 13 seconds to under 2 seconds! Check out the final code implementation and prompt here.

\[ASSET HERE - FILE TOO LARGE ATM\]

### Local processing for sensitive user input

Next, to help users enjoy their trip even more, we'll build a simple expense manager that takes the manual work out of sorting through receipts and calculating budgets.

Since receipts might contain sensitive information like credit card number and addresses, this is another great use case for an on-device solution. With on-device, users can be confident that private information will be processed locally on the device without any of their data being sent to the cloud.

In addition, Gemini Nano 4 has improved model capabilities for multimodality, especially for image understanding tasks like OCR and visual data extraction, making it a great solution for tasks like extracting information from receipts.

For this use case, the prompt will analyze an image of the receipt, and output information such as: a generated title, amount spent and category of the expense. To ensure the model outputs the information in the preferred format, we can use [ML Kit's Structured Output API](https://developers.google.com/ml-kit/genai/prompt/android/structured-output) to seamlessly output a Kotlin data object that we define.

```
// implementation("com.google.mlkit:genai-prompt:1.0.0-beta3")
// ksp("com.google.mlkit:genai-schema-compiler:1.0.0-alpha1")

@Generable("Information extracted from an expense receipt")
data class ParsedReceipt(
  @Guide("Generated title for the expense less than 6 words. Based on restaurant or activity name.")
  val title: String,
  @Guide("Total amount of the expense. Look for values at the bottom and words like total or balance due.")
  val amount: Double,
  @Guide("Type of expense", enumValues = ["travel", "food", "shopping", "entertainment", "other"])
  val category: String,
)

val prompt = "Determine if the image is a receipt or expense. 
    If it is NOT a receipt or expense, output the text 'NOT_A_RECEIPT'.
    Otherwise, parse the receipt information."

val request = generateContentRequest(ImagePart(bitmap), TextPart(prompt)) {}
val requestWithStructuredOutput = generateTypedContentRequest(request, ParsedReceipt::class)

// Define the configuration for Gemini Nano 4 E4B preview model  
// When selecting models, you can specify which performance charactertists are most important
//  for your use case. Use ModelPreference.FULL when you want to prioritize reasoning power over speed. 
//  Use ModelPreference.FAST when complex logic is not required and latency is a priority.
val previewFullConfig = generationConfig {
    modelConfig = modelConfig {
        releaseStage = ModelReleaseStage.PREVIEW
        preference = ModelPreference.FULL
    }
}

val geminiNano4BPreviewModel = Generation.getClient(previewFullConfig)
val response = geminiNano4BPreviewModel.generateContent(requestWithStructuredOutput)
val parsedReceipt: ParsedReceipt? = response.candidates.firstOrNull()?.response
```

### Multimodal input

Lastly, to help users record audio memos during the trip, let's build a fully on-device voice notes feature. Using [ML Kit's Speech Recognition API](https://developers.google.com/ml-kit/genai/speech-recognition/android), we'll enable users to record short voice notes that are automatically transcribed to text. With the transcribed text, we'll use ML Kit's Prompt API to identify which trip activity is associated with the recorded voice note, letting users easily recap their trip as they scroll through the trip's itinerary.
![Screenshot_20260702_115529.png](https://developer.android.com/static/blog/assets/Screenshot_20260702_115529_506ad03837_ZMEjEn.webp) The Roman holiday itinerary shows voice note extracts.

The [**ML Kit GenAI Speech Recognition API**](https://developers.google.com/ml-kit/genai/speech-recognition/android) allows you to transcribe audio content to text fully on-device using two distinct modes. **Basic mode** uses a traditional on-device speech recognition model and is available on most Android devices with API level 31 and higher. **Advanced mode** uses Gemini Nano to offer broader language coverage and better quality, and is currently supported on Pixel 10 devices.

For our feature we combine the Speech Recognition API with the ML Kit GenAI Prompt API:

```
// implementation("com.google.mlkit:genai-prompt:1.0.0-beta3")
// implementation("com.google.mlkit:genai-speech-recognition:1.0.0-alpha1")

val tripEvents = ... 

// Set up speech recognition
val speechRecognizerOptions =
    speechRecognizerOptions {
        locale = Locale.US
        preferredMode = SpeechRecognizerOptions.Mode.MODE_ADVANCED
    }
val speechRecognizer: SpeechRecognizer = SpeechRecognition.getClient(speechRecognizerOptions)

suspend fun transcribeVoiceNote(recognizer: SpeechRecognizer) {
    // Display partial text as the user is recording audio
    var partialTextResponse = ""

    // Display the full text once user is finished recording audio
    var transcription = ""

    val request: SpeechRecognizerRequest
        = speechRecognizerRequest { audioSource = AudioSource.fromMic() }
    recognizer.startRecognition(request).collect { response ->
        when (response) {
            is SpeechRecognizerResponse.PartialTextResponse -> {
                partialTextResponse = response.text
            }
            is SpeechRecognizerResponse.FinalTextResponse -> {
                transcription = response.text
                processAndCategorizeVoiceNote(transcription, tripEvents)
            }
        }
    }
}

fun processAndCategorizeVoiceNote(transcribedVoiceNote: String, events: List<Event>) {
    val prompt = "Given the voice note $transcribedVoiceNote
     and the following events for this trip: $events, rewrite this transcription
     to remove filler words. Then, identify which events from the
     list this rewritten transcription matches to."

     // Utilize ML Kit's Prompt API to process voice note and tag it with the relevant trip activities
     Generation.getClient().generateContent(prompt)
}
```

### Conclusion

Using ML Kit's GenAI APIs, we were able to take advantage of Gemini Nano to develop fully on-device intelligent features for the JetPacker app, and provide an improved user experience without any additional cloud costs.

Check out the full source code for Jetpacker on Github, and watch the video [Build Intelligent Android apps with Google's AI](https://www.youtube.com/watch?v=_iuXykdlTkk) to learn more about how to integrate intelligent features directly into your app using on-device models, cloud-powered reasoning, and the latest agentic frameworks.

### Learn more

Check out the other parts of this blog post series:

[**Part 1:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html) Introduction of the app and a high-level overview.

[**Part 2 (this post!):**](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html)On-device intelligence. Deep-dive into ML Kit's GenAI APIs and Gemini Nano to build privacy-first features like itinerary summarization, receipt parsing, and local audio processing.

[**Part 3:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html)Hybrid and cloud reasoning. Explore how to use Firebase AI Logic to ground LLM answers in real-world data like Google Maps and web context.

[**Part 4:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html) System integration. Integrating with the Android intelligence system using AppFunctions.

**Part 5 (coming soon):** In-app agentic workflows. Extend the app with an end-to-end booking assistant powered by A2UI and ADK.

Interested in more on Android Development? Follow Android Developers on [YouTube](https://www.youtube.com/@AndroidDevelopers) or [LinkedIn](https://www.linkedin.com/showcase/androiddev/)!

All code snippets in this blog post follow the following copyright notice:

```
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
```
- [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
Written by:

-

  ## [Caren Chang](https://developer.android.com/blog/authors/caren-chang)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/caren-chang) ![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp) ![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)
Continue reading
- 3 Authors 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/features_in_Jetpacker_Features_with_Firebase_AI_Logic_Strapi_0a6fbb7edb_21AGRW.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: Cloud and hybrid inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef), [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 8 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
- [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)](https://developer.android.com/blog/authors/jolanda-verhoef) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/0713_Jetpacker_Strapi_d07d6f2d4b_Z1tB3HE.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: Introduction to Jetpacker](https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker) Jetpacker is a technical showcase app that our team built from the ground up for this year's Google I/O (built using Antigravity). At its core, Jetpacker helps users plan, explore, and enjoy their next big adventure.
  [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef) • 4 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
- [![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/AFD_ABL_104_Jet_Packer_App_Functions_Strapi_6b8d975401_ZbOM76.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: Integrate into Android's intelligence system using AppFunctions](https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post, we explored how to leverage Firebase AI Logic to build cloud-hosted and hybrid AI features.
  [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) • 6 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)