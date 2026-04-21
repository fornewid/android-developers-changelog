---
title: Access helpful resources  |  Android Studio  |  Android Developers
url: https://developer.android.com/studio/gemini/access-helpful-resources
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Android Studio](https://developer.android.com/studio)
* [Gemini in Android Studio](https://developer.android.com/gemini-in-android)

# Access helpful resources Stay organized with collections Save and categorize content based on your preferences.





There are multiple ways that the agent can get up-to-date
information. These tools enable the agent to use information that was published
after its last training cutoff date, improving the quality of its responses.

## Android Knowledge Base

The Android Knowledge Base gives the agent access to fresh, authoritative
documentation about API changes, new libraries, updated best practices, and more
from the following sources:

* Android developer docs
* [Firebase](https://firebase.google.com/docs)
* [Google Developers](https://developers.google.com)
* [Kotlin docs](https://kotlinlang.org/docs)

The Android Knowledge Base provides the agent with the following two new tools.
To see all the tools available to the agent, type `/tools` into the prompt
field.

* `search_android_docs`: Searches the Android Knowledge Base for authoritative,
  high-quality documentation relevant to your query.
* `fetch_android_docs`: Retrieves the full content of the documents identified
  by the search tool.

The Android Knowledge Base should be invoked automatically when applicable, but
you can increase the chance that the agent will use it by specifically asking
the agent to use Android documentation in your prompt. For example, instead of
just saying "Upgrade navigation to Navigation 3" say "Upgrade navigation to
Navigation 3. Refer to Android documentation for guidance."

The Android Knowledge Base is also accessible using [Android CLI](/tools/agents)
using any agent and IDE of your choice. To learn more, see
[`android docs`](/tools/agents/android-cli#docs).

## Agent Web Search

When the agent can't find what it needs from the [Android Knowledge Base](#android-knowledge-base),
it can search the web. The Agent Web Search tool instructs Gemini to conduct a
real-time web search from Google, reducing the chance of providing outdated guidance or obsolete code examples.

The Agent Web Search tool gives the agent access to fresh, authoritative
information across the open web, including:

* **Latest library versions:** Retrieve the most recent releases for libraries
  like Coil or GitLive's Firebase KMP libraries.
* **New API Documentation:** Access documentation for tools and services
  released after the model's training.

The Agent Web Search is automatically available as an agent tool. To see all the
tools available to the agent, type `/tools` into the prompt field.

* `web_search`: Searches the live web using Google Search to find up-to-date
  information, documentation, and technical details relevant to your query.

The Agent Web Search should be invoked automatically when the agent determines
that a search is needed to provide an accurate answer. However, you can increase
the likelihood that the agent will use the tool by specifically asking it to
check for current information or typing `web_search` in your prompt.

### Example prompts

* "Tell me about GitLive's Firebase KMP libraries. Search the web for the
  latest version information before providing your answer."
* "How do I implement Xweather's Android API? Refer to the latest web
  documentation for the implementation steps."

### Permissions

To help ensure you have full control over your data and agent behavior, the Agent
Web Search tool leverages Android Studio's [permission model](/studio/gemini/permissions).
The agent won't access the web without your explicit consent.