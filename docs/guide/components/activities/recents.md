---
title: https://developer.android.com/guide/components/activities/recents
url: https://developer.android.com/guide/components/activities/recents
source: md.txt
---

# Recents screen

The Recents screen, also called the Overview screen, recent task list, or recent apps screen, is a system-level UI that lists recently accessed[activities](https://developer.android.com/guide/components/activities)and[tasks](https://developer.android.com/guide/components/activities/tasks-and-back-stack). The user can navigate through the list, select a task to resume, or remove a task from the list by swiping it away.

The Recents screen uses a[document-centric model](https://developer.android.com/about/versions/lollipop#Documents)---introduced in Android 5.0 (API level 21)---in which multiple instances of the same activity containing different documents can appear as tasks in the Recents screen. For example, Google Drive might have a task for each of several Google documents. Each document appears as a task in the Recents screen:
The Recents screen showing two Google Drive documents, each represented as a separate task.

Another common example is when the user is using their browser and they tap**Share** \>**Gmail** . The Gmail app's**Compose**screen appears. Tapping the Recents button at that time reveals Chrome and Gmail running as separate tasks:
The Recents screen showing Chrome and Gmail running as separate tasks.

Normally, you let the system define how your tasks and activities are represented in the Recents screen. You don't need to modify this behavior. However, your app can determine how and when activities appear in the Recents screen.

The[`ActivityManager.AppTask`](https://developer.android.com/reference/android/app/ActivityManager.AppTask)class lets you manage tasks, and the activity flags of the[`Intent`](https://developer.android.com/reference/android/content/Intent)class let you specify when an activity is added or removed from the Recents screen. Also, the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)attributes let you set the behavior in the manifest.

## Add tasks to the Recents screen

Using the flags of the[`Intent`](https://developer.android.com/reference/android/content/Intent)class to add a task gives you greater control over when and how a document gets opened or reopened in the Recents screen. When you use the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)attributes, you can choose between always opening the document in a new task or reusing an existing task for the document.

### Use the Intent flag to add a task

When you create a new document for your activity, you call the[`startActivity()`](https://developer.android.com/reference/android/content/Context#startActivity(android.content.Intent))method, passing to it the intent that launches the activity. To insert a logical break so that the system treats your activity as a new task in the Recents screen, pass the[`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_DOCUMENT)flag in the[`addFlags()`](https://developer.android.com/reference/android/content/Intent#addFlags(int))method of the[`Intent`](https://developer.android.com/reference/android/content/Intent)that launches the activity.
| **Note:** The[`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_DOCUMENT)flag replaces the[`FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET)flag, which was deprecated in Android 5.0 (API level 21).

If you set the[`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_MULTIPLE_TASK)flag when you create the new document, the system always creates a new task with the target activity as the root. This setting lets the same document be opened in more than one task. The following code demonstrates how the main activity does this:  

### Kotlin

```kotlin
fun createNewDocument(view: View) {
    val newDocumentIntent = newDocumentIntent()
    if (useMultipleTasks) {
        newDocumentIntent.addFlags(Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
    }
    startActivity(newDocumentIntent)
}

private fun newDocumentIntent(): Intent =
        Intent(this, NewDocumentActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT or
                    android.content.Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS)
            putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, documentCounter++)
        }
```

### Java

```java
public void createNewDocument(View view) {
      final Intent newDocumentIntent = newDocumentIntent();
      if (useMultipleTasks) {
          newDocumentIntent.addFlags(Intent.FLAG_ACTIVITY_MULTIPLE_TASK);
      }
      startActivity(newDocumentIntent);
  }

  private Intent newDocumentIntent() {
      boolean useMultipleTasks = checkbox.isChecked();
      final Intent newDocumentIntent = new Intent(this, NewDocumentActivity.class);
      newDocumentIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT);
      newDocumentIntent.putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, documentCounter++);
      return newDocumentIntent;
  }

}
```
| **Note:** Activities launched with the`FLAG_ACTIVITY_NEW_DOCUMENT`flag must have the`android:launchMode="standard"`attribute value (the default) set in the manifest.

When the main activity launches a new activity, the system searches through existing tasks for one whose intent matches the intent component name and the intent data for the activity. If the task is not found, or the intent contained the`FLAG_ACTIVITY_MULTIPLE_TASK`flag, a new task is created with the activity as its root.

If the system finds a task whose intent matches the intent component name and the intent data, it brings that task to the front and passes the new intent to[`onNewIntent()`](https://developer.android.com/reference/android/app/Activity#onNewIntent(android.content.Intent)). The new activity gets the intent and creates a new document in the Recents screen, as shown in the following example:  

### Kotlin

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_new_document)
    documentCount = intent
            .getIntExtra(DocumentCentricActivity.KEY_EXTRA_NEW_DOCUMENT_COUNTER, 0)
    documentCounterTextView = findViewById(R.id.hello_new_document_text_view)
    setDocumentCounterText(R.string.hello_new_document_counter)
}

override fun onNewIntent(newIntent: Intent) {
    super.onNewIntent(newIntent)
    /* If FLAG_ACTIVITY_MULTIPLE_TASK has not been used, this Activity
    will be reused. */
    setDocumentCounterText(R.string.reusing_document_counter)
}
```

### Java

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_new_document);
    documentCount = getIntent()
            .getIntExtra(DocumentCentricActivity.KEY_EXTRA_NEW_DOCUMENT_COUNTER, 0);
    documentCounterTextView = (TextView) findViewById(
            R.id.hello_new_document_text_view);
    setDocumentCounterText(R.string.hello_new_document_counter);
}

