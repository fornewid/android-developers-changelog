---
title: https://developer.android.com/studio/releases/past-releases/as-otter-2-feature-drop-release-notes
url: https://developer.android.com/studio/releases/past-releases/as-otter-2-feature-drop-release-notes
source: md.txt
---

The following are new features in Android Studio Otter 2 Feature Drop.

## Access fresh documentation with the Android Knowledge Base

Agent Mode is now equipped with the Android Knowledge Base. With the knowledge
base, the agent can use information that was published after its last training
cutoff date, improving the quality of its responses and reducing the chance of
providing outdated guidance and code examples. The knowledge base gives the
agent access to fresh, authoritative documentation about API changes, new
libraries, updated best practices, and more from the following sources:

- Android developer docs
- [Firebase](https://firebase.google.com/docs)
- [Google Developers](https://developers.google.com)
- [Kotlin docs](https://kotlinlang.org/docs)

The Android Knowledge Base provides the agent with the following two new tools.
To see all the tools available to the agent, type `/tools` into the prompt
field.

- `search_android_docs`: Searches the Android Knowledge Base for authoritative, high-quality documentation relevant to your query.
- `fetch_android_docs`: Retrieves the full content of the documents identified by the search tool.

The Android Knowledge Base should be invoked automatically when applicable, but
you can increase the chance that the agent will use it by specifically asking
the agent to use Android documentation in your prompt. For example, instead of
just saying "Upgrade navigation to Navigation 3" say "Upgrade navigation to
Navigation 3. Refer to Android documentation for guidance."

## Communications from Android Studio

Android Studio Otter 1 Canary 3 and higher includes a new option to opt into
communications from our team. This enables you to receive relevant emails
and notifications regarding updates and new features in Android Studio. You
will see this option when you sign in.
![](https://developer.android.com/static/studio/preview/features/images/communications-opt-in.png) Communications opt-in