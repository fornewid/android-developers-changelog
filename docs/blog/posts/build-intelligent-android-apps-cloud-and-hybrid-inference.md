---
title: https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference
url: https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference
source: md.txt
---

[How-tos](https://developer.android.com/blog/categories/how-tos)

# Build intelligent Android apps: Cloud and hybrid inference

8-min read ![](https://developer.android.com/static/blog/assets/features_in_Jetpacker_Features_with_Firebase_AI_Logic_Strapi_0a6fbb7edb_21AGRW.webp) 22 Jul 2026 3 Authors [Thomas Ezan,](https://developer.android.com/blog/authors/thomas-ezan) [Jolanda Verhoef,](https://developer.android.com/blog/authors/jolanda-verhoef) [Caren Chang](https://developer.android.com/blog/authors/caren-chang) Welcome back to the blog post series "[Build intelligent Android apps](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html)" where we take a basic Android app and transform it into a **personalized** , **intelligent** , and **agentic** experience. In our [previous post](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html) we explored how to build intelligent on-device features using Gemini Nano through ML Kit's Prompt API.

In this post, we will look at how you can leverage [**Firebase AI Logic**](https://firebase.google.com/docs/ai-logic)to build cloud-hosted and hybrid AI features:

- Grounding answers in real-world context
- Routing requests dynamically between cloud and local execution using hybrid inference
- Translating content with custom routing systems

<br />

[Video](https://www.youtube.com/watch?v=_iuXykdlTkk)

<br />

Sometimes a use case requires AI models with greater world knowledge, a much larger context window, or the ability to handle complex queries. In those scenarios, we can leverage cloud models.

Other times, you want the best of both worlds: using hybrid inference to run on-device when available to lower costs, while falling back to the cloud to ensure compatibility for all devices.
![features.png](https://developer.android.com/static/blog/assets/features_f241976ea5_ZkDp5d.webp) Cloud and hybrid features in Jetpacker: Museum assistant with web grounding, hybrid restaurant review drafting, and support chat featuring custom-routed live translation.

Let's look at how we implemented three cloud and hybrid features in [Jetpacker](https://github.com/android/ai-samples/tree/main/jetpacker):

- a museum assistant with web grounding
- hybrid restaurant review drafting
- hotel support chat featuring custom-routed live translation.

## Use LLM grounding for up-to-date informationMuseum assistant chatbot with LLM grounding

The **Museum assistant**is an interactive chatbot designed to help users plan their museum visits. It provides visitors with up-to-date details regarding specific exhibits, current opening hours, ticket pricing, and more.
![museum_assistant_upscaled.png](https://developer.android.com/static/blog/assets/museum_assistant_upscaled_86ffae3c30_Z20TuJD.webp) Museum assistant is a chatbot that answers questions, such as 'How can I get a ticket discount for Le Louvre?'

When building AI features, getting the model to answer with fresh, accurate, and specific real-world information is a common challenge. While cloud models possess massive amounts of world knowledge, they might not know about seasonal exhibits or the current day's opening hours.
![grounding.png](https://developer.android.com/static/blog/assets/grounding_6a8e593136_22EPJv.webp) Grounding data is added to the context window to enable the model to answer questions correctly and accurately.

To bridge this gap, we can use grounding techniques to add extra context to the model's context window. The [Firebase AI Logic SDK](https://firebase.google.com/products/firebase-ai-logic) supports three types of grounding:

- [**URL grounding**](https://firebase.google.com/docs/ai-logic/url-context)**:** Grounding responses using content from a specific webpage (e.g. current ticket prices or museum rules).
- [**Google Search grounding**](https://firebase.google.com/docs/ai-logic/grounding-google-search)**:** Letting the model query the real-time Google search index for up-to-date details.
- [**Maps grounding**](https://firebase.google.com/docs/ai-logic/grounding-google-maps)**:** Using Google Maps location data.

In Jetpacker, we dynamically construct the available tools based on enabled feature flags and initialize the generative model using the Firebase AI SDK:

```kotlin
// implementation("com.google.firebase:firebase-ai-logic")

private var toolList = mutableListOf<Tool>()

init {
    if (ENABLE_SEARCH_GROUNDING) {
        toolList.add(Tool.googleSearch())
    }
    if (ENABLE_URL_GROUNDING) {
        toolList.add(Tool.urlContext())
    }
}

private val generativeModel = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-3-flash",
        systemInstruction = content {
            text("You are a helpful museum assistant answering questions about a museum. Use plain text.")
        },
        tools = toolList
    )
```

When the user queries the assistant, if URL grounding is enabled, we append the specific museum resource URLs directly into the prompt:

```kotlin
val groundingText = if (FeatureFlags.ENABLE_URL_GROUNDING) {
    "\n If the following message above is about the rules and terms to visit Le Louvre, " +
    "if needed answer this urls ${urlList.joinToString()}"
} else {
    ""
}

val prompt = "$text $groundingText"

var response = chat.sendMessage(prompt)
```

## Hybrid inference: On-device review generation with Maps deep link

Not every AI task requires a cloud-based model, and not every device is online. To help developers balance latency, cost, and offline availability, we recently introduced the [Firebase API for Hybrid Inference](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started?api=dev).

In Jetpacker, the **restaurant review** feature lets users review select topics and automatically drafts a review. To enable this for all users, we prioritize local execution with Gemini Nano, and fall back to cloud models on devices that don't support Gemini Nano.
![review_upscaled.png](https://developer.android.com/static/blog/assets/review_upscaled_c12b0e6b00_ecjNx.webp) The restaurant review feature uses hybrid inference to draft a review based on topics

```kotlin
// implementation("com.google.firebase:firebase-ai-logic")
// implementation("com.google.firebase:firebase-ai-ondevice:16.0.0-beta03")


// Initialize the model with hybrid routing configuration
val reviewModel = Firebase.ai.generativeModel(
    modelName = "gemini-3.1-flash-lite",
    onDeviceConfig = OnDeviceConfig(
        inferenceMode = InferenceMode.PREFER_ON_DEVICE
    )
)
```

The Hybrid Inference API supports four distinct routing modes:

- **PREFER_ON_DEVICE:** Prioritizes local execution and falls back to cloud if Gemini Nano is unavailable.
- **PREFER_IN_CLOUD:** Prioritizes cloud execution and falls back to on-device if the device goes offline.
- **ONLY_ON_DEVICE:** Restricts execution strictly to the device.
- **ONLY_IN_CLOUD:** Restricts execution strictly to the cloud.

Once the review is generated, we copy it to the clipboard and use an intent to open Google Maps directly to the restaurant's review page, providing a seamless user experience:

```kotlin
private fun copyAndOpenMapsReview(context: Context, reviewText: String, placeId: String) {
    val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
    val clip = ClipData.newPlainText("User Review", reviewText)
    clipboard.setPrimaryClip(clip)

    val uri = Uri.parse("https://search.google.com/local/writereview/mobile?placeid=$placeId")
    val intent = Intent(Intent.ACTION_VIEW, uri).apply {
        setPackage("com.google.android.apps.maps")
    }
    context.startActivity(intent)
}
```

## Custom hybrid routing: Hotel support chat translation with simulated personas

The **hotel support chat** was built to let users finalize logistics and check on hotel details. This feature uses system instructions to configure a localized receptionist assistant. By passing specific information---such as the preferred language and hotel information---in the instructions, we can set up a conversational persona representing a specific hotel.

```kotlin
private val generativeModel = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        systemInstruction = content {
            text("""
              You are a helpful hotel receptionist at $hotelName only speaking $language. 
              Answer politely in $language. The bar closes at 10pm and breakfast is from 7am to 10am.
              There's someone at the desk 24/7. You can retrieve your luggage from the storage room 
              at the back of the lobby at any time.
              """)
        },
        modelName = "gemini-3-flash-preview"
    )
```

Because receptionist responses are in the hotel's local language (for example, French for Hotel Le Meurice in Paris), we need to translate messages to the user's preferred language.
![translation_upscaled.png](https://developer.android.com/static/blog/assets/translation_upscaled_5e297d961e_2wJzig.webp) Hotel support chat messages are automatically translated to the user's preferred language

While hybrid models can configure simple routing preferences, complex scenarios require custom routing logic. In Jetpacker, we implement a custom routing stack that takes into account:

- **Language identification:** Using the on-device [ML Kit Language Identification API](https://developers.google.com/ml-kit/language/identification/android), we can detect the incoming message language.
- **On-device translation (Gemini Nano):** [ML Kit's Prompt API](https://developers.google.com/ml-kit/genai/prompt/android) lets us translate common language pairs directly on the device, saving bandwidth and cloud cost.
- **Cloud translation (Gemini 3 Flash):** For more complex languages, we use Gemini Flash 3 to get a higher quality translation.

```kotlin
// implementation("com.google.android.gms:play-services-mlkit-language-id:17.0.0") 

// ML Kit for Language Identification (powered by Google Play Services)
private val languageIdentifier = LanguageIdentification.getClient()

// On-device translator model (prefer Gemini Nano) for translating common language pairs
private val hybridTranslationModel = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-3-flash",
        onDeviceConfig = OnDeviceConfig(mode = InferenceMode.PREFER_ON_DEVICE)
    )

// Cloud translator model for more complex language pairs
private val cloudTranslationModel = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-3-flash"
    )
```

When a message needs to be translated, we identify the source language and apply our custom routing logic, executing either on-device or cloud translation:

```kotlin
fun translateMessage(message: SupportChatMessage) {
    viewModelScope.launch {
        // 1. Detect language using ML Kit Language Identification
        val sourceLang = try {
            Tasks.await(languageIdentifier.identifyLanguage(message.text))
        } catch (e: Exception) {
            "Undefined"
        }

        // 2. Custom routing: we've verified the translation quality for English and Korean with Gemini Nano, and will translate message on-device for those two languages
        val routeToCloud = sourceLang != "en" && sourceLang != "kr"

        val prompt = "Translate the following text to $selectedLanguage. Just return the translated sentence: ${message.text}."

        val (translatedText, routePrefix) = if (routeToCloud) {
            val result = cloudTranslationModel.generateContent(prompt)
            result.text to "[Cloud]"
        } else {
            val result = hybridTranslationModel.generateContent(prompt)
            result.text to "[On-Device]"
        }

        if (translatedText != null) {
            _translations.update { current ->
                current + (message.id to "$routePrefix: $translatedText")
            }
        }
    }
}
```

In this example, the custom routing logic only takes into consideration the translation's source and target language. However, based on your app's use case, you can expand the routing logic to include other factors such as the on-device model version, network connectivity, battery status, and more.

## Securing the AI Pipelines: Firebase App Check

Lastly, using AI in the cloud opens up possibilities of API key abuse or unauthorized billing. To secure API calls, we integrated [**Firebase App Check**](https://firebase.google.com/docs/app-check) using both Play Integrity (production) and the local Debug Provider (for local development or emulators).

In the [JetPackerApplication.kt](https://github.com/android/ai-samples/blob/main/jetpacker/android/app/src/main/kotlin/com/example/jetpacker/JetPackerApplication.kt) file, we install the debug provider at startup and trigger anonymous authentication to establish a secure user session:

```kotlin
//  implementation("com.google.firebase:firebase-appcheck-playintegrity") 
//  implementation("com.google.firebase:firebase-appcheck-debug")  
//  implementation("com.google.firebase:firebase-auth") 

override fun onCreate() {
    super.onCreate()
    Firebase.initialize(context = this)
    Firebase.appCheck.installAppCheckProviderFactory(
        DebugAppCheckProviderFactory.getInstance()
    )
    Firebase.auth.signInAnonymously()
}
```

When building locally on an emulator, App Check prints a local token secret to logcat:

```
Enter this debug secret into the allow list in the Firebase Console: a8c2dd4c-xxxx-xxxx-xxxx-ef6c114ba27e
```

Once registered in the Firebase console, local requests are fully verified and authenticated by App Check, protecting our backend while letting us test the app locally.

## Conclusion

By combining cloud model capabilities (grounding, system instructions) with on-device capabilities (hybrid routing, translation, security app checks), we created a travel app that is smart, secure, and available offline.

Check out the [full source code for Jetpacker on GitHub](https://github.com/android/ai-samples/tree/main/jetpacker), and explore the Firebase documentation to get started:

[Firebase AI Logic Documentation](https://firebase.google.com/docs/ai-logic/get-started)  
[Firebase Hybrid Inference API](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started)

## Learn more

Check out the other parts of this blog post series:

[**Part 1**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html)**:** Introduction of the app and a high-level overview.  
[**Part 2**](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html)**:** On-device intelligence. Deep-dive into ML Kit's GenAI APIs and Gemini Nano to build privacy-first features like itinerary summarization, receipt parsing, and local audio processing.  
[**Part 3 (this post!):**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html) Hybrid and cloud reasoning. Explore how to use Firebase AI Logic to ground LLM answers in real-world data like Google Maps and web context.  
[**Part 4:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html)System integration. Integrating with the Android intelligence system using AppFunctions.   
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

  ## [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan)

  ###### Senior Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/thomas-ezan) ![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp) ![View Thomas Ezan's profile](https://developer.android.com/static/blog/assets/thomas_ezan_d29c7508d0_l9O72.webp)
-

  ## [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jolanda-verhoef) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)
-

  ## [Caren Chang](https://developer.android.com/blog/authors/caren-chang)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/caren-chang) ![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp) ![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)
Continue reading
- [![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/0625_Building_Jet_Packer_with_Intelligent_On_Device_features_Strapi_v02_3f5a8b17b0_1UrFxh.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: On-device inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post we introduced Jetpacker, the demo app we'll use throughout this series.
  [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 6 min read
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