@Override
protected void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    /* If FLAG_ACTIVITY_MULTIPLE_TASK has not been used, this activity
    is reused to create a new document.
     */
    setDocumentCounterText(R.string.reusing_document_counter);
}
```

### Use the activity attribute to add a task

An activity can also specify in its manifest that it always launches into a new task by using the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)attribute[`android:documentLaunchMode`](https://developer.android.com/guide/topics/manifest/activity-element#dlmode). This attribute has four values, which produce the following effects when the user opens a document with the application:

`intoExisting`
:   The activity reuses an existing task for the document. This is the same as setting the[`FLAG_ACTIVITY_NEW_DOCUMENT`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_NEW_DOCUMENT)flag*without* setting the[`FLAG_ACTIVITY_MULTIPLE_TASK`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_MULTIPLE_TASK)flag, as described in the[Using the Intent flag to add a task](https://developer.android.com/guide/components/activities/recents#flag-new-doc)section.

`always`
:   The activity creates a new task for the document, even if the document is already opened. Using this value is the same as setting both the`FLAG_ACTIVITY_NEW_DOCUMENT`and`FLAG_ACTIVITY_MULTIPLE_TASK`flags.

`none`
:   The activity does not create a new task for the document. The Recents screen treats the activity as it would by default. It displays a single task for the app, which resumes from whatever activity the user last invoked.

`never`
:   The activity does not create a new task for the document. Setting this value overrides the behavior of the`FLAG_ACTIVITY_NEW_DOCUMENT`and`FLAG_ACTIVITY_MULTIPLE_TASK`flags. If either of these are set in the intent, and the Recents screen displays a single task for the app, it resumes from whatever activity the user last invoked.
| **Note:** For values other than`none`and`never`, the activity must be defined with`launchMode="standard"`. If this attribute is not specified,`documentLaunchMode="none"`is used.

## Remove tasks

By default, a document task automatically exits from the Recents screen when its activity finishes. You can override this behavior with the[`ActivityManager.AppTask`](https://developer.android.com/reference/android/app/ActivityManager.AppTask)class, with an[`Intent`](https://developer.android.com/reference/android/content/Intent)flag, or with an[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)attribute.

You can always exclude a task from the Recents screen entirely by setting the`<activity>`attribute[`android:excludeFromRecents`](https://developer.android.com/guide/topics/manifest/activity-element#exclude)to`true`.

You can set the maximum number of tasks that your app can include in the Recents screen by setting the`<activity>`attribute[`android:maxRecents`](https://developer.android.com/guide/topics/manifest/activity-element#maxrecents)to an integer value. When the maximum number of tasks is reached, the least recently used task disappears from the Recents screen. The default is 16, and the maximum value is 50 (25 on low memory devices). Values less than 1 are not valid.

### Use the AppTask class to remove tasks

In the activity that creates a new task in the Recents screen, you can specify when to remove the task and finish all activities associated with it by calling the[`finishAndRemoveTask()`](https://developer.android.com/reference/android/app/ActivityManager.AppTask#finishAndRemoveTask())method:  

### Kotlin

```kotlin
fun onRemoveFromOverview(view: View) {
    // It is good pratice to remove a document from the overview stack if not needed anymore.
    finishAndRemoveTask()
}
```

### Java

```java
public void onRemoveFromRecents(View view) {
    // The document is no longer needed; remove its task.
    finishAndRemoveTask();
}
```
| **Note:** Using the[`finishAndRemoveTask()`](https://developer.android.com/reference/android/app/ActivityManager.AppTask#finishAndRemoveTask())method overrides the use of the[`FLAG_ACTIVITY_RETAIN_IN_RECENTS`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_RETAIN_IN_RECENTS)flag discussed in the next section.

### Retain finished tasks

If you want to retain a task in the Recents screen, even if its activity has finished, pass the[`FLAG_ACTIVITY_RETAIN_IN_RECENTS`](https://developer.android.com/reference/android/content/Intent#FLAG_ACTIVITY_RETAIN_IN_RECENTS)flag in the[`addFlags()`](https://developer.android.com/reference/android/content/Intent#addFlags(int))method of the intent that launches the activity.  

### Kotlin

```kotlin
private fun newDocumentIntent() =
        Intent(this, NewDocumentActivity::class.java).apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT or
                    android.content.Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS)
            putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, getAndIncrement())
        }
