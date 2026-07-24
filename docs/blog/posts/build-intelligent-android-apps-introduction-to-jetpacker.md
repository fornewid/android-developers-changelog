---
title: https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker
url: https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker
source: md.txt
---

[How-tos](https://developer.android.com/blog/categories/how-tos)

# Build intelligent Android apps: Introduction to Jetpacker

4-min read ![](https://developer.android.com/static/blog/assets/0713_Jetpacker_Strapi_d07d6f2d4b_Z1tB3HE.webp) 22 Jul 2026 [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)](https://developer.android.com/blog/authors/jolanda-verhoef) [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef) Developer Relations Engineer Building GenAI features in your app usually means navigating through various models, APIs and architecture choices:

- **Execution location:** Where does your model run? On device, in the cloud, or both?
- **Complexity:** How complex is your setup? Are you doing a single inference call or do you need a more agentic flow?
- **In-app or Android System:** Should your feature be built into your Android app or does it fit better as an Android system integration?

In this blog post series we'll navigate these choices with you. We will take you along on a journey, starting with a basic mobile app and transforming it into a **personalized** , **intelligent** , and **agentic** experience.

## Jetpacker: a demo travel app

Jetpacker is a **technical showcase app** that our team built from the ground up for this year's Google I/O (built using Antigravity). At its core, Jetpacker helps users plan, explore, and enjoy their next big adventure. It shows an overview of your trips, the itinerary of each trip, and details of each event on that trip. Of course following all best practices of Android development, including a beautifully expressive Material UI design.

<br />

[Video](https://www.youtube.com/watch?v=_iuXykdlTkk)

<br />

And best of all? It's fully [open source](https://github.com/android/ai-samples/tree/main/jetpacker)!

Today we are publishing a series of**technical blog posts** diving deep into each of these features. We'll provide detailed implementation steps, code snippets, and architectural insights to help you build your own intelligent Android applications.

## [On-device intelligence](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html)

![Screenshot 2026-07-02 at 12.57.08 PM.png](https://developer.android.com/static/blog/assets/Screenshot_2026_07_02_at_12_57_08_PM_808698b355_1A8yMF.webp) On-device features in Jetpacker: Summarizing trip itineraries, managing expenses, and voice notes

Using an on-device model comes with **no additional cloud inference** costs, means you don't have to worry about **internet connectivity** , and lets users be confident that private information will be **processed locally**, on the device, without any of their data being sent to the cloud.

In Jetpacker, we chose on-device inference for three of our features:

- The **trip overview** feature transforms a messy, multi-day itinerary into a concise, actionable summary. It leverages Gemini Nano through the [ML Kit GenAI APIs](https://developers.google.com/ml-kit/genai/prompt/android) to process data locally on the device. We consider this a nice-to-have feature where we don't want to incur extra cloud costs, making on-device inference the right choice.
- The **expense tracker** automatically extracts structured data from receipt images to help users track their travel spending. It uses the [multimodal capabilities](https://developers.google.com/ml-kit/genai/prompt/android/get-started#provide-multimodal) of Gemini Nano 4 through the ML Kit GenAI APIs. We choose an on-device solution so that any privacy-sensitive information on the receipt images never leaves the user's device.
- The **audio diary** records, transcribes, and categorizes voice notes into relevant trip activities. It is powered by the [ML Kit Speech Recognition](https://developers.google.com/ml-kit/genai/speech-recognition/android) and [GenAI Prompt APIs](https://developers.google.com/ml-kit/genai/prompt/android/get-started). We chose an on-device solution for privacy and connectivity reasons.

## [Cloud \& hybrid inference](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html)

![features.png](https://developer.android.com/static/blog/assets/features_954606d688_Z1uIu4l.webp) Cloud and hybrid features in Jetpacker: Museum assistant with web grounding, hybrid restaurant review drafting, and hotel support chat featuring custom-routed live translation.

Sometimes your use-case requires AI models with **greater world knowledge** or a much **larger context window** and with greater ability in **handling complex tasks**. In that case, we can switch from running an on-device model to using a cloud model instead.

Or, if you want to get the best of both worlds, you can use hybrid inference to **dynamically choose** either a cloud or on-device model at runtime. This allows us to **lower costs** by moving inference to the device when it is available, but at the same time **support all Android devices** running the app.

In Jetpacker, we implemented several features using cloud or hybrid inference:

- The **place Q\&A** feature answers user questions about specific locations by grounding responses in real-world data. It uses [Firebase AI Logic](https://firebase.google.com/docs/ai-logic) integrated with [Google Maps](https://firebase.google.com/docs/ai-logic/grounding-google-maps) and [web context](https://firebase.google.com/docs/ai-logic/grounding-google-search). Using a cloud model is necessary here for its greater world knowledge.
- The **review drafting** feature helps users compose detailed reviews for the places they have visited. It leverages both on-device and cloud models through Firebase AI Logic's new [Hybrid inference API](https://firebase.google.com/docs/ai-logic/hybrid/android/get-started). This is a feature we wanted to make available to all app users, so we're using a cloud model as a fallback when an on-device model is unavailable.
- The **automatic chat translation** dynamically translates chat messages in real time to facilitate seamless communication, demonstrating custom hybrid inference logic. Again, we want this feature to be available to all app users, but at the same time have some specific considerations on when to choose on-device versus cloud.

## [System integration](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html)

<br />

[Video](https://www.youtube.com/watch?v=qtQMH8RBYIo)

<br />

While not a feature you see in the app itself, the Android system integration opens up the app's core capabilities directly to the Android operating system. It uses the [AppFunctions API](https://developer.android.com/ai/appfunctions) to integrate with system-level intelligence.

## In-app agentic workflows (coming soon!)

![agentic-feature-booking-assistant.png](https://developer.android.com/static/blog/assets/agentic_feature_booking_assistant_e9f4481776_1W5zsk.webp) The booking assistant shows several in-progress flight bookings, asking the user for input before making a final booking.

Agenticness introduces a higher level of**autonomy** , enabling models to act as agents. Instead of a single inference call, an agent works towards a specific goal via an orchestration loop that allows it to **reason** , use **tools** , and **adapt**its path. Depending on your requirements, these intelligent agents can run either in the cloud, directly on-device, or in a hybrid setup.

For Jetpacker we added a **booking assistant** that automates end-to-end booking workflows directly within the application to streamline reservations. It is built using [A2UI](https://a2ui.org/) and [ADK](https://adk.dev/) running in the cloud. The Android app functions as a front-end to the multi-agentic system running in the cloud.

## Learn more

Check out the other parts of this blog post series:

[**Part 1 (this post!):**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html) Introduction of the app and a high-level overview.  
[**Part 2:**](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html) On-device intelligence. Deep-dive into ML Kit's GenAI APIs and Gemini Nano to build privacy-first features like itinerary summarization, receipt parsing, and local audio processing.  
[**Part 3:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html) Hybrid and cloud reasoning. Explore how to use Firebase AI Logic to ground LLM answers in real-world data like Google Maps and web context.  
[**Part 4:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html) System integration. Integrating with the Android intelligence system using AppFunctions.  
Part 5 (coming soon): In-app agentic workflows. Extend the app with an end-to-end booking assistant powered by A2UI and ADK.

Interested in more on Android Development? Follow Android Developers on [YouTube](https://www.youtube.com/@AndroidDevelopers) or [LinkedIn](https://www.linkedin.com/showcase/androiddev/)!
- [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
Written by:

-

  ## [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jolanda-verhoef) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_Z1KU2ms.webp)
Continue reading
- 3 Authors 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/features_in_Jetpacker_Features_with_Firebase_AI_Logic_Strapi_0a6fbb7edb_21AGRW.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: Cloud and hybrid inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan), [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef), [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 8 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
- [![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/0625_Building_Jet_Packer_with_Intelligent_On_Device_features_Strapi_v02_3f5a8b17b0_1UrFxh.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: On-device inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post we introduced Jetpacker, the demo app we'll use throughout this series.
  [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 6 min read
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