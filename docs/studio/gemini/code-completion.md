---
title: https://developer.android.com/studio/gemini/code-completion
url: https://developer.android.com/studio/gemini/code-completion
source: md.txt
---

# Accelerate coding with AI code completion

Gemini offers AI-enabled autocompletion of code in Android Studio that appears as gray italicized text as you type. This feature saves you time and lets you complete coding projects faster by suggesting full functions. When AI code completion is enabled, Gemini might send additional information from your codebase such as surrounding pieces of your code, file types, and other necessary information to provide context to the LLM and provide more relevant suggestions.

To use AI code completion, follow these steps:

1. Enable context sharing by selecting**Use all Gemini features** in the[Gemini settings](https://developer.android.com/studio/gemini/configure-gemini). AI code completion only works when Gemini can access context from your codebase.
2. Open a file and start typing. Suggestions only trigger when the cursor is at the end of a line or anywhere on a blank line.
3. Press<kbd>Tab</kbd>to accept a suggestion and<kbd>Esc</kbd>to clear a suggestion.

Keep in mind that the system won't always generate code completions. It's possible that the model doesn't have enough information to generate a response with high confidence.

You can toggle AI code completion on and off at any time by clicking the Gemini icon at the bottom of the Studio IDE![](https://developer.android.com/static/studio/gemini/images/gemini-active.png)and clicking**Enable AI code completion**.