---
title: https://developer.android.com/ai/appfunctions/quality-guidelines
url: https://developer.android.com/ai/appfunctions/quality-guidelines
source: md.txt
---

AppFunctions are the practical equivalent of MCP servers on Android. They let
you share parts of your app's logic with AI agents and assistants.

Agents use descriptions to select the AppFunction that fulfills a request. This
selection process works like traditional MCP tool discovery, where AI
applications use MCP server and tool descriptions to guide their choices. Your
app acts as the Android MCP server, and each AppFunction acts as one of its
tools. Provide the following descriptions:

- **App description (the Android MCP server).** Your app description is the first entry point for agents to understand what your app can do. To help agents discover your app, lead with its primary domain and concisely list the tasks that your AppFunctions let it accomplish.
  - Write the app description yourself, in your app metadata XML file.
  - Use the app description to describe what individual function descriptions can't, such as the order in which to call functions.
- **AppFunction descriptions (the tools).** Each function description explains the behavior of one AppFunction. Function descriptions are generally structured around a verb, such as *update* , *create* , or *book* , and a resource, such as *settings* , *channel* , or *room*.

> [!IMPORTANT]
> **Important:** Agents might not read all of the text that you provide for discovery, such as app and function descriptions. How much they read depends on the agent, so put key information first and keep the text concise.

## Function description guidelines

Agents rely on function descriptions to decide which function fits a request
and how to call it.

### Write concise, unambiguous AppFunction descriptions

The less ambiguous a description is, the more reliably an agent can choose the
right function for a request. The following table lists what to do and what to
avoid in function descriptions:

