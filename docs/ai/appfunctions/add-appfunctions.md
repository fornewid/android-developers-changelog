---
title: https://developer.android.com/ai/appfunctions/add-appfunctions
url: https://developer.android.com/ai/appfunctions/add-appfunctions
source: md.txt
---

> Documentation index: https://developer.android.com/ai/appfunctions/llms.txt

This guide explains how to integrate the AppFunctions API into your Android app,
implement the logic for a function, and verify that the integration works
correctly.

## Version compatibility

This implementation requires that your project `compileSdk` be set to API level
37 or higher. Your project must use Android Gradle Plugin 9.1.0 or higher.

Your app is not required to verify whether AppFunctions are supported; this is
automatically handled within the AppFunctions Jetpack library.
[`AppFunctionManager`](https://developer.android.com/reference/androidx/appfunctions/AppFunctionManager.md.txt) returns an instance if the feature is supported, and
returns null if not.

### Dependencies

Add the required library dependencies to your module's `build.gradle.kts` (or
`build.gradle`) file, and configure the KSP plugin in your top-level app module
as shown:

```kotlin
dependencies {
  implementation("androidx.appfunctions:appfunctions:1.0.0-rc01")
  // If this project uses any Kotlin source, use Kotlin Symbol Processing (KSP)
  // See Add the KSP plugin to your project
  ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-rc01")
}
```

## Implement AppFunctions logic

To implement an AppFunction for your Android app, create a class that implements
the specific AppFunctions logic. This involves creating serializable data
classes for parameters and responses, and then providing the core logic within
the function method.

