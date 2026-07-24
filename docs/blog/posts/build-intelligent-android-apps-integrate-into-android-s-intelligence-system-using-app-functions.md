---
title: https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions
url: https://developer.android.com/blog/posts/build-intelligent-android-apps-integrate-into-android-s-intelligence-system-using-app-functions
source: md.txt
---

[How-tos](https://developer.android.com/blog/categories/how-tos)

# Build intelligent Android apps: Integrate into Android's intelligence system using AppFunctions

6-min read ![](https://developer.android.com/static/blog/assets/AFD_ABL_104_Jet_Packer_App_Functions_Strapi_6b8d975401_ZbOM76.webp) 22 Jul 2026 [![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)](https://developer.android.com/blog/authors/ben-weiss) [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss) Developer Relations Engineer Welcome back to the blog post series "[Build intelligent Android apps](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html)" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our [previous post](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html), we explored how to leverage Firebase AI Logic to build cloud-hosted and hybrid AI features.

Traditional mobile UIs excel at focused, hands-on tasks, and the Android intelligence system is introducing complementary features to make complex, multi-step actions even easier. By supplementing traditional user interfaces, AppFunctions provide a powerful new entry point: A privileged agent on the device can access app features in the background. This can be particularly helpful when users are driving, walking or otherwise multitasking.

In this article, we'll show you how we designed and integrated these capabilities into our travel planning app, [JetPacker](https://github.com/android/ai-samples/tree/main/jetpacker), using Android AppFunctions. We'll explore the rationale behind our feature choices, discuss the specialized tooling we used to accelerate development, and dive into the code that makes it all work.

## Designing AI-ready features: making choices that matter for your users

To select which features to provide to the intelligence system, we looked for tasks where a voice or text command is objectively faster than tapping through screens. In this side-by-side screen recording you can see this contrast perfectly: on the left, a user tapping through multiple screens to log an expense; on the right, the same task completed instantly in the background via a privileged agent.

Our first choice was expense tracking. Logging a coffee expense during a trip usually takes quite a few taps---unlocking the phone, opening the app, finding the active trip, navigating to the expenses tab, tapping the add button, taking a picture of the receipt, and checking the result. By providing the `addExpense` and `getExpenses` features as AppFunctions, the system agent handles the heavy lifting. When the user says, "Add a five-dollar coffee expense to my Paris trip," the agent automatically searches for the correct trip ID in the background and inserts the expense, skipping the manual UI flow entirely.

We also prioritized itinerary management. Finding what activity is next on a busy trip itinerary usually requires scrolling through a dense timeline view. By providing `getItinerary` and `addItineraryEvent` to the system, the user can simply ask, "What am I doing next in Paris?" and get an immediate answer.

Finally, we focused on hands-free note capturing. Typing out reminders or notes while walking down a busy street is difficult and unsafe. Exposing a voice note capability allows the user to say, "The flight was amazing, I saw a beautiful sunset and managed to sleep well," and the privileged agent automatically transcribes and saves it directly into the travel database using the addVoiceNote AppFunction.

## Android MCP powered by AppFunctions

This entire experience is built on Android MCP. Under this design, the app acts as a local MCP server. Rather than remote APIs, you provide your app features directly to the on-device intelligence system.  

[Android AppFunctions](https://developer.android.com/ai/appfunctions) is the API that brings this concept to life. It reads annotated Kotlin functions and compiles them into type-safe, sandboxed tool definitions that the privileged agent can discover and invoke locally on the device.
![Android MCP diagram.png](https://developer.android.com/static/blog/assets/Android_MCP_diagram_4d09483a18_Z29VBSa.webp) Diagram highlighting our apps, the android platform, and system agents coordinate AppFunctions.

Under the Android MCP model, your app acts as a local MCP server that exposes structured tools, while the Android platform serves as the central tool registry. On the MCP client side, agent apps are registered with the intelligence system after being granted system-privileged permissions to access the registry.

When a user interacts with a registered agent, its LLM determines if the request can be handled by an AppFunction, queries the platform's metadata, and executes the appropriate registered functions in the background. This local MCP client-server design gives you full control: you choose exactly which features are accessible to the agent, keeping the rest of your app's data private.

## How we accelerated development with Android skills

To streamline the integration process, we leveraged the [AppFunctions development skill](https://github.com/android/skills/tree/main/device-ai/appfunctions). The AppFunctions development skill is a complete development companion. It guided us through the entire lifecycle: mapping Kotlin data classes to serialize parameters, generating the necessary `Service` entry points, refining our `KDoc` documentation to ensure the LLM understands parameter boundaries, and setting up automated testing using ADB.

## Providing app features to the intelligence system

Enough with the theory, let's dive into the implementation.

#### Configuration and dependency setup

We begin by adding the AppFunctions dependencies. One for the API and one for the Kotlin Symbol Processing compiler.

```
implementation("androidx.appfunctions:appfunctions:1.0.0-alpha10")
ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-alpha10")
```

#### Modeling custom data types

Any custom object exchanged with the agent must be annotated with `@AppFunctionSerializable`. In our [TripSerializable.kt](https://github.com/android/ai-samples/tree/main/jetpacker/android/feature/appfunctions/src/main/java/com/example/jetpacker/feature/appfunctions/TripSerializable.kt) file, we define our trip data model:

```kotlin
@AppFunctionSerializable(isDescribedByKDoc = true)
data class TripSerializable(
    /** The trip's unique identifier. */
    val id: String,
    /** The trip's title. */
    val title: String,
    /** The trip's destination location. */
    val location: String,
    /** The trip's start date in milliseconds. */
    val startDate: Long,
    /** The trip's end date in milliseconds. */
    val endDate: Long,
    /** A list of participants. */
    val participants: List<String>,
)
```

#### Providing features using the @AppFunction annotation

Next, the skill wrote the Kotlin functions that perform the database queries and annotate them with `@AppFunction`. We can view this in searchTrip:

```kotlin
/**
 * Looks for trips based on optional filters like id, title (name), location, and dates.
 *
 * @param id The unique identifier of the trip.
 * @param title The title or name of the trip.
 * @param location The destination location.
 * @param startDate The minimum start date in milliseconds.
 * @param endDate The maximum end date in milliseconds.
 * @return A list of trips matching the filters.
 */
@AppFunction(isDescribedByKDoc = true)
suspend fun searchTrip(
    id: String? = null,
    title: String? = null,
    location: String? = null,
    startDate: Long? = null,
    endDate: Long? = null
): List<TripSerializable> {
    return withContext(Dispatchers.IO) {
    // implementation
}
```

Since AppFunctions run on the UI thread by default, we use `withContext(Dispatchers.IO)` to switch to a background dispatcher. Additionally, we refine our KDoc to use clear, imperative verbs and specify parameter constraints. This documentation compiles directly into the tool's schema, which the privileged agent uses to resolve parameters and handle runtime errors.

#### The service entry point and Hilt integration

To register these features with the intelligence system, we create an abstract base class that extends `AppFunctionService`. We annotate it with `@AppFunctionServiceEntryPoint`:

```kotlin
@RequiresApi(36)
@AndroidEntryPoint
@AppFunctionServiceEntryPoint(
    serviceName = "JetPackerAppFunctionService",
    appFunctionXmlFileName = "jetpacker_app_function_service"
)
abstract class BaseJetPackerAppFunctionService : AppFunctionService() {
    @Inject internal lateinit var tripDao: TripDao
    // DAOs and database references are injected here...
}
```

During compilation, KSP generates the final concrete service subclass, `JetPackerAppFunctionService`, as declared with the `serviceName` parameter. We also register `app_metadata.xml` in the app's manifest. This file provides global operational rules for JetPacker's declared AppFunctions.

## Testing and verifying your AppFunctions

Once implemented, you should verify that your AppFunctions are registered and working correctly.

Running devices or emulators with Android 17 or newer, you can use ADB commands from your terminal to list and invoke your functions. Running `adb shell cmd app_function list-app-functions` displays all registered functions for your package. You can then execute a specific function and test its database integration by running `adb shell cmd app_function execute-app-function` while passing a raw JSON parameters string.

Instead of these ADB commands, you can also use the [AppFunctions Testing Agent](https://github.com/android/appfunctions) to inspect your configuration, list and execute AppFunctions, and even see how your AppFunctions behave in a real conversational flow.

## Wrapping it up

When thinking about app features that can be contributed to the intelligence system using AppFunctions requires a slight shift in how we think about code and documentation. AppFunctions enable you to use this new interaction model for apps, which allows using an agent to access app features..

First, the [AppFunctions development skill](https://github.com/android/skills/tree/main/device-ai/appfunctions) is an essential lifecycle tool, helping you discover features, implement and refine AppFunctions for your apps. Second, KDoc comments are a compiled API asset; clear parameter descriptions directly impact the execution accuracy of the system agent. Finally, Android MCP provides local-first execution allowing apps to safely collaborate with AI agents.

Contributing app features through AppFunctions makes your application ready for the intelligence system. Let us know how you are adapting your apps for the agentic era!

## Learn more

Check out the other parts of this blog post series:  
[**Part 1:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html) Introduction of the app and a high-level overview.  
[**Part 2:**](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html) On-device intelligence. Deep-dive into ML Kit's GenAI APIs and Gemini Nano to build privacy-first features like itinerary summarization, receipt parsing, and local audio processing.  
[**Part 3:**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-cloud-hybrid-inference.html) Hybrid and cloud reasoning. Explore how to use Firebase AI Logic to ground LLM answers in real-world data like Google Maps and web context.  
[**Part 4 (this post!):**](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html) System integration. Integrating with the Android intelligence system using AppFunctions.  
Part 5 (coming soon): In-app agentic workflows. Extend the app with an end-to-end booking assistant powered by A2UI and ADK.

Interested in more on Android Development? Follow Android Developers on [YouTube](https://www.youtube.com/@AndroidDevelopers) or [LinkedIn](https://www.linkedin.com/showcase/androiddev/)!

All code snippets in this blog post follow the following copyright notice:

```
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
```
- [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
Written by:

-

  ## [Ben Weiss](https://developer.android.com/blog/authors/ben-weiss)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/ben-weiss) ![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp) ![View Ben Weiss's profile](https://developer.android.com/static/blog/assets/1_1_U4_K_Lr4r_A_Kx_Pq0_Crp_L3vr_Q_a4d1920594_2dcD9g.webp)
Continue reading
- [![View Caren Chang's profile](https://developer.android.com/static/blog/assets/Caren_Chang_e58d793559_1i40VV.webp)](https://developer.android.com/blog/authors/caren-chang) 22 Jul 2026 22 Jul 2026 ![](https://developer.android.com/static/blog/assets/0625_Building_Jet_Packer_with_Intelligent_On_Device_features_Strapi_v02_3f5a8b17b0_1UrFxh.webp) [How-tos](https://developer.android.com/blog/categories/how-tos)

  ## [Build intelligent Android apps: On-device inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-on-device-inference) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our previous post we introduced Jetpacker, the demo app we'll use throughout this series.
  [Caren Chang](https://developer.android.com/blog/authors/caren-chang) • 6 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps)
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
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1PnraM.webp)