```

### Java

```java
private Intent newDocumentIntent() {
    final Intent newDocumentIntent = new Intent(this, NewDocumentActivity.class);
    newDocumentIntent.addFlags(Intent.FLAG_ACTIVITY_NEW_DOCUMENT |
      android.content.Intent.FLAG_ACTIVITY_RETAIN_IN_RECENTS);
    newDocumentIntent.putExtra(KEY_EXTRA_NEW_DOCUMENT_COUNTER, getAndIncrement());
    return newDocumentIntent;
}
```

To achieve the same effect, set the[`<activity>`](https://developer.android.com/guide/topics/manifest/activity-element)attribute[`android:autoRemoveFromRecents`](https://developer.android.com/guide/topics/manifest/activity-element#autoremrecents)to`false`. The default value is`true`for document activities and`false`for regular activities. Using this attribute overrides the`FLAG_ACTIVITY_RETAIN_IN_RECENTS`flag.

## Enable recents URL sharing (Pixel only)

On Pixel devices running Android 12 or higher, users can share links to recently viewed web content directly from the Recents screen. After visiting the content in an app, the user can swipe to the Recents screen and find the app where they viewed the content, then tap the link button to copy or share the URL.
The Recents screen with a link to share recently viewed web content.

Any app can enable Recents linking for users by providing a web UI and overriding[`onProvideAssistContent()`](https://developer.android.com/reference/android/app/Activity#onProvideAssistContent(android.app.assist.AssistContent)), as shown in the following example:  

### Kotlin

```kotlin
class MainActivity : AppCompatActivity() {
    protected fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onProvideAssistContent(outContent: AssistContent) {
        super.onProvideAssistContent(outContent)
        outContent.setWebUri(Uri.parse("https://example.com/myCurrentPage"))
    }
}
```

### Java

```java
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public void onProvideAssistContent(AssistContent outContent) {
        super.onProvideAssistContent(outContent);

        outContent.setWebUri(Uri.parse("https://example.com/myCurrentPage"));
    }
}
```