The following code shows an example implementation for creating a task in the
[TODO app](https://github.com/android/architecture-samples), including defining custom parameters and response
types and the main function logic using a repository.


```kotlin
@RequiresApi(36)
@AndroidEntryPoint
@AppFunctionServiceEntryPoint(
    serviceName = "TaskAppFunctionService",
    appFunctionXmlFileName = "task_app_function_service",
)
abstract class BaseTaskAppFunctionService : AppFunctionService() {
    @Inject internal lateinit var taskRepository: TaskRepository

    /**
     * Creates a task with a title, content, or both.
     *
     * @param createTaskParams The title and content of the task. At least one
     *   of them is required.
     * @return The created task, including its ID.
     */
    @AppFunctionDeclaration(isDescribedByKDoc = true)
    suspend fun createTask(
        createTaskParams: CreateTaskParams,
    ): Task = withContext(Dispatchers.IO) {
        // Developers can use predefined exceptions to let the agent know
        // why it failed.
        if (createTaskParams.title == null && createTaskParams.content == null) {
            throw AppFunctionInvalidArgumentException("A task needs a title, content, or both.")
        }

        val id = taskRepository.createTask(
            createTaskParams.title,
            createTaskParams.content
        )

        return@withContext taskRepository
            .getTask(id)
            ?.toTask()
            ?: throw AppFunctionElementNotFoundException("Task not found for ID = $id")
    }

    // Maps internal TaskEntity
    private fun TaskEntity.toTask() = Task(id = id, title = title, content = description)
}
```

<br />

### Key points about the code

- By default, an AppFunction implementation runs in the Android UI thread. Therefore, a long-running operation should do the following:
  - Declare the AppFunction as a suspend function.
  - Switch to a suitable coroutine dispatcher when the operation could block the thread.
- When `isDescribedByKDoc` is set to `true`, the function description or the serializable description is encoded as part of the `AppFunctionMetadata` to help the agent understand how to use the app's AppFunction. Starting with version 1.0.0-beta01, `isDescribedByKDoc` has no default value, so set it explicitly.

## Declare the AppFunction service in your manifest

Register the KSP-generated service declaration and `app_metadata` property
inside your module manifest, for example, in `src/main/AndroidManifest.xml`. The
KSP compiler generates the concrete service class (`TaskAppFunctionService`)
extending your abstract entry point class, along with the corresponding XML
schema in your `assets/` directory.


```xml
<service
    android:name="com.example.snippets.ai.TaskAppFunctionService"
    android:permission="android.permission.BIND_APP_FUNCTION_SERVICE"
    android:exported="true"
    tools:targetApi="36">
    <property
        android:name="android.app.appfunctions.schema"
        android:value="app_functions_schema.xsd" />
    <property
        android:name="android.app.appfunctions.v2"
        android:value="task_app_function_service.xml" />
    <intent-filter>
        <action android:name="android.app.appfunctions.AppFunctionService" />
    </intent-filter>
</service>
<property
    android:name="android.app.appfunctions.app_metadata"
    android:resource="@xml/app_metadata" />
```

<br />

## Optional: Toggle AppFunction availability at runtime

Use the `AppFunctionManager` API to explicitly enable or disable functions when
gating your AppFunctions. Gating can be useful when certain features of your app
are not available to all users. By dynamically enabling or disabling
AppFunctions, the intelligence system knows exactly which features are available
for your user at any given time.

To safely gate AppFunctions that require a specific account state, follow a
two-step process:

**Step 1. Make the function disabled by default**

To prevent the function from being accessible before your feature flag is
verified, set the `isEnabled` parameter of your `@AppFunctionDeclaration`
annotation to `false`.


```kotlin
@AppFunctionDeclaration(isEnabled = false, isDescribedByKDoc = true)
suspend fun createTask(
    createTaskParams: CreateTaskParams,
): Task = TODO()
```

<br />

**Step 2. Dynamically enable the function at runtime**

For each `@AppFunctionServiceEntryPoint` class, the compiler generates a
corresponding class containing function ID constants (using an `Ids` suffix).
You can use these generated ID constants alongside the `setAppFunctionEnabled`
method from `AppFunctionManager` to change a function's enabled state at
runtime.


```kotlin
suspend fun onFeatureEnabled(context: Context) {
    try {
        AppFunctionManager.getInstance(context)
            ?.setAppFunctionEnabled(
                BaseTaskAppFunctionServiceIds.CREATE_TASK_ID,
                AppFunctionManager.APP_FUNCTION_STATE_ENABLED,
            )
    } catch (e: Exception) {
        // Handle exception: AppFunctions indexation may not be fully completed
        // upon initial app startup.
    }
}

suspend fun onFeatureDisabled(context: Context) {
    try {
        AppFunctionManager.getInstance(context)
            ?.setAppFunctionEnabled(
                BaseTaskAppFunctionServiceIds.CREATE_TASK_ID,
                AppFunctionManager.APP_FUNCTION_STATE_DISABLED,
            )
    } catch (e: Exception) {
        // Handle exception
    }
}
```

<br />

## Considerations of types of functionalities to make available

Security is always paramount. When you're choosing which capabilities of your
app to make available as AppFunctions, keep in mind that AI agents might process
user queries on the server to use advanced LLM capabilities.

To provide a great user experience that also avoids exposing sensitive
information, we recommend following these guidelines:

- **Functionality that benefits from natural language**: Make tasks available that are easier for a user to express in conversation than through manual UI navigation.
- **Narrow access**: Create AppFunctions that only give the agent access to data and actions that are required to fulfill the user's specific request.
- **Non-sensitive information**: Only share data that is not highly personal or confidential, or data the user explicitly consents to share in the context of the action.
- **Safe, non-destructive actions** : Make available only safe, non-destructive tasks that users would normally do in your app, such as creating a task or searching for notes. For more information, see [Permissible actions and data
  sharing](https://developer.android.com/ai/appfunctions/quality-guidelines#permissible-actions).

## Verify AppFunction integration

Because your AppFunctions act as services that AI agents call, testing has two
sides: how your function behaves, and how agents behave when calling it.

### Test your function

Start with unit tests for your function logic, accounting for how an agent call
through the AppFunctions library differs from a direct Kotlin call:

- **Default values** : Kotlin default parameter values don't apply. An omitted optional parameter arrives as `null`, `0`, `false`, or an empty list or array, so a `limit: Int = 10` parameter arrives as `0`. Test omitted parameters with those values and resolve defaults in the function body. For more information, see [Optional parameters](https://developer.android.com/ai/appfunctions/quality-guidelines.md.txt#optional-parameters).
- **Main thread** : Platform calls start on the main thread, and calling your `suspend` function directly from a unit test doesn't catch main-thread blocking. Make sure database, network, and disk I/O run on a background coroutine dispatcher, such as `Dispatchers.IO`.
- **Exceptions** : When a request can't succeed, throw a specific [`AppFunctionException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionException.md.txt) subclass. Other uncaught exceptions reach the agent as [`AppFunctionAppUnknownException`](https://developer.android.com/reference/kotlin/androidx/appfunctions/AppFunctionAppUnknownException.md.txt) with your raw exception message attached, which doesn't identify the kind of failure. For more information, see [Error handling](https://developer.android.com/ai/appfunctions/quality-guidelines.md.txt#error-handling).
- **Model inputs**: Because inputs come from a model rather than constrained UI controls, test blank strings, synonyms such as "dollars" for "USD", and out-of-range values.

On a device or emulator, use `adb shell cmd app_function` to verify that the
platform indexed your generated metadata and can invoke your service.

Use `adb shell cmd app_function list-app-functions --package $myPackageName` to
see details of the AppFunctions your app provides.

You can also execute an AppFunction directly from the command line using its
explicit identifier (`"$enclosingClassName#$methodName"`):

```bash
adb shell "cmd app_function execute-app-function \
  --package com.example.android.appfunctions \
  --function 'com.example.android.appfunctions.BaseTaskAppFunctionService#createTask' \
  --parameters '{\"createTaskParams\": {\"title\": \"Buy milk\", \"content\": \"From grocery store\"}}'"
```

### Test with agents

Test with an agent to verify that it selects the right function from your
descriptions and that the request works as you expect. Because each agent
behaves differently, test with the agents that call your AppFunctions:

- **Sample agent** : To test tool discovery and end-to-end workflows locally, install and run the open-source [AppFunctions testing agent](https://github.com/android/appfunctions) on your device.
- **Gemini** : To test how Gemini on Android calls your AppFunctions, join the Connected Apps Platform developer preview and follow [Create and manage
  Connected Apps](https://developer.android.com/ai/appfunctions/create-manage-connected-apps).
- **In-app agent** : If your app includes its own agent that calls `AppFunctionManager` for functions in the same package, test your functions through that agent as well.

During development, you can also verify your integration using chat-based
assistants like Gemini in Android Studio with the [AppFunctions agent skill](https://developer.android.com/ai/appfunctions/add-appfunctions.md.txt#android-skills-card__implement-appfunctions),
or provide a prompt such as the following:

    Execute `adb shell cmd app_function` to learn how the tool works, then act as a
    chat agent aiming to invoke AppFunctions to fulfill user prompts for this app.
    Use the AppFunction descriptions to choose functions and parameters.

## Migrate from lower API versions

In version 1.0.0-alpha10, AppFunctions introduced a compile-time
`@AppFunctionServiceEntryPoint` architecture that consolidates library
dependencies and replaces legacy configuration providers
(`AppFunctionConfiguration.Provider`). Version 1.0.0-alpha12 removed the legacy
providers. Version 1.0.0-alpha13 renamed the `@AppFunction` annotation to
`@AppFunctionDeclaration`, and version 1.0.0-beta01 renamed the
`appfn:description` attribute in your app metadata XML file to
`appfn:instructions`. Version 1.0.0-rc01 removed the legacy
`appfunctions:aggregateAppFunctions` compiler option; if your build passes it as
a KSP argument, remove it.

If your app uses a lower version of AppFunctions (such as 1.0.0-alpha09 or
1.0.0-alpha10), you can automate your migration using the [AppFunctions agent
skill](https://developer.android.com/ai/appfunctions/add-appfunctions#android-skills-card__implement-appfunctions) in an AI IDE like Gemini in Android Studio. The skill contains
dedicated migration rules that guide an agent to consolidate your build
dependencies, create the required `@AppFunctionServiceEntryPoint` service
wrapper, decouple context parameters, update your manifest declarations, apply
the 1.0.0-beta01 renames, and remove retired compiler options.


## Android skills

[View on GitHub](https://github.com/android/skills/tree/main/device-ai/appfunctions)

### Implement AppFunctions

Use the AppFunctions [Android skill](https://developer.android.com/tools/agents/android-skills.md.txt) to expose key user workflows to the Android system, allowing AI agents to discover and execute them on-device. To install the skill from the [Android CLI](https://developer.android.com/tools/agents/android-cli.md.txt), run:

    android skills add appfunctions

To activate the skill, try the following prompt:

    Use the AppFunctions skill to upgrade my app's AppFunctions implementation to 1.0.0-rc01.

<br />