---
title: https://developer.android.com/ai/appfunctions
url: https://developer.android.com/ai/appfunctions
source: md.txt
---

AppFunctions allow your Android app to share specific pieces of functionality
that the system and various AI agents and assistants can discover and invoke. By
defining these functions, you enable your app to provide services, data, and
actions to the Android OS, allowing users to complete tasks through AI agents
and system-level interactions.

AppFunctions serve as the mobile equivalent of tools within the [Model Context
Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro). While MCP traditionally standardizes how agents
connect to server-side tools, AppFunctions provide the same mechanism for
Android apps. This enables you to expose your app's capabilities as
orchestratable "tools" that authorized apps (callers) can discover and
execute to fulfill user intents. Callers must have the
[`EXECUTE_APP_FUNCTIONS`](https://developer.android.com/reference/android/Manifest.permission#EXECUTE_APP_FUNCTIONS) permission to discover and execute AppFunctions,
and can include agents, apps, and AI assistants like Gemini.

AppFunctions work with devices running Android 16 or higher.

### Example use cases

AppFunctions provide a powerful mechanism to automate tasks and streamline user
interactions. By exposing your app's capabilities, you enable users to
accomplish complex goals using natural language, often bypassing the need for
step-by-step, manual navigation with your UI.

The following scenarios illustrate how AppFunctions can be used to drive
experiences within a variety of app categories:

- **Task management and productivity**
  - **User request** : "*Remind me to pick up my package at work today at 5 PM*".
  - **AppFunction action**: The caller identifies the relevant task management app and invokes a function to create a task, automatically populating the title, time, and location fields based on the user's prompt.
- **Media and entertainment**
  - **User request** : "*Create a new playlist with the top jazz albums from this
    year*".
  - **AppFunction action**: The caller executes a playlist creation function within a music app, passing context like "top jazz albums for 2026" as the query to generate and launch the content immediately.
- **Cross-app workflows**
  - **User request** : "*Find the noodle recipe from Lisa's email and add the
    ingredients to my shopping list*".
  - **AppFunction action**: This request uses functions from multiple apps. First, the caller uses an email app's search function to retrieve the content. Then, it extracts the relevant ingredients and invokes a shopping list app's function to populate the user's list.
- **Calendar and scheduling**
  - **User request** : "*Add Mom's birthday party to my calendar for next Monday
    at 6 PM*".
  - **AppFunction action**: The approved agentic app invokes the calendar app's "create event" function, parsing the relevant context like "next Monday" and "6 PM" to create the entry without the user needing to manually open the calendar.

## How AppFunctions work

**AppFunctions** is an [Android 16 platform feature](https://developer.android.com/reference/android/app/appfunctions/package-summary) and an accompanying
[Jetpack library](https://developer.android.com/jetpack/androidx/releases/appfunctions) that allows apps to expose specific functions for callers,
such as agent apps, to access and execute on device.

The following diagram illustrates the typical flow of how AppFunctions are
shared by apps to an agent and subsequently executed. Agents are likely to
consider both server-side remote MCP tools and local AppFunctions together when
handling user requests. The detailed flow for using local AppFunctions is as
follows:

- **AppFunction declaration**: The Android app is built to expose its AppFunctions, such as "Create Note" or "Send Message".
- **Schema generation**: The AppFunctions Jetpack library generates an XML schema file that lists all the declared AppFunctions in the app. This file is used by the Android OS to index the available AppFunctions.
- **Metadata retrieval**: The agent can retrieve AppFunction metadata by querying it.
- **AppFunction selection and execution**: Based on user prompts, the agent will select and execute the appropriate AppFunction with the appropriate parameters.

![Diagram showing the typical flow of AppFunctions from app exposure to agent execution.](https://developer.android.com/static/ai/assets/images/appfunctions.svg) **Figure 1**: The typical flow of how AppFunctions are exposed and subsequently executed by an agent.

The AppFunctions Jetpack library simplifies exposing your app's functionality.
With the annotation processor, developers annotate the functions they want
to expose. Callers can then discover and invoke these indexed functions using
`AppFunctionManager`.

Your app is not required to verify whether the AppFunction feature is supported;
this is automatically handled within the Jetpack library. For example,
[AppFunctionManager](https://developer.android.com/reference/androidx/appfunctions/AppFunctionManagerCompat) can verify whether or not the feature is supported.

Here's an example of AppFunctions for a note-taking app with
capabilities to create, edit, and list notes.

    class NoteFunctions(
      private val noteRepository: NoteRepository
    ) {
        /**
         * A note.
         *
         * @param id The note's ID.
         * @param title The note's title.
         * @param content The note's content.
         */
        @AppFunctionSerializable(isDescribedByKDoc = true)
        data class Note(val id: Int, val title: String, val content: String)

        /**
         * Lists all available notes.
         *
         * @param appFunctionContext The context in which the AppFunction is executed.
         */
        @AppFunction(isDescribedByKDoc = true)
        suspend fun listNotes(appFunctionContext: AppFunctionContext): List<Note>? {
            return if (noteRepository.appNotes.isEmpty()) null else viewModel.appNotes
        }

        /**
         * Adds a new note to the app.
         *
         * @param appFunctionContext The context in which the AppFunction is executed.
         * @param title The title of the note.
         * @param content The note's content.
         */
        @AppFunction(isDescribedByKDoc = true)
        suspend fun createNote(
          appFunctionContext: AppFunctionContext,
          title: String,
          content: String
        ): Note {
            return noteRepository.createNote(title, content)
        }

        /**
         * Edits a single note.
         *
         * @param appFunctionContext The context in which the AppFunction is executed.
         * @param noteId The target note's ID.
         * @param title The new title if it should be updated.
         * @param content The new content if it should be updated.
         */
        @AppFunction(isDescribedByKDoc = true)
        suspend fun editNote(
          appFunctionContext: AppFunctionContext,
          noteId: String,
          title: String?,
          content: String,
        ): Note? {
            return noteRepository.updateNote(noteId, title, content)
        }
    }