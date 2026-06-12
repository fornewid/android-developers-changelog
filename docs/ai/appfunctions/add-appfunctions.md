---
title: https://developer.android.com/ai/appfunctions/add-appfunctions
url: https://developer.android.com/ai/appfunctions/add-appfunctions
source: md.txt
---

<br />

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

    // Add this to your app module at the top level. For multi module applications,
    // you only need to specify this once.
    ksp {
      arg("appfunctions:aggregateAppFunctions", "true")
    }

    dependencies {
      implementation("androidx.appfunctions:appfunctions:1.0.0-alpha09")
      implementation("androidx.appfunctions:appfunctions-service:1.0.0-alpha09")
      // If this project uses any Kotlin source, use Kotlin Symbol Processing (KSP)
      // See Add the KSP plugin to your project
      ksp("androidx.appfunctions:appfunctions-compiler:1.0.0-alpha09")
    }

## Implement AppFunctions logic

To implement an AppFunction for your Android app, create a class that implements
the specific AppFunctions logic. This involves creating serializable data
classes for parameters and responses, and then providing the core logic within
the function method.

The following code shows an example implementation for creating a task in the
[TODO app](https://github.com/android/architecture-samples), including defining custom parameters and response
types and the main function logic using a repository.

    package com.example.android.appfunctions


    import androidx.appfunctions.AppFunctionSerializable
    import androidx.appfunctions.AppFunctionContext
    import androidx.appfunctions.AppFunctionElementNotFoundException
    import androidx.appfunctions.AppFunctionInvalidArgumentException
    import androidx.appfunctions.service.AppFunction
    import javax.inject.Inject
    ...

    // Developers can provide additional parameters in the constructor if needed.
    // This requires a custom factory setup in the next step.
    class TaskFunctions @Inject constructor(
      private val taskRepository: TaskRepository
    ) {
      /** The parameter to create the task. */
      @AppFunctionSerializable(isDescribedByKDoc = true)
      data class CreateTaskParams(
        /** The title of the task. */
        val title: String,
        /** The content of the task. */
         val content: String
      )

      /** The user-created task. */
      @AppFunctionSerializable(isDescribedByKDoc = true)
      data class Task(
        /** The ID of the task. */
        val id: String,
        /** The title of the task. */
        val title: String,
        /** The content of the task. */
        val content: String
      )

      /**
       * Creates a task based on [createTaskParams].
       *
       * @param createTaskParams The parameter to describe how to create the task.
       */
      @AppFunction(isDescribedByKDoc = true)
      suspend fun createTask(
        appFunctionContext: AppFunctionContext,
        createTaskParams: CreateTaskParams,
      ): Task = withContext(Dispatchers.IO) {
        // Developers can use predefined exceptions to let the agent know
        // why it failed.
        if (createTaskParams.title == null && createTaskParams.content == null) {
          throw AppFunctionInvalidArgumentException("Title or content should be non-null")
        }

        val id = taskRepository.createTask(
                 createTaskParams.title,
                 createTaskParams.content)

        return taskRepository
            .getTask(id)
            ?.toTask()
            ?: throw AppFunctionElementNotFoundException("Task not found for ID = $id")
      }


      // Maps internal TaskEntity
      private fun TaskEntity.toTask() = Task(id = id, title = title, content = description)
    }

### Key points about the code

- By default, an AppFunction implementation runs in the Android UI thread. Therefore, a long-running operation should do the following:
  - Declare the AppFunction as a suspend function.
  - Switch to a suitable coroutine dispatcher when the operation could block the thread.
- When `isDescribedByKDoc` is set to `true`, the function description or the serializable description is encoded as part of the `AppFunctionMetadata` to help the agent understand how to use the app's AppFunction.

## Optional: Use Hilt to provide a custom AppFunction factory

If your `AppFunction` implementation class requires dependencies in its
constructor (like as in `TaskRepository` in the previous example), you need to
provide a custom factory so the system knows how to instantiate it. This is an
optional step and only necessary if your function class has constructor
parameters. This example shows how to create a custom `AppFunctionFactory` and
configure it within your `Application` class, using Hilt for dependency
injection.

    import android.app.Application
    import androidx.appfunctions.service.AppFunctionConfiguration
    import com.example.android.appfunctions.TaskFunctions
    import dagger.hilt.android.HiltAndroidApp
    import javax.inject.Inject

    @HiltAndroidApp
    class TodoApplication : Application(), AppFunctionConfiguration.Provider {
      @Inject lateinit var taskFunctions: TaskFunctions
      override fun onCreate() {
        super.onCreate()
      }
      // This shows how AppFunctions works with Hilt.
      override val appFunctionConfiguration: AppFunctionConfiguration
        get() =
          AppFunctionConfiguration.Builder()
            .addEnclosingClassFactory(TaskFunctions::class.java) { taskFunctions }
            .build()
    }

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

    @AppFunction(isEnabled = false, isDescribedByKDoc = true)
    suspend fun createTask(...) { ... }

**Step 2. Dynamically enable the function at runtime**

For each `AppFunction` class, the compiler generates a corresponding class
containing function ID constants (using an `Ids` suffix). You can use these
generated ID constants alongside the `setAppFunctionEnabled` method from
`AppFunctionManagerCompat` to change a function's enabled state at runtime.

    import androidx.appfunctions.AppFunctionManager
    // Assuming there is a hook API to observe user state or feature flags
    suspend fun onFeatureEnabled() {
        try {
            AppFunctionManager.getInstance(context)
                .setAppFunctionEnabled(
                    // Function ID is generated for developer to get
                    TaskFunctionsIds.CREATE_TASK_ID,
                    AppFunctionManagerCompat.APP_FUNCTION_STATE_ENABLED,
                )
        } catch (e: Exception) {
            // Handle exception: AppFunctions indexation may not be fully completed
            // upon initial app startup.
        }
    }

    suspend fun onFeatureDisabled() {
        AppFunctionManagerCompat.getInstance(context)
            .setAppFunctionEnabled(
                TaskFunctionsIds.CREATE_TASK_ID,
                AppFunctionManagerCompat.APP_FUNCTION_STATE_DISABLED,
            )
    }

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

In Gemini in Android Studio, or other agents of your choice, provide a prompt
such as the following.

    Execute `adb shell cmd app_function` to learn how the tool works, then act as a
    chat agent aiming to invoke AppFunctions to fulfil user prompts for this app.
    Rely on the AppFunction description as instructions.