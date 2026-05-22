---
title: https://developer.android.com/ai/adk
url: https://developer.android.com/ai/adk
source: md.txt
---

<br />

The [Agent Development Kit](https://adk.dev) (ADK) for Android library lets you
build and integrate sophisticated AI agents directly into your Android apps. ADK
is an open-source developer framework for building AI-powered agents that run
locally, on hosted services, and on Android mobile devices. The framework
supports Kotlin and Java programming languages, allowing you to start building
quickly agents and scale up to complex, multi-agent applications.

The ADK for Android library provides specialized dependencies and runtime
support tailored for mobile environments. You can build agents that execute AI
models on-device using Gemini Nano using ML Kit GenAI APIs, allowing you to create
privacy-focused and low-latency AI experiences that can function without network
access.

## Use ADK Kotlin in Android projects

You can use the ADK Kotlin agent API to build AI agents that run inside Android
apps. The agent code you write is identical to the ADK Kotlin
[Get started](https://adk.dev/get-started/kotlin/) guide. The differences are the Gradle dependency,
the project configuration, and how you invoke the agent at runtime.

### Prerequisites

The ADK for Android library has the following development requirements:

- [Android Studio](https://developer.android.com/studio)
- Android SDK (compileSdk 34 or higher, minSdk 24 or higher)

### Configure your Android project

In your Android project's `build.gradle.kts`, add the ADK Android dependency
and the KSP annotation processor:

    plugins {
        id("com.android.application")
        kotlin("android")
        id("com.google.devtools.ksp") version "2.1.20-2.0.1"
    }

    android {
        namespace = "com.example.agent"
        compileSdk = 34

        defaultConfig {
            applicationId = "com.example.agent"
            minSdk = 24
            targetSdk = 34
        }
    }

    dependencies {
        implementation("com.google.adk:google-adk-kotlin-core-android:0.1.0")
        ksp("com.google.adk:google-adk-kotlin-processor:0.1.0")
    }

    kotlin {
        jvmToolchain(17)
    }

> [!IMPORTANT]
> **Important:** This dependency configuration *replaces* the JVM dependency. Android projects use `google-adk-kotlin-core-android` instead of `google-adk-kotlin-core`. Do not add both. The Android artifact includes the full ADK agent API along with Android-specific model support.

### Define your agent

The agent code is identical to the ADK [Kotlin Quickstart](https://adk.dev/get-started/kotlin/#define-the-agent-code). The
`HelloTimeAgent` code example with the `@Tool`, `@Param`, and
`.generatedTools()` syntax works without modification on Android:

    package com.example.agent
    import com.google.adk.kt.agents.Instruction
    import com.google.adk.kt.agents.LlmAgent
    import com.google.adk.kt.annotations.Param
    import com.google.adk.kt.annotations.Tool
    import com.google.adk.kt.models.Gemini
    class TimeService {
        /** Mock tool implementation */
        @Tool
        fun getCurrentTime(
            @Param("Name of the city to get the time for") city: String
        ): Map<String, String> {
            return mapOf("city" to city, "time" to "The time is 10:30am.")
        }
    }
    object HelloTimeAgent {
        @JvmField
        val rootAgent = LlmAgent(
            name = "hello_time_agent",
            description = "Tells the current time in a specified city.",
            model = Gemini(
                name = "gemini-flash-latest",
                apiKey = System.getenv("GOOGLE_API_KEY")
                    ?: error("GOOGLE_API_KEY environment variable not set."),
            ),
            instruction = Instruction(
                "You are a helpful assistant that tells the current time in a city. "
                    + "Use the 'getCurrentTime' tool for this purpose."
            ),
            tools = TimeService().generatedTools(),
        )
    }

> [!WARNING]
> **Warning:** Do not embed API keys in client apps or include your API key in a published application. For production use cases, call cloud models through your own backend service or through [Firebase AI Logic](https://firebase.google.com/docs/ai-logic) so that API keys are never exposed in client code.

### Run the agent from your Android app

On Android-powered devices, use `InMemoryRunner` to invoke the agent and collect
responses from a coroutine, as shown in the following code example:

    import com.google.adk.kt.runners.InMemoryRunner
    import com.google.adk.kt.sessions.InMemorySessionService
    import com.google.adk.kt.types.Content
    import com.google.adk.kt.types.Part
    import com.google.adk.kt.types.Role
    import kotlinx.coroutines.CoroutineScope
    import kotlinx.coroutines.launch
    // Create a runner and session service
    val sessionService = InMemorySessionService()
    val runner = InMemoryRunner(
        agent = HelloTimeAgent.rootAgent,
        sessionService = sessionService,
    )
    // Call the agent from a coroutine (e.g. in a ViewModel or Activity)
    scope.launch {
        runner.runAsync(
            userId = "user-123",
            sessionId = "session-123",
            newMessage = Content(
                role = Role.USER,
                parts = listOf(Part(text = "What time is it in New York?")),
            ),
        ).collect { event ->
            val text = event.content?.parts?.firstOrNull()?.text
            if (!text.isNullOrBlank()) {
                // Update your UI with the agent's response
            }
        }
    }

## On-device models with Gemini Nano

The ADK for Android artifact includes support for on-device inference using
[Gemini Nano](https://developer.android.com/ai/gemini-nano) through ML Kit GenAI API. This approach allows agents to run
without network access, keeping data on the device.

To use an on-device model, create a `GenaiPrompt` model instead
of `Gemini`, as shown in the following code example:

    import com.google.adk.kt.models.mlkit.GenaiPrompt
    import com.google.mlkit.genai.prompt.GenerativeModel
    // Create an ML Kit GenerativeModel for on-device inference
    val generativeModel: GenerativeModel = // ... initialize using ML Kit
    val onDeviceModel = GenaiPrompt.create(
        generativeModel = generativeModel,
        name = "gemini-nano",
    )
    val agent = LlmAgent(
        name = "on_device_agent",
        model = onDeviceModel,
        instruction = Instruction("You are a helpful assistant."),
    )

You can also combine cloud and on-device models in a multi-agent system: use a
cloud-based `Gemini` for the root orchestrator and on-device `GenaiPrompt`
models for sub-agents that handle privacy-sensitive tasks. For more on this
pattern, see the ADK for Kotlin and Android [blog post](https://developers.googleblog.com/adk-kotlin-android-building-ai-agents/).

For a complete working Activity and more examples, see the ADK Kotlin examples
on [GitHub](https://github.com/google/adk-kotlin/tree/main/examples).