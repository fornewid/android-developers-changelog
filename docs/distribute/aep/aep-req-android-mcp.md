---
title: https://developer.android.com/distribute/aep/aep-req-android-mcp
url: https://developer.android.com/distribute/aep/aep-req-android-mcp
source: md.txt
---

> [!NOTE]
> **Note:** ***Delayed enforcement notice*** . *Enforcement is deferred **until the
> latter of March 1, 2027 or three months after the launch of self-service
> registration** for Android MCP. Current AEP participants will receive advance
> notice prior to the start of enforcement*.

Integrate Android MCP using [AppFunctions](https://developer.android.com/ai/appfunctions) to allow your
Android app to share specific pieces of functionality that the system and
various AI agents and assistants, like Google Gemini, can discover and invoke.
By defining these functions, you enable your app to provide services, data, and
actions on Android, allowing users to complete tasks through AI agents and
system-level interactions.

To ensure a streamlined development experience, it is highly recommended that
developers use the [AppFunctions Jetpack
SDK](https://developer.android.com/jetpack/androidx/releases/appfunctions), which provides a type-safe,
convenient interface for building robust integrations

**Integration with Android MCP is currently optional during the Early Access
Program**.

## Required implementation

To qualify for AEP, your app must adhere to the following requirements:

- The app must use the [AppFunctions
  APIs](https://developer.android.com/reference/android/app/appfunctions/package-summary) to implement at least one relevant use case.
- We highly recommend Implementation through the [AppFunctions Jetpack
  SDK](https://developer.android.com/reference/androidx/appfunctions/package-summary) to ensure a convenient and type-safe integration.
- Pass all mandatory integration tests.

## Guideline applicability

This guideline is applicable to apps with any of the following use cases:

| App type | Example use cases |
|---|---|
| Messaging \& Communication | Messaging, searching contacts, making calls |
| Notes | Create, edit, search, organize notes using context from the user and other apps |
| Calendar | Create, edit, and manage calendar events |
| Task management \& Productivity | Create, manage, and search tasks |
| Health \& Fitness tracking | Manage activities (start, stop, pause, or resume), track fitness and health metrics, on demand workouts |
| Shopping \& Retail | Cross-catalog search, cart and inventory management, purchasing support |
| Travel \& Local | Itinerary management, ride sharing, navigation, local discovery |
| Food \& Dining | Reservations, ordering and delivery of food, recipes and meal planning |
| Creativity | Create assets, edit photos, build creative workflows and projects |
| Media \& Photos | Contextual search and sharing for photos, photo editing, and media and playback experiences for music apps. |
| Tools \& System | On-device actions, remote hardware management (locking doors, finding devices, checking battery or fuel levels) |

## Exemptions

This guideline is not applicable to apps that don't support the previously
described use cases.

## Feature documentation and resources

The following resources provide implementation guidance and technical details on
the Android MCP feature. These resources are for your reference only and don't
contain additional program requirements.

- [Overview of AppFunctions](https://developer.android.com/ai/appfunctions)
- [Add the AppFunctions API to your app](https://developer.android.com/ai/appfunctions/add-appfunctions)