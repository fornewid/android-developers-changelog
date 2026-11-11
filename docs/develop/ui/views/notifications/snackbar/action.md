---
title: https://developer.android.com/develop/ui/views/notifications/snackbar/action
url: https://developer.android.com/develop/ui/views/notifications/snackbar/action
source: md.txt
---

Try the Compose way Jetpack Compose is the recommended UI toolkit for Android. Learn how to add notifications in Compose. [Snackbar →](https://developer.android.com/develop/ui/compose/components/snackbar.md.txt) ![](https://developer.android.com/static/images/android-compose-ui-logo.png)

You can add an action to a
`Snackbar`
to let the user respond to your message. When you do this, the
`Snackbar` puts a button next to the message text, and the user can
trigger your action by tapping the button. For example, an email app might put
an *undo* button on its "email archived" message. If the user taps the
*undo* button, the app takes the email back out of the archive.
![Snackbar notification with an UNDO action button](https://developer.android.com/static/images/ui/notifications/action_snackbar_undo.png) **Figure 1.** A `Snackbar` with an undo action button that restores a removed item.

To add an action to a `Snackbar` message, define a listener object
that implements the
`View.OnClickListener`
interface. The system calls your listener's
`onClick()`
method if the user taps the message action. For example, this snippet shows a
listener for an undo action:

```kotlin
class MyUndoListener : View.OnClickListener {

    override fun onClick(v: View) {
        // Code to undo the user's last action.
    }
}
```

Use one of the
`setAction()`
methods to attach the listener to your `Snackbar`. Attach the
listener before you call
`show()`,
as shown in this code sample:

```kotlin
val mySnackbar = Snackbar.make(
    findViewById(R.id.myCoordinatorLayout),
    R.string.email_archived,
    Snackbar.LENGTH_SHORT
)
mySnackbar.setAction(R.string.undo_string, MyUndoListener())
mySnackbar.show()
```
If you are using [Jetpack Compose](https://developer.android.com/jetpack/compose), you can show a `SnackbarHost`, as shown in the following example:

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {

    super.onCreate(savedInstanceState)

    setContent {
        DACPlaygroundTheme {
            val snackbarHostState = remember { SnackbarHostState() }
            val scope = rememberCoroutineScope()
            Scaffold(
                snackbarHost = { SnackbarHost(snackbarHostState) },
                content = { padding ->
                    Button(
                        modifier = Modifier.padding(padding),
                        onClick = {
                            scope.launch {
                                snackbarHostState.showSnackbar(
                                    message = "1 item removed",
                                    actionLabel = "UNDO",
                                    duration = SnackbarDuration.Short
                                ).run {
                                    when (this) {
                                        Dismissed -> Log.d("SNACKBAR", "Dismissed")
                                        ActionPerformed -> Log.d("SNACKBAR", "UNDO CLICKED")
                                    }
                                }
                            }
                        }
                    ) { Text("Show snackbar") }
                }
            )
        }
    }
}
```

> [!NOTE]
> **Note:** A `Snackbar` automatically goes away after a short time, so the user might not see the message or have a chance to tap the button. For this reason, offer other ways to perform `Snackbar` actions.