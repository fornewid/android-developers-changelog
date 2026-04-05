---
title: Handle user interaction  |  Jetpack Compose  |  Android Developers
url: https://developer.android.com/develop/ui/compose/glance/user-interaction
source: html-scrape
---

* [Android Developers](https://developer.android.com/)
* [Develop](https://developer.android.com/develop)
* [Core areas](https://developer.android.com/develop/core-areas)
* [UI](https://developer.android.com/develop/ui)
* [Docs](https://developer.android.com/develop/ui/compose/documentation)

# Handle user interaction Stay organized with collections Save and categorize content based on your preferences.



Glance simplifies handling user interaction via the `Action` classes. Glance's
`Action` classes define the actions a user can take, and you can specify the
operation performed in response to the action. You can apply an `Action` to any
component with the [`GlanceModifier.clickable`](/reference/kotlin/androidx/glance/GlanceModifier#(androidx.glance.GlanceModifier).clickable(androidx.glance.action.Action)) method.

App widgets live on a remote process, so the actions are defined at creation
time and the execution happens in the remote process. In native `RemoteViews`,
this is done via `PendingIntents`.

The following actions are described on this page:

* [Launch an activity](/develop/ui/compose/glance/user-interaction#launch-activity)
* [Launch a service](/develop/ui/compose/glance/user-interaction#launch-service)
* [Send a broadcast event](/develop/ui/compose/glance/user-interaction#send-broadcast)
* [Run callback](/develop/ui/compose/glance/user-interaction#run-actioncallback)

**Note:** See [`ActionAppWidget.kt`](https://cs.android.com/androidx/platform/frameworks/support/+/androidx-main:glance/glance-appwidget/integration-tests/demos/src/main/java/androidx/glance/appwidget/demos/ActionAppWidget.kt) for an example of how to handle
actions.

## Launch an activity

To launch an activity on user interaction, provide the
[`actionStartActivity`](/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionStartActivity(android.content.Intent,%20androidx.glance.action.ActionParameters))(..) function to a `Button` or other composable via the
`GlanceModifier.clickable`(..) modifier.

Provide one of the following in `actionStartActivity`:

* The target activity class
* The [`ComponentName`](/reference/android/content/ComponentName)
* An Intent

Glance translates the Action into a `PendingIntent` with the provided target and
parameters. In the following example, the `NavigationActivity` is launched when a
user clicks the button:

```
@Composable
fun MyContent() {
    // ..
    Button(
        text = "Go Home",
        onClick = actionStartActivity<MyActivity>()
    )
}

GlanceSnippets.kt
```

## Launch a service

Similar to launching an activity, launch a service on user interaction using one
of the [`actionStartService`](/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionstartservice) methods.

Provide one of the following in `actionStartService`:

* The target activity class
* The [`ComponentName`](/reference/android/content/ComponentName)
* An intent

```
@Composable
fun MyButton() {
    // ..
    Button(
        text = "Sync",
        onClick = actionStartService<SyncService>(
            isForegroundService = true // define how the service is launched
        )
    )
}

GlanceSnippets.kt
```

## Send a broadcast event

Send a broadcast event on user interaction using one of the
[`actionSendBroadcast`](/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionstartbroadcastreceiver) methods:

Provide one of the following in `actionSendBroadcast`:

* String action
* The [`ComponentName`](/reference/android/content/ComponentName)
* An intent
* [`BroadcastReceiver`](/reference/android/content/BroadcastReceiver) class

```
@Composable
fun MyButton() {
    // ..
    Button(
        text = "Send",
        onClick = actionSendBroadcast<MyReceiver>()
    )
}

GlanceSnippets.kt
```

## Perform custom actions

Instead of launching a specific target, Glance can use a lambda action or an
`actionRunCallback` to perform an action, such as updating the UI or state on
user interaction.

### Run lambda actions

You can use lambda functions as callbacks to the UI interactions.

**Note:** Lambda callbacks run in the context of a `WorkManager` worker that is run
in a `Service`. Apps that target Android 12 or higher can't start activities
from services or broadcast receivers that act as [trampolines](/about/versions/12/behavior-changes-12#notification-trampolines). Instead of
starting activities from lambdas, use the [`actionStartActivity`](/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionStartActivity(android.content.Intent,%20androidx.glance.action.ActionParameters))
callback to start the activity from the `GlanceAppWidget`.

For example, pass the lambda function to the `GlanceModifier.clickable`
modifier:

```
Text(
    text = "Submit",
    modifier = GlanceModifier.clickable {
        submitData()
    }
)

GlanceSnippets.kt
```

Or, pass it to the `onClick` parameter on composables that support it:

```
Button(
    text = "Submit",
    onClick = {
        submitData()
    }
)

GlanceSnippets.kt
```

### Run ActionCallback

Alternatively, use the [`actionRunCallback`](/reference/kotlin/androidx/glance/appwidget/action/package-summary#actionruncallback) methods to perform an action on
user interaction. To do this, provide a custom implementation of the
[`ActionCallback`](/reference/kotlin/androidx/glance/appwidget/action/ActionCallback):

```
@Composable
private fun MyContent() {
    // ..
    Image(
        provider = ImageProvider(R.drawable.ic_hourglass_animated),
        modifier = GlanceModifier.clickable(
            onClick = actionRunCallback<RefreshAction>()
        ),
        contentDescription = "Refresh"
    )
}

class RefreshAction : ActionCallback {
    override suspend fun onAction(
        context: Context,
        glanceId: GlanceId,
        parameters: ActionParameters
    ) {
        // TODO implement
    }
}

GlanceSnippets.kt
```

On the user click, the `suspend onAction` method of the provided
`ActionCallback` is called, executing the defined logic (i.e., requesting
refresh data).

To update the widget after the action is performed, create a new instance and
call `update`(..). For more details, see the [Manage GlanceAppWidget state](/develop/ui/compose/glance/glance-app-widget#manage-state)
section.

```
class RefreshAction : ActionCallback {
    override suspend fun onAction(
        context: Context,
        glanceId: GlanceId,
        parameters: ActionParameters
    ) {
        // do some work but offset long-term tasks (e.g a Worker)
        MyAppWidget().update(context, glanceId)
    }
}

GlanceSnippets.kt
```

**Note:** Glance uses a custom async `BroadcastReceiver` to handle the user click
and call the `onRun` method of the provided `ActionCallback`. This
allows extra execution time, but certain restrictions apply. Any long or
consuming tasks should be offset into, for example, a [`Worker`](/topic/libraries/architecture/workmanager).

## Provide parameters to actions

To provide additional information to an action, use the [`ActionParameters`](/reference/kotlin/androidx/glance/action/ActionParameters)
API to create a typed key-value pair. For example, to define the clicked
destination:

```
private val destinationKey = ActionParameters.Key<String>(
    NavigationActivity.KEY_DESTINATION
)

class MyAppWidget : GlanceAppWidget() {

    // ..

    @Composable
    private fun MyContent() {
        // ..
        Button(
            text = "Home",
            onClick = actionStartActivity<NavigationActivity>(
                actionParametersOf(destinationKey to "home")
            )
        )
        Button(
            text = "Work",
            onClick = actionStartActivity<NavigationActivity>(
                actionParametersOf(destinationKey to "work")
            )
        )
    }

    override suspend fun provideGlance(context: Context, id: GlanceId) {
        provideContent { MyContent() }
    }
}

GlanceSnippets.kt
```

Underneath, the parameters are included in the intent used to launch the
activity, allowing the target Activity to retrieve it.

```
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val destination = intent.extras?.getString(KEY_DESTINATION) ?: return
        // ...
    }
}

GlanceSnippets.kt
```

The parameters are also provided to the `ActionCallback`. Use the defined
`Parameters.Key` to retrieve the value:

```
class RefreshAction : ActionCallback {

    private val destinationKey = ActionParameters.Key<String>(
        NavigationActivity.KEY_DESTINATION
    )

    override suspend fun onAction(
        context: Context,
        glanceId: GlanceId,
        parameters: ActionParameters
    ) {
        val destination: String = parameters[destinationKey] ?: return
        // ...
    }
}

GlanceSnippets.kt
```

[Previous

arrow\_back

Unit testing with Glance](/develop/ui/compose/glance/testing)

[Next

Track metrics for your widget

arrow\_forward](/develop/ui/compose/glance/metrics)