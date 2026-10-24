---
title: https://developer.android.com/guide/components/activities/recents
url: https://developer.android.com/guide/components/activities/recents
source: md.txt
---

The Recents screen, also called the Overview screen, recent task
list, or recent apps screen, is a system-level UI that lists recently accessed
[activities](https://developer.android.com/guide/components/activities) and [tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack).
The user can navigate through the list, select a task to
resume, or remove a task from the list by swiping it away.

The Recents screen uses a [document-centric
model](https://developer.android.com/about/versions/lollipop#Documents)---introduced in Android 5.0 (API
level 21)---in which multiple instances of
the same activity containing different documents can appear as tasks in the
Recents screen. For example, Google Drive might have a task for each of
several Google documents. Each document appears as a task in the Recents
screen:
The Recents screen showing two Google Drive documents, each represented as a separate task.

Another common example is when the user is using their browser and they tap
**Share** \> **Gmail** . The Gmail app's **Compose** screen appears. Tapping the
Recents button at that time reveals Chrome and Gmail running as separate
tasks:
The Recents screen showing Chrome and Gmail running as separate tasks.

Normally, you let the system define how your tasks and activities are
represented in the Recents screen. You don't need to modify this
behavior. However, your app can determine how and when activities appear in the
Recents screen.

The
[`ActivityManager.AppTask`](https://developer.android.com/reference/kotlin/android/app/ActivityManager.AppTask)
class lets you manage tasks, and the activity flags of the
[`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent) class let you specify when an
activity is added or removed from the Recents screen. Also, the
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) attributes let you set
the behavior in the manifest.

> [!NOTE]
> **Note:** This guide covers OS-level task management and how your app appears in the system's Recents screen. To manage UI navigation within your Compose app, see [Navigation 3](https://developer.android.com/guide/navigation/navigation-3).

## Add tasks to the Recents screen

Using the flags of the [`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent) class to
add a task gives you greater control over when and how a document gets opened or
reopened in the Recents screen. When you use the
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) attributes, you can
choose between always opening the document in a new task or reusing an existing
task for the document.

### Use the Intent flag to add a task

When you create a new document for your activity, you call the
[`startActivity()`](https://developer.android.com/reference/kotlin/android/content/Context#startactivity)
method, passing to it the intent that launches the activity. To insert a logical
break so that the system treats your activity as a new task in the Recents
screen, pass the
[`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_new_document)
flag in the [`addFlags()`](https://developer.android.com/reference/kotlin/android/content/Intent#addflags)
method of the [`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent) that launches the
activity.

> [!NOTE]
> **Note:** The [`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_new_document) flag replaces the [`FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_clear_when_task_reset) flag, which was deprecated in Android 5.0 (API level 21).

If you set the [`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_multiple_task)
flag when you create the new document, the system always creates a new task with
the target activity as the root. This setting lets the same document be
opened in more than one task. The following code demonstrates how the main
activity does this and starts the new Activity from your composable:

```kotlin
private fun newDocumentIntent(context: Context): Intent =
    Intent(context, NewDocumentActivity::class.java).apply {
        addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT or Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS)
        putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, documentCounter++)
    }

@Composable
fun CreateDocumentButton() {
    val context = LocalContext.current
    Button(
        onClick = {
            val intent = newDocumentIntent(context)
            // Add FLAG_ACTIVITY_MULTIPLE_TASK if needed based on state
            context.startActivity(intent)
        }
    ) {
        Text("Create New Document")
    }
}
```

> [!NOTE]
> **Note:** Activities launched with the `FLAG_ACTIVITY_NEW_DOCUMENT` flag must have the `android:launchMode="standard"` attribute value (the default) set in the manifest.

When the main activity launches a new activity, the system searches through
existing tasks for one whose intent matches the intent component name and the
intent data for the activity. If the task is not found, or the intent contains
the `FLAG_ACTIVITY_MULTIPLE_TASK`
flag, a new task is created with the activity as its root.

If the system finds a task whose intent matches the intent component name and
the intent data, it brings that task to the front and passes the new intent to
[`onNewIntent()`](https://developer.android.com/reference/kotlin/android/app/Activity#onnewintent_1).
The new activity gets the intent and creates a new document in the Recents
screen, as shown in the following example:

```kotlin
class DocumentCentricActivity : ComponentActivity() {
    private var documentState by mutableStateOf(
        DocumentState(
            count = 0,
            textResId = R.string.hello_new_document_counter
        )
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val initialCount = intent.getIntExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, 0)

        documentState = documentState.copy(count = initialCount)

        setContent {
            MaterialTheme {
                DocumentScreen(
                    count = documentState.count,
                    textResId = documentState.textResId
                )
            }
        }
    }

    override fun onNewIntent(newIntent: Intent) {
        super.onNewIntent(newIntent)
        // If FLAG_ACTIVITY_MULTIPLE_TASK has not been used, this Activity is reused.
        documentState = documentState.copy(
            textResId = R.string.reusing_document_counter
        )
    }

    data class DocumentState(val count: Int, @StringRes val textResId: Int)

    companion object {
        const val KEY_EXTRA_NEW_DOCUMENT_COUNTER = "KEY_EXTRA_NEW_DOCUMENT_COUNTER"
    }
}