| Do | Don't |
|---|---|
| Describe the function's purpose and the outcome of running it, in clear and neutral language. | Don't use descriptions as prompts. Commands such as "You MUST say" and "You must ask the user for" instruct the agent how to behave instead of describing the function. |
| Front-load descriptions with key information, and keep them concise. | Don't pad descriptions with filler, such as "This function is used to." Filler makes a description longer without making it clearer. |
| Accurately reflect what the code does, including its parameters and output. For example, a function described as read-only shouldn't write or delete data. | Don't use misleading names, such as a function named `fetchData` that deletes user data. |
| Write function descriptions in [KDoc format](https://kotlinlang.org/docs/kotlin-doc.html), including parameters and the return type. Follow the [Kotlin style guide](https://developer.android.com/kotlin/style-guide) for naming, and make descriptions understandable without knowledge of the implementation. | Don't use excessive capitalization or special characters to draw attention to parts of the description, such as `**CRITICAL**` or `VERY IMPORTANT`. |
| Use human-readable names for AppFunctions. |   |
| Be clear and direct about what each AppFunction does. | Don't give procedural instructions that involve other functions, such as "Search for the contact first." Agents use your app description to plan calls across functions, so describe that order there instead. |
| Describe what the agent can expect from the function, with language such as "If you have X, then Y." |   |
| Assume that agents have their own instructions for using AppFunctions in general. Your function description says what the function does, and the agent's instructions cover how to use it. | Don't try to override or embed agent-level instructions in function descriptions. |

### Write with encapsulation in mind

Keep each function description self-contained, so that it guides the agent in
using that function and no other. The following table lists encapsulation
guidelines:

| Do | Don't |
|---|---|
| Write function descriptions that are specific and focused, with a single, well-defined purpose. For example, "create, find, and delete personal tasks." | Don't write a description that's overly broad, which can cause the agent to call your function at inappropriate times or for the wrong reasons. |
|   | Don't create multipurpose AppFunctions, or expose many AppFunctions for the same use case. Agents are more likely to choose the wrong function when several functions have similar intents. |
|   | Don't refer to, or try to influence the behavior of, other AppFunctions in your app or in other apps. This can create unintended dependencies and side effects. |

## Permissible actions and data sharing

Follow these guidelines to protect user privacy and safety when agents use
your app's functions:

| Do | Don't |
|---|---|
| Perform only safe, non-destructive tasks that the user would normally do in your app, where the agent can provide clear parameters from the user's request---for example, creating a task with a title or searching for notes. |   |
| Share only information that isn't highly personal or confidential, or data that the user explicitly consents to share for the action. | Don't give the agent wide-ranging access to user data or system resources. |
|   | Don't design AppFunctions that require or return passwords, financial details, private keys, or other highly sensitive personal information. |
| Perform actions that a user requested, even when they run later or in the background---for example, sending a message at a time that the user chose. | Don't perform actions that the user didn't request, such as tasks that start on their own or that go beyond the request. |
| Focus on functionality that benefits from natural language, such as tasks that are easier to express in conversation than through UI navigation---for example, "\[AI agent\], can you please help me find some available times next week on my calendar, and then suggest a flight to Chicago on one of those days?" |   |
| On form factors beyond phones, respect the user's privacy on shared devices, such as TVs, Android Auto, and Android Automotive OS. | Don't disclose information or perform actions that your app's UI doesn't support on that form factor. |
| Clearly and uniquely identify your function's purpose. | Don't pretend to be another tool or service. Your function's name and description must not be confusingly similar to other tools, which could cause the agent to select your function by mistake. |

## Parameter and return value design

Careful parameter and return value design prevents ambiguity and reduces the
chance of invalid calls. Follow these conventions:

| Do | Don't |
|---|---|
| Define parameters only for data that your function needs. | Don't request information that the function doesn't use. This minimizes data exposure and simplifies the function's use. |
| Use parameter names that reflect the expected input, such as `taskId`, `searchQuery`, or `recipientEmail`. | Don't use names like `full_context` or `conversation_history`. Such names are ambiguous because agents use these terms for their own context and conversation history. An agent could misinterpret them and pass a large amount of unnecessary data to your function, leading to data exfiltration. |
| Use the types that AppFunctions supports instead of defining your own---for example, `LocalDate`, `LocalTime`, `LocalDateTime`, or `Instant` for dates and times, and `Uri` for links. The library represents these types the same way in every app, so agents get a consistent format. For the full list of supported types, see [`AppFunctionSerializable`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionSerializable). |   |
| If a parameter isn't essential to the function's purpose, make it optional. This gives the agent flexibility when it only has partial information from the user. For more information, see [Optional parameters](https://developer.android.com/ai/appfunctions/quality-guidelines#optional-parameters). |   |
| If your AppFunction updates existing resources, make sure that each parameter can distinguish between "set to null" and "don't change." For an example, see [Updates to existing resources](https://developer.android.com/ai/appfunctions/quality-guidelines#update-resources). |   |
| To let the agent open a specific screen in your app, return a [`PendingIntent`](https://developer.android.com/reference/android/app/PendingIntent) for that screen. The agent can launch the `PendingIntent` as is, without building an intent for your app. Create it with an explicit intent and [`FLAG_IMMUTABLE`](https://developer.android.com/privacy-and-security/risks/pending-intent) so that the agent can't change where it leads. |   |

### Optional parameters

Only nullable, primitive, list, and array types can be optional. When the agent
omits an optional parameter, the library passes the type's default
value---`null`, zero, `false`, or empty---instead of the default that you declare.
Resolve meaningful defaults in the function body, as in the following example:

    /**
     * Creates a note.
     *
     * @param title The title of the note.
     * @param content The body text of the note.
     * @param attachments The files to attach to the note.
     * @param owner The ID of the user who owns the note.
     * @return The created note.
     */
    @AppFunctionDeclaration(isDescribedByKDoc = true)
    suspend fun createNote(
        title: String, // Required
        content: String? = null, // Optional
        attachments: List<Attachment> = emptyList(), // Optional
        owner: String? = null, // Optional
    ): Note = withContext(Dispatchers.IO) {
        noteRepository.createNote(
            title = title,
            // The library ignores declared default values and passes null for
            // omitted nullable parameters, so resolve meaningful defaults here.
            content = content ?: "",
            attachments = attachments,
            owner = owner ?: currentUserId(),
        )
    }

### Updates to existing resources

The following example uses a nullable `SetField` wrapper for each field that
the agent can update. A null `SetField` means "don't change," and
`SetField(null)` means "set to null":

    /** A new value for a field of an existing item. */
    @AppFunctionSerializable(isDescribedByKDoc = true)
    data class SetField<T>(
        /** The new value of the field. */
        val value: T,
    )

    /**
     * Updates an existing note. Omitted fields keep their values.
     *
     * @param noteId The ID of the note to update.
     * @param title The new title of the note.
     * @param content The new body text of the note.
     * @return The updated note.
     */
    @AppFunctionDeclaration(isDescribedByKDoc = true)
    suspend fun updateNote(
        noteId: String,
        title: SetField<String>? = null,
        content: SetField<String?>? = null,
    ): Note = withContext(Dispatchers.IO) {
        val note = noteRepository.getNote(noteId)
            ?: throw AppFunctionElementNotFoundException(
                "No note found with ID $noteId"
            )
        noteRepository.updateNote(
            noteId = noteId,
            // A null SetField means "don't change", and SetField(null) means
            // "set to null", so don't use ?: for nullable fields.
            title = title?.value ?: note.title,
            content = if (content != null) content.value else note.content,
        )
    }

## Error handling

When a call fails, the agent receives the exception that your function throws,
including its type and message. Follow these conventions so that the agent can
recover from the failure or report it to the user:

| Do | Don't |
|---|---|
| Throw the [`AppFunctionException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionException) subclass that matches the cause, with a message that describes the problem in plain language---for example, [`AppFunctionInvalidArgumentException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionInvalidArgumentException) when an argument isn't valid, or [`AppFunctionElementNotFoundException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionElementNotFoundException) when a requested item doesn't exist. The type tells the agent what kind of failure occurred, and the message gives it the details it needs to recover, such as correcting an argument or telling the user. The `updateNote` example in [Updates to existing resources](https://developer.android.com/ai/appfunctions/quality-guidelines#update-resources) shows this pattern. | Don't let other exceptions escape your function. The agent receives them as [`AppFunctionAppUnknownException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionAppUnknownException), which doesn't identify the kind of failure. |