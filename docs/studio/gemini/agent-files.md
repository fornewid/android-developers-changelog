---
title: https://developer.android.com/studio/gemini/agent-files
url: https://developer.android.com/studio/gemini/agent-files
source: md.txt
---

# Customize Gemini using AGENTS.md files

| **Note:** Agent files titled`AGENTS.md`are compatible with Android Studio Narwhal 4 Feature Drop Canary 4 and higher. To use agent files with Android Studio Narwhal 3 Feature Drop, use the name`AGENT.md`instead of`AGENTS.md`.

Give Gemini in Android Studio customized instructions to follow using one or more`AGENTS.md`files.`AGENTS.md`files are placed alongside the other files in your codebase, so it's straightforward to check them in to your version control system (VCS) and share project-specific instructions, coding style rules, and other guidance with your entire team.

To get started, follow these steps:

1. Create an`AGENTS.md`file anywhere in your project's file system. Gemini scans the current directory and all parent directories for`AGENTS.md`files when you submit a query. For more details, see[How`AGENTS.md`files work](https://developer.android.com/studio/gemini/agent-files#how-agent-files-work).

   | **Tip:** Use multiple instruction files across different directories for more granular control over different parts of your codebase. For example, you can have a global`AGENTS.md`file at the project root and more specific`AGENTS.md`files in subdirectories for different modules.
2. Add your instructions. Write your instructions using Markdown. For readability, consider using headings and bullet points for different rules.[See example instructions](https://developer.android.com/studio/gemini/agent-files#example-instructions).

3. Save and commit the file to your VCS to share it with your team.

## Manage`AGENTS.md`files as context

You can apply or remove`AGENTS.md`files as context for a particular query using the**Context** drawer in the chat panel. The**`AGENTS.md`Files** options includes all`AGENTS.md`files in the current directory and its parent directories.
![Manage AGENTS.md files as context](https://developer.android.com/static/studio/gemini/images/context-menu-agent-md.png)**Figure 1.** Manage`AGENTS.md`files as context.

## Example instructions

You can use the`AGENTS.md`file to give instructions to the agent. The following are some examples, but the instructions that you provide should be specific to your project.

- "The main activity is`/path/to/MainActivity.kt`."
- "The code to support navigating between screens is`path/to/navigation/UiNavigation.kt`"
- "The code handling HTTP requests is at`<path>`."
- Project architecture
  - "Place all business logic in ViewModels."
  - "Always follow official architecture recommendations, including use of a layered architecture. Use a unidirectional data flow (UDF), ViewModels, lifecycle-aware UI state collection, and other recommendations."
- Preferred libraries: "Use the \<library name\> library for navigation."
- Defining placeholder names for common API services or internal terminology: "The primary backend service is referred to as 'PhotoSift-API'."
- Company style guides: "All new UI components must be built with Jetpack Compose. Don't suggest XML-based layouts."

## Modularize your`AGENTS.md`files

You can break down large`AGENTS.md`files into smaller files that can be reused in different contexts:

1. Separate out a set of instructions and save them in another Markdown file, such as`style-guidance.md`.

2. Reference the smaller Markdown files in an`AGENTS.md`file by using the`@`symbol followed by the path to the file you want to import. The following path formats are supported:

   - Relative paths:
     - `@./file.md`- Import from the same directory
     - `@../file.md`- Import from the parent directory
     - `@./subdirectory/file.md`- Import from a subdirectory
   - Absolute paths:`@/absolute/path/to/file.md`

For example, the following`AGENTS.md`file references two other instruction files:  

    # My AGENTS.md

    You are an experienced Android app developer.

    @./get-started.md

    ## Coding style

    @./shared/style-guidance.md

## How`AGENTS.md`files work

Gemini automatically scans the current directory and parent directories for`AGENTS.md`files and adds their content to the beginning of every prompt as a preamble. If you don't have a file open when you submit a query, then the`AGENTS.md`file at the project root (if there is one) is included by default.
| **Note:** If you have a`GEMINI.md`file and`AGENTS.md`file in the same directory, the`GEMINI.md`file takes precedence.

## What's the difference between`AGENTS.md`files and Rules?

[Rules](https://developer.android.com/studio/gemini/rules)also let you define instructions and preferences that apply to all prompts. However, rules are defined in the IntelliJ file`/.idea/project.prompts.xml`, whereas`AGENTS.md`files are saved next to your source code and are IDE-neutral. We recommend using`AGENTS.md`files if one of the primary purposes is to share the instructions with your team.
| **Note:** Gemini combines rules and instructions in`AGENTS.md`files when processing your query.