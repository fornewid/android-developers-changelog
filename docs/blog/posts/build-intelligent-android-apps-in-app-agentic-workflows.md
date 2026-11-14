---
title: https://developer.android.com/blog/posts/build-intelligent-android-apps-in-app-agentic-workflows
url: https://developer.android.com/blog/posts/build-intelligent-android-apps-in-app-agentic-workflows
source: md.txt
---

> Documentation index: https://developer.android.com/blog/llms.txt

[How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

# Build intelligent Android apps: In-app agentic workflows

9 min read ![](https://developer.android.com/static/blog/assets/0817_Booking_assistant_agentic_cloud_Strapi_36710f6e0c_hrRjy.webp) 28 Sep 2026 [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp)](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) Developer Relations Engineer Welcome back to the blog post series "Build intelligent Android apps" where you take a basic Android app and transform it into a personalized, intelligent, and agentic experience. In our [previous post](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html) you learned how to connect to the intelligence system using AppFunctions.

In this post, you will learn how to build autonomous **in-app agentic workflows** running in the cloud.
[Video](https://www.youtube.com/watch?v=_iuXykdlTkk)

Sometimes a task is too complex for a single device session. For example, booking a complete holiday itinerary involves coordinating flight times, selecting hotel rooms, reserving museum tickets, and planning restaurant reservations. If you run this multi-step process directly on a mobile device, the app might get closed and lose your progress. Managing all these steps and API credentials on a phone also gets complicated quickly.

For these long-running, multi-step workflows, you can use a custom self-hosted backend. The backend executes the booking agents in the background, while the Android app connects to the session, visualizes the progress, and requests user input only when necessary.

Using a cloud-hosted agentic backend offers a few advantages:

- **Background execution:**Booking agents run autonomously in the cloud, so progress is never lost if the mobile app goes to the background or loses internet connectivity.
- **Complex multi-agent orchestration:** A coordinator agent can delegate bookings to specialized subagents and handle dependencies between them.
- **Client-agnostic UI rendering:**The backend describes the interface structure dynamically, letting you update the UI layout without releasing a new client version.

![booking-assistant.png](https://developer.android.com/static/blog/assets/booking_assistant_af7122459f_Z1hi27t.webp) The booking assistant shows all booking progress, organized by event type.

With these benefits in mind, we added a **Booking Assistant** to [Jetpacker](https://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-introduction-jetpack.html) that coordinates flights, hotels, museums, and restaurant reservations. Let's look at how we orchestrated a multi-agent system powered by the Agent Development Kit (ADK), with the Agent-User Interaction protocol(AG-UI) and Agent-to-User Interface protocol (A2UI) to send and display interactive cards natively in Jetpack Compose.

### Powering complex workflows with ADK agents

Rather than coordinating the orchestration flow manually using custom REST endpoints or complex web sockets, you can use the [**Agent Development Kit (ADK)**](http://adk.dev/). With ADK, you can define agents and equip them with python function tools to query databases and execute bookings.
![diagram.png](https://developer.android.com/static/blog/assets/diagram_538369031d_Z9CqT1.webp) The Android app sends the current trip itinerary data to the server. The coordinator agent chooses which subagents to trigger. Each subagent provides its results to a shared session queue that streams the results back to the Android app.

Here is how to define a simple agent and run it using ADK:

```
# server/main.py

# Note: ADK supports many different coding languages. For now, we use the Python version as it includes support for A2UI which we'll use later in this blog post.

from google.adk import Agent
from google.adk.runners import InMemoryRunner
from google.adk.tools import FunctionTool

# Define custom tools to interact with database
def search_flights(destination: str, date: str) -> list[str]:
    # In production, here you would query our flight database and return dynamic results
    return ["10:00 AM", "2:00 PM"]

def reserve_flight(flight_time: str) -> str:
    # In production, here you would save the reservation transaction
    return "Reserved flight at " + flight_time

# Instantiate the booking agent with specialized tools
flight_agent = Agent(
    name="Flight Booker",
    model="gemini-3.1-flash-lite",
    instruction="Help the user search for flights and book a reservation.",
    tools=[
        FunctionTool(search_flights),
        FunctionTool(reserve_flight, require_confirmation=True)
    ]
)

# Run the agent in memory using a session ID
runner = InMemoryRunner(flight_agent)
async for event in runner.run_async(user_id=user_id, session_id=session_id):
    if event.content:
        print("Agent said:", event.content)
```

When you run an agent using this setup, ADK manages the execution steps for you. It automatically tracks the conversation context, routes messages between the user and the model, and executes the registered tools when the model requests them. This allows you to focus on writing clean procedural logic while the framework handles the orchestration in the background.
![web_debug.png](https://developer.android.com/static/blog/assets/web_debug_aeb22204ff_Z11Alg4.webp)

<br />

To connect this backend agent to our Jetpacker app, the server needs a way to stream updates in real time to the device, which is handled using the **AG-UI protocol** . The agent also needs a structured way to describe and update interactive components (like option selectors and seating grids) dynamically on the phone, which is where the **A2UI protocol** comes in.

### Standardizing agent-client communication with AG-UI

Running agents in the cloud and rendering UI on Android requires a standard communication channel. For this, you will use the [AG-UI](https://ag-ui.com/) protocol.

AG-UI is a bidirectional transport layer protocol that standardizes message types between agents and UI clients. The agent can inform the client of lifecycle events, text messages, tool calls, and state management. The client, in turn, can send user text messages, tool call results, and custom action events back to the agent.

On the server side, it yields updates formatted as standard Server-Sent Events (like `event: TEXT_MESSAGE_CONTENT` containing the JSON delta). On Android, the Kotlin SDK listens to this stream and automatically maps the payloads to type-safe client events:

```kotlin
// BookingAssistantViewModel.kt

import com.agui.client.agent.HttpAgent
import com.agui.client.agent.HttpAgentConfig
import com.agui.core.types.RunAgentInput
import com.agui.core.types.UserMessage
import com.agui.core.types.TextMessageStartEvent
import com.agui.core.types.TextMessageContentEvent
import com.agui.core.types.TextMessageEndEvent

val config = HttpAgentConfig(
    agentId = "booking-assistant",
    threadId = threadId,
    url = "https://<your-backend-url>"
)
val agent = HttpAgent(config, httpClient)

// Set up the input with the session thread and user instruction
val input = RunAgentInput(
    threadId = threadId,
    runId = runId,
    messages = listOf(UserMessage("Book a flight to Paris"))
)

// Run the agent flow and collect lifecycle events
agent.runAgentObservable(input)
    .collect { event ->
        when (event) {
            is TextMessageStartEvent -> { /* ... */ }
            is TextMessageContentEvent -> { /* ... */ }
            is TextMessageEndEvent -> {
                // Handle the completed message
            }
        }
    }
```

You can then write a UI to render these different types of standardized AG-UI events. This will give you the prototypical "Chatbot" experience:
![manage_bookings.png](https://developer.android.com/static/blog/assets/manage_bookings_7f57defae9_1KcBWQ.webp) A basic interface that lets a user chat with an assistant.

### Letting the agent speak UI with A2UI

Traditional chatbots typically return plain text or custom JSON payloads. When building complex interfaces, the client application has to parse these payloads and map them to specific, pre-built screens. This creates a dependency: every time you add a new feature, change the layout, or support a new user interaction, you have to update both the backend agent and the mobile application. This requires publishing an app update and waiting for users to install it.

To solve this, use the [A2UI](http://a2ui.org/) protocol. A2UI allows agents to describe the UI components to render on the client dynamically. The client app declares a catalog of components it supports, and the server sends a JSON payload specifying the component layout and properties:

```
{
  "version": "v0.9",
  "updateComponents": {
    "surfaceId": "Flight Reservation",
    "components": [
      {
        "id": "flight_option_picker",
        "component": "InteractiveOptionPicker",
        "properties": {
          "prompt": "Select a flight time:",
          "options": [
            "10:00 AM",
            "2:00 PM"
          ],
          "selectedIdx": null,
          "confirmBtnText": "Confirm Flight"
        }
      }
    ]
  }
}
```

The server specifies which catalog components to render along with their active property values, cleanly decoupling the client's visual implementation details from the agent's workflow state.

### Designing the backend UI schema

For the agent to generate these JSON payloads correctly, it needs to know which components are available and what properties they accept.

To do this, use the [ADK A2UI integration](https://adk.dev/integrations/a2ui/). Instead of manually writing prompt instructions for every component in our catalog, the [A2uiSchemaManager](https://github.com/a2ui-project/a2ui/blob/v0.9/agent_sdks/python/src/a2ui/core/schema/manager.py#L28) compiles their JSON schemas and layout instructions directly into the system prompt. This ensures the model learns the exact structure and formatting rules it must follow to generate valid A2UI payloads:

```
# server/main.py

from a2ui.schema.manager import A2uiSchemaManager
from a2ui.schema.constants import VERSION_0_9
from a2ui.schema.catalog import CatalogConfig
from a2ui.basic_catalog.provider import BasicCatalog

# Initialize A2UI Schema Manager with custom booking component catalog
schema_manager = A2uiSchemaManager(
    version=VERSION_0_9,
    catalogs=[
        BasicCatalog.get_config(version=VERSION_0_9),
        CatalogConfig.from_path(
            name="https://example.com/catalogs/booking_assistant/v1/catalog.json",
            catalog_path="booking_catalog.json"
        )
    ]
)

# Compile prompt instructions including the A2UI JSON schema
A2UI_SYSTEM_INSTRUCTION = schema_manager.generate_system_prompt(
    role_description="You are a helpful travel booking assistant.",
    ui_description="Use InteractiveOptionPicker for choices, SeatSelectionPicker for seat selection...",
    include_schema=True,
    include_examples=True,
    allowed_components=["InteractiveOptionPicker", "SeatSelectionPicker", "BookingStatus"]
)
```

With this generated system instruction, the LLM is grounded in the schema layout and knows exactly how to formulate component updates that the Android client is capable of rendering.

### Natively rendering A2UI with Jetpack Compose

To render these component trees natively on Android, use the new Jetpack Compose A2UI Renderer library.

First, add the dependencies to our module's `build.gradle.kts` file:

```kotlin
// android/feature/trip/booking_assistant/build.gradle.kts
dependencies {
    implementation("androidx.a2ui:a2ui-model:1.0.0-alpha01")
    implementation("androidx.a2ui.compose:compose-runtime:1.0.0-alpha01")
    implementation("androidx.a2ui.compose:compose-ui:1.0.0-alpha01")
    implementation("androidx.compose.material3:material3-a2ui:1.0.0-alpha01")
}
```

Each component class in the catalog (such as `BookingStatusComponent`) defines how to map the properties received from the JSON payload into a Jetpack Compose composable function.

Register the custom components in a catalog:

```kotlin
// CustomBookingAssistantCatalog.kt

import androidx.a2ui.compose.ui.A2uiCatalog

fun bookingAssistantCatalog(): A2uiCatalog {
    return A2uiCatalog(
        catalogId = "https://example.com/catalogs/booking_assistant/v1/catalog.json",
        components = listOf(
            InteractiveOptionPickerComponent(),
            SeatSelectionPickerComponent(),
            BookingStatusComponent()
        )
    )
}
```

Tip: Jetpacker implements custom components (`InteractiveOptionPicker`, `SeatSelectionPicker`, `BookingStatus`) tailored for booking flows. If your agent uses standard elements (such as text, cards, buttons, rows, columns, checkboxes, and date-time pickers), `material3-a2ui` also provides `materialA2uiBasicCatalogV1(...)`, giving you ready-to-use Material 3 implementations without writing any custom components.

Note: To keep the backend and mobile client aligned, both rely on the same catalog definition ID (`https://example.com/catalogs/booking_assistant/v1/catalog.json`). If you add or modify properties on the backend catalog, you must increase the version number, and update the matching Kotlin component class to prevent parsing errors.

In the `BookingAssistantViewModel`, process the A2UI messages using the `A2uiMessageProcessor` and update our active surfaces:

```kotlin
// BookingAssistantViewModel.kt
import androidx.lifecycle.ViewModel
import androidx.a2ui.model.processor.A2uiSurfaceModel
import androidx.a2ui.compose.ui.A2uiMessageProcessor
import kotlinx.coroutines.flow.StateFlow

class BookingAssistantViewModel : ViewModel() {
    private val messageProcessor = A2uiMessageProcessor(
        catalogs = listOf(bookingAssistantCatalog())
    )
    val activeSurfaces: StateFlow<List<A2uiSurfaceModel>> = messageProcessor.activeSurfaces
    
    init {
        viewModelScope.launch(Dispatchers.Default) { processor.collectMessages() }
    }

    // ...
}
```

In the Compose screen, collect these surfaces and render each one using the official `A2uiSurface` composable from `androidx.compose.material3:material3-a2ui`. A2uiSurface automatically handles reactive component state observation, Material 3 loading indicators, error fallbacks, and animated transitions between updates:

```kotlin
// BookingAssistantScreen.kt
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.a2ui.A2uiSurface

@Composable
fun BookingAssistantScreen(
    viewModel: BookingAssistantViewModel,
    modifier: Modifier = Modifier
) {
    val activeSurfaces by viewModel.activeSurfaces.collectAsState()
    LazyColumn(
        modifier = modifier.fillMaxWidth(),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        items(activeSurfaces) { surfaceModel ->
            Card(modifier = Modifier.fillMaxWidth()) {
                A2uiSurface(
                    surfaceModel = surfaceModel,
                    modifier = Modifier.fillMaxWidth().wrapContentHeight()
                )
            }
        }
    }
}
```

You will now see several UI surfaces generated by our agent running in the backend:
![booking-assistant.png](https://developer.android.com/static/blog/assets/booking_assistant_af7122459f_Z1hi27t.webp) A well-designed booking assistant that relies on UI instead of text to interact with the user.

### Bringing it all together

By hosting agent workflows in the cloud and using the AG-UI and A2UI protocols together, we can build dynamic, native Android interfaces driven directly by AI models. AG-UI establishes the real-time bidirectional streaming channel for messages and lifecycle events, while A2UI enables the cloud agent to dynamically describe interactive UI components, keeping the client application perfectly decoupled from the step-by-step backend orchestration logic.

Check out the full source code for [Jetpacker on GitHub](https://github.com/android/ai-samples/tree/main/jetpacker), and watch the video [Build Intelligent Android apps with Google's AI](https://www.youtube.com/watch?v=_iuXykdlTkk) to learn more about how to integrate agentic workflows directly into your app.

Check out the other parts of this blog post series:  
▪️ [Part 1](https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker.md.txt): Introduction of the app and a high-level overview.  
📱 [Part 2](http://android-developers.googleblog.com/2026/07/android-on-device-inference.html): On-device intelligence. Dive deep into ML Kit's GenAI APIs and Gemini Nano to build privacy-first features like itinerary summarization, receipt parsing, and local audio processing.  
☁️ [Part 3](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference.md.txt): Hybrid and cloud reasoning. Explore how to use Firebase AI Logic to ground LLM answers in real-world data like Google Maps and web context.  
⚙️ [Part 4](http://android-developers.googleblog.com/2026/07/build-intelligent-android-apps-appfunctions.html): System integration. Integrating with the Android intelligence system using AppFunctions.  
🤖 Part 5 (this post!): In-app agentic workflows. Extend the app with end-to-end booking assistants powered by A2UI and ADK.

Interested in more on Android Development? Follow Android Developers on [YouTube](https://www.youtube.com/@AndroidDevelopers) or [LinkedIn](https://www.linkedin.com/showcase/androiddev/)!

All code snippets in this blog post follow the following copyright notice:

```
Copyright 2026 Google LLC.
SPDX-License-Identifier: Apache-2.0
```
- [#Android intelligence](https://developer.android.com/blog/topics/android-intelligence.md.txt)
Written by:

-

  ## [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt)

  ###### Developer Relations Engineer

  [read_more
  View profile](https://developer.android.com/blog/authors/jolanda-verhoef) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp) ![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp)
Continue reading
- [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp)](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) 21 Jul 2026 21 Jul 2026 ![](https://developer.android.com/static/blog/assets/0713_Jetpacker_Strapi_d07d6f2d4b_Z2d3f6n.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Build intelligent Android apps: Introduction to Jetpacker](https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-introduction-to-jetpacker.md.txt) Jetpacker is a technical showcase app that our team built from the ground up for this year's Google I/O (built using Antigravity). At its core, Jetpacker helps users plan, explore, and enjoy their next big adventure.
  [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) • 4 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps.md.txt)
- 3 Authors 21 Jul 2026 21 Jul 2026 ![](https://developer.android.com/static/blog/assets/features_in_Jetpacker_Features_with_Firebase_AI_Logic_Strapi_0a6fbb7edb_28oUwB.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Build intelligent Android apps: Cloud and hybrid inference](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/build-intelligent-android-apps-cloud-and-hybrid-inference.md.txt) Welcome back to the blog post series "Build intelligent Android apps" where we take a basic Android app and transform it into a personalized, intelligent, and agentic experience.
  [Thomas Ezan](https://developer.android.com/blog/authors/thomas-ezan.md.txt), [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt), [Caren Chang](https://developer.android.com/blog/authors/caren-chang.md.txt) • 8 min read
  - [#Intelligent Apps](https://developer.android.com/blog/topics/intelligent-apps.md.txt)
- [![View Jolanda Verhoef's profile](https://developer.android.com/static/blog/assets/jolanda_b0e2beee3e_1gwMmp.webp)](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) 23 Jan 2025 23 Jan 2025 ![](https://developer.android.com/static/blog/assets/camera_X_Jetpack_09bc5a0414_1xSUVV.webp) [How-tos](https://developer.android.com/blog/categories/how-tos.md.txt)

  ## [Create a spotlight effect with CameraX and Jetpack Compose](https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose.md.txt)

  [arrow_forward](https://developer.android.com/blog/posts/create-a-spotlight-effect-with-camera-x-and-jetpack-compose.md.txt) In this post, we'll dive into something a bit more visually engaging --- implementing a spotlight effect on top of our camera preview, using face detection as the basis for the effect.
  [Jolanda Verhoef](https://developer.android.com/blog/authors/jolanda-verhoef.md.txt) • 8 min read
  - [#Android](https://developer.android.com/blog/topics/android.md.txt)
  - [#Compose](https://developer.android.com/blog/topics/compose.md.txt)
  - [#Mobile App Development](https://developer.android.com/blog/topics/mobile-app-development.md.txt)
  - +1 ↩
Stay in the loop


Get the latest Android development insights delivered to your inbox
weekly.
[mail
Subscribe](https://developer.android.com/subscribe) ![A 3D illustration of the Android mascot, wearing a jetpack that's emitting a large cloud of bubbles](https://developer.android.com/static/blog/assets/rocket-android.CVJQZOf1_1zVtXW.webp)