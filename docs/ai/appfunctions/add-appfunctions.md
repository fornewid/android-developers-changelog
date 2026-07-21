---
title: https://developer.android.com/ai/appfunctions/add-appfunctions
url: https://developer.android.com/ai/appfunctions/add-appfunctions
source: md.txt
---

This guide explains how to integrate the AppFunctions API into your Android app,
implement the logic for a function, and verify that the integration works
correctly.

## Version compatibility

This implementation requires that your project `compileSdk` be set to API level
36 or higher.

Your app is not required to verify whether AppFunctions are supported; this is
automatically handled within the AppFunctions Jetpack library.
[`AppFunctionManager`](https://developer.android.com/reference/androidx/appfunctions/AppFunctionManager) returns an instance if the feature is supported, and
returns null if not.

### Dependencies

Add the required library dependencies to your module's `build.gradle.kts` (or
build.gradle) file, and configure the KSP plugin in your top-level app module as
shown:

    dependencies {
      implementation("androidx.appfunctions:appfunctions:1.0.0-alpha10")
      // If this project uses any Kotlin source, use Kotlin Symbol Processing (KSP)
      // See Add the KSP plugin to your project
      ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-alpha10")
    }

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
     * Creates a task based on [createTaskParams].
     *
     * @param createTaskParams The parameter to describe how to create the task.
     */
    @AppFunction(isDescribedByKDoc = true)
    suspend fun createTask(
        createTaskParams: CreateTaskParams,
    ): Task = withContext(Dispatchers.IO) {
        // Developers can use predefined exceptions to let the agent know
        // why it failed.
        if (createTaskParams.title == null && createTaskParams.content == null) {
            throw AppFunctionInvalidArgumentException("Title or content should be non-null")
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
- When `isDescribedByKDoc` is set to `true`, the function description or the serializable description is encoded as part of the `AppFunctionMetadata` to help the agent understand how to use the app's AppFunction.

## Declare the AppFunction service in your manifest

Register the KSP-generated service declaration and `app_metadata` property
inside your module manifest, for example, in `src/main/AndroidManifest.xml`.
The KSP compiler generates the concrete service class (`TaskAppFunctionService`)
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
verified, set the `isEnabled` parameter of your `@AppFunction` annotation to
`false`.


```kotlin
@AppFunction(isEnabled = false, isDescribedByKDoc = true)
suspend fun createTask(
    createTaskParams: CreateTaskParams,
): Task = TODO()
```

<br />

**Step 2. Dynamically enable the function at runtime**

For each `AppFunction` class, the compiler generates a corresponding class
containing function ID constants (using an `Ids` suffix). You can use these
generated ID constants alongside the `setAppFunctionEnabled` method from
`AppFunctionManagerCompat` to change a function's enabled state at runtime.


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
app to make available as AppFunctions, it's important to remember that system
agents may process user queries on the server to leverage advanced LLM
capabilities.

To provide a great user experience that also avoids exposing sensitive
information, we recommend following these guidelines:

- **Functionality that benefits from natural language**: Make tasks available that are easier for a user to express in conversation than through manual UI navigation.
- **Narrow access**: Create AppFunctions that only give the agent access to data and actions that are required to fulfill the user's specific request.
- **Non-sensitive information**: Only share data that is not highly personal or confidential, or data the user explicitly consents to share in the context of the action.
- **Unambiguous confirmation for any destructive action**: Be extremely cautious with functions that perform destructive actions (like deleting data). While the agent might invoke them, your app should include its own confirmation step and use clear, unambiguous language about the intentions. It's also helpful to add more than one confirmation step to really ensure that the user is aware of what they are being asked to do.

## Verify AppFunction integration

To verify whether you have correctly integrated AppFunctions, you can use `adb
shell cmd app_function`.

Use `adb shell cmd app_function list-app-functions | grep --after-context 10
$myPackageName` to see details of the AppFunctions your app provides.

You can also execute an AppFunction directly from the command line using its
explicit identifier (`"$enclosingClassName#$methodName"`):

    adb shell "cmd app_function execute-app-function \
      --package com.example.android.appfunctions \
      --function 'com.example.android.appfunctions.BaseTaskAppFunctionService#createTask' \
      --parameters '{\"createTaskParams\": {\"title\": \"Buy milk\", \"content\": \"From grocery store\"}}'"

To experience Android MCP in action and verify end-to-end workflows without
needing any prompts, install and run the [AppFunctions testing
agent](https://github.com/android/appfunctions) Android app on your device.

If you're verifying your integration using chat-based assistants like Gemini in
Android Studio, use the AppFunctions development skill, or provide a prompt such
as the following:

    Execute `adb shell cmd app_function` to learn how the tool works, then act as a
    chat agent aiming to invoke AppFunctions to fulfil user prompts for this app.
    Rely on the AppFunction description as instructions.

## Migrate from lower API versions

In version 1.0.0-alpha10, AppFunctions introduced a compile-time
`@AppFunctionServiceEntryPoint` architecture that consolidates library
dependencies and replaces legacy configuration providers
(`AppFunctionConfiguration.Provider`).

If your app currently uses an earlier version of AppFunctions (such as
1.0.0-alpha09), you can automate your migration using the [AppFunctions agent
skill](https://github.com/android/skills/tree/main/device-ai/appfunctions) in an AI IDE like Gemini in Android Studio. The skill
contains dedicated migration rules that guide an agent to consolidate your build
dependencies, create the required `@AppFunctionServiceEntryPoint` service
wrapper, decouple context parameters, and update your manifest declarations.

To initiate an automated migration with your AI agent, use a prompt such as the
following:

    Use the AppFunctions migration skill to upgrade my app's AppFunctions implementation from 1.0.0-alpha09 to the 1.0.0-alpha10 @AppFunctionServiceEntryPoint architecture.