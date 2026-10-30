---
title: https://developer.android.com/ai/gemini-nano/mlkit-agent-api
url: https://developer.android.com/ai/gemini-nano/mlkit-agent-api
source: md.txt
---

With ML Kit's on-device [agentic workflows](https://developers.google.com/machine-learning/glossary#agentic-workflow) (`com.google.mlkit:genai-agent`,
available through the [AICore Developer Preview program](https://developers.google.com/ml-kit/genai/aicore-dev-preview)), you can build
autonomous, multi-turn conversational agents powered by Gemini Nano and the
Android AICore system service.

> [!CAUTION]
> **Caution:** Agentic workflows and tool calling rely on generative AI model predictions, which might not always suggest the correct tool or arguments. You are responsible for the safety and quality of any outputs generated or actions taken based on model tool predictions.

Built on top of the `GenerativeModel` class, which provides
[direct model access](https://developers.google.com/ml-kit/genai/prompt/android), the `AgentRunner` class automates complete
[agentic loops](https://developers.google.com/machine-learning/glossary#agentic-loop): planning multi-step actions, invoking typed tools (such as
querying an app repository, calling a backend API, or reading a local database),
evaluating tool results, and managing conversational context locally on-device
with zero network latency and full user privacy. While the `GenerativeModel` class
supports client-managed multi-turn history using a `List<Content>` object (with
`USER` and `MODEL` roles) and a `sessionId` value, the `AgentRunner` class
provides managed multi-turn sessions (using the `AgentSession` interface) that
record in-memory conversation history automatically across turns so that you
don't have to manage transcripts manually. Static tool declarations and system
instructions are also automatically cached on-device, reducing
time-to-first-token latency without extra configuration.

## Core components

- **The `Agent` class** : Declares instructions, available tools, and execution guardrails using the `Agent.builder()` method. Defaults to `maxTurns = 10` automatically.
- **The `AgentRunner` class** : Built on top of the `GenerativeModel` class, orchestrating autonomous reasoning loops and managed sessions with on-device models. Main-safe by default on `Dispatchers.IO`, with `temperature` defaulting to `null` (which defers to the model's default; pass `temperature = 0.0f` for greedy decoding).
- **The `AgentSession` interface** : Scoped multi-turn conversation session handle obtained using the `runner.getOrCreateSession(sessionId)` method that records in-memory conversation history automatically across turns, with the `runAsync(content)` and `close()` methods.
- **The `AgentEvent` interface** : The reactive Kotlin `Flow` stream emitting text tokens and tool updates.
- **The `AgentTool` class** : Typed functions callable by the model, defined using Android AppFunctions (`@AppFunctionDeclaration`).
- **The `GenAiException` class** : Typed exception hierarchy (`com.google.mlkit.genai.common.GenAiException`) signaling failure states such as `MAX_TURNS_EXCEEDED`, `NOT_AVAILABLE`, or `BUSY`.


## Android skills

[View on GitHub](https://github.com/android/skills/tree/main/device-ai/mlkit-agent-api)

### Use the ML Kit Agent API

Use an [Android skill](https://developer.android.com/tools/agents/android-skills) to build autonomous on-device agentic workflows in your app. To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli), run:

    android skills add mlkit-agent-api

<br />

## Prerequisites and dependencies

Ensure your development environment and Gradle configuration meet the following
requirements before integrating the Agent API.

### Platform and hardware requirements

- **Android version** : Android 14 (API level 34) or higher enrolled in the [AICore Developer Preview program](https://developers.google.com/ml-kit/genai/aicore-dev-preview).
- **Supported devices** : For a list of supported devices and their Gemini Nano model versions, see [Custom generation and agent device support](https://developers.google.com/ml-kit/genai#prompt-device).
- **Minimum SDK** : `minSdk 26` or higher.
- **Kotlin**: Kotlin 2.3 or higher.

### Gradle configuration

Add the `genai-agent` dependency to your module's `build.gradle.kts` file:

    dependencies {
        // Gemini Nano agentic workflows
        implementation("com.google.mlkit:genai-agent:1.0.0-alpha1")

        // Optional: Only required when defining tools using Android AppFunctions
        implementation("androidx.appfunctions:appfunctions:1.0.0-alpha13")
        ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-alpha13")
    }

While `genai-agent` itself does not require an annotation processor or compiler
plugin, defining tools with `androidx.appfunctions` requires the
`appfunctions-compiler` KSP plugin.

> [!NOTE]
> **Note:** The `AgentRunner.runSingleTurnAsync()` and `AgentSession.runAsync()` methods are main-safe by contract. Heavy tensor computations on the NPU or GPU run on background threads internally, so you can safely collect response flows directly in a ViewModel or Compose UI without manual `flowOn(Dispatchers.IO)`.

### Quickstart: Initialize an agent

The following code sample shows how to instantiate an on-device agent and runner:

    import com.google.mlkit.genai.agent.Agent
    import com.google.mlkit.genai.agent.AgentRunner

    // Configure the agent with system instructions
    val agent = Agent.builder()
        .setInstructions("You are a helpful on-device assistant.")
        .build()

    // Create the runner to execute prompts
    val runner = AgentRunner(agent)

## Define tools

The model can call typed tools to query app data, communicate with backend
services, or trigger in-app actions. Tools are defined declaratively using
Android AppFunctions (`androidx.appfunctions`):

    package com.example.ai.agent.tools

    import androidx.appfunctions.AppFunctionDeclaration
    import androidx.appfunctions.AppFunctionSerializable
    import androidx.appfunctions.AppFunctionService
    import androidx.appfunctions.AppFunctionServiceEntryPoint
    import kotlinx.coroutines.Dispatchers
    import kotlinx.coroutines.withContext

    @AppFunctionSerializable
    data class OrderDetails(
        val orderId: String,
        val status: String,
        val eta: String,
    )

    @AppFunctionServiceEntryPoint(
        serviceName = "OrderAppFunctionService",
        appFunctionXmlFileName = "order_app_functions",
    )
    abstract class OrderTools : AppFunctionService() {

        /**
         * Fetches details and delivery status for an in-app order.
         *
         * @param orderId The alphanumeric order identifier
         */
        @AppFunctionDeclaration(isDescribedByKDoc = true)
        suspend fun fetch_order_details(
            orderId: String
        ): OrderDetails = withContext(Dispatchers.IO) {
            // Query local database or call your backend API
            OrderDetails(
                orderId = orderId,
                status = "Out for delivery",
                eta = "2:30 PM",
            )
        }
    }

Register the generated service in your app's `AndroidManifest.xml` file:

    <service
        android:name=".OrderAppFunctionService"
        android:permission="android.permission.BIND_APP_FUNCTION_SERVICE"
        android:exported="true">
        <property
            android:name="android.app.appfunctions.schema"
            android:value="app_functions_schema.xsd" />
        <property
            android:name="android.app.appfunctions.v2"
            android:value="order_app_functions.xml" />
        <intent-filter>
            <action android:name="android.app.appfunctions.AppFunctionService" />
        </intent-filter>
    </service>

### Restrict caller access with the `ACCESS_LEVEL_SELF` constant

AppFunctions don't have to be public to the system or external callers. In
Android, access control is handled through caller access levels rather than
inspecting caller identities.

By default (using the `ACCESS_LEVEL_ANDROID_TRUSTED` constant), AppFunctions can
be called by platform-certified on-device assistants holding the
`EXECUTE_APP_FUNCTIONS` system permission. If your tool is strictly intended for
your app's internal agent (for example, managing user carts or private database
records), restrict caller access using the `ACCESS_LEVEL_SELF` constant:

    import androidx.appfunctions.AppFunctionAccessLevel
    import androidx.appfunctions.AppFunctionDeclaration
    import androidx.appfunctions.AppFunctionService
    import androidx.appfunctions.AppFunctionServiceEntryPoint
    import androidx.appfunctions.ExperimentalAppFunctionsApi
    import androidx.appfunctions.metadata.AppFunctionMetadata

    @AppFunctionServiceEntryPoint(
        serviceName = "OrderAppFunctionService",
        appFunctionXmlFileName = "order_app_functions",
    )
    abstract class OrderTools : AppFunctionService() {

        /**
         * Cancels an order. Restricted strictly to this app's internal agent.
         */
        @OptIn(ExperimentalAppFunctionsApi::class)
        @AppFunctionDeclaration(isDescribedByKDoc = true)
        @AppFunctionAccessLevel(
            level = AppFunctionMetadata.ACCESS_LEVEL_SELF,
            isCompatEnforcementEnabled = true,
        )
        fun cancel_order(
            orderId: String
        ): String {
            // Only your app's internal agent can invoke this function
            return "Order $orderId cancelled successfully."
        }
    }

When restricted with the `ACCESS_LEVEL_SELF` constant, the platform blocks
external surfaces and system assistants from discovering or executing the
function over IPC.

## Configure the agent

Configure an `Agent` instance with system instructions and enable AppFunctions,
then initialize the `AgentRunner` instance:

    import com.google.mlkit.genai.agent.Agent
    import com.google.mlkit.genai.agent.AgentRunner

    // Configure the agent with system instructions and enable AppFunctions
    val agent = Agent.builder()
        .setName("OrderAssistant")
        .setInstructions(
            "You are a helpful assistant for looking up store orders. " +
            "Use available tools to fetch order information."
        )
        .enableAppFunctions(true) // Automatically discovers all registered AppFunctions in your app
        .build()

    // Initialize the runner
    val runner = AgentRunner(agent)

Optionally, call the `addAppFunctionIds("fetch_order_details", "cancel_order")`
method to scope discovery strictly to specific AppFunction IDs instead of
exposing all in-app functions.

### Agent defaults

- **Turn limits** : The `Agent.Builder` class defaults `maxTurns = 10` automatically as a [termination condition](https://developers.google.com/machine-learning/glossary#termination_condition) to prevent infinite tool-calling loops. You don't need to call the `setMaxTurns(10)` method manually for standard conversational or tool-calling workflows.
- **Deterministic greedy decoding** : The `AgentRunner` class sets the default `temperature` parameter to `null`, deferring to the underlying model's default. For deterministic tool selection and JSON schema compliance on-device, pass `temperature = 0.0f` ([temperature](https://developers.google.com/machine-learning/glossary#temperature)) to the `AgentRunner` constructor. Avoid setting cloud-style temperatures (\> 0.4f), which increase [hallucination](https://developers.google.com/machine-learning/glossary#hallucination) risks and schema degradation on mobile models.

## Multi-turn execution and streaming events

> [!CAUTION]
> **Caution:** Don't store an `AgentSession` instance or `AgentRunner` instance directly in an `Activity` or `Fragment` component. When the screen rotates or a configuration change occurs, the `Activity` component is recreated, destroying all conversational state. Always hold sessions inside an AndroidX `ViewModel` class so history survives configuration changes. Call the `session.close()` method in the `ViewModel.onCleared()` method to release session memory when the screen is destroyed.

Obtain an `AgentSession` instance using the `runner.getOrCreateSession(sessionId)` method inside an
Android `ViewModel` class. The session returns a `Flow<AgentEvent>` stream emitting real-time
text tokens and tool execution updates:

    package com.example.ai.agent

    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import com.google.mlkit.genai.agent.AgentEvent
    import com.google.mlkit.genai.agent.AgentRunner
    import com.google.mlkit.genai.agent.AgentSession
    import com.google.mlkit.genai.common.GenAiException
    import com.google.mlkit.genai.prompt.Content
    import kotlinx.coroutines.flow.MutableStateFlow
    import kotlinx.coroutines.flow.StateFlow
    import kotlinx.coroutines.flow.asStateFlow
    import kotlinx.coroutines.flow.catch
    import kotlinx.coroutines.flow.update
    import kotlinx.coroutines.launch

    data class AgentUiState(
        val messages: List<String> = emptyList(),
        val currentResponse: String = "",
        val activeToolStatus: String? = null,
        val isLoading: Boolean = false,
        val errorMessage: String? = null
    )

    class ChatViewModel(
        private val runner: AgentRunner,
        private val sessionId: String = "chat_session"
    ) : ViewModel() {

        // Scoped session preserves conversation history across configuration changes (screen rotations)
        private val session: AgentSession = runner.getOrCreateSession(sessionId)

        private val _uiState = MutableStateFlow(AgentUiState())
        val uiState: StateFlow<AgentUiState> = _uiState.asStateFlow()

        fun sendMessage(userText: String) {
            _uiState.update {
                it.copy(
                    messages = it.messages + userText,
                    currentResponse = "",
                    activeToolStatus = null,
                    isLoading = true,
                    errorMessage = null
                )
            }

            viewModelScope.launch {
                val content = Content.builder().text(userText).build()
                session.runAsync(content)
                    .catch { e ->
                        val message = when {
                            e is GenAiException && e.errorCode == GenAiException.ErrorCode.MAX_TURNS_EXCEEDED ->
                                "Agent exceeded the maximum reasoning turns allowed."
                            e is GenAiException && e.errorCode == GenAiException.ErrorCode.NOT_AVAILABLE ->
                                "On-device AI is currently unavailable."
                            e is GenAiException && e.errorCode == GenAiException.ErrorCode.BUSY ->
                                "On-device AI is busy. Please try again."
                            else -> e.localizedMessage ?: "Agent error"
                        }
                        _uiState.update {
                            it.copy(
                                isLoading = false,
                                activeToolStatus = null,
                                errorMessage = message
                            )
                        }
                    }
                    .collect { event ->
                        when (event) {
                            is AgentEvent.TextMessage -> {
                                _uiState.update {
                                    it.copy(
                                        currentResponse = if (event.isPartial) {
                                            it.currentResponse + event.text
                                        } else {
                                            event.text.ifEmpty { it.currentResponse }
                                        },
                                        activeToolStatus = null
                                    )
                                }
                            }
                            is AgentEvent.FunctionCall -> {
                                _uiState.update {
                                    it.copy(activeToolStatus = "Executing ${event.name}...")
                                }
                            }
                            is AgentEvent.FunctionResponse -> {
                                _uiState.update {
                                    it.copy(activeToolStatus = "Received data from ${event.name}")
                                }
                            }
                            else -> {}
                        }
                    }

                // Finalize message once stream completes
                _uiState.update {
                    it.copy(
                        messages = it.messages + it.currentResponse,
                        currentResponse = "",
                        activeToolStatus = null,
                        isLoading = false
                    )
                }
            }
        }

        override fun onCleared() {
            super.onCleared()
            // Cleanly evicts conversation memory from RAM when ViewModel is destroyed
            session.close()
        }
    }

### Stream text tokens directly

For conversational interfaces where tool execution details don't need to be
displayed separately in the UI, use the `textTokens()` extension function on the
`Flow<AgentEvent>` interface:

    import com.google.mlkit.genai.agent.textTokens
    import com.google.mlkit.genai.prompt.Content

    val content = Content.builder().text("What is my order status?").build()
    session.runAsync(content)
        .textTokens()
        .collect { token ->
            print(token)
        }

## Single-turn execution

For one-off tasks where dialogue history shouldn't be retained in RAM (for
example, photo tagging or ephemeral text summarization), call the
`runner.runSingleTurnAsync(content)` method directly:

    // Ephemeral single-turn: cleans up session state from RAM automatically upon completion
    val content = Content.builder()
        .text("Summarize the order history for customer #1042: ...")
        .build()

    runner.runSingleTurnAsync(content)
        .textTokens()
        .collect { token ->
            displaySummary(token)
        }

When invoking the `runner.runSingleTurnAsync(content)` method directly, the `AgentRunner`
instance allocates an ephemeral session ID internally and automatically deletes the
conversation state from memory upon completion, preventing memory leaks.

## Session lifecycle and memory management

Multi-turn dialogue history is stored in memory and indexed by its `sessionId`
value:

- **Configuration changes** : Retaining the `AgentSession` instance inside an Android `ViewModel` class preserves conversation history across screen rotations automatically without plumbing strings on every turn.
- **Session eviction** : Call the `session.delete()` method to synchronously evict a session when a conversation thread is dismissed, or call the non-suspending `session.close()` method in the `ViewModel.onCleared()` method to free RAM.
- **Bulk eviction** : Call the `runner.deleteSession(sessionId)` method to free a specific session, or the `runner.clearAllSessions()` method to evict all cached conversations.
- **Runner lifecycle** : The `AgentRunner` class implements the `AutoCloseable` interface. When sharing a runner across screens, close individual `AgentSession` handles in each screen's `ViewModel.onCleared()` method, and call the `runner.close()` method when shutting down the runner completely.
- **Concurrent sessions** : A single `AgentRunner` instance can host multiple distinct sessions simultaneously. Each `sessionId` value maintains an isolated conversational history.

## Error handling with the `GenAiException` class

Runtime failures during agent execution, such as when the agent reaches maximum
tool turns without generating a response or when on-device AI is temporarily
unavailable, are emitted or thrown as a `GenAiException` exception
(`com.google.mlkit.genai.common.GenAiException`). Handle failures reactively
using the Kotlin Coroutines Flow `catch` operator:

    session.runAsync(content)
        .catch { e ->
            if (e is GenAiException) {
                when (e.errorCode) {
                    GenAiException.ErrorCode.MAX_TURNS_EXCEEDED -> {
                        // Turn limit exceeded
                    }
                    GenAiException.ErrorCode.NOT_AVAILABLE -> {
                        // Gemini Nano or AICore unavailable
                    }
                    GenAiException.ErrorCode.BUSY -> {
                        // System busy or rate limit reached
                    }
                    else -> {
                        // Other GenAiException errors
                    }
                }
            }
        }
        .collect { event ->
            // Process response events
        }

### Key error codes

- `GenAiException.ErrorCode.MAX_TURNS_EXCEEDED` (`-112`): The agent exceeded the maximum turn limit (the `maxTurns` limit) without generating a final response.
- `GenAiException.ErrorCode.NOT_AVAILABLE` (`8`): The Gemini Nano model or AICore system service isn't available or ready.
- `GenAiException.ErrorCode.BUSY` (`9`): System is busy or the calling app has exceeded its quota.