@Composable
fun DocumentScreen(count: Int, @StringRes textResId: Int) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center
    ) {
        // UI reacts to whichever string resource ID was passed down
        Text(text = stringResource(id = textResId))
        Spacer(modifier = Modifier.height(8.dp))
        Text(text = "Counter: $count")
    }
}
```

In the preceding code, the Activity handles the OS-level routing (`onCreate`
and `onNewIntent`), while the `@Composable` function is responsible only for
rendering the UI based on the provided state.

### Use the activity attribute to add a task

An activity can also specify in its manifest that it always launches into a new
task by using the [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)
attribute [`android:documentLaunchMode`](https://developer.android.com/guide/topics/manifest/activity-element#dlmode).
This attribute has four values, which produce the following effects when the user
opens a document with the application:

`intoExisting`
:   The activity reuses an existing task for the document. This is the same as setting the
    [`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_new_document)
    flag *without* setting the
    [`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_multiple_task)
    flag, as described in the
    [Using the Intent flag to add a task](https://developer.android.com/guide/components/activities/recents#flag-new-doc) section.

`always`
:   The activity creates a new task for the document, even if the document is
    already opened. Using this value is the same as setting both the
    `FLAG_ACTIVITY_NEW_DOCUMENT` and `FLAG_ACTIVITY_MULTIPLE_TASK` flags.

`none`
:   The activity does not create a new task for the document. The Recents
    screen treats the activity as it would by default. It displays a single task
    for the app, which resumes from whatever activity the user last invoked.

`never`
:   The activity does not create a new task for the document. Setting this value
    overrides the behavior of the
    `FLAG_ACTIVITY_NEW_DOCUMENT` and `FLAG_ACTIVITY_MULTIPLE_TASK`
    flags. If either of these are set in the intent, and the Recents screen
    displays a single task for the app, it resumes from whatever activity the
    user last invoked.

> [!NOTE]
> **Note:** For values other than `none` and `never`, the activity must be defined with `launchMode="standard"`. If this attribute is not specified, `documentLaunchMode="none"` is used.

## Remove tasks

By default, a document task automatically exits from the Recents screen
when its activity finishes. You can override this behavior with the
[`ActivityManager.AppTask`](https://developer.android.com/reference/kotlin/android/app/ActivityManager.AppTask)
class, with an [`Intent`](https://developer.android.com/reference/kotlin/android/content/Intent) flag, or with
an [`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) attribute.

You can always exclude a task from the Recents screen entirely by setting
the `<activity>` attribute
[`android:excludeFromRecents`](https://developer.android.com/guide/topics/manifest/activity-element#exclude)
to `true`.

You can set the maximum number of tasks that your app can include in the
Recents screen by setting the
`<activity>` attribute
[`android:maxRecents`](https://developer.android.com/guide/topics/manifest/activity-element#maxrecents) to an
integer value. When the maximum number of tasks is reached,
the least recently used task disappears from the Recents screen. The default is 16,
and the maximum value is 50 (25 on low memory devices). Values less
than 1 are not valid.

### Use the AppTask class to remove tasks

In the activity that creates a new task in the Recents screen, you can
specify when to remove the task and finish all activities associated with it by
calling the
[`finishAndRemoveTask()`](https://developer.android.com/reference/kotlin/android/app/ActivityManager.AppTask#finishandremovetask)
method:

```kotlin
@Composable
fun RemoveTaskButton() {
    val context = LocalContext.current
    Button(
        onClick = {
            // It is good practice to remove a document from the overview stack if not needed anymore.
            (context as? Activity)?.finishAndRemoveTask()
        }
    ) {
        Text("Remove from Recents")
    }
}
```

> [!NOTE]
> **Note:** Using the [`finishAndRemoveTask()`](https://developer.android.com/reference/kotlin/android/app/ActivityManager.AppTask#finishandremovetask) method overrides the use of the [`FLAG_ACTIVITY_RETAIN_IN_RECENTS`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_retain_in_recents) flag discussed in the next section.

### Retain finished tasks

If you want to retain a task in the Recents screen, even if its activity has
finished, pass the
[`FLAG_ACTIVITY_RETAIN_IN_RECENTS`](https://developer.android.com/reference/kotlin/android/content/Intent#flag_activity_retain_in_recents)
flag in the
[`addFlags()`](https://developer.android.com/reference/kotlin/android/content/Intent#addflags) method of the
intent that launches the activity.

```kotlin
private fun newDocumentIntent() =
        Intent(this, NewDocumentActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT or
                    android.content.Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS)
            putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, getAndIncrement())
        }
```

To achieve the same effect, set the
[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element) attribute
[`android:autoRemoveFromRecents`](https://developer.android.com/guide/topics/manifest/activity-element#autoremrecents)
to `false`. The default value is `true` for document activities and `false` for
regular activities. Using this attribute overrides the
`FLAG_ACTIVITY_RETAIN_IN_RECENTS` flag.

## Enable recents URL sharing (Pixel only)

On Pixel devices running Android 12 or higher, users can share links
to recently viewed web content directly from the Recents screen. After visiting
the content in an app, the user can swipe to the Recents screen and find the app
where they viewed the content, then tap the link button to copy or share the
URL.
The Recents screen with a link to share recently viewed web content.

Any app can enable Recents linking for users by providing a web UI and
overriding
[`onProvideAssistContent()`](https://developer.android.com/reference/kotlin/android/app/Activity#onprovideassistcontent),
as shown in the following example:

```kotlin
class MainActivity : ComponentActivity() {

    // Track the current URL as state so the UI can update it during navigation
    private var currentWebUri by mutableStateOf("https://example.com/home")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            AppTheme {
                // Pass a lambda to your Compose UI so it can update the URL state
                // as the user navigates through your app.
                MainScreen(
                    onPageChanged = { newUrl -> currentWebUri = newUrl }
                )
            }
        }
    }

    override fun onProvideAssistContent(outContent: AssistContent) {
        super.onProvideAssistContent(outContent)

        // The system calls this when the user enters the Recents screen.
        // Provide the active URI tracked by the Compose state.
        outContent.webUri = Uri.parse(currentWebUri)
    }
}
```