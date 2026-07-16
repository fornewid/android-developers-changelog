---
title: https://developer.android.com/agents/skills/play/engage-sdk-integration/skill
url: https://developer.android.com/agents/skills/play/engage-sdk-integration/skill
source: md.txt
---

This skill guides you through integrating the Play Engage SDK into an Android
app. It ensures that the code follows the mandatory structure and uses the
required Engage entities for each vertical.

## Workflow

Follow these steps to assist the developer:

1. **Identify vertical and cluster:**

   - Ask the developer which vertical their app belongs to based on **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)**.
   - Check if the integration is for TV or mobile. If the integration is for TV, read the TV-specific sections in [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns) as well.
   - Use `{VERTICAL}.md` in the **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)** directory to identify the corresponding Engage entities and the `client` class name. The `client` field in the JSON provides the full class name. For example, `com.google.android.engage.food.service.AppEngageFoodClient`.
   - **Note:** Initializing the client class requires a `Context` parameter. For example, `AppEngageFoodClient(context)`.
   - Always refer to [common.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/common) for common entities.
   - Ask which cluster type they want to publish from the supported cluster types for that vertical.
   - Find the method to call from `{VERTICAL}.md` in the **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)** directory for the specified cluster. Each method will specify the request it expects.
   - Get the request structure from [requests.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/requests) and clusters from [clusters.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/clusters). Then suggest and use sources to fill the fields in the request structure correctly, along with the required entities and clusters.
2. **Generate structured boilerplate code:**

   - Create a new directory for all Engage-related code. Name the directory to match the naming convention of the existing codebase.
   - Generate the following classes using templates in [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns):
     - `Constants`: holds constant values such as attempt counts and publish types.
     - `ItemToEntityConverter`: converts the app's local models to Engage's Entity models.
     - `ClusterRequestFactory`: constructs the publish requests.
     - `EngageWorker`: handles the actual publishing and publish errors using WorkManager.
     - `EngagePublisher`: orchestrates periodic and one-time jobs.
     - `EngageBroadcastReceiver`: listens for AppEngageService intents and starts a one-time publish job from `EngagePublisher`. **Important** : Implement both **static registration** and **dynamic registration** patterns, including the companion object `register` method inside the `EngageBroadcastReceiver` class.
3. **Suggest entity mapping:**

   - Ask the developer to provide their local model schema (for example, a data class or a JSON snippet).
   - If they haven't provided one, share entities from `{VERTICAL}.md` in the **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)** directory as a guide.
   - Once the local model is identified, suggest a mapping to the corresponding Engage entity.
   - Generate the conversion logic using the `ItemToEntityConverter` pattern in [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns) and add it to the generated `{ENGAGE_CODE_DIR}/ItemToEntityConverter`.
4. **Suggest data source:**

   - Ask the developer to provide the source of actual data you'll publish.
   - Once you identify the data source, use it to fetch the data in the app's local model schema.
   - Use `{ENGAGE_CODE_DIR}/ItemToEntityConverter` to convert this data to an Engage entity.
   - Use obtained Engage entity model data with `{ENGAGE_CODE_DIR}/
     ClusterRequestFactory` to get cluster requests.
   - Call corresponding cluster publishing method obtained from `{VERTICAL}.md` in the **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)** directory with the obtained request in previous step in `{ENGAGE_CODE_DIR}/EngageWorker`.
5. **Gradle and manifest updates:**

   - Suggest updates to `build.gradle` and `AndroidManifest.xml`.
   - For mobile apps, use [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns).
   - For TV apps, use the TV-specific sections in [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns).
   - Provide the necessary `implementation` dependencies for `build.gradle` or `build.gradle.kts` from [patterns.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/patterns).
   - Provide the `<receiver>` and `<service>` declarations for `AndroidManifest.xml`.
   - Note: Except for TV, there aren't any vertical-specific imports. For all other verticals, `com.google.android.engage:engage-core:1.6.0` is sufficient.
6. **Debugging:**

   - Perform a Gradle sync.
   - If errors occur, follow this resolution order:
     - Fix import errors. For package `com.google.android.engage` or classes starting with `AppEngage`, verify the package name in the `{VERTICAL}.md` in **[references/schemas/](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas)** directory or [common.md](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/common).
     - Fix any other errors.
   - Execute a full Gradle build and resolve any remaining compilation issues. Repeat this step until the Gradle build is successful.
7. **User checklist:** At the end of code generation, notify the user to go
   through this checklist to verify that the integration is complete and as
   intended:

   - \[ \] Verify that all the Engage-related files are created in `{ENGAGE_CODE_DIR}/`:
     - `Constants`
     - `ItemToEntityConverter`
     - `ClusterRequestFactory`
     - `EngageWorker`
     - `{cluster_type}Publisher`
     - `EngageBroadcastReceiver`
   - \[ \] Verify that app's local model is converted to Engage entity by populating the fields correctly in the model in `{ENGAGE_CODE_DIR}/ItemToEntityConverter`.
   - \[ \] Verify that all image URIs in `ItemToEntityConverter` point to images matching the strict aspect ratio requirements of the vertical (for example, 16:9, 1:1, 2:3).
   - \[ \] Verify that `{ENGAGE_CODE_DIR}/EngageWorker` uses the data source identified in Step 4.
   - \[ \] Verify that `EngageBroadcastReceiver.register(context)` is called within the `Application` class or `MainActivity` to register the receiver dynamically.
   - \[ \] Verify that `AndroidManifest.xml` contains the static `<receiver>` declaration for `EngageBroadcastReceiver` with the necessary intent actions.
   - **Important** : Explicitly instruct the developer to call `EngageBroadcastReceiver.register(context)` inside their custom `Application` class `onCreate()` (or their main activity `onCreate()`) to dynamically register the receiver. Stress that **both** static and dynamic registrations are required for the integration to function.

## Reference materials

- **FAQ:** [Engage FAQ](https://developer.android.com/guide/playcore/engage/faq) - Refer to this document for answers to frequently
  asked questions from developers.

- **Vertical-specific guides:**

  - [Food Vertical](https://developer.android.com/guide/playcore/engage/food)
  - [Watch Vertical](https://developer.android.com/guide/playcore/engage/watch)
  - [Listen Vertical](https://developer.android.com/guide/playcore/engage/listen)
  - [Read Vertical](https://developer.android.com/guide/playcore/engage/read)
  - [Shopping Vertical](https://developer.android.com/guide/playcore/engage/shopping)
  - [Social Vertical](https://developer.android.com/guide/playcore/engage/social)
  - [Travel Vertical](https://developer.android.com/guide/playcore/engage/travel)
  - [Health and Fitness Vertical](https://developer.android.com/guide/playcore/engage/healthandfitness)
  - [Other Verticals](https://developer.android.com/guide/playcore/engage/otherverticals)
  - [TV Getting Started](https://developer.android.com/guide/playcore/engage/tv/getting-started)
  - [TV Recommendations](https://developer.android.com/guide/playcore/engage/tv/recommendations)
  - [TV Continue Watching](https://developer.android.com/guide/playcore/engage/tv/continue-watching)
  - [TV Entitlements](https://developer.android.com/guide/playcore/engage/tv/entitlements)
- **Vertical-specific schemas:**

  - [Food Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/food)
  - [Watch Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/watch)
  - [Listen Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/listen)
  - [Read Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/read)
  - [Shopping Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/shopping)
  - [Social Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/social)
  - [Travel Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/travel)
  - [TV Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/tv)
  - [Other Schema](https://developer.android.com/agents/skills/play/engage-sdk-integration/references/schemas/other)