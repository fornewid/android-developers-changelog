---
title: https://developer.android.com/studio/gemini/code-completion
url: https://developer.android.com/studio/gemini/code-completion
source: md.txt
---

> [!NOTE]
> **Note:** [Next Edit Prediction](https://developer.android.com/studio/gemini/next-edit-prediction) is now the default experience for users on some Gemini flash models. We encourage you to try it out. You can toggle between Next Edit Prediction and traditional AI code completion at **File** (**Android Studio** on macOS) \> **Settings \> Tools \> AI \> Editor**.

AI in Android Studio offers autocompletion of code that appears as gray
italicized text as you type. This feature saves you time and lets you complete
coding projects faster by suggesting full functions. When AI code completion is
enabled, the agent might send additional information from your codebase such as
surrounding pieces of your code, file types, and other necessary information to
provide context to the LLM and provide more relevant suggestions.

To use AI code completion, follow these steps:

1. Enable context sharing by going to the [AI settings and allowing the agent
   to read files from your project](https://developer.android.com/studio/gemini/permissions). AI code completion only works when the agent can access context from your codebase.
2. Open a file and start typing. Suggestions only trigger when the cursor is at the end of a line or anywhere on a blank line.
3. Press <kbd>Tab</kbd> to accept a suggestion and <kbd>Esc</kbd> to clear a suggestion.

Keep in mind that the system won't always generate code completions. It's
possible that the model doesn't have enough information to generate a response
with high